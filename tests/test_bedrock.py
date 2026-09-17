from ai_quotation_intelligence.bedrock import (
    BedrockConverseAdapter,
    BedrockResult,
    TokenUsage,
    build_converse_request,
)
from ai_quotation_intelligence.config import Settings, load_settings
from ai_quotation_intelligence.domain import AgentResultStatus


class FakeClient:
    def __init__(self, response=None, error=None):
        self.response = response
        self.error = error
        self.calls = []

    def converse(self, **kwargs):
        self.calls.append(kwargs)
        if self.error is not None:
            raise self.error
        return self.response


def settings() -> Settings:
    return Settings(
        aws_region="eu-north-1",
        bedrock_model_id="test-model",
        bedrock_max_tokens=12,
        bedrock_temperature=0.0,
    )


def test_request_construction_is_typed_and_repeatable() -> None:
    first = build_converse_request("hello", settings())
    second = build_converse_request("hello", settings())

    assert first == second
    assert first == {
        "modelId": "test-model",
        "messages": [{"role": "user", "content": [{"text": "hello"}]}],
        "inferenceConfig": {"maxTokens": 12, "temperature": 0.0},
    }


def test_valid_response_is_extracted_without_raw_payload() -> None:
    client = FakeClient(
        {
            "output": {"message": {"content": [{"text": "BEDROCK_C08_OK"}]}},
            "usage": {"inputTokens": 2, "outputTokens": 1, "totalTokens": 3},
        }
    )

    result = BedrockConverseAdapter(settings(), client).invoke("hello", request_id="r-1")

    assert isinstance(result, BedrockResult)
    assert result.status is AgentResultStatus.SUCCESS
    assert result.text == "BEDROCK_C08_OK"
    assert result.usage == TokenUsage(2, 1, 3)


def test_missing_or_empty_response_is_invalid() -> None:
    for response in ({}, {"output": {}}, {"output": {"message": {"content": []}}}):
        result = BedrockConverseAdapter(settings(), FakeClient(response)).invoke("hello")
        assert result.status is AgentResultStatus.INVALID
        assert result.text is None


def test_wrong_content_type_is_invalid() -> None:
    response = {"output": {"message": {"content": [{"image": "not-text"}]}}}

    result = BedrockConverseAdapter(settings(), FakeClient(response)).invoke("hello")

    assert result.status is AgentResultStatus.INVALID


def test_provider_failure_is_unavailable_without_secret_details() -> None:
    result = BedrockConverseAdapter(settings(), FakeClient(error=RuntimeError("secret-value"))).invoke("hello")

    assert result.status is AgentResultStatus.UNAVAILABLE
    assert result.text is None
    assert "secret-value" not in (result.message or "")


def test_empty_prompt_is_invalid_without_provider_call() -> None:
    client = FakeClient({})

    result = BedrockConverseAdapter(settings(), client).invoke("   ")

    assert result.status is AgentResultStatus.INVALID
    assert client.calls == []


def test_adapter_passes_configured_model_and_never_credentials() -> None:
    client = FakeClient({"output": {"message": {"content": [{"text": "ok"}]}}})
    adapter = BedrockConverseAdapter(settings(), client)

    adapter.invoke("hello")

    assert client.calls[0]["modelId"] == "test-model"
    assert "aws_access_key_id" not in client.calls[0]
    assert "aws_secret_access_key" not in client.calls[0]


def test_load_settings_reads_provider_configuration(monkeypatch) -> None:
    monkeypatch.setenv("AQI_AWS_REGION", "us-east-1")
    monkeypatch.setenv("AQI_BEDROCK_MODEL_ID", "amazon.nova-micro-v1:0")

    loaded = load_settings()

    assert loaded.aws_region == "us-east-1"
    assert loaded.bedrock_model_id == "amazon.nova-micro-v1:0"


def test_provider_client_uses_bounded_timeout_and_retry_configuration(monkeypatch) -> None:
    captured = {}

    def fake_client(service_name, **kwargs):
        captured["service_name"] = service_name
        captured.update(kwargs)
        return FakeClient({})

    monkeypatch.setattr("ai_quotation_intelligence.bedrock.boto3.client", fake_client)
    configured = Settings(
        aws_region="eu-north-1",
        bedrock_connect_timeout=3,
        bedrock_read_timeout=7,
        bedrock_max_attempts=2,
    )

    BedrockConverseAdapter(configured)._provider_client()

    assert captured["service_name"] == "bedrock-runtime"
    assert captured["region_name"] == "eu-north-1"
    assert captured["config"].connect_timeout == 3
    assert captured["config"].read_timeout == 7
    assert captured["config"].retries["max_attempts"] == 2
