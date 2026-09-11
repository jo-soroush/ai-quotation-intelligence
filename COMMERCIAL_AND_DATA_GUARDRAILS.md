# COMMERCIAL_AND_DATA_GUARDRAILS.md

## 1. Purpose and Authority

This file defines project-wide invariants for quotation inputs, time and hours, monetary values, rates, estimated and actual data, historical evidence, similarity and comparison evidence, risk intelligence, deterministic calculations, AI authority, structured AI outputs, synthetic data, Excel export, human approval, S3 persistence boundaries, and failure behavior.

Deterministic software owns authoritative commercial truth.

AI may interpret and explain verified values. AI may not create authoritative commercial facts.

Unknown financially material semantics must fail closed. This is a governance contract, not implementation evidence or Card authorization.

## 2. Core Guardrails G01–G40

### G01 — AI cannot invent hourly rates

Rates must come from validated request data, validated configuration, or approved historical/synthetic data sources. An absent required rate produces MISSING_RATE. Never substitute zero or ask the model to guess.

### G02 — AI cannot calculate authoritative totals

Authoritative totals are computed by deterministic software. AI may display or explain validated totals only.

### G03 — AI cannot override deterministic calculations

A disagreement produces DETERMINISTIC_CONFLICT. The deterministic value remains authoritative and the AI value is invalid for that field.

### G04 — Missing estimated hours is not zero

null / missing / unknown != 0.

### G05 — Missing hourly rate is not zero

null / missing / unknown != 0.

### G06 — Units and currency must be explicit

Time units and monetary currency must be explicit at system boundaries. The initial V1 direction may use hours and SEK, but Core must not assume them without validated context.

### G07 — Estimated and actual values must never be conflated

Keep estimated_hours, actual_hours, estimated_cost, and actual_cost distinct. Missing actual outcomes cannot be treated as actual equals estimated.

### G08 — Historical evidence requires provenance

Risk and comparison evidence must retain source identity such as quote_id, project type, work item, and relevant outcome or variance. AI explanations must be traceable to underlying evidence.

### G09 — Risk suggestions require evidence

Every risk suggestion requires historical or deterministic evidence. Insufficient evidence produces INSUFFICIENT_EVIDENCE.

### G10 — Unsupported AI claims are invalid

Unsupported factual, commercial, or risk claims produce AI_UNSUPPORTED_CLAIM and must be rejected or removed, not upgraded into evidence.

### G11 — Synthetic data must stay explicitly synthetic

Public portfolio historical quotations are synthetic by default and must never be described as real company quotations, real customer pricing, or real delivery outcomes.

### G12 — Secrets and confidential data are prohibited in the public repository

Do not store AWS access keys, secret keys, tokens, customer confidential quotation data, real confidential pricing, or private commercial documents.

### G13 — Bedrock failure cannot silently create a quotation

Bedrock failure, timeout, invalid response, or unavailability produces AI_UNAVAILABLE or AI_INVALID. No fabricated fallback quotation is allowed.

### G14 — Structured AI output must be validated

Model output must pass expected structure and schema validation before entering application state. Invalid output produces AI_INVALID.

### G15 — Excel totals must reconcile

Excel values must reconcile exactly with deterministic quotation calculations. Failure produces EXCEL_RECONCILIATION_FAILED and stops finalization.

### G16 — Final quotation requires explicit human approval

Required flow is Draft → Deterministic Validation → Human Review → Approval → Final Excel Export. Without approval, return APPROVAL_REQUIRED and do not produce a final state.

### G17 — Human approval does not override arithmetic truth

Approval may accept or reject a business decision but cannot silently mutate deterministic results. Changed inputs require recalculation.

### G18 — Scope change must remain distinguishable

Historical data must preserve whether scope changed. Scope-change-driven overruns must not automatically be attributed to poor estimation.

### G19 — Historical absence is not evidence of success

Missing actual cost, actual hours, delay, outcome, or scope-change data cannot mean on budget, on time, successful, or no scope change.

### G20 — Comparison requires compatible semantics

Verify compatible units and fields before comparing quotations. Incompatible currency or time representations cannot be compared as equivalent.

### G21 — Percentage variance uses deterministic semantics

Use variance = actual - estimated and calculate percentage variance deterministically from validated values. Estimated equal to zero requires explicit denominator handling. AI cannot invent variance percentages.

### G22 — Cost arithmetic is deterministic

Conceptually, estimated_item_cost = estimated_hours × hourly_rate and estimated_total_cost = sum(validated estimated item costs). Actual cost semantics follow validated source contracts.

### G23 — Similarity is not truth

A similar historical quotation is context, not an automatic price or recommendation. Do not copy a prior price as a new price without validated current inputs and deterministic calculation.

### G24 — Risk evidence and risk language must remain separate

RiskEvidence is validated historical/statistical evidence. RiskSuggestion is AI-assisted interpretation based on that evidence. Never reverse ownership.

### G25 — AI cannot fabricate work items

A suggested work item not supplied or inferred from an approved tool or source is a draft suggestion, not historical fact. Commercial calculations use validated approved work items only.

### G26 — Draft quotation is not approved quotation

Distinguish conceptually at least DRAFT, VALIDATED, AWAITING_REVIEW, APPROVED, and REJECTED.

### G27 — Monetary values require numeric validation

Reject NaN, infinity, invalid strings, and negative values where semantically prohibited. Exact ranges belong to domain-model Cards.

### G28 — Time values require numeric validation

Reject invalid, non-finite, or semantically impossible time values. Do not silently coerce malformed values.

### G29 — Null, zero, and unknown are different states

This applies to hours, rates, costs, duration, actual outcomes, delay, and scope-change indicators. Do not collapse them.

### G30 — Evidence counts must match source records

A statement such as 4 of 5 comparable projects exceeded estimate requires deterministic numerator 4 and denominator 5. AI cannot invent counts.

### G31 — Aggregate statistics are deterministic

Average overrun, median variance, comparable count, overrun rate, total hours, and total costs come from deterministic code. AI explains them.

### G32 — Insufficient evidence must remain visible

The system must be able to return INSUFFICIENT_EVIDENCE instead of forcing a confident risk conclusion.

### G33 — Historical evidence must not be modified by the model

Model output may reference evidence but cannot rewrite source records.

### G34 — Commercial output must be reproducible from validated inputs

The same validated inputs and deterministic logic produce the same authoritative numeric output independently of model wording.

### G35 — Model temperature/randomness cannot alter authoritative commercial values

Generation settings may change narrative wording but must not change validated numeric truth.

### G36 — Tool output is untrusted until validated at its boundary

Historical retrieval, Bedrock, storage, API input, and Excel-related data must be validated before entering authoritative application state.

### G37 — Real and synthetic data must not be mixed silently

If both are supported later, provenance must distinguish them explicitly. Public portfolio mode defaults to synthetic.

### G38 — Currency conversion is out of scope unless explicitly implemented

Do not silently convert currencies. Incompatible currencies produce CURRENCY_MISMATCH or an equivalent explicit failure.

### G39 — No autonomous commercial approval

An agent, tool, or model may never transition a quotation into approved or final commercial state without explicit human approval.

### G40 — Final Excel export must use approved validated state

The final workbook must be generated from the approved, validated quotation state, not raw model output.

## 3. Risk Evidence Model

The conceptual relationship is:

HistoricalQuote → deterministic comparison/statistics → RiskEvidence → AI interpretation → RiskSuggestion

Example only:

Historical comparable projects: 5
Projects above estimate: 4
Average hour variance: +21%

AI may describe that testing effort historically exceeded estimate in most comparable projects. It may not present +21% as a guaranteed future result. Historical correlation is not prediction certainty.

## 4. Deterministic Ownership Table

| Field or concept | Authority |
| --- | --- |
| estimated_hours | validated input/domain state |
| hourly_rate | validated input/configuration/source |
| estimated_item_cost | deterministic engine |
| estimated_total_cost | deterministic engine |
| actual_hours | validated historical data |
| actual_cost | validated historical data |
| hour_variance | deterministic engine |
| cost_variance | deterministic engine |
| variance_percent | deterministic engine |
| comparable_quote_count | deterministic analysis |
| risk evidence statistics | deterministic analysis |
| risk explanation | AI-assisted |
| draft narrative | AI-assisted |
| approval | human |
| final Excel numbers | validated deterministic state |

## 5. AI Authority Table

AI may interpret the request, select approved tools, summarize historical evidence, explain deterministic statistics, draft quotation narrative, suggest evidence-backed risks, identify missing information, and express uncertainty.

AI may not invent rates, historical outcomes, totals, evidence IDs, evidence counts, or deterministic variance/statistics; silently fill missing commercial values; redefine deterministic totals; approve a quotation; bypass human review; or convert a draft into final state autonomously.

## 6. Data Provenance

Historical and comparison evidence requires provenance supporting, conceptually:

quote_id
data_origin
synthetic flag
relevant work item/project type
estimated values
actual values when available
scope-change state when available
comparison/statistical derivation identity where needed

Exact schema is owned by domain-model Cards.

## 7. Synthetic Data Rules

The planned V1 portfolio dataset direction is approximately 40 historical quotation cases with multiple work items, estimated values, actual outcomes, and realistic fictional categories such as:

Software Development
Cloud / Platform
Data Engineering
AI / ML PoC
Test Automation / QA
Software Architecture
Requirements Engineering
Project Management
Embedded / Integration
Digitalization

Possible roles include:

Software Developer
Senior Software Developer
Solution Architect
Data Engineer
ML Engineer
Test Engineer
Requirements Analyst
Project Manager
Technical Lead

Controlled synthetic patterns may include testing often overrunning, integration often overrunning, scope change correlating with higher overrun, project management staying closer to estimate, and cases under, near, and over estimate. These patterns are synthetic design patterns only and do not represent a real company.

## 8. Failure / STOP States

Canonical conceptual states include:

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

Exact exception class names are not defined here.

## 9. Excel Boundary

Excel is a mandatory V1 output. Planned sheets may include Quotation, Risk Analysis, and Historical Evidence.

Authoritative numbers must come from validated deterministic state. Final totals must reconcile. Raw unvalidated model output cannot own authoritative numeric cells. Final output requires human approval and traceable quotation identity/version where appropriate.

## 10. AWS / Storage Boundary

S3-loaded objects must be parsed and validated. Provider-specific boto3 objects stay outside Core. Object existence in S3 does not make data commercially authoritative. No silent overwrite behavior is assumed. Exact persistence and idempotency design belongs to owning Cards.

## 11. Testing Expectations

Future Cards must test applicable invariants, including missing hours/rates not becoming zero, AI not overriding totals, unsupported risk rejection, evidence-count reconciliation, deterministic variance, explicit denominator handling, synthetic provenance, invalid or unavailable Bedrock behavior, Excel reconciliation, and final export blocking without approval.

These tests do not yet exist as implementation evidence.

## 12. Final Rule Block

MISSING != ZERO.
ESTIMATED != ACTUAL.
SIMILAR != IDENTICAL.
HISTORICAL EVIDENCE != FUTURE CERTAINTY.
AI EXPLAINS; DETERMINISTIC SOFTWARE CALCULATES.
NO EVIDENCE → NO RISK CLAIM.
NO VALIDATION → NO AUTHORITATIVE STATE.
NO HUMAN APPROVAL → NO FINAL QUOTATION.
NO SILENT FALLBACK.
NO FABRICATED COMMERCIAL TRUTH.

