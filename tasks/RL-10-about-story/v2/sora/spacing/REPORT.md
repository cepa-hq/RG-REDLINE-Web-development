# RL-10 — Sora heading spacing revision

28 November 2026, Asia/Kolkata. Agent codex-redline-about. Owner found Sora headings congested. New isolated sample at tasks/RL-10-about-story/v2/sora/spacing/, baseline task branch commit 648979e8a8dd6a3fbcec1b642e9cda5f9a0c505d. Prior Sora sample preserved. No live website or global brand decision.

The earlier heading rule inherited -0.035em letter spacing and 1.22 line height from the initial design. Changed only this shared heading declaration to +0.012em tracking and 1.32 line height. Font size, weight, body text, content, logos, cards, animation and all JavaScript are unchanged. Text naturally occupies more width and height.

Actual browser checks: desktop computed H1 remains Sora 38px, now 0.456px letter spacing and 50.16px line height; visual review passed. Phone content width 375px has client/scroll widths 375/375, H1 remains 32px with 0.384px letter spacing and 42.24px line height; visual review passed. Tablet client/scroll widths 805/805; visual review passed. No additional functionality tests were needed because this changes one typography declaration only.

Standalone HTML 177,603 bytes; SHA-256 4918d619fb492e2b344342081888cfca83dda3bfd23330da72b25dea58ad8bb2. Baseline Sora HTML SHA-256 51c56b50cae6b002493d2bed7a7898ad1c36fc2361de01d357714f29fa9d284d. Buildless HTML contains full source, font and existing licences. To reproduce, replace the sole heading declaration `font-weight:650;line-height:1.22;letter-spacing:-.035em` with `font-weight:650;line-height:1.32;letter-spacing:.012em` in that baseline.

No WordPress, shared files, customer/order/review data or other agent work changed. Recovery: discard this isolated spacing comparison. Editing claim released at Git checkpoint; issue #10 remains open for owner review.
