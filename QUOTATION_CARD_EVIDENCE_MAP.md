# AI Quotation Intelligence System — V1 Card Evidence Map

Status: CANONICAL VERIFIED EVIDENCE LEDGER
This file does not own live operational state. PROJECT_CONTROL.md is authoritative
for current phase, Active Card, authorization, blockers, and current Git state.
Implementation evidence below is immutable Card evidence, not a live-state ledger.

## 0. Role and Ownership

QUOTATION_CARD_EVIDENCE_MAP.md records actual implementation evidence for every official V1 Card.

It owns:

- files actually changed;
- commands actually run;
- tests actually executed;
- test results;
- failures;
- evaluation results;
- Exit Gate evidence;
- Git evidence when Git exists;
- known limitations;
- learning records;
- Card completion proof.
- FINAL_CARD_STATE_CONSISTENCY_GATE result and cross-section consistency evidence.

It does not own:

- architecture;
- Roadmap identity or order;
- live authorization;
- Card contracts;
- project invariants.

Ownership:

PROJECT_PROFILE.md → stable architecture and invariants.
PROJECT_CONTROL.md → live state and authorization.
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md → Card identity and order.
QUOTATION_CARD_SPECIFICATIONS.md → detailed Card contract.
QUOTATION_CARD_EVIDENCE_MAP.md → verified implementation evidence.
CARD_LEARNING_AND_DECISION_LOG.md → engineering rationale, alternatives, failure/root-cause/fix explanation, tradeoffs, and lessons learned.

This file does not authorize implementation.

The Evidence Map may record whether the Learning / Decision Log is current, but it does not duplicate its narrative. The Evidence Map owns observed and proven technical evidence and completion proof; CARD_LEARNING_AND_DECISION_LOG.md owns engineering rationale and learning. Documentation status is not implementation evidence: COMPLETE learning documentation does not prove code, tests, Exit Gates, AWS, Bedrock, S3, or Git delivery. Technical evidence does not prove that engineering rationale was documented. Both are independent completion requirements.

Learning Documentation Status vocabulary:

~~~text
NOT_STARTED → no implementation learning has been recorded
PARTIAL → some actual implementation reasoning is recorded but required learning remains incomplete
CURRENT → the record is up to date with the current implementation checkpoint
COMPLETE → the final learning record satisfies the Card completion documentation requirement
~~~

## 1. Evidence Principles

~~~
DESIGN INTENT != IMPLEMENTATION EVIDENCE
TEST NOT RUN != PASS
STATIC INSPECTION != RUNTIME VERIFICATION
EXPECTED RESULT != OBSERVED RESULT
CODE EXISTS != EXIT GATE PROVEN
MERGED != COMPLETE
DEPLOY CONFIG EXISTS != DEPLOYED
BEDROCK CODE EXISTS != BEDROCK VERIFIED
S3 CODE EXISTS != S3 VERIFIED
FAILURE IS EVIDENCE
UNKNOWN MUST STAY UNKNOWN
NO EVIDENCE → NO COMPLETION CLAIM
~~~

Never fabricate command output, test results, Git commits, AWS state, Bedrock responses, S3 behavior, deployment state, runtime behavior, file paths, or evaluation scores.

## 2. Verified Project Evidence Summary (Not Live State)

This is a historical C01 checkpoint snapshot captured before the C02–C06
application Cards were implemented. It is retained as historical evidence and
must not be read as the current capability summary.

~~~
Project: AI Quotation Intelligence System
Target: V1
Application Implementation: V1-C01 BASELINE IMPLEMENTED / DOMAIN IMPLEMENTATION NOT_STARTED
Active Card: NONE
Completed Cards: V1-C01 — Repository Baseline
Implementation Evidence: PRESENT — C01 baseline
Git Repository: YES
Tests: C01 BASELINE TESTS PRESENT / PASS
AWS Implementation: NOT_STARTED
Bedrock Integration: NOT_STARTED
S3 Integration: NOT_STARTED
Deployment: NOT_STARTED
Golden Case: NOT_STARTED
~~~

Governance migration evidence is not V1 application implementation evidence.

## 2A. Post-C06 Full-Project Audit and Systemic Repair Evidence

The full-project audit identified three issues before V1-C07: a mistyped
historical C01 delivery hash, an application-level C05 aggregate boundary that
allowed incompatible metric/unit values to be combined, and a stale C01-only
README. The bounded maintenance repair corrected the hash, added homogeneous
metric/unit validation and adversarial C05 tests, updated README through C06,
and added narrow Git-evidence and capability-documentation review guidance.

Observed repair validation: C05 focused tests 12 passed; C04/C05/C06 related
tests 31 passed; full suite 50 passed; governance regression 60 passed; and
governance view reconciliation passed. The maintenance repair was delivered
through commit `81b8a61c6c585800f484362f2714092f2375edd8`, PR #14, and merge
commit `eda681e24d4536bc8596f298d5c903471d96b52e`. V1-C07 remains
unauthorized.

Subsequent full-project audit verification found that the prior remediation had
itself recorded an invalid C01 hash, while the C03 delivery evidence used an
abbreviated hash. Git object and PR verification resolved the exact C01 delivery
commit as `93d6bdbdc074687f366658c4ebddc43912b7571e` and the exact C03 delivery
commit as `204147915fcab7e2e161e083230b0b56cb2f97e0`. The same remediation also
reconciled stale C08-pending/C07-only current-state sections in
PROJECT_CONTROL.md. No application or Harness files were changed.

## 2B. AEVS v1.1 Independent Audit and Bounded Remediation (Governance Only)

The prior Phase 1 implementation self-audit reported PASS. The subsequent
independent Claude Code audit was reported as **FAIL** with three MEDIUM
findings: M-01 incomplete package-module coverage, M-02 forbidden-boundary
matching gaps, and M-03 an unpinned audited candidate. It reported no
CRITICAL or HIGH findings. This is historical audit evidence supplied for
remediation, not an independent PASS for the changed candidate.

Observed bounded remediation:

- M-01: `tests/test_architecture.py` now discovers all package `*.py` files,
  requires an exact classification map, and inspects Core imports including
  `__init__.py`. Isolated new-module and new-package fixtures return the
  expected failure when unclassified.
- M-02: import direction resolves local modules by architectural category.
  Isolated provider adapter, agent tools, quotation agent, tooling package,
  API boundary, boto3, and botocore probes all return the expected failure.
- M-03: at this remediation stage, `scripts/candidate_identity.py` computed a
  read-only SHA-256 identity from base revision, branch, changed/added/deleted paths, modes, and exact
  content hashes. Isolated Git fixtures prove stable identity when unchanged,
  and mismatch after same-path content change, untracked addition, deletion,
  or base-revision change. A staged-content check fails before staging and
  passes after the exact candidate is staged in the fixture. A repository
  subdirectory probe detects unstaged drift elsewhere in the repository.

Executed validation: `.venv/bin/pytest -q tests/test_architecture.py
tests/test_candidate_identity.py` → 18 passed; `.venv/bin/pytest -q` → 88
passed; `bash scripts/test_governance_harness.sh` → PASS=60, FAIL=0;
`.venv/bin/python scripts/reconcile_governance_views.py --check` → PASS;
`bash scripts/quotation_session_bootstrap.sh` → PASS=127, WARN=1, FAIL=0
(working-tree changes); `git diff --check` → PASS. Python compilation,
package/config import smoke, and governance shell syntax checks passed.
An initial architecture-fixture test failed because its relative import
pointed at a nonexistent namespace; the fixture was corrected and the
focused suite reran successfully. That failed attempt remains part of the
remediation history.

Known limits: the architecture check is static and does not inspect dynamic
imports, runtime object/value leakage, or semantic misuse. Candidate identity
covers visible untracked files; ignored files are excluded from the delivery
candidate and would change the identity if force-staged. It does not itself
prove independent audit authorization. **Independent re-audit: PENDING.**
No delivery or C09 implementation is evidenced here.

Independent re-audit after the earlier bounded remediation reported FAIL:
M-01 CLOSED, M-03 CLOSED, M-02 direct probes CLOSED, and new M-04 OPEN.
M-04 was a Core → Support → forbidden-category static re-export escape:
the prior checker inspected Core outbound imports but not Support outbound
imports. The M-04 remediation now checks outbound static imports for every
classified module against an explicit category policy. Core allows Core and
Support; Support allows only Support; the existing Provider allows Core and
Support. Future Agent Tool/Application Boundary local dependency directions
remain empty pending their owning Cards. A reachability self-check rejects a
policy that would make a forbidden category reachable from Core.

M-04 focused proof, using isolated temporary package trees: direct
Core → Provider FAIL as expected; Core → Support → Provider, Agent Tool, and
Application Boundary each FAIL as expected; a Support `__init__.py` Provider
re-export and Support boto3 import each FAIL as expected; legitimate Core →
Support and Support → Support/stdlib imports PASS; a weakened Support policy
that allows Provider FAILS the policy self-check. The current package's
complete module classification/import check and new unclassified module and
package-`__init__.py` probes pass. `.venv/bin/pytest -q
tests/test_architecture.py tests/test_candidate_identity.py` → 25 passed;
`.venv/bin/pytest -q` → 95 passed; `bash scripts/test_governance_harness.sh`
→ PASS=60, FAIL=0; `.venv/bin/python
scripts/reconcile_governance_views.py --check` → PASS; `bash
scripts/quotation_session_bootstrap.sh` → PASS=127, WARN=1, FAIL=0
(dirty-tree warning); `git diff --check`, Python compilation, package/config
import smoke, and governance shell syntax checks → PASS. An initial focused
collection attempt failed with an indentation error in the new fixture test;
the misplaced call was repaired and the focused and full suites reran PASS.
The checker remains static: dynamic imports, runtime object/value leakage,
and semantic misuse are not proved absent. Independent M-04 re-audit:
**PENDING**. No Git delivery or C09 authorization is implied.

Subsequent independent AEVS v1.1 audit was reported PASS for candidate
`24fcc567464a755fa68e373fbc6b1bc38c31b7113cd8dae590ebaaa1afd614cd`.
Human delivery approval was supplied for that identity. The delivery attempt
STOPPED before staging, commit, push, PR, or merge: the then-current identity
hashed `main` as part of the candidate, while the Git workflow required a
delivery branch. The pre-staging identity matched, but moving the exact same
contents to a branch would have changed the hash. No delivery occurred.

Bounded branch/identity governance remediation changes the identity model:
base revision and sorted path/status/mode/content entries remain hashed;
branch is returned only as provenance. An isolated Git fixture computed the
same identity on `main` and `delivery/aevs-v1.1` with identical base and
candidate entries, then detected a one-byte content change. The fixture also
verified `verify --expected` and `--require-staged` on the delivery branch;
existing tests retain add, deletion, base-change, determinism, and staged/
worktree-drift probes. `.venv/bin/pytest -q tests/test_candidate_identity.py
tests/test_architecture.py` → 26 passed; `.venv/bin/pytest -q` → 96 passed;
`bash scripts/test_governance_harness.sh` → PASS=60, FAIL=0;
`.venv/bin/python scripts/reconcile_governance_views.py --check` → PASS;
`bash scripts/quotation_session_bootstrap.sh` → PASS=127, WARN=1, FAIL=0
(dirty-tree warning); `git diff --check`, Python compilation, package/config
import smoke, and governance shell syntax checks → PASS. No application source
or dependencies changed. The new candidate is **not independently audited**;
independent re-audit and new human delivery approval are PENDING. No real
delivery branch, staging, commit, push, PR, merge, or C09 work occurred.

The fresh independent branch/identity re-audit subsequently reported the
branch-only design verified but identified **M-05**: `verify --require-staged`
could falsely PASS while the index held unaudited bytes under local Git state
such as skip-worktree, assume-unchanged, clean filters, or
`core.fileMode=false`. The verifier reported an end-to-end unaudited commit
after that false PASS. This is an independent finding supplied for bounded
remediation, not an independent PASS for the current candidate.

M-05 local remediation uses one schema/base/path-status-mode-SHA256 identity
model over three directly inspected sources: worktree bytes, Git index blobs
and modes, and committed HEAD tree blobs and modes. Pre-stage verification
requires the worktree identity to match the audited identity. After staging,
`--require-staged` additionally requires the index identity to match and
rejects candidate skip-worktree/assume-unchanged flags. After commit,
`--require-committed` compares the committed tree directly with the audited
identity before push. Git porcelain visibility, clean-filtered worktree
comparisons, and `core.fileMode` settings are not used as staged truth.
Isolated Git fixtures exercise both flags, clean-filtered bytes, mode
divergence, extra/missing staged changes, exact deletion and untracked
addition semantics, a missing new worktree file, unaudited committed bytes,
an exact committed candidate, and symlink target bytes. Branch independence,
base/content sensitivity, and prior architecture tests remain in scope for
regression. During local self-review, the first worktree-state version could
omit a staged new path after its worktree file disappeared; the scan was
changed to fail explicitly and an isolated regression fixture was added.
The verifier runs at a point in time; it does not atomically bind
later Git actions, so delivery must still verify the intended commit/ref and
STOP on subsequent drift. Ignored files remain outside the delivery candidate.
Independent M-05 re-audit: **PENDING**. No real delivery action or C09 work is
evidenced.

M-05 executed local validation: `.venv/bin/pytest -q
tests/test_candidate_identity.py` → 19 passed; `.venv/bin/pytest -q
tests/test_architecture.py` → 19 passed; `.venv/bin/pytest -q` → 108 passed;
`bash scripts/test_governance_harness.sh` → PASS=60, FAIL=0;
`.venv/bin/python scripts/reconcile_governance_views.py --write` and
`--check` → PASS; `bash scripts/quotation_session_bootstrap.sh` →
PASS=127, WARN=1, FAIL=0 (dirty-tree warning); `git diff --check`, Python
compilation, package/config import smoke, and governance shell syntax checks
→ PASS. These are implementer-local results, not independent closure of M-05.

M-05b — The independent audit identified that replace refs could mask the
actual staged or committed blob: ordinary `git cat-file` follows
`refs/replace/*`, so the verifier could read audited bytes for a different
object ID and falsely PASS. Root cause: candidate Git object reads used the
default replace-aware Git behavior. Independent reproduction: isolated staged
and committed fixtures created replacement refs from unaudited blob IDs to
the audited blob ID; in both fixtures ordinary `git cat-file blob <unaudited>`
returned the audited bytes and the pre-fix verifier returned PASS. The new
attack tests failed before the fix for exactly that false-PASS behavior.
Fix: add Git's global `--no-replace-objects` option in the shared `_git`
helper, covering all Git plumbing reads including base/HEAD tree listings and
index/committed blob reads. Regression proof: after the fix, both attack tests
return FAIL for the unaudited candidate; exact staged and exact committed
candidates still PASS, and ordinary wrong staged/committed candidates FAIL.
The focused candidate identity suite reports 21 passed and the architecture
suite reports 19 passed. The independent attack tests also assert the ordinary
`cat-file` replacement behavior to ensure the fixture exercises the finding.
Full validation: `.venv/bin/pytest -q` → 110 passed; `bash
scripts/test_governance_harness.sh` → PASS=60, FAIL=0; `.venv/bin/python
scripts/reconcile_governance_views.py --write` and `--check` → PASS; `bash
scripts/quotation_session_bootstrap.sh` → PASS=127, WARN=1, FAIL=0 (working
tree changes); `git diff --check` → PASS; Python compilation and candidate
module import smoke → PASS. Bootstrap credential-pattern and suspicious
secret-filename checks → PASS. The independent M-05b re-audit later reported
PASS for the exact candidate identity recorded below. No application code,
dependencies, or C09 authorization changed.

AEVS v1.1 post-delivery provenance blocker and resolution — the approved,
independently audited candidate reached PR #22 but the first delivery attempt
stopped before merge because the workflow was interpreted to require the
delivery, PR, and merge identifiers in the Evidence Map before merge. Those
values did not all exist until the Git actions occurred. The root cause was
not distinguishing frozen pre-delivery candidate evidence from post-delivery
provenance. The Post-Delivery Provenance Rule now makes those future values
non-blocking; observed identifiers can be reported in the final delivery
output, with any durable retrospective record handled separately after
delivery. The audited candidate was not changed to add delivery identifiers.

Observed PR #22 delivery: independent audit PASS and delivery approval GRANTED
for candidate identity
`f2da89985d748c0362533e1c2c252bcb50c151f6a6873ceef32d77d4dffd6c2a`; branch
`delivery/aevs-v1.1`; delivery commit
`7d085c4f06bb556df1df4a1c41bd6e9a092da42d`; PR
https://github.com/jo-soroush/ai-quotation-intelligence/pull/22; merge commit
`8a10c41023770ffcd3be13de93b3ccb1af838319`. The PR had no reported checks;
no checks were bypassed. Final local `main` and `origin/main` both resolved to
`8a10c41023770ffcd3be13de93b3ccb1af838319`, ahead/behind 0/0, working tree
clean. Post-delivery validation: full pytest 110 passed; candidate identity
21 passed; architecture 19 passed; Governance Harness PASS=60/FAIL=0;
reconciliation `--check` PASS; bootstrap PASS=128/WARN=0/FAIL=0; compilation,
import/config and shell syntax checks PASS; `git diff --check` PASS;
`FINAL_CARD_STATE_CONSISTENCY_GATE` for V1-C08 COMPLETE PASS. C01–C08 remain
COMPLETE, Active Card is NONE, and C09 remains NOT_AUTHORIZED / NOT_STARTED.

Phase B maintenance validation history: the first Governance Harness run
reported GD-07 FAIL (PASS=60, FAIL=1). Root cause: the new scenario used the
repository-state fixture, which does not construct the approval snapshot its
candidate-immutability assertion requires. Fix: use the existing isolated
approval fixture and copy the three canonical policy files into it. The
scenario then verified the rules, allowed commit/PR/merge with future IDs
marked NOT_CREATED, kept candidate state unchanged, and rejected an injected
pre-merge SHA requirement. Rerun: `bash scripts/test_governance_harness.sh` →
PASS=61, FAIL=0.

Independent governance audit of the Phase B candidate reported PASS with
Critical=0, High=0, Medium=0. Its GD-07 mutation-coverage weakness was LOW:
the case rejected only one injected merge-SHA precondition, so other policy
regressions could pass undetected. Root cause was a narrow text check rather
than coverage of each Post-Delivery Provenance Rule invariant. Bounded GD-07
remediation strengthens the existing temporary-fixture GD-07 case: the valid
eight-clause policy must pass structural/semantic checks, while seven rewritten
clause mutants and seven contradictory-addition mutants must be rejected.
The mutants cover future Git identifier preconditions, editing the frozen
audited candidate, bypassing human delivery approval, skipping staged or
committed identity verification, embedding a maintenance candidate's own SHA,
recursive evidence commits, and fabricated/predicted provenance. The focused
GD-07 run passed all 14 mutation checks and the valid baseline. Independent
re-audit of this changed governance candidate remains PENDING.
Final remediation validation: full Governance Harness PASS=61/FAIL=0;
`.venv/bin/pytest -q` 110 passed; governance reconciliation `--check` PASS;
bootstrap PASS=127/WARN=1/FAIL=0 (expected uncommitted maintenance tree);
`git diff --check`, Bash syntax, Python compilation/import, and obvious
credential-pattern checks PASS. No application or dependency files changed.

M-GD07 follow-up finding: the preceding GD-07 checker rejected contradictions
only inside GIT_WORKFLOW.md §13A; the Harness and Skill needed only to mention
the rule, and contradictory policy elsewhere could escape. Root cause was
scoping the negative scan to the extracted §13A body and returning early for
the companion owners. The canonical policy was not changed. GD-07 now scans
the complete text of each of the three owners, retains structural safeguards
for §13A and companion delivery rules, and checks §13A's PROJECT_CONTROL.md
live-state ownership. Temporary mutants place each tested contradiction in
§13A, elsewhere in GIT_WORKFLOW.md, in the Harness, and in the Skill. Focused
GD-07 passed the valid baseline and rejected 8 rewritten-clause mutants plus
64 contradictory-addition mutants, including separate commit/PR/merge future
identifier preconditions and the requested wording variants. This proves
rejection of those exercised semantic mutations, not arbitrary paraphrases.
Independent re-audit of the changed governance candidate remains PENDING.

M-GD07b independent re-audit: FAIL, with one new MEDIUM finding and no new
Critical or High findings. Placement coverage had improved, but the negative
regexes recognized only 11 of 51 independently tried natural wordings; no
future-identifier precondition wording in that matrix was caught. In
particular, `Expected merge SHA may be written before merge.` passed the real
focused GD-07 case at all eight probed placements. Root cause: a set of
sentence-shape patterns cannot reliably decide whether arbitrary prose
contradicts policy. The audit made no project-file edits; the starting
candidate identity was
`1aae7b77046c8bd63e5d7490104c8a002df416e3769340d11d98901d6e14778a`.

Bounded M-GD07b remediation keeps the canonical policy text unchanged and
replaces the negative prose regexes with approved SHA-256 byte digests for
the three complete policy owners in the existing GD-07 Harness case. Existing
structural safeguard checks remain. Any edit anywhere in those owners,
including a contradictory addition or benign rewording, now fails closed
until a separately reviewed policy update explicitly refreshes its digest.
This is policy-change detection, not semantic classification of English.
The focused case passed the unchanged baseline and rejected 8 clause rewrites,
25 distinct added wordings at 8 placements each, and 3 protective edits that
correctly require review. Those wordings include the audit's named miss,
passive future-SHA prerequisite, indirect approval bypass, committed-tree
skip, own-hash, recursive evidence, invented PR number, and alternate
live-state owner. Independent re-audit of this new candidate is PENDING.
Final local validation: focused GD-07 PASS; Governance Harness PASS=61/FAIL=0;
`.venv/bin/pytest -q` 110 passed; reconciliation `--check` PASS;
bootstrap PASS=127/WARN=1/FAIL=0 (uncommitted tree); `git diff --check`,
shell syntax, Python compilation/import, and credential-pattern checks PASS.

## 3. Evidence Record Standard

Each Card record uses exactly these sections:

1. Card
2. Contract Source
3. State
4. Human Start Approval
5. Files Changed
6. Commands Run
7. Focused Tests
8. Relevant Regression
9. Card Evaluation
10. Commercial / Data Invariants
11. AI / Provider Validation
12. Security Validation
13. Failures / Blockers
14. Exit Gate Evidence
15. CARD_QUALITY_GATE
16. Git Evidence
17. Known Limitations
18. What We Learned
19. Completion Evidence
20. Recommended State

Card-record values are factual evidence for the named Card and checkpoint; they
are not a competing current-state authority. Current live state is read from
PROJECT_CONTROL.md and runtime Git commands.

## 4. Future Evidence Expectations

These are expected evidence categories, not current evidence:

For consequential requirements and invariants in future Cards, use a compact
trace in the applicable Card record, without changing its numbered section
structure:

| ID | Canonical Requirement / Invariant | Implementation Evidence | Verification Evidence | Observed Result |
| --- | --- | --- | --- | --- |
| Card-local ID | Exact canonical clause/reference | Path/behavior once implemented; otherwise NONE | Executed command/case and result once run; otherwise NONE | NOT_YET_EXECUTED until observed |

Do not trace trivial details. Planned cases and expected behavior are not
execution evidence. After execution, preserve failures and subsequent recovery
results; do not replace a failed observation with a bare PASS.
For C09 and later, record the exact frozen candidate identity, independent
verifier findings and PASS/BLOCKED result, remediation and re-audit where
needed, and any post-audit re-verification in the applicable Card record.
An implementation self-audit is labeled SELF-AUDIT, never independent PASS.

- V1-C01 — Repository Baseline: repository structure; Git initialization; configuration; importability; test baseline; .gitignore; secret hygiene
- V1-C02 — Domain Models: domain model files; validation tests; null/zero semantics; estimated/actual separation; numeric validation
- V1-C03 — Synthetic Historical Data: dataset or generator; record count; schema validity; synthetic provenance; designed pattern checks
- V1-C04 — Quote Calculation Engine: deterministic arithmetic; hours × rate; totals; edge cases; reconciliation
- V1-C05 — Historical Comparison Engine: hour/cost variance; percentage variance; aggregate statistics; missing actual handling
- V1-C06 — Similar Quote Retrieval: ranking/retrieval tests; explainable similarity; empty/insufficient results; no price-copy behavior
- V1-C07 — Risk Evidence Engine: evidence counts; supporting quote IDs; aggregate reconciliation; insufficient evidence behavior
- V1-C08 — Amazon Bedrock Integration: provider contract; Bedrock adapter; structured output validation; AI_INVALID; AI_UNAVAILABLE; provider isolation; real Bedrock verification only if executed
- V1-C09 — Agent Tools: tool contracts; validation; delegation to existing services; failure propagation
- V1-C10 — Quotation Agent: tool use; tool selection; structured result; unsupported claim rejection; no deterministic override; failure paths
- V1-C11 — Human Review Gate: approve path; reject path; approval-required behavior; invalid transition behavior
- V1-C12 — Excel Generation: workbook; required sheets; deterministic totals; reconciliation; approval requirement
- V1-C13 — FastAPI Application: API routes; typed validation; error mapping; business-logic delegation; approval behavior
- V1-C14 — Amazon S3 Integration: storage adapter; serialization; retrieval validation; failure behavior; provider isolation
- V1-C15 — AWS Deployment: Lambda/API Gateway artifacts; deployed verification; IAM review; local mode preserved
- V1-C16 — CloudWatch Observability: structured logs; correlation IDs; failure traceability; redaction; CloudWatch evidence if deployed
- V1-C17 — Evaluation Harness: repeatable evaluation cases; metric results; PASS/FAIL behavior; intentionally bad-case detection
- V1-C18 — Guardrails and Failure Handling: applicable failure states; no silent fallback; invalid AI rejection; approval boundary; Excel reconciliation; commercial invariant enforcement
- V1-C19 — Golden Case: complete end-to-end scenario; historical retrieval; deterministic analysis; RiskEvidence; Bedrock/agent; human approval; Excel; API/storage/cloud path where applicable; observability; evaluation
- V1-C20 — Demo UI: UI flow; draft/approved distinction; approval interaction; evidence display; Excel access; no duplicated business logic

## 5. Failure Recording Rule

Failures must be recorded rather than erased. Future failure records must include:

Timestamp:
Card:
Step:
Command/Test:
Observed Result:
Expected Result:
Failure Code:
Impact:
Rollback Needed:
Resolved:
Resolution Evidence:

A failed test remains visible after later repair.

## 6. Test Evidence Format

Future actual test records must include:

Command:
Scope:
Observed Result:
PASS / FAIL:
Relevant Output:
Files/Components Covered:
Limitations:

Do not write a generic “tests passed” claim without actual test identity and output.

## 7. Evaluation Evidence Format

Future evaluation records must include:

Evaluation ID:
Card:
Dataset/Case:
Metric:
Expected Threshold if defined:
Observed Value:
PASS / FAIL / INFORMATIONAL:
Evidence Source:
Limitations:

Do not invent thresholds unless defined by the owning Card or approved evaluation design.

## 8. Commercial / Data Invariant Evidence

Future evidence must explicitly prove applicable rules such as:

~~~
missing != zero
estimated != actual
rates validated
currency explicit
deterministic totals
variance deterministic
evidence counts reconcile
RiskEvidence traceable
synthetic provenance preserved
Excel totals reconcile
~~~

These are not marked PASS globally. They become evidence per Card.

## 9. AI Evidence

Future AI evidence must distinguish:

- mocked provider test;
- local adapter test;
- real Bedrock call;
- agent evaluation.

A mocked response is not live Bedrock verification.

Where applicable, record model ID, provider, structured schema, tool calls, failure state, validated output, unsupported claims, latency, and token metadata only when actually available.

Do not store secrets or sensitive prompt contents unnecessarily.

## 10. AWS Evidence

Future AWS evidence must distinguish:

- configuration exists;
- resource created;
- resource deployed;
- resource invoked successfully.

For S3, an adapter test is not real S3 verification. For Lambda/API Gateway, deployment configuration is not a deployed API. For CloudWatch, logging code is not CloudWatch evidence.

## 11. Git Evidence

Once Git exists, Card evidence may record:

Branch:
Start Commit:
End Commit:
Commit:
Push:
PR:
Merge:

Until Git exists:

NOT_AVAILABLE

Never invent a commit hash.

## 12. Exit Gate Proof

Every Card Exit Gate must later be proven with specific evidence:

Exit Gate Requirement:
Evidence:
PASS / FAIL / NOT_PROVEN:
Notes:

A Card cannot be COMPLETE if any required Exit Gate condition is NOT_PROVEN.

## 13. CARD_QUALITY_GATE

Future gate fields:

Focused Tests:
Relevant Regression:
Card Evaluation:
Commercial/Data Invariants:
AI Validation:
Security Validation:
Exit Gate:
Evidence Current:
PROJECT_CONTROL Updated:
Git Diff Reviewed:
Git Status Reviewed:
Known Limitations Recorded:

CARD_QUALITY_GATE:
PASS | BLOCKED | NOT_RUN

Current value for unstarted Cards: NOT_RUN. V1-C01 values are recorded in its Card record below.

## 14. Completion Rule

Card COMPLETE requires:

- exact contract satisfied;
- required tests actually executed;
- required evaluation actually executed;
- applicable invariants proven;
- failures resolved or explicitly accepted;
- exact Exit Gate proven;
- evidence map current;
- What We Learned recorded;
- CARD_QUALITY_GATE PASS;
- FINAL_CARD_STATE_CONSISTENCY_GATE PASS after final reconciliation;
- Git evidence current where applicable;
- PROJECT_CONTROL reconciled;
- approved delivery complete where required.

Without these:

NOT COMPLETE

## 15. Evidence Update Discipline

Update evidence incrementally during implementation. Do not reconstruct history from memory.

After meaningful validation, record the observed result. After failure, record it immediately. After recovery, record both the original failure and recovery proof.

Evidence Map: records observed failure and recovery evidence.
Learning Log: records explanation, root cause, fix rationale, tradeoff, and lesson.

Future Card completion requires the Evidence Map to be current AND the Learning / Decision Log to be current before CARD_QUALITY_GATE may PASS. Neither record replaces the other.

Governance migration output is not V1 application Card evidence.

## 16. Current Card Evidence Records

## V1-C01 — Repository Baseline

### 1. Card

V1-C01 — Repository Baseline

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

pyproject.toml
src/ai_quotation_intelligence/__init__.py
src/ai_quotation_intelligence/config.py
src/ai_quotation_intelligence/logging_config.py
tests/test_baseline.py
.gitignore
.env.example
README.md

### 6. Commands Run

git switch -c card/v1-c01-repository-baseline
./.venv/bin/pip install -e '.[dev]'
./.venv/bin/python -c 'import ai_quotation_intelligence; from ai_quotation_intelligence.config import load_settings; assert load_settings().environment == "local"'
./.venv/bin/pytest
git ls-files / secret-pattern checks
provider dependency and future-Card leakage checks
git status --short --branch
git log -1 --format='%H%n%s'
git show --stat --oneline HEAD
git remote -v
git rev-parse --abbrev-ref --symbolic-full-name '@{u}'
git rev-list --left-right --count HEAD...@{u}
bash scripts/final_card_state_consistency.sh
bash scripts/final_card_state_consistency.sh /private/tmp/c01-table-mismatch
bash scripts/final_card_state_consistency.sh /private/tmp/c01-exit-mismatch
bash scripts/final_card_state_consistency.sh /private/tmp/c01-active-mismatch

### 7. Focused Tests

PASS — 3 passed in 0.01s

### 8. Relevant Regression

NOT_RUN / NOT_APPLICABLE — no prior application implementation existed

### 9. Card Evaluation

PASS — applicable C01 validation set passed

### 10. Commercial / Data Invariants

NOT_RUN / NOT_APPLICABLE_YET

### 11. AI / Provider Validation

NOT_RUN / NOT_APPLICABLE_YET

### 12. Security Validation

PASS — secret files/patterns not tracked; environment files remain protected

### 13. Failures / Blockers

NONE RECORDED FOR IMPLEMENTATION

### 14. Exit Gate Evidence

PASS — package imports successfully; pytest executes successfully; configuration loads successfully; Core source contains no AWS/provider dependency; repository/package structure and secret-safe baseline checks passed.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — evidence and learning records updated with actual implementation decisions and validation results; completion delivery and reconciliation are recorded.

### 16. Git Evidence

Branch: card/v1-c01-repository-baseline (delivered)
Start Commit: af47e98d6170551a5446b45c4dadf7f17f9e0ad1
Delivery Commit: 93d6bdbdc074687f366658c4ebddc43912b7571e — feat: establish V1 C01 repository baseline
Remote/Upstream: origin / origin/card/v1-c01-repository-baseline
Commit: COMPLETED — human-approved
Push: COMPLETED — human-approved to origin/card/v1-c01-repository-baseline
Working Tree at delivery: CLEAN; final main tree CLEAN
GIT_DELIVERY_APPROVAL: GRANTED / CONSUMED — PR #1 merged
PR: MERGED — #1
Merge: COMPLETED — 693e17be652cdd4f82cdfe6da2bef89f6529103c
Final Reconciliation Commit for C01 completion event: 0af07c84c1d64b83afa57a516699a90110b5ec4c

### 17. Known Limitations

The validated Card is COMPLETE. The approved normal delivery chain completed through PR #1 and merge. CI, Docker, domain logic, and future-Card dependencies remain intentionally absent.

### 18. What We Learned

Recorded in CARD_LEARNING_AND_DECISION_LOG.md → V1-C01.

### 19. Completion Evidence

Exit Gate is proven. The Card is COMPLETE after valid GIT_DELIVERY_APPROVAL, PR #1, merge, and final reconciliation.
FINAL_CARD_STATE_CONSISTENCY_GATE: PASS — current-state representations and Git state agree.
Validator result: PASS; table, Exit Gate, and active-Card negative fixtures returned non-zero with STATE_RECONCILIATION_REQUIRED.
Governance hardening delivery: PR #2 merged into main at 6ed41e3be169390a98f30114973595d91250d982.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C01
Learning Documentation Status:
CURRENT

## V1-C02 — Domain Models

### 1. Card

V1-C02 — Domain Models

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

PROJECT_CONTROL.md, pyproject.toml, src/ai_quotation_intelligence/domain/__init__.py, src/ai_quotation_intelligence/domain/models.py, tests/test_domain_models.py, scripts/test_governance_harness.sh, scripts/reconcile_governance_views.py, scripts/final_card_state_consistency.sh, QUOTATION_ENGINEERING_HARNESS.md, AGENTS.md, .agents/skills/quotation-card-execution/SKILL.md, CARD_LEARNING_AND_DECISION_LOG.md, GOVERNANCE_HARNESS_PROOF_CASES.md

### 6. Commands Run

bash scripts/quotation_session_bootstrap.sh; .venv/bin/pip install -e '.[dev]'; .venv/bin/pytest -q; bash scripts/test_governance_harness.sh; bash -n scripts/quotation_session_bootstrap.sh; bash -n scripts/final_card_state_consistency.sh; bash -n scripts/test_governance_harness.sh; .venv/bin/python scripts/reconcile_governance_views.py --write; .venv/bin/python scripts/reconcile_governance_views.py --check; git diff --check

### 7. Focused Tests

PASS — .venv/bin/pytest -q: 14 passed in 0.06s

### 8. Relevant Regression

PASS — bash scripts/test_governance_harness.sh: PASS=39, FAIL=0 (23 prior governance cases, GV-01 through GV-08 generated-view cases, and HF-01 through HF-08 fixture-independence cases)

### 9. Card Evaluation

PASS — focused construction, invalid-input, nested-model, enum, boundary, serialization, nested approval-boundary, and provenance-consistency checks are covered by tests/test_domain_models.py

### 10. Commercial / Data Invariants

PASS / NOT_APPLICABLE — explicit currency, hours, non-negative numeric, estimated/actual, null/zero distinction, and provider-neutral boundaries inspected; calculation semantics remain out of scope

### 11. AI / Provider Validation

PASS / NOT_APPLICABLE — no provider implementation or SDK dependency added; Core models contain no AWS/provider types

### 12. Security Validation

PASS — secret-safe diff and provider-neutrality inspection; no secret files or credentials introduced

### 13. Failures / Blockers

Observed failures and fixes:
- Initial C02 test fixture used lowercase currency while the explicit contract requires uppercase three-letter currency codes; corrected the fixture and reran pytest.
- Governance regression fixtures initially copied mutable live C02 state, causing five expected-baseline cases to fail; changed the fixture source to committed HEAD and reran the suite.
- Pre-delivery audit found that a DraftQuote accepted an approved nested Quote, that HistoricalQuote accepted contradictory nested/top-level provenance, and that PROJECT_CONTROL contained conflicting C02 lifecycle labels. Added model-level invariants, regression tests, and reconciled the live state.

### 14. Exit Gate Evidence

Typed domain contracts validate the C02 boundaries, including nested approval and cross-boundary provenance consistency, and are ready for C03 without owning calculations, provider payloads, retrieval, risk analysis, AI, persistence, or future capabilities. Post-repair `bash scripts/final_card_state_consistency.sh V1-C02 READY_FOR_DELIVERY` passed. Generated governance views were reconciled from PROJECT_CONTROL.md and exact Card evidence sections; the reconciliation check passed and the write operation was idempotent.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS

### 16. Git Evidence

Delivered through approved Git delivery: commit `0dfd38a5b3d201052b4dea930becc96c6927225e`, pushed branch `card/v1-c02-domain-models`, PR #4, merged to `main` as `164ae7c3982009025ec16de72cd0d4ad1efc646d`.

### 17. Known Limitations

No unresolved implementation limitation. Calculations, datasets, retrieval, risk analysis, AI, persistence, API, and infrastructure remain intentionally absent.

### 18. What We Learned

Recorded below from actual C02 implementation and validation.

### 19. Completion Evidence

COMPLETE — implementation, validation, approved delivery, PR #4 merge, and final reconciliation completed.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C02
Learning Documentation Status:
COMPLETE

## V1-C03 — Synthetic Historical Data

### 1. Card

V1-C03 — Synthetic Historical Data

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

- `src/ai_quotation_intelligence/data/__init__.py`
- `src/ai_quotation_intelligence/data/synthetic_history.py`
- `tests/test_synthetic_history.py`
- `PROJECT_CONTROL.md`

### 6. Commands Run

- `.venv/bin/pytest -q tests/test_synthetic_history.py tests/test_domain_models.py tests/test_baseline.py`
- direct deterministic dataset and provenance probes
- `.venv/bin/pytest -q` → 18 passed
- `.venv/bin/pytest -q tests/test_synthetic_history.py` after pattern repair → 5 passed
- `bash scripts/test_governance_harness.sh` → 60 passed, 0 failed
- `.venv/bin/python scripts/reconcile_governance_views.py --check` → PASS
- `bash scripts/final_card_state_consistency.sh V1-C03 READY_FOR_DELIVERY` → PASS
- `gh pr view 7` → PR #7 MERGED; merge commit `9fd7673bbb31167857f8d8f5f468d5631cde302d`
- `bash scripts/quotation_session_bootstrap.sh` → WARN (127 PASS, 1 WARN, 0 FAIL; dirty-tree warning only)

### 7. Focused Tests

PASS — 5 C03 tests passed; dataset contains 40 unique valid records, is reproducible, preserves synthetic provenance, and numerically satisfies the controlled patterns.

### 8. Relevant Regression

PASS — `bash scripts/test_governance_harness.sh` completed with 60 passed and 0 failed.

### 9. Card Evaluation

PASS — schema, provenance, record-count, reproducibility, numeric pattern, and no-provider-boundary checks executed; 5 focused C03 tests pass and the prior 18-test project suite remains covered by the full rerun.

### 10. Commercial / Data Invariants

PASS — explicit SEK currency, non-negative Hours/Money, estimated item hours distinct from observed outcome hours, and synthetic provenance validated. No calculation engine added.

### 11. AI / Provider Validation

PASS / NOT_APPLICABLE — C03 contains no AI, AWS, or provider implementation.

### 12. Security Validation

PASS — records are fictional and synthetic; no credentials or customer data added.

### 13. Failures / Blockers

Pre-delivery audit found that initial `under_estimate` values were numerically reversed and the initial pattern test checked labels without checking numeric relationships. The deterministic fixture values and tests were corrected; the repaired focused suite passed 5/5.

### 14. Exit Gate Evidence

The generator produces 40 deterministic, multi-item `HistoricalQuote` records through the C02 contracts, with synthetic provenance and numerically coherent under/near/over-estimate, testing, integration, and scope-change patterns. No analytics behavior is included.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — implementation rationale, focused tests, full regression, scope, provenance, security, and provider-boundary evidence recorded. Delivery remains pending.

### 16. Git Evidence

Delivered through approved Git delivery: commit `204147915fcab7e2e161e083230b0b56cb2f97e0`, pushed branch `card/v1-c03-synthetic-historical-data`, PR #7, merged to `main` as `9fd7673bbb31167857f8d8f5f468d5631cde302d`.

### 17. Known Limitations

The dataset is an in-memory deterministic generator; persistence, calculation, comparison, retrieval, and risk analysis remain later-Card responsibilities.

### 18. What We Learned

C03 data quality is stronger when controlled patterns are explicit in the source templates while values remain ordinary C02 contracts. Keeping actual outcomes on `ProjectOutcome` avoids confusing supplied observations with C04 calculations.

### 19. Completion Evidence

COMPLETE — implementation, validation, approved delivery, PR #7 merge, and outcome-only reconciliation completed.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C03
Learning Documentation Status:
CURRENT
Learning Documentation Status:
NOT_STARTED

## V1-C04 — Quote Calculation Engine

### 1. Card

V1-C04 — Quote Calculation Engine

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

`src/ai_quotation_intelligence/calculation.py`, `tests/test_calculation.py`, and the C04 sections of PROJECT_CONTROL.md, QUOTATION_CARD_EVIDENCE_MAP.md, and CARD_LEARNING_AND_DECISION_LOG.md.

### 6. Commands Run

Focused C04 pytest, full pytest, reconciliation check, governance regression, bootstrap, C04 COMPLETE consistency validation, shell syntax checks, Python compilation, and `git diff --check` were executed after implementation and delivery.

### 7. Focused Tests

PASS — 11 passed (`.venv/bin/pytest -q tests/test_calculation.py`)

### 8. Relevant Regression

Governance regression: 60 passed, 0 failed.

### 9. Card Evaluation

PASS — item hours × rate, multi-item totals, Decimal precision, zero values, negative-input rejection, missing-input rejection, non-finite-input rejection, mixed-currency rejection, empty-quote rejection, supplied-total reconciliation, deterministic repeatability, and input non-mutation were observed in focused tests.

### 10. Commercial / Data Invariants

PASS — deterministic estimated item cost and total arithmetic; explicit currency and hours units remain owned by C02 models; no rounding rule was invented because the contract does not define one.

### 11. AI / Provider Validation

PASS / NOT_APPLICABLE — implementation is standard-library Decimal arithmetic over C02 models and has no AI, network, AWS, or provider dependency.

### 12. Security Validation

PASS — no secrets, customer data, provider SDKs, or network behavior introduced.

### 13. Failures / Blockers

No implementation failures observed. Delivery and outcome-only reconciliation completed through PR #9.

### 14. Exit Gate Evidence

Deterministic arithmetic and reconciliation tests passed; focused and full application validation passed; C01–C03 complete-state protection and C05 unstarted-state protection were preserved.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS

### 16. Git Evidence

Implementation Evidence: PRESENT — calculation implementation and validation are recorded in this C04 section.
Git Delivery Evidence: PRESENT — delivery commit `266884504a40584d9d7497a648beb1268c8f827f`, PR #9 merged, merge commit `3ed46f0ce81ccf502e5d2833ce2e7e9a33c1801b`.

### 17. Known Limitations

Only estimated item-cost and estimated-total arithmetic is owned by C04. Actual-cost variance, historical comparison, retrieval, risk, AI, approval workflow, export, and infrastructure remain later-Card responsibilities. Currency conversion and rounding are not implemented because they are not defined by this contract.

### 18. What We Learned

Authoritative totals must be derived from item-level Decimal results, while supplied totals can be used only as reconciliation assertions. Boundary tests should prove both arithmetic and domain validation behavior.

### 19. Completion Evidence

C04 implementation, validation, Git delivery, and outcome-only reconciliation are COMPLETE. The audit-reported missing-input and non-finite-input coverage was added and passed.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C04
Learning Documentation Status:
CURRENT

## V1-C05 — Historical Comparison Engine

### 1. Card

V1-C05 — Historical Comparison Engine

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

`src/ai_quotation_intelligence/comparison.py`, `tests/test_comparison.py`, and C05 governance evidence/state updates.

### 6. Commands Run

Focused C05 pytest, full pytest, reconciliation, governance regression, bootstrap, C05 READY_FOR_DELIVERY consistency validation, C05 COMPLETE consistency validation, and `git diff --check` were executed after implementation and delivery.

### 7. Focused Tests

PASS — 10 passed (`.venv/bin/pytest -q tests/test_comparison.py`)

### 8. Relevant Regression

Governance regression: 60 passed, 0 failed.

### 9. Card Evaluation

PASS — hour and cost variance, percentage semantics, zero denominator, missing outcomes, Decimal determinism, C03 integration, scope-change preservation, source immutability, currency validation, even-count hour median, and average/median cost variance were observed; full suite: 40 passed.

### 10. Commercial / Data Invariants

PASS — variance uses actual minus estimate; missing actual outcomes remain absent; cost variance is not inferred without validated actual cost.

### 11. AI / Provider Validation

PASS / NOT_APPLICABLE — deterministic Python implementation with no AI, network, AWS, or provider dependency.

### 12. Security Validation

PASS — no secrets, customer data, provider SDKs, or network behavior introduced.

### 13. Failures / Blockers

No implementation or delivery failures observed. C05 delivery and outcome-only reconciliation completed through PR #10.

### 14. Exit Gate Evidence

Deterministic historical estimate-versus-outcome comparison, applicable aggregates, missing-outcome handling, and C03 integration passed focused and full validation.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS

### 16. Git Evidence

Implementation Evidence: PRESENT — comparison implementation and validation are recorded in this C05 section.
Git Delivery Evidence: PRESENT — PR #10 merged; delivery commit `8389bb6deb8a8ab2bb997014d547468ba9f7dfaa`; merge commit `573b5e5632dd7d5e5380cdf7678889c53b99ac62`.

### 17. Known Limitations

C05 intentionally does not implement similarity retrieval, risk scoring, AI/provider behavior, or infrastructure. Cost variance remains unavailable when validated actual cost is absent; no actual cost is inferred from hours.

### 18. What We Learned

Comparison evidence is derived from validated C02/C03 records, and estimated totals are obtained through the C04 calculation engine rather than reimplemented.

### 19. Completion Evidence

C05 COMPLETE — implementation, validation, Git delivery, and post-merge outcome reconciliation are complete. Delivery commit `8389bb6deb8a8ab2bb997014d547468ba9f7dfaa`, PR #10, and merge commit `573b5e5632dd7d5e5380cdf7678889c53b99ac62` are recorded in PROJECT_CONTROL.md.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C05
Learning Documentation Status:
COMPLETE

## V1-C06 — Similar Quote Retrieval

### 1. Card

V1-C06 — Similar Quote Retrieval

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

`src/ai_quotation_intelligence/retrieval.py`, `tests/test_retrieval.py`, and C06 governance evidence/state updates.

### 6. Commands Run

Focused C06 pytest, full pytest, reconciliation, governance regression, bootstrap, C06 READY_FOR_DELIVERY consistency validation, and `git diff --check` were executed after implementation.

### 7. Focused Tests

PASS — 8 passed (`.venv/bin/pytest -q tests/test_retrieval.py`)

### 8. Relevant Regression

Governance regression: 60 passed, 0 failed.

### 9. Card Evaluation

PASS — bounded Decimal feature-overlap retrieval, explainable matching features, stable identity/provenance, deterministic ranking and ties, result limits, empty/insufficient history, currency compatibility, source immutability, and no commercial-value copying were observed; full suite: 48 passed.

### 10. Commercial / Data Invariants

PASS — retrieval returns contextual references only; it does not create rates, prices, final effort, or risk decisions. Currency compatibility is enforced without conversion.

### 11. AI / Provider Validation

PASS / NOT_APPLICABLE — deterministic provider-neutral Python implementation with no AI, network, AWS, or provider dependency.

### 12. Security Validation

PASS — no secrets, customer data, provider SDKs, or network behavior introduced.

### 13. Failures / Blockers

No implementation or delivery failures observed. C06 delivery and outcome-only reconciliation completed through PR #12.

### 14. Exit Gate Evidence

Bounded, explainable, deterministic comparable-quotation retrieval with stable identity/provenance and explicit empty/insufficient-result behavior passed focused and full validation.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS

### 16. Git Evidence

Implementation Evidence: PRESENT — retrieval implementation and validation are recorded in this C06 section.
Git Delivery Evidence: PRESENT — PR #12 merged; delivery commit `2946e2a2c98735155ef71d9a5358e9a2b4bb6016`; merge commit `0c03ce555dd13da5c0062c28be53f50168f768a9`.

### 17. Known Limitations

C06 uses simple explainable structured token overlap and item-count matching; it does not use embeddings, vector search, RAG, or semantic model inference. Similarity remains contextual and never supplies commercial truth.

### 18. What We Learned

Stable feature explanations and deterministic tie ordering are required for retrieval evidence to remain inspectable and reproducible.

### 19. Completion Evidence

COMPLETE — implementation, validation, Git delivery, and post-merge outcome reconciliation completed. Delivery commit `2946e2a2c98735155ef71d9a5358e9a2b4bb6016`, PR #12, and merge commit `0c03ce555dd13da5c0062c28be53f50168f768a9` are recorded in PROJECT_CONTROL.md.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C06
Learning Documentation Status:
COMPLETE

## V1-C07 — Risk Evidence Engine

### 1. Card

V1-C07 — Risk Evidence Engine

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

src/ai_quotation_intelligence/risk_evidence.py
tests/test_risk_evidence.py

### 6. Commands Run

.venv/bin/pytest tests/test_risk_evidence.py -q
.venv/bin/pytest tests/test_synthetic_history.py tests/test_calculation.py tests/test_comparison.py tests/test_retrieval.py tests/test_risk_evidence.py -q
.venv/bin/pytest -q
.venv/bin/python scripts/reconcile_governance_views.py --check
bash scripts/test_governance_harness.sh
bash scripts/quotation_session_bootstrap.sh
git diff --check

### 7. Focused Tests

PASS — 11 passed (`.venv/bin/pytest tests/test_risk_evidence.py -q`)

### 8. Relevant Regression

PASS — C03–C07 related tests: 47 passed; full suite: 61 passed.

### 9. Card Evaluation

PASS — count/rate/statistic reconciliation, exact even-count median assertion, missing-outcome exclusion, empty history, provenance, immutability, deterministic repeatability, and mixed-origin rejection were observed.

### 10. Commercial / Data Invariants

PASS — C05 comparison and aggregate arithmetic remain authoritative; metric/unit identity, synthetic provenance, missing-value semantics, and no-price-copy boundaries are preserved.

### 11. AI / Provider Validation

PASS / NOT_APPLICABLE — deterministic local Python implementation with no AI, network, AWS, or provider dependency.

### 12. Security Validation

PASS — repository security/provider boundary inspected; no secrets or provider coupling introduced.

### 13. Failures / Blockers

Initial focused validation exposed a local denominator-field error and an incorrect cost-test assumption about C03 actual-cost availability. Both were corrected; an independent audit also identified missing explicit numeric median coverage, which was repaired with an even-count Decimal regression test. No C02–C06 defect or blocker remains.

### 14. Exit Gate Evidence

The engine emits typed, traceable RiskEvidence with reconciled comparable and overrun counts, deterministic rate and variance statistics, source/work-item/scope context, and explicit insufficient-evidence results for empty or unavailable metric inputs.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — implementation, focused tests, upstream regressions, full suite, deterministic behavior, provenance, immutability, boundaries, and evidence/learning records are current.

### 16. Git Evidence

Implementation Evidence: PRESENT — deterministic risk-evidence implementation and validation are recorded in this C07 section.
Git Delivery Evidence: PRESENT — PR #16 merged; delivery commit `e3d6825628634866c89f5e6d772cc98376c6e736`; merge commit `e5b87edac75a20f1784c53a09acb22414dcf3ece`.

### 17. Known Limitations

No arbitrary minimum sample threshold is invented; `INSUFFICIENT_EVIDENCE` is returned when the selected metric has no usable validated observations. C06 retrieval is not required as an input by the current C07 contract.

### 18. What We Learned

C07 must keep deterministic evidence aggregation separate from later AI risk interpretation. Missing outcomes and missing actual costs remain visible as insufficient evidence, and C05 remains the owner of comparison arithmetic.

### 19. Completion Evidence

COMPLETE — implementation, validation, evidence, learning, Git delivery, and post-merge outcome reconciliation are complete. Delivery commit `e3d6825628634866c89f5e6d772cc98376c6e736`, PR #16, and merge commit `e5b87edac75a20f1784c53a09acb22414dcf3ece` were verified from Git/GitHub output.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C07
Learning Documentation Status:
CURRENT

## V1-C08 — Amazon Bedrock Integration

### 1. Card

V1-C08 — Amazon Bedrock Integration

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

`pyproject.toml`, `.env.example`, `src/ai_quotation_intelligence/config.py`,
`src/ai_quotation_intelligence/bedrock.py`, `tests/test_bedrock.py`, `README.md`,
and the C08 sections of `PROJECT_CONTROL.md`, this Evidence Map, and the Learning Log.

### 6. Commands Run

`.venv/bin/pip install -e '.[dev]'`; `.venv/bin/python` import/version check;
focused, related, and full pytest; `py_compile`; Python Bedrock smoke test;
reconciliation write/check; governance harness; bootstrap; `git diff --check`.

### 7. Focused Tests

PASS — 9 tests passed: deterministic request construction, response extraction/validation,
provider failure, invalid prompt, credential boundary, configuration loading,
and bounded timeout/retry configuration.

### 8. Relevant Regression

PASS — 51 tests passed in the C04–C08 related regression suite.

### 9. Card Evaluation

PASS — typed provider-isolated adapter, deterministic requests, response validation,
and controlled SUCCESS / INVALID / UNAVAILABLE outcomes.

### 10. Commercial / Data Invariants

PASS — deterministic Core and C04–C07 authorities remain unchanged; no provider
payloads or credentials enter domain logic.

### 11. AI / Provider Validation

PASS — boto3 Converse adapter invoked successfully with configured Nova Micro;
mocked tests distinguish provider responses from live evidence; no C09/C10 behavior.

### 12. Security Validation

PASS — no credentials in repository or explicit credential arguments; standard SDK
credential resolution is used.

### 13. Failures / Blockers

Initial environment lacked boto3 because C08 had not previously introduced it; the
dependency was declared and installed. No blocking implementation failure remained.

### 14. Exit Gate Evidence

PROVEN — C08 contract, provider boundary, response validation, bounded provider
failure handling, configuration, security, tests, and live Python smoke evidence passed.
Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — focused, related, full, governance, and scope validation passed; Learning Log current.

### 16. Git Evidence

PRESENT — delivery commit `a29189d7d62145936aaa4f024ce8076a4bef30b7`, PR #18 merged, merge commit `def3367540ac17bfb9ab1f3acfb97fe6302bc656`.

### 17. Known Limitations

C08 does not implement agent tools, quotation-agent orchestration, human review,
Excel, API, S3, deployment, or advanced resilience. Model output remains bounded
text and is not authoritative for arithmetic, evidence, or decisions.

### 18. What We Learned

Implemented a small injectable Converse adapter rather than leaking boto3 objects
into Core. The live smoke test used `amazon.nova-micro-v1:0` in `us-east-1` and
returned `BEDROCK_C08_OK` with usage 17 input / 9 output / 26 total tokens and
observed latency 781.78 ms.

### 19. Completion Evidence

COMPLETE — implementation, validation, approved delivery, merge, and outcome reconciliation are complete.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C08
Learning Documentation Status:
CURRENT

## V1-C09 — Agent Tools

### 1. Card

V1-C09 — Agent Tools

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

Approved C09 delivery completed through PR #25; C10 remains unauthorized.

### 4. Human Start Approval

YES

Explicit human authorization for V1-C09 implementation only.

### 5. Files Changed

`src/ai_quotation_intelligence/agent_tools.py` (new), `tests/test_agent_tools.py` (new),
`tests/test_architecture.py`, `PROJECT_CONTROL.md`, this C09 Evidence Map section,
and the C09 Learning Log section. No C01–C08 implementation or future-Card module changed.

### 6. Commands Run

`.venv/bin/pytest -q tests/test_agent_tools.py`; `.venv/bin/pytest -q
tests/test_architecture.py`; `.venv/bin/pytest -q`; `bash
scripts/test_governance_harness.sh`; `bash scripts/quotation_session_bootstrap.sh`;
`python3 scripts/reconcile_governance_views.py --write` and `--check`;
Python compilation/import smoke; shell syntax; `git diff --check`.
`bash scripts/final_card_state_consistency.sh V1-C09 ACTIVE` and a
changed-file secret-pattern/whitespace scan were also run.

### 7. Focused Tests

PASS — 24 C09 tool tests. Valid contracts, all five completed-tool delegations,
typed outputs, deterministic repeatability, missing evidence, unavailable and
unsupported operations, malformed delegated output, provenance, numeric
tampering, rejection of caller-supplied historical records, no approval/Excel
capability, and sanitized service failures passed.

### 8. Relevant Regression

Historical pre-audit validation: 23 architecture tests passed; complete module
registration and import-policy checks permitted Agent Tool → Core/Support,
prohibited Core → Agent Tool and Agent Tool → Provider/SDK, and preserved the
Support anti-laundering boundary. Full pytest: 138 passed after historical-input
boundary correction. The later independent audit found that the Support
allowance was unused; current policy permits Agent Tool → Core only, with a
focused rejection fixture for Agent Tool → Support.
Post-remediation rerun: C09 tools 24 passed, architecture 24 passed, combined
48 passed, and full pytest 139 passed. Governance Harness PASS=61 / FAIL=0;
reconciliation, ACTIVE-state consistency, compilation/import, shell syntax,
secret-pattern scan, and `git diff --check` passed. Bootstrap reported
PASS=127 / WARN=1 / FAIL=0; the warning is the expected undelivered dirty tree.
Post-merge on clean main: C09 24 passed, architecture 24 passed, full pytest
139 passed, Governance Harness PASS=61 / FAIL=0, reconciliation PASS,
ACTIVE-state consistency PASS before outcome reconciliation, and bootstrap
PASS=128 / WARN=0 / FAIL=0.

### 9. Card Evaluation

PASS — existing C03–C07 owners are invoked and their exact results preserved.
Every tool loads and validates the full C03 synthetic corpus internally;
untrusted callers cannot supply or cherry-pick historical records. The C05 and C07
insufficient-evidence semantics remain visible. C08 is not invoked.
Risk classification: ELEVATED tool-execution boundary. Contract invariants,
adversarial malformed-result/tampering cases, and failure injection were
required and executed; no live Bedrock, property/fuzz/concurrency framework,
or external-effect rollback was applicable to this pure local tool layer.
Source adaptation: NOT_APPLICABLE — only existing in-repository capabilities
and ordinary language/library constructs were used.

### 10. Commercial / Data Invariants

PASS — no tool-owned arithmetic, invented rates/totals, missing-value
substitution, fabricated risk evidence, approval, or finalization. Source IDs,
quote IDs, data origin, full C03 corpus identity, and deterministic Core values are checked at output
boundaries. Cost statistics with no actual costs fail as insufficient evidence.

### 11. AI / Provider Validation

PASS / LIVE BEDROCK NOT_APPLICABLE — C09 imports no Bedrock/provider SDK and
does not issue model-driven tool calls; C08's bounded text result is not a
structured tool-call contract.

### 12. Security Validation

PASS — fixed available-tool resolver rejects deferred and arbitrary methods;
service errors expose only a failure code and tool/request identity, not
exception text; no secrets, external writes, or provider payloads were added.

### 13. Failures / Blockers

An adversarial probe initially failed: a structurally valid comparison with
the correct source ID but a forged numeric variance was accepted by the tool
boundary (`.venv/bin/pytest -q
tests/test_agent_tools.py::test_plausible_numeric_overrides_from_delegates_are_not_authoritative`,
1 failed). Root cause: shape/provenance checks alone did not bind numeric
results to the deterministic owner. C09 now compares delegated results with
the existing Core owner's deterministic output; focused rerun passed (46
combined C09/architecture tests). The full suite passed (137) after the
additional whitespace-ID rejection case.

A second adversarial probe initially failed: a caller-supplied historical
record with an altered actual-hours value and unchanged source identity was
accepted by `get_risk_evidence` (`.venv/bin/pytest -q
tests/test_agent_tools.py::test_caller_cannot_supply_altered_historical_outcomes`,
1 failed). Root cause: caller-controlled history was passed to Core and then
used as the reference for exact output comparison. C09 removed history fields
from all tool inputs; each tool now obtains and verifies the complete C03
corpus internally. Focused C09 rerun passed (24 tests); combined C09/architecture
rerun passed (47), and full pytest passed (138). This was a C09 trust-boundary
defect, not a C03–C07 service defect.

The first `bash scripts/final_card_state_consistency.sh V1-C09 ACTIVE` run
failed three exact-state assertions because the active-Card, evidence-state,
and approval lines included explanatory suffixes. The canonical parser expects
bare `V1-C09`, `ACTIVE`, and `YES` values. The C09 state records were formatted
accordingly; the rerun passed all seven ACTIVE-state assertions.

Independent C09 audit reported PASS with one actionable LOW finding: the
architecture policy allowed `AGENT_TOOL → SUPPORT` although the C09 module
imports only Core. The bounded remediation removed only that unused policy
edge and added a focused Support-import rejection fixture. The original audit
PASS remains historical; this changed candidate requires independent re-audit
before any delivery approval.
The human delivery approval subsequently identified the remediated candidate
`719f63e6559af7f269af7b3b51863fc78d7e5c346e70f03bb33d0e44f3ef7679`
as independently audited. Worktree, staged index, and committed tree were
mechanically verified against that exact identity before push.

### 14. Exit Gate Evidence

Typed request/output models and five independently tested tool methods are
implemented. Each returns traceable, validated Core data or raises a typed
`ToolFailure`; no success is fabricated. Delegation is to C03 synthetic history,
C05 comparison/statistics, C06 similarity, and C07 risk evidence. Core-owned
calculation remains in C04/C05; no C09 total, invented evidence, approval,
finalization, model tool-call loop, or Excel implementation exists.
Tool inputs contain query parameters only, not historical evidence records.

Exit Gate Status: PROVEN by implementation validation and independently audited delivery

### 15. CARD_QUALITY_GATE

PASS — bounded C09 implementation, focused/full/architecture/governance
validation, failure-path and adversarial probes, Evidence Map, and Learning Log
are current. Exact audited candidate was delivered under human approval.

### 16. Git Evidence

Branch: card/v1-c09-agent-tools; start commit:
`5625eff2e6edc4cf8c498cf7d4569be84186bc96`; audited candidate identity:
`719f63e6559af7f269af7b3b51863fc78d7e5c346e70f03bb33d0e44f3ef7679`.
Delivery commit `3dee2d0345e783ad491e8683204a071ad010b8c4` was pushed;
PR: MERGED — #25; merge commit `d0f0f70f385c2e876512ce9706d5ffd33ef3664a`.
Exact staged/index and committed-tree identity checks passed before push;
post-merge local main and origin/main matched with 0/0 divergence and clean tree.

### 17. Known Limitations

All C09 tools currently use only C03's deterministic synthetic dataset; no
caller-provided subset or general storage source is accepted. Draft
creation/validation and Excel generation are deliberately
deferred and rejected as unsupported. Exact Core re-execution at output
boundaries favors trustworthiness over compute efficiency; revisit only with
an authorized owner/contract change.

### 18. What We Learned

C09 tool boundaries need both provenance checks and exact comparison to
deterministic owners; type/shape validation alone cannot catch plausible
numeric tampering. Source identity on a caller-controlled historical record
does not make that record trusted. An explicit deferred-tool set is safer than placeholders
that return apparent success for later-Card capabilities.

### 19. Completion Evidence

COMPLETE — implementation, validation, independently audited candidate,
human-approved exact Git delivery, PR #25 merge, and outcome reconciliation.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C09
Learning Documentation Status:
CURRENT

## V1-C10 — Quotation Agent

Pre-C10 canonical maintenance (not C10 implementation): inspection found that
the Roadmap omitted an explicit C10 Exit Gate even though the Card
Specification makes that gate authoritative, and that C10 lacked the compact
pre-implementation verification block required for C09 and later. That
maintenance candidate added the gate and derived verification block without
authorizing or starting C10; it was subsequently delivered through PR #27.
C10 implementation tests and Exit Gate proof were NOT_RUN / NOT_PROVEN at
that maintenance checkpoint. Separate explicit C10 start approval followed.

### 1. Card

V1-C10 — Quotation Agent

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

The exact remediated C10 candidate was independently audited, human-approved,
and delivered through PR #28. The accepted LOW token-limit sizing note remains
non-blocking; no post-audit candidate content was changed.

### 4. Human Start Approval

YES

Explicit human authorization covered V1-C10 implementation and exact audited
Git delivery only; V1-C11 and later remain unauthorized.

### 5. Files Changed

PROJECT_CONTROL.md; QUOTATION_CARD_EVIDENCE_MAP.md; CARD_LEARNING_AND_DECISION_LOG.md; src/ai_quotation_intelligence/quotation_agent.py (created); tests/test_quotation_agent.py (created); tests/test_architecture.py (updated); src/ai_quotation_intelligence/config.py and .env.example (bounded Bedrock output-token default correction). No C08/C09 provider/tool module, dependency, or C11+ implementation changed.

### 6. Commands Run

Original implementation validation: 45 C10 focused, 24 C09, 32 architecture, and 192 full pytest passed. After bounded independent-audit remediation: `.venv/bin/pytest -q tests/test_quotation_agent.py` (57 passed); `.venv/bin/pytest -q tests/test_agent_tools.py` (24 passed); `.venv/bin/pytest -q tests/test_architecture.py` (32 passed); `.venv/bin/pytest -q` (204 passed); `python3 scripts/reconcile_governance_views.py --write` and `--check` (PASS); `bash scripts/test_governance_harness.sh` (61 PASS / 0 FAIL); `bash scripts/quotation_session_bootstrap.sh` (127 PASS / 1 expected dirty-worktree WARN / 0 FAIL); Python compilation/import, shell syntax, changed-file secret-pattern scan, and `git diff --check` (PASS). Candidate identity is recomputed only after final validation/documentation.

Post-merge on clean `main`: C10 focused 57 passed; C09 regression 24 passed;
architecture 32 passed; full pytest 204 passed; Governance Harness 61/0;
reconciliation check PASS; bootstrap 128 PASS / 0 WARN / 0 FAIL; Python
compilation/import, shell syntax, and diff check PASS. GitHub reported no PR
checks; no required branch protection or ruleset was configured.

### 7. Focused Tests

PASS — 57 C10 tests: original coverage plus unexpected final-assembly exception containment, forbidden and safe missing-information prose, the seven-call derivation invariant, and effective bounded Bedrock output configuration for a grounded structured final response.

### 8. Relevant Regression

PASS — C09 focused regression 24 passed; architecture 32 passed; full pytest 204 passed. C08 provider and C09 tool implementation code remain unchanged.

### 9. Card Evaluation

PASS — scripted model actions drive genuine tool selection and multiple C09 calls; a mocked C08 Converse client proves the existing text adapter can supply the JSON protocol. No live Bedrock call was required or executed.

### 10. Commercial / Data Invariants

PASS (self-validation) — Core `calculate_quote` supplies the only authoritative estimated total; C09 owns historical, similarity, variance, statistics, and risk evidence. Model-proposed totals, invented evidence IDs, changed request arguments, approval/finalization, and unsupported risk text are rejected by tests. Missing evidence remains an explicit non-success status.

### 11. AI / Provider Validation

PASS (mocked) — C08 BedrockResult status/text/request identity are validated; C08's adapter implementation remains unchanged and provider SDK objects never enter Core or Agent. Only its existing output-token configuration default changed. Bedrock unavailable and provider exceptions return sanitized non-success. LIVE BEDROCK: NOT_RUN / NOT_REQUIRED for deterministic C10 validation.

### 12. Security Validation

PASS (self-validation) — allowlisted C09 tool dispatch; strict JSON with duplicate-key rejection; strict tool arguments; request data and IDs supplied by validated input, not by model; bounded seven-call loop with repeat rejection and derivation invariant; fixed safe success narratives and focused forbidden-prose tests; evidence-linked risk wording generated from C09 metrics; sanitized final-assembly/provider errors; no SDK import leakage. Static architecture tests verify forbidden directions. A default C08 Converse request now carries a bounded 1024 output-token budget, checked against a representative grounded final JSON without a live AWS call.

Proportional C10 threat review (ELEVATED): protected assets are validated quotation inputs, Core totals, C09 evidence provenance, and human approval authority. Trust boundaries are user text → model prompt, Bedrock text → action parser, action → C09 tools, and C09 result → AgentResult. Attacks/failures include prompt injection, unknown/deferred tool requests, forged arguments or evidence IDs, invalid provider/tool output, repeated actions, and exception-detail leakage. Controls are strict action schemas, fixed tool allowlist and input construction, output identity/provenance checks, bounded execution, constrained success wording, Core arithmetic delegation, and sanitized non-success results. `tests/test_quotation_agent.py` and `tests/test_architecture.py` exercise these controls. Residual: C08 live generation behavior and later human review are not proven by these deterministic tests; exact C10 content was independently audited before delivery.

### 13. Failures / Blockers

Three original validation failures were preserved and resolved. First, focused pytest collection failed because `request` is a reserved pytest fixture name; the C10 fixture was renamed `agent_request`, then focused tests collected and passed. Second, the loop-limit test expected INVALID but C09 correctly returned INSUFFICIENT_EVIDENCE for cost statistics in the synthetic corpus before the limit; the test fixture was changed to use distinct valid tool actions, and the bounded-loop case passed. Third, bootstrap returned PASS=126/WARN=1/FAIL=1 because the C10 state update replaced the long `Application Implementation: V1-C01 BASELINE IMPLEMENTED` prefix that its read-only sanity check requires. PROJECT_CONTROL kept the true C10 state while restoring that established prefix; the bootstrap rerun returned PASS=127/WARN=1/FAIL=0. None was hidden as a first-pass success.

The independent audit of the original C10 candidate reported PASS with actionable MEDIUM robustness/deployment-readiness findings and a LOW orchestration-limit documentation finding; that PASS is historical, not a certification of the changed candidate. Its observations were: `_final(...)` dispatch lacked uniform unexpected-exception containment; `_safe_prose` authority checks lacked focused tests; C08's 64-token default could truncate legitimate C10 final JSON; and seven-call rationale was not mechanically protected. Bounded remediation added an INVALID sanitized exception boundary, 7 forbidden and 2 safe prose cases, an explicit 3 + 2×2 limit explanation/invariant, and a 1024-token default in existing configuration and `.env.example`. The C08 adapter interface, C10 structured protocol, commercial authority, C09 provenance/tool allowlist, and C11+ boundaries were not changed. Focused, C09, architecture, and full pytest reruns passed at 57/24/32/204; reconciliation PASS, Governance Harness 61/0, bootstrap 127/1 expected WARN/0, compilation/import/shell syntax/security scan/diff PASS. The human delivery instruction subsequently identified exact remediated identity `80cf063ea390776f581b04744043d48fb15473194365ee527ed391dfe71f5893` as independently audited PASS and accepted the remaining LOW token-sizing note as non-blocking. No new content fix followed that audit.

### 14. Exit Gate Evidence

Self-validated against the six Roadmap clauses:

1. Model chooses only C09's five completed names; all five are exercised in `test_success_uses_all_available_c09_tools_and_preserves_core_commercial_truth`.
2. Strict action/argument parsing and C09 output type, tool identity, request ID, and risk provenance checks precede use; malformed, unknown, deferred, and forged cases fail.
3. Core calculates draft totals; C09 supplies historical outcomes and risk evidence; model numeric/commercial fields and unsupported factual risk wording cannot enter successful output.
4. C09 insufficient evidence, absent risk evidence, and model-declared gaps return explicit non-success statuses.
5. Success is rebuilt and validated as a typed `AgentResult` containing an unapproved `DraftQuote` and evidence-linked suggestions, never raw Bedrock text.
6. Only draft status is constructed; approval, finalization, Excel, and C11+ tool requests fail.

Exit Gate Status: PROVEN by implementation validation, exact-identity independent audit, and approved delivery. No approval/finalization capability was added.

### 15. CARD_QUALITY_GATE

PASS — implementation, evidence, learning, required validation, exact-identity independent audit, accepted LOW residual, and approved PR #28 delivery are complete.

### 16. Git Evidence

Branch: `card/v1-c10-quotation-agent`; start commit `41bbceaffdafc257df4222fad297fbbf0221cc20`; audited identity `80cf063ea390776f581b04744043d48fb15473194365ee527ed391dfe71f5893`. Worktree, staged/index, and committed-tree verification matched that identity. Delivery commit `68370daa4d9defcdb6cfd3455db1c26a9c4c3480` was pushed; PR: MERGED — #28; Merge: COMPLETED — `ecb73841eeb80a863d0f969c66105d9b02226caa`. Post-merge local main and origin/main matched with 0/0 divergence and a clean tree before this separate outcome-only reconciliation.

### 17. Known Limitations

The C09 corpus is synthetic and fixed; C10 does not generalize C09 to external historical stores. C08 exposes text, not native tool calls; C10 uses strict JSON over that text with no live Bedrock test. The 1024-token default is a bounded local baseline, not proof of live model behavior; explicit environment overrides can change it. Successful narrative wording is deliberately limited to three safe statements, a safety/expressiveness tradeoff to avoid unverifiable free-form factual claims. C11 review, C12 Excel, and C13+ remain outside C10.

### 18. What We Learned

The strict model action envelope can support genuine tool selection without granting model authority over arguments, commercial values, evidence, or finalization. A valid test action must reach its target boundary before it can prove a later loop condition; the cost-statistics fixture initially proved an earlier evidence failure instead.

### 19. Completion Evidence

COMPLETE — implementation, validation, exact independently audited candidate, human-approved PR #28 merge, and this separate outcome-only state reconciliation. Final consistency remains subject to post-reconciliation runtime verification on clean main.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C10
Learning Documentation Status:
CURRENT

## V1-C11 — Human Review Gate

Pre-C11 canonical maintenance (not C11 implementation): read-only preflight
on clean `main` at `ad7dc32e59512ce0c1ff7f2873c9307558472991`
reported BLOCKED because the Roadmap omitted the authoritative C11 Exit Gate
and this Card's specification omitted the required C09+ pre-implementation
verification block. This maintenance candidate adds only those derived
contract/verification records; C11 implementation, tests, and Exit Gate proof
remain NOT_RUN / NOT_PROVEN. PROJECT_CONTROL.md continues to own the live
NOT_AUTHORIZED / NOT_STARTED state. Observed maintenance validation:
`python scripts/reconcile_governance_views.py --write` and `--check` PASS;
Governance Harness PASS=61/FAIL=0; session bootstrap PASS=127/WARN=1/FAIL=0
(the WARN is the expected modified worktree); full pytest 204 passed;
architecture tests 32 passed; `git diff --check`, shell syntax, Python
compile/import, and changed-line secret-pattern checks passed. These are
maintenance validation results, not C11 implementation or Exit Gate proof.

### 1. Card

V1-C11 — Human Review Gate

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

Explicit human C11 start authorization and exact-candidate Git delivery approval
were granted; the latter was consumed by PR #31.

### 5. Files Changed

`src/ai_quotation_intelligence/human_review.py` (new),
`tests/test_human_review.py` (new), `tests/test_architecture.py`,
`PROJECT_CONTROL.md`, this Evidence Map, and
`CARD_LEARNING_AND_DECISION_LOG.md`. No C12+ application or dependency file.

### 6. Commands Run

`.venv/bin/pytest -q tests/test_human_review.py` (32 passed),
`tests/test_quotation_agent.py` (57 passed), `tests/test_agent_tools.py`
(24 passed), `tests/test_architecture.py` (42 passed), and full
`.venv/bin/pytest -q` (246 passed). Governance Harness 61 PASS / 0 FAIL;
reconciliation `--write` and `--check` PASS after the preserved first
failure; bootstrap 127 PASS / 1 expected dirty-tree WARN / 0 FAIL; shell
syntax, 31 Python compile/import checks, changed-file secret-pattern scan,
new-file whitespace scan, and `git diff --check` PASS.

Post-merge on clean `main` at `cc4ef118bb46488bb0cd1ac23ea15612b40be1e5`:
C11 focused 32 passed; C10 regression 57; C09 regression 24;
architecture 42; full pytest 246; Governance Harness 61 PASS / 0 FAIL;
reconciliation `--check` PASS; bootstrap 128 PASS / 0 WARN / 0 FAIL;
Python syntax/import (31 files), shell syntax, changed-file credential-pattern
scan, and Git diff checks PASS. GitHub reported no PR checks or configured
main branch protection/ruleset; none was bypassed.

### 7. Focused Tests

PASS — 32 C11 tests against a real C10 result backed by C09/Core and a
scripted model. Approval/rejection, malformed input, status, identity,
evidence, stale result, repeat decision, record tampering, failure
sanitization, and explicit reviewer action were exercised.

### 8. Relevant Regression

PASS — C10 focused 57; C09 focused 24; architecture 42 (including REVIEW
classification and forbidden import directions); full suite 246.

### 9. Card Evaluation

PASS — a successful C10 `AgentResult` can enter one review session;
only an explicit validated `ApprovalDecision` yields APPROVED or REJECTED;
`require_approved` rejects no decision, rejection, and changed current
results. The exact candidate received independent audit PASS before delivery.

### 10. Commercial / Data Invariants

PASS (self-validation) — Core `calculate_quote_total` reconciles the draft
before review; approval/rejection changes status only, not items, rates,
hours, total, origin, or evidence links. Changed inputs invalidate the old
session and need a newly revalidated draft.

### 11. AI / Provider Validation

PASS (self-validation) — C11 has no Bedrock/client import or invocation and
does not extract a human decision from C10 narrative/model text. C10 result
status and evidence are revalidated at the C11 boundary.

### 12. Security Validation

PASS (self-validation) — tests reject fabricated identity/evidence,
unsuccessful C10 outcomes, stale approvals, repeated/opposite decisions,
malformed human action, and record-copy authority tampering. Error codes
exclude internal exception text. Architecture tests keep Agent, Agent Tool,
Provider, Support, Core, and future Application modules from importing REVIEW.
Changed-file secret-pattern, syntax/import, and whitespace checks passed.

### 13. Failures / Blockers

First `reconcile_governance_views.py --write` and `--check` failed:
`Active Card has incompatible lifecycle state: V1-C11`. The Card-start
status table used `IN_PROGRESS`; the existing reconciliation contract
requires `ACTIVE`. Changing only the lifecycle vocabulary produced PASS on
both reruns. No application behavior was implicated.

Initial architecture self-validation was green with `human_review.py`
classified CORE, but source review found that existing AGENT → CORE would
permit future Agent imports of approval code. The module was moved to a
dedicated REVIEW category with REVIEW → CORE only; 42 architecture tests
then passed. An initial audit-copy eligibility property was also removed
because nested Quote values are mutable; the held session remains the sole
eligibility gate, tested against a tampered returned rejection record.

### 14. Exit Gate Evidence

SELF_VALIDATION: explicit human action and one validated approve/reject
transition (`test_explicit_human_approval_preserves_core_truth_and_provenance`,
`test_human_rejection_is_visible_and_not_eligible`); AI/model text cannot
impersonate an action (`test_invalid_action_and_model_text_cannot_impersonate_human`);
only a revalidated successful draft enters review (unsuccessful and malformed
result tests); Core arithmetic is unchanged (approval and changed-input
tests); exact C10 snapshot binds quote/request/evidence identity (mutation
and stale-decision tests); invalid transitions and copy-tampering fail;
no C12+ module/action was added. Independent audit PASS and approved exact
Git delivery are complete.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent audit, accepted non-blocking LOW and
documented V1 limits, approved PR #31 delivery, and post-merge validation.

### 16. Git Evidence

Start base `d09e57a0ed22819ae7b7e46a4e25433b74de33ec`; branch
`card/v1-c11-human-review-approval`; independently audited candidate identity
`602a6a6e892325c434bb521d59aec47a486fabe20a214dd96053165f08af8a03`.
Worktree, staged/index, and committed-tree identities matched exactly.
Delivery commit `b5a283fd4e4f6aa5cda3a51e2aea26bfce4dc83e` was pushed;
PR: MERGED — #31, https://github.com/jo-soroush/ai-quotation-intelligence/pull/31;
Merge: COMPLETED — `cc4ef118bb46488bb0cd1ac23ea15612b40be1e5`.
Post-merge local main and origin/main matched at that SHA with 0/0 divergence
and a clean tree before this separate outcome-only reconciliation.

### 17. Known Limitations

`reviewer_id` is caller-asserted, not authenticated; a trusted future caller
must obtain it from an actual human action. C11 cannot prove the caller
supplied genuine C10 output or independently reconstruct C09 source records.
It preserves and checks the received validated result/evidence links. Repeat
decisions are blocked within one in-memory session; durable cross-process
replay/concurrency policy requires a later authorized persistence boundary.
The returned `ReviewRecord` is an inspectable copy, not an authority token.
The independent audit's LOW note about the strict `AgentResult` exact-type
check lacking a dedicated necessity test, and these documented V1 limitations,
were explicitly accepted as non-blocking by the human delivery approver.

### 18. What We Learned

CURRENT — architecture authority separation, snapshot binding, lifecycle
vocabulary failure, and audit-copy mutability are explained in the C11
Learning and Decision Log.

### 19. Completion Evidence

COMPLETE — implementation, validation, independent audit PASS for the exact
candidate, human-approved PR #31 merge, and separate outcome-only C11 state
reconciliation. Final consistency remains subject to clean-main runtime proof.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C11
Learning Documentation Status:
CURRENT

## V1-C12 — Excel Generation

Pre-C12 canonical maintenance, not C12 implementation: the read-only C12
preflight was BLOCKED. The Roadmap lacked the authoritative C12 Exit Gate
referenced by the specification; the required C09+ pre-implementation
verification block was absent; the Roadmap listed a per-item role that no
`QuoteItem` provides; and it listed historical figures not bound into the
C11-approved `AgentResult`. This bounded maintenance adds the Roadmap gate
and derived verification block. It makes the three V1 sheets required, treats
role as unsupported/optional, and limits the Historical Evidence sheet to
approved evidence IDs and their approved risk-suggestion links. C12 may not
search for or select new evidence after approval. C11's held
`require_approved(current=...)` gate, not a copied record or status, is the
export eligibility boundary. The workbook must use static Core-derived
commercial values, inert untrusted text, and explicit failure. `Draft_Quote.xlsx`
is an example name. No source code, dependency, or architecture permission is
added; C12 remains NOT_AUTHORIZED / NOT_STARTED. Maintenance validation and
candidate identity are kept distinct from implementation proof. Observed
maintenance validation: architecture tests 42 passed; full pytest 246 passed;
Governance Harness 61 PASS / 0 FAIL; generated-view reconciliation `--write`
and `--check` PASS; session bootstrap 127 PASS / 1 expected modified-worktree
WARN / 0 FAIL; Python syntax/import (31 files), shell syntax, changed-file
credential-pattern scan, and `git diff --check` PASS. The resulting candidate
identity is computed and reported outside this candidate to avoid
self-reference. C12 implementation tests and Exit Gate proof remain NOT_RUN /
NOT_PROVEN.

### 1. Card

V1-C12 — Excel Generation

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

Explicit V1-C12 implementation authorization and exact-candidate Git delivery
approval were granted; the latter was consumed by PR #34.

### 5. Files Changed

`src/ai_quotation_intelligence/excel_export.py` and
`tests/test_excel_export.py` created; `tests/test_architecture.py`,
`pyproject.toml`, `PROJECT_CONTROL.md`, this Evidence Map, and
`CARD_LEARNING_AND_DECISION_LOG.md` modified. No C13+ source, AWS,
storage, API, or deployment files.

### 6. Commands Run

`.venv/bin/pytest -q tests/test_excel_export.py` (60 passed),
`tests/test_human_review.py` (32), `tests/test_quotation_agent.py` (57),
`tests/test_agent_tools.py` (24), `tests/test_architecture.py` (57), and
full `.venv/bin/pytest -q` (321 passed). Governance Harness 61 PASS / 0 FAIL;
reconciliation `--write` and `--check` PASS after the recorded initial
Card-start lifecycle-label failure. Bootstrap 127 PASS / 1 expected
modified-worktree WARN / 0 FAIL. Python compile/import, shell syntax,
`.venv/bin/pip check`, changed-file secret-pattern scan, and
`git diff --check` passed. openpyxl 3.1.5 imports from the declared
`openpyxl>=3.1,<4.0` dependency.

Post-merge on clean `main` at `c828f00af069c3de83cc327fd6ee0feb3c89aee6`:
C12 focused 60 passed; C11 regression 32; C10 regression 57; C09 regression
24; architecture 57; full pytest 321; Governance Harness 61 PASS / 0 FAIL;
reconciliation `--check` PASS; bootstrap 128 PASS / 0 WARN / 0 FAIL;
`.venv/bin/pip check`, openpyxl 3.1.5 import, Python compilation/import,
shell syntax, changed-file credential-pattern scan, and Git diff checks PASS.
GitHub reported no PR checks or configured main branch protection/rules; none
was bypassed.

### 7. Focused Tests

PASS (self-validation) — 60 C12 tests: real C10 → C11 → C12 approved
path, exact three-sheet content, Core values, evidence links, denied approval
states, stale/mutated results, inert formula-like text, malformed generated
workbooks, injected formula/hyperlink/macro, explicit failure, and semantic
repeatability. No live AWS or provider call during export.

### 8. Relevant Regression

PASS (self-validation) — C11 32, C10 57, C09 24, architecture 57,
full suite 321. EXPORT is classified with REVIEW and CORE imports only;
negative architecture fixtures reject forbidden inbound/outbound directions.

### 9. Card Evaluation

PASS — held `ReviewSession.require_approved(current=...)` gates
in-memory bytes export; a copied record, approved-looking Quote, rejected
or unreviewed state, and stale/modified result cannot authorize it. The
artifact reloads as `.xlsx` with exactly Quotation, Risk Analysis, and
Historical Evidence sheets. The exact candidate received independent audit
PASS before approved delivery.

### 10. Commercial / Data Invariants

PASS (self-validation) — C04 `calculate_item_cost` and
`calculate_quote_total` supply authoritative static values. The approved
total and each reloaded numeric cell are compared exactly; a Core mismatch
or Excel numeric round-trip loss blocks export. No role, historical metric,
tax, discount, or new evidence is manufactured.

### 11. AI / Provider Validation

PASS (self-validation) — C12 imports no Agent, Agent Tool, Provider,
Bedrock SDK, API, or storage module, and invokes no model or C09 search.
The integration fixture uses scripted C10 output only to form a validated
approved input; export itself reads C11's held decision snapshot.

### 12. Security Validation

PASS (self-validation) — all untrusted exported string categories use one
inert-text boundary; reloaded cells are neither formulas nor hyperlinks.
Workbook validation rejects injected formulas, links, macro entries,
unexpected cells/sheets, and numeric drift. Failure codes do not include
internal exception text. No path or overwrite input exists. Secret-pattern,
syntax/import, and architecture checks passed.

### 13. Failures / Blockers

At Card start `reconcile_governance_views.py --check` failed because the
PROJECT_CONTROL status table used `ACTIVE / IMPLEMENTATION` where the
existing reconciler requires the exact lifecycle token `ACTIVE`. The table
was corrected and `--write`/`--check` passed. The first focused C12 run
failed because its scripted C10 narrative was outside C10's exact allowed
protocol and an architecture negative fixture incorrectly denied C12's
required EXPORT → REVIEW import. Correcting those test assumptions exposed
an openpyxl round-trip detail: saved empty-string cells reload as empty
cells. The workbook validator was corrected to accept that representation
only for expected blank cells. A subsequent formula-injection fixture also
needed to honor the domain model's outer-whitespace normalization and the
C11 request/quote identity relationship. Final focused and full reruns pass;
no failure was hidden or treated as evidence of initial success.

### 14. Exit Gate Evidence

PASS: current held C11 approval only (denial/stale/copy tests);
three required loadable sheets (approved export test); Core item/total and
currency reconciliation (integration and drift tests); approved risk and
evidence references only, with unsupported role/metrics absent; inert text
and post-save formula/link/macro checks; explicit typed failure; no C13+
module/action. Independent audit PASS and approved exact Git delivery are
complete.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent audit, human-accepted non-blocking LOW
test-coverage note and documented V1 limits, approved PR #34 delivery, and
post-merge validation.

### 16. Git Evidence

Start base `70f4eca6c6dd0c9db91a944e1d927e15600b7611` on clean,
synchronized main; implementation branch `card/v1-c12-excel-generation`.
Independently audited candidate identity
`a65b6a34cc4a689b0dcbd16eb49d6c60d8c2a88b30ef34223de2fdac083b9e7f`.
Worktree, staged/index, and committed-tree identities matched exactly.
Delivery commit `9af4c84fdd66cad27eab6f63445beb2e895fe9bf` was pushed;
PR: MERGED — #34, https://github.com/jo-soroush/ai-quotation-intelligence/pull/34;
Merge: COMPLETED — `c828f00af069c3de83cc327fd6ee0feb3c89aee6`.
Post-merge local main and origin/main matched at that SHA with 0/0 divergence
and a clean tree before this separate outcome-only reconciliation.

### 17. Known Limitations

Approval remains C11's in-memory/same-process held-session authority;
caller-asserted reviewer reference is not cryptographic authentication.
The approved result carries evidence IDs and suggestion links, not the
underlying historical records or metrics. The sheet discloses that limit
and synthetic-by-default V1 context. Unrepresentable Excel numeric values
fail explicitly rather than being rounded into a successful export. Bytes
are not persisted; byte-identical ZIP output is not required.
The independent audit's LOW note on direct multi-suggestion/multi-evidence
link test coverage, and these documented V1 limitations, were explicitly
accepted as non-blocking by the human delivery approver.

### 18. What We Learned

CURRENT — the C12 Learning and Decision Log records approval-gate,
in-memory output, Core/export, text-safety, architecture, library, and
failure/recovery rationale.

### 19. Completion Evidence

COMPLETE — implementation, validation, independent audit PASS for the exact
candidate, human-approved PR #34 merge, and separate outcome-only C12 state
reconciliation. Final consistency remains subject to clean-main runtime proof.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C12
Learning Documentation Status:
CURRENT

## V1-C13 — FastAPI Application

### 1. Card

V1-C13 — FastAPI Application

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

Explicit C13 implementation approval and exact-candidate Git delivery approval
were granted; delivery approval was consumed by PR #37.

### 5. Files Changed

`PROJECT_CONTROL.md`, `QUOTATION_CARD_EVIDENCE_MAP.md`,
`CARD_LEARNING_AND_DECISION_LOG.md`, `pyproject.toml`,
`tests/test_architecture.py`; created `src/ai_quotation_intelligence/api.py`
and `tests/test_api.py`. No C14+ source, provider adapter, Core commercial
calculation, review, or export implementation changed.

### 6. Commands Run

`.venv/bin/pip install -e '.[dev]'`; `.venv/bin/pip check`;
`.venv/bin/pytest -q tests/test_api.py`; separate C09–C12 and architecture
focused pytest invocations; `.venv/bin/pytest -q`;
`bash scripts/test_governance_harness.sh` (failure and proving rerun);
`.venv/bin/python scripts/reconcile_governance_views.py --write` and
`--check`; `bash scripts/quotation_session_bootstrap.sh`;
`.venv/bin/python -m compileall -q src tests`; `bash -n` on the two
governance shell scripts; `git diff --check`; package import/version smoke;
targeted credential and forbidden-import scans.

### 7. Focused Tests

PASS — `tests/test_api.py`: 23 passed. Exact six routes, OpenAPI and health,
C10 status mapping, real C10→C11→C12 workflow, workbook reload, explicit
approval/rejection, stale result, repeated/concurrent decisions, process-
local loss, capacity/duplicate rejection, mass-assignment and oversized-body
denial, C11 gate mutation, C12 failure mapping, and sanitized injected
failures were exercised.

### 8. Relevant Regression

PASS — separate suites: C12 60 passed; C11 32 passed; C10 57 passed;
C09 24 passed; architecture 61 passed. Full suite: 348 passed, one
FastAPI/Starlette TestClient deprecation warning, no failures.

### 9. Card Evaluation

PASS — six-route transport adapter
delegates to C10/C11/C12. A real C10 scripted-model run plus real C11 held
session and C12 workbook gates exercises cross-request success and rejection.
Independent audit passed the exact candidate identity; the three reported LOW
findings were accepted by the human delivery approver as non-blocking.

### 10. Commercial / Data Invariants

PASS — transport input excludes client-assigned totals, evidence, approval,
and actual-outcome fields; domain/C10 validate request and result; C11
revalidates the successful draft; C12 rechecks approval and Core-owned
commercial/workbook truth. No C13 arithmetic or fresh evidence discovery.

### 11. AI / Provider Validation

PASS — C10 INVALID/UNAVAILABLE/INSUFFICIENT_EVIDENCE map to explicit
422/503/422 failures. The API imports no C08 SDK or C09 Agent Tools and
requires an injected C10-compatible runner; no live Bedrock call was used.

### 12. Security Validation

PASS in focused tests — client status/record/total/evidence mass assignment,
missing reviewer, invalid decision, stale/repeated decision, unapproved or
rejected export, capacity overflow, request-size overflow, provider/internal
exception leakage, fixed safe XLSX response headers, and unsupported future
routes were challenged. Same-process lock permits one concurrent decision.
Targeted changed-file credential-pattern scan had no matches; `api.py` has no
direct boto3/botocore, C09 Agent Tools, S3, Lambda, API Gateway, or CloudWatch
reference. Python compilation, shell syntax, and API/package import smoke
passed. FastAPI 0.142.2, httpx 0.28.1, openpyxl 3.1.5; `pip check` passed.

### 13. Failures / Blockers

First architecture run (`.venv/bin/pytest -q tests/test_architecture.py`):
2 failed / 53 passed. The pre-C13 tests asserted that no Application module
could import REVIEW or EXPORT. C13 legitimately delegates to both. The tests
were narrowed to allow APPLICATION_BOUNDARY while adding negative probes for
unneeded AGENT, AGENT_TOOL, PROVIDER, SUPPORT, and SDK imports; rerun 61
passed. No implementation authority was broadened beyond actual imports.

First Governance Harness run: PASS=36/FAIL=25. The Card-start update had
removed `Delivery Commit`, `PR`, and `Merge Commit` fields from the Active
Card Record. Temporary fixture construction requires those labels even before
delivery. Restored each as `NOT_CREATED` without inventing future Git IDs;
rerun PASS=61/FAIL=0. The original failures remain historical evidence.

Session bootstrap: PASS=127/WARN=1/FAIL=0. The WARN is the expected dirty
working tree for an undelivered implementation candidate, not a test or
Card-completion PASS. Governance generated-view reconciliation `--write`
and `--check` both passed; `git diff --check` passed.

Pre-implementation read-only C13 preflight: BLOCKED. Inspection found no
authoritative C13 Roadmap Exit Gate, no mandatory C09+ verification block in
the C13 specification, ambiguous approve/reject transport despite C11's
explicit two-way decision contract, and no stated cross-request handling for
the held in-memory C11 session required by C12. This maintenance candidate
adds the Roadmap gate and verification block, makes the six listed routes V1
requirements, identifies `/approve` as an explicit APPROVED/REJECTED decision
transport, and permits bounded single-process state without granting it
approval authority. These are canonical contract corrections, not C13
implementation or Exit Gate proof. The separate maintenance candidate was
independently audited PASS with no findings and delivered in PR #36. This
historical preflight does not prove C13 implementation.

Maintenance validation observed on `maintenance/pre-c13-canonical-remediation`:
governance reconciliation `--write` and `--check` PASS; Governance Harness
PASS=61/FAIL=0; `.venv/bin/pytest -q` 321 passed; architecture tests 57
passed; bootstrap PASS=127/WARN=1/FAIL=0 (expected undelivered working-tree
warning); shell syntax, Python compilation/import smoke, changed-diff secret
pattern scan, and `git diff --check` PASS. These results validate the
maintenance candidate, not C13 implementation or its Exit Gate.

### 14. Exit Gate Evidence

PASS: six exact routes and typed input/output (`test_api.py`);
handlers delegate to existing C10/C11/C12 and do not import C09, provider,
or Core arithmetic (`api.py`, architecture suite); C10 failures and malformed
HTTP inputs are sanitized; decision payload, not `/approve` URL, chooses
APPROVED/REJECTED through C11; C12 receives the held C11 session plus
current result and rejects stale/unapproved state; bounded store and lock
preserve one-decision semantics; injected provider/internal failures return
bounded codes; no C14+ module or service. Independent audit independently
proved this gate for the exact candidate.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent audit, accepted non-blocking LOW findings,
approved PR #37 delivery, and complete post-merge validation.

### 16. Git Evidence

Start base `48428e2b303421580820f5195a7fc3a5a3f9419c`; delivery branch
`card/v1-c13-fastapi-api-layer`; audited candidate identity
`8b1ed88292e7bdeb416fe18b1a6268fc06a9763ffd6805da947a05882b17273e` matched
worktree, staged index, and committed tree. Delivery commit
`8c39b5fd58568eb172519e278ef5db6f504f545b` pushed; PR: MERGED — #37,
https://github.com/jo-soroush/ai-quotation-intelligence/pull/37; Merge: COMPLETED —
`b695fbf7366b66e73fb47f354ac65ada8c352435`. Post-merge local `main` and
`origin/main` matched at that merge commit, 0/0, with clean tree before this
separate outcome-only reconciliation.

Post-merge on `main`: C13 API 23 passed; C12 60; C11 32; C10 57; C09 24;
full pytest 348; architecture 61; Governance Harness 61 PASS / 0 FAIL;
reconciliation `--check` PASS; bootstrap 128 PASS / 0 WARN / 0 FAIL;
`.venv/bin/pip check`, FastAPI 0.142.2/httpx 0.28.1 import, Python
compilation/import, security pattern scan, and `git diff --check` PASS. No
CI checks were configured for the PR; none were bypassed.

### 17. Known Limitations

Process-local store is lost on restart and not shared across workers;
reviewer ID is caller-asserted rather than authenticated. No deployment,
server command, S3, or persistence is provided. Existing AWS access would
be needed to compose a live Bedrock runner; no live call was required.
TestClient currently emits one Starlette deprecation warning for `httpx`.
The independent audit's three LOW findings (RLock necessity test strength,
partly redundant exact AgentResult type guard, and TestClient deprecation)
were explicitly accepted as non-blocking by the human delivery approver.

### 18. What We Learned

See the C13 Learning / Decision Log: the store is transport continuity,
not approval; C11/C12 gates remain load-bearing; legacy architecture and
governance fixture assumptions needed bounded state-aware corrections.

### 19. Completion Evidence

COMPLETE — implementation, independent audit PASS, human-approved PR #37
merge, and post-merge validation are complete. The final Card-state
consistency gate is evaluated on the delivered reconciliation state.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C13
Learning Documentation Status:
CURRENT

## V1-C14 — Amazon S3 Integration

### 1. Card

V1-C14 — Amazon S3 Integration

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

Created `src/ai_quotation_intelligence/storage_contract.py`,
`src/ai_quotation_intelligence/s3_storage.py`, and `tests/test_s3_storage.py`.
Modified `src/ai_quotation_intelligence/config.py`,
`tests/test_architecture.py`, `PROJECT_CONTROL.md`, this Evidence Map,
`CARD_LEARNING_AND_DECISION_LOG.md`, `SOURCE_ADAPTATION_TRACEABILITY.md`,
and `scripts/quotation_session_bootstrap.sh` (a narrow source-ledger sanity
check needed for the new C14 reference-only record).
No C13 source, dependency declaration, Roadmap, or Card Specification changed.

### 6. Commands Run

Observed implementation checkpoint: `.venv/bin/pytest -q
tests/test_s3_storage.py tests/test_architecture.py` passed 102 tests before
the malformed-SDK-error hardening. Subsequent separate focused commands:
`.venv/bin/pytest -q tests/test_s3_storage.py` passed 34 and
`.venv/bin/pytest -q tests/test_architecture.py` passed 69. Earlier full
`.venv/bin/pytest -q` passed 389 before that final one-test addition.
Final commands: focused C14 34 PASS, C12 60 PASS, C13 23 PASS, architecture
69 PASS, full `.venv/bin/pytest -q` 390 PASS/one existing warning;
`python scripts/reconcile_governance_views.py --write` and `--check` PASS;
`bash scripts/test_governance_harness.sh` 61 PASS/0 FAIL;
`bash scripts/quotation_session_bootstrap.sh` 127 PASS/1 expected dirty-tree
WARN/0 FAIL after the source-ledger sanity fix. `.venv/bin/pip check`,
Python compile/import, `bash -n`, and `git diff --check` all PASS.

### 7. Focused Tests

PASS — 34 deterministic local C14 tests, including real C11-approved/C12
export bytes, fake S3 conditional-write behavior, botocore Stubber call
shape, retrieval integrity, malformed responses, failure sanitization,
same-process contention, and ambiguous-write retry behavior. No network,
bucket, or credentials used.

### 8. Relevant Regression

C12/C13 combined regression checkpoint: `.venv/bin/pytest -q
tests/test_s3_storage.py tests/test_excel_export.py tests/test_api.py` passed
116, with one pre-existing non-functional Starlette/httpx TestClient warning.
Final separate results: C12 60 PASS, C13 23 PASS; full suite 390 PASS.

### 9. Card Evaluation

Local ELEVATED-boundary evaluation: key/identity collision probes, duplicate
conditional write, forged metadata/content, missing-versus-access denial,
provider malformed-success/error payloads, no public ACL/delete/bucket or
C13 operations, and ambiguous-write recovery covered by focused tests.
Threat model and targeted mutation-resistance rationale are in the C14
Learning / Decision Log. Live S3: NOT_RUN / NOT_REQUIRED; the user has no
bucket and this does not block the local Exit Gate.

### 10. Commercial / Data Invariants

C14 performs no commercial arithmetic or approval decision. The focused
round-trip fixture obtains a validated workbook from actual C11 approval and
C12 export, then verifies storage bytes/identity only. Storage cannot prove
arbitrary external provenance: trusted composition must supply C12 bytes.

### 11. AI / Provider Validation

Provider isolation verified by adapter/architecture tests: boto3/botocore
stay in PROVIDER; owned result/failure types cross the storage contract.
No Bedrock, AI, or live S3 call was used.

### 12. Security Validation

Focused adversarial tests exercise path-like identity rejection, fixed key
namespace, ZIP/XLSX envelope rejection, conditional no-overwrite, metadata
and body substitution, strict provider success response, exception-message
sanitization, and no explicit credential/ACL argument. Architecture tests
prove no reverse S3 adapter import by CORE/REVIEW/EXPORT/APPLICATION_BOUNDARY.

### 13. Failures / Blockers

Implementation review found that a first-pass `PK`-prefix check could admit
arbitrary non-XLSX bytes. This was corrected with a bounded ZIP/XLSX package
envelope check, leaving C12's business validation with C12. Review also
found a malformed unhashable SDK error code could escape sanitization;
explicit string-type validation and a regression test corrected it. Neither
first-pass gap is erased from this record. No current implementation blocker
is known; independent audit and delivery remain pending.

The first bootstrap run failed its source-adaptation sanity check because it
hard-coded an empty ledger; C14's documented AWS API reference was the first
record. The script now validates matching nonzero counts and actual record
headings while retaining the original empty-ledger case. Bootstrap rerun
passed with only the expected dirty-worktree warning.

The first post-reconciliation FINAL_CARD_STATE_CONSISTENCY_GATE run failed
because exact-value fields and the Git-evidence parser did not accept
descriptive suffixes in State, approval, recommended state, and learning
status, and the status table emitted `34` rather than its required `PASS`
focused-test value. Delivery was intact; this was a state-record format
mismatch. This bounded follow-up normalizes those labels and records delivery
evidence in the established explicit PR/Merge format. The gate is rerun on
synchronized main after this follow-up merges.

Pre-implementation read-only C14 preflight: BLOCKED before authorization by
the missing authoritative Roadmap Exit Gate and missing C09+ verification
block. It also identified ambiguity in the primary persistable artifact/input
and retrieval authority. This canonical maintenance resolves those contract
gaps only; C14 remains NOT_STARTED / NOT_AUTHORIZED. The user reports that no
S3 bucket currently exists; no AWS calls or resource changes were performed,
and bucket absence is not a blocker. Exact key format, duplicate/idempotency
policy, integrity mechanism, architecture category, and IAM details remain
implementation decisions.

Independent audit of the original documentation candidate
`4d3f48ebd8f4f5dbda1852c083ca003321588dc6f39f30856365565190715fc8` returned
PASS with one MEDIUM finding: C14's Advanced Verification Decision was less
complete than the established C09–C13 per-technique tables and did not
explicitly decide Threat Modeling. One LOW process note observed that the
candidate was initially on `main`. The candidate was moved without content
change to `maintenance/pre-c14-canonical-remediation` (the original identity
was reverified there); the focused remediation expanded only the C14
Advanced Verification Decision using the established 14-technique taxonomy.
Threat Modeling is REQUIRED due to C14's ELEVATED storage trust boundary;
real/live AWS remains optional supplementary evidence. No C14 implementation,
dependency, architecture, or authorization change was made.

Independent audit of implementation candidate identity
`98f286074c8d1897ae19664d845c778862c8f1c915e3cec80b2c640e42401500` returned
PASS: zero critical/high/medium findings, one accepted non-blocking LOW
finding, no blockers, and independent Exit Gate proof. The LOW finding was
that PROJECT_CONTROL §18 still showed C14 Quality Gate NOT_RUN and Evidence
PARTIAL while current sections recorded self-validation and audit status.
The human accepted it as cosmetic for delivery; outcome-only reconciliation
updates the table and preserves the original finding here as history.

### 14. Exit Gate Evidence

Self-validation plus independent audit maps the Roadmap gate to: C12-origin round-trip fixture;
provider-neutral `StorageContract`; deterministic content-bound key under a
fixed namespace; atomic `IfNoneMatch="*"` reject-duplicate PutObject;
validated GetObject metadata, content type/length, SHA-256 and XLSX package
envelope; explicit missing/access/provider/integrity errors; standard boto3
credential chain; no ACL/public/delete/create/presigned operations; local
fake and botocore Stubber verification; unchanged C13; architecture tests.
Live AWS remains optional and unexecuted. Independent audit proved the exact
candidate; delivery and post-merge validation completed.

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent audit, approved PR #41 delivery, and
post-merge validation passed. The accepted LOW finding remains recorded
above; it was not remediated in the implementation candidate.

### 16. Git Evidence

Start base: `f4692032c986585f54610799ad3867077e6c1`.
Delivery branch: `card/v1-c14-s3-storage`.
Audited candidate identity:
`98f286074c8d1897ae19664d845c778862c8f1c915e3cec80b2c640e42401500`
matched the worktree, staged index, and committed tree.
Delivery commit: `e73b8de7a7b521c706e210e21d3776d44a23bb43`.
Push: COMPLETED — `origin/card/v1-c14-s3-storage`.
PR: MERGED — #41; https://github.com/jo-soroush/ai-quotation-intelligence/pull/41.
Merge: COMPLETED — `2f99f4c24f9182029ded27b15c4f123c810a61fe`.
Post-merge main validation:
C14 34, C12 60, C13 23, full pytest 390, architecture 69, Governance Harness
61/0, reconciliation PASS, bootstrap 128/0/0, pip check and SDK imports,
compilation/import, shell syntax, security pattern scan, and diff checks PASS.
No status checks were reported for PR #41; none were bypassed. Completion
reconciliation and final state gate are processed separately.

### 17. Known Limitations

No live bucket/IAM/policy/encryption behavior verified; none is required for
C14 Exit Gate. The storage contract cannot cryptographically attest that
bytes came from C12, so trusted application composition remains necessary.
No C13 upload, persistence workflow across processes, delete, public
sharing, presigned URL, or deployment is provided. After an ambiguous
network failure following an S3 write, retry is an explicit duplicate;
caller can retrieve using the known content-bound identity. No rollback
deletion is attempted.
The accepted non-blocking audit LOW was the cosmetic stale C14 row in
PROJECT_CONTROL §18; reconciliation updates it, with the original audit
observation preserved above. No S3 bucket was created; live AWS remains
NOT_RUN / NOT_REQUIRED.

### 18. What We Learned

See C14 Learning / Decision Log for architecture, conditional-write,
integrity, failure, threat-model, source-reference, and recovery rationale.

### 19. Completion Evidence

COMPLETE — exact candidate delivery and post-merge gates passed; final state
consistency gate runs on main after the label/evidence-format reconciliation.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C14
Learning Documentation Status:
COMPLETE

## V1-C15 — AWS Deployment

### 1. Card

V1-C15 — AWS Deployment

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE
State Detail: Exit Gate PROVEN; repaired-artifact live health independently verified; PR #45 merged; final reconciliation and state consistency complete

### 4. Human Start Approval

YES
Approval Detail: Explicit 2026-10-02 authorization covered local implementation, bounded initial deployment, one repaired-artifact retry in account `553541119072` / `us-east-1`, KEEP DEPLOYED, and Git delivery. Approvals were consumed by completion; C16 remains unauthorized.

### 5. Files Changed

`deployment/__init__.py`, `deployment/lambda_handler.py`, `deployment/c15-http-api.json`, `deployment/requirements-lambda.txt`, `deployment/README.md`, `scripts/build_c15_lambda.py`, `scripts/validate_c15_package.py`, `scripts/c15_signed_health.py`, `tests/test_c15_deployment.py`; plus `pyproject.toml`, `tests/test_architecture.py`, `PROJECT_CONTROL.md`, `QUOTATION_CARD_EVIDENCE_MAP.md`, `CARD_LEARNING_AND_DECISION_LOG.md`, and `SOURCE_ADAPTATION_TRACEABILITY.md`. C13 `api.py` was not changed.

### 6. Commands Run

Initial local validation used `python -m pytest -q tests/test_c15_deployment.py`, C13/C12/C14 regressions, full pytest, architecture tests, a Linux ZIP build/validator, and `python -m pip check`. The separately approved first live attempt created a private artifact bucket, uploaded immutable key `c15/ff64e11a83a3a70e31524179bad196eeb75a0e120a8859962e26f7101816a939.zip`, and created CloudFormation stack `aqi-c15-nonprod`; read-only AWS inspection verified deployed Lambda/API/IAM resources. The first `python scripts/c15_signed_health.py --api-id yj2yk1sk3g --region us-east-1` returned HTTP 500. During the subsequent local-only remediation, the broken ZIP was imported in an isolated Linux Python 3.13 container, a fresh ZIP was built at `/tmp/aqi-c15-remediation.AfXp10/aqi-c15-lambda.zip`, and `python scripts/validate_c15_package.py ... --runtime-smoke` passed; no AWS call was made in that phase. After separate live retry approval, the repaired immutable ZIP was uploaded to the same bucket, the existing stack was updated through a reviewed change set, and the same signed health command returned HTTP 200.

### 7. Focused Tests

PASS — 21 passed after remediation (19 original plus two deterministic dependency-closure regressions). Simulated HTTP API payload-2.0 events prove `/health`, JSON/error routing, and exact base64 XLSX bytes/MIME/Content-Disposition through Mangum; malformed events and adapter exceptions return sanitized 500; template route/IAM/config, targeted template mutations, and builder/package boundary are checked. The validator rejects the previously deployed incomplete archive; an isolated Linux container imports the repaired packaged handler and returns `{"status":"ok"}` without network or AWS client construction.

### 8. Relevant Regression

C13/C12/C14 combined regression: 117 passed (23/60/34); architecture: 70 passed; full pytest: 412 passed. One pre-existing Starlette/httpx TestClient deprecation warning remains.

### 9. Card Evaluation

PASS — the initial real stack's signed `/health` returned HTTP 500, and independent CloudWatch diagnosis reported `Runtime.ImportModuleError: No module named 'opentelemetry'`. The isolated Linux import reproduced the failure before application initialization. The corrected archive passed dependency closure and isolated handler/health import, was deployed to the same stack under separate approval, and the real signed `/health` returned HTTP 200 with `{"status":"ok"}`. Independent live verification and candidate audit passed; Git delivery and final reconciliation are recorded below. This proves deployment reachability, not Bedrock, application S3, durable review state, or production readiness.

### 10. Commercial / Data Invariants

PASS — no commercial arithmetic, approval, Excel generation, C13 route, or C14 storage behavior was changed; static C13 export bytes remain under the existing C11/C12 authority.

### 11. AI / Provider Validation

PASS for repaired local package import/health isolation — C08 creates the Bedrock client lazily, and the isolated runtime smoke forbids boto3 client creation during `/health`. Live Bedrock invocation is NOT_RUN / NOT_REQUIRED for C15.

### 12. Security Validation

LOCAL_AND_DEPLOYED_CONFIGURATION_PASS — read-only AWS inspection after the approved retry found six `AWS_IAM` routes, no API CORS configuration, the unchanged log-only Lambda runtime role, no Bedrock runtime permission (empty `BedrockModelArn`), and no application-S3 runtime permission. The artifact bucket retains all four public-access blocks, bucket-owner-enforced ownership, and SSE-S3. The repaired package excludes credential-like files and includes the required runtime dependency; no credential was added. Real signed `/health` HTTP 200 proves live application startup only.

### 13. Failures / Blockers

Observed and repaired locally: `pip install mangum==0.20.0` installed the package but returned shell exit 1 because pyenv could not rehash unwritable shims; `pip show`, import and tests proved installation. The first ZIP validator failed because pip generated bytecode; builder now excludes bytecode. The next validator failed on botocore's required public `cacert.pem`; validator now narrowly allows only that file while rejecting credential-like PEMs. An initial architecture assertion counted imported symbols as module imports; corrected to validate both. On resume, the reported wildcard risk was rechecked: the current pre-edit template already rejected literal `*`, but its optional account field was broader than supported resource forms. The parameter now accepts only absence, accountless foundation-model ARNs, or 12-digit-account inference-profile/application-inference-profile ARNs; whitespace and malformed forms fail. A mutation test widens the pattern to `.*` and verifies the contract test fails. AWS documentation review clarified the Lambda integration URI form, now explicit in the template and tests. The first C15 ACTIVE-state consistency run failed three exact assertions: Project Control expected `Active Card: V1-C15`, the Evidence Map expected a standalone `ACTIVE` state value, and the approval subsection expected a standalone `YES`; each original value included human-readable suffixes. C09 history established these fields as bare canonical values, with details on following lines. No AWS or application-authority failure was observed.

Later live failure: under separate human approval, CloudFormation stack `aqi-c15-nonprod` reached `CREATE_COMPLETE` in account `553541119072`, region `us-east-1`; Lambda `arn:aws:lambda:us-east-1:553541119072:function:aqi-c15-api`, API `yj2yk1sk3g`, and deployment-artifact bucket `aqi-c15-artifacts-c69acfc4` were retained. The first signed HTTPS `/health` returned HTTP 500. An independent CloudWatch diagnosis identified `Runtime.ImportModuleError: Unable to import module 'lambda_handler': No module named 'opentelemetry'`. In this remediation, isolated Linux Python 3.13 import of the deployed ZIP reproduced the exact import chain `lambda_handler → ai_quotation_intelligence.api → fastapi.telemetry → opentelemetry`, failing before application initialization. Package metadata and pip resolution proved FastAPI 0.142.2 requires `opentelemetry-api>=1.44.0`; the old `--no-deps` snapshot omitted it. `opentelemetry-api==1.45.0` requires only `typing-extensions>=4.5.0`, already pinned. The new validator checks every packaged distribution against the exact pinned snapshot and evaluates the packaged `Requires-Dist` closure for Linux Python 3.13. It rejects the old broken ZIP. A freshly built ZIP passes the validator and isolated Linux packaged handler `/health` smoke; it has **not** been uploaded or deployed. Live retry is NOT_RUN / NOT_AUTHORIZED.

### 14. Exit Gate Evidence

Initial local evidence: route set and JSON request/error mapping passed; controlled `.xlsx` round-tripped byte-for-byte through payload-2.0 base64 response. The initial package validator passed the ZIP despite missing FastAPI's OpenTelemetry import dependency. The separately approved live deployment created stack ID `arn:aws:cloudformation:us-east-1:553541119072:stack/aqi-c15-nonprod/d1faf150-be49-11f1-9c0b-0e7fb78001fd` and API endpoint `https://yj2yk1sk3g.execute-api.us-east-1.amazonaws.com`; deployed route/IAM configuration matched the bounded template, but signed `/health` was HTTP 500, not the required 200. The local remediation ZIP is `/tmp/aqi-c15-remediation.AfXp10/aqi-c15-lambda.zip`, size 19,810,905 bytes, SHA-256 `5ff6ffe282706a7b8b423580cefc74dffeb54c1ef225ef6bb889cb3fb322279c`, differing from deployed ZIP SHA-256 `ff64e11a83a3a70e31524179bad196eeb75a0e120a8859962e26f7101816a939`. `python scripts/validate_c15_package.py ... --runtime-smoke` returned `C15_PACKAGED_HANDLER_AND_HEALTH: PASS` and `C15_LAMBDA_PACKAGE_VALIDATION: PASS` with Docker networking disabled and only extracted artifact contents on the module path. Focused C15 tests: 21 passed; C13/C12/C14 combined regressions: 117 passed; full pytest: 412 passed; architecture: 70 passed; Governance Harness: 61/0; reconciliation and ACTIVE-state consistency: PASS; bootstrap: 127 PASS / 1 expected dirty-tree WARN / 0 FAIL; pip check and diff check: PASS. The repaired ZIP is local only.

Separately approved repaired-artifact live retry, 2026-10-02: candidate identity `32f798da8ee13c489ba0c553c17cb9990e644aebace57b0e4c1df8dbc2fed98a` and repaired ZIP SHA-256 `5ff6ffe282706a7b8b423580cefc74dffeb54c1ef225ef6bb889cb3fb322279c` were verified before AWS mutation. The ZIP was uploaded once under immutable key `c15/5ff6ffe282706a7b8b423580cefc74dffeb54c1ef225ef6bb889cb3fb322279c.zip` to the existing private deployment-artifact bucket `aqi-c15-artifacts-c69acfc4`. A reviewed change set updated only the existing `aqi-c15-nonprod` stack without resource replacement; final status was `UPDATE_COMPLETE`. Lambda `aqi-c15-api` retained Python 3.13, x86_64, 512 MiB, 30-second timeout, `lambda_handler.handler`, and its original log-only role. Deployed `CodeSha256` `X/b/4oJwanuLQjWAzvx03/61TB7yJe9ruInLP7MiJ5w=` exactly matched the local repaired ZIP's base64 SHA-256. API `yj2yk1sk3g` retained the same six AWS_IAM routes, Lambda proxy integration, scoped invoke permission, and no CORS. A real SigV4-signed HTTPS `GET /health` at `https://yj2yk1sk3g.execute-api.us-east-1.amazonaws.com` returned HTTP 200 with exact body `{"status":"ok"}` between `2026-10-02 11:26:18 UTC` and `11:26:21 UTC`. Minimal associated Lambda logs showed initialization, invocation, and completion without ImportModuleError, traceback, or obvious credential/secret pattern. Live Bedrock and application/data S3 were not used; their runtime permissions remain absent. Resources were retained by human choice. Post-live C15 tests: 21 passed; full pytest: 412 passed; architecture: 70 passed; Governance Harness: 61/0; reconciliation, ACTIVE-state consistency, package runtime smoke, pip check, and diff check: PASS.

Exit Gate Status: PROVEN — local startup and API Gateway event simulation, reproducible deployment configuration, least-privilege IAM and route checks, exact repaired artifact identity, successful real API Gateway → Lambda → FastAPI signed `/health`, independent live verification, and post-live regressions passed. No full-cloud quotation workflow, production readiness, Bedrock/S3 operation, or durable process-local state is claimed.

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent audit and independent live verification passed; approved PR #45 delivery and post-merge validation passed; outcome-only completion reconciliation is recorded here.

### 16. Git Evidence

Branch `card/v1-c15-aws-deployment` started from `3d36b7c1448a6b89031f49d532070310fcbb20b3`. Independently verified candidate identity `d3544c66c1e2a243dcb82d0590e57d12b6bd2043cf7e5a514558044be2ceea39` matched the worktree, staged index, and committed tree. Delivery commit `34189d39041286141a78a1edd9bef0a85d53bcc4`; push completed; PR #45 (`https://github.com/jo-soroush/ai-quotation-intelligence/pull/45`) merged as `37b4ab7852522723529edf652fa125c01f5cca0e`.

### 17. Known Limitations

C13 process-local review state is not durable/shared across Lambda environments; reserved/provisioned concurrency is not a state solution. The first health attempt failed at Lambda import; the repaired ZIP has now passed a real signed health retry. No live Bedrock or application-S3 proof and no production-readiness claim. The default runtime role has no Bedrock or application-S3 permission. Binary XLSX remains locally validated through the adapter, not through a full live workflow. The artifact bucket and stack are retained by human decision; further live AWS change requires separate authorization.

### 18. What We Learned

Local event simulation proves adapter semantics, not actual AWS reachability. A pinned Linux-wheel ZIP can be built and inspected without AWS, but filename/presence checks alone did not prove importability when `--no-deps` was used. Complete packaged metadata closure plus isolated Linux handler/health import is required. Deployment identity and runtime identity must remain separate; process memory cannot be claimed as durable.

### 19. Completion Evidence

COMPLETE — implementation and independently verified live Exit Gate delivered in PR #45; final state reconciliation recorded. The final consistency gate is run on synchronized main after this reconciliation merges.

### 20. Recommended State

COMPLETE
Approved delivery and final state reconciliation passed. Active Card: NONE.
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
Learning Documentation Status:
COMPLETE
Implementation rationale, initial HTTP 500, root cause, repair, live retry, delivery, and limitations are recorded; first failure remains preserved.

### Pre-C15 Canonical Remediation (Documentation Only)

The read-only C15 preflight was BLOCKED by the missing authoritative
Roadmap Exit Gate and missing mandatory C09+ verification block. It also
identified unspecified treatment of C13 process-local state under Lambda,
whether real AWS is required for the final gate, public/private deployment
and access control, and reproducibility versus Console-only setup.

This maintenance adds the C15 Roadmap Exit Gate and complete verification
block, and resolves those points as an accepted V1 process-local-state
limitation, local-first implementation/audit with live AWS required only for
the final Exit Gate, a bounded non-production access boundary, and
repository-controlled reproducibility. No implementation, AWS resource,
dependency, or architecture permission was added. C14 remains COMPLETE;
Active Card remains NONE; C15 remains NOT_AUTHORIZED / NOT_STARTED.
Validation results for this documentation candidate are recorded only after
they are actually run.

## V1-C16 — CloudWatch Observability

### 1. Card

V1-C16 — CloudWatch Observability

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

`PROJECT_CONTROL.md`; this Evidence Map; `CARD_LEARNING_AND_DECISION_LOG.md`;
`src/ai_quotation_intelligence/{logging_config,api,quotation_agent,agent_tools,bedrock,s3_storage}.py`;
`tests/{test_observability,test_architecture}.py`. No dependency, deployment,
Lambda handler, IAM, or AWS resource definition was changed. The separately
approved live step updated the existing Lambda code in place, using the
retained C15 stack and log group; no new stack resource was created.

### 6. Commands Run

`PYTHONPATH=.:src pytest -q` (430 passed); focused C16 and architecture
pytest; C08/C09/C10/C13/C14/C15 regression pytest (168 passed);
`python scripts/reconcile_governance_views.py --write` and `--check`;
`bash scripts/final_card_state_consistency.sh V1-C16 ACTIVE`;
`bash scripts/test_governance_harness.sh` (61 PASS / 0 FAIL);
`bash scripts/quotation_session_bootstrap.sh` (127 PASS / one expected dirty-tree WARN / 0 FAIL);
`python -m pip check`; `python -m compileall -q src deployment scripts`;
`bash -n scripts/*.sh`; credential-pattern scan; `git diff --check`.
The local-implementation checkpoint ran no AWS command. Separately approved
live execution used read-only STS, CloudFormation, Lambda, API Gateway, IAM,
S3, and CloudWatch checks; `aws cloudformation execute-change-set` for the
existing `aqi-c16-997af354`; `aws cloudformation wait stack-update-complete`;
and exactly one signed `GET /health` through `scripts/c15_signed_health.py`.
Post-live focused/regression/full/architecture pytest, Governance Harness,
reconciliation, ACTIVE-state check, pip, compile/shell syntax, credential
scan, and diff checks passed at the counts above.
The post-delivery main validation then passed: full pytest 430, architecture
73, Governance Harness 61/0, reconciliation PASS, bootstrap 128/0/0, pip,
compile/shell syntax, secret scan, and diff checks.

### 7. Focused Tests

PASS — `tests/test_observability.py`: 15 passed; JSON fields and stdout,
request/quotation correlation, concurrent isolation, API latency/final status,
agent/tool/Bedrock/S3 outcomes, token usage, sensitive-data absence, sink
failure, no-AWS local health, and targeted identifier-filter mutation sensitivity.

### 8. Relevant Regression

PASS — C08/C09/C10/C13/C14/C15 combined regression: 168 passed with
`PYTHONPATH=.:src`; full suite: 430 passed. Existing Starlette/httpx
TestClient deprecation warning remains unrelated and accepted.

### 9. Card Evaluation

PASS — deterministic invariants, contracts, component integration,
failure injection, adversarial privacy tests, and targeted mutation
sensitivity passed. Conditional concurrency/context isolation was exercised;
generated property tests and fuzzing were not needed for this fixed schema.
Differential, agent evaluation, and formal methods were not applicable.
Rollback is a bounded instrumentation revert with no AWS observability
resource to remove. The one signed live health request emitted the expected
structured API event in the retained log group; independent live verification
passed, and approved delivery is recorded below.

### 10. Commercial / Data Invariants

PASS — existing commercial, review, export, and storage regressions passed;
instrumentation neither changes these authorities nor logs commercial values.

### 11. AI / Provider Validation

PASS — injected Bedrock success/failure tests prove latency, optional valid
token counts, and sanitized failure categories without logging prompts,
raw model responses, or `BedrockResult.message`.

### 12. Security Validation

PASS — adversarial tests reject unsafe identifiers and raw log messages,
exercise a provider secret-looking exception, and verify reviewer/body/prompt/
workbook absence. Repository credential-pattern scan, package syntax, pip
integrity, and `git diff --check` passed. The deployed runtime role remained
log-only; the six API routes remained `AWS_IAM`, CORS was absent, and the
observed event contained no prohibited sensitive field or payload.

### 13. Failures / Blockers

The read-only preflight was BLOCKED by the missing authoritative
Roadmap Exit Gate, missing C09+ verification block, and unresolved scope and
security ambiguities. The pre-C16 remediation addressed canonical
documentation only; no AWS resource was modified. C16 local implementation
was then explicitly authorized and started. Two new-test fixture defects
(unstructured warning capture and an over-broad synthetic API payload) were
corrected; the first C15 standalone regression invocation omitted repository
root from `PYTHONPATH` and was rerun successfully. Final live CloudWatch
evidence was initially paused because change set `aqi-c16-997af354` proposed
an `ApiIntegration` Modify via dynamic `ApiFunction.Arn` dependency. An
independent diagnosis classified this as non-semantic, and a separate human
approval authorized execution of that exact existing change set. The
subsequent stack events show only the in-place `ApiFunction` update; the
integration ID and URI remained unchanged. No iterative remediation was
performed. The independent live verifier confirmed the event schema,
correlation, and sensitive-data absence.

### 14. Exit Gate Evidence

Local implementation alone did not prove the live requirement. After separate
human approval, the retained `aqi-c15-nonprod` stack in account `553541119072`
and region `us-east-1` executed existing change set `aqi-c16-997af354` to
`UPDATE_COMPLETE` on 2026-10-04. It changed the `ApiFunction` code in place;
no physical resource ID, runtime IAM, API route authorization, CORS, or
effective API integration URI changed. The artifact key is
`c15/997af354e5ca234fe6551ffa16dca66e5708c2ae63a995f2ba21c701a729d2e3.zip`;
the ZIP SHA-256 is `997af354e5ca234fe6551ffa16dca66e5708c2ae63a995f2ba21c701a729d2e3`;
Lambda `aqi-c15-api` reported `CodeSha256` =
`mXrzVOXKI0/mVR/6FtymblcIwq5jqZXyuiHHAacp0uM=`, exactly matching the
locally computed base64 SHA-256. The previous C15 artifact remains available
as the rollback key.

Exactly one real AWS_IAM/SigV4 `GET /health` through API `yj2yk1sk3g` at
`https://yj2yk1sk3g.execute-api.us-east-1.amazonaws.com` returned HTTP 200
and `{"status":"ok"}` during 2026-10-04 18:25:11–18:25:21 UTC. CloudWatch
log group `/aws/lambda/aqi-c15-api`, stream
`2026/10/04/[$LATEST]34cc8ca8a00f473e89456f82f128148d`, contains this
actual structured event at 2026-10-04T18:25:17.819Z:

```json
{"component":"api","duration_ms":16,"event":"api_request","http_status":200,"operation":"health","request_id":"8dd0f9cdf3d145838b08a30996eec2ec","status":"success"}
```

The event is parseable JSON with all required health fields, a bounded
request ID, and no credential, token, secret, prompt, raw model/provider
message, reviewer ID, request/response body, workbook, or commercial/customer
payload. This live proof demonstrates deployment reachability and C16
observability only, not Bedrock/S3 readiness, business-workflow correctness,
durable state, or production readiness. Live Bedrock and application S3 were
not invoked; no custom metrics, alarms, dashboard, X-Ray, IAM change, or new AWS
stack resource was introduced. The retained log group still has seven-day
retention. Post-live local mode and suites passed (C16 15, relevant regressions
168, full pytest 430, architecture 73, Governance Harness 61/0).

Exit Gate Status: PROVEN

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent local and live verification, Exit Gate,
approved PR #48 delivery, post-merge validation, and completion reconciliation.

### 16. Git Evidence

Audited candidate identity: `edbb6a9df2737722484fc24a2ac210645483823ca466b39c24dd0810d7e04d98` — exact match verified across worktree, staged index, and committed tree.
Delivery Commit: `00ddb696f965ef695e7bef547d0541c97604500b`
GIT_DELIVERY_APPROVAL: GRANTED / CONSUMED — PR #48 merged
PR: MERGED — #48 — https://github.com/jo-soroush/ai-quotation-intelligence/pull/48
Merge: COMPLETED — `810cab18e20c9e4560eaee52e2043d32ba40f75b`
Post-merge main validation: full pytest 430 passed; architecture 73 passed; Governance Harness 61 PASS / 0 FAIL; reconciliation PASS; clean bootstrap 128 PASS / 0 WARN / 0 FAIL; pip, compile/shell syntax, secret scan, and diff checks PASS.

### 17. Known Limitations

The live event proves health-path observability, not agent, Bedrock, S3,
commercial, or production behavior. The accepted non-blocking LOW findings
from the independent local audit remain known limitations: ContextVar reset
is defensive but its removal is not uniquely caught by current tests; and
redaction guarantees are tested through the structured logging pathway, while
hypothetical stray `print()` or secondary-logger paths are not covered (no
such path exists in the delivered candidate). The C15 resources and new code
artifact are intentionally retained; further AWS modification requires
separate approval. No production-readiness claim is made.

### 18. What We Learned

Bounded stdout JSON and context-local IDs provide local operational visibility
without turning logging into business authority. Raw provider messages must
never be used as error fields. See the C16 Learning and Decision Log for the
test-fixture failures, threat model, alternatives, and rollback rationale.

### 19. Completion Evidence

Live CloudWatch proof and independent live verification passed; approved Git
delivery and post-merge validation completed. C16 is COMPLETE; Active Card is
NONE. Retained AWS resources remain unchanged, Bedrock and application S3 were
not used for C16 live verification, and C17 remains NOT_AUTHORIZED.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C16
Learning Documentation Status:
CURRENT

## V1-C17 — Evaluation Harness

### 1. Card

V1-C17 — Evaluation Harness

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

### 5. Files Changed

Local C17 candidate changes:

- `evaluation/__init__.py`
- `evaluation/c17.py`
- `evaluation/golden_v1.json`
- `evaluation/golden_v1.sha256`
- `tests/test_evaluation.py`
- `tests/test_architecture.py`
- `PROJECT_CONTROL.md`
- this Evidence Map
- `CARD_LEARNING_AND_DECISION_LOG.md`

No production source, dependency, deployment, AWS, Bedrock, Roadmap, or Card
Specification file changed.

### 6. Commands Run

- `.venv/bin/pytest -q tests/test_evaluation.py`: 35 passed
- `.venv/bin/pytest -q tests/test_calculation.py tests/test_comparison.py tests/test_retrieval.py tests/test_risk_evidence.py tests/test_agent_tools.py tests/test_quotation_agent.py tests/test_excel_export.py`: 183 passed
- `.venv/bin/pytest -q tests/test_architecture.py`: 76 passed
- `PYTHONPATH=.:src .venv/bin/pytest -q`: 468 passed with one accepted
  Starlette/httpx deprecation warning
- `PYTHONPATH=.:src .venv/bin/python -m evaluation.c17`: PASS report; output is
  one authoritative JSON document
- two in-process serialized evaluation runs: both PASS; byte-identical;
  report SHA-256 `928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`
  (5,283 bytes)
- `.venv/bin/python scripts/reconcile_governance_views.py --write` and
  `--check`: PASS and idempotent
- `bash scripts/test_governance_harness.sh`: 61 PASS / 0 FAIL
- `bash scripts/final_card_state_consistency.sh V1-C17 ACTIVE`: PASS
- `bash scripts/quotation_session_bootstrap.sh`: 127 PASS / 1 expected dirty
  worktree WARN / 0 FAIL; sensitive-filename and credential-pattern scans PASS
- `.venv/bin/pip check`: no broken requirements
- `.venv/bin/python -m compileall -q src evaluation deployment scripts tests`:
  PASS
- `bash -n scripts/*.sh`: PASS
- `git diff --check`: PASS

The first broad `.venv/bin/pytest -q` invocation omitted the repository's
established root path and failed during C15 collection with
`ModuleNotFoundError: deployment`. The canonical `PYTHONPATH=.:src` rerun
passed all 468 tests; no implementation defect was involved.

### 7. Focused Tests

PASS — 35 C17 tests cover dataset integrity, exact metric thresholds,
PASS/FAIL/ERROR semantics, independent fixed oracles, Hit@3, provenance,
zero-reference behavior, typed output, tool/agent/Excel contracts, report
privacy, reproducibility, offline execution, failure injection, and all ten
targeted mutation-equivalent probes. The probes detect: lowering a 100% gate;
raising the 0% unsupported-risk threshold; skipping a case; changing a
denominator; allowing an implementation-derived wrong answer; accepting a
retrieval hit below rank 3; treating report-only data as gating; relabeling
ERROR as PASS; omitting dataset version/hash; and persisting a prohibited raw
field. Caught: 10/10; not caught: 0.

### 8. Relevant Regression

PASS — 183 C04/C05/C06/C07/C09/C10/C12 tests passed; 76 architecture tests
passed; the complete suite passed 468 tests.

### 9. Card Evaluation

PASS — fixed synthetic Golden Dataset version `c17-golden-v1`, SHA-256
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`.
Ten cases were evaluated: calculation 2, historical comparison 2, retrieval 1,
risk evidence 1, structured output 1, tool contract 1, scripted agent 1, and
Excel 1. Results: calculation 2/2; comparison 2/2; retrieval Hit@3 1/1;
evidence/provenance 1/1; unsupported-risk rate 0/3 = 0%; structured output
1/1; tool contract 1/1; agent completion 1/1; Excel 1/1. Latency, Bedrock
usage, and cost are explicitly `NOT_MEASURED_OFFLINE` and report-only. Overall
status: PASS. A second run produced byte-identical authoritative JSON.

### 10. Commercial / Data Invariants

PASS — existing Core arithmetic and comparison owners are evaluated without
duplicating business logic; zero remains explicit; estimated and actual values
remain distinct; retrieval similarity is graded only as Hit@3; historical
identity/provenance is retained; the dataset is marked synthetic at dataset,
record, and quote levels; Excel totals reconcile through C12.

### 11. AI / Provider Validation

PASS — the agent cases use a fixed provider-neutral scripted trace. No live
model, Bedrock adapter, AWS credentials, network, or LLM-as-judge is used.
Model output remains subject to the delivered C10 typed/protocol validation.

### 12. Security Validation

PASS — report construction is allowlisted and rejects prompt/model-response,
reviewer, workbook-byte, request/response-body, credential, token, secret, and
customer-data fields; failure reasons are bounded categories. Tests block
network calls and remove AWS credential/profile environment variables while
the complete evaluation still passes. Architecture tests prove production
modules do not import the separate evaluation owner. Threat-model coverage
includes circular oracles, fixture tampering, dataset/version drift,
denominator/threshold manipulation, silent skipping, synthetic-as-real
misrepresentation, stochastic-judge authority, raw payload leakage,
misleading PASS, production-readiness overclaim, and provenance loss.

### 13. Failures / Blockers

The read-only C17 preflight was BLOCKED by the missing authoritative Roadmap
Exit Gate, missing C09+ verification block, and unresolved oracle, metric,
threshold, non-determinism/trial, cost/repeatability, report, failure/
escalation, live-Bedrock, and architecture-ownership contracts. Human-approved
documentation-only remediation resolves those canonical gaps. No C17
implementation had started at that time.

During implementation, the first focused collection could not import the
root-level offline `evaluation` package because pytest exposes only `src/`.
The focused C17 test module now adds the repository root to its own import path;
global pytest/runtime packaging was not widened. The first CLI evaluation also
showed existing C16 operational log lines before the JSON report. The CLI now
captures those lines during evaluation so stdout is exactly one authoritative
report document without changing production logging. The first broad pytest
command omitted `PYTHONPATH=.:src` and failed during C15 collection; the
canonical rerun passed 468 tests. No blocker remains for independent local
audit. The first bootstrap rerun also returned 126 PASS / 1 WARN / 1 FAIL
because the current `Application Implementation` line had been compacted and
no longer contained a legacy exact prefix required by the smoke check. Restoring
the explicit enumerated current-state line made the next bootstrap pass
127 / 1 expected dirty-tree WARN / 0 FAIL without changing semantic state.

Independent local audit: PASS for the exact candidate identity recorded below;
no implementation findings or blockers. One informational note concerned
the verifier's initial mutation-test methodology only; it was not an
implementation defect and required no remediation. It remains accepted,
non-blocking audit context.

### 14. Exit Gate Evidence

The final C17 Exit Gate is PASS. A fixed inspectable
synthetic dataset has a version and independently checked content hash; exact
independent expected values are not runtime-generated; all nine gating metrics
meet their canonical thresholds; report-only metrics cannot gate; deterministic
reruns are byte-identical; the authoritative JSON contains dataset identity,
metric numerators/denominators/thresholds/status, case results, bounded failure
reasons, and evidence references; privacy constraints pass; no LLM judge,
live Bedrock, AWS, network, or production-runtime dependency exists.
Independent local audit passed; the exact audited candidate was delivered by
PR #51 and clean-main post-merge validation passed. The result supports only
the canonical fixed-synthetic-contract claim, not real-world commercial
correctness or production readiness.

Exit Gate Status: PROVEN / PASS

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent local audit, approved PR #51 delivery,
post-merge validation, and outcome-only completion reconciliation.

### 16. Git Evidence

Audited candidate identity `0b41e981503c02e8dd6143bfd206e6863511a83a15b585b46d4f37ec0e63a83b`; the exact nine-file candidate was staged with an identical index
identity and committed as `a88fdfbe05c6e3ca8fb323557f5e71274bb71163`.
Push: COMPLETED — `origin/card/v1-c17-evaluation-harness` (C17 delivery)
PR: MERGED — #51 — https://github.com/jo-soroush/ai-quotation-intelligence/pull/51
Merge: COMPLETED — `528487dfa7bd49f7411fe644b6407dbd0922a48c` (C17 delivery)
Pushed to `origin/card/v1-c17-evaluation-harness`; PR #51
(https://github.com/jo-soroush/ai-quotation-intelligence/pull/51) merged at
`528487dfa7bd49f7411fe644b6407dbd0922a48c`. Post-merge main was synchronized
at the merge commit with zero ahead/behind and a clean working tree. This
completion reconciliation records observed outcomes; its own commit/PR values
are reported after those Git events rather than self-recorded.

### 17. Known Limitations

The small fixed synthetic dataset proves only the defined repository contracts,
not open-ended retrieval/model quality, real-market commercial correctness, or
production readiness. Tool/agent cases intentionally use C09's delivered C03
synthetic corpus while the compact C17-owned history fixtures grade Core
contracts. Latency, Bedrock usage, and cost are unmeasured/report-only in the
offline baseline. No stochastic or live-model conclusions are made.

Advanced-technique decisions after implementation: deterministic invariants,
contract/integration tests, targeted mutation resistance, failure injection,
adversarial harness-integrity testing, threat modeling, and scripted agent
evaluation were performed. Generated property tests and fuzzing were evaluated
but not added because the small fixed exact schema/oracle suite and explicit
mutation cases cover the material boundary without a new generator/fuzzer.
Differential testing was not added because no genuinely independent second
implementation exists. Concurrency/race testing is not applicable to the
sequential stateless runner. Formal methods are not applicable. Rollback is a
Git restore of the last known-good harness and dataset version/hash; evaluation
performs no production or AWS mutation requiring operational teardown.

### 18. What We Learned

Stable data identity, strict case-count reconciliation, code-owned thresholds,
and explicit report construction are all needed: deterministic fixtures alone
do not prevent skipped cases, denominator drift, circular expectations, or
privacy leakage. A separate root-level owner keeps the harness out of Lambda
and production imports while still allowing it to consume public contracts.

### 19. Completion Evidence

COMPLETE — PR #51 merged at `528487dfa7bd49f7411fe644b6407dbd0922a48c`;
clean-main validation passed (35 focused C17 tests, 468 full pytest tests,
76 architecture tests, Governance Harness 61 PASS / 0 FAIL, reconciliation
PASS, and C17 evaluation PASS). Dataset `c17-golden-v1` SHA-256 remains
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`; the
deterministic report SHA-256 remains
`928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.
Active Card is NONE. C18 remains NOT_AUTHORIZED / NOT_STARTED. No AWS, live
Bedrock, application S3, dependency, implementation, dataset, or evaluation
change occurred during delivery or completion reconciliation.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C17
Learning Documentation Status:
CURRENT

## V1-C18 — Guardrails and Failure Handling

### 1. Card

V1-C18 — Guardrails and Failure Handling

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

V1-C18 delivered via PR #54 and validated on synchronized clean main. Final
C18 Exit Gate PASS; Active Card NONE; C19 remains NOT_AUTHORIZED / NOT_STARTED.

### 4. Human Start Approval

YES

Local C18 implementation and exact-candidate Git delivery authorized and
consumed. A separate Phase 2 approval authorized only the public request
correction requiring `estimated_hours.unit`.

### 5. Files Changed

`PROJECT_CONTROL.md`; `src/ai_quotation_intelligence/api.py`;
`tests/test_api.py`; `tests/test_c18_guardrail_matrix.py`; this Evidence Map;
`CARD_LEARNING_AND_DECISION_LOG.md`. The production change is limited to the
external request boundary; the matrix test protects evidence completeness.

### 6. Commands Run

Pre-fix reproduction: `.venv/bin/pytest -q
tests/test_api.py::test_external_request_rejects_missing_estimated_hours_unit`
(failed as expected: HTTP 200 instead of 422). Phase 2 and Phase 3 then ran
the focused API/schema proof, the exact matrix-integrity tests, directly reused
C02–C16 evidence suites, deterministic failure-injection/adversarial subsets,
isolated source-copy mutation probes A–K, mutation L, full pytest,
architecture, Governance Harness, reconciliation, ACTIVE-state consistency,
bootstrap, pip/compile/secret/diff checks, and the unchanged C17 evaluation.

### 7. Focused Tests

PASS — Phase 2 omitted-unit rejection and explicit-unit acceptance/OpenAPI
requiredness: 2 passed. Phase 3 matrix completeness and omission resistance:
2 passed. No production test was duplicated merely to carry a C18 label.

### 8. Relevant Regression

Directly reused C02–C16 evidence suite: 309 passed. Deterministic failure
injection subset: 42 passed. Adversarial subset: 39 passed. Full pytest: 472
passed. Architecture: 76 passed. Governance Harness: 61 PASS / 0 FAIL. C17
evaluation: PASS; dataset SHA-256
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`;
authoritative report SHA-256
`928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.

### 9. Card Evaluation

PASS — all 15 canonical rows resolved and final PASS; failure injection,
cross-cutting integration, adversarial verification, threat reconciliation,
and targeted mutation resistance all passed locally. This is a local contract
gate, not independent audit, delivery, production readiness, or C19 evidence.

### 10. Commercial / Data Invariants

PASS — missing versus zero, invalid/non-finite values, explicit currency/unit,
deterministic arithmetic/reconciliation, evidence provenance, and approval
authority remain fail closed under the cited direct evidence.

### 11. AI / Provider Validation

PASS — malformed/authority-seeking model output, provider invalidity and
unavailability, unsupported tools/actions, fabricated evidence, and tool
failure remain explicit and cannot create a draft or fallback success.

### 12. Security Validation

PASS — API mass assignment, provider/storage/export error sanitization,
observability allowlisting/redaction, secret/payload exclusion, and bounded
failure mappings passed their direct tests and mutation challenges.

### 13. Failures / Blockers

The C18 read-only preflight was blocked by canonical-documentation gaps; the
human-approved documentation remediation resolved them. C18 was subsequently
authorized and activated. Phase 1 classified 14 states
`EXISTING_EVIDENCE_SUFFICIENT` and identified one proven gap:
`COMMERCIAL_SEMANTICS_UNVERIFIED`, because the public request boundary accepted
missing `estimated_hours.unit` and the domain default supplied `hours`.
Phase 2 added a boundary-local required field and focused regression. Phase 3
completed the all-state local verification without finding another enforcement
gap. Independent audit and Git delivery remain outstanding.

Phase 3 test-construction failure retained: the first run of
`test_c18_matrix_omission_mutation_is_caught` failed because its parser also
treated the earlier canonical-state code block as matrix rows and reported a
duplicate `MISSING_RATE`. This was not a runtime enforcement gap. The parser
was bounded to Markdown table lines beginning with `|`; the focused rerun then
passed, followed by the complete focused/full suites.

### Pre-C18 Canonical Remediation — Contract, Not Execution Evidence

The exact Guardrails §8 state set is:

```text
MISSING_RATE
MISSING_REQUIRED_HOURS
INVALID_COMMERCIAL_VALUE
CURRENCY_MISMATCH
COMMERCIAL_SEMANTICS_UNVERIFIED
DETERMINISTIC_CONFLICT
INSUFFICIENT_EVIDENCE
AI_UNSUPPORTED_CLAIM
AI_INVALID
AI_UNAVAILABLE
AI_BOUNDARY_VIOLATION
COMMERCIAL_INVARIANT_FAILED
EXCEL_RECONCILIATION_FAILED
APPROVAL_REQUIRED
SECURITY_BOUNDARY_VIOLATION
```

C18's primary evidence artifact contains one row per state with the canonical
trigger, owner, expected result, implementation/test evidence, original
classification, C18 action, and final result. Historical classifications are
preserved: 14 `EXISTING_EVIDENCE_SUFFICIENT` and one
`ENFORCEMENT_GAP_REQUIRES_FIX`.

| Canonical state | Trigger | Owning component / layer | Expected result / status | Existing implementation and test/evidence | Evidence classification | C18 action | Final verification result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MISSING_RATE | Required `hourly_rate` absent from a quotation item | C02 domain / C04 deterministic Core | Validation fails before calculation or authoritative quote state | `QuoteItem` required field; `test_missing_hours_or_rate_are_rejected_before_calculation` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| MISSING_REQUIRED_HOURS | Required `estimated_hours` absent | C02 domain / C04 deterministic Core | Validation fails; missing is never zero | `QuoteItem` required field; `test_missing_hours_or_rate_are_rejected_before_calculation` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| INVALID_COMMERCIAL_VALUE | Negative, non-finite, or malformed hours/money | C02 domain models | Typed validation rejects value before arithmetic/state | `test_money_rejects_invalid_values`, `test_negative_inputs_are_rejected_by_c02_models`, `test_non_finite_numeric_inputs_are_rejected_by_c02_models` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| CURRENCY_MISMATCH | Quote items or actual/estimated values use incompatible currency | C02 domain / C04-C06 comparison/retrieval | Explicit validation failure; no conversion or comparison success | `test_mixed_currency_and_empty_quotes_are_rejected_by_c02_models`, `test_actual_cost_currency_mismatch_is_rejected`, `test_incompatible_currency_is_rejected_without_conversion` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| COMMERCIAL_SEMANTICS_UNVERIFIED | External request omits `estimated_hours.unit` | C13 public request schema | HTTP 422 `invalid_request`; no stored/application state; schema advertises required unit | `RequestHours` / `ItemInput`; `test_external_request_rejects_missing_estimated_hours_unit`, `test_external_request_accepts_explicit_estimated_hours_unit` | ENFORCEMENT_GAP_REQUIRES_FIX | BOUNDED_EXTERNAL_SCHEMA_FIX_PLUS_REGRESSION | PASS |
| DETERMINISTIC_CONFLICT | Supplied/model value conflicts with deterministic commercial truth | C04 Core / C09-C10 agent boundary | Deterministic value remains authoritative; conflict rejected/no draft | `test_supplied_total_must_reconcile_with_authoritative_item_costs`, `test_invalid_model_generated_tool_arguments_cannot_override_request`, `test_fabricated_evidence_commercial_claims_and_approval_fail` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| INSUFFICIENT_EVIDENCE | No history, no applicable outcomes, or no validated risk evidence | C06-C07 retrieval/risk; C09-C10 tool/agent | Explicit empty/insufficient result; no match/evidence/draft fabricated | `test_empty_history_is_explicitly_insufficient`, `test_missing_cost_is_insufficient_for_cost_metric`, `test_unavailable_c09_capability_and_missing_evidence_are_explicit`, `test_missing_risk_evidence_remains_visible` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| AI_UNSUPPORTED_CLAIM | Model asserts commercial/risk/approval facts outside validated evidence | C10 quotation agent | INVALID result, no draft or authority promotion | `test_unsafe_model_missing_information_prose_fails_closed`, `test_malformed_or_authority_seeking_model_response_is_invalid`, `test_fabricated_evidence_commercial_claims_and_approval_fail` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| AI_INVALID | Provider/model envelope or structured action is malformed | C08 adapter / C10 agent | Explicit INVALID; no authoritative draft/fallback | `test_missing_or_empty_response_is_invalid`, `test_wrong_content_type_is_invalid`, `test_malformed_or_authority_seeking_model_response_is_invalid`, `test_provider_failures_and_invalid_envelopes_cannot_create_drafts` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| AI_UNAVAILABLE | Provider or required tool raises/unavailable status | C08 adapter / C09 tools / C10 agent | Explicit UNAVAILABLE, sanitized message, no draft | `test_provider_failure_is_unavailable_without_secret_details`, `test_unavailable_c09_capability_and_missing_evidence_are_explicit`, `test_c09_delegated_failure_does_not_leak_exception_detail`, `test_provider_failures_and_invalid_envelopes_cannot_create_drafts` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| AI_BOUNDARY_VIOLATION | Unsupported tool/action, authority override, or invalid tool result/evidence identity | C09 tool resolver / C10 agent | INVALID bounded result; no unsupported execution/final success | `test_fixed_resolver_rejects_future_and_arbitrary_operations`, `test_unknown_deferred_and_future_operations_fail_closed`, `test_malformed_tool_output_is_not_accepted`, `test_prompt_injection_cannot_grant_future_tool_or_approval` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| COMMERCIAL_INVARIANT_FAILED | Quote total/state/provenance fails deterministic validation | C02 domain / C04 Core / C11 review | Reject before review/export/authoritative state | `test_supplied_total_must_reconcile_with_authoritative_item_costs`, `test_historical_quote_rejects_mismatched_provenance`, `test_invalid_start_state_and_false_commercial_total_fail` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| EXCEL_RECONCILIATION_FAILED | Commercial/evidence reconciliation, render, or workbook validation fails | C12 Excel export | Explicit `ExportFailure`; no workbook bytes or success artifact returned | `test_core_reconciliation_failure_blocks_export`, `test_invalid_workbook_and_generation_failure_never_return_partial_success`, `test_reload_validation_rejects_injected_formula_link_or_macro` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| APPROVAL_REQUIRED | Export attempted pending/rejected or transition repeated/invalid/model-authored | C11 review / C12 export / C13 API | Explicit rejection/error; no export or approval impersonation | `test_human_rejection_is_visible_and_not_eligible`, `test_every_repeat_or_opposite_decision_fails`, `test_invalid_action_and_model_text_cannot_impersonate_human`, `test_unreviewed_rejected_and_unsuccessful_results_never_export`, `test_export_still_depends_on_c11_gate` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |
| SECURITY_BOUNDARY_VIOLATION | Mass assignment, fabricated evidence, provider/storage false-success, or sensitive logging/error data | C09/C13/C14/C16 boundaries | Reject or sanitize; no authority/persistence success or sensitive output | `test_top_level_mass_assignment_rejected`, `test_fabricated_risk_evidence_and_counts_are_rejected`, `test_malformed_put_success_never_becomes_stored_artifact`, `test_untrusted_metadata_and_unstructured_message_never_escape`, `test_provider_and_internal_exceptions_are_sanitized` | EXISTING_EVIDENCE_SUFFICIENT | NO_ACTION_REUSE_EVIDENCE | PASS |

Phase 1 classifications and Phase 2 remediation history are preserved. Phase
3 re-read the implementations and assertions behind all 14 reused rows; the
309-test direct suite passed. Failure injection passed 42 tests; adversarial
verification passed 39. Isolated source-copy mutations A–K were all caught by
independent assertions. Mutation L is enforced by
`tests/test_c18_guardrail_matrix.py`: removing one row makes completeness false,
and the live matrix test requires exactly 15 ordered, resolved rows with the
historical 14/1 classifications.

Failure-injection results: invalid commercial input, invalid/unavailable
provider, tool failure, storage failure/malformed success, Excel reconciliation
or render failure, and approval/transition failure all remained explicit; no
false success or fabricated fallback occurred. Cross-cutting propagation from
commercial validation to quote state, provider/tool to agent result, approval
to export, storage provider to typed failure, API failure mapping, and existing
C16 runtime paths to bounded structured events passed.

Threat model reconciliation: silent success, fabricated quotation, commercial
invariant bypass, approval bypass, invalid AI promotion, evidence fabrication,
unsupported action, false storage/export success, provider-error leakage,
secret/payload leakage, partial-state misrepresentation, omitted matrix rows,
and misleading all-pass claims are all directly covered and PASS. Generated
property tests, fuzzing, differential testing, and concurrency/race testing
were evaluated but not added: fixed boundary cases and existing concurrent
transition/context tests are sufficient, no independent differential oracle
exists, and no new shared-mutable implementation was introduced. Formal
methods remain NOT_APPLICABLE.

Rollback remains Git-only: the Phase 2 API change is individually reversible;
there is no migration, persistent-format, deployment, AWS-resource, dependency,
or operational rollback. Bedrock Guardrails remain deferred. No AWS/live
Bedrock action, persistence, policy redesign, dependency, or C17 change occurred.

### 14. Exit Gate Evidence

All 15 rows are complete and final PASS. Direct reused evidence, the Phase 2
schema fix, failure injection, adversarial checks, cross-cutting integration,
threat reconciliation, and 12/12 targeted mutations passed. C17 remained
byte-identical by dataset/report identities; full local validation passed.

Exit Gate Status: PROVEN / PASS — all 15 guardrail rows final PASS; exact
independent audit, delivery, clean-main validation, and completion
reconciliation are recorded.

### 15. CARD_QUALITY_GATE

PASS — exact-identity independent local audit, approved PR #54 delivery,
post-merge validation, and outcome-only completion reconciliation.

### 16. Git Evidence

Audited candidate identity
`f5df6c5c8f18839b3ad0791b7405dbc236fbb996767898b76b13e9c00cba191f`
matched the staged index and committed tree. Delivery commit
`b2a14030d053d49a68501aee3a079c1e22e3bb92` was pushed to
`origin/card/v1-c18-guardrails-failure-handling` and merged through PR #54
(`https://github.com/jo-soroush/ai-quotation-intelligence/pull/54`) as merge
commit `b5006f8d712713d6019ec655d8008032774e23c5`. On synchronized main,
PR: MERGED — #54 — https://github.com/jo-soroush/ai-quotation-intelligence/pull/54
Merge: COMPLETED — `b5006f8d712713d6019ec655d8008032774e23c5`
post-merge full pytest passed (472), architecture tests passed (76),
Governance Harness passed (61 PASS / 0 FAIL), reconciliation and C18 final
state consistency passed, clean bootstrap passed (128 / 0 / 0), and pip,
compile, secret, diff, and unchanged C17 evaluation checks passed. The C17
dataset SHA-256 remains
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`; its
report SHA-256 remains
`928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.
Completion reconciliation records observed delivery and verification results;
its own Git identifiers are reported after their corresponding actions.

### 17. Known Limitations

The evidence matrix is a governance artifact validated by a targeted test, not
a runtime subsystem. C18 proves the delivered deterministic failure contracts;
it does not establish production readiness or universal commercial correctness.
The existing Starlette/httpx deprecation warning remains non-blocking.

### 19. Completion Evidence

COMPLETE — PR #54 merged at
`b5006f8d712713d6019ec655d8008032774e23c5`; synchronized clean-main
validation passed (27 focused API/matrix tests, 2 matrix tests, 472 full
pytest tests, 76 architecture tests, Governance Harness 61 PASS / 0 FAIL,
reconciliation PASS, final C18 state consistency PASS, and C17 evaluation
PASS). All 15 canonical guardrail rows are final PASS. The historical
`COMMERCIAL_SEMANTICS_UNVERIFIED` enforcement gap and its bounded public
request fix remain recorded; Phase 1's 14 sufficient-evidence classifications
remain unchanged. C17 dataset and report identities remain unchanged. Active
Card is NONE; C19 is NOT_AUTHORIZED / NOT_STARTED. No AWS, live Bedrock,
Bedrock Guardrails, dependency, persistence, policy, or deployment change
occurred during delivery or completion reconciliation. This result makes no
universal commercial-correctness or production-readiness claim.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C18
Learning Documentation Status:
CURRENT

### 18. What We Learned

The internal `Hours` default can be useful for existing internal construction,
but reusing that permissive model directly at the public request boundary
silently invents a caller's unit. An API-owned subclass with a required
`unit` field keeps public schema validation strict without changing global
domain semantics. The test first reproduced HTTP 200 before the change, then
proved 422/no stored state, valid explicit input, and OpenAPI requiredness.

### 19. Completion Evidence

NONE

### 20. Recommended State

ACTIVE / IMPLEMENTED AND VERIFIED LOCALLY / READY FOR INDEPENDENT LOCAL AUDIT /
UNDELIVERED / NOT COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C18
Learning Documentation Status:
CURRENT — pre-implementation decisions and Phase 2 implementation learning recorded; remaining C18 learning will be added only as evidence exists

## V1-C19 — Golden Case

### Pre-C19 Canonical Remediation — Documentation Only; Not C19 Execution Evidence

The read-only C19 preflight was BLOCKED: the Roadmap lacked a C19-specific
Exit Gate, the C09+ verification block was missing, and local/live execution,
approval, C17 relationship, scenario identity, artifact format, and retention
were unresolved. Human decisions resolved these contract questions. This
documentation remediation adds the separate C19 Exit Gate and verification
contract while preserving the project-wide Roadmap Final Gate.

The approved execution model is one local, deterministic, repeatable synthetic
Golden Case through existing component contracts. Local FastAPI is exercised;
provider and storage boundaries use deterministic injected clients; approval
uses the existing C11 path with an explicitly synthetic test actor; applicable
existing C16 events are captured locally. Live AWS, Bedrock, S3, CloudWatch,
Lambda, and API Gateway are not required. C13 process-local state remains an
accepted limitation and is not repaired. C17 is not a dependency and remains
unchanged; its existing identities are regression evidence only. C18 remains
a completed prerequisite without duplicating its all-15 matrix.

The unchanged C17 regression identity is dataset version `c17-golden-v1`,
dataset SHA-256 `1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`,
and report SHA-256 `928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.

The contract now requires a fixed synthetic scenario ID/version/SHA, stable
serialization, independently authored expected values, exact once-only
required-step accounting, a bounded machine-readable PASS/FAIL/ERROR report,
two-run normalized reproducibility, ephemeral workbook/report/injected
storage/event artifacts, privacy controls, harness-level failure/mutation/
adversarial proof, Git-only rollback, and a claim bounded to one synthetic
scenario. The C13 process-local limitation is not a C19 deliverable.

No C19 implementation, tests, fixture, report, workbook, or other runtime
artifact was created or executed by this remediation. C19 remains
NOT_AUTHORIZED / NOT_STARTED; no C20 work is authorized. The status and
execution fields below remain NOT_RUN / NOT_PROVEN and are not converted into
PASS by this contract change.

### Documentation-Remediation Validation Evidence (2026-10-05)

- `python scripts/reconcile_governance_views.py --write`: PASS.
- `python scripts/reconcile_governance_views.py --check`: PASS.
- Initial `.venv/bin/pytest -q` invocation stopped during collection because
  the repository `PYTHONPATH=.:src` was not set (`ModuleNotFoundError:
  deployment`). No tests ran in that invocation. Corrected invocation
  `PYTHONPATH=.:src .venv/bin/pytest -q`: 472 passed, one existing
  Starlette/httpx deprecation warning.
- `.venv/bin/pytest -q tests/test_architecture.py`: 76 passed.
- `bash scripts/test_governance_harness.sh`: 61 PASS / 0 FAIL. Its expected
  invalid-fixture argparse diagnostic was emitted during a passing case.
- `bash scripts/quotation_session_bootstrap.sh`: 127 PASS / 1 expected
  dirty-tree WARN / 0 FAIL; secret-bearing filename and obvious credential
  pattern checks passed.
- `.venv/bin/python -m pip check`: no broken requirements.
- `.venv/bin/python -m compileall -q src tests`: PASS.
- `git diff --check`: PASS. No credential/private-key pattern was found in
  the four authorized documents.

These are repository/governance validation results for the documentation
candidate only. They are not C19 Golden Case execution, scenario, component,
cloud, or Exit Gate evidence. No AWS/Bedrock call was made.

### 1. Card

V1-C19 — Golden Case

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

Explicit local deterministic implementation authorization granted on 2026-10-05 for branch `card/v1-c19-golden-case` from `009c281ae26c5d6e59fefbff0add0d511cf58650`. Separate exact-candidate Git delivery authorization was granted and consumed for PR #57. AWS/live Bedrock, production changes, and V1-C20 remain unauthorized.

### 5. Files Changed

Governance: `PROJECT_CONTROL.md`, `QUOTATION_CARD_EVIDENCE_MAP.md`,
`CARD_LEARNING_AND_DECISION_LOG.md`.

Non-production C19 owner: `evaluation/c19.py`,
`evaluation/golden_case_v1.json`, `evaluation/golden_case_v1.sha256`.

Verification: `tests/test_c19_golden_case.py`, `tests/test_architecture.py`.

No `src/`, dependency, deployment, C17, C18, Roadmap, Specification, or
Guardrails file changed.

### 6. Commands Run

- Pre-implementation: full pytest, architecture, Governance Harness,
  reconciliation, bootstrap, and C17 evaluation on exact authorized base.
- `PYTHONPATH=.:src .venv/bin/python -m evaluation.c19` twice: PASS with
  equivalent normalized reports.
- `PYTHONPATH=.:src .venv/bin/pytest -q tests/test_c19_golden_case.py`.
- `PYTHONPATH=.:src .venv/bin/pytest -q tests/test_c19_golden_case.py tests/test_architecture.py`.
- `PYTHONPATH=.:src .venv/bin/pytest -q`.
- `PYTHONPATH=.:src .venv/bin/pytest -q tests/test_architecture.py`.
- `bash scripts/test_governance_harness.sh`.
- C17 evaluation and SHA-256 verification.
- Governance reconciliation/write/check, ACTIVE-state consistency, bootstrap,
  pip, compile/syntax, secret, and diff checks are recorded below after their
  final executions.

### 7. Focused Tests

PASS — 26 C19 tests. They cover fixed fixture identity, independent arithmetic
oracle, complete Golden Flow, two fresh runs, C17 regression, report privacy,
six deterministic boundary failures, no-live-client construction, 13 required
mutation/tamper targets, and duplicate-step integrity.

### 8. Relevant Regression

PASS — full pytest 499 passed (pre-C19 472 + 26 dedicated C19 cases + one new
architecture inventory/boundary case). Architecture 77 passed (pre-C19 76 +
one C19 evaluation-owner case). Governance Harness 61 PASS / 0 FAIL.

### 9. Card Evaluation

PASS — scenario `c19-golden-case-001`, version `c19-golden-v1`, SHA-256
`672c675ed79c98caf0b7cccbf1ea32d908107ec7d0846f56d0c7454c5d822c1e`.
Report schema `c19-golden-report-v1`; normalized authoritative report SHA-256
`c3dc642907993c9658e091755893fdb2b976773bf88b0b4cd3dd9d1ec8fc0312`.
Two independent fresh executions returned PASS and identical normalized
reports; their workbook business/reconciliation summaries were equivalent.
Generated reports, workbook bytes, injected storage state, and captured events
remained ephemeral.

Final local validation: focused C19 26 passed; full pytest 499 passed with one
existing Starlette/httpx deprecation warning; architecture 77 passed;
Governance Harness 61 PASS / 0 FAIL; generated-view reconciliation PASS;
ACTIVE-state consistency PASS; dirty-branch bootstrap 127 PASS / 1 expected
working-tree WARN / 0 FAIL; pip check found no broken requirements;
`compileall` PASS; canonical bootstrap secret/sensitive-name scans PASS; and
`git diff --check` PASS. Nothing is staged.

### 10. Commercial / Data Invariants

PASS — fixed explicit inputs produced independently authored item costs
`1430`, `2625`, and `900` SEK, total `4955` SEK, and 43 estimated hours.
Runtime Core output matched exactly. Synthetic history remained identified;
retrieval returned fixed top IDs `001`, `011`, `021`; the selected comparison
retained quote/source identity and exact 43/54/11-hour values. RiskEvidence
retained three fixed evidence IDs and 40-source provenance. No expected total
is generated by Core at evaluation time.

### 11. AI / Provider Validation

PASS — six fixed calls traversed the real `BedrockConverseAdapter` with an
injected network-incapable client. Five real C09 tools ran in the fixed
sequence history, similarity, comparison, statistics, and risk; the sixth
response was validated structured final output. Invalid/unavailable provider
injections failed closed. AI supplied no arithmetic, evidence identity, or
approval authority. No live Bedrock or LLM judge was used.

### 12. Security Validation

PASS — report construction is allowlisted and rejects prohibited fields.
No credential/token, secret, prompt, raw model response, reviewer ID, workbook
bytes/content dump, request/response body, provider exception, real customer
data, or raw log appears. A test patches both SDK client factories to fail if
called; the Golden Case still passes through injected clients. No live AWS,
S3, CloudWatch, Lambda, API Gateway, or Bedrock action occurred.

### 13. Failures / Blockers

NONE unresolved. Inspect-first discovery found existing interfaces sufficient;
no production integration gap appeared. During implementation, the first
local harness run exposed a harness-only misuse of the dataclass
`VarianceSummary` as a Pydantic model. The harness was corrected to read its
typed fields directly and compute observed overrun rate from actual counts;
the repaired focused and full suites pass. No product defect was found.

### 14. Exit Gate Evidence

| Exit Gate area | Evidence | Result |
| --- | --- | --- |
| Fixed synthetic identity | canonical JSON, explicit ID/version/synthetic marker, sibling SHA | PASS |
| Independent expected values | transparent fixture literals; `13×110 + 21×125 + 9×100 = 4955` | PASS |
| Existing component chain | local FastAPI, Core, retrieval/comparison/statistics, RiskEvidence, C09/C10 | PASS |
| Provider boundary | real Bedrock adapter plus fixed injected client; no network | PASS |
| Human authority | preapproval export 409; real C11 decision route; AI approval false | PASS |
| Excel | real C12 generation, reload, business reconciliation, integrity checks | PASS |
| Storage | real C14 adapter persist/retrieve with injected client and valid derived identity | PASS |
| Observability | existing C16 API/agent/tool/provider/storage events captured and bounded | PASS |
| Report/status/steps | schema v1; 18 fixed steps exactly once; PASS/FAIL/ERROR fail closed | PASS |
| Reproducibility | two fresh app/store/provider/storage/event instances; reports identical | PASS |
| Harness failure injection | provider invalid/unavailable, approval skip, Excel failure, storage false success, missing events | PASS |
| Mutation resistance | 13/13 applicable canonical targets CAUGHT; duplicate step also caught | PASS |
| Adversarial/agent evaluation | no approval bypass, fabricated evidence, invalid output, hidden failure, or authority expansion | PASS |
| Threat/privacy | all 17 canonical C19 threat classes covered; bounded synthetic claim | PASS |
| C17/C18 boundaries | C17 unchanged PASS with exact hashes; C18 regressions in full suite | PASS |
| Scope/rollback | no production/dependency/persistence/cloud change; Git-only rollback; artifacts ephemeral | PASS |
| Full validation | 499 pytest, 77 architecture, Governance Harness 61/0 | PASS |

Required steps (18): fixture identity; FastAPI boundary; Core calculation;
historical retrieval; similar retrieval; historical comparison; deterministic
statistics; RiskEvidence; agent tools; provider adapter; QuotationAgent;
structured-output validation; human approval; Excel generation; Excel reload/
reconciliation; storage adapter; observability; C17 regression. All 18 PASS.

Failure injection: six of six PASS; each generated overall FAIL, never PASS.
Required-step omission and duplication generated report-integrity rejection;
skipped approval and failed Excel reconciliation generated FAIL.

Mutation results: 13 CAUGHT / 0 NOT_CAUGHT / 0 NOT_APPLICABLE. Targets were
required-step omission, failed step marked PASS, approval bypass, fixture
version/SHA weakening, wrong total, fabricated evidence, invalid structured
result, skipped Excel reconciliation, false storage success, omitted
observability evidence, prohibited reviewer identity, scenario tampering
without identity update, and PASS from partial execution.

Threat model: false Golden PASS, skipped step, circular oracle, fixture
tampering, version/SHA drift, commercial mismatch, fabricated evidence, AI
authority expansion, approval bypass, invalid workbook, false storage success,
misleading observability, sensitive leakage, synthetic-as-real overclaim, C17
contamination, accidental live cloud, and hidden C13 limitation are all PASS.

Advanced verification decisions: deterministic invariants, contracts,
integration, mutation resistance, bounded failure injection, adversarial,
threat modeling, agent evaluation, and rollback were performed. Generated
property testing was not selected because C19 owns one fixed case; fuzzing was
not selected because targeted schema/tamper tests cover the small new surface;
differential testing was not selected because no independent implementation
oracle exists; concurrency/race is not applicable to the sequential harness;
formal methods are not applicable.

C17 regression: PASS, dataset version `c17-golden-v1`, dataset SHA-256
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`,
report SHA-256
`928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.

Exit Gate Status: PROVEN — PASS; 18/18 required steps; independent audit PASS;
PR #57 merged; clean-main validation PASS. Claim remains limited to one fixed
synthetic end-to-end Golden Case across existing V1 component contracts.

### 15. CARD_QUALITY_GATE

PASS — exact C19 contract and Exit Gate passed local verification, independent
audit, approved Git delivery, post-merge validation, and completion
reconciliation.

### 16. Git Evidence

Audited candidate identity `c4f1e6bcc0cae35d458350fc8d9d0d11aaf1542b8fea09cbf88b811eba22cf5f` matched staged and committed content. Delivery commit `5c7f048875a01eb66fef2f75d1a5b19d7ff99024` was pushed and merged by PR #57 (`https://github.com/jo-soroush/ai-quotation-intelligence/pull/57`) at merge commit `0d4b4f4daf3d2d3d19c3384fdb2afa3b15831f50`. Clean-main post-delivery validation: focused C19 26 passed; full pytest 499 passed; architecture 77 passed; Governance Harness 61 PASS / 0 FAIL; reconciliation and ACTIVE consistency PASS; bootstrap 128 PASS / 0 WARN / 0 FAIL; C17 regression PASS with unchanged dataset/report hashes; pip, compile, secret-pattern, and diff checks PASS. No CI checks were configured on the PR.

### 17. Known Limitations

- This proves exactly one fixed synthetic local scenario, not production
  readiness, real-market correctness, customer suitability, profitability,
  generalized model quality, production-scale reliability, or certification.
- C13 state remains process-local. The run intentionally keeps one fresh local
  app/store instance per execution and does not claim deployed multi-request
  durability.
- Provider/storage clients and event capture are deterministic local
  injections; C15/C16 remain the separate cloud/deployment evidence.
- Workbook correctness uses exact business/reconciliation semantics rather
  than binary identity.

### 18. What We Learned

The existing owner boundaries compose without production changes. Recording
bounded outputs around real C09 dispatch preserves orchestration evidence
without weakening tool validation, while an explicit fixed step ledger makes
false PASS mechanically detectable. Details and the harness-only dataclass
correction are preserved in the Learning and Decision Log.

### 19. Completion Evidence

COMPLETE / DELIVERED — delivery PR #57 merged at
`0d4b4f4daf3d2d3d19c3384fdb2afa3b15831f50`; clean-main validation passed
(focused C19 26, full pytest 499, architecture 77, Governance Harness 61/0,
reconciliation and final state consistency PASS, bootstrap 128/0/0, C17 PASS).
Scenario `c19-golden-case-001` / `c19-golden-v1` remains SHA-256
`672c675ed79c98caf0b7cccbf1ea32d908107ec7d0846f56d0c7454c5d822c1e`; report
schema `c19-golden-report-v1`, report SHA-256
`c3dc642907993c9658e091755893fdb2b976773bf88b0b4cd3dd9d1ec8fc0312`;
18/18 required steps PASS, commercial result 4,955 SEK / 43 hours, normalized
two-run report equality and workbook business equivalence PASS, failure
injection 6/6, canonical mutations 13/13 CAUGHT, duplicate-step CAUGHT,
independent auditor probes 8/8 CAUGHT, adversarial PASS, agent evaluation
PASS, threat model 17/17 PASS. The bounded claim is: “One fixed synthetic
end-to-end Golden Case passed across the existing V1 component contracts.”

Accepted independent-audit findings remain non-blocking and unremediated:
LOW — `_assemble_report()` contains a redundant unreachable defense-in-depth
completeness guard under the pre-seeded ledger; `validate_report()` is the
load-bearing completeness check and passed isolated source-level mutation.
INFORMATIONAL — numbered Learning Log template sections retain “NOT YET
RECORDED” despite substantive C19 narrative; this is documentation-template
completeness only. Neither finding changes the accepted candidate or result.
No production source, AWS/live Bedrock, real S3, live CloudWatch, dependency,
persistence, C17, C18, or deployment change occurred. C13 process-local state
remains an accepted limitation. C20 remains NOT_AUTHORIZED / NOT_STARTED.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C19
Learning Documentation Status:
CURRENT

## V1-C20 — Demo UI

### 1. Card

V1-C20 — Demo UI

### 2. Contract Source

QUOTATION_CARD_SPECIFICATIONS.md

Roadmap identity and title verified from AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md.

### 3. State

COMPLETE

### 4. Human Start Approval

YES

Explicit V1-C20 local implementation and self-validation authorization was
granted on 2026-10-06 for branch `card/v1-c20-demo-ui` from exact base
`d0c9b9e842b04d7e62f644aaf241acf7781e3c72`. Git delivery, production
backend/API/CORS changes, persistence, authentication, live AWS/Bedrock, and
project-wide V1 finalization were not part of the start approval. Separate
human Git-delivery approval was granted and consumed by PR #61.

### 5. Files Changed

Production backend files: NONE.

Tracked candidate scope: `.gitignore`; `demo/{__init__.py,c20_backend.py}`;
the bounded `frontend/` React/Vite project (source, typed client, tests,
Playwright E2E/configuration, isolated mutation runner, npm manifest/lockfile,
and run instructions); `tests/{test_architecture.py,test_c20_demo_ui.py}`; and
C20 updates in `PROJECT_CONTROL.md`, this Evidence Map, and
`CARD_LEARNING_AND_DECISION_LOG.md`. The bootstrap's filename/credential scans
now prune ignored nested dependency/build/browser trees so C20 `node_modules`
does not create false secret-filename warnings. Generated dependencies, builds, browser
binaries/reports, downloads, caches, and TypeScript build-info are ignored.

### 6. Commands Run

- Verified clean synchronized `main` at
  `d0c9b9e842b04d7e62f644aaf241acf7781e3c72` and created
  `card/v1-c20-demo-ui`.
- Pre-implementation baseline: full pytest 506 passed; architecture 77 passed;
  Governance Harness 61 PASS / 0 FAIL; reconciliation PASS; bootstrap
  128 PASS / 0 WARN / 0 FAIL; C17 evaluation PASS.
- Inspected the exact C20 canonical contract, existing FastAPI/OpenAPI models,
  provider/agent/tool/review/Excel boundaries, synthetic history, tests, and
  delivered pre-C20 API presentation fields.
- Installed the locked npm graph with scripts disabled; 110 packages were
  audited with zero vulnerabilities. Ran strict TypeScript, production build,
  Vitest, isolated mutations, real Chromium success/failure E2E, rendered
  desktop/tablet review, C20 Python contracts, architecture, full pytest, and
  C17/C18/C19 regressions.
- Final governance/static checkpoint: reconciliation write/check PASS;
  Governance Harness 61 PASS / 0 FAIL; bootstrap 127 PASS / one expected dirty
  worktree WARN / 0 FAIL; pip check, Python compilation, shell syntax, bundle/
  diff credential scan, and `git diff --check` PASS.
- Completion reconciliation validation on `maintenance/v1-c20-completion-reconciliation`
  (base `4a3781beb01e4db00e6ff6bda673911011de2cf3`): full pytest 513 passed
  using `PYTHONPATH=.`; C20 composition tests 5 passed; architecture 79 passed;
  C18 tests 2 passed; C19 Golden Case 26 passed; Governance Harness 61 PASS /
  0 FAIL; governance reconciliation write/check PASS; bootstrap 127 PASS /
  1 expected dirty-tree WARN / 0 FAIL; C17 PASS with exact hashes below; pip
  check, compilation, shell syntax, and `git diff --check` PASS. Initial plain
  pytest invocation failed collection because the repository root was absent
  from the import path; the environment-only `PYTHONPATH=.` retry passed.

### 7. Focused Tests

PASS — `npm test`: 3 files / 22 tests. `tests/test_c20_demo_ui.py`: 5 passed.
Coverage includes free-form/preset inputs, explicit hours units, multiple
items, loading/serialization, evidence-vs-AI labels, empty/failure states,
review denial/approval/rejection, export, error sanitization, synthetic and
process disclosures, keyboard focus, and current OpenAPI route/request shapes.

### 8. Relevant Regression

PASS — full pytest 513 passed (baseline 506 + 5 C20 composition/contract tests
+ 2 architecture tests). Architecture 79 passed (baseline 77 + 2). C18 matrix
2 passed. C19 focused 26 passed with 18/18 Golden steps. Exact C17/C19
identities remained unchanged. C17 dataset SHA-256 is
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`; report
SHA-256 is `928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.
C19 scenario SHA-256 is
`672c675ed79c98caf0b7cccbf1ea32d908107ec7d0846f56d0c7454c5d822c1e`; report
SHA-256 is `c3dc642907993c9658e091755893fdb2b976773bf88b0b4cd3dd9d1ec8fc0312`.

### 9. Card Evaluation

PASS — 2 Playwright Chromium tests ran against fresh real Vite/FastAPI
processes. Success covered synthetic input → agent/tools/evidence → backend
approval → genuine backend XLSX download. Failure covered real injected
provider unavailability, HTTP 503, bounded messaging, and no draft UI.

### 10. Commercial / Data Invariants

PASS — explicit `hours` and `SEK` are sent. The browser derives no commercial
or evidence truth. The backend returned `4620 SEK` for the preset
`12×110 + 20×125 + 8×100`; typed evidence was displayed and export stayed
locked until the backend reported approval.

### 11. AI / Provider Validation

PASS — the deterministic client is injected through the real
`BedrockConverseAdapter`; QuotationAgent schema/tool/evidence validation and its
bounded five-tool sequence remain active. No boto client or live Bedrock is
constructed. Provider failure remains explicit and creates no quote.

### 12. Security Validation

PASS — safe React rendering, bounded error allowlist, no browser
storage, no raw provider/reviewer response display, `/api`-only transport, and
no frontend Python/internal import are directly tested. Bundle/diff credential
patterns were absent and npm audit found zero vulnerabilities.

### 13. Failures / Blockers

Repaired failures are preserved. Initial TypeScript/Vitest/Python focused runs
found config, discovery, fixture, and test-construction errors; bounded fixes
reran green. Initial Chromium launch was blocked before page execution by the
macOS sandbox; approved elevated execution then ran the browser. The first real
browser run passed success E2E but found `error ?? message` hid the explicit
no-draft outcome; the banner and tests were corrected and both browser flows
passed. Port 8000 belonged to an unrelated process, so C20 moved to 8765 and
left it untouched. OpenAPI probe assumptions were corrected from `{quote_id}`/
internal `Hours` to `{id}`/public `RequestHours`; the probe then exposed the
pre-existing generic-JSON OpenAPI description for an actually-XLSX export.
Runtime/browser XLSX proof remains authoritative and a backend metadata change
is out of scope. Visual review prompted display-only decimal formatting; Ctrl-C
handling was bounded at the launcher edge. No unresolved blocker remains.

During completion reconciliation, an initial plain pytest invocation failed
collection because this project's pytest configuration adds `src/` but not the
repository root, where `demo/`, `evaluation/`, and `deployment/` live. Running
the same suite with `PYTHONPATH=.` passed all 513 tests. The first candidate
final-state consistency probe also identified two Evidence Map serialization
details required by the validator: an exact `COMPLETE` Learning Documentation
Status token and canonical `PR: MERGED` / `Merge: COMPLETED` Git evidence
labels. These were corrected. The repeat probe passes the governance-state
checks; its remaining failures are the expected non-default branch, missing
upstream, and dirty-tree checks, which can pass only after this candidate is
delivered and the gate is rerun on clean synchronized main.

### 14. Exit Gate Evidence

| C20 Exit Gate area | Direct evidence | Local result |
| --- | --- | --- |
| Stack/strict types/build/dependencies | lockfile, `npm ci`, typecheck, build, zero-vulnerability audit | PASS |
| Existing API/proxy/no backend redesign | OpenAPI probe, typed `/api` client, Vite proxy, architecture tests | PASS |
| No duplicated backend authority | source review, tests, total-substitution mutation caught | PASS |
| Synthetic request/evidence/AI distinction | component tests, browser success, desktop/tablet render review | PASS |
| Human approval and real Excel | composition/browser preapproval gate, backend decision, XLSX download | PASS |
| Truthful representative failures | validation/provider/AI/evidence/review/export/network tests and provider-failure E2E | PASS |
| Browser security/privacy | safe-render/error/storage/import tests, mutations, bundle/diff scan, npm audit | PASS |
| Accessibility/usability/responsive | semantic controls/status/dialog, keyboard/focus tests, two viewport reviews | PASS |
| Test/mutation/prior regressions | 22 Vitest, 2 Chromium, 11/11 applicable mutations, 513 Python, C17/C18/C19 | PASS |
| No cloud/persistence/auth and bounded claim | injected clients, loopback only, visible disclosures, no production source | PASS |

Exit Gate Status: PROVEN — the C20-specific Roadmap Exit Gate is satisfied by
the exact merged implementation candidate, the independent audit disposition
reported for candidate identity
`9ba7309505f18d976c079de9b5635e760fd5ecc97f308ec208ebf17dc49a05a6`, and the
recorded post-merge validation. PR #61 merged at
`4a3781beb01e4db00e6ff6bda673911011de2cf3`. No separate audit report artifact
was found in the repository; the PASS disposition is attributed to the
authorized completion input and is not assigned a fabricated file reference.
This proves the C20 Card Exit Gate only. The separate project-wide Final Gate
audit remains PENDING and Project V1 remains NOT_FINALIZED.

### C20 Exit Gate Completion Evidence Matrix

The detailed Roadmap Exit Gate clauses are grouped below only where one direct
test or artifact proves the same bounded contract. Evidence paths name delivered
source/tests; execution counts are from the recorded PR #61 post-merge run,
not newly claimed as rerun by this governance edit. The independently supplied
audit PASS is not represented as a repository artifact.

| # | Mandatory C20 requirement | Direct evidence | Result / limitation |
| --- | --- | --- | --- |
| 1 | React + TypeScript + Vite frontend and bounded npm stack | `frontend/package.json`, `frontend/package-lock.json`, `frontend/src/` | PASS — approved stack only |
| 2 | Strict TypeScript, typed API requests/responses/errors, production build | `frontend/tsconfig.app.json`, `frontend/src/types.ts`, `frontend/src/api.ts`; PR #61 validation | PASS — strict typecheck and build reported PASS |
| 3 | Existing FastAPI routes/contracts and local `/api` proxy; no backend CORS/API redesign | `frontend/vite.config.ts`, `frontend/src/api.ts`, `tests/test_c20_demo_ui.py::test_frontend_contract_matches_current_fastapi_openapi` | PASS — existing routes; no CORS/backend contract change |
| 4 | No frontend business logic or authoritative commercial arithmetic | `frontend/src/App.tsx`, `frontend/src/components/`, `tests/test_architecture.py`; mutation report | PASS — backend values remain authoritative; total-substitution mutation caught |
| 5 | Synthetic request, multiple items, explicit hours units, visible synthetic disclosure | `frontend/src/demoPreset.ts`, `frontend/src/components/QuoteRequestForm.tsx`, `tests/test_c20_demo_ui.py` | PASS — free-form and preset inputs are synthetic; explicit units used |
| 6 | Backend quote totals displayed without client-side recomputation | `frontend/src/App.tsx`, `frontend/src/types.ts`, successful E2E | PASS — preset result 4620 SEK; no client authority |
| 7 | Comparable historical quotations and similarity signals | `frontend/src/components/EvidencePanel.tsx`, API response fixtures, successful E2E | PASS — backend-returned evidence only |
| 8 | Estimate/actual comparison evidence and variance | `frontend/src/components/EvidencePanel.tsx`, typed API fixtures, successful E2E | PASS — backend projection only |
| 9 | Structured RiskEvidence/provenance and clear separation from AI interpretation | `frontend/src/components/EvidencePanel.tsx`, `frontend/src/App.tsx`, component tests | PASS — deterministic evidence and constrained narrative are distinct |
| 10 | Missing-information, validation, provider and sanitized API/network failures | `frontend/src/api.ts`, `frontend/src/App.test.tsx`, provider-failure E2E | PASS — real provider failure remained HTTP 503 with no draft |
| 11 | Backend-derived review/workflow state; truthful loading, empty, and terminal states | `frontend/src/App.tsx`, `frontend/src/components/ReviewPanel.tsx`, component tests | PASS |
| 12 | Explicit approve/reject through existing backend review route; AI/local UI cannot approve | `frontend/src/components/ReviewPanel.tsx`, composition tests, E2E and mutation probes | PASS — backend response is authoritative |
| 13 | Export remains unavailable when backend denies/pre-approval | `frontend/src/App.tsx`, `frontend/src/components/ReviewPanel.tsx`, E2E | PASS — pre-approval restriction exercised |
| 14 | Actual backend-generated XLSX download after approval; no frontend workbook | C12 export in `demo/c20_backend.py`, `frontend/src/api.ts`, Chromium success E2E | PASS — genuine XLSX download observed; pre-existing generic-JSON OpenAPI description accepted as LOW |
| 15 | Safe rendering; no unsafe HTML, prompts, raw model/provider errors, reviewer identity, or arbitrary payload dumps | React text rendering, `frontend/src/security.test.ts`, component/security tests, mutation probes | PASS — prohibited raw content not rendered |
| 16 | No secrets in bundle and no prohibited sensitive browser storage | package build, secret scan, `frontend/src/security.test.ts`, mutation probes | PASS — no browser storage; bundle scan clean; npm audit had 0 vulnerabilities |
| 17 | Semantic labels, keyboard operation, visible focus, readable status/error feedback | `frontend/src/components/QuoteRequestForm.tsx`, `ReviewPanel.tsx`, component accessibility tests | PASS — no WCAG certification claim |
| 18 | Desktop/laptop/tablet usability and layout review | `frontend/src/styles.css`; recorded desktop/tablet visual review | PASS — possible screenshot-only sticky overlap not reproduced; accepted INFORMATIONAL |
| 19 | Vitest/React Testing Library component and UI tests | `frontend/src/App.test.tsx`, `api.test.ts`, `security.test.ts`; PR #61 validation | PASS — 22 tests |
| 20 | API request/response contract tests against current FastAPI | `frontend/src/api.test.ts`, `tests/test_c20_demo_ui.py::test_frontend_contract_matches_current_fastapi_openapi` | PASS |
| 21 | Real-browser successful request → evidence/draft → approval → Excel flow | `frontend/e2e/demo.spec.ts`; PR #61 Chromium result | PASS — 1 successful real Chromium flow |
| 22 | Real-browser meaningful failure flow | `frontend/e2e/demo.spec.ts`; PR #61 Chromium result | PASS — provider unavailable, no false draft; 1 failure flow |
| 23 | Targeted mutation resistance | `frontend/scripts/mutation-probes.mjs`; PR #61 result | PASS — 11/11 applicable mutations CAUGHT |
| 24 | Bounded failure injection, adversarial checks, and C20 threat review | Python provider-failure composition test, UI failure/E2E tests, 11 mutation probes, supplied independent audit | PASS — bounded C20 scope; no duplicate C18 matrix |
| 25 | No production backend, API, CORS, persistence, auth, cloud, or live AWS changes | merged PR #61 exact file list; `tests/test_architecture.py`; source review recorded in PR | PASS — presentation/composition only; no live AWS/Bedrock/S3/CloudWatch |
| 26 | C13 process-local limitation and maximum claim remain explicit | `frontend/README.md`, UI disclosure, merged Evidence Map §17 and PR #61 description | PASS — local synthetic demo only; no production/multi-instance claim |
| 27 | C17/C18/C19 remain unchanged and regressions pass | C17 hashes below; `tests/test_c18_guardrail_matrix.py`; `tests/test_c19_golden_case.py`; post-merge run | PASS — identities unchanged |
| 28 | Independent audit and delivery/post-merge evidence | exact audited identity; PR #61 merged; GitHub PR body; post-merge validation recorded below | PASS — audit outcome supplied as PASS; no separate audit artifact found |

### C20 Advanced Verification Reconciliation

| Technique | Canonical disposition | Actual evidence / decision | Outcome |
| --- | --- | --- | --- |
| Deterministic invariants | REQUIRED | backend totals/evidence and approval/export ordering asserted in composition, component, and browser tests | PASS |
| Contract tests | REQUIRED | frontend API tests plus OpenAPI-to-frontend contract test | PASS |
| Integration | REQUIRED | real local FastAPI/Vite composition; two Chromium E2E paths | PASS |
| Generated property tests | CONDITIONAL / EVALUATE | no additional transformation invariant beyond explicit typed/request contracts was identified | NOT RUN — justified |
| Targeted mutation resistance | REQUIRED | isolated UI mutation runner | PASS — 11/11 caught |
| Failure injection | REQUIRED, BOUNDED | provider unavailable through real injected backend; validation/review/export/network cases covered in focused tests | PASS |
| Fuzzing | CONDITIONAL / EVALUATE | no custom parser/serializer was introduced | NOT RUN — justified |
| Differential | NOT_APPLICABLE | no independent second frontend implementation exists | NOT APPLICABLE |
| Concurrency/race | CONDITIONAL / EVALUATE | duplicate/stale request behavior considered and bounded by UI state/tests; no shared backend concurrency was added | NOT APPLICABLE beyond tested UI behavior |
| Adversarial testing | REQUIRED, BOUNDED | unsafe-text, authority, fabricated-success, disclosure, evidence, and error mutations | PASS — 11/11 applicable probes caught |
| Threat modeling | REQUIRED | C20 browser/privacy/authority risks mapped and checked in Evidence §§12–14 and independent audit | PASS |
| Agent evaluations | NOT_APPLICABLE for C20 | agent behavior unchanged; C19 remains the existing regression owner | NOT APPLICABLE; C19 rerun PASS |
| Rollback/recovery | REQUIRED | tracked changes are Git-reversible; generated browser/build/download artifacts are ignored/ephemeral; no cloud/data migration | PASS |
| Formal methods | NOT_APPLICABLE | disproportionate for this presentation layer; contracts, E2E, and mutations supply proportionate checks | NOT APPLICABLE |

### 15. CARD_QUALITY_GATE

PASS — implementation narrative, decisions, alternatives, technology
rationale, preserved failure/root-cause/fix history, tradeoffs, completed
learning, future reminder, later-Card impact, and evidence references are
current in the Learning Log. Independent audit PASS and delivery are reconciled.

### 16. Git Evidence

Implementation branch `card/v1-c20-demo-ui`; exact base
`d0c9b9e842b04d7e62f644aaf241acf7781e3c72`; audited candidate identity
`9ba7309505f18d976c079de9b5635e760fd5ecc97f308ec208ebf17dc49a05a6`.
Delivery commit: `b345b1c29dfb028bc8d1b5767c3f17d9956d209e`.
PR: MERGED — #61 — https://github.com/jo-soroush/ai-quotation-intelligence/pull/61
Merge: COMPLETED — `4a3781beb01e4db00e6ff6bda673911011de2cf3`.

Completion-reconciliation candidate: branch
`maintenance/v1-c20-completion-reconciliation`, base
`4a3781beb01e4db00e6ff6bda673911011de2cf3`; exact governance candidate
identity is generated after validation. Nothing is staged, committed, or
pushed by this reconciliation task. The final-state consistency run on clean
synchronized main remains required after delivery.

### 17. Known Limitations

- C13 state remains process-local, single-process, and non-durable.
- Deterministic injected provider transport is not a live-model claim.
- One Chromium engine; no cross-browser or accessibility-certification claim.
- Export OpenAPI metadata says generic JSON while runtime returns proven XLSX.
- Existing Starlette/httpx TestClient deprecation warning remains unrelated.
- Accepted LOW audit finding: pre-existing OpenAPI metadata describes XLSX
  export as generic JSON; runtime XLSX download passed and the metadata was not
  changed.
- Accepted INFORMATIONAL audit note: possible tablet full-page sticky-header
  overlap was not reproduced as an interactive defect and was not changed.
- Claim remains limited to a professional local synthetic demonstration.

### 18. What We Learned

CURRENT — see the full C20 narrative in `CARD_LEARNING_AND_DECISION_LOG.md`.

### 19. Completion Evidence

Implementation delivery is verified: PR #61 is MERGED at
`4a3781beb01e4db00e6ff6bda673911011de2cf3`, with delivery commit
`b345b1c29dfb028bc8d1b5767c3f17d9956d209e` and the audited identity recorded
above. Independent audit disposition PASS (no separate audit file exists in
the repository; see §14). Recorded post-merge validation is PASS: full Python
513, architecture 79, Harness 61/0, reconciliation PASS, bootstrap 128/0/0,
TypeScript/build PASS, Vitest 22, Chromium 2, mutations 11/11, and C17/C18/C19
regressions PASS. This governance-only completion candidate records
C20 COMPLETE / DELIVERED and Active Card NONE, subject to its own authorized
delivery. The final runtime consistency gate has NOT YET PASSED; it must be
run on synchronized clean main after this candidate is delivered. Project V1
remains NOT_FINALIZED; the separate project-wide Final Gate audit is PENDING.

The candidate consistency probe reports 26 governance-state PASS checks. Its
only remaining failures are runtime Git requirements: current branch must be
default `main`, a synchronized upstream must exist, and the working tree must
be clean. This expected pre-delivery FAIL is not recorded as the final gate;
the final gate must be rerun after authorized completion-reconciliation
delivery.

### 20. Recommended State

COMPLETE
Learning / Decision Log:
CARD_LEARNING_AND_DECISION_LOG.md → V1-C20
Learning Documentation Status:
COMPLETE
Implementation, alternatives, technology rationale, preserved failures/root
causes/fixes, tradeoffs, learning, future reminders, and later Card impact are
recorded from actual implementation and delivery evidence.

### Pre-C20 Canonical Remediation — Approved Contract Decisions (2026-10-05)

Read-only C20 preflight was BLOCKED: the Roadmap had no C20-specific Exit
Gate; the Specification referred to a nonexistent Roadmap Exit Gate; the C09+
verification block was missing; the boundary between already-proven backend/
cloud completion and portfolio/project finalization was unclear; and frontend
stack, local/deployed execution, AWS/CORS, browser security/privacy, and claim
boundaries were unresolved. Human decisions recorded by this documentation-only
remediation resolve those questions; they do not authorize or start C20.

Canonical contract now specifies React + TypeScript + Vite/npm, strict and typed
frontend contracts, Vitest + React Testing Library + bounded Playwright, and a
local synthetic portfolio demo through the Vite `/api` proxy to existing
FastAPI contracts. No backend/CORS/API change, AWS/frontend hosting, live
Bedrock, authentication platform, persistence, or production business logic is
authorized. One UI-owned synthetic preset is optional; C19 is not a runtime
dependency. C13 process-local state remains an accepted limitation. C20 has a
dedicated Exit Gate distinct from the project-wide Final Gate; after C20
delivery/reconciliation, a separate project-wide Final Gate audit is required
before project completion may be claimed.

Remediation scope is documentation only. No implementation, frontend files,
package manifest, dependency installation, tests, fixtures, AWS, or Bedrock
activity occurred. Live PROJECT_CONTROL state remains untouched: Active Card
NONE; C20 NOT_AUTHORIZED / NOT_STARTED. No implementation or validation result
is asserted by this contract record.

### Pre-C20 API Presentation Contract Remediation — Local Candidate (2026-10-06)

The independently identified C20 implementation-readiness gap was confirmed:
the existing agent computed and validated similar quotations, historical
comparisons, and full RiskEvidence reports but discarded those typed results,
while `AgentResult.message` was stored but omitted from `GET /quotes/{id}`.
Human approval selected Option C: retain those already-produced results and
expose a minimal safe projection through the existing retrieval route. This is
a separate maintenance remediation; C20 remains NOT_AUTHORIZED / NOT_STARTED.

Implementation is bounded to
`src/ai_quotation_intelligence/{domain/models.py,quotation_agent.py,api.py}`.
`AgentResult` now has optional tuple-backed presentation snapshots for similar
quotes, historical comparisons, and risk-evidence summaries. Each risk summary
reconciles count/rate/statistic values to its typed `RiskEvidence`, requires
unique bounded provenance, and failure results reject presentation evidence.
`QuotationAgent` captures only the current request's successfully validated
`SimilarQuotesOutput`, `ComparisonsOutput`, and `RiskEvidenceOutput` after the
existing single tool invocation. It neither changes the tool loop nor invokes
a tool again. The existing final evidence-ID check remains the authority for
model-selected evidence.

`GET /quotes/{id}` additively exposes `message`, `similar_quotes`,
`comparisons`, and `risk_evidence` through explicit typed allowlisted transport
models. Existing quote/request/status/review/draft fields and POST response
shapes remain unchanged. Raw tool wrappers, prompts, provider output,
exceptions, credentials, reviewer identity, and unrelated history are not
projected. `LocalQuoteStore`, routes, requests, review/approval, Excel,
persistence, dependencies, CORS, provider behavior, arithmetic, and business
authority are unchanged.

Tests added only in `tests/{test_domain_models,test_quotation_agent,test_api}.py`.
They prove additive legacy construction and JSON round-trip; typed capture is
exactly equal to the already-executed tool outputs; the successful five-tool
trace is unchanged and has no second invocation; malformed typed output and
fabricated evidence fail closed; failure results contain no presentation
snapshot; GET returns the bounded projection and stored permitted message;
POST shape and exact route set remain stable; and distinct request evidence
does not mix. Existing C11/C12 mutation and reconciliation tests confirm review
and export authority remain unchanged.

Observed local evidence: domain 15 passed; quotation-agent 58 passed; API 27
passed; combined domain/agent/API/review/Excel 192 passed; full pytest 506
passed; architecture 77 passed; C18 matrix 2 passed; C19 Golden Case 26 passed.
C17 evaluation PASS retained dataset SHA-256
`1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`
and report SHA-256
`928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.
C19 retained scenario SHA-256
`672c675ed79c98caf0b7cccbf1ea32d908107ec7d0846f56d0c7454c5d822c1e`
and report SHA-256
`c3dc642907993c9658e091755893fdb2b976773bf88b0b4cd3dd9d1ec8fc0312`.
The sole observed warning is the pre-existing Starlette/httpx TestClient
deprecation warning.

Governance Harness passed 61/0; generated-view reconciliation passed; the
maintenance-branch bootstrap returned 127 PASS / one expected dirty-tree WARN /
zero FAIL. `pip check`, Python compilation, shell syntax, changed-diff secret
scan, and `git diff --check` passed. The completed-C19 final-state helper passed
all canonical state/evidence checks and, as designed, did not return its clean-
main PASS while this uncommitted maintenance branch was active (non-main branch,
no upstream, dirty tree). No C19 state contradiction was found and
`PROJECT_CONTROL.md` remains untouched.

Twelve isolated source-copy mutations were executed and all were CAUGHT by
load-bearing tests: wrong comparable identity; wrong variance; wrong risk
statistics; fabricated evidence ID; missing source provenance; cross-request
evidence mixing; repeated tool invocation; unvalidated typed evidence
promotion; evidence attached to failure; raw provider field exposure; stored
message omission; and approval/export bypass. Temporary mutation copies were
removed and never altered the candidate. Failure injection through existing
malformed-tool/provider/API/review/export tests remained explicit and
sanitized. Threat/adversarial review found no new authority, raw payload
exposure, cross-request contamination, or false-success path.

Generated property testing was not used because the fixed typed invariants are
covered directly. Fuzzing was not used because no parser was introduced.
Differential verification was not used because there is no independent
implementation oracle. Concurrency received existing C13 decision/isolation
regression only; the remediation introduces no new shared state. Rollback is
Git-only. No AWS, live Bedrock, new dependency, persistence, C17/C18/C19
artifact change, or frontend implementation occurred. This candidate remains
uncommitted and requires independent audit and separate delivery approval.

## 17. Current Card Table

<!-- BEGIN GENERATED: CURRENT_CARD_TABLE -->
DO NOT EDIT THIS BLOCK MANUALLY. Generated by scripts/reconcile_governance_views.py.
| Card | Title | State | Start Approved | Focused Tests | Exit Gate | Quality Gate | Evidence | Recommended State |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V1-C01 | Repository Baseline | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C02 | Domain Models | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C03 | Synthetic Historical Data | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C04 | Quote Calculation Engine | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C05 | Historical Comparison Engine | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C06 | Similar Quote Retrieval | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C07 | Risk Evidence Engine | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C08 | Amazon Bedrock Integration | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C09 | Agent Tools | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C10 | Quotation Agent | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C11 | Human Review Gate | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C12 | Excel Generation | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C13 | FastAPI Application | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C14 | Amazon S3 Integration | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C15 | AWS Deployment | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C16 | CloudWatch Observability | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C17 | Evaluation Harness | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C18 | Guardrails and Failure Handling | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C19 | Golden Case | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
| V1-C20 | Demo UI | COMPLETE | YES | PASS | PROVEN | PASS | PRESENT | COMPLETE |
<!-- END GENERATED: CURRENT_CARD_TABLE -->

## 18. Current Summary

<!-- BEGIN GENERATED: CURRENT_SUMMARY -->
DO NOT EDIT THIS BLOCK MANUALLY. Generated by scripts/reconcile_governance_views.py.
Project Phase: V1_C20_COMPLETE
V1-C01: COMPLETE
V1-C02: COMPLETE
V1-C03: COMPLETE
V1-C04: COMPLETE
V1-C05: COMPLETE
V1-C06: COMPLETE
V1-C07: COMPLETE
V1-C08: COMPLETE
V1-C09: COMPLETE
V1-C10: COMPLETE
V1-C11: COMPLETE
V1-C12: COMPLETE
V1-C13: COMPLETE
V1-C14: COMPLETE
V1-C15: COMPLETE
V1-C16: COMPLETE
V1-C17: COMPLETE
V1-C18: COMPLETE
V1-C19: COMPLETE
V1-C20: COMPLETE
Active Card: NONE
Completed Cards: V1-C01, V1-C02, V1-C03, V1-C04, V1-C05, V1-C06, V1-C07, V1-C08, V1-C09, V1-C10, V1-C11, V1-C12, V1-C13, V1-C14, V1-C15, V1-C16, V1-C17, V1-C18, V1-C19, V1-C20
No later Card is authorized.
Detailed technical evidence remains in the exact Card sections above; this summary is derived and non-authoritative.
<!-- END GENERATED: CURRENT_SUMMARY -->

## Final V1 Project-Wide AWS Evidence Re-verification — 2026-10-06

Source: human-supplied execution report titled “Final V1 live AWS evidence
re-verification,” reporting a separately authorized read-only verification by
Codex GPT-6 Luna — Medium. The detailed attributed operational record is in
`PROJECT_CONTROL.md` §13. The original CLI/API output and a durable raw audit
artifact were not retained or available to the documentation reconciliation
agent; no AWS calls or independent reproduction were performed for this entry.

Bounded Final Gate evidence classification from the supplied report:

| Project-wide Final Gate row | Reported evidence | Classification / limit |
| --- | --- | --- |
| `cloud deployment works` | Reported healthy CloudFormation/Lambda/API configuration and one SigV4-signed `/health` request returning HTTP 200 with `{"status":"ok"}` | **REPORTED PASS, bounded to deployment/resource health and one signed health request**; no full cloud quotation workflow or live Bedrock inference was exercised |
| `observability works` | One structured successful API health event was observed in CloudWatch and associated with the request by timestamp/invocation window | **REPORTED PASS, bounded to the health path**; direct request-ID correlation and all-path/failure observability were not established |

The report states that no AWS mutation, deployment, live Bedrock call, object
listing/access, or full quotation workflow occurred. Its observations describe
the reported verification time only and do not certify continuing cloud
health. These two classifications do not pass the complete Project-Wide Final
Gate or declare V1 finalized. They supplement, and do not rewrite, the
historical C15 deployment and C16 observability records above.

## 19. Final V1 Project-Wide Exit Gate Reconciliation — Phase 1 Candidate

Candidate state: **INDEPENDENTLY AUDITED — PASS** — project-wide Final Gate
reconciliation only; formal V1 closure remains separate and not yet completed.
C01–C20 remain COMPLETE / DELIVERED; Active Card is NONE; Project V1 remains
NOT_FINALIZED. Formal closure still requires separate Git delivery
authorization, delivery, and the authorized post-delivery project-state
reconciliation.

The independently audited artifact is the twelve-row reconciliation delivered
by PR #64 (merge `eea2a69c23fc7ea2526aebc0150beb410c9a8a83`), with
disposition **INDEPENDENTLY AUDITED — PASS**; subsequent corroborating
repository context is `main` at `312c2c20049265c15875f71351a418ddf7ad76f0`
after PR #65 and PR #66.

The canonical gate is the twelve-line checklist under `### Final Gate` in
`AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md` §1294. Wording below is reproduced
from that checklist. Evidence classes distinguish this Phase 1 local execution
(06 October 2026), prior independent audits, retained Card records, and the
human-supplied 2026-10-06 AWS execution report. A row PASS means the bounded V1
contract named by the canonical row is supported; it does not expand the
project's production-readiness claim.

| # | Exact Final Gate wording | Implementation and verification evidence | Governance / delivery evidence and class | Limitations | Assessment |
|---|---|---|---|---|---|
| 1 | all required functionality works | `src/ai_quotation_intelligence/` provides domain/Core, synthetic history, calculation, comparison, retrieval, risk, agent/tools, Bedrock adapter, API, review, Excel, and S3 boundaries. `deployment/` owns the bounded Lambda/API configuration. `demo/c20_backend.py` and `frontend/src/` provide the local demo. Phase 1: full pytest 513 passed; real local Chromium E2E 2 passed through draft, evidence, approval, and XLSX export plus provider-failure flow. | C01–C20 delivery records in §§647–4015; C20 PR #61 and completion PR #62; current README delivered in PR #63. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | Functional claim is limited to implemented V1 contracts, synthetic local demo, and the separately bounded AWS health check. It is not universal correctness, live cloud quotation workflow, or production readiness. | **PASS** — component, API, workflow, and local browser evidence cover the required V1 functionality. |
| 2 | all critical tests pass | Phase 1: full Python suite 513 passed; architecture 79 passed; C20 composition 5 passed; C18 focused matrix 2 passed; C19 focused suite 26 passed; Vitest 22 passed; npm audit zero vulnerabilities; strict TypeScript typecheck and production build passed; Governance Harness 61/0. | Card-specific test records and merged delivery evidence, including PRs #54, #57, #61–#63. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | No test suite proves arbitrary production behavior. C20 has one primary browser engine. The Starlette/httpx deprecation warning is pre-existing and non-blocking. | **PASS** — required local regression and gate suites completed successfully. |
| 3 | Golden Case passes | `evaluation/c19.py`, fixed scenario `c19-golden-case-001`, version `c19-golden-v1`; Phase 1 reran two executions with identical normalized report, all 18 required steps PASS. Scenario SHA-256 `672c675ed79c98caf0b7cccbf1ea32d908107ec7d0846f56d0c7454c5d822c1e`; report SHA-256 `c3dc642907993c9658e091755893fdb2b976773bf88b0b4cd3dd9d1ec8fc0312`. | C19 Exit Gate evidence and PR #57 delivery in this map §V1-C19; independent audit and clean-main delivery record. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | One fixed, deterministic, synthetic Golden Case only; it does not prove broad production readiness. | **PASS** — current execution reproduced the canonical identities and 18/18 result. |
| 4 | agent uses tools correctly | `src/ai_quotation_intelligence/agent_tools.py`, `quotation_agent.py`, typed provider boundary in `bedrock.py`; `tests/test_agent_tools.py`, `tests/test_quotation_agent.py`; C17 `agent-scripted-001` and `tool-risk-hours-001`; C19 agent trace. | C09/C10 evidence §§1445/1642; C17 evaluation §2896; C19 evaluation §3410; PRs #25/#26/#28 and #57. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | The local C17/C19 and C20 demo use scripted deterministic provider behavior. Historical Bedrock smoke evidence is separate and does not mean the deployed Lambda ran model inference. | **PASS** — bounded tool protocol, ordering, and validation are covered by unit, evaluation, integration, and Golden Case evidence. |
| 5 | risk output is evidence-grounded | `src/ai_quotation_intelligence/risk_evidence.py`, `agent_tools.py`, and `quotation_agent.py` retain evidence identity and provenance; tests `test_risk_evidence.py`, `test_agent_tools.py`, `test_quotation_agent.py`; C17 provenance/unsupported-risk metrics and C19 evidence references. | C07/C09/C10, C17, C18 and C19 records in this map; C18's 15-state guardrail evidence reports all rows PASS. **FRESHLY_EXECUTED** via full/focused regressions and C17/C19; **PREVIOUSLY_INDEPENDENTLY_AUDITED**; **HISTORICAL_RETAINED**. | Evidence is synthetic historical data; risk indicators do not predict future outcomes or establish certainty. | **PASS** — risk suggestions require validated, resolvable evidence; unsupported-risk rate in fixed C17 evaluation is 0/3. |
| 6 | commercial calculations are deterministic | `src/ai_quotation_intelligence/calculation.py` owns item/quote arithmetic using `Decimal`; comparison/statistics are deterministic backend owners. `tests/test_calculation.py`, `test_comparison.py`; C17 calculation cases 2/2 PASS. | C04–C07 and C17 records; commercial guardrails G01–G10/G20–G24; C18 all-15 gate. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | Determinism is subject to validated inputs and explicit unit/currency semantics; this does not prove real-market pricing accuracy. | **PASS** — frontend/model cannot own authoritative totals; deterministic code validates and calculates them. |
| 7 | human approval is enforced | `src/ai_quotation_intelligence/human_review.py` and `api.py`; `tests/test_human_review.py`, `test_api.py`, C20 composition tests and real-browser approve/reject flow. Export before approval is blocked by the backend; the browser test downloads XLSX only after backend approval. | C11 evidence §1765, C13 API evidence §2156, C20 evidence §3721 and PR #61; guardrail G16. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | The demo has no authentication platform and does not claim multi-user identity assurance. Human authority is enforced at the existing backend review boundary. | **PASS** — explicit review route controls state; AI and UI state do not grant approval. |
| 8 | Excel output is valid | `src/ai_quotation_intelligence/excel_export.py` produces approved workbooks and reconciles business values; `tests/test_excel_export.py`, C17 `excel-approved-001`, C19 workbook reload/reconciliation, and actual browser XLSX download. | C12 and C19 evidence; C20 E2E/PR #61; accepted audit finding records the pre-existing generic-JSON OpenAPI metadata mismatch while runtime XLSX succeeds. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | OpenAPI export metadata still advertises generic JSON rather than runtime XLSX (accepted LOW); runtime XLSX bytes, gating, and reconciliation are tested. | **PASS** — backend export is approval-gated and workbook values reconcile. |
| 9 | cloud deployment works | Historical C15 template/package/deployment evidence plus C15 independent live verification records; reported 2026-10-06 CloudFormation/Lambda/API state and one SigV4-signed `/health` HTTP 200, recorded in PROJECT_CONTROL.md §13 and this map's AWS evidence entry. | C15 PR #45/clean-main completion evidence; C16 retained deployed state; current supplied report provenance described above. **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**, **REPORTED_AWS_EVIDENCE**. | 2026-10-06 observations are report-derived: raw CLI/API output and a durable raw audit artifact were not retained. Proves resource/configuration health and one signed health request at that time only; not full quotation inference, Lambda Bedrock, public UI, multi-user persistence, or continuing health. | **PASS, BOUNDED / REPORTED** — the V1 deployment-health claim has retained C15 evidence and attributed current health-path report evidence. |
| 10 | observability works | `src/ai_quotation_intelligence/logging_config.py` and API/agent/tool/provider event paths; `tests/test_observability.py`; C16's retained independently verified structured health event; 2026-10-06 report of a fresh structured `api_request` health success event with timestamp-window correlation. | C16 PR #48 and independent historical verification; PROJECT_CONTROL.md §13 report-derived entry; this map's AWS evidence section. **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**, **REPORTED_AWS_EVIDENCE**. | The new reported event was correlated by time/invocation window, not request ID; raw output is unavailable. Evidence covers health path and configured logging, not every route/failure path or comprehensive monitoring. | **PASS, BOUNDED / REPORTED** — retained C16 event evidence plus attributed health-path event report support the established scope. |
| 11 | evaluation suite runs successfully | `evaluation/c17.py`, `evaluation/c19.py`, C18 15-state matrix and focused regression. Phase 1 freshly executed C17 PASS with dataset SHA `1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b` and report SHA `928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`; C18 focused 2 passed; C19 18/18 PASS with expected scenario/report hashes. | C17/C18/C19 evidence §§2896/3135/3410; deliveries PRs #51/#54/#57 and clean-main validations. **FRESHLY_EXECUTED**, **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | C17's cost, latency, and live Bedrock use are explicitly not measured offline. C19 is one synthetic case; C18 checks defined guardrails, not every possible failure. | **PASS** — all delivered evaluation and guardrail programs ran with their fixed expected identities. |
| 12 | README explains architecture and limitations | Delivered root `README.md` covers C01–C20, component boundaries, local setup, tests/evaluations, AWS scope, synthetic data, approval, limitations, and bounded claims; reviewed against implementation and canonical records. PR #63 delivered audited README/AWS traceability candidate; independent re-audit marked this row PASS. | PR #63 merge `723b920b380e65a0497b70e17fa764f9c72867b6`; README review/re-audit evidence in current delivery history. **FRESHLY_EXECUTED** (content review), **PREVIOUSLY_INDEPENDENTLY_AUDITED**, **HISTORICAL_RETAINED**. | `deployment/README.md` retains one pre-delivery C15 planning sentence that calls C15 ACTIVE/UNDELIVERED; current PROJECT_CONTROL and root README give delivered status and explain the bounded deployment. This is a non-blocking subordinate documentation limitation and is not treated as current state. | **PASS** — root README matches the delivered architecture and states material limits; its AWS claims link to attributed §13 provenance. |

### Evidence class and overall disposition

- **FRESHLY_EXECUTED (2026-10-06):** 513 Python tests; 79 architecture;
  five C20 composition; two C18; 26 C19; C17 and C19 deterministic evaluations
  and hashes; 29/29 C20 final Card-state assertions on clean main; Harness
  61/0; reconciliation; clean-main bootstrap 128/0/0; pip/syntax/shell/secret
  checks; npm install/audit, typecheck/build, 22 Vitest, 11 applicable UI
  mutation probes caught, and two real Chromium E2E tests. These were executed
  in the immediately preceding Phase 1 session before this branch was created.
- **PREVIOUSLY_INDEPENDENTLY_AUDITED:** exact delivered candidates for C17–C20,
  README/AWS traceability PR #63, and retained C15/C16 verification, as cited
  in their Card/delivery records. The C20 audit PASS disposition is recorded
  as supplied outcome evidence; no separate audit artifact is claimed.
- **HISTORICAL_RETAINED:** the delivered C01–C20 implementation, Card tests,
  prior PR/merge evidence, C15 deployment and C16 observability records.
- **REPORTED_AWS_EVIDENCE:** only the separately authorized 2026-10-06 report
  for current resource metadata, one signed health request, and a structured
  health event; source and artifact limits remain in PROJECT_CONTROL.md §13.
- **Overall candidate recommendation:** all twelve canonical rows are PASS
  within the explicitly bounded V1 scope. Cloud deployment and observability
  are PASS only at the health/resource scope and retain the report-derived
  classification. No full cloud quotation workflow or live Lambda Bedrock
  inference was verified. Formal Final Gate closure remains PENDING independent
  final audit and approved delivery; Project V1 is NOT_FINALIZED.
