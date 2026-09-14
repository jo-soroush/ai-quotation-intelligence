#!/usr/bin/env python3
"""Build an isolated governance fixture with explicitly declared Card state."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


CARD_RE = re.compile(r"^## (V1-C(?:0[1-9]|1[0-9]|20)) — (.+)$")


def cards_from(roadmap: str) -> list[tuple[str, str]]:
    cards = [match.groups() for match in map(CARD_RE.match, roadmap.splitlines()) if match]
    if not cards:
        raise ValueError("roadmap contains no Cards")
    return cards


def parse_cards(value: str) -> list[str]:
    if not value or value == "NONE":
        return []
    cards = [item.strip() for item in value.split(",") if item.strip()]
    if any(not re.fullmatch(r"V1-C(?:0[1-9]|1[0-9]|20)", card) for card in cards):
        raise ValueError(f"invalid Card list: {value}")
    return cards


def replace_section_value(text: str, start: int, end: int, label: str, value: str) -> str:
    block = text[start:end]
    pattern = re.compile(rf"^{re.escape(label)}.*$", re.MULTILINE)
    if not pattern.search(block):
        raise ValueError(f"missing fixture field: {label}")
    block = pattern.sub(f"{label}{value}", block, count=1)
    return text[:start] + block + text[end:]


def section_bounds(text: str, heading: str) -> tuple[int, int]:
    start = text.find(heading)
    if start < 0:
        raise ValueError(f"missing section: {heading}")
    next_heading = text.find("\n## ", start + len(heading))
    return start, len(text) if next_heading < 0 else next_heading


def replace_field_in_section(text: str, heading: str, label: str, value: str) -> str:
    start, end = section_bounds(text, heading)
    return replace_section_value(text, start, end, label, value)


def normalize_active_card_record(path: Path, cards: list[tuple[str, str]], completed: list[str], active: str, active_state: str) -> None:
    text = path.read_text()
    record_card = active or (completed[-1] if completed else "NONE")
    record_title = dict(cards).get(record_card, "")
    record_state = active_state if active else "COMPLETE" if completed else "NOT_STARTED"
    number = int(record_card.split("-C", 1)[1]) if record_card != "NONE" else 0
    delivery = f"fixture-{number:02d}-delivery" if completed and not active else "NOT_CREATED"
    pr = f"MERGED — #{number}" if completed and not active else "NOT_CREATED"
    merge = (f"{number:02x}" * 40)[:40] if completed and not active else "NOT_CREATED"
    heading = "## 5. Active Card Record"
    start, end = section_bounds(text, heading)
    block = text[start:end]
    replacements = [
        (r"^Card ID:.*$", f"Card ID: {record_card}"),
        (r"^Title:.*$", f"Title: {record_title}"),
        (r"^State:.*$", f"State: {record_state}"),
        (r"^Delivery Commit:.*$", f"Delivery Commit: {delivery}"),
        (r"^PR:.*$", f"PR: {pr}"),
        (r"^Merge Commit:.*$", f"Merge Commit: {merge}"),
    ]
    for pattern, replacement in replacements:
        block, count = re.subn(pattern, replacement, block, count=1, flags=re.MULTILINE)
        if count != 1:
            raise ValueError(f"missing Active Card Record field: {pattern}")
    path.write_text(text[:start] + block + text[end:])


def control_state(active: str, active_state: str, completed: list[str], next_card: str) -> str:
    if active:
        return f"{active.replace('-', '_')}_{active_state}"
    if completed:
        return f"{completed[-1].replace('-', '_')}_COMPLETE"
    return "READY_FOR_V1_C01_AUTHORIZATION"


def normalize_control(path: Path, cards: list[tuple[str, str]], completed: list[str], active: str, active_state: str, next_card: str, next_state: str) -> None:
    text = path.read_text()
    current_heading = "## 2. Current Project State"
    current_start, current_end = section_bounds(text, current_heading)
    phase = control_state(active, active_state, completed, next_card)
    last = completed[-1] if completed else "NONE"
    last_title = dict(cards).get(last, "")
    next_title = dict(cards).get(next_card, "")
    active_value = active or "NONE"
    active_value_with_title = active_value if active_value == "NONE" else f"{active}"
    authorization = f"{completed[-1].replace('V1-', '')} scope authorization consumed by completion; later Cards not authorized" if not active and completed else ("NONE — no Card currently authorized" if not active else f"{active} — explicit fixture authorization")
    text = replace_section_value(text, current_start, current_end, "Project Phase: ", phase)
    current_start, current_end = section_bounds(text, current_heading)
    for label, value in [
        ("Active Card: ", active_value_with_title),
        ("Active Card State: ", active_state if active else "NONE"),
        ("Last COMPLETE Card: ", f"{last} — {last_title}" if last else "NONE"),
        ("Next Roadmap Card: ", f"{next_card} — {next_title}" if next_card else "NONE"),
        ("Next Card Authorized: ", "NO — fixture does not authorize a later Card"),
        ("Implementation Authorization: ", authorization),
    ]:
        text = replace_field_in_section(text, current_heading, label, value)

    roadmap_heading = "## 7. Roadmap Position"
    completed_value = "; ".join(f"{card} — {dict(cards)[card]}" for card in completed) if completed else "NONE"
    text = replace_field_in_section(text, roadmap_heading, "Completed Cards: ", completed_value)
    text = replace_field_in_section(text, roadmap_heading, "Active Card: ", active_value)
    text = replace_field_in_section(text, roadmap_heading, "Next Roadmap Card: ", f"{next_card} — {next_title}" if next_card else "NONE")
    text = replace_field_in_section(text, roadmap_heading, "Later Cards: ", "NOT_AUTHORIZED")

    table_heading = "## 18. V1 Card Status Table"
    table_start, table_end = section_bounds(text, table_heading)
    table = text[table_start:table_end]
    lines = []
    for line in table.splitlines():
        match = re.match(r"^\| (V1-C(?:0[1-9]|1[0-9]|20)) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$", line)
        if not match:
            lines.append(line)
            continue
        card, title = match.group(1), match.group(2).strip()
        state = active_state if card == active else "COMPLETE" if card in completed else "NOT_STARTED"
        approval = "YES" if card == active or card in completed else "NO"
        quality = "PASS" if card == active or card in completed else "NOT_RUN"
        evidence = "PRESENT" if card == active or card in completed else "PENDING"
        lines.append(f"| {card} | {title} | {state} | {approval} | {quality} | {evidence} |")
    text = text[:table_start] + "\n".join(lines) + text[table_end:]
    path.write_text(text)


def card_sections(text: str) -> dict[str, tuple[int, int]]:
    matches = list(re.finditer(r"^## (V1-C(?:0[1-9]|1[0-9]|20)) — .+$", text, re.MULTILINE))
    result: dict[str, tuple[int, int]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        result[match.group(1)] = (match.start(), end)
    return result


def normalize_evidence(path: Path, cards: list[tuple[str, str]], completed: list[str], active: str, active_state: str, learning_status: str) -> None:
    text = path.read_text()
    # Work from the end so section offsets remain stable.
    for card, _ in reversed(cards):
        start, end = card_sections(text)[card]
        block = text[start:end]
        is_complete = card in completed
        is_active = card == active
        state = "COMPLETE" if is_complete else active_state if is_active else "NOT_STARTED"
        approval = "YES" if is_complete or is_active else "NO"
        tests = "PASS — fixture evidence" if is_complete or is_active else "NOT_RUN"
        exit_status = "PROVEN" if is_complete or is_active else "NOT_PROVEN"
        quality = "PASS" if is_complete or is_active else "NOT_RUN"
        recommendation = "COMPLETE" if is_complete else active_state if is_active else "NOT_STARTED"
        card_number = int(card.split("-C", 1)[1])
        fixture_hash = (f"{card_number:02x}" * 40)[:40]
        replacements = [
            (r"(### 5\. Files Changed\n\n)[^\n]+", rf"\1{'PRESENT — fixture implementation evidence' if is_complete or is_active else 'NONE'}"),
            (r"(### 3\. State\n\n)[^\n]+", rf"\1{state}"),
            (r"(### 4\. Human Start Approval\n\n)[^\n]+", rf"\1{approval}"),
            (r"(### 7\. Focused Tests\n\n)[^\n]+", rf"\1{tests}"),
            (r"(Exit Gate Status:\s*)[^\n]+", rf"\1{exit_status}"),
            (r"(### 15\. CARD_QUALITY_GATE\n\n)[^\n]+", rf"\1{quality}"),
            (r"(### 20\. Recommended State\n\n)[^\n]+", rf"\1{recommendation}"),
            (r"(Learning Documentation Status:\n)[^\n]+", rf"\1{learning_status if is_complete or is_active else 'NOT_STARTED'}"),
        ]
        if is_complete:
            replacements.extend([
                (r"(### 19\. Completion Evidence\n\n)[^\n]+", rf"\1COMPLETE — fixture completion evidence recorded."),
                (r"(### 16\. Git Evidence\n\n)[\s\S]*?(?=\n### 17\.)", rf"\1Fixture delivery evidence: PR #{card_number} merged to main at merge commit {fixture_hash}.\n"),
            ])
        for pattern, replacement in replacements:
            block, count = re.subn(pattern, replacement, block, count=1)
            if count != 1:
                raise ValueError(f"missing Evidence Map field for {card}: {pattern}")
        text = text[:start] + block + text[end:]
    path.write_text(text)


def build(source_root: Path, target_root: Path, completed: list[str], active: str, active_state: str, next_card: str, next_state: str, learning_status: str) -> None:
    if target_root.exists() and any(target_root.iterdir()):
        raise ValueError(f"fixture target is not empty: {target_root}")
    target_root.mkdir(parents=True, exist_ok=True)
    ignore = shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache", "*.pyc")
    for item in source_root.iterdir():
        if item.name in {".git", ".venv", "__pycache__", ".pytest_cache"}:
            continue
        destination = target_root / item.name
        if item.is_dir():
            shutil.copytree(item, destination, ignore=ignore)
        else:
            shutil.copy2(item, destination)

    roadmap = (target_root / "AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md").read_text()
    cards = cards_from(roadmap)
    card_ids = {card for card, _ in cards}
    if any(card not in card_ids for card in completed + ([active] if active else []) + ([next_card] if next_card else [])):
        raise ValueError("fixture references a Card not present in the Roadmap")
    if active and active in completed:
        raise ValueError("fixture Card cannot be both active and completed")
    if active and active_state not in {"ACTIVE", "READY_FOR_DELIVERY"}:
        raise ValueError("active fixture state must be ACTIVE or READY_FOR_DELIVERY")
    normalize_control(target_root / "PROJECT_CONTROL.md", cards, completed, active, active_state, next_card, next_state)
    normalize_active_card_record(target_root / "PROJECT_CONTROL.md", cards, completed, active, active_state)
    normalize_evidence(target_root / "QUOTATION_CARD_EVIDENCE_MAP.md", cards, completed, active, active_state, learning_status)
    print(str(target_root))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--completed", default="NONE")
    parser.add_argument("--active", default="NONE")
    parser.add_argument("--active-state", default="ACTIVE")
    parser.add_argument("--next", dest="next_card", default="NONE")
    parser.add_argument("--next-state", default="NOT_STARTED")
    parser.add_argument("--learning-status", choices={"CURRENT", "COMPLETE"}, default="COMPLETE")
    args = parser.parse_args()
    build(args.source_root.resolve(), args.root.resolve(), parse_cards(args.completed), "" if args.active == "NONE" else args.active, args.active_state, "" if args.next_card == "NONE" else args.next_card, args.next_state, args.learning_status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
