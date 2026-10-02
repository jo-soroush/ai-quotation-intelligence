# C15 non-production deployment plan — repaired live health passed

This directory contains the local C15 candidate for API Gateway HTTP API
(payload 2.0) → Python 3.13 AWS Lambda → the unchanged C13 FastAPI app.
Local C15 implementation alone did not authorize AWS changes. A separate
human approval authorized one bounded deployment in `us-east-1`; the stack
reached `CREATE_COMPLETE`, but the first real signed `/health` returned HTTP
500. The missing packaged `opentelemetry-api` dependency was reproduced and
repaired locally. A later separate human approval authorized one immutable ZIP
upload, update of the existing stack, and signed health retry. That retry
returned HTTP 200 with `{"status":"ok"}` on 2026-10-02. Further AWS
mutation and Git delivery are not authorized; C15 remains ACTIVE and
UNDELIVERED pending independent live verification.

## Current retained non-production resources

Account `553541119072`, stack `aqi-c15-nonprod`, Lambda `aqi-c15-api`, API
`yj2yk1sk3g`, and private deployment-artifact bucket
`aqi-c15-artifacts-c69acfc4` were created under explicit approval and are
intentionally retained. The first deployed ZIP had SHA-256
`ff64e11a83a3a70e31524179bad196eeb75a0e120a8859962e26f7101816a939`.
The independent CloudWatch diagnosis identified `Runtime.ImportModuleError:
No module named 'opentelemetry'`; local Linux reproduction found the same
import chain. The repaired deployed ZIP has SHA-256
`5ff6ffe282706a7b8b423580cefc74dffeb54c1ef225ef6bb889cb3fb322279c`;
the existing stack is `UPDATE_COMPLETE` and a real SigV4 `/health` returned
HTTP 200. C15 remains ACTIVE, UNDELIVERED, and NOT COMPLETE. These
resources are not a production-readiness claim.

## Decisions and boundaries

- `deployment/lambda_handler.py` composes the existing C10 agent, C08 lazy
  Bedrock adapter, C09 tools, and C13 `create_app` only. It does not change
  C13's six routes, C11 approval, C12 export, or C14 storage. AWS calls do
  not occur during import or `/health`.
- Mangum 0.20.0 (MIT, recorded in SOURCE_ADAPTATION_TRACEABILITY.md) handles
  ASGI/Lambda events and binary response encoding. HTTP API payload 2.0 is
  sufficient for the existing routes and avoids REST API-specific binary
  media configuration. The adapter path is tested with exact XLSX bytes,
  MIME type, and Content-Disposition; a live export is not claimed.
- CloudFormation JSON plus a local ZIP builder and documented AWS CLI
  commands provide a small reviewable, repeatable procedure. SAM/CDK/Terraform
  would add a framework; direct console-only setup would hide drift.
- All six routes use API Gateway `AWS_IAM`. There is no anonymous quotation
  API, app authentication platform, custom domain, wildcard CORS, or public
  production-readiness claim. A future live `/health` request must be signed
  by a caller permitted `execute-api:Invoke` for that API route. The repo
  provides `scripts/c15_signed_health.py` for that later approved smoke.
- Lambda uses an execution role, never deployer credentials or static keys.
  The default runtime role has log-stream/write permissions scoped to its
  own log group. Optional `BedrockModelArn` grants only `bedrock:InvokeModel`
  on that exact ARN when configured consistently with `BedrockModelId`.
  Without it, model-backed routes can return C10 UNAVAILABLE. No S3
  permission is granted; C14 is not composed into the API.
- The stack's seven-day log group is minimal platform diagnostics, not C16
  dashboards, alarms, metrics, or tracing.

## Bounded C15 threat model

The cloud trust boundaries are deployer → CloudFormation/S3 artifact,
API caller → IAM-protected Gateway → Lambda, and Lambda → optional Bedrock.
Anonymous commercial-route exposure is constrained by `AWS_IAM` on every
route; no wildcard CORS is configured. Deployer overprivilege is addressed
by scoping stack, artifact-bucket, role-pass, and route-invoke permissions;
runtime overprivilege is addressed by a dedicated role with no default S3 or
Bedrock grant and a non-wildcard ARN constraint on any optional model grant.
Static-key/package leakage is challenged by repository and ZIP scans.
Binary corruption is challenged by exact local base64/XLSX round-trip tests.
Cold-start/multi-environment state loss is documented as an accepted limit,
not masked by concurrency settings. Console-only drift is prevented by the
template/procedure. Local tests are labeled local; they cannot become false
live-deployment evidence. A later independent reviewer must challenge these
claims against real AWS configuration before the final Exit Gate.

## Local build and validation

From the repository root, with Python 3.13 and package-index access:

```sh
python scripts/build_c15_lambda.py --output /tmp/aqi-c15-lambda.zip
python scripts/validate_c15_package.py /tmp/aqi-c15-lambda.zip --runtime-smoke
python -m pytest -q tests/test_c15_deployment.py tests/test_api.py
```

The builder refuses an existing output path. It installs the exact tested
dependency snapshot using Linux x86_64 / CPython 3.13 wheels, including
project-declared boto3/botocore instead of depending on a mutable
Lambda-managed SDK. It packages the application, Mangum, openpyxl, and their
runtime dependencies, but no tests, `.env`, AWS profile, or credential file.
It never calls AWS. Rebuild with a new output filename after dependency
changes; review the lock and `pyproject.toml` together. The validator checks
the archive's complete `Requires-Dist` closure against the pinned snapshot.
The optional `--runtime-smoke` additionally needs a locally available
`python:3.13-slim` Linux/amd64 Docker image; it disables container networking
and host package access, then imports the packaged handler and exercises
`/health`. The ZIP is a local
build artifact and must not be committed.

The selected initial settings are Python 3.13, x86_64, 512 MiB, 30 seconds,
and Lambda's default ephemeral storage. These are bounded compatibility
defaults for FastAPI/Pydantic/openpyxl/boto3, not performance claims.
`AQI_AWS_REGION` and `AQI_ENVIRONMENT` are set from deployment context;
`AQI_BEDROCK_MODEL_ID` is a non-secret parameter. `AQI_S3_BUCKET` is not
required. No live Bedrock or S3 call is part of health or the C15 gate.

## Live resource procedure — any retry requires separate human approval

Before any live command, choose and record the AWS account, region, private
artifact-bucket name, unique function/stack names, deployer identity, expected
cost, and whether resources will remain or be torn down. The approved private
artifact bucket named above now exists; another bucket must not be created as
part of the local packaging remediation.
Expected resources: one private deployment-artifact S3 bucket if not already
provided, one Lambda function, one Lambda execution role/inline policy, one
API Gateway HTTP API with six IAM-protected routes and default stage, one
Lambda invoke permission, and one minimal CloudWatch log group. S3 storage,
Lambda invocations/duration, API Gateway requests, and logs may incur cost.
No C14 quotation-artifact bucket or ECR repository is created.

The deployer must have narrowly scoped rights to upload the ZIP into the
approved artifact bucket, create/update the CloudFormation stack and its
listed Lambda/API Gateway/IAM/log resources, pass the stack-created role to
Lambda, and invoke the protected health route for smoke. Bucket creation,
public-access-block, and encryption configuration rights are needed only if
the deployer is approved to create that artifact bucket. Deployer credentials
stay in standard local AWS authentication, never in Lambda code/config.
The runtime role gets only the log actions above and, if explicitly selected,
one exact-model Bedrock invocation grant. No `s3:*`, `bedrock:*`, deletion,
bucket-management, or application authentication grant is in the template.

After separate approval for any live retry, an operator can run the following
repository-controlled procedure. These are **instructions, not evidence of
execution**. Use a unique, private bucket; the example assumes it has been
approved and created/configured (including Block Public Access) by an
authorized operator. If no such bucket exists, obtain specific approval and
create one through approved AWS administration first. Do not infer a bucket
from a default or auto-create it silently.

```sh
export AQI_C15_REGION='approved-region'
export AQI_C15_BUCKET='approved-private-artifact-bucket'
export AQI_C15_STACK='approved-c15-stack'
export AQI_C15_FUNCTION='approved-c15-function'
python scripts/build_c15_lambda.py --output /tmp/aqi-c15-approved.zip
AQI_C15_SHA=$(shasum -a 256 /tmp/aqi-c15-approved.zip | awk '{print $1}')
aws s3 cp /tmp/aqi-c15-approved.zip "s3://$AQI_C15_BUCKET/c15/$AQI_C15_SHA.zip" --region "$AQI_C15_REGION"
aws cloudformation deploy --region "$AQI_C15_REGION" \
  --stack-name "$AQI_C15_STACK" \
  --template-file deployment/c15-http-api.json \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    "ArtifactBucket=$AQI_C15_BUCKET" \
    "ArtifactKey=c15/$AQI_C15_SHA.zip" \
    "FunctionName=$AQI_C15_FUNCTION"
aws cloudformation describe-stacks --region "$AQI_C15_REGION" --stack-name "$AQI_C15_STACK"
python scripts/c15_signed_health.py --api-id 'actual-api-id-from-stack-output' --region "$AQI_C15_REGION"
```

Before live proof, verify the deployed API ID/Lambda ARN and region from
stack outputs, timestamp the real HTTPS `/health` status/body, confirm no
static credential in package/config, and rerun local mode. The signed smoke
uses standard AWS credential-provider resolution and refuses redirects; it
does not invoke Bedrock or S3. The result proves reachability, not quotation
workflow durability or model/storage readiness.

## Failure, recovery, and accepted limitation

On a failed update, inspect the stack's event status through read-only AWS
commands. For a previously working deployment, retain its artifact object
key and template revision; redeploy that known-good repository revision and
key with the same bounded `cloudformation deploy` procedure. Do not delete
resources or overwrite the earlier artifact as an implicit rollback.
The human selected KEEP DEPLOYED for the initial stack and artifact bucket.
Resource deletion is not part of this local remediation.

C13's `LocalQuoteStore` is process-local. Lambda cold starts/replacements or
different execution environments can lose or divide review state. Neither
reserved concurrency of one nor provisioned concurrency makes it durable.
Therefore a full live analyze→draft→approve→export workflow is not required
for C15; any one-environment success would be supplementary only. C15 does
not add a database, sticky sessions, or a production-safe state guarantee.
