#!/usr/bin/env bash
# FINAL_CARD_STATE_CONSISTENCY_GATE
# PROJECT_CONTROL.md owns live state; Git commands own runtime Git facts.
# Card-specific evidence is read only from the requested Evidence Map section.
set -u
set -o pipefail

CARD_ID="${1:-}"
EXPECTED_STATE="${2:-COMPLETE}"
ROOT="${3:-$(pwd)}"

if [[ -z "$CARD_ID" || ! "$CARD_ID" =~ ^V1-C(0[1-9]|1[0-9]|20)$ ]]; then
  printf 'usage: bash scripts/final_card_state_consistency.sh V1-C01 [COMPLETE|READY_FOR_DELIVERY|ACTIVE|UNSTARTED] [ROOT]\n' >&2
  exit 2
fi

case "$EXPECTED_STATE" in
  COMPLETE|READY_FOR_DELIVERY|ACTIVE|UNSTARTED) ;;
  *) printf 'unsupported expected state: %s\n' "$EXPECTED_STATE" >&2; exit 2 ;;
esac

cd "$ROOT" || exit 2

failures=0
pass() { printf 'PASS  %s\n' "$1"; }
fail() { printf 'FAIL  %s\n' "$1"; failures=$((failures + 1)); }

require_file() {
  local path="$1"
  [[ -f "$path" ]] && return 0
  fail "required file missing: $path"
  return 1
}

# Extract a level-2 Markdown section whose heading begins with a literal prefix.
section() {
  local file="$1"
  local heading_prefix="$2"
  awk -v prefix="$heading_prefix" '
    $0 ~ /^## / {
      if (inside) exit
      if (index($0, prefix) == 1) inside=1
    }
    inside { print }
  ' "$file"
}

# Extract a level-3 subsection from an isolated level-2 section.
subsection() {
  local marker="$1"
  awk -v marker="$marker" '
    $0 ~ /^### / {
      if (inside) exit
      if ($0 == marker) inside=1
    }
    inside { print }
  '
}

has_exact_line() {
  local text="$1"
  local expected="$2"
  awk -v expected="$expected" '$0 == expected { found=1 } END { exit(found ? 0 : 1) }' <<<"$text"
}

has_prefixed_line() {
  local text="$1"
  local prefix="$2"
  awk -v prefix="$prefix" 'index($0, prefix) == 1 { found=1 } END { exit(found ? 0 : 1) }' <<<"$text"
}

has_text() {
  local text="$1"
  local expected="$2"
  grep -Fq -- "$expected" <<<"$text"
}

table_matches() {
  local text="$1"
  local expected_state="$2"
  local expected_approval="$3"
  local expected_tests="$4"
  local expected_exit="$5"
  local expected_quality="$6"
  local expected_evidence="$7"
  local expected_recommended="$8"
  awk -F'|' -v card="$CARD_ID" -v state="$expected_state" -v approval="$expected_approval" \
    -v tests="$expected_tests" -v exit_gate="$expected_exit" -v quality="$expected_quality" \
    -v evidence="$expected_evidence" -v recommended="$expected_recommended" '
    NF >= 10 {
      for (i = 2; i <= 10; i++) gsub(/^[ \t]+|[ \t]+$/, "", $i)
      if ($2 == card && $4 == state && $5 == approval && $6 == tests &&
          $7 == exit_gate && $8 == quality && $9 == evidence && $10 == recommended) found=1
    }
    END { exit(found ? 0 : 1) }
  ' <<<"$text"
}

printf 'FINAL_CARD_STATE_CONSISTENCY_GATE\n'
printf 'Card: %s\n' "$CARD_ID"
printf 'Expected state: %s\n' "$EXPECTED_STATE"

for path in PROJECT_CONTROL.md AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md \
  QUOTATION_CARD_SPECIFICATIONS.md QUOTATION_CARD_EVIDENCE_MAP.md; do
  require_file "$path" || exit 1
done

roadmap_section="$(section AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md "## $CARD_ID —")"
spec_section="$(section QUOTATION_CARD_SPECIFICATIONS.md "## $CARD_ID —")"
evidence_section="$(section QUOTATION_CARD_EVIDENCE_MAP.md "## $CARD_ID —")"
control_section="$(section PROJECT_CONTROL.md "## 2. Current Project State")"
roadmap_position_section="$(section PROJECT_CONTROL.md "## 7. Roadmap Position")"
evidence_summary_section="$(section QUOTATION_CARD_EVIDENCE_MAP.md "## 18. Current Summary")"
evidence_table_section="$(section QUOTATION_CARD_EVIDENCE_MAP.md "## 17. Current Card Table")"

[[ -n "$roadmap_section" ]] && pass "Card exists in Roadmap" || fail "Card missing from Roadmap"
[[ -n "$spec_section" ]] && pass "Card exists in Card Specifications" || fail "Card missing from Card Specifications"
[[ -n "$evidence_section" ]] && pass "Card evidence section exists" || fail "Card evidence section missing"

card_heading="$(awk -v prefix="## $CARD_ID —" 'index($0, prefix) == 1 { print; exit }' <<<"$roadmap_section")"
card_title="${card_heading#* — }"
if [[ -n "$card_title" ]] && has_exact_line "$evidence_section" "$CARD_ID — $card_title"; then
  pass "Card identity and title match across Roadmap and Evidence Map"
else
  fail "Card identity/title mismatch across Roadmap and Evidence Map"
fi

active_line="$(awk 'index($0, "Active Card:") == 1 { print; exit }' <<<"$control_section")"

case "$EXPECTED_STATE" in
  COMPLETE)
    expected_phase="Project Phase: ${CARD_ID//-/_}_COMPLETE"
    has_prefixed_line "$control_section" "$expected_phase" && pass "Project Control records completed Card phase" || fail "Project Control completed phase mismatch"
    [[ "$active_line" == "Active Card: NONE" ]] && pass "Active Card is NONE" || fail "Active Card is not NONE"
    has_prefixed_line "$control_section" "Last COMPLETE Card: $CARD_ID" && pass "Project Control records requested Card as last complete" || fail "Completed Card is not recorded in Project Control"
    has_prefixed_line "$roadmap_position_section" "Completed Cards: $CARD_ID" && pass "Project Control completed-card list contains requested Card" || fail "Completed-card list does not contain requested Card"
    has_prefixed_line "$control_section" "Next Card Authorized: NO" && pass "No later Card is authorized" || fail "Later Card authorization is not explicitly NO"
    has_text "$control_section" "Implementation Authorization:" && has_text "$control_section" "authorization consumed by completion" && has_text "$control_section" "later Cards not authorized" && pass "Completed Card is not currently authorized" || fail "Completed Card remains currently authorized"
    ;;
  READY_FOR_DELIVERY|ACTIVE)
    [[ "$active_line" == "Active Card: $CARD_ID" ]] && pass "Project Control active Card matches request" || fail "Project Control active Card mismatch"
    ;;
  UNSTARTED)
    [[ "$active_line" == "Active Card: NONE" ]] && pass "No Card is active" || fail "Unexpected active Card for unstarted request"
    ;;
esac

state_section="$(subsection '### 3. State' <<<"$evidence_section")"
approval_section="$(subsection '### 4. Human Start Approval' <<<"$evidence_section")"
tests_section="$(subsection '### 7. Focused Tests' <<<"$evidence_section")"
quality_section="$(subsection '### 15. CARD_QUALITY_GATE' <<<"$evidence_section")"
git_section="$(subsection '### 16. Git Evidence' <<<"$evidence_section")"
completion_section="$(subsection '### 19. Completion Evidence' <<<"$evidence_section")"
recommended_section="$(subsection '### 20. Recommended State' <<<"$evidence_section")"

evidence_expected_state="$EXPECTED_STATE"
[[ "$EXPECTED_STATE" == "UNSTARTED" ]] && evidence_expected_state="NOT_STARTED"
has_exact_line "$state_section" "$evidence_expected_state" && pass "Card evidence state is $evidence_expected_state" || fail "Card evidence state is not $evidence_expected_state"

case "$EXPECTED_STATE" in
  COMPLETE)
    has_exact_line "$approval_section" "YES" && pass "Historical human start approval is recorded" || fail "Human start approval is missing"
    if has_text "$tests_section" "NOT_RUN" || ! has_text "$tests_section" "PASS"; then fail "Required focused test evidence is not passing"; else pass "Focused test evidence is present and not NOT_RUN"; fi
    has_text "$quality_section" "PASS" && pass "CARD_QUALITY_GATE evidence is PASS" || fail "CARD_QUALITY_GATE evidence is not PASS"
    has_text "$evidence_section" "Exit Gate Status: PROVEN" && pass "Exit Gate evidence is PROVEN" || fail "Exit Gate evidence is not PROVEN"
    has_text "$completion_section" "COMPLETE" && pass "Completion evidence is present" || fail "Completion evidence is missing"
    has_exact_line "$recommended_section" "COMPLETE" && pass "Recommended State is COMPLETE" || fail "Recommended State is not COMPLETE"
    has_text "$evidence_section" "Learning Documentation Status:" && has_text "$evidence_section" "CURRENT" && pass "Learning documentation evidence is current" || fail "Learning documentation evidence is not current"
    has_text "$git_section" "PR: MERGED" && has_text "$git_section" "Merge: COMPLETED" && pass "Historical Git delivery evidence is complete" || fail "Historical Git delivery evidence is incomplete"
    table_matches "$evidence_table_section" COMPLETE YES PASS PROVEN PASS PRESENT COMPLETE && pass "Evidence Map status table agrees with completed Card" || fail "Evidence Map status table contradicts completed Card"
    has_text "$evidence_summary_section" "$CARD_ID Exit Gate Evidence is PROVEN" && has_text "$evidence_summary_section" "$CARD_ID CARD_QUALITY_GATE is PASS" && pass "Evidence Map summary gates agree with completed Card" || fail "Evidence Map summary gates contradict completed Card"
    ;;
  READY_FOR_DELIVERY)
    has_exact_line "$approval_section" "YES" && pass "Human start approval is recorded" || fail "Human start approval is missing"
    has_exact_line "$recommended_section" "READY_FOR_DELIVERY" && pass "Recommended State is READY_FOR_DELIVERY" || fail "Recommended State is not READY_FOR_DELIVERY"
    ;;
  ACTIVE)
    has_exact_line "$approval_section" "YES" && pass "Human start approval is recorded" || fail "Human start approval is missing"
    ;;
  UNSTARTED)
    has_exact_line "$state_section" "NOT_STARTED" && pass "Card evidence is NOT_STARTED" || fail "Card evidence is not NOT_STARTED"
    table_matches "$evidence_table_section" NOT_STARTED NO NOT_RUN NOT_PROVEN NOT_RUN NONE NOT_STARTED && pass "Evidence Map status table agrees with unstarted Card" || fail "Evidence Map status table contradicts unstarted Card"
    ;;
esac

if [[ "$EXPECTED_STATE" == "COMPLETE" ]]; then
  current_branch="$(git branch --show-current 2>/dev/null || true)"
  default_branch="$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null || true)"
  default_branch="${default_branch#origin/}"
  [[ -n "$default_branch" ]] || default_branch="$current_branch"
  [[ "$current_branch" == "$default_branch" ]] && pass "Runtime branch is default branch ($default_branch)" || fail "Runtime branch is not default branch ($default_branch): ${current_branch:-NOT_AVAILABLE}"
  if upstream="$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null)"; then
    ahead_behind="$(git rev-list --left-right --count HEAD...@{u} 2>/dev/null || true)"
    [[ "$ahead_behind" == $'0\t0' ]] && pass "Runtime branch is synchronized with upstream ($upstream)" || fail "Runtime branch is not synchronized with upstream ($upstream): ${ahead_behind:-NOT_AVAILABLE}"
  else
    fail "Runtime branch has no upstream"
  fi
  if [[ -z "$(git status --porcelain)" ]]; then pass "Runtime working tree is clean"; else fail "Runtime working tree is not clean"; fi
fi

if [[ "$failures" -eq 0 ]]; then
  printf 'FINAL_CARD_STATE_CONSISTENCY_GATE: PASS\n'
  exit 0
fi

printf 'FINAL_CARD_STATE_CONSISTENCY_GATE: FAIL\n'
printf 'STATE_RECONCILIATION_REQUIRED\n'
printf 'STOP\n'
exit 1
