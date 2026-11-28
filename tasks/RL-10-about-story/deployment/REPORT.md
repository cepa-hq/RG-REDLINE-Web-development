# RL-10 — Approved About page production release

Agent codex-redline-about. 28 November 2026, Asia/Kolkata. Status: production released and verified. Source checkpoint before release: df7dbbf3ad953cbd7369d4d9ee85ec792ecfe556. Task branch agent/codex-redline-about/rl-10-about-story, issue #10 and archive/review PR #11.

## Authorization and delivered result

Owner explicitly finalised Exo 2, Brushed Silver and publication as a native WordPress HTML block. New About page19 is published at https://rg-redline.com/about/ using the existing page-no-title template. No previous About page existed. The temporary comparison controls and titanium alternative are removed; all headings are locked to #C4C8CD, +0.02em tracking and 1.32 line height. Existing sizes/weights, licensed font, weighted wordmark, CEPA artwork, serious owner-supplied story, black circuitry, illuminated hover cards, flag, architecture panels and reading progress are retained.

The source is one core/html block, not an iframe or page-builder layout. Standalone document wrappers were removed. CSS selectors are scoped to #rg-about; standalone html/body rules and WordPress shell spacing adjustments are limited to body.page-id-19 or html:has(body.page-id-19). Root state classes and keyframes were adapted without changing shared CSS. Existing theme header/footer are hidden only on this page. Outside margin/padding is zero. The page's brand link leads to the homepage. No homepage/shared navigation edit was made.

The known site's inline-JS ampersand formatting issue is handled by one equivalent local guard replacing &&. No WordPress filters, plugins or security settings changed. Anonymous rendered script is byte-for-byte identical to expected script; SHA-256 05d3fcfaa38424b9d66a9534cb456f9c5e8b12ec6d1f12cf3a996da4b5a5aea7.

## Release and evidence

Fresh connector evidence before every write verified https://rg-redline.com. Installed WordPress reported 7.1.5, active Twenty Twenty-Five 1.5. New page was created as a draft, exported, then populated, read back and finally published after exact block verification. Connector has no atomic revision guard; claimed writes were serialized with fresh hashes, not described as a hard lock.

Final native content SHA-256 4e0bce0c9d594aad6d5e57216c38b8b4c60b6dfded37a40df36a572cdfff04dc; 192,102 bytes. Actual final page metadata and sentinel values are in after-readback.json. The same hash was observed before publication and in final published readback.

| Check | Actual result |
| --- | --- |
| Native block | Exactly one core/html block; content/hash retained |
| Anonymous response | HTTP200 at /about/; canonical https://rg-redline.com/about/ |
| Indexing safeguard | Public head retains noindex,nofollow; global settings unchanged |
| Script retention | Anonymous rendered app script exact match; Node syntax passed |
| Desktop live layout | Root x0, width1348, margin0; document client/scroll widths1348/1348 |
| Approved typography | Exo2; body16px; H1 colour rgb(196,200,205), tracking .76px |
| Live phone-width frame | Actual public page in390px iframe,375px document; no admin bar, root x0, client/scroll375/375, body16px, H1 32px, correct font/silver |
| Live tablet-width frame | Actual public page in820px iframe; client/scroll805/805; visual review |
| Architecture | Desktop click and phone keyboard ArrowRight selection verified; correct single panel |
| Motion | Pause/Resume control verified; paused class read back |
| Flag | Live desktop and phone Canvas cloth rendering observed; GPU path unavailable in this browser, not claimed tested |
| Reading progress | Live 0/intermediate/100 values observed; green bar present |
| Homepage sentinel | Page14 content hash remains 042e8bb2e633d84d13b91012b1fb4f0b683001215deff58332b4d2ad28bd48a4; static frontpage14 unchanged |

Iframe width checks exercised the actual published WordPress page, rather than a local copy. They are responsive browser checks, not physical phone testing. No production speed-score benchmark or complete site accessibility certification claimed. Existing cached canvas traces, frame caps, hidden-tab pause, offscreen flag suppression and reduced-motion handling remain; no extra external page asset downloads introduced.

## Provenance and boundaries

Typography/colour approval is in DECISIONS.md. Manufacture, CEPA ownership and Indian R&D/testing statements come from the owner's brief; not an independent certification audit. The 100% made-in-India statement remains scoped to REDLINE products under design. Source approved preview hash 8fadcbf7c2139611f49525ca625d779d73a68fbd14e2f3f373016f7ae1f3e330. Font/asset licences and source notices travel inside the native block. No invented ratings, facilities, test results or survival guarantees added.

No global template files, plugin activation, Reading/indexing/store-visibility settings, WooCommerce data, orders/customers/reviews, tracking, menus, homepage or other agent resources changed. Existing source previews remain intact. Standalone final HTML is a convenience companion; the native block is the deployed canonical artifact.

## Recovery and handoff

before-page19.json captures the newly created page's empty draft baseline and template. Scoped rollback, after fresh target/hash/ownership checks, is to return only page19 to draft; if exact content restoration is needed, clear its content via the supported clear field and retain the template/title/slug from that baseline. Do not restore the whole database or touch homepage/options. The published block and builder permit exact reapplication if authorised. No pending deployment remains.

Release/editing claim is released at this checkpoint. GitHub PR remains an archive/review item; deployment did not depend on merging it. User review can continue on the live About page.
