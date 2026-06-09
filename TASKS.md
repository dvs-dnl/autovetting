# AutoVetting — Task Queue

**Living lifecycle tracker** for in-flight and ready-to-deploy work on autovetting.com.
Deploy gate: the hourly orchestrator pushes what's in **Ready to deploy / publish** — nothing else.

## In flight

*(none)*

## Ready to deploy / publish

*Tasks finished locally and verified. The hub orchestrator only pushes what's in this section.*

### autovetting-mazda-mx5-nd-launch-2026-06-09 — ready 2026-06-09

- Status: ready
- Started: 2026-06-09
- Touched files: inspect/index.html, pinpoint/index.html
- Notes: 2026-06-09 02:00: Launched Mazda MX-5 Miata ND (2016-2020). Added mazda-mx5-2016 inspection checklist (14 items / 5 sections — airbag recall 24V-695 Critical, 2016-2019 auto TCM recall 19V-072, soft-top leaks, ND1/ND2 155hp/181hp engine split, clutch slave cylinder, rear-diff whine, thin paint, Mazda Connect, i-stop) with vinNote (single 2.0L PE-VPS; ND1/ND2 via 10th VIN digit; recall VIN-check). Wired VEHICLE_MENU MX-5 across 2016-2020 (5 years). Fixed pinpoint inspectUrl model 'MX-5 Miata Club'->'MX-5 Miata' so the existing Pinpoint card link resolves to the new checklist (routing verified 2016/2017/2018/2019/2020->mazda-mx5-2016). Recalls verified fresh via NHTSA/Mazda WebSearch. Pillar blog post written to gitignored _hub (criterion 4). Commit: 303bb2c. Sibling check: no Done(last 10) block shares inspect/index.html or pinpoint/index.html (SEO/repair files only) — no Started backfill needed. Verified against: n/a. Syntax-check: PASS (inspect scripts 2+5, pinpoint). Dead-links: verified (no new static hrefs; pinpoint inspectUrl -> /inspect/ valid). Scanner: PASS (272 files). NOT YET PUSHED — this session has no github network egress (DNS/TCP unreachable); main is 2 ahead of origin (303bb2c + 4b0a52a). Push when networked.

## Done (last 10)
<!-- orchestrator moves Ready items here after push -->

### autovetting-seo-sitemap-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: sitemap.xml, robots.txt
- Notes: Generated sitemap.xml with 24 URLs covering all pages including 10 new repair guides and /about/. Referenced in robots.txt (previously missing).

### autovetting-seo-howto-schema-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: repair/oil-change/index.html, repair/brake-pads-rotors/index.html, repair/battery-replacement/index.html, repair/cabin-filter/index.html, repair/air-filter/index.html
- Notes: Injected JSON-LD HowTo schema into all 5 existing repair guides. Includes steps, tools, supplies, time, cost.

### autovetting-seo-faq-schema-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: decode/index.html
- Notes: FAQPage JSON-LD injected into /decode/ (4 VIN Q&As + BreadcrumbList). Inspect already had FAQPage schema; skipped to avoid duplication.

### autovetting-seo-og-tags-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: index.html, repair/index.html, repair/oil-change/index.html, repair/brake-pads-rotors/index.html, repair/battery-replacement/index.html, repair/cabin-filter/index.html, repair/air-filter/index.html
- Notes: Added og:title, og:description, og:url, og:type, og:image, og:site_name, twitter:card to homepage, repair index, and 5 existing repair guides.

### autovetting-seo-llms-txt-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: llms.txt
- Notes: Created /llms.txt with site description, tool listings, repair guide index, data sources, and optional-skip directives for /garage/ and /search/.

### autovetting-seo-new-repair-guides-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: repair/spark-plugs/index.html, repair/coolant-flush/index.html, repair/transmission-fluid/index.html, repair/power-steering-fluid/index.html, repair/wiper-blades/index.html, repair/wheel-bearing/index.html, repair/alternator/index.html, repair/thermostat/index.html, repair/fuel-filter/index.html, repair/timing-belt/index.html
- Notes: Created /repair/[slug]/index.html for 10 new guides. Each has HowTo-ready guideData JSON, OG tags, canonical, title, description.

### autovetting-seo-about-page-2026-06-07 — done 2026-06-07

- Status: done
- Started: 2026-06-07
- Touched files: about/index.html
- Notes: Methodology and About page with Organization JSON-LD schema, 5 content sections (what it is, data sources, methodology, no-affiliate model, who built it). GEO authority signal.

