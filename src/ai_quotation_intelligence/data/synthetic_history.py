"""Deterministic, fictional historical quotations for local development.

This module creates C03 input data only. It does not calculate quotation
totals, compare records, retrieve similar quotes, or produce risk evidence.
All values below are deliberately supplied synthetic observations.
"""

from datetime import datetime, timedelta, timezone
from decimal import Decimal

from ai_quotation_intelligence.domain import (
    DataOrigin,
    HistoricalQuote,
    Hours,
    Money,
    ProjectOutcome,
    Quote,
    QuoteItem,
    QuoteStatus,
)


_CURRENCY = "SEK"
_CASE_COUNT = 40
_PATTERNS = (
    ("under_estimate", Decimal("54"), False, "Software Development", "Developer"),
    ("near_estimate", Decimal("42"), False, "Requirements Engineering", "Business Analyst"),
    ("testing_overrun", Decimal("68"), False, "Test Automation / QA", "QA Engineer"),
    ("integration_overrun", Decimal("72"), False, "Embedded / Integration", "Integration Engineer"),
    ("scope_change_overrun", Decimal("80"), True, "Digitalization", "Product Manager"),
    ("under_estimate", Decimal("55"), False, "Cloud / Platform", "Platform Engineer"),
    ("near_estimate", Decimal("45"), False, "Software Architecture", "Architect"),
    ("over_estimate", Decimal("29"), False, "Project Management", "Project Manager"),
    ("scope_change_overrun", Decimal("76"), True, "AI / ML Proof of Concept", "ML Engineer"),
    ("near_estimate", Decimal("42"), False, "Data Engineering", "Data Engineer"),
)


def _items(case_number: int, category: str, role: str) -> list[QuoteItem]:
    """Return three fictional work items with explicit estimated hours."""

    variation = Decimal(case_number % 4)
    return [
        QuoteItem(
            item_id=f"c03-{case_number:03d}-design",
            description=f"{category} design",
            estimated_hours=Hours(value=Decimal("12") + variation),
            hourly_rate=Money(amount=Decimal("110"), currency=_CURRENCY),
        ),
        QuoteItem(
            item_id=f"c03-{case_number:03d}-build",
            description=f"{category} {role.lower()} work",
            estimated_hours=Hours(value=Decimal("20") + variation),
            hourly_rate=Money(amount=Decimal("125"), currency=_CURRENCY),
        ),
        QuoteItem(
            item_id=f"c03-{case_number:03d}-verify",
            description=f"{category} verification",
            estimated_hours=Hours(value=Decimal("8") + variation),
            hourly_rate=Money(amount=Decimal("100"), currency=_CURRENCY),
        ),
    ]


def generate_synthetic_history() -> list[HistoricalQuote]:
    """Build the deterministic C03 historical quotation collection.

    The ten supplied pattern rows are repeated four times to provide 40
    varied, reproducible records. Actual outcomes are fictional observed
    values, not calculations performed by a quotation engine.
    """

    records: list[HistoricalQuote] = []
    start = datetime(2022, 1, 10, 9, tzinfo=timezone.utc)
    for case_number in range(1, _CASE_COUNT + 1):
        pattern, actual_hours, scope_changed, category, role = _PATTERNS[(case_number - 1) % len(_PATTERNS)]
        quote_id = f"synthetic-c03-quote-{case_number:03d}"
        quote = Quote(
            quote_id=quote_id,
            project_name=f"Fictional {category} Case {case_number:03d}",
            currency=_CURRENCY,
            items=_items(case_number, category, role),
            status=QuoteStatus.VALIDATED,
            created_at=start + timedelta(days=case_number * 17),
            data_origin=DataOrigin.SYNTHETIC,
        )
        records.append(
            HistoricalQuote(
                quote=quote,
                outcome=ProjectOutcome(
                    actual_hours=Hours(value=actual_hours),
                    completed_at=quote.created_at + timedelta(days=21),
                    scope_changed=scope_changed,
                    outcome_label=pattern,
                ),
                source_id=f"synthetic-c03-source-{case_number:03d}",
                data_origin=DataOrigin.SYNTHETIC,
            )
        )
    return records
