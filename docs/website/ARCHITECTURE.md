# Website architecture and incremental delivery

## Confirmed project constraints

| Item | Owner brief |
| --- | --- |
| Domain | rg-redline.com |
| Platform | WordPress + WooCommerce |
| Presentation | “Without a theme”; custom page-by-page delivery, no assumed off-the-shelf theme |
| Build sequence | Pages individually designed, implemented, tested and released |
| Repository purpose | Shared task, brand, artifact and development coordination |

Domain provisioning, hosting, staging address, installed software versions, active theme/shell, source paths and deployment access have not been inspected or verified in this setup task.

## Resolve the rendering boundary before implementation

The owner's “without a theme” requirement is a presentation constraint, not permission to remove unknown active infrastructure. Inspect the actual installation and document its request/render entry points before writing code.

Confirm whether a minimal bootstrap/shell, plugin-owned rendering or another owner-approved arrangement is in use. Do not silently install Flatsome, a commercial theme, a page builder or a headless framework. Do not disable an active shell or omit WordPress/WooCommerce integration hooks to obtain an empty canvas.

Record the confirmed source repository and deployment path. This coordination repository may hold implementations and exports, but its existence does not prove a working tree matches the deployed WordPress instance.

## Proposed ownership boundaries

These are coordination boundaries, not a declaration that these components already exist.

| Surface | Ownership rule |
| --- | --- |
| Site shell, header, footer, navigation and render hooks | One shared-shell owner at a time |
| Design tokens, typography, base components | One design-system owner; publish versioned contracts |
| Homepage and each content page | Separate task with exact root, route, page ID and local assets |
| Shop, category and product templates | Commerce owner; explicitly coordinate shared product components |
| Cart, checkout, account and order-success logic | Separate commerce tasks with checkout/data regression checks |
| SEO, sitemap, structured data, indexing and icons | Shared SEO task with environment-specific scope |
| Analytics/consent, forms, email and integrations | Separate tasks with identifiers and behavior recorded safely |
| Release/deployment | One release owner per target environment |

Independent page owners may work in parallel when their scopes do not overlap. Coordinate shared contracts before parallel integration.

## Per-page delivery record

For every page, publish:

1. Task Issue; responsible agent; owner authorization covering design/implementation/deployment as applicable.
2. Intended URL, WordPress resource ID, source paths, local asset paths and page-specific namespace.
3. Baseline source commit and current WordPress revision/hash/setting snapshot.
4. Shared dependencies, their owner and compatible version.
5. Scope exclusions and expected behavior.
6. Reviewable artifact/preview and exact implementation change.
7. Desktop, tablet, phone, keyboard and reduced-motion checks appropriate to the page.
8. Navigation, forms, WooCommerce, SEO and performance checks affected by the change.
9. Target environment, release evidence and scoped rollback.

Suggested initial sequence: verify infrastructure/rendering boundary; agree shared tokens and shell; build homepage; build shop/category/product; build cart/checkout/account; build support/story/policies; complete SEO/tracking and release checks. This is a proposal, not approval to start every workstream.

## Engineering requirements

- Scope page assets to the relevant routes. Avoid duplicating heavy animation libraries or globally loading every page script.
- Progressive enhancement: core text, links, product decisions and checkout must remain accessible without nonessential animation.
- Use reduced-motion support and pause/stop controls for persistent motion; suspend background animation in hidden tabs.
- Validate accessible contrast, touch targets, focus states, meaningful alt text and responsive overflow.
- Preserve WooCommerce variation, stock, price, cart, checkout, payment and order-state behavior; respect existing authoritative plugins.
- Never edit WordPress or WooCommerce core. Record any compatibility patch and its replacement/maintenance plan.
- Guard admin/API writes with appropriate permissions, validation and CSRF protections; avoid exposing secrets to page scripts.
- Treat canonical URLs, crawl restrictions, robots directives, sitemap hosts, verification tokens, analytics destinations and caches as environment-specific release items.
- Do not assume publishing staging automatically preserves production orders or environment configuration.

## Evidence and configuration

Commit reviewed source, task-local patches, non-sensitive setting deltas and sanitized test reports. Keep credentials and sensitive before-state backups outside this public repository. Record where authorized maintainers can recover them without posting access tokens or private URLs.

