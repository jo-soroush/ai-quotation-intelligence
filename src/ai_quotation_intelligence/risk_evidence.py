"""Deterministic, traceable risk evidence generation for V1-C07."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable, Literal

from ai_quotation_intelligence.comparison import (
    HistoricalComparison,
    compare_historical_quotes,
    summarize_variances,
)
from ai_quotation_intelligence.domain import (
    AgentResultStatus,
    DataOrigin,
    HistoricalQuote,
    RiskEvidence,
    VarianceResult,
)


Metric = Literal["hours", "cost"]


@dataclass(frozen=True)
class RiskEvidenceReport:
    """Deterministic evidence statistics with traceable historical context."""

    status: AgentResultStatus
    metric: Metric
    unit: str | None
    comparable_project_count: int
    overrun_count: int
    overrun_rate: Decimal | None
    average_variance: Decimal | None
    median_variance: Decimal | None
    evidence: tuple[RiskEvidence, ...]
    source_quote_ids: tuple[str, ...]
    source_ids: tuple[str, ...]
    work_item_context: tuple[str, ...]
    scope_change_quote_ids: tuple[str, ...]
    outcome_labels: tuple[str, ...]


def _metric_variance(comparison: HistoricalComparison, metric: Metric) -> VarianceResult | None:
    return comparison.hour_variance if metric == "hours" else comparison.cost_variance


def _empty_report(metric: Metric) -> RiskEvidenceReport:
    return RiskEvidenceReport(
        status=AgentResultStatus.INSUFFICIENT_EVIDENCE,
        metric=metric,
        unit=None,
        comparable_project_count=0,
        overrun_count=0,
        overrun_rate=None,
        average_variance=None,
        median_variance=None,
        evidence=(),
        source_quote_ids=(),
        source_ids=(),
        work_item_context=(),
        scope_change_quote_ids=(),
        outcome_labels=(),
    )


def build_risk_evidence(
    records: Iterable[HistoricalQuote],
    *,
    metric: Metric = "hours",
) -> RiskEvidenceReport:
    """Build traceable evidence from validated historical quotations.

    Missing actual outcomes are excluded from the selected metric's evidence;
    they are never converted to successful or zero-variance observations.
    The function delegates comparison and aggregate arithmetic to C05.
    """

    historical_records = tuple(records)
    if metric not in {"hours", "cost"}:
        raise ValueError("metric must be 'hours' or 'cost'")
    if not historical_records:
        return _empty_report(metric)

    origins = {record.data_origin for record in historical_records}
    if len(origins) != 1:
        raise ValueError("risk evidence requires one data origin")
    data_origin = next(iter(origins))
    comparisons = compare_historical_quotes(historical_records)
    selected = tuple(
        (record, comparison, _metric_variance(comparison, metric))
        for record, comparison in zip(historical_records, comparisons, strict=True)
        if _metric_variance(comparison, metric) is not None
    )
    if not selected:
        return _empty_report(metric)

    observations = tuple(item[2] for item in selected if item[2] is not None)
    summary = summarize_variances(observations)
    unit = observations[0].unit
    source_quote_ids = tuple(record.quote.quote_id for record, _, _ in selected)
    source_ids = tuple(record.source_id for record, _, _ in selected)
    work_item_context = tuple(
        item.description
        for record, _, _ in selected
        for item in record.quote.items
    )
    scope_change_quote_ids = tuple(
        record.quote.quote_id
        for record, _, _ in selected
        if record.outcome.scope_changed is True
    )
    outcome_labels = tuple(
        record.outcome.outcome_label
        for record, _, _ in selected
        if record.outcome.outcome_label is not None
    )
    comparable_project_count = len(observations)
    overrun_rate = Decimal(summary.overrun_count) / Decimal(comparable_project_count)
    evidence = (
        RiskEvidence(
            evidence_id=f"risk-{metric}-overrun-rate",
            source_quote_ids=list(source_quote_ids),
            metric="overrun_rate",
            observed_value=overrun_rate,
            unit="ratio",
            data_origin=data_origin,
        ),
        RiskEvidence(
            evidence_id=f"risk-{metric}-average-variance",
            source_quote_ids=list(source_quote_ids),
            metric="average_variance",
            observed_value=summary.average_variance,
            unit=unit,
            data_origin=data_origin,
        ),
        RiskEvidence(
            evidence_id=f"risk-{metric}-median-variance",
            source_quote_ids=list(source_quote_ids),
            metric="median_variance",
            observed_value=summary.median_variance,
            unit=unit,
            data_origin=data_origin,
        ),
    )
    return RiskEvidenceReport(
        status=AgentResultStatus.SUCCESS,
        metric=metric,
        unit=unit,
        comparable_project_count=comparable_project_count,
        overrun_count=summary.overrun_count,
        overrun_rate=overrun_rate,
        average_variance=summary.average_variance,
        median_variance=summary.median_variance,
        evidence=evidence,
        source_quote_ids=source_quote_ids,
        source_ids=source_ids,
        work_item_context=work_item_context,
        scope_change_quote_ids=scope_change_quote_ids,
        outcome_labels=outcome_labels,
    )


__all__ = ["Metric", "RiskEvidenceReport", "build_risk_evidence"]
