"""Deterministic, explainable similar-quotation retrieval for V1-C06."""

from dataclasses import dataclass
from decimal import Decimal
import re
from typing import Iterable

from ai_quotation_intelligence.domain import (
    DataOrigin,
    HistoricalQuote,
    NewQuoteRequest,
    Quote,
    SimilarQuote,
)


@dataclass(frozen=True)
class SimilarQuoteMatch:
    """A SimilarQuote result with the source identity and provenance retained."""

    result: SimilarQuote
    source_id: str
    data_origin: DataOrigin


def _tokens(value: str) -> frozenset[str]:
    return frozenset(re.findall(r"[a-z0-9]+", value.lower()))


def _request_features(request: Quote | NewQuoteRequest) -> tuple[frozenset[str], frozenset[str], int]:
    return (
        _tokens(request.project_name),
        frozenset(
            token
            for item in request.items
            for token in _tokens(item.description)
        ),
        len(request.items),
    )


def _candidate_features(record: HistoricalQuote) -> tuple[frozenset[str], frozenset[str], int]:
    return _request_features(record.quote)


def _jaccard(left: frozenset[str], right: frozenset[str]) -> Decimal:
    union = left | right
    return Decimal("0") if not union else Decimal(len(left & right)) / Decimal(len(union))


def _score(
    request_features: tuple[frozenset[str], frozenset[str], int],
    candidate_features: tuple[frozenset[str], frozenset[str], int],
) -> tuple[Decimal, list[str]]:
    request_project, request_work, request_count = request_features
    candidate_project, candidate_work, candidate_count = candidate_features
    score = (
        Decimal("0.5") * _jaccard(request_project, candidate_project)
        + Decimal("0.4") * _jaccard(request_work, candidate_work)
        + Decimal("0.1") * Decimal(request_count == candidate_count)
    )
    matching_features: list[str] = []
    if request_project & candidate_project:
        matching_features.append("project_name_tokens")
    if request_work & candidate_work:
        matching_features.append("work_item_tokens")
    if request_count == candidate_count:
        matching_features.append("item_count")
    if not matching_features:
        matching_features.append("no_exact_feature_match")
    return score, matching_features


def retrieve_similar_quotes(
    request: Quote | NewQuoteRequest,
    history: Iterable[HistoricalQuote],
    *,
    limit: int = 5,
) -> tuple[SimilarQuoteMatch, ...]:
    """Return stable, ranked historical references without copying commercial values."""

    if limit < 0:
        raise ValueError("limit must be non-negative")
    if limit == 0:
        return ()

    request_features = _request_features(request)
    matches: list[SimilarQuoteMatch] = []
    for record in history:
        if record.quote.currency != request.currency:
            raise ValueError("similarity requires matching quote currencies")
        score, matching_features = _score(request_features, _candidate_features(record))
        matches.append(
            SimilarQuoteMatch(
                result=SimilarQuote(
                    quote_id=record.quote.quote_id,
                    similarity_score=score,
                    matching_features=matching_features,
                ),
                source_id=record.source_id,
                data_origin=record.data_origin,
            )
        )
    matches.sort(key=lambda match: (-match.result.similarity_score, match.result.quote_id, match.source_id))
    return tuple(matches[:limit])


__all__ = ["SimilarQuoteMatch", "retrieve_similar_quotes"]
