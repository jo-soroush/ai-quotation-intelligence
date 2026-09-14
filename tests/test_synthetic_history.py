from decimal import Decimal

from ai_quotation_intelligence.data import generate_synthetic_history
from ai_quotation_intelligence.domain import DataOrigin, QuoteStatus


def test_c03_has_approximately_forty_valid_multi_item_records() -> None:
    records = generate_synthetic_history()

    assert len(records) == 40
    assert len({record.quote.quote_id for record in records}) == 40
    assert all(record.data_origin is DataOrigin.SYNTHETIC for record in records)
    assert all(record.quote.data_origin is DataOrigin.SYNTHETIC for record in records)
    assert all(record.quote.status is QuoteStatus.VALIDATED for record in records)
    assert all(len(record.quote.items) >= 3 for record in records)


def test_c03_records_are_reproducible() -> None:
    first = generate_synthetic_history()
    second = generate_synthetic_history()

    assert [record.model_dump(mode="json") for record in first] == [
        record.model_dump(mode="json") for record in second
    ]


def test_c03_contains_controlled_outcome_patterns() -> None:
    records = generate_synthetic_history()
    labels = {record.outcome.outcome_label for record in records}

    assert {"under_estimate", "near_estimate", "over_estimate"}.issubset(labels)
    assert "testing_overrun" in labels
    assert "integration_overrun" in labels
    assert "scope_change_overrun" in labels
    assert any(record.outcome.scope_changed is True for record in records)


def estimated_hours(record) -> Decimal:
    return sum((item.estimated_hours.value for item in record.quote.items), Decimal("0"))


def test_c03_pattern_labels_match_numeric_outcomes() -> None:
    records = generate_synthetic_history()
    by_label = {
        label: [record for record in records if record.outcome.outcome_label == label]
        for label in {record.outcome.outcome_label for record in records}
    }

    assert all(record.outcome.actual_hours.value > estimated_hours(record) for record in by_label["under_estimate"])
    assert all(
        abs(record.outcome.actual_hours.value - estimated_hours(record)) <= Decimal("5")
        for record in by_label["near_estimate"]
    )
    assert all(record.outcome.actual_hours.value < estimated_hours(record) for record in by_label["over_estimate"])
    assert all(record.outcome.actual_hours.value > estimated_hours(record) for label in ("testing_overrun", "integration_overrun") for record in by_label[label])
    assert all(
        record.outcome.scope_changed is True and record.outcome.actual_hours.value > estimated_hours(record)
        for record in by_label["scope_change_overrun"]
    )


def test_c03_preserves_estimated_and_actual_values_as_distinct_fields() -> None:
    records = generate_synthetic_history()

    assert all(item.estimated_hours is not None for record in records for item in record.quote.items)
    assert all(record.outcome.actual_hours is not None for record in records)
