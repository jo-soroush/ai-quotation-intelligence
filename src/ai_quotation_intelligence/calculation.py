"""Deterministic quotation arithmetic for V1-C04.

This module owns authoritative estimated-cost arithmetic.  It consumes the
validated C02 domain contracts and deliberately performs no pricing strategy,
historical analysis, AI/provider calls, or currency conversion.
"""

from decimal import Decimal

from ai_quotation_intelligence.domain.models import Money, Quote, QuoteItem


def _finite(value: Decimal, field_name: str) -> Decimal:
    if not value.is_finite():
        raise ValueError(f"{field_name} must be finite")
    return value


def calculate_item_cost(item: QuoteItem) -> Money:
    """Calculate one item's estimated cost as estimated hours multiplied by rate."""

    hours = _finite(item.estimated_hours.value, "estimated hours")
    rate = _finite(item.hourly_rate.amount, "hourly rate")
    return Money(
        amount=hours * rate,
        currency=item.hourly_rate.currency,
    )


def calculate_quote_total(quote: Quote) -> Money:
    """Derive a quote's estimated total from its validated item costs.

    A supplied estimated total is treated as a reconciliation assertion rather
    than an independent source of arithmetic truth.
    """

    item_costs = [calculate_item_cost(item) for item in quote.items]
    total_amount = sum((cost.amount for cost in item_costs), Decimal("0"))
    total = Money(amount=total_amount, currency=quote.currency)
    if quote.estimated_total_cost is not None:
        supplied = _finite(quote.estimated_total_cost.amount, "estimated total")
        if supplied != total.amount:
            raise ValueError("supplied estimated total does not reconcile with item costs")
    return total


def calculate_quote(quote: Quote) -> Quote:
    """Return a quote with its authoritative estimated total populated.

    The input model is not mutated.  Existing totals must reconcile before the
    calculated result is returned.
    """

    total = calculate_quote_total(quote)
    return quote.model_copy(update={"estimated_total_cost": total})


__all__ = ["calculate_item_cost", "calculate_quote", "calculate_quote_total"]
