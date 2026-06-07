# AutoVetting — Task Queue

## Ready

- [ ] **SEO-001** `sitemap.xml` — Generated with 24 URLs, all pages including 10 new repair guides and /about/. Referenced in robots.txt, previously missing.
- [ ] **SEO-002** `HowTo schema — repair guides` — Injected JSON-LD HowTo schema into all 5 existing repair guides (oil-change, brake-pads-rotors, battery-replacement, cabin-filter, air-filter). Includes steps, tools, supplies, time, cost.
- [ ] **SEO-003** `FAQ schema — inspect + decode` — FAQPage JSON-LD injected into /decode/ (4 VIN Q&As + BreadcrumbList). Inspect already had FAQPage schema; skipped to avoid duplication.
- [ ] **SEO-004** `OG/Twitter tags` — Added og:title, og:description, og:url, og:type, og:image, og:site_name, twitter:card to: index.html, repair/index.html, repair/oil-change, repair/brake-pads-rotors, repair/battery-replacement, repair/cabin-filter, repair/air-filter.
- [ ] **SEO-005** `llms.txt` — Created /llms.txt with site description, tool listings, repair guide index, data sources, and optional-skip directives for /garage/ and /search/.
- [ ] **SEO-006** `10 new repair guides` — Created /repair/[slug]/index.html for: spark-plugs, coolant-flush, transmission-fluid, power-steering-fluid, wiper-blades, wheel-bearing, alternator, thermostat, fuel-filter, timing-belt. Each has HowTo-ready guideData JSON, OG tags, canonical, title, description.
- [ ] **SEO-007** `/about/index.html` — Methodology and About page with Organization JSON-LD schema, 5 content sections (what it is, data sources, methodology, no-affiliate model, who built it). GEO authority signal.

## Done

<!-- orchestrator moves Ready items here after push -->
