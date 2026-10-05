"""Provider-isolated Amazon Bedrock Converse integration for V1-C08."""

from dataclasses import dataclass
from time import monotonic_ns
from typing import Any, Protocol

import boto3
from botocore.config import Config

from ai_quotation_intelligence.config import Settings, load_settings
from ai_quotation_intelligence.domain import AgentResultStatus
from ai_quotation_intelligence.logging_config import emit_event


class ConverseClient(Protocol):
    def converse(self, **kwargs: Any) -> dict[str, Any]: ...


@dataclass(frozen=True)
class TokenUsage:
    input_tokens: int | None = None
    output_tokens: int | None = None
    total_tokens: int | None = None


@dataclass(frozen=True)
class BedrockResult:
    """Application-level result; raw provider payloads do not escape the adapter."""

    status: AgentResultStatus
    text: str | None
    request_id: str
    usage: TokenUsage | None = None
    message: str | None = None


def build_converse_request(prompt: str, settings: Settings | None = None) -> dict[str, Any]:
    """Build a deterministic Converse request without credentials or provider state."""

    resolved = settings or load_settings()
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("prompt must be non-empty")
    return {
        "modelId": resolved.bedrock_model_id,
        "messages": [
            {"role": "user", "content": [{"text": prompt}]},
        ],
        "inferenceConfig": {
            "maxTokens": resolved.bedrock_max_tokens,
            "temperature": resolved.bedrock_temperature,
        },
    }


def _extract_response(response: object, request_id: str) -> BedrockResult:
    if not isinstance(response, dict):
        return BedrockResult(AgentResultStatus.INVALID, None, request_id, message="response must be an object")
    output = response.get("output")
    message = output.get("message") if isinstance(output, dict) else None
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, list) or not content:
        return BedrockResult(AgentResultStatus.INVALID, None, request_id, message="response content is missing")
    text_parts = [item.get("text") for item in content if isinstance(item, dict) and isinstance(item.get("text"), str)]
    text = "".join(text_parts).strip()
    if not text:
        return BedrockResult(AgentResultStatus.INVALID, None, request_id, message="response text is empty")
    usage_data = response.get("usage")
    usage = None
    if isinstance(usage_data, dict):
        usage = TokenUsage(
            input_tokens=usage_data.get("inputTokens"),
            output_tokens=usage_data.get("outputTokens"),
            total_tokens=usage_data.get("totalTokens"),
        )
    return BedrockResult(AgentResultStatus.SUCCESS, text, request_id, usage=usage)


class BedrockConverseAdapter:
    """Small, injectable adapter around the Bedrock Runtime Converse API."""

    def __init__(self, settings: Settings | None = None, client: ConverseClient | None = None) -> None:
        self.settings = settings or load_settings()
        self._client = client

    def _provider_client(self) -> ConverseClient:
        if self._client is None:
            self._client = boto3.client(
                "bedrock-runtime",
                region_name=self.settings.aws_region,
                config=Config(
                    connect_timeout=self.settings.bedrock_connect_timeout,
                    read_timeout=self.settings.bedrock_read_timeout,
                    retries={"mode": "standard", "max_attempts": self.settings.bedrock_max_attempts},
                ),
            )
        return self._client

    def invoke(self, prompt: str, *, request_id: str = "bedrock-request") -> BedrockResult:
        """Invoke Converse and translate provider/response failures explicitly."""

        started = monotonic_ns()
        try:
            result = self._invoke(prompt, request_id=request_id)
        except Exception:
            emit_event("bedrock_call", component="bedrock", operation="converse",
                       status="failure", request_id=request_id,
                       duration_ms=(monotonic_ns() - started) // 1_000_000,
                       sanitized_error="unexpected_error")
            raise
        usage = result.usage
        emit_event("bedrock_call", component="bedrock", operation="converse",
                   status=result.status.value, request_id=request_id,
                   duration_ms=(monotonic_ns() - started) // 1_000_000,
                   input_tokens=usage.input_tokens if usage else None,
                   output_tokens=usage.output_tokens if usage else None,
                   sanitized_error="provider_unavailable" if result.status is AgentResultStatus.UNAVAILABLE
                   else "invalid_provider_response" if result.status is AgentResultStatus.INVALID else None)
        return result

    def _invoke(self, prompt: str, *, request_id: str) -> BedrockResult:

        try:
            request = build_converse_request(prompt, self.settings)
        except ValueError as exc:
            return BedrockResult(AgentResultStatus.INVALID, None, request_id, message=str(exc))
        try:
            response = self._provider_client().converse(**request)
        except Exception as exc:  # provider SDK errors are intentionally bounded at this boundary
            return BedrockResult(
                AgentResultStatus.UNAVAILABLE,
                None,
                request_id,
                message=f"provider invocation failed: {type(exc).__name__}",
            )
        return _extract_response(response, request_id)


__all__ = [
    "BedrockConverseAdapter",
    "BedrockResult",
    "ConverseClient",
    "TokenUsage",
    "build_converse_request",
]
