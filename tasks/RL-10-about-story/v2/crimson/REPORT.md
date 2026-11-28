# RL-10 — Crimson Pro font comparison

28 November 2026, Asia/Kolkata. Agent: codex-redline-about. Source-only review sample; no deployment. Related issue #10 and draft PR #11. Base task commit 7810d340d6d4c1e9db88979394513c9d533b5672. Scope is only tasks/RL-10-about-story/v2/crimson/.

The owner requested the exact v2 page with their uploaded font. All text now uses Crimson Pro, including headings, body, navigation and controls. Font sizes, weights, layout rules, copy, logos, circuitry, card lighting, flag, reading progress and JavaScript are preserved. Different glyph metrics naturally change line wrapping and some content-driven card heights. The previous v2 sample is preserved.

Font provenance: uploaded CrimsonPro_Complete.zip, Library ID libfile_741affb52d908191a2919a4d59c3ef6e. Embedded the original unmodified file CrimsonPro_Complete/Fonts/WEB/fonts/CrimsonPro-Variable.woff2, 85,944 bytes. Source upright weight axis is 200–900, default 400. No italic face is needed because the original page uses upright typography. The supplied OFL notice is included unchanged inside the standalone HTML and font-assets.json. The uploaded ZIP is untouched.

Validation: original v2 SHA-256 guard passed. Build verifies the entire body and script remain byte-for-byte unchanged; only font declarations, fallback family and embedded font licence/payload change. Desktop visual inspection and computed family confirm RG Crimson; document client/scroll widths 1348/1348. Phone iframe 390px, content 375px: client/scroll widths 375/375, body 16px, H1 32px, Crimson family confirmed. Tablet iframe 820px, content 805px: client/scroll widths 805/805. Phone/tablet visual wrapping checked. Architecture panel selection and Pause/Resume smoke checks passed. Unchanged animations retain v2's prior checks and limitations, including WebGL being unavailable in the QA browser; no broader regression or speed benchmark is claimed for this font-only change.

Final HTML: RG-REDLINE-About-Us-Crimson-Pro.html, 250,530 bytes; SHA-256 03422725154c2f1198fa556d02a882df1da7bac2757d5f9c26d8e4576404e479. Open directly in a browser; the font and logos are embedded, with no external asset requests.

To reproduce in this repository, run `python build.py` from this folder. The default baseline is the parent v2 HTML. For a different filesystem location pass `--base /path/to/RG-REDLINE-About-Us-v2.html`; the expected baseline hash is checked before building.

No WordPress, live homepage, shared brand document, other agent work or business data was modified. Recovery is discarding this isolated font comparison. Release the editing claim at the checkpoint and leave issue #10 open for owner review.
