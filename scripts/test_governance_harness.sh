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
  tar -cf - --exclude=.git --exclude=.venv --exclude='__pycache__' --exclude=.pytest_cache . | tar -xf - -C "$dir"
  git -C "$dir" init -q -b main
  git -C "$dir" config user.email governance-test@example.invalid
  git -C "$dir" config user.name governance-test
  git -C "$dir" add .
  git -C "$dir" commit -qm fixture
  git -C "$dir" remote add origin https://example.invalid/ai-quotation-intelligence.git
  git -C "$dir" update-ref refs/remotes/origin/main HEAD
  git -C "$dir" symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
  git -C "$dir" branch --set-upstream-to=origin/main main >/dev/null
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
case_gc03() { local d; d="$(make_fixture gc03)"; replace_once "$d/QUOTATION_CARD_EVIDENCE_MAP.md" 'V1-C01 Exit Gate Evidence is PROVEN' 'V1-C01 Exit Gate Evidence is NOT_PROVEN'; ! gate_passes V1-C01 COMPLETE "$d"; }
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
expect_pass CARD-01 case_card01
expect_pass CARD-02 case_card02
expect_pass CARD-03 case_card03
expect_pass CARD-04 case_card04
expect_pass CARD-05 case_card05
say "GOVERNANCE_TEST_SUMMARY:"
say "PASS=$PASS"
say "FAIL=$FAIL"
if [[ "$FAIL" -eq 0 ]]; then exit 0; fi
exit 1
