"""Deterministic C11 review boundary; no model, provider, export, or storage action.

The caller is responsible for obtaining an explicit human decision through a
trusted channel. A reviewer_id is an asserted reference, not authentication.
"""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, model_validator

from ai_quotation_intelligence.calculation import calculate_quote_total
from ai_quotation_intelligence.domain import (
    AgentResult,
    AgentResultStatus,
    ApprovalDecision,
    ApprovalStatus,
    DraftQuote,
    Quote,
    QuoteStatus,
)


class ReviewFailureCode(StrEnum):
    INVALID_RESULT = "invalid_result"
    NOT_REVIEWABLE = "not_reviewable"
    INVALID_DECISION = "invalid_decision"
    INVALID_TRANSITION = "invalid_transition"
    STALE_DRAFT = "stale_draft"
    APPROVAL_REQUIRED = "approval_required"


class ReviewFailure(Exception):
    """A bounded failure that never includes untrusted input or exception text."""

    def __init__(self, code: ReviewFailureCode) -> None:
        self.code = code
        super().__init__(code.value)


def _validated_result(value: object) -> AgentResult:
    if type(value) is not AgentResult:
        raise ReviewFailure(ReviewFailureCode.INVALID_RESULT)
    try:
        result = AgentResult.model_validate_json(value.model_dump_json())
    except Exception:
        raise ReviewFailure(ReviewFailureCode.INVALID_RESULT) from None

    draft = result.draft_quote
    if result.status is not AgentResultStatus.SUCCESS or draft is None:
        raise ReviewFailure(ReviewFailureCode.NOT_REVIEWABLE)
    quote = draft.quote
    if (draft.status is not QuoteStatus.DRAFT
            or quote.status is not QuoteStatus.DRAFT
            or quote.quote_id != f"draft-{result.request_id}"
            or quote.estimated_total_cost is None
            or not result.evidence_ids
            or len(result.evidence_ids) != len(set(result.evidence_ids))
            or result.evidence_ids != draft.evidence_ids
            or result.risk_suggestions != draft.risk_suggestions
            or len({item.suggestion_id for item in result.risk_suggestions})
               != len(result.risk_suggestions)
            or any(len(suggestion.evidence_ids) != len(set(suggestion.evidence_ids))
                   or not set(suggestion.evidence_ids) <= set(result.evidence_ids)
                   for suggestion in result.risk_suggestions)):
        raise ReviewFailure(ReviewFailureCode.NOT_REVIEWABLE)
    try:
        if calculate_quote_total(quote) != quote.estimated_total_cost:
            raise ReviewFailure(ReviewFailureCode.NOT_REVIEWABLE)
    except Exception:
        raise ReviewFailure(ReviewFailureCode.NOT_REVIEWABLE) from None
    return result


class ReviewRecord(BaseModel):
    """Inspectible decision and exact reviewed draft, without export authority."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    request_id: str
    reviewed_draft: DraftQuote
    quote: Quote
    decision: ApprovalDecision
    evidence_ids: tuple[str, ...]

    @model_validator(mode="after")
    def decision_matches_reviewed_draft(self) -> "ReviewRecord":
        status = {
            ApprovalStatus.APPROVED: QuoteStatus.APPROVED,
            ApprovalStatus.REJECTED: QuoteStatus.REJECTED,
        }.get(self.decision.status)
        if (status is None or self.quote.status is not status
                or self.quote.quote_id != f"draft-{self.request_id}"
                or self.decision.quote_id != self.quote.quote_id
                or self.quote.model_copy(update={"status": QuoteStatus.DRAFT}) != self.reviewed_draft.quote
                or tuple(self.reviewed_draft.evidence_ids) != self.evidence_ids
                or self.reviewed_draft.status is not QuoteStatus.DRAFT):
            raise ValueError("review record does not match reviewed draft and decision")
        return self

class ReviewSession:
    """One in-memory decision over a validated, exact C10 result snapshot."""

    def __init__(self, source: AgentResult) -> None:
        self._snapshot = _validated_result(source).model_dump_json()
        self._state = QuoteStatus.AWAITING_REVIEW
        self._record: ReviewRecord | None = None

    @property
    def state(self) -> QuoteStatus:
        return self._state

    def _match_current(self, current: object) -> None:
        try:
            clean = _validated_result(current)
        except ReviewFailure:
            raise ReviewFailure(ReviewFailureCode.STALE_DRAFT) from None
        if clean.model_dump_json() != self._snapshot:
            raise ReviewFailure(ReviewFailureCode.STALE_DRAFT)

    def decide(self, decision: object, *, current: object) -> ReviewRecord:
        """Accept one explicit human action; do not infer it from model text."""
        if self._state is not QuoteStatus.AWAITING_REVIEW:
            raise ReviewFailure(ReviewFailureCode.INVALID_TRANSITION)
        self._match_current(current)
        if type(decision) is not ApprovalDecision:
            raise ReviewFailure(ReviewFailureCode.INVALID_DECISION)
        try:
            clean = ApprovalDecision.model_validate_json(decision.model_dump_json())
        except Exception:
            raise ReviewFailure(ReviewFailureCode.INVALID_DECISION) from None
        source = AgentResult.model_validate_json(self._snapshot)
        if (clean.status not in {ApprovalStatus.APPROVED, ApprovalStatus.REJECTED}
                or clean.quote_id != source.draft_quote.quote.quote_id):
            raise ReviewFailure(ReviewFailureCode.INVALID_DECISION)

        state = (QuoteStatus.APPROVED if clean.status is ApprovalStatus.APPROVED
                 else QuoteStatus.REJECTED)
        draft = source.draft_quote
        try:
            quote_data = draft.quote.model_dump()
            quote_data["status"] = state
            record = ReviewRecord(
                request_id=source.request_id,
                reviewed_draft=draft.model_copy(deep=True),
                quote=Quote.model_validate(quote_data),
                decision=clean,
                evidence_ids=tuple(source.evidence_ids),
            )
        except Exception:
            raise ReviewFailure(ReviewFailureCode.INVALID_RESULT) from None
        self._record = record
        self._state = state
        return record.model_copy(deep=True)

    def require_approved(self, *, current: object) -> ReviewRecord:
        """Only eligibility gate; C12 owns any eventual final artifact."""
        if self._state is not QuoteStatus.APPROVED or self._record is None:
            raise ReviewFailure(ReviewFailureCode.APPROVAL_REQUIRED)
        self._match_current(current)
        return self._record.model_copy(deep=True)


__all__ = ["ReviewFailure", "ReviewFailureCode", "ReviewRecord", "ReviewSession"]
