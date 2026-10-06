"""Local-only C20 server using real FastAPI contracts and deterministic clients.

The tiny HTTP bridge exists only because the repository's approved Python
environment has no ASGI server dependency. It delegates all route, validation,
agent, review, and Excel behavior to the real process-local FastAPI app.
"""

from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import sys
from threading import RLock
from typing import Any, Final

ROOT: Final = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fastapi.testclient import TestClient  # noqa: E402

from ai_quotation_intelligence.agent_tools import AgentTools  # noqa: E402
from ai_quotation_intelligence.api import LocalQuoteStore, create_app  # noqa: E402
from ai_quotation_intelligence.bedrock import BedrockConverseAdapter  # noqa: E402
from ai_quotation_intelligence.config import Settings  # noqa: E402
from ai_quotation_intelligence.quotation_agent import QuotationAgent  # noqa: E402


_REQUEST_ID = re.compile(r'"request_id":"([A-Za-z0-9._-]{1,64})"')
_FAILURE_PROJECT = '"project_name":"Synthetic Provider Failure"'
_TRACE: Final[tuple[dict[str, Any], ...]] = (
    {"kind": "tool", "name": "get_historical_quotes", "arguments": {}},
    {"kind": "tool", "name": "find_similar_quotes", "arguments": {"limit": 5}},
    {"kind": "tool", "name": "compare_estimate_to_actual", "arguments": {}},
    {"kind": "tool", "name": "calculate_quote_statistics", "arguments": {"metric": "hours"}},
    {"kind": "tool", "name": "get_risk_evidence", "arguments": {"metric": "hours"}},
    {
        "kind": "final",
        "narrative": "Validated historical risk evidence is linked to this draft for human review.",
        "evidence_ids": ["risk-hours-overrun-rate"],
        "risk_suggestions": [
            {"severity": "medium", "evidence_ids": ["risk-hours-overrun-rate"]},
        ],
        "missing_information": [],
    },
)


class DemoConverseClient:
    """Per-request fixed provider transport; never constructs a live SDK client."""

    def __init__(self) -> None:
        self._next: dict[str, int] = {}
        self._lock = RLock()

    def converse(self, **kwargs: Any) -> dict[str, Any]:
        messages = kwargs.get("messages")
        try:
            prompt = messages[0]["content"][0]["text"]
        except (KeyError, IndexError, TypeError):
            return {"output": {"message": {"content": []}}}
        if _FAILURE_PROJECT in prompt:
            raise RuntimeError("synthetic provider unavailable")
        match = _REQUEST_ID.search(prompt)
        if match is None:
            return {"output": {"message": {"content": []}}}
        request_id = match.group(1)
        with self._lock:
            index = self._next.get(request_id, 0)
            if index >= len(_TRACE):
                return {"output": {"message": {"content": []}}}
            self._next[request_id] = index + 1
            action = _TRACE[index]
        text = json.dumps(action, sort_keys=True, separators=(",", ":"))
        return {
            "output": {"message": {"content": [{"text": text}]}},
            "usage": {"inputTokens": 1, "outputTokens": 1, "totalTokens": 2},
        }


def build_app():
    client = DemoConverseClient()
    model = BedrockConverseAdapter(settings=Settings(environment="c20-local-demo"), client=client)
    return create_app(QuotationAgent(model, AgentTools()), store=LocalQuoteStore())


class DemoHandler(BaseHTTPRequestHandler):
    client: TestClient

    def do_GET(self) -> None:  # noqa: N802
        self._forward("GET")

    def do_POST(self) -> None:  # noqa: N802
        self._forward("POST")

    def _forward(self, method: str) -> None:
        length_header = self.headers.get("Content-Length", "0")
        length = int(length_header) if length_header.isdecimal() else 0
        body = self.rfile.read(length) if length else None
        headers = {
            key: value for key, value in self.headers.items()
            if key.lower() in {"content-type", "accept"}
        }
        response = self.client.request(method, self.path, content=body, headers=headers)
        self.send_response(response.status_code)
        for key in ("content-type", "content-disposition"):
            value = response.headers.get(key)
            if value is not None:
                self.send_header(key, value)
        self.send_header("Content-Length", str(len(response.content)))
        self.end_headers()
        self.wfile.write(response.content)

    def log_message(self, format: str, *args: object) -> None:
        print(f"c20-demo {self.address_string()} {format % args}")


def main() -> None:
    host = "127.0.0.1"
    port = int(os.getenv("AQI_DEMO_PORT", "8765"))
    app = build_app()
    try:
        with TestClient(app, raise_server_exceptions=False) as client:
            DemoHandler.client = client
            server = ThreadingHTTPServer((host, port), DemoHandler)
            print(f"C20 local demo backend listening at http://{host}:{port}", flush=True)
            try:
                server.serve_forever()
            finally:
                server.server_close()
    except KeyboardInterrupt:
        print("C20 local demo backend stopped.", flush=True)


if __name__ == "__main__":
    main()
