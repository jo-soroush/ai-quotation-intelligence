"""C13 process-local HTTP adapter for the delivered C10–C12 boundaries.

The injected agent owns analysis. A held C11 session owns review authority;
C12 alone renders export bytes. This module has no durable or multi-worker state.
"""

from datetime import datetime
from threading import RLock
from time import monotonic_ns
from typing import Annotated, Literal, Protocol
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, ValidationError

from ai_quotation_intelligence.domain import (
    AgentRequest, AgentResult, AgentResultStatus, ApprovalDecision,
    ApprovalStatus, DraftQuote, Hours, Money, NewQuoteRequest, QuoteItem, TimeUnit,
)
from ai_quotation_intelligence.excel_export import ExportFailure, ExportFailureCode, export_approved_quote
from ai_quotation_intelligence.human_review import ReviewFailure, ReviewFailureCode, ReviewSession
from ai_quotation_intelligence.logging_config import begin_request, emit_event, end_request


SafeId = Annotated[str, StringConstraints(pattern=r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$")]
ShortText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]
LongText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=2000)]
XLSX_MIME = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
MAX_SESSIONS = 128
MAX_REQUEST_BYTES = 65536


class TransportModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class RequestHours(Hours):
    """Public request time value; callers must state its unit explicitly."""

    unit: TimeUnit


class ItemInput(TransportModel):
    item_id: SafeId
    description: ShortText
    estimated_hours: RequestHours
    hourly_rate: Money


class QuotationInput(TransportModel):
    project_name: ShortText
    currency: str
    items: list[ItemInput] = Field(min_length=1, max_length=40)
    requested_at: datetime


class AgentInput(TransportModel):
    request_id: SafeId
    quotation_request: QuotationInput
    instructions: LongText | None = None


class DecisionInput(TransportModel):
    status: Literal[ApprovalStatus.APPROVED, ApprovalStatus.REJECTED]
    reviewer_id: ShortText
    reason: LongText | None = None
    decided_at: datetime | None = None


class AgentView(TransportModel):
    request_id: str
    status: AgentResultStatus
    quote_id: str | None = None
    message: str | None = None


class QuoteView(TransportModel):
    quote_id: str
    request_id: str
    status: AgentResultStatus
    review_state: str
    draft_quote: DraftQuote


class DecisionView(TransportModel):
    quote_id: str
    review_state: str
    reviewer_id: str


class HealthView(TransportModel):
    status: Literal["ok"] = "ok"


class AgentRunner(Protocol):
    def run(self, value: object) -> AgentResult: ...


class ApiFailure(Exception):
    def __init__(self, status: int, code: str) -> None:
        self.status = status
        self.code = code
        super().__init__(code)


class LocalQuoteStore:
    """Bounded, single-process association; never an approval authority."""

    def __init__(self, limit: int = MAX_SESSIONS) -> None:
        if limit < 1:
            raise ValueError("store limit must be positive")
        self._limit = limit
        self._lock = RLock()
        self._entries: dict[str, tuple[AgentResult, ReviewSession]] = {}

    def add(self, result: AgentResult, session: ReviewSession) -> str:
        draft = result.draft_quote
        if draft is None:
            raise ApiFailure(422, "invalid_agent_result")
        quote_id = draft.quote.quote_id
        with self._lock:
            if quote_id in self._entries:
                raise ApiFailure(409, "quote_exists")
            if len(self._entries) >= self._limit:
                raise ApiFailure(503, "session_capacity")
            self._entries[quote_id] = (result.model_copy(deep=True), session)
        return quote_id

    def current(self, quote_id: str) -> tuple[AgentResult, ReviewSession]:
        try:
            return self._entries[quote_id]
        except KeyError:
            raise ApiFailure(404, "quote_not_found") from None


def _domain_request(value: AgentInput) -> AgentRequest:
    request = value.quotation_request
    return AgentRequest(
        request_id=value.request_id,
        quotation_request=NewQuoteRequest(
            project_name=request.project_name,
            currency=request.currency,
            items=[QuoteItem(**item.model_dump()) for item in request.items],
            requested_at=request.requested_at,
        ),
        instructions=value.instructions,
    )


def _agent_result(agent: AgentRunner, value: AgentInput) -> AgentResult:
    try:
        request = _domain_request(value)
    except ValidationError:
        raise ApiFailure(422, "invalid_request") from None
    try:
        result = agent.run(request)
    except Exception:
        raise ApiFailure(503, "agent_unavailable") from None
    if type(result) is not AgentResult:
        raise ApiFailure(500, "invalid_agent_result")
    try:
        clean = AgentResult.model_validate_json(result.model_dump_json())
    except Exception:
        raise ApiFailure(500, "invalid_agent_result") from None
    if clean.request_id != request.request_id:
        raise ApiFailure(500, "invalid_agent_result")
    if clean.status is AgentResultStatus.INVALID:
        raise ApiFailure(422, "agent_invalid")
    if clean.status is AgentResultStatus.UNAVAILABLE:
        raise ApiFailure(503, "agent_unavailable")
    if clean.status is AgentResultStatus.INSUFFICIENT_EVIDENCE:
        raise ApiFailure(422, "insufficient_evidence")
    if clean.status is not AgentResultStatus.SUCCESS:
        raise ApiFailure(500, "invalid_agent_result")
    return clean


def _session(result: AgentResult) -> ReviewSession:
    try:
        return ReviewSession(result)
    except ReviewFailure:
        raise ApiFailure(422, "invalid_agent_result") from None


def _review_failure(exc: ReviewFailure) -> ApiFailure:
    if exc.code is ReviewFailureCode.STALE_DRAFT:
        return ApiFailure(409, "stale_review")
    if exc.code is ReviewFailureCode.INVALID_TRANSITION:
        return ApiFailure(409, "invalid_transition")
    if exc.code is ReviewFailureCode.APPROVAL_REQUIRED:
        return ApiFailure(409, "approval_required")
    return ApiFailure(422, "invalid_review")


def _export_failure(exc: ExportFailure) -> ApiFailure:
    if exc.code is ExportFailureCode.APPROVAL_REQUIRED:
        return ApiFailure(409, "approval_required")
    if exc.code is ExportFailureCode.STALE_RESULT:
        return ApiFailure(409, "stale_review")
    if exc.code in {ExportFailureCode.COMMERCIAL_MISMATCH, ExportFailureCode.EVIDENCE_MISMATCH}:
        return ApiFailure(409, "export_reconciliation_failed")
    return ApiFailure(500, "export_failed")


def create_app(agent: AgentRunner, *, store: LocalQuoteStore | None = None) -> FastAPI:
    """Compose one process-local API with an injected existing C10 runner."""
    sessions = store if store is not None else LocalQuoteStore()
    app = FastAPI(debug=False)

    @app.exception_handler(RequestValidationError)
    async def invalid_http(_: Request, __: RequestValidationError) -> JSONResponse:
        return JSONResponse(status_code=422, content={"code": "invalid_request"})

    @app.exception_handler(ApiFailure)
    async def known_failure(_: Request, exc: ApiFailure) -> JSONResponse:
        return JSONResponse(status_code=exc.status, content={"code": exc.code})

    @app.exception_handler(Exception)
    async def unknown_failure(_: Request, __: Exception) -> JSONResponse:
        return JSONResponse(status_code=500, content={"code": "internal_error"})

    @app.middleware("http")
    async def limit_request_size(request: Request, call_next):
        token = begin_request(uuid4().hex)
        started = monotonic_ns()
        status = 500
        try:
            if request.method == "POST":
                length = request.headers.get("content-length")
                if length is not None and (not length.isdecimal() or int(length) > MAX_REQUEST_BYTES):
                    status = 413
                    return JSONResponse(status_code=413, content={"code": "request_too_large"})
                chunks = bytearray()
                async for chunk in request.stream():
                    if len(chunks) + len(chunk) > MAX_REQUEST_BYTES:
                        status = 413
                        return JSONResponse(status_code=413, content={"code": "request_too_large"})
                    chunks.extend(chunk)
                # Starlette's cached request replays the bounded body to FastAPI.
                request._body = bytes(chunks)
            response = await call_next(request)
            status = response.status_code
            return response
        finally:
            route = request.scope.get("route")
            operation = getattr(route, "name", None)
            if operation not in {"health", "analyze", "draft", "get_quote", "decide", "export"}:
                operation = "unmatched"
            params = request.scope.get("path_params") or {}
            emit_event("api_request", component="api", operation=operation,
                       status="success" if status < 400 else "failure",
                       quotation_id=params.get("id"), http_status=status,
                       duration_ms=(monotonic_ns() - started) // 1_000_000,
                       sanitized_error="http_error" if status >= 400 else None)
            end_request(token)

    @app.get("/health", response_model=HealthView)
    def health() -> HealthView:
        return HealthView()

    @app.post("/quotes/analyze", response_model=AgentView)
    def analyze(value: AgentInput) -> AgentView:
        result = _agent_result(agent, value)
        _session(result)  # C11's validation protects even non-persisted analysis.
        emit_event("quotation_analyzed", component="api", operation="analyze",
                   status="success", quotation_id=result.draft_quote.quote.quote_id)
        return AgentView(request_id=result.request_id, status=result.status,
                         quote_id=result.draft_quote.quote.quote_id, message=result.message)

    @app.post("/quotes/draft", response_model=AgentView)
    def draft(value: AgentInput) -> AgentView:
        result = _agent_result(agent, value)
        session = _session(result)
        quote_id = sessions.add(result, session)
        emit_event("quotation_drafted", component="api", operation="draft",
                   status="success", quotation_id=quote_id)
        return AgentView(request_id=result.request_id, status=result.status,
                         quote_id=quote_id, message=result.message)

    @app.get("/quotes/{id}", response_model=QuoteView)
    def get_quote(id: SafeId) -> QuoteView:
        with sessions._lock:
            current, session = sessions.current(id)
            return QuoteView(quote_id=id, request_id=current.request_id,
                             status=current.status, review_state=session.state.value,
                             draft_quote=current.draft_quote.model_copy(deep=True))

    @app.post("/quotes/{id}/approve", response_model=DecisionView)
    def decide(id: SafeId, value: DecisionInput) -> DecisionView:
        with sessions._lock:
            current, session = sessions.current(id)
            try:
                decision = ApprovalDecision(quote_id=id, status=value.status,
                                            reviewer_id=value.reviewer_id,
                                            reason=value.reason, decided_at=value.decided_at)
                record = session.decide(decision, current=current)
            except ValidationError:
                raise ApiFailure(422, "invalid_decision") from None
            except ReviewFailure as exc:
                raise _review_failure(exc) from None
            return DecisionView(quote_id=id, review_state=session.state.value,
                                reviewer_id=record.decision.reviewer_id)

    @app.post("/quotes/{id}/export")
    def export(id: SafeId) -> Response:
        with sessions._lock:
            current, session = sessions.current(id)
            try:
                blob = export_approved_quote(session, current=current)
            except ExportFailure as exc:
                raise _export_failure(exc) from None
            return Response(content=blob, media_type=XLSX_MIME,
                            headers={"Content-Disposition": 'attachment; filename="Draft_Quote.xlsx"'})

    return app


__all__ = ["AgentInput", "AgentRunner", "LocalQuoteStore", "create_app"]
