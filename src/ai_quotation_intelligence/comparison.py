"""Deterministic historical estimate-versus-outcome comparison for V1-C05."""

from dataclasses import dataclass
from decimal import Decimal
from statistics import median
from typing import Iterable

from ai_quotation_intelligence.calculation import calculate_quote_total
from ai_quotation_intelligence.domain.models import (
    HistoricalQuote,
    VarianceResult,
)


def _finite(value: Decimal, field_name: str) -> Decimal:
    if not value.is_finite():
        raise ValueError(f"{field_name} must be finite")
    return value


def _variance(estimated: Decimal, actual: Decimal, unit: str) -> VarianceResult:
    estimated = _finite(estimated, "estimated value")
    actual = _finite(actual, "actual value")
    variance = actual - estimated
    percentage = None if estimated == 0 else (variance / estimated) * Decimal("100")
    return VarianceResult(
        metric="estimate_vs_actual",
        estimated=estimated,
        actual=actual,
        variance=variance,
        percentage=percentage,
        unit=unit,
    )


@dataclass(frozen=True)
class HistoricalComparison:
    """Comparison evidence for one validated historical quotation."""

    quote_id: str
    source_id: str
    hour_variance: VarianceResult | None
    cost_variance: VarianceResult | None
    scope_changed: bool | None
    outcome_label: str | None


@dataclass(frozen=True)
class VarianceSummary:
    """Deterministic aggregate over already-produced variance evidence."""

    metric: str
    observations: tuple[VarianceResult, ...]
    overrun_count: int
    average_variance: Decimal | None
    median_variance: Decimal | None


def compare_historical_quote(record: HistoricalQuote) -> HistoricalComparison:
    """Compare one historical estimate with its available observed outcome.

    Missing outcomes remain explicit. Cost comparison is produced only when a
    validated actual cost exists; no actual cost is inferred from hours.
    """

    estimated_hours = sum(
        (item.estimated_hours.value for item in record.quote.items), Decimal("0")
    )
    actual_hours = record.outcome.actual_hours
    hour_variance = (
        None
        if actual_hours is None
        else _variance(estimated_hours, actual_hours.value, actual_hours.unit.value)
    )

    cost_variance = None
    if record.outcome.actual_cost is not None:
        estimated_cost = calculate_quote_total(record.quote)
        if record.outcome.actual_cost.currency != estimated_cost.currency:
            raise ValueError("historical actual cost must use the quote currency")
        cost_variance = _variance(
            estimated_cost.amount,
            record.outcome.actual_cost.amount,
            record.outcome.actual_cost.currency,
        )

    return HistoricalComparison(
        quote_id=record.quote.quote_id,
        source_id=record.source_id,
        hour_variance=hour_variance,
        cost_variance=cost_variance,
        scope_changed=record.outcome.scope_changed,
        outcome_label=record.outcome.outcome_label,
    )


def compare_historical_quotes(
    records: Iterable[HistoricalQuote],
) -> tuple[HistoricalComparison, ...]:
    """Compare records in input order without mutating the source collection."""

    return tuple(compare_historical_quote(record) for record in records)


def summarize_variances(
    variances: Iterable[VarianceResult],
) -> VarianceSummary:
    """Aggregate variance evidence using exact Decimal average and median."""

    observations = tuple(variances)
    if observations:
        first_metric = observations[0].metric
        first_unit = observations[0].unit
        if any(
            result.metric != first_metric or result.unit != first_unit
            for result in observations[1:]
        ):
            raise ValueError("variance observations must share metric and unit")
    values = tuple(
        _finite(result.variance, "variance")
        for result in observations
        if result.variance is not None
    )
    if not values:
        return VarianceSummary(
            metric="estimate_vs_actual",
            observations=observations,
            overrun_count=0,
            average_variance=None,
            median_variance=None,
        )
    return VarianceSummary(
        metric=observations[0].metric,
        observations=observations,
        overrun_count=sum(value > 0 for value in values),
        average_variance=sum(values, Decimal("0")) / Decimal(len(values)),
        median_variance=median(values),
    )


__all__ = [
    "HistoricalComparison",
    "VarianceSummary",
    "compare_historical_quote",
    "compare_historical_quotes",
    "summarize_variances",
]
