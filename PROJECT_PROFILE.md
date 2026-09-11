# PROJECT_PROFILE.md — AI Quotation Intelligence System

## 1. Role of This File

PROJECT_PROFILE.md owns the stable facts, mission, architecture, V1 boundaries, technology posture, and critical invariants of the AI Quotation Intelligence System.

It defines:

- what the system is intended to do;
- what V1 includes and excludes;
- which responsibilities belong to deterministic software, AI, and humans;
- which provider and cloud boundaries are approved;
- how data, evidence, security, evaluation, and failure handling must be treated.

This file does not own:

- live project state;
- Card execution state;
- implementation evidence;
- Git reality;
- Card authorization.

Live state belongs in the project-control record. Card identity, order, scope, and exit criteria belong in AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md and the applicable Card contract. Verified implementation evidence belongs in the evidence record. This profile does not authorize implementation or a Card start.

## 2. Project Identity

~~~
Project: AI Quotation Intelligence System
Version Target: V1
System Type: AI-assisted quotation intelligence and risk-analysis platform
Operating Posture: Local-first, AWS cloud-ready
AI Provider: Amazon Bedrock
Primary AI Model Direction: Amazon Nova initially, provider-neutral Core
Decision Posture: Human-in-the-loop
Commercial Authority: Deterministic software + human approval
Public Data Posture: Synthetic portfolio data only unless explicitly approved otherwise
~~~

The system is an independent portfolio and engineering project. It must not represent synthetic information as the data, pricing, customers, or commercial practices of a real company.

## 3. Mission

The intended V1 flow is:

~~~
Quotation Request
→ Validation
→ Historical Quote Retrieval
→ Deterministic Estimate-vs-Actual Analysis
→ Similar Quote Analysis
→ Risk Evidence
→ Controlled Bedrock Intelligence
→ Draft Quotation
→ Validation
→ Human Review
→ Excel Generation
→ S3 Storage
→ Evaluation + Observability
~~~

The system uses historical quotation information and deterministic analysis to help a human prepare a grounded draft quotation. It must preserve the evidence used, surface uncertainty and missing information, and keep final commercial authority outside the AI layer.

## 4. Product Principle

~~~
AI may interpret, explain, compare, and draft.
AI does not own commercial truth or final approval.
~~~

The system is decision support for quotation preparation, not autonomous commercial authorization.

## 5. Original Business Requirements

The following requirements are mandatory V1 requirements and must not be silently removed:

- AI agent creates draft quotations.
- Historical quotation data is used.
- Time, work items, and monetary parts are included.
- Previous quotations are compared with actual outcomes.
- Risk suggestions are generated from historical performance.
- The final quotation is generated as an Excel file.

## 6. V1 Goals

V1 is intended to establish:

- a realistic synthetic historical quotation dataset;
- typed domain models;
- a deterministic calculation engine;
- estimate-vs-actual historical analysis;
- similar quotation retrieval;
- an evidence-backed risk engine;
- Amazon Bedrock integration;
- a genuine tool-using quotation agent;
- structured AI output;
- a human approval gate;
- Excel generation with openpyxl;
- a FastAPI application;
- Amazon S3 integration;
- AWS Lambda deployment;
- API Gateway integration;
- IAM least privilege;
- CloudWatch observability;
- an evaluation harness;
- explicit failure handling;
- Golden Case end-to-end validation;
- a lightweight portfolio UI after backend completion.

These are planned V1 goals. Their presence here is not evidence that they have been implemented.

## 7. V1 Non-Goals

The following are excluded from V1 unless a later approved Card provides a clear technical and business justification:

~~~
real company confidential quotation data
autonomous commercial approval
AI-authoritative pricing
AI-authoritative totals
multi-agent architecture
LangGraph by default
vector database by default
RAG by default
Kubernetes
EKS
SageMaker
unnecessary microservices
large React frontend
complex MLOps
CRM
ERP
billing/payment execution
~~~

Technology must not be added for portfolio appearance alone.

## 8. Human Authority

~~~
AI proposes.
Deterministic software calculates and validates.
Human approves or rejects the quotation.
~~~

No final quotation may be finalized without explicit human approval. Approval must be represented as an explicit state and must occur after deterministic validation.

## 9. Approved Core Architecture

The approved logical flow is:

~~~
User / UI
→ FastAPI
→ Quotation Agent
→ Tools
→ Quote Engine
→ Historical Data / S3
→ Deterministic Analysis
→ Risk Evidence
→ Amazon Bedrock
→ Structured Draft
→ Validation Gate
→ Human Review
→ Excel Generation
→ S3
→ Evaluation / Observability
~~~

The intended AWS delivery direction is:

~~~
User / UI
→ API Gateway
→ AWS Lambda
→ FastAPI
→ Quotation Agent
→ Amazon S3 / Quote Engine / Amazon Bedrock / Excel Generator
→ Human Review
→ Generated Excel in Amazon S3
~~~

Local execution remains a first-class operating mode.

## 10. Architecture Ownership

Responsibilities must have one clear owner:

| Area | Owner |
| --- | --- |
| Domain contracts and business concepts | domain/core |
| Use-case coordination | application services |
| Tool selection and task context | agent orchestration |
| Arithmetic and commercial totals | deterministic quote engine |
| Estimate-vs-actual and aggregate statistics | historical analysis |
| Supported risk findings | risk evidence |
| Model invocation contract | AI provider boundary |
| Bedrock request/response translation | Bedrock adapter |
| Artifact persistence | storage adapter |
| Workbook construction | Excel export |
| HTTP delivery | API |
| Quality measurement and repeatable cases | evaluation |
| Operational events and diagnostics | observability |

Adapters and delivery layers must not duplicate domain ownership. FastAPI, Bedrock, S3, and Excel-specific representations must not become the source of commercial truth.

## 11. Provider Isolation

AI access must follow this boundary:

~~~
Core
→ AI Provider Contract
→ Bedrock Adapter
→ Amazon Bedrock
~~~

Storage access must follow this boundary:

~~~
Core
→ Storage Contract
→ S3 Adapter
→ Amazon S3
~~~

No Bedrock response objects or S3 SDK objects may become Core domain models. Provider-specific payloads, credentials, retries, and SDK details remain outside Core.

## 12. Canonical Data Boundary

Planned domain concepts include:

~~~
Quote
QuoteItem
HistoricalQuote
ProjectOutcome
NewQuoteRequest
VarianceResult
SimilarQuote
RiskEvidence
RiskSuggestion
DraftQuote
ApprovalDecision
AgentRequest
AgentResult
~~~

These concepts establish the intended boundary, not a final schema. Exact fields, validation rules, persistence details, and ownership must be defined by their owning Cards rather than guessed here.

## 13. Synthetic Data Strategy

The public portfolio version uses synthetic data only unless a separate explicit approval changes that posture.

Synthetic data must:

- be clearly labeled;
- use realistic but fictional project types;
- contain designed historical patterns;
- include estimated and actual outcomes;
- never be represented as real company data;
- never use real company pricing.

The dataset should be meaningful for evaluation rather than purely random. Historical patterns must be documented and reproducible.

## 14. Deterministic Commercial Boundary

Deterministic software owns:

~~~
estimated cost
actual cost
hour variance
cost variance
percentage variance
totals
reconciliation
validation of numeric ranges
~~~

The calculation engine is authoritative for arithmetic, work-item totals, quotation totals, and reconciliation. AI may explain these results but cannot redefine them.

## 15. Historical Evidence and Risk Intelligence

Risk suggestions must be supported by historical evidence.

Example evidence:

~~~
Comparable projects: 5
Testing over estimate: 4/5
Average variance: +21%
~~~

The AI may explain this evidence, compare it, and draft a clear suggestion. It may not invent unsupported risk claims, comparable projects, historical outcomes, or variance values.

## 16. AI Provider Strategy

Amazon Bedrock is the V1 AI provider. Core remains provider-neutral.

The initial direction is Amazon Nova through boto3 and the Converse API where appropriate. Exact model selection, request formats, permissions, and limits remain implementation concerns for their owning Cards.

Required AI behavior:

- structured output;
- schema validation;
- bounded retries;
- timeouts;
- explicit failure state;
- evidence references;
- missing-information reporting;
- no fabricated commercial values.

Bedrock failure must remain visible and must not silently produce a valid quotation.

## 17. AI Authority Boundary

AI may:

- understand a quotation request;
- select approved tools;
- summarize;
- compare;
- interpret historical evidence;
- explain risk;
- draft narrative;
- surface uncertainty;
- surface missing information.

AI may not:

- invent rates;
- invent actual outcomes;
- calculate authoritative totals;
- override deterministic calculations;
- fabricate evidence;
- approve the final quotation;
- bypass human approval.

## 18. Agent Architecture

The quotation agent must be a genuine tool-using component rather than a fixed chain labeled as an agent.

Planned tools include:

~~~
get_historical_quotes
find_similar_quotes
calculate_quote_statistics
compare_estimate_to_actual
get_risk_evidence
create_draft_quote
validate_draft_quote
generate_excel
~~~

Tools should have typed inputs and outputs, be independently testable, fail explicitly, and keep business logic out of prompts. Exact interfaces are defined by the owning Cards.

## 19. Human Review Gate

The mandatory flow is:

~~~
Agent Draft
→ Deterministic Validation
→ Human Review
→ Approve / Reject
→ Final Excel Export
~~~

The approval state must be explicit. Rejection, missing approval, or failed validation must prevent finalization.

## 20. Excel Output

Excel is a mandatory business requirement. Initial output may contain:

~~~
Quotation
Risk Analysis
Historical Evidence
~~~

The quotation workbook may include work item, role, estimated hours, hourly rate, estimated cost, and total. Risk and historical sheets must identify the supporting evidence and comparisons. All commercial totals must reconcile with deterministic calculations.

## 21. AWS Posture

AWS is used only where technically justified. The approved V1 direction is:

~~~
Amazon Bedrock
Amazon S3
AWS Lambda
API Gateway
IAM
CloudWatch
~~~

Local execution must remain possible. Cloud-specific behavior stays behind adapters and must not be required for local validation of Core logic.

## 22. Security Posture

The project must enforce:

- no secrets in Git;
- .env ignored when configuration files are introduced;
- least-privilege IAM;
- standard AWS credential mechanisms;
- no hard-coded AWS keys;
- external and model content treated as untrusted;
- synthetic public data;
- log redaction;
- human approval before consequential commercial finalization.

Security-sensitive configuration must be explicit, reviewable, and separated from domain models.

## 23. Observability

Useful operational information should include:

~~~
request_id
agent run
tool calls
tool failures
Bedrock calls
latency
model identity
token/cost metadata when available
S3 operation status
final request status
~~~

Observability must support diagnosis and evaluation without logging secrets, credentials, or unnecessary sensitive content. Heavy observability infrastructure is not justified by default.

## 24. Evaluation Strategy

Evaluation comes before complexity. Planned measures include:

- calculation correctness;
- historical comparison correctness;
- similarity retrieval quality;
- risk evidence correctness;
- unsupported-risk rate;
- structured-output validity;
- tool-call success;
- agent task completion;
- Excel correctness;
- latency;
- Bedrock usage;
- cost.

Evaluation should use repeatable cases, expected results, and a small fixed Golden Dataset. Manual impressions alone are insufficient for V1 credibility.

## 25. Failure and Recovery Posture

Explicit failure states are required for:

~~~
invalid quotation input
missing required fields
insufficient historical evidence
invalid Bedrock output
Bedrock unavailable
S3 unavailable
tool failure
Excel generation failure
commercial reconciliation failure
approval missing
~~~

Failures must remain visible and actionable. The system must not fabricate fallback answers, silently convert missing information into valid commercial values, or treat an AI failure as approval.

## 26. Technology Posture

### ADOPT

~~~
Python
FastAPI
Pydantic
pytest
boto3
Amazon Bedrock
Amazon S3
AWS Lambda
API Gateway
IAM
CloudWatch
openpyxl
Git
GitHub
~~~

### EVALUATE WHEN NEEDED

~~~
Bedrock Guardrails
DynamoDB
Knowledge Bases
RAG
Vector database
MCP
LangGraph
Step Functions
ECS
~~~

### AVOID WITHOUT CLEAR NEED

~~~
Kubernetes
EKS
SageMaker
multi-agent architecture
large frontend
complex microservices
~~~

Every technology addition requires a clear technical or business justification and must remain within the approved Card scope.

## 27. Critical Project Invariants

- Original business requirements cannot be silently removed.
- AI cannot invent authoritative commercial values.
- AI cannot override deterministic totals.
- Risk suggestions require evidence.
- Unsupported AI claims are invalid.
- Synthetic data cannot be represented as real company data.
- Final quotation requires human approval.
- Bedrock failure cannot silently create a valid quotation.
- Invalid structured output fails explicitly.
- Excel totals must reconcile.
- Provider-specific payloads stay outside Core.
- No secrets belong in the repository.
- Card completion requires actual evidence.

## 28. Development Model

V1 is built through bounded Cards defined by:

~~~
AI_QUOTATION_INTELLIGENCE_V1_ROADMAP.md
~~~

Roadmap position does not automatically authorize implementation. Each Card requires its own scope, dependency checks, approval, validation, and evidence. Work must not be inferred from a future Card or from this profile alone.

## 29. Local-First, Cloud-Ready

Core logic must run locally. Cloud-specific behavior stays behind adapters. Local development and evaluation must be possible without requiring deployed AWS resources, while the approved interfaces must permit later deployment to AWS.

## 30. Definition of Success

V1 is successful when a user can submit a quotation request and the system can:

- retrieve relevant historical quotations;
- compare estimates with outcomes;
- produce deterministic statistics;
- produce evidence-backed risk analysis;
- use Bedrock through a controlled agent workflow;
- create a draft quotation;
- require human review;
- generate a correct Excel file;
- store and retrieve required artifacts through AWS;
- expose the workflow through an API;
- provide tests, evaluation, and observability;
- pass the Golden Case.

These are success criteria, not claims of current implementation.

## 31. Final Principle

~~~
REAL DATA CONTRACTS BEFORE AI.
DETERMINISTIC COMMERCIAL TRUTH BEFORE AI INTERPRETATION.
EVIDENCE BEFORE RISK CLAIMS.
AI DRAFTS; HUMANS APPROVE.
NO SILENT FALLBACK.
NO FABRICATED EVIDENCE.
EVALUATION BEFORE COMPLEXITY.
LOCAL-FIRST, CLOUD-READY.
PORTFOLIO VALUE IS A CONSEQUENCE OF BUILDING THE SYSTEM CORRECTLY.
~~~
