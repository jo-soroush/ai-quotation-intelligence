"""V1-C17 offline evaluation contracts and harness-integrity probes."""

from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import socket
import sys
from typing import Any
from urllib import request as urllib_request

import pytest

# pytest is configured to expose only ``src``. C17 intentionally lives outside
# that production package, so this focused suite exposes the repository-owned
# offline package without changing runtime packaging or global test settings.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import evaluation.c17 as c17


def _dataset() -> dict[str, Any]:
    return json.loads(c17.DEFAULT_DATASET_PATH.read_text(encoding="utf-8"))


def _write_dataset(tmp_path: Path, data: dict[str, Any]) -> Path:
    path = tmp_path / "golden.json"
    payload = (json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    path.write_bytes(payload)
    path.with_suffix(".sha256").write_text(sha256(payload).hexdigest() + "\n", encoding="ascii")
    return path


def _metric(report: dict[str, Any], name: str) -> dict[str, Any]:
    return next(item for item in report["metrics"] if item["name"] == name)


def test_fixed_golden_dataset_passes_every_gating_metric() -> None:
    report = c17.evaluate()

    assert report["overall_status"] == "PASS"
    assert report["dataset_version"] == "c17-golden-v1"
    assert report["dataset_sha256"] == "1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b"
    assert report["synthetic"] is True
    assert len(report["case_results"]) == 10
    assert all(item["status"] == "PASS" for item in report["case_results"])
    assert all(item["status"] == "PASS" for item in report["metrics"] if not item["report_only"])


def test_machine_report_is_exactly_reproducible() -> None:
    first = c17.serialize_report(c17.evaluate())
    second = c17.serialize_report(c17.evaluate())

    assert first == second
    assert sha256(first.encode()).hexdigest() == sha256(second.encode()).hexdigest()


def test_dataset_is_fixed_synthetic_and_independently_authored() -> None:
    loaded = c17.load_dataset()

    assert loaded.data["synthetic"] is True
    assert loaded.data["oracle_source"] == "independently_authored_and_preverified"
    assert all(record["data_origin"] == "synthetic" for record in loaded.data["history"])
    assert all(record["quote"]["data_origin"] == "synthetic" for record in loaded.data["history"])
    assert set(loaded.data["cases"]) == set(c17.CASE_CATEGORIES)


def test_gating_thresholds_are_the_canonical_exact_values() -> None:
    assert c17.GATING_THRESHOLDS == {
        "calculation_correctness": c17.Decimal("1"),
        "historical_comparison_correctness": c17.Decimal("1"),
        "retrieval_hit_at_3": c17.Decimal("1"),
        "evidence_provenance_correctness": c17.Decimal("1"),
        "unsupported_risk_rate": c17.Decimal("0"),
        "structured_output_validity": c17.Decimal("1"),
        "tool_call_contract_success": c17.Decimal("1"),
        "agent_task_completion": c17.Decimal("1"),
        "excel_correctness": c17.Decimal("1"),
    }


def test_wrong_calculation_oracle_fails_instead_of_becoming_truth(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["calculation"][0]["expected_total"]["amount"] = "2000.01"

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "calculation_correctness") == {
        "name": "calculation_correctness", "report_only": False,
        "numerator": 1, "denominator": 2, "value": "0.5",
        "threshold": "1", "status": "FAIL",
    }


def test_wrong_historical_oracle_fails(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["historical_comparison"][0]["expected"]["hour_variance"]["variance"] = "5"

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "historical_comparison_correctness")["status"] == "FAIL"


def test_retrieval_expected_only_below_top_three_fails_hit_at_3(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["retrieval"][0]["expected_similar_quote_ids"] = ["syn-hist-app-003"]

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "retrieval_hit_at_3")["value"] == "0"
    assert _metric(report, "retrieval_hit_at_3")["status"] == "FAIL"


def test_fabricated_risk_reference_fails_provenance_and_unsupported_rate(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["risk_evidence"][0]["expected"]["evidence_ids"] = ["fabricated-evidence"]

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "evidence_provenance_correctness")["status"] == "FAIL"
    assert _metric(report, "unsupported_risk_rate")["value"] == "1"
    assert _metric(report, "unsupported_risk_rate")["status"] == "FAIL"


def test_zero_emitted_risk_references_have_zero_rate_but_required_evidence_still_fails(
    tmp_path: Path,
) -> None:
    data = _dataset()
    selected = set(data["cases"]["risk_evidence"][0]["history_quote_ids"])
    for record in data["history"]:
        if record["quote"]["quote_id"] in selected:
            record["outcome"]["actual_hours"] = None
    expected = data["cases"]["risk_evidence"][0]["expected"]
    expected.update({
        "status": "insufficient_evidence",
        "comparable_project_count": 0,
        "overrun_count": 0,
        "overrun_rate": None,
        "average_variance": None,
        "median_variance": None,
        "source_quote_ids": [],
        "source_ids": [],
        "evidence_ids": [],
    })

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "unsupported_risk_rate")["value"] == "0"
    assert _metric(report, "unsupported_risk_rate")["status"] == "PASS"
    assert _metric(report, "evidence_provenance_correctness")["status"] == "FAIL"


def test_tool_contract_mismatch_fails(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["tool_call"][0]["expected_evidence_id"] = "fabricated-evidence"

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "tool_call_contract_success")["status"] == "FAIL"


def test_invalid_scripted_agent_output_fails_agent_and_structured_metrics(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["agent_task"][0]["script"] = [
        {
            "kind": "final", "narrative": "Draft for human review.",
            "evidence_ids": [], "risk_suggestions": [], "missing_information": [],
        }
    ]

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "agent_task_completion")["status"] == "FAIL"
    assert _metric(report, "structured_output_validity")["status"] == "FAIL"


def test_excel_mismatch_fails_without_persisting_workbook_content(tmp_path: Path) -> None:
    data = _dataset()
    data["cases"]["excel"][0]["expected_total"] = "1599"

    report = c17.evaluate(_write_dataset(tmp_path, data))
    serialized = c17.serialize_report(report)

    assert report["overall_status"] == "FAIL"
    assert _metric(report, "excel_correctness")["status"] == "FAIL"
    assert "workbook_bytes" not in serialized
    assert "c17-synthetic-reviewer" not in serialized


def test_dataset_byte_tampering_returns_error(tmp_path: Path) -> None:
    path = _write_dataset(tmp_path, _dataset())
    path.write_bytes(path.read_bytes() + b" ")

    report = c17.evaluate(path)

    assert report["overall_status"] == "ERROR"
    assert report["case_results"] == []


def test_dataset_version_drift_returns_error_even_with_updated_hash(tmp_path: Path) -> None:
    data = _dataset()
    data["dataset_version"] = "c17-golden-v2-unapproved"

    report = c17.evaluate(_write_dataset(tmp_path, data))

    assert report["overall_status"] == "ERROR"


@pytest.mark.parametrize(
    "mutation",
    [
        "duplicate_case",
        "missing_expected",
        "invalid_case_type",
        "synthetic_misrepresentation",
    ],
)
def test_malformed_or_tampered_dataset_returns_error(tmp_path: Path, mutation: str) -> None:
    data = _dataset()
    if mutation == "duplicate_case":
        data["cases"]["calculation"][1]["case_id"] = data["cases"]["calculation"][0]["case_id"]
    elif mutation == "missing_expected":
        del data["cases"]["calculation"][0]["expected_total"]
    elif mutation == "invalid_case_type":
        data["cases"]["calculation"][0] = "not-an-object"
    else:
        data["synthetic"] = False

    assert c17.evaluate(_write_dataset(tmp_path, data))["overall_status"] == "ERROR"


def test_silent_case_skipping_is_rejected() -> None:
    one_result = [{
        "case_id": "only-one", "metric": "calculation_correctness", "status": "PASS",
        "failure_reason": None, "evidence_references": [],
    }]

    with pytest.raises(c17.EvaluationIntegrityError, match="case_count_mismatch"):
        c17._gating_metric("calculation_correctness", one_result, expected_count=2)


def test_standard_metric_denominator_manipulation_is_rejected() -> None:
    result = [{
        "case_id": "case", "metric": "calculation_correctness", "status": "PASS",
        "failure_reason": None, "evidence_references": [],
    }]

    with pytest.raises(c17.EvaluationIntegrityError, match="metric_denominator_manipulation"):
        c17._gating_metric(
            "calculation_correctness", result, 1, numerator=1, denominator=100,
        )


def test_report_only_metrics_are_explicitly_non_gating() -> None:
    report = c17.evaluate()

    for name in c17.REPORT_ONLY_METRICS:
        assert _metric(report, name) == {
            "name": name, "report_only": True, "numerator": None, "denominator": None,
            "value": None, "threshold": None, "status": "NOT_MEASURED_OFFLINE",
        }
    assert report["overall_status"] == "PASS"


def test_error_report_cannot_be_relabeled_pass() -> None:
    report = c17._error_report("0" * 64, "evaluation_integrity_error")
    report["overall_status"] = "PASS"

    with pytest.raises(c17.EvaluationIntegrityError, match="misleading_pass_status"):
        c17._validate_report(report)


@pytest.mark.parametrize("field", ["dataset_version", "dataset_sha256"])
def test_report_requires_dataset_identity(field: str) -> None:
    report = c17.evaluate()
    del report[field]

    with pytest.raises(c17.EvaluationIntegrityError, match="report_fields_invalid"):
        c17.serialize_report(report)


@pytest.mark.parametrize(
    "forbidden_field",
    ["raw_prompt", "raw_model_response", "reviewer_id", "workbook_bytes", "request_body", "aws_secret_access_key"],
)
def test_report_rejects_prohibited_raw_fields(forbidden_field: str) -> None:
    report = c17.evaluate()
    report["case_results"][0][forbidden_field] = "must-not-persist"

    with pytest.raises(c17.EvaluationIntegrityError):
        c17.serialize_report(report)


def test_failure_reason_must_be_bounded_not_raw_exception_text() -> None:
    report = c17.evaluate()
    report["case_results"][0]["status"] = "FAIL"
    report["case_results"][0]["failure_reason"] = "raw provider exception: credential=bad"
    _metric(report, report["case_results"][0]["metric"])["status"] = "FAIL"
    report["overall_status"] = "FAIL"

    with pytest.raises(c17.EvaluationIntegrityError, match="report_failure_reason_unbounded"):
        c17.serialize_report(report)


def test_ordinary_evaluation_needs_no_network_or_aws_credentials(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def blocked(*_args: Any, **_kwargs: Any) -> None:
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket, "create_connection", blocked)
    monkeypatch.setattr(urllib_request, "urlopen", blocked)
    for name in (
        "AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN",
        "AWS_PROFILE", "AWS_DEFAULT_PROFILE",
    ):
        monkeypatch.delenv(name, raising=False)

    assert c17.evaluate()["overall_status"] == "PASS"


def test_machine_report_contains_no_prohibited_payload_or_business_claim() -> None:
    serialized = c17.serialize_report(c17.evaluate())
    lower = serialized.lower()

    assert "reviewer_id" not in lower
    assert "raw_prompt" not in lower
    assert "raw_model_response" not in lower
    assert "workbook_bytes" not in lower
    assert "customer_data" not in lower
    assert "production ready" not in lower
    assert "commercially correct" not in lower
    assert (
        "The system passed the defined deterministic contracts on the fixed synthetic Golden Dataset."
        in serialized
    )


def test_unknown_metric_definition_is_rejected() -> None:
    with pytest.raises(c17.EvaluationIntegrityError, match="unknown_metric_definition"):
        c17._gating_metric("invented_quality_score", [], 0)


def test_evaluation_does_not_mutate_dataset_file() -> None:
    before = c17.DEFAULT_DATASET_PATH.read_bytes()
    c17.evaluate()
    after = c17.DEFAULT_DATASET_PATH.read_bytes()

    assert before == after
    assert sha256(after).hexdigest() == c17.load_dataset().sha256
