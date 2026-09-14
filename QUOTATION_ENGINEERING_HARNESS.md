# AI Quotation Intelligence System — V1 Engineering Harness

Status: CANONICAL GOVERNANCE HARNESS
PROJECT_CONTROL.md is the sole owner of live operational state and authorization.
The execution metadata below is procedural context, not an independent state ledger.

## 1. Role of This File

QUOTATION_ENGINEERING_HARNESS.md defines how one authorized Card is executed safely from start to completion.

It owns:

- execution sequence;
- CONTENT_ALIGNMENT_GATE;
- SOURCE_ADAPTATION_GATE when external-source relevance exists;
- inspect-before-write behavior;
- Contract Map;
- Risk Map;
- ROADMAP_ALIGNMENT_GATE;
- bounded implementation;
- validation ladder;
- failure handling;
- evidence updates;
- checkpoints;
- CARD_QUALITY_GATE;
- Card completion control;
- STOP behavior.

It does not own:

- architecture;
- Roadmap order;
- live project state;
- detailed Card contracts;
- implementation evidence;
- commercial/data policy;
- Git policy itself.

Ownership:

PROJECT_PROFILE.md → architecture and invariants.
PROJECT_CONTROL.md → sole live operational state and authorization.
Git commands → current runtime Git facts.
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md → Card identity and order.
QUOTATION_CARD_SPECIFICATIONS.md → detailed Card contracts.
QUOTATION_CARD_EVIDENCE_MAP.md → implementation evidence.
CARD_LEARNING_AND_DECISION_LOG.md → engineering rationale, alternatives, failure/root-cause/fix narrative, technology rationale, lessons learned, and future-maintainer reminders.
SOURCE_ADAPTATION_TRACEABILITY.md → external-source study/adoption decision, license awareness, what was and was not taken, changes, risks, Card linkage, and evidence/learning linkage.
GOVERNANCE_HARNESS_PROOF_CASES.md → formal governance proof scenarios; not executed-test evidence.
COMMERCIAL_AND_DATA_GUARDRAILS.md → commercial/data/AI invariants.
GIT_WORKFLOW.md → Git delivery procedure once migrated.
AGENTS.md → coding-agent router.

This file does not authorize implementation.

`scripts/quotation_session_bootstrap.sh` is a SESSION / REPOSITORY SMOKE CHECK.
It answers whether the repository can be safely inspected or resumed. Its
result is not pytest evidence, Exit Gate proof, CARD_QUALITY_GATE proof, or
FINAL_CARD_STATE_CONSISTENCY_GATE proof.

`scripts/test_governance_harness.sh` is the executable governance regression
runner. It uses temporary fixture copies and does not replace Card validation,
the Exit Gate, or the formal proof-case contract.

`scripts/governance_fixture_builder.py` constructs explicit temporary
governance scenarios for those tests. It may reuse current script
implementations, but never uses the live repository lifecycle or current HEAD
as fixture semantic truth.

### Governance Regression Fixture Independence

Governance regression fixtures may reuse the current implementation of the
governance scripts, but each fixture must explicitly construct its own
Roadmap-aligned lifecycle state. Fixtures must not infer completed Cards,
Active Card, authorization, or semantic state from the live repository,
current HEAD, PR number, or merge commit. Fixture Git setup must keep all
diagnostics separate from path/control values and must fail immediately when
required initialization fails.

For active Card execution, context-loss recovery, and safe resume, read the canonical files in this order:

~~~text
AGENTS.md
PROJECT_PROFILE.md
PROJECT_CONTROL.md
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md
QUOTATION_CARD_SPECIFICATIONS.md
QUOTATION_CARD_EVIDENCE_MAP.md
CARD_LEARNING_AND_DECISION_LOG.md
QUOTATION_ENGINEERING_HARNESS.md
SOURCE_ADAPTATION_TRACEABILITY.md when external-source relevance exists
GOVERNANCE_HARNESS_PROOF_CASES.md when reviewing governance proof scenarios
COMMERCIAL_AND_DATA_GUARDRAILS.md
GIT_WORKFLOW.md
.agents/skills/quotation-card-execution/SKILL.md
~~~

QUOTATION_CARD_EVIDENCE_MAP.md records observed and proven evidence. CARD_LEARNING_AND_DECISION_LOG.md explains why decisions were made, what problems occurred, why they occurred, how they were fixed, and what was learned. Narrative does not replace technical proof, and evidence does not replace rationale.

## 2. Core Execution Model

The canonical flow is:

~~~text
Instructions
→ Context
→ Capabilities
→ Permissions
→ Active Card
→ Inspect Repository / Git Reality
→ Reconcile State
→ Contract Map
→ Risk Map
→ Human Start Approval
→ CONTENT_ALIGNMENT_GATE
→ SOURCE_ADAPTATION_GATE (when applicable)
→ ROADMAP_ALIGNMENT_GATE
→ Define One Bounded Step
→ Implement
→ Validate
→ Record Evidence
→ GOVERNANCE_RECONCILIATION --write
→ GOVERNANCE_VIEW_RECONCILIATION_GATE --check
→ Checkpoint
→ Accept / Fix / Rollback
→ Prove Exit Gate
→ CARD_QUALITY_GATE
→ READY_FOR_DELIVERY
→ GIT_DELIVERY_APPROVAL
→ Stage / Commit / Push / PR / Merge
→ Outcome-Only Final Reconciliation
→ Commit / Push Reconciliation if required
→ Query Runtime Git State
→ FINAL_CARD_STATE_CONSISTENCY_GATE PASS
→ Card COMPLETE
→ Active Card NONE
→ STOP
→ Separate Approval for Next Card
~~~

No automatic continuation is permitted.

## 3. Card Resolution

Before implementation:

~~~text
Read PROJECT_CONTROL.md.
Resolve exactly one Active Card.
Verify State is suitable for start.
Verify explicit Human Start Approval = YES.
Verify Card exists in the Roadmap.
Verify Card exists in Card Specifications.
~~~

If no authorized Active Card:

~~~text
REQUIRED_APPROVAL_MISSING
STOP
~~~

If identity does not match:

~~~text
CARD_MISMATCH
STOP
~~~

If scope does not match:

~~~text
CARD_SCOPE_MISMATCH
STOP
~~~

If a dependency does not match verified Roadmap facts:

~~~text
CARD_DEPENDENCY_MISMATCH
STOP
~~~

Do not infer authorization from Card order.

## 4. Repository and Git Inspection

Before the first implementation write:

- inspect repository structure;
- inspect relevant existing files;
- inspect existing owners;
- inspect tests;
- inspect configuration;
- inspect Git reality if Git exists;
- inspect working tree;
- inspect branch;
- inspect HEAD;
- inspect untracked and modified files.

Do not modify during inspection.

If Git does not exist, record NOT_AVAILABLE. Do not invent Git state.

## 5. State Reconciliation

Compare:

~~~text
PROJECT_CONTROL.md
repository reality
Git reality
Roadmap
Card Specification
Evidence Map
~~~

If they disagree materially:

~~~text
PROJECT_STATE_CONFLICT
STOP
~~~

Repository reality is stronger than chat memory. Verified evidence is stronger than completion claims. Reconcile before implementation.

## 6. Contract Map

Before writing, create an inspect-only Contract Map for the active Card.

Include:

~~~text
Card ID
Title
Engineering Goal
Learning Goal
Expected Owners
Inputs
Outputs
Domain Contracts
Provider Boundaries
Commercial/Data Invariants
Security Requirements
Tests/Evaluation
Exit Gate
Out of Scope
Future-Card Boundaries
~~~

The Contract Map must identify what the Card owns and must not own. Do not implement while building it.

## 7. Risk Map

Before writing, create an inspect-only Risk Map.

Review only risks relevant to the active Card, such as:

~~~text
commercial calculation ambiguity
missing/null/zero confusion
estimated versus actual conflation
currency ambiguity
time-unit ambiguity
evidence provenance loss
synthetic/real data confusion
AI commercial authority leakage
unsupported risk claims
provider payload leakage
human approval bypass
Excel reconciliation risk
S3 validation risk
secret leakage
future-Card leakage
duplicate implementation
unrelated refactor
test coverage gap
failure-path gap
~~~

For each relevant risk record:

~~~text
Risk:
Why Relevant:
Existing Protection:
Required Validation:
STOP Condition:
~~~

Do not invent unrelated risks.

## 8. Commercial and Data Semantic Check

Before commercially meaningful implementation, verify applicable semantics from COMMERCIAL_AND_DATA_GUARDRAILS.md:

~~~text
hours
currency
hourly rate
estimated cost
actual cost
estimated versus actual
variance
percentage variance
null versus zero
scope-change semantics
historical evidence provenance
synthetic provenance
approval state
Excel reconciliation
~~~

If financially material semantics remain unclear:

~~~text
COMMERCIAL_SEMANTICS_UNVERIFIED
STOP
~~~

Do not guess.

## 9. AI and Bedrock Boundary Check

For AI-related Cards verify that AI may interpret, summarize, select approved tools, explain evidence, draft narrative, and surface missing information.

AI may not:

~~~text
invent rates
invent historical outcomes
invent authoritative totals
override deterministic calculations
fabricate evidence IDs
fabricate evidence counts
approve a quotation
bypass human review
silently fill missing commercial values
~~~

Model output is untrusted until validated.

If violated:

~~~text
AI_BOUNDARY_VIOLATION
STOP
~~~

## 10. Provider Boundary Check

Required:

~~~text
Core
→ AI Provider Contract
→ Bedrock Adapter

Core
→ Storage Contract
→ S3 Adapter
~~~

No boto3 response object, Bedrock SDK payload, or S3 SDK object becomes a Core domain model.

If provider-specific ownership leaks into Core:

~~~text
PROVIDER_BOUNDARY_VIOLATION
STOP
~~~

## 11A. CONTENT_ALIGNMENT_GATE

CONTENT_ALIGNMENT_GATE is an additional pre-implementation gate. It does
not replace ROADMAP_ALIGNMENT_GATE, the Card Start Gate, or dependency
checks. It must PASS before bounded implementation, file modification,
code generation, test creation, or dependency changes.

The gate must identify from the actual user or task instruction:

~~~text
Current Card ID
Current Card title
Canonical Card contract
Actual requested work
Explicit user constraints
Files/components the request would affect
Implied future or out-of-scope work
~~~

Compare the requested work with the matching entries in
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md and
QUOTATION_CARD_SPECIFICATIONS.md. Confirm that the work belongs to the
current Card, matches its intent, fits its ownership, introduces no
invented requirement, remains bounded, and does not mix current and future
Card scope. Also verify commercial/data, AI, provider, security, and human
approval boundaries.

Correct Card ID does not imply correct work. For example:

~~~text
Active Card: V1-C02 — Domain Models
Requested work: Implement FastAPI endpoints
Result: CONTENT_ALIGNMENT_GATE: BLOCKED
Reason: FastAPI application work belongs to a later Card and is outside the
        current Card contract.
~~~

Phrases such as “while here”, “small cleanup”, “prepare for later”,
“future-proof this”, “since we are already editing this file”, or “add this
now for convenience” do not justify future-Card, unrelated, or out-of-scope
work. If requested work belongs primarily to another Card, BLOCK rather
than switching Cards or reinterpreting the request.

The gate must BLOCK at minimum for:

~~~text
wrong Card ID
correct Card ID with wrong requested content
mixed current and future Card scope
invented requirement
out-of-scope work
disguised future work
unrelated cleanup or refactor
commercial/data/AI/human boundary conflict
work owned primarily by another Card
premature future-Card infrastructure or technology
~~~

Use this record:

~~~text
CONTENT_ALIGNMENT_GATE
Current Card:
Canonical Card Contract:
Actual Requested Work:
Explicit Constraints:
Affected Files/Components:
Implied Future/Out-of-Scope Work:
Comparison:
Result: PASS | BLOCKED
Mismatch Type: WRONG_CARD | WRONG_CARD_CONTENT | MIXED_CARD_SCOPE |
               FUTURE_CARD_LEAKAGE | INVENTED_REQUIREMENT | OUT_OF_SCOPE |
               BOUNDARY_CONFLICT | UNRELATED_WORK
Reason:
Required Action: STOP when BLOCKED
~~~

CONTENT_ALIGNMENT_GATE: PASS is allowed only when the request maps to the
current Card contract, no material future leakage or invented requirement
exists, scope is bounded, and all relevant boundaries remain preserved. A
PASS is not implementation evidence and does not waive human approval or
any other gate. If BLOCKED, preserve the requested work, mismatch reason,
gate result, and stop reason; do not modify scope, switch Cards, or start
another Card.

## 11B. SOURCE_ADAPTATION_GATE

Run SOURCE_ADAPTATION_GATE when a Card materially studies an external
repository for implementation guidance, adapts external code/design/pattern,
reuses an external component/module/example, adopts architecture substantially
influenced by an external source, or copies/transforms non-trivial
configuration or implementation material. Do not require meaningless records
for trivial language syntax, ubiquitous constructs, ordinary standard-library
usage, or normal API usage without material adaptation.

Before material incorporation, select exactly one decision from the
canonical taxonomy:

~~~text
BUILD
ADAPT
REUSE
REFERENCE ONLY
REJECT
~~~

Do not use ambiguous labels such as USE, MAYBE USE, INSPIRED BY, COPY, or
BORROW without mapping them to one canonical decision. Studying a source
does not authorize incorporation; useful study may end as REFERENCE ONLY or
REJECT.

Before ADAPT or REUSE, verify this Source Adaptation Gate record is complete:

~~~text
SOURCE_ADAPTATION_GATE
Source / Repository:
URL:
File / Module:
Source Type:
License:
License Verification Status:
What Was Studied:
Decision:
Reason for Decision:
What Was Taken:
What Was Not Taken:
Changes Made:
Risks / Limitations:
Security / Data Concerns:
Card:
Evidence Reference:
Learning Log Reference:
Result: PASS | BLOCKED
~~~

`License Verification Status` must be VERIFIED, UNVERIFIED, or
NOT_APPLICABLE. REUSE with UNKNOWN or UNVERIFIED license status blocks
incorporation. ADAPT with UNKNOWN or UNVERIFIED license status blocks code
or design incorporation where license obligations may apply. REFERENCE ONLY
may proceed with UNVERIFIED status only when nothing is incorporated; keep
the unresolved status explicit and do not provide legal conclusions.

For BUILD, record that the source was studied but implementation is
independent, including what was learned and intentionally not copied where
material. BUILD must not disguise material incorporation; if external code
or design is incorporated, use ADAPT or REUSE as appropriate.

ADAPT additionally requires exact source identification, license handling,
What Was Taken, What Was Not Taken, Changes Made, risks/limitations, and
later Evidence Map and Learning Log linkage. REUSE additionally requires the
exact component/source, verified license status, version or reference where
relevant, integration/configuration changes, risks/limitations, Card linkage,
and later evidence linkage. Normal package dependency usage is not source
code REUSE unless an external implementation artifact is actually reused in
a traceability-relevant way.

REFERENCE ONLY requires that nothing material is incorporated. REJECT
requires the source evaluation and rejection reason to remain visible, with
nothing incorporated. Both decisions remain historical records.

No material external code, configuration, architecture artifact, or
implementation fragment may enter the project without this traceability
decision. If material source information is missing, or external material
enters without a record, use:

~~~text
UNTRACKED_EXTERNAL_SOURCE
SOURCE_ADAPTATION_GATE: BLOCKED
STOP
~~~

Preserve the finding; do not retroactively hide its origin. If an external
source introduces secret exposure, unsafe network behavior, suspicious
dependencies, customer-data risk, unsupported dependencies, insecure
execution, or license uncertainty, preserve the finding and stop as required.

CONTENT_ALIGNMENT_GATE remains independent. A valid source does not justify
future-Card leakage: studying a FastAPI source during the Domain Models Card
may be REFERENCE ONLY, but implementing that FastAPI layer is
CONTENT_ALIGNMENT_GATE: BLOCKED. Dependency checks remain separate and no
dependencies are invented.

## 11. ROADMAP_ALIGNMENT_GATE

Before implementation produce:

~~~text
ROADMAP_ALIGNMENT_GATE

Card:
Dependency Check:
Repository-State Check:
Duplicate-Implementation Check:
Ownership Check:
Contract Check:
Commercial/Data Guardrail Check:
AI Boundary Check:
Provider Boundary Check:
Security Check:
Future-Scope Check:
Approval Check:
Authorized Bounded Step:
Focused Validation:
Exit-Gate Requirement Advanced:

Result:
PASS | BLOCKED
~~~

If BLOCKED:

~~~text
ROADMAP_ALIGNMENT_GATE_BLOCKED
STOP
~~~

No implementation occurs before PASS.

## 12. One Bounded Step

After alignment PASS, define exactly one bounded implementation step.

A bounded step must:

- advance one meaningful part of the Card;
- have a clear owner;
- have clear validation;
- be reversible where practical;
- avoid unrelated files;
- avoid future-Card work.

Do not apply one uncontrolled patch to multiple risky concerns when the Card naturally contains separate steps.

## 13. Implementation Rules

During implementation:

~~~text
preserve ownership
preserve typed boundaries
preserve deterministic commercial truth
preserve provider isolation
preserve human approval boundary
keep retries bounded
keep tool behavior bounded
avoid speculative infrastructure
avoid unrelated refactors
avoid hidden migration work
avoid future-Card leakage
~~~

If a material architecture change becomes necessary:

~~~text
ARCHITECTURE_CHANGE_REQUEST
STOP
~~~

If significant new technology becomes necessary:

~~~text
TECHNOLOGY_CHANGE_REQUEST
STOP
~~~

Request human approval before proceeding.

## 14. Validation Ladder

Validate narrow to broad using only levels applicable to the active Card:

~~~text
1. syntax/static validation
2. import/contract validation
3. focused unit test
4. component/contract test
5. commercial/data invariant test
6. AI/provider failure test
7. relevant regression
8. integration test
9. runtime/degraded-path test
10. Card-specific evaluation
11. exact Exit Gate proof
~~~

Do not require future infrastructure before its Card exists.

~~~text
TEST NOT RUN != PASS
~~~

## 15. Failure Procedure

On any required validation failure:

1. stop implementation expansion;
2. record the exact failure in QUOTATION_CARD_EVIDENCE_MAP.md;
3. record the observed result;
4. determine whether the current state is safe;
5. roll back if needed;
6. fix only within current authorized scope;
7. rerun focused validation;
8. retain original failure and recovery evidence;
9. do not claim PASS until rerun evidence proves it.

Failure is evidence. Do not erase failed attempts.

The Evidence Map records the technical observed failure and recovery evidence. The Learning and Decision Log records what happened, why it happened, the root cause, how it was fixed, why that fix was selected, and what should be remembered later. A repaired failure must not disappear.

## 16. Required STOP Codes

~~~text
PROJECT_STATE_CONFLICT
CARD_MISMATCH
CARD_SCOPE_MISMATCH
CARD_DEPENDENCY_MISMATCH
CONTENT_ALIGNMENT_MISMATCH
WRONG_CARD_CONTENT
OUT_OF_SCOPE_WORK
MIXED_CARD_SCOPE
DUPLICATE_IMPLEMENTATION
UNTRACKED_EXTERNAL_SOURCE
FUTURE_CARD_LEAKAGE
ROADMAP_ALIGNMENT_GATE_BLOCKED
REQUIREMENT_REGRESSION
COMMERCIAL_SEMANTICS_UNVERIFIED
COMMERCIAL_INVARIANT_FAILED
AI_BOUNDARY_VIOLATION
AI_INVALID
AI_UNAVAILABLE
AI_UNSUPPORTED_CLAIM
INSUFFICIENT_EVIDENCE
PROVIDER_BOUNDARY_VIOLATION
EXCEL_RECONCILIATION_FAILED
SECURITY_BOUNDARY_VIOLATION
REQUIRED_VALIDATION_FAILED
REQUIRED_APPROVAL_MISSING
ARCHITECTURE_CHANGE_REQUEST
TECHNOLOGY_CHANGE_REQUEST
~~~

## 17. Evidence Update Rule

After meaningful implementation or validation, update QUOTATION_CARD_EVIDENCE_MAP.md incrementally. Record mutable/latest validation evidence in the Evidence Map; the Learning Log may preserve validation results only as dated or explicitly historical events and must not act as a current status dashboard. Before final quality proof or READY_FOR_DELIVERY, run `python scripts/reconcile_governance_views.py --write` followed by `python scripts/reconcile_governance_views.py --check`. Only explicitly generated Evidence Map blocks may be changed by the reconciliation tool; detailed Card evidence remains manual and authoritative for observed facts.

Record only:

~~~text
actual files changed
actual commands
actual tests
actual observed outputs
actual failures
actual evaluations
actual Git state
actual AWS state
actual Bedrock state
~~~

Never reconstruct evidence from memory at Card end when it could have been recorded earlier.

After meaningful implementation and validation, update the active Card's record in CARD_LEARNING_AND_DECISION_LOG.md when applicable. Record actual experience only: what was built, key design decisions, why the approach was chosen, alternatives, technology rationale, problems, root cause, fix, tradeoffs and limitations, lessons learned, and impact on later Cards. Do not invent rationale or learning before it occurs.

## 18. Checkpoint Model

Use:

~~~text
Action
→ State Change
→ Checkpoint
→ Validation
→ Accept / Fix / Rollback
~~~

A checkpoint may include repository state, approved Git commit where available, known modified files, test state, evidence state, Learning / Decision Log state, CONTENT_ALIGNMENT_GATE result, and safe resume point.

CONTENT_ALIGNMENT_GATE result:
PASS | BLOCKED | NOT_RUN

Source Adaptation:
NOT_APPLICABLE | NOT_STARTED | UNDER_REVIEW | APPROVED | IMPLEMENTED | REJECTED | BLOCKED
Decision:
BUILD | ADAPT | REUSE | REFERENCE ONLY | REJECT | NONE
Traceability Record:
<record ID or NONE>

Learning / Decision Log:
CURRENT | PARTIAL | NOT_STARTED | COMPLETE

Do not invent a Git checkpoint if Git is unavailable.

## 19. Safe Resume

After interruption or context loss, read:

~~~text
AGENTS.md
PROJECT_PROFILE.md
PROJECT_CONTROL.md
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md
QUOTATION_CARD_SPECIFICATIONS.md
QUOTATION_CARD_EVIDENCE_MAP.md
CARD_LEARNING_AND_DECISION_LOG.md
QUOTATION_ENGINEERING_HARNESS.md
COMMERCIAL_AND_DATA_GUARDRAILS.md
GIT_WORKFLOW.md once migrated
~~~

Then inspect repository and Git reality.

Never resume from chat memory alone.

If safe resume cannot be proven:

~~~text
PROJECT_STATE_CONFLICT
STOP
~~~

## 20. CARD_QUALITY_GATE

Before recommending COMPLETE, evaluate:

~~~text
Focused Tests
Relevant Regression
Card Evaluation
Commercial/Data Invariants
AI/Provider Validation
Security Validation
Exit Gate Proof
Evidence Current
PROJECT_CONTROL Current
Git Diff Reviewed
Git Status Reviewed
Known Limitations Recorded
Learning / Decision Log Current
Learning Record Complete
Source Adaptation: NOT_APPLICABLE when no material external source was involved
Source Adaptation Traceability: required and current when ADAPT or REUSE materially occurred
Approved Delivery Complete where applicable
~~~

Learning / Decision Log Current means, where applicable, that design rationale, material alternatives, technology rationale, failure/root-cause/fix history, tradeoffs and limitations, What We Learned, and future-maintainer reminders are recorded from actual experience. If required learning documentation is missing:

~~~text
CARD_QUALITY_GATE: BLOCKED
~~~

When material external-source adaptation or reuse occurred, the quality
gate must also verify that SOURCE_ADAPTATION_TRACEABILITY.md contains an
explicit decision, complete source and license information, What Was Taken,
What Was Not Taken, Changes Made where applicable, risks/limitations, Card
linkage, and evidence and learning references. If required traceability is
incomplete:

~~~text
CARD_QUALITY_GATE: BLOCKED
~~~

When no material external source was involved, `Source Adaptation:
NOT_APPLICABLE` does not block completion.

Return:

~~~text
CARD_QUALITY_GATE: PASS | BLOCKED
~~~

If BLOCKED, the Card cannot become COMPLETE.

## 21. Learning Record

Before Card completion, update CARD_LEARNING_AND_DECISION_LOG.md with actual:

~~~text
what was built
key design decisions
why the approach was chosen
alternatives considered
technology/library rationale
problems encountered
root cause
fix and why it was selected
tradeoffs and limitations
lessons learned
impact on later Cards
~~~

Do not prefill these fields before implementation. A Card is not fully complete if the code works but the engineering reasoning has been lost. Preserve enough context for a future maintainer to understand:

~~~text
WHAT
WHY
ALTERNATIVES
FAILURE
ROOT CAUSE
FIX
EVIDENCE
TRADEOFF
LEARNING
~~~

## 22. Exit Gate Proof

Prove the Exit Gate exactly:

~~~text
Exit Gate Requirement:
Observed Evidence:
PASS / FAIL / NOT_PROVEN:
Limitations:
~~~

No vague “feature works” claim and no completion based only on code existence.

## 23. Card Completion

A Card may become COMPLETE only if:

- the contract is satisfied;
- required validations were executed;
- the Exit Gate is proven;
- Evidence is current;
- CARD_LEARNING_AND_DECISION_LOG.md is current;
- failure and fix history is recorded where applicable;
- design rationale is recorded;
- What We Learned is complete;
- the Learning Record is complete;
- CARD_QUALITY_GATE is PASS;
- PROJECT_CONTROL is reconciled;
- READY_FOR_DELIVERY is reached;
- one valid GIT_DELIVERY_APPROVAL covers the exact validated delivery state;
- the normal commit/push/PR/merge chain is complete.
- FINAL_CARD_STATE_CONSISTENCY_GATE is PASS across all current Card-state representations.

Outcome-only final reconciliation may record only observed delivery results,
historical delivery hashes, completion evidence, the completed-card list, and
the Active Card transition to NONE. It must not change implementation, scope,
contract, validated payload, or unrelated policy. Such reconciliation does not
invalidate the consumed GIT_DELIVERY_APPROVAL. The final consistency gate runs
after any required reconciliation commit/push, against a clean working tree;
runtime Git facts are queried directly and current HEAD is never required in a
tracked document.

Then:

~~~text
Card State = COMPLETE
Active Card = NONE
STOP
~~~

Do not start the next Card.

## 24. Human Approval Boundaries

Explicit human approval is required for:

~~~text
Card start
next Card
material scope change
architecture change
significant technology addition
sensitive/destructive action
credential-sensitive action
external write/action capability
GIT_DELIVERY_APPROVAL for the normal commit/push/PR/merge chain
deployment/release
~~~

Routine reversible implementation is allowed only inside an already authorized Card and bounded scope.

## 25. Git Delivery Boundary

Once GIT_WORKFLOW.md is migrated, follow it.

By default:

~~~text
one Card = one branch
no direct work on main
no force push
no secret commits
no unrelated work in a Card commit
no auto-merge
no automatic next Card
~~~

If Git is not initialized, record NOT_AVAILABLE.

## 26A. GIT_DELIVERY_APPROVAL

READY_FOR_DELIVERY is the state after implementation, required validation,
Evidence Map, Learning Log, ROADMAP_ALIGNMENT_GATE, CARD_QUALITY_GATE, and
Exit Gate proof are complete, with normal Git delivery still pending.

One explicit GIT_DELIVERY_APPROVAL authorizes `git add`, commit, push, PR
creation, and merge for the exact validated Card state. Record the Card,
branch, validated file set/diff, tests, gate results, and working-tree state
before approval.

The approval does not cover force push, destructive history actions,
architecture or scope changes outside the Card contract, sensitive
credentials, unrelated external actions, or deployment/release unless
separately authorized and owned by the Card.

If implementation files, governance evidence, staged diff, tests, gate
results, branch, or delivery file set materially changes after approval:

~~~text
GIT_DELIVERY_APPROVAL: INVALIDATED
STOP
REVALIDATE
NEW HUMAN APPROVAL REQUIRED
~~~

## 26B. FINAL_CARD_STATE_CONSISTENCY_GATE

Run the deterministic `scripts/final_card_state_consistency.sh <CARD_ID>
[EXPECTED_STATE] [ROOT]` validator after any required reconciliation
commit/push and before marking a Card COMPLETE. It compares
PROJECT_CONTROL.md, the detailed Card record and Current Card Table and
Current Summary in QUOTATION_CARD_EVIDENCE_MAP.md, the Learning Log current
state and completion record, the active Card and authorization state, the
CARD_QUALITY_GATE, Exit Gate, tests/evidence, Git delivery state,
Recommended State, and Completed Cards list.

The validator must return zero only when all current representations agree.
For example: `bash scripts/final_card_state_consistency.sh V1-C01 COMPLETE`.
It validates the requested Card only; it does not require current HEAD to be
stored in a tracked document.
On mismatch:

~~~text
FINAL_CARD_STATE_CONSISTENCY_GATE: FAIL
STATE_RECONCILIATION_REQUIRED
STOP
~~~

The completion chain is therefore:

~~~text
implementation → validation → evidence / learning
→ ROADMAP_ALIGNMENT_GATE → CARD_QUALITY_GATE → Exit Gate PROVEN
→ delivery → final reconciliation
→ FINAL_CARD_STATE_CONSISTENCY_GATE PASS
→ COMPLETE → Active Card NONE → STOP
~~~

## 26. Security Check

For every Card, where applicable inspect:

~~~text
secrets
.env handling
AWS credentials
logging/redaction
real confidential company/customer data
synthetic provenance
external untrusted input
model output validation
least privilege
external write capabilities
~~~

If violated:

~~~text
SECURITY_BOUNDARY_VIOLATION
STOP
~~~

## 27. Quotation-Specific Invariant Check

Where applicable prove:

~~~text
MISSING != ZERO
ESTIMATED != ACTUAL
SIMILAR != IDENTICAL
HISTORICAL EVIDENCE != FUTURE CERTAINTY
AI EXPLAINS; DETERMINISTIC SOFTWARE CALCULATES
NO EVIDENCE → NO RISK CLAIM
NO HUMAN APPROVAL → NO FINAL QUOTATION
EXCEL TOTALS RECONCILE
SYNTHETIC DATA STAYS SYNTHETIC
PROVIDER OBJECTS STAY OUTSIDE CORE
~~~

## 28. Recorded C01 Completion Context (Not Live State)

Current live operational state is owned by PROJECT_CONTROL.md. Runtime Git
facts must be queried from Git; the values below document the completed C01
event and are not an independent current-state ledger.

The current project state is:

~~~text
Governance: COMPLETE
Learning Governance: COMPLETE
Governance Hardening: COMPLETE
Final Governance Hardening Audit: PASS
Hardening Blockers: NONE
Application Implementation: V1-C01 BASELINE IMPLEMENTED
Active Card: NONE
C01 Start Authorization: GRANTED (historical; Card complete)
Git Repository: YES
V1-C01 State: COMPLETE
GIT_DELIVERY_APPROVAL: GRANTED / CONSUMED — PR #1 merged
Current source records: NONE
~~~

GOVERNANCE_HARNESS_PROOF_CASES.md is the canonical formal proof-scenario
specification. A formal proof case is not an executable test;
NOT_EXECUTED is not PASS, and NOT_PROVEN is not PASS.

This harness defines future execution behavior. It does not authorize C01.

## 29. Migration-Specific Rule

Canonical governance files may be rewritten only through explicitly bounded migration steps.

Governance migration is not V1 application implementation.

Do not record governance migration events as V1 application Card evidence.

## 30. Final Execution Rule

~~~text
RESOLVE ONE CARD.
INSPECT BEFORE WRITE.
RECONCILE REALITY.
BUILD CONTRACT MAP.
BUILD RISK MAP.
VERIFY HUMAN APPROVAL.
PASS ROADMAP_ALIGNMENT_GATE.
IMPLEMENT ONE BOUNDED STEP.
VALIDATE NARROW TO BROAD.
FAILURE → RECORD + STOP.
EVIDENCE BEFORE CLAIM.
PROVE EXIT GATE.
PASS CARD_QUALITY_GATE.
READY_FOR_DELIVERY.
GIT_DELIVERY_APPROVAL.
COMMIT → PUSH → PR → MERGE.
OUTCOME-ONLY FINAL RECONCILIATION.
RECONCILIATION COMMIT/PUSH IF REQUIRED.
RUNTIME GIT VERIFICATION.
FINAL_CARD_STATE_CONSISTENCY_GATE: PASS.
COMPLETE CARD.
ACTIVE CARD → NONE.
STOP.
NEXT CARD → NEW HUMAN APPROVAL.
~~~
