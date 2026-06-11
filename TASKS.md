# AutoVetting — Task Queue

**Living lifecycle tracker** for in-flight and ready-to-deploy work on autovetting.com.
Deploy gate: the hourly orchestrator pushes what's in **Ready to deploy / publish** — nothing else.

## In flight

*(none)*

## Ready to deploy / publish

*Tasks finished locally and verified. The hub orchestrator only pushes what's in this section.*

### autovetting-recall-audit-wave2-ledger-gate-2026-06-10 — ready 2026-06-10

- Status: ready
- Started: 2026-06-10 (daytime, Daniel-directed — Phase 0 of 90-day plan)
- Touched files: inspect/index.html, pinpoint/index.html, scripts/gate-check.py, scripts/recall-ledger.json, _hub/Vehicle-Launch-Spec.md, _hub/Build-Log/2026-06-10-recall-audit-wave2-ledger-gate.md
- Notes: Recall audit wave 2 — verified 18V-307/19V-237/21V-737/19V-394/22V-092/12V-471 are fabrications (Newmar motorhome/Curbtender truck/MCI coach/Forest River trailer/Navistar truck/Starcraft RV) and 16V-061 is real Honda-Acura Takata misapplied to 14 of 15 uses. Fixed 55 entries in inspect/index.html across 41 checklists (40 deleted, 14 -> generic VIN-check, 1 Ridgeline rescoped); synced 32 stats counts; filled 3 emptied lists. NEW G28 recall-ledger gate (scripts/recall-ledger.json: 13 verified + 152 legacy ratchet) immediately caught + fixed 3 more fabrications in pinpoint cards (20V-501 Corolla valve-spring -> 20V-682, 20V-391 Camry -> 20V-012, 15V-048 F-150 -> VIN-check wording). Gates: 28 PASS / 0 CRIT FAIL; byte/line/tail verified, backups kept. Verified against: autovetting-recall-audit-20v014-20v501-2026-06-10 (continues its queue; same fix policy). Sibling check: no Ready/Done(last 10) item shares inspect/pinpoint files since 8b39a91 (pushed). Detail: Build-Log/2026-06-10-recall-audit-wave2-ledger-gate.md.

### autovetting-blog-deploy-pipeline-2026-06-10 — ready 2026-06-10

- Status: ready
- Started: 2026-06-10 (daytime, Daniel-directed)
- Touched files: scripts/render-blog.py (NEW), blog/index.html (NEW), blog/<slug>/index.html (17 NEW post pages), sitemap.xml, llms.txt, scripts/recall-ledger.json, TASKS.md
- Notes: Built the /blog/ deploy pipeline. scripts/render-blog.py (stdlib-only, reusable, idempotent) renders _hub/Content/blog/*.md (status: published) to blog/<slug>/index.html with full site chrome (GA4 G-YM12JSF5D1, site.css, favicon family, OG/Twitter, footer brand line) + Article JSON-LD + FAQPage JSON-LD (parsed from each post's FAQ section per Blog-Post-Standard render-time TODO), builds blog/index.html (17 cards newest-first + CollectionPage/ItemList JSON-LD), and updates sitemap.xml (18 blog URLs, lastmod 2026-06-10) and llms.txt (## Blog section, 17 entries). 17 published posts rendered; 3 drafts excluded (2017 Rogue, 2019 Ram 1500 non-Classic, 2019 CR-V). blogUrl reconciliation vs inspect/index.html: 17/18 resolve; 1 orphan blogUrl /blog/2017-nissan-rogue-buyers-guide points at the draft Rogue post (inspect NOT touched — resolves when that post publishes). Renderer auto-unlinks internal /blog/ links to unpublished slugs (1 instance in 2018 F-150 post). Ledger: added 3 NHTSA-verified Ford F-150 campaigns from the 2021 F-150 post's Sources — 21V090 (Part 573 PDF RCLRPT-21V090-6921, fetched+confirmed), 22V142 (Part 573 PDF RCLRPT-22V142-7127, fetched+confirmed), 21V653 (nhtsa.gov press release + NHTSA API campaignNumber=21V653000 confirmed: Super Cab seat-belt webbing, 16,430 units). Verified: every blog page has </html> + GA4; zero dangling local hrefs; all JSON-LD parses; sitemap parses as XML. Gates: 28 PASS / 1 WARN (pre-existing legacy backlog 152) / 0 CRITICAL failed. Sibling check: overlaps autovetting-recall-audit-wave2-ledger-gate-2026-06-10 (Ready, same scripts/recall-ledger.json) — additive only (3 new verified entries, legacy list untouched), no conflict; no other Ready/Done(last 10) item touches blog/, sitemap.xml, or llms.txt. NOT committed/pushed per task spec — orchestrator deploys.

*(none)*

## Done (last 10)
<!-- orchestrator moves Ready items here after push -->

### autovet-seo-content-2019-honda-crv-2026-06-10 — done 2026-06-10

- Status: done
- Started: 2026-06-10
- Touched files: _hub/Content/blog/2026-06-10-2019-honda-crv-buyers-guide.md, _hub/Content/_seo-research/2026-06-10-2019-honda-crv.md, _hub/Content/_seo-research/top-500-vehicles.md (Already-covered row)
- Notes: 2026-06-10: drafted 2019 Honda CR-V pillar post (5th gen 2017–2022; Tier-1 #15).
  Output: Content/blog/2026-06-10-2019-honda-crv-buyers-guide.md (status: draft, ~2,150 words), Content/_seo-research/2026-06-10-2019-honda-crv.md.
  Sibling check: Verified against: autovetting-recall-audit-20v014-20v501-2026-06-10 (post recall numbers aligned with audit-verified 21V215/23V858 scope, CR-V 2018–2020), autovetting-mazda-mx5-nd-launch-2026-06-09 (different vehicle). No re-sync needed.
  Recalls verified via WebSearch primary sources: 19V383 Part 573 PDF (RCLRPT-19V383-5322), 23V858 (RCAK-23V858-9680), 19V865 (cited in prose, no PDF surfaced — Justia record in research file), oil-dilution warranty extension (Consumer Reports), class-action 2019–2023 scope. No fabricated IDs; 12V battery-drain pattern described as complaint pattern, no invented TSB.
  Standard validation: PASS (no /decode/, footnote-only externals ×6, pinpoint ?q=CR-V + inspect deep-link present, real repair slugs only, TL;DR + 6-question FAQ, read-next slot).
  NOT in Ready to deploy — drafts in gitignored _hub are private until Daniel reviews and migrates (per task spec; auto-pusher does not watch Content/blog/).

### autovetting-recall-audit-20v014-20v501-2026-06-10 — done 2026-06-10

- Status: done
- Started: 2026-06-10
- Touched files: inspect/index.html
- Notes: 2026-06-10 02:00: Systemic recall-number audit (the 2026-06-08 Awaiting-Daniel follow-up; GTM-audit priority "fix live recall errors first"). Verified via NHTSA Part 573 reports + WebSearch that 20V-014 is a Triumph motorcycle campaign and 20V-501 is an Altec Industries campaign — both fabricated on all 21 car occurrences. Fixed: 8x Honda/Acura 20V-014 -> 23V-858 (Denso fuel pump, per-model year scopes from Part 573: Accord/Civic/CR-V/HR-V/MDX/RDX 2018-2020, Fit 2018-2019, Passport 2019-2020); Corolla 2020 "valve spring 20V-501" item fully rewritten -> Denso fuel pump 20V-682/20TA02 (no valve-spring recall exists; 5 prose+item+vinNote occurrences); Subaru Impreza/Legacy/Outback 20V-501 -> 21V-587 (WRG-21 fuel pump, 2018-2020); Crosstrek 20V-501 entry DELETED (not covered by 21V-587, no injector recall exists); Prius gen3 fake pump entries (19V-752/20V-014) -> verified 14V-053 inverter IPM (gen3 has no Denso pump recall); Mazda CX-30 20V-501 -> 20V-346 (brake caliper bolts, Mazda 4420F); Mazda6 20V-501 -> 21V-875 (fuel pump, Mazda 5321K); acura-mdx-2018 bogus "EyeSight ECU" 18V-307 entry deleted (EyeSight is Subaru-only). stats.recalls counts reconciled (prius 4->3, crosstrek 3->2, mdx 3->2, corolla 3->2). Commit: 8b39a91 (5da009c amended to include this TASKS.md entry). Sibling check: overlaps autovetting-mazda-mx5-nd-launch-2026-06-09 (done, Started 2026-06-09) — disjoint regions (recall entries vs MX-5 checklist); Verified against: autovetting-mazda-mx5-nd-launch-2026-06-09. Syntax-check: PASS (scripts 2+5; full CHECKLISTS+VEHICLE_MENU brace-extraction eval: 245 keys / 17 years; tail verified; href count 20==20). Dead-links: verified (no href changes). Scanner: PASS (277 files). ⚠️ FOLLOW-UP queued: 18V-307 appears 11x with 5 different invented defects (Honda fuel pump / Subaru EyeSight / VW roof glass / Mitsubishi injector / Mazda i-ACTIVSENSE) — needs same model-by-model audit next run; 19V-237, 21V-737, 19V-394, 16V-061, 22V-092 from same authoring pattern also unverified.
  2026-06-10 02:30: PUSHED by overnight builder via HTTPS+PAT, 970f468..8b39a91. Deploy-gate hook: all CRITICAL gates passed. Moved to Done.



### autovetting-mazda-mx5-nd-launch-2026-06-09 — done 2026-06-10

- Status: done
- Started: 2026-06-09
- Touched files: inspect/index.html, pinpoint/index.html
- Notes: 2026-06-09 02:00: Launched Mazda MX-5 Miata ND (2016-2020). Added mazda-mx5-2016 inspection checklist (14 items / 5 sections — airbag recall 24V-695 Critical, 2016-2019 auto TCM recall 19V-072, soft-top leaks, ND1/ND2 155hp/181hp engine split, clutch slave cylinder, rear-diff whine, thin paint, Mazda Connect, i-stop) with vinNote (single 2.0L PE-VPS; ND1/ND2 via 10th VIN digit; recall VIN-check). Wired VEHICLE_MENU MX-5 across 2016-2020 (5 years). Fixed pinpoint inspectUrl model 'MX-5 Miata Club'->'MX-5 Miata' so the existing Pinpoint card link resolves to the new checklist (routing verified 2016/2017/2018/2019/2020->mazda-mx5-2016). Recalls verified fresh via NHTSA/Mazda WebSearch. Pillar blog post written to gitignored _hub (criterion 4). Commit: 303bb2c. Sibling check: no Done(last 10) block shares inspect/index.html or pinpoint/index.html (SEO/repair files only) — no Started backfill needed. Verified against: n/a. Syntax-check: PASS (inspect scripts 2+5, pinpoint). Dead-links: verified (no new static hrefs; pinpoint inspectUrl -> /inspect/ valid). Scanner: PASS (272 files). NOT YET PUSHED — this session has no github network egress (DNS/TCP unreachable); main is 2 ahead of origin (303bb2c + 4b0a52a). Push when networked.
  2026-06-10 02:00: PUSHED by overnight builder via HTTPS+PAT (SSH port 22 blocked; HTTPS egress worked). origin/main now at 970f468 (range 7fa5ab0..970f468, includes 4b0a52a recall fixes). Deploy-gate hook: 27 passed, 0 failed.



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

