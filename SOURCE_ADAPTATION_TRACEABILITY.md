# AI Quotation Intelligence System — Source Adaptation Traceability

Status: CANONICAL SOURCE-ADAPTATION LEDGER

## 1. Role and Ownership

SOURCE_ADAPTATION_TRACEABILITY.md owns the project-wide record of external
source study and adaptation decisions.

It records what external sources were studied, why they were studied, what
was relevant, whether anything was taken, whether the result was built,
adapted, reused, referenced only, or rejected, the observed license context,
changes made, risks and limitations, Card linkage, and evidence linkage.

It does not own implementation evidence, live project state, Card
authorization, architecture authority, Git state, Card contracts, or final
legal conclusions. License and legal observations are recorded factually;
this ledger is not legal advice.

Ownership remains separated as follows:

```text
SOURCE_ADAPTATION_TRACEABILITY.md → external-source decision and adaptation history
CARD_LEARNING_AND_DECISION_LOG.md → engineering rationale and lessons
QUOTATION_CARD_EVIDENCE_MAP.md → technical proof
PROJECT_PROFILE.md → stable architecture and invariants
PROJECT_CONTROL.md → live project state and authorization
GIT_WORKFLOW.md → Git delivery state and evidence
```

Studying a source does not authorize adoption. A useful pattern may still
result in REFERENCE ONLY or REJECT. Every material decision must be explicit.

## 2. Canonical Decision Taxonomy

The only canonical Source Adaptation decisions are:

```text
BUILD
ADAPT
REUSE
REFERENCE ONLY
REJECT
```

Definitions:

- `BUILD` → build an independent implementation after studying the
  problem/domain; no source code or implementation artifact is incorporated.
- `ADAPT` → use an external design, algorithm, pattern, code fragment, or
  implementation as a starting point and materially modify it for this
  project.
- `REUSE` → incorporate an external component, library, module, or
  implementation substantially as-is, subject to license and technical
  approval.
- `REFERENCE ONLY` → study or cite a source for learning, architecture, or
  context without incorporating its code or implementation.
- `REJECT` → evaluate a source and explicitly decide not to use or adapt it.

Do not introduce alternative decision labels that conflict with this
taxonomy.

## 3. Canonical Source Adaptation Record

Each material source-study or adaptation record uses exactly these fields:

1. Record ID
2. Card
3. Source / Repository
4. URL
5. File / Module
6. Source Type
7. License
8. License Verification Status
9. What We Studied
10. Why We Studied It
11. Decision
12. Reason for Decision
13. What Was Taken
14. What Was Not Taken
15. Changes Made
16. Risks / Limitations
17. Security / Data Concerns
18. Architecture Impact
19. Evidence Reference
20. Learning Log Reference
21. Date Recorded
22. Status

Permitted Source Type values include:

```text
GitHub Repository
Library
Framework
AWS Documentation
Vendor Documentation
Research Paper
Technical Article
Example Project
Code Snippet
Architecture Reference
Other
```

No record is created for trivial standard syntax or ubiquitous language
constructs where no meaningful external artifact or decision is involved.

## 4. License and Incorporation Rules

The `License` field records the observed license or `UNKNOWN`.
`License Verification Status` uses exactly:

```text
VERIFIED
UNVERIFIED
NOT_APPLICABLE
```

Before `ADAPT` or `REUSE`, license awareness is required. `REUSE` with an
`UNKNOWN` or `UNVERIFIED` license blocks incorporation until resolved.
`ADAPT` with an `UNKNOWN` or `UNVERIFIED` license blocks code or design
incorporation where license obligations may apply until resolved.
`REFERENCE ONLY` may proceed with `UNVERIFIED` status when nothing is copied
or incorporated, but the status remains explicit. Do not declare license
compatibility without verified support.

## 5. Taken, Not Taken, and Changes

For `ADAPT` or `REUSE`, record precisely what was taken and what was not
taken. Specific descriptions are required, such as an interface pattern,
retry structure, schema concept, or error-handling pattern, together with
explicit statements that source code, storage layers, authentication code,
or other artifacts were not copied when applicable.

For `ADAPT`, `Changes Made` records material modifications such as renamed or
restructured interfaces, changed provider boundaries, removed unsupported
features, added validation, replaced storage, or changed error handling.
For `REUSE`, it records configuration and integration changes. For `BUILD`,
`REFERENCE ONLY`, and `REJECT`, use `NOT_APPLICABLE` unless meaningful
project-specific notes exist.

## 6. Card, Evidence, and Architecture Linkage

Every record links to one Card as `V1-Cxx`, or uses `PROJECT-WIDE` only when
the source is genuinely not owned by one Card. Do not invent dependencies.

`Evidence Reference` points to actual proof when source material affected
implementation, for example:

```text
QUOTATION_CARD_EVIDENCE_MAP.md → V1-C08
```

`Learning Log Reference` points to the explanatory record, for example:

```text
CARD_LEARNING_AND_DECISION_LOG.md → V1-C08
```

This ledger does not duplicate long technical evidence or learning
narratives.

When a source influences a material architecture decision, record:

```text
Architecture Impact: YES
```

and summarize the affected boundary or component. The corresponding
Learning Log record later preserves Architecture Before / After where
applicable. If there is no material impact, record `Architecture Impact: NO`.
Do not claim current architecture changes.

## 7. Security and Data Rules

Record observed concerns involving secrets, credentials, external data,
customer data, telemetry, unsafe network behavior, code execution, package
supply chain, or unsupported dependencies. Never silently copy environment
files, secrets, datasets, credentials, or confidential quotation data from
an external source.

No external code, configuration, architecture artifact, or substantial
implementation fragment may enter the project without a traceability
decision when adaptation or reuse is material. Engineering judgment applies
to trivial standard syntax and ubiquitous constructs.

## 8. Record Status

`Status` does not replace `Decision`. The allowed record statuses are:

```text
PROPOSED
UNDER_REVIEW
APPROVED
REJECTED
IMPLEMENTED
SUPERSEDED
```

Examples of the relationship are `Decision: ADAPT` with `Status: APPROVED`
or, after actual incorporation, `Decision: ADAPT` with `Status: IMPLEMENTED`.
No current record is approved or implemented.

## 9. Recorded Ledger State (Not Live Project State)

```text
Current Records: NONE
Source Adaptation Records: NONE
Historical migration-time Application Implementation: NOT_STARTED
Historical migration-time Active Card: NONE
Historical migration-time V1-C01 Authorization: NO
Historical migration-time Git Repository: NO

These fields are retained as historical ledger context. PROJECT_CONTROL.md
owns current project state and authorization; Git owns runtime Git facts.
```

No external source has been formally adopted through this ledger. Prior
source/template material is not current external implementation reuse.

## 10. Educational Purpose

The ledger should allow a future reader to answer:

```text
What did we study?
Why?
What did we choose?
Why?
What did we reject?
Did we copy anything?
What changed?
What license applied?
Which Card used it?
Where is the implementation evidence?
What did we learn from it?
```

## 11. Final Rule

```text
STUDYING A SOURCE DOES NOT AUTHORIZE ADOPTION.
DECISION MUST BE EXPLICIT.
NO SILENT COPYING.
LICENSE STATUS MUST REMAIN HONEST.
EVIDENCE AND LEARNING REFERENCES MUST POINT TO THEIR CANONICAL RECORDS.
CURRENT RECORDS: NONE.
```
