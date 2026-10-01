"""C14 storage contract and S3 adapter checks, with no network or AWS bucket."""

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from io import BytesIO
from threading import Lock

import boto3
import pytest
from botocore import UNSIGNED
from botocore.config import Config
from botocore.exceptions import ClientError, EndpointConnectionError, NoCredentialsError
from botocore.response import StreamingBody
from botocore.stub import Stubber

from ai_quotation_intelligence.calculation import calculate_quote_total
from ai_quotation_intelligence.config import Settings, load_settings
from ai_quotation_intelligence.data.synthetic_history import generate_synthetic_history
from ai_quotation_intelligence.domain import (
    AgentResult, AgentResultStatus, ApprovalDecision, ApprovalStatus, DraftQuote,
    QuoteStatus,
)
from ai_quotation_intelligence.excel_export import export_approved_quote
from ai_quotation_intelligence.human_review import ReviewSession
from ai_quotation_intelligence.s3_storage import (
    S3StorageAdapter, XLSX_CONTENT_TYPE, derive_object_key,
)
from ai_quotation_intelligence.storage_contract import (
    ArtifactIdentity, RetrievedArtifact, StorageContract, StorageFailure,
    StorageFailureCode, StoredArtifact, WorkbookArtifact,
)


def client_error(code: str, operation: str = "PutObject") -> ClientError:
    return ClientError({"Error": {"Code": code, "Message": "secret-provider-detail"}}, operation)


class FakeS3:
    """Atomic conditional-write behavior, not a replica of C14 key logic."""

    def __init__(self) -> None:
        self.objects: dict[str, dict[str, object]] = {}
        self.calls: list[tuple[str, dict[str, object]]] = []
        self.lock = Lock()
        self.put_error: Exception | None = None
        self.get_error: Exception | None = None
        self.store_then_error: Exception | None = None
        self.put_response: object | None = None
        self.get_response: object | None = None

    def put_object(self, **kwargs):
        with self.lock:
            self.calls.append(("put_object", kwargs))
            if self.put_error is not None:
                raise self.put_error
            key = kwargs["Key"]
            if key in self.objects and kwargs.get("IfNoneMatch") == "*":
                raise client_error("PreconditionFailed")
            self.objects[key] = dict(kwargs)
            if self.store_then_error is not None:
                raise self.store_then_error
            if self.put_response is not None:
                return self.put_response
            return {"ResponseMetadata": {"HTTPStatusCode": 200}, "ETag": '"opaque-etag"'}

    def get_object(self, **kwargs):
        self.calls.append(("get_object", kwargs))
        if self.get_error is not None:
            raise self.get_error
        if self.get_response is not None:
            return self.get_response
        stored = self.objects.get(kwargs["Key"])
        if stored is None:
            raise client_error("NoSuchKey", "GetObject")
        content = stored["Body"]
        return {
            "ResponseMetadata": {"HTTPStatusCode": 200},
            "Metadata": dict(stored["Metadata"]),
            "ContentLength": len(content),
            "ContentType": stored["ContentType"],
            "Body": BytesIO(content),
        }


def settings() -> Settings:
    return Settings(s3_bucket="aqi-test-bucket", aws_region="eu-north-1")


@pytest.fixture
def artifact() -> WorkbookArtifact:
    """Use the real C11 approval and C12 export boundaries as input."""
    historical = generate_synthetic_history()[0].quote
    quote = historical.model_copy(update={
        "quote_id": "draft-storage-case", "status": QuoteStatus.DRAFT,
        "estimated_total_cost": None,
    })
    quote = quote.model_copy(update={"estimated_total_cost": calculate_quote_total(quote)})
    draft = DraftQuote(quote=quote, evidence_ids=["evidence-1"])
    result = AgentResult(
        request_id="storage-case", status=AgentResultStatus.SUCCESS,
        draft_quote=draft, evidence_ids=["evidence-1"],
    )
    session = ReviewSession(result)
    session.decide(ApprovalDecision(
        quote_id=quote.quote_id, status=ApprovalStatus.APPROVED,
        reviewer_id="human-reviewer",
        decided_at=datetime(2026, 10, 1, tzinfo=timezone.utc),
    ), current=result)
    blob = export_approved_quote(session, current=result)
    return WorkbookArtifact.from_validated_export(
        request_id=result.request_id, quote_id=quote.quote_id, workbook_bytes=blob,
    )


def assert_failure(code: StorageFailureCode, call) -> None:
    with pytest.raises(StorageFailure) as error:
        call()
    assert error.value.code is code
    assert str(error.value) == code.value


def test_contract_and_real_c12_artifact_round_trip(artifact: WorkbookArtifact) -> None:
    fake = FakeS3()
    adapter: StorageContract = S3StorageAdapter(settings(), fake)
    stored = adapter.persist(artifact)
    loaded = adapter.retrieve(stored.identity)

    assert type(stored) is StoredArtifact
    assert stored.identity == artifact.identity
    assert stored.byte_length == len(artifact.workbook_bytes)
    assert type(loaded) is RetrievedArtifact
    assert loaded.identity == artifact.identity
    assert loaded.workbook_bytes == artifact.workbook_bytes
    assert fake.calls[0][0] == "put_object"
    request = fake.calls[0][1]
    assert request["Bucket"] == "aqi-test-bucket"
    assert request["Key"] == derive_object_key(artifact.identity)
    assert request["Body"] == artifact.workbook_bytes
    assert request["ContentType"] == XLSX_CONTENT_TYPE
    assert request["IfNoneMatch"] == "*"
    assert request["Metadata"] == {
        "artifact-sha256": artifact.identity.content_sha256,
        "identity-sha256": request["Key"].removeprefix("generated/v1/").removesuffix(".xlsx"),
    }
    assert set(request) == {"Bucket", "Key", "Body", "ContentType", "Metadata", "IfNoneMatch"}
    assert fake.calls[1] == ("get_object", {"Bucket": "aqi-test-bucket", "Key": request["Key"]})


def test_identity_key_is_fixed_namespace_deterministic_and_content_bound(artifact) -> None:
    identity = artifact.identity
    first = derive_object_key(identity)
    assert first == derive_object_key(identity)
    assert first.startswith("generated/v1/") and first.endswith(".xlsx")
    assert len(first.removeprefix("generated/v1/").removesuffix(".xlsx")) == 64
    assert "/" not in first.removeprefix("generated/v1/")
    assert first != derive_object_key(ArtifactIdentity("other-request", identity.quote_id, identity.content_sha256))
    assert first != derive_object_key(ArtifactIdentity(identity.request_id, "other-quote", identity.content_sha256))
    assert first != derive_object_key(ArtifactIdentity(identity.request_id, identity.quote_id, "0" * 64))


@pytest.mark.parametrize("bad", ["../quote", "a/b", "a\\b", " a", "@abc", "a.b", "", "a" * 129])
def test_path_like_or_unbounded_identity_cannot_control_key(bad: str, artifact) -> None:
    assert_failure(StorageFailureCode.INVALID_INPUT, lambda: ArtifactIdentity(
        bad, artifact.identity.quote_id, artifact.identity.content_sha256,
    ))


def test_invalid_artifact_and_forged_digest_fail_before_provider(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)
    assert_failure(StorageFailureCode.INVALID_INPUT, lambda: WorkbookArtifact.from_validated_export(
        request_id="r", quote_id="q", workbook_bytes=b'{"total": 900}',
    ))
    assert_failure(StorageFailureCode.INVALID_INPUT, lambda: WorkbookArtifact.from_validated_export(
        request_id="r", quote_id="q", workbook_bytes=b"PK\x03\x04not-an-xlsx",
    ))
    assert_failure(StorageFailureCode.INVALID_INPUT, lambda: adapter.persist(b"PK\x03\x04anything"))
    forged = WorkbookArtifact.from_validated_export(
        request_id="r", quote_id="q", workbook_bytes=artifact.workbook_bytes,
    )
    object.__setattr__(forged, "workbook_bytes", forged.workbook_bytes + b"changed")
    assert_failure(StorageFailureCode.INVALID_INPUT, lambda: adapter.persist(forged))
    assert fake.calls == []


def test_duplicate_is_explicit_and_existing_object_is_unchanged(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)
    adapter.persist(artifact)
    before = dict(fake.objects[derive_object_key(artifact.identity)])
    assert_failure(StorageFailureCode.DUPLICATE, lambda: adapter.persist(artifact))
    assert fake.objects[derive_object_key(artifact.identity)] == before


def test_missing_object_is_distinct_from_access_denied(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)
    assert_failure(StorageFailureCode.NOT_FOUND, lambda: adapter.retrieve(artifact.identity))
    fake.get_error = client_error("AccessDenied", "GetObject")
    assert_failure(StorageFailureCode.ACCESS_DENIED, lambda: adapter.retrieve(artifact.identity))
    fake.get_error = client_error("NoSuchBucket", "GetObject")
    assert_failure(StorageFailureCode.UNAVAILABLE, lambda: adapter.retrieve(artifact.identity))


@pytest.mark.parametrize("code,expected", [
    ("AccessDenied", StorageFailureCode.ACCESS_DENIED),
    ("PreconditionFailed", StorageFailureCode.DUPLICATE),
    ("ConditionalRequestConflict", StorageFailureCode.CONFLICT),
    ("SlowDown", StorageFailureCode.UNAVAILABLE),
    ("UnexpectedProviderCode", StorageFailureCode.STORAGE_FAILED),
])
def test_put_client_errors_are_sanitized(artifact, code, expected) -> None:
    fake = FakeS3()
    fake.put_error = client_error(code)
    assert_failure(expected, lambda: S3StorageAdapter(settings(), fake).persist(artifact))


@pytest.mark.parametrize("error,expected", [
    (NoCredentialsError(), StorageFailureCode.ACCESS_DENIED),
    (EndpointConnectionError(endpoint_url="https://secret-provider.example"), StorageFailureCode.UNAVAILABLE),
    (RuntimeError("secret-provider-detail"), StorageFailureCode.STORAGE_FAILED),
])
def test_non_client_provider_errors_are_sanitized(artifact, error, expected) -> None:
    fake = FakeS3()
    fake.put_error = error
    assert_failure(expected, lambda: S3StorageAdapter(settings(), fake).persist(artifact))


def test_malformed_sdk_error_code_is_sanitized(artifact) -> None:
    fake = FakeS3()
    fake.put_error = ClientError({"Error": {"Code": ["AccessDenied"],
                                              "Message": "secret-provider-detail"}}, "PutObject")
    assert_failure(StorageFailureCode.PROVIDER_INVALID,
                   lambda: S3StorageAdapter(settings(), fake).persist(artifact))


@pytest.mark.parametrize("response", [
    {}, {"ResponseMetadata": {"HTTPStatusCode": 204}, "ETag": '"opaque"'},
    {"ResponseMetadata": {"HTTPStatusCode": 200}},
    {"ResponseMetadata": {"HTTPStatusCode": True}, "ETag": '"opaque"'},
])
def test_malformed_put_success_never_becomes_stored_artifact(artifact, response) -> None:
    fake = FakeS3()
    fake.put_response = response
    assert_failure(StorageFailureCode.PROVIDER_INVALID,
                   lambda: S3StorageAdapter(settings(), fake).persist(artifact))


def test_retrieval_detects_body_metadata_type_and_length_substitution(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)
    adapter.persist(artifact)
    original = fake.get_object(Bucket="aqi-test-bucket", Key=derive_object_key(artifact.identity))
    fake.get_response = {**original, "Body": BytesIO(artifact.workbook_bytes + b"tampered"),
                         "ContentLength": len(artifact.workbook_bytes) + 8}
    assert_failure(StorageFailureCode.INTEGRITY_MISMATCH, lambda: adapter.retrieve(artifact.identity))
    fake.get_response = {**original, "Metadata": {"artifact-sha256": "0" * 64}}
    assert_failure(StorageFailureCode.INTEGRITY_MISMATCH, lambda: adapter.retrieve(artifact.identity))
    fake.get_response = {**original, "ContentType": "text/plain"}
    assert_failure(StorageFailureCode.INTEGRITY_MISMATCH, lambda: adapter.retrieve(artifact.identity))
    fake.get_response = {**original, "ContentLength": len(artifact.workbook_bytes) + 1}
    assert_failure(StorageFailureCode.INTEGRITY_MISMATCH, lambda: adapter.retrieve(artifact.identity))


def test_malformed_get_response_and_read_failure_are_sanitized(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)
    fake.get_response = {"ResponseMetadata": {"HTTPStatusCode": 200}}
    assert_failure(StorageFailureCode.PROVIDER_INVALID, lambda: adapter.retrieve(artifact.identity))

    class BrokenBody:
        def read(self, size):
            raise RuntimeError("secret-provider-detail")

    fake.get_response = {
        "ResponseMetadata": {"HTTPStatusCode": 200}, "Metadata": {
            "artifact-sha256": artifact.identity.content_sha256,
            "identity-sha256": derive_object_key(artifact.identity).split("/")[-1][:-5],
        },
        "ContentLength": len(artifact.workbook_bytes),
        "ContentType": XLSX_CONTENT_TYPE, "Body": BrokenBody(),
    }
    assert_failure(StorageFailureCode.STORAGE_FAILED, lambda: adapter.retrieve(artifact.identity))


def test_configuration_is_explicit_and_injected_client_avoids_boto3(monkeypatch, artifact) -> None:
    assert_failure(StorageFailureCode.CONFIGURATION_MISSING, lambda: S3StorageAdapter(Settings(), FakeS3()))
    assert_failure(StorageFailureCode.CONFIGURATION_MISSING,
                   lambda: S3StorageAdapter(Settings(s3_bucket=""), FakeS3()))
    assert_failure(StorageFailureCode.CONFIGURATION_MISSING,
                   lambda: S3StorageAdapter(Settings(s3_bucket="../unsafe"), FakeS3()))
    monkeypatch.setenv("AQI_S3_BUCKET", "aqi-test-bucket")
    assert load_settings().s3_bucket == "aqi-test-bucket"
    monkeypatch.setattr("ai_quotation_intelligence.s3_storage.boto3.client",
                        lambda *args, **kwargs: pytest.fail("network client constructed"))
    assert S3StorageAdapter(settings(), FakeS3()).persist(artifact).identity == artifact.identity


def test_default_client_uses_region_bounded_config_and_standard_credentials(monkeypatch) -> None:
    captured = {}

    def fake_client(service_name, **kwargs):
        captured.update({"service_name": service_name, **kwargs})
        return FakeS3()

    monkeypatch.setattr("ai_quotation_intelligence.s3_storage.boto3.client", fake_client)
    S3StorageAdapter(settings())._provider_client()
    assert captured["service_name"] == "s3"
    assert captured["region_name"] == "eu-north-1"
    assert captured["config"].connect_timeout == 5
    assert captured["config"].read_timeout == 30
    assert captured["config"].retries["max_attempts"] == 1
    assert "aws_access_key_id" not in captured and "aws_secret_access_key" not in captured


def test_botocore_stubber_checks_real_sdk_call_shape_without_network(artifact) -> None:
    client = boto3.client("s3", region_name="eu-north-1", config=Config(signature_version=UNSIGNED))
    key = derive_object_key(artifact.identity)
    metadata = {
        "artifact-sha256": artifact.identity.content_sha256,
        "identity-sha256": key.split("/")[-1][:-5],
    }
    with Stubber(client) as stubber:
        stubber.add_response("put_object", {
            "ResponseMetadata": {"HTTPStatusCode": 200}, "ETag": '"opaque"',
        }, {
            "Bucket": "aqi-test-bucket", "Key": key, "Body": artifact.workbook_bytes,
            "ContentType": XLSX_CONTENT_TYPE, "Metadata": metadata, "IfNoneMatch": "*",
        })
        stubber.add_response("get_object", {
            "ResponseMetadata": {"HTTPStatusCode": 200},
            "Metadata": metadata, "ContentLength": len(artifact.workbook_bytes),
            "ContentType": XLSX_CONTENT_TYPE,
            "Body": StreamingBody(BytesIO(artifact.workbook_bytes), len(artifact.workbook_bytes)),
        }, {"Bucket": "aqi-test-bucket", "Key": key})
        adapter = S3StorageAdapter(settings(), client)
        assert adapter.persist(artifact).identity == artifact.identity
        assert adapter.retrieve(artifact.identity).workbook_bytes == artifact.workbook_bytes
        stubber.assert_no_pending_responses()


def test_conditional_put_handles_same_process_race_without_overwrite(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)

    def attempt():
        try:
            return adapter.persist(artifact)
        except StorageFailure as exc:
            return exc.code

    with ThreadPoolExecutor(max_workers=2) as pool:
        outcomes = list(pool.map(lambda _: attempt(), range(2)))
    assert sum(type(value) is StoredArtifact for value in outcomes) == 1
    assert outcomes.count(StorageFailureCode.DUPLICATE) == 1
    assert adapter.retrieve(artifact.identity).workbook_bytes == artifact.workbook_bytes
    assert all(call[1].get("IfNoneMatch") == "*" for call in fake.calls if call[0] == "put_object")


def test_ambiguous_write_failure_never_fabricates_success_or_overwrites_on_retry(artifact) -> None:
    fake = FakeS3()
    fake.store_then_error = EndpointConnectionError(endpoint_url="https://secret-provider.example")
    adapter = S3StorageAdapter(settings(), fake)
    assert_failure(StorageFailureCode.UNAVAILABLE, lambda: adapter.persist(artifact))
    fake.store_then_error = None
    assert_failure(StorageFailureCode.DUPLICATE, lambda: adapter.persist(artifact))
    assert adapter.retrieve(artifact.identity).workbook_bytes == artifact.workbook_bytes


def test_contract_values_are_storage_owned_and_do_not_leak_provider_response(artifact) -> None:
    fake = FakeS3()
    adapter = S3StorageAdapter(settings(), fake)
    stored = adapter.persist(artifact)
    retrieved = adapter.retrieve(artifact.identity)
    assert type(stored) is StoredArtifact and type(retrieved) is RetrievedArtifact
    assert not hasattr(stored, "ResponseMetadata")
    assert not hasattr(retrieved, "ETag")
    assert sha256(retrieved.workbook_bytes).hexdigest() == artifact.identity.content_sha256
