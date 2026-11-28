# Page 14 deployment — before checkpoint

Owner explicitly authorised Black Brushed Radar v3 as the REDLINE homepage with options included. Target verified https://rg-redline.com; static front page14 is published, template page-no-title. Baseline content hash c037fcfadc3602afa73bb9d3d5e0f8988ae0785f981a00847eaafcfc04b2744e. Current root anonymously serves noindex,nofollow. No settings change is planned.

Source artifact v3 hash c6918807f23789ff691ae06aa9813b5dac6bbbdb126a66d6e0140395ae2e7fae. Adapted one core/html block hash 75f06db37a38f168ef3e6bec2243365c8464572d07d35977f4874aeaccf5fb06. Remove document/head wrappers and keep font license. Scope standalone html/body selectors to page 14; retain existing page-only theme-shell spacing/hiding integration. Preserve all UI options and the weighted wordmark.

Files before-page14.html and homepage-block.html are exact raw-content before/after checkpoints (no implicit newline appended). Native WP writer lacks an atomic compare-and-swap guard; release writes are serialised and the page hash will be reread immediately before saving.

Scoped recovery: reread page14 and coordinate if later changes exist, then restore only before-page14.html if needed. Keep site indexing and commerce visibility unchanged. This before export is historical recovery evidence and contains the older superseded thin logo; it is not an approved reusable REDLINE identity asset. Do not copy it into new designs.

Validation/deployment report follows after actual smoke checks. No other page, theme template, plugin or site setting is owned by this release.
