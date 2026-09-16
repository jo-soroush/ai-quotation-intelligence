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

The repaired generator uses actual-hours values above estimated hours for under-estimate and overrun patterns, below estimates for over-estimate, and within five hours for near-estimate. Five focused C03 tests now prove these relationships, alongside 40 unique valid records, multi-item structure, synthetic provenance, deterministic repeatability, and estimated/actual separation. The implementation was delivered in commit `2041479` through PR #7 and merged to `main` as `9fd7673bbb31167857f8d8f5f468d5631cde302d`; the outcome-only reconciliation recorded C03 as complete without changing the validated dataset.

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

## V1-C07 — Risk Evidence Engine

### 1. Card

V1-C07 — Risk Evidence Engine

### 2. What We Intended to Build

Transform validated comparison results into deterministic, traceable RiskEvidence with reconciled counts, statistics, supporting quote IDs, and visible uncertainty.

### 3. Why This Card Exists

Evidence aggregation must be established separately from later AI risk language so that risk claims remain grounded, reproducible, and provenance-backed.

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

## V1-C08 — Amazon Bedrock Integration

### 1. Card

V1-C08 — Amazon Bedrock Integration

### 2. What We Intended to Build

Add a provider-isolated Amazon Bedrock adapter behind a provider-neutral AI contract with structured validation and explicit failure handling.

### 3. Why This Card Exists

Bedrock is the approved V1 AI direction, but provider payloads and failures must remain outside Core and must never own commercial truth.

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

## V1-C09 — Agent Tools

### 1. Card

V1-C09 — Agent Tools

### 2. What We Intended to Build

Expose existing validated quotation capabilities through typed, bounded, traceable tool contracts without duplicating domain or calculation logic.

### 3. Why This Card Exists

The future agent needs controlled access to approved capabilities while deterministic services remain the owners of business behavior.

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

## V1-C10 — Quotation Agent

### 1. Card

V1-C10 — Quotation Agent

### 2. What We Intended to Build

Build a genuine bounded tool-using quotation agent that selects approved tools and returns validated structured draft output grounded in deterministic results.

### 3. Why This Card Exists

The project requires AI-assisted draft quotation intelligence, but orchestration must remain separate from commercial truth, evidence creation, and human approval.

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

## V1-C11 — Human Review Gate

### 1. Card

V1-C11 — Human Review Gate

### 2. What We Intended to Build

Implement explicit review and approval state transitions between validated agent draft output and finalization eligibility.

### 3. Why This Card Exists

Consequential commercial finalization requires a visible human decision, while approval must not alter deterministic arithmetic truth.

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

## V1-C12 — Excel Generation

### 1. Card

V1-C12 — Excel Generation

### 2. What We Intended to Build

Generate the professional quotation workbook from approved validated state, with traceable evidence and deterministic total reconciliation.

### 3. Why This Card Exists

Excel is the mandatory V1 quotation output and must not allow raw model output to become authoritative numeric content.

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

## V1-C13 — FastAPI Application

### 1. Card

V1-C13 — FastAPI Application

### 2. What We Intended to Build

Expose the quotation workflow through typed FastAPI transport contracts while delegating business ownership to application and domain services.

### 3. Why This Card Exists

Clients need a stable workflow interface, but the transport layer must not become a second owner of quotation logic or approval policy.

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
