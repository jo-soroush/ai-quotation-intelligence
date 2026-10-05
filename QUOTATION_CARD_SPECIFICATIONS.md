# AI Quotation Intelligence System — V1 Card Specifications

Status: CANONICAL GOVERNANCE CONTRACT
Contract metadata only; this file does not own implementation state, Active Card,
or authorization. Read PROJECT_CONTROL.md for live operational state.

This file defines the detailed execution contract for all official V1 Cards.

This file does not authorize implementation.

## Ownership

- Roadmap: Card identity, order, high-level goal, and high-level Exit Gate.
- This file: detailed Card execution contracts.
- PROJECT_CONTROL.md: live project/Card state and authorization.
- QUOTATION_CARD_EVIDENCE_MAP.md: implementation evidence once migrated.
- PROJECT_PROFILE.md: stable architecture and project invariants.
- COMMERCIAL_AND_DATA_GUARDRAILS.md: commercial/data/AI invariants.

## Card Contract Standard

Every Card uses exactly these 14 sections:

1. Title
2. Engineering Goal
3. Learning Goal
4. Why It Exists
5. Architecture Concept
6. Current System Before Card
7. Design Decision
8. Implementation Scope
9. Out of Scope
10. Dependencies
11. Tests / Evaluation
12. Exit Gate
13. What We Learned
14. Completion Evidence

Sections 1–12 define the pre-implementation contract. Sections 13 and 14 are evidence-bearing post-implementation sections. Before implementation, both must remain exactly:

NOT YET RECORDED — complete only from actual implementation evidence.

For C09 and later, complete a compact verification block within each Card's
existing pre-implementation sections before implementation: Risk
Classification and Escalation Triggers; Canonical Sources; a derived
Acceptance Contract (Given, When, Then, failure and prohibited behavior where
meaningful); applicable Critical Invariants; Verification Strategy; Advanced
Verification Decision with REQUIRED, CONDITIONAL / EVALUATE, or
NOT_APPLICABLE plus reason for each Harness technique; Independent Verifier
Expectations; consequential Evidence / Traceability Requirements; and Known
Non-Scope. These fields refine verification of the existing contract, not
Card identity, scope, dependencies, authorization, or architecture. The
Harness owns selection and audit policy; the Evidence Map owns observed
results. No completed C01–C08 contract is retrofitted by this rule.

## Global Execution Rules

- One Card is active at a time.
- No Card implementation starts without explicit human start approval.
- Future-Card leakage, unrelated refactors, and silent architecture expansion are prohibited.
- Material technology additions require approval.
- Deterministic software owns authoritative commercial calculations.
- AI output remains untrusted until parsed and validated.
- RiskEvidence remains separate from RiskSuggestion.
- Unsupported historical or risk claims are prohibited.
- Synthetic portfolio data remains synthetic.
- Final quotation requires human approval.
- Test not run != PASS.
- Design intent != evidence.
- COMPLETE requires exact Exit Gate proof and actual evidence.
- READY_FOR_DELIVERY means implementation, validation, evidence, learning, and quality/Exit Gates are complete while Git delivery is pending.
- One GIT_DELIVERY_APPROVAL covers normal commit, push, PR creation, and merge for the exact validated Card state.
- FINAL_CARD_STATE_CONSISTENCY_GATE must PASS after final reconciliation before a Card may become COMPLETE.
- The next Card requires separate approval.

The Roadmap currently contains no explicit dependency declarations. No dependency is invented in this file.

## V1-C01 — Repository Baseline

### 1. Title

V1-C01 — Repository Baseline

### 2. Engineering Goal

Create the professional repository and application baseline without implementing business logic.

### 3. Learning Goal

Repository structure, Python packaging, environment isolation, configuration boundaries, testing baseline, Git hygiene, and local-first/cloud-ready setup.

### 4. Why It Exists

A clean, secret-safe baseline is required before domain implementation can be owned and evaluated coherently.

### 5. Architecture Concept

Establish clean repository, package, configuration, and test ownership boundaries before domain implementation.

### 6. Current System Before Card

The project is in GOVERNANCE_MIGRATION. No application package, tests, pyproject.toml, dependency baseline, or Git repository is currently verified.

This Card is a contract, not a claim that the Card has started or that its dependencies are complete.

### 7. Design Decision

Repository baseline only; no business logic or future Card implementation is included.

### 8. Implementation Scope

- initialize Git repository when this Card is authorized
- establish professional repository structure
- create Python project/package baseline
- establish clean package ownership
- create tests baseline
- add pyproject.toml or justified dependency/config baseline
- add .gitignore
- add .env.example only if justified
- add README baseline if supported by the Roadmap
- establish configuration boundary
- establish local test command
- establish a secret-safe baseline

### 9. Out of Scope

- quote domain models
- synthetic historical data
- calculation or comparison engines
- retrieval or risk intelligence
- Bedrock, agent tools, or quotation agent
- human approval implementation
- Excel business output
- FastAPI workflow
- S3, Lambda, API Gateway, or CloudWatch
- evaluation harness or Demo UI

### 10. Dependencies

Explicit Roadmap dependency: none stated. Preserve the Roadmap order; do not infer additional dependencies.

The Roadmap is authoritative for dependency facts. If a dependency is unclear, stop with CARD_SPEC_ROADMAP_MISMATCH rather than guessing.

### 11. Tests / Evaluation

Repository structure, importability, configuration boundary, secret-safe baseline, and test-command baseline only. No business behavior is evaluated.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The repository has the professional structure, package/configuration baseline, local test baseline, and secret-safe setup required by the Roadmap for C02. No business logic is included.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C01

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 32. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 33. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C02 — Domain Models

### 1. Title

V1-C02 — Domain Models

### 2. Engineering Goal

Create typed domain and Pydantic contracts for quotation intelligence.

### 3. Learning Goal

Typed contracts, validation boundaries, explicit units, estimated/actual semantics, provenance, and provider-neutral Core ownership.

### 4. Why It Exists

Stable domain contracts prevent transport, provider, and model payloads from becoming commercial truth.

### 5. Architecture Concept

Typed domain contracts own quotation concepts and semantics; provider and transport models remain outside Core.

### 6. Current System Before Card

C01 may provide the repository/package baseline. No quotation domain models are currently implemented or evidenced.

This Card is a contract, not a claim that the Card has started or that its dependencies are complete.

### 7. Design Decision

Define typed contracts and validation semantics without implementing calculations, retrieval, AI, or persistence.

### 8. Implementation Scope

- define applicable concepts: Quote, QuoteItem, HistoricalQuote, ProjectOutcome, NewQuoteRequest, VarianceResult, SimilarQuote, RiskEvidence, RiskSuggestion, DraftQuote, ApprovalDecision, AgentRequest, AgentResult
- encode explicit hours and currency
- preserve estimated versus actual separation
- distinguish null, zero, and unknown
- validate numeric values and units
- represent synthetic provenance where applicable
- keep provider SDK ownership outside Core

### 9. Out of Scope

- calculation engine
- synthetic dataset
- historical comparison logic
- similarity engine
- risk analysis
- Bedrock or agent
- Excel, API, or AWS persistence

### 10. Dependencies

Explicit Roadmap dependency: none stated. C02 follows C01 in the Roadmap sequence; do not infer more.

The Roadmap is authoritative for dependency facts. If a dependency is unclear, stop with CARD_SPEC_ROADMAP_MISMATCH rather than guessing.

### 11. Tests / Evaluation

Valid and invalid models, required fields, numeric safety, missing/null/zero semantics, estimated/actual separation, currency/time semantics, and provenance semantics.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

Typed quotation domain contracts validate the required boundaries and are ready for C03 without owning calculations, provider payloads, or future capabilities.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C02

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C03 — Synthetic Historical Data

### 1. Title

V1-C03 — Synthetic Historical Data

### 2. Engineering Goal

Create realistic, controlled synthetic quotation history for portfolio use.

### 3. Learning Goal

Synthetic data design, provenance labeling, controlled patterns, reproducibility, and dataset quality checks.

### 4. Why It Exists

Historical comparison and evidence require representative, clearly synthetic records that can support repeatable evaluation.

### 5. Architecture Concept

Synthetic historical records conform to C02 contracts and remain distinguishable from real company information.

### 6. Current System Before Card

C02 may provide typed contracts. No synthetic historical dataset exists or is evidenced.

This Card is a contract, not a claim that the Card has started or that its dependencies are complete.

### 7. Design Decision

Use approximately 40 fictional quotation cases with multiple work items and deliberately designed patterns rather than meaningless random noise.

### 8. Implementation Scope

- create approximately 40 historical quotation cases
- include multiple work items per quotation
- include fictional categories and roles
- include estimated values and actual outcomes
- include scope-change/outcome context where defined by C02
- preserve synthetic provenance
- implement reproducibility if generation code is used
- include controlled under-, near-, and over-estimate patterns

### 9. Out of Scope

- analytics or comparison engine
- similarity retrieval
- RiskEvidence generation
- Bedrock or agent
- human approval
- Excel, API, or AWS implementation

### 10. Dependencies

Explicit Roadmap dependency: none stated. C03 follows C02 in the Roadmap sequence; do not infer more.

The Roadmap is authoritative for dependency facts. If a dependency is unclear, stop with CARD_SPEC_ROADMAP_MISMATCH rather than guessing.

### 11. Tests / Evaluation

Schema validity, quote/item relationships, approximate intended record count, synthetic provenance, controlled-pattern sanity checks, deterministic reproducibility where applicable, and absence of real company data.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

A valid, clearly synthetic, meaningful historical quotation dataset exists and supports the next deterministic intelligence Card without implementing analytics.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C03

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C04 — Quote Calculation Engine

### 1. Title

V1-C04 — Quote Calculation Engine

### 2. Engineering Goal

Implement deterministic authoritative quotation arithmetic.

### 3. Learning Goal

Commercial arithmetic, numeric validation, unit/currency handling, reproducibility, and reconciliation.

### 4. Why It Exists

Quotation totals must be independently calculable and must not depend on model output.

### 5. Architecture Concept

The deterministic quote engine owns authoritative item costs, totals, and applicable reconciliation; it has no model dependency.

### 6. Current System Before Card

C01–C03 may provide the baseline, contracts, and synthetic inputs. No authoritative calculation engine is currently implemented or evidenced.

This Card is a contract, not a claim that the Card has started or that its dependencies are complete.

### 7. Design Decision

Keep commercial truth in deterministic code and make missing, invalid, and non-finite values explicit failures.

### 8. Implementation Scope

- calculate validated estimated item costs
- calculate validated estimated totals
- implement applicable deterministic arithmetic
- validate numeric inputs
- preserve explicit missing-value behavior
- preserve explicit currency/time semantics
- ensure reproducibility
- keep the engine independent of model output

### 9. Out of Scope

- historical comparison engine
- similarity retrieval
- risk evidence
- Bedrock or agent
- Excel finalization
- FastAPI or AWS deployment

### 10. Dependencies

Explicit Roadmap dependency: none stated. C04 follows C03 in the Roadmap sequence; do not infer more.

The Roadmap is authoritative for dependency facts. If a dependency is unclear, stop with CARD_SPEC_ROADMAP_MISMATCH rather than guessing.

### 11. Tests / Evaluation

Hours × rate, totals, missing hours, missing rates, zero, invalid numeric input, non-finite values, reconciliation, and explicit currency/unit handling.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

Deterministic quotation arithmetic is validated for the Card scope, reconciles correctly, and is ready to support later analysis without AI or provider dependency.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C04

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C05 — Historical Comparison Engine

### 1. Title

V1-C05 — Historical Comparison Engine

### 2. Engineering Goal

Compare historical estimates against actual delivery outcomes deterministically.

### 3. Learning Goal

Variance semantics, aggregate statistics, denominator handling, missing outcomes, and scope-change context.

### 4. Why It Exists

Evidence-backed quotation intelligence requires reproducible comparison of estimates and actual outcomes.

### 5. Architecture Concept

Historical comparison consumes validated historical records and produces deterministic variance/statistical results; missing outcomes remain explicit.

### 6. Current System Before Card

C01–C04 may provide the baseline, domain contracts, synthetic records, and quote arithmetic. No historical comparison engine is currently implemented or evidenced.

This Card is a contract, not a claim that the Card has started or that its dependencies are complete.

### 7. Design Decision

Use variance = actual - estimated, handle invalid denominators explicitly, and keep scope-change-driven outcomes distinguishable.

### 8. Implementation Scope

- calculate hour variance
- calculate cost variance
- calculate percentage variance where valid
- calculate overrun counts
- calculate average and median variance where owned here
- aggregate only observations from one compatible metric and unit domain; reject mixed hours/cost or mixed currencies
- preserve scope-change context
- preserve delay/outcome context only where validated data supports it
- keep all results deterministic and independent of AI

### 9. Out of Scope

- similar quote retrieval
- RiskEvidence construction
- Bedrock or agent
- human approval
- Excel, API, or AWS implementation

### 10. Dependencies

Explicit Roadmap dependency: none stated. C05 follows C04 in the Roadmap sequence; do not infer more.

The Roadmap is authoritative for dependency facts. If a dependency is unclear, stop with CARD_SPEC_ROADMAP_MISMATCH rather than guessing.

### 11. Tests / Evaluation

Estimate/actual separation, positive/negative/zero variance, percentage variance, zero denominator, missing actual values, aggregate counts, average/median calculations where owned, homogeneous metric/unit aggregation, incompatible-unit rejection, scope-change context, and no AI involvement.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

Historical estimate-vs-actual comparisons and applicable aggregate statistics are deterministic, explicit about missing outcomes, and ready to support C06/C07.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C05

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C06 — Similar Quote Retrieval

### 1. Title

V1-C06 — Similar Quote Retrieval

### 2. Engineering Goal

Retrieve relevant historical quotations using bounded, explainable V1 similarity logic.

### 3. Learning Goal

Deterministic retrieval and ranking, similarity feature selection, empty-result behavior, and why similarity remains contextual rather than authoritative.

### 4. Why It Exists

A new quotation needs relevant historical context, but comparable records must not silently become prices, effort commitments, or facts.

### 5. Architecture Concept

HistoricalQuote data → validated comparison features → similarity logic → ranked SimilarQuote results.

### 6. Current System Before Card

C01–C05 may later provide the repository baseline, domain contracts, synthetic history, deterministic arithmetic, and historical comparisons. Current application implementation remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Use simple explainable retrieval suitable for V1 before introducing vector databases or RAG. Similarity is context, not truth.

### 8. Implementation Scope

- select supported features such as project type, work items, role mix, team size, duration, delivery model, and scope characteristics
- validate compatible inputs
- rank comparable historical quotations
- return explanations and stable identity/provenance
- handle empty and insufficient result sets deterministically

### 9. Out of Scope

- new hourly rates, prices, or final effort from similarity
- RiskEvidence generation
- AI interpretation or Bedrock orchestration
- full agent
- human approval
- Excel, FastAPI, S3, or AWS deployment
- vector database or RAG by default

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Expected relevant results, ranking sanity, deterministic behavior where appropriate, empty history, insufficient comparable cases, incompatible semantics, no automatic price copying, and stable result identity/provenance.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require bounded, explainable, validated comparable-quotation retrieval with explicit empty/insufficient-result behavior and no price-copy semantics.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C06

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C07 — Risk Evidence Engine

### 1. Title

V1-C07 — Risk Evidence Engine

### 2. Engineering Goal

Transform validated historical comparison results into deterministic, traceable RiskEvidence.

### 3. Learning Goal

Evidence aggregation versus AI interpretation, uncertainty representation, source traceability, and honest evidence thresholds.

### 4. Why It Exists

Risk intelligence must be grounded in reproducible historical evidence rather than unsupported model narrative.

### 5. Architecture Concept

HistoricalQuote → Comparison Engine → Similar Quote Retrieval → deterministic statistics → RiskEvidence.

### 6. Current System Before Card

C01–C06 may later provide contracts, synthetic history, comparison results, and comparable records. No RiskEvidence implementation currently exists; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Evidence statistics belong to deterministic software. AI may later interpret them but cannot create or rewrite them.

### 8. Implementation Scope

- calculate comparable project count
- calculate overrun count and rate
- calculate average and median variance where supported
- retain supporting quote IDs and work-item context
- retain scope-change and outcome context where available
- return INSUFFICIENT_EVIDENCE when evidence is weak

### 9. Out of Scope

- natural-language risk narrative
- Bedrock integration
- agent orchestration
- human approval
- Excel, API, or AWS deployment

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Numerator/denominator reconciliation, evidence IDs, source-record counts, aggregate reconciliation, missing actuals not becoming success, unsupported categories, insufficient evidence visibility, scope-change distinction, and reproducibility.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require deterministic, traceable RiskEvidence with reconciled counts/statistics and explicit insufficient-evidence behavior.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C07

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C08 — Amazon Bedrock Integration

### 1. Title

V1-C08 — Amazon Bedrock Integration

### 2. Engineering Goal

Add Amazon Bedrock behind a provider-isolated AI contract without allowing SDK objects into Core.

### 3. Learning Goal

boto3 Bedrock Runtime, Converse API, structured responses, adapter isolation, schema validation, timeout/retry behavior, and explicit failures.

### 4. Why It Exists

Controlled AI interpretation requires a replaceable provider boundary and explicit handling of invalid or unavailable model responses.

### 5. Architecture Concept

Core → AI Provider Contract → Bedrock Adapter → Amazon Bedrock.

### 6. Current System Before Card

C01–C07 may later provide the baseline, contracts, data, arithmetic, comparison, retrieval, and evidence services. Bedrock is planned but not integrated; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Amazon Bedrock is the V1 provider, with Amazon Nova as the initial direction, while provider-specific request/response formats remain inside the adapter.

### 8. Implementation Scope

- define the provider contract
- implement the Bedrock adapter boundary
- use boto3 and Converse API where appropriate
- parse and validate structured responses
- implement bounded retry and timeout behavior
- expose AI_INVALID and AI_UNAVAILABLE explicitly
- keep secrets and provider payloads outside Core
- prevent authoritative commercial arithmetic in model output

### 9. Out of Scope

- full quotation agent
- tool orchestration
- human approval
- Excel
- FastAPI workflow
- S3 business persistence unless explicitly required by the Roadmap
- deployment, RAG, Knowledge Bases, or multi-agent architecture

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Provider contract, valid mocked response, invalid response, schema failure, timeout, provider exception, retry bound, AI_UNAVAILABLE, AI_INVALID, and no provider-payload leakage into Core. Real network calls are not required for every test.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require a provider-isolated Bedrock adapter with validated structured responses, bounded failure behavior, and no provider ownership in Core.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C08

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C09 — Agent Tools

### 1. Title

V1-C09 — Agent Tools

### 2. Engineering Goal

Expose existing quotation capabilities as validated tools for the future quotation agent.

### 3. Learning Goal

Tool contracts, orchestration boundaries, error propagation, delegation, and preventing duplicated business logic inside prompts.

### 4. Why It Exists

The agent needs bounded capabilities with typed inputs, outputs, and explicit failures rather than hidden prompt logic.

### 5. Architecture Concept

Quotation Agent → Tool Interface → existing application/domain services.

### 6. Current System Before Card

C01–C08 have delivered the baseline, domain services, retrieval, evidence,
and Bedrock adapter according to PROJECT_CONTROL.md and their Evidence Map
records. The C09 tool layer and C10 agent are not implemented.

This is a pre-implementation contract description, not evidence that C09 is
authorized or complete. Query PROJECT_CONTROL.md for live state.

### 7. Design Decision

Tools wrap existing validated capabilities and do not become a second business-logic layer.

### 8. Implementation Scope

- define validated tool interfaces
- expose planned categories such as historical retrieval, similarity, statistics, comparison, risk evidence, draft, validation, and Excel
- delegate to existing owned capabilities
- validate inputs and outputs
- propagate failures explicitly
- retain traceable tool identity
- keep arithmetic outside prompts

### 9. Out of Scope

- reimplementation of C04–C07 engines
- full agent decision loop
- final approval
- Excel finalization beyond an owned capability
- API or deployment

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Tool input/output validation, deterministic service delegation, failure propagation, missing data, unsupported operations, traceability, and no commercial-authority leakage into the model layer.

Pre-implementation C09 verification block (derived from this Card sections
2, 5, 7–9, 11–12; Roadmap V1-C09; PROJECT_PROFILE.md sections 10, 17–18;
COMMERCIAL_AND_DATA_GUARDRAILS.md G02–G03, G08–G10, G24, G30–G31, G36,
G39):

- Risk Classification: ELEVATED for tool execution and untrusted boundaries.
  Reassess if actual C09 scope introduces an external or irreversible effect;
  that change requires its own authorization and risk decision.
- Escalation Triggers: tool invocation, validation, evidence provenance,
  commercial authority, explicit failure propagation, future agent use.
- Acceptance Contract: Given validated inputs and an available approved
  existing service, when its tool interface is invoked, then it delegates to
  that service and returns a validated, traceable result. Given invalid input,
  malformed output, unavailable capability, or service failure, when invoked,
  then it fails explicitly without fabricated success. It must never compute
  authoritative totals, invent RiskEvidence, approve/finalize a quotation,
  invoke an unauthorized action, or implement a future-Card capability.
- Critical Invariants: existing service ownership is preserved; tool results
  and model output are untrusted until validated; failures remain failures;
  source identity remains traceable; no AI or tool path overrides
  deterministic commercial truth or human approval.
- Verification Strategy: independent contract cases for valid and invalid
  input/output, delegation, unsupported capability, failure propagation,
  provenance, and forbidden authority; mechanical Core import boundary check.
- Advanced Verification Decision (reassess against actual C09 design at Card
  start; no framework is implied):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Service ownership and authority boundaries |
  | Contract tests | REQUIRED | Typed input/output and explicit failures |
  | Integration | CONDITIONAL / EVALUATE | Needed if tool-service wiring cannot be proven by contract tests |
  | Generated property tests | CONDITIONAL / EVALUATE | Only if combinatorial validated inputs exceed focused examples |
  | Targeted mutation-resistance | CONDITIONAL / EVALUATE | Challenge consequential permission/failure assertions if examples appear weak |
  | Failure injection | CONDITIONAL / EVALUATE | Required if actual interface has ambiguous partial failure or replay |
  | Fuzzing | NOT_APPLICABLE | No unbounded parser surface is specified |
  | Differential | NOT_APPLICABLE | No alternative equivalent implementation is specified |
  | Concurrency/race | CONDITIONAL / EVALUATE | Needed if shared state or concurrent execution is introduced |
  | Adversarial testing | REQUIRED | Malformed inputs/results and unauthorized operation probes |
  | Threat modeling | REQUIRED | Tool execution creates a trust/permission boundary |
  | Agent evals | NOT_APPLICABLE | Full agent loop belongs to C10/C17 |
  | Rollback/recovery | CONDITIONAL / EVALUATE | Needed if C09 creates persistent or external effects |
  | Formal methods | NOT_APPLICABLE | No exceptional formal-state risk is specified |
- Independent Verifier Expectations: spec-first review of the frozen diff,
  independent counterexamples, false-green challenge, failure and permission
  review, and evidence/architecture checks. Findings require re-audit.
- Evidence / Traceability Requirements: map consequential tool validation,
  delegation, provenance, failure, and prohibited-authority claims to actual
  implementation paths, executed cases, and observed results in the Evidence
  Map. Before execution, observations remain NOT_YET_EXECUTED.
- Known Non-Scope: section 9 remains authoritative. Planned tool categories
  whose underlying capability is not yet owned by a completed Card cannot
  silently become implementations or successful invocations in C09.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require bounded, validated tool contracts that delegate to existing capabilities without duplicate business ownership.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C09

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C10 — Quotation Agent

### 1. Title

V1-C10 — Quotation Agent

### 2. Engineering Goal

Build a genuine tool-using AI quotation agent that orchestrates approved tools and produces validated structured draft output.

### 3. Learning Goal

Practical agent orchestration, tool selection, structured model output, grounding, failure handling, and human-in-the-loop boundaries.

### 4. Why It Exists

The original business requirement calls for an AI agent that creates draft quotations, while commercial truth and final approval remain deterministic and human-owned.

### 5. Architecture Concept

Quotation Request → Agent → approved tools → validated evidence and deterministic results → Bedrock reasoning → structured DraftQuote/AgentResult → validation.

### 6. Current System Before Card

C01–C09 may later provide the baseline, contracts, data, deterministic services, Bedrock adapter, and tool interfaces. No quotation agent is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

The agent orchestrates validated capabilities but does not own commercial truth, evidence creation, approval, or finalization.

### 8. Implementation Scope

- understand the quotation request
- identify missing information
- select and invoke approved tools
- gather historical evidence
- interpret validated deterministic results
- explain evidence-backed risks
- draft quotation narrative
- express uncertainty
- return validated structured output
- propagate AI, tool, evidence, and commercial failures explicitly

### 9. Out of Scope

- hourly rates, actual outcomes, evidence IDs/counts, or authoritative totals invented by AI
- deterministic calculation replacement
- final approval or autonomous final state
- final Excel export
- FastAPI, S3, deployment, UI, or multi-agent architecture

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Tool selection, required invocation, tool-result use, missing information, insufficient evidence, unsupported claims, invalid output, Bedrock unavailability, tool failure, structured result validation, unchanged deterministic numbers, and no approval bypass.

Pre-implementation C10 verification block (derived from this Card sections
2, 5, 7–9, 11–12; Roadmap V1-C10; PROJECT_PROFILE.md; and
COMMERCIAL_AND_DATA_GUARDRAILS.md; this is a verification plan, not C10
authorization or implementation evidence):

- Risk Classification: ELEVATED for model-directed tool selection and the
  commercial/evidence trust boundary. Reassess if implementation introduces
  external or irreversible effects beyond this Card.
- Escalation Triggers: agent autonomy and tool execution; untrusted model,
  argument, and tool output; evidence provenance; commercial authority;
  missing information and explicit failure; human approval boundary.
- Canonical Sources: Roadmap V1-C10, this Card's sections 2–12,
  PROJECT_PROFILE.md, COMMERCIAL_AND_DATA_GUARDRAILS.md, and the existing C08
  provider and C09 tool contracts. These do not grant C11+ scope.
- Acceptance Contract: Given a quotation request and available approved C09
  tools, when the agent reasons and acts, then it selects only those tools,
  validates selection, arguments, and results, and returns a grounded,
  validated structured AgentResult for review. Given missing information,
  insufficient evidence, invalid model/tool output, or unavailable or failed
  capabilities, it surfaces the condition explicitly rather than fabricating
  success. It never invents commercial values or evidence, changes
  deterministic results, or approves/finalizes a quotation.
- Critical Invariants: deterministic software, not the model, owns commercial
  truth; only authorized C09 tools execute; model arguments and tool results
  remain untrusted until validated; evidence retains provenance and missing
  evidence stays visible; provider-specific objects do not become Core domain
  state; orchestration is bounded and fails closed; C11+ ownership and human
  approval remain outside C10. Verify with contract, adversarial, failure,
  and architecture cases rather than prompt wording alone.
- Verification Strategy: use deterministic request/result contract tests,
  mocked Bedrock and C09 tool traces, malformed/contradictory output and
  failure cases, bounded-orchestration checks, provenance and commercial
  invariant checks, and the existing architecture boundary suite. Live
  provider testing is evaluated against the eventual implementation and
  available environment, not presumed by this pre-implementation block.
- Advanced Verification Decision (reassess against the actual C10 design at
  Card start; no implementation mechanism or new framework is prescribed):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Commercial authority, provenance, and bounded action must hold |
  | Contract tests | REQUIRED | Validated tool and structured result boundaries |
  | Integration | CONDITIONAL / EVALUATE | Evaluate whether mocked contracts suffice to prove component wiring |
  | Generated property tests | CONDITIONAL / EVALUATE | Use if combinatorial routing or validated input space exceeds focused cases |
  | Targeted mutation-resistance | CONDITIONAL / EVALUATE | Challenge consequential routing, failure, and approval assertions |
  | Failure injection | REQUIRED | Bedrock/tool unavailability and invalid output must fail explicitly |
  | Fuzzing | CONDITIONAL / EVALUATE | Evaluate if the chosen parser exposes a broad untrusted input surface |
  | Differential | NOT_APPLICABLE | No equivalent second implementation is specified |
  | Concurrency/race | CONDITIONAL / EVALUATE | Needed if shared state or concurrent execution is introduced |
  | Adversarial testing | REQUIRED | Probe invented values/evidence, unauthorized tools, and model override attempts |
  | Threat modeling | REQUIRED | Model-directed tool use crosses a permission and trust boundary |
  | Agent evals | CONDITIONAL / EVALUATE | Evaluate bounded C10 behavior; C17 evaluation infrastructure is not C10 scope |
  | Rollback/recovery | CONDITIONAL / EVALUATE | Needed if actual C10 design introduces persistent or external effects |
  | Formal methods | NOT_APPLICABLE | No exceptional formal-state risk is specified |
- Independent Verifier Expectations: inspect the frozen candidate against the
  Roadmap Exit Gate and C10 contract, challenge false-green tests and
  commercial/evidence authority, verify only available C09 tools are used,
  inspect failure and architecture boundaries, and require re-audit after a
  material correction.
- Evidence / Traceability Requirements: link consequential tool-selection,
  input/output validation, grounding, provenance, boundedness, failures,
  commercial invariants, and prohibited approval claims to actual paths,
  executed tests, and observed outcomes in the Evidence Map. Record material
  design rationale and lessons in the Learning Log. Until C10 is authorized
  and executed, these observations remain NOT_RUN / NOT_PROVEN.
- Known Non-Scope: section 9 remains authoritative; C11 human review,
  C12 final Excel export, C13+ interfaces, storage, deployment, observability,
  evaluation infrastructure, and later platform work stay with their Cards.
  No exact call count, wire schema, protocol placement, or new architecture
  dependency permission is selected here.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require a genuine bounded tool-using agent that returns grounded validated draft output without overriding deterministic truth or human approval.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C10

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C11 — Human Review Gate

### 1. Title

V1-C11 — Human Review Gate

### 2. Engineering Goal

Implement explicit human review and approval before final quotation finalization.

### 3. Learning Goal

Human-in-the-loop state transitions, approval boundaries, consequential-action control, and why approval must not mutate deterministic truth.

### 4. Why It Exists

Commercial finalization requires a deliberate human decision after validation rather than an autonomous model or tool transition.

### 5. Architecture Concept

Agent Draft → Deterministic Validation → AWAITING_REVIEW → Human Approve / Reject → finalization eligibility.

### 6. Current System Before Card

C01–C10 may later provide the repository, contracts, deterministic services, evidence, provider boundary, tools, and agent. No review gate is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Represent review and approval explicitly. No agent, Bedrock call, or tool may approve, and approval cannot override arithmetic.

### 8. Implementation Scope

- represent DRAFT, VALIDATED, AWAITING_REVIEW, APPROVED, and REJECTED conceptually
- block finalization without explicit human approval
- keep rejection visible
- reject invalid state transitions
- require recalculation/revalidation when validated commercial inputs change
- preserve deterministic totals through approval

### 9. Out of Scope

- Excel generation itself
- FastAPI transport
- S3 integration
- AWS deployment
- UI implementation

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Unapproved finalization blocked, approve path, reject path, invalid transitions, agent self-approval blocked, changed-input invalidation where applicable, and approval not altering deterministic totals.

Pre-implementation C11 verification block (derived from this Card sections
2, 5, 7–12; Roadmap V1-C11; PROJECT_PROFILE.md;
COMMERCIAL_AND_DATA_GUARDRAILS.md; and existing domain/C10 contracts; this is
a verification plan, not C11 authorization or implementation evidence):

- Risk Classification: ELEVATED because human approval is a consequential
  commercial authority boundary; a bypass could permit unauthorized
  finalization or falsely attribute a decision to a human.
- Escalation Triggers: approval/authorization bypass, substituted or changed
  draft or evidence, invalid upstream result, invalid state transition,
  deterministic-total mutation, and future-Card finalization leakage.
- Canonical Sources: Roadmap V1-C11, this Card's sections 2–12,
  PROJECT_PROFILE.md, COMMERCIAL_AND_DATA_GUARDRAILS.md, and existing
  DraftQuote, AgentResult, ApprovalDecision, and QuoteStatus contracts.
- Acceptance Contract: Given a valid or revalidated draft and an explicit
  human review action, when review occurs, then approve or reject is recorded
  as an explicit validated state bound to the reviewed quote and evidence,
  without changing deterministic commercial results. Given absent human
  action, invalid or unsuccessful C10 output, changed commercial inputs,
  substituted evidence, or an invalid transition, review must not produce
  approvable success or finalization eligibility. AI, agents, models, and
  tools cannot impersonate the human decision; C12+ export is not performed.
- Critical Invariants: no human approval means no final quotation (Roadmap
  V1-C11; Guardrail G16); approval is human-only and never overrides
  arithmetic (G17/G39); invalid or changed drafts require validation before
  review (this Card sections 5 and 8); reviewed quote/evidence identity and
  provenance remain bound to the decision (G08 and Roadmap V1-C11); explicit
  approve/reject state and invalid-transition rejection remain visible (this
  Card section 8). Verify with deterministic contract, changed-input,
  provenance, and adversarial authority cases.
- Verification Strategy: focused approve/reject and approval-required cases;
  invalid-transition and changed-input cases; unsuccessful C10 result,
  substituted draft/evidence, and AI self-approval attempts; deterministic
  total preservation; relevant C10/domain regression and architecture checks.
  Test the chosen review boundary without requiring C12+ infrastructure.
- Advanced Verification Decision (reassess against actual C11 design at Card
  start; no new testing framework or implementation mechanism is prescribed):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Approval and commercial authority must remain separate |
  | Contract tests | REQUIRED | Review inputs, decisions, and state boundaries must validate |
  | Integration | CONDITIONAL / EVALUATE | Evaluate actual C10-to-review and later finalization boundary wiring |
  | Generated property tests | CONDITIONAL / EVALUATE | Use if transition/input combinations exceed focused examples |
  | Targeted mutation-resistance | REQUIRED | Challenge consequential approval and invalid-transition checks |
  | Failure injection | REQUIRED | Invalid or unavailable upstream results and failed validation must not approve |
  | Fuzzing | CONDITIONAL / EVALUATE | Evaluate if the chosen boundary adds a broad untrusted input surface |
  | Differential | NOT_APPLICABLE | No second equivalent review implementation is specified |
  | Concurrency/race | CONDITIONAL / EVALUATE | Evaluate if shared or persistent decision state is introduced |
  | Adversarial testing | REQUIRED | Probe impersonation, substituted drafts/evidence, and bypass |
  | Threat modeling | REQUIRED | Human authority is a consequential trust boundary |
  | Agent evals | NOT_APPLICABLE | C11 does not own agent quality or C17 evaluation infrastructure |
  | Rollback/recovery | CONDITIONAL / EVALUATE | Evaluate if decisions gain persistent or external effects |
  | Formal methods | NOT_APPLICABLE | No exceptional formal-state requirement is specified |
- Independent Verifier Expectations: inspect the frozen candidate against
  the Roadmap Exit Gate and this contract; challenge false-green approval,
  invalid-transition, provenance, changed-input, and commercial-truth tests;
  verify no C12+ capability or unapproved architecture permission was added.
- Evidence / Traceability Requirements: link the review decision boundary,
  input/result validation, quote/evidence identity, deterministic-total
  preservation, approval-required behavior, failure paths, and prohibited
  autonomous approval to actual paths, executed tests, and observed results
  in the Evidence Map. Preserve material rationale in the Learning Log.
  Until C11 is separately authorized and executed, these remain NOT_RUN /
  NOT_PROVEN.
- Known Non-Scope: section 9 remains authoritative. Excel generation,
  FastAPI, S3, deployment, UI, multi-agent workflow, autonomous approval,
  C18's general guardrail platform, and C12+ infrastructure/workflows remain
  outside C11. Exact transition matrix, terminality, repeated decisions,
  re-review, draft-version binding, reviewer identity mechanism, audit
  storage, timestamp policy, architecture placement, and error taxonomy are
  deferred to authorized C11 implementation and must satisfy the gate.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require an explicit review/approval state and enforcement of approval before final quotation finalization.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C11

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C12 — Excel Generation

### 1. Title

V1-C12 — Excel Generation

### 2. Engineering Goal

Generate the mandatory professional quotation workbook using openpyxl from approved validated state.

### 3. Learning Goal

Spreadsheet generation, reconciliation, traceability, formatting boundaries, and separation of AI narrative from authoritative numeric cells.

### 4. Why It Exists

Excel is a mandatory business output and must faithfully represent approved deterministic quotation state.

### 5. Architecture Concept

Approved Validated Quote → Excel Generation → Reconciliation Check → Final Workbook.

### 6. Current System Before Card

C01–C11 may later provide contracts, deterministic calculations, review state, and approval. No workbook generator is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Authoritative numeric cells come from validated deterministic Core state;
final export requires a fresh C11 approval-eligibility check against the
current result and exact reconciliation. C12 V1 renders static authoritative
values; workbook formulas are not a second business-rule authority.

### 8. Implementation Scope

- generate a valid `.xlsx` workbook with the required V1 Quotation, Risk
  Analysis, and Historical Evidence sheets; their minimum semantic content is
  defined in the Roadmap, not by fixed cell coordinates or styling
- use C11's held approval eligibility gate against the current validated
  `AgentResult` before export; a copied `ReviewRecord`, a status value, or an
  approval-looking Quote is not export authority; reject rejected, unreviewed,
  stale, or modified state. C11's gate is in-memory/same-process in V1
- write only validated quotation identity, currency, work items, hours, rates,
  and static Core-derived item costs and total; reconcile the workbook's
  commercial values exactly with deterministic Core results
- render only risk suggestions and evidence IDs bound to that approved
  result. The Historical Evidence sheet records those IDs and their approved
  suggestion links; it does not claim historical quote IDs, estimated/actual
  values, variance, or comparison details absent from the approved payload.
  C12 does not independently search for or select evidence after approval
- treat `role` as optional/unsupported for V1 because `QuoteItem` has no such
  field; never infer or fabricate it from other text or history
- render untrusted text inert, including formula-like leading `=`, `+`, `-`,
  or `@`, without prescribing an escaping mechanism; preserve only supported
  provenance and never present synthetic history as real
- fail explicitly on invalid state, workbook validation, or reconciliation;
  use openpyxl as the specified C12 library after implementation approval.
  Its dependency is not added by this pre-C12 maintenance. Output bytes versus
  a local path and local file handling remain implementation decisions;
  `Draft_Quote.xlsx` is an example name, not a mandatory path

### 9. Out of Scope

- API transport
- S3 storage integration
- AWS deployment
- UI
- new commercial calculations inside the workbook
- persistence, reviewer authentication infrastructure, email, Bedrock
  reasoning, autonomous approval, multi-agent workflow, and C18's general
  guardrail platform

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Workbook creation/loadability with openpyxl; the three required sheets and
their supported fields; semantic content, sheet-set, and contract-required
ordering repeatability without byte-identical ZIP requirements; exact Core
numeric reconciliation; held C11 approval gate, rejected/unreviewed and
stale/modified input rejection; bound evidence-reference traceability and
synthetic-source honesty; unsupported role/historical-field non-fabrication;
inert untrusted/formula-like text; explicit validation/export failures; no
numeric authority from model text or workbook formulas; no C13+ behavior.

Pre-implementation C12 verification block (derived from this Card, Roadmap
V1-C12, PROJECT_PROFILE.md, COMMERCIAL_AND_DATA_GUARDRAILS.md, and delivered
C02/C04/C09/C10/C11 contracts; this is a verification plan, not C12
authorization or implementation evidence):

- Risk Classification: ELEVATED because final Excel export crosses the human
  approval and commercial-output boundaries. A bypass, changed draft, or
  incorrect workbook total could produce a consequential false quotation.
- Escalation Triggers: approval bypass or stale replay; numeric or currency
  drift; invented role/history/evidence; formula interpretation of untrusted
  text; synthetic history represented as real; invalid workbook or failure
  treated as successful final export; C13+ scope leakage.
- Canonical Sources: Roadmap V1-C12 and its Exit Gate, this Card's sections
  2–12, PROJECT_PROFILE.md, COMMERCIAL_AND_DATA_GUARDRAILS.md, Core C04
  arithmetic, C10 `AgentResult`, and C11 `ReviewSession.require_approved`.
- Acceptance Contract: Given a current validated C10 result and held C11
  approval, when C12 rechecks eligibility, it may render a loadable `.xlsx`
  with the three required sheets, static Core-derived commercial values,
  approved risk/evidence references, and explicit provenance limitations.
  Without approval or with rejected, changed, or stale input, export fails.
  Unsupported role or historical figures are not fabricated. Invalid workbook
  content, formula-active untrusted text, or total mismatch cannot succeed.
- Critical Invariants: no current C11 approval means no final Excel (Roadmap
  V1-C12; Guardrails G16/G40); C11 eligibility is not inferred from a copied
  record or status (delivered C11 boundary); Excel numbers equal Core truth
  (G15/G22); evidence is only approved/bound evidence (G08/G09/G33);
  synthetic provenance is not misrepresented (G11); text cannot become an
  executable formula; missing commercial or historical values are not
  silently filled (G04/G05/G19/G29). Verify with contract, reconciliation,
  changed-input, provenance, and adversarial export cases.
- Verification Strategy: focus on approved export, all denied approval states,
  stale/modified data, exact item/total reconciliation, workbook loadability,
  sheet/content checks, evidence links, unsupported-field absence, formula
  injection, deterministic semantic output, failure propagation, and
  architecture isolation. Regress C11 review and Core arithmetic without
  requiring AWS, S3, API, UI, or byte-identical workbook files.
- Advanced Verification Decision (reassess against actual C12 implementation;
  no new framework is prescribed):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Final numbers and approval eligibility must remain exact |
  | Contract tests | REQUIRED | Workbook and C11 input boundaries must validate |
  | Integration | REQUIRED | Reopen the produced workbook and exercise the C11-to-export path |
  | Generated property tests | CONDITIONAL / EVALUATE | Use if numeric/text combinations outgrow focused cases |
  | Targeted mutation-resistance | REQUIRED | Challenge approval bypass and reconciliation assertions |
  | Failure injection | REQUIRED | Invalid workbook and delegated validation failures must not export |
  | Fuzzing | CONDITIONAL / EVALUATE | Consider for broad untrusted spreadsheet text inputs |
  | Differential | NOT_APPLICABLE | No second equivalent exporter is specified |
  | Concurrency/race | CONDITIONAL / EVALUATE | Assess if shared state or file writes are introduced |
  | Adversarial testing | REQUIRED | Probe forged approval, stale evidence, formulas, and numeric drift |
  | Threat modeling | REQUIRED | Approval and spreadsheet output are consequential boundaries |
  | Agent evals | NOT_APPLICABLE | C12 does not own model quality or C17 evaluation |
  | Rollback/recovery | CONDITIONAL / EVALUATE | Assess if persistent files or external effects are introduced |
  | Formal methods | NOT_APPLICABLE | No exceptional formal-state requirement is specified |
- Independent Verifier Expectations: inspect the frozen candidate against
  the Roadmap gate, C11 held-approval use, Core reconciliation, safe text,
  supported evidence only, three-sheet loadability, and no C13+ or unused
  architecture permission; challenge tests that could pass on a copied
  approval record, invented field, or plausible but wrong workbook number.
- Evidence / Traceability Requirements: link observed C11 eligibility,
  current-result binding, Core totals, workbook cells/sheets, evidence IDs,
  synthetic-source disclosure, text safety, failure cases, and exact executed
  tests to the Evidence Map. Preserve decisions and limitations in the
  Learning Log. Until C12 is authorized and executed these remain NOT_RUN /
  NOT_PROVEN.
- Known Non-Scope: section 9 remains authoritative. Exact cell coordinates,
  styling, file path/bytes API, architecture category/import directions,
  approval-gate injection, and output persistence policy remain C12
  implementation decisions under least privilege. No tax/VAT/discount logic,
  new historical search, authentication, S3/API/UI, or generalized guardrail
  platform is added. Byte-identical `.xlsx` output is not required.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate requires a valid reconciled `.xlsx` workbook generated
only from current C11-approved state, with required supported content,
non-fabrication, safe text, and explicit failure. This section expands that
gate without adding a second approval or commercial authority.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C12

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C13 — FastAPI Application

### 1. Title

V1-C13 — FastAPI Application

### 2. Engineering Goal

Expose the quotation workflow through a typed FastAPI application without moving business ownership into transport.

### 3. Learning Goal

Typed API contracts, request validation, dependency boundaries, error mapping, and application orchestration exposure.

### 4. Why It Exists

A clear API delivery layer is needed to expose the workflow while preserving domain and application ownership.

### 5. Architecture Concept

Client / UI → FastAPI → Application Services → Domain / Agent / Engines.

### 6. Current System Before Card

C01–C12 may later provide the baseline, contracts, services, agent, review state, and Excel capability. No FastAPI workflow is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

FastAPI is transport only. API models must not become Core domain ownership.

### 8. Implementation Scope

- expose typed request and response contracts
- support quotation submission
- support draft generation and review state where applicable
- support approval/rejection where applicable
- support Excel retrieval/export where appropriate
- map failures explicitly
- keep business logic in application/domain services
- avoid secrets in responses

The Roadmap's six V1 routes are required transport surfaces. Its historical
`/approve` path carries an explicit APPROVED or REJECTED `ApprovalDecision`;
the path itself never selects approval. Analysis/draft may invoke existing
C10 capabilities, review delegates the caller's decision to C11, and export
returns validated C12 `.xlsx` bytes only after C12 checks the held C11
`ReviewSession` against the current `AgentResult`. Client-supplied status,
copied `ReviewRecord`, or model text cannot substitute for that authority.
The reviewer reference remains caller-asserted, not authenticated by C13.

A bounded process-local association may carry the current validated result
and held review session across requests in the supported single-process V1
runtime. It owns neither commercial truth nor approval. Repeated/concurrent
requests must preserve C11's one-decision, transition, and freshness rules
and C12's approval check. Restart loses this state; multi-process sharing,
durability, and persistent storage are not C13 guarantees. Exact registry,
locking, schema, status-code, response-header, and dependency-injection
choices remain implementation decisions.

### 9. Out of Scope

- S3 adapter implementation
- Lambda/API Gateway deployment
- CloudWatch-specific observability
- UI
- duplicated business logic in endpoints
- database, Redis, S3-backed or other persistent/distributed session storage
- authentication infrastructure, email, multi-agent expansion, new commercial arithmetic, or autonomous approval
- C17 evaluation or C18 generalized guardrail platform

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Request validation, invalid payloads, happy path, agent failure mapping, approval-required mapping, reject/approve behavior, transport/domain separation, and no endpoint business-logic duplication.

C09+ pre-implementation verification block (derived contract and plan, not
C13 implementation, authorization, or test evidence):

- Risk Classification: ELEVATED because this transport crosses AI failure,
  human approval, process-local state, and final Excel delivery boundaries;
  a bypass or leaked internal failure could expose consequential output.
- Escalation Triggers: client-forged approval or commercial state; stale or
  repeated review/export; concurrent decision bypass; C10 failure treated as
  success; malformed/oversized input; raw exception, secret, or provider-data
  leakage; C14+ infrastructure or business logic entering handlers.
- Canonical Sources: Roadmap V1-C13 and its Exit Gate, this Card's sections
  2–12, PROJECT_PROFILE.md, COMMERCIAL_AND_DATA_GUARDRAILS.md, delivered
  C10 `AgentRequest`/`AgentResult`, C11 `ApprovalDecision`/`ReviewSession`,
  C12 `export_approved_quote`, and domain models.
- Acceptance Contract: Given a valid request, when a required route executes,
  then typed input is validated and an existing owner supplies the result;
  analysis/draft cannot approve, explicit approve/reject goes through C11,
  and export succeeds only through C12's current-result approval gate. Given
  malformed input, unknown process-local quote/session, C10 INVALID,
  UNAVAILABLE, or INSUFFICIENT_EVIDENCE, C11 transition/freshness failure,
  C12 approval/reconciliation/export failure, or unexpected internal failure,
  the API returns a deterministic sanitized failure and no fabricated success.
  The six Roadmap routes remain distinct; no automatic draft-to-approval or
  approval-to-export chain is implied.
- Critical Invariants: HTTP data is untrusted until validated (G36); no AI,
  route name, copied record, or client status creates human approval (G16/G39);
  final export uses current approved validated state (G40); commercial values
  remain Core-owned and Excel reconciliation remains C12-owned (G15/G17);
  process-local state cannot bypass C11 freshness/one-decision checks;
  provider-specific data remains outside Core and sanitized at transport.
  Verify by route contracts, authority-bypass, failure, state, and
  architecture tests.
- Verification Strategy: test each required route, typed request/response
  and OpenAPI construction, invalid input, explicit approve/reject, C10/C11/C12
  failure mapping, missing/stale/repeated/concurrent session behavior,
  approval-gated workbook delivery, sanitized unexpected errors, and
  transport-only import/ownership boundaries. Test lightweight health
  without a live Bedrock call. Do not require C14+ infrastructure.
- Advanced Verification Decision (reassess against the authorized C13 design;
  this does not prescribe a framework):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Approval/export and response mapping must not vary by transport path |
  | Contract tests | REQUIRED | The six routes and typed HTTP boundaries must be exercised |
  | Integration | REQUIRED | Cross-request C10-to-C11-to-C12 flow must preserve held authority |
  | Generated property tests | CONDITIONAL / EVALUATE | Use if payload/state combinations outgrow focused cases |
  | Targeted mutation-resistance | REQUIRED | Challenge approval/export gate and failure-mapping tests |
  | Failure injection | REQUIRED | Delegated and unexpected errors must stay sanitized and fail closed |
  | Fuzzing | CONDITIONAL / EVALUATE | Consider for broad untrusted JSON surfaces |
  | Differential | NOT_APPLICABLE | No second equivalent API is specified |
  | Concurrency/race | REQUIRED | Same-process repeated/concurrent decisions must not bypass C11 |
  | Adversarial testing | REQUIRED | Probe forged status/records, stale state, and authority escalation |
  | Threat modeling | REQUIRED | HTTP exposure crosses consequential authority boundaries |
  | Agent evals | NOT_APPLICABLE | C10/C17 own model quality, not C13 transport |
  | Rollback/recovery | CONDITIONAL / EVALUATE | Assess process-local loss and any actual external effects |
  | Formal methods | NOT_APPLICABLE | No exceptional formal-state requirement is specified |
- Independent Verifier Expectations: inspect each route's real delegation,
  C11/C12 gate use, same-process state and concurrent behavior, sanitized
  failures, absence of copied-metadata authority, and least-privilege imports;
  challenge tests that pass despite skipped approval or duplicate business
  logic. No live AWS or C14+ proof substitutes for these checks.
- Evidence / Traceability Requirements: record actual route contracts,
  request/response and failure cases, C11 session identity/freshness,
  C12 workbook gate, concurrency checks, security probes, architecture
  results, executed commands, and limitations in the Evidence Map; record
  design rationale and any real failure/root-cause/fix in the Learning Log.
  Until C13 is separately authorized and executed, these are NOT_RUN /
  NOT_PROVEN.
- Known Non-Scope: section 9 remains authoritative. Exact HTTP schemas,
  status codes, MIME/Content-Disposition/filename, process-local registry
  and locking mechanism, sync/async routes, health body, CORS configuration,
  dependency set, and architecture permissions are C13 implementation
  decisions under least privilege. Health does not require a live Bedrock or
  AWS call. No database, Redis, persistence, authentication platform, S3,
  deployment, UI, or C18-wide guardrail platform is added.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require a typed FastAPI delivery layer that exposes the workflow without taking ownership of business logic.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C13

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C14 — Amazon S3 Integration

### 1. Title

V1-C14 — Amazon S3 Integration

### 2. Engineering Goal

Add provider-isolated S3 persistence and retrieval through a storage contract.
For the V1 quotation artifact flow, the primary persistable artifact is the
validated `.xlsx` bytes produced by C12's approved export boundary. C14 does
not accept arbitrary caller-supplied commercial content as an authoritative
quotation artifact. Any other justified stored data must use an existing
validated owner schema; C14 does not create new commercial or approval truth.

### 3. Learning Goal

Storage adapters, serialization boundaries, SDK isolation, validation after retrieval, and failure handling.

### 4. Why It Exists

Required artifacts and historical data need a controlled persistence boundary that remains compatible with local execution.

### 5. Architecture Concept

Core / Application → Storage Contract → S3 Adapter → Amazon S3.

The SDK remains isolated in the adapter; Core does not depend on the S3
adapter. REVIEW and EXPORT do not depend on the S3 adapter, and
APPLICATION_BOUNDARY does not automatically gain storage authority. Exact
module category (including whether to reuse PROVIDER or introduce STORAGE)
and allowed dependency directions are deferred to authorized C14
implementation and must follow actual imports and least privilege. This
maintenance grants no architecture permission or dependency direction; no
dependency-laundering path is allowed.

### 6. Current System Before Card

C01–C13 provide the existing contracts, services, API, and C12 validated
export output. No S3 persistence integration is implemented; C14 remains
NOT_STARTED and NOT_AUTHORIZED until separate human approval.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

S3 is an adapter, not commercial truth or approval authority. C12 owns
workbook generation and its approval/commercial validation; C14 persists and
retrieves the storage-ready C12 artifact with validated identity. Retrieved
bytes require storage-boundary identity/integrity validation. C14 does not
re-run C11 approval or C12 commercial/workbook business validation and does
not require or consume `ReviewSession`, `ReviewRecord`, or `AgentResult`.
Retrieval uses validated storage identity through the storage contract;
arbitrary S3 key text is not authority. C14 adds no public HTTP retrieval
endpoint or authentication system.

### 8. Implementation Scope

- define the storage contract and provider-isolated S3 adapter
- persist and retrieve C12 validated `.xlsx` artifact bytes with validated storage identity
- derive deterministic object keys from validated identity; do not accept arbitrary caller-controlled keys as storage authority or let path/prefix-like untrusted input control the final namespace
- choose and test explicit duplicate/idempotency behavior; never rely on implicit SDK overwrite behavior
- validate retrieved storage identity/integrity without duplicating C12 business validation
- retain only metadata necessary for identity, retrieval/integrity, and artifact classification; do not persist review sessions/records, reviewer details, provider payloads, or duplicated commercial-authority state
- expose missing-object, access/credential, service, malformed-response, duplicate, and integrity failures explicitly and sanitize provider errors
- keep boto3/botocore objects and exceptions outside Core/domain contracts
- preserve deterministic local testing and local-mode composition without network/AWS
- use standard AWS credential resolution and least privilege; C14 does not provision the bucket

The bucket and its region are supplied by runtime configuration. IAM grants
only permissions justified by the implemented persist/retrieve behavior
(PutObject/GetObject may be required); any additional permission must be
justified by actual use. `s3:*`, DeleteObject, bucket creation/deletion, and
public ACL changes are not C14 permissions. Encryption remains runtime or
deployment configuration; C14 does not impose KMS. Credentials follow the
existing C08 standard AWS provider chain and are never placed in source,
persisted, logged, or returned.

### 9. Out of Scope

- C11 approval checks or review-session handling
- C10 agent execution, C09 evidence discovery, or any AI reasoning
- commercial arithmetic, quotation state transitions, or Excel generation
- arbitrary client commercial payloads as authoritative storage artifacts
- C13 route changes or automatic API-triggered upload
- anonymous public retrieval endpoints, presigned URLs, public sharing/ACLs, or CloudFront
- bucket provisioning/deletion or object deletion
- deployment, Lambda, API Gateway, CloudWatch infrastructure, evaluation platform, or UI
- database, Redis, authentication, email, multi-agent workflow, or C18 generalized guardrail platform
- domain/commercial authority in storage code

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Deterministic local adapter contract for C12 artifact persistence/retrieval,
serialization/validation, identity/key derivation, duplicate behavior, missing
object, malformed/invalid retrieval, service/access failures, provider
isolation, credential secrecy, and no provider-object leakage. Tests must not
require network or real AWS; a live S3 test is optional supplementary
evidence. Do not require moto or other new test dependencies by default.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is authoritative and is expanded here only to clarify
the C12 artifact boundary, storage/retrieval integrity, explicit duplicate and
failure behavior, local deterministic verification, and provider isolation.

### C09+ Pre-Implementation Verification Block

This block records the implementation contract and verification plan only; it
does not authorize or start C14 and is not implementation evidence.

- Risk Classification: ELEVATED because persistence, identity derivation,
  retrieval integrity, and AWS credential boundaries can expose or confuse
  quotation artifacts if weakened; S3 object existence is not commercial or
  approval authority.
- Escalation Triggers: arbitrary caller-controlled keys; silent overwrite;
  artifact not produced by C12's validated export path; identity collision;
  unvalidated retrieval; credential or raw SDK exception leakage; public ACL
  or sharing; an unapproved AWS dependency/resource; C11/C10 authority being
  recreated in storage; or C15+ scope entering C14.
- Canonical Sources: Roadmap V1-C14 and its Exit Gate; this Card's sections
  2–12; PROJECT_PROFILE.md; COMMERCIAL_AND_DATA_GUARDRAILS.md §10; C12's
  `export_approved_quote` validated `.xlsx` output; C08's existing AWS
  credential/provider-isolation precedent; current architecture policy.
- Acceptance Contract: Given C12-validated workbook bytes and validated
  storage identity supplied through trusted application composition, persist
  and retrieve the artifact through the storage contract with deterministic
  identity, explicit duplicate/missing/failure behavior, and storage-boundary
  validation. Given malformed, missing, mismatched, duplicate, unavailable,
  or unauthorized storage conditions, fail explicitly and sanitize provider
  details. Local deterministic tests must prove the adapter without AWS.
- Critical Invariants: C12 remains the workbook/approval boundary; C14 does
  not re-create C11 approval or accept arbitrary caller commercial content;
  S3 is not commercial authority; keys derive deterministically from
  validated identity; no implicit overwrite; retrieved data is validated;
  boto3/botocore objects and credentials stay outside Core/domain state;
  CORE, REVIEW, and EXPORT do not depend on the S3 adapter;
  APPLICATION_BOUNDARY gets no automatic storage permission; no public
  ACL/presigned/public sharing; no bucket provisioning/deletion; no C13 or
  C15+ scope or dependency laundering.
- Verification Strategy: deterministic storage-contract tests for round-trip,
  key derivation, collisions/duplicates, missing objects, malformed and
  mismatched retrieval, explicit provider/access failure and sanitization;
  architecture/import boundary tests; credential/secret checks; local mode
  without network. Live S3 calls are optional and do not replace local tests.
- Advanced Verification Decision (reassess against the authorized C14 design;
  no specific testing framework or live AWS setup is prescribed):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Artifact identity, no implicit overwrite, validated retrieval, and no storage-derived commercial authority must hold |
  | Contract tests | REQUIRED | Storage inputs, outputs, missing objects, duplicates, and typed failures must follow the storage contract |
  | Integration | REQUIRED | Deterministic local tests must exercise the storage contract through the adapter boundary without AWS |
  | Generated property tests | CONDITIONAL / EVALUATE | Evaluate if validated identity/key combinations create a meaningful combinatorial space beyond focused cases |
  | Targeted mutation-resistance | REQUIRED | Challenge key derivation, duplicate/overwrite, integrity, and false-success checks at this ELEVATED trust boundary |
  | Failure injection | REQUIRED | Missing objects, access/credential failures, service errors, malformed responses, and integrity failures must fail explicitly and sanitized |
  | Fuzzing | CONDITIONAL / EVALUATE | Evaluate if implementation exposes broad parsers for untrusted identity, metadata, or retrieved storage content |
  | Differential | NOT_APPLICABLE | No second equivalent storage implementation or oracle is required |
  | Concurrency/race | CONDITIONAL / EVALUATE | Evaluate against the selected duplicate policy if concurrent writes could race or weaken no-overwrite behavior |
  | Adversarial testing | REQUIRED | Probe arbitrary-key control, artifact substitution, namespace collision, overwrite, public-access, and forged-success attempts |
  | Threat modeling | REQUIRED | ELEVATED persistence crosses artifact, namespace, credential, provider-error, public-access, and integrity trust boundaries |
  | Agent evals | NOT_APPLICABLE | C14 owns storage behavior, not agent/model quality or C17 evaluation |
  | Rollback/recovery | CONDITIONAL / EVALUATE | Evaluate retry/recovery behavior for partial or ambiguous provider outcomes; object deletion and bucket rollback remain out of scope |
  | Formal methods | NOT_APPLICABLE | No exceptional formal-state requirement is specified; explicit contracts and deterministic tests are required instead |

  Real AWS/S3, bucket provisioning, and live S3 tests remain NOT_REQUIRED for
  implementation, independent audit, and the Exit Gate. A live S3 check may
  provide optional supplementary evidence only.
- Independent Verifier Expectations: verify that the artifact originates
  from the C12 validated export composition boundary; challenge caller key,
  artifact substitution, overwrite, malformed retrieval, and failure
  sanitization; inspect dependency direction and ensure S3 state cannot grant
  approval or commercial authority; distinguish local tests from optional
  live AWS evidence.
- Evidence / Traceability: record exact candidate identity, C12 input/output
  boundary, chosen identity/key and duplicate policies, tests and failures,
  architecture and security evidence, limitations, and any optional live S3
  observation. Never claim AWS behavior not actually tested. Record bucket
  provisioning and IAM/runtime configuration only as external assumptions;
  never record credentials or secrets.
- Known Non-Scope: bucket provisioning/deletion, object deletion, public ACLs,
  presigned URLs, CloudFront, C13 route or automatic-upload changes, C15
  deployment, C16 observability, database/Redis, authentication, UI, email,
  multi-agent work, new commercial calculations, approval logic, Excel
  generation, C17 evaluation, and C18 generalized guardrails.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C14

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C15 — AWS Deployment

### 1. Title

V1-C15 — AWS Deployment

### 2. Engineering Goal

Deploy the approved API architecture using API Gateway → AWS Lambda → FastAPI.

### 3. Learning Goal

Serverless deployment, configuration boundaries, least-privilege IAM, local/cloud parity, and evidence-based deployment verification.

### 4. Why It Exists

A bounded AWS deployment demonstrates cloud readiness while keeping the local system usable and the architecture simple.

### 5. Architecture Concept

User → API Gateway → Lambda → FastAPI → existing application services.

### 6. Current System Before Card

C01–C14 may later provide the application, API, storage, and provider integrations. No AWS deployment is implemented or evidenced; repository state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Use the approved serverless direction and keep deployment concerns outside Core. Do not add larger infrastructure without explicit approval.

### 8. Implementation Scope

- define deployment configuration for API Gateway, Lambda, and FastAPI
- externalize configuration
- apply least-privilege IAM
- preserve adapter boundaries
- preserve local execution
- validate startup/import compatibility
- establish repeatable deployment procedure appropriate to project scale
- record deployment evidence only when actually verified

### 9. Out of Scope

- CloudWatch-specific observability owned by C16
- evaluation harness owned by C17
- UI
- unnecessary infrastructure
- unapproved platform expansion

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Deployment configuration validation, startup/import compatibility, basic deployed health/integration where actually deployed, explicit failure reporting, IAM/configuration review, no secrets, and local-mode verification.

Test not run != PASS. Design intent != implementation evidence.

### 11A. Pre-Implementation Verification (C09+)

- Risk Classification: ELEVATED — deployment crosses public-cloud exposure,
  IAM and credential boundaries, Lambda process lifetime/scaling, binary
  API response handling, configuration, deployment drift, and potentially
  billable live-resource creation. A false live-deployment claim would also
  invalidate the Card's central evidence.
- Escalation Triggers: unexpected public exposure; static credential or
  secret leakage; unjustified wildcard/overprivileged IAM; any claim that
  Lambda makes C13 process-local review state durable; undocumented
  Console-only deployment state; binary workbook corruption; unapproved
  resource creation; or evidence that claims live AWS proof from local
  emulation.
- Canonical Sources: this C15 specification and its Roadmap Exit Gate;
  delivered C13 API and its process-local state contract; delivered C14
  storage boundary; PROJECT_PROFILE.md; COMMERCIAL_AND_DATA_GUARDRAILS.md;
  QUOTATION_ENGINEERING_HARNESS.md; and PROJECT_CONTROL.md for live state
  and authorization.
- Acceptance Contract: Given the delivered C13 application and a
  repository-controlled, externalized deployment configuration, when C15
  validates locally and deploys with separate deployer/runtime identities,
  then API Gateway → Lambda → FastAPI starts and serves the unchanged C13
  routes, preserves the existing binary `.xlsx` export response through the
  selected adapter, and a real HTTPS API Gateway `GET /health` returns the
  expected C13 response. Local execution remains functional. Failures are
  explicit and sanitized; live proof is not claimed from simulation.
  Completion additionally requires the Roadmap Exit Gate's real AWS
  evidence and approved live-resource action. No deployment behavior may
  imply durable C13 state, production readiness, or new C13 authority.
- Critical Invariants: C13's six routes and contracts remain unchanged;
  C11/C12 authority is not bypassed; process-local state may be lost or
  isolated across Lambda environments; no persistence is added; credentials
  are not static or embedded; deployer and runtime identities are distinct;
  runtime IAM is least privilege and justified by composed features; config
  is external; deployment is repeatable from repository-controlled
  procedure; binary XLSX semantics are preserved; no unrestricted CORS or
  anonymous production claim; local mode remains usable; local/simulated
  proof remains distinct from live AWS evidence.
- Verification Strategy: validate deployment manifests/procedure and
  external configuration locally; import/build the Lambda entrypoint;
  simulate API Gateway events through the adapter, including `/health` and
  binary XLSX behavior; regress all six C13 routes and existing authority
  boundaries; inspect IAM/configuration, package contents, credentials,
  error exposure, CORS, and reproducibility; preserve local execution.
  Separately record a real Lambda/API Gateway deployment and HTTPS `/health`
  response before the final Exit Gate. No live Bedrock or S3 call is needed.
- Advanced Verification Decision (reassess against the authorized C15
  design; live AWS remains required only for final Exit Gate deployment
  evidence, not for implementation tests or initial independent code audit):

  | Technique | Decision | Reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | C13 route/authority invariants, credential separation, local-mode behavior, and the process-local-state limitation must remain explicit and stable |
  | Contract tests | REQUIRED | Lambda/API Gateway adapter behavior must preserve the delivered HTTP contracts, including health and binary XLSX response semantics |
  | Integration | REQUIRED | Locally simulated API Gateway events must traverse the selected adapter into FastAPI; final live AWS integration is separately required by the Exit Gate |
  | Generated property tests | CONDITIONAL / EVALUATE | Evaluate if deployment-event or configuration shapes have a meaningful combinatorial space beyond representative contract cases |
  | Targeted mutation-resistance | REQUIRED | Challenge route preservation, credential/config checks, binary response encoding, and safeguards against false live-deployment evidence |
  | Failure injection | REQUIRED | Exercise import/startup, configuration, adapter, and deployment-response failures and prove explicit sanitized failure rather than false success |
  | Fuzzing | CONDITIONAL / EVALUATE | Evaluate if the chosen adapter/configuration parser exposes broad untrusted event or manifest parsing surfaces |
  | Differential | NOT_APPLICABLE | No second equivalent deployment adapter/runtime is required as an oracle |
  | Concurrency/race | CONDITIONAL / EVALUATE | Evaluate deployment-specific parallel invocation effects, while explicitly not treating concurrency settings as durable/shared C13 state |
  | Adversarial testing | REQUIRED | Probe public exposure, overprivileged identity, static-secret packaging, response transformation, permissive CORS, and state-loss claims |
  | Threat Modeling | REQUIRED | ELEVATED deployment crosses cloud exposure, IAM, credentials, package/configuration, API response, process-local state, drift, and evidence-truth boundaries |
  | Agent evals | NOT_APPLICABLE | C15 owns deployment and transport integration, not model quality or C17 evaluation |
  | Rollback/recovery | REQUIRED | A repeatable bounded redeployment of the prior known-good artifact/configuration is required after failed deployment |
  | Formal methods | NOT_APPLICABLE | No exceptional formal proof requirement is specified; explicit contracts, local simulation, security review, and live reachability evidence are required |

- Independent Verifier Expectations: inspect exact deployment files and
  permissions; independently simulate the API Gateway/Lambda adapter path,
  `/health`, and binary XLSX handling; confirm local mode and all C13 routes
  remain unchanged; challenge static-credential leakage, runtime IAM scope,
  public exposure/CORS, deployment reproducibility, rollback, process-local
  state claims, and the distinction between simulated and live evidence.
  Before completion, verify actual Lambda/API Gateway identifiers and a
  real HTTPS `/health` response; do not treat local emulation as live proof.
- Evidence / Traceability: distinguish local tests, simulated adapter
  evidence, independent configuration review, and live AWS observations.
  Live evidence records region, stable Lambda/API Gateway identifiers,
  HTTPS status and expected body, timestamp, no-static-credential
  confirmation, and local-mode regression, without recording secrets.
  Record resource/cost and teardown decisions only after separate human
  approval. External adapter/deployment references follow
  SOURCE_ADAPTATION_TRACEABILITY.md; reference-only study is not runtime
  evidence.
- Known Non-Scope: C13 route/schema/authority changes; C14 automatic
  composition or S3 upload; Bedrock invocation; durable ReviewSession or
  other database/DynamoDB/Redis state; sticky sessions or distributed
  correctness; production HA; authentication platforms; unrestricted public
  production API; UI, email, multi-agent work, commercial logic, approval or
  Excel changes; C16 observability platform; C17 evaluation; C18 generalized
  guardrails; C20 frontend; ECS/EKS/Kubernetes; custom domain/Route53/ACM;
  CloudFront; and deployment tools/adapters not yet selected.

### 12. Exit Gate

The Roadmap Exit Gate is authoritative and must be proven exactly. Its
real-AWS deployment requirement, live `/health` evidence, accepted
process-local-state limitation, access boundary, and C13/C14 authority
protections must not be weakened by implementation convenience.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C15

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C16 — CloudWatch Observability

### 1. Title

V1-C16 — CloudWatch Observability

### 2. Engineering Goal

Add bounded structured operational logs for the quotation workflow with useful
correlation and failure/latency visibility, without moving business authority
into logging or building an observability platform.

### 3. Learning Goal

Structured logs, correlation identifiers, agent/tool operation visibility,
CloudWatch Logs, failure diagnosis, and sensitive-data redaction.

### 4. Why It Exists

Operators need to trace workflow failures and latency while preserving confidentiality and keeping observability separate from business logic.

### 5. Architecture Concept

Request → application workflow → structured operational events → local logging
and CloudWatch Logs where deployed.

### 6. Current System Before Card

C01–C15 may later provide the application, integrations, and deployment. Observability is not implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Use bounded, machine-parseable correlated events with local logging support;
never fabricate unavailable model metadata or place business decisions in
logging.

### 8. Implementation Scope

- capture `request_id` and `quotation_id` where appropriate for operational
  correlation
- capture API latency, errors, and final request status
- capture agent-run, tool-call/failure, and Bedrock-call outcome/latency
  visibility; record token usage only when available
- capture S3 operation outcome only where C14 is actually used
- support local structured logging and CloudWatch Logs where deployed
- sanitize provider errors and exclude secrets and sensitive payload content
- keep logging observational; do not change commercial, approval, provider,
  storage, route, or schema semantics
- instrumentation may be placed in existing API, agent, tool, Bedrock,
  storage, or support logging paths when justified; `lambda_handler.py` is not
  required by default and may change only if evidence shows it is necessary
  for correlation/context propagation

### 9. Out of Scope

- custom CloudWatch metrics or EMF
- CloudWatch alarms or dashboards
- X-Ray or distributed tracing
- third-party observability or enterprise monitoring platforms
- production SRE program
- evaluation harness (C17)
- business workflow redesign
- durable state, authentication, UI, C18+, or C20+

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Structured event shape; request/quotation correlation; API latency/final
status; agent/tool/Bedrock outcomes and latency; available token usage; S3
visibility only when used; sanitized failure logging; prohibited-field
absence; local logging without AWS; and preserved architecture boundaries.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is authoritative. C16 local implementation and initial
independent local audit do not require live AWS. The final Exit Gate requires
separately approved live proof that a representative structured event from
the retained C15 Lambda `aqi-c15-api` reaches the retained log group
`/aws/lambda/aqi-c15-api`, includes correlation, and excludes prohibited
sensitive fields. C16 must not create a parallel deployment. Any AWS
modification requires separate explicit human approval.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.

### 11A. Pre-Implementation Verification (C09+)

- **Risk Classification: ELEVATED.** Logging touches provider failures,
  operational identifiers, commercial-adjacent workflow data, and a live
  cloud runtime boundary. Confidentiality failures and false observability
  claims are material.
- **Escalation Triggers:** raw prompts, model responses, provider exceptions,
  secrets, credentials, reviewer identifiers, workbook/user/commercial data
  enter logs; correlation context crosses requests; logging changes behavior
  or authority; unexpected IAM/resource changes are proposed; unbounded event
  volume or cost appears; local simulation is represented as live proof.
- **Canonical Sources:** C16 Roadmap contract and Exit Gate; this specification;
  delivered C13 API/error contract; C10 agent, C09 tools, C08 Bedrock adapter,
  C14 storage boundary, and C15 Lambda/log-group deployment; Commercial and
  Data Guardrails; Engineering Harness; PROJECT_CONTROL for authorization and
  live state.
- **Acceptance Contract:** Given delivered C13/C15 and existing workflow
  boundaries, when C16 instrumentation is exercised locally and, after
  separate AWS approval, in the retained deployed Lambda, then bounded
  structured events expose applicable correlation, operation, outcome,
  latency, and available token usage while excluding prohibited sensitive
  data. Local mode remains usable without AWS. A representative real event
  must reach the retained C15 log group for the final Exit Gate. Logging
  changes no route, response, commercial, approval, provider, or storage
  behavior and does not claim durable workflow state.
- **Critical Invariants:** `request_id` is per request and context does not
  leak between requests; `quotation_id` is only an operational correlation
  identifier; no credentials/secrets, raw provider error, prompt/model output,
  workbook bytes/content, reviewer_id, free-form user content, arbitrary
  bodies, or unnecessary sensitive commercial values are logged. Provider
  failures such as `BedrockResult.message=str(exc)` are sanitized before log
  emission. Logging owns no business or decision authority. No Core arithmetic
  changes. C16 does not add runtime IAM or AWS resources for logging-only
  behavior. Local logging works without AWS.
- **Verification Strategy:** locally verify event schema/field bounds,
  correlation propagation and isolation, API latency/final status, agent/tool
  event visibility, Bedrock outcome/latency and token usage when available,
  S3 outcomes only when C14 is used, sanitized failures, redaction under
  adversarial inputs, no new dependencies without justification, and
  architecture boundaries. Exercise failure paths and rollback by disabling
  or reverting instrumentation/deployment revision. Separately, after
  approval, inspect a representative event in the retained CloudWatch log
  group and verify its correlation and prohibited-field absence. Do not treat
  local simulation as live evidence.
- **Advanced Verification Decision:** reassess against the authorized C16
  implementation; local proof is sufficient for implementation/audit, while
  a bounded live log event is required only for the final Exit Gate.

  | Technique | Decision | C16-specific reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Exact allowed event fields, bounded values, correlation scope, and forbidden data must be stable and testable. |
  | Contract tests | REQUIRED | Logging event structure and component event names/status/latency fields must satisfy the defined operational contract. |
  | Integration | REQUIRED | Injected local events must reach the local logging sink; final live proof separately confirms a C15 Lambda event reaches the retained CloudWatch log group. |
  | Generated property tests | CONDITIONAL / EVALUATE | Evaluate generated strings/identifiers and context combinations if bounded event serialization has a meaningful input space. |
  | Targeted mutation-resistance | REQUIRED | Prove tests fail if redaction, context clearing, provider-error sanitization, or event-field bounds are removed. |
  | Failure injection | REQUIRED | Inject provider/tool/API/storage failures and verify sanitized outcome events without changing returned failure semantics. |
  | Fuzzing | CONDITIONAL / EVALUATE | Evaluate only if log serialization or redaction processes broad untrusted text; otherwise bounded adversarial cases suffice. |
  | Differential | NOT_APPLICABLE | Two logging backends are not an oracle pair; local and CloudWatch sinks need contract compatibility, not comparative output equivalence. |
  | Concurrency/race | CONDITIONAL / EVALUATE | Evaluate concurrent requests for request/quotation context leakage or cross-request correlation contamination. |
  | Adversarial testing | REQUIRED | Attempt to inject prompts, raw provider errors, secrets, reviewer IDs, workbook/user content, and oversized values into events. |
  | Threat Modeling | REQUIRED | ELEVATED risk spans confidentiality, operational correlation, provider failures, log ingestion cost, live cloud boundaries, and false-observability claims. |
  | Agent evals | NOT_APPLICABLE | C16 owns operational event visibility, not model behavior or C17 evaluation. |
  | Rollback/recovery | REQUIRED | Demonstrate a bounded way to disable/revert instrumentation and restore the preceding known-good application/deployment revision if logging breaks behavior or leaks data. |
  | Formal methods | NOT_APPLICABLE | Typed/event contract tests, redaction probes, isolation tests, and live log inspection provide proportionate evidence; no formal proof is specified. |

- **Independent Verifier Expectations:** independently inspect exact event
  fields and all touched application/provider/tool/storage boundaries; test
  correlation isolation, sanitization, failure visibility, local operation,
  and architecture rules; challenge false event claims and prohibited-data
  leakage. For final Exit Gate, independently inspect an actual event in the
  retained log group and distinguish that live evidence from local tests.
- **Evidence / Traceability:** record actual local event/test evidence and
  actual live event evidence separately. Live evidence identifies the retained
  Lambda/log group, event/time and correlation presence, confirms prohibited
  fields absent, and avoids recording log payloads that contain sensitive
  data. Record no secret values. Cite real implementation decisions and
  failures in the Learning Log after they occur.
- **Known Non-Scope:** C17 evaluation; custom CloudWatch metrics; EMF; alarms;
  dashboards; X-Ray/distributed tracing; third-party or enterprise
  observability; production SRE; workflow redesign; commercial arithmetic;
  approval changes; durable state; authentication; UI; C18+ and C20+.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C16

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C17 — Evaluation Harness

### 1. Title

V1-C17 — Evaluation Harness

### 2. Engineering Goal

Build a repeatable evaluation harness that measures quotation-intelligence quality and correctness.

### 3. Learning Goal

Evaluation-first engineering for deterministic logic, retrieval, evidence, agent behavior, structured output, Excel correctness, latency, and Bedrock usage.

### 4. Why It Exists

A professional system needs measurable quality rather than reliance on a visually convincing demonstration.

### 5. Architecture Concept

Fixed synthetic Golden Dataset → offline harness → deterministic contract graders → machine-readable metric report.

### 6. Current System Before Card

C01–C16 may later provide the workflow and observability. No evaluation harness is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Evaluate defined system contracts on a fixed synthetic dataset with independent deterministic oracles. V1 does not use LLM-as-judge or claim open-ended model quality; latency, Bedrock usage, and cost are report-only where measurable.

### 8. Implementation Scope

- run repeatable evaluation cases
- measure calculation correctness
- measure historical comparison correctness
- measure similar-quotation quality
- measure RiskEvidence and provenance correctness
- measure unsupported-risk rate
- validate structured output and tool-call success
- measure agent completion, Excel correctness, latency, and Bedrock usage/cost where measurable
- report PASS/FAIL/ERROR, metric results, case outcomes, dataset identity, and evidence provenance
- run offline without AWS, live Bedrock, secrets, network, or production-runtime changes

### 9. Out of Scope

- Golden Case final end-to-end demonstration
- UI
- new model architecture
- production monitoring system
- LLM-as-judge or subjective model-quality grading
- live Bedrock/AWS evaluation, production deployment changes, and CI integration
- generalized security evaluation or production-release policy

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

The offline harness runs the fixed synthetic Golden Dataset deterministically,
distinguishes PASS/FAIL/ERROR, reports metrics and per-case evidence, and
detects contract-invalid outputs. It requires no network, AWS, live Bedrock,
secrets, or CI service.

Test not run != PASS. Design intent != implementation evidence.

### 11A. Pre-Implementation Verification (C09+)

- **Risk Classification: ELEVATED.** The harness is offline, but circular
  oracles, fixture/denominator/threshold manipulation, synthetic-data misuse,
  stochastic grading, report leakage, and false PASS claims could materially
  misrepresent system quality or commercial correctness.
- **Escalation Triggers:** expected values produced by the code under test;
  confidential/real customer data; unversioned or hash-mismatched fixtures;
  silently skipped cases or mutable denominators/thresholds; an LLM judge or
  stochastic provider acting as PASS authority; report payload/secret leakage;
  an evaluation dependency from production runtime; a real-world correctness
  or production-readiness claim; AWS/network requirements; or unapproved
  dependency/architecture expansion.
- **Canonical Sources:** C17 Roadmap contract and Exit Gate; this
  specification; delivered Core calculation and historical contracts, C06
  retrieval, C07 risk/evidence, C08 provider contract, C09/C10 tool/agent
  contracts, C11 review boundary, C12 export contracts, C13 API, C14 storage,
  and C15/C16 deployment/observability boundaries; Commercial and Data
  Guardrails; Engineering Harness; PROJECT_CONTROL for live state and
  authorization.
- **Acceptance Contract:** Given the existing delivered contracts and a fixed
  synthetic-only Golden Dataset with independently authored expected results,
  when the dedicated offline harness runs with deterministic provider traces,
  then it emits reproducible, thresholded contract metrics and an authoritative
  machine-readable report bound to the dataset version/hash. No model judge,
  live Bedrock, AWS, network, secret, production-runtime modification, or
  confidential data is needed. Passing means only that defined deterministic
  contracts passed on that fixed synthetic dataset.
- **Critical Invariants:** the dataset has stable `case_id`, version, and
  deterministic content identity/SHA-256; expected results are independently
  authored and never self-oracled. Required metrics and denominators are
  determined by the fixed dataset/applicability, not silently reduced by
  skipped cases. Calculation, historical comparison, Hit@3, evidence and
  provenance, structured output, tool protocol, scripted-agent completion,
  and Excel thresholds are exact as in the Roadmap. Unsupported-risk rate is
  zero; required-but-absent risk evidence separately fails completeness.
  Latency/usage/cost are report-only. Reports exclude secrets, real prompts or
  responses, `reviewer_id`, workbook bytes, arbitrary bodies, and confidential
  data. Evaluation is not business authority and production code never
  depends on it.
- **Verification Strategy:** validate dataset schema, stable serialization,
  expected-value independence and hash/version; exercise each formula and
  threshold with passing and deliberately failing deterministic fixtures;
  verify required evidence/provenance, tool and agent protocol, typed output,
  and C12 deterministic workbook invariants; test overall PASS/FAIL/ERROR,
  case/metric reporting, privacy, and reproducible reruns. Challenge denominator
  reduction, skipped cases, threshold/config tampering, and invalid dataset
  integrity. Run offline/headless without network/AWS. Do not rerun stochastic
  trials or call live Bedrock.
- **Advanced Verification Decision:**

  | Technique | Decision | C17-specific reason |
  | --- | --- | --- |
  | Deterministic invariants | REQUIRED | Fixed expected values, formulas, dataset identity, thresholds, and status transitions must be exact and reproducible. |
  | Contract tests | REQUIRED | Dataset, metric, typed-output, tool protocol, evidence linkage, and machine-report fields have explicit contracts. |
  | Integration | REQUIRED | The offline runner must consume fixed cases across the applicable calculation/retrieval/risk/agent/export contracts and emit one coherent report without entering production runtime. |
  | Generated property tests | CONDITIONAL / EVALUATE | Use only if metric/dataset structures have meaningful generated invariants beyond the fixed Golden Dataset; generated results must not replace independent expected values. |
  | Targeted mutation-resistance | REQUIRED | Show tests reject altered expected values, formula/threshold/denominator changes, case skipping, hash/version mismatch, and weakened report/status rules. |
  | Failure injection | REQUIRED | Inject malformed datasets, hash/version mismatch, unknown metric, invalid cases, grader failures, and non-deterministic output; integrity failures must produce ERROR, not false PASS. |
  | Fuzzing | CONDITIONAL / EVALUATE | Evaluate if dataset/report parsers accept broad untrusted input; fixed schemas may be adequately challenged with bounded adversarial malformed cases. |
  | Differential | CONDITIONAL / EVALUATE | Use only where a genuinely independent oracle exists, such as separately authored exact expected values; do not compare the implementation to its own calculation or invent a second implementation as an oracle. |
  | Concurrency/race | NOT_APPLICABLE | Baseline V1 harness is sequential and offline; reassess only if implementation introduces parallel execution or shared mutable state. |
  | Adversarial testing | REQUIRED | Challenge circular oracles, fixture tampering, denominator/threshold manipulation, silent skips, synthetic-data misrepresentation, report leakage, and false PASS claims, without duplicating all prior security suites. |
  | Threat Modeling | REQUIRED | ELEVATED risks include quality misrepresentation, provenance loss, privacy leakage, dataset drift, and non-deterministic judge authority. |
  | Agent evals | REQUIRED | C17 explicitly grades fixed scripted-agent protocol/task cases; this is deterministic contract evaluation, not open-ended model-quality judgment. |
  | Rollback/recovery | REQUIRED | Preserve a prior known-good harness/dataset version and define bounded revert/restore of evaluation code and fixtures after a bad harness update. |
  | Formal methods | NOT_APPLICABLE | Exact fixture oracles, invariant/contract tests, mutation checks, and deterministic reports are proportionate; no formal proof is specified. |

- **Independent Verifier Expectations:** independently verify the fixed
  dataset/hash and expected-value provenance; recompute metric numerators,
  denominators, thresholds, and overall status from per-case results; probe
  case skipping and circular-oracle mutations; verify report redaction,
  deterministic reruns, and architecture isolation; confirm FAIL/ERROR blocks
  completion and no live AWS or LLM judge was used. Reject claims beyond the
  fixed synthetic contracts.
- **Evidence / Traceability:** preserve dataset version/hash, exact commands,
  report schema/results, per-case evidence references, failures and recovery,
  reproducibility result, dependency/architecture review, and privacy checks.
  Clearly distinguish gating PASS/FAIL metrics from report-only observations.
  No credentials, prohibited payloads, or confidential data are recorded.
- **Known Non-Scope:** live Bedrock/AWS; LLM-as-judge; stochastic model trials
  and statistical policy; CI service integration; C19 Golden Case; general
  security-evaluation platform; C11 review-quality grading (existing C11
  approval/rejection regression remains authoritative);
  subjective reviewer-quality evaluation;
  real-market/commercial correctness, profitability, or production-readiness
  claims; production-runtime dependency; dashboards/observability; C18+ and
  C20+ scope.

### 12. Exit Gate

The Roadmap Exit Gate is authoritative. C17 is deterministic-first and
synthetic-only; live Bedrock, AWS, network access, and production-runtime
changes are not required. Report-only latency/usage/cost cannot gate PASS.
Failure or invalid evaluation integrity blocks the C17 Exit Gate as defined
in the Roadmap.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C17

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C18 — Guardrails and Failure Handling

### 1. Title

V1-C18 — Guardrails and Failure Handling

### 2. Engineering Goal

Implement and prove enforcement of project-wide commercial, data, AI, security, and workflow failure boundaries.

### 3. Learning Goal

Fail-closed engineering, explicit error states, degraded-path behavior, model-output rejection, and commercial safety.

### 4. Why It Exists

Invalid inputs, provider failures, unsupported claims, and missing approval must remain visible rather than becoming silent success.

### 5. Architecture Concept

Input / Tool / Provider / Storage / AI Output → validation boundary → explicit state → continue or fail closed.

### 6. Current System Before Card

C01–C17 provide the existing system and evidence context. C18-wide enforcement
has not yet been audited; do not assume either absence or sufficiency of an
individual control before inspection. C18 implementation remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Align enforcement with COMMERCIAL_AND_DATA_GUARDRAILS.md and reject invalid state explicitly; do not fabricate fallback quotations.

### 8. Implementation Scope

- VERIFICATION-FIRST and HARDENING-ONLY: map and inspect enforcement for every
  canonical failure state in `COMMERCIAL_AND_DATA_GUARDRAILS.md` §8 before
  proposing implementation changes.
- Prove ALL 15 canonical states:
  `MISSING_RATE`, `MISSING_REQUIRED_HOURS`, `INVALID_COMMERCIAL_VALUE`,
  `CURRENCY_MISMATCH`, `COMMERCIAL_SEMANTICS_UNVERIFIED`,
  `DETERMINISTIC_CONFLICT`, `INSUFFICIENT_EVIDENCE`, `AI_UNSUPPORTED_CLAIM`,
  `AI_INVALID`, `AI_UNAVAILABLE`, `AI_BOUNDARY_VIOLATION`,
  `COMMERCIAL_INVARIANT_FAILED`, `EXCEL_RECONCILIATION_FAILED`,
  `APPROVAL_REQUIRED`, and `SECURITY_BOUNDARY_VIOLATION`.
- For each state, record trigger, owner, expected fail-closed result, current
  implementation path, existing test/evidence, sufficiency classification,
  new C18 action, and final verification result in the C18 evidence matrix.
- Classify evidence as `EXISTING_EVIDENCE_SUFFICIENT`,
  `EXISTING_EVIDENCE_PARTIAL`, `NEW_C18_TEST_REQUIRED`, or
  `ENFORCEMENT_GAP_REQUIRES_FIX`. Reuse existing C04–C17 evidence only when it
  directly and sufficiently proves the exact invariant. Never add a duplicate
  test just to label it C18. Partial/missing evidence gets bounded deterministic
  tests; production changes require a proven gap and the smallest justified
  fix plus regression test.
- Preserve valid deterministic state only when explicitly marked partial;
  invalid AI/provider output cannot become authoritative; missing evidence,
  provider/storage/tool/export failure, unauthorized transitions, or rejection
  cannot become silent success or fabricated fallback.
- Reuse C16 structured logging only for affected paths that already use it;
  retain bounded sanitization and correlation. Do not create a new
  observability subsystem.

### 9. Out of Scope

- redesign of Guardrails policy
- UI
- unrelated resilience infrastructure

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Each applicable failure path, explicit error/state, no silent success, deterministic truth, approval boundary, unsupported-claim rejection, and malformed provider/storage output.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap C18 Exit Gate is authoritative and requires every one of the 15
canonical §8 states to have sufficient enforcement evidence and a final PASS.
Sample coverage is insufficient. Evidence reuse is allowed only when direct
and sufficient. A partial or missing row blocks completion until a bounded
test proves it; a proven gap requires the minimal fix and regression proof.

The Exit Gate also requires explicit proof that commercial input failures,
historical/evidence failure, invalid or unavailable AI/provider behavior, tool
failure, approval/unauthorized operations, Excel/export failure, and S3/storage
failure remain fail-closed; no fallback quotation is fabricated, no invalid
AI output is promoted, no partial state is presented as complete, and no
failure is masked as success. Failure information is bounded and sanitized.
Existing C16 observability may be reused where already present; no new
observability resources are required.

Bedrock Guardrails product integration is declined/deferred for V1 C18. No
live AWS or Bedrock proof, AWS preparation, new persistence, new dependency,
or C17 dataset/report/evaluation change is required. C18 does not redesign
guardrail policy or commercial, arithmetic, evidence, approval, or export
authority. C18 alone does not establish production readiness. Any bounded
implementation fix is Git-reversible and introduces no migration or cloud
rollback requirement.

### C09+ Pre-Implementation Verification Block

#### Risk Classification

**ELEVATED.** C18 spans commercial invariants, AI-output rejection, evidence
integrity, approval boundaries, provider/storage/tool failures, and
security-sensitive fail-closed behavior. Incorrect enforcement can create
silent false-success or misleading commercial state. It is not CRITICAL because
the approved scope adds no new commercial authority, persistence, or cloud
infrastructure by default; it verifies and hardens existing authority.

#### Escalation Triggers

Stop for human direction if a material policy contradiction is discovered, an
existing authority boundary must change, a fix requires new persistence/cloud
resources, live AWS/Bedrock or Bedrock Guardrails appears necessary, a new
dependency is claimed necessary, or an enforcement gap cannot be fixed without
changing prior-Card authority. Do not turn a missing or partial proof into
PASS.

#### Canonical Sources

- `COMMERCIAL_AND_DATA_GUARDRAILS.md` §8: exact 15-state taxonomy and policy.
- C18 Roadmap Exit Gate: all-state acceptance contract and approved scope.
- C04–C17 Specifications, Evidence Map, and tests: implementation contracts
  and potentially reusable direct evidence.
- C16 observability contract: existing bounded logging behavior where present.
- C11/C12/C13/C14 contracts: approval, export, API, and storage boundaries.

#### Acceptance Contract

Use the all-15 evidence matrix. Every row must identify canonical state,
trigger, owner, expected result, existing implementation path and evidence,
sufficiency classification, action, actual result, and final PASS/FAIL. Existing
evidence is reused only when it directly proves the exact invariant. The full
matrix, not a sample, must pass before C18 can pass its Exit Gate.

#### Critical Invariants

- Deterministic Core owns commercial arithmetic; the LLM never owns or silently
  overrides authoritative commercial arithmetic or deterministic evidence.
- Invalid commercial input fails before authoritative quotation state.
- Evidence/provenance, human approval, and export authority remain with their
  existing owners.
- Invalid AI output cannot become authoritative state; failures do not create
  fabricated fallback quotations or false success.
- Partial state remains explicitly partial; unavailable/rejected/failed states
  remain explicit and bounded.
- No policy redesign, new persistence authority, or live cloud dependency.

#### Failure-Handling Contract

Every covered state terminates as an explicit typed failure, bounded error,
rejected transition, unavailable result, or explicitly partial state according
to its existing owner. Never report silent success, fabricate a fallback
quotation/evidence/object identity, mask a provider/storage/tool/export failure,
promote invalid AI output, bypass approval, or relabel partial state complete.
Do not invent retries or recovery behavior.

For commercial input and deterministic conflicts, fail before invalid input
becomes authoritative quotation state. For historical no-match, malformed data,
or insufficient evidence, follow the owning canonical contract with an
explicit empty/no-match/insufficient-evidence result; never fabricate a match.
Provider invalidity/unavailability remains explicit and preserves only valid
deterministic state. Tool failures remain bounded and cannot create evidence or
unsupported actions. Approval and unauthorized transitions remain owned by
C11/current workflow contracts. Excel failure cannot report a successful
artifact or bypass reconciliation. S3 failure cannot report stored success or
fabricate object identity and must retain sanitized failure information. An
existing C13 API boundary surfaces bounded failures under its current contract;
change no route/status/schema absent a proven gap and separate authority.

#### Security / Privacy and Observability

Preserve current security/privacy behavior. Failure output must not expose AWS
credentials/tokens, secrets, raw provider exception details where sanitization
is required, raw prompts or model responses, `reviewer_id`, workbook binary,
arbitrary request bodies, or confidential commercial/customer payload. Reuse
C16 structured logging only on paths that already use it; where emitted, the
failure outcome remains visible with bounded correlation and existing
sanitization. Do not force every failure into CloudWatch or add a broad event
taxonomy.

#### Data, Persistence, and Dependency Boundary

C18 adds no database, persistence authority, S3 data model, customer-data
collection, secret, credential, or third-party dependency. Prefer current
stdlib, project types, test mechanisms, and injectable provider/storage
boundaries. Do not add resilience, retry, guardrail, or policy frameworks
without a new human decision. Bedrock Guardrails product integration is
DECLINED / DEFERRED for V1 C18. No live AWS/Bedrock call or preparation is
required or authorized by this contract.

#### C16 and C17 Relationship

C16 observability is reused where an affected runtime path already supports
it; C18 creates no log group, metric, alarm, dashboard, X-Ray, or other
observability resource. C17 is NOT a C18 dependency. Do not modify its Golden
Dataset, metrics, report schema, or evaluation logic. C17 may be run as
regression evidence, but C18 owns its own all-15-state matrix.

#### Verification Strategy

Audit existing paths and tests first; trace each §8 state to its owning layer;
reuse sufficient evidence with references; add bounded deterministic tests only
for partial/missing evidence; inject provider/storage/tool/export failures
through existing boundaries; make the smallest reversible fix only for a
proven gap; then rerun the complete matrix, cross-cutting integration and
relevant prior-Card regressions. Verify any applicable C16 log event remains
sanitized. Do not perform destructive live failure tests.

#### Architecture Ownership

C18 begins as a cross-cutting proof/audit Card, not a new runtime subsystem.
Existing owning layers remain responsible for their failure states; no new
architecture category, source module, or package is required by default. Do
not create a central guardrail manager. If later evidence makes a narrow
architecture change appear necessary, stop for justification and independent
review under the authorized C18 scope.

#### Advanced Verification Decision

| Technique | Decision | C18-specific reason |
| --- | --- | --- |
| Deterministic invariants | REQUIRED | Each fail-closed state and authority boundary needs an exact expected outcome. |
| Contract tests | REQUIRED | Existing component/API/provider/storage/tool contracts are the enforcement boundaries. |
| Integration | REQUIRED | Failure propagation crosses existing layers and must not become success between them. |
| Generated property tests | CONDITIONAL / EVALUATE | Useful only if numeric/input boundaries have meaningful combinatorial space beyond fixed cases. |
| Targeted mutation-resistance | REQUIRED | Challenge silent success, bypass, fabricated fallback, and weakened failure states. |
| Failure injection | REQUIRED | Provider, storage, tool, and export unavailability are explicit C18 concerns. |
| Fuzzing | CONDITIONAL / EVALUATE | Use only where a parser/schema/input surface warrants it. |
| Differential | CONDITIONAL / EVALUATE | Use only if a genuinely independent oracle exists; do not duplicate implementation logic as an oracle. |
| Concurrency/race | CONDITIONAL / EVALUATE | Needed only where affected transitions use shared mutable state or concurrency. |
| Adversarial testing | REQUIRED | Exercise approval bypass, invalid AI output, fabricated evidence, unsupported actions, and misleading failures. |
| Threat modeling | REQUIRED | The Card spans commercial, evidence, AI, approval, storage, and security boundaries. |
| Agent evals | REQUIRED where agent/provider/tool failure paths are involved | Deterministic scripted traces must show invalid AI/tool outcomes fail closed. |
| Rollback/recovery | REQUIRED | Each bounded fix must be Git-reversible; current scope adds no cloud/data rollback. |
| Formal methods | NOT_APPLICABLE | Contract, injection, and mutation evidence is proportionate; no formal-proof claim is made. |

#### Independent Verifier Expectations

Independently inspect all 15 rows against Guardrails §8 and cited evidence;
challenge whether reuse actually proves the exact invariant; check for omitted
states, false-green classifications, untested failure propagation, unsafe
fallbacks, authority changes, sensitive leakage, and C17/C19 leakage. A verifier
may return BLOCKED when a row is not directly proven.

#### Evidence / Traceability

The Evidence Map is the technical matrix and records actual commands/results
only after execution. The Learning Log records rationale and actual problems
or remediation without inventing implementation history. Each row links its
source contract, owner, test/evidence, classification, C18 action, and final
result. No evidence is inferred from design intent.

#### Known Non-Scope

Bedrock Guardrails product, live AWS/Bedrock proof, destructive cloud tests,
new observability infrastructure, custom metrics/alarms/dashboards/X-Ray,
policy redesign, new guardrail manager/subsystem or architecture category,
new runtime module/package by default, new persistence/database,
new customer-data collection, new third-party dependency, automatic retry or
circuit-breaker infrastructure, C17 dataset/metrics/report changes, C19+, and
production-readiness claims.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C18

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C19 — Golden Case

### 1. Title

V1-C19 — Golden Case

### 2. Engineering Goal

Prove one controlled, fixed, synthetic end-to-end quotation scenario across the existing V1 component contracts. C19 is local, deterministic, and repeatable; it integrates existing components only and is not a deployment or UI Card.

### 3. Learning Goal

End-to-end integration, evidence gathering, workflow validation, failure visibility, and governance-compliant demonstration using existing local/component interfaces and deterministic injected provider/storage clients.

### 4. Why It Exists

A single controlled scenario verifies that delivered components work together without bypassing commercial, AI, evidence, human-approval, export, storage, or privacy boundaries. C19 proves this one synthetic workflow only; it does not establish real-world correctness or production readiness.

### 5. Architecture Concept

Fixed synthetic request → local FastAPI boundary → QuotationAgent/tools → historical and similar retrieval → estimate/actual comparison and deterministic statistics → RiskEvidence → existing provider/Bedrock adapter with fixed injected client → validated structured draft → C11 human-authority approval action → C12 Excel generation/reload/reconciliation → C14 storage adapter with injected client → applicable existing C16 structured event capture.

### 6. Current System Before Card

C01–C18 are complete and delivered. No C19 Golden Case has been executed or evidenced; C19 remains NOT_STARTED until separately authorized. Their completion does not itself prove that their contracts compose in one end-to-end scenario.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

C19 integrates existing components only. It exercises the real local FastAPI boundary and real existing provider, storage, approval, and export interfaces, injecting deterministic clients at Bedrock/provider and S3 boundaries. There is no live AWS, Bedrock, S3, CloudWatch, Lambda, or API Gateway invocation. Failures follow their owning Card's existing contract and are never hidden behind an end-to-end workaround.

C13's process-local `LocalQuoteStore` is a previously accepted V1 limitation. The complete multi-step Golden Case must not depend on deployed Lambda/API Gateway requests sharing process state; C19 does not repair this limitation. C15/C16 cloud/deployment evidence remains separate from C19's local business/application integration proof.

Human approval uses the real C11 interface and a clearly identified synthetic deterministic test actor. This proves the human-owned transition contract, not that a person manually reviewed the automated run. AI cannot approve, and approval may not be achieved by direct state mutation. Reports/logs exclude `reviewer_id` where canonical privacy rules prohibit it.

### 8. Implementation Scope

- execute one fixed synthetic scenario through the existing local FastAPI, Core, history/retrieval/comparison/statistics, RiskEvidence, agent tools, QuotationAgent, provider/Bedrock adapter, structured-output validation, C11 approval, C12 Excel, C14 storage-adapter, and applicable existing C16 event paths
- use a fixed deterministic provider trace and deterministic injected storage client without network or live services; validate provider output through existing contracts
- author expected commercial results independently of the implementation under test; include explicit commercial units/currency, synthetic historical inputs, stable evidence relationships, and deterministic values
- generate a real C12 workbook after approval, reload it, and prove exact business-value/reconciliation and existing workbook-integrity contracts; keep workbook ephemeral
- produce one authoritative machine-readable report with scenario identity, exact required-step accounting, bounded step outcomes, commercial/evidence references, C17 regression result, and overall status
- prove report/fixture integrity, privacy, deterministic two-run equivalence, and that a required failure, omission, skipped approval, or failed Excel reconciliation cannot produce PASS
- collect only applicable bounded local C16 event evidence from existing event paths

### 9. Out of Scope

- live AWS, Bedrock, Bedrock Guardrails, S3, CloudWatch, deployed Lambda, or API Gateway invocation
- solving C13 process-local persistence or introducing a database, persistent workflow store, migration, or new S3 data model
- new production module/architecture category, business logic, adapter, API route/schema/auth/status redesign, deployment, or UI
- C18's full all-15 guardrail matrix or changes to C17's dataset, metrics, report schema, or evaluation logic
- new dependency, LLM-as-judge, real/customer/confidential data, generalized security certification, or production-readiness claim
- committing generated workbook binaries, raw logs, or run reports by default

### 10. Dependencies

No additional explicit Roadmap dependency is created. C01–C18 are the existing component context. C17 is not a C19 dependency; it is rerun unchanged only as regression evidence. C18 is complete; C19 preserves its behavior without duplicating its all-15 matrix. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

The scenario is synthetic-only with stable scenario ID, explicit version, stable serialization, and SHA-256 identity. Expected values are independently fixed, never derived by the implementation under test. The machine-readable report has an explicit schema version and PASS / FAIL / ERROR semantics: PASS requires every required step exactly once and every invariant passing; FAIL means the scenario executed and one or more required contracts failed; ERROR means fixture, report, or execution integrity prevents valid evaluation, including missing, duplicated, or unaccounted required steps. A skipped or failed step cannot yield PASS.

The report includes at minimum `report_schema_version`, `scenario_id`,
`scenario_version`, `scenario_sha256`, `overall_status`, all required-step
results, deterministic expected/actual commercial reconciliation,
retrieval/comparison references, RiskEvidence/provenance references,
agent/tool trace outcome, structured-output validity, C11 approval result,
C12 Excel reconciliation, C14 storage-contract result, applicable C16
observability result, unchanged C17 regression result, and bounded failure
category. Fixture inputs include stable request/quotation identity, items,
rates, estimated hours with explicit unit, currency, relevant synthetic
historical inputs, expected evidence relationships, and fixed expected values.
The exact report filesystem path is an implementation detail.

At least two independent executions must produce identical normalized reports. Normalize/exclude incidental timestamps, generated request IDs, temporary paths, and correlation IDs. Compare workbook business-cell and reconciliation results across runs rather than binary workbook hashes. Required-step failure, required-step omission, skipped approval, and failed Excel reconciliation must each prevent PASS. The report excludes credentials, secrets, raw prompts/responses/request bodies, `reviewer_id`, workbook bytes/content dumps, confidential data, and unsanitized provider errors. Reports may be ephemeral; canonical evidence records sufficient identity/results to reproduce them. Workbook, injected storage state, and captured events are ephemeral.

Exercise bounded harness-integrity mutations, failure injection, and adversarial scenarios; do not duplicate C18's full failure matrix. Rerun C17 unchanged and preserve its expected dataset/report identities. Test not run != PASS. Design intent != implementation evidence.

C17 regression identity is fixed as dataset version `c17-golden-v1`, dataset
SHA-256 `1e2bec2a2c58a9c0082491d8ef746da723689a7f73a9c255e47268a6a6a4cc6b`,
and report SHA-256 `928880c6042e4ab9fa826cf1ba51b88cd2a762209c5006144c2e53f233cf832c`.

### 12. Exit Gate

The dedicated `Exit Gate — V1-C19` in the Roadmap is authoritative and proves this one fixed synthetic scenario. The project-wide Roadmap `Final Gate` remains separate and broader. Every required flow step must be accounted for exactly once; missing, duplicated, or unaccounted steps are ERROR, while an executed step-contract failure is FAIL. No missing/failed step or partial execution may produce PASS. The harness must stop or record a bounded owning-contract failure and may not fabricate fallback success or invent retries. The C13 process-local limitation remains explicit. No live cloud service, new architecture, persistence, dependency, or C17 modification is required.

### C09+ Pre-Implementation Verification Block

#### Risk Classification

**ELEVATED.** C19 integrates commercial arithmetic, evidence, AI orchestration,
human approval, Excel, storage, API, and observability in one assurance claim.
A false Golden PASS could materially overstate V1 integration. It is not
CRITICAL because one synthetic local scenario adds no commercial authority,
persistence, or cloud infrastructure and exercises existing owners.

#### Escalation Triggers

Stop for human direction if the scenario requires live AWS/Bedrock, deployed
Lambda/API Gateway, real S3/CloudWatch, a new route/schema/public contract,
new production architecture, adapter, business logic, persistence, migration,
dependency, C13 process-local persistence repair, C17 modification, changed
prior-Card authority, or operational/cloud cleanup. Stop if expected values
cannot be independently authored, real/confidential data is required, a
required step has no existing interface, or PASS would require skipping or
concealing a failed/partial step. Resolve no contract contradiction by
assumption.

#### Canonical Sources

- C19 Roadmap and its separate `Exit Gate — V1-C19`; the project-wide `Final
  Gate` remains separate.
- `COMMERCIAL_AND_DATA_GUARDRAILS.md` for commercial truth, evidence, AI,
  synthetic data, approval, Excel, storage, and privacy.
- C02–C18 Specifications, Evidence Map, tests, and public/component contracts
  for Core, history, retrieval, comparison/statistics, RiskEvidence, provider,
  tools/agent, C11 approval, C12 Excel, C13 API, C14 storage, C16 events, and
  unchanged C17 regression.
- C13's accepted process-local `LocalQuoteStore` limitation; C15/C16 cloud
  proof remains separate.
- `QUOTATION_ENGINEERING_HARNESS.md`, `PROJECT_CONTROL.md`, and
  `GIT_WORKFLOW.md` for execution/evidence/state/rollback controls.

#### Acceptance Contract

Given one fixed synthetic scenario with verified ID/version/SHA and
independently authored expected commercial values, execute it locally through
existing interfaces with fixed provider/storage injection.

When the local FastAPI-to-Excel/storage workflow runs, account for every
predeclared required step exactly once and validate component contracts,
approval, report/privacy integrity, applicable C16 evidence, and unchanged C17
regression.

Then PASS is allowed only when every required invariant passes, two independent
normalized reports match, and workbook business/reconciliation results agree.
An executed step-contract failure is FAIL; missing, duplicated, unaccounted, or
invalidly evaluated steps/fixture/report are ERROR. Neither status may be
presented as PASS.

Prohibited behavior includes live cloud calls, skipped/duplicated steps,
fabricated fallback or evidence, AI-supplied approval, circular expected
values, sensitive report fields, and hiding the C13 process-local limitation.

#### Golden Case Report Contract

The authoritative machine-readable report uses explicit allowlisted fields:
`report_schema_version`, `scenario_id`, `scenario_version`,
`scenario_sha256`, `overall_status`, once-only required-step outcomes,
expected/actual commercial reconciliation, retrieval/comparison references,
RiskEvidence/provenance references, agent/tool trace outcome,
structured-output validity, C11 approval, C12 Excel reconciliation, C14
storage-contract result, applicable C16 observability result, unchanged C17
regression result, and bounded failure category. It excludes raw prompts/model
responses, `reviewer_id`, workbook bytes/content dumps, arbitrary
request/response bodies, credentials/secrets, confidential payloads, and
unsanitized provider errors. Report path is not frozen. Report, workbook,
in-memory injected storage state, and local event capture may be ephemeral;
governance evidence records their reproducible identity/results.

#### Critical Invariants

- Deterministic Core owns commercial arithmetic. Expected values are
  independent of the implementation under test; units, currency, and
  estimated/actual semantics are explicit.
- Historical/similar outputs and RiskEvidence retain existing provenance and
  authority; no match, evidence ID, or claim is fabricated.
- Model output is untrusted until existing validation. Provider failure cannot
  create a response/quotation; AI/tool output cannot create approval.
- Approval uses the real C11 interface and an explicitly synthetic test actor;
  no direct state mutation or claim of actual manual review is allowed.
- The real C12 workbook is generated after approval, reloaded, and reconciled.
  The real C14 adapter receives that artifact with an injected client and
  cannot claim false storage success or invent bucket/key/object identity.
- Every required step is accounted for exactly once. Partial, omitted,
  duplicated, or failed execution cannot report PASS.
- Reports/events are bounded and sanitized; synthetic data stays synthetic.
  C13 process-local state is neither hidden nor repaired.
- C17/C18 remain unchanged. No live cloud dependency or new production
  authority, architecture, persistence, or dependency is introduced.

#### Threat Model

Explicitly consider false Golden PASS; omitted/duplicated steps; circular
oracle; fixture tampering and scenario version/hash drift; commercial-total
mismatch; fabricated evidence; AI authority expansion; approval bypass;
invalid workbook; false storage success; misleading or missing observability;
sensitive evidence, reviewer, prompt, response, or credential leakage;
synthetic results presented as real-world proof; C17 contamination; accidental
live AWS/Bedrock; and concealment of C13 process-local limitations. Naming a
threat is not proof of control; applicable evidence is required.

#### Verification Strategy

Inspect existing public contracts before harness construction. Freeze and hash
the synthetic scenario; independently review expected values. Exercise local
FastAPI and chain real existing interfaces, including scripted provider,
explicit C11 approval, actual C12 generation/reload/reconciliation, and C14
storage with an injected client. Capture only applicable existing C16 events
and verify bounded event class/name, component/operation, status, existing
correlation semantics, and privacy. Validate allowlisted report construction
and exact once-only step accounting. Run twice and compare normalized reports
and workbook business semantics. Inject required-step failure/omission, skipped
approval, and Excel-reconciliation failure; each must block PASS. Consider
mutations for omitted/duplicated steps, failed step marked PASS, approval
bypass, weakened fixture hash/version, wrong totals, fabricated evidence,
invalid structured result, skipped reconciliation, false storage success,
missing event evidence, sensitive leakage, and partial execution reported as
PASS. Rerun C17 unchanged and relevant regressions. Do not add production
behavior to simplify the scenario.

#### Advanced Verification Decision

| Technique | Decision | C19-specific reason |
| --- | --- | --- |
| Deterministic invariants | REQUIRED | Exact commercial values, evidence identity, approval, workbook reconciliation, and step accounting define the case. |
| Contract tests | REQUIRED | Existing Card-owned public/component contracts must remain satisfied. |
| Integration | REQUIRED | Existing-component end-to-end integration is C19's purpose. |
| Generated property tests | CONDITIONAL / EVALUATE | Only if an input space materially benefits beyond the fixed scenario. |
| Targeted mutation-resistance | REQUIRED | Detect false PASS, skipped steps, approval bypass, and integrity weakening. |
| Failure injection | REQUIRED, HARNESS-LEVEL | Required-step failure must make PASS impossible; do not duplicate C18's matrix. |
| Fuzzing | CONDITIONAL / EVALUATE | Only if a meaningful new parser/report attack surface exists. |
| Differential | CONDITIONAL / EVALUATE | Only with a genuinely independent oracle. |
| Concurrency/race | NOT_APPLICABLE by default | The scenario is sequential and adds no concurrent/shared state. |
| Adversarial testing | REQUIRED, BOUNDED | Challenge approval, evidence, step omission, and misleading PASS. |
| Threat modeling | REQUIRED | Golden PASS is an assurance claim that must not mislead or leak evidence. |
| Agent evals | REQUIRED | Exercise real agent orchestration with a fixed deterministic provider trace. |
| Rollback/recovery | REQUIRED | Harness/fixture changes are Git-reversible and generated artifacts ephemeral. |
| Formal methods | NOT_APPLICABLE | Deterministic contracts/integration/mutation are proportionate; no formal-proof claim. |

#### Independent Verifier Expectations

Independently inspect scenario identity and oracle derivation, required steps,
real component interfaces, approval, workbook values, storage evidence, C16
events, report allowlist/status, two-run equivalence, and unchanged C17
identity. Challenge omissions, duplicates, approval bypass, incorrect totals,
fabricated evidence, or PASS from partial execution. Verify scope/privacy and
C13/C17/C18 boundaries. The verifier may return BLOCKED; design intent is not
execution evidence.

#### Evidence / Traceability

The Evidence Map records scenario identity, report/result identity, actual
step results, commands, and validation. The Learning Log records actual
rationale, alternatives, failures/fixes, tradeoffs, learning, and later-Card
impact. Neither substitutes for the other. Generated report/workbook may be
ephemeral; preserve bounded identity/results sufficient to reproduce. Never
claim an unexecuted step PASS.

#### Known Non-Scope

Live AWS/Bedrock/S3/CloudWatch/Lambda/API Gateway; Bedrock Guardrails; solving
C13 process-local persistence; deployment/UI; new business logic, production
architecture/module/category, adapter, route/schema, persistence/database,
migration, dependency, public CLI, C18 matrix duplication, C17 dataset/metric/
report changes, LLM-as-judge, real/confidential data, retained workbook/raw
logs, cloud cleanup, retries beyond an existing owner contract, and
production-readiness or universal-correctness claims.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C19

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## V1-C20 — Demo UI

### 1. Title

V1-C20 — Demo UI

### 2. Engineering Goal

Add a lightweight portfolio-quality UI for demonstrating the completed V1 workflow.

### 3. Learning Goal

Presenting an AI system professionally without moving business logic into presentation code.

### 4. Why It Exists

A small interface makes the completed workflow understandable while preserving the API and application as the system owner.

### 5. Architecture Concept

Browser → React/TypeScript/Vite → local `/api` proxy → existing FastAPI HTTP
contracts → existing quotation workflow. The frontend depends only on HTTP
contracts and does not reproduce or import backend business logic.

### 6. Current System Before Card

C01–C19 may later provide the completed backend and Golden Case. No UI is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Use React + TypeScript + Vite with npm. This is the approved bounded exception
to the earlier Streamlit preference: C20 is a professional product-style
portfolio prototype, and this stack preserves a clear presentation/API/backend
separation without authorizing a frontend platform. Use TypeScript strict mode,
typed API requests/responses/errors, a bounded reusable API client, and separate
transport, UI state, and view components. Avoid unexplained `any`.

Do not introduce Next.js, Redux, Zustand, Tailwind, Material UI, Chakra,
shadcn, Bootstrap, another state framework, or another design system by default.
Plain CSS/CSS modules or lightweight native styling is sufficient unless
implementation evidence justifies otherwise. Additional major dependencies
require STOP and human approval.

Authorized bounded toolchain: React, React DOM, TypeScript, Vite, Vitest, React
Testing Library and appropriate DOM/user-event support, and Playwright. Resolve
mutually compatible supported versions during implementation. No dependency is
installed by this remediation.

Run locally: browser → React/Vite → Vite `/api` proxy → local FastAPI → existing
backend. Do not add backend CORS, API/schema, authentication, or deployed
infrastructure changes. If this topology or existing API contracts cannot
support the flow, STOP for human approval.

### 8. Implementation Scope

- Support free-form synthetic request input and one optional, clearly synthetic
  C20-owned preset; never import or execute `evaluation/c19.py` at runtime.
- Use actual existing API routes/contracts (independently verify their current
  truth): request/analysis/draft, quote retrieval, approve/reject, export, and
  health as applicable. Do not add a route or alter public contracts for UI
  convenience.
- Demonstrate work items, hours/rates, analysis, comparable historical quotes,
  estimate-vs-actual evidence, RiskEvidence, AI explanation/draft, missing
  information, review state, human approve/reject, and backend Excel download.
- Present deterministic/evidence-based information distinctly from AI text.
  The backend remains authoritative for validation, arithmetic, retrieval,
  evidence, provider/model validation, workflow, approval, export and failures.
  Frontend may format returned values but must not calculate authoritative
  totals, rates, risk statistics, or evidence.
- Approval/rejection uses the existing C11 backend boundary. The frontend must
  not assert approval locally, fabricate a reviewer decision, or let AI approve.
  Backend denial keeps export unavailable. Download only the real workbook
  returned by the existing C12 export endpoint after backend approval.
- Handle loading, empty, validation/missing semantics, provider unavailable or
  invalid, approval/rejection, export failure, and sanitized API/network error
  states truthfully. Representative UI failure evidence is sufficient; C20 does
  not repeat the full C18 matrix.
- No user-facing storage/S3 or observability/CloudWatch screen. No login,
  accounts, roles, authentication platform, browser AWS credentials, or
  deployed Lambda/API Gateway path.
- Local synthetic portfolio demo only. `LocalQuoteStore` remains process-local;
  one stable local FastAPI process may support the demo. C20 adds no persistence,
  does not repair this accepted limitation, and does not claim multi-instance
  reliability.
- Use minimal React presentation/session state; backend responses are
  authoritative. Assess stale async responses if UI permits overlapping work.
- Desktop-first, usable at common laptop/tablet widths. Use semantic/labeled
  controls, keyboard operation, visible focus, meaningful status/errors not
  conveyed only by color, and reasonable contrast. No WCAG certification or
  mobile-app claim.

### 9. Out of Scope

- production SaaS/deployment, frontend AWS hosting, Amplify, CloudFront,
  Cognito, Route53, IAM, live AWS/Bedrock/S3/CloudWatch/Lambda/API Gateway
- backend CORS/API/schema/route/authentication changes, new persistence, or
  repair of C13 process-local state
- duplicated business logic, new provider path, C19 runtime dependency,
  storage/log viewer, CRM/ERP, design-system/platform project, mobile-first app
- real/customer/confidential data, prompts/raw model output, secrets, raw
  provider errors, prohibited reviewer identity, arbitrary payload dumps
- project-wide Final Gate audit/reconciliation (a separate post-C20 phase)

### 10. Dependencies

The Roadmap implementation order is authoritative; C20 follows completed
backend Cards. C19 is prior integration evidence, NOT a C20 runtime dependency.
The explicitly approved frontend/tool dependencies are React, React DOM,
TypeScript, Vite, Vitest, React Testing Library with appropriate DOM/user-event
support, and Playwright. No other major dependency is authorized by default.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Require strict TypeScript checking and production build. Use Vitest + React
Testing Library for core forms, loading/status, backend error display,
evidence-versus-AI presentation, approval/rejection, export gating/download, and
absence of client commercial authority. Verify request/response shapes against
existing FastAPI contracts. Use bounded Playwright real-browser local E2E for a
synthetic request → analysis/draft → evidence → approve → Excel download flow
and at least one meaningful failure state. Do not build visual-regression or
cross-browser certification infrastructure. One primary browser engine is
sufficient. Screenshots, if produced, are illustrative only.

Check safe AI-text rendering, no unsafe HTML injection, bundle secret absence,
privacy and browser-storage boundaries, keyboard/usability baseline, and
representative error states. Existing Python full regression and C17/C18/C19
regressions run unchanged.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The dedicated `### Exit Gate — V1-C20` in the Roadmap is authoritative. It is
separate from the project-wide Final Gate and requires the implementation,
security, usability, integration, and verification outcomes summarized in that
gate. C20 completion does not declare PROJECT V1 COMPLETE: after C20 delivery
and outcome reconciliation, a separate project-wide Final Gate audit must
verify all rows, including README architecture/setup/evidence/limitations.

### 13. Risk Classification

MODERATE: C20 adds a user-facing browser surface and associated security risks,
but no commercial, AI, approval, persistence, or cloud authority. Escalate to
ELEVATED and STOP for human review if implementation needs backend/API or CORS
changes, persistence, authentication, live AWS/Bedrock, frontend business logic,
or broad new tooling.

### 14. Escalation Triggers

Stop for missing information in existing public APIs or any required route,
schema, status, CORS, production backend, persistence, authentication, AWS,
Bedrock, new production architecture, or unauthorized major dependency change.
Also stop if policy/authority boundaries conflict with the actual interface.

### 15. Canonical Sources

PROJECT_CONTROL owns authorization/state. Use the Roadmap C20 contract, this
Specification, Evidence Map, Learning Log, current C13 API schemas/routes,
Commercial/Data Guardrails, and relevant backend owner-Card contracts. Verify
actual route/schema behavior during implementation; do not infer it from this
list.

### 16. Acceptance Contract

Every C20 Roadmap Exit Gate item requires directly traceable implementation and
executed evidence. The local UI uses existing API contracts only; backend
responses own commercial and workflow truth. No missing/failed required check
is PASS.

### 17. Critical Invariants

- No authoritative commercial arithmetic, risk statistics, evidence, approval,
  or export logic in frontend.
- Approval remains a human action through the existing backend route; AI cannot
  approve and local UI state cannot create backend authority.
- Synthetic-only content is visibly identified. C13 process-local limitation
  remains accepted and disclosed.
- Evidence and AI explanation remain visibly distinct; untrusted text is safely
  rendered and failures are bounded/sanitized.
- Browser calls existing API through the local proxy; no CORS/backend contract
  redesign or cloud dependency.

### 18. Verification Strategy

Strict TypeScript/type/build; component/UI tests; API contract tests; local
Vite/FastAPI integration; bounded browser E2E success and failure; accessibility
/usability; privacy/security; mutation and failure injection; bounded
adversarial/threat-model checks; unchanged Python and prior-Card regressions.

### 19. Advanced Verification Decision

1. Deterministic invariants — REQUIRED: backend values, approval ordering,
   evidence labels, and API-to-view mapping must have exact outcomes.
2. Contract tests — REQUIRED: existing FastAPI request/response contracts are
   the frontend's only system boundary.
3. Integration — REQUIRED: prove local browser/UI to FastAPI workflow.
4. Generated property tests — CONDITIONAL / EVALUATE: only if input/state
   transformations create a meaningful invariant space.
5. Targeted mutation-resistance — REQUIRED: challenge client totals, approval
   gating, evidence labels, rendering safety, and failure-to-success drift.
6. Failure injection — REQUIRED, BOUNDED: provider/API/approval/export/network
   failures must render truthfully without duplicating C18.
7. Fuzzing — CONDITIONAL / EVALUATE: only if a custom parser/serializer is
   introduced.
8. Differential — NOT_APPLICABLE by default: there is no independent second UI
   implementation.
9. Concurrency/race — CONDITIONAL / EVALUATE: assess stale async responses if
   concurrent requests can overlap; do not invent concurrency otherwise.
10. Adversarial testing — REQUIRED, BOUNDED: unsafe AI text, approval bypass,
    fabricated success/evidence, commercial-authority drift, and secrets.
11. Threat modeling — REQUIRED: C20 adds a browser and user-facing trust
    boundary.
12. Agent evals — NOT_APPLICABLE as C20-specific technique: C20 does not change
    agent behavior; C19/C10 remain regression evidence.
13. Rollback/recovery — REQUIRED: tracked frontend/toolchain changes are
    Git-reversible; no cloud/data rollback.
14. Formal methods — NOT_APPLICABLE: disproportionate for this presentation
    surface.

### 20. Independent Verifier Expectations

Independently inspect the API-only boundary, actual route/schema compatibility,
absence of duplicated business logic and secrets, browser flow, approval/export
authority, representative failures, privacy/accessibility, mutations, and
bounded claims. A verifier may return BLOCKED.

### 21. Evidence / Traceability

Record actual file paths, resolved dependency versions, commands/counts,
component/API/browser results, security/accessibility review, mutation/failure
outcomes, prior regressions, and limitations. Screenshots are illustrative,
not correctness evidence. No result is recorded before it occurs.

### 22. Known Non-Scope

Production SaaS, cloud hosting, auth platform, backend/API/CORS redesign,
persistence, business logic, provider changes, storage/observability UI, C19
runtime coupling, mobile-first/design-system work, and the post-C20 project-wide
Final Gate audit.

### 23. C20 Security, Privacy, and UI-State Contract

Safely render untrusted/model-controlled text; do not use `dangerouslySetInnerHTML`
unless separately justified and sanitized. Do not expose prompts, raw model
responses, raw provider errors, credentials/tokens, secrets, prohibited
`reviewer_id`, workbook bytes, arbitrary request/response bodies, or
confidential/customer payloads. Do not put secrets in frontend source or bundle.
Do not use localStorage/sessionStorage for prohibited sensitive data. Backend
failure messages remain sanitized. UI state is presentation/session state only;
backend responses are authoritative. Use minimal React state, not Redux/Zustand
by default. Evaluate stale-response risk if overlapping asynchronous requests
are possible.

### 24. Mutation and Adversarial Targets

Later implementation/audit must consider: UI total substituted for backend
total; approve/export enabled after backend denial; API failure shown as success;
AI explanation relabeled as deterministic evidence; fabricated RiskEvidence;
unsafe HTML/model-text rendering; reviewer identity/raw error leakage;
synthetic disclosure removed; stale response overwrites newer state when
applicable; frontend imports/duplicates business logic or bypasses API; UI
generates Excel instead of using backend; or C13 process-local limitation hidden
in portfolio claims. Applicable mutations must be caught by evidence; do not
execute them as part of this pre-implementation remediation.

### 25. Threat Model

Require disposition/evidence for XSS and unsafe model-text rendering; secrets in
bundles; prompt/model/provider-error or reviewer-identity exposure; approval or
commercial-authority drift; fabricated evidence; false-success UI; stale async
state; sensitive browser storage; synthetic data presented as real history;
API-boundary bypass; hidden C13 process-local limitation; and production/public
readiness overclaim.

### 26. Failure Injection and User-Facing Failure Contract

Use bounded deterministic API/provider/approval/export/network-style failures
that the local existing backend can represent. Verify honest loading, validation,
provider unavailable/invalid, approval/rejection, export failure, and sanitized
generic network/API states. Do not reproduce C18's full guardrail matrix or add
retry behavior/new failure semantics. Backend denial or failure must never be
presented as successful approval/export.

### 27. Claim Boundary

Maximum claim: “A professional local React/TypeScript demonstration UI
exercised the existing V1 quotation workflow using synthetic data.” C20 does
not prove production SaaS, secure multi-user operation, persistence, public
cloud readiness, real-customer readiness, real-market commercial accuracy,
accessibility certification, mobile-app readiness, enterprise authentication/
security, or production-scale reliability.

### 28. Project-Wide Finalization After C20

After C20 delivery and completion reconciliation, a separate FINAL V1
PROJECT-WIDE AUDIT / FINAL GATE RECONCILIATION is required. It verifies every
project-wide Final Gate row, all Cards C01–C20 delivered/complete, README
architecture/setup/evidence/limitations, bounded claims, clean synchronized
repository, and retained AWS resource/status facts and limitations. This is not
part of C20. No release/tag is required by this contract.

### 29. Rollback, Generated Artifacts, and Source Adaptation

Rollback is Git-only for tracked frontend/test/config files. `node_modules`,
build output, Playwright transient files, downloaded Excel files, and generated
test artifacts remain untracked/ephemeral by default. No cloud, S3, database, or
operational rollback is expected. React/TypeScript/Vite/testing/browser
documentation may be REFERENCE ONLY. No external template/code/component reuse
is authorized by remediation; any later actual reuse requires normal source and
license traceability review before incorporation.

### 30. C20 Demo Preset and C19 Boundary

Free-form synthetic input is supported; one lightweight C20-owned synthetic
preset is allowed and must be visibly identified. It need not have a
C17/C19-style fixture identity unless later used as a correctness oracle. C19
remains prior integration evidence only: C20 must not import or execute
`evaluation/c19.py` as runtime/demo code. C20 may rerun C19 unchanged for
regression evidence.

### 31. Local Composition Boundary

A bounded non-production local launcher/composition may be used only if existing
application/provider interfaces support it without production source or public
contract changes. It may inject deterministic provider behavior; it must not
duplicate backend logic or call live cloud services. No public CLI is required.
If the approved local topology cannot be supported by existing interfaces,
STOP for human approval.
Before Card COMPLETE:

CARD_LEARNING_AND_DECISION_LOG.md → V1-C20

must be current and contain actual implementation learning and rationale where applicable. Required content includes, as applicable, what was actually built, key design decisions, why the selected approach was chosen, alternatives for material decisions, technology/library rationale, problems, root cause, fix and fix rationale, tradeoffs/limitations, What We Learned, a future-maintainer reminder, and impact on later Cards.

QUOTATION_CARD_EVIDENCE_MAP.md proves technical facts and validation. CARD_LEARNING_AND_DECISION_LOG.md preserves rationale and engineering understanding. Learning documentation does not replace evidence, and evidence does not replace learning documentation. Both are required for completion.

If a real implementation or validation failure occurs, preserve technical failure and recovery evidence in QUOTATION_CARD_EVIDENCE_MAP.md and preserve the root cause, fix rationale, and lesson in CARD_LEARNING_AND_DECISION_LOG.md. A repaired failure must not disappear. Do not invent a failure where none occurred.

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

NOT YET RECORDED — complete only from actual implementation evidence.

## Historical Migration Baseline (Not Current Project State)

This preserved contract snapshot records the migration-time baseline in which all 20 Cards were NOT_STARTED, no Card was authorized, and no Card was COMPLETE. It is not current project state or authorization authority; consult PROJECT_CONTROL.md for live state. This file remains a governance contract and does not authorize implementation.
