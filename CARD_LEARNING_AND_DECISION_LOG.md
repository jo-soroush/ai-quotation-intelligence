# AI Quotation Intelligence System — V1 Card Learning and Decision Log

Status: CANONICAL EDUCATIONAL ENGINEERING RECORD
Implementation State: NOT_STARTED
Active Card: NONE
Authorization: NONE

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

## Current Project State

Application Implementation: NOT_STARTED
Active Card: NONE
V1-C01 Authorized: NO
Git Repository: NO

No Card learning record may contain implementation claims before implementation begins.

## V1-C01 — Repository Baseline

### 1. Card

V1-C01 — Repository Baseline

### 2. What We Intended to Build

Create a professional, importable, testable, secret-safe repository and Python/application baseline without implementing quotation business logic.

### 3. Why This Card Exists

A clean ownership, configuration, packaging, and testing boundary is needed before domain implementation can be built and evaluated coherently.

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

## V1-C02 — Domain Models

### 1. Card

V1-C02 — Domain Models

### 2. What We Intended to Build

Create typed quotation-intelligence domain contracts with explicit hours, currency, estimated-versus-actual semantics, numeric validation, null-versus-zero meaning, and provenance boundaries.

### 3. Why This Card Exists

Shared typed semantics prevent later calculation, evidence, AI, API, and storage components from inventing incompatible meanings.

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

## V1-C03 — Synthetic Historical Data

### 1. Card

V1-C03 — Synthetic Historical Data

### 2. What We Intended to Build

Create approximately 40 meaningful synthetic historical quotation cases with multiple work items, explicit provenance, and controlled estimate-versus-outcome patterns.

### 3. Why This Card Exists

Historical comparison and risk evidence require repeatable portfolio data while protecting confidential information and avoiding meaningless random noise.

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

## V1-C04 — Quote Calculation Engine

### 1. Card

V1-C04 — Quote Calculation Engine

### 2. What We Intended to Build

Implement deterministic, authoritative quotation arithmetic for validated hours, rates, item costs, totals, and reconciliation.

### 3. Why This Card Exists

Commercial truth must be reproducible and must remain outside AI output so that quotations cannot depend on model arithmetic or silent coercion.

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

## V1-C05 — Historical Comparison Engine

### 1. Card

V1-C05 — Historical Comparison Engine

### 2. What We Intended to Build

Compare historical estimates with actual delivery outcomes deterministically, including explicit hour and cost variance, percentage semantics, aggregates, and scope-change context.

### 3. Why This Card Exists

Grounded quotation intelligence requires reproducible historical comparison that preserves missing outcomes and distinguishes scope-driven overruns from ordinary estimation variance.

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
