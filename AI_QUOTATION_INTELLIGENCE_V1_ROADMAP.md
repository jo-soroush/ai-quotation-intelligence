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

---

## V1-C12 — Excel Generation

Generate the requested quotation document using openpyxl.

### Output

```text
Draft_Quote.xlsx
```

### Recommended Sheets

```text
Quotation
Risk Analysis
Historical Evidence
```

### Quotation Sheet

```text
work item
role
estimated hours
hourly rate
estimated cost
total
```

### Risk Analysis Sheet

```text
risk
area
severity indicator
historical pattern
suggestion
```

### Historical Evidence Sheet

```text
historical quote IDs
estimated values
actual values
variance
comparison summary
```

---

# Phase 5 — API and AWS Cloud

## V1-C13 — FastAPI Application

Expose the system through a clean API layer.

### Initial Endpoints

```text
POST /quotes/analyze
POST /quotes/draft
POST /quotes/{id}/approve
POST /quotes/{id}/export
GET  /quotes/{id}
GET  /health
```

FastAPI must remain a delivery layer rather than contain core business logic.

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

---

# Phase 6 — Reliability, Evaluation and Operations

## V1-C16 — CloudWatch Observability

Add operational visibility for the deployed system.

### Capture

```text
request_id
agent run
tool calls
tool failures
Bedrock calls
Bedrock latency
token usage when available
S3 operations
API latency
errors
final request status
```

### Rules

Do not log:

```text
secrets
AWS credentials
sensitive user data
unnecessary prompt contents
```

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

Maintain a small fixed evaluation dataset with expected results.

The project should measure quality rather than rely only on manual impressions.

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
