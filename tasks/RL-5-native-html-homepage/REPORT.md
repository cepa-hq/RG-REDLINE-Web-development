# RL-5 — Native HTML homepage

Status: deployed to WordPress and verified on 28 November 2026 (IST). Site remains in its pre-existing WooCommerce Coming soon mode; authorised visitors can preview the design.

Target: https://rg-redline.com. Page 14, slug `home`, template `page-no-title`. One `core/html` block; raw content hash c037fcfadc3602afa73bb9d3d5e0f8988ae0785f981a00847eaafcfc04b2744e.

Source: authoritative `Roun-Groun-REDLINE-Concept.html`, SHA256 `6d58482d6d32961d4058b3b01d2b7449cf2710c0d8cb3c26a9d9656e6151f654`. Original embedded font license retained.

Adaptation: strip document wrappers; scope CSS and DOM queries to #rl-redline-home; namespace display font/keyframes; page-ID-specific theme-shell removal and zero outside margins/padding. Original internal design spacing, circuit animation, device inspection, map modes, reduced motion and motion toggle retained. Replace offline/privacy statement with web-appropriate concept notice.

Baseline: Twenty Twenty-Five 1.5; Easy MCP AI 2.5.2 active; WooCommerce 11.3.1 active; Reading show_on_front=posts, page_on_front=0, page_for_posts=0. Anonymous robots meta `max-image-preview:large`; robots.txt allows normal site crawling. No former homepage modified.

Validation completed:

- JavaScript syntax check passes. Stored page SHA256 matches the built HTML exactly; one root core/html block, no child builder blocks.
- Reading: show_on_front=page, page_on_front=14, page_for_posts=0. Page 14 is published and uses page-no-title.
- Native Reading setting `Discourage search engines from indexing this site` checked and save confirmation observed before page publication. Both authenticated concept page and anonymous responses contain `noindex, nofollow`.
- Anonymous requests to /, /home/ and /shop/ return the existing Coming soon screen rather than the concept. WooCommerce Coming soon setting was deliberately preserved.
- robots.txt is still crawlable and advertises the normal sitemap; no claim of a robots.txt Disallow-all is made. Crawlers can fetch and read noindex. No search submission performed.
- Browser desktop viewport 1363x936: original embedded font loaded, SVG devices rendered, no horizontal document overflow. Root begins at x=0 and spans the content viewport; only the logged-in WordPress admin bar contributes a 32px top offset. Theme outer containers report margin/padding 0; theme header/footer display:none only on page 14.
- Interactive browser checks passed: anchor navigation, VECTOR inspection dialog and close, Night / Storm modes, reset to Terrain, motion off/on. Original responsive CSS and reduced-motion rules preserved; no separate mobile device execution performed.
- Browser console sample showed extension metadata errors from chrome-extension:// only; those are not attributed to the homepage. No blanket zero-console-errors claim.

Deployment details:

- New page title: Roun Groun REDLINE — Beyond the threshold. URL: https://rg-redline.com/ (front page).
- Source checkpoint commit: fd28e8eeb4d5d411b92c1d45884003072e296909.
- REST settings update recorded exactly two setting changes; indexing safeguard saved through native Reading UI because blog_public is not registered in core settings REST.
- No settings outside this task's claim were edited. No global template/theme/plugin changes.
- Noindex is a search-engine instruction, not a guarantee of immediate removal of any previously indexed URL. Existing Coming soon screen conceals the concept from normal anonymous visitors; it is not a password/access-control guarantee.

Rollback: set Reading show_on_front=posts and page_on_front=0, then move only new page 14 back to draft. Keep blog_public=0 until owner requests launch/indexing. Do not restore indexing automatically. Re-read current settings/page revision before any rollback; coordinate if another agent changed them.

Other work: logo task #3 / PR #4 untouched. Parent roungroun.com untouched. No plugin/theme/template edits.
