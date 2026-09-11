# AI Quotation Intelligence System — V1 Card Specifications

Status: CANONICAL GOVERNANCE CONTRACT
Implementation State: NOT_STARTED
Active Card: NONE
Authorization: NONE

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

Estimate/actual separation, positive/negative/zero variance, percentage variance, zero denominator, missing actual values, aggregate counts, average/median calculations where owned, scope-change context, and no AI involvement.

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

C01–C08 may later provide the baseline, domain services, retrieval, evidence, and provider contract. The full agent and tool layer are not implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

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

Authoritative numeric cells come from validated deterministic state; final export requires approved state and reconciliation.

### 8. Implementation Scope

- generate workbook with planned Quotation, Risk Analysis, and Historical Evidence sheets
- write validated quotation fields
- include evidence references where applicable
- reconcile workbook totals with deterministic totals
- reject invalid or unapproved export state
- preserve quotation identity/version where appropriate
- use openpyxl as the planned library

### 9. Out of Scope

- API transport
- S3 storage integration
- AWS deployment
- UI
- new commercial calculations inside the workbook

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Workbook creation, required sheets, expected fields, numeric reconciliation, approval requirement, invalid-state rejection, evidence traceability, and no numeric authority from model output.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require a valid reconciled workbook generated from approved validated state.

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

### 9. Out of Scope

- S3 adapter implementation
- Lambda/API Gateway deployment
- CloudWatch-specific observability
- UI
- duplicated business logic in endpoints

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Request validation, invalid payloads, happy path, agent failure mapping, approval-required mapping, reject/approve behavior, transport/domain separation, and no endpoint business-logic duplication.

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

Add provider-isolated S3 persistence for required quotation artifacts and data.

### 3. Learning Goal

Storage adapters, serialization boundaries, SDK isolation, validation after retrieval, and failure handling.

### 4. Why It Exists

Required artifacts and historical data need a controlled persistence boundary that remains compatible with local execution.

### 5. Architecture Concept

Core / Application → Storage Contract → S3 Adapter → Amazon S3.

### 6. Current System Before Card

C01–C13 may later provide contracts, services, approved output, and API access. No S3 persistence integration is implemented; application state remains NOT_STARTED.

This is a contract description, not a claim that prior Cards or this Card are complete.

### 7. Design Decision

S3 is an adapter, not commercial truth. Retrieved objects require parsing and validation before entering authoritative state.

### 8. Implementation Scope

- define storage contract
- persist and retrieve approved V1 artifacts/data where justified
- serialize and deserialize through owned schemas
- validate loaded objects
- expose missing-object and service failures explicitly
- keep boto3/S3 objects outside Core
- preserve local mode where possible
- avoid silent overwrite assumptions

### 9. Out of Scope

- deployment
- CloudWatch
- UI
- unrelated database introduction
- domain ownership in storage code

### 10. Dependencies

Explicit Roadmap dependency: none stated. This Card remains ordered according to AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md. Do not infer additional dependencies.

If a dependency is later required but cannot be verified from the Roadmap, use CARD_SPEC_ROADMAP_MISMATCH and stop.

### 11. Tests / Evaluation

Adapter contract, serialization/deserialization, missing object, invalid object, S3 failure propagation, provider isolation, no provider-object leakage, and validation after load.

Test not run != PASS. Design intent != implementation evidence.

### 12. Exit Gate

The Roadmap Exit Gate is expanded only to require provider-isolated S3 persistence with validated serialization, explicit failure behavior, and no SDK ownership in Core.

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

## Current Canonical State

All 20 Cards are NOT_STARTED. No Card is authorized. No Card is COMPLETE. This file is a governance contract and does not authorize implementation.
