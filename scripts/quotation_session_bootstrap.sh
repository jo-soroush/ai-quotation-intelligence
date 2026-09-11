#!/usr/bin/env bash
# Read-only session check. It never repairs, authorizes, implements, deploys,
# installs, or performs Git/AWS write operations.
set -u
set -o pipefail

PASS=0; WARN=0; FAIL=0
say() { printf '%s\n' "$*"; }
pass() { PASS=$((PASS + 1)); say "PASS  $*"; }
warn() { WARN=$((WARN + 1)); say "WARN  $*"; }
fail() { FAIL=$((FAIL + 1)); say "FAIL  $*"; }
info() { say "INFO  $*"; }

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "$SCRIPT_DIR/.." 2>/dev/null && pwd)"
if [[ ! -d "$PROJECT_ROOT" ]]; then
  fail "invalid project root: $PROJECT_ROOT"; say "BOOTSTRAP_STATUS: FAIL"; exit 1
fi
cd -- "$PROJECT_ROOT" || { fail "cannot enter project root"; exit 1; }

say "========================================"
say "AI QUOTATION INTELLIGENCE SESSION CHECK"
say "========================================"
say "Project root: $PROJECT_ROOT"

if [[ -f PROJECT_PROFILE.md ]] && grep -Fq "Project: AI Quotation Intelligence System" PROJECT_PROFILE.md; then
  pass "project identity is correct"
else
  fail "canonical project identity is missing or inconsistent"
fi

REQUIRED_FILES=(
  AGENTS.md PROJECT_PROFILE.md PROJECT_CONTROL.md
  AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md
  QUOTATION_CARD_SPECIFICATIONS.md QUOTATION_CARD_EVIDENCE_MAP.md
  CARD_LEARNING_AND_DECISION_LOG.md
  QUOTATION_ENGINEERING_HARNESS.md COMMERCIAL_AND_DATA_GUARDRAILS.md
  GIT_WORKFLOW.md .agents/skills/quotation-card-execution/SKILL.md
  PROJECT_MIGRATION_STATUS.md
)
for path in "${REQUIRED_FILES[@]}"; do
  [[ -f "$path" ]] && pass "canonical file exists: $path" || fail "required file missing: $path"
done

say "GOVERNANCE HARDENING"
if [[ -f SOURCE_ADAPTATION_TRACEABILITY.md ]]; then
  pass "canonical file exists: SOURCE_ADAPTATION_TRACEABILITY.md"
else
  fail "required file missing: SOURCE_ADAPTATION_TRACEABILITY.md"
fi

if [[ -f SOURCE_ADAPTATION_TRACEABILITY.md ]]; then
  taxonomy_missing=0
  for decision in BUILD ADAPT REUSE "REFERENCE ONLY" REJECT; do
    if awk -v wanted="$decision" '
      /^## 2\. Canonical Decision Taxonomy$/ {inside=1; next}
      /^## 3\. Canonical Source Adaptation Record$/ {inside=0}
      inside && $0 == wanted {found=1}
      END {exit(found ? 0 : 1)}
    ' SOURCE_ADAPTATION_TRACEABILITY.md; then
      :
    else
      taxonomy_missing=1
      warn "source taxonomy missing canonical decision: $decision"
    fi
  done
  [[ "$taxonomy_missing" -eq 0 ]] && pass "source taxonomy: BUILD, ADAPT, REUSE, REFERENCE ONLY, REJECT"

  source_metadata_fields="$(awk '
    /^## 3\. Canonical Source Adaptation Record$/ {inside=1; next}
    /^Permitted Source Type values include:/ {inside=0}
    inside && /^[0-9]+\. / {c++}
    END {print c+0}
  ' SOURCE_ADAPTATION_TRACEABILITY.md)"
  [[ "$source_metadata_fields" -eq 22 ]] && pass "source metadata fields: 22" || fail "source metadata fields: $source_metadata_fields (expected 22)"

  if grep -Fq "Current Records: NONE" SOURCE_ADAPTATION_TRACEABILITY.md && \
     grep -Fq "Source Adaptation Records: NONE" SOURCE_ADAPTATION_TRACEABILITY.md; then
    pass "source adaptation current records: NONE"
  else
    fail "source adaptation current-state sanity check failed"
  fi
fi

pair_check() {
  pair_phrase="$1"
  pair_label="$2"
  if grep -Fq "$pair_phrase" QUOTATION_ENGINEERING_HARNESS.md && \
     grep -Fq "$pair_phrase" .agents/skills/quotation-card-execution/SKILL.md; then
    pass "$pair_label"
  else
    fail "$pair_label"
  fi
}

pair_check "CONTENT_ALIGNMENT_GATE" "CONTENT_ALIGNMENT_GATE present in Harness and Skill"
pair_check "Actual requested work" "actual requested-work extraction present"
pair_check "Correct Card ID does not" "correct Card plus wrong content protection present"
pair_check "future-Card" "future Card leakage protection present"
pair_check "invented requirement" "invented requirement protection present"
pair_check "mixed" "mixed Card scope protection present"
pair_check "out-of-scope" "out-of-scope protection present"
pair_check "SOURCE_ADAPTATION_GATE" "SOURCE_ADAPTATION_GATE present in Harness and Skill"
pair_check "No material external" "no silent copying protection present"
pair_check "UNKNOWN or UNVERIFIED" "license protection present"
pair_check "disguise" "BUILD anti-disguise protection present"
pair_check "ADAPT" "ADAPT handling present"
pair_check "REUSE" "REUSE handling present"
pair_check "REFERENCE ONLY" "REFERENCE ONLY handling present"
pair_check "REJECT" "REJECT handling present"
pair_check "NOT_APPLICABLE" "NOT_APPLICABLE handling present"
pair_check "CARD_QUALITY_GATE" "Card quality-gate integration present"

say "ARCHITECTURE CHANGE CAPTURE"
architecture_missing=0
for phrase in "Architecture Before:" "Change Introduced:" "Architecture After:" "Why Changed:" "Affected Components:" "Boundary / Dependency Impact:" "Tradeoff / Limitation:"; do
  grep -Fq "$phrase" CARD_LEARNING_AND_DECISION_LOG.md || { architecture_missing=1; warn "architecture capture field missing: $phrase"; }
done
[[ "$architecture_missing" -eq 0 ]] && pass "Architecture Before/After capture fields present"
grep -Fq "Future Revisit Condition:" CARD_LEARNING_AND_DECISION_LOG.md && info "Future Revisit Condition: PRESENT" || info "Future Revisit Condition: NOT_PRESENT"

say "EVIDENCE HONESTY SANITY"
if grep -Fq "Application Implementation: NOT_STARTED" PROJECT_CONTROL.md && \
   ! grep -Fq "Implementation Evidence: COMPLETE" PROJECT_CONTROL.md && \
   ! grep -Fq "Git Evidence: COMPLETE" PROJECT_CONTROL.md && \
   ! grep -Fq "Live Bedrock evidence: COMPLETE" PROJECT_CONTROL.md; then
  pass "no contradictory implementation evidence claim in current control"
else
  fail "contradictory implementation evidence claim detected"
fi
if [[ ! -d tests ]] && ! grep -Fq "Test PASS claims: COMPLETE" PROJECT_CONTROL.md; then
  pass "no contradictory test PASS claim with absent tests"
else
  warn "test PASS claim requires review"
fi
if [[ -f CARD_LEARNING_AND_DECISION_LOG.md ]] && \
   grep -Fq "Application Implementation: NOT_STARTED" CARD_LEARNING_AND_DECISION_LOG.md && \
   ! grep -Fq "Source Adaptation Records: IMPLEMENTED" SOURCE_ADAPTATION_TRACEABILITY.md; then
  pass "no contradictory source-adaptation implementation claim"
else
  fail "contradictory source-adaptation implementation claim detected"
fi

say "PROJECT_CONTROL"
if [[ -f PROJECT_CONTROL.md ]]; then
  for label in "Project Phase" "Application Implementation" "Active Card" "Active Card State" "Next Roadmap Card" "Next Card Authorized" "Safe Resume"; do
    line="$(grep -E -m1 "^$label:" PROJECT_CONTROL.md 2>/dev/null || true)"
    [[ -n "$line" ]] && info "$line" || warn "field not reliably parsed: $label"
  done
else
  fail "PROJECT_CONTROL.md cannot be inspected"
fi

say "ROADMAP / CARD CONSISTENCY"
if [[ -f AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md && -f QUOTATION_CARD_SPECIFICATIONS.md && -f QUOTATION_CARD_EVIDENCE_MAP.md ]]; then
  pass "roadmap, specifications, and evidence map are present"
  for n in $(seq 1 20); do
    id="V1-C$(printf '%02d' "$n")"
    grep -Fq "$id" AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md && pass "Roadmap contains $id" || fail "Roadmap missing $id"
    grep -Fq "$id" QUOTATION_CARD_SPECIFICATIONS.md && pass "Card Specifications contains $id" || fail "Card Specifications missing $id"
    grep -Fq "$id" QUOTATION_CARD_EVIDENCE_MAP.md && pass "Evidence Map contains $id" || fail "Evidence Map missing $id"
    grep -Fq "$id" CARD_LEARNING_AND_DECISION_LOG.md && pass "Learning Log contains $id" || fail "Learning Log missing $id"
  done
else
  fail "roadmap/card documents are missing"
fi

say "LEARNING / DECISION LOG"
if [[ -f CARD_LEARNING_AND_DECISION_LOG.md ]]; then
  learning_cards="$(awk '/^## V1-C[0-9][0-9] — /{c++} END{print c+0}' CARD_LEARNING_AND_DECISION_LOG.md)"
  learning_sections="$(awk '/^## V1-C[0-9][0-9] — /{inside=1} inside && /^### [0-9]+\. /{c++} END{print c+0}' CARD_LEARNING_AND_DECISION_LOG.md)"
  expected_ids="$(for n in $(seq 1 20); do printf 'V1-C%02d ' "$n"; done)"
  learning_ids="$(awk '/^## V1-C[0-9][0-9] — /{print $2}' CARD_LEARNING_AND_DECISION_LOG.md | tr '\n' ' ' )"
  [[ "$learning_cards" -eq 20 ]] && pass "Learning Log Card records: 20" || fail "Learning Log Card records: $learning_cards (expected 20)"
  [[ "$learning_sections" -eq 360 ]] && pass "Learning Log Card-specific sections: 360" || fail "Learning Log Card-specific sections: $learning_sections (expected 360)"
  [[ "$learning_ids" == "$expected_ids" ]] && pass "Learning Log Card order: V1-C01 through V1-C20" || fail "Learning Log Card order is inconsistent"
  learning_complete="$(awk '/^Learning Documentation Status:$/ {getline; if ($0 == "COMPLETE") c++} END{print c+0}' CARD_LEARNING_AND_DECISION_LOG.md)"
  if [[ "$learning_complete" -gt 0 ]]; then
    warn "Learning Log contains $learning_complete COMPLETE learning status value(s) while implementation is NOT_STARTED"
  else
    pass "no false COMPLETE learning status detected"
  fi
else
  fail "Learning Log cannot be inspected"
fi

say "GIT"
if [[ -d .git ]]; then
  info "Git repository: YES"
  info "Branch: $(git branch --show-current 2>/dev/null || printf '%s' NOT_AVAILABLE)"
  info "HEAD: $(git rev-parse --short HEAD 2>/dev/null || printf '%s' NOT_AVAILABLE)"
  status="$(git status --short 2>/dev/null || true)"
  [[ -z "$status" ]] && pass "working tree is clean" || { warn "working tree has changes"; printf '%s\n' "$status"; }
  git remote -v 2>/dev/null || true
else
  info "Git repository: NO"
  info "Branch: NOT_AVAILABLE"
  info "HEAD: NOT_AVAILABLE"
  info "Working tree: NOT_AVAILABLE"
fi

say "PYTHON / PROJECT BASELINE"
if command -v python3 >/dev/null 2>&1; then
  pyver="$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null || true)"
  pass "python3 available: ${pyver:-unknown}"
else
  warn "python3 unavailable"
fi
for path in pyproject.toml requirements.txt; do
  [[ -f "$path" ]] && info "present: $path" || info "NOT_CREATED: $path"
done
for path in src tests; do
  [[ -d "$path" ]] && info "present: $path/" || info "NOT_CREATED: $path/"
done

say "PYTEST"
if [[ -d tests ]]; then
  if command -v python3 >/dev/null 2>&1 && python3 -m pytest --version >/dev/null 2>&1; then
    if PYTHONDONTWRITEBYTECODE=1 python3 -m pytest --collect-only -q -p no:cacheprovider >/dev/null 2>&1; then
      pass "pytest collection: PASS"
    else
      fail "pytest collection: FAIL"
    fi
  else
    warn "pytest collection: NOT_RUN"
  fi
else
  info "pytest collection: NOT_AVAILABLE (tests directory not created)"
fi

say "SECRET / SENSITIVE FILE NAMES"
secret_found=0
while IFS= read -r -d '' path; do
  name="${path##*/}"
  case "$name" in
    .env.example) ;;
    .env|.env.*|credentials|credentials.json|aws_credentials|*.pem|*.key|secret*|token*)
      warn "SECRET_OR_SENSITIVE_FILE_DETECTED: $path"; secret_found=1 ;;
  esac
done < <(find . -path './.git' -prune -o -path './.venv' -prune -o -path './venv' -prune -o -path './__pycache__' -prune -o -path './build' -prune -o -path './dist' -prune -o -type f -print0)
[[ "$secret_found" -eq 0 ]] && pass "no suspicious secret-bearing filenames detected"

say "CREDENTIAL PATTERN CHECK"
credential_files="$(rg -l --hidden --glob '!.git/**' --glob '!.venv/**' --glob '!venv/**' --glob '!__pycache__/**' --glob '!build/**' --glob '!dist/**' '(AKIA|ASIA)[A-Z0-9]{12,}' . 2>/dev/null || true)"
if [[ -n "$credential_files" ]]; then
  while IFS= read -r path; do [[ -n "$path" ]] && warn "possible credential pattern detected in $path"; done <<< "$credential_files"
else
  pass "no obvious AWS credential pattern detected"
fi

say "AWS / PROVIDER CONFIGURATION"
if command -v aws >/dev/null 2>&1; then
  info "AWS CLI: PRESENT"
  region="$(aws configure get region 2>/dev/null || true)"
  info "AWS region: ${region:-NOT_CONFIGURED}"
else
  info "AWS CLI: NOT_AVAILABLE"
  info "AWS region: NOT_CHECKED"
fi
if command -v python3 >/dev/null 2>&1 && python3 -c 'import boto3' >/dev/null 2>&1; then info "boto3: PRESENT"; else info "boto3: NOT_AVAILABLE"; fi
if rg -l --hidden --glob '!.git/**' --glob '!*/__pycache__/**' '(Amazon Bedrock|bedrock|Bedrock)' . >/dev/null 2>&1; then info "Bedrock repository integration: PRESENT_REFERENCES_ONLY"; else info "Bedrock repository integration: NOT_PRESENT"; fi
if rg -l --hidden --glob '!.git/**' --glob '!*/__pycache__/**' '(Amazon S3|s3|S3)' . >/dev/null 2>&1; then info "S3 repository integration: PRESENT_REFERENCES_ONLY"; else info "S3 repository integration: NOT_PRESENT"; fi
info "No Bedrock, S3, or other AWS API calls are made by this script."

say "APPLICATION / MIGRATION STRUCTURE"
for name in domain application adapters agent api; do
  [[ -d "src/$name" || -d "$name" ]] && info "boundary present: $name" || info "NOT_CREATED: $name"
done
info "migration fragments: NOT_PRESENT; canonical specifications are authoritative"

say "PASS=$PASS WARN=$WARN FAIL=$FAIL"
if [[ "$FAIL" -gt 0 ]]; then say "BOOTSTRAP_STATUS: FAIL"; exit 1; fi
if [[ "$WARN" -gt 0 ]]; then say "BOOTSTRAP_STATUS: WARN"; exit 0; fi
say "BOOTSTRAP_STATUS: PASS"; exit 0

# THIS SCRIPT INSPECTS.
# IT DOES NOT REPAIR.
# IT DOES NOT AUTHORIZE.
# IT DOES NOT IMPLEMENT.
# IT DOES NOT DEPLOY.
# BOOTSTRAP PASS != CARD APPROVAL.
