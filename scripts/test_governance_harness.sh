#!/usr/bin/env bash
# Deterministic governance regression suite.
# All mutations occur in temporary fixture copies, never in the real repository.
set -u
set -o pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/ai-quotation-governance.XXXXXX")"
trap 'rm -rf "$TMP_ROOT"' EXIT

PASS=0
FAIL=0
say() { printf '%s\n' "$*"; }

make_fixture() {
  local name="$1"
  local dir="$TMP_ROOT/$name"
  mkdir -p "$dir"
  python3 "$ROOT/scripts/governance_fixture_builder.py" \
    --source-root "$ROOT" --root "$dir" \
    --completed V1-C01 --active NONE --next V1-C02 --next-state NOT_STARTED >/dev/null
  [[ -d "$dir" && -f "$dir/PROJECT_CONTROL.md" && -f "$dir/QUOTATION_CARD_EVIDENCE_MAP.md" ]] || return 1
  git -C "$dir" init -q -b main >/dev/null 2>&1 || return 1
  git -C "$dir" config user.email governance-test@example.invalid >/dev/null 2>&1 || return 1
  git -C "$dir" config user.name governance-test >/dev/null 2>&1 || return 1
  git -C "$dir" add . >/dev/null 2>&1 || return 1
  git -C "$dir" commit -qm fixture >/dev/null 2>&1 || return 1
  git -C "$dir" remote add origin https://example.invalid/ai-quotation-intelligence.git >/dev/null 2>&1 || return 1
  git -C "$dir" update-ref refs/remotes/origin/main HEAD >/dev/null 2>&1 || return 1
  git -C "$dir" symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main >/dev/null 2>&1 || return 1
  git -C "$dir" branch --set-upstream-to=origin/main main >/dev/null 2>&1 || return 1
  python3 "$ROOT/scripts/reconcile_governance_views.py" --write --root "$dir" >/dev/null 2>&1 || return 1
  if ! git -C "$dir" diff --quiet -- QUOTATION_CARD_EVIDENCE_MAP.md; then
    git -C "$dir" add QUOTATION_CARD_EVIDENCE_MAP.md >/dev/null 2>&1 || return 1
    git -C "$dir" commit -qm generated-views >/dev/null 2>&1 || return 1
  fi
  git -C "$dir" update-ref refs/remotes/origin/main HEAD >/dev/null 2>&1 || return 1
  printf '%s\n' "$dir"
}

make_fixture_state() {
  local name="$1" completed="$2" active="$3" active_state="$4" next_card="$5" next_state="$6" learning_status="${7:-COMPLETE}"
  local dir="$TMP_ROOT/$name"
  mkdir -p "$dir"
  python3 "$ROOT/scripts/governance_fixture_builder.py" \
    --source-root "$ROOT" --root "$dir" --completed "$completed" --active "$active" \
    --active-state "$active_state" --next "$next_card" --next-state "$next_state" --learning-status "$learning_status" >/dev/null || return 1
  [[ -d "$dir" && -f "$dir/PROJECT_CONTROL.md" && -f "$dir/QUOTATION_CARD_EVIDENCE_MAP.md" ]] || return 1
  git -C "$dir" init -q -b main >/dev/null 2>&1 || return 1
  git -C "$dir" config user.email governance-test@example.invalid >/dev/null 2>&1 || return 1
  git -C "$dir" config user.name governance-test >/dev/null 2>&1 || return 1
  git -C "$dir" add . >/dev/null 2>&1 || return 1
  git -C "$dir" commit -qm fixture >/dev/null 2>&1 || return 1
  git -C "$dir" remote add origin https://example.invalid/ai-quotation-intelligence.git >/dev/null 2>&1 || return 1
  git -C "$dir" update-ref refs/remotes/origin/main HEAD >/dev/null 2>&1 || return 1
  git -C "$dir" symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main >/dev/null 2>&1 || return 1
  git -C "$dir" branch --set-upstream-to=origin/main main >/dev/null 2>&1 || return 1
  python3 "$ROOT/scripts/reconcile_governance_views.py" --write --root "$dir" >/dev/null 2>&1 || return 1
  if ! git -C "$dir" diff --quiet -- QUOTATION_CARD_EVIDENCE_MAP.md; then
    git -C "$dir" add QUOTATION_CARD_EVIDENCE_MAP.md >/dev/null 2>&1 || return 1
    git -C "$dir" commit -qm generated-views >/dev/null 2>&1 || return 1
  fi
  git -C "$dir" update-ref refs/remotes/origin/main HEAD >/dev/null 2>&1 || return 1
  printf '%s\n' "$dir"
}

replace_once() {
  local file="$1"
  local old="$2"
  local new="$3"
  P3_OLD="$old" P3_NEW="$new" perl -0pi -e 's/\Q$ENV{P3_OLD}\E/$ENV{P3_NEW}/' "$file"
}

gate_passes() {
  bash "$ROOT/scripts/final_card_state_consistency.sh" "$1" "$2" "$3" >/dev/null 2>&1
}

expect_pass() {
  local id="$1"
  shift
  if "$@"; then say "GOVERNANCE_TEST $id PASS"; PASS=$((PASS + 1)); else say "GOVERNANCE_TEST $id FAIL"; FAIL=$((FAIL + 1)); fi
}

expect_fail() {
  local id="$1"
  shift
  if "$@"; then say "GOVERNANCE_TEST $id FAIL"; FAIL=$((FAIL + 1)); else say "GOVERNANCE_TEST $id PASS"; PASS=$((PASS + 1)); fi
}

case_gc01() { local d; d="$(make_fixture gc01)"; gate_passes V1-C01 COMPLETE "$d"; }
case_gc02() { local d; d="$(make_fixture gc02)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" '| V1-C01 | Repository Baseline | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |' '| V1-C01 | Repository Baseline | NOT_STARTED | NO | NOT_RUN | NOT_PROVEN | NOT_RUN | NONE | NOT_STARTED |'; ! gate_passes V1-C01 COMPLETE "$d"; }
case_gc03() { local d; d="$(make_fixture gc03)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" 'V1-C01: COMPLETE' 'V1-C01: NOT_STARTED'; ! gate_passes V1-C01 COMPLETE "$d"; }
case_gc04() { local d; d="$(make_fixture gc04)"; replace_once "$d/PROJECT_CONTROL.md" 'Active Card: NONE' 'Active Card: V1-C01'; ! gate_passes V1-C01 COMPLETE "$d"; }
case_gc05() { local d; d="$(make_fixture gc05)"; replace_once "$d/PROJECT_CONTROL.md" 'Implementation Authorization: C01 scope authorization consumed by completion; later Cards not authorized' 'Implementation Authorization: V1-C01 currently authorized'; ! gate_passes V1-C01 COMPLETE "$d"; }
case_gc06() { local d; d="$(make_fixture gc06)"; ! gate_passes V1-C99 COMPLETE "$d"; }
case_gc07() { local d; d="$(make_fixture gc07)"; ! gate_passes V1-C02 COMPLETE "$d"; }
case_gc08() { local d; d="$(make_fixture gc08)"; gate_passes V1-C02 UNSTARTED "$d"; }
case_gc09() { local d; d="$(make_fixture gc09)"; ! gate_passes V1-C02 COMPLETE "$d"; }
case_gc10() { local d; d="$(make_fixture gc10)"; : > "$d/unrelated.tmp"; ! gate_passes V1-C01 COMPLETE "$d"; }
case_gc11() { local d; d="$(make_fixture gc11)"; gate_passes V1-C01 COMPLETE "$d"; }
case_gc12() { local d; d="$(make_fixture gc12)"; git -C "$d" commit --allow-empty -qm drift; git -C "$d" update-ref refs/remotes/origin/main HEAD^; ! gate_passes V1-C01 COMPLETE "$d"; }

approval_fixture() {
  local name="$1"
  local d="$TMP_ROOT/$name"
  mkdir -p "$d"
  cat > "$d/approved.snapshot" <<'EOF'
IMPLEMENTATION=baseline
FILES=governance
SCOPE=card
VALIDATION=PASS
EOF
  cp "$d/approved.snapshot" "$d/current.state"
  printf '%s\n' "$d"
}

approval_valid() {
  local d="$1"
  cmp -s "$d/approved.snapshot" "$d/current.state"
}

approval_outcome_only_valid() {
  local d="$1"
  cmp -s "$d/approved.snapshot" "$d/current.state" || return 1
  printf '%s\n' 'DELIVERY_OUTCOME=RECORDED' > "$d/outcome.reconciliation"
  cmp -s "$d/approved.snapshot" "$d/current.state"
}

case_gd01() { local d; d="$(approval_fixture gd01)"; approval_valid "$d"; }
case_gd02() { local d; d="$(approval_fixture gd02)"; replace_once "$d/current.state" 'IMPLEMENTATION=baseline' 'IMPLEMENTATION=changed'; ! approval_valid "$d"; }
case_gd03() { local d; d="$(approval_fixture gd03)"; printf '%s\n' 'FILES=unrelated' >> "$d/current.state"; ! approval_valid "$d"; }
case_gd04() { local d; d="$(approval_fixture gd04)"; approval_outcome_only_valid "$d"; }
case_gd05() { local d; d="$(approval_fixture gd05)"; replace_once "$d/current.state" 'SCOPE=card' 'SCOPE=expanded'; ! approval_valid "$d"; }
case_gd06() { local d; d="$(approval_fixture gd06)"; replace_once "$d/current.state" 'VALIDATION=PASS' 'VALIDATION=FAIL'; ! approval_valid "$d"; }

post_delivery_policy_valid() {
  local file="$1"
  python3 - "$file" <<'PY'
import re
import sys
import hashlib
from pathlib import Path

policy_file = Path(sys.argv[1])
policy_bytes = policy_file.read_bytes()
text = policy_bytes.decode('utf-8')
flat = re.sub(r'\s+', ' ', text)
if 'Post-Delivery Provenance Rule' not in text:
    sys.exit(1)
name = policy_file.name
workflow = name.startswith('GIT_WORKFLOW.md')
if workflow:
    approved_sha256 = 'fd80295f6bb78983a89c213b5ce1ce72d16baa73f7a2100e59dca11d567a4497'
elif name.startswith('QUOTATION_ENGINEERING_HARNESS.md'):
    approved_sha256 = 'a447f172daa7a3a353e1e880ef8cdd0249660aa9c0bb2beb1f5bb8977c1293bb'
elif name.startswith('SKILL.md'):
    approved_sha256 = '851e2a2a5ee7143aa6f8ebb6ff549e6c71399f86a2688baac714983a91953758'
else:
    sys.exit(1)
if workflow:
    if not re.search(r'one explicit human GIT_DELIVERY_APPROVAL', text, re.I):
        sys.exit(1)
    section = re.search(r'^## 13A\. Post-Delivery Provenance Rule\s*$(.*?)(?=^## )', text, re.M | re.S)
    if not section:
        sys.exit(1)
    body = section.group(1)
    parts = re.findall(r'^([1-8])\.\s+(.*?)(?=^[1-8]\.\s+|\Z)', body, re.M | re.S)
    clauses = {int(number): re.sub(r'\s+', ' ', value).lower() for number, value in parts}
    if len(parts) != 8 or set(clauses) != set(range(1, 9)):
        sys.exit(1)
else:
    clauses = {}

def has(number, *patterns):
    return all(re.search(pattern, clauses[number]) for pattern in patterns)

# Each protection must be present in its policy owner; a heading alone is not proof.
required = not workflow or (
    has(1, r'frozen|immutab', r'independent.*audit', r'approval', r'(do not|never|must not) modify', r'(commit|pr|merge).*sha|identifier') and
    has(2, r'(cannot|must not|not).*prerequisite', r'commit sha', r'pr number|pr url', r'merge sha', r'(does not|cannot|must not) block') and
    has(3, r'final delivery (output|report)', r'observed', r'(only|actual).*observed|observed.*(only|actual)') and
    has(4, r'separat', r'maintenance', r'(do not|never|must not) require', r'own.*(commit|identifier)') and
    has(5, r'(do not|never|must not).*repeat', r'edit/commit/hash/edit|recurs', r'own sha') and
    has(6, r'preserve.*candidate identity', r'(do not|never|must not) invent', r'real delivery gates') and
    has(7, r'independent audit.*content', r'audited content equals staged.*equals committed') and
    has(8, r'project_control\.md.*live project/card state', r'evidence map|quotation_card_evidence_map\.md.*evidence history', r'git.*runtime')
)
if not required:
    sys.exit(1)

# The companion owners must retain their own delivery safeguards as well.
if name.startswith('QUOTATION_ENGINEERING_HARNESS.md'):
    required_patterns = (
        r'--require-staged.*--require-committed',
        r'CARD_QUALITY_GATE or human approval',
        r'Post-Delivery Provenance Rule.*not preconditions.*frozen.*candidate.*Report actual values after observation',
    )
    if not all(re.search(p, flat, re.I) for p in required_patterns):
        sys.exit(1)
if name.startswith('SKILL.md'):
    if not all(re.search(p, flat, re.I) for p in (
        r'--require-staged.*--require-committed',
        r'one explicit GIT_DELIVERY_APPROVAL.*commit.*push.*PR.*merge',
        r'Post-Delivery Provenance Rule.*never modify.*frozen.*audited candidate.*Missing future identifiers do not block.*Report observed values',
        r'Current live operational state is owned by PROJECT_CONTROL\.md',
    )):
        sys.exit(1)

# This is an audited-policy integrity gate, not an English-language parser.
# Any edit anywhere in an owner, including a protective rewording, requires
# separate review and an explicit update of its approved digest. Keeping the
# structural checks above makes the protected relationships visible in GD-07.
if hashlib.sha256(policy_bytes).hexdigest() != approved_sha256:
    sys.exit(1)
PY
}

gd07_mutant_rejected() {
  local source="$1" name="$2" clause="$3" wording="$4" mutant="$5"
  cp "$source" "$mutant" || return 1
  GD07_CLAUSE="$clause" GD07_WORDING="$wording" perl -0pi -e '
    BEGIN { $n = $ENV{GD07_CLAUSE}; $replacement = "$n. **Mutated policy.** $ENV{GD07_WORDING}\n" }
    $count = s/^\Q$n\E\. .*?(?=^[1-8]\. |^## |\z)/$replacement/msg;
    die "GD-07 mutation did not apply\n" unless $count == 1;
  ' "$mutant" || return 1
  if post_delivery_policy_valid "$mutant"; then
    say "GD-07 MUTATION $name FAIL"
    return 1
  fi
  say "GD-07 MUTATION $name PASS"
}

gd07_contradiction_rejected() {
  local source="$1" name="$2" wording="$3" mutant="$4" location="$5"
  cp "$source" "$mutant" || return 1
  case "$location" in
    section) replace_once "$mutant" '## 14. GIT_DELIVERY_APPROVAL' "$wording"$'\n\n''## 14. GIT_DELIVERY_APPROVAL' ;;
    workflow-pr) replace_once "$mutant" '## 15. Pull-Request Content' "$wording"$'\n\n''## 15. Pull-Request Content' ;;
    workflow-evidence) replace_once "$mutant" '## 22. Git Evidence' "$wording"$'\n\n''## 22. Git Evidence' ;;
    harness-mid) replace_once "$mutant" '## 17. Evidence Update Rule' "$wording"$'\n\n''## 17. Evidence Update Rule' ;;
    skill-mid) replace_once "$mutant" '## 17. Resume After Interruption' "$wording"$'\n\n''## 17. Resume After Interruption' ;;
    append) printf '\n%s\n' "$wording" >> "$mutant" ;;
    *) return 1 ;;
  esac
  grep -Fq "$wording" "$mutant" || return 1
  if post_delivery_policy_valid "$mutant"; then
    say "GD-07 CONTRADICTION $name FAIL"
    return 1
  fi
  say "GD-07 CONTRADICTION $name PASS"
}

gd07_rejected_everywhere() {
  local d="$1" name="$2" wording="$3" workflow="$4" harness="$5" skill="$6"
  gd07_contradiction_rejected "$workflow" "$name/13A" "$wording" "$d/GIT_WORKFLOW.md.$name.13A" section || return 1
  gd07_contradiction_rejected "$workflow" "$name/PR_SECTION" "$wording" "$d/GIT_WORKFLOW.md.$name.pr" workflow-pr || return 1
  gd07_contradiction_rejected "$workflow" "$name/EVIDENCE_SECTION" "$wording" "$d/GIT_WORKFLOW.md.$name.evidence" workflow-evidence || return 1
  gd07_contradiction_rejected "$workflow" "$name/END" "$wording" "$d/GIT_WORKFLOW.md.$name.end" append || return 1
  gd07_contradiction_rejected "$harness" "$name/HARNESS_MID" "$wording" "$d/QUOTATION_ENGINEERING_HARNESS.md.$name.mid" harness-mid || return 1
  gd07_contradiction_rejected "$harness" "$name/HARNESS_END" "$wording" "$d/QUOTATION_ENGINEERING_HARNESS.md.$name.end" append || return 1
  gd07_contradiction_rejected "$skill" "$name/SKILL_MID" "$wording" "$d/SKILL.md.$name.mid" skill-mid || return 1
  gd07_contradiction_rejected "$skill" "$name/SKILL_END" "$wording" "$d/SKILL.md.$name.end" append
}

post_delivery_action_allowed() {
  local dir="$1" action="$2"
  [[ "$action" == "commit" || "$action" == "PR" || "$action" == "merge" ]] || return 1
  grep -Fxq 'CANDIDATE_FROZEN=YES' "$dir/post-delivery-inputs" &&
    grep -Fxq 'INDEPENDENT_AUDIT=PASS' "$dir/post-delivery-inputs" &&
    grep -Fxq 'DELIVERY_APPROVAL=GRANTED' "$dir/post-delivery-inputs" &&
    approval_valid "$dir"
}

case_gd07() {
  local d workflow harness skill action
  d="$(approval_fixture gd07)" || return 1
  workflow="$d/GIT_WORKFLOW.md"
  harness="$d/QUOTATION_ENGINEERING_HARNESS.md"
  skill="$d/.agents/skills/quotation-card-execution/SKILL.md"
  cp "$ROOT/GIT_WORKFLOW.md" "$workflow" || return 1
  cp "$ROOT/QUOTATION_ENGINEERING_HARNESS.md" "$harness" || return 1
  mkdir -p "$(dirname "$skill")" || return 1
  cp "$ROOT/.agents/skills/quotation-card-execution/SKILL.md" "$skill" || return 1
  post_delivery_policy_valid "$workflow" || { say 'GD-07 BASELINE GIT_WORKFLOW FAIL'; return 1; }
  post_delivery_policy_valid "$harness" || { say 'GD-07 BASELINE HARNESS FAIL'; return 1; }
  post_delivery_policy_valid "$skill" || { say 'GD-07 BASELINE SKILL FAIL'; return 1; }

  printf '%s\n' \
    'CANDIDATE_FROZEN=YES' \
    'INDEPENDENT_AUDIT=PASS' \
    'DELIVERY_APPROVAL=GRANTED' \
    'DELIVERY_COMMIT_SHA=NOT_CREATED' \
    'PR_NUMBER_URL=NOT_CREATED' \
    'MERGE_SHA=NOT_CREATED' \
    'FINAL_MAIN_SHA=NOT_CREATED' > "$d/post-delivery-inputs"
  grep -Fxq 'MERGE_SHA=NOT_CREATED' "$d/post-delivery-inputs" || return 1
  for action in commit PR merge; do
    post_delivery_action_allowed "$d" "$action" || return 1
  done
  replace_once "$d/post-delivery-inputs" 'DELIVERY_APPROVAL=GRANTED' 'DELIVERY_APPROVAL=NOT_GRANTED'
  for action in commit PR merge; do
    post_delivery_action_allowed "$d" "$action" && return 1
  done
  replace_once "$d/post-delivery-inputs" 'DELIVERY_APPROVAL=NOT_GRANTED' 'DELIVERY_APPROVAL=GRANTED'

  gd07_mutant_rejected "$workflow" FUTURE_SHA_PRECONDITION 2 'Before committing, opening the PR, or merging, the frozen candidate must contain the corresponding commit SHA, PR number, and merge SHA.' "$d/GIT_WORKFLOW.md.future" || return 1
  gd07_mutant_rejected "$workflow" FROZEN_CANDIDATE_EDIT 1 'The delivery agent may edit the independently audited frozen candidate to add post-delivery provenance.' "$d/GIT_WORKFLOW.md.frozen" || return 1
  gd07_mutant_rejected "$workflow" HUMAN_APPROVAL_WEAKENING 1 'Delivery may proceed without explicit Human Delivery Approval.' "$d/GIT_WORKFLOW.md.approval" || return 1
  gd07_mutant_rejected "$workflow" STAGED_COMMITTED_WEAKENING 7 'Delivery may proceed without staged or committed candidate identity verification against the audited candidate.' "$d/GIT_WORKFLOW.md.identity" || return 1
  gd07_mutant_rejected "$workflow" SELF_REFERENTIAL_SHA 4 'A maintenance candidate must embed its own commit SHA before it can be committed.' "$d/GIT_WORKFLOW.md.self" || return 1
  gd07_mutant_rejected "$workflow" RECURSIVE_EVIDENCE_COMMIT 5 'Maintainers may repeat the evidence edit, commit, new SHA, and edit cycle until the record embeds the latest commit SHA.' "$d/GIT_WORKFLOW.md.recursive" || return 1
  gd07_mutant_rejected "$workflow" FABRICATED_PROVENANCE 3 'The delivery report may pre-fill predicted Git identifiers before they exist.' "$d/GIT_WORKFLOW.md.fabricated" || return 1
  gd07_mutant_rejected "$workflow" LIVE_STATE_OWNERSHIP 8 'The Evidence Map is the live operational state owner.' "$d/GIT_WORKFLOW.md.ownership" || return 1

  # Eight placements across the three complete owners, including late exceptions.
  gd07_rejected_everywhere "$d" FUTURE_SHA_PRECONDITION 'Before merge, the candidate must record the merge SHA.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" FUTURE_COMMIT_SHA 'Before commit, the candidate must record the commit SHA.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" FUTURE_PR_NUMBER 'Before opening the PR, the candidate must record the PR number.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" FROZEN_CANDIDATE_EDIT 'The delivery agent may edit the frozen candidate to add provenance SHA values.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" FROZEN_EDIT_VARIANT 'The frozen audited candidate may be updated with delivery provenance identifiers.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" HUMAN_APPROVAL_WEAKENING 'Delivery may proceed without explicit Human Delivery Approval.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" STAGED_COMMITTED_WEAKENING 'Delivery may proceed without staged and committed candidate identity verification.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" SELF_REFERENTIAL_SHA 'A maintenance candidate must embed its own commit SHA before commit.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" RECURSIVE_EVIDENCE_COMMIT 'Maintainers may repeat the evidence edit and commit cycle for each new SHA.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" FABRICATED_PROVENANCE 'The delivery report may pre-fill predicted Git identifiers before they exist.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" APPROVAL_OPTIONAL_VARIANT 'Human approval is optional for delivery.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" SELF_SHA_VARIANT 'A maintenance commit should record its own SHA.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" RECURSIVE_VARIANT 'Update Evidence Map with the new SHA and commit again until stable.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" FABRICATED_VARIANT 'The final output may include expected merge SHA computed in advance.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" IDENTITY_OPTIONAL_VARIANT 'Staged and committed identity checks are optional.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" LIVE_STATE_OWNERSHIP 'The Evidence Map is the live operational state owner.' "$workflow" "$harness" "$skill" || return 1
  # Independently reported misses: exact bytes change even when syntax is passive or indirect.
  gd07_rejected_everywhere "$d" PASSIVE_FUTURE_SHA 'The merge SHA must be written into the Evidence Map prior to merging the pull request.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" EXPECTED_MERGE_SHA 'Expected merge SHA may be written before merge.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" ACCEPTABLE_FROZEN_EDIT 'It is acceptable to modify the frozen candidate in order to record the merge SHA.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" IMPLIED_APPROVAL 'An independent audit PASS may be treated as delivery approval.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" SKIP_COMMITTED_TREE 'Skip the committed-tree verification when time is short.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" OWN_COMMIT_HASH 'Each delivery commit must contain its own commit hash.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" REPEAT_EVIDENCE_COMMITS 'Repeat evidence commits for each new SHA.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" ESTIMATE_PR_NUMBER 'Agents may estimate the PR number before it exists.' "$workflow" "$harness" "$skill" || return 1
  gd07_rejected_everywhere "$d" OUTPUT_OWNS_LIVE_STATE 'The final delivery output replaces PROJECT_CONTROL.md as live project state.' "$workflow" "$harness" "$skill" || return 1

  # This gate deliberately fails closed for benign edits too; it does not infer meaning.
  cp "$workflow" "$d/GIT_WORKFLOW.md.protective-edit" || return 1
  printf '\n%s\n' 'Delivery must never proceed without human approval.' >> "$d/GIT_WORKFLOW.md.protective-edit"
  post_delivery_policy_valid "$d/GIT_WORKFLOW.md.protective-edit" && return 1
  cp "$harness" "$d/QUOTATION_ENGINEERING_HARNESS.md.protective-edit" || return 1
  printf '\n%s\n' 'Do not skip staged and committed identity verification.' >> "$d/QUOTATION_ENGINEERING_HARNESS.md.protective-edit"
  post_delivery_policy_valid "$d/QUOTATION_ENGINEERING_HARNESS.md.protective-edit" && return 1
  cp "$skill" "$d/SKILL.md.protective-edit" || return 1
  printf '\n%s\n' 'Human approval remains mandatory.' >> "$d/SKILL.md.protective-edit"
  post_delivery_policy_valid "$d/SKILL.md.protective-edit" && return 1
  say 'GD-07 PROTECTIVE EDITS REQUIRE REVIEW PASS'

  printf '%s\n' \
    'DELIVERY_COMMIT_SHA=observed-after-commit' \
    'PR_NUMBER_URL=observed-after-creation' \
    'MERGE_SHA=observed-after-merge' \
    'FINAL_MAIN_SHA=observed-after-merge' > "$d/final-delivery-report"
  cmp -s "$d/approved.snapshot" "$d/current.state"
}

single_active_valid() {
  local d="$1"
  local control
  control="$(awk '/^## 2\. Current Project State$/{inside=1; next} /^## /{if(inside) exit} inside{print}' "$d/PROJECT_CONTROL.md")"
  local active
  active="$(awk 'index($0, "Active Card:") == 1 { print; exit }' <<<"$control")"
  [[ "$active" == "Active Card: NONE" || "$active" =~ ^Active\ Card:\ V1-C[0-9][0-9]$ ]]
}

future_leakage_blocked() {
  local state="$1"
  local approval="$2"
  [[ "$state" == "NOT_STARTED" && "$approval" == "NO" ]]
}

case_card01() { local d; d="$(make_fixture card01)"; single_active_valid "$d"; }
case_card02() { local d; d="$(make_fixture card02)"; replace_once "$d/PROJECT_CONTROL.md" 'Active Card: NONE' 'Active Card: V1-C01, V1-C02'; ! single_active_valid "$d"; }
case_card03() { local d; d="$(make_fixture card03)"; replace_once "$d/PROJECT_CONTROL.md" 'Next Card Authorized: NO' 'Next Card Authorized: YES'; ! gate_passes V1-C01 COMPLETE "$d"; }
case_card04() { future_leakage_blocked NOT_STARTED NO; }
case_card05() { local d; d="$(make_fixture card05)"; gate_passes V1-C01 COMPLETE "$d" && gate_passes V1-C02 UNSTARTED "$d"; }

view_check() { python3 "$ROOT/scripts/reconcile_governance_views.py" --check --root "$1" >/dev/null 2>&1; }
view_write() { python3 "$ROOT/scripts/reconcile_governance_views.py" --write --root "$1" >/dev/null 2>&1; }
card_section() { awk -v card="$1" '/^## V1-C[0-9][0-9] —/{if (found) exit; found = index($0, "## " card " —") == 1} found{print}' "$2"; }

promote_c02_fixture() {
  local d="$1"
  replace_once "$d/PROJECT_CONTROL.md" 'Project Phase: V1_C01_COMPLETE' 'Project Phase: V1_C02_ACTIVE'
  replace_once "$d/PROJECT_CONTROL.md" 'Active Card: NONE' 'Active Card: V1-C02'
  replace_once "$d/PROJECT_CONTROL.md" '| V1-C02 | Domain Models | NOT_STARTED | NO | NOT_RUN | PENDING |' '| V1-C02 | Domain Models | READY_FOR_DELIVERY | YES | PASS | PRESENT |'
  replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" $'## V1-C02 — Domain Models\n\n### 1. Card\n\nV1-C02 — Domain Models\n\n### 2. Contract Source\n\nQUOTATION_CARD_SPECIFICATIONS.md\n\nRoadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.\n\n### 3. State\n\nNOT_STARTED' $'## V1-C02 — Domain Models\n\n### 1. Card\n\nV1-C02 — Domain Models\n\n### 2. Contract Source\n\nQUOTATION_CARD_SPECIFICATIONS.md\n\nRoadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.\n\n### 3. State\n\nREADY_FOR_DELIVERY'
  replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" $'### 4. Human Start Approval\n\nNO' $'### 4. Human Start Approval\n\nYES'
  replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" $'### 7. Focused Tests\n\nNOT_RUN' $'### 7. Focused Tests\n\nPASS'
  replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" $'### 20. Recommended State\n\nNOT_STARTED' $'### 20. Recommended State\n\nREADY_FOR_DELIVERY'
}

case_gv01() { local d; d="$(make_fixture gv01)"; view_check "$d"; }
case_gv02() { local d; d="$(make_fixture gv02)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" '| V1-C02 | Domain Models | NOT_STARTED | NO | NOT_RUN | NOT_PROVEN | NOT_RUN | NONE | NOT_STARTED |' '| V1-C02 | Domain Models | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |'; ! view_check "$d"; }
case_gv03() { local d; d="$(make_fixture gv03)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" 'V1-C02: NOT_AUTHORIZED / NOT_STARTED' 'V1-C02: NOT_AUTHORIZED / COMPLETE'; ! view_check "$d"; }
case_gv04() { local d; d="$(make_fixture gv04)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" '| V1-C02 | Domain Models | NOT_STARTED | NO | NOT_RUN | NOT_PROVEN | NOT_RUN | NONE | NOT_STARTED |' '| V1-C02 | Domain Models | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |'; view_write "$d" && view_check "$d"; }
case_gv05() { local d; d="$(make_fixture gv05)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" '| V1-C02 | Domain Models | NOT_STARTED | NO | NOT_RUN | NOT_PROVEN | NOT_RUN | NONE | NOT_STARTED |' '| V1-C02 | Domain Models | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |'; view_write "$d" || return 1; cp "$d/QUOTATION_CARD_EVIDENCE_MAP.md" "$d/after-first-write"; view_write "$d" && cmp -s "$d/after-first-write" "$d/QUOTATION_CARD_EVIDENCE_MAP.md"; }
case_gv06() { local d before after; d="$(make_fixture gv06)"; before="$(card_section V1-C02 "$d/QUOTATION_CARD_EVIDENCE_MAP.md")"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" '| V1-C02 | Domain Models | NOT_STARTED | NO | NOT_RUN | NOT_PROVEN | NOT_RUN | NONE | NOT_STARTED |' '| V1-C02 | Domain Models | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |'; view_write "$d" || return 1; after="$(card_section V1-C02 "$d/QUOTATION_CARD_EVIDENCE_MAP.md")"; [[ "$before" == "$after" ]]; }
case_gv07() { local d; d="$(make_fixture gv07)"; replace_once "$d/PROJECT_CONTROL.md" 'Active Card: NONE' 'Active Card: V1-C02'; ! gate_passes V1-C02 READY_FOR_DELIVERY "$d"; }
case_gv08() { local d; d="$(make_fixture gv08)"; promote_c02_fixture "$d"; view_write "$d" && view_check "$d" && gate_passes V1-C02 READY_FOR_DELIVERY "$d"; }

case_hf01() { local d; d="$(make_fixture_state hf01 V1-C01 NONE ACTIVE V1-C02 NOT_STARTED)"; [[ -d "$d" ]] && gate_passes V1-C01 COMPLETE "$d" && gate_passes V1-C02 UNSTARTED "$d"; }
case_hf02() { local d; d="$(make_fixture_state hf02 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; [[ -d "$d" ]] && view_check "$d"; }
case_hf03() { local d; d="$(make_fixture_state hf03 V1-C01,V1-C02,V1-C03,V1-C04,V1-C05 NONE ACTIVE V1-C06 NOT_STARTED)"; [[ -d "$d" ]] && view_check "$d"; }
case_hf04() { local before after; before="$(make_fixture_state hf04 V1-C01 NONE ACTIVE V1-C02 NOT_STARTED)"; after="$(make_fixture_state hf04b V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; [[ -d "$before" && -d "$after" && "$before" != "$after" ]]; }
case_hf05() { local d; d="$(make_fixture_state hf05 V1-C01 NONE ACTIVE V1-C02 NOT_STARTED)"; [[ "$d" == "$TMP_ROOT/hf05" && -d "$d" ]]; }
case_hf06() { local d output; output="$(make_fixture_state hf06 V1-C01 NONE ACTIVE V1-C02 NOT_STARTED)"; [[ "$output" != *"On branch"* && "$output" == "$TMP_ROOT/hf06" ]]; }
case_hf07() { local d; d="$(make_fixture_state hf07 V1-C01 NONE ACTIVE V1-C02 NOT_STARTED)"; [[ -d "$d" ]] && view_check "$d"; }
case_hf08() { local d="$TMP_ROOT/hf08"; ! make_fixture_state hf08 V1-C01 NONE ACTIVE BAD_STATE V1-C02 NOT_STARTED; }

case_fc01() { local d; d="$(make_fixture_state fc01 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; [[ -d "$d" ]] && gate_passes V1-C02 COMPLETE "$d"; }
case_fc02() { local d; d="$(make_fixture_state fc02 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; [[ -d "$d" ]] && gate_passes V1-C02 COMPLETE "$d"; }
case_fc03() { local d; d="$(make_fixture_state fc03 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/PROJECT_CONTROL.md" 'Completed Cards: V1-C01 — Repository Baseline; V1-C02 — Domain Models' 'Completed Cards: V1-C01 — Repository Baseline'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_fc04() { local d; d="$(make_fixture_state fc04 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED CURRENT)"; gate_passes V1-C02 COMPLETE "$d"; }
case_fc05() { local d; d="$(make_fixture_state fc05 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; gate_passes V1-C02 COMPLETE "$d"; }
case_fc06() { local d; d="$(make_fixture_state fc06 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" $'Learning Documentation Status:\nCOMPLETE' $'Learning Documentation Status:\nPARTIAL'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_fc07() { local d; d="$(make_fixture_state fc07 V1-C01 NONE ACTIVE V1-C02 NOT_STARTED)"; gate_passes V1-C01 COMPLETE "$d"; }
case_fc08() { local d; d="$(make_fixture_state fc08 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; gate_passes V1-C02 COMPLETE "$d"; }
case_fc09() { local d; d="$(make_fixture_state fc09 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" 'merged' 'delivered'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_fc10() { local d; d="$(make_fixture_state fc10 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" 'merged' 'delivered'; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" '164ae7c3982009025ec16de72cd0d4ad1efc646d' 'no-merge-hash'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_fc11() { local d; d="$(make_fixture_state fc11 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; gate_passes V1-C02 COMPLETE "$d"; }
case_fc12() { local d; d="$(make_fixture_state fc12 V1-C01,V1-C02,V1-C03,V1-C04,V1-C05 NONE ACTIVE V1-C06 NOT_STARTED)"; gate_passes V1-C05 COMPLETE "$d"; }

case_pc_state01() { local d; d="$(make_fixture_state pc-state-01 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; gate_passes V1-C02 COMPLETE "$d"; }
case_pc_state02() { local d; d="$(make_fixture_state pc-state-02 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/PROJECT_CONTROL.md" 'State: COMPLETE' 'State: READY_FOR_DELIVERY'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_pc_state03() { local d; d="$(make_fixture_state pc-state-03 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/PROJECT_CONTROL.md" 'Delivery Commit: fixture-02-delivery' 'Delivery Commit: NOT_CREATED'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_pc_state04() { local d; d="$(make_fixture_state pc-state-04 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/PROJECT_CONTROL.md" 'PR: MERGED — #2' 'PR: NOT_CREATED'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_pc_state05() { local d; d="$(make_fixture_state pc-state-05 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; replace_once "$d/PROJECT_CONTROL.md" 'Merge Commit: 0202020202020202020202020202020202020202' 'Merge Commit: NOT_CREATED'; ! gate_passes V1-C02 COMPLETE "$d"; }
case_pc_state06() { local d; d="$(make_fixture_state pc-state-06 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; gate_passes V1-C01 COMPLETE "$d"; }
case_pc_state07() { local d; d="$(make_fixture_state pc-state-07 V1-C01,V1-C02 NONE ACTIVE V1-C03 NOT_STARTED)"; gate_passes V1-C02 COMPLETE "$d"; }
case_pc_state08() { local d; d="$(make_fixture_state pc-state-08 V1-C01,V1-C02,V1-C03,V1-C04,V1-C05 NONE ACTIVE V1-C06 NOT_STARTED)"; gate_passes V1-C05 COMPLETE "$d"; }
case_pc_state09() { local d; d="$(make_fixture_state pc-state-09 V1-C01,V1-C02,V1-C03,V1-C04,V1-C05 NONE ACTIVE V1-C06 NOT_STARTED)"; replace_once "$d/PROJECT_CONTROL.md" 'State: COMPLETE' 'State: READY_FOR_DELIVERY'; ! gate_passes V1-C05 COMPLETE "$d"; }

if [[ "${1:-}" == "--case" && "${2:-}" == "GD-07" ]]; then
  expect_pass GD-07 case_gd07
  say "PASS=$PASS"
  say "FAIL=$FAIL"
  [[ "$FAIL" -eq 0 ]]
  exit $?
fi

say "GOVERNANCE_TEST_SUITE: START"
expect_pass GC-01 case_gc01
expect_pass GC-02 case_gc02
expect_pass GC-03 case_gc03
expect_pass GC-04 case_gc04
expect_pass GC-05 case_gc05
expect_pass GC-06 case_gc06
expect_pass GC-07 case_gc07
expect_pass GC-08 case_gc08
expect_pass GC-09 case_gc09
expect_pass GC-10 case_gc10
expect_pass GC-11 case_gc11
expect_pass GC-12 case_gc12
expect_pass GD-01 case_gd01
expect_pass GD-02 case_gd02
expect_pass GD-03 case_gd03
expect_pass GD-04 case_gd04
expect_pass GD-05 case_gd05
expect_pass GD-06 case_gd06
expect_pass GD-07 case_gd07
expect_pass CARD-01 case_card01
expect_pass CARD-02 case_card02
expect_pass CARD-03 case_card03
expect_pass CARD-04 case_card04
expect_pass CARD-05 case_card05
expect_pass GV-01 case_gv01
expect_pass GV-02 case_gv02
expect_pass GV-03 case_gv03
expect_pass GV-04 case_gv04
expect_pass GV-05 case_gv05
expect_pass GV-06 case_gv06
expect_pass GV-07 case_gv07
expect_pass GV-08 case_gv08
expect_pass HF-01 case_hf01
expect_pass HF-02 case_hf02
expect_pass HF-03 case_hf03
expect_pass HF-04 case_hf04
expect_pass HF-05 case_hf05
expect_pass HF-06 case_hf06
expect_pass HF-07 case_hf07
expect_pass HF-08 case_hf08
expect_pass FC-01 case_fc01
expect_pass FC-02 case_fc02
expect_pass FC-03 case_fc03
expect_pass FC-04 case_fc04
expect_pass FC-05 case_fc05
expect_pass FC-06 case_fc06
expect_pass FC-07 case_fc07
expect_pass FC-08 case_fc08
expect_pass FC-09 case_fc09
expect_pass FC-10 case_fc10
expect_pass FC-11 case_fc11
expect_pass FC-12 case_fc12
expect_pass PC-STATE-01 case_pc_state01
expect_pass PC-STATE-02 case_pc_state02
expect_pass PC-STATE-03 case_pc_state03
expect_pass PC-STATE-04 case_pc_state04
expect_pass PC-STATE-05 case_pc_state05
expect_pass PC-STATE-06 case_pc_state06
expect_pass PC-STATE-07 case_pc_state07
expect_pass PC-STATE-08 case_pc_state08
expect_pass PC-STATE-09 case_pc_state09
say "GOVERNANCE_TEST_SUMMARY:"
say "PASS=$PASS"
say "FAIL=$FAIL"
if [[ "$FAIL" -eq 0 ]]; then exit 0; fi
exit 1
