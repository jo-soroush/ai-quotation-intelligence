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
