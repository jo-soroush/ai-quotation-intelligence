"""Provider-neutral C14 contract for a C12-validated quotation workbook.

Trusted composition supplies bytes returned by C12. These types validate the
storage envelope and integrity identity; they do not grant approval or repeat
C12's workbook and commercial validation.
"""

from dataclasses import dataclass
from enum import StrEnum
from hashlib import sha256
from io import BytesIO
import re
from typing import Protocol
from zipfile import BadZipFile, ZipFile


MAX_WORKBOOK_BYTES = 20 * 1024 * 1024
_IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,127}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")


def _xlsx_envelope(blob: bytes) -> bool:
    """Check artifact classification, not C12 workbook/business correctness."""
    try:
        with ZipFile(BytesIO(blob)) as archive:
            names = set(archive.namelist())
    except (BadZipFile, OSError, ValueError):
        return False
    return {"[Content_Types].xml", "xl/workbook.xml"}.issubset(names)


class StorageFailureCode(StrEnum):
    INVALID_INPUT = "invalid_input"
    CONFIGURATION_MISSING = "configuration_missing"
    DUPLICATE = "duplicate"
    NOT_FOUND = "not_found"
    ACCESS_DENIED = "access_denied"
    UNAVAILABLE = "unavailable"
    CONFLICT = "conflict"
    PROVIDER_INVALID = "provider_invalid"
    INTEGRITY_MISMATCH = "integrity_mismatch"
    STORAGE_FAILED = "storage_failed"


class StorageFailure(Exception):
    """A typed storage failure whose message contains no provider details."""

    def __init__(self, code: StorageFailureCode) -> None:
        self.code = code
        super().__init__(code.value)


@dataclass(frozen=True, slots=True)
class ArtifactIdentity:
    request_id: str
    quote_id: str
    content_sha256: str

    def __post_init__(self) -> None:
        if (type(self.request_id) is not str or not _IDENTIFIER.fullmatch(self.request_id)
                or type(self.quote_id) is not str or not _IDENTIFIER.fullmatch(self.quote_id)
                or type(self.content_sha256) is not str
                or not _SHA256.fullmatch(self.content_sha256)):
            raise StorageFailure(StorageFailureCode.INVALID_INPUT)


@dataclass(frozen=True, slots=True)
class WorkbookArtifact:
    """A bounded storage-ready envelope, created after C12 has exported bytes."""

    identity: ArtifactIdentity
    workbook_bytes: bytes

    def __post_init__(self) -> None:
        if (type(self.identity) is not ArtifactIdentity
                or type(self.workbook_bytes) is not bytes
                or not self.workbook_bytes.startswith(b"PK\x03\x04")
                or len(self.workbook_bytes) > MAX_WORKBOOK_BYTES
                or not _xlsx_envelope(self.workbook_bytes)
                or sha256(self.workbook_bytes).hexdigest() != self.identity.content_sha256):
            raise StorageFailure(StorageFailureCode.INVALID_INPUT)

    @classmethod
    def from_validated_export(
        cls, *, request_id: str, quote_id: str, workbook_bytes: bytes,
    ) -> "WorkbookArtifact":
        """Package trusted C12 output; this is not proof of its provenance."""
        if type(workbook_bytes) is not bytes:
            raise StorageFailure(StorageFailureCode.INVALID_INPUT)
        identity = ArtifactIdentity(request_id, quote_id, sha256(workbook_bytes).hexdigest())
        return cls(identity, workbook_bytes)


@dataclass(frozen=True, slots=True)
class StoredArtifact:
    identity: ArtifactIdentity
    byte_length: int


@dataclass(frozen=True, slots=True)
class RetrievedArtifact:
    identity: ArtifactIdentity
    workbook_bytes: bytes


class StorageContract(Protocol):
    def persist(self, artifact: WorkbookArtifact) -> StoredArtifact: ...
    def retrieve(self, identity: ArtifactIdentity) -> RetrievedArtifact: ...


__all__ = [
    "ArtifactIdentity", "MAX_WORKBOOK_BYTES", "RetrievedArtifact", "StorageContract",
    "StorageFailure", "StorageFailureCode", "StoredArtifact", "WorkbookArtifact",
]
