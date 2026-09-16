from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from ai_quotation_intelligence.comparison import (
    compare_historical_quote,
    compare_historical_quotes,
    summarize_variances,
)
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import (
    DataOrigin,
    HistoricalQuote,
    Hours,
    Money,
    ProjectOutcome,
    Quote,
    QuoteItem,
    QuoteStatus,
    VarianceResult,
)


def record(
    estimated_hours: str,
    actual_hours: str | None,
    *,
    actual_cost: Money | None = None,
    scope_changed: bool | None = None,
) -> HistoricalQuote:
    quote = Quote(
        quote_id="comparison-quote",
        project_name="Comparison fixture",
        currency="SEK",
        items=[
            QuoteItem(
                item_id="item-1",
                description="Comparison work",
                estimated_hours=Hours(value=Decimal(estimated_hours)),
                hourly_rate=Money(amount=Decimal("100"), currency="SEK"),
            )
        ],
        status=QuoteStatus.VALIDATED,
        created_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        data_origin=DataOrigin.SYNTHETIC,
    )
    return HistoricalQuote(
        quote=quote,
        outcome=ProjectOutcome(
            actual_hours=(Hours(value=Decimal(actual_hours)) if actual_hours is not None else None),
            actual_cost=actual_cost,
            scope_changed=scope_changed,
        ),
        source_id="comparison-source",
        data_origin=DataOrigin.SYNTHETIC,
    )


def test_variance_direction_and_percentage_are_deterministic() -> None:
    above = compare_historical_quote(record("10", "12")).hour_variance
    below = compare_historical_quote(record("10", "8")).hour_variance
    equal = compare_historical_quote(record("10", "10")).hour_variance
    assert above and above.variance == Decimal("2") and above.percentage == Decimal("20")
    assert below and below.variance == Decimal("-2") and below.percentage == Decimal("-20")
    assert equal and equal.variance == Decimal("0") and equal.percentage == Decimal("0")


def test_cost_variance_uses_validated_actual_cost_without_inference() -> None:
    result = compare_historical_quote(
        record("10", "12", actual_cost=Money(amount=Decimal("1200"), currency="SEK"))
    )
    assert result.cost_variance and result.cost_variance.variance == Decimal("200")


def test_missing_outcome_remains_explicit() -> None:
    result = compare_historical_quote(record("10", None))
    assert result.hour_variance is None
    assert result.cost_variance is None


def test_zero_estimate_has_variance_but_no_percentage() -> None:
    result = compare_historical_quote(record("0", "2")).hour_variance
    assert result and result.variance == Decimal("2") and result.percentage is None


def test_summary_counts_positive_variance_and_calculates_decimal_average_median() -> None:
    results = [compare_historical_quote(record("10", actual)).hour_variance for actual in ("12", "8", "10")]
    summary = summarize_variances(result for result in results if result is not None)
    assert summary.overrun_count == 1
    assert summary.average_variance == Decimal("0")
    assert summary.median_variance == Decimal("0")


def test_summary_uses_two_middle_values_for_even_hour_variance_median() -> None:
    results = [
        compare_historical_quote(record("10", actual)).hour_variance
        for actual in ("14", "8", "18", "10")
    ]
    summary = summarize_variances(result for result in results if result is not None)
    assert summary.average_variance == Decimal("2.5")
    assert summary.median_variance == Decimal("2")


def test_summary_aggregates_decimal_cost_variances_and_excludes_missing_cost() -> None:
    results = [
        compare_historical_quote(
            record("10", "10", actual_cost=Money(amount=Decimal(cost), currency="SEK"))
        ).cost_variance
        for cost in ("1100", "900", "1000", "1200")
    ]
    missing_cost = compare_historical_quote(record("10", "10")).cost_variance
    assert missing_cost is None
    summary = summarize_variances(result for result in results if result is not None)
    assert summary.average_variance == Decimal("50")
    assert summary.median_variance == Decimal("50")


@pytest.mark.parametrize(
    "left,right",
    [
        (
            VarianceResult(
                metric="estimate_vs_actual",
                estimated=Decimal("10"),
                actual=Decimal("12"),
                variance=Decimal("2"),
                unit="hours",
            ),
            VarianceResult(
                metric="estimate_vs_actual",
                estimated=Decimal("100"),
                actual=Decimal("120"),
                variance=Decimal("20"),
                unit="SEK",
            ),
        ),
        (
            VarianceResult(
                metric="estimate_vs_actual",
                estimated=Decimal("100"),
                actual=Decimal("120"),
                variance=Decimal("20"),
                unit="SEK",
            ),
            VarianceResult(
                metric="estimate_vs_actual",
                estimated=Decimal("100"),
                actual=Decimal("120"),
                variance=Decimal("20"),
                unit="EUR",
            ),
        ),
    ],
)
def test_summary_rejects_incompatible_metric_or_unit(left: VarianceResult, right: VarianceResult) -> None:
    with pytest.raises(ValueError, match="share metric and unit"):
        summarize_variances([left, right])


def test_c03_history_integrates_without_mutation_and_preserves_provenance() -> None:
    history = generate_synthetic_history()
    before = tuple(record.quote.model_dump(mode="json") for record in history)
    comparisons = compare_historical_quotes(history)
    assert len(comparisons) == 40
    assert all(item.data_origin is DataOrigin.SYNTHETIC for item in history)
    assert before == tuple(record.quote.model_dump(mode="json") for record in history)
    assert comparisons == compare_historical_quotes(history)


def test_actual_cost_currency_mismatch_is_rejected() -> None:
    with pytest.raises(ValueError, match="quote currency"):
        compare_historical_quote(
            record("10", "10", actual_cost=Money(amount=Decimal("1000"), currency="EUR"))
        )


def test_variance_result_requires_valid_numeric_values() -> None:
    with pytest.raises(ValidationError):
        VarianceResult(
            metric="estimate_vs_actual",
            estimated=Decimal("NaN"),
            actual=Decimal("1"),
            variance=Decimal("1"),
            unit="hours",
        )
