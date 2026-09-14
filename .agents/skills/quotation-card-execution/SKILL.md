---
name: quotation-card-execution
description: Execute exactly one authorized AI Quotation Intelligence V1 Card using canonical project state, inspect-first control, bounded implementation, validation, evidence, and explicit human approvals.
---

# Quotation Card Execution Skill

This is the operational procedure for executing exactly one authorized V1 Card in the AI Quotation Intelligence System. It supports Codex, Claude Code, Cursor, similar coding agents, and human-assisted coding workflows. It does not redefine canonical project truth.

## 1. Required Read Order

Before implementation, read in order:

1. AGENTS.md
2. PROJECT_PROFILE.md
3. PROJECT_CONTROL.md
4. AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md
5. QUOTATION_CARD_SPECIFICATIONS.md
6. QUOTATION_CARD_EVIDENCE_MAP.md
7. CARD_LEARNING_AND_DECISION_LOG.md
8. QUOTATION_ENGINEERING_HARNESS.md
9. COMMERCIAL_AND_DATA_GUARDRAILS.md
10. GIT_WORKFLOW.md

During governance migration also read PROJECT_MIGRATION_STATUS.md. Never resume from chat memory alone.

CARD_LEARNING_AND_DECISION_LOG.md is the canonical source for engineering rationale and learning history during Card start, Card resume, context recovery, and pre-completion review.

When a Card has external-source relevance, also read SOURCE_ADAPTATION_TRACEABILITY.md during Card start, resume, context recovery, and pre-completion review. Do not load it unnecessarily when no material external source is involved.

## 2. Resolve Exactly One Card

Read PROJECT_CONTROL.md as the sole live operational-state and authorization owner, then resolve:

Card ID, title, state, human start approval, authorized scope, safe checkpoint, and known blockers.

Implementation requires:

- Active Card != NONE
- Human Start Approval = YES
- the Card exists in the Roadmap, Card Specifications, and Evidence Map
- Card title and scope match across canonical sources
- dependencies are satisfied when explicitly defined
- no conflicting Active Card exists
- repository and Git state are understood

If approval is absent:
```
REQUIRED_APPROVAL_MISSING
STOP
```

If identity or scope differs:
```
CARD_MISMATCH
CARD_SCOPE_MISMATCH
STOP
```

If a dependency is not proven:
```
CARD_DEPENDENCY_MISMATCH
STOP
```

Do not infer authorization from Card order.

## 3. Inspect Before Write

Perform read-only inspection before the first implementation write:

- repository root and relevant files
- existing owners, application structure, tests, and configuration
- repository/Git state, branch, HEAD, working tree, untracked and modified files
- remote/upstream when available

If Git does not exist, record NOT_AVAILABLE. Do not initialize or change Git during inspection. Do not overwrite unrelated user work.

Compare repository reality, Git reality, PROJECT_CONTROL.md, Roadmap, Card Specification, and Evidence Map. If materially inconsistent:

```
PROJECT_STATE_CONFLICT
STOP
```

Repository reality outranks chat memory; verified evidence outranks claims.

## 4. Contract Map

Before writing, create an inspect-only Contract Map for the active Card:

```
Card:
Engineering Goal:
Learning Goal:
Current Owners:
Expected Owners:
Inputs:
Outputs:
Domain Contracts:
Application Contracts:
Provider Boundaries:
Commercial/Data Invariants:
AI Authority Boundary:
Human Approval Boundary:
Security Requirements:
Tests/Evaluation:
Exit Gate:
Out of Scope:
Future-Card Boundaries:
```

Do not implement while building this map.

## 5. Risk Map

Create an inspect-only Risk Map containing only risks relevant to the active Card. Consider, where applicable:

- missing versus zero
- estimated versus actual
- currency, hours, and rate semantics
- deterministic total ownership
- variance semantics
- evidence provenance
- synthetic versus real data
- similarity treated as truth
- RiskEvidence versus RiskSuggestion confusion
- unsupported AI claims
- Bedrock or S3 provider leakage
- approval bypass
- Excel reconciliation
- secret leakage
- duplicate implementation
- future-Card leakage
- unrelated refactoring
- test or failure-path gaps
- deployment claims without evidence

For each relevant risk record:

```
Risk:
Why Relevant:
Existing Protection:
Required Validation:
STOP Condition:
```

## 6. Commercial/Data Gate

For commercially meaningful work, verify applicable rules in COMMERCIAL_AND_DATA_GUARDRAILS.md, including hours, rates, currency, estimated/actual distinction, variance, null/zero semantics, historical and synthetic provenance, approval state, and Excel reconciliation.

If material semantics are unclear:

```
COMMERCIAL_SEMANTICS_UNVERIFIED
STOP
```

Never guess.

## 7. AI and Provider Gate

AI may understand requests, select approved tools, summarize, interpret evidence, explain risk, draft narrative, and surface missing information.

AI may not invent rates, outcomes, totals, evidence or evidence counts; override deterministic calculations; silently fill commercial values; approve a quotation; or bypass human review.

Required provider boundaries:

```
Core → AI Provider Contract → Bedrock Adapter
Core → Storage Contract → S3 Adapter
```

Provider SDK objects and payloads remain outside Core. If a boundary is violated:

```
AI_BOUNDARY_VIOLATION
PROVIDER_BOUNDARY_VIOLATION
STOP
```

## 8. CONTENT_ALIGNMENT_GATE

Run CONTENT_ALIGNMENT_GATE after canonical context has been read, project
and Card identity have been reconciled, and Active Card and authorization
checks have passed. Run it before implementation, file modification, test
creation, dependency changes, or bounded execution. It is additional to,
and does not replace, ROADMAP_ALIGNMENT_GATE or dependency checks.

Derive the actual requested work from the user or task instruction. Record:

```
Current Card ID:
Current Card title:
Canonical Card contract:
Actual requested work:
Explicit user constraints:
Expected files/components affected:
Implied future or out-of-scope work:
```

Compare the request with the matching entries in
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md and
QUOTATION_CARD_SPECIFICATIONS.md. Verify that it belongs to the current
Card, matches its intent, fits Card ownership, remains bounded, and contains
no invented requirement, hidden scope expansion, unrelated cleanup/refactor,
future-Card work, or mixed Card scope. Check commercial, data, AI, provider,
security, and human-approval boundaries as applicable.

Correct Card ID does not mean correct requested work. For example:

```
Authorized Card: V1-C02 — Domain Models
Requested work: Implement FastAPI endpoints
Result: CONTENT_ALIGNMENT_GATE: BLOCKED
Reason: the requested work does not belong to the active Card contract.
```

Reject justifications such as “while here”, “small cleanup”, “prepare for
later”, “future-proof this”, “since this file is already open”, or “add this
now for convenience” when they introduce future-Card or unrelated scope.
Work primarily owned by another Card must BLOCK; do not switch Cards,
reinterpret the request, or widen authorization.

The gate must BLOCK for:

```
WRONG_CARD
WRONG_CONTENT
MIXED_CARD_SCOPE
FUTURE_CARD_LEAKAGE
INVENTED_REQUIREMENT
OUT_OF_SCOPE
BOUNDARY_CONFLICT
UNRELATED_WORK
work primarily owned by another Card
premature infrastructure or technology owned by a future Card
```

For aligned work, record:

```
CONTENT_ALIGNMENT_GATE: PASS
Requested Work:
Current Card Contract:
Mapping:
```

For a mismatch, record:

```
CONTENT_ALIGNMENT_GATE: BLOCKED
Mismatch Type:
Requested Work:
Current Card Contract:
Conflict:
Required Action: STOP
```

Use these aligned stop codes where applicable:

```
CONTENT_ALIGNMENT_MISMATCH
WRONG_CARD_CONTENT
FUTURE_CARD_LEAKAGE
INVENTED_REQUIREMENT
OUT_OF_SCOPE_WORK
MIXED_CARD_SCOPE
```

CONTENT_ALIGNMENT_GATE: PASS means content alignment only. It does not
authorize implementation or waive human approval, dependency checks, or
ROADMAP_ALIGNMENT_GATE. Human Card-start approval does not bypass this
gate; an authorized V1-C02 request for V1-C13 work remains BLOCKED. If the
gate is BLOCKED, preserve the request, mismatch reason, gate result, and
stop reason, then STOP without modifying files or starting another Card.

Dependency protection remains independent: this gate checks requested work
and content, while the dependency gate checks explicit dependencies when
they exist. Do not invent dependencies.

## 8A. SOURCE_ADAPTATION_GATE

Determine whether the active Card materially studies an external repository
for implementation guidance, adapts external code/design/pattern, reuses an
external component/module/example, adopts architecture materially influenced
by an external source, or copies/transforms non-trivial configuration or
implementation material. If none applies:

```
Source Adaptation: NOT_APPLICABLE
```

Do not create meaningless records for trivial syntax, standard-library usage,
or ubiquitous programming constructs.

When applicable, select exactly one canonical decision:

```
BUILD
ADAPT
REUSE
REFERENCE ONLY
REJECT
```

Do not replace these with ambiguous labels. Studying a source does not
authorize incorporation; inspection may still result in REFERENCE ONLY or
REJECT.

Before material ADAPT or REUSE, run SOURCE_ADAPTATION_GATE and verify the
source ledger has, at minimum, source/repository, URL, file/module where
relevant, source type, license, license verification status, what was
studied, decision, reason, what will be taken, what will not be taken,
Changes Made where applicable, risks/limitations, security/data concerns,
and Card linkage. Missing required information produces:

```
SOURCE_ADAPTATION_GATE: BLOCKED
STOP
```

License enforcement is mandatory: REUSE with UNKNOWN or UNVERIFIED license
blocks incorporation; ADAPT with UNKNOWN or UNVERIFIED license blocks code
or design incorporation where obligations may apply. REFERENCE ONLY may
proceed with UNVERIFIED status only when nothing is incorporated. Do not
invent license compatibility or provide legal conclusions.

BUILD means independent implementation. If material external code or design
is incorporated, BUILD is invalid and the decision must be corrected to
ADAPT or REUSE as appropriate. Block any attempt to disguise adaptation as
BUILD.

ADAPT requires exact source, license handling, What Was Taken, What Was Not
Taken, Changes Made, risks/limitations, Card linkage, and later Evidence Map
and Learning Log references. REUSE requires the exact source/component,
verified license, version/reference where relevant,
integration/configuration changes, risks/limitations, Card linkage, and
later evidence and learning references. Normal package use is not source
code REUSE unless an external implementation artifact is materially reused.

REFERENCE ONLY requires that nothing material is incorporated; an unverified
license may remain explicit. REJECT requires the evaluation and rejection
reason to remain visible, with nothing incorporated. Neither decision may be
erased after the fact.

No material external code, configuration, architecture artifact, or
implementation fragment may enter without a traceability record. If it does,
use:

```
UNTRACKED_EXTERNAL_SOURCE
SOURCE_ADAPTATION_GATE: BLOCKED
STOP
```

Preserve findings involving suspicious packages, unsafe network behavior,
credentials/secrets, customer data, unsupported dependencies, insecure
execution, or license uncertainty. CONTENT_ALIGNMENT_GATE remains separate:
a valid source cannot justify future-Card leakage, unrelated cleanup, or
work owned by another Card.

## 8B. ROADMAP_ALIGNMENT_GATE

Before implementation produce:

```
ROADMAP_ALIGNMENT_GATE
Card:
Dependency Check:
Repository-State Check:
Duplicate Check:
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
Result: PASS | BLOCKED
```

If BLOCKED:

```
ROADMAP_ALIGNMENT_GATE_BLOCKED
STOP
```

No implementation may begin before PASS.

## 9. One Bounded Step

After PASS, define exactly one bounded step:

```
Step ID:
Goal:
Files Expected:
Owner:
Inputs:
Outputs:
Validation:
Rollback/Recovery:
Exit-Gate Progress:
```

The step must advance the active Card, have a clear owner and validation, avoid unrelated refactors and future-Card work, and be reversible where practical.

## 10. Implementation Rules

Implement only the authorized bounded step. Preserve ownership, typed boundaries, deterministic commercial truth, AI limits, provider isolation, human approval, and synthetic provenance. Avoid speculative infrastructure, unnecessary technology, hidden migration work, cleanup unrelated to the Card, and future-Card implementation.

Material architecture change requires:

```
ARCHITECTURE_CHANGE_REQUEST
STOP
```

Significant technology addition requires:

```
TECHNOLOGY_CHANGE_REQUEST
STOP
```

## 11. Validation Ladder

Use only levels applicable to the active Card:

1. syntax/static
2. import/contract
3. focused unit test
4. component test
5. commercial/data invariant
6. AI/provider failure test
7. relevant regression
8. integration
9. runtime/degraded-path
10. Card evaluation
11. exact Exit Gate proof

Test not run != PASS. Do not require future infrastructure before its Card.

## 12. Failure Loop

When required validation fails, stop expansion and record the failure in QUOTATION_CARD_EVIDENCE_MAP.md:

```
Command/Test:
Observed Result:
Expected Result:
Failure Code:
Impact:
Safe State:
Rollback Needed:
Resolution:
```

Fix only within authorized scope, rerun focused validation, preserve the original failure, and add recovery evidence. Never erase failed evidence or claim PASS without a proving rerun.

The Evidence Map records the observed failure, command or test result, and recovery proof. CARD_LEARNING_AND_DECISION_LOG.md records what happened, observed behavior, root cause, how it was fixed, why that fix was selected, and the lesson. A repaired failure must not disappear. Do not continue past a blocking failure until it is understood and resolved according to the Harness.

## 12.1. Implementation Reasoning

As meaningful events occur, update the active Card's learning record with actual experience where applicable:

```
what was built
design decision and why the approach was chosen
alternatives considered
technology/library rationale
problem and observed behavior
root cause
fix and why it was chosen
tradeoff or limitation
lesson learned
future reminder
impact on later Cards
```

Do not invent content merely to fill sections.

For material engineering choices, capture enough rationale for a future maintainer to understand:

```
Decision:
Context:
Chosen Option:
Why Chosen:
Alternatives:
Why Not Chosen:
Tradeoff:
Evidence/References:
Future Revisit Condition:
```

When a Card actually introduces a material technology, library, or service, record its purpose, why it was needed, why this option was chosen, alternatives, complexity or operational cost where relevant, portability or lock-in implications where relevant, and future replacement condition where relevant. Do not pre-record technologies merely because they appear in the Roadmap.

## 13. Evidence and Checkpoint

After meaningful work, update QUOTATION_CARD_EVIDENCE_MAP.md with actual files, commands, tests, results, evaluations, failures, Git/AWS/Bedrock state, limitations, and Exit Gate evidence only.

After a validated bounded step, record:

```
Card:
Step:
Files Changed:
Validation State:
Evidence State:
Git State:
CONTENT_ALIGNMENT_GATE: PASS | BLOCKED | NOT_RUN
CONTENT_ALIGNMENT_GATE Reason:
Source Adaptation: NOT_APPLICABLE | NOT_STARTED | UNDER_REVIEW | APPROVED | IMPLEMENTED | REJECTED | BLOCKED
Decision: BUILD | ADAPT | REUSE | REFERENCE ONLY | REJECT | NONE
Traceability Record: <record ID or NONE>
License Status: VERIFIED | UNVERIFIED | NOT_APPLICABLE | UNKNOWN
Source Adaptation Gate: PASS | BLOCKED | NOT_RUN
Learning / Decision Log: NOT_STARTED | PARTIAL | CURRENT | COMPLETE
Safe Resume Point:
Known Limitations:
Git Checkpoint: NOT_AVAILABLE / NOT_CREATED unless an actual approved hash exists
```

Do not invent evidence or commit hashes.

## 14. Exit Gate and Quality Gate

Prove the exact Card Exit Gate:

```
Exit Gate Requirement:
Observed Evidence:
PASS | FAIL | NOT_PROVEN:
Limitations:
```

Before recommending completion, evaluate focused tests, regression, Card evaluation, commercial/data invariants, AI/provider validation, security, Exit Gate, current evidence, PROJECT_CONTROL, Git diff/status, limitations, Learning / Decision Log Current, learning, and approved delivery.

Before CARD_QUALITY_GATE may be PASS, verify as applicable that the active Card has an implementation narrative, design rationale, material alternatives, technology rationale, preserved failure/root-cause/fix history, tradeoffs and limitations, completed What We Learned, future-maintainer reminder, later-Card impact, and evidence references pointing to the Evidence Map. If required learning documentation is missing:

```
CARD_QUALITY_GATE: BLOCKED
```

When material external-source adaptation or reuse occurred, also verify that
SOURCE_ADAPTATION_TRACEABILITY.md contains the canonical decision, complete
source and license information, What Was Taken, What Was Not Taken, Changes
Made where applicable, risks/limitations, Card linkage, and evidence and
learning references. If required traceability is incomplete:

```
CARD_QUALITY_GATE: BLOCKED
```

When Source Adaptation is `NOT_APPLICABLE`, it does not block completion.

```
CARD_QUALITY_GATE: PASS | BLOCKED
```

If any required condition is NOT_PROVEN or the gate is BLOCKED, the Card cannot complete.

## 15. Learning Record and Completion

Before completion, update CARD_LEARNING_AND_DECISION_LOG.md with actual technical learning, architecture tradeoffs, failures or surprises, and reminders for later Cards. Do not fabricate learning.

QUOTATION_CARD_EVIDENCE_MAP.md owns observed and proven technical evidence. CARD_LEARNING_AND_DECISION_LOG.md owns rationale, explanation, failure analysis, recovery narrative, and lessons learned. Learning text does not prove a technical claim; evidence alone does not preserve engineering rationale. Both are required.

A working implementation alone is insufficient for Card COMPLETE. Card completion requires technical proof and engineering understanding.

A Card may become COMPLETE only when its contract, required validations, Exit Gate, evidence, Learning Record, CARD_QUALITY_GATE, PROJECT_CONTROL reconciliation, and approved Git delivery are complete.

The completion chain is:

```
Contract satisfied
→ required validation executed
→ Exit Gate proven
→ Evidence Map current
→ Learning & Decision Log current
→ CARD_QUALITY_GATE PASS
→ READY_FOR_DELIVERY
→ one GIT_DELIVERY_APPROVAL for the exact validated Card state
→ commit → push → PR → merge
→ outcome-only final reconciliation
→ reconciliation commit/push if required
→ runtime Git verification
→ FINAL_CARD_STATE_CONSISTENCY_GATE PASS
→ Card COMPLETE
→ Active Card NONE
→ STOP
```

Then:

```
Card = COMPLETE
Active Card = NONE
STOP
```

Never start the next Card automatically.

## 16. Git Handoff and Approval

Only after validation and quality evidence are ready, set READY_FOR_DELIVERY and follow GIT_WORKFLOW.md. One explicit GIT_DELIVERY_APPROVAL covers the normal commit, push, PR, and merge chain for the exact validated Card state. Do not force push by default. Merge is not Card completion.

Outcome-only reconciliation that records only observed delivery results does not
invalidate the consumed approval. Any implementation, scope, contract,
validated-payload, material evidence, staged-diff, validation, branch, or
unrelated-file change after approval sets GIT_DELIVERY_APPROVAL: INVALIDATED,
requires STOP, revalidation, and new approval.

## 17. Resume After Interruption

Re-read the canonical files, including CARD_LEARNING_AND_DECISION_LOG.md and SOURCE_ADAPTATION_TRACEABILITY.md when external-source relevance exists, inspect repository and Git reality, compare the safe checkpoint, Evidence Map, Learning / Decision Log, and Source Adaptation state, and reconcile PROJECT_CONTROL.md. If safe state cannot be proven:

```
PROJECT_STATE_CONFLICT
STOP
```

## 18. Required STOP Codes

```
PROJECT_STATE_CONFLICT
CARD_MISMATCH
CARD_SCOPE_MISMATCH
CARD_DEPENDENCY_MISMATCH
CARD_BRANCH_MISMATCH
DUPLICATE_IMPLEMENTATION
CONTENT_ALIGNMENT_MISMATCH
WRONG_CARD_CONTENT
OUT_OF_SCOPE_WORK
MIXED_CARD_SCOPE
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
UNEXPECTED_WORKTREE_STATE
GIT_BASELINE_UNVERIFIED
SECRET_OR_SENSITIVE_DATA_DETECTED
UNRELATED_WORK_CONFLICT
DESTRUCTIVE_GIT_ACTION_REQUIRED
UNTRACKED_EXTERNAL_SOURCE
```

## 19. Quotation Invariant Check

Where applicable prove:

```
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
```

## 20. Recorded C01 Completion Context (Not Live State)

Current live operational state is owned by PROJECT_CONTROL.md. Runtime Git
facts must be queried from Git; the values below are historical execution
context and do not independently authorize or activate a Card.

```
Application Implementation: V1-C01 BASELINE IMPLEMENTED
Active Card: NONE
C01 Start Authorization: GRANTED (historical; Card complete)
V1-C01 State: COMPLETE
GIT_DELIVERY_APPROVAL: GRANTED / CONSUMED — PR #1 merged
Git Repository: YES
Current source records: NONE
```

This Skill is being created during governance migration. It does not authorize C01.

## 21. Final Execution Loop

```
RESOLVE CARD
→ READ CONTRACT + EVIDENCE
→ INSPECT REPOSITORY / GIT
→ RECONCILE REALITY
→ CONTRACT MAP
→ RISK MAP
→ VERIFY HUMAN START APPROVAL
→ CONTENT_ALIGNMENT_GATE
→ SOURCE_ADAPTATION_GATE (when applicable)
→ ROADMAP_ALIGNMENT_GATE
→ DEFINE ONE BOUNDED STEP
→ IMPLEMENT
→ VALIDATE
→ RECORD EVIDENCE
→ GOVERNANCE_RECONCILIATION --write
→ GOVERNANCE_VIEW_RECONCILIATION_GATE --check
→ CHECKPOINT
→ ACCEPT / FIX / ROLLBACK
→ PROVE EXIT GATE
→ LEARNING RECORD
→ CARD_QUALITY_GATE
→ READY_FOR_DELIVERY
→ GIT_DELIVERY_APPROVAL
→ COMMIT → PUSH → PR → MERGE
→ OUTCOME-ONLY FINAL RECONCILIATION
→ RECONCILIATION COMMIT/PUSH IF REQUIRED
→ RUNTIME GIT VERIFICATION
→ FINAL_CARD_STATE_CONSISTENCY_GATE PASS
→ CARD COMPLETE

Mutable/latest validation results belong in the Evidence Map. The Learning Log
records rationale and historical validation events, not a current status
dashboard; run generated-view reconciliation after either document is updated.
→ ACTIVE CARD NONE
→ STOP
```

No step authorizes work beyond the active Card or explicit human approval.

`scripts/quotation_session_bootstrap.sh` is a SESSION / REPOSITORY SMOKE CHECK
only. It does not execute pytest or prove a Card, Exit Gate, quality gate, or
final consistency state; Card validation runs separately.

Run `bash scripts/test_governance_harness.sh` for executable governance
regression checks. Its temporary fixtures must not mutate the canonical
repository and its results do not replace Card-specific validation.

Governance regression fixture independence is mandatory: temporary fixtures
must explicitly construct their own Card lifecycle state and must not infer
semantics from the live repository or current HEAD. Fixture Git diagnostics
must never be used as path or control data.
