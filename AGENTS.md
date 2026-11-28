# REDLINE agent ground rules

Applies to all brand, design, code, WordPress and WooCommerce work coordinated here. Owner instructions in the active task take precedence; preserve authorization already given rather than requesting it repeatedly.

## REDLINE logo identity — owner-confirmed 28 November 2026

REDLINE must always use the **fat/weighted Roun Groun wordmark**. The original thin parent-brand wordmark is prohibited for REDLINE, including previews, header/footer lockups, watermarks, social visuals and packaging. Do not substitute typed text or silently fall back to the thin mark when an asset is unavailable. Preserve the recognisable weighted letterforms and use an appropriate approved colour treatment. Refer to the logo section of docs/brand/BRAND_BRIEF.md; preserve source provenance and distinguish concept conversions from approved production masters.

## Read and verify

Read README.md, docs/brand/BRAND_BRIEF.md, docs/website/ARCHITECTURE.md and docs/coordination/README.md before work. Inspect the current default branch, active branches, open PRs and open task Issues. When implementation lives elsewhere, inspect that source and its instructions too. Re-read relevant state after a long interruption.

Confirm the target site/environment from live evidence before every website mutation. rg-redline.com is the owner-stated production domain; staging and access are not yet recorded. Do not assume a connector opened for roungroun.com or testarea.roungroun.com targets REDLINE.

## Declare ownership before editing

Create one visible task Issue, with an agent identifier, objective, base revision, exact scope, proposed branch, dependencies, validation and rollback. Use docs/coordination/TASK_PLAN_TEMPLATE.md. Record WordPress page/post/attachment IDs, routes, option keys, plugin paths and shared assets, not just vague page names.

Claim only the resources you need. A task Issue is a cooperative ownership declaration, not an atomic lock. Before writing, re-check active work and the current resource. If two tasks overlap, publish the agreed ownership split, sequence or interface contract in both Issues and receive the affected active owner’s acknowledgement before modifying their surface. Silence, elapsed time or an old checkpoint is not consent. Continue independent work while resolving overlap.

## Isolate source and shared surfaces

Use a unique branch per task: agent/<agent-id>/rl-<issue-number>-<short-description>. Do not work on the shared default branch or another agent’s branch. Use separate worktrees/checkouts if sharing a filesystem. Commit task-scoped changes; never force-push, reset, discard, revert or overwrite another agent’s work.

Header, footer, routing, design tokens, global CSS, bootstrap/render hooks, shared JS, plugin manifests, dependencies, schemas/APIs, cart/checkout/account code and SEO/tracking configuration are shared surfaces. Give each active shared surface one accountable owner. A page task does not automatically own its header/footer or shared plugins. Propose shared changes separately and publish the contract before dependent work.

Namespace page CSS/classes, assets and JS; scope selectors to the page root. Do not add body-wide style resets or load page scripts site-wide without a declared shared task. Keep equipment claims factual and sourced.

## WordPress writes need the same isolation

A Git branch does not isolate a WordPress database or a deployed plugin directory. Parallel page work is allowed only on separately claimed resources with compatible shared dependencies.

Before every save, re-read/export the exact current file, page revision or option values and compare with your recorded baseline. If an unexpected change is present, stop that write and coordinate; do not reapply an old full-page export. Preserve unrelated metadata and settings. Use a revision/hash guard where supported. If the platform has no atomic guard, record that limitation and serialize writers; do not claim a race is impossible.

Save a task-scoped before checkpoint, the proposed after artifact, a patch/diff or setting delta, target environment and a rollback before deployment. Keep sensitive backups outside this public repo. Avoid direct plugin-editor changes unless necessary and authorized; if used, export exact before/after source and reconcile it with the task branch.

Never replace an entire plugin, options record, page collection or staging database for a small change when a scoped update is possible. Do not change core WordPress/WooCommerce files, theme/rendering strategy, plugin activation, permalinks, payment, email, DNS or security settings outside explicit task scope.

## Authorization, release and data

Prepare and test all authorized reversible work without unnecessary permission stops. Website deployments and PR merges require owner authorization covering the target and scope; reuse existing authorization. Do not infer a production deployment from permission to make a concept or documentation.

Only one designated release owner may mutate a shared environment at a time. Record the release window, exact artifacts/commits, environment, dependencies and smoke checks in the Issue. A page release must not overwrite another task’s settings or customer records. Do not publish an entire staging database over production without an explicit, reviewed data migration plan protecting live orders, customers, reviews and environment-specific settings.

Do not merge other agents’ PRs or decide their conflicts unilaterally. Stop on unexplained upstream changes. Preserve an immediately usable scoped rollback; never use a full restore that discards later unrelated changes as a routine rollback.

## Checkpoints and truthful completion

Update the Issue at start, scope changes, deploy-before, deploy-after, blockers and handoff/completion. Include exact files/resource IDs, baseline/current commit, evidence, test outcomes and next action. Never claim unrun tests passed, proposals are approved, source commits are deployed, or GitHub rules prevent unannounced local edits.

Open a PR with the linked Issue and docs/coordination/COMPLETION_TEMPLATE.md details. Leave the Issue open until the authorized review/release process is complete. Mark blocked work explicitly and release/transfer ownership through a recorded handoff. Do not take over a stale claim without owner/active-agent resolution.

No secrets, personal customer data, private analytics, database dumps or unredacted operational logs in this public repository. Do not communicate with customers or publish brand content unless within the owner's explicit task.

## Limits of these rules

AGENTS.md, Issues and branches coordinate work; they do not technically lock WordPress or enforce reviews. Do not claim branch protection or required status checks are enabled unless verified in GitHub settings. Propose enforcement separately; do not change repository access/security settings under a content task.

