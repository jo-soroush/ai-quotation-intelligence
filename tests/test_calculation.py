from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from ai_quotation_intelligence.calculation import (
    calculate_item_cost,
    calculate_quote,
    calculate_quote_total,
)
from ai_quotation_intelligence.domain.models import Hours, Money, Quote, QuoteItem


def item(item_id: str, hours: str, rate: str, currency: str = "SEK") -> QuoteItem:
    return QuoteItem(
        item_id=item_id,
        description=f"Work {item_id}",
        estimated_hours=Hours(value=Decimal(hours)),
        hourly_rate=Money(amount=Decimal(rate), currency=currency),
    )


def quote(*items: QuoteItem, total: str | None = None, currency: str = "SEK") -> Quote:
    return Quote(
        quote_id="Q-C04-001",
        project_name="Synthetic calculation fixture",
        currency=currency,
        items=list(items),
        created_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
        estimated_total_cost=(Money(amount=Decimal(total), currency=currency) if total else None),
    )


def test_calculates_one_item_cost_with_decimal_arithmetic() -> None:
    assert calculate_item_cost(item("one", "8", "125")).amount == Decimal("1000")


def test_calculates_multi_item_total_from_item_costs() -> None:
    result = calculate_quote_total(item_quote := quote(item("one", "8", "125"), item("two", "2.5", "80")))
    assert result == Money(amount=Decimal("1200"), currency="SEK")
    assert calculate_quote(item_quote).estimated_total_cost == result


def test_supplied_total_must_reconcile_with_authoritative_item_costs() -> None:
    with pytest.raises(ValueError, match="does not reconcile"):
        calculate_quote_total(quote(item("one", "8", "125"), total="999"))


def test_decimal_precision_and_repeated_calculation_are_deterministic() -> None:
    quotation = quote(item("one", "0.1", "0.2"))
    assert calculate_item_cost(quotation.items[0]).amount == Decimal("0.02")
    assert calculate_quote(quotation) == calculate_quote(quotation)
    assert quotation.estimated_total_cost is None


def test_zero_hours_and_zero_rate_are_valid() -> None:
    assert calculate_item_cost(item("hours-zero", "0", "125")).amount == Decimal("0")
    assert calculate_item_cost(item("rate-zero", "8", "0")).amount == Decimal("0")


def test_negative_inputs_are_rejected_by_c02_models() -> None:
    with pytest.raises(ValidationError):
        item("negative-hours", "-1", "125")
    with pytest.raises(ValidationError):
        item("negative-rate", "1", "-125")


def test_missing_hours_or_rate_are_rejected_before_calculation() -> None:
    with pytest.raises(ValidationError):
        QuoteItem(
            item_id="missing-hours",
            description="Incomplete work",
            hourly_rate=Money(amount=Decimal("125"), currency="SEK"),
        )
    with pytest.raises(ValidationError):
        QuoteItem(
            item_id="missing-rate",
            description="Incomplete work",
            estimated_hours=Hours(value=Decimal("8")),
        )


@pytest.mark.parametrize("value", [Decimal("NaN"), Decimal("Infinity"), Decimal("-Infinity")])
def test_non_finite_numeric_inputs_are_rejected_by_c02_models(value: Decimal) -> None:
    with pytest.raises(ValidationError):
        Hours(value=value)
    with pytest.raises(ValidationError):
        Money(amount=value, currency="SEK")


def test_mixed_currency_and_empty_quotes_are_rejected_by_c02_models() -> None:
    with pytest.raises(ValidationError):
        quote(item("sek", "1", "10", "SEK"), item("eur", "1", "10", "EUR"))
    with pytest.raises(ValidationError):
        quote()
