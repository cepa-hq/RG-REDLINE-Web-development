# Multi-agent coordination workflow

GitHub Issues are the current task ledger. A shared editable ACTIVE_WORK file is not a lock and is not the authority for ownership.

## Lifecycle

**Proposed → Claimed → In progress → Review → Released/Completed**, with **Blocked** or **Handed off** recorded explicitly when needed. Use Issue comments/headings if labels or a project board are unavailable; these documents do not create labels or configure a board.

1. **Discover:** read root instructions, brand/architecture documents and relevant implementation instructions. Inspect open Issues/PRs, branches, recent commits and the exact live resources when relevant.
2. **Plan:** open a task Issue using [the plan template](TASK_PLAN_TEMPLATE.md). Include agent ID, resource/file ownership, dependencies, exclusions, base revision, branch, tests and rollback.
3. **Coordinate:** compare overlap by exact file, WordPress ID, option key, route and shared component. For overlapping active work, agree scope/sequence/interface with the affected owner in both Issues before editing that resource.
4. **Isolate:** own branch/worktree for each task. A branch isolates source only; do not treat it as a WordPress deployment sandbox.
5. **Checkpoint:** record after a meaningful milestone, before/after each deployment, on scope change, on blockers, and before ending a work session.
6. **Review:** submit a PR and real validation evidence. Separate design approval, merge state, staging deployment and production deployment.
7. **Release:** one release owner per target environment; use [the release checklist](RELEASE_CHECKLIST.md). Apply authorization already given within its scope.
8. **Complete/handoff:** use [completion](COMPLETION_TEMPLATE.md) or [handoff](HANDOFF_TEMPLATE.md). Close only after the applicable authorized review/release has finished.

## Naming and storage

- Task ID: RL-<Issue number>.
- Branch: agent/<agent-id>/rl-<issue-number>-<slug>.
- Task artifacts: tasks/RL-<issue-number>-<slug>/.
- Suggested artifact names: PLAN.md, CHECKPOINT.md, REPORT.md; source/export files and scoped patches beside them.
- Shared approved decisions: versioned documents under docs/, changed through their own declared task.
- Pull requests: link the task Issue, describe behavior and scope, list actual tests/limitations and deployment state.

Do not continuously rewrite another task's checkpoint. Link related tasks rather than copying their outdated content.

## Practical resource claims

A task might claim page ID 42, /about/, its own page template and /assets/pages/about/. It does not thereby claim global.css, the header, payment settings or a shared page-render plugin.

If deployment uses a shared plugin ZIP, two page owners must not each ship complete ZIPs based on different versions. A designated integrator combines reviewed changes against the current baseline and records the exact deployment artifact.

A release claim identifies environment, resources, release owner and start/end state in a dedicated Issue comment. Acknowledge overlapping release requests and serialize them. Release stale claims through an explicit handoff/owner resolution, never by assuming inactivity means abandonment.

## Blocked ledger or access

If GitHub writes are unavailable, prepare reviewable artifacts and explain the specific access blocker. Do not change shared website resources while ownership cannot be coordinated. Owner-approved alternatives must be explicit and later reconciled into this ledger.

## Enforcement limits

These are cooperative rules, not technical locks. Branch protection, required reviews and CI enforcement are not configured by creating these files. No tool can see every unpushed/local change. Stop and coordinate when an unexpected upstream or live-state difference appears.

