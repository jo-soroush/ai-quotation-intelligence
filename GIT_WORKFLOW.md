# GIT_WORKFLOW.md — AI Quotation Intelligence System

## 1. Role of This File

This file defines how approved Card work is versioned and delivered through Git and GitHub once Git exists.

It owns branch, staging, commit, push, pull-request, merge, rollback, Git-evidence, and human-approval rules for delivery. It does not own project architecture, Card identity/order, Card authorization, implementation scope, evidence policy, or deployment policy beyond the Git delivery boundary.

Ownership:
- PROJECT_CONTROL.md: live Git/Card state once Git exists
- QUOTATION_ENGINEERING_HARNESS.md: execution sequence and approval checkpoints
- QUOTATION_CARD_EVIDENCE_MAP.md: actual Git evidence
- GIT_WORKFLOW.md: Git/GitHub delivery policy

## 2. Current Git State

Project path: /Users/jo.soroush/john/my_projhects/AI_QUOTATION_INTELLIGENCE_

Git Repository: YES
.git Present: YES
Current Branch: main
HEAD: 9e44dac3d69740b2f415d9ec728626553bc4e933
Remote: origin → https://github.com/jo-soroush/ai-quotation-intelligence.git
Upstream: origin/main
Working Tree: PROJECT_CONTROL.md modified; no other modifications observed
Commits: governance baseline commit present
Push: governance baseline pushed; future pushes require explicit approval
PR: NONE
Merge: NONE

This is policy for future Git use. It does not initialize Git or authorize any Git write action.

## 3. Core Delivery Principle

One Card → One Branch → Bounded Changes → Validation → Evidence → Human Approval → Commit → Human Approval → Push → Human Approval → PR → Human Approval → Merge → Reconcile PROJECT_CONTROL → Card COMPLETE → STOP

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
- do not bypass human merge approval

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

Before requesting commit approval, review:
- git diff
- git diff --staged
- git status

Verify scope, Card ownership, absence of future-Card leakage, accidental deletions, secrets, confidential data, generated noise, unrelated refactors, and unexpected governance/evidence changes.

If the diff does not match authorized scope:
CARD_SCOPE_MISMATCH
STOP

## 10. Validation Before Commit

Commit is not a substitute for validation. Before requesting commit approval, required focused validation must have run and Card evidence must be current.

Applicable evidence includes focused tests, relevant regression, Card evaluation, Exit Gate progress, known failures, known limitations, and an Evidence Map update.

If required validation failed:
REQUIRED_VALIDATION_FAILED
STOP

Do not commit a falsely claimed passing state.

## 11. Commit Approval

Explicit human approval is required before every commit.

An agent may prepare proposed files, a diff summary, a validation summary, and a proposed commit message, but must not commit without explicit approval.

Without approval:
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

After an approved commit, verify HEAD changed as expected, the commit exists, it contains intended files, and the working-tree state is understood.

When the active process permits updates, record the actual commit hash in PROJECT_CONTROL.md and QUOTATION_CARD_EVIDENCE_MAP.md. Never fabricate a hash.

## 14. Push Approval and Rules

Commit approval does not imply push approval.

Before push, report:
Branch:
Commit:
Remote:
Upstream:
Working Tree:
Validation State:
Known Limitations:

Explicit human approval is required. Without it:
REQUIRED_APPROVAL_MISSING
STOP

By default:
- push only the active Card branch
- never use force push, --force, or --force-with-lease unless explicitly approved for justified recovery
- do not push secrets or unrelated branches
- verify the remote target

After push, verify upstream state where possible and record actual push evidence.

## 15. Pull-Request Approval and Content

Push approval does not imply pull-request approval. Explicit human approval is required to create a PR.

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

## 16. Merge Approval and Rule

PR creation does not imply merge approval. Explicit human approval is required for merge; auto-merge is not enabled by default.

Before merge, verify review state, CI state if CI exists, required Card validation, Evidence Map, Exit Gate, CARD_QUALITY_GATE, known limitations, and conflicts.

The merge strategy may be selected intentionally once repository policy exists. Possible strategies include merge commit, squash merge, or rebase merge. This file does not authorize one automatically.

After merge, verify the actual merged state and record evidence. Do not infer merge success from a request or interface action alone.

## 17. Card Completion and Git

Merge alone is not Card completion. A Card is complete only when its contract is satisfied, required validations pass, the Exit Gate is proven, evidence is current, the Learning Record is complete, CARD_QUALITY_GATE is PASS, PROJECT_CONTROL.md is reconciled, and required approved Git delivery is complete.

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
Start Commit:
Commit Created:
Commit Hash:
Push Completed:
Remote Branch:
PR Created:
PR ID/URL:
Merge Completed:
Merge Commit:
Final Working Tree:

Each field must reflect actual observed state. Unknown values are NOT_VERIFIED or NOT_AVAILABLE; never infer them.

## 23. CI Boundary

If CI exists later, its results are evidence. If CI does not exist, do not claim CI passed.

Local tests and CI tests are distinct evidence. A green CI status does not replace Card-specific Exit Gate proof.

## 24. GitHub Boundary

GitHub is a delivery platform, not project truth.

PR open != accepted
PR merged != Card COMPLETE
issue closed != implementation verified
remote branch exists != local branch clean

Evidence and PROJECT_CONTROL.md remain authoritative for project state.

## 25. Approval Matrix

Explicit human approval is required for:
- Git initialization when Card scope requires it
- creating or changing the default branch where consequential
- commit
- push
- PR creation
- merge
- force push
- history rewrite
- destructive reset or clean
- branch deletion with meaningful work
- release tag
- deployment or release action

Read-only Git inspection does not require approval. Routine non-destructive editing inside an authorized Card follows the Engineering Harness.

## 26. Current Project Posture

Verified current posture:

Git Repository: YES
Implementation: NOT_STARTED
Active Card: V1-C01 — Repository Baseline
C01 Authorized: YES

Therefore no commit, push, PR, merge, or other consequential Git delivery action is currently authorized. GIT_WORKFLOW.md remains governance policy while C01 implementation has not started.

## 27. Final Git Rule

ONE CARD → ONE BRANCH.
INSPECT BEFORE WRITE.
REVIEW DIFF BEFORE STAGE.
VALIDATE BEFORE COMMIT.
COMMIT REQUIRES APPROVAL.
PUSH REQUIRES NEW APPROVAL.
PR REQUIRES NEW APPROVAL.
MERGE REQUIRES NEW APPROVAL.
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
- separate approval for commit, push, PR, and merge
- no force push by default
- safe recovery
- protection of unrelated user work
- Git evidence distinctions
- merge not equaling Card completion
- Card completion stopping the workflow
- separate approval for the next Card
- C01 authorized; implementation remains not started

No checklist item authorizes a Git write action.
