# REDLINE homepage release — 28 November 2026

## Outcome

The owner-authorised Black Brushed Radar v3 is deployed as the existing static homepage at https://rg-redline.com/, WordPress page 14. One native core/html block; published state, page-no-title template and static-home assignment retained. Options included: Black brushed metal / Forged graphite / Oxide steel, White / Green radar, Calibrated / Subtle / Studio light, radar pause/resume.

Final raw content SHA256 `042e8bb2e633d84d13b91012b1fb4f0b683001215deff58332b4d2ad28bd48a4`, 125,301 bytes. Source standalone v3 remains unchanged with SHA256 c6918807f23789ff691ae06aa9813b5dac6bbbdb126a66d6e0140395ae2e7fae.

## Implementation and compatibility

Standalone head/document wrappers removed; embedded font license retained. Page-shell CSS remains scoped to page14, including zero outer padding/margins and hiding only the theme header/footer around this page. Weighted SVG logo definition reused in header/footer/watermark. All design markup/options preserved.

The initial save retained raw code exactly, but live WordPress output entity-encoded selected && tokens in the inline script. Live smoke checks caught this before completion. A scoped syntax-equivalent guard rewrite removed the affected ampersands; no shared filters, plugins or settings changed. See WORDPRESS-COMPATIBILITY.md and checkpoint c926e15. The public rendered script now passes Node --check and contains no introduced ampersand HTML entities.

## Verified live

- Anonymous root HTTP 200, homepage H1, three weighted SVG logo uses, both white/green options, zero per-tile beam elements; robots meta `noindex, nofollow` before and after.
- WordPress readback: one root core/html, final exact hash/size, page_on_front14 and show_on_front=page.
- Browser desktop 1363x936: equipment SVGs rendered, radar visible; green and white beam values tested; finish switching to forged/oxide/brushed tested; Studio/Subtle/Calibrated controls exercised; pause/resume tested; defaults restored for the review tab.
- Equipment concept dialog opened/closed. Field interface Night mode and reset to Terrain worked. Anchor navigation worked.
- Root x=0, full viewport content width, no horizontal overflow. wp-site-blocks, main and post-content report margin0/padding0. Theme outer header/footer display:none. The logged-in admin toolbar accounts for the 32px top offset; no extra layout gap.
- Rendered anonymous script syntax check passed, not just source/raw storage syntax.

Existing responsive CSS, reduced motion and hidden-tab suspension retained. Prior standalone responsive checks are documented separately; this release did not perform a fresh physical-device or performance benchmark. No zero-console-errors claim is made for unrelated browser-extension logging.

## Unchanged shared configuration / recovery

No site-settings, indexing, store-visibility, plugin, theme-template, checkout, payment, analytics or other-page edits. Existing store-pages-only Coming soon setting remains; the homepage is public and remains noindex. Parent Roun Groun environments untouched.

Before export exact hash c037fcfadc3602afa73bb9d3d5e0f8988ae0785f981a00847eaafcfc04b2744e in before-page14.html. Original export is historical recovery evidence, not an approved thin-logo asset. For an emergency rollback reread latest page14 and coordinate any later edits before restoring only its prior content. Preserve indexing and store settings. Do not restore an entire database.

Release ownership is handed off after this report; future writers must reread page14's actual current hash. Source branch/checkpoint history and PR #9 record the deployment. No technical locking or impossible-race guarantee is claimed.
