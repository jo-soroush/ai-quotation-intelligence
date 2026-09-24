"""Candidate identity uses real Git state in isolated repositories."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "candidate_identity.py"


def _git(repo: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def _git_output(repo: Path, *args: str, input: bytes | None = None) -> bytes:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        input=input,
    ).stdout


def _candidate(repo: Path, *args: str, base_ref: str = "HEAD") -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args, "--repo", str(repo), "--base-ref", base_ref],
        check=False,
        capture_output=True,
        text=True,
    )


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    root = tmp_path / "candidate"
    root.mkdir()
    _git(root, "init", "-q", "-b", "main")
    (root / "existing.txt").write_text("baseline\n", encoding="utf-8")
    (root / "deleted.txt").write_text("to delete\n", encoding="utf-8")
    _git(root, "add", "existing.txt", "deleted.txt")
    _git(root, "-c", "user.name=Candidate Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "baseline")
    (root / "existing.txt").write_text("first candidate\n", encoding="utf-8")
    return root


def _manifest(repo: Path) -> dict[str, object]:
    result = _candidate(repo, "compute")
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def _base(repo: Path) -> str:
    return subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()


def test_identity_is_deterministic_and_content_sensitive(repo: Path) -> None:
    first = _manifest(repo)
    assert first == _manifest(repo)
    assert first["paths"][0]["status"] == "M"
    (repo / "existing.txt").write_text("second candidate\n", encoding="utf-8")
    second = _manifest(repo)
    assert second["identity"] != first["identity"]
    mismatch = _candidate(repo, "verify", "--expected", first["identity"])
    assert mismatch.returncode == 1
    assert json.loads(mismatch.stdout)["identity_match"] == "FAIL"


def test_delivery_branch_preserves_content_identity_and_verification(repo: Path) -> None:
    audited = _manifest(repo)
    assert audited["branch"] == "main"
    _git(repo, "switch", "-q", "-c", "delivery/aevs-v1.1")
    delivery = _manifest(repo)
    assert delivery["branch"] == "delivery/aevs-v1.1"
    assert delivery["base"] == audited["base"]
    assert delivery["paths"] == audited["paths"]
    assert delivery["identity"] == audited["identity"]
    verified = _candidate(repo, "verify", "--expected", audited["identity"])
    assert verified.returncode == 0
    assert json.loads(verified.stdout)["branch"] == "delivery/aevs-v1.1"
    _git(repo, "add", "existing.txt")
    staged = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert staged.returncode == 0
    assert json.loads(staged.stdout)["staged_matches_worktree"] is True
    (repo / "existing.txt").write_text("first candidatr\n", encoding="utf-8")
    changed = _manifest(repo)
    assert changed["identity"] != audited["identity"]
    drift = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert drift.returncode == 1


def test_new_untracked_file_and_deletion_change_identity(repo: Path) -> None:
    first = _manifest(repo)
    (repo / "new.txt").write_text("untracked content\n", encoding="utf-8")
    added = _manifest(repo)
    assert added["identity"] != first["identity"]
    assert {entry["path"]: entry["status"] for entry in added["paths"]}["new.txt"] == "A"
    (repo / "deleted.txt").unlink()
    deleted = _manifest(repo)
    assert deleted["identity"] != added["identity"]
    assert {entry["path"]: entry["status"] for entry in deleted["paths"]}["deleted.txt"] == "D"


def test_staging_does_not_change_identity_and_delivery_checks_index(repo: Path) -> None:
    audited = _manifest(repo)
    before_stage = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert before_stage.returncode == 1
    _git(repo, "add", "existing.txt")
    assert _manifest(repo)["identity"] == audited["identity"]
    after_stage = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert after_stage.returncode == 0
    assert json.loads(after_stage.stdout)["staged_matches_worktree"] is True
    (repo / "existing.txt").write_text("unreviewed drift\n", encoding="utf-8")
    drift = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert drift.returncode == 1


def test_invalid_expected_identity_fails_closed(repo: Path) -> None:
    result = _candidate(repo, "verify", "--expected", "not-a-sha")
    assert result.returncode != 0


def test_base_revision_changes_identity_even_with_same_final_file(repo: Path) -> None:
    _git(repo, "add", "existing.txt")
    _git(repo, "-c", "user.name=Candidate Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "intermediate")
    (repo / "existing.txt").write_text("final candidate\n", encoding="utf-8")
    recent = json.loads(_candidate(repo, "compute", base_ref="HEAD").stdout)
    earlier = json.loads(_candidate(repo, "compute", base_ref="HEAD^").stdout)
    assert recent["base"] != earlier["base"]
    assert recent["paths"][0]["sha256"] == earlier["paths"][0]["sha256"]
    assert recent["identity"] != earlier["identity"]


def test_staged_check_from_subdirectory_still_covers_repository_root(repo: Path) -> None:
    nested = repo / "nested"
    nested.mkdir()
    audited = _manifest(repo)
    _git(repo, "add", "existing.txt")
    (repo / "existing.txt").write_text("unstaged root drift\n", encoding="utf-8")
    result = _candidate(nested, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    assert json.loads(result.stdout)["staged_matches_worktree"] is False


@pytest.mark.parametrize(
    ("flag", "marker"),
    [("--skip-worktree", "S"), ("--assume-unchanged", "h")],
)
def test_index_flags_cannot_hide_unaudited_staged_blob(
    repo: Path, flag: str, marker: str
) -> None:
    audited = _manifest(repo)
    (repo / "existing.txt").write_text("unaudited bytes\n", encoding="utf-8")
    _git(repo, "add", "existing.txt")
    (repo / "existing.txt").write_text("first candidate\n", encoding="utf-8")
    _git(repo, "update-index", flag, "existing.txt")
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["delivery_identity"] == audited["identity"]
    assert verdict["index_identity"] != audited["identity"]
    assert verdict["forbidden_index_flags"] == [f"existing.txt: {marker}"]


def test_replace_ref_cannot_mask_unaudited_staged_blob(repo: Path) -> None:
    audited = _manifest(repo)
    audited_blob = _git_output(repo, "hash-object", "-w", "--stdin", input=b"first candidate\n").decode().strip()

    (repo / "existing.txt").write_text("unaudited staged bytes\n", encoding="utf-8")
    _git(repo, "add", "existing.txt")
    unaudited_blob = _git_output(repo, "rev-parse", ":existing.txt").decode().strip()
    (repo / "existing.txt").write_text("first candidate\n", encoding="utf-8")
    _git(repo, "update-ref", f"refs/replace/{unaudited_blob}", audited_blob)

    # Prove the fixture reproduces ordinary cat-file's replace-ref behavior.
    assert _git_output(repo, "cat-file", "blob", unaudited_blob) == b"first candidate\n"
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["delivery_identity"] == audited["identity"]
    assert verdict["index_identity"] != audited["identity"]


def test_replace_ref_cannot_mask_unaudited_committed_blob(repo: Path) -> None:
    base = _base(repo)
    audited = _manifest(repo)
    audited_blob = _git_output(repo, "hash-object", "-w", "--stdin", input=b"first candidate\n").decode().strip()

    (repo / "existing.txt").write_text("unaudited committed bytes\n", encoding="utf-8")
    _git(repo, "add", "existing.txt")
    _git(repo, "-c", "user.name=Candidate Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "unaudited")
    committed_blob = _git_output(repo, "rev-parse", "HEAD:existing.txt").decode().strip()
    _git(repo, "update-ref", f"refs/replace/{committed_blob}", audited_blob)

    # Prove the fixture reproduces ordinary cat-file's replace-ref behavior.
    assert _git_output(repo, "cat-file", "blob", committed_blob) == b"first candidate\n"
    result = _candidate(
        repo, "verify", "--expected", audited["identity"], "--require-committed", base_ref=base
    )
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["candidate_source"] == "commit"
    assert verdict["delivery_identity"] != audited["identity"]


def test_index_flag_fails_even_when_staged_bytes_match(repo: Path) -> None:
    audited = _manifest(repo)
    _git(repo, "add", "existing.txt")
    _git(repo, "update-index", "--skip-worktree", "existing.txt")
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["index_identity"] == audited["identity"]
    assert verdict["forbidden_index_flags"] == ["existing.txt: S"]


def test_clean_filter_transformed_index_blob_is_rejected(repo: Path) -> None:
    audited = _manifest(repo)
    _git(repo, "config", "filter.upper.clean", "tr a-z A-Z")
    (repo / ".git/info/attributes").write_text("existing.txt filter=upper\n", encoding="utf-8")
    _git(repo, "add", "existing.txt")
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["delivery_identity"] == audited["identity"]
    assert verdict["index_identity"] != audited["identity"]


def test_core_filemode_false_cannot_hide_mode_mismatch(repo: Path) -> None:
    os.chmod(repo / "existing.txt", 0o755)
    audited = _manifest(repo)
    assert {entry["path"]: entry["mode"] for entry in audited["paths"]}["existing.txt"] == "100755"
    _git(repo, "config", "core.fileMode", "false")
    _git(repo, "add", "existing.txt")
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["delivery_identity"] == audited["identity"]
    assert verdict["index_identity"] != audited["identity"]


def test_extra_staged_change_is_rejected_even_when_worktree_is_audited(repo: Path) -> None:
    audited = _manifest(repo)
    _git(repo, "add", "existing.txt")
    (repo / "deleted.txt").write_text("not audited\n", encoding="utf-8")
    _git(repo, "add", "deleted.txt")
    (repo / "deleted.txt").write_text("to delete\n", encoding="utf-8")
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert result.returncode == 1
    verdict = json.loads(result.stdout)
    assert verdict["delivery_identity"] == audited["identity"]
    assert verdict["index_identity"] != audited["identity"]


def test_staged_new_file_missing_from_worktree_fails_closed(repo: Path) -> None:
    (repo / "extra.txt").write_text("staged only\n", encoding="utf-8")
    _git(repo, "add", "extra.txt")
    (repo / "extra.txt").unlink()
    result = _candidate(repo, "compute")
    assert result.returncode == 2
    assert "missing new candidate file: extra.txt" in result.stderr


def test_untracked_addition_requires_exact_staged_blob(repo: Path) -> None:
    (repo / "new.txt").write_text("audited addition\n", encoding="utf-8")
    audited = _manifest(repo)
    _git(repo, "add", "existing.txt")
    missing = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert missing.returncode == 1
    _git(repo, "add", "new.txt")
    matched = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert matched.returncode == 0
    (repo / "new.txt").write_text("transformed staging\n", encoding="utf-8")
    _git(repo, "add", "new.txt")
    (repo / "new.txt").write_text("audited addition\n", encoding="utf-8")
    transformed = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert transformed.returncode == 1


def test_audited_deletion_requires_absence_from_index(repo: Path) -> None:
    (repo / "deleted.txt").unlink()
    audited = _manifest(repo)
    _git(repo, "add", "existing.txt")
    still_indexed = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert still_indexed.returncode == 1
    _git(repo, "add", "-u", "deleted.txt")
    absent = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert absent.returncode == 0


def test_unaudited_committed_blob_fails_committed_verification(repo: Path) -> None:
    base = _base(repo)
    audited = _manifest(repo)
    (repo / "existing.txt").write_text("unaudited bytes\n", encoding="utf-8")
    _git(repo, "add", "existing.txt")
    _git(repo, "-c", "user.name=Candidate Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "unaudited")
    result = _candidate(repo, "verify", "--expected", audited["identity"], "--require-committed", base_ref=base)
    assert result.returncode == 1
    assert json.loads(result.stdout)["candidate_source"] == "commit"


def test_exact_committed_tree_passes_and_branch_stays_provenance(repo: Path) -> None:
    base = _base(repo)
    audited = _manifest(repo)
    _git(repo, "switch", "-q", "-c", "delivery/aevs-v1.1")
    _git(repo, "add", "existing.txt")
    staged = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged", base_ref=base)
    assert staged.returncode == 0
    _git(repo, "-c", "user.name=Candidate Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "audited")
    committed = _candidate(repo, "verify", "--expected", audited["identity"], "--require-committed", base_ref=base)
    assert committed.returncode == 0
    verdict = json.loads(committed.stdout)
    assert verdict["candidate_source"] == "commit"
    assert verdict["branch"] == "delivery/aevs-v1.1"
    assert verdict["delivery_identity"] == audited["identity"]


def test_symlink_addition_uses_link_target_bytes(repo: Path) -> None:
    (repo / "link.txt").symlink_to("existing.txt")
    audited = _manifest(repo)
    _git(repo, "add", "existing.txt", "link.txt")
    staged = _candidate(repo, "verify", "--expected", audited["identity"], "--require-staged")
    assert staged.returncode == 0
    assert {entry["path"]: entry["mode"] for entry in audited["paths"]}["link.txt"] == "120000"
