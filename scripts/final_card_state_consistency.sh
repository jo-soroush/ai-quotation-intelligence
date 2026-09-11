#!/usr/bin/env bash
set -u

ROOT="${1:-$(pwd)}"
cd "$ROOT" || exit 2

failures=0
check() {
  local description="$1"
  local file="$2"
  local expected="$3"
  if grep -Fq "$expected" "$file"; then
    printf 'PASS  %s\n' "$description"
  else
    printf 'FAIL  %s — missing: %s\n' "$description" "$expected"
    failures=$((failures + 1))
  fi
}

check_first() {
  local description="$1"
  local file="$2"
  local prefix="$3"
  local expected="$4"
  local actual
  actual="$(awk -v prefix="$prefix" 'index($0, prefix) == 1 { print; exit }' "$file")"
  if [[ "$actual" == "$expected" ]]; then
    printf 'PASS  %s\n' "$description"
  else
    printf 'FAIL  %s — observed: %s\n' "$description" "${actual:-NOT_FOUND}"
    failures=$((failures + 1))
  fi
}

check_section() {
  local description="$1"
  local file="$2"
  local start="$3"
  local end="$4"
  local expected="$5"
  local section
  section="$(awk -v start="$start" -v end="$end" 'index($0, start) { inside=1 } inside && end != "" && index($0, end) && $0 !~ start { exit } inside { print }' "$file")"
  if grep -Fq "$expected" <<<"$section"; then
    printf 'PASS  %s\n' "$description"
  else
    printf 'FAIL  %s — missing: %s\n' "$description" "$expected"
    failures=$((failures + 1))
  fi
}

printf 'FINAL_CARD_STATE_CONSISTENCY_GATE\n'

current_head="$(git rev-parse HEAD 2>/dev/null || printf '%s' NOT_AVAILABLE)"
check "PROJECT_CONTROL is complete" PROJECT_CONTROL.md "Project Phase: V1_C01_COMPLETE"
check_first "PROJECT_CONTROL has no active Card" PROJECT_CONTROL.md "Active Card:" "Active Card: NONE"
check "PROJECT_CONTROL records C01 as last complete Card" PROJECT_CONTROL.md "Last COMPLETE Card: V1-C01 — Repository Baseline"
check "PROJECT_CONTROL records C01 quality PASS" PROJECT_CONTROL.md "CARD_QUALITY_GATE: PASS"
check "PROJECT_CONTROL records delivery approval consumed" PROJECT_CONTROL.md "GIT_DELIVERY_APPROVAL: GRANTED / CONSUMED — PR #1 merged"
check "PROJECT_CONTROL records merged PR" PROJECT_CONTROL.md "PR: MERGED — #1"
check "PROJECT_CONTROL records the actual HEAD" PROJECT_CONTROL.md "HEAD commit: $current_head"

check_first "Evidence Map current Card is none" QUOTATION_CARD_EVIDENCE_MAP.md "Active Card:" "Active Card: NONE"
check "Evidence Map authorization is historical" QUOTATION_CARD_EVIDENCE_MAP.md "Authorization: C01 start approval recorded historically; no active Card"
check_section "Evidence Map C01 detailed state is complete" QUOTATION_CARD_EVIDENCE_MAP.md "## V1-C01 — Repository Baseline" "## V1-C02 — Domain Models" $'\nCOMPLETE'
check_section "Evidence Map C01 detailed Exit Gate is proven" QUOTATION_CARD_EVIDENCE_MAP.md "## V1-C01 — Repository Baseline" "## V1-C02 — Domain Models" "Exit Gate Status: PROVEN"
check_section "Evidence Map C01 detailed quality gate passes" QUOTATION_CARD_EVIDENCE_MAP.md "## V1-C01 — Repository Baseline" "## V1-C02 — Domain Models" "completion delivery and reconciliation are recorded."
check_section "Evidence Map C01 recommended state is complete" QUOTATION_CARD_EVIDENCE_MAP.md "## V1-C01 — Repository Baseline" "## V1-C02 — Domain Models" $'\nCOMPLETE'
check "Evidence Map Current Card Table is reconciled" QUOTATION_CARD_EVIDENCE_MAP.md "| V1-C01 | Repository Baseline | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |"
check "Evidence Map C02 remains unauthorized and unstarted" QUOTATION_CARD_EVIDENCE_MAP.md "| V1-C02 | Domain Models | NOT_STARTED | NO | NOT_RUN | NOT_PROVEN | NOT_RUN | NONE | NOT_STARTED |"
check "Evidence Map Current Summary Exit Gate is proven" QUOTATION_CARD_EVIDENCE_MAP.md "V1-C01 Exit Gate Evidence is PROVEN; later Card Exit Gates are NOT_PROVEN."
check "Evidence Map Current Summary records C01 complete" QUOTATION_CARD_EVIDENCE_MAP.md "V1-C01 is COMPLETE; later Cards are NOT_STARTED."
c01_section="$(awk '/^## V1-C01 — Repository Baseline/{inside=1} /^## V1-C02 — Domain Models/{inside=0} inside {print}' QUOTATION_CARD_EVIDENCE_MAP.md)"
if grep -Fq "Learning Documentation Status:" <<<"$c01_section" && grep -Fq "CURRENT" <<<"$c01_section"; then
  printf 'PASS  Evidence Map C01 learning documentation is current\n'
else
  printf 'FAIL  Evidence Map C01 learning documentation is not current\n'
  failures=$((failures + 1))
fi

check_first "Learning Log has no active Card" CARD_LEARNING_AND_DECISION_LOG.md "Active Card:" "Active Card: NONE"
check "Learning Log authorization is historical" CARD_LEARNING_AND_DECISION_LOG.md "Authorization: C01 start approval recorded historically; no active Card"
check "Learning Log records C01 complete" CARD_LEARNING_AND_DECISION_LOG.md "V1-C01 State: COMPLETE"
check "Learning Log records historical start approval" CARD_LEARNING_AND_DECISION_LOG.md "V1-C01 Start Authorization: GRANTED (historical; Card complete)"
check "Learning Log records current HEAD" CARD_LEARNING_AND_DECISION_LOG.md "HEAD: $current_head"

check_first "AGENTS has no active Card" AGENTS.md "Active Card:" "Active Card: NONE"
check "AGENTS records C01 complete" AGENTS.md "V1-C01 State: COMPLETE"
check_first "Harness has no active Card" QUOTATION_ENGINEERING_HARNESS.md "Active Card:" "Active Card: NONE"
check "Harness authorization is historical" QUOTATION_ENGINEERING_HARNESS.md "Authorization: C01 start approval recorded historically; no active Card"
check "Harness records C01 complete" QUOTATION_ENGINEERING_HARNESS.md "V1-C01 State: COMPLETE"
check_first "Skill has no active Card" .agents/skills/quotation-card-execution/SKILL.md "Active Card:" "Active Card: NONE"
check "Skill records C01 complete" .agents/skills/quotation-card-execution/SKILL.md "V1-C01 State: COMPLETE"

if grep -Fq "V1-C01 is COMPLETE after PR #1 merged into main. Active Card is NONE." GIT_WORKFLOW.md; then
  printf 'PASS  Git workflow current posture is complete\n'
else
  printf 'FAIL  Git workflow current posture is not reconciled\n'
  failures=$((failures + 1))
fi

if [[ "$failures" -eq 0 ]]; then
  printf 'FINAL_CARD_STATE_CONSISTENCY_GATE: PASS\n'
  exit 0
fi

printf 'FINAL_CARD_STATE_CONSISTENCY_GATE: FAIL\n'
printf 'STATE_RECONCILIATION_REQUIRED\n'
printf 'STOP\n'
exit 1
