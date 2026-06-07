# AutoVetting — Task Queue

**Living lifecycle tracker** for in-flight and ready-to-deploy work on autovetting.com.
Deploy gate: the hourly orchestrator pushes what's in **Ready to deploy / publish** — nothing else.

## In flight

*(none)*

## Ready to deploy / publish

*Tasks finished locally and verified. The hub orchestrator only pushes what's in this section.*

### autovetting-seo-sitemap-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: sitemap.xml, robots.txt
- Notes: Generated sitemap.xml with 24 URLs covering all pages including 10 new repair guides and /about/. Referenced in robots.txt (previously missing).

### autovetting-seo-howto-schema-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: repair/oil-change/index.html, repair/brake-pads-rotors/index.html, repair/battery-replacement/index.html, repair/cabin-filter/index.html, repair/air-filter/index.html
- Notes: Injected JSON-LD HowTo schema into all 5 existing repair guides. Includes steps, tools, supplies, time, cost.

### autovetting-seo-faq-schema-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: decode/index.html
- Notes: FAQPage JSON-LD injected into /decode/ (4 VIN Q&As + BreadcrumbList). Inspect already had FAQPage schema; skipped to avoid duplication.

### autovetting-seo-og-tags-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: index.html, repair/index.html, repair/oil-change/index.html, repair/brake-pads-rotors/index.html, repair/battery-replacement/index.html, repair/cabin-filter/index.html, repair/air-filter/index.html
- Notes: Added og:title, og:description, og:url, og:type, og:image, og:site_name, twitter:card to homepage, repair index, and 5 existing repair guides.

### autovetting-seo-llms-txt-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: llms.txt
- Notes: Created /llms.txt with site description, tool listings, repair guide index, data sources, and optional-skip directives for /garage/ and /search/.

### autovetting-seo-new-repair-guides-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: repair/spark-plugs/index.html, repair/coolant-flush/index.html, repair/transmission-fluid/index.html, repair/power-steering-fluid/index.html, repair/wiper-blades/index.html, repair/wheel-bearing/index.html, repair/alternator/index.html, repair/thermostat/index.html, repair/fuel-filter/index.html, repair/timing-belt/index.html
- Notes: Created /repair/[slug]/index.html for 10 new guides. Each has HowTo-ready guideData JSON, OG tags, canonical, title, description.

### autovetting-seo-about-page-2026-06-07

- Status: ready
- Started: 2026-06-07
- Touched files: about/index.html
- Notes: Methodology and About page with Organization JSON-LD schema, 5 content sections (what it is, data sources, methodology, no-affiliate model, who built it). GEO authority signal.

## Done (last 10)

<!-- orchestrator moves Ready items here after push -->
