# RL-7 — Radar Titanium concept v2

Owner requested five changes to the approved-for-exploration Black Titanium concept. This is a standalone HTML revision, not a live WordPress deployment.

## Delivered changes

- Weighted/fat Roun Groun wordmark in header, footer and watermark. No thin wordmark fallback. The vector silhouette is traced from the coloured lettering of owner-supplied Banner 8.png; the original PNG was read-only. Distressed generated exports were inspected and excluded. This is a concept vector conversion, not a declaration that every earlier generated logo is an approved master.
- Titanium/grey darkened by one step while preserving metal texture and translucent surfaces.
- A single 18-second clockwise radar field replaces the diagonal travelling band. Circuit exposure and pad illumination share its angle. No independent per-tile sweep or autonomous spark timers remain.
- All .light-edge elements and their CSS sweep rules removed. Hover/focus elevates a tile by 5px, briefly brightens its boundary once, then settles. No repetitive strobe.
- Circuit routes increased from v1 19 desktop / 11 phone to 60 desktop / 28 phone, with parallel buses, vias, pads and small component outlines. Static geometry is rasterised only on resize.

## Performance / accessibility

One visible canvas at capped resolution, drawing at 24fps desktop / 18fps phone. Background animation suspends when the tab is hidden. Radar pause/resume and prefers-reduced-motion handling retained. Surface finish/intensity comparison controls remain. No external image/font/script assets, framework, video or WebGL dependency. Full standalone file: 122,356 bytes, SHA256 4a141f2c1ccf42eba527988d27b6140a4b8771f470858051eb1e0cb24af62662. v1 was 198,983 bytes. No hardware speed benchmark or production Core Web Vitals claim.

## Actual validation

- Node JavaScript syntax check passed.
- Browser desktop 1363x936: logo geometry rendered; three weighted symbol uses; no thin raster logo, no .light-edge elements, no horizontal overflow. Radar visible and rotates; pause/resume and oxide-to-brushed finish switching tested.
- Actual mouse hover confirmed :hover, computed translateY(-5px), boundary-confirm animation and settled edge opacity 0.22.
- VECTOR concept dialog opened and closed successfully.
- Phone 390x844 and tablet 820x1000 iframe viewports checked (content widths 375 and 805 after scrollbar), neither horizontally overflows. Phone menu opened and closed after anchor selection. These are browser responsive frames, not physical-device tests.
- Narrow-screen product callouts hidden to avoid overlapping the instrument illustration; final tablet display:none confirmed.
- Static checks: no duplicate IDs, broken same-document anchors or external asset requests.
- Reduced-motion and hidden-tab suspension are present in source; no OS accessibility setting was changed for this task.

## Brand decision / Git state

Owner-confirmed weighted-only logo rule merged to main through PR #8, merge commit 095c3b135178745e7f762ed114cd5d80c829b4e6. It is authoritative in AGENTS.md and docs/brand/BRAND_BRIEF.md, with task memory in BRAND-MEMORY.md.

Concept files are review artifacts. Storing this v2 does not deploy it or approve live product/safety claims. WP page 14, site indexing, WooCommerce visibility, other agent task files and generated logo export files were not modified.

## Recovery

v1 remains unchanged as RG-REDLINE-Black-Titanium-Concept.html. Select v1 for visual comparison if needed; keep the owner-confirmed weighted-only brand rule even if this background proposal is rejected. No production rollback is needed because no live settings/content were changed.
