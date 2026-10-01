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

### 13. What We Learned

NOT YET RECORDED — complete only from actual implementation evidence.

### 14. Completion Evidence

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

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require evidence-backed deployment of the approved API direction while preserving local execution and least-privilege boundaries.

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

Add useful operational observability for the quotation workflow without unnecessary observability infrastructure.

### 3. Learning Goal

Structured logs, correlation IDs, agent/tool tracing, cloud observability, failure diagnosis, and sensitive-data redaction.

### 4. Why It Exists

Operators need to trace workflow failures and latency while preserving confidentiality and keeping observability separate from business logic.

### 5. Architecture Concept

Request → application workflow → structured events/logging → CloudWatch where deployed.

### 6. Current System Before Card

C01–C15 may later provide the application, integrations, and deployment. Observability is not implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Use structured, correlated events with local logging support; never fabricate unavailable model metadata or place business decisions in logging.

### 8. Implementation Scope

- capture request_id and quotation_id where appropriate
- capture agent run, tool, Bedrock, S3, workflow, latency, and error fields where available
- include model identity and token/cost metadata only when actually available
- support CloudWatch where deployed
- redact secrets and sensitive commercial content
- preserve local logging without CloudWatch

### 9. Out of Scope

- evaluation harness
- business workflow redesign
- enterprise observability stack
- third-party observability platform without approval

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Structured event shape, request correlation, tool/Bedrock/S3 failure visibility, redaction expectations, no secret leakage, and local logging behavior.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require useful correlated observability with appropriate redaction and no unnecessary infrastructure.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
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

Golden/evaluation cases → system execution → deterministic and AI checks → metrics → evaluation report.

### 6. Current System Before Card

C01–C16 may later provide the workflow and observability. No evaluation harness is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Separate deterministic evaluation from model-quality evaluation and use repeatable cases; do not force metrics unsupported by the task.

### 8. Implementation Scope

- run repeatable evaluation cases
- measure calculation correctness
- measure historical comparison correctness
- measure similar-quotation quality
- measure RiskEvidence and provenance correctness
- measure unsupported-risk rate
- validate structured output and tool-call success
- measure agent completion, Excel correctness, latency, and Bedrock usage/cost where measurable
- report PASS/FAIL and metric results

### 9. Out of Scope

- Golden Case final end-to-end demonstration
- UI
- new model architecture
- production monitoring system

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

The harness runs repeatable cases, distinguishes PASS/FAIL, reports metrics, detects intentionally bad outputs where practical, and preserves evidence traceability.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require repeatable measurable evaluation with separate deterministic and AI-quality checks.

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

C01–C17 may later provide the workflow and evaluation context. Failure enforcement is not implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Align enforcement with COMMERCIAL_AND_DATA_GUARDRAILS.md and reject invalid state explicitly; do not fabricate fallback quotations.

### 8. Implementation Scope

- enforce applicable missing-rate/hour, invalid-value, currency, semantics, evidence, AI, commercial, Excel, approval, and security failures
- cover tool, S3, malformed historical, provider-output, approval, and transition failures
- preserve partial deterministic state only as explicitly partial
- keep failure states observable
- prevent invalid AI output from authoritative application state

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

The Roadmap Exit Gate is expanded only to require evidenced enforcement of applicable guardrails with explicit fail-closed behavior.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
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

Prove the complete professional V1 backend/cloud workflow end-to-end using one controlled representative quotation scenario.

### 3. Learning Goal

End-to-end integration, evidence gathering, workflow validation, failure visibility, and governance-compliant demonstration.

### 4. Why It Exists

A single controlled scenario verifies that the separate Cards work together without bypassing commercial, AI, evidence, or approval boundaries.

### 5. Architecture Concept

Quotation Request → validation → historical/similar retrieval → comparison → RiskEvidence → agent → Bedrock → structured draft → validation → human review → approval → Excel → persistence/API → observability/evaluation.

### 6. Current System Before Card

C01–C18 may later provide the complete components. No Golden Case is implemented or evidenced; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

C19 integrates existing components only. Failures are recorded and stopped or routed to the owning Card; they are not hidden in an end-to-end workaround.

### 8. Implementation Scope

- execute a controlled synthetic quotation scenario
- demonstrate retrieval, comparison, deterministic statistics, RiskEvidence, agent tool use, structured Bedrock output, validation, review, approval, Excel, reconciliation, and applicable persistence/API paths
- collect observability and evaluation evidence
- preserve all invariants and reproducibility

### 9. Out of Scope

- Demo UI
- new architecture
- new major technology
- hidden refactoring of earlier Cards

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Scenario reproducibility, required invariants, evidence traceability, deterministic totals, agent boundary, approval enforcement, Excel correctness, failure visibility, and evaluation report.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require a passing controlled end-to-end Golden Case with all applicable boundaries evidenced and no hidden component redesign.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
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

User → lightweight UI → FastAPI/application interface → existing quotation workflow.

### 6. Current System Before Card

C01–C19 may later provide the completed backend and Golden Case. No UI is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

Use Streamlit or a similarly lightweight justified option; the UI remains presentation-only and does not become a second business system.

### 8. Implementation Scope

- demonstrate quotation request and work-item input
- show similar historical cases, estimate/actual evidence, RiskEvidence, AI explanation, and missing-information warnings
- show draft/review state
- expose human approve/reject action through the existing boundary
- show Excel generation/download
- show useful workflow, error, and status states
- keep synthetic portfolio nature clear

### 9. Out of Scope

- large frontend
- design-system project
- authentication platform without explicit justification
- CRM, ERP, or unrelated product features

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Core user flow, input validation, approval/rejection interaction, draft/final distinction, Excel access, failure display, no duplicated business logic, and basic usability.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require a lightweight presentation layer that demonstrates the completed workflow without owning business logic.

The exact Roadmap Exit Gate remains authoritative; this section expands it without changing its meaning.
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
