# RL-10 — Sora About page preview

28 November 2026, Asia/Kolkata. Agent codex-redline-about. Owner liked Sora in the shortlist and requested an About page sample. Base task branch commit ffde7374e76e22db6bd1f13fa7cfa767a7ed8d87. Scope: new tasks/RL-10-about-story/v2/sora/ only. Issue #10 and draft PR #11 remain the review ledger. This is not approval to change production or declare a final global type system.

Sora is applied throughout headings, paragraphs, navigation and controls. Weighted Roun Groun and CEPA logo artwork, serious content, pure black, circuitry, hover illumination, flag, architecture panels and reading progress are preserved. Existing font sizes and weights are retained. Glyph metrics naturally change text wrapping and content-driven heights. One responsive adjustment puts navigation on a second row at 801–1000px to prevent Sora's wider text from splitting the tablet header labels and pause control. Main section/card layout is unchanged.

Font: licensed Sora variable upright Latin/punctuation/rupee WOFF subset from the preceding font chooser, originally Google Fonts ofl/sora. Source https://github.com/google/fonts/tree/main/ofl/sora and designer https://github.com/sora-xor/sora-font . Weight axis 100–800. Full OFL notice embedded in HTML and font-assets.json. Prior About versions and the uploaded Crimson ZIP remain unchanged.

Actual checks: baseline v2 SHA guard passed; body and JavaScript are byte-for-byte identical to v2. Desktop visual review confirmed Sora and no horizontal overflow (1348/1348). Phone document widths 375/375; computed Sora family, 16px body and 32px H1; visual wrapping checked. Tablet widths 805/805; header wrapping issue caught and corrected, computed nowrap labels and 135px two-row header verified. No broader animation regression or performance benchmark is claimed for this font-only sample; unchanged scripts retain v2's documented checks and GPU verification limit.

Final RG-REDLINE-About-Us-Sora.html: 177,604 bytes. SHA-256 51c56b50cae6b002493d2bed7a7898ad1c36fc2361de01d357714f29fa9d284d. Embedded font SHA-256 b78339c6c035286749a2ce94a6875ee97e8dfad558f039af3e8a0583b55a1501. Open HTML directly, with no external asset requests. Build with `python build.py` from this repository folder; parent v2 HTML is the guarded input. Elsewhere pass `--base /path/to/RG-REDLINE-About-Us-v2.html`.

No live WordPress page/settings, homepage, shared brand document, customer/order/review data or other agent work changed. Recovery: discard isolated Sora sample. Editing claim released at checkpoint; issue remains open for review.
