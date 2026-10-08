from pathlib import Path

from scripts import governance_fixture_builder


def test_fixture_copy_excludes_generated_directories_and_keeps_source(
    tmp_path: Path, monkeypatch
) -> None:
    source = tmp_path / "source"
    target = tmp_path / "fixture"
    frontend = source / "frontend"

    for path in (
        source / "ordinary.txt",
        source / "AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md",
        source / "PROJECT_CONTROL.md",
        source / "QUOTATION_CARD_EVIDENCE_MAP.md",
        frontend / "src" / "App.tsx",
        frontend / "package.json",
        frontend / "vite.config.ts",
        frontend / "e2e" / "demo.spec.ts",
        frontend / "node_modules" / "example" / "index.js",
        frontend / ".playwright-browsers" / "chromium" / "browser.bin",
        frontend / "playwright-report" / "index.html",
        frontend / ".git" / "config",
        frontend / ".venv" / "bin" / "python",
        frontend / "__pycache__" / "module.pyc",
        frontend / ".pytest_cache" / "v" / "cache" / "nodeids",
        frontend / "cache.pyc",
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture content\n", encoding="utf-8")

    # This regression isolates recursive copy policy; lifecycle normalization
    # is independently exercised by the Governance Harness.
    monkeypatch.setattr(governance_fixture_builder, "cards_from", lambda _roadmap: [])
    monkeypatch.setattr(governance_fixture_builder, "normalize_control", lambda *_args: None)
    monkeypatch.setattr(
        governance_fixture_builder, "normalize_active_card_record", lambda *_args: None
    )
    monkeypatch.setattr(governance_fixture_builder, "normalize_evidence", lambda *_args: None)

    governance_fixture_builder.build(
        source,
        target,
        completed=[],
        active="",
        active_state="ACTIVE",
        next_card="",
        next_state="NOT_STARTED",
        learning_status="COMPLETE",
    )

    for relative_path in (
        "ordinary.txt",
        "frontend/src/App.tsx",
        "frontend/package.json",
        "frontend/vite.config.ts",
        "frontend/e2e/demo.spec.ts",
    ):
        assert (target / relative_path).is_file()

    for relative_path in (
        "frontend/node_modules",
        "frontend/.playwright-browsers",
        "frontend/playwright-report",
        "frontend/.git",
        "frontend/.venv",
        "frontend/__pycache__",
        "frontend/.pytest_cache",
        "frontend/cache.pyc",
    ):
        assert not (target / relative_path).exists()
