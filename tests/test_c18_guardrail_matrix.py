"""C18 evidence-matrix integrity; runtime enforcement remains with prior owners."""

from pathlib import Path


EVIDENCE_MAP = Path(__file__).parents[1] / "QUOTATION_CARD_EVIDENCE_MAP.md"
CANONICAL_STATES = (
    "MISSING_RATE",
    "MISSING_REQUIRED_HOURS",
    "INVALID_COMMERCIAL_VALUE",
    "CURRENCY_MISMATCH",
    "COMMERCIAL_SEMANTICS_UNVERIFIED",
    "DETERMINISTIC_CONFLICT",
    "INSUFFICIENT_EVIDENCE",
    "AI_UNSUPPORTED_CLAIM",
    "AI_INVALID",
    "AI_UNAVAILABLE",
    "AI_BOUNDARY_VIOLATION",
    "COMMERCIAL_INVARIANT_FAILED",
    "EXCEL_RECONCILIATION_FAILED",
    "APPROVAL_REQUIRED",
    "SECURITY_BOUNDARY_VIOLATION",
)


def _matrix_rows(text: str) -> dict[str, tuple[str, ...]]:
    section = text.split("## V1-C18 — Guardrails and Failure Handling", 1)[1]
    section = section.split("## V1-C19 — Golden Case", 1)[0]
    rows: dict[str, tuple[str, ...]] = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = tuple(cell.strip() for cell in line.strip().strip("|").split("|"))
        if cells and cells[0] in CANONICAL_STATES:
            assert cells[0] not in rows, f"duplicate C18 matrix row: {cells[0]}"
            rows[cells[0]] = cells
    return rows


def _matrix_is_complete(rows: dict[str, tuple[str, ...]]) -> bool:
    if tuple(rows) != CANONICAL_STATES:
        return False
    for state, cells in rows.items():
        if len(cells) != 8 or cells[-1] != "PASS":
            return False
        if any(marker in " ".join(cells) for marker in ("TO_BE_ASSESSED", "NOT_RUN")):
            return False
        expected = (
            "ENFORCEMENT_GAP_REQUIRES_FIX"
            if state == "COMMERCIAL_SEMANTICS_UNVERIFIED"
            else "EXISTING_EVIDENCE_SUFFICIENT"
        )
        if cells[5] != expected:
            return False
    return True


def test_c18_evidence_matrix_has_exactly_15_resolved_rows() -> None:
    assert _matrix_is_complete(_matrix_rows(EVIDENCE_MAP.read_text()))


def test_c18_matrix_omission_mutation_is_caught() -> None:
    rows = _matrix_rows(EVIDENCE_MAP.read_text())
    mutated = dict(rows)
    mutated.pop("SECURITY_BOUNDARY_VIOLATION")
    assert not _matrix_is_complete(mutated)
