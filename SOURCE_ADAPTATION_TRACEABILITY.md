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
Current record statuses are stated in the records below; status does not
supersede the separate Card implementation and delivery gates.

## 9. Recorded Ledger State (Not Live Project State)

```text
Current Records: 7 — one V1-C14 reference; two V1-C15 library reuses and four vendor references
Source Adaptation Records: 7 — 2 REUSE; 5 REFERENCE ONLY
Historical migration-time Application Implementation: NOT_STARTED
Historical migration-time Active Card: NONE
Historical migration-time V1-C01 Authorization: NO
Historical migration-time Git Repository: NO

These fields are retained as historical ledger context. PROJECT_CONTROL.md
owns current project state and authorization; Git owns runtime Git facts.
```

The C15 library decisions below authorize incorporation into the local
package candidate; the first approved live package included Mangum but failed
handler import because another required distribution was missing. The repaired
package remains local and undeployed. Prior
source/template material is not current external implementation reuse.

### V1-C15-SOURCE-01 — Mangum ASGI/Lambda adapter

1. Record ID: V1-C15-SOURCE-01
2. Card: V1-C15
3. Source / Repository: Kludex/mangum, release 0.20.0
4. URL: https://github.com/Kludex/mangum/tree/0.20.0 ; https://github.com/Kludex/mangum/blob/0.20.0/LICENSE
5. File / Module: Mangum package and published license
6. Source Type: Library
7. License: MIT
8. License Verification Status: VERIFIED — release-tagged repository LICENSE and package metadata checked
9. What We Studied: ASGI-to-API-Gateway/Lambda event and response adaptation, Python 3.13 support, and license.
10. Why We Studied It: C15 needs a maintained adapter that preserves C13 semantics, including binary XLSX responses.
11. Decision: REUSE
12. Reason for Decision: The bounded, published adapter avoids implementing a new ASGI event protocol and is locally testable.
13. What Was Taken: Unmodified Mangum 0.20.0 runtime distribution via dependency resolution; no source snippets copied.
14. What Was Not Taken: Examples, deployment templates, authentication systems, and application business logic.
15. Changes Made: Repository-owned Lambda composition wraps the delivered FastAPI app; the library itself is not changed.
16. Risks / Limitations: Local simulation cannot prove live API Gateway behavior; version and binary mapping need focused regression tests.
17. Security / Data Concerns: The adapter processes untrusted HTTP events but owns no approval, commercial, or credential authority.
18. Architecture Impact: Deployment-only entrypoint outside Core; no reverse package dependency.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C15
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
21. Date Recorded: 2026-10-02
22. Status: IMPLEMENTED — included in both live ZIPs; first health failed, repaired-artifact retry passed; C15 not delivered

### V1-C15-SOURCE-06 — OpenTelemetry API runtime dependency

1. Record ID: V1-C15-SOURCE-06
2. Card: V1-C15
3. Source / Repository: OpenTelemetry Python `opentelemetry-api` distribution, version 1.45.0
4. URL: https://pypi.org/project/opentelemetry-api/1.45.0/ ; https://github.com/open-telemetry/opentelemetry-python/tree/main/opentelemetry-api
5. File / Module: Published `opentelemetry-api` wheel, its `METADATA`, and bundled `licenses/LICENSE`
6. Source Type: Library / transitive runtime dependency
7. License: Apache-2.0
8. License Verification Status: VERIFIED — installed distribution metadata declares `Apache-2.0`, and its bundled license text was inspected
9. What We Studied: FastAPI 0.142.2 `Requires-Dist: opentelemetry-api>=1.44.0`, resolver selection of 1.45.0, the distribution's `typing-extensions>=4.5.0` requirement, and the isolated Linux import failure without it.
10. Why We Studied It: The explicit `--no-deps` Lambda snapshot omitted this required distribution, causing the deployed handler import to fail before application initialization.
11. Decision: REUSE
12. Reason for Decision: Pin and package the unmodified required runtime distribution rather than substitute an import shim or broaden application/deployment behavior.
13. What Was Taken: Unmodified `opentelemetry-api==1.45.0` runtime wheel through the existing Lambda package builder; no source snippets copied.
14. What Was Not Taken: OpenTelemetry SDK, exporters, instrumentation, observability configuration, or C16 platform behavior.
15. Changes Made: Added the exact transitive pin to the C15 runtime snapshot and strengthened package closure/import validation; no changes to the distribution itself.
16. Risks / Limitations: Snapshot drift can recur if package metadata changes; the validator now checks dependency closure and a separate isolated Linux handler import.
17. Security / Data Concerns: This is a FastAPI import dependency, not permission to emit telemetry, collect secrets, or make network calls during handler import.
18. Architecture Impact: Packaged dependency only; no new application or Core import authority.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C15
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
21. Date Recorded: 2026-10-02
22. Status: IMPLEMENTED — repaired dependency packaged and deployed to the existing C15 Lambda under separate approval; signed live health HTTP 200; C15 not delivered

### V1-C15-SOURCE-02 — HTTP API Lambda proxy and IAM documentation

1. Record ID: V1-C15-SOURCE-02
2. Card: V1-C15
3. Source / Repository: Amazon API Gateway Developer Guide
4. URL: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html ; https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control-iam.html
5. File / Module: HTTP API Lambda proxy payload 2.0; IAM route authorization
6. Source Type: AWS Documentation
7. License: UNKNOWN
8. License Verification Status: UNVERIFIED
9. What We Studied: Version 2.0 event/response shape, binary base64 response flag, and signed IAM-protected route behavior.
10. Why We Studied It: C15 must preserve XLSX bytes and bound non-production API exposure.
11. Decision: REFERENCE ONLY
12. Reason for Decision: Vendor behavior informs local contract tests and template review; no sample code or deployment artifact was copied.
13. What Was Taken: Documented service semantics only.
14. What Was Not Taken: AWS examples, IAM policy templates, or unrelated API Gateway features.
15. Changes Made: NOT_APPLICABLE
16. Risks / Limitations: The initial signed health returned HTTP 500 at Lambda import; after separately approved package repair/redeployment, a real signed health returned HTTP 200. This proves reachability and startup, not durable review state or production readiness.
17. Security / Data Concerns: IAM protects all six routes; SigV4 smoke must use standard temporary credentials and a constrained target.
18. Architecture Impact: Deployment template only; no C13/Core authority change.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C15
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
21. Date Recorded: 2026-10-02
22. Status: APPROVED

### V1-C15-SOURCE-03 — Lambda Python ZIP packaging documentation

1. Record ID: V1-C15-SOURCE-03
2. Card: V1-C15
3. Source / Repository: AWS Lambda Developer Guide
4. URL: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
5. File / Module: Python ZIP deployment package and Linux-compatible wheels
6. Source Type: AWS Documentation
7. License: UNKNOWN
8. License Verification Status: UNVERIFIED
9. What We Studied: ZIP root layout, bundled dependencies, and Python 3.13 Linux x86_64 wheel targeting.
10. Why We Studied It: C15 must package Pydantic/openpyxl/boto3 dependencies reproducibly from macOS for Lambda.
11. Decision: REFERENCE ONLY
12. Reason for Decision: Only runtime packaging semantics were consulted; no AWS code or configuration was copied.
13. What Was Taken: Documented compatibility constraints only.
14. What Was Not Taken: Vendor sample source, layers, container images, or deployment procedures.
15. Changes Made: NOT_APPLICABLE
16. Risks / Limitations: Local ZIP inspection alone cannot prove Lambda runtime import; final live deployment remains required.
17. Security / Data Concerns: Package excludes local secrets and includes project-declared SDK versions instead of relying on mutable runtime SDK contents.
18. Architecture Impact: Deployment-only build script; no Core/provider direction changes.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C15
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
21. Date Recorded: 2026-10-02
22. Status: APPROVED

### V1-C15-SOURCE-04 — CloudFormation resource schema reference

1. Record ID: V1-C15-SOURCE-04
2. Card: V1-C15
3. Source / Repository: AWS CloudFormation Template Reference
4. URL: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigatewayv2-route.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-apigatewayv2-integration.html ; https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html
5. File / Module: API Gateway V2 Route/Integration and Lambda Function resource properties
6. Source Type: AWS Documentation
7. License: UNKNOWN
8. License Verification Status: UNVERIFIED
9. What We Studied: Resource property names for the reviewable local HTTP API/Lambda template.
10. Why We Studied It: C15 needs a repository-controlled deployment topology without undocumented Console configuration.
11. Decision: REFERENCE ONLY
12. Reason for Decision: Service schema was consulted; no vendor sample template or policy was incorporated.
13. What Was Taken: Documented property semantics only.
14. What Was Not Taken: Example stacks, scripts, account-specific identifiers, and IAM policies.
15. Changes Made: NOT_APPLICABLE
16. Risks / Limitations: The initial stack reached `CREATE_COMPLETE`, but its first signed health failed at handler import. The later separately approved repaired-artifact retry returned real signed HTTP 200; this does not prove durable review state or production readiness.
17. Security / Data Concerns: All product routes are IAM-protected; actual AWS IAM behavior remains pending live evidence.
18. Architecture Impact: Deployment template only; no package architecture permission change.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C15
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
21. Date Recorded: 2026-10-02
22. Status: APPROVED

### V1-C15-SOURCE-05 — Bedrock Converse runtime IAM reference

1. Record ID: V1-C15-SOURCE-05
2. Card: V1-C15
3. Source / Repository: Amazon Bedrock User Guide
4. URL: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html
5. File / Module: Converse API prerequisites
6. Source Type: AWS Documentation
7. License: UNKNOWN
8. License Verification Status: UNVERIFIED
9. What We Studied: Converse requires model-invocation permission when that runtime feature is actually enabled.
10. Why We Studied It: C15 must not grant Bedrock access automatically yet must describe the exact optional runtime permission.
11. Decision: REFERENCE ONLY
12. Reason for Decision: Only documented service authorization semantics were consulted; no IAM sample or code was copied.
13. What Was Taken: Permission name/behavior as an AWS API fact.
14. What Was Not Taken: Broad IAM policies, model-access provisioning steps, or live invocation examples.
15. Changes Made: NOT_APPLICABLE
16. Risks / Limitations: Actual model entitlement, region, and IAM sufficiency remain unproven without approved live use.
17. Security / Data Concerns: Default template grants no Bedrock permission; optional permission is limited to a non-wildcard model/profile ARN.
18. Architecture Impact: Conditional runtime IAM only; no application/provider code change.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C15
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C15
21. Date Recorded: 2026-10-02
22. Status: APPROVED

### V1-C14-SOURCE-01 — S3 conditional-write API reference

1. Record ID: V1-C14-SOURCE-01
2. Card: V1-C14
3. Source / Repository: Amazon S3 User Guide and S3 API Reference
4. URL: https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html ; https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html
5. File / Module: Conditional writes; PutObject `If-None-Match`
6. Source Type: AWS Documentation
7. License: UNKNOWN
8. License Verification Status: UNVERIFIED
9. What We Studied: The documented `If-None-Match: *` conditional PutObject behavior, including existing-object and concurrent-write failures.
10. Why We Studied It: C14 requires an explicit no-silent-overwrite policy without a check-then-write race.
11. Decision: REFERENCE ONLY
12. Reason for Decision: The vendor API behavior informs the adapter contract; no AWS sample code, IAM policy, configuration artifact, or architecture design is incorporated.
13. What Was Taken: No source code or implementation artifact; only the documented API semantics were consulted.
14. What Was Not Taken: Vendor examples, IAM policies, deployment instructions, and unrelated S3 operations.
15. Changes Made: NOT_APPLICABLE
16. Risks / Limitations: Live S3 behavior is not proven by documentation or local tests alone; bucket policy and permissions remain runtime concerns.
17. Security / Data Concerns: Conditional writes avoid ordinary overwrite but do not grant retrieval authorization or commercial authority; no credentials or customer data were used.
18. Architecture Impact: NO — existing provider isolation remains the governing boundary.
19. Evidence Reference: QUOTATION_CARD_EVIDENCE_MAP.md → V1-C14
20. Learning Log Reference: CARD_LEARNING_AND_DECISION_LOG.md → V1-C14
21. Date Recorded: 2026-10-01
22. Status: APPROVED

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
CURRENT RECORDS: 2 — REUSE; 5 — REFERENCE ONLY.
```
