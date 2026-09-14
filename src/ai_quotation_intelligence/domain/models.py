"""Typed, provider-neutral domain contracts for quotation intelligence.

These models validate shape and semantic boundaries only. They deliberately do
not calculate totals, compare history, retrieve similar quotations, or invoke
AI/providers; those responsibilities belong to later Cards.
"""

from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator


NonEmptyText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
CurrencyCode = Annotated[
    str,
    StringConstraints(strip_whitespace=True, to_upper=True, pattern=r"^[A-Z]{3}$"),
]
NonNegativeDecimal = Annotated[Decimal, Field(ge=Decimal("0"))]
UnitInterval = Annotated[Decimal, Field(ge=Decimal("0"), le=Decimal("1"))]


class DomainModel(BaseModel):
    """Shared strict configuration for Core contracts."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True)


class TimeUnit(StrEnum):
    HOURS = "hours"


class DataOrigin(StrEnum):
    SYNTHETIC = "synthetic"
    REAL = "real"
    UNKNOWN = "unknown"


class QuoteStatus(StrEnum):
    DRAFT = "draft"
    VALIDATED = "validated"
    AWAITING_REVIEW = "awaiting_review"
    APPROVED = "approved"
    REJECTED = "rejected"


class ApprovalStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class RiskSeverity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"


class AgentResultStatus(StrEnum):
    SUCCESS = "success"
    INVALID = "invalid"
    UNAVAILABLE = "unavailable"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"


class Money(DomainModel):
    """A non-negative monetary amount whose currency is always explicit."""

    amount: NonNegativeDecimal
    currency: CurrencyCode


class Hours(DomainModel):
    """A non-negative time quantity with an explicit unit."""

    value: NonNegativeDecimal
    unit: TimeUnit = TimeUnit.HOURS


class ProjectOutcome(DomainModel):
    """Observed outcome data; missing actuals remain explicitly unknown."""

    actual_hours: Hours | None = None
    actual_cost: Money | None = None
    completed_at: datetime | None = None
    scope_changed: bool | None = None
    outcome_label: NonEmptyText | None = None


class QuoteItem(DomainModel):
    """A quotation work item without calculation behavior."""

    item_id: NonEmptyText
    description: NonEmptyText
    estimated_hours: Hours
    hourly_rate: Money
    actual_hours: Hours | None = None
    actual_cost: Money | None = None


class Quote(DomainModel):
    """A quotation contract; totals are supplied values, never calculated here."""

    quote_id: NonEmptyText
    project_name: NonEmptyText
    currency: CurrencyCode
    items: list[QuoteItem] = Field(min_length=1)
    status: QuoteStatus = QuoteStatus.DRAFT
    estimated_total_cost: Money | None = None
    actual_total_cost: Money | None = None
    created_at: datetime
    data_origin: DataOrigin = DataOrigin.UNKNOWN

    @model_validator(mode="after")
    def totals_match_quote_currency(self) -> "Quote":
        for item in self.items:
            if item.hourly_rate.currency != self.currency:
                raise ValueError("quote item rates must use the quote currency")
            if item.actual_cost is not None and item.actual_cost.currency != self.currency:
                raise ValueError("quote item actual costs must use the quote currency")
        for total in (self.estimated_total_cost, self.actual_total_cost):
            if total is not None and total.currency != self.currency:
                raise ValueError("quote totals must use the quote currency")
        return self


class HistoricalQuote(DomainModel):
    """A quotation plus its observed outcome and provenance."""

    quote: Quote
    outcome: ProjectOutcome
    source_id: NonEmptyText
    data_origin: DataOrigin

    @model_validator(mode="after")
    def provenance_matches_nested_quote(self) -> "HistoricalQuote":
        if self.quote.data_origin is not self.data_origin:
            raise ValueError("historical quote provenance must match nested quote provenance")
        return self


class NewQuoteRequest(DomainModel):
    """Validated input contract for requesting a new quotation draft."""

    project_name: NonEmptyText
    currency: CurrencyCode
    items: list[QuoteItem] = Field(min_length=1)
    requested_at: datetime

    @model_validator(mode="after")
    def item_rates_match_request_currency(self) -> "NewQuoteRequest":
        if any(item.hourly_rate.currency != self.currency for item in self.items):
            raise ValueError("quote item rates must use the request currency")
        return self


class VarianceResult(DomainModel):
    """A typed result boundary; variance arithmetic belongs to a later Card."""

    metric: NonEmptyText
    estimated: NonNegativeDecimal | None = None
    actual: NonNegativeDecimal | None = None
    variance: Decimal | None = None
    percentage: Decimal | None = None
    unit: NonEmptyText


class SimilarQuote(DomainModel):
    """A ranked reference to a historical quote, not a copied commercial value."""

    quote_id: NonEmptyText
    similarity_score: UnitInterval
    matching_features: list[NonEmptyText] = Field(min_length=1)


class RiskEvidence(DomainModel):
    """Traceable observed evidence that can support a later risk suggestion."""

    evidence_id: NonEmptyText
    source_quote_ids: list[NonEmptyText] = Field(min_length=1)
    metric: NonEmptyText
    observed_value: Decimal
    unit: NonEmptyText
    data_origin: DataOrigin


class RiskSuggestion(DomainModel):
    """An interpretation linked to evidence; no risk analysis is performed here."""

    suggestion_id: NonEmptyText
    severity: RiskSeverity
    message: NonEmptyText
    evidence_ids: list[NonEmptyText] = Field(min_length=1)
    confidence: UnitInterval | None = None


class DraftQuote(DomainModel):
    """An unapproved draft quotation with explicit status and evidence links."""

    quote: Quote
    status: QuoteStatus = QuoteStatus.DRAFT
    risk_suggestions: list[RiskSuggestion] = Field(default_factory=list)
    evidence_ids: list[NonEmptyText] = Field(default_factory=list)

    @model_validator(mode="after")
    def must_not_be_approved(self) -> "DraftQuote":
        if self.status is QuoteStatus.APPROVED or self.quote.status is QuoteStatus.APPROVED:
            raise ValueError("a DraftQuote cannot contain an approved quote")
        return self


class ApprovalDecision(DomainModel):
    """Human decision boundary for a quotation; execution belongs to later Cards."""

    quote_id: NonEmptyText
    status: ApprovalStatus
    reviewer_id: NonEmptyText
    decided_at: datetime | None = None
    reason: NonEmptyText | None = None


class AgentRequest(DomainModel):
    """Provider-neutral request envelope for later agent orchestration."""

    request_id: NonEmptyText
    quotation_request: NewQuoteRequest
    instructions: NonEmptyText | None = None


class AgentResult(DomainModel):
    """Provider-neutral result envelope with explicit failure statuses."""

    request_id: NonEmptyText
    status: AgentResultStatus
    draft_quote: DraftQuote | None = None
    risk_suggestions: list[RiskSuggestion] = Field(default_factory=list)
    evidence_ids: list[NonEmptyText] = Field(default_factory=list)
    message: NonEmptyText | None = None
