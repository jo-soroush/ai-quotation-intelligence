# AGENTS.md

## AI Quotation Intelligence System — Coding Agent Entry Point

This file is the router for coding agents and human-assisted coding workflows.

It supports:

- Codex;
- Claude Code;
- Cursor;
- future coding agents;
- human and VS Code workflows.

It is intentionally not the full rulebook. Read the canonical owner for details instead of duplicating every project rule here.

## 1. Canonical Files

For Card implementation or resume, read in this order:

1. AGENTS.md
   → coding-agent routing and project-wide execution boundaries

2. PROJECT_PROFILE.md
   → stable mission, architecture, V1 boundaries, and AI/commercial invariants

3. PROJECT_CONTROL.md
   → current state, Active Card, authorization, and safe resume point

4. AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md
   → Card identity, order, dependencies, engineering goals, and Exit Gates

5. QUOTATION_CARD_SPECIFICATIONS.md
   → exact detailed Card contracts
   Status now: MIGRATED / CANONICAL

6. QUOTATION_CARD_EVIDENCE_MAP.md
   → verified implementation, tests, failures, and Exit Gate evidence
   Status now: MIGRATED / CANONICAL

7. CARD_LEARNING_AND_DECISION_LOG.md
   → engineering rationale, decision history, failure/root-cause/fix narrative, lessons learned, and future-maintainer reminders for each Card
   Status now: MIGRATED / CANONICAL

8. QUOTATION_ENGINEERING_HARNESS.md
   → execution control and STOP behavior
   Status now: MIGRATED / CANONICAL

9. COMMERCIAL_AND_DATA_GUARDRAILS.md
   → deterministic commercial/data truth and invariants
   Status now: MIGRATED / CANONICAL

10. GIT_WORKFLOW.md
    → Git/GitHub delivery procedure
    Status now: MIGRATED / CANONICAL

11. .agents/skills/quotation-card-execution/SKILL.md
    → operational procedure for executing exactly one Card
    Status now: MIGRATED / CANONICAL

12. scripts/quotation_session_bootstrap.sh
    → read-only session baseline verification
    Status now: MIGRATED / CANONICAL

13. SOURCE_ADAPTATION_TRACEABILITY.md
    → external-source study, adaptation/reuse decision, license awareness,
      what was and was not taken, risks, Card linkage, and evidence/learning
      linkage
    Status now: CREATED / CANONICAL

14. GOVERNANCE_HARNESS_PROOF_CASES.md
    → formal governance proof scenarios; not executed-test evidence
    Status now: CREATED / CANONICAL

During governance migration also read PROJECT_MIGRATION_STATUS.md.

Do not load every file indiscriminately.

For ownership, QUOTATION_CARD_SPECIFICATIONS.md defines what a Card is intended to build, QUOTATION_CARD_EVIDENCE_MAP.md records what was actually observed and proven, and CARD_LEARNING_AND_DECISION_LOG.md records why decisions were made, what problems occurred, why they occurred, how they were fixed, and what was learned. PROJECT_CONTROL.md remains the owner of current state and authorization.

For each Card, preserve enough rationale for a future reader to understand what changed, why it changed, why the chosen approach was selected, alternatives considered, problems, root cause, fix, tradeoffs, lessons learned, and impact on later Cards. Do not invent these before implementation.

A repaired failure must not disappear from project history. The Evidence Map stores observed technical evidence; the Learning and Decision Log explains what happened, why it happened, how the fix was chosen, and what should be remembered.

CARD_LEARNING_AND_DECISION_LOG.md is part of the information that must be current before a Card can be considered fully documented. Completion enforcement is integrated across QUOTATION_ENGINEERING_HARNESS.md, .agents/skills/quotation-card-execution/SKILL.md, QUOTATION_CARD_SPECIFICATIONS.md, and QUOTATION_CARD_EVIDENCE_MAP.md; read those canonical owners for the detailed rules.

When a Card studies an external source, proposes reuse or adaptation, or is materially influenced by external code, design, pattern, library, or example, read SOURCE_ADAPTATION_TRACEABILITY.md during execution, resume, and relevant context recovery. Do not load it when the Card has no external-source relevance.

External source study does not equal adoption. Material source decisions use only BUILD, ADAPT, REUSE, REFERENCE ONLY, or REJECT. SOURCE_ADAPTATION_TRACEABILITY.md owns the full record format and decision history.

No material external code, configuration, architecture artifact, or implementation fragment may be silently introduced. Material adaptation or reuse requires a traceability decision first; trivial language syntax and ubiquitous constructs do not require meaningless records.

ADAPT or REUSE with UNKNOWN or UNVERIFIED license status must not proceed where license obligations remain unresolved. REFERENCE ONLY may remain UNVERIFIED when nothing is incorporated. Record observations without providing legal conclusions.

SOURCE_ADAPTATION_TRACEABILITY.md records where a source came from and what decision was made. CARD_LEARNING_AND_DECISION_LOG.md records why the engineering decision mattered and what was learned. QUOTATION_CARD_EVIDENCE_MAP.md records what was technically proven. None replaces the others.

## 2. Sources of Truth

When information conflicts, use:

~~~
Repository reality > chat memory
Roadmap > generated prompt
Active Card contract > assumptions
Verified Evidence > completion claims
Deterministic commercial/data guardrails > AI/model output
Human approval > consequential action
~~~

Material conflict:

~~~
PROJECT_STATE_CONFLICT
STOP
NO IMPLEMENTATION
~~~

A prompt requests work. It does not redefine project truth.

## 3. Project Identity

Project: AI Quotation Intelligence System

Purpose:

Analyze historical quotations and actual outcomes, generate evidence-backed risk intelligence, create AI-assisted draft quotations, require human review, and export correct Excel quotations.

Operating posture: Local-first, AWS cloud-ready.

AI provider: Amazon Bedrock in V1.

Public portfolio data: Synthetic by default.

## 4. Original Business Requirements — Non-Negotiable

These requirements remain mandatory:

- AI agent creates draft quotations.
- Historical quotation data is used.
- Quotation data includes time, work items, and monetary parts.
- Historical estimates are compared with actual outcomes.
- Risk suggestions are based on historical performance.
- Quotation output is generated as Excel.

Any prompt or implementation that removes one of these:

~~~
REQUIREMENT_REGRESSION
STOP
~~~

## 5. Critical V1 Non-Negotiables

~~~
NO AI-authoritative hourly rates
NO AI-authoritative commercial totals
NO AI override of deterministic calculations
NO unsupported risk claims
NO fabricated historical evidence
NO final quotation without human approval
NO real company confidential data in the public portfolio repository
NO hard-coded AWS credentials
NO provider-specific Bedrock/S3 payload ownership in Core
NO silent missing-value substitution
NO silent AI fallback
NO Card COMPLETE with failed or unexecuted required validation
NO automatic next Card
NO future-Card implementation without authorization
NO technology addition merely for prestige
~~~

## 6. Card Start

Before any implementation:

~~~
read PROJECT_CONTROL.md
resolve exactly one official Active Card
read its Roadmap entry
read its complete Card Specification once migrated
read existing Card Evidence once migrated
inspect repository + Git reality
verify dependencies
verify explicit human Card-start approval
~~~

Wrong Card, scope, or dependency:

~~~
CARD_MISMATCH
CARD_SCOPE_MISMATCH
CARD_DEPENDENCY_MISMATCH
→ STOP
~~~

If no active authorized Card:

~~~
REQUIRED_APPROVAL_MISSING
STOP
~~~

## 7. Inspect Before Write

Before the first implementation write of every Card:

- inspect repository reality;
- inspect Git reality;
- identify existing owners;
- build an inspect-only Contract Map;
- build an inspect-only Risk Map;
- check duplicate implementation;
- check future-Card leakage;
- produce ROADMAP_ALIGNMENT_GATE: PASS | BLOCKED.

If the gate is BLOCKED:

~~~
STOP
~~~

Do not implement during inspection.

## 8. Implementation Rules

Inside an approved Card:

~~~
one Card = one coherent goal
preserve existing ownership
preserve provider isolation
keep commercial calculations deterministic
keep model output untrusted
keep tool calls bounded
keep retries bounded
avoid unrelated refactors
avoid speculative infrastructure
do not implement future Cards
do not widen scope silently
~~~

A material architecture, scope, or technology change requires explicit human approval.

## 9. Commercial / Data / AI Safety

Before the canonical Guardrails file is migrated, enforce these minimum rules:

- missing estimated hours != zero;
- missing hourly rate != zero;
- currency must be explicit;
- hours and monetary units must be explicit;
- estimated and actual values must remain distinguishable;
- historical evidence must retain identity and provenance;
- synthetic data must remain explicitly synthetic;
- AI cannot invent historical outcomes;
- AI cannot invent rates;
- AI cannot override deterministic totals;
- AI cannot fabricate evidence;
- risk suggestions require evidence;
- invalid model output fails explicitly;
- Bedrock failure cannot silently produce a valid quotation;
- Excel totals must reconcile;
- final quotation requires human approval.

Unknown financially or commercially material semantics:

~~~
COMMERCIAL_SEMANTICS_UNVERIFIED
STOP
~~~

## 10. AI / Bedrock Boundary

AI may:

- understand a quotation request;
- choose approved tools;
- summarize;
- compare;
- interpret historical evidence;
- explain risks;
- draft narrative;
- surface uncertainty;
- surface missing information.

AI may not:

- invent rates;
- invent actual outcomes;
- calculate authoritative totals;
- override deterministic calculations;
- fabricate evidence;
- approve the final quotation;
- bypass human approval;
- redefine source verification status.

Model output is untrusted until parsed and validated.

Expected failure states include:

~~~
AI_UNAVAILABLE
AI_INVALID
INSUFFICIENT_EVIDENCE
~~~

## 11. Agent Boundary

The Quotation Agent must be a genuine tool-using component.

Planned tool categories include:

~~~
historical quote retrieval
similar quote retrieval
deterministic statistics
estimate-vs-actual comparison
risk evidence
draft generation
draft validation
Excel generation
~~~

The agent must not hide deterministic business logic inside prompts.

## 12. Human Approval Boundary

Required flow:

~~~
Agent Draft
→ Deterministic Validation
→ Human Review
→ Approve / Reject
→ Final Excel Export
~~~

No alternative autonomous finalization path is allowed.

## 13. Provider Isolation

Required direction:

~~~
Core
→ AI Provider Contract
→ Bedrock Adapter
→ Amazon Bedrock

Core
→ Storage Contract
→ S3 Adapter
→ Amazon S3
~~~

Core must not depend directly on:

- boto3 response dictionaries;
- Bedrock SDK response objects;
- S3 SDK objects;
- API transport models;
- UI models.

## 14. Validation and Evidence

Validate narrow to broad as applicable:

~~~
syntax/import/static contract
focused unit test
component/contract test
integration test
commercial/data invariant
AI/tool failure test
relevant regression
runtime/degraded-path test
Card evaluation
exact Exit Gate
CARD_QUALITY_GATE
~~~

Rules:

~~~
test not run != PASS
static inspection != runtime verification
design intent != implementation evidence
merge != COMPLETE
failure is evidence
~~~

Once migrated, update QUOTATION_CARD_EVIDENCE_MAP.md incrementally with actual results only.

Never invent:

- commands;
- source paths;
- runtime results;
- Git state;
- test results;
- AWS state;
- evidence.

## 15. Independent Verification Principle

For high-impact Cards or changes, final verification should be independently checkable.

Prioritize this for:

- commercial calculations;
- risk evidence;
- AI authority boundary;
- human approval enforcement;
- Excel reconciliation;
- security;
- Golden Case;
- deployment and release.

A verifier must be able to return BLOCKED.

## 16. Checkpoint / Recovery

Use:

~~~
Action
→ State Change
→ Versioned Checkpoint
→ Validation
→ Accept or Rollback
~~~

After context loss, resume from:

~~~
PROJECT_PROFILE.md
PROJECT_CONTROL.md
Roadmap
active Card contract
active Card evidence
repository
Git
~~~

Never resume from chat memory alone.

If the safe resume point cannot be proven:

~~~
PROJECT_STATE_CONFLICT
STOP
~~~

## 17. Approval Boundaries

Explicit human approval is required for:

~~~
Card start
next Card
material scope change
material architecture change
significant technology addition
destructive/sensitive operation
secret/credential-sensitive action
external write/action capability
commit
push
PR
merge
release/deploy
~~~

Routine reversible implementation may proceed only inside an already approved Card and scope.

## 18. Git

Until Git is initialized:

~~~
Git state is NOT_AVAILABLE.
~~~

After Git exists, follow GIT_WORKFLOW.md once migrated.

Never by default:

~~~
work directly on main
force push
rewrite shared history
commit secrets
mix unrelated work
auto-merge
auto-start next Card
~~~

## 19. Card Closure

A Card is COMPLETE only when:

~~~
exact Card contract satisfied
exact Exit Gate proven
required tests/evaluations PASS
applicable commercial/data/AI/security invariants PASS
Evidence current
Learning Record complete
CARD_QUALITY_GATE: PASS
repository/Git reviewed
required approved delivery complete
PROJECT_CONTROL reconciled
~~~

Then:

~~~
Card = COMPLETE
Active Card = NONE
STOP
~~~

Do not start the next Card without separate explicit human approval.

## 20. Current Migration State

~~~
Project Phase: V1_C01_AUTHORIZED
Governance: COMPLETE
Strict Governance Audit: PASS
Learning Governance: COMPLETE
Learning Governance Final Audit: PASS
PROJECT_PROFILE.md: MIGRATED / CANONICAL
PROJECT_CONTROL.md: CURRENT / HARDENING RECONCILIATION IN PROGRESS
AGENTS.md: CURRENT FILE
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md: CANONICAL ROADMAP
COMMERCIAL_AND_DATA_GUARDRAILS.md: MIGRATED / CANONICAL
QUOTATION_CARD_SPECIFICATIONS.md: MIGRATED / CANONICAL
QUOTATION_CARD_EVIDENCE_MAP.md: MIGRATED / CANONICAL
CARD_LEARNING_AND_DECISION_LOG.md: MIGRATED / CANONICAL
SOURCE_ADAPTATION_TRACEABILITY.md: CREATED / CANONICAL
GOVERNANCE_HARNESS_PROOF_CASES.md: CREATED / CANONICAL; FORMAL CASES NOT EXECUTED
QUOTATION_ENGINEERING_HARNESS.md: MIGRATED / CANONICAL
GIT_WORKFLOW.md: MIGRATED / CANONICAL
.agents/skills/quotation-card-execution/SKILL.md: MIGRATED / CANONICAL
scripts/quotation_session_bootstrap.sh: MIGRATED / CANONICAL
Application Implementation: NOT_STARTED
Active Card: V1-C01 — Repository Baseline
C01 Authorized: YES
Git repository: YES
Current branch: main
HEAD: 9e44dac3d69740b2f415d9ec728626553bc4e933
Remote: origin → https://github.com/jo-soroush/ai-quotation-intelligence.git
Tracking: main → origin/main
Current source adaptation records: NONE
Historical source/template material is not canonical project authority.
Proof cases executed: 0
Proof cases PASS: 0
Proof cases NOT_EXECUTED: 18
Executable proof suite: NOT_CREATED
~~~

## 21. Required STOP Codes

~~~
PROJECT_STATE_CONFLICT
CARD_MISMATCH
CARD_SCOPE_MISMATCH
CARD_DEPENDENCY_MISMATCH
DUPLICATE_IMPLEMENTATION
FUTURE_CARD_LEAKAGE
ROADMAP_ALIGNMENT_GATE_BLOCKED
REQUIREMENT_REGRESSION
COMMERCIAL_SEMANTICS_UNVERIFIED
COMMERCIAL_INVARIANT_FAILED
AI_BOUNDARY_VIOLATION
AI_INVALID
AI_UNAVAILABLE
INSUFFICIENT_EVIDENCE
EXCEL_RECONCILIATION_FAILED
SECURITY_BOUNDARY_VIOLATION
REQUIRED_VALIDATION_FAILED
REQUIRED_APPROVAL_MISSING
~~~

## 22. Final Operating Rule

~~~
PROMPTS REQUEST WORK.
CANONICAL PROJECT STATE DEFINES TRUTH.
INSPECT BEFORE WRITE.
ONE CARD AT A TIME.
DETERMINISTIC SOFTWARE OWNS COMMERCIAL TRUTH.
AI INTERPRETS AND DRAFTS.
EVIDENCE BEFORE RISK CLAIMS.
VERIFY BEFORE CLAIM.
HUMAN APPROVAL BEFORE FINALIZATION.
CARD COMPLETE → STOP.
NEXT CARD → NEW HUMAN APPROVAL.
~~~

Additional constraints:

- Do not use legacy domain terminology.
- Do not claim any application implementation exists.
- Do not treat the existing Git baseline as evidence that application implementation exists.
- Do not claim tests passed.
- Do not create future canonical files.
- Do not rename legacy files yet.
- Do not modify PROJECT_PROFILE.md.
- Do not modify PROJECT_CONTROL.md.
- Do not modify the Roadmap.
- Do not modify PROJECT_MIGRATION_STATUS.md.
- Modify AGENTS.md only.
