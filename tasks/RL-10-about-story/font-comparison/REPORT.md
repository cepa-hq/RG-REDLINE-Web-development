# RL-10 — REDLINE font shortlist and visual chooser

28 November 2026, Asia/Kolkata. Agent codex-redline-about. New isolated font-comparison/ folder only, based on task branch commit 2a0064406bd184e721c33ef9bee4c4199d4b58e8. Related issue #10 and draft PR #11. No brand selection, merge, live font change or deployment implied.

Owner requested beautiful, authoritative fonts suitable for REDLINE and web development after rejecting Crimson Pro. The design shortlist is Exo 2, Sora, Chakra Petch, Barlow Semi Condensed and Oxanium. Manrope is included as a clean paragraph pairing. Rankings and suitability descriptions are design judgments. My first recommendation is Exo 2 semibold headings with Manrope regular body; Sora is the polished alternative, Chakra Petch the stronger circuitry treatment. Oxanium has a more pronounced science-fiction/gaming association, so selective use is proposed.

The single HTML file contains editable heading text, family switching, 600/700 heading weight, uppercase toggle and Manrope-versus-selected-family body comparison. All fonts, code and weighted owner-reference wordmark geometry are embedded. No external asset requests, analytics or persistence. The Explore REDLINE element is explicitly part of the typography specimen, not a functional navigation button.

## Primary font sources

- Exo 2: https://github.com/google/fonts/tree/main/ofl/exo2 . Official description notes the technological/elegant direction, small-text use and variable family.
- Sora: https://github.com/sora-xor/sora-font and Google Fonts ofl/sora. Designer describes interface-oriented design.
- Chakra Petch: https://github.com/google/fonts/tree/main/ofl/chakrapetch . Family source/licence inspected.
- Barlow: https://github.com/jpt/barlow and Google Fonts ofl/barlowsemicondensed. Designer supplies multiple widths/weights.
- Oxanium: https://github.com/sevmeyer/oxanium . Designer describes square futuristic lettering.
- Manrope: https://github.com/google/fonts/tree/main/ofl/manrope . Family source/licence inspected.

All six family licences were fetched from their official Google Fonts source folders and included fully in the HTML. SIL OFL 1.1 permits website use subject to its terms: https://openfontlicense.org/ . No commercial licensing cost is introduced by these selections. Local comparison payload uses Latin/punctuation/rupee subsets converted to WOFF; full notices travel with the file. The uploaded Crimson ZIP is unchanged and not reused here.

Sora, Exo 2, Oxanium and Manrope source weight axes verified from font metadata: 100–800, 100–900, 200–800 and 200–800 respectively. Chakra Petch and Barlow Semi Condensed comparison embeds static 400/600/700 files. The preview only selects real embedded 400/600/700 weights. Production would load only a chosen family/pair in a suitable webfont format and relevant weights, rather than the whole chooser. No production speed benchmark is claimed.

## Actual checks

Generated artifact RG-REDLINE-Font-Comparison.html: 321,923 bytes. SHA-256 f87b3c7bc7565b9a1a25c8572748268d1161cd563fc6faa85d85948c24751af7. This buildless HTML is also the complete source, including font payload and notices; open it directly in a browser.

Browser visual inspection confirmed all five specimen styles. Font switching, editable heading, 700 weight, uppercase toggle and selected-font body pairing were verified through DOM readback and visible state. Phone Sora switching verified. Corrected a controls-grid overflow found in QA; final document client/scroll widths are 375/375 on phone and 1348/1348 on desktop. Phone preview paragraph 16px, heading 32px. Selector labels are visible and controls keyboard accessible; a browser automation exact-label lookup failed once, then ID-based semantic controls succeeded. This was not an application error.

No changes to About versions, WordPress resources, shared brand documents, other task files or business data. Recovery is discarding this isolated chooser. Editing claim released at Git checkpoint; issue #10 remains open for owner selection/review.
