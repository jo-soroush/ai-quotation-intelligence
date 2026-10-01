"""C14 S3 adapter: conditional persistence and validated retrieval only."""

from hashlib import sha256
import re
from typing import Any, Protocol

import boto3
from botocore.config import Config
from botocore.exceptions import (
    BotoCoreError, ClientError, NoCredentialsError, PartialCredentialsError,
)

from ai_quotation_intelligence.config import Settings, load_settings
from ai_quotation_intelligence.storage_contract import (
    ArtifactIdentity, MAX_WORKBOOK_BYTES, RetrievedArtifact, StorageFailure,
    StorageFailureCode, StoredArtifact, WorkbookArtifact,
)


XLSX_CONTENT_TYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
_BUCKET = re.compile(r"[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]\Z")
_PREFIX = "generated/v1/"


class S3Client(Protocol):
    def put_object(self, **kwargs: Any) -> dict[str, Any]: ...
    def get_object(self, **kwargs: Any) -> dict[str, Any]: ...


def _validated_identity(value: object) -> ArtifactIdentity:
    if type(value) is not ArtifactIdentity:
        raise StorageFailure(StorageFailureCode.INVALID_INPUT)
    return ArtifactIdentity(value.request_id, value.quote_id, value.content_sha256)


def _identity_digest(identity: ArtifactIdentity) -> str:
    """Hash length-delimited identity fields, including the content digest."""
    parts = (identity.request_id, identity.quote_id, identity.content_sha256)
    payload = b"".join(
        len(encoded).to_bytes(2, "big") + encoded
        for encoded in (part.encode("utf-8") for part in parts)
    )
    return sha256(payload).hexdigest()


def derive_object_key(identity: ArtifactIdentity) -> str:
    """A fixed namespace and digest; no caller supplies a final S3 key."""
    return f"{_PREFIX}{_identity_digest(_validated_identity(identity))}.xlsx"


def _owned_metadata(identity: ArtifactIdentity) -> dict[str, str]:
    return {
        "artifact-sha256": identity.content_sha256,
        "identity-sha256": _identity_digest(identity),
    }


def _provider_failure(exc: Exception, *, operation: str) -> StorageFailure:
    if isinstance(exc, ClientError):
        try:
            code = exc.response["Error"]["Code"]
        except (KeyError, TypeError):
            return StorageFailure(StorageFailureCode.PROVIDER_INVALID)
        if type(code) is not str:
            return StorageFailure(StorageFailureCode.PROVIDER_INVALID)
        if code in {"AccessDenied", "InvalidAccessKeyId", "SignatureDoesNotMatch", "ExpiredToken", "403"}:
            return StorageFailure(StorageFailureCode.ACCESS_DENIED)
        if operation == "get" and code in {"NoSuchKey", "NotFound", "404"}:
            return StorageFailure(StorageFailureCode.NOT_FOUND)
        if operation == "put" and code in {"PreconditionFailed", "412"}:
            return StorageFailure(StorageFailureCode.DUPLICATE)
        if operation == "put" and code in {"ConditionalRequestConflict", "409"}:
            return StorageFailure(StorageFailureCode.CONFLICT)
        if code in {"SlowDown", "RequestTimeout", "ServiceUnavailable", "InternalError", "NoSuchBucket"}:
            return StorageFailure(StorageFailureCode.UNAVAILABLE)
        return StorageFailure(StorageFailureCode.STORAGE_FAILED)
    if isinstance(exc, (NoCredentialsError, PartialCredentialsError)):
        return StorageFailure(StorageFailureCode.ACCESS_DENIED)
    if isinstance(exc, BotoCoreError):
        return StorageFailure(StorageFailureCode.UNAVAILABLE)
    return StorageFailure(StorageFailureCode.STORAGE_FAILED)


def _success_response(value: object, *, etag: bool = False) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise StorageFailure(StorageFailureCode.PROVIDER_INVALID)
    meta = value.get("ResponseMetadata")
    if (not isinstance(meta, dict) or type(meta.get("HTTPStatusCode")) is not int
            or meta["HTTPStatusCode"] != 200
            or (etag and (not isinstance(value.get("ETag"), str) or not value["ETag"]))):
        raise StorageFailure(StorageFailureCode.PROVIDER_INVALID)
    return value


class S3StorageAdapter:
    """Synchronous adapter; S3 is storage, never approval or commercial truth."""

    def __init__(self, settings: Settings | None = None, client: S3Client | None = None) -> None:
        resolved = settings if settings is not None else load_settings()
        if (type(resolved) is not Settings
                or type(resolved.s3_bucket) is not str
                or not _BUCKET.fullmatch(resolved.s3_bucket)
                or ".." in resolved.s3_bucket
                or type(resolved.aws_region) is not str
                or not resolved.aws_region.strip()):
            raise StorageFailure(StorageFailureCode.CONFIGURATION_MISSING)
        self._settings = resolved
        self._client = client

    def _provider_client(self) -> S3Client:
        if self._client is None:
            try:
                self._client = boto3.client(
                    "s3",
                    region_name=self._settings.aws_region,
                    config=Config(
                        connect_timeout=5,
                        read_timeout=30,
                        retries={"mode": "standard", "max_attempts": 1},
                    ),
                )
            except Exception as exc:
                raise _provider_failure(exc, operation="connect") from None
        return self._client

    def persist(self, artifact: WorkbookArtifact) -> StoredArtifact:
        if type(artifact) is not WorkbookArtifact:
            raise StorageFailure(StorageFailureCode.INVALID_INPUT)
        clean = WorkbookArtifact(_validated_identity(artifact.identity), artifact.workbook_bytes)
        identity = clean.identity
        try:
            response = self._provider_client().put_object(
                Bucket=self._settings.s3_bucket,
                Key=derive_object_key(identity),
                Body=clean.workbook_bytes,
                ContentType=XLSX_CONTENT_TYPE,
                Metadata=_owned_metadata(identity),
                IfNoneMatch="*",
            )
        except StorageFailure:
            raise
        except Exception as exc:
            raise _provider_failure(exc, operation="put") from None
        _success_response(response, etag=True)
        return StoredArtifact(identity, len(clean.workbook_bytes))

    def retrieve(self, identity: ArtifactIdentity) -> RetrievedArtifact:
        clean = _validated_identity(identity)
        try:
            response = self._provider_client().get_object(
                Bucket=self._settings.s3_bucket, Key=derive_object_key(clean),
            )
        except StorageFailure:
            raise
        except Exception as exc:
            raise _provider_failure(exc, operation="get") from None

        value = _success_response(response)
        if (not isinstance(value.get("Metadata"), dict)
                or type(value.get("ContentLength")) is not int
                or value["ContentLength"] < 0
                or not isinstance(value.get("ContentType"), str)
                or not callable(getattr(value.get("Body"), "read", None))):
            raise StorageFailure(StorageFailureCode.PROVIDER_INVALID)
        if (value["Metadata"] != _owned_metadata(clean)
                or value["ContentType"] != XLSX_CONTENT_TYPE
                or value["ContentLength"] > MAX_WORKBOOK_BYTES):
            raise StorageFailure(StorageFailureCode.INTEGRITY_MISMATCH)
        body = value["Body"]
        try:
            content = body.read(MAX_WORKBOOK_BYTES + 1)
            close = getattr(body, "close", None)
            if callable(close):
                close()
        except Exception:
            raise StorageFailure(StorageFailureCode.STORAGE_FAILED) from None
        if (type(content) is not bytes or len(content) != value["ContentLength"]
                or sha256(content).hexdigest() != clean.content_sha256):
            raise StorageFailure(StorageFailureCode.INTEGRITY_MISMATCH)
        try:
            WorkbookArtifact(clean, content)
        except StorageFailure:
            raise StorageFailure(StorageFailureCode.INTEGRITY_MISMATCH) from None
        return RetrievedArtifact(clean, content)


__all__ = ["S3Client", "S3StorageAdapter", "XLSX_CONTENT_TYPE", "derive_object_key"]
