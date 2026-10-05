"""C16 operational logging contracts, entirely local and provider-isolated."""

from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
import json
import logging
from zipfile import ZipFile

from fastapi.testclient import TestClient
import pytest

from ai_quotation_intelligence.agent_tools import (
    AgentTools, HistoricalQuotesInput, RiskEvidenceInput, ToolFailure, ToolServices,
)
from ai_quotation_intelligence.api import create_app
from ai_quotation_intelligence.bedrock import BedrockConverseAdapter, BedrockResult
from ai_quotation_intelligence.config import Settings
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import AgentRequest, AgentResultStatus, NewQuoteRequest
from ai_quotation_intelligence.logging_config import (
    begin_request, configure_logging, emit_event, end_request,
)
from ai_quotation_intelligence.quotation_agent import QuotationAgent
from ai_quotation_intelligence.s3_storage import S3StorageAdapter
from ai_quotation_intelligence.storage_contract import ArtifactIdentity, StorageFailure, WorkbookArtifact


class EventCapture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.events = []

    def emit(self, record):
        if hasattr(record, "aqi_event"):
            self.events.append(record.aqi_event)


@pytest.fixture
def events():
    logger = configure_logging()
    capture = EventCapture()
    logger.addHandler(capture)
    try:
        yield capture.events
    finally:
        logger.removeHandler(capture)


def _request(request_id="c16-agent"):
    quote = generate_synthetic_history()[0].quote
    return AgentRequest(
        request_id=request_id,
        quotation_request=NewQuoteRequest(project_name=quote.project_name,
                                         currency=quote.currency, items=quote.items,
                                         requested_at=quote.created_at),
    )


def _api_body(request_id="c16-api"):
    request = _request(request_id)
    payload = request.model_dump(mode="json")
    payload["quotation_request"]["items"] = [
        {key: item[key] for key in ("item_id", "description", "estimated_hours", "hourly_rate")}
        for item in payload["quotation_request"]["items"]
    ]
    return payload


class FailingModel:
    def invoke(self, prompt, *, request_id):
        raise RuntimeError("provider-secret free-form prompt customer name")


def test_json_shape_allowlist_and_local_stdout(capsys, events):
    emit_event("api_request", component="api", operation="health", status="success",
               request_id="safe-id", quotation_id="draft-safe", duration_ms=4,
               input_tokens=2, output_tokens=3)
    data = json.loads(capsys.readouterr().out.strip().splitlines()[-1])
    assert data == events[-1]
    assert data == {"event": "api_request", "component": "api", "operation": "health",
                    "status": "success", "request_id": "safe-id", "quotation_id": "draft-safe",
                    "duration_ms": 4, "input_tokens": 2, "output_tokens": 3}


def test_untrusted_metadata_and_unstructured_message_never_escape(capsys, events):
    secret = "AK" + "IA1234567890123456 reviewer_id prompt workbook-bytes"
    emit_event("api_request", component="api", operation="health", status="failure",
               request_id=secret, quotation_id="../secret", sanitized_error=secret,
               duration_ms=-1, input_tokens="99")
    assert events[-1] == {"event": "api_request", "component": "api",
                          "operation": "health", "status": "failure"}
    configure_logging().warning(secret)
    output = capsys.readouterr().out
    assert secret not in output
    assert json.loads(output.strip().splitlines()[-1])["event"] == "unstructured_suppressed"
    with pytest.raises(TypeError):
        emit_event("api_request", component="api", operation="health",
                   status="success", prompt="private prompt")
    emit_event("api_request", component="api", operation="health", status="failure",
               sanitized_error="password")
    assert "sanitized_error" not in events[-1]
    before = len(events)
    emit_event("private_secret", component="api", operation="health", status="failure")
    assert len(events) == before
    configure_logging().warning("bypass attempt", extra={"aqi_event": {
        "event": "api_request", "component": "api", "operation": "health",
        "status": "success", "prompt": secret}})
    bypass_output = capsys.readouterr().out
    assert secret not in bypass_output
    assert json.loads(bypass_output.strip().splitlines()[-1])["event"] == "unstructured_suppressed"


def test_context_reset_and_concurrent_isolation(events):
    def one(value):
        token = begin_request(value)
        try:
            emit_event("api_request", component="api", operation="health", status="success",
                       request_id="fallback")
        finally:
            end_request(token)
    with ThreadPoolExecutor(max_workers=8) as pool:
        list(pool.map(one, [f"req-{index}" for index in range(30)]))
    assert {event["request_id"] for event in events if event["event"] == "api_request"} == {
        f"req-{index}" for index in range(30)}
    emit_event("api_request", component="api", operation="health", status="success",
               request_id="after")
    assert events[-1]["request_id"] == "after"


def test_api_agent_correlation_latency_status_and_no_bodies(events):
    agent = QuotationAgent(FailingModel(), AgentTools())
    client = TestClient(create_app(agent), raise_server_exceptions=False)
    payload = _api_body()
    payload["instructions"] = "private customer request body"
    assert client.get("/health").json() == {"status": "ok"}
    response = client.post("/quotes/analyze", json=payload)
    assert response.status_code == 503
    assert response.json() == {"code": "agent_unavailable"}
    api_events = [item for item in events if item["event"] == "api_request"]
    assert [item["http_status"] for item in api_events] == [200, 503]
    assert all(type(item["duration_ms"]) is int for item in api_events)
    run_events = [item for item in events if item["event"].startswith("agent_run_")]
    assert [item["status"] for item in run_events] == ["started", "unavailable"]
    assert len({item["request_id"] for item in run_events + api_events[1:]}) == 1
    assert api_events[0]["request_id"] != api_events[1]["request_id"]
    encoded = json.dumps(events)
    for forbidden in ("private customer", "provider-secret", "reviewer_id", "workbook-bytes"):
        assert forbidden not in encoded


def test_agent_success_emits_quotation_identifier_without_draft_content(events):
    evidence_id = AgentTools().get_risk_evidence(
        RiskEvidenceInput(request_id="evidence-fixture")).report.evidence[0].evidence_id
    class SuccessfulModel:
        def __init__(self):
            self.calls = 0

        def invoke(self, prompt, *, request_id):
            self.calls += 1
            payload = ({"kind": "tool", "name": "get_risk_evidence", "arguments": {"metric": "hours"}}
                       if self.calls == 1 else
                       {"kind": "final", "narrative": "Draft for human review.",
                        "evidence_ids": [evidence_id], "risk_suggestions": [],
                        "missing_information": []})
            return BedrockResult(AgentResultStatus.SUCCESS, json.dumps(payload), request_id)
    result = QuotationAgent(SuccessfulModel(), AgentTools()).run(_request("agent-success"))
    assert result.status is AgentResultStatus.SUCCESS
    finished = [item for item in events if item["event"] == "agent_run_finished"][-1]
    assert finished["status"] == "success"
    assert finished["quotation_id"] == result.draft_quote.quote.quote_id
    assert "Draft for human review" not in json.dumps(events)


def test_api_quotation_id_is_operational_only(events):
    client = TestClient(create_app(QuotationAgent(FailingModel(), AgentTools())),
                        raise_server_exceptions=False)
    assert client.get("/quotes/draft-safe").status_code == 404
    event = [item for item in events if item["event"] == "api_request"][-1]
    assert event["quotation_id"] == "draft-safe"
    assert event["http_status"] == 404
    assert set(event) <= {"event", "component", "operation", "status", "request_id",
                          "quotation_id", "duration_ms", "http_status", "sanitized_error"}


def test_concurrent_api_requests_never_share_context(events):
    client = TestClient(create_app(QuotationAgent(FailingModel(), AgentTools())),
                        raise_server_exceptions=False)
    with ThreadPoolExecutor(max_workers=8) as pool:
        assert list(pool.map(lambda _: client.get("/health").status_code, range(20))) == [200] * 20
    ids = [item["request_id"] for item in events if item["event"] == "api_request"]
    assert len(ids) == len(set(ids)) == 20


def test_api_reviewer_and_body_are_not_logged(events):
    client = TestClient(create_app(QuotationAgent(FailingModel(), AgentTools())),
                        raise_server_exceptions=False)
    response = client.post("/quotes/not-found/approve", json={
        "status": "approved", "reviewer_id": "private-reviewer", "reason": "private body"})
    assert response.status_code == 404
    assert "private-reviewer" not in json.dumps(events)
    assert "private body" not in json.dumps(events)


def test_tool_success_and_sanitized_failure(events):
    AgentTools().get_historical_quotes(HistoricalQuotesInput(request_id="tool-ok"))
    def broken():
        raise RuntimeError("AWS_SECRET_ACCESS_KEY=do-not-log")
    with pytest.raises(ToolFailure):
        AgentTools(ToolServices(history=broken)).get_historical_quotes(
            HistoricalQuotesInput(request_id="tool-bad"))
    tool_events = [item for item in events if item["event"] == "tool_call"]
    assert [item["status"] for item in tool_events] == ["success", "failure"]
    assert tool_events[1]["sanitized_error"] == "service_failure"
    assert "do-not-log" not in json.dumps(tool_events)


class FakeConverse:
    def __init__(self, response=None, error=None):
        self.response, self.error = response, error

    def converse(self, **kwargs):
        if self.error:
            raise self.error
        return self.response


def test_bedrock_tokens_latency_and_exception_sanitization(events):
    settings = Settings(aws_region="us-east-1", bedrock_model_id="test-model")
    response = {"output": {"message": {"content": [{"text": "raw model response secret"}]}},
                "usage": {"inputTokens": 7, "outputTokens": 5}}
    adapter = BedrockConverseAdapter(settings, FakeConverse(response))
    assert adapter.invoke("private prompt", request_id="bedrock-1").status is AgentResultStatus.SUCCESS
    failure = BedrockConverseAdapter(settings, FakeConverse(error=RuntimeError("secret-provider-payload")))
    assert failure.invoke("private prompt", request_id="bedrock-2").status is AgentResultStatus.UNAVAILABLE
    calls = [item for item in events if item["event"] == "bedrock_call"]
    assert calls[0]["input_tokens"] == 7 and calls[0]["output_tokens"] == 5
    assert calls[0]["duration_ms"] >= 0
    assert calls[1]["sanitized_error"] == "provider_unavailable"
    assert "input_tokens" not in calls[1] and "output_tokens" not in calls[1]
    assert not any(text in json.dumps(calls) for text in
                   ("private prompt", "raw model response secret", "secret-provider-payload"))


class MissingS3:
    def get_object(self, **kwargs):
        from botocore.exceptions import ClientError
        raise ClientError({"Error": {"Code": "NoSuchKey", "Message": "secret object payload"}}, "GetObject")


def test_s3_missing_operation_event_has_no_object_content(events):
    adapter = S3StorageAdapter(Settings(s3_bucket="aqi-test-bucket", aws_region="us-east-1"), MissingS3())
    identity = ArtifactIdentity("storage-req", "draft-storage-req", "a" * 64)
    with pytest.raises(StorageFailure):
        adapter.retrieve(identity)
    storage = [item for item in events if item["event"] == "storage_operation"][-1]
    assert storage["operation"] == "retrieve"
    assert storage["sanitized_error"] == "not_found"
    assert storage["request_id"] == "storage-req"
    assert storage["quotation_id"] == "draft-storage-req"
    assert "secret object payload" not in json.dumps(storage)


class MemoryS3:
    def __init__(self):
        self.object = None

    def put_object(self, **kwargs):
        self.object = kwargs
        return {"ResponseMetadata": {"HTTPStatusCode": 200}, "ETag": '"etag"'}

    def get_object(self, **kwargs):
        stored = self.object
        return {"ResponseMetadata": {"HTTPStatusCode": 200},
                "Metadata": stored["Metadata"], "ContentLength": len(stored["Body"]),
                "ContentType": stored["ContentType"], "Body": BytesIO(stored["Body"])}


def test_s3_persist_retrieve_visibility_without_workbook_contents(events):
    stream = BytesIO()
    with ZipFile(stream, "w") as archive:
        archive.writestr("[Content_Types].xml", "secret-workbook")
        archive.writestr("xl/workbook.xml", "secret-workbook")
    artifact = WorkbookArtifact.from_validated_export(
        request_id="storage-roundtrip", quote_id="draft-storage-roundtrip",
        workbook_bytes=stream.getvalue())
    adapter = S3StorageAdapter(Settings(s3_bucket="aqi-test-bucket", aws_region="us-east-1"), MemoryS3())
    adapter.persist(artifact)
    assert adapter.retrieve(artifact.identity).workbook_bytes == artifact.workbook_bytes
    storage = [item for item in events if item["event"] == "storage_operation"]
    assert [(item["operation"], item["status"]) for item in storage] == [
        ("persist", "success"), ("retrieve", "success")]
    assert all(item["quotation_id"] == artifact.identity.quote_id for item in storage)
    assert "secret-workbook" not in json.dumps(storage)


def test_logging_failure_cannot_change_business_result(monkeypatch):
    import ai_quotation_intelligence.logging_config as boundary
    monkeypatch.setattr(boundary._LOGGER, "info", lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("sink failed")))
    emit_event("api_request", component="api", operation="health", status="failure")
    assert AgentTools().get_historical_quotes(HistoricalQuotesInput(request_id="still-works")).records


def test_local_health_logging_requires_no_aws_client(monkeypatch, events):
    import boto3
    def forbidden_client(*args, **kwargs):
        raise AssertionError("AWS client construction is not needed for local logging")
    monkeypatch.setattr(boto3, "client", forbidden_client)
    client = TestClient(create_app(QuotationAgent(FailingModel(), AgentTools())),
                        raise_server_exceptions=False)
    assert client.get("/health").json() == {"status": "ok"}
    assert any(item["event"] == "api_request" and item["operation"] == "health"
               for item in events)


def test_mutation_sensitivity_for_identifier_filter(monkeypatch, events):
    import ai_quotation_intelligence.logging_config as boundary
    secret = "secret/customer/body"
    def no_secret():
        emit_event("api_request", component="api", operation="health", status="success",
                   request_id=secret)
        assert secret not in json.dumps(events[-1])
    no_secret()
    monkeypatch.setattr(boundary, "_identifier", lambda value: value)
    with pytest.raises(AssertionError):
        no_secret()
