from copy import deepcopy
from decimal import Decimal

from ai_quotation_intelligence.comparison import compare_historical_quote
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import (
    AgentResultStatus,
    DataOrigin,
    Hours,
    Money,
    TimeUnit,
)
from ai_quotation_intelligence.risk_evidence import build_risk_evidence


def test_risk_evidence_reconciles_counts_rate_statistics_and_ids() -> None:
    records = generate_synthetic_history()[:4]
    report = build_risk_evidence(records)
    expected = [compare_historical_quote(record).hour_variance for record in records]
    expected = [result for result in expected if result is not None]

    assert report.status is AgentResultStatus.SUCCESS
    assert report.comparable_project_count == len(expected)
    assert report.overrun_count == sum(result.variance > 0 for result in expected)
    assert report.overrun_rate == Decimal(report.overrun_count) / Decimal(len(expected))
    assert report.average_variance == sum((result.variance for result in expected), Decimal("0")) / Decimal(len(expected))
    assert report.source_quote_ids == tuple(record.quote.quote_id for record in records)
    assert report.source_ids == tuple(record.source_id for record in records)
    assert len(report.evidence) == 3
    assert all(item.data_origin is DataOrigin.SYNTHETIC for item in report.evidence)
    assert all(set(item.source_quote_ids) == set(report.source_quote_ids) for item in report.evidence)


def test_even_count_median_is_asserted_as_exact_decimal_value() -> None:
    base = generate_synthetic_history()[:4]
    records = []
    for record, delta in zip(
        base,
        (Decimal("-2"), Decimal("4"), Decimal("6"), Decimal("10")),
        strict=True,
    ):
        estimated = sum(
            (item.estimated_hours.value for item in record.quote.items), Decimal("0")
        )
        records.append(
            record.model_copy(
                update={
                    "outcome": record.outcome.model_copy(
                        update={
                            "actual_hours": Hours(
                                value=estimated + delta, unit=TimeUnit.HOURS
                            )
                        }
                    )
                }
            )
        )

    report = build_risk_evidence(records)

    assert report.average_variance == Decimal("4.5")
    assert report.median_variance == Decimal("5")


def test_risk_evidence_uses_cost_metric_without_reimplementing_arithmetic() -> None:
    base = generate_synthetic_history()[:2]
    records = [
        record.model_copy(
            update={
                "outcome": record.outcome.model_copy(
                    update={
                        "actual_cost": Money(
                            amount=Decimal(str(5000 + index * 100)), currency="SEK"
                        )
                    }
                )
            }
        )
        for index, record in enumerate(base)
    ]
    report = build_risk_evidence(records, metric="cost")

    assert report.status is AgentResultStatus.SUCCESS
    assert report.metric == "cost"
    assert report.unit == "SEK"
    assert report.comparable_project_count == 2
    assert all(item.unit in {"ratio", "SEK"} for item in report.evidence)


def test_missing_outcomes_are_excluded_not_success() -> None:
    records = list(generate_synthetic_history())
    records[0] = records[0].model_copy(update={"outcome": records[0].outcome.model_copy(update={"actual_hours": None})})
    before = deepcopy(records)

    report = build_risk_evidence(records)

    assert report.comparable_project_count == 39
    assert records == before
    assert records[0].quote.quote_id not in report.source_quote_ids


def test_empty_history_is_explicitly_insufficient() -> None:
    report = build_risk_evidence([])

    assert report.status is AgentResultStatus.INSUFFICIENT_EVIDENCE
    assert report.comparable_project_count == 0
    assert report.overrun_rate is None
    assert report.evidence == ()


def test_missing_cost_is_insufficient_for_cost_metric() -> None:
    records = list(generate_synthetic_history())
    records[0] = records[0].model_copy(update={"outcome": records[0].outcome.model_copy(update={"actual_cost": None})})

    report = build_risk_evidence(records, metric="cost")

    assert report.status is AgentResultStatus.INSUFFICIENT_EVIDENCE
    assert report.comparable_project_count == 0
    assert report.evidence == ()


def test_scope_and_outcome_context_is_preserved() -> None:
    records = generate_synthetic_history()
    report = build_risk_evidence(records)

    assert report.scope_change_quote_ids
    assert report.outcome_labels
    assert report.work_item_context


def test_repeated_generation_is_identical() -> None:
    records = generate_synthetic_history()

    assert build_risk_evidence(records) == build_risk_evidence(records)


def test_full_c03_history_is_consumed_without_mutation() -> None:
    records = generate_synthetic_history()

    report = build_risk_evidence(records)

    assert report.comparable_project_count == 40
    assert len(report.source_quote_ids) == 40
    assert len(set(report.source_quote_ids)) == 40


def test_unsupported_metric_is_rejected() -> None:
    try:
        build_risk_evidence(generate_synthetic_history(), metric="money")  # type: ignore[arg-type]
    except ValueError as exc:
        assert str(exc) == "metric must be 'hours' or 'cost'"
    else:
        raise AssertionError("unsupported metrics must be rejected")


def test_mixed_data_origins_are_rejected() -> None:
    records = list(generate_synthetic_history())
    records[0] = records[0].model_copy(update={"data_origin": DataOrigin.REAL, "quote": records[0].quote.model_copy(update={"data_origin": DataOrigin.REAL})})

    try:
        build_risk_evidence(records)
    except ValueError as exc:
        assert str(exc) == "risk evidence requires one data origin"
    else:
        raise AssertionError("mixed data origins must be rejected")
