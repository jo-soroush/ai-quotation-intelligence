from datetime import datetime, timezone

import pytest

from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import DataOrigin, HistoricalQuote, NewQuoteRequest
from ai_quotation_intelligence.retrieval import retrieve_similar_quotes


def request_for(record: HistoricalQuote, *, project_name: str | None = None) -> NewQuoteRequest:
    return NewQuoteRequest(
        project_name=project_name or record.quote.project_name,
        currency=record.quote.currency,
        items=record.quote.items,
        requested_at=datetime(2026, 9, 16, tzinfo=timezone.utc),
    )


def test_more_similar_quote_ranks_ahead_with_explanation() -> None:
    history = generate_synthetic_history()
    results = retrieve_similar_quotes(
        request_for(history[0]),
        (history[1], history[0]),
        limit=2,
    )
    assert [match.result.quote_id for match in results] == [history[0].quote.quote_id, history[1].quote.quote_id]
    assert results[0].result.similarity_score > results[1].result.similarity_score
    assert "project_name_tokens" in results[0].result.matching_features
    assert results[0].source_id == history[0].source_id


def test_ties_are_sorted_by_quote_id_deterministically() -> None:
    history = generate_synthetic_history()
    first = history[0].model_copy(update={
        "quote": history[0].quote.model_copy(update={"quote_id": "tie-b"}),
        "source_id": "tie-source-b",
    })
    second = history[0].model_copy(update={
        "quote": history[0].quote.model_copy(update={"quote_id": "tie-a"}),
        "source_id": "tie-source-a",
    })
    results = retrieve_similar_quotes(request_for(history[0]), (first, second))
    assert [match.result.quote_id for match in results] == ["tie-a", "tie-b"]
    assert results == retrieve_similar_quotes(request_for(history[0]), (first, second))


def test_limit_zero_empty_history_and_small_history_are_deterministic() -> None:
    history = generate_synthetic_history()
    request = request_for(history[0])
    assert retrieve_similar_quotes(request, history, limit=0) == ()
    assert retrieve_similar_quotes(request, (), limit=5) == ()
    assert len(retrieve_similar_quotes(request, history[:1], limit=5)) == 1


def test_negative_limit_is_rejected() -> None:
    history = generate_synthetic_history()
    with pytest.raises(ValueError, match="non-negative"):
        retrieve_similar_quotes(request_for(history[0]), history, limit=-1)


def test_incompatible_currency_is_rejected_without_conversion() -> None:
    history = generate_synthetic_history()
    request = request_for(history[0]).model_copy(update={"currency": "EUR"})
    with pytest.raises(ValueError, match="matching quote currencies"):
        retrieve_similar_quotes(request, history[:1])


def test_c03_history_is_consumed_without_mutation_and_keeps_synthetic_provenance() -> None:
    history = generate_synthetic_history()
    before = tuple(record.model_dump(mode="json") for record in history)
    results = retrieve_similar_quotes(request_for(history[0]), history, limit=40)
    assert len(results) == 40
    assert all(match.data_origin is DataOrigin.SYNTHETIC for match in results)
    assert all(match.result.quote_id.startswith("synthetic-c03-quote-") for match in results)
    assert before == tuple(record.model_dump(mode="json") for record in history)


def test_similarity_returns_context_not_commercial_values() -> None:
    history = generate_synthetic_history()
    result = retrieve_similar_quotes(request_for(history[0]), history[:1])[0].result
    assert result.quote_id == history[0].quote.quote_id
    assert result.matching_features
    assert not hasattr(result, "estimated_total_cost")
    assert not hasattr(result, "actual_total_cost")


def test_result_identity_and_provenance_are_stable_across_repeated_runs() -> None:
    history = generate_synthetic_history()
    request = request_for(history[5], project_name="Cloud Platform")
    first = retrieve_similar_quotes(request, history, limit=3)
    second = retrieve_similar_quotes(request, history, limit=3)
    assert [(item.result.quote_id, item.source_id, item.data_origin) for item in first] == [
        (item.result.quote_id, item.source_id, item.data_origin) for item in second
    ]
