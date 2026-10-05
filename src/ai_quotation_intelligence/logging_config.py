"""C16 bounded JSON operational events; never a business-authority channel."""

from contextvars import ContextVar, Token
import json
import logging
import re
import sys


_LOGGER = logging.getLogger("ai_quotation_intelligence")
_REQUEST_ID: ContextVar[str | None] = ContextVar("aqi_request_id", default=None)
_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}\Z")
_QUOTATION_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,127}\Z")
_EVENTS = frozenset({"api_request", "quotation_analyzed", "quotation_drafted",
                     "agent_run_started", "agent_run_finished", "tool_call",
                     "bedrock_call", "storage_operation"})
_COMPONENTS = frozenset({"api", "agent", "agent_tool", "bedrock", "s3_storage"})
_OPERATIONS = frozenset({"health", "analyze", "draft", "get_quote", "decide", "export",
                         "unmatched", "run", "get_historical_quotes", "find_similar_quotes",
                         "compare_estimate_to_actual", "calculate_quote_statistics",
                         "get_risk_evidence", "converse", "persist", "retrieve"})
_STATUSES = frozenset({"started", "success", "failure", "invalid", "unavailable",
                       "insufficient_evidence"})
_ERRORS = frozenset({"http_error", "unexpected_error", "provider_unavailable",
                     "invalid_provider_response", "invalid_input", "invalid_output",
                     "unavailable", "insufficient_evidence", "unsupported_operation",
                     "service_failure", "configuration_missing", "duplicate", "not_found",
                     "access_denied", "conflict", "provider_invalid", "integrity_mismatch",
                     "storage_failed"})
_OPTIONAL_FIELDS = frozenset({"request_id", "quotation_id", "duration_ms", "http_status",
                              "input_tokens", "output_tokens", "sanitized_error"})


def _safe_event(data: object) -> bool:
    if type(data) is not dict or not {"event", "component", "operation", "status"} <= data.keys():
        return False
    if not data.keys() <= {"event", "component", "operation", "status"} | _OPTIONAL_FIELDS:
        return False
    if (type(data["event"]) is not str or data["event"] not in _EVENTS
            or type(data["component"]) is not str or data["component"] not in _COMPONENTS
            or type(data["operation"]) is not str or data["operation"] not in _OPERATIONS
            or type(data["status"]) is not str or data["status"] not in _STATUSES):
        return False
    for key, pattern in (("request_id", _IDENTIFIER), ("quotation_id", _QUOTATION_IDENTIFIER)):
        if key in data and (type(data[key]) is not str or not pattern.fullmatch(data[key])):
            return False
    for key in ("duration_ms", "http_status", "input_tokens", "output_tokens"):
        if key in data and (type(data[key]) is not int or not 0 <= data[key] <= 1_000_000_000):
            return False
    return "sanitized_error" not in data or (
        type(data["sanitized_error"]) is str and data["sanitized_error"] in _ERRORS)


class _JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        data = getattr(record, "aqi_event", None)
        if not _safe_event(data):
            data = {"event": "unstructured_suppressed", "component": "logging",
                    "operation": "format", "status": "failure"}
        return json.dumps(data, separators=(",", ":"), sort_keys=True)


def configure_logging(level: str = "INFO") -> logging.Logger:
    """Install one stdout handler; no AWS client or CloudWatch SDK is involved."""
    _LOGGER.setLevel(getattr(logging, level.upper(), logging.INFO))
    structured = next((handler for handler in _LOGGER.handlers
                       if getattr(handler, "_aqi_structured", False)), None)
    if structured is None:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(_JsonFormatter())
        handler._aqi_structured = True
        _LOGGER.addHandler(handler)
    else:
        structured.stream = sys.stdout
    _LOGGER.propagate = False
    return _LOGGER


def begin_request(request_id: str) -> Token[str | None]:
    """Set an HTTP-request-scoped identifier, reset by the caller in finally."""
    if not _IDENTIFIER.fullmatch(request_id):
        raise ValueError("invalid operational request identifier")
    return _REQUEST_ID.set(request_id)


def end_request(token: Token[str | None]) -> None:
    _REQUEST_ID.reset(token)


def _identifier(value: object) -> str | None:
    return value if type(value) is str and _IDENTIFIER.fullmatch(value) else None


def emit_event(
    event: str, *, component: str, operation: str, status: str,
    request_id: str | None = None, quotation_id: str | None = None,
    duration_ms: int | None = None, http_status: int | None = None,
    input_tokens: int | None = None, output_tokens: int | None = None,
    sanitized_error: str | None = None,
) -> None:
    """Allowlist metadata. Invalid/untrusted values are omitted, never stringified."""
    if (type(event) is not str or type(component) is not str
            or type(operation) is not str or type(status) is not str
            or event not in _EVENTS or component not in _COMPONENTS
            or operation not in _OPERATIONS or status not in _STATUSES):
        return
    data: dict[str, str | int] = {"event": event, "component": component,
                                  "operation": operation, "status": status}
    request = _REQUEST_ID.get() or _identifier(request_id)
    if request is not None:
        data["request_id"] = request
    quote = quotation_id if type(quotation_id) is str and _QUOTATION_IDENTIFIER.fullmatch(quotation_id) else None
    if quote is not None:
        data["quotation_id"] = quote
    for key, value in (("duration_ms", duration_ms), ("http_status", http_status),
                       ("input_tokens", input_tokens), ("output_tokens", output_tokens)):
        if type(value) is int and 0 <= value <= 1_000_000_000:
            data[key] = value
    if type(sanitized_error) is str and sanitized_error in _ERRORS:
        data["sanitized_error"] = sanitized_error
    try:
        configure_logging()
        _LOGGER.info("operational_event", extra={"aqi_event": data})
    except Exception:
        # Observability must not change quotation or provider semantics.
        pass


__all__ = ["configure_logging", "begin_request", "end_request", "emit_event"]
