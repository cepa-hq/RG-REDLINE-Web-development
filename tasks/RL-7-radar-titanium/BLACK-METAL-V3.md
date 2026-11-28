# Black brushed-metal variant v3 — 28 November 2026

Owner requested retaining the v2 page while providing black brushed-metal background and two radar colours, white or green.

## Changes

Black brushed-metal replaces the lighter steel foundation, retaining visible brushing/reflections rather than a flat black fill. Layout, weighted logo, equipment illustrations, translucent tile treatment, hover boundaries and existing interactions remain. The existing Surface controls panel adds Beam colour > White / Green (White default). The same shared 18-second rotating radar geometry drives either colour; the selected tone also colours the illuminated trace segments and pads. No independent tile beams or new asset dependencies.

## Checks

- Node JavaScript syntax passed.
- Browser: white and green selected successfully; green radar and matching circuit illumination visually observed. Both colour states read back from data-beam; pause/resume checked; default White restored in the preview.
- Desktop viewport 1363x936: no horizontal overflow; three weighted-logo symbol uses and zero tile-beam elements.
- Exact source markup comparison with v2 passed for hero heading, equipment cards, engineering section, field console and navigation links.
- Static validation: exactly two beam options, no duplicate IDs, no broken same-document anchors.
- v2 source hash remains 4a141f2c1ccf42eba527988d27b6140a4b8771f470858051eb1e0cb24af62662. v3 is separate: 124,757 bytes, SHA256 c6918807f23789ff691ae06aa9813b5dac6bbbdb126a66d6e0140395ae2e7fae.
- Existing reduced-motion handling, hidden-tab suspension and canvas cap retained. No new physical-device/performance benchmark performed; prior v2 responsive checks remain documented separately.

No live WordPress or shared brand-rule edits in this follow-up. Rollback/visual comparison: use preserved v2. Standalone concept only; not deployed.
