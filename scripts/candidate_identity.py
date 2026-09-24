#!/usr/bin/env python3
"""Read-only content identity for the exact Git candidate awaiting audit.

Includes changes committed after the base, staged/unstaged changes, and all
visible untracked files. Ignored files are outside the delivery candidate.
Branch is reported as provenance but is not hashed. No identity is written
into the candidate itself.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys


SCHEMA = "aqi-candidate-v1"
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")


class CandidateError(Exception):
    """Candidate cannot be identified or safely compared."""


def _git(repo: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "--no-replace-objects", "-C", str(repo), *args],
        capture_output=True,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise CandidateError(f"git {' '.join(args)} failed: {detail}")
    return result.stdout


def _safe_path(raw: bytes) -> str:
    name = os.fsdecode(raw)
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or name in {"", "."}:
        raise CandidateError(f"invalid candidate path: {name!r}")
    return name


def _paths(raw: bytes) -> set[str]:
    return {_safe_path(item) for item in raw.split(b"\0") if item}


def _file_identity(root: Path, name: str) -> tuple[str, str] | None:
    path = root / name
    try:
        info = path.lstat()
    except FileNotFoundError:
        return None
    if stat.S_ISLNK(info.st_mode):
        content = os.fsencode(os.readlink(path))
        mode = "120000"
    elif stat.S_ISREG(info.st_mode):
        content = path.read_bytes()
        mode = "100755" if info.st_mode & 0o111 else "100644"
    else:
        raise CandidateError(f"unsupported candidate file type: {name}")
    return mode, hashlib.sha256(content).hexdigest()


def _git_blob_identity(root: Path, mode: str, oid: str) -> tuple[str, str]:
    if mode not in {"100644", "100755", "120000"}:
        raise CandidateError(f"unsupported Git candidate mode: {mode}")
    return mode, hashlib.sha256(_git(root, "cat-file", "blob", oid)).hexdigest()


def _tree_state(root: Path, revision: str) -> dict[str, tuple[str, str]]:
    state = {}
    for item in _git(root, "ls-tree", "-r", "-z", revision).split(b"\0"):
        if not item:
            continue
        header, raw_path = item.split(b"\t", 1)
        mode, _kind, oid = header.decode("ascii").split(" ")
        state[_safe_path(raw_path)] = _git_blob_identity(root, mode, oid)
    return state


def _index_state(root: Path) -> dict[str, tuple[str, str]]:
    state = {}
    for item in _git(root, "ls-files", "--stage", "-z").split(b"\0"):
        if not item:
            continue
        header, raw_path = item.split(b"\t", 1)
        mode, oid, stage = header.decode("ascii").split(" ")
        if stage != "0":
            raise CandidateError("unresolved Git index entries")
        state[_safe_path(raw_path)] = _git_blob_identity(root, mode, oid)
    return state


def _worktree_state(
    root: Path, names: set[str], required_present: set[str]
) -> dict[str, tuple[str, str]]:
    state = {}
    for name in names:
        identity = _file_identity(root, name)
        if identity is not None:
            state[name] = identity
        elif name in required_present:
            raise CandidateError(f"missing new candidate file: {name}")
    return state


def _candidate_entries(
    base: dict[str, tuple[str, str]], state: dict[str, tuple[str, str]]
) -> list[dict[str, str]]:
    entries = []
    for name in sorted(base.keys() | state.keys()):
        if base.get(name) == state.get(name):
            continue
        if name not in state:
            mode, digest, status = "deleted", "-", "D"
        else:
            mode, digest = state[name]
            status = "M" if name in base else "A"
        entries.append({"path": name, "status": status, "mode": mode, "sha256": digest})
    return entries


def _forbidden_index_flags(root: Path, candidate_paths: set[str]) -> list[str]:
    forbidden = []
    for item in _git(root, "ls-files", "-v", "-z").split(b"\0"):
        if not item:
            continue
        if item[1:2] != b" ":
            raise CandidateError("unexpected Git index flag format")
        marker = item[:1].decode("ascii")
        name = _safe_path(item[2:])
        if name in candidate_paths and (marker == "S" or marker.islower()):
            forbidden.append(f"{name}: {marker}")
    return sorted(forbidden)


def candidate_manifest(
    repo: Path, base_ref: str, source: str = "worktree"
) -> dict[str, object]:
    if not base_ref or base_ref.startswith("-"):
        raise CandidateError("base ref must be an explicit Git revision")
    root = Path(os.fsdecode(_git(repo, "rev-parse", "--show-toplevel").removesuffix(b"\n")))
    if _git(root, "ls-files", "-u", "-z"):
        raise CandidateError("unresolved Git index entries")
    base = _git(root, "merge-base", "HEAD", base_ref).decode("ascii").strip()
    branch = _git(root, "symbolic-ref", "--quiet", "--short", "HEAD").decode("utf-8").strip()
    base_state = _tree_state(root, base)
    if source == "worktree":
        index_state = _index_state(root)
        untracked = _paths(_git(root, "ls-files", "--others", "--exclude-standard", "-z"))
        added = (index_state.keys() - base_state.keys()) | untracked
        state = _worktree_state(root, base_state.keys() | index_state.keys() | untracked, added)
    elif source == "index":
        state = _index_state(root)
    elif source == "commit":
        state = _tree_state(root, "HEAD")
    else:
        raise CandidateError(f"unknown candidate source: {source}")
    entries = _candidate_entries(base_state, state)
    if source == "worktree" and not entries:
        raise CandidateError("candidate contains no changed or untracked files")
    return {"schema": SCHEMA, "base": base, "branch": branch, "paths": entries}


def candidate_identity(manifest: dict[str, object]) -> str:
    # Branch names describe workflow location, not candidate content. Keep the
    # audited base and exact file manifest bound to the one content identity.
    content = {key: manifest[key] for key in ("schema", "base", "paths")}
    canonical = json.dumps(content, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("compute", "verify"))
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--base-ref", default="origin/main")
    parser.add_argument("--expected", help="identity from the independent verifier's audit record")
    parser.add_argument("--require-staged", action="store_true")
    parser.add_argument("--require-committed", action="store_true")
    args = parser.parse_args()

    if args.command == "verify" and (args.expected is None or not SHA256_RE.fullmatch(args.expected)):
        parser.error("verify requires --expected with a 64-character lowercase SHA-256 identity")
    if args.require_staged and args.require_committed:
        parser.error("--require-staged and --require-committed are mutually exclusive")
    if args.command == "compute" and (args.expected is not None or args.require_staged or args.require_committed):
        parser.error("--expected, --require-staged and --require-committed are only valid for verify")

    try:
        source = "commit" if args.require_committed else "worktree"
        manifest = candidate_manifest(args.repo, args.base_ref, source)
        identity = candidate_identity(manifest)
        if args.command == "compute":
            print(json.dumps({"identity": identity, **manifest}, sort_keys=True, indent=2))
            return 0
        index_identity = None
        forbidden_flags: list[str] = []
        if args.require_staged:
            index_manifest = candidate_manifest(args.repo, args.base_ref, "index")
            index_identity = candidate_identity(index_manifest)
            paths = {entry["path"] for entry in manifest["paths"] + index_manifest["paths"]}
            root = Path(os.fsdecode(_git(args.repo, "rev-parse", "--show-toplevel").removesuffix(b"\n")))
            forbidden_flags = _forbidden_index_flags(root, paths)
        staged_match = (
            index_identity == identity and not forbidden_flags if args.require_staged else None
        )
        matched = identity == args.expected and staged_match is not False
        print(json.dumps({
            "identity_match": "PASS" if matched else "FAIL",
            "audited_identity": args.expected,
            "delivery_identity": identity,
            "candidate_source": source,
            "index_identity": index_identity,
            "forbidden_index_flags": forbidden_flags,
            "staged_matches_worktree": staged_match,
            "base": manifest["base"],
            "branch": manifest["branch"],
            "paths": manifest["paths"],
        }, sort_keys=True, indent=2))
        return 0 if matched else 1
    except (CandidateError, OSError, UnicodeError) as error:
        print(f"CANDIDATE_IDENTITY: FAIL — {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
