# AI Quotation Intelligence System — V1 Card Learning and Decision Log

Status: CANONICAL EDUCATIONAL ENGINEERING RECORD
This file owns rationale, alternatives, root causes, fixes, tradeoffs, and
historical learning. It does not own live phase, Active Card, authorization,
runtime Git state, implementation evidence, or Card contracts.
Read PROJECT_CONTROL.md for live operational state and query Git for runtime
Git facts.

## Role and Ownership

This file is the long-term educational and engineering rationale log for all V1 Cards.

It owns design rationale, technology rationale, alternatives considered, implementation narrative, failure and root-cause explanation, recovery explanation, lessons learned, and future reminders.

It does not own live project state, Card authorization, architecture authority, implementation evidence, Git state, test truth, AWS truth, or Card contracts.

QUOTATION_CARD_SPECIFICATIONS.md defines what each Card plans to do.
QUOTATION_CARD_EVIDENCE_MAP.md records what was actually proven.
PROJECT_CONTROL.md records live state and authorization.

## Educational Record Standard

Every completed Card should eventually explain what changed, why it was necessary, what existed before, which decision was made, why it was appropriate, which alternatives were considered, what failed, why it failed, how it was fixed, what evidence proved the result, what was learned, what a future maintainer should remember, and how the result affects later Cards.

Failures must not be erased after recovery. Later records should preserve the problem, observed behavior, expected behavior, root cause, fix, validation, and remaining limitation.

For a repeated or structural failure, use the existing Card sections to record
the Problem, Root Cause, Why Existing Controls Missed It, Fix, Prevention Rule,
and evidence that the recurrence path is closed. A passing rerun alone does
not explain why the original control missed the defect. Do not create a
separate root-cause ledger or rewrite completed Card history for this policy.

Material decisions should later record their context, chosen option, alternatives, tradeoffs, evidence references, and future revisit condition. Technology decisions should later explain purpose, need, alternatives, complexity, operational cost, portability, and replacement conditions.

This file references evidence; it does not duplicate raw command output or test output.

## Architecture Change Capture

When a Card materially changes system architecture, boundaries, component
ownership, dependency direction, provider abstraction, deployment topology,
or data flow, its existing learning-record fields must capture:

```text
Architecture Before:
Change Introduced:
Architecture After:
Why Changed:
Affected Components:
Boundary / Dependency Impact:
Tradeoff / Limitation:
Future Revisit Condition:
```

This applies only when the Card materially changes architecture. Examples
include introducing an application layer, adding or removing an adapter
boundary, changing ownership between Core and infrastructure, adding a
provider abstraction, changing data flow, introducing persistent storage or
an API/service boundary, changing deployment topology or dependency
direction, or moving responsibility between deterministic software and the
AI layer. Trivial file moves, naming cleanup, formatting, and isolated
implementation details are not architecture changes.

Use the existing Card sections rather than adding a new numbered section:

```text
Key Design Decisions → Architecture Before, Change Introduced, Architecture After
Why We Chose This Approach → Why Changed and the architecture rationale
Tradeoffs and Limitations → cost, complexity, coupling, portability, and operational impact
Impact on Later Cards → downstream effects, constraints, and Future Revisit Condition
```

PROJECT_PROFILE.md remains the owner of stable and current canonical
architecture. This file owns the historical explanation of how architecture
changed and why; it does not replace architecture authority or duplicate
long architecture documentation. If a real failure or limitation causes an
architecture change, preserve the observed problem, root cause, decision,
Architecture Before, Architecture After, fix or recovery, tradeoff, and
validation reference. Do not erase the failed architecture context.

No Architecture Before or Architecture After state is to be fabricated
before implementation. Current Cards have no implemented architecture
change, and their existing post-implementation placeholders remain
unfilled.

## Completion Relationship

A Card is educationally complete only when implementation evidence exists, applicable failure and fix history is recorded, design and technology rationale are recorded, tradeoffs and limitations are recorded, What We Learned is complete, and future reminders are recorded.

This file alone does not mark a Card COMPLETE. Card completion remains governed by QUOTATION_CARD_SPECIFICATIONS.md, QUOTATION_CARD_EVIDENCE_MAP.md, QUOTATION_ENGINEERING_HARNESS.md, and PROJECT_CONTROL.md.

## AEVS v1.1 Bounded Remediation Learning (Governance Only)

The Phase 1 implementer self-audit reported PASS; the independent Claude
Code audit later reported FAIL (M-01, M-02, M-03). This remediation addresses
those findings without changing C01–C08 application behavior. Independent
re-audit of the changed candidate remains pending.

The subsequent independent re-audit reported FAIL: M-01 and M-03 CLOSED,
M-02's direct escape probes CLOSED, and new M-04 OPEN. These are independent
reported outcomes, not a PASS for the current candidate.

M-01 — Problem: new package modules, including re-export `__init__.py` files,
could escape the architecture check. Root Cause: the test iterated a manual
Core file list rather than comparing it with discovered package files. Why
Existing Controls Missed It: the docstring told future maintainers to
register modules, but no assertion enforced registration. Fix: discover all
package Python files and require exact architectural classification. Prevention
Rule: a Card adding, moving, or reassigning a module updates classification,
while an omission fails automatically. Evidence Recurrence Path Is Closed in
local verification: isolated new-module and new-package tests fail on missing
classification; `tests/test_architecture.py` passed 12 tests. Independent
confirmation is still pending.

M-02 — Problem: realistic provider, agent/tool, and API namespaces could pass
through the old forbidden-name matcher. Root Cause: a short token blacklist
encoded names rather than dependency direction. Why Existing Controls Missed
It: the original self-test exercised only a few exact tokens and did not
challenge every prohibited category. Fix: resolve imports to discovered,
classified package modules; Core cannot depend on PROVIDER, AGENT_TOOL, or
APPLICATION_BOUNDARY modules, and boto3/botocore remain external SDK
restrictions. Prevention Rule: each prohibited category has an isolated
counterexample test; future modules must be classified. Evidence Recurrence
Path Is Closed in local verification: provider adapter, agent tools,
quotation agent, tooling package, API, and SDK probes all failed as expected;
independent confirmation remains pending. Static imports are the limit of
this control.

M-03 — Problem: a verifier PASS tied to filenames/diff description could be
reused after same-path content changed. Root Cause: the candidate had no
deterministic content identity. Why Existing Controls Missed It: the policy
used an ambiguous “substantive” change exception and did not mechanically
compare audited and delivery candidates. Fix at that stage: compute a read-only SHA-256
identity over base revision, branch, path/status/mode/content manifest;
compare it with the independent verifier's reported identity before delivery
and again after approved staging. Prevention Rule: any candidate-content
change invalidates the prior independent PASS, without an implementer
self-exemption. Evidence Recurrence Path Is Closed in local verification:
isolated Git fixtures changed content at the same path, added an untracked
file, deleted a file, and changed the base revision; each changed the
identity. Unchanged and staged-equivalent candidates remained stable.
Independent confirmation remains pending. The verifier's identity stays
outside pre-delivery candidate files to avoid a self-referential hash.

M-04 — Problem: Core could import a Support re-export of Provider, Agent Tool,
or Application Boundary without the architecture test failing. Root Cause:
the checker classified all modules but inspected outbound imports only from
Core. Why Existing Control Missed It: the visible Core edge ended at allowed
Support; `_local_category()` did not inspect Support's own import. Fix: validate
static outbound imports from every classified module against a category
dependency policy. Core permits Core/Support, Support permits only Support,
and the current Provider permits Core/Support. Future Agent Tool and
Application Boundary directions remain empty until their owning Cards decide
them. A separate policy reachability check rejects a weakened Support policy
that would make a forbidden category reachable from Core. Prevention Rule:
classify every module and reject every forbidden static local edge, including
`__init__.py` re-exports; retain isolated laundering counterexamples. Local
focused proof passed for all three forbidden Support chains, a Support package
re-export, legitimate Core-to-Support and Support imports, and the policy
self-test. This is static import evidence only; dynamic imports, runtime
object/value leakage, and semantic misuse remain outside this control.
Independent M-04 re-audit: PENDING.

Branch/identity delivery blocker — A later independent AEVS audit was reported
PASS for the exact candidate identity
`24fcc567464a755fa68e373fbc6b1bc38c31b7113cd8dae590ebaaa1afd614cd`,
and human delivery approval was supplied. Delivery correctly STOPPED before
staging: the identity included the branch name, so an unchanged candidate
would acquire a different hash on the required delivery branch. This was a
candidate-provenance modeling error, not a failure of the architecture fix.
Root Cause: branch/workspace location was mixed into the hashed content
manifest. Why Existing Controls Missed It: tests challenged file and base
changes but did not challenge a branch-only move. Fix: hash schema, base, and
exact candidate path/status/mode/content entries; report branch separately as
provenance. An isolated Git test now switches from `main` to a delivery branch
without changing identity, while a one-byte edit and staged/worktree drift
still fail verification. Alternative rejected: special-casing branch names or
committing directly on `main`, which would weaken the model or bypass the
documented workflow. Prevention Rule: every audited candidate identity must
be stable across an explicitly approved branch-only transition, then be
recomputed before staging and verified again after staging. The base revision
remains hashed. Local tests passed; this changed candidate requires a new
independent audit and new human delivery approval. No delivery occurred.

M-05 — A fresh independent branch/identity re-audit verified the branch-only
design but reported that `--require-staged` could PASS despite unaudited index
content under skip-worktree, assume-unchanged, clean filters, or
`core.fileMode=false`; the verifier reproduced an unaudited commit after a
false PASS. Root Cause: the previous staged check inferred index equivalence
from porcelain worktree diff and visible untracked state, while Git commits
the index rather than worktree bytes. Why Existing Control Missed It: normal
staging tests challenged ordinary drift, not Git local-state controls that
hide or transform the staged blob or mode. Fix: retain one canonical
schema/base/path-status-mode-content identity, but derive it directly from
worktree, index, and committed tree sources. Read index blobs/modes from Git
plumbing, fail on candidate skip-worktree/assume-unchanged flags, and require
both audited worktree and index identities before commit. Verify the committed
HEAD tree against the same audited identity before push. The rejected
alternative was a procedural warning against index flags or another porcelain
diff check; neither proves committed bytes. Direct blob inspection costs extra
I/O but keeps the proof deterministic and auditable. Prevention Rule: exact
candidate provenance has three checkpoints—worktree before staging, index
before commit, committed tree before push—and any mismatch stops delivery.
Local fixture tests cover the reported bypasses and exact/inauthentic commits;
local self-review also caught a missing-new-worktree-file omission in the
initial scan, which was changed to an explicit failure and regression-tested.
Independent M-05 re-audit remains PENDING. No application behavior or C09
state changed.

Technical commands and observed results are in QUOTATION_CARD_EVIDENCE_MAP.md
section 2B. This historical learning record is not a second live-state ledger
or a claim that the independent re-audit passed.

M-05b — Replace refs exposed a second object-identity boundary in the same
candidate verifier. Git's normal object-reading behavior follows
`refs/replace/*`; therefore `cat-file` could return audited replacement bytes
for an unaudited blob ID present in the index or committed tree. Independent
staged and committed fixtures demonstrated this: ordinary `cat-file` returned
the audited bytes and the pre-fix verifier falsely passed both candidates.
The root cause was using default Git object semantics for direct object reads.
The fix places `--no-replace-objects` in the shared Git invocation helper,
which applies uniformly to tree enumeration and blob reads across worktree
base, index, and committed-tree verification. A narrower per-call fix was
rejected because any missed object-read path would preserve the bypass.
After the change, the attack fixtures fail closed and exact staged/committed
content continues to pass; the focused candidate identity and architecture
suites report 21 and 19 passing tests. This keeps the existing single
schema/base/path/status/mode/content identity model. Lesson: object IDs alone
do not guarantee that Git plumbing returns the stored object when replacement
refs are enabled; security-sensitive verification must explicitly opt out of
that indirection on every Git operation. Independent M-05b re-audit later
reported PASS for the delivered candidate identity. No application behavior,
dependency, or C09 state changed.

AEVS v1.1 post-delivery provenance blocker — Problem: the independently
audited candidate had an approved commit and open PR #22, but delivery stopped
before merge because the workflow was understood to require the delivery
commit, PR, and merge identifiers in the Evidence Map before merging. Root
cause: the policy did not clearly separate candidate content, which exists
before audit and must remain frozen, from identifiers generated by later Git
actions. Requiring a merge SHA before merge can create an impossible
self-reference and can repeatedly invalidate an otherwise valid audit.

Fix: the Post-Delivery Provenance Rule in GIT_WORKFLOW.md,
QUOTATION_ENGINEERING_HARNESS.md, and the Card Execution Skill states that
future Git identifiers do not block the action that creates them. The final
delivery output reports actual observed provenance; if durable repository
history is needed, it is a separate retrospective maintenance change after
delivery. The maintenance candidate never needs to contain its own future
identifiers. Recursive evidence commits are prohibited. This was chosen over
editing PR #22's frozen candidate because such an edit would change its
independently audited identity. PROJECT_CONTROL remains the owner of live
state; the Evidence Map, Learning Log, GIT_WORKFLOW.md, Git, and final delivery
output retain their existing owners.

Prevention: future delivery-generated commit, PR, merge, and final-main
identifiers cannot be required in the candidate whose delivery creates them.
Governance regression GD-07 models a frozen candidate with independent PASS
and human approval while delivery identifiers are NOT_CREATED, verifies the
candidate stays unchanged as a separate observed delivery report is produced,
and rejects a contradictory policy requiring a merge SHA before merge.

Observed delivery evidence is recorded in QUOTATION_CARD_EVIDENCE_MAP.md
section 2B: PR #22 merged at `8a10c41023770ffcd3be13de93b3ccb1af838319` from
delivery commit `7d085c4f06bb556df1df4a1c41bd6e9a092da42d`, with audited
identity `f2da89985d748c0362533e1c2c252bcb50c151f6a6873ceef32d77d4dffd6c2a`.
The separate maintenance candidate records this history without requiring
its own commit or PR identifiers. No application code, dependencies, or C09
state changed.

Regression-fixture failure and repair: the first Phase B Governance Harness
run reported GD-07 FAIL (PASS=60, FAIL=1). The scenario had been built on the
repository lifecycle fixture, which intentionally has no approved candidate
snapshot; therefore its unchanged-candidate assertion could not pass. The
repair reused the existing isolated approval fixture and copied the canonical
workflow/Harness/Skill text into that temporary fixture. This keeps the case
within the current harness style and tests both the allowed lifecycle with
not-yet-created IDs and rejection of an injected merge-SHA precondition. The
full rerun passed 61 cases with zero failures. The failure and recovery are
preserved in the Evidence Map.

Independent governance audit then passed (Critical=0, High=0, Medium=0) but
raised a LOW GD-07 coverage finding. The original fixture tested one added
merge-SHA blocker; it did not prove that the policy would reject weakened
approval, frozen-content, staged/committed identity, self-reference,
recursion, or observed-provenance language. The root cause was treating one
negative example and broad text searches as a sufficient policy regression.
The bounded repair keeps the existing Harness/fixture architecture and the
canonical policy unchanged. GD-07 now checks the eight policy clauses by
their semantic roles, then rejects both replacement and contradictory-addition
mutants for seven independent failure classes. This dual style matters:
deleting a safeguard and adding an exception are different regressions, and
the latter can coexist with otherwise correct wording. The valid baseline and
all 14 mutants passed the focused GD-07 test. Independent re-audit of the new
governance candidate is PENDING; no delivery approval is inferred.

M-GD07 follow-up: a separate review found that the improved GD-07 still
scanned contradictions only inside GIT_WORKFLOW.md §13A. The Harness and
Skill passed merely by containing the rule name, and later workflow sections
were not checked for contrary exceptions. Thus the earlier mutation result
was valid for its fixtures but narrower than whole-surface protection. The
root cause was an early return for companion owners and a negative scan over
the extracted section rather than the complete policy text.

The bounded repair changes the GD-07 fixture/checker, not the canonical
policy. It keeps §13A's required clause roles, adds companion-owner safeguard
checks and PROJECT_CONTROL live-state ownership, then applies semantic
contradiction checks to the entire text of each owner. Each tested bad rule is
inserted in four locations; variants cover optional approval and identity
checks, a maintenance commit's own SHA, recursive Evidence Map updates,
advance-predicted merge provenance, and frozen-candidate editing. This is a
regression net for these policy relationships, not a general natural-language
proof of every conceivable wording. Independent re-audit remains PENDING.

M-GD07b re-audit failed with a MEDIUM coverage finding: only 11 of 51
independently phrased contradictions were detected, and `Expected merge SHA
may be written before merge.` passed at every location. The root cause was
trying to infer policy meaning from finite sentence-shape regexes. Adding
another collection of phrasings would improve a sample but leave the same
unbounded paraphrase problem and could reject valid safeguards as threats.

The chosen bounded fix treats the independently reviewed policy bytes as an
integrity boundary. GD-07 still checks the visible structural safeguards,
then compares the complete GIT_WORKFLOW.md, Harness, and Skill bytes against
their approved SHA-256 digests. Any edit, whether harmful, helpful, or merely
formatting, requires separate policy review and a deliberate digest update.
That conservative tradeoff is explicit: the Harness detects policy drift, not
the meaning of arbitrary English. The fixture exercises the audit's missed
wordings across eight locations and confirms protective additions also fail
closed for review. The canonical policy text and live-state ownership remain
unchanged. Independent re-audit of this candidate is PENDING.

## Historical C01 Completion Context

Application Implementation: V1-C01 BASELINE IMPLEMENTED / DOMAIN IMPLEMENTATION NOT_STARTED
Active Card at C01 completion: NONE
V1-C01 Start Authorization: GRANTED (historical; Card complete)
V1-C01 State: COMPLETE
GIT_DELIVERY_APPROVAL: GRANTED / CONSUMED — PR #1 merged
Git Repository at C01 delivery: YES
Branch at C01 delivery: main
Runtime Git state is not owned here; query Git and PROJECT_CONTROL.md for current state.
Remote at C01 delivery: origin → https://github.com/jo-soroush/ai-quotation-intelligence.git
Tracking at C01 delivery: origin/main; C01 delivered through PR #1; governance hardening delivered through PR #2

V1-C01 implementation learning is recorded below. No later Card learning record contains implementation claims.

## V1-C01 — Repository Baseline

### 1. Card

V1-C01 — Repository Baseline

### 2. What We Intended to Build

Create a professional, importable, testable, secret-safe repository and Python/application baseline without implementing quotation business logic.

### 3. Why This Card Exists

A clean ownership, configuration, packaging, and testing boundary is needed before domain implementation can be built and evaluated coherently.

### 4. What We Actually Built

Created the C01 repository baseline: `pyproject.toml`, a `src/ai_quotation_intelligence/` package with version, configuration, and standard-library logging boundaries, a three-test pytest baseline, README setup instructions, a trackable secret-free `.env.example`, and a `.gitignore` exception that preserves protection for real `.env` files. No quotation business logic or future-Card integration was added.

### 5. Key Design Decisions

Used a `src/` layout and `pyproject.toml` with no runtime dependencies. Pytest is a development-only dependency. Configuration is environment-backed through a small dataclass, and logging uses the Python standard library. `.env.example` is explicitly unignored while `.env` remains ignored.

### 6. Why We Chose This Approach

This keeps Core local-first and provider-neutral, establishes import/test/configuration ownership without inventing domain contracts, and keeps the dependency surface minimal. The `.env.example` exception was necessary because the existing `.env.*` rule otherwise ignored the safe example file.

### 7. Alternatives Considered

Considered adding Pydantic, FastAPI, boto3, openpyxl, or an external settings/logging framework; these were not needed for C01 and belong to later Card scope or would add unnecessary coupling.

### 8. Why Alternatives Were Not Chosen

Those additions would introduce future-Card dependencies or provider/API behavior before their contracts exist. Standard-library configuration and logging satisfy the C01 boundary with fewer dependencies.

### 9. Technologies / Libraries Used

Python 3.13.12 in the existing ignored `.venv`, `pyproject.toml`, setuptools editable packaging, pytest 8.4.2 for development tests, and Python standard-library `dataclasses`, `os`, and `logging`.

### 10. Why These Technologies Were Used

They provide the required package, configuration, logging, and test baseline while preserving provider neutrality and local execution. No AWS SDK, API framework, spreadsheet library, or agent framework is required by C01.

### 11. Problems Encountered

The existing local `.venv` did not contain pytest. The existing `.env.*` ignore rule also matched `.env.example`. Creating the dedicated branch initially failed in the sandbox because Git ref writes required escalation.

### 12. Root Cause

Pytest had not yet been installed into the pre-existing environment; `.gitignore` intentionally used a broad environment-file pattern; and the workspace sandbox did not permit writing `.git/refs` without escalation.

### 13. How We Fixed It

Declared pytest as a bounded development dependency and installed the project’s dev extra into `.venv`. Added `!.env.example` after the environment ignore patterns so only the safe example is trackable. Created the dedicated C01 branch, then recorded the human-approved commit `93d6bdbdc074687f366658c4ebddc43912b7571e` and push to its remote branch.

### 14. Validation / Evidence References

`QUOTATION_CARD_EVIDENCE_MAP.md` V1-C01: import/configuration check PASS; pytest PASS with 3 tests; structure PASS; secret tracking PASS; provider dependency boundary PASS; future-Card leakage PASS; `git diff --check` PASS; delivery commit and remote/upstream verification recorded.

### 15. Tradeoffs and Limitations

The baseline uses simple environment variables rather than a settings library, so richer validation belongs to a later contract. The human-approved C01 commit, push, PR #1, and merge are complete under the single GIT_DELIVERY_APPROVAL delivery step. CI, Docker, and business behavior remain absent by design.

### 16. What We Learned

The existing repository already had a pushed governance baseline, but that does not satisfy the C01 application baseline. A minimal standard-library Core is sufficient for package/configuration/logging ownership, while pytest can remain development-only.

The final C01 reconciliation exposed that detailed Card state and aggregate Current Card Table state had been updated independently. The root cause was the absence of a deterministic cross-section completion check. The repair added FINAL_CARD_STATE_CONSISTENCY_GATE and a dependency-free validator; its negative fixtures stop on contradictory state and the corrected repository passes.

Separate P3 governance maintenance found that the first regression-fixture
mutations did not match the actual table and summary text, so the negative
cases initially failed to exercise their intended contradictions. The root
cause was fixture assumptions instead of section-scoped field assertions. The
fixture mutations and validator table/summary checks were corrected; the final
temporary-fixture governance suite passed 23 of 23 cases. This is governance
regression evidence, not new V1 application implementation or C01 technical
evidence.

### 17. What Should Be Remembered Later

Keep `.venv/` and real `.env` files ignored. Review any future configuration dependency against the provider-neutral Core boundary. Do not treat this baseline as evidence that domain, AI, AWS, Excel, API, or evaluation work exists.

### 18. Impact on Later Cards

V1-C02 can add typed domain contracts inside the established package without changing the C01 configuration/logging boundary. Later Cards must add their own dependencies and validation only within their authorized scope.

## V1-C02 — Domain Models

### 1. Card

V1-C02 — Domain Models

### 2. What We Intended to Build

Create typed quotation-intelligence domain contracts with explicit hours, currency, estimated-versus-actual semantics, numeric validation, null-versus-zero meaning, and provenance boundaries.

### 3. Why This Card Exists

Shared typed semantics prevent later calculation, evidence, AI, API, and storage components from inventing incompatible meanings.

### 4. What We Actually Built

Implemented a provider-neutral `domain` package containing strict Pydantic contracts for Money, Hours, Quote, QuoteItem, ProjectOutcome, HistoricalQuote, NewQuoteRequest, VarianceResult, SimilarQuote, RiskEvidence, RiskSuggestion, DraftQuote, ApprovalDecision, AgentRequest, and AgentResult. The models validate shape, required fields, explicit units/currency, non-negative numeric values, status boundaries, nested currency consistency, provenance, and serialization. They do not calculate totals, compare history, retrieve records, analyze risk, invoke AI, or persist data.

### 5. Key Design Decisions

The domain package is the Core owner of quotation concepts. `Money` keeps amount and currency together; `Hours` keeps the time unit explicit; estimated and actual values are separate optional fields so missing actuals remain unknown. Strict extra-field rejection prevents accidental provider payloads from becoming domain state. Drafts cannot be approved or contain an approved nested quote, and evidence/suggestion records require explicit source identifiers. Historical quote provenance must agree with the nested quote provenance.

### 6. Why We Chose This Approach

Pydantic 2 was selected because the C02 contract explicitly requires Pydantic contracts and it provides deterministic validation plus JSON round-tripping without introducing an API or provider framework. Decimal is used for monetary and measured values to avoid binary floating-point representation in the contract layer. Standard-library datetime and enums keep the Core provider-neutral.

### 7. Alternatives Considered

Alternatives considered were plain dataclasses, unconstrained dictionaries, and a larger domain framework. Plain dataclasses would require separately rebuilding validation and serialization; dictionaries would not provide stable contracts; a larger framework would add scope and dependencies without C02 need.

### 8. Why Alternatives Were Not Chosen

The selected approach satisfies the explicit Pydantic requirement while keeping the package independent of FastAPI, AWS SDKs, Bedrock, S3, persistence, and calculation services. Later Cards can consume these contracts without making the models responsible for their behavior.

### 9. Technologies / Libraries Used

Pydantic 2 (`pydantic>=2.0,<3.0`) was added as the sole runtime dependency. Pytest remains the existing development dependency. No provider, API, persistence, data-generation, or agent dependency was added.

### 10. Why These Technologies Were Used

Pydantic was required by the canonical C02 Roadmap contract. The existing pytest setup was retained so the baseline and C02 behavior run through one command.

### 11. Problems Encountered

The first C02 test run failed because a fixture assumed lowercase currency would be normalized, while the contract intentionally requires an explicit uppercase three-letter code. A governance regression run also failed five cases because its temporary fixtures copied mutable active-C02 state instead of a committed completed-C01 baseline. The pre-delivery audit then exposed two cross-model validation gaps and one contradictory live-state label.

### 12. Root Cause

The currency fixture was corrected to use the explicit contract form. The governance fixture builder was changed to source fixtures from committed `HEAD`, isolating regression scenarios from the live Card state while continuing to invoke the real validator. Model-level validators now reject approved nested drafts and mismatched historical provenance; PROJECT_CONTROL now has one C02 lifecycle state.

### 13. How We Fixed It

`.venv/bin/pytest -q` passed before these targeted repairs with 9 tests and passed after the repairs with 14 tests. New regression tests cover allowed and approved-nested drafts plus consistent REAL/SYNTHETIC and mismatched provenance. Model import, configuration loading, JSON serialization, negative-hours rejection, nested-currency rejection, shell syntax, `git diff --check`, and the governance suite passed. The governance suite reported 23/23 cases passing after the fixture fix. The C02 READY_FOR_DELIVERY consistency validator also passed after reconciliation.

### 14. Validation / Evidence References

Evidence is recorded in the V1-C02 section of QUOTATION_CARD_EVIDENCE_MAP.md. Historical validation events include the initial 9-test run and the post-repair 14-test run; the governance regression suite completed with 23 passed cases before the generated-view cases were added. The Evidence Map is authoritative for the latest observed result. C02 was delivered through commit `0dfd38a5b3d201052b4dea930becc96c6927225e`, PR #4, and merge commit `164ae7c3982009025ec16de72cd0d4ad1efc646d`.

### 15. Tradeoffs and Limitations

Decimal and explicit currency/unit wrappers improve safety but leave arithmetic and currency conversion to later Cards. Cross-model validators are necessary where a valid nested object can still form an invalid aggregate. Some concepts remain intentionally permissive because their business semantics belong to later calculation, comparison, risk, agent, and approval Cards.

### 16. What We Learned

C02 demonstrated that stable contracts should encode boundaries without embedding use-case behavior. Keeping estimates, actuals, provenance, and evidence links explicit prevents later services or models from silently inventing commercial truth. Field-by-field validity is insufficient: nested state and cross-model provenance must also be checked. Governance views that can change must be generated from PROJECT_CONTROL.md and exact Card evidence sections; mutable latest results belong in the Evidence Map, while this log preserves historical events and learning.

The governance suite later exposed that fixture setup had been inheriting the live Card lifecycle from `HEAD`. The permanent repair introduced an explicit temporary-repository fixture builder and isolated Git initialization; HF-01 through HF-08 now prove that scenario state, filesystem paths, and Git diagnostics remain independent of the live repository.

### 17. What Should Be Remembered Later

C02 supplies the typed foundation for C03 synthetic history and later deterministic services. Do not add calculation, retrieval, risk, AI, persistence, API, or export behavior to these models for convenience; extend a contract only when the owning Card and canonical specification require it.

### 18. Impact on Later Cards

C03 can build synthetic historical records against these contracts. Later Cards can consume stable provider-neutral types while retaining ownership of calculations, comparison, retrieval, risk, agents, approval, export, API, and persistence. C03 remains unstarted and unauthorized.

## V1-C03 — Synthetic Historical Data

### 1. Card

V1-C03 — Synthetic Historical Data

### 2. What We Intended to Build

Create approximately 40 meaningful synthetic historical quotation cases with multiple work items, explicit provenance, and controlled estimate-versus-outcome patterns.

### 3. Why This Card Exists

Historical comparison and risk evidence require repeatable portfolio data while protecting confidential information and avoiding meaningless random noise.

### 4. What We Actually Built

Built `ai_quotation_intelligence.data.synthetic_history`, a deterministic in-memory generator of 40 fictional `HistoricalQuote` records. Each record contains three work items, estimated item hours and rates, an observed actual-hours outcome, explicit synthetic provenance, a source identifier, and controlled outcome context.

### 5. Key Design Decisions

The generator owns data construction only. C02 `HistoricalQuote`, `Quote`, `QuoteItem`, `Hours`, and `Money` remain the validation boundary; no parallel schema or authoritative total calculation was introduced.

### 6. Why We Chose This Approach

Standard Python collections, `datetime`, `Decimal`, and the existing Pydantic domain contracts were sufficient. A fixed ordered pattern catalog and deterministic case numbering provide reproducibility without a random seed or external dependency.

### 7. Alternatives Considered

Alternatives were a checked-in static JSON dataset, seeded random generation, or a larger data-factory dependency.

### 8. Why Alternatives Were Not Chosen

Static JSON would duplicate schema construction and weaken direct contract validation; random generation would make controlled business patterns harder to inspect; a dependency would add no value for this local foundation. The small explicit catalog keeps the records reviewable and repeatable.

### 9. Technologies / Libraries Used

Python standard library plus the existing Pydantic C02 contracts. No AWS, Bedrock, FastAPI, persistence, or analytics library was added.

### 10. Why These Technologies Were Used

The standard library and existing domain contracts were enough to express deterministic dates, Decimal quantities, and nested validation without provider coupling.

### 11. Problems Encountered

The independent pre-delivery audit found that the initial `under_estimate` rows had actual hours below estimated hours, reversing their meaning. It also found that the first pattern test asserted labels and counts but not numeric relationships.

### 12. Root Cause

The root cause was an incorrect pair of deterministic template values combined with label-only regression coverage. The generator remained within scope; the defect was in dataset semantics, not a C04 calculation requirement.

### 13. How We Fixed It

The repaired generator uses actual-hours values above estimated hours for under-estimate and overrun patterns, below estimates for over-estimate, and within five hours for near-estimate. Five focused C03 tests now prove these relationships, alongside 40 unique valid records, multi-item structure, synthetic provenance, deterministic repeatability, and estimated/actual separation. The implementation was delivered in commit `204147915fcab7e2e161e083230b0b56cb2f97e0` through PR #7 and merged to `main` as `9fd7673bbb31167857f8d8f5f468d5631cde302d`; the outcome-only reconciliation recorded C03 as complete without changing the validated dataset.

### 14. Validation / Evidence References

The generator is intentionally in-memory and does not persist a file. Pattern labels and supplied outcomes are controlled data fixtures for later analysis, not analysis itself; C04 arithmetic and C05 comparison remain future work.

### 15. Tradeoffs and Limitations

Keep synthetic provenance on both `HistoricalQuote` and nested `Quote`, and continue validating generated records through the C02 models. Do not replace explicit observed outcomes with calculations in C03.

### 16. What We Learned

The generated contracts are intended as inputs for C04 calculation and later comparison, retrieval, risk, agent, approval, export, API, and storage Cards without implementing those behaviors early.

### 17. What Should Be Remembered Later

Synthetic provenance is a cross-model invariant: both the historical record and nested quotation must remain explicitly synthetic. Keep generated outcomes as observed fixture values and leave authoritative arithmetic to C04.

### 18. Impact on Later Cards

C04 can consume the estimated item hours and rates without inheriting a calculation engine. C05 and later Cards can use the controlled labels and outcome fields for comparison and evidence work, while C06+ behavior remains outside this Card. C04 still requires separate human authorization.

## V1-C04 — Quote Calculation Engine

### 1. Card

V1-C04 — Quote Calculation Engine

### 2. What We Intended to Build

Implement deterministic, authoritative quotation arithmetic for validated hours, rates, item costs, totals, and reconciliation.

### 3. Why This Card Exists

Commercial truth must be reproducible and must remain outside AI output so that quotations cannot depend on model arithmetic or silent coercion.

### 4. What We Actually Built

Implemented `ai_quotation_intelligence.calculation` with deterministic `calculate_item_cost`, `calculate_quote_total`, and `calculate_quote` functions over the existing C02 `QuoteItem`, `Quote`, and `Money` contracts. Item cost is estimated hours multiplied by hourly rate; quote totals are derived by summing those item costs. The implementation does not mutate inputs and performs no historical analysis, provider calls, or workflow orchestration.

### 5. Key Design Decisions

The calculation module is separate from, but directly consumes, the C02 domain package. Decimal values are multiplied and summed without float conversion. A supplied estimated total is checked against the derived total rather than trusted as an independent arithmetic source. Existing C02 validation remains responsible for non-negative values, explicit units, explicit currency, required items, and mixed-currency rejection.

### 6. Why We Chose This Approach

C04 owns commercial arithmetic because deterministic code must remain the source of quotation truth. Keeping this responsibility in a small provider-neutral module makes the result reusable by later Cards without placing calculations in prompts, agents, data generation, APIs, or UI code.

### 7. Alternatives Considered

Alternatives were floating-point arithmetic, mutating the input Quote, accepting a supplied total without reconciliation, or introducing a duplicate C04 quotation schema. Each would weaken numeric safety, traceability, or the C02 ownership boundary.

### 8. Why Alternatives Were Not Chosen

The contract requires Decimal-safe deterministic arithmetic and reuse of C02 models. No rounding or currency-conversion policy is defined, so neither behavior was invented.

### 9. Technologies / Libraries Used

Python standard-library `decimal.Decimal` and the existing Pydantic C02 models. No new dependency was added.

### 10. Why These Technologies Were Used

Decimal preserves the exact monetary semantics already established by C02, while ordinary Python functions keep the engine deterministic and provider-neutral.

### 11. Problems Encountered

The independent audit found that the implementation behavior was correct, but focused tests did not explicitly cover missing required inputs or non-finite Decimal values. The main design risk was allowing an independently supplied total to diverge from item arithmetic; the implementation and regression test explicitly guard that boundary.

### 12. Root Cause

The potential inconsistency was a contract-boundary risk: Quote permits an optional supplied estimated total while C04 must own the authoritative calculation. Treating that field as an assertion resolves the risk without changing C02.

### 13. How We Fixed It

The engine derives each item cost, sums the derived costs, and rejects a supplied estimated total that does not exactly reconcile. The audit coverage gap was fixed by adding explicit missing-hours, missing-rate, and NaN/Infinity/-Infinity rejection tests. Focused tests now cover one and multiple items, Decimal precision, zero values, invalid inputs, currencies, determinism, and reconciliation.

### 14. Validation / Evidence References

Focused C04 tests passed 9 tests; the full suite, reconciliation gate, governance regression, bootstrap, shell/Python syntax checks, and C04 READY_FOR_DELIVERY validator were run after the coverage repair. Exact observed results are recorded in the C04 Evidence Map section.

### 15. Tradeoffs and Limitations

C04 intentionally calculates estimated costs only. It does not add rounding, FX conversion, actual-vs-estimate variance, pricing strategy, or historical interpretation because those semantics are not part of the exact C04 contract.

### 16. What We Learned

Commercial arithmetic should be simple, deterministic, and independently testable. A total is safer when it is structurally derived from item results, and a pre-existing total must be reconciled rather than silently accepted.

### 17. What Should Be Remembered Later

Do not move authoritative arithmetic into later AI or agent layers. Later Cards may consume the calculated Quote, but comparison and evidence analysis must remain separate responsibilities.

### 18. Impact on Later Cards

C05 can compare validated estimated and observed historical values without reimplementing C04 arithmetic. C06+ Cards can consume stable totals while remaining outside this engine’s scope.

C04 delivery outcome: delivered through commit `266884504a40584d9d7497a648beb1268c8f827f`, PR #9, and merge commit `3ed46f0ce81ccf502e5d2833ce2e7e9a33c1801b`. Outcome-only reconciliation moved C04 to COMPLETE and cleared the Active Card; V1-C05 remains unauthorized.

## V1-C05 — Historical Comparison Engine

### 1. Card

V1-C05 — Historical Comparison Engine

### 2. What We Intended to Build

Compare historical estimates with actual delivery outcomes deterministically, including explicit hour and cost variance, percentage semantics, aggregates, and scope-change context.

### 3. Why This Card Exists

Grounded quotation intelligence requires reproducible historical comparison that preserves missing outcomes and distinguishes scope-driven overruns from ordinary estimation variance.

### 4. What We Actually Built

Implemented deterministic historical comparison over validated C02/C03 contracts. The comparison produces per-record hour variance, optional cost variance, percentage variance where the estimate is non-zero, scope-change context, and deterministic aggregate summaries.

### 5. Key Design Decisions

The comparison module reuses `HistoricalQuote`, `VarianceResult`, and the C04 `calculate_quote_total` function. Variance is defined as actual minus estimate, so positive values represent overruns and negative values represent underruns. Missing actual outcomes remain `None`; actual cost is never inferred from hours.

### 6. Why We Chose This Approach

Deterministic comparison keeps historical evidence reproducible and prevents later AI layers from becoming the source of variance truth. C04 remains responsible for estimated-cost arithmetic, while C05 interprets validated historical outcomes.

### 7. Alternatives Considered

Alternatives considered were embedding comparison in the C04 calculation engine, inferring actual cost from actual hours, adding similarity ranking, or returning untyped dictionaries.

### 8. Why Alternatives Were Not Chosen

Those alternatives would mix Card ownership, fabricate unavailable commercial evidence, introduce C06 behavior, or weaken typed contracts.

### 9. Technologies / Libraries Used

Python standard-library `Decimal`, `dataclasses`, and the existing Pydantic domain models. No dependency was added.

### 10. Why These Technologies Were Used

Decimal preserves exact variance and aggregate arithmetic; frozen dataclasses provide stable provider-neutral result boundaries without creating parallel quotation schemas.

### 11. Problems Encountered

No implementation failure was observed. The main design issue was separating missing actual cost from calculable estimated cost; this was handled by making cost variance optional and validating currency only when actual cost exists.

### 12. Root Cause

The C03 records intentionally contain observed actual hours but no actual cost. Inferring cost would silently create evidence, so cost comparison requires a validated `ProjectOutcome.actual_cost`.

### 13. How We Fixed It

The implementation computes hour variance directly, delegates estimated total calculation to C04, preserves missing outcomes, rejects actual-cost currency mismatch, and aggregates positive variance counts plus Decimal average/median values.

### 14. Validation / Evidence References

The independent C05 audit identified a regression-coverage gap: implementation aggregates had no explicit even-count median or cost-variance aggregate tests. Two numeric regression tests were added, covering the two-middle-value median, Decimal average cost variance, Decimal median cost variance, and exclusion of missing actual cost. Focused C05 tests then passed 10 tests; the full suite passed 40 tests. The broader tests cover variance direction, percentage and zero-denominator semantics, cost variance, missing outcomes, Decimal validation, C03 integration, immutability, deterministic repeatability, and currency mismatch.

### 15. Tradeoffs and Limitations

The implementation deliberately does not provide similarity ranking, retrieval, risk scoring, AI interpretation, or infrastructure. Cost variance is unavailable when actual cost is absent, and no rounding policy was invented.

### 16. What We Learned

Comparison must preserve the distinction between unavailable evidence and zero variance. Positive/negative direction tests are essential because a numerically valid formula can still have reversed meaning.

### 17. What Should Be Remembered Later

Future maintainers must keep C04 as the only estimated-cost arithmetic authority and must not turn C05 filtering or summaries into C06 similarity retrieval.

### 18. Impact on Later Cards

C05 provides deterministic variance evidence for C06 and C07 without implementing retrieval or risk decisions. Later Cards can consume its typed results and explicit missing-data behavior.

## V1-C06 — Similar Quote Retrieval

### 1. Card

V1-C06 — Similar Quote Retrieval

### 2. What We Intended to Build

Retrieve relevant historical quotations with bounded, explainable V1 similarity logic and stable provenance without making similarity authoritative.

### 3. Why This Card Exists

Comparable history provides context for quotation intelligence, but simple explainable retrieval should establish a safe foundation before optional vector or RAG complexity.

### 4. What We Actually Built

Implemented deterministic similar-quotation retrieval over validated C02 `Quote`, `NewQuoteRequest`, and `HistoricalQuote` contracts. Results reuse the C02 `SimilarQuote` model and retain source ID and synthetic provenance in a typed C06 match boundary.

### 5. Key Design Decisions

V1 retrieval uses explainable structured feature overlap: normalized project-name tokens, work-item description tokens, and item-count agreement. Scores use Decimal arithmetic, results are ordered by descending score with quote ID/source ID tie-breakers, and commercial values are never copied into results.

### 6. Why We Chose This Approach

The existing C02 contracts expose stable structured quotation fields without requiring a new schema or provider dependency. Simple overlap is inspectable and reproducible for V1 while similarity remains contextual rather than authoritative.

### 7. Alternatives Considered

Alternatives were embeddings, vector search/RAG, opaque model ranking, and copying historical prices or effort into the result.

### 8. Why Alternatives Were Not Chosen

Those alternatives would add C06-external infrastructure or make contextual similarity appear to be commercial truth. Price/effort copying is explicitly outside C06.

### 9. Technologies / Libraries Used

Python standard library `Decimal`, `dataclasses`, regular expressions, and existing Pydantic domain models. No dependency was added.

### 10. Why These Technologies Were Used

Decimal keeps scores deterministic; frozen dataclasses retain typed source identity and provenance without duplicating quotation schemas.

### 11. Problems Encountered

No implementation failure was observed. The main boundary decision was retaining provenance and source identity because the existing `SimilarQuote` model intentionally contains only contextual result fields.

### 12. Root Cause

The C02 `SimilarQuote` contract does not itself carry source ID or data origin, while C06 requires stable identity/provenance evidence. The C06 match wrapper preserves those fields without altering the C02 model.

### 13. How We Fixed It

The retrieval boundary returns `SimilarQuoteMatch`, combining the validated C02 result with source ID and provenance; it validates currency compatibility, handles empty/limited inputs, and applies stable deterministic ordering.

### 14. Validation / Evidence References

Focused C06 tests passed 8 tests; the full suite passed 48 tests. Coverage includes ranking sanity, stable ties, limits, empty/small history, invalid limits, currency mismatch, C03 integration, immutability, provenance, and no commercial-value copying.

### 15. Tradeoffs and Limitations

The V1 feature set is intentionally limited to structured token overlap and item-count agreement. It does not provide embeddings, vector databases, RAG, semantic retrieval, pricing, risk, AI, or infrastructure.

### 16. What We Learned

Retrieval must expose why a record matched and must preserve historical provenance; stable tie-breaking prevents otherwise identical inputs from producing ambiguous evidence.

### 17. What Should Be Remembered Later

Future maintainers must keep SimilarQuote results contextual, preserve C03 source records, and avoid turning C06 ranking into price copying or C07 risk logic.

### 18. Impact on Later Cards

C06 provides bounded comparable-quotation references for later evidence/risk workflows without implementing RiskEvidence, AI interpretation, or approval behavior.

## V1-C07 — Risk Evidence Engine

### 1. Card

V1-C07 — Risk Evidence Engine

### 2. What We Intended to Build

Transform validated comparison results into deterministic, traceable RiskEvidence with reconciled counts, statistics, supporting quote IDs, and visible uncertainty.

### 3. Why This Card Exists

Evidence aggregation must be established separately from later AI risk language so that risk claims remain grounded, reproducible, and provenance-backed.

### 4. What We Actually Built

Implemented `build_risk_evidence()` and typed `RiskEvidenceReport`. The engine
consumes validated C03 historical records through the C05 comparison engine,
selects one metric domain at a time, and emits reconciled counts, overrun rate,
average/median variance, traceable quotation/source IDs, work-item context,
scope-change IDs, outcome labels, and typed `RiskEvidence` items. No
`RiskSuggestion`, AI, approval, pricing, or provider behavior was added.

### 5. Key Design Decisions

Evidence is `SUCCESS` only when the selected metric has validated observations.
Empty history and a metric with no available actual outcomes return
`INSUFFICIENT_EVIDENCE`. Missing actual values are excluded, never converted to
zero or success. C05 owns comparison and aggregate arithmetic; C07 retains the
resulting evidence context.

### 6. Why We Chose This Approach

The implementation uses frozen dataclasses for the report and existing C02
`RiskEvidence` and `AgentResultStatus` models. It accepts `hours` or `cost`
explicitly, preserves the C05 homogeneous metric/unit invariant, and requires
one provenance origin across the input collection.

### 7. Alternatives Considered

Alternatives were a generic dictionary result, duplicated variance calculation,
using C06 similarity as risk proof, and returning a `RiskSuggestion`.

### 8. Why Alternatives Were Not Chosen

Those alternatives would weaken typing, duplicate authoritative C05 behavior,
cross the C06/C07 evidence boundary, or implement later AI interpretation
prematurely.

### 9. Technologies / Libraries Used

Standard-library Python, `Decimal`, existing Pydantic domain models, and the
existing C04/C05 deterministic functions.

### 10. Why These Technologies Were Used

No provider or external dependency was needed; existing Core contracts keep
the engine local and reproducible.

### 11. Problems Encountered

The first focused run exposed an incorrect report denominator reference and an
incorrect expectation that C03 supplied actual costs. C03 contains actual
hours only, so the cost-success test uses a validated explicit-cost fixture;
the real C03 cost path correctly returns `INSUFFICIENT_EVIDENCE`. An independent
audit then found that the tests exercised, but did not explicitly assert, the
numeric median; an even-count Decimal regression case was added.

### 12. Root Cause

The denominator was mistakenly assumed to be a field on C05 `VarianceSummary`,
and the test initially treated absent C03 actual costs as successful cost
evidence. Both were local C07 assumptions, not earlier-Card defects.

### 13. How We Fixed It

The report now derives its denominator from selected validated observations and
distinguishes unsupported cost evidence from successful cost evidence. The
focused tests now assert the exact even-count median value rather than only
exercising the code path.

### 14. Validation / Evidence References

Focused C07 tests passed 11; C03–C07 related tests passed 47; the full suite
passed 61. Tests cover count/rate/statistic reconciliation, exact even-count
median behavior, cost evidence,
missing outcomes and costs, empty history, context retention, deterministic
repeatability, immutability, and mixed-origin rejection.

### 15. Tradeoffs and Limitations

No rounding, FX conversion, risk threshold, or arbitrary minimum sample size was
introduced. Insufficient evidence is represented when the selected metric has
no usable validated observations.

### 16. What We Learned

RiskEvidence is deterministic evidence for later interpretation. It is not a
risk decision, recommendation, approval, rejection, price, or forecast.

### 17. What Should Be Remembered Later

V1-C08 may later interpret this evidence through a provider-isolated AI Card;
that work remains unauthorized and unimplemented.

### 18. Impact on Later Cards

C08 can consume stable evidence without moving deterministic statistics into AI;
future Cards must preserve provenance, missing-data semantics, and the human
approval boundary. C07 was delivered through verified delivery commit
`e3d6825628634866c89f5e6d772cc98376c6e736`, PR #16, and merge commit
`e5b87edac75a20f1784c53a09acb22414dcf3ece`; outcome reconciliation recorded
C07 as COMPLETE and cleared the Active Card. V1-C08 remains unauthorized.

## V1-C08 — Amazon Bedrock Integration

### 1. Card

V1-C08 — Amazon Bedrock Integration

### 2. What We Intended to Build

Add a provider-isolated Amazon Bedrock adapter behind a provider-neutral AI contract with structured validation and explicit failure handling.

### 3. Why This Card Exists

Bedrock is the approved V1 AI direction, but provider payloads and failures must remain outside Core and must never own commercial truth.

### 4. What We Actually Built

Implemented `bedrock.py`, a small injectable Amazon Bedrock Runtime Converse
adapter, plus environment-backed C08 settings and the official `boto3` dependency.
The Core receives a typed bounded result rather than raw SDK response objects.

### 5. Key Design Decisions

Converse is used behind a lazy client boundary. Request construction is deterministic;
response envelopes are validated; provider failures map to `UNAVAILABLE`, malformed
responses to `INVALID`, and successful text to `SUCCESS`. Timeouts and retries are
bounded through botocore configuration. Credentials use standard SDK resolution.

### 6. Why We Chose This Approach

The external preflight established a working Nova Micro Converse path, so C08 owns
the reproducible Python dependency and isolates the provider at the intended Card
boundary without changing deterministic C01–C07 authorities.

### 7. Alternatives Considered

Considered direct SDK calls in Core, `invoke_model`, raw response leakage, a generic
multi-provider framework, and live-only tests.

### 8. Why Alternatives Were Not Chosen

Those alternatives would weaken provider isolation, add unnecessary abstraction, or
make deterministic unit validation depend on live AWS availability.

### 9. Technologies / Libraries Used

Python standard library dataclasses, `boto3` 1.43.96, botocore `Config`, and the
existing `AgentResultStatus` model.

### 10. Why These Technologies Were Used

`boto3` is the supported AWS SDK boundary; injected clients make application tests
repeatable, while botocore configuration provides bounded connection/read timeouts
and retry attempts without creating a later resilience architecture.

### 11. Problems Encountered

The initial project environment did not contain boto3 because C08 had not introduced
it; this was an expected dependency gap, not an AWS access failure. Activation state
and evidence were reconciled to READY_FOR_DELIVERY after implementation.

### 12. Root Cause

The root cause was that provider integration and its dependency were intentionally
deferred until the authorized C08 Card. The fix was to declare/install boto3 and keep
all provider interaction inside the adapter.

### 13. How We Fixed It

Added reproducible dependency/configuration, typed request/result handling, response
validation, controlled error mapping, mocked tests, and one minimal live smoke test.

### 14. Validation / Evidence References

Focused C08 tests: 9 passed. C04–C08 related tests: 51 passed. Full suite: 70 passed.
The live Python smoke test invoked `amazon.nova-micro-v1:0` in `us-east-1` and
returned `BEDROCK_C08_OK`; usage was 17 input / 9 output / 26 total tokens and
observed latency was 781.78 ms.

### 15. Tradeoffs and Limitations

No structured model-output domain schema was invented because C08 specifies response
validation but not agent/tool output ownership. The adapter returns bounded text;
advanced retry, agent orchestration, and production deployment remain later scope.

### 16. What We Learned

Provider SDK isolation and explicit malformed-response handling are prerequisites for
safe later AI interpretation; model output must remain untrusted and non-authoritative.

### 17. What Should Be Remembered Later

C09 may build bounded Agent Tools over this integration. C08 does not add tools, an
agent loop, quotation generation, approval, Excel, API, storage, or deployment.

Delivery outcome: implementation commit `a29189d7d62145936aaa4f024ce8076a4bef30b7`
was merged through PR #18 with merge commit
`def3367540ac17bfb9ab1f3acfb97fe6302bc656`; C08 is terminally complete and no
Card is active.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C09 — Agent Tools

### 1. Card

V1-C09 — Agent Tools

### 2. What We Intended to Build

Expose existing validated quotation capabilities through typed, bounded, traceable tool contracts without duplicating domain or calculation logic.

### 3. Why This Card Exists

The future agent needs controlled access to approved capabilities while deterministic services remain the owners of business behavior.

### 4. What We Actually Built

One provider-free `agent_tools.py` module with typed Pydantic requests/results,
explicit `ToolFailure` codes, fixed resolution of five completed capabilities,
injected service functions for isolated tests, and output validation against
Core-owned deterministic results. Focused C09 and architecture tests were added.
No agent loop, approval, draft generator, Excel, API, or storage behavior was built.

### 5. Key Design Decisions

C09 exposes C03 synthetic history, C06 similarity, C05 comparison/statistics,
and C07 risk evidence. Deferred draft creation/validation and Excel names are
explicitly rejected by a fixed resolver. The tool layer checks provenance and
re-executes the relevant pure Core owner to reject plausible numeric changes in
delegated results; it does not implement arithmetic or evidence generation.
Tool requests carry query parameters, never historical records; every method
obtains the complete verified C03 corpus through its internal source boundary.
The architecture category `AGENT_TOOL` may import Core only. Core cannot
import Agent Tools, and Support cannot launder a forbidden dependency.

### 6. Why We Chose This Approach

Only C03–C07 provide owned capabilities now. Returning a successful placeholder
for later-Card functions would fabricate a capability. Reusing deterministic
Core functions keeps commercial ownership where it already belongs; checking
their exact outputs closes the observed numeric-tampering gap without copying
the formulas. A fixed resolver makes unsupported calls explicit without C10
tool selection or model-driven invocation. Loading the full owned corpus inside
the tool boundary prevents a future agent from supplying or cherry-picking
records while still allowing an explicit missing-source failure.

### 7. Alternatives Considered

Considered exposing all Roadmap tool names as successful stubs, returning only
shape-validated delegated values, importing C08 for model-driven tool calls,
moving commercial checks into C09, and allowing callers to pass historical
records into the tool requests.

### 8. Why Alternatives Were Not Chosen

Successful stubs would misrepresent future-Card readiness; shape checks missed
a forged numeric variance in an executed adversarial probe; C08 has no
structured tool-calling contract; duplicated arithmetic would weaken C04/C05
ownership and make two commercial authorities. Caller-supplied records also
allowed an executed altered-outcome probe to fabricate apparently traceable
risk evidence, so provenance labels alone were not a sufficient input gate.

### 9. Technologies / Libraries Used

Existing Python 3.13+ standard library dataclasses, enums, and typing;
existing Pydantic validation. No dependency added.

### 10. Why These Technologies Were Used

Pydantic already defines C02's typed domain boundaries and provides runtime
input/output shape validation. Dataclasses hold the existing Core service
results. Injectable callables permit deterministic unavailable, malformed,
and failure probes without Bedrock or network access.

### 11. Problems Encountered

The first focused C09/architecture run passed 44 tests. A later adversarial
probe that changed only a comparison variance while preserving source identity
failed its expected-rejection assertion (1 failed): the tool accepted the
plausible tampered result. A later ACTIVE-state consistency check failed three
exact-line assertions in the C09 governance records. A second adversarial
probe failed (1 failed): a caller changed historical actual hours while
retaining source identity, and the initial risk tool accepted it. No external
or partial side effect occurred.

The independent C09 audit subsequently reported PASS with one actionable LOW:
the architecture policy allowed Agent Tool → Support even though the actual
tool module imports only Core. This was an unnecessary permission, not an
observed tool-behavior failure.

### 12. Root Cause

Output validation initially checked type, provenance, and missing-data
relationships, but these do not prove a numeric value came from C05. The
governance mismatch came from adding explanatory text on lines that the
existing consistency script parses as exact state values. The altered-outcome
probe revealed that tool inputs still owned their own history collection;
comparing Core output to Core recomputation over that same untrusted input
could only prove calculation consistency, not evidence authenticity.
The architecture allowance was broader than the imports required for C09;
the original policy change opened both Core and Support without a concrete
Support dependency.

### 13. How We Fixed It

The tool boundary now compares delegated outputs against results from the
existing deterministic owners (C03/C05/C06/C07), with no C09 arithmetic.
The adversarial probe then passed, as did the 46-test combined focused suite
after one additional whitespace-ID case. Typed numeric checks and missing-cost
cases were added to prevent coercion or silent evidence creation.
The C09 state and approval records now use bare canonical values with
explanation on following lines; the ACTIVE-state consistency gate passed on rerun.
Historical records were removed from tool request models; the tool layer now
loads and validates the full C03 dataset before delegating. The new probe
passed on focused rerun (24 C09 tests).
The bounded audit remediation narrowed `AGENT_TOOL` to `{CORE}` and added an
architecture fixture that rejects Agent Tool → Support. No tool behavior or
other category policy changed. Because candidate content changed, independent
re-audit of the remediated candidate was required; the earlier audit PASS was
not treated as approval of the new identity.

### 14. Validation / Evidence References

See QUOTATION_CARD_EVIDENCE_MAP.md → V1-C09 for the executed failure and
recovery, commands, focused C09 24 passed, architecture 23 passed, full pytest
138 passed, Governance Harness 61 passed / 0 failed,
and C09 Exit Gate proof. The later audit LOW and bounded remediation are
recorded there with post-remediation C09 24 passed, architecture 24 passed,
full pytest 139 passed. Subsequent human delivery approval identified the
remediated identity as independently audited; exact staged and committed
verification passed before push.

### 15. Tradeoffs and Limitations

Exact owner re-execution costs additional deterministic work, but keeps the
boundary robust against injected numeric tampering and creates no second
formula. History retrieval is limited to C03 synthetic records; there is no
general storage/repository capability yet. C08 remains unused because C09
does not own an agent protocol. The independent-audit and delivery gates
were subsequently satisfied for the exact remediated identity.

### 16. What We Learned

Preserving source IDs is necessary but insufficient: a result can have correct
provenance and still alter a commercial statistic—or the input record itself
can be fabricated. In this pure local C09 boundary, source-owned history and
exact comparison to the owning deterministic service are both required.

### 17. What Should Be Remembered Later

C10 may call these code-level methods but must not treat the deferred names
as implemented, permit model-supplied commercial totals, or assume C08's text
result contains structured tool calls. A future history provider needs its
own authorized source contract and provenance checks; do not silently relax
the C03-only restriction or accept model-supplied history in C09.

### 18. Impact on Later Cards

C10 receives bounded, tested local tool interfaces without receiving agent
reasoning or selection logic. C11–C20 remain untouched; their capabilities
must be implemented and approved in their own Cards. C09 was delivered by
commit `3dee2d0345e783ad491e8683204a071ad010b8c4` through PR #25, merged
as `d0f0f70f385c2e876512ce9706d5ffd33ef3664a`. C09 is complete; C10
remains unauthorized.

## V1-C10 — Quotation Agent

Pre-implementation governance finding (not C10 implementation): the C10
Specification referred to an authoritative Roadmap Exit Gate that did not
exist, and the global C09+ rule required a compact verification block that
the C10 section lacked. The root cause was incomplete propagation of the
later-Card verification template into these two canonical C10 owners. This
could leave C10's completion criterion and independent verification plan
ambiguous before authorization. The bounded fix added the existing-scope Exit
Gate and a derived, risk-based verification block without choosing an agent
protocol, opening architecture permissions, or granting C10 approval. The
lesson is to reconcile the Roadmap gate and specification verification fields
before starting a Card. That maintenance change was later independently
audited and delivered through PR #27; separate C10 authorization followed.

### 1. Card

V1-C10 — Quotation Agent

### 2. What We Intended to Build

Build a genuine bounded tool-using quotation agent that selects approved tools and returns validated structured draft output grounded in deterministic results.

### 3. Why This Card Exists

The project requires AI-assisted draft quotation intelligence, but orchestration must remain separate from commercial truth, evidence creation, and human approval.

### 4. What We Actually Built

`quotation_agent.py` implements a bounded C10 model/tool loop. It parses one
strict JSON action per model response, invokes only completed C09 tools with
typed inputs reconstructed from the validated AgentRequest, validates C09
outputs, and returns an evidence-linked `AgentResult` containing an
unapproved `DraftQuote`. Existing Core `calculate_quote` supplies the draft
total. C08's existing text adapter can be injected without adding native
tool-use behavior or changing C08/C09.

### 5. Key Design Decisions

The selected action protocol has `tool` and `final` forms with forbidden
extra fields and duplicate JSON keys. The model can select a C09 tool and
bounded non-authoritative options (metric or similarity limit); it cannot
supply the request, identity, history, totals, or tool result. Final output
selects evidence IDs, advisory severity, and one of three safe narrative
statements; C10 derives risk wording from validated C09 evidence metrics.
Seven tool calls plus one final model turn are permitted; an identical
tool/argument pair fails on repetition. `TextModel` is a provider-neutral
injected Protocol in the AGENT module; C08's BedrockConverseAdapter satisfies
its runtime shape. AGENT imports CORE for domain contracts and the existing
calculation owner, and AGENT_TOOL for C09 dispatch; it imports neither
PROVIDER nor SUPPORT. No new dependency or C08 extension was needed.

### 6. Why We Chose This Approach

The strict action shape makes selection genuinely model-driven without
granting model execution authority. Reconstructing C09 inputs prevents
model-generated arguments from overriding a validated quotation request.
Directly calling Core's calculation owner is necessary because C09's draft
creation tool is intentionally deferred; copying arithmetic into C10 would
create a second commercial authority. Injecting the C08 adapter keeps its
SDK and provider objects outside Agent and Core. Constrained success wording
prevents arbitrary model prose from becoming an unsupported factual claim.

### 7. Alternatives Considered

Considered an open-ended ReAct loop, native Bedrock tool use, a free-form
model-generated draft, forwarding model-created commercial fields, adding a
new C09 draft tool, and letting Agent import Provider/Support directly.

### 8. Why Alternatives Were Not Chosen

Those alternatives either exceed the C08/C09 contracts, add unnecessary
permissions or technology, make safety limits unclear, duplicate commercial
authority, or accept unsupported model claims. A fixed chain was also
rejected because C10 must let the model select among approved tools. The
chosen bound allows the five available operations and the two metric
variants while stopping repeated identical actions and further calls.

### 9. Technologies / Libraries Used

Existing Pydantic/domain contracts, Python standard-library JSON/regex,
Core calculation, C09 AgentTools, and the C08 Bedrock adapter interface.
No package, cloud service, or framework was added.

### 10. Why These Technologies Were Used

Pydantic matches the repository's strict typed-boundary convention. The
standard-library parser supports explicit duplicate-key rejection. Core,
C09, and C08 remain the actual capability owners, so the agent only
orchestrates and validates at its trust boundaries.

### 11. Problems Encountered

Two focused-test failures and one governance smoke-check failure occurred. Pytest initially
refused to collect `tests/test_quotation_agent.py` because its fixture was
named `request`, a reserved pytest name. After collection was fixed, the
loop-limit test returned INSUFFICIENT_EVIDENCE before reaching its intended
limit assertion when it invoked cost statistics on the current synthetic
corpus. Later, session bootstrap reported one FAIL when the live C10 state
update shortened PROJECT_CONTROL's long implementation-status line. The
observed failures and passing reruns are retained in the C10 Evidence Map;
none was treated as a successful first run.

### 12. Root Cause

The first failure was a test fixture naming collision. The second was a
test-design mistake: a valid C09 evidence failure preempted the later C10
orchestration limit that the test meant to exercise. It was not a C09
calculation defect or grounds to fabricate cost observations. The bootstrap
failure was an existing exact-prefix sanity check, not contradictory C10
implementation evidence; the shorter but truthful status wording no longer
contained `Application Implementation: V1-C01 BASELINE IMPLEMENTED`.

### 13. How We Fixed It

Renamed the fixture `agent_request`. Replaced the limit-test sequence with
distinct valid C09 actions so each preceding tool call succeeds and the
next requested call actually reaches the bound. Focused, architecture, C09
regression, and full-suite reruns passed after the corrections. Risk
suggestion text was also narrowed from model free text to fixed wording
derived from C09 risk metrics after self-review identified the unsupported
qualitative-claim path. The full truthful implementation-status sequence was
restored in PROJECT_CONTROL and extended through C10, preserving the
bootstrap's expected prefix without changing the read-only bootstrap script;
bootstrap then passed apart from the expected dirty-worktree warning.

### 14. Validation / Evidence References

QUOTATION_CARD_EVIDENCE_MAP.md → V1-C10 records the implementation paths,
observed failures, passing commands, adversarial cases, Exit Gate mapping,
and remaining limitations. `tests/test_quotation_agent.py` exercises real
C09/Core behavior and a mocked C08 Converse transport; `tests/test_architecture.py`
proves the AGENT category's local dependency directions.

### 15. Tradeoffs and Limitations

The successful narrative is deliberately constrained to three safe
statements, so it is less expressive than unrestricted model prose. C10
relies on C09's verified synthetic history and does not make external data
available. C08 remains text-only; the JSON protocol is prompt-and-parse,
not native provider tool calling. No live Bedrock request was needed for
deterministic validation. There is no retry/fallback agent framework, C11
review transition, C12 Excel export, or C13+ infrastructure.

### Bounded post-audit remediation (focused independent re-audit pending)

The independent audit of the original C10 candidate was PASS with actionable
MEDIUM robustness/deployment-readiness findings and a LOW maintainability
finding. That historical PASS does not certify the changed candidate. The
final-action dispatch called `_final(...)` outside the loop's uniform
unexpected-exception boundary, so an unforeseen assembly error could escape
`run()` and expose exception text through its caller. `_safe_prose` enforced
authority limits but had no focused tests; its intended rejection and safe
controls could silently regress. C08's 64-token configuration default was
adequate for its earlier smoke response but could truncate C10's structured
final JSON. Finally, the seven-call bound was correct but unexplained and
unprotected if available tools or metric variants changed.

The narrow fix wraps only `_final(...)` dispatch with sanitized typed INVALID
failure for unexpected exceptions, retaining `_final`'s specific validation
returns. Focused tests now exercise numeric, currency, percentage, approval,
finalization, guarantee, and certainty text in `missing_information`, plus
ordinary safe gaps and injected final-assembly failure. The loop remains seven
calls: three single-call capabilities plus two metric-sensitive capabilities
with hours/cost variants. A test asserts that derivation against C09's
allowlist and the metric contract. Existing `Settings.bedrock_max_tokens` and
`.env.example` move from 64 to a bounded 1024; the C08 adapter contract and
provider isolation are unchanged. A deterministic test verifies the effective
Converse request capacity exceeds a representative validated structured final
response even under a conservative one-token-per-byte bound. The previous
64-token baseline remains historical evidence, not a claimed passing runtime
configuration. Explicit environment overrides and live Bedrock generation
remain deployment-time considerations, not unobserved test successes.

The chosen changes avoid a new error framework, prose policy expansion, C08
adapter rewrite, arbitrary unbounded output setting, or autonomous-agent
loop. The lesson is that a parser/final-construction boundary needs the same
exception containment as provider/tool boundaries, and operational defaults
must be tested against the larger consumer's actual response shape. The
changed candidate requires its own focused independent re-audit before any
delivery approval; C11 and later remain unauthorized.

Observed post-remediation reruns were 57 C10 focused, 24 C09 regression, 32
architecture, and 204 full pytest passes; reconciliation passed; Governance
Harness passed 61/0; bootstrap passed 127 with its expected dirty-worktree
warning and no failures; compilation/import, shell syntax, secret-pattern,
and diff checks passed. These are local validation observations, not a new
independent audit or live Bedrock result.

The later human delivery instruction confirmed independent PASS for the exact
remediated identity `80cf063ea390776f581b04744043d48fb15473194365ee527ed391dfe71f5893`
and explicitly accepted the remaining LOW output-token sizing note as
non-blocking. The frozen candidate was not edited. Worktree, staged-index,
and committed-tree identity checks passed; delivery commit
`68370daa4d9defcdb6cfd3455db1c26a9c4c3480` was pushed and merged in
PR #28 as `ecb73841eeb80a863d0f969c66105d9b02226caa`. Post-merge on
clean `main`, C10/C09/architecture/full pytest passed 57/24/32/204,
Governance Harness passed 61/0, reconciliation passed, and bootstrap passed
128/0/0. This outcome-only record is separate from the audited candidate;
its own future Git identifiers are not prerequisites or embedded here.

### 16. What We Learned

For model-driven actions, validation must be at the execution boundary,
not just in the prompt. The model may choose a tool, but cannot author its
request identity, commercial inputs, historical evidence, or deterministic
results. A test for a later safety limit must first use data that passes
earlier owned-capability gates. Constraining model-authored factual prose
is simpler and more reliable here than attempting open-ended semantic
fact-checking with another model.

### 17. What Should Be Remembered Later

Keep the C09 tool allowlist, strict JSON/action validation, repeated-call
guard, request/result identity checks, Core arithmetic delegation, and
evidence-ID linkage intact. Do not replace the safe narrative selection
with unrestricted prose without a separately justified and independently
verified grounding mechanism. An AgentResult with status SUCCESS is still
an unapproved draft; the completed C10 delivery does not grant C11 approval
or quotation-finalization authority.

### 18. Impact on Later Cards

C11 may review this validated draft but must own explicit human approval;
C12 owns final Excel generation after approval. C13+ may wire interfaces
and runtime services without moving Provider SDK payloads into Core or
granting C10 delivery/finalization authority. C17/C18 may later evaluate or
generalize the agent's safety behavior, but C10 does not build those systems.

## V1-C11 — Human Review Gate

Pre-implementation governance finding (not C11 implementation): read-only
C11 preflight was BLOCKED by two missing canonical records. The specification
called the Roadmap Exit Gate authoritative, but the C11 Roadmap section had
no explicit gate; the global C09+ verification rule also had not been applied
to C11. The root cause was incomplete propagation of the later-Card gate and
verification template, leaving the completion criterion and independent
verification plan ambiguous before authorization. This bounded maintenance
adds an existing-scope Exit Gate and an ELEVATED, derived verification block.
It does not choose an exact transition matrix, reviewer authentication or
storage mechanism, draft-version scheme, architecture placement, or C12+
capability. The prevention lesson is to reconcile the Roadmap gate and
specification verification block before human Card-start authorization;
actual C11 implementation, audit, and delivery remain future work.

### 1. Card

V1-C11 — Human Review Gate

### 2. What We Intended to Build

Implement explicit review and approval state transitions between validated agent draft output and finalization eligibility.

### 3. Why This Card Exists

Consequential commercial finalization requires a visible human decision, while approval must not alter deterministic arithmetic truth.

### 4. What We Actually Built

An in-memory deterministic `ReviewSession` accepts only a revalidated C10
`AgentResult` with a successful draft, reconciled Core total, consistent
request/quote identity, and consistent evidence links. A separate existing
`ApprovalDecision` supplies one explicit reviewer action. The session returns
a structured `ReviewRecord` and exposes `require_approved(current=...)` as
its sole finalization-eligibility check. It does not export, persist, call
Bedrock, or authenticate a person.

### 5. Key Design Decisions

Architecture Before: AGENT may import CORE; no C11 review module existed.
Change Introduced: `human_review.py` is classified REVIEW, with REVIEW → CORE
as its only allowed local direction. All other local categories are barred
from importing REVIEW. Architecture After: C11 can revalidate using existing
domain and calculation owners, while C10 Agent and C09 Agent Tool cannot
acquire review authority through their existing Core permissions.

The exact C10 `AgentResult` is the input, not a free-standing `DraftQuote`:
its status, request identity, evidence links, and draft can be checked
together. The session stores an exact validated JSON snapshot, not merely a
quote ID or a new hash/version scheme. A decision compares a fresh current
result with that snapshot. `ApprovalDecision` retains its optional reason
and timestamp; C11 never invents either. Only AWAITING_REVIEW may transition
once to APPROVED or REJECTED; a changed draft needs a new validated session.

### 6. Why We Chose This Approach

It is the smallest local authority gate that can distinguish an unsuccessful
C10 outcome from a reviewable draft, detect commercial/evidence substitution,
and preserve an inspectable human decision without creating persistence or
identity infrastructure. `calculate_quote_total` is called only to verify
Core-owned arithmetic; C11 does not calculate or override a total itself.
`ReviewRecord` is an audit copy, not authority; eligibility is checked by
the session against the current result and its held decision.

### 7. Alternatives Considered

Using `DraftQuote` alone; storing only quote/request IDs; a hash or version
service; mutating the draft into an approved draft; classifying Review as
CORE; and adding authentication, a database, or an event store.

### 8. Why Alternatives Were Not Chosen

`DraftQuote` alone loses the C10 success/failure envelope. IDs alone do not
detect changed hours, rates, totals, evidence, or narrative. Exact local
snapshot comparison suffices without a new hash/version service. `DraftQuote`
forbids approved status, so the reviewed draft stays DRAFT while a separate
validated Quote and decision carry the resulting state. CORE placement would
allow Agent → CORE to import approval code. Authentication and persistence
belong to later authorized boundaries, not C11.

### 9. Technologies / Libraries Used

Existing Python standard library, Pydantic/domain models, and Core
calculation service; no new dependency or AWS service.

### 10. Why These Technologies Were Used

They were already owned and tested by C02/C04/C10, and allow strict typed
round-trip validation and deterministic commercial reconciliation without a
second arithmetic or provider implementation.

### 11. Problems Encountered

The first Card-start reconciliation failed with `Active Card has incompatible
lifecycle state: V1-C11` after `IN_PROGRESS` was used in the control status
table. Initial C11 code placed review in CORE and focused tests passed, but
source review found that this would permit C10 Agent to import approval code.
An initial `ReviewRecord.finalization_eligible` property also read a mutable
returned Quote copy, allowing caller-side mutation to change that apparent
eligibility without changing the held human decision.

### 12. Root Cause

The reconciliation tool's lifecycle vocabulary accepts `ACTIVE`, not
`IN_PROGRESS`. The existing AGENT → CORE architecture permission is too broad
to place human approval authority in CORE. Pydantic frozen records do not
deep-freeze nested mutable Quote models, so a derived eligibility flag on a
returned audit copy was not an authority-safe boundary.

### 13. How We Fixed It

The control/evidence state now uses `ACTIVE`, and reconciliation passes.
Approval code moved to a distinct REVIEW category with REVIEW → CORE only;
architecture tests reject imports from Agent, Agent Tool, Provider, Support,
Core, and application boundaries. The copy-derived eligibility property was
removed; `ReviewSession.require_approved` now checks the held decision and
exact current result, with a regression showing mutation of a returned
rejection record cannot grant eligibility.

### 14. Validation / Evidence References

QUOTATION_CARD_EVIDENCE_MAP.md → V1-C11 records the failed and passing
reconciliation, focused/adversarial and architecture tests, and final broad
validation once executed. Initial focused C11 and architecture rerun: 73
passed. Independent audit and Git delivery remain pending.

### 15. Tradeoffs and Limitations

`reviewer_id` is a required caller assertion, not proof of authentication;
the trusted future caller must ensure it comes from a real human action, not
model output. C11 can bind to the validated C10 result it receives, but cannot
cryptographically prove that a caller supplied genuine C10 output. Evidence
source records are validated by C10/C09; C11 preserves their IDs and checks
internal consistency rather than fetching history again. One session rejects
repeat decisions, but cross-process replay/idempotency requires a future
persistent boundary. No timestamp is generated when the existing optional
field is absent. Returned audit copies are mutable; only the held session's
`require_approved` check grants eligibility.

### 16. What We Learned

An import category is an authority boundary, not merely a code-organization
label. A green behavior test does not prove that a future Agent cannot import
approval through an otherwise allowed dependency. Snapshot binding and an
explicit human action prevent silent promotion of a changed draft in this
local boundary, while authentication remains a separate trust obligation.

### 17. What Should Be Remembered Later

C12/C13 must not treat a copied `ReviewRecord`, a QuoteStatus, a C10 message,
or a reviewer string alone as approval. They must use the held approval gate
against the current validated result and supply reviewer identity from a
trusted human-facing boundary. If persistence is later added, define replay,
concurrency, and stale-decision semantics explicitly before deployment.

### 18. Impact on Later Cards

C12 may consume only approved validated state after explicit permission to
depend on REVIEW is justified. C13 may supply the authenticated human action
and current result, but no application dependency was opened in C11. C14+
storage/deployment and C18 general guardrails remain separate Card work.

Delivery outcome: the exact C11 candidate identity
`602a6a6e892325c434bb521d59aec47a486fabe20a214dd96053165f08af8a03`
received independent audit PASS. The human approver accepted the LOW
exact-type-check test-necessity note and the documented V1 trust, in-memory
repeat-decision, optional-timestamp, and conservative snapshot limits without
changing the frozen candidate. Staged and committed-tree identity checks
passed; delivery commit `b5a283fd4e4f6aa5cda3a51e2aea26bfce4dc83e`
was pushed and merged through PR #31 as
`cc4ef118bb46488bb0cd1ac23ea15612b40be1e5`. Clean-main post-merge
focused C11/C10/C09 tests passed 32/57/24, architecture passed 42, full
pytest passed 246, Governance Harness passed 61/0, reconciliation passed,
and bootstrap passed 128/0/0. This outcome-only reconciliation records
C11 completion separately from the audited implementation. C12 remains
unauthorized and unstarted.

## V1-C12 — Excel Generation

Pre-implementation canonical maintenance (not C12 implementation): read-only
preflight was BLOCKED by the missing authoritative Roadmap Exit Gate, missing
C09+ verification block, unsupported Roadmap role field, and unbound
historical-value fields. The root cause was treating a conceptual workbook
outline as if delivered C02–C11 models carried every listed field. Inspection
found no `QuoteItem.role`; C03's local role word appears only inside a
description and cannot be recovered as approved line-item data. C11's
approved result binds evidence IDs and risk suggestions, not historical
estimated/actual values, variance, or comparison records. The bounded fix
adds the C12 gate and verification plan, makes the existing three sheet names
the V1 required set, marks role optional/unsupported, and limits historical
content to evidence references demonstrably bound to the approved result.
The alternative of fetching C09 history after approval was rejected for V1:
it could select or attach evidence the human never reviewed. The alternative
of deriving role from prose or history was rejected as fabrication. C12 must
use C11's held approval gate, render static Core-owned numbers, make
formula-like text inert, and fail visibly; bytes/path output, styling, and
least-privilege export architecture remain decisions for authorized C12
implementation. openpyxl is specified but not added in this maintenance;
no AWS action is needed. This avoids inventing data or approval authority
while preserving the mandatory Excel business output. C12 remains
NOT_AUTHORIZED / NOT_STARTED; no implementation or Exit Gate proof is claimed.

### 1. Card

V1-C12 — Excel Generation

### 2. What We Intended to Build

Generate the professional quotation workbook from approved validated state, with traceable evidence and deterministic total reconciliation.

### 3. Why This Card Exists

Excel is the mandatory V1 quotation output and must not allow raw model output to become authoritative numeric content.

### 4. What We Actually Built

An in-memory C12 `.xlsx` exporter with exactly three semantic sheets,
typed failures, C11 held-session eligibility, Core calculation
reconciliation, safe-text rendering, workbook reload validation, and 60
focused tests. The EXPORT architecture category imports REVIEW and CORE
only. It is self-validated but not independently audited or delivered.

### 5. Key Design Decisions

`export_approved_quote(session, current=...) -> bytes` accepts a real held
`ReviewSession`, calls `require_approved`, and renders the returned decision
snapshot rather than trusting a caller's copied record. C04 functions
calculate item costs and total; C12 never implements pricing arithmetic.
Risk and Historical Evidence rows use approved suggestion/evidence IDs, not
post-approval lookup. All workbook strings cross one inert-text boundary;
the saved workbook is reopened and compared to the approved semantic rows.
EXPORT → {REVIEW, CORE} is the only new local dependency direction.

### 6. Why We Chose This Approach

Bytes avoid file paths, overwrites, persistence, and S3 authority. The held
C11 session is the only existing approval eligibility proof. Rendering the
returned snapshot avoids a second read of mutable caller input after the
gate. Static Core-derived numbers keep Excel from becoming a calculation
engine. The independent reload catches workbook serialization drift before
any bytes are returned. A dedicated EXPORT category keeps C11 authority
available to export without giving Agent, Tool, Provider, or Core export
privileges.

### 7. Alternatives Considered

Local-path output; status/ReviewRecord-based approval; Excel formulas for
totals; a fresh C09 history lookup; embedding role or unbound historical
metrics; placing export inside CORE or REVIEW; and broad architecture
permissions were considered against the delivered contracts.

### 8. Why Alternatives Were Not Chosen

Paths add overwrite/traversal and persistence policy without C12 need.
Copied approval metadata or status cannot prove C11 eligibility. Formulas
would create another business-rule authority. Fresh lookup could attach
evidence never reviewed. `QuoteItem` lacks role, and approved results lack
historical metric records. CORE/REVIEW placement would give lower layers
workbook concerns; broader permissions have no exercised imports.

### 9. Technologies / Libraries Used

openpyxl 3.1.5 was installed under the declared `openpyxl>=3.1,<4.0`
project dependency. Existing Pydantic contracts, C04 arithmetic, C11
review gate, and pytest architecture harness were reused. No AWS service or
new external-source implementation artifact was incorporated.

### 10. Why These Technologies Were Used

openpyxl is the canonical C12 workbook library and supports local `.xlsx`
creation and independent reload without cloud resources. The project uses
bounded dependency ranges rather than a lockfile, so the declaration follows
that convention. Its portability cost is the dependency and Excel's limited
numeric representation; exact post-save reconciliation makes the latter an
explicit failure instead of a silent commercial change. Revisit only if the
canonical workbook contract or project dependency convention changes.

### 11. Problems Encountered

The first Card-start reconciliation check failed on `ACTIVE /
IMPLEMENTATION` in the status table. The first focused suite failed because
the scripted C10 narrative violated C10's exact protocol and an existing
architecture negative fixture denied EXPORT's necessary REVIEW import.
After correcting those, the first workbook reload check rejected expected
blank cells because openpyxl serializes empty strings as absent cells. A
leading-space formula fixture also conflicted with domain text normalization
and C11's request/quote identity rule.

### 12. Root Cause

The governance reconciler consumes exact lifecycle tokens, not descriptive
variants. The test setup initially assumed a broader model protocol and an
unchanged pre-C12 dependency matrix. The workbook validator assumed an
empty string would survive ZIP serialization as a literal string. The
adversarial fixture assumed Pydantic would preserve outer spaces in
`NonEmptyText` and did not maintain `quote_id = draft-{request_id}`.

### 13. How We Fixed It

The C12 status-table state became exact `ACTIVE`, followed by successful
generated-view `--write`/`--check`. The scripted narrative now uses a valid
C10 literal, and architecture tests explicitly permit only EXPORT → REVIEW
and CORE while rejecting other directions. The validator accepts a reloaded
empty cell only when the expected value is the empty string. The formula
fixture now checks the normalized text and maintains C11 identity. Focused
and full tests passed on rerun; no failure was erased.

### 14. Validation / Evidence References

QUOTATION_CARD_EVIDENCE_MAP.md → V1-C12 records exact commands, 60 focused
C12 tests, C11/C10/C09 and architecture regressions, full 321-pass pytest,
Governance Harness, reconciliation, bootstrap, dependency/import, security,
diff checks, original failures, and recovered reruns. These are
self-validation results, not independent audit or delivery proof.

### 15. Tradeoffs and Limitations

Approval remains in-memory and same-process; reviewer reference is
caller-asserted, not authenticated. Approved evidence carries IDs and risk
links but not underlying historical records or metrics. The Evidence sheet
discloses the bound-reference limit and synthetic-by-default portfolio
context; it does not assert a specific origin for every opaque ID. The
exporter returns bytes only. Excel numbers that cannot round-trip exactly
fail instead of being rounded. Byte-identical ZIP output is not required.

### 16. What We Learned

Export correctness has two separate proofs: C11's current-result decision
gate controls *whether* export may happen, while Core/reload reconciliation
controls *what* the file actually contains. Cell type, not merely displayed
text, determines whether an untrusted value can execute as a formula.
Serialization details must be tested against reloaded artifacts rather than
assumed from in-memory workbook objects.

### 17. What Should Be Remembered Later

Do not turn a copied `ReviewRecord`, status, saved workbook, or opaque
evidence ID into approval or underlying historical truth. Any future
persistence/API/S3 boundary must carry an independently authorized C11
eligibility design; it must not reconstruct approval from metadata. Do not
remove exact post-save numeric checks merely to make difficult Decimal
values exportable.

### 18. Impact on Later Cards

C13+ may consume the bytes through a separately authorized application
boundary; no API, S3, persistence, or UI authority is granted here. Richer
history in a later workbook would require a new approved evidence-binding
contract before human review, not a C12 post-approval search. Durable review
authority across processes remains a separate future design decision.

Delivery outcome: the exact C12 candidate identity
`a65b6a34cc4a689b0dcbd16eb49d6c60d8c2a88b30ef34223de2fdac083b9e7f`
received independent audit PASS. The human approver accepted the LOW direct
multi-link test-coverage note and the documented V1 in-memory approval,
caller-asserted reviewer, bound-reference-only history, and fail-closed
numeric representation limits without changing the frozen candidate. Staged
and committed-tree identities matched; delivery commit
`9af4c84fdd66cad27eab6f63445beb2e895fe9bf` was pushed and merged
through PR #34 as `c828f00af069c3de83cc327fd6ee0feb3c89aee6`.
Clean-main post-merge C12/C11/C10/C09 tests passed 60/32/57/24,
architecture passed 57, full pytest passed 321, Governance Harness passed
61/0, reconciliation passed, bootstrap passed 128/0/0, and dependency,
openpyxl import, syntax, security, and diff checks passed. This separate
outcome-only reconciliation records C12 completion; C13 remains unauthorized
and unstarted.

## V1-C13 — FastAPI Application

### 1. Card

V1-C13 — FastAPI Application

### 2. What We Intended to Build

Expose the quotation workflow through typed FastAPI transport contracts while delegating business ownership to application and domain services.

### 3. Why This Card Exists

Clients need a stable workflow interface, but the transport layer must not become a second owner of quotation logic or approval policy.

### 4. What We Actually Built

`api.py` exposes the six Roadmap routes through an injected FastAPI factory.
Analysis and draft call C10; the draft route retains the validated result and
held C11 `ReviewSession` in a bounded process-local store. The decision route
passes an explicit caller APPROVED/REJECTED action to C11. Export calls C12
with the held session and current result and returns C12-validated `.xlsx`
bytes. GET returns a serialized, reviewable draft plus minimal process state;
health checks only the API process.

### 5. Key Design Decisions

The factory requires an injected C10-compatible runner instead of importing
Bedrock or constructing C09/C10 internals. Transport input forbids extra
fields and excludes status, totals, evidence IDs, and approval objects. A
128-entry store keyed by C10's quote ID holds deep-copied results and the
actual C11 session; duplicate IDs and capacity exhaustion fail closed. One
process-local reentrant lock serializes reads, review decisions, and export
against that held pair. C11/C12, not the lock or store, determine authority.

Failure mapping is deterministic: malformed/domain input and C10 INVALID or
INSUFFICIENT_EVIDENCE → 422; C10 UNAVAILABLE/delegated agent exception → 503;
unknown ID → 404; duplicate ID, invalid transition, stale or missing approval,
or export reconciliation → 409; unexpected/malformed internal output → 500.
Responses contain bounded codes, not raw exception text. A 64 KiB body cap
and bounded transport text/list fields are local HTTP protections.

### 6. Why We Chose This Approach

It exposes the required workflow without giving the API direct commercial,
model, approval, evidence-search, or workbook authority. The store only
bridges HTTP requests; C11 rechecks the current result for decisions and C12
rechecks approval on every export. Fixed `Draft_Quote.xlsx` disposition avoids
caller-controlled paths or response-header construction.

### 7. Alternatives Considered

Considered a global Bedrock-backed singleton, direct C10 import permission,
client-returned approval records, one endpoint that drafts/approves/exports,
persistent/distributed sessions, and filesystem workbook output. Also
considered a separate ASGI server dependency for local serving.

### 8. Why Alternatives Were Not Chosen

They add hidden provider coupling, permit authority forgery, collapse the
human step, or enter C14+/deployment scope. A server can be supplied at the
deployment/composition boundary later; C13 proves the ASGI app contract
without adding `uvicorn` solely for prestige.

### 9. Technologies / Libraries Used

FastAPI runtime, existing Pydantic/domain/C10–C12 contracts, existing
openpyxl through C12, and `httpx` as the FastAPI TestClient dev dependency.
No new AWS service, SDK, database, or persistence library.

### 10. Why These Technologies Were Used

FastAPI is the authorized HTTP framework; its typed validation and response
models serve the six-route transport contract. `httpx` supports deterministic
in-process HTTP contract tests. Existing C11/C12 implementations remain the
only approval and export eligibility owners.

### 11. Problems Encountered

The initial focused architecture run failed two legacy assertions: they
assumed no application boundary could import REVIEW or EXPORT. The initial
API GET view also exposed only IDs/status, leaving no reviewable draft content.

### 12. Root Cause

Those assertions represented the pre-C13 import graph, not C13's approved
adapter role. The first GET response modeled authority isolation but omitted
the safe serialized data a human needs to inspect before deciding.

### 13. How We Fixed It

Narrowed APPLICATION_BOUNDARY to actual CORE/REVIEW/EXPORT imports only,
updated the reverse-direction assertions, and added negative import tests
for AGENT, AGENT_TOOL, PROVIDER, SUPPORT, and SDK imports. GET now returns a
serialized deep copy of the draft; the API accepts no copied draft or
approval-looking object as authority. Focused tests were rerun and passed.

### 14. Validation / Evidence References

See `QUOTATION_CARD_EVIDENCE_MAP.md` → V1-C13 for executed route,
architecture, regression, security, governance, and candidate-identity
results. The initial architecture failure and proving rerun remain recorded.

### 15. Tradeoffs and Limitations

Restart loses process-local state; workers do not share it. Reviewer ID is
caller-asserted, not authenticated. The API is not deployed, has no S3 or
durable session, and a live C10/Bedrock composition still needs existing AWS
credentials/access. The app factory requires an injected runner; a later
deployment may provide server startup. HTTP body buffering is capped at
64 KiB. `httpx` TestClient currently emits a Starlette deprecation warning;
tests remain passing, and changing HTTP test clients is outside this Card.

### 16. What We Learned

Process-local retention is not the same as approval authority. Explicit
transport allowlists, held-session checks, and a lock around decision/export
give the thin API enough workflow continuity without duplicating C11/C12.

### 17. What Should Be Remembered Later

Do not deploy multiple workers and imply shared review state. Do not accept
JSON-shaped `ReviewRecord`, APPROVED status, or C10 text as human action.
If durable sessions/authentication are later authorized, preserve C11/C12's
freshness and approval gates rather than replacing them with stored flags.

### 18. Impact on Later Cards

C14 may persist artifacts only under separate authorization; C15 may compose
the injected ASGI app with a server/deployment runtime. Neither gains an
approval bypass. Authentication, distributed state, and C18-wide protections
remain separate scope.

### Pre-implementation canonical maintenance

The read-only C13 preflight was BLOCKED before authorization: the Roadmap
lacked its authoritative Exit Gate, the C09+ verification block was absent,
the listed `/approve` route did not explain how C11 rejection travels over
HTTP, and the contract did not explain how C11's held in-memory session reaches
later C12 export requests. The root cause was a C13 transport outline that
preceded the delivered C11/C12 authority contracts, leaving cross-request
authority and verification implicit.

The bounded correction retains the six existing routes. The historically
named `/approve` route transports an explicit APPROVED or REJECTED C11
decision; naming cannot grant approval. A bounded process-local association
may retain the current validated result and held review session, but C11/C12
remain the authority and must recheck transitions, freshness, and approval.
This is preferable to adding a duplicate rejection route or pretending a
copied approval record is a token. It also avoids prematurely introducing
database, Redis, or distributed-session infrastructure. Restart loses V1
process-local state, and multi-worker coherence is not claimed.

The Roadmap gate and C09+ verification block made those boundaries auditable
without fixing HTTP schema, status-code, locking, or dependency choices before
C13 implementation. That separate maintenance change introduced no API code,
dependency, architecture permission, or C13 start authorization; it was
independently audited PASS and delivered in PR #36 before this Card start.

## V1-C14 — Amazon S3 Integration

### 1. Card

V1-C14 — Amazon S3 Integration

### 2. What We Intended to Build

Add provider-isolated S3 persistence with explicit serialization, retrieval validation, local-mode support, and failure propagation.

### 3. Why This Card Exists

V1 artifacts may need durable storage, but S3 object existence must not make unvalidated content commercially authoritative or leak SDK types into Core.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C15 — AWS Deployment

### 1. Card

V1-C15 — AWS Deployment

### 2. What We Intended to Build

Deploy the approved API direction through API Gateway, AWS Lambda, and FastAPI with externalized configuration, least privilege, and local/cloud parity.

### 3. Why This Card Exists

The portfolio workflow needs a bounded cloud delivery path, while deployment claims must remain evidence-based and architecture must not expand into unnecessary infrastructure.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C16 — CloudWatch Observability

### 1. Card

V1-C16 — CloudWatch Observability

### 2. What We Intended to Build

Add bounded structured operational observability with correlation, workflow failure visibility, latency metadata, and sensitive-data redaction.

### 3. Why This Card Exists

Quotation workflows spanning tools, AI, storage, and cloud need traceable failures without turning observability into business logic or exposing secrets.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C17 — Evaluation Harness

### 1. Card

V1-C17 — Evaluation Harness

### 2. What We Intended to Build

Build repeatable evaluation for deterministic calculations, historical comparison, retrieval, RiskEvidence, AI structure, tools, agent behavior, Excel, latency, and measurable provider usage.

### 3. Why This Card Exists

Repeatable measurable checks are needed to distinguish deterministic correctness from model quality and to prevent a convincing demo from replacing evaluation.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C18 — Guardrails and Failure Handling

### 1. Card

V1-C18 — Guardrails and Failure Handling

### 2. What We Intended to Build

Implement and prove explicit fail-closed enforcement of commercial, data, AI, security, provider, storage, Excel, and workflow failure boundaries.

### 3. Why This Card Exists

The system must reject invalid or unsupported states visibly rather than silently producing a fabricated quotation or treating partial state as success.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C19 — Golden Case

### 1. Card

V1-C19 — Golden Case

### 2. What We Intended to Build

Prove one controlled end-to-end V1 quotation workflow across validation, history, deterministic analysis, RiskEvidence, agent/Bedrock behavior, approval, Excel, storage/API, observability, and evaluation.

### 3. Why This Card Exists

An integrated representative scenario demonstrates that the independently owned components work together without bypassing governance or hiding failures.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## V1-C20 — Demo UI

### 1. Card

V1-C20 — Demo UI

### 2. What We Intended to Build

Add a lightweight portfolio UI that demonstrates the completed quotation workflow while consuming existing application interfaces and keeping business logic outside presentation code.

### 3. Why This Card Exists

The finished system needs an understandable professional demonstration of evidence, draft state, approval, Excel output, and visible failures without a large frontend project.

### 4. What We Actually Built

NOT YET RECORDED — complete from actual implementation experience.

### 5. Key Design Decisions

NOT YET RECORDED — complete from actual implementation experience.

### 6. Why We Chose This Approach

NOT YET RECORDED — complete from actual implementation experience.

### 7. Alternatives Considered

NOT YET RECORDED — complete from actual implementation experience.

### 8. Why Alternatives Were Not Chosen

NOT YET RECORDED — complete from actual implementation experience.

### 9. Technologies / Libraries Used

NOT YET RECORDED — complete from actual implementation experience.

### 10. Why These Technologies Were Used

NOT YET RECORDED — complete from actual implementation experience.

### 11. Problems Encountered

NOT YET RECORDED — complete from actual implementation experience.

### 12. Root Cause

NOT YET RECORDED — complete from actual implementation experience.

### 13. How We Fixed It

NOT YET RECORDED — complete from actual implementation experience.

### 14. Validation / Evidence References

NOT YET RECORDED — complete from actual implementation experience.

### 15. Tradeoffs and Limitations

NOT YET RECORDED — complete from actual implementation experience.

### 16. What We Learned

NOT YET RECORDED — complete from actual implementation experience.

### 17. What Should Be Remembered Later

NOT YET RECORDED — complete from actual implementation experience.

### 18. Impact on Later Cards

NOT YET RECORDED — complete from actual implementation experience.

## Post-C06 Full-Project Audit and Systemic Repair

The independent full-project audit found three defects before V1-C07. The C01
delivery commit hash was mistyped in the Evidence Map and this log; C05
`summarize_variances()` accepted incompatible metric/unit observations; and
README still described the repository as C01-only. These were not application
Card transitions and did not require changing PROJECT_CONTROL.md.

The maintenance repair corrected the historical C01 hash, added metric/unit
homogeneity validation at the C05 aggregate boundary, and added adversarial
tests for mixed hours/cost and mixed currencies. It also clarified the C05
contract, added verified Git delivery-evidence capture guidance, added a
narrow Card-quality rule for semantic incompatibility testing and capability
documentation review, updated README through C06, and clarified the C01-only
Evidence Map snapshot as historical.

The root causes were separate: manual immutable-hash transcription without
object verification, a generic aggregate API that retained numeric values but
did not enforce their metric/unit identity, and no capability-change trigger
for project-facing documentation review. Governance Harness architecture was
left unchanged because these are Git-process, application-semantic, and
documentation-ownership concerns respectively.

A subsequent full-project audit found that the earlier evidence repair had not
independently re-resolved the C01 object before recording its replacement hash,
so the replacement remained invalid. It also found stale C08-pending and
C07-only state summaries in PROJECT_CONTROL.md. Git/PR verification was repeated
before this bounded remediation; the exact C01 and C03 delivery hashes were then
recorded, and the current PROJECT_CONTROL summaries were reconciled. This is a
second evidence-capture and state-consistency failure, preserved here rather
than rewritten away.

Observed repair validation: C05 focused tests passed 12 tests; related C04,
C05, and C06 tests passed 31 tests; the full suite passed 50 tests; governance
regression passed 60/60; reconciliation passed; and bootstrap reported only
the expected dirty-working-tree warning on the pre-delivery maintenance
branch. After independent re-audit, the repair was delivered through commit
`81b8a61c6c585800f484362f2714092f2375edd8`, PR #14, and merge commit
`eda681e24d4536bc8596f298d5c903471d96b52e`. This maintenance delivery did not
change Card lifecycle state; V1-C07 remains unauthorized.

## Final Principle

CODE EXPLAINS WHAT.
EVIDENCE PROVES WHAT HAPPENED.
THIS LOG EXPLAINS WHY.

DO NOT ERASE FAILURES.
DO NOT INVENT LESSONS.
DO NOT INVENT RATIONALE.
RECORD ROOT CAUSE.
RECORD THE FIX.
RECORD WHY THE FIX WAS CHOSEN.
RECORD WHAT SHOULD BE REMEMBERED.

A FUTURE READER SHOULD BE ABLE TO UNDERSTAND THE PROJECT WITHOUT RELYING ON CHAT HISTORY.
