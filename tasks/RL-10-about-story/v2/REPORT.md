# RL-10 — About Us, second concept

Status: sample ready for owner review. 28 November 2026, Asia/Kolkata. Agent: codex-redline-about. Continues issue #10 and draft PR #11. Base task commit: 690ed0c2fa7013b40ea04d168f3a9d74fcb8e31b. Claim limited to tasks/RL-10-about-story/v2/. Previous concept preserved.

## Owner clarification

Seriousness applies to the information. The visual treatment and interactions should be expressive, stylish and fun. The owner rejected the grey gradient, ruler-like section layout, basic typography and flat flag. This instruction takes precedence over older visual restraint for this concept. No shared brand document or live website is modified by the sample.

## Delivered

- Pure #000000 background, stronger branching circuitry, contact pads and moving red/white signal pulses; no radar.
- Sculpted black cards, rounded surfaces, distinct sections, local pointer-following border illumination, light strips and hover lift. Keyboard focus also reveals lighting. Touch screens receive static edge illumination.
- Embedded, subset variable Space Grotesk body type and Syne headings. Body remains 16px. H1 is 38px desktop, 34px tablet, 32px phone; no oversized display headings.
- A floating layered engineering illustration uses the weighted Roun Groun logo. It is labelled as an illustration, not a real product specification.
- Green top reading-progress line plus percentage/ring readout, measuring actual scroll progress. This is local UI only, not analytics tracking.
- Indian flag with a deformed cloth mesh, directional lighting and weave in the WebGL renderer. A shaded Canvas cloth renderer runs when WebGL is unavailable. Original tricolour and 24-spoke Chakra retained; fold shading changes apparent brightness.
- CEPA engineering history, both brands, Indian R&D/testing, owner-supplied made-in-India claim and five interactive architecture principles. No invented certifications, performance numbers, test results, locations or rescue guarantees.

## Provenance and licences

The owner supplied ownership, local manufacturing heritage, Indian research/testing-centre and 100% made-in-India facts in the preceding task brief. They are not independently audited. The 100% claim remains scoped to every REDLINE product under design, not every parent-brand product or individual electronic component.

Logo payload is reused unchanged from RL-10 v1: actual CEPA Group artwork (`cepa group_cepa group-03.png`, Library ID libfile_931967ee432c8191898a4775c23b8717) with alpha-preserving monochrome rendering; weighted Roun Groun geometry from RL-7 owner reference. No thin logo is used. Font sources are Google Fonts' official google/fonts repository, Space Grotesk and Syne under SIL OFL 1.1. Font subsets and full licences are embedded; font-assets.json also records source paths, licence text and checksums. Licences travel with the standalone HTML.

## Actual validation

| Check | Result |
| --- | --- |
| Reproducible build | Python standard-library build succeeded; file/hash recorded in build-summary.json |
| JavaScript syntax | Node --check passed |
| Desktop | Visual review at 1348px document width; client/scroll widths 1348/1348 |
| Phone | 390px iframe, 375px document; client/scroll widths 375/375; 16px body and 32px Syne H1; flag, header, cards and navigation inspected |
| Tablet | 820px iframe, 805px document; client/scroll widths 805/805; 16px body and 34px H1; visual review |
| Background | Computed rgb(0, 0, 0) |
| Reading progress | Verified 0% initially, intermediate values around 48–50%, and 100% at document end; green line and ring visible |
| Architecture | Click selection and keyboard ArrowRight/End verified on phone/desktop; one selected panel |
| Hover lighting | Actual pointer interaction on India card; coordinate variables update and illuminated green edge seen in screenshot |
| Pause/resume | Control label/root class and chip computed paused state verified; resume restores motion |
| Flag | Shaded Canvas fallback observed on desktop and phone; browser reports WebGL unavailable. GPU mesh branch is implemented and source-reviewed but could not be visually tested in this browser |

Circuit plate is cached at resize, drawing capped at 30fps desktop / 24fps phone with bounded path count and reduced pixel ratio. Flag redraws only near the viewport, and persistent motion stops for hidden documents or Pause. Reduced-motion logic is implemented and source-reviewed, not emulated in this browser. Core copy never waits for animation to become visible. No external runtime dependencies, videos, image requests or font requests. Final HTML is about 215KB uncompressed. No production performance benchmark is claimed.

## Reproduction, deployment and recovery

Open RG-REDLINE-About-Us-v2.html in a browser. To rebuild, run `python build.py`; it reads page.html, about.js, logo-assets.json and font-assets.json, then writes the standalone HTML and dist/index.html. No additional Python package is required.

Standalone document only. No WordPress page, option, plugin, live homepage, header/footer, customer, order or review was touched. No merge or production deployment occurred. Recovery is discarding this isolated v2 folder. WordPress integration would require adapting the standalone document shell and claiming an exact page/resource separately. Noindex/nofollow is included in the sample; live indexing settings are unchanged.

The editing claim is released at the Git checkpoint. Issue #10 remains open for owner review; draft PR #11 holds both concepts.
