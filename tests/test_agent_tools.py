"""C09 contracts: bounded delegation, explicit failure, and provenance."""

from dataclasses import replace
from decimal import Decimal

import pytest

from ai_quotation_intelligence.agent_tools import (
    AgentTools,
    AVAILABLE_TOOLS,
    ComparisonsInput,
    ComparisonsOutput,
    DEFERRED_TOOLS,
    FailureCode,
    HistoricalQuotesInput,
    HistoricalQuotesOutput,
    RiskEvidenceInput,
    RiskEvidenceOutput,
    SimilarQuotesInput,
    SimilarQuotesOutput,
    StatisticsInput,
    StatisticsOutput,
    ToolFailure,
    ToolServices,
)
from ai_quotation_intelligence.comparison import (
    compare_historical_quotes,
    summarize_variances,
)
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import (
    AgentResultStatus,
    NewQuoteRequest,
    RiskEvidence,
    SimilarQuote,
)
from ai_quotation_intelligence.retrieval import SimilarQuoteMatch, retrieve_similar_quotes
from ai_quotation_intelligence.risk_evidence import build_risk_evidence


@pytest.fixture
def history():
    return tuple(generate_synthetic_history())


@pytest.fixture
def new_request(history):
    quote = history[0].quote
    return NewQuoteRequest(
        project_name=quote.project_name,
        currency=quote.currency,
        items=quote.items,
        requested_at=quote.created_at,
    )


def assert_failure(code: FailureCode, operation, *args) -> ToolFailure:
    with pytest.raises(ToolFailure) as raised:
        operation(*args)
    assert raised.value.code is code
    return raised.value


def test_completed_tools_have_typed_outputs_and_preserve_core_results(history, new_request) -> None:
    tools = AgentTools()
    historical = tools.get_historical_quotes(HistoricalQuotesInput(request_id="h1"))
    assert isinstance(historical, HistoricalQuotesOutput)
    assert historical.tool == "get_historical_quotes"
    assert historical.request_id == "h1"
    assert historical.records == tuple(generate_synthetic_history())

    similar = tools.find_similar_quotes(SimilarQuotesInput(
        request_id="s1", request=new_request, limit=2,
    ))
    assert isinstance(similar, SimilarQuotesOutput)
    assert similar.tool == "find_similar_quotes"
    assert similar.matches == retrieve_similar_quotes(new_request, history, limit=2)
    assert {(match.result.quote_id, match.source_id) for match in similar.matches} <= {
        (record.quote.quote_id, record.source_id) for record in history
    }

    comparison = tools.compare_estimate_to_actual(ComparisonsInput(request_id="c1"))
    assert isinstance(comparison, ComparisonsOutput)
    assert comparison.tool == "compare_estimate_to_actual"
    assert comparison.comparisons == compare_historical_quotes(history)

    statistics = tools.calculate_quote_statistics(StatisticsInput(
        request_id="t1", metric="hours",
    ))
    expected = compare_historical_quotes(history)
    assert isinstance(statistics, StatisticsOutput)
    assert statistics.tool == "calculate_quote_statistics"
    assert statistics.summary == summarize_variances(
        tuple(item.hour_variance for item in expected if item.hour_variance is not None)
    )
    assert statistics.sources == tuple((record.quote.quote_id, record.source_id) for record in history)

    risk = tools.get_risk_evidence(RiskEvidenceInput(request_id="r1"))
    assert isinstance(risk, RiskEvidenceOutput)
    assert risk.tool == "get_risk_evidence"
    assert risk.report == build_risk_evidence(history)
    assert risk.report.source_ids == tuple(record.source_id for record in history)


def test_each_tool_is_repeatable(history, new_request) -> None:
    tools = AgentTools()
    calls = (
        (tools.get_historical_quotes, HistoricalQuotesInput(request_id="repeat")),
        (tools.find_similar_quotes, SimilarQuotesInput(request_id="repeat", request=new_request)),
        (tools.compare_estimate_to_actual, ComparisonsInput(request_id="repeat")),
        (tools.calculate_quote_statistics, StatisticsInput(request_id="repeat")),
        (tools.get_risk_evidence, RiskEvidenceInput(request_id="repeat")),
    )
    for operation, request in calls:
        assert operation(request) == operation(request)


def test_fixed_resolver_rejects_future_and_arbitrary_operations() -> None:
    tools = AgentTools()
    assert AVAILABLE_TOOLS == {name for name in (
        "get_historical_quotes", "find_similar_quotes", "calculate_quote_statistics",
        "compare_estimate_to_actual", "get_risk_evidence",
    )}
    for name in AVAILABLE_TOOLS:
        assert callable(tools.resolve_tool(name))
    for name in (*DEFERRED_TOOLS, "approve_quote", "finalize_quote", "__class__"):
        assert_failure(FailureCode.UNSUPPORTED_OPERATION, tools.resolve_tool, name)


@pytest.mark.parametrize("name,payload", [
    ("get_historical_quotes", {"request_id": "x", "estimated_total_cost": 999999}),
    ("get_historical_quotes", {"request_id": ""}),
    ("get_historical_quotes", {"request_id": "   "}),
    ("compare_estimate_to_actual", {"request_id": "x", "history": [], "risk_evidence": "invented"}),
    ("calculate_quote_statistics", {"request_id": "x", "history": [], "metric": "price"}),
    ("get_risk_evidence", {"request_id": "x", "history": [], "metric": "cost", "approval": True}),
])
def test_untrusted_input_cannot_add_authoritative_values(name, payload) -> None:
    assert_failure(FailureCode.INVALID_INPUT, AgentTools().resolve_tool(name), payload)


def test_invalid_limit_and_fabricated_history_input_fail(new_request, history) -> None:
    tools = AgentTools()
    assert_failure(FailureCode.INVALID_INPUT, tools.find_similar_quotes, {
        "request_id": "x", "request": new_request, "limit": 0,
    })
    assert_failure(FailureCode.INVALID_INPUT, tools.compare_estimate_to_actual,
                   {"request_id": "x", "history": history})
    assert_failure(FailureCode.INVALID_INPUT, tools.get_risk_evidence,
                   {"request_id": "x", "history": ()})


@pytest.mark.parametrize("service_name,operation,input_name", [
    ("history", "get_historical_quotes", "historical"),
    ("similarity", "find_similar_quotes", "similar"),
    ("comparisons", "compare_estimate_to_actual", "comparison"),
    ("statistics", "calculate_quote_statistics", "statistics"),
    ("risk_evidence", "get_risk_evidence", "risk"),
])
def test_unavailable_completed_capability_is_not_success(
    service_name, operation, input_name, history, new_request,
) -> None:
    inputs = {
        "historical": HistoricalQuotesInput(request_id="missing"),
        "similar": SimilarQuotesInput(request_id="missing", request=new_request),
        "comparison": ComparisonsInput(request_id="missing"),
        "statistics": StatisticsInput(request_id="missing"),
        "risk": RiskEvidenceInput(request_id="missing"),
    }
    services = replace(ToolServices(), **{service_name: None})
    failure = assert_failure(FailureCode.UNAVAILABLE, AgentTools(services).resolve_tool(operation), inputs[input_name])
    assert failure.request_id == "missing"


def test_delegated_failure_propagates_without_secret_text(history) -> None:
    def broken(_records):
        raise RuntimeError("token=private-marker")

    tools = AgentTools(replace(ToolServices(), comparisons=broken))
    failure = assert_failure(FailureCode.SERVICE_FAILURE, tools.compare_estimate_to_actual,
                             ComparisonsInput(request_id="broken"))
    assert "private-marker" not in str(failure)
    assert failure.__cause__ is None
    assert failure.__suppress_context__


def test_missing_actual_cost_does_not_become_statistics_success(history) -> None:
    missing = tuple(record.model_copy(update={"outcome": record.outcome.model_copy(
        update={"actual_hours": None, "actual_cost": None,
        })}) for record in history)
    tools = AgentTools(replace(ToolServices(), history=lambda: list(missing)))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.compare_estimate_to_actual,
                   ComparisonsInput(request_id="altered-history"))
    tools = AgentTools()
    assert_failure(FailureCode.INSUFFICIENT_EVIDENCE, tools.calculate_quote_statistics,
                   StatisticsInput(request_id="missing-cost", metric="cost"))
    assert_failure(FailureCode.INSUFFICIENT_EVIDENCE, tools.get_risk_evidence,
                   RiskEvidenceInput(request_id="missing-cost", metric="cost"))


def test_malformed_delegated_history_and_comparison_are_rejected(history) -> None:
    bad_history = replace(ToolServices(), history=lambda: [{"fake": "history"}])
    assert_failure(FailureCode.INVALID_OUTPUT, AgentTools(bad_history).get_historical_quotes,
                   HistoricalQuotesInput(request_id="x"))
    bad_comparisons = replace(ToolServices(), comparisons=lambda _records: ("fake",))
    assert_failure(FailureCode.INVALID_OUTPUT, AgentTools(bad_comparisons).compare_estimate_to_actual,
                   ComparisonsInput(request_id="x"))
    forged = replace(compare_historical_quotes(history)[0], source_id="invented-source")
    wrong_source = replace(ToolServices(), comparisons=lambda records: (forged, *compare_historical_quotes(records)[1:]))
    assert_failure(FailureCode.INVALID_OUTPUT, AgentTools(wrong_source).compare_estimate_to_actual,
                   ComparisonsInput(request_id="x"))
    plausible_but_unowned = replace(ToolServices(), history=lambda: list(history[:3]))
    assert_failure(FailureCode.INVALID_OUTPUT, AgentTools(plausible_but_unowned).get_historical_quotes,
                   HistoricalQuotesInput(request_id="x"))


def test_malformed_similarity_and_statistics_outputs_are_rejected(history, new_request) -> None:
    fake_match = SimilarQuoteMatch(
        SimilarQuote(quote_id="invented-quote", similarity_score=Decimal("1"), matching_features=["x"]),
        "invented-source", history[0].data_origin,
    )
    tools = AgentTools(replace(ToolServices(), similarity=lambda *_args, **_kw: (fake_match,)))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.find_similar_quotes,
                   SimilarQuotesInput(request_id="x", request=new_request))
    tools = AgentTools(replace(ToolServices(), statistics=lambda _values: {"average": 99}))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.calculate_quote_statistics,
                   StatisticsInput(request_id="x"))


def test_fabricated_risk_evidence_and_counts_are_rejected(history) -> None:
    valid = build_risk_evidence(history)
    invented = RiskEvidence(
        evidence_id="invented", source_quote_ids=["invented-quote"], metric="overrun_rate",
        observed_value=Decimal("1"), unit="ratio", data_origin=history[0].data_origin,
    )
    forged = replace(valid, evidence=(invented,))
    tools = AgentTools(replace(ToolServices(), risk_evidence=lambda *_args, **_kw: forged))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.get_risk_evidence,
                   RiskEvidenceInput(request_id="x"))
    forged_count = replace(valid, comparable_project_count=999)
    tools = AgentTools(replace(ToolServices(), risk_evidence=lambda *_args, **_kw: forged_count))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.get_risk_evidence,
                   RiskEvidenceInput(request_id="x"))


def test_non_success_risk_result_does_not_become_success(history) -> None:
    invalid = replace(build_risk_evidence(history), status=AgentResultStatus.INVALID)
    tools = AgentTools(replace(ToolServices(), risk_evidence=lambda *_args, **_kw: invalid))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.get_risk_evidence,
                   RiskEvidenceInput(request_id="x"))


def test_plausible_numeric_overrides_from_delegates_are_not_authoritative(history, new_request) -> None:
    original = compare_historical_quotes(history)
    forged_variance = original[0].hour_variance.model_copy(update={"variance": Decimal("999")})
    forged_comparison = replace(original[0], hour_variance=forged_variance)
    tools = AgentTools(replace(ToolServices(), comparisons=lambda _records: (forged_comparison, *original[1:])))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.compare_estimate_to_actual,
                   ComparisonsInput(request_id="x"))

    valid_match = retrieve_similar_quotes(new_request, history, limit=1)[0]
    forged_match = replace(valid_match, result=valid_match.result.model_copy(
        update={"similarity_score": Decimal("0.99")},
    ))
    tools = AgentTools(replace(ToolServices(), similarity=lambda *_args, **_kw: (forged_match,)))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.find_similar_quotes,
                   SimilarQuotesInput(request_id="x", request=new_request, limit=1))

    valid_risk = build_risk_evidence(history)
    forged_evidence = valid_risk.evidence[0].model_copy(update={"observed_value": Decimal("0.99")})
    tools = AgentTools(replace(ToolServices(), risk_evidence=lambda *_args, **_kw: replace(
        valid_risk, evidence=(forged_evidence, *valid_risk.evidence[1:]),
    )))
    assert_failure(FailureCode.INVALID_OUTPUT, tools.get_risk_evidence,
                   RiskEvidenceInput(request_id="x"))


def test_caller_cannot_supply_altered_historical_outcomes(history) -> None:
    altered = history[0].model_copy(update={"outcome": history[0].outcome.model_copy(
        update={"actual_hours": history[0].outcome.actual_hours.model_copy(update={"value": Decimal("999")})},
    )})
    assert_failure(FailureCode.INVALID_INPUT, AgentTools().get_risk_evidence,
                   {"request_id": "fabricated", "history": (altered,)})
    for model in (SimilarQuotesInput, ComparisonsInput, StatisticsInput, RiskEvidenceInput):
        assert "history" not in model.model_fields


def test_delegation_uses_owners_and_preserves_exact_numeric_values(history) -> None:
    calls: list[str] = []

    def comparisons(records):
        calls.append("comparison")
        return compare_historical_quotes(records)

    def statistics(values):
        calls.append("statistics")
        return summarize_variances(values)

    def risk(records, *, metric):
        calls.append("risk")
        return build_risk_evidence(records, metric=metric)

    tools = AgentTools(replace(ToolServices(), comparisons=comparisons, statistics=statistics, risk_evidence=risk))
    result = tools.calculate_quote_statistics(StatisticsInput(request_id="x"))
    risk_result = tools.get_risk_evidence(RiskEvidenceInput(request_id="x"))
    assert calls == ["comparison", "statistics", "risk"]
    assert result.summary.average_variance == summarize_variances(
        tuple(item.hour_variance for item in compare_historical_quotes(history))
    ).average_variance
    assert risk_result.report.overrun_rate == build_risk_evidence(history).overrun_rate
    assert not hasattr(tools, "approve_quote")
    assert not hasattr(tools, "generate_excel")
