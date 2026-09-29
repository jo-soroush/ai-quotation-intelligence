"""Bounded C09 interfaces over completed, deterministic Core capabilities.

This module does not select tools, invoke a model, or own commercial arithmetic.
Draft creation, approval, and Excel remain unavailable until their owning Cards.
"""

from collections.abc import Callable
from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, ValidationError

from ai_quotation_intelligence.comparison import (
    HistoricalComparison,
    VarianceSummary,
    compare_historical_quotes,
    summarize_variances,
)
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import (
    AgentResultStatus,
    DataOrigin,
    HistoricalQuote,
    NewQuoteRequest,
    RiskEvidence,
    SimilarQuote,
    VarianceResult,
)
from ai_quotation_intelligence.retrieval import SimilarQuoteMatch, retrieve_similar_quotes
from ai_quotation_intelligence.risk_evidence import Metric, RiskEvidenceReport, build_risk_evidence


class FailureCode(StrEnum):
    INVALID_INPUT = "invalid_input"
    INVALID_OUTPUT = "invalid_output"
    UNAVAILABLE = "unavailable"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"
    UNSUPPORTED_OPERATION = "unsupported_operation"
    SERVICE_FAILURE = "service_failure"


class ToolFailure(Exception):
    """Explicit, non-sensitive failure at a tool boundary."""

    def __init__(self, code: FailureCode, tool: str, request_id: str = "unknown") -> None:
        self.code = code
        self.tool = tool
        self.request_id = request_id
        super().__init__(f"{tool}: {code.value}")


class ToolInput(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)
    request_id: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class HistoricalQuotesInput(ToolInput):
    pass


class HistoricalQuotesOutput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    tool: Literal["get_historical_quotes"] = "get_historical_quotes"
    request_id: str
    records: tuple[HistoricalQuote, ...]


class SimilarQuotesInput(ToolInput):
    request: NewQuoteRequest
    limit: int = Field(default=5, ge=1, le=40)


class SimilarQuotesOutput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    tool: Literal["find_similar_quotes"] = "find_similar_quotes"
    request_id: str
    matches: tuple[SimilarQuoteMatch, ...]


class ComparisonsInput(ToolInput):
    pass


class ComparisonsOutput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    tool: Literal["compare_estimate_to_actual"] = "compare_estimate_to_actual"
    request_id: str
    comparisons: tuple[HistoricalComparison, ...]


class StatisticsInput(ComparisonsInput):
    metric: Metric = "hours"


class StatisticsOutput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    tool: Literal["calculate_quote_statistics"] = "calculate_quote_statistics"
    request_id: str
    metric: Metric
    summary: VarianceSummary
    sources: tuple[tuple[str, str], ...]  # (quote_id, source_id), aligned with observations


class RiskEvidenceInput(StatisticsInput):
    pass


class RiskEvidenceOutput(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    tool: Literal["get_risk_evidence"] = "get_risk_evidence"
    request_id: str
    report: RiskEvidenceReport


@dataclass(frozen=True)
class ToolServices:
    """Injectable completed owners; None means capability unavailable."""

    history: Callable[[], object] | None = generate_synthetic_history
    similarity: Callable[..., object] | None = retrieve_similar_quotes
    comparisons: Callable[..., object] | None = compare_historical_quotes
    statistics: Callable[..., object] | None = summarize_variances
    risk_evidence: Callable[..., object] | None = build_risk_evidence


AVAILABLE_TOOLS = frozenset({
    "get_historical_quotes",
    "find_similar_quotes",
    "calculate_quote_statistics",
    "compare_estimate_to_actual",
    "get_risk_evidence",
})
DEFERRED_TOOLS = frozenset({"create_draft_quote", "validate_draft_quote", "generate_excel"})


def _input(model: type[ToolInput], value: object, tool: str) -> ToolInput:
    try:
        # Rebuild even model instances: model_construct/model_copy can bypass validation.
        data = value.model_dump() if isinstance(value, BaseModel) else value
        return model.model_validate(data)
    except (ValidationError, ValueError, TypeError, AttributeError):
        raise ToolFailure(FailureCode.INVALID_INPUT, tool) from None


def _historical(record: object, tool: str, request_id: str) -> HistoricalQuote:
    try:
        if not isinstance(record, HistoricalQuote):
            raise TypeError("historical record type")
        return HistoricalQuote.model_validate(record.model_dump())
    except (ValidationError, ValueError, TypeError, AttributeError):
        raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id) from None


def _history(records: object, tool: str, request_id: str) -> tuple[HistoricalQuote, ...]:
    if not isinstance(records, (list, tuple)):
        raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id)
    clean = tuple(_historical(record, tool, request_id) for record in records)
    if not clean:
        raise ToolFailure(FailureCode.INSUFFICIENT_EVIDENCE, tool, request_id)
    if (len({record.source_id for record in clean}) != len(clean)
            or len({record.quote.quote_id for record in clean}) != len(clean)
            or len({record.data_origin for record in clean}) != 1):
        raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id)
    return clean


def _variance(value: object, tool: str, request_id: str) -> VarianceResult | None:
    if value is None:
        return None
    try:
        if not isinstance(value, VarianceResult):
            raise TypeError("variance type")
        if any(number is not None and (type(number) is not Decimal or not number.is_finite())
               for number in (value.estimated, value.actual, value.variance, value.percentage)):
            raise TypeError("variance number type")
        return VarianceResult.model_validate(value.model_dump())
    except (ValidationError, ValueError, TypeError, AttributeError):
        raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id) from None


def _comparison(value: object, tool: str, request_id: str) -> HistoricalComparison:
    if not isinstance(value, HistoricalComparison):
        raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id)
    if (not isinstance(value.quote_id, str) or not value.quote_id
            or not isinstance(value.source_id, str) or not value.source_id
            or value.scope_changed is not None and not isinstance(value.scope_changed, bool)
            or value.outcome_label is not None and not isinstance(value.outcome_label, str)):
        raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id)
    return HistoricalComparison(
        value.quote_id, value.source_id,
        _variance(value.hour_variance, tool, request_id),
        _variance(value.cost_variance, tool, request_id),
        value.scope_changed, value.outcome_label,
    )


class AgentTools:
    """Fixed, code-level C09 tool boundaries; no selection or agent loop."""

    def __init__(self, services: ToolServices | None = None) -> None:
        self._services = services if services is not None else ToolServices()

    def resolve_tool(self, name: str) -> Callable[..., object]:
        """Resolve only completed C09 operations; never dispatch arbitrary methods."""
        if not isinstance(name, str) or name not in AVAILABLE_TOOLS:
            raise ToolFailure(FailureCode.UNSUPPORTED_OPERATION, str(name))
        return {
            "get_historical_quotes": self.get_historical_quotes,
            "find_similar_quotes": self.find_similar_quotes,
            "calculate_quote_statistics": self.calculate_quote_statistics,
            "compare_estimate_to_actual": self.compare_estimate_to_actual,
            "get_risk_evidence": self.get_risk_evidence,
        }[name]

    @staticmethod
    def _call(service: Callable[..., object] | None, tool: str, request_id: str, *args: object, **kwargs: object) -> object:
        if service is None:
            raise ToolFailure(FailureCode.UNAVAILABLE, tool, request_id)
        try:
            return service(*args, **kwargs)
        except Exception:
            # Do not expose delegated exception text, which may contain secrets.
            raise ToolFailure(FailureCode.SERVICE_FAILURE, tool, request_id) from None

    def _source_history(self, tool: str, request_id: str) -> tuple[HistoricalQuote, ...]:
        """Only C03's owned corpus may enter C09 as historical evidence."""
        records = _history(self._call(self._services.history, tool, request_id), tool, request_id)
        if records != tuple(self._call(generate_synthetic_history, tool, request_id)):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, request_id)
        return records

    def get_historical_quotes(self, request: HistoricalQuotesInput) -> HistoricalQuotesOutput:
        tool = "get_historical_quotes"
        data = _input(HistoricalQuotesInput, request, tool)
        records = self._source_history(tool, data.request_id)
        return HistoricalQuotesOutput(request_id=data.request_id, records=records)

    def find_similar_quotes(self, request: SimilarQuotesInput) -> SimilarQuotesOutput:
        tool = "find_similar_quotes"
        data = _input(SimilarQuotesInput, request, tool)
        history = self._source_history(tool, data.request_id)
        raw = self._call(self._services.similarity, tool, data.request_id, data.request, history, limit=data.limit)
        if not isinstance(raw, tuple):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        if not raw:
            raise ToolFailure(FailureCode.INSUFFICIENT_EVIDENCE, tool, data.request_id)
        if len(raw) > data.limit:
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        sources = {(record.quote.quote_id, record.source_id, record.data_origin) for record in history}
        matches: list[SimilarQuoteMatch] = []
        for match in raw:
            try:
                if not isinstance(match, SimilarQuoteMatch) or not isinstance(match.result, SimilarQuote):
                    raise TypeError("match type")
                clean = SimilarQuoteMatch(
                    SimilarQuote.model_validate(match.result.model_dump()),
                    match.source_id,
                    DataOrigin(match.data_origin),
                )
            except (ValidationError, ValueError, TypeError, AttributeError):
                raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id) from None
            if (clean.result.quote_id, clean.source_id, clean.data_origin) not in sources:
                raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
            matches.append(clean)
        if len({(match.result.quote_id, match.source_id) for match in matches}) != len(matches):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        if tuple(matches) != self._call(retrieve_similar_quotes, tool, data.request_id,
                                        data.request, history, limit=data.limit):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        return SimilarQuotesOutput(request_id=data.request_id, matches=tuple(matches))

    def compare_estimate_to_actual(self, request: ComparisonsInput) -> ComparisonsOutput:
        tool = "compare_estimate_to_actual"
        data = _input(ComparisonsInput, request, tool)
        history = self._source_history(tool, data.request_id)
        raw = self._call(self._services.comparisons, tool, data.request_id, history)
        if not isinstance(raw, tuple) or len(raw) != len(history):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        comparisons = tuple(_comparison(item, tool, data.request_id) for item in raw)
        for record, comparison in zip(history, comparisons, strict=True):
            if ((comparison.quote_id, comparison.source_id) != (record.quote.quote_id, record.source_id)
                    or (comparison.hour_variance is None) != (record.outcome.actual_hours is None)
                    or (comparison.cost_variance is None) != (record.outcome.actual_cost is None)
                    or comparison.scope_changed != record.outcome.scope_changed
                    or comparison.outcome_label != record.outcome.outcome_label):
                raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        if comparisons != self._call(compare_historical_quotes, tool, data.request_id, history):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        if all(item.hour_variance is None and item.cost_variance is None for item in comparisons):
            raise ToolFailure(FailureCode.INSUFFICIENT_EVIDENCE, tool, data.request_id)
        return ComparisonsOutput(request_id=data.request_id, comparisons=comparisons)

    def calculate_quote_statistics(self, request: StatisticsInput) -> StatisticsOutput:
        tool = "calculate_quote_statistics"
        data = _input(StatisticsInput, request, tool)
        history = self._source_history(tool, data.request_id)
        raw_comparisons = self._call(self._services.comparisons, tool, data.request_id, history)
        if not isinstance(raw_comparisons, tuple) or len(raw_comparisons) != len(history):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        comparisons = tuple(_comparison(item, tool, data.request_id) for item in raw_comparisons)
        if comparisons != self._call(compare_historical_quotes, tool, data.request_id, history):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        selected: list[VarianceResult] = []
        sources: list[tuple[str, str]] = []
        for record, comparison in zip(history, comparisons, strict=True):
            if (comparison.quote_id, comparison.source_id) != (record.quote.quote_id, record.source_id):
                raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
            variance = comparison.hour_variance if data.metric == "hours" else comparison.cost_variance
            if variance is not None:
                selected.append(variance)
                sources.append((comparison.quote_id, comparison.source_id))
        if not selected:
            raise ToolFailure(FailureCode.INSUFFICIENT_EVIDENCE, tool, data.request_id)
        raw_summary = self._call(self._services.statistics, tool, data.request_id, tuple(selected))
        if not isinstance(raw_summary, VarianceSummary):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        observations = tuple(_variance(item, tool, data.request_id) for item in raw_summary.observations)
        if (observations != tuple(selected) or raw_summary.metric != "estimate_vs_actual"
                or type(raw_summary.overrun_count) is not int
                or not 0 <= raw_summary.overrun_count <= len(selected)
                or type(raw_summary.average_variance) is not Decimal
                or type(raw_summary.median_variance) is not Decimal
                or not raw_summary.average_variance.is_finite()
                or not raw_summary.median_variance.is_finite()):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        summary = VarianceSummary(
            raw_summary.metric, tuple(selected), raw_summary.overrun_count,
            raw_summary.average_variance, raw_summary.median_variance,
        )
        if summary != self._call(summarize_variances, tool, data.request_id, tuple(selected)):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        return StatisticsOutput(request_id=data.request_id, metric=data.metric, summary=summary, sources=tuple(sources))

    def get_risk_evidence(self, request: RiskEvidenceInput) -> RiskEvidenceOutput:
        tool = "get_risk_evidence"
        data = _input(RiskEvidenceInput, request, tool)
        history = self._source_history(tool, data.request_id)
        raw = self._call(self._services.risk_evidence, tool, data.request_id, history, metric=data.metric)
        if not isinstance(raw, RiskEvidenceReport) or raw.metric != data.metric:
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        if raw != self._call(build_risk_evidence, tool, data.request_id, history, metric=data.metric):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        if raw.status is AgentResultStatus.INSUFFICIENT_EVIDENCE:
            raise ToolFailure(FailureCode.INSUFFICIENT_EVIDENCE, tool, data.request_id)
        if raw.status is not AgentResultStatus.SUCCESS:
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        pairs = {(record.quote.quote_id, record.source_id, record.data_origin) for record in history}
        if (not raw.evidence or not raw.source_ids
                or len(raw.source_ids) != len(raw.source_quote_ids)
                or type(raw.comparable_project_count) is not int
                or type(raw.overrun_count) is not int
                or raw.comparable_project_count != len(raw.source_ids)
                or not 0 <= raw.overrun_count <= raw.comparable_project_count
                or raw.unit is None or raw.average_variance is None or raw.median_variance is None
                or any(type(number) is not Decimal or not number.is_finite()
                       for number in (raw.overrun_rate, raw.average_variance, raw.median_variance))
                or not 0 <= raw.overrun_rate <= 1):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        evidence: list[RiskEvidence] = []
        for item in raw.evidence:
            try:
                if not isinstance(item, RiskEvidence):
                    raise TypeError("risk evidence type")
                if type(item.observed_value) is not Decimal or not item.observed_value.is_finite():
                    raise TypeError("risk evidence number type")
                evidence.append(RiskEvidence.model_validate(item.model_dump()))
            except (ValidationError, ValueError, TypeError, AttributeError):
                raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id) from None
        origin = history[0].data_origin
        if (any((quote_id, source_id, origin) not in pairs
                for quote_id, source_id in zip(raw.source_quote_ids, raw.source_ids, strict=True))
                or any(item.data_origin is not origin
                       or not set(item.source_quote_ids) <= set(raw.source_quote_ids)
                       for item in evidence)):
            raise ToolFailure(FailureCode.INVALID_OUTPUT, tool, data.request_id)
        report = RiskEvidenceReport(
            raw.status, raw.metric, raw.unit, raw.comparable_project_count,
            raw.overrun_count, raw.overrun_rate, raw.average_variance,
            raw.median_variance, tuple(evidence), raw.source_quote_ids,
            raw.source_ids, raw.work_item_context, raw.scope_change_quote_ids,
            raw.outcome_labels,
        )
        return RiskEvidenceOutput(request_id=data.request_id, report=report)


__all__ = [
    "AgentTools", "AVAILABLE_TOOLS", "DEFERRED_TOOLS", "ToolServices", "ToolFailure",
    "FailureCode", "HistoricalQuotesInput", "HistoricalQuotesOutput", "SimilarQuotesInput",
    "SimilarQuotesOutput", "ComparisonsInput", "ComparisonsOutput", "StatisticsInput",
    "StatisticsOutput", "RiskEvidenceInput", "RiskEvidenceOutput",
]
