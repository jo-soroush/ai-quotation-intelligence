"""V1-C19 fixed synthetic Golden Case and harness-integrity proof."""

from copy import deepcopy
from decimal import Decimal
from hashlib import sha256
import json
from pathlib import Path

import pytest

from evaluation.c19 import (
    C17_DATASET_SHA256,
    C17_REPORT_SHA256,
    DEFAULT_SCENARIO_PATH,
    PASS_CLAIM,
    REQUIRED_STEPS,
    ReportIntegrityError,
    load_scenario,
    run_once,
    run_twice,
    serialize_report,
    validate_report,
)


@pytest.fixture(scope="module")
def scenario():
    return load_scenario()


@pytest.fixture(scope="module")
def golden_report():
    report = run_once()
    assert report["overall_status"] == "PASS"
    return report


def test_fixture_identity_synthetic_semantics_and_independent_oracle(scenario) -> None:
    data = scenario.data
    raw = DEFAULT_SCENARIO_PATH.read_bytes()
    assert sha256(raw).hexdigest() == scenario.sha256
    assert DEFAULT_SCENARIO_PATH.with_suffix(".sha256").read_text().split() == [
        scenario.sha256, DEFAULT_SCENARIO_PATH.name]
    assert data["synthetic"] is True
    assert all(item["synthetic"] is True for item in data["historical_inputs"])
    assert all(item["estimated_hours"]["unit"] == "hours"
               for item in data["request"]["quotation_request"]["items"])
    # Independent, transparent arithmetic over fixture literals; Core is not the oracle.
    assert [Decimal("13") * Decimal("110"), Decimal("21") * Decimal("125"),
            Decimal("9") * Decimal("100")] == [Decimal(value)
                                                    for value in data["expected"]["estimated_item_costs"]]
    assert sum((Decimal(value) for value in data["expected"]["estimated_item_costs"]),
               Decimal("0")) == Decimal(data["expected"]["estimated_total"]) == Decimal("4955")


def test_complete_golden_flow_report_and_agent_eval(golden_report, scenario) -> None:
    validate_report(golden_report, scenario)
    assert golden_report["claim_boundary"] == PASS_CLAIM
    assert len(golden_report["required_step_results"]) == len(REQUIRED_STEPS) == 18
    assert [row["step_id"] for row in golden_report["required_step_results"]] == list(REQUIRED_STEPS)
    assert all(row["status"] == "PASS" for row in golden_report["required_step_results"])
    assert golden_report["agent_tool_trace_outcome"] == {
        "status": "PASS", "tool_sequence": [
            "get_historical_quotes", "find_similar_quotes", "compare_estimate_to_actual",
            "calculate_quote_statistics", "get_risk_evidence"],
        "provider_call_count": 6, "bounded": True,
    }
    assert golden_report["approval_workflow_result"]["ai_supplied_approval"] is False
    assert golden_report["approval_workflow_result"]["preapproval_export_blocked"] is True
    assert golden_report["storage_contract_result"]["real_s3"] is False


def test_two_fresh_runs_are_identical_and_workbook_business_results_equivalent() -> None:
    first, second, equivalent = run_twice()
    assert first is not second
    assert equivalent is True
    assert serialize_report(first) == serialize_report(second)
    assert first["excel_reconciliation_result"] == second["excel_reconciliation_result"]
    assert first["deterministic_commercial_reconciliation"] == second[
        "deterministic_commercial_reconciliation"]


@pytest.mark.parametrize("fault,failed_step", [
    ("provider_invalid", "provider_adapter"),
    ("provider_unavailable", "provider_adapter"),
    ("skip_approval", "human_approval"),
    ("excel_reconciliation_failure", "excel_reload_reconciliation"),
    ("storage_false_success", "storage_adapter"),
    ("omit_observability", "observability"),
])
def test_real_boundary_failure_injection_prevents_pass(fault: str, failed_step: str) -> None:
    report = run_once(fault=fault)
    assert report["overall_status"] == "FAIL"
    row = next(item for item in report["required_step_results"] if item["step_id"] == failed_step)
    assert row["status"] == "FAIL"
    assert report["claim_boundary"] == "No Golden Case pass claim is made."


def test_no_live_clients_are_constructed(monkeypatch) -> None:
    def forbidden(*_args, **_kwargs):
        raise AssertionError("live SDK client construction is prohibited")

    monkeypatch.setattr("ai_quotation_intelligence.bedrock.boto3.client", forbidden)
    monkeypatch.setattr("ai_quotation_intelligence.s3_storage.boto3.client", forbidden)
    assert run_once()["overall_status"] == "PASS"


def test_c17_is_unchanged_regression_only(golden_report) -> None:
    assert golden_report["c17_regression_result"] == {
        "status": "PASS", "dataset_version": "c17-golden-v1",
        "dataset_sha256": C17_DATASET_SHA256, "report_sha256": C17_REPORT_SHA256,
        "unchanged": True,
    }


def test_report_allowlist_and_privacy(golden_report) -> None:
    encoded = serialize_report(golden_report)
    for prohibited in (
        "reviewer_id", "c19-test-actor", "raw_prompt", "model_response",
        "workbook_bytes", "request_body", "aws_access_key_id", "provider_exception",
    ):
        assert prohibited not in encoded
    assert "Fictional Software Development Case 001" not in encoded


def _expect_mutation_caught(report: dict, scenario) -> None:
    with pytest.raises(ReportIntegrityError):
        validate_report(report, scenario)


def test_mutation_01_omit_required_step_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["required_step_results"].pop()
    _expect_mutation_caught(report, scenario)


def test_mutation_02_failed_step_marked_pass_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    row = report["required_step_results"][2]
    row.update({"passed": False, "status": "PASS", "failure_category": "forced_failure"})
    report.update({"overall_status": "FAIL", "bounded_failure_category": "forced_failure",
                   "claim_boundary": "No Golden Case pass claim is made."})
    _expect_mutation_caught(report, scenario)


def test_mutation_03_approval_bypass_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["approval_workflow_result"]["ai_supplied_approval"] = True
    _expect_mutation_caught(report, scenario)


def test_mutation_04_fixture_version_or_hash_weakening_is_caught(
    golden_report, scenario, tmp_path: Path,
) -> None:
    report = deepcopy(golden_report)
    report["scenario_sha256"] = "0" * 64
    _expect_mutation_caught(report, scenario)
    data = json.loads(DEFAULT_SCENARIO_PATH.read_text())
    data["scenario_version"] = "unsupported-c19-version"
    scenario_path = tmp_path / DEFAULT_SCENARIO_PATH.name
    raw = (json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()
    scenario_path.write_bytes(raw)
    scenario_path.with_suffix(".sha256").write_text(
        f"{sha256(raw).hexdigest()}  {scenario_path.name}\n")
    assert run_once(scenario_path)["overall_status"] == "ERROR"


def test_mutation_05_wrong_commercial_total_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["deterministic_commercial_reconciliation"]["actual_total"] = "4954"
    _expect_mutation_caught(report, scenario)


def test_mutation_06_fabricated_evidence_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["risk_evidence_references"]["evidence_ids"].append("fabricated-evidence")
    _expect_mutation_caught(report, scenario)


def test_mutation_07_invalid_structured_result_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["structured_output_validity"]["schema_valid"] = False
    _expect_mutation_caught(report, scenario)


def test_mutation_08_skipped_excel_reconciliation_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["excel_reconciliation_result"]["reconciled"] = False
    _expect_mutation_caught(report, scenario)


def test_mutation_09_false_storage_success_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["storage_contract_result"]["retrieved"] = False
    _expect_mutation_caught(report, scenario)


def test_mutation_10_missing_observability_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["observability_contract_result"]["events"] = []
    _expect_mutation_caught(report, scenario)


def test_mutation_11_sensitive_report_field_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["approval_workflow_result"]["reviewer_id"] = "synthetic-c19-test-actor"
    _expect_mutation_caught(report, scenario)


def test_mutation_12_scenario_tamper_without_identity_update_is_error(tmp_path: Path) -> None:
    data = json.loads(DEFAULT_SCENARIO_PATH.read_text())
    data["request"]["quotation_request"]["items"][0]["estimated_hours"]["value"] = "14"
    scenario_path = tmp_path / DEFAULT_SCENARIO_PATH.name
    scenario_path.write_text(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    scenario_path.with_suffix(".sha256").write_text(
        DEFAULT_SCENARIO_PATH.with_suffix(".sha256").read_text())
    assert run_once(scenario_path)["overall_status"] == "ERROR"


def test_mutation_13_partial_execution_reported_pass_is_caught(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["required_step_results"] = report["required_step_results"][:-2]
    report["overall_status"] = "PASS"
    _expect_mutation_caught(report, scenario)


def test_duplicate_required_step_is_integrity_error(golden_report, scenario) -> None:
    report = deepcopy(golden_report)
    report["required_step_results"].append(deepcopy(report["required_step_results"][0]))
    _expect_mutation_caught(report, scenario)
