# RL-5 homepage visibility follow-up — 28 November 2026

Owner reported the homepage link did not show the design. Cause: the preserved WooCommerce Coming soon screen applied to the entire website, so unauthenticated visitors could not view page 14.

Scoped correction: native WooCommerce Settings > Site visibility > **Apply to store pages only** changed from unchecked to checked. Coming soon remains selected; Live was not selected. This makes non-store pages including the homepage viewable, while store pages keep the holding screen. Private-link option and admin badge left unchanged. The native save confirmation was observed and the checkbox read back checked. The connector's site-visibility settings endpoint returned an empty list, so native UI was used.

Indexing: global WordPress search discouragement remains enabled. An anonymous HTTP GET to the exact root https://rg-redline.com/ returned 200, the #rl-redline-home root, H1 GO BEYOND. COME BACK., and robots meta noindex,nofollow after propagation. A query-string check returned the same. Initial immediate anonymous check still showed the old screen; a later request showed the concept. The cache purge tool reported nothing cleared, and no broad cache flush was run. No claim is made that the purge caused the fix.

Page content, homepage assignment, template, plugins, payment/checkout configuration and other agent assets were not edited. Logged-in browser rendering verified and marked for owner review. No search submission.

Rollback: re-read current visibility controls and, if appropriate, uncheck only Apply to store pages only and save. Preserve indexing discouragement. No atomic option guard was available; this task serialized the native write after checking active tasks and live state.
