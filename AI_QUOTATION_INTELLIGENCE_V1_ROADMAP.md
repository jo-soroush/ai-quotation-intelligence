# AI Quotation Intelligence System — V1 Roadmap

## Project Goal

Build a professional cloud-based quotation intelligence system that fully covers the original business requirements while also serving as a serious Amazon Bedrock learning and portfolio project.

The system must:

- use an AI agent to create draft quotations
- use historical quotation data
- include time, work items, and monetary values
- compare previous estimates with actual project outcomes
- generate evidence-backed risk suggestions
- produce quotations as Excel files
- keep commercial calculations deterministic
- require human review before finalization
- run locally during development and be deployable on AWS
- include testing, evaluation, observability, and failure handling

The project must remain independent from any real company name or confidential data.

All historical project and commercial data used for the public portfolio version will be synthetic.

---

# Target Architecture

```text
                    User / UI
                        │
                        ▼
                     FastAPI
                        │
                        ▼
               Quotation Agent
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
 Historical Tool   Analysis Tool   Quote Tool
          │             │             │
          ▼             ▼             ▼
         S3       Python Engine    Excel Tool
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   Variance         Similarity        Risk Evidence
   Analysis          Analysis           Engine
        └───────────────┬────────────────┘
                        │
                        ▼
                 Amazon Bedrock
                        │
                        ▼
             Structured AI Output
                        │
                        ▼
                 Validation Gate
                        │
                        ▼
                  Human Review
                        │
                        ▼
                Generate Excel
                        │
                        ▼
                       S3
```

AWS deployment target:

```text
User / UI
   ↓
API Gateway
   ↓
AWS Lambda
   ↓
FastAPI
   ↓
Quotation Agent
   ├── Amazon S3
   ├── Python Quote Engine
   ├── Amazon Bedrock
   └── Excel Generator
   ↓
Human Review
   ↓
Generated Excel
   ↓
Amazon S3
```

---

# Technology Stack

## ADOPT

```text
Python
FastAPI
Pydantic
pytest

boto3
Amazon Bedrock
Amazon Nova
Amazon S3
AWS Lambda
Amazon API Gateway
AWS IAM
Amazon CloudWatch

openpyxl

Git
GitHub
```

## EVALUATE WHEN NEEDED

```text
Amazon Bedrock Guardrails
DynamoDB
Knowledge Bases
RAG
Vector database
MCP
LangGraph
Step Functions
ECS
```

## AVOID WITHOUT A CLEAR NEED

```text
Kubernetes
EKS
SageMaker
Complex microservices
Multi-agent architecture
Large React frontend
```

The project must not add technology only for portfolio appearance. Every technology must have a clear technical or business justification.

---

# Core Engineering Rules

1. Original business requirements must never be removed to reduce scope.

2. Commercial calculations must be deterministic.

```text
hours × hourly_rate = cost
```

The LLM must not invent or override commercial values.

3. Historical evidence must exist before an AI risk explanation is generated.

4. AI output must be structured and validated.

5. Human approval is required before a quotation is finalized.

6. Core business logic must remain independent from AWS provider code where practical.

7. The project must work locally before cloud deployment.

8. All public portfolio data must be synthetic.

9. No real company name, confidential quotation, internal pricing, or customer data may appear in the repository.

10. Every Card must have explicit tests and exit criteria.

---

# Phase 1 — Foundation

## V1-C01 — Repository Baseline

Create the project engineering foundation.

### Scope

```text
repository structure
Python environment
dependency management
configuration
logging
pytest
.gitignore
README skeleton
```

### Exit Gate

```text
application imports successfully
pytest executes successfully
configuration loads correctly
core domain has no unnecessary AWS dependency
```

---

## V1-C02 — Domain Models

Create strongly typed domain contracts using Pydantic.

### Core Models

```text
Quote
QuoteItem
ProjectOutcome
HistoricalQuote
NewQuoteRequest
VarianceResult
SimilarQuote
RiskEvidence
RiskSuggestion
DraftQuote
AgentRequest
AgentResult
```

### Goals

- explicit contracts
- validation
- structured AI boundaries
- easier testing
- stable interfaces between components

---

## V1-C03 — Synthetic Historical Data

Create realistic historical quotation data for development and evaluation.

### Initial Dataset

```text
approximately 40 historical quotations
multiple work items per quotation
estimated values
actual outcomes
controlled patterns
```

Example project categories:

```text
Software Development
Cloud / Platform
Data Engineering
AI / ML Proof of Concept
Test Automation / QA
Software Architecture
Requirements Engineering
Project Management
Embedded / Integration
Digitalization
```

Example controlled patterns:

```text
Testing tends to overrun
Integration tends to overrun
Scope changes correlate with higher actual effort
Project management usually remains close to estimate
Some projects finish under estimate
Some projects finish close to estimate
```

The dataset must be synthetic but meaningful rather than purely random.

---

# Phase 2 — Deterministic Intelligence

## V1-C04 — Quote Calculation Engine

Implement all deterministic commercial calculations.

### Capabilities

```text
estimated cost
actual cost
hour variance
cost variance
percentage variance
quotation totals
work-item totals
project totals
```

### Rule

The LLM must never be responsible for arithmetic or commercial totals.

---

## V1-C05 — Historical Comparison Engine

Compare estimates with actual project outcomes.

### Capabilities

```text
estimate vs actual comparison
work-package statistics
project-type statistics
role-level statistics
scope-change patterns
overrun frequency
average variance
```

Example:

```text
Testing

Historical projects: 8
Projects above estimate: 6
Average variance: +19.8%
```

---

## V1-C06 — Similar Quote Retrieval

Find relevant historical quotations for a new request.

### Initial Similarity Signals

```text
project_type
work_packages
team composition
scope characteristics
duration
delivery model
```

### Output

```text
ranked comparable quotations
similarity explanation
supporting quotation IDs
```

No vector database is required initially unless evaluation shows that simpler retrieval is insufficient.

---

## V1-C07 — Risk Evidence Engine

Generate deterministic evidence for potential quotation risks.

### Example

```text
RISK-003

Area:
Testing

Comparable projects:
5

Projects above estimate:
4 / 5

Average variance:
+21.4%

Evidence:
Q-005
Q-012
Q-019
Q-031
```

The AI layer must receive this evidence rather than invent risks without support.

---

# Phase 3 — Amazon Bedrock and Agent Architecture

## V1-C08 — Amazon Bedrock Integration

Connect the application to Amazon Bedrock using boto3.

### Initial Capabilities

```text
Bedrock Runtime client
Converse API
Amazon Nova
structured model responses
timeout handling
error handling
configuration
```

### Bedrock Responsibilities

```text
understand quotation request
interpret historical evidence
explain risks
draft quotation narrative
produce structured AI output
```

### Bedrock Must Not

```text
invent prices
calculate totals
override deterministic results
approve quotations
invent unsupported historical evidence
```

---

## V1-C09 — Agent Tools

Expose bounded application capabilities as tools that the quotation agent can use.

### Initial Tools

```text
get_historical_quotes()

find_similar_quotes()

calculate_quote_statistics()

compare_estimate_to_actual()

get_risk_evidence()

create_draft_quote()

validate_draft_quote()

generate_excel()
```

Tools must:

- have typed inputs
- have typed outputs
- be independently testable
- fail explicitly
- avoid hidden business logic inside prompts

### Exit Gate

* tool interfaces have typed inputs
* tool interfaces have typed outputs
* each tool is independently testable
* each tool fails explicitly rather than fabricating success
* tools delegate to existing owned capabilities without duplicating business logic
* no tool computes authoritative totals, invents evidence, or approves/finalizes a quotation

---

## V1-C10 — Quotation Agent

Implement the actual AI agent required by the project.

### Agent Flow

```text
Receive new quotation request
↓
Understand the request
↓
Determine required information
↓
Select appropriate tools
↓
Retrieve historical quotations
↓
Analyze comparable outcomes
↓
Obtain deterministic risk evidence
↓
Use Bedrock to interpret evidence
↓
Create draft quotation
↓
Return structured result for review
```

### Agent Responsibilities

```text
reason over the request
select tools
use tool results
maintain task context
produce a grounded draft
surface missing information
avoid unsupported claims
```

The agent must be a genuine tool-using component rather than a fixed chain labeled as an agent.

### Exit Gate

* the agent understands a quotation request and selects only C09's available tools
* tool selection and tool results are validated before use
* commercial totals, historical outcomes, and risk evidence are never computed or invented by the model
* missing or insufficient evidence is surfaced explicitly rather than silently omitted
* the returned successful result is a validated structured AgentResult rather than unvalidated model text
* no final approval or autonomous finalization occurs

---

# Phase 4 — Governance and Output

## V1-C11 — Human Review Gate

A commercial quotation must not be finalized autonomously.

### Flow

```text
Agent Draft
↓
Validation
↓
Human Review
↓
Approve / Reject
↓
Final Export
```

### Rules

- AI proposes
- deterministic systems validate
- human approves
- approval state must be explicit

### Exit Gate

* final quotation finalization remains blocked without an explicit human review decision
* approval and rejection are explicit, validated human actions; AI, agents, models, and tools cannot create or impersonate approval
* only a valid or revalidated quotation draft enters review; invalid, unavailable, or insufficient C10 results cannot become approvable success
* review cannot change authoritative deterministic commercial calculations, and changed commercial inputs require revalidation
* the reviewed quote and evidence identity and provenance remain bound to the decision
* approval and rejection state is represented explicitly, and invalid transitions are rejected
* C11 establishes review and finalization eligibility without implementing C12+ export, transport, storage, deployment, or UI responsibilities

---

## V1-C12 — Excel Generation

Generate the requested quotation document using openpyxl.

### Output

```text
Draft_Quote.xlsx
```

This is an example filename, not a required path or naming convention. The
required artifact is a loadable `.xlsx` workbook; its return representation
and any local file handling are C12 implementation decisions. No S3 output is
required by C12.

### Required V1 Sheets

```text
Quotation
Risk Analysis
Historical Evidence
```

### Quotation Sheet

```text
work item
estimated hours
hourly rate
estimated cost
total
```

Include quotation identity and explicit currency. The displayed commercial
values must come from the approved, validated quotation and reconcile with
Core. A per-item `role` is optional/unsupported in V1 because `QuoteItem` has
no role field; it must not be inferred from descriptions, model text, or
historical records. Do not silently substitute a role value.

### Risk Analysis Sheet

```text
risk suggestion
severity indicator
bound evidence ID references
```

Render only risk content and evidence links carried by the approved result.
Do not invent an area or historical pattern that the approved result does not
contain.

### Historical Evidence Sheet

```text
approved historical evidence ID references
links between those IDs and approved risk suggestions
```

The approved C11/C10 result currently binds evidence IDs, not historical
quote records, estimated/actual values, variances, or comparison summaries.
Those richer fields are unsupported for C12 V1 unless a later canonical
contract binds them to the reviewed result. C12 must not perform a new
historical search or select new evidence after approval. The sheet must make
the limited evidence-reference scope visible rather than fabricate or imply
missing historical metrics; synthetic history must never be presented as real.

### Exit Gate

* only current, revalidated C11-approved state can produce a final workbook; copied review metadata, an APPROVED-looking status, or stale/modified state is insufficient
* the result is a valid `.xlsx` workbook produced through the approved Excel boundary, with the three required V1 sheets and only supported, approved content
* workbook commercial values reconcile exactly with deterministic Core truth; export does not invent or alter hours, rates, currency, item costs, totals, evidence, or approval state
* absent role or historical metrics are not fabricated; evidence references and synthetic-history limitations remain explicit
* untrusted text is rendered inert as spreadsheet content, not executable formulas; workbook validation or reconciliation failure is explicit and blocks final export
* C12 does not implement FastAPI, S3, deployment, UI, persistence, Bedrock reasoning, autonomous approval, or later-Card scope

---

# Phase 5 — API and AWS Cloud

## V1-C13 — FastAPI Application

Expose the system through a clean API layer.

### V1 Required Endpoints

```text
POST /quotes/analyze
POST /quotes/draft
POST /quotes/{id}/approve
POST /quotes/{id}/export
GET  /quotes/{id}
GET  /health
```

FastAPI must remain a delivery layer rather than contain core business logic.

`POST /quotes/analyze` and `POST /quotes/draft` expose existing analysis and
draft capabilities without granting approval. `GET /quotes/{id}` retrieves the
process-held quotation/review view; it does not reconstruct authority from
client data. Despite its historical path name, `POST /quotes/{id}/approve` is
the human review-decision route: its explicit, validated C11
`ApprovalDecision` may be APPROVED or REJECTED. The route name never implies
approval. `POST /quotes/{id}/export` delivers C12's validated `.xlsx` bytes
only after the current C11 approval gate succeeds. `GET /health` reports
lightweight API/process health without requiring a live Bedrock or AWS call.

For V1, a bounded process-local association may retain the current validated
`AgentResult` and held C11 `ReviewSession` across HTTP requests. That
association is not commercial or approval authority: C11 owns the decision,
and C12 must recheck approval against the current result. Repeated or
concurrent requests in the supported single-process runtime must not bypass
C11's one-decision, transition, or freshness checks. Process restart loses
this state; shared state across workers/processes and persistent session
storage are not guaranteed by C13.

### Exit Gate

* the required V1 routes expose only the approved quotation workflow through typed, validated HTTP contracts
* handlers remain adapters and do not own commercial arithmetic, AI reasoning, evidence discovery, approval authority, or Excel business logic
* C10 failures map to explicit, sanitized transport responses; malformed HTTP input cannot reach authoritative operations
* approve and reject require an explicit caller decision delegated to C11; client status, copied review records, model text, and route names cannot create approval authority
* export delegates to C12 using the held C11 session and current `AgentResult`; stale or modified review state cannot export
* cross-request process-local state and concurrent or repeated requests preserve C11 transition/freshness and C12 approval checks without claiming durable or multi-process authority
* unexpected internal or provider failures cannot expose secrets, raw provider payloads, or internal exception details
* required endpoints are contract-tested; C13 introduces no C14+ storage, deployment, observability, or UI infrastructure

---

## V1-C14 — Amazon S3 Integration

Use S3 for persistent project artifacts.

### Suggested Structure

```text
historical/
generated/
evaluation/
```

Potential contents:

```text
historical quotations
synthetic outcomes
generated Excel files
evaluation artifacts
```

Access must be controlled through IAM.

### Exit Gate

C14 may be COMPLETE only when all of the following are independently proven:

* provider-isolated persistence and retrieval operate through a storage contract and S3 adapter; deterministic local validation remains possible
* the V1 generated quotation artifact comes from the already validated C12 `.xlsx` export boundary, not arbitrary caller-supplied commercial content
* C14 accepts storage-ready artifact bytes and validated storage identity; it does not recreate C11 approval checks or require C11/C10 review objects
* object identity/key derivation is deterministic and validated; arbitrary caller-controlled S3 keys or path/prefix-like untrusted input cannot control the storage namespace or collide across artifacts
* duplicate/idempotency behavior is explicit, deterministic, documented, tested, and never silently overwrites an existing artifact
* retrieval has explicit missing-object behavior and validates storage identity/integrity at the storage boundary without duplicating C12 workbook or commercial validation
* provider/service, access/credential, malformed-response, duplicate, and integrity failures are explicit and sanitized; no raw boto3/botocore object or exception becomes Core/domain authority
* credentials are obtained through the standard AWS credential provider chain, never hard-coded, persisted, logged, or exposed; least privilege is preserved
* C14 does not make objects public, set public ACLs, or add public sharing; bucket provisioning and encryption configuration remain runtime/deployment concerns
* deterministic local tests prove the adapter without network or real AWS; live S3 validation is optional supplementary evidence and is not an Exit Gate prerequisite
* C14 remains independently composable: no C13 route change or automatic `/quotes/{id}/export` upload is introduced
* no C15+ deployment, observability, evaluation, UI, or other infrastructure is introduced

For the V1 quotation artifact flow, the validated C12 workbook is the primary
persistable artifact. C14 does not make the contents commercially
authoritative merely because an object exists in S3. The bucket is supplied
through runtime configuration; C14 does not provision or manage it.

---

## V1-C15 — AWS Deployment

Deploy the API using a simple serverless architecture.

### Target

```text
API Gateway
↓
AWS Lambda
↓
FastAPI
```

### Infrastructure Concerns

```text
IAM least privilege
environment configuration
Bedrock permissions
S3 permissions
logging
timeouts
deployment validation
```

The local version must continue to function independently.

### Exit Gate

C15 may be COMPLETE only when evidence proves all of the following:

* the delivered C13 FastAPI application is deployable through the approved
  API Gateway → AWS Lambda → FastAPI direction, while local/non-Lambda
  execution continues to work independently;
* deployment changes infrastructure only: the six C13 routes, request and
  response contracts, approval rules, ReviewSession authority, C12 export
  authority, commercial arithmetic, agent reasoning, and C14 storage
  authority are unchanged;
* deployment configuration is externalized, AWS credentials are not
  hard-coded, committed, packaged, or supplied as static application
  access-key configuration, and Lambda uses AWS-native temporary
  credentials/execution-role semantics;
* deployer identity is separate from the Lambda runtime identity, and
  deployment and runtime permissions are least-privilege and justified by
  actual operations; no Bedrock or S3 permission is granted merely because
  those capabilities exist in the repository;
* deployment is reproducible from repository-controlled configuration and
  procedure, not dependent on undocumented Console-only state;
* Lambda startup/import compatibility is validated locally before live
  deployment; the API Gateway → Lambda → FastAPI route is proven, including
  correct binary `.xlsx` response handling for the existing C13 export route
  through the selected adapter path;
* the existing C13 process-local state limitation remains explicit: C15
  does not claim durable, shared, multi-instance-safe, or production-safe
  review workflow state, and does not add persistence to solve it;
* exposure is bounded for a non-production deployment, commercial routes
  are not intentionally exposed as an unrestricted anonymous production
  service, access control is considered before external exposure, and
  unrestricted CORS is not introduced;
* a repeatable bounded recovery procedure can redeploy the prior known-good
  artifact/configuration after a failed deployment; C16+ observability or
  other future-Card infrastructure is not introduced;
* local/simulated evidence is distinguished from live AWS evidence. Before
  C15 is COMPLETE, a real Lambda deployment and real API Gateway integration
  must exist in the approved AWS target account/region, and a real HTTPS
  `GET /health` through API Gateway must return the expected C13 health
  response. Record the target region, stable
  deployment identifiers, status, response, timestamp, confirmation that
  no static AWS credential was embedded, and confirmation that local mode
  still works. This smoke proves deployment reachability only, not Bedrock,
  S3, or full quotation-workflow readiness;
* live AWS deployment is required for this final Exit Gate, but live Bedrock
  invocation and live S3 workflow are not. Actual infrastructure evidence
  is never inferred from local emulation.

The C13 in-memory workflow limitation is accepted for this V1 deployment.
Lambda cold starts, execution-environment replacement, and routing across
environments can lose or fail to share that state. Reserved concurrency of
one does not guarantee sequential requests reuse one environment, and
provisioned concurrency does not make process memory durable. A full live
analyze → draft → approve → export workflow is therefore not required for
this Exit Gate; any single-environment run is supplementary evidence only.

After separate C15 start authorization, local implementation and independent
code/configuration audit may begin without AWS resources or live AWS. Before
live resource creation, separate explicit human approval is required, with
the planned resources, cost-sensitive
services, and teardown posture presented. Final live proof requires an AWS
account, standard AWS authentication, a target region, and sufficient deployer
permissions. A real deployment is a non-production test target, not a claim
of public-production readiness. The selected AWS-native exposure control,
deployment mechanism, and implementation details remain C15 decisions.

AWS preparation decision: B — local implementation can begin without
additional AWS setup; AWS account/authentication, target region, and sufficient
deployer permissions are required only before final live deployment evidence.
Startup configuration must be distinguished from configuration needed only
when an optional provider feature is invoked. An S3 bucket is not required
unless separately authorized runtime composition actually uses C14.
Whether `/health` itself is publicly reachable or invoked through controlled
deployment access is an implementation decision and does not make quotation
routes safe for unrestricted public access. Secrets Manager or Parameter Store
is not automatically required absent a separately established application
secret need.

No C14 auto-wiring is implied: C15 does not change the C13 export route into
an S3 upload, and an S3 bucket is not required to begin C15 or perform the
mandatory `/health` smoke. Runtime S3 or Bedrock permissions are justified
only if actual authorized runtime composition uses those capabilities.
Default platform logs needed to diagnose startup do not authorize the C16
observability platform. AWS-provided HTTPS is sufficient; custom domains,
Route53, and ACM custom certificates are not required.

---

# Phase 6 — Reliability, Evaluation and Operations

## V1-C16 — CloudWatch Observability

Add bounded structured operational visibility for the deployed system while
keeping local logging first-class.

### Capture

```text
request_id
quotation_id where appropriate
agent run and outcome
tool calls and failures
Bedrock calls, outcome, and latency
token usage only when available
S3 operations where C14 is actually used
API latency, errors, and final request status
```

### Rules

Do not log:

```text
secrets
AWS credentials
full prompts or raw model responses
raw provider exception text
workbook bytes or contents
reviewer_id
free-form user/customer content
arbitrary request/response bodies
sensitive commercial values unless explicitly necessary and separately approved
```

Use machine-parseable bounded events with operational fields such as event,
request_id, optional quotation_id, component, operation, status, duration,
available token usage, and a sanitized error category. Correlation identifiers
identify a workflow for operations; they are not permission to expose its
contents.

### Boundaries

- Instrumentation may be added to existing API, agent, tool, Bedrock, storage,
  or support logging paths when needed to emit these events. It must not change
  routes, schemas, business or approval authority, provider/storage semantics,
  or commercial calculations.
- `lambda_handler.py` changes are not required by default; allow them only if
  implementation evidence shows they are necessary for correlation/context
  propagation.
- Provider failures such as `BedrockResult.message=str(exc)` must not be logged
  raw; log only a bounded sanitized category/message.
- Local structured logging must work without AWS. In deployed C15, use the
  retained Lambda log group `/aws/lambda/aqi-c15-api`; do not create a parallel
  deployment. Its existing stdout/stderr log permissions are sufficient for
  the logging-only scope. No new runtime IAM or AWS resource is assumed.
- Final C16 Exit Gate proof requires separately authorized bounded live
  evidence that a representative structured event from the retained C15
  Lambda appears in that log group with correlation present and prohibited
  sensitive fields absent. Local simulation is not live evidence. Any AWS
  modification requires separate explicit human approval.
- Bound event volume and avoid payload logging. Reuse the retained 7-day C15
  log retention unless a change is separately approved; ingestion and storage
  volume are the primary C16 cost risks.

### Exit Gate

C16 is COMPLETE only when independent evidence proves:

- operational events are structured, bounded, and consistently correlated
  with request_id and quotation_id where appropriate;
- API latency, errors, and final request status are visible;
- agent runs, tool calls/failures, Bedrock outcome/latency, and token usage
  when available are observable; S3 outcomes are visible only when C14 is
  actually used;
- local logging works without AWS, and the deployed C15 runtime sends
  representative C16 structured events to `/aws/lambda/aqi-c15-api`;
- a live log event is independently verified to contain correlation and
  allowed operational fields while excluding credentials, secrets, raw
  provider errors, prompts/responses, workbook data, reviewer_id, arbitrary
  bodies, and unnecessary sensitive commercial/user data;
- provider errors are sanitized before logging, and observability does not
  become commercial, approval, provider, or storage authority;
- no Core commercial arithmetic changes, new runtime IAM, or new AWS resource
  is introduced for the logging-only scope without separately approved need;
- event volume is bounded and the retained seven-day log retention is reused
  unless separately approved otherwise;
- C16 does not implement custom metrics, EMF, alarms, dashboards, X-Ray,
  distributed tracing, or third-party observability infrastructure.

Local implementation and independent local audit do not require live AWS.
Live AWS evidence is required only for the final Exit Gate and must use the
retained C15 Lambda `aqi-c15-api` and log group
`/aws/lambda/aqi-c15-api`. C16 must not create a parallel deployment.

### Out of Scope

Custom CloudWatch metrics, EMF, alarms, dashboards, X-Ray/distributed tracing,
third-party or enterprise observability platforms, production SRE programs,
C17 evaluation, workflow redesign, commercial arithmetic, approval changes,
durable state, authentication, UI, and C18+ / C20+ Cards are out of scope.

---

## V1-C17 — Evaluation Harness

Build a repeatable evaluation suite.

### Evaluation Areas

```text
calculation correctness
historical comparison correctness
similarity retrieval quality
risk evidence correctness
unsupported-risk rate
structured-output validity
tool-call success rate
agent task completion
Excel correctness
latency
Bedrock usage
cost
```

### Golden Dataset

Maintain a small fixed V1 Golden Dataset with stable case IDs and independently
reviewed expected results. It is synthetic only. Expected results must not be
generated by the implementation under evaluation. The dataset has a version
and stable serialized-content SHA-256; every report is interpreted together
with both identities.

### C17 Evaluation Contract

C17 is OFFLINE, DETERMINISTIC-FIRST, repeatable, and synthetic-Golden-Dataset
based. It uses deterministic oracles, not LLM-as-judge. It requires no live
Bedrock, AWS, network, secrets, or production-runtime change. It does not
claim real-world commercial correctness or production readiness.

The oracle hierarchy is: exact independently authored deterministic expected
value; exact schema/typed-contract validation; exact evidence/provenance
linkage; fixed expected IDs or allowed-set membership; then deterministic
protocol/final-state grading. The harness must not derive expected values
from the implementation under test.

Required PASS/FAIL metrics and thresholds on the fixed Golden Dataset:

| Metric | Definition | PASS threshold |
| --- | --- | --- |
| Calculation correctness | Exact expected arithmetic cases / total calculation cases | 100% |
| Historical comparison correctness | Exact expected comparison cases / total comparison cases | 100% |
| Retrieval Hit@3 | Cases with at least one `expected_similar_quote_ids` member in the first 3 returned IDs / total retrieval cases | 100% |
| Evidence/provenance correctness | Cases with all required evidence identifiers and expected fixture provenance / total applicable cases | 100% |
| Unsupported-risk rate | Unsupported emitted risk references / all emitted risk references | 0%; if none are emitted, rate is 0, but a fixture requiring risk evidence and receiving none fails completeness |
| Structured-output validity | Schema-valid final outputs / total applicable cases | 100% |
| Tool-call contract success | Contract-valid supported calls / total attempted tool calls | 100% |
| Agent task completion | Completed valid scripted-agent cases / total scripted-agent cases | 100% |
| Excel correctness | Workbooks satisfying deterministic C12 reconciliation/structure contracts / total workbook cases | 100% |

Tool-call validity requires a supported tool, valid arguments and result
contract, no fabricated evidence identifier, and no unsupported protocol
action. Agent completion requires an allowed final state, valid structured
result, required evidence linkage, no protocol/prohibited-action violation,
and bounded execution. Exact call order is not graded unless an existing
contract makes ordering normative. Existing C12 contracts, not visual/manual
inspection, are the workbook oracle. Approximate results pass only if an
existing canonical contract defines tolerance.

Latency, Bedrock usage/token counts, and cost are report-only when measurable;
they have no V1 numeric thresholds and cannot change overall PASS/FAIL.
Standard C17 runs use deterministic scripted/fake/provider-neutral behavior:
one deterministic run is sufficient, and the same code, dataset identity,
and deterministic provider trace must produce the same metric outcomes. No
majority vote, confidence interval, or repeated model trial is required.
Any stochastic/live-model study requires separately approved scope and
trial/statistical policy.

The machine-readable report is authoritative and includes
`report_schema_version`, dataset version and SHA-256, `overall_status` of
PASS/FAIL/ERROR, per-metric numerator, denominator, value, threshold where
applicable, status or report-only marker, and per-case `case_id`, result,
bounded failure category/reason, and required evidence/provenance references.
It must not persist credentials, secrets, production prompts/responses,
`reviewer_id`, workbook bytes, arbitrary request/response bodies, or
confidential customer/business data. Synthetic identifiers and bounded
synthetic expected values may be included where needed.

Overall status is PASS only when every gating metric meets threshold; FAIL
when any gating metric misses; ERROR when evaluation integrity is invalid
(including malformed data, version/hash mismatch, unknown metric definition,
invalid cases, or nondeterministic harness execution). Report-only metrics
cannot independently fail evaluation. FAIL or ERROR blocks C17 completion
and delivery, without establishing policy for future production releases.

### C17 Roadmap Exit Gate

C17 may be COMPLETE only when all of the following are proven:

- A small fixed synthetic-only Golden Dataset exists with stable `case_id`
  values, `dataset_version`, deterministic serialization/content identity,
  SHA-256, and independently authored/reviewed expected results; no
  confidential or real-customer quotation history is used, and the
  implementation under test does not generate its own oracle.
- The offline deterministic harness executes the fixed suite without AWS,
  live Bedrock, network access, credentials, or secrets, and the same code,
  dataset hash/version, and deterministic provider trace yield identical
  metric outcomes.
- Exact deterministic oracles prove calculation correctness = 100% and
  historical comparison correctness = 100%.
- Fixed expected similar-quotation IDs prove retrieval Hit@3 = 100% on this
  Golden Dataset only; no universal retrieval-quality claim is made.
- Evidence/provenance correctness = 100%; unsupported-risk rate = 0%, while
  required-but-missing risk evidence independently fails completeness.
- Structured-output validity = 100%; tool-call contract success = 100%;
  scripted agent task completion = 100%; and deterministic C12 Excel
  correctness = 100%.
- Latency, Bedrock usage/token counts, and cost are reported when measurable
  but are clearly report-only and do not gate PASS.
- No LLM-as-judge is used; no live Bedrock or AWS call is required.
- A deterministic machine-readable report is generated with schema version,
  dataset version/hash, per-metric formulas/results and thresholds, per-case
  outcomes, bounded failure categories, and required provenance references;
  report privacy/redaction requirements pass.
- Status semantics are correct: PASS requires every threshold; any missed
  gating threshold is FAIL; invalid evaluation integrity is ERROR; report-only
  observations cannot alone cause FAIL. FAIL/ERROR blocks C17 completion.
- Threat/adversarial checks challenge circular oracles, fixture/hash/version
  tampering, metric denominators/thresholds, silent case skipping, synthetic
  data misrepresentation, non-deterministic judge authority, report leakage,
  lost provenance, and inflated PASS/production claims.
- Evaluation code is a dedicated offline owner outside production runtime;
  production API/Lambda/application modules do not depend on it. It consumes
  existing public contracts and does not become business authority. Any
  narrow architecture rule needed is justified and independently verified.
- No new third-party dependency is introduced without demonstrated need and
  normal approval/license/source-adaptation review. CI integration remains
  out of scope; the harness is headless/CI-compatible by design.
- Existing C09–C16 regression/security evidence remains authoritative for
  those Cards; C17 only applies bounded protocol constraints needed for its
  scripted cases. C11 reviewer quality is not graded and `reviewer_id` is
  absent from reports.
- The claim is limited to passing defined deterministic contracts on the
  fixed synthetic Golden Dataset. No real-market correctness, real-customer
  model quality, profitability/pricing quality, universal correctness, or
  production-readiness claim is made.
- Learning and Evidence records are current, the C17 quality/Exit Gates pass,
  and the final Card-state consistency gate passes. C17 FAIL or ERROR blocks
  completion; CI, live Bedrock, AWS, and production deployment are not
  completion prerequisites.

This Exit Gate is for offline contract evaluation, not the C19 end-to-end
Golden Case, generalized security evaluation, model-as-judge platform, or
future production-release policy.

---

## V1-C18 — Guardrails and Failure Handling

Design explicit failure behavior.

### Failure Cases

```text
invalid quotation input
missing required fields
no historical matches
insufficient evidence
invalid Bedrock output
Bedrock unavailable
S3 unavailable
tool failure
Excel generation failure
unauthorized operation
```

### Expected Principle

```text
fail explicitly
preserve evidence
avoid fabricated fallback answers
return actionable error information
```

Amazon Bedrock Guardrails may be added here if they provide measurable value.

---

# Phase 7 — End-to-End System

## V1-C19 — Golden Case

Verify the complete professional workflow.

### Golden Flow

```text
New quotation request
↓
FastAPI
↓
Quotation Agent
↓
Historical retrieval
↓
Similar quotation analysis
↓
Estimate vs actual comparison
↓
Risk evidence
↓
Amazon Bedrock reasoning
↓
Structured draft quotation
↓
Validation
↓
Human approval
↓
Excel generation
↓
Amazon S3
```

### Final Gate

The project is not considered V1 complete until:

```text
all required functionality works
all critical tests pass
Golden Case passes
agent uses tools correctly
risk output is evidence-grounded
commercial calculations are deterministic
human approval is enforced
Excel output is valid
cloud deployment works
observability works
evaluation suite runs successfully
README explains architecture and limitations
```

---

# Phase 8 — Portfolio UI

## V1-C20 — Demo UI

Add a lightweight user interface after the complete backend passes the Golden Case.

Preferred initial option:

```text
Streamlit
```

### UI Capabilities

```text
Create new quotation request
Enter work items
Enter estimated hours
Enter hourly rates
Analyze historical projects
View comparable quotations
View risk evidence
View AI draft
Approve / reject
Generate Excel
Download quotation
```

The UI must consume the existing API/core system rather than duplicate business logic.

---

# Final Roadmap

```text
Phase 1
V1-C01 Repository Baseline
V1-C02 Domain Models
V1-C03 Synthetic Historical Data

Phase 2
V1-C04 Quote Calculation Engine
V1-C05 Historical Comparison Engine
V1-C06 Similar Quote Retrieval
V1-C07 Risk Evidence Engine

Phase 3
V1-C08 Amazon Bedrock Integration
V1-C09 Agent Tools
V1-C10 Quotation Agent

Phase 4
V1-C11 Human Review Gate
V1-C12 Excel Generation

Phase 5
V1-C13 FastAPI Application
V1-C14 Amazon S3 Integration
V1-C15 AWS Deployment

Phase 6
V1-C16 CloudWatch Observability
V1-C17 Evaluation Harness
V1-C18 Guardrails & Failure Handling

Phase 7
V1-C19 Golden Case

Phase 8
V1-C20 Demo UI
```

---

# Definition of V1

```text
V1-C01 → V1-C19 = Complete professional backend and cloud system
V1-C20       = Portfolio/demo UI
```

---

# Portfolio Positioning

The finished project should demonstrate:

```text
Agentic AI
Amazon Bedrock
AWS Cloud Engineering
Python
FastAPI
Tool-Using Agents
Structured LLM Output
Deterministic Business Logic
Historical Data Analysis
Risk Intelligence
Human-in-the-Loop Governance
Evaluation
Observability
Failure Handling
Excel Automation
Testing
Cloud Deployment
```

The project should be presented as an independent portfolio project inspired by a real-world quotation workflow.

It must never imply that synthetic data represents the historical data, pricing, customers, or commercial practices of any real company.
