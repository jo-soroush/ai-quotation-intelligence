"""C20 non-production composition over the unchanged C13 HTTP contract."""

from pathlib import Path

from fastapi.testclient import TestClient

from ai_quotation_intelligence.api import XLSX_MIME
from demo.c20_backend import build_app


def payload(project_name: str = "Synthetic platform modernisation demo") -> dict:
    return {
        "request_id": "c20-python-demo",
        "quotation_request": {
            "project_name": project_name,
            "currency": "SEK",
            "requested_at": "2026-10-06T09:00:00Z",
            "items": [
                {
                    "item_id": "demo-discovery",
                    "description": "Platform discovery and solution design",
                    "estimated_hours": {"value": "12", "unit": "hours"},
                    "hourly_rate": {"amount": "110", "currency": "SEK"},
                },
                {
                    "item_id": "demo-delivery",
                    "description": "Synthetic platform implementation",
                    "estimated_hours": {"value": "20", "unit": "hours"},
                    "hourly_rate": {"amount": "125", "currency": "SEK"},
                },
                {
                    "item_id": "demo-validation",
                    "description": "Integration and quality validation",
                    "estimated_hours": {"value": "8", "unit": "hours"},
                    "hourly_rate": {"amount": "100", "currency": "SEK"},
                },
            ],
        },
    }


def test_demo_composition_exercises_real_draft_evidence_review_and_excel() -> None:
    client = TestClient(build_app(), raise_server_exceptions=False)
    drafted = client.post("/quotes/draft", json=payload())
    assert drafted.status_code == 200
    quote_id = drafted.json()["quote_id"]

    view = client.get(f"/quotes/{quote_id}")
    assert view.status_code == 200
    body = view.json()
    assert body["draft_quote"]["quote"]["estimated_total_cost"] == {
        "amount": "4620", "currency": "SEK",
    }
    assert body["similar_quotes"]
    assert body["comparisons"]
    assert body["risk_evidence"]
    assert body["message"] == (
        "Validated historical risk evidence is linked to this draft for human review."
    )
    assert body["review_state"] == "awaiting_review"

    blocked = client.post(f"/quotes/{quote_id}/export")
    assert (blocked.status_code, blocked.json()) == (409, {"code": "approval_required"})
    approved = client.post(f"/quotes/{quote_id}/approve", json={
        "status": "approved", "reviewer_id": "synthetic-demo-reviewer",
    })
    assert (approved.status_code, approved.json()["review_state"]) == (200, "approved")
    exported = client.post(f"/quotes/{quote_id}/export")
    assert exported.status_code == 200
    assert exported.headers["content-type"] == XLSX_MIME
    assert exported.content.startswith(b"PK")


def test_demo_composition_provider_failure_is_explicit_and_creates_no_quote() -> None:
    client = TestClient(build_app(), raise_server_exceptions=False)
    response = client.post("/quotes/draft", json=payload("Synthetic Provider Failure"))
    assert (response.status_code, response.json()) == (503, {"code": "agent_unavailable"})
    assert client.get("/quotes/draft-c20-python-demo").status_code == 404


def test_demo_composition_never_constructs_live_provider_client(monkeypatch) -> None:
    def forbidden(*_args, **_kwargs):
        raise AssertionError("live provider client must not be constructed")

    monkeypatch.setattr("ai_quotation_intelligence.bedrock.boto3.client", forbidden)
    client = TestClient(build_app(), raise_server_exceptions=False)
    assert client.post("/quotes/draft", json=payload()).status_code == 200


def test_demo_launcher_is_nonproduction_and_independent_of_c19_runtime() -> None:
    source = (Path(__file__).parents[1] / "demo" / "c20_backend.py").read_text()
    assert "evaluation.c19" not in source
    assert "evaluation/c19" not in source
    assert "boto3.client" not in source
    assert "127.0.0.1" in source


def test_frontend_contract_matches_current_fastapi_openapi() -> None:
    schema = build_app().openapi()
    assert set(schema["paths"]) == {
        "/health",
        "/quotes/analyze",
        "/quotes/draft",
        "/quotes/{id}",
        "/quotes/{id}/approve",
        "/quotes/{id}/export",
    }
    hours = schema["components"]["schemas"]["RequestHours"]
    assert set(hours["required"]) == {"value", "unit"}
    quote_view = schema["components"]["schemas"]["QuoteView"]
    assert {"message", "similar_quotes", "comparisons", "risk_evidence"} <= set(quote_view["properties"])
    decision = schema["components"]["schemas"]["DecisionInput"]
    assert set(decision["required"]) == {"status", "reviewer_id"}
    assert "200" in schema["paths"]["/quotes/{id}/export"]["post"]["responses"]
