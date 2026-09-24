# GIT_WORKFLOW.md — AI Quotation Intelligence System

## 1. Role of This File

This file defines how approved Card work is versioned and delivered through Git and GitHub once Git exists.

It owns branch, staging, commit, push, pull-request, merge, rollback, Git-evidence, and human-approval rules for delivery. It does not own project architecture, Card identity/order, Card authorization, implementation scope, evidence policy, or deployment policy beyond the Git delivery boundary.

Ownership:
- PROJECT_CONTROL.md: live Git/Card state once Git exists
- QUOTATION_ENGINEERING_HARNESS.md: execution sequence and approval checkpoints
- QUOTATION_CARD_EVIDENCE_MAP.md: actual Git evidence
- GIT_WORKFLOW.md: Git/GitHub delivery policy

## 2. Runtime Git State and Historical Evidence

Project path: /Users/jo.soroush/john/my_projhects/AI_QUOTATION_INTELLIGENCE_

Current branch, HEAD, remote, upstream, synchronization, and working-tree
state are runtime Git facts. Query Git directly; PROJECT_CONTROL.md is the
sole owner of live operational state.

Historical C01 delivery evidence is recorded in the Evidence Map:
C01 implementation commit, PR #1, and its merge commit. Governance hardening
was delivered through PR #2. These are historical events, not a current
delivery-status ledger.

This is policy for future Git use. It does not initialize Git or authorize any Git write action.

## 3. Core Delivery Principle

One Card → One Branch → Bounded Changes → Validation → Evidence → READY_FOR_DELIVERY → one GIT_DELIVERY_APPROVAL → git add → verify index identity → commit → verify committed-tree identity → push → PR → merge → final reconciliation → FINAL_CARD_STATE_CONSISTENCY_GATE PASS → Card COMPLETE → Active Card NONE → STOP

Each transition is explicit. Do not automatically perform the next Git action.

## 4. Card / Branch Model

The default model is one implementation Card per dedicated branch.

Recommended identity-based names:
- card/v1-c01-repository-baseline
- card/v1-c02-domain-models
- card/v1-c03-synthetic-historical-data

Continue the same pattern for later Roadmap Cards. An approved alternative may be used when recorded in PROJECT_CONTROL.md.

Rules:
- the branch corresponds to exactly one active Card
- unrelated work is not mixed into a Card branch
- future-Card implementation is prohibited
- direct implementation on the default branch is prohibited by default
- a shared branch is not reused across unrelated Cards

If branch and Card do not match:
CARD_BRANCH_MISMATCH
STOP

## 5. Main / Default Branch

The default branch represents accepted project history.

By default:
- do not implement directly on the default branch
- do not rewrite default-branch history
- do not force push the default branch
- do not merge unvalidated Card work
- do not merge without a valid GIT_DELIVERY_APPROVAL and required checks

Repository initialization and default-branch setup belong to the authorized repository-baseline Card. They must not be performed during governance migration.

## 6. Pre-Write Git Inspection

Once Git exists and before implementation, inspect:
- git status --short
- current branch
- HEAD
- remote configuration
- upstream
- untracked files
- modified files

Confirm that the current branch matches the active Card and that unrelated work can be safely isolated.

If Git does not exist, record NOT_AVAILABLE; never invent Git state. Do not modify during inspection.

Unexpected dirty state:
UNEXPECTED_WORKTREE_STATE
STOP

Do not delete or overwrite unrelated user work.

## 7. Start Commit

At Card start, once Git exists, record:

Branch:
Start Commit:
Initial Working Tree State:

The Start Commit identifies the baseline before Card implementation. Never invent commit hashes.

If a reliable start point cannot be established:
GIT_BASELINE_UNVERIFIED
STOP

## 8. Staging Rules

Before staging, review the actual diff and stage narrowly. Stage only files belonging to the authorized Card.

Never stage:
- .env or secret files
- credentials, keys, or tokens
- unrelated changes
- editor or cache artifacts
- large generated artifacts unless intentionally versioned
- real confidential customer or company data

If sensitive data is detected:
SECRET_OR_SENSITIVE_DATA_DETECTED
STOP

Do not commit first and clean later.

## 9. Diff Review

Before requesting GIT_DELIVERY_APPROVAL, review:
- git diff
- git diff --staged
- git status

Verify scope, Card ownership, absence of future-Card leakage, accidental deletions, secrets, confidential data, generated noise, unrelated refactors, and unexpected governance/evidence changes.

If the diff does not match authorized scope:
CARD_SCOPE_MISMATCH
STOP

## 10. Validation Before GIT_DELIVERY_APPROVAL

Git delivery is not a substitute for validation. Before requesting GIT_DELIVERY_APPROVAL, required focused validation must have run, Evidence and Learning must be current, ROADMAP_ALIGNMENT_GATE must PASS, CARD_QUALITY_GATE must PASS, and the Exit Gate must be PROVEN.

For future independently audited candidates, the verifier's PASS must name
the exact content identity from `scripts/candidate_identity.py compute`.
Before requesting delivery approval, recompute it using the same audited base
revision and run `scripts/candidate_identity.py verify --base-ref <BASE_SHA>
--expected <AUDITED_SHA256>`. A nonzero result or a missing independent PASS
blocks delivery. The identity covers the base revision, changed and new paths
(including visible untracked files), deletions, modes, and exact content
hashes. The current branch is reported as provenance but is not hashed.
Filename equality alone is not sufficient.

Applicable evidence includes focused tests, relevant regression, Card evaluation, Exit Gate progress, known failures, known limitations, and an Evidence Map update.

If required validation failed:
REQUIRED_VALIDATION_FAILED
STOP

Do not commit a falsely claimed passing state.

## 11. GIT_DELIVERY_APPROVAL

After the Card reaches READY_FOR_DELIVERY, one explicit human GIT_DELIVERY_APPROVAL authorizes the normal delivery chain for the exact validated Card state:

- `git add`
- commit
- push
- PR creation
- merge

Before requesting approval, report the Card, branch, HEAD/start commit, validated file set and diff, validation results, Evidence Map and Learning Log state, ROADMAP_ALIGNMENT_GATE, CARD_QUALITY_GATE, Exit Gate, and unrelated-file check.
Also report the audited identity, current delivery identity, and PASS result
from their mechanical comparison. The independent verifier's audit record is
the source of the expected identity; the implementer cannot certify it.
If the audited checkout is not on the required delivery branch, identify the
planned branch transition in the approval request. After that authorized
transition, recompute and compare the same content identity before staging.
The base revision and complete candidate manifest must remain unchanged.

GIT_DELIVERY_APPROVAL does not authorize force push, history rewrite, destructive Git actions, architecture or scope changes outside the Card contract, sensitive credential use, unrelated external actions, or deployment/release unless separately authorized and owned by the Card.

Without GIT_DELIVERY_APPROVAL:
REQUIRED_APPROVAL_MISSING
STOP

## 12. Commit Rules

Each commit should be scoped, coherent, reviewable, attributable to the active Card, and free of secrets or unrelated work.

Recommended message style:
- V1-C01: establish repository baseline
- V1-C04: add deterministic quote calculations
- V1-C08: add Bedrock provider adapter

These are guidance, not authorization or a mandatory format. Avoid vague messages such as update, changes, or fix stuff. Do not amend or rewrite shared commits without explicit approval.

## 13. Post-Commit Verification

After an approved commit, verify HEAD changed as expected, the commit exists,
it contains intended files, and the working-tree state is understood. Before
push, run `scripts/candidate_identity.py verify --base-ref <BASE_SHA>
--expected <AUDITED_SHA256> --require-committed`. This reads the committed
HEAD tree and compares its identity with the audited candidate; commit success
or a clean worktree is not proof of exact committed content. A mismatch is
STOP before push, PR, or merge.

For delivery evidence, resolve the delivery commit from the actual Card branch
or fetched remote/PR reference and verify the Git object before recording it.
Confirm the commit subject and Card context, record the exact observed hash,
and keep the delivery commit distinct from the later merge commit. Do not
manually invent or approximate immutable hashes, and do not require every
historical object to remain reachable from current `main` forever.

Record immutable event hashes in the Evidence Map when observed. Do not record
mutable current HEAD, current branch, or current working-tree values as live
state in tracked governance files; query those facts from Git.

## 14. GIT_DELIVERY_APPROVAL Invalidation and Delivery Rules

GIT_DELIVERY_APPROVAL is valid only for the exact validated delivery state.
An explicitly planned move of the unchanged audited candidate to its approved
delivery branch is a workflow transition, not a candidate-content change.
Recompute and verify the audited identity on that branch before staging; a
mismatch, different base, unexpected branch, or changed file set is STOP.
After approved narrow staging and before commit, repeat the identity
comparison with `--require-staged`. The verifier constructs the candidate
directly from base tree versus Git index blobs and modes, using the same
content identity as the audited worktree candidate. It requires both worktree
and index identities to match the audited identity, and fails on candidate
skip-worktree or assume-unchanged flags. It does not trust porcelain diff
visibility, clean-filtered worktree comparisons, or `core.fileMode` settings
as staged-content proof. An extra staged change, missing candidate entry, or
visible untracked file fails the exact index comparison. After commit, the
same identity is constructed from base tree versus committed HEAD tree and
must match before push. Any candidate-content change after independent PASS invalidates that PASS and
requires independent re-verification, regardless of whether the implementer
considers the change substantive. This rule applies before delivery approval
as well as after it.

If any of the following occurs after approval, the approval is invalidated immediately and execution stops:

- implementation files change;
- candidate governance evidence changes before commit;
- the staged candidate diff changes;
- tests are rerun and fail;
- CARD_QUALITY_GATE becomes FAIL;
- the Exit Gate becomes NOT_PROVEN;
- the branch changes unexpectedly; or
- unrelated files enter the delivery set.

Outcome-only final reconciliation is an exception after the approved delivery:
it may record only observed delivery results, historical hashes, completion
evidence, completed-card state, and the Active Card transition to NONE. It must
not change implementation, scope, contract, validated payload, or unrelated
policy, and does not invalidate the consumed approval. Any other pre-delivery
candidate-content change invalidates the audited identity and approval; there
is no implementer-granted minor-edit exception.

Record `GIT_DELIVERY_APPROVAL: INVALIDATED`, preserve the reason, revalidate the Card state, and obtain a new approval before delivery.

By default:
- push only the active Card branch
- never use force push, --force, or --force-with-lease unless explicitly approved for justified recovery
- do not push secrets or unrelated branches
- verify the remote target
- do not implement or edit after approval without invalidation and re-approval

After each normal delivery action, verify the actual result. A failed check, changed diff, wrong branch, hidden unrelated file, or merge conflict is a STOP condition; do not continue automatically.

## 15. Pull-Request Content

PR creation is covered by the single GIT_DELIVERY_APPROVAL when the exact validated delivery state remains unchanged.

Before creating one, Card scope must be stable, required validation and evidence must be current, and the diff must be reviewable.

A Card PR should state:
Card:
Engineering Goal:
Scope:
Files / Components:
Validation:
Evaluation:
Commercial/Data Invariants:
AI/Provider Validation where relevant:
Security Validation:
Known Limitations:
Exit Gate State:
Evidence:
Human Approval Requirements:

Do not claim a passing result that was not executed. A PR does not make a Card complete.

## 16. Merge Rule

Merge is covered by the single GIT_DELIVERY_APPROVAL when the exact validated delivery state remains unchanged. Auto-merge is not enabled by default.

Before merge, verify review state, CI state if CI exists, required Card validation, Evidence Map, Exit Gate, CARD_QUALITY_GATE, known limitations, and conflicts.

The merge strategy may be selected intentionally once repository policy exists. Possible strategies include merge commit, squash merge, or rebase merge. This file does not authorize one automatically.

After merge, verify the actual merged state and record evidence. Do not infer merge success from a request or interface action alone.

## 17. Card Completion and Git

READY_FOR_DELIVERY means implementation and validation are complete, Evidence and Learning are current, ROADMAP_ALIGNMENT_GATE and CARD_QUALITY_GATE are PASS, the Exit Gate is PROVEN, and normal Git delivery is pending.

A Card is complete only when its contract is satisfied, required validations pass, the Exit Gate is proven, evidence is current, the Learning Record is complete, CARD_QUALITY_GATE is PASS, PROJECT_CONTROL.md is reconciled through outcome-only final reconciliation, one valid GIT_DELIVERY_APPROVAL covered the exact delivery state, the normal commit/push/PR/merge chain completed successfully, any required reconciliation commit/push completed, runtime Git state is verified, and FINAL_CARD_STATE_CONSISTENCY_GATE is PASS.

Then:
Card COMPLETE
Active Card NONE
STOP

The next Card requires separate approval.

## 18. Rollback / Recovery

Prefer safe, additive recovery. Do not use destructive Git commands casually.

By default avoid:
- git reset --hard
- git clean -fd
- force push
- history rewrite
- mass checkout overwrite
- branch deletion with unverified work

If destructive recovery appears necessary:
DESTRUCTIVE_GIT_ACTION_REQUIRED
STOP

Request explicit human approval. Prefer a revert, new corrective commit, restoration of proven-safe files, or a bounded recovery branch according to verified state.

## 19. Unrelated User Work

Never delete, overwrite, stage, commit, revert, or normalize unrelated user changes merely to obtain a clean tree.

If unrelated work exists, record it and exclude it from Card scope. If safe isolation is impossible:
UNRELATED_WORK_CONFLICT
STOP

## 20. Secrets and Confidential Data

Never commit AWS access key IDs, AWS secret access keys, session tokens, API keys, passwords, private certificates, secret .env values, real confidential quotation data, or real confidential company/customer pricing.

If discovered:
SECRET_OR_SENSITIVE_DATA_DETECTED
STOP

Do not print secret values in logs or reports.

## 21. Generated Files

Generated output should be versioned only when the project intentionally treats it as source, evidence, or an artifact.

Examples that may usually remain untracked, depending on future policy:
- temporary Excel outputs
- cache files
- coverage artifacts
- local logs
- Python cache
- virtual environments

The exact .gitignore policy belongs to C01. Do not silently decide it during governance migration.

## 22. Git Evidence

Future Card evidence should distinguish:

Git Initialized:
Branch Created:
Base Branch/Commit:
Start Commit:
Commit Created:
Exact Delivery Commit SHA:
Push Completed:
Remote Branch:
PR Created:
PR ID/URL:
Merge Completed:
Exact Merge SHA:
Exact Changed File Set:
Exact Validation Commands and Observed Results:
Audited Candidate Identity: independent verifier's SHA-256 result
Delivery Candidate Identity: recomputed SHA-256 result
Identity Match: PASS / FAIL
Final Working Tree:

Each field must reflect actual observed state. Unknown values are NOT_VERIFIED or NOT_AVAILABLE; never infer them.
Query runtime Git facts directly; do not duplicate mutable HEAD values in a
tracked ledger. Keep the verifier's identity in the independent audit record
until pre-delivery comparison, not in a candidate file where it would change
the hash recursively. Record compared identities as observed delivery
provenance when the owning evidence record is updated after delivery.
Post-approval changes also follow section 14.
Reproducible source, tested artifact identity, and traceable delivery are
adopted provenance principles. Full SLSA attestation infrastructure is not
justified now; SBOM generation remains risk-triggered for a later Card.

## 23. CI Boundary

If CI exists later, its results are evidence. If CI does not exist, do not claim CI passed.

Local tests and CI tests are distinct evidence. A green CI status does not replace Card-specific Exit Gate proof.

## 24. GitHub Boundary

GitHub is a delivery platform, not project truth.

PR open != accepted
PR merged != Card COMPLETE
issue closed != implementation verified
remote branch exists != local branch clean

PROJECT_CONTROL.md is authoritative for live project state. The Evidence Map
is authoritative for verified implementation and delivery evidence.

## 25. Approval Matrix

Explicit human approval is required for:
- Git initialization when Card scope requires it
- creating or changing the default branch where consequential
- GIT_DELIVERY_APPROVAL for normal Card delivery
- force push
- history rewrite
- destructive reset or clean
- branch deletion with meaningful work
- release tag
- deployment or release action

Read-only Git inspection does not require approval. Routine non-destructive editing inside an authorized Card follows the Engineering Harness.

## 26. Current Project Posture

Current posture is owned by PROJECT_CONTROL.md. This file defines the policy
and process only. Historical C01 completion evidence remains in the Evidence
Map; V1-C02 requires separate human authorization.

## 27. Final Git Rule

ONE CARD → ONE BRANCH.
INSPECT BEFORE WRITE.
REVIEW DIFF BEFORE STAGE.
VALIDATE BEFORE READY_FOR_DELIVERY.
ONE GIT_DELIVERY_APPROVAL → COMMIT → PUSH → PR → MERGE.
INVALIDATED APPROVAL → STOP → REVALIDATE → NEW APPROVAL.
NO SECRETS.
NO FORCE PUSH BY DEFAULT.
NO UNRELATED WORK.
MERGE != COMPLETE.
CARD COMPLETE → ACTIVE CARD NONE → STOP.
NEXT CARD → NEW HUMAN APPROVAL.

## 28. Validation Checklist

Check this policy for:
- AI Quotation Intelligence project identity
- no legacy domain terminology
- current Git state reconciled with PROJECT_CONTROL.md
- no Git initialization during governance migration
- one Card / one branch
- direct default-branch implementation prohibited by default
- pre-write Git inspection
- start commit recording
- diff and narrow staging review
- secret protection
- validation before commit
- one GIT_DELIVERY_APPROVAL for the normal commit/push/PR/merge chain
- approval invalidation on material post-approval change
- no force push by default
- safe recovery
- protection of unrelated user work
- Git evidence distinctions
- merge not equaling Card completion
- Card completion stopping the workflow
- separate approval for the next Card
- C01 completion and consumed GIT_DELIVERY_APPROVAL are historical Evidence Map facts

No checklist item authorizes a Git write action.
