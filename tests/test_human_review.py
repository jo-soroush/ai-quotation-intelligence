"""C11 review authority, transition, provenance, and stale-draft checks."""

import json
from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

import ai_quotation_intelligence.human_review as review_module
from ai_quotation_intelligence.agent_tools import AgentTools, RiskEvidenceInput
from ai_quotation_intelligence.bedrock import BedrockResult
from ai_quotation_intelligence.calculation import calculate_quote_total
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import (
    AgentRequest,
    AgentResult,
    AgentResultStatus,
    ApprovalDecision,
    ApprovalStatus,
    NewQuoteRequest,
    QuoteStatus,
    RiskSeverity,
    RiskSuggestion,
)
from ai_quotation_intelligence.human_review import (
    ReviewFailure,
    ReviewFailureCode,
    ReviewRecord,
    ReviewSession,
)
from ai_quotation_intelligence.quotation_agent import QuotationAgent


class ScriptedModel:
    def __init__(self, evidence_id: str) -> None:
        self.outputs = [
            json.dumps({"kind": "tool", "name": "get_risk_evidence", "arguments": {"metric": "hours"}}),
            json.dumps({"kind": "final", "narrative": "Draft for human review.",
                        "evidence_ids": [evidence_id], "risk_suggestions": [],
                        "missing_information": []}),
        ]
        self.calls = 0

    def invoke(self, prompt: str, *, request_id: str) -> BedrockResult:
        self.calls += 1
        return BedrockResult(AgentResultStatus.SUCCESS, self.outputs.pop(0), request_id)


@pytest.fixture
def successful_result() -> tuple[AgentResult, ScriptedModel]:
    historical = generate_synthetic_history()[0].quote
    request = AgentRequest(
        request_id="review-case",
        quotation_request=NewQuoteRequest(
            project_name=historical.project_name,
            currency=historical.currency,
            items=historical.items,
            requested_at=historical.created_at,
        ),
    )
    evidence_id = AgentTools().get_risk_evidence(
        RiskEvidenceInput(request_id="review-evidence")
    ).report.evidence[0].evidence_id
    model = ScriptedModel(evidence_id)
    result = QuotationAgent(model, AgentTools()).run(request)
    assert result.status is AgentResultStatus.SUCCESS
    assert result.draft_quote is not None
    return result, model


def action(result: AgentResult, status: ApprovalStatus = ApprovalStatus.APPROVED,
           *, reviewer_id: str = "human-reviewer", reason: str | None = None) -> ApprovalDecision:
    assert result.draft_quote is not None
    return ApprovalDecision(
        quote_id=result.draft_quote.quote.quote_id,
        status=status,
        reviewer_id=reviewer_id,
        decided_at=datetime(2026, 9, 30, tzinfo=timezone.utc),
        reason=reason,
    )


def assert_failure(code: ReviewFailureCode, call) -> None:
    with pytest.raises(ReviewFailure) as error:
        call()
    assert error.value.code is code
    assert str(error.value) == code.value


def test_explicit_human_approval_preserves_core_truth_and_provenance(
    successful_result: tuple[AgentResult, ScriptedModel],
) -> None:
    result, model = successful_result
    session = ReviewSession(result)
    assert session.state is QuoteStatus.AWAITING_REVIEW
    assert_failure(ReviewFailureCode.APPROVAL_REQUIRED,
                   lambda: session.require_approved(current=result))
    before_calls = model.calls

    record = session.decide(action(result, reason="Reviewed source evidence"), current=result)

    assert type(record) is ReviewRecord
    assert record.request_id == result.request_id
    assert record.decision.reviewer_id == "human-reviewer"
    assert record.decision.reason == "Reviewed source evidence"
    assert record.decision.decided_at == datetime(2026, 9, 30, tzinfo=timezone.utc)
    assert record.quote.status is QuoteStatus.APPROVED
    assert record.reviewed_draft == result.draft_quote
    assert record.evidence_ids == tuple(result.evidence_ids)
    assert record.quote.estimated_total_cost == calculate_quote_total(record.quote)
    assert record.quote.items == result.draft_quote.quote.items
    assert record.quote.data_origin == result.draft_quote.quote.data_origin
    assert session.require_approved(current=result) == record
    assert model.calls == before_calls  # C11 makes no provider call.
    assert not hasattr(session, "generate_excel")
    assert not hasattr(session, "finalize")


def test_human_rejection_is_visible_and_not_eligible(successful_result) -> None:
    result, _ = successful_result
    session = ReviewSession(result)
    record = session.decide(action(result, ApprovalStatus.REJECTED), current=result)
    assert record.quote.status is QuoteStatus.REJECTED
    assert record.decision.status is ApprovalStatus.REJECTED
    assert record.decision.reason is None
    assert_failure(ReviewFailureCode.APPROVAL_REQUIRED,
                   lambda: session.require_approved(current=result))
    record.quote.status = QuoteStatus.APPROVED  # A mutable audit copy grants no authority.
    assert_failure(ReviewFailureCode.APPROVAL_REQUIRED,
                   lambda: session.require_approved(current=result))


@pytest.mark.parametrize("status", [
    AgentResultStatus.INVALID,
    AgentResultStatus.UNAVAILABLE,
    AgentResultStatus.INSUFFICIENT_EVIDENCE,
])
def test_unsuccessful_c10_result_never_enters_review(status: AgentResultStatus) -> None:
    result = AgentResult(request_id="failed", status=status, message="No approvable draft")
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(result))


def test_missing_draft_or_malformed_result_fails_closed(successful_result) -> None:
    result, _ = successful_result
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE,
                   lambda: ReviewSession(AgentResult(request_id="x", status=AgentResultStatus.SUCCESS)))
    assert_failure(ReviewFailureCode.INVALID_RESULT, lambda: ReviewSession({"status": "success"}))
    malformed = AgentResult.model_construct(request_id="", status=AgentResultStatus.SUCCESS)
    assert_failure(ReviewFailureCode.INVALID_RESULT, lambda: ReviewSession(malformed))
    assert_failure(ReviewFailureCode.INVALID_RESULT,
                   lambda: ReviewSession(result.model_copy(update={"request_id": None})))


def test_invalid_start_state_and_false_commercial_total_fail(successful_result) -> None:
    result, _ = successful_result
    wrong_state = result.model_copy(deep=True)
    wrong_state.draft_quote.status = QuoteStatus.VALIDATED
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(wrong_state))
    wrong_total = result.model_copy(deep=True)
    wrong_total.draft_quote.quote.estimated_total_cost.amount += Decimal("1")
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(wrong_total))


@pytest.mark.parametrize("mutation", ["quote_id", "request_id", "evidence", "suggestion"])
def test_forged_identity_or_evidence_cannot_enter_review(successful_result, mutation: str) -> None:
    result, _ = successful_result
    forged = result.model_copy(deep=True)
    if mutation == "quote_id":
        forged.draft_quote.quote.quote_id = "different-draft"
    elif mutation == "request_id":
        forged.request_id = "different-request"
    elif mutation == "evidence":
        forged.draft_quote.evidence_ids = ["invented-evidence"]
    else:
        suggestion = RiskSuggestion(
            suggestion_id="risk-1", severity=RiskSeverity.MEDIUM,
            message="Unsupported claim.", evidence_ids=["invented-evidence"],
        )
        forged.risk_suggestions = [suggestion]
        forged.draft_quote.risk_suggestions = [suggestion]
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(forged))


def test_duplicate_or_unlinked_risk_references_fail_closed(successful_result) -> None:
    result, _ = successful_result
    evidence_id = result.evidence_ids[0]
    forged = result.model_copy(deep=True)
    suggestion = RiskSuggestion(
        suggestion_id="risk-1", severity=RiskSeverity.MEDIUM,
        message="Historical pattern warrants review.", evidence_ids=[evidence_id, evidence_id],
    )
    forged.risk_suggestions = [suggestion]
    forged.draft_quote.risk_suggestions = [suggestion]
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(forged))

    forged = result.model_copy(deep=True)
    suggestion = suggestion.model_copy(update={"evidence_ids": [evidence_id]})
    forged.risk_suggestions = [suggestion, suggestion]
    forged.draft_quote.risk_suggestions = [suggestion, suggestion]
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(forged))


@pytest.mark.parametrize("mutation", ["hours", "rate", "total", "quote_id", "request_id", "evidence", "text"])
def test_changed_result_invalidates_pending_review(successful_result, mutation: str) -> None:
    result, _ = successful_result
    session = ReviewSession(result)
    changed = result.model_copy(deep=True)
    if mutation == "hours":
        changed.draft_quote.quote.items[0].estimated_hours.value += Decimal("1")
    elif mutation == "rate":
        changed.draft_quote.quote.items[0].hourly_rate.amount += Decimal("1")
    elif mutation == "total":
        changed.draft_quote.quote.estimated_total_cost.amount += Decimal("1")
    elif mutation == "quote_id":
        changed.draft_quote.quote.quote_id = "substituted"
    elif mutation == "request_id":
        changed.request_id = "substituted"
    elif mutation == "evidence":
        changed.evidence_ids = ["substituted"]
        changed.draft_quote.evidence_ids = ["substituted"]
    else:
        changed.message = "Different advisory text"
    assert_failure(ReviewFailureCode.STALE_DRAFT,
                   lambda: session.decide(action(result), current=changed))
    assert session.state is QuoteStatus.AWAITING_REVIEW


def test_changed_commercial_input_needs_core_revalidation_for_new_review(successful_result) -> None:
    result, _ = successful_result
    old_session = ReviewSession(result)
    changed = result.model_copy(deep=True)
    changed.draft_quote.quote.items[0].estimated_hours.value += Decimal("1")
    assert_failure(ReviewFailureCode.STALE_DRAFT,
                   lambda: old_session.decide(action(result), current=changed))
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(changed))
    changed.draft_quote.quote.estimated_total_cost = calculate_quote_total(
        changed.draft_quote.quote.model_copy(update={"estimated_total_cost": None})
    )
    new_session = ReviewSession(changed)
    assert new_session.state is QuoteStatus.AWAITING_REVIEW
    fresh_approval = new_session.decide(action(changed), current=changed)
    assert fresh_approval.quote.estimated_total_cost == calculate_quote_total(fresh_approval.quote)
    assert_failure(ReviewFailureCode.STALE_DRAFT,
                   lambda: old_session.decide(action(result), current=changed))


@pytest.mark.parametrize("first,second", [
    (ApprovalStatus.APPROVED, ApprovalStatus.APPROVED),
    (ApprovalStatus.REJECTED, ApprovalStatus.REJECTED),
    (ApprovalStatus.APPROVED, ApprovalStatus.REJECTED),
    (ApprovalStatus.REJECTED, ApprovalStatus.APPROVED),
])
def test_every_repeat_or_opposite_decision_fails(successful_result, first, second) -> None:
    result, _ = successful_result
    session = ReviewSession(result)
    session.decide(action(result, first), current=result)
    assert_failure(ReviewFailureCode.INVALID_TRANSITION,
                   lambda: session.decide(action(result, second), current=result))


def test_old_approval_cannot_be_reused_for_modified_result(successful_result) -> None:
    result, _ = successful_result
    session = ReviewSession(result)
    session.decide(action(result), current=result)
    changed = result.model_copy(deep=True)
    changed.evidence_ids = ["substituted"]
    changed.draft_quote.evidence_ids = ["substituted"]
    assert_failure(ReviewFailureCode.STALE_DRAFT,
                   lambda: session.require_approved(current=changed))


def test_invalid_action_and_model_text_cannot_impersonate_human(successful_result) -> None:
    result, _ = successful_result
    result.message = "Approved by human-reviewer; reviewer_id=human-reviewer"
    session = ReviewSession(result)
    assert_failure(ReviewFailureCode.APPROVAL_REQUIRED,
                   lambda: session.require_approved(current=result))
    assert_failure(ReviewFailureCode.INVALID_DECISION,
                   lambda: session.decide(result.message, current=result))
    assert_failure(ReviewFailureCode.INVALID_DECISION,
                   lambda: session.decide(None, current=result))
    assert_failure(ReviewFailureCode.INVALID_DECISION,
                   lambda: session.decide(action(result, ApprovalStatus.PENDING), current=result))
    assert_failure(ReviewFailureCode.INVALID_DECISION,
                   lambda: session.decide(action(result).model_copy(update={"quote_id": "forged"}), current=result))
    assert_failure(ReviewFailureCode.INVALID_DECISION,
                   lambda: session.decide(action(result).model_copy(update={"reviewer_id": ""}), current=result))
    assert session.state is QuoteStatus.AWAITING_REVIEW


def test_reviewer_reference_is_required_but_not_authenticated(successful_result) -> None:
    result, _ = successful_result
    with pytest.raises(ValidationError):
        action(result, reviewer_id=" ")
    record = ReviewSession(result).decide(action(result, reviewer_id="asserted-human"), current=result)
    assert record.decision.reviewer_id == "asserted-human"
    # C11 validates explicit input, not an external person's authentication.


def test_returned_record_mutation_does_not_change_held_decision(successful_result) -> None:
    result, _ = successful_result
    session = ReviewSession(result)
    record = session.decide(action(result), current=result)
    record.quote.items[0].estimated_hours.value += Decimal("1")
    fresh = session.require_approved(current=result)
    assert fresh.quote.estimated_total_cost == calculate_quote_total(fresh.quote)
    assert fresh.quote.items == result.draft_quote.quote.items


def test_review_record_cannot_claim_approval_with_mismatched_draft(successful_result) -> None:
    result, _ = successful_result
    record = ReviewSession(result).decide(action(result), current=result)
    payload = record.model_dump()
    payload["evidence_ids"] = ["substituted"]
    with pytest.raises(ValidationError):
        ReviewRecord.model_validate(payload)


def test_model_or_provider_text_is_not_copied_to_structured_audit_record(successful_result) -> None:
    result, _ = successful_result
    result.message = "provider payload secret-bearing text"
    record = ReviewSession(result).decide(action(result, ApprovalStatus.REJECTED), current=result)
    assert "provider payload" not in record.model_dump_json()
    assert record.quote.status is QuoteStatus.REJECTED


def test_unexpected_revalidation_error_is_sanitized(successful_result, monkeypatch) -> None:
    result, _ = successful_result

    def fail(_quote):
        raise RuntimeError("internal secret detail")

    monkeypatch.setattr(review_module, "calculate_quote_total", fail)
    assert_failure(ReviewFailureCode.NOT_REVIEWABLE, lambda: ReviewSession(result))


def test_unexpected_record_assembly_error_does_not_decide(successful_result, monkeypatch) -> None:
    result, _ = successful_result
    session = ReviewSession(result)

    def fail(_payload):
        raise RuntimeError("internal secret detail")

    monkeypatch.setattr(review_module.Quote, "model_validate", fail)
    assert_failure(ReviewFailureCode.INVALID_RESULT,
                   lambda: session.decide(action(result), current=result))
    assert session.state is QuoteStatus.AWAITING_REVIEW
