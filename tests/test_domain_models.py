from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from ai_quotation_intelligence.domain import (
    AgentRequest,
    AgentResult,
    AgentResultStatus,
    DataOrigin,
    DraftQuote,
    HistoricalQuote,
    Hours,
    Money,
    NewQuoteRequest,
    Quote,
    QuoteItem,
    QuoteStatus,
    RiskEvidence,
    RiskSeverity,
    RiskSuggestion,
    TimeUnit,
)
from ai_quotation_intelligence.domain.models import (
    HistoricalComparisonEvidence,
    RiskEvidenceSummary,
)


NOW = datetime(2026, 9, 14, tzinfo=timezone.utc)


def item() -> QuoteItem:
    return QuoteItem(
        item_id="item-1",
        description="Analysis",
        estimated_hours=Hours(value=Decimal("8")),
        hourly_rate=Money(amount=Decimal("100"), currency="SEK"),
    )


def quote() -> Quote:
    return Quote(
        quote_id="quote-1",
        project_name="Example project",
        currency="SEK",
        items=[item()],
        created_at=NOW,
        data_origin=DataOrigin.SYNTHETIC,
    )


def test_valid_nested_models_and_defaults() -> None:
    request = NewQuoteRequest(
        project_name="Example project",
        currency="SEK",
        items=[item()],
        requested_at=NOW,
    )

    assert request.currency == "SEK"
    assert request.items[0].estimated_hours.unit is TimeUnit.HOURS
    assert quote().status is QuoteStatus.DRAFT


@pytest.mark.parametrize(
    "payload",
    [
        {"amount": Decimal("-1"), "currency": "SEK"},
        {"amount": Decimal("10"), "currency": "SWEDISH"},
    ],
)
def test_money_rejects_invalid_values(payload: dict) -> None:
    with pytest.raises(ValidationError):
        Money(**payload)


def test_required_fields_and_enum_boundaries_are_enforced() -> None:
    with pytest.raises(ValidationError):
        QuoteItem(description="missing id", estimated_hours=Hours(value=1), hourly_rate=Money(amount=1, currency="SEK"))

    with pytest.raises(ValidationError):
        Hours(value=1, unit="days")

    with pytest.raises(ValidationError):
        Quote(
            quote_id="quote-1",
            project_name="Example project",
            currency="SEK",
            items=[
                QuoteItem(
                    item_id="item-1",
                    description="Analysis",
                    estimated_hours=Hours(value=1),
                    hourly_rate=Money(amount=1, currency="USD"),
                )
            ],
            created_at=NOW,
        )


def test_serialization_round_trip_preserves_nested_contract() -> None:
    original = AgentRequest(
        request_id="request-1",
        quotation_request=NewQuoteRequest(
            project_name="Example project",
            currency="SEK",
            items=[item()],
            requested_at=NOW,
        ),
    )

    restored = AgentRequest.model_validate_json(original.model_dump_json())
    assert restored == original


def test_draft_cannot_be_approved_and_evidence_is_traceable() -> None:
    evidence = RiskEvidence(
        evidence_id="evidence-1",
        source_quote_ids=["quote-1"],
        metric="hour variance",
        observed_value=Decimal("2"),
        unit="hours",
        data_origin=DataOrigin.SYNTHETIC,
    )
    suggestion = RiskSuggestion(
        suggestion_id="risk-1",
        severity=RiskSeverity.MEDIUM,
        message="Review testing effort.",
        evidence_ids=[evidence.evidence_id],
    )
    draft = DraftQuote(quote=quote(), risk_suggestions=[suggestion])
    result = AgentResult(
        request_id="request-1",
        status=AgentResultStatus.SUCCESS,
        draft_quote=draft,
        evidence_ids=[evidence.evidence_id],
    )

    assert result.draft_quote is draft
    with pytest.raises(ValidationError):
        DraftQuote(quote=quote(), status=QuoteStatus.APPROVED)


def test_agent_result_presentation_evidence_is_additive_and_round_trips() -> None:
    legacy = AgentResult(request_id="legacy", status=AgentResultStatus.INVALID)
    assert legacy.similar_quotes == ()
    assert legacy.historical_comparisons == ()
    assert legacy.risk_evidence_reports == ()

    evidence = [
        RiskEvidence(
            evidence_id=f"risk-hours-{metric}",
            source_quote_ids=["quote-1"],
            metric=metric,
            observed_value=value,
            unit=unit,
            data_origin=DataOrigin.SYNTHETIC,
        )
        for metric, value, unit in (
            ("overrun_rate", Decimal("1"), "ratio"),
            ("average_variance", Decimal("2"), "hours"),
            ("median_variance", Decimal("2"), "hours"),
        )
    ]
    result = AgentResult(
        request_id="request-presentation",
        status=AgentResultStatus.SUCCESS,
        evidence_ids=[evidence[0].evidence_id],
        similar_quotes=[{
            "quote_id": "quote-1",
            "similarity_score": Decimal("0.75"),
            "matching_features": ["project_name_tokens"],
        }],
        historical_comparisons=[HistoricalComparisonEvidence(
            quote_id="quote-1",
            source_id="source-1",
            hour_variance={
                "metric": "estimate_vs_actual",
                "estimated": Decimal("8"),
                "actual": Decimal("10"),
                "variance": Decimal("2"),
                "percentage": Decimal("25"),
                "unit": "hours",
            },
        )],
        risk_evidence_reports=[RiskEvidenceSummary(
            metric="hours",
            unit="hours",
            comparable_project_count=1,
            overrun_count=1,
            overrun_rate=Decimal("1"),
            average_variance=Decimal("2"),
            median_variance=Decimal("2"),
            evidence=evidence,
            source_quote_ids=["quote-1"],
        )],
    )

    restored = AgentResult.model_validate_json(result.model_dump_json())
    assert restored == result
    assert isinstance(restored.similar_quotes, tuple)
    assert isinstance(restored.historical_comparisons, tuple)
    assert isinstance(restored.risk_evidence_reports, tuple)


def test_agent_result_rejects_presentation_evidence_on_failure() -> None:
    with pytest.raises(ValidationError, match="failure result"):
        AgentResult(
            request_id="failed",
            status=AgentResultStatus.UNAVAILABLE,
            similar_quotes=[{
                "quote_id": "quote-1",
                "similarity_score": Decimal("0.5"),
                "matching_features": ["item_count"],
            }],
        )


@pytest.mark.parametrize("mutation", ["wrong_rate", "missing_source"])
def test_agent_result_rejects_inconsistent_presentation_evidence(mutation: str) -> None:
    source_quote_ids = ["quote-1"]
    evidence = [
        RiskEvidence(
            evidence_id="risk-hours-overrun-rate",
            source_quote_ids=source_quote_ids,
            metric="overrun_rate",
            observed_value=Decimal("1"),
            unit="ratio",
            data_origin=DataOrigin.SYNTHETIC,
        ),
        RiskEvidence(
            evidence_id="risk-hours-average-variance",
            source_quote_ids=source_quote_ids,
            metric="average_variance",
            observed_value=Decimal("2"),
            unit="hours",
            data_origin=DataOrigin.SYNTHETIC,
        ),
        RiskEvidence(
            evidence_id="risk-hours-median-variance",
            source_quote_ids=source_quote_ids,
            metric="median_variance",
            observed_value=Decimal("2"),
            unit="hours",
            data_origin=DataOrigin.SYNTHETIC,
        ),
    ]
    overrun_rate = Decimal("0") if mutation == "wrong_rate" else Decimal("1")
    if mutation == "missing_source":
        evidence[0] = evidence[0].model_copy(update={"source_quote_ids": ["missing"]})

    with pytest.raises(ValidationError):
        AgentResult(
            request_id="request-inconsistent",
            status=AgentResultStatus.SUCCESS,
            evidence_ids=[evidence[0].evidence_id],
            risk_evidence_reports=[RiskEvidenceSummary(
                metric="hours",
                unit="hours",
                comparable_project_count=1,
                overrun_count=1,
                overrun_rate=overrun_rate,
                average_variance=Decimal("2"),
                median_variance=Decimal("2"),
                evidence=evidence,
                source_quote_ids=source_quote_ids,
            )],
        )


def test_allowed_draft_quote_succeeds() -> None:
    draft = DraftQuote(quote=quote())

    assert draft.status is QuoteStatus.DRAFT
    assert draft.quote.status is QuoteStatus.DRAFT


def test_draft_rejects_approved_nested_quote() -> None:
    approved = quote().model_copy(update={"status": QuoteStatus.APPROVED})

    with pytest.raises(ValidationError, match="approved quote"):
        DraftQuote(quote=approved)


@pytest.mark.parametrize("origin", [DataOrigin.REAL, DataOrigin.SYNTHETIC])
def test_historical_quote_accepts_consistent_provenance(origin: DataOrigin) -> None:
    historical = HistoricalQuote(
        quote=quote().model_copy(update={"data_origin": origin}),
        outcome={},
        source_id="source-1",
        data_origin=origin,
    )

    assert historical.data_origin is origin
    assert historical.quote.data_origin is origin


def test_historical_quote_rejects_mismatched_provenance() -> None:
    with pytest.raises(ValidationError, match="provenance"):
        HistoricalQuote(
            quote=quote(),
            outcome={},
            source_id="source-1",
            data_origin=DataOrigin.REAL,
        )
