# RL-5 — Native HTML homepage

Status: draft prepared; publication waits for indexing safeguard.

Target: https://rg-redline.com. Page 14, slug `home`, template `page-no-title`. One `core/html` block; raw content hash c037fcfadc3602afa73bb9d3d5e0f8988ae0785f981a00847eaafcfc04b2744e.

Source: authoritative `Roun-Groun-REDLINE-Concept.html`, SHA256 `6d58482d6d32961d4058b3b01d2b7449cf2710c0d8cb3c26a9d9656e6151f654`. Original embedded font license retained.

Adaptation: strip document wrappers; scope CSS and DOM queries to #rl-redline-home; namespace display font/keyframes; page-ID-specific theme-shell removal and zero outside margins/padding. Original internal design spacing, circuit animation, device inspection, map modes, reduced motion and motion toggle retained. Replace offline/privacy statement with web-appropriate concept notice.

Baseline: Twenty Twenty-Five 1.5; Easy MCP AI 2.5.2 active; WooCommerce 11.3.1 active; Reading show_on_front=posts, page_on_front=0, page_for_posts=0. Anonymous robots meta `max-image-preview:large`; robots.txt allows normal site crawling. No former homepage modified.

Checks so far: JS syntax passes; saved page hash matches local block exactly; WordPress reports exactly one core/html block. Browser verification pending.

Rollback: set Reading show_on_front=posts and page_on_front=0, then move only new page 14 back to draft. Keep blog_public=0 until owner requests launch/indexing. Do not restore indexing automatically. Re-read current settings/page revision before any rollback; coordinate if another agent changed them.

Other work: logo task #3 / PR #4 untouched. Parent roungroun.com untouched. No plugin/theme/template edits.
