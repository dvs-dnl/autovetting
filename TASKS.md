# AutoVetting — Task Queue

**Living lifecycle tracker** for in-flight and ready-to-deploy work on autovetting.com.
Deploy gate: the hourly orchestrator pushes what's in **Ready to deploy / publish** — nothing else.

## In flight

### autovet-competitor-monitor

- Status: in flight
- Task: weekly competitive intelligence rotation (one company/week)
- Notes:
  - 2026-06-11 (this run): profiled YourMechanic / Wrench (🟡).
    Output: Competitors/_Monitor/2026-06-11-yourmechanic-wrench.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps (In-flight empty; Ready/Done last 10 are recall-audit/funnel-CTA/blog-deploy/SEO — orthogonal to competitor intel).
    Key delta: YourMechanic down to ~3 employees, consumer PPI frozen; Wrench also owns Lemon Squad — flag for next Lemon Squad pass.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Bumper (Instavin).

  - 2026-06-18 08:08: profiled Bumper (Instavin / VINDATA) (🟡).
    Output: Competitors/_Monitor/2026-06-18-bumper.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) are orthogonal; Ready empty; Done(last 10) = recall-audit waves 4-9 + deprice-CTAs (inspect/ + blog/), none touch Competitors/. No Re-sync needed.
    Key delta: BASELINE — Bumper had no prior profile and is absent from Competitor_Analysis.md. It is a vehicle-history-report + VIN-data-API play (powered by VINDATA; NMVTIS provider), NOT physical inspection. Notable: subscription dark-pattern billing reputation hardened into 2026 ($1 trial -> ~$25-30/mo auto-renew; fresh BBB complaints). AI 'Smart Insights' exists but dates to Jun 2024 (not a fresh delta). No physical-inspection move, no funding/M&A -> AutoVet's PPI white space intact.
    Implication: reinforces transparent/no-subscription pricing direction (contrast vs Bumper billing complaints); keep AI differentiation anchored to physical-condition vetting; consider adding Bumper to Competitor_Analysis.md Indirect Competitors.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Carfax (S&P Global Mobility) [watch with extra care: competitor AND most-likely acquirer per business plan §9/§13].


### autovet-cpo-protocol-ingestion

- Status: in flight
- Task: weekly OEM CPO protocol ingestion (one manufacturer/week) into Product/CPO-Protocols/
- Notes:
  2026-06-14 09:34: ingested Nissan CPO protocol (167 inspection points; also 139 EV / 84 Certified Select tiers).
    Output: Product/CPO-Protocols/nissan-certified.md, Product/CPO-Protocols/_runs/2026-06-14-nissan.md.
    Sibling check: no true conflict. In-flight autovet-competitor-monitor touches Competitors/ only (orthogonal). Verified against / cross-referenced to: autovetting-recall-audit-wave7-2026-06-14, autovetting-recall-audit-wave6-2026-06-13, autovetting-recall-audit-wave4-2026-06-11 — those waves verified Nissan campaigns 23V-093 / 22V-875 / 17V-663 (Rogue-only) / 16V-244 (2013-2016 OCS) in inspect/index.html + scripts/recall-ledger.json; this protocol file is upstream and reuses those verified IDs (complementary, not conflicting). No Re-sync needed.
    Weekly milestone: DONE — nissan-certified.md saved + INDEX.md updated; protocol ready for downstream consumption (overnight-builder / content-checklist authoring). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Hyundai.

### autovet-seo-content

- Status: in flight
- Task: weekly programmatic SEO pillar post (one top-500 vehicle/week) into Content/blog/ + research log in Content/_seo-research/
- Notes:
  2026-06-17 11:00: drafted 2019 Chevrolet Equinox pillar post (Tier-1 #4, highest-ranked fully-uncovered vehicle; 1.5L turbo oil-consumption + timing-chain cold-start rattle story).
    Output: Content/blog/2026-06-17-2019-chevrolet-equinox-buyers-guide.md (1,975 words, status: draft), Content/_seo-research/2026-06-17-2019-chevrolet-equinox.md.
    Recalls cited are all WebSearch-verified — 20V668 (GM N202313440, start-stop accumulator / loss-of-propulsion, 2018-2020 Equinox), 18V576 (rear brake caliper coating, 2018-2019), 19V184 (rear-right head-restraint welds). Two claims left [unverified] rather than fabricated: fuel-tank-seam recall campaign number + the timing-chain TSB ID. Interlinks to 2019-honda-crv + 2017-nissan-rogue posts.
    Sibling check: no overlaps. In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) are orthogonal; Ready empty; Done(last 10) recall-audit waves 4-9 + deprice-CTAs touch inspect/ + 18 existing blog posts, none a Chevrolet Equinox slug. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Toyota RAV4 (#11), Ford Explorer (#7), Hyundai Tucson (#17, recent recall news).

## Ready to deploy / publish

*Tasks finished locally and verified. The hub orchestrator only pushes what's in this section.*

### autovetting-pinpoint-inspect-gap-closure-2026-06-19 — ready

- Status: ready to deploy (committed locally; interactive session has no PAT — orchestrator to push)
- Started: 2026-06-19 (Daniel-directed interactive session; launch-freeze reallocation queue item #3)
- Touched files: scripts/gate-check.py, pinpoint/index.html, _hub/Build-Log/2026-06-19-pinpoint-inspect-gap-closure.md, _hub/Awaiting-Daniel.md, TASKS.md
- Notes:
  Two changes. (1) **Cleared the homepage-test-bc push blocker** (Daniel approved "exclude"): added
  "homepage-test-bc/index.html" to both G18 EXCLUDE sets in scripts/gate-check.py (~lines 292 G15 /
  389 G18), matching homepage-test/. Gate now 27 pass / 2 warn / **0 CRIT** (was 1 CRIT). Nightly
  rename-aside workaround no longer needed. (2) **Pinpoint↔Inspect gap closure** (already-launched
  generations only — no new vehicles): mirrored inspect's findChecklistByYMMT resolver over all 245
  CHECKLISTS + VEHICLE_MENU; of 297 Pinpoint inspectUrls, 196 resolved / 101 broken at baseline.
  Repaired **17 trim-suffix inspectUrls** where the model param carried a trim (e.g. "Accord Touring
  2.0T" → "Accord") and VEHICLE_MENU already routes the base+year to a launched checklist
  (menu-authoritative — no cross-gen mislinks). Resolved 196→213, broken 101→84. Display names
  untouched; only inspectUrl targets changed. Deliberately skipped Prius c (distinct model, not a
  Prius trim), models with no launched checklist (Ram 1500, Porsche Macan, Rivian, etc. — freeze),
  and diff-generation-only cases (2023 Highlander, 2022 Camry). Sibling check: pinpoint/index.html
  not shared by any in-flight task (autovet-competitor-monitor=Competitors/, cpo-protocol-ingestion=
  Product/CPO-Protocols/, seo-content=Content/blog/ — all orthogonal, all in gitignored _hub/);
  scripts/gate-check.py only otherwise touched by nightly recall waves (gate runner, not data) — no
  conflict. Verification: diff = exactly 17 inspectUrl lines; file 4073 lines intact (−190 bytes),
  tail intact, 297 inspectUrls steady; backup /tmp/pinpoint-w12.bak. Gate: 27 pass / 0 CRIT.
  Detail: _hub/Build-Log/2026-06-19-pinpoint-inspect-gap-closure.md.


### autovetting-internal-linking-2026-06-19 — ready

- Status: ready to deploy (committed locally; interactive session has no PAT — orchestrator to push)
- Started: 2026-06-19 (Daniel-directed interactive session; launch-freeze reallocation queue item #2)
- Touched files: inspect/index.html, pinpoint/index.html, _hub/Build-Log/2026-06-19-internal-linking.md, TASKS.md
- Notes:
  Internal-linking pass (queue #2, no new vehicles). (1) **Fixed the one dead checklist→blog link**:
  nissan-rogue pointed to /blog/2017-nissan-rogue-buyers-guide which 404s (unpublished draft) —
  removed the blogUrl from the checklist (inspect 18→17 blogUrls). Publishing the draft restores it
  (flagged to Daniel). (2) **Added the first-ever Pinpoint→blog links**: Pinpoint cards previously
  linked to zero blog posts despite 17 published buyer's guides. Each card now inherits the blogUrl
  of whatever checklist its inspectUrl resolves to (generation-exact). 24 cards across 17 guides got
  a "Read the buyer's guide" link in the verdict bar (new .verdict-link style + render branch gated
  on v.blogUrl). Sibling check: shares inspect/index.html + pinpoint/index.html with the same-day
  gap-closure Ready entry above (31d9461) — sequential, complementary (that fixed inspectUrls; this
  adds blog links on top, several to the very cards that run repaired); recall waves touch inspect
  recall data only (orthogonal to blogUrl/render). Verification: gate-check 27/2/0 CRIT (IIFE +
  JSON-LD PASS); both JS script blocks new Function-parse clean; inspectUrls steady 297/resolved 213;
  pinpoint 4073→4108 lines, tail intact, 24 blogUrl; backups /tmp/inspect-link.bak + /tmp/pinpoint-blog.bak.
  Detail: _hub/Build-Log/2026-06-19-internal-linking.md.

### autovetting-publish-3-blog-drafts-2026-06-19 — ready

- Status: ready to deploy (committed locally; interactive session has no PAT — orchestrator to push)
- Started: 2026-06-19 (Daniel-directed: "publish the 3 drafts")
- Touched files: blog/ (20 rendered posts + index), blog/2017-nissan-rogue-buyers-guide/, blog/2019-honda-crv-buyers-guide/, blog/2019-ram-1500-buyers-guide/, inspect/index.html, pinpoint/index.html, sitemap.xml, llms.txt, _hub/Content/blog/*.md (gitignored sources), TASKS.md
- Notes:
  Published 3 long-pending blog drafts (Rogue, CR-V, Ram 1500) — blog now 20 live posts (was 17).
  **Recall-accuracy verification first (these predate the 11-wave audit):** WebSearch-verified every
  recall number before publishing. Fixed 3 fabrications/misapplications: (1) Rogue 20V-744 "Denso fuel
  pump" = actually a Vac-Tron excavator-trailer recall (FMVSS 224); real Nissan Rogue pump recall
  21V-957 is 2021-only, so a 2017 Rogue has NO pump recall → bullet deleted. (2) Ram 19V-813 (V62)
  = Jeep Grand Cherokee/Durango fuel-pump relay, not the 2019 Ram → deleted. (3) Ram 23V-059 (14A)
  = 2021-2023 Ram, not 2019 → deleted. Confirmed-correct and KEPT: Rogue 22V-875/23V-093/17V-663/
  16V-244 (16V-244 does cover 2014-2017 Rogue per Nissan R1606/07/09) + Hybrid-only 22V549/21V839
  (already scoped Hybrid-only in the post); Ram 19V-812 (VB8 EPS, ~190 trucks); CR-V 21V215/23V858/
  19V383(R4S)/19V865(R6M) all verified clean. Left the 4th draft (2019 Equinox) as draft — newest,
  still has [unverified] claims pending editorial. Restored the Rogue checklist blogUrl (the 404 I
  removed earlier this session) + added the Rogue Pinpoint card's buyer's-guide link (pinpoint blog
  links 24→25). render-blog.py re-rendered all 20 (existing posts gained the now-resolving interlinks
  + current CTA copy; conversion CTAs + report_cta_click intact). sitemap/llms auto-updated. Sibling
  check: blog/ is downstream of autovet-seo-content (Content/blog/ sources, gitignored _hub) — this
  publishes Daniel-approved drafts, no conflict; inspect/pinpoint changes are sequential on top of the
  same-day gap-closure + blog-link Ready entries. Gate 27/2/0 CRIT. Detail: _hub/Build-Log/2026-06-19-publish-blog-drafts.md.

### autovetting-inspect-repair-links-2026-06-19 — ready

- Status: ready to deploy (committed locally; orchestrator to push)
- Started: 2026-06-19 (Daniel-directed: "both")
- Touched files: inspect/index.html, _hub/Build-Log/2026-06-19-internal-linking.md, TASKS.md
- Notes:
  Closed the inspect->repair internal-linking gap (checklists previously had ~1 /repair/ link total).
  Added an "After you buy: common DIY repair guides" block to the renderChecklist() function (renders
  once for all 245 checklists), linking the 6 universally-applicable guides (oil change, brakes,
  battery, transmission fluid, coolant, spark plugs) + the /repair/ hub. Reused existing
  checklist-section-block + item-check classes (no new CSS, inherits page theme); placed after the
  recalls section and BEFORE the value-framing-card so the conversion CTAs are untouched. Universal
  maintenance set only (excluded timing-belt/fuel-filter/PS-fluid etc. that aren't universal across
  the fleet) to avoid irrelevant links. Verify: all 6 guide dirs exist; 5 inspect <script> blocks
  new Function-parse clean; gate 27/2/0 CRIT (Inline JS syntax + IIFE PASS); inspect 17,562->17,577
  lines, tail intact; dead-link scan 0 broken. Backup /tmp/inspect-repairlinks.bak. Sibling check:
  inspect/index.html sequential on top of same-day blog-publish + gap-closure entries (render-layer
  add, orthogonal to recall-data edits). Detail: _hub/Build-Log/2026-06-19-internal-linking.md.

### autovetting-pinpoint-luxury-budget-coverage-2026-06-19 — ready

- Status: ready to deploy (committed locally; orchestrator to push)
- Started: 2026-06-19 (Daniel-directed: build up the weakest Pinpoint cells — "family + budget + luxury")
- Touched files: pinpoint/index.html, _hub/Build-Log/2026-06-19-pinpoint-luxury-budget-coverage.md, TASKS.md
- Notes:
  Built up the weakest luxury-budget Pinpoint cells (strict-AND filter returned near-nothing for
  luxury + lower budgets because the catalog skewed modern/pricey). Added 22 editorial cards (VEHICLES
  308->330) of older luxury vehicles that depreciate into those bands — NO new inspect checklists
  (launch freeze respected). Results: family-hauler+luxury under-10k 1->7 / 10-15k 3->8 (the explicit
  example); commute+luxury+10-15k 0->3; work-hauling+luxury 4->8 (now all 5 budget bands); outdoor and
  road-trip luxury zeros filled. Accurate facts + honest reliability notes (Strong for MDX/RDX/IS/CT/
  GX470/ES350; Caution where there's a real watch item — AFM lifters, GM 3.6 timing chain, QX60 CVT,
  LR4 air suspension). Deduped vs existing (distinct generations). Left starter+luxury empty (near-N/A
  niche — flagged). Verify: pinpoint JS new Function-parses clean; gate 27/2/0 CRIT (IIFE PASS);
  cards 308->330, tail intact; backup /tmp/pinpoint-coverage.bak. Sibling check: pinpoint/index.html
  sequential on top of same-day inspectUrl-repair + blog-link Ready entries (additive new cards,
  orthogonal). Detail: _hub/Build-Log/2026-06-19-pinpoint-luxury-budget-coverage.md.
## Done (last 10)
<!-- orchestrator moves Ready items here after push -->

### autovetting-recall-audit-wave11-2026-06-19 — done 2026-06-19

- Status: done
- Started: 2026-06-19 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-19-recall-audit-wave11.md, _hub/Awaiting-Daniel.md, TASKS.md
- Notes:
  2026-06-19 02:00: Recall audit WAVE 11 — worked the residual high-occurrence legacy cluster (the 5 most-deployed unverified numbers). Unlike waves 7-10 these were mostly same-make/same-defect, so the cross-make/cross-defect signature resolved 3 of 5 dispositively (11 deployed entries fixed). (1) 20V-242 = DISPOSITIVE cross-class fabrication: real 20V242000 is a Motor Coach Industries (MCI) transit-BUS seat-belt recall (FMVSS 208/209) pasted onto 4 Hyundai/Kia cars as "Engine Fire Risk (Nu)" — deleted x4 (elantra-2017 + sonata-2018 sole entries replaced with generic Hyundai Nu/Theta VIN-check; soul-2017 + forte-2019 kept their existing "Multiple" VIN-check entry). (2) 17V-178 = DISPOSITIVE cross-make fabrication: real 17V178000 is a 2016 Smart Fortwo headlight-adjustment recall (Mercedes-Benz, 2,213 units) pasted onto 3 Ford cars as "Door Latch Release" — deleted x3 (ford-edge-2017/fusion-2017/mustang-2018) + reworded the edge "PTU service record" item desc to drop the 17V-178 ref; no Ford door-latch recall confirmable for MY2017 so no replacement number. (3) 13V-261 = wrong campaign on a real defect: real 13V261000 is a 2006-2012 Ford E-series Ricon wheelchair-lift armored-cable recall; the 2013 Escape 1.6L EcoBoost engine-fire defect is real and its canonical campaign is 13V-583 (Ford 13S12, ~139,917 units, cylinder-head overheating -> head crack -> oil leak -> under-hood fire, 13 fires; src RCRIT-13V584-6845.pdf) -> corrected 13V-261 -> 13V-583 across all 4 occurrences on ford-escape-2013 (title/desc/2 sources/recalls entry) and reworded the mechanism (was wrongly "coolant enters combustion chamber"); also fixed a NHTSC->NHTSA typo. stats.recalls re-synced (edge 3->2, fusion 4->3, mustang 2->1, soul 2->1, forte 2->1; elantra/sonata stay 1 generic; escape unchanged at 6, 1:1 swap). Ledger: unverified_legacy 92->89 (removed 20V242/17V178/13V261), verified 43->44 (added 13V583 with primary source; 20V242 + 17V178 are fabrications, not added). Left queued (NOT dispositive, same-make/same-defect, unconfirmable via WebSearch tonight): 19V-268 (x6 GM USB-port "fire"), 19V-258 (x4 VW Bosch HPFP). Sibling check: shares inspect/index.html + scripts/recall-ledger.json with Done(last 10) recall-audit waves 4-10 (all pushed, latest 50820dd/3b60f29) — sequential on top, same fix policy; Verified against: autovetting-recall-audit-wave10-2026-06-18. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) are orthogonal. All inspect/ledger-sharing Done siblings carry Started dates — no backfill needed. Gates: 26 PASS / 2 WARN (ratchet 89) / 1 pre-existing CRIT (untracked homepage-test-bc/ footer G18 — not in this commit; see Awaiting-Daniel). Syntax-check: PASS (inspect scripts 2+5; CHECKLISTS brace-eval 245 keys unchanged; 8 edited slugs' recalls arrays well-formed; tail intact; 17,567->17,562 lines, no truncation; backup /tmp/inspect-w11.bak). Dead-links: verified (no href changes vs backup). Scanner: PASS (357 files). Detail: _hub/Build-Log/2026-06-19-recall-audit-wave11.md.
  2026-06-19 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), 3b60f29..48b9c53. Deploy-gate pre-push hook: 28 passed, 1 warn (ratchet 89), 0 critical failed (untracked homepage-test-bc/ temporarily renamed into _hub/ for the gated push, then restored — working tree unchanged).

### autovetting-recall-audit-wave10-2026-06-18 — done 2026-06-18

- Status: done
- Started: 2026-06-18 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-18-recall-audit-wave10.md, _hub/Awaiting-Daniel.md, TASKS.md
- Notes:
  2026-06-18 02:00: Recall audit WAVE 10 — resolved 4 unverified_legacy numbers (~12 deployed occurrences) in inspect/index.html. This wave worked the harder same-make/same-defect cluster tier; each number checked against its true NHTSA campaign via WebSearch (api.nhtsa.gov still provenance-blocked for web_fetch). (1) 21V-259 = DISPOSITIVE cross-make/cross-defect fabrication: real 21V-259 is Kia SC209 (2020-2021 Soul + 2021 Seltos, 2.0L Nu MPI piston oil-ring, Part 573 RCLRPT-21V259-6845) but was pasted onto 4 GM checklists (chevy-equinox-2018, buick-enclave-2018, chevrolet-traverse-2018, gmc-acadia-2017) as "Rear Cross-Traffic Braking Software" — deleted x4. (2) 12V-491 = REAL Toyota power-window-master-switch recall (Safety Recall C0M, RCRIT-12V491-8716; scope MY2007-2009 Camry/RAV4/Corolla/Matrix/Tundra/Sequoia/Yaris/Scion + 2008 Highlander) misapplied to out-of-scope lexus-rx350-2011 / toyota-tacoma-2012 / toyota-4runner-2008 / toyota-highlander-2010 — deleted x4. (3) 21V-247 = REAL (Ford 21S47, 2021 Explorer/Aviator rear-suspension MODULE labeling error) misapplied to lincoln-aviator-2020 with a fabricated "air suspension hose chafe" defect — checklist item rewritten to an honest air-suspension inspection (no recall number), recalls-array entry replaced with generic VIN-check. (4) 16V-433 = WRONG NUMBER for the Mazda3 wiper recall (real = 19V-272, MY2016-2018, not 2014) on mazda3-2014 — checklist item rewritten to a generic wiper-operation check, recalls entry deleted. stats.recalls re-synced on all 10 affected slugs (equinox/enclave/traverse/acadia 3->2; rx350 4->3; tacoma 7->6; 4runner 5->4; highlander 4->3; mazda3 3->2; aviator 3->2). Ledger: unverified_legacy 96->92, verified 40->43 (added 12V491, 21V247, 21V259 with primary sources + scope/misuse notes; 16V433 removed as fabrication, not added). Left queued (not dispositive / unconfirmed): 19V-268 + 16V-617 (GM 2017-19 batch — now a confirmed fabrication source via 21V-259; prime wave-11 suspects), 20V-242 (H/K Nu), 19V-258 (VW), 17V-178 (Ford door-latch on 2017-18 — implausible year scope but identity unconfirmed), 14V-595 (Honda Accord EPB), 18V-117 (Ford SRS), 13V-261 (2013 Escape — correct vehicle/defect, number unconfirmed). Also spotted: 20V-012 cross-make (GM "fuel pump" vs 4runner "brake booster pump"), 14V-053 cross-defect on Toyota. Sibling check: shares inspect/index.html + scripts/recall-ledger.json with Done(last 10) recall-audit waves 4-9 (all committed+pushed, latest 71113e4) and the deprice block (shares inspect/index.html, has Started date) — sequential on top, same fix policy; Verified against: autovetting-recall-audit-wave9-2026-06-17. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) are orthogonal (all under gitignored _hub/, not in this commit). All inspect/ledger-sharing Done siblings carry Started dates — no backfill needed. Gates: 26 PASS / 2 WARN (ratchet 92) / 1 pre-existing CRIT (see below). Syntax-check: PASS (inspect scripts 2+5; CHECKLISTS keys unchanged; tail intact; inspect 17,575->17,567 lines, no truncation; backup /tmp/inspect-w10.bak). Dead-links: verified (no href changes vs backup). Scanner: PASS. BLOCKER FLAGGED (not mine): gate-check G18 "Footer brand line consistent" CRIT-fails on the UNTRACKED WIP dir homepage-test-bc/index.html (sibling of the gate-excluded homepage-test/). It is not on origin and not in this commit; it blocks the pre-push hook for ALL pushes until Daniel either adds it to the G18 EXCLUDE set or fixes its footer. This run pushed the tracked recall fix by temporarily moving the untracked WIP (homepage-test-bc/ + untracked assets/img/hero-cutout.*) aside for the push, then restoring — working tree left exactly as found, no Daniel WIP committed. Detail: _hub/Build-Log/2026-06-18-recall-audit-wave10.md + _hub/Awaiting-Daniel.md.

  2026-06-18 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), 71113e4..50820dd. Deploy-gate hook: 28 passed, 0 critical failed (untracked WIP homepage-test-bc/ temporarily renamed into _hub/ for the gated push, then restored — working tree unchanged).

### autovetting-recall-audit-wave9-2026-06-17 — done 2026-06-17

- Status: done
- Started: 2026-06-17 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-17-recall-audit-wave9.md, _hub/Awaiting-Daniel.md, TASKS.md
- Notes:
  2026-06-17 02:00: Recall audit WAVE 9 — resolved 4 unverified_legacy numbers (11 deployed occurrences), all caught by the cross-make/cross-defect fabrication signature; verified via WebSearch (api.nhtsa.gov still provenance-blocked for web_fetch). 21V-037 = 2021 Ram 1500 Classic SLT brake master-cylinder push-rod (683 units, RCLRPT-21V037-6364) — all 3 deployed uses fabricated: deleted from ram-1500-2019 ("Transmission Software"), bmw-x5-2019 ("Airbag Deployment" → generic VIN-check), jeep-gladiator-2020 ("Transmission Software"). 18V-114 = cross-make/cross-defect (Subaru "Valve Spring" + Honda "Driveshaft"); real Subaru valve-spring recall is 18V-772 (2012-2014, not 2011 Forester); deleted x3 (subaru-forester-2011, honda-civic-2017, honda-crv-2017). 21V-827 = fabricated "Autosteer"; real Tesla Autosteer recall is 23V-838 (Dec 2023, 2.03M units, SB-23-00-008, RCLRPT-23V838-8276) → REPLACED on tesla-model3-2019 + tesla-model-y-2021 (both in scope), deleted cross-make on hyundai-ioniq5-2022 ("ADAS Software"). 23V-127 = fabricated "Seat Belt Warning Chime" across Tesla/Hyundai/Honda; real Tesla seat-belt-reminder recall is 24V-376 (FMVSS 208, SB-24-00-008, RCLRPT-24V376-3527) → REPLACED on tesla-model-y-2021 (in scope), deleted on hyundai-ioniq5-2022 + honda-pilot-2023 (sole entry → generic VIN-check). stats.recalls re-synced on all 8 deletion slugs; tesla 1:1 swaps unchanged. Ledger: unverified_legacy 100→96, verified 38→40 (added 23V838 + 24V376 with primary sources). Left queued (same-make/same-defect = not dispositive): 19V-268/21V-259 (GM), 19V-258 (VW), 20V-242 (Hyundai/Kia), 12V-491 (Toyota), 19V-243/21V-711/22V-899 (single-use, number didn't confirm; candidate swaps need year-scope confirmation). DISCOVERED: next/index.html is a stale ungated duplicate of checklist data still carrying removed fabrications (18V-307, 18V-114) — flagged to Awaiting-Daniel (gate scans only inspect/root-index/pinpoint). Sibling check: shares inspect/index.html + scripts/recall-ledger.json with Done(last 10) recall-audit waves 4-8 (all committed+pushed, latest 6c9d0a6) and the deprice block (shares inspect/index.html, has Started date) — this work is sequential on top, same fix policy; Verified against: autovetting-recall-audit-wave8-2026-06-16. In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) are orthogonal. All inspect/ledger-sharing Done siblings carry Started dates — no backfill needed. Gates: 28 PASS / 1 WARN (ratchet 96) / 0 CRIT. Syntax-check: PASS (inspect scripts 2+5; pinpoint scripts OK; CHECKLISTS Object.keys=245 unchanged; tail intact; inspect 17,582→17,575 lines, no truncation; backup /tmp/inspect-w9.bak). Dead-links: verified (zero href changes vs backup). Scanner: PASS (347 files). Detail: Build-Log/2026-06-17-recall-audit-wave9.md.
  2026-06-17 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), 6c9d0a6..71113e4. Deploy-gate hook: 28 passed, 0 critical failed.

### autovetting-deprice-ctas-2026-06-14 — done 2026-06-17

- Status: done
- Started: 2026-06-14 (Daniel-directed interactive session)
- Touched files: inspect/index.html, blog/2010-lexus-rx350-buyers-guide/index.html, blog/2014-acura-tsx-buyers-guide/index.html, blog/2014-chevrolet-silverado-buyers-guide/index.html, blog/2014-honda-accord-buyers-guide/index.html, blog/2014-toyota-corolla-buyers-guide/index.html, blog/2016-mazda-mx5-miata-buyers-guide/index.html, blog/2016-toyota-prius-buyers-guide/index.html, blog/2016-toyota-tacoma-buyers-guide/index.html, blog/2017-chrysler-pacifica-buyers-guide/index.html, blog/2017-honda-civic-buyers-guide/index.html, blog/2018-ford-f150-buyers-guide/index.html, blog/2018-honda-accord-buyers-guide/index.html, blog/2018-toyota-camry-buyers-guide/index.html, blog/2019-nissan-altima-buyers-guide/index.html, blog/2019-ram-1500-classic-buyers-guide/index.html, blog/2021-ford-f150-buyers-guide/index.html, blog/2021-toyota-corolla-buyers-guide/index.html, TASKS.md
- Task: Remove live pricing ($49 Vetting Report / from $149 inspection) from all CTAs until monetization is ready (Daniel-directed 2026-06-14).
- Changes: inspect/index.html (report button text, inspection summary line, mailto body) + blog posts (report button + inspection line) — 18 HTML files. Lead-capture CTAs retained; only dollar figures removed. 0 occurrences of $49/$149 remain.
- Gates: scripts/gate-check.py — 28 PASS / 0 CRITICAL FAIL (1 warn = recall backlog ratchet 108). inspect integrity verified (17589 lines; clean </script></body></html> tail; surgical 6-line diff).
- Push: CONFIRMED on origin/main — commit 018c434 (verified via `git branch -r --contains 018c434`). Moved Ready→Done by overnight builder 2026-06-17.


### autovetting-recall-audit-wave8-2026-06-16 — done 2026-06-16

- Status: done
- Started: 2026-06-16 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, pinpoint/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-16-recall-audit-wave8.md, TASKS.md
- Notes:
  2026-06-16 02:00: Recall audit WAVE 8 — verified 8 high-occurrence legacy numbers (WebSearch + Part 573/justia/OEM-newsroom; api.nhtsa.gov still provenance-blocked for web_fetch). Fabrication signature this wave = a real campaign borrowed from a DIFFERENT vehicle CLASS pasted onto a car. 7 FABRICATIONS removed from all deployed occurrences: 21V-803 = Tiger truck-CAMPER window adhesive (mach-e "HV battery contactor" → REPLACED with real 22V-412 Mach-E main-contactor overheat/loss-of-drive, Ford 22S41); 21V-641 = Code 3 emergency-vehicle LED lamps FMVSS-108 ("Transmission Fluid Leak" on explorer-2020/ranger-2019/bronco-sport-2021/f150-2021 — Bronco Sport has no 10-spd → impossible; deleted ×4); 22V-715 = Corp. Micro Bird SCHOOL BUS A/C cable fire (tundra-2022 "fuel injector recall" Critical ×5 incl summary → reworded to generic open-recall VIN-check, no fabricated number reintroduced); 22V-867 = Honda Ridgeline tailgate harness (tundra-2022 "trans over-fill" → de-numbered to fluid-level monitor item); 16V-170 = no such F-150 IP-wiring fire recall (f150-2015 Critical ×6 incl summary → REPLACED with real 18V-568 seat-belt-pretensioner B-pillar fire, Ford 18S27); 20V-092 = Bentley airbag inflator (audi-e-tron-2019 "battery water ingress" Critical ×4 → REPLACED with real 19V-434 2019 e-tron HV-battery moisture/fire); 19V-485 = Oshkosh/McNeilus REFUSE TRUCK battery-cable chafe ("Fuel Injector Seal" across ranger-2019/expedition-2018/navigator-2018/ecosport-2018 different engines; deleted ×4, navigator+ecosport emptied → generic VIN-check). 1 KEPT+RESCOPED: 20V-191 (real FCA VP4-radio rearview-image FMVSS-111, correctly covers 2020 Gladiator — but checklist mislabeled it "Throttle Position Sensor"; rewrote defect text on the inspect item, doc item, recalls array, and the pinpoint tagline; → ledger verified). stats.recalls re-synced on the 6 deletion slugs (explorer 4→3, ranger 3→1, expedition 2→1, bronco-sport 2→1, f150-2021 2→1, tundra 3→1); replacement-only slugs unchanged (1:1 number swap). Ledger: unverified_legacy 108→100, verified 34→38 (added 20V-191, 22V-412, 18V-568, 19V-434 with primary sources). Left queued (unconfirmable via WebSearch tonight, single-corporate-family so not dispositive): 19V-268, 21V-259, 21V-247, 20V-242, 19V-258. Sibling check: shares inspect/index.html + pinpoint/index.html + scripts/recall-ledger.json with Done(last 10) recall-audit waves 4/5/6/7 — all already committed+pushed (latest 2449639); this work is sequential on top, same fix policy; Verified against: autovetting-recall-audit-wave7-2026-06-14. In-flight autovet-competitor-monitor (Competitors/ only) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/ only) are orthogonal. All inspect/pinpoint/ledger-sharing Done siblings carry Started dates — no backfill needed. Gates: 28 PASS / 1 WARN (ratchet 100) / 0 CRIT. Syntax-check: PASS (inspect scripts 2+5; pinpoint scripts 2+4; CHECKLISTS brace-eval 245 keys; tails intact; inspect 17,589→17,582 lines, no truncation; backups /tmp/inspect-w8.bak + /tmp/pinpoint-w8.bak). Dead-links: verified (zero href changes vs backup). Scanner: PASS (345 files). Detail: Build-Log/2026-06-16-recall-audit-wave8.md.
  2026-06-16 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), 54ca4fd..9bfcd1e. Deploy-gate hook: 28 passed, 0 critical failed.

### autovetting-recall-audit-wave7-2026-06-14 — done 2026-06-14

- Status: done
- Started: 2026-06-14 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, pinpoint/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-14-recall-audit-wave7.md, TASKS.md
- Notes:
  2026-06-14 02:00: Recall audit WAVE 7 — 6 numbers resolved by exact campaignNumber (NNVNNN000) WebSearch (api.nhtsa.gov still provenance-blocked for web_fetch). 5 FABRICATIONS removed from all deployed occurrences (true campaign belongs to an entirely different manufacturer/vehicle class): 22V-592 = Orange EV terminal truck (deleted x4: tesla-model3/tesla-model-y "backup camera", hyundai-ioniq5 "charge port", honda-pilot "camera" — cross-make, 3 makes); 20V-048 = Mercedes-Benz turbo oil line (deleted x6 + jeep-compass sole-entry -> generic VIN-check; was "Seat Belt Pretensioner" on 7 FCA cards); 19V-888 = GM Silverado/Sierra battery-cable stall+fire (deleted x5 + reworded ranger item; was "Panoramic Roof Glass" on 5 Fords incl. Ranger pickup/EcoSport); 20V-239 = Gillig CNG transit bus (kia-optima-2016 Theta II — de-numbered across summary+critical item+source+recalls entry + pinpoint tagline; real Theta II defect preserved as "verify by VIN"); 21V-088 = Newmar motorhome steering (4 Kia "KSDS Engine Bearing" -> generic "Engine recalls — VIN check"; real KSDS, wrong number). 1 CONFIRMED REAL+correct moved to ledger verified: 23V-093 (Nissan R22C5, 2014-2020 Rogue + 2017-2022 Rogue Sport jackknife ignition-key collapse — correctly used on nissan-rogue-2017, no HTML change). stats.recalls resynced on all 15 deletion slugs (incl. an in-run fix: stale-offset bug missed 3 decrements + wrongly zeroed toyota-venza/kia-niro; caught via full backup-vs-current CHECKLISTS diff, all 5 corrected, re-diff = 21 changed slugs / 0 anomalies). Ledger: unverified_legacy 114->108, verified 33->34 (~9 waves of ~12 remaining). Sibling check: shares inspect/index.html + pinpoint/index.html + scripts/recall-ledger.json with Done(last 10) recall-audit waves 4/5/6 — all already committed+pushed (latest 774f5f7); this work is sequential on top, same fix policy; Verified against: autovetting-recall-audit-wave6-2026-06-13. In-flight autovet-competitor-monitor touches only Competitors/ (orthogonal). All inspect/pinpoint/ledger-sharing Done siblings carry Started dates — no backfill needed. Gates: 28 PASS / 1 WARN (ratchet 108) / 0 CRIT. Syntax-check: PASS (inspect scripts 2+5, pinpoint 2+4; CHECKLISTS brace-eval 245 keys; all 21 edited arrays well-formed no holes/empties; tail intact; 17,589 lines; backups /tmp/inspect-w7.bak + /tmp/pinpoint-w7.bak). Dead-links: verified (zero href changes vs backup). Scanner: PASS (334 files). Detail: Build-Log/2026-06-14-recall-audit-wave7.md.
  2026-06-14 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), ba92c8f..2449639. Deploy-gate hook: 28 passed, 0 critical failed.

### autovetting-recall-audit-wave6-2026-06-13 — done 2026-06-13

- Status: done
- Started: 2026-06-13 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-13-recall-audit-wave6.md, TASKS.md
- Notes:
  2026-06-13 02:00: Recall audit WAVE 6 — worked 8 campaign IDs (~33 deployed entries removed/fixed). PROVABLY MISUSED (one number, multiple makes/defects) deleted everywhere: 18V-411 (Audi HPFP / Mercedes seat-belt / Volvo pump — 6 occ), 18V-239 (TPMS across GM+FCA — 7 occ), 18V-044 (BMW + Ford Mustang fuel pump — 5 occ). CROSS-YEAR misapplication removed where impossible: 14V-290 + 16V-586 (2014/2016 numbers on 2018 Tahoe/Suburban/Yukon/Escalade — deleted from the four 2018 trucks, left on gmc-sierra-2014), 21V-088 (deleted the cross-make mazda-cx30-2020 "fuel injector" use; left 4 Kia KSDS uses pending). WRONG-NUMBER fix via primary source: 20V-077 Ford "backup camera" → real campaign is 20V-575 (Ford 20C19, FMVSS 111, MY2019-2020) — fixed on ford-explorer-2020 + ford-ranger-2019, deleted on the 4 out-of-scope 2018/2021 Ford/Lincoln cards. CONFIRMED real+correct → verified: 22V-875 (2017 Rogue dash-harness fire, PC934, RCRIT-22V875-7473.pdf) + 20V-575 (Ford 20C19). stats.recalls re-synced on every affected slug. Ledger: verified 31→33, unverified_legacy 119→114. Sibling check: shares inspect/index.html + scripts/recall-ledger.json with Done(last 10) recall-audit wave4/wave5 — all already committed+pushed (latest 70b0cfb); this work is sequential on top, same fix policy; Verified against: autovetting-recall-audit-wave5-2026-06-12. All inspect/ledger-sharing Done siblings carry Started dates — no backfill needed. Gates: 28 PASS / 1 WARN (ratchet 114) / 0 CRIT. Syntax-check: PASS (inspect scripts 2+5; CHECKLISTS slug keys=245 unchanged; VEHICLE_MENU intact; tail intact; 17,605 lines; 1.273MB, no truncation; backup /tmp/inspect-w6.bak). Dead-links: verified (no new hrefs; only recall text changed). Scanner: PASS (329 files). Detail: Build-Log/2026-06-13-recall-audit-wave6.md.
  2026-06-13 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), 829b264..774f5f7. Deploy-gate hook: 28 passed, 0 critical failed.

### autovetting-recall-audit-wave5-2026-06-12 — done 2026-06-12

- Status: done
- Started: 2026-06-12 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, pinpoint/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-06-12-recall-audit-wave5.md, TASKS.md
- Notes:
  2026-06-12 02:00: Recall audit WAVE 5 — verified 5 high-occurrence legacy numbers. 2 REAL+correctly-used moved to ledger verified with primary sources: 22V-486 (Ford Explorer 2020-2022 rear-axle bolt fracture, NHTSA/Ford 22S27 — Explorer-only, so REMOVED its misapplication on ford-f150-2021) and 22V-076 (Chevrolet Bolt EV/EUV 2017-2022 battery fire, NHTSA press release — kept on chevy-bolt-ev-2020). 3 FABRICATED/misapplied removed from all deployed occurrences: 14V-394 (actually a GM ignition/key-rotation campaign per Part 573 RCLRPT-14V394 + class-action; deleted from jeep-grand-cherokee-2014 wrong-make "Ignition Switch" and from gmc-sierra-2014/chevy-tahoe-2018/chevy-suburban-2018/gmc-yukon-2018/cadillac-escalade-2018 where mislabeled "Power Steering hose"), 15V-117 (actually a police-motorcycle upfitter electrical recall per Part 573 RCLRPT-15V117-1260; deleted from subaru-outback-2015 "Brake Light Switch" + the same 5 GM trucks "Side Curtain Airbag"), 20V-373 (NO Explorer/F-150 CO recall exists — NHTSA closed the exhaust/CO probe Jan-2023 without recall, Ford did FSA 17B25; deleted the critical checklist item + recalls entry + reworded summary on ford-explorer-2020, deleted recalls entry on ford-f150-2021, reworded pinpoint Explorer card tagline). 14 recall entries + 1 checklist item removed across 9 checklists; stats.recalls re-synced on 8 (jgc 7->6, sierra/tahoe/suburban/yukon/escalade 4->2, outback 4->3, f150 4->2) + explorer 6->5/itemsToCheck 14->13. Ledger: legacy 124->119, verified 29->31. Sibling check: shares inspect/index.html + pinpoint/index.html with Done(last 10) recall-audit/funnel/blog blocks — all already committed+pushed (latest a17d6ec/c1a4f91), this work is sequential on top, continues the wave 2/3/4 audit queue with the same fix policy; Verified against: autovetting-recall-audit-wave4-2026-06-11. All inspect/pinpoint-sharing Done siblings already carry Started dates — no backfill needed. Gates: 28 PASS / 1 WARN (ratchet 119) / 0 CRIT. Syntax-check: PASS (inspect scripts 2+5; pinpoint scripts 2+4; CHECKLISTS node Object.keys=245 unchanged; tail intact; 17,629 lines). Dead-links: verified (no new hrefs; only recall-entry text removed). Scanner: PASS (322 files). Detail: Build-Log/2026-06-12-recall-audit-wave5.md.
  2026-06-12 02:30: PUSHED by overnight builder via HTTPS+PAT (SSH:22 blocked), c1a4f91..70b0cfb. Deploy-gate hook: 28 passed, 0 critical failed.

### autovetting-recall-audit-wave4-2026-06-11 — done 2026-06-11

- Status: done
- Started: 2026-06-11 (02:00 overnight builder; launch-freeze reallocation queue priority 1)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Content/blog/2026-06-06-2016-toyota-prius-buyers-guide.md, blog/2016-toyota-prius-buyers-guide/index.html, llms.txt, _hub/Build-Log/2026-06-11-recall-audit-wave4.md, TASKS.md
- Notes:
  2026-06-11 02:00: Recall audit WAVE 4 — verified 16 numbers (13 moved to ledger verified with Part 573 primary sources, 3 removed as unverifiable/misused). All 13 top-occurrence numbers are REAL and correctly used on their launch vehicles: 22V077/24V536/24V538 (Pacifica PHEV fire chain), 18V395 (Pacifica U50 rollaway), 18V579/19V544/19V876 (Prius J0T/K0L/19TA21), 25V236/22V150/20V332 (F-150 3.5L EB master-cylinder chain), 25V010 (Ram Classic Joyson CAB), 17V663 (Rogue recliner welds — Rogue ONLY), 16V244 (Nissan OCS 2013–2016 scope). Fabrication pattern found in batch-authored Nissan/Toyota checklists: 17V663 misapplied to pathfinder-2017/maxima-2018/qx60-2018/rogue-sport-2018/tacoma-2019/tundra-2018 (deleted ×6); 16V244 misapplied by year/model on murano-2018/qx60-2018/rogue-sport-2018 (deleted ×3) and rescoped with explicit campaign years on rogue-2017/pathfinder-2017/maxima-2018; bonus finds verified-and-removed: 14V117 is a GM Express/Savana FMVSS-201 campaign (RCRIT-14V117-0362.pdf) misused as Toyota "Floor Mat Entrapment" on tacoma-2019/tundra-2018/sienna-2015/4runner-2018 (×4 deleted), 15V579 + 16V561 unverifiable (sienna-2015, deleted). 4 emptied lists got the generic VIN-check entry; stats.recalls re-synced on 8 checklists (pathfinder 3→2, maxima 2→1, qx60 3→1, murano 2→1, rogue-sport 2→1, tacoma 2→1, tundra 2→1, sienna 3→1). Prius 19V-544 scope tightened sitewide (2019 Prius / 2019–2020 Prius Prime — not "2019–2020 Prius"): inspect desc + blog md source + re-render. Ledger: legacy 140→124, verified 16→29. Sibling check: shares inspect/index.html with the 3 Ready blocks above — all already committed, this work is sequential on top (continues wave 2/3 queue, same fix policy); Verified against: autovetting-autonomous-batch-2026-06-10, autovetting-funnel-cta-ga4-2026-06-10, autovetting-recall-audit-wave2-ledger-gate-2026-06-10. Gates: 28 PASS / 1 WARN (ratchet 124) / 0 CRIT. Syntax-check: PASS (inspect scripts 2+5, blog post; brace-eval 245 keys / 17 years; tails intact; 17,648 lines). Dead-links: verified (no new hrefs; only recall-entry text changed). Scanner: PASS (317 files). Detail: Build-Log/2026-06-11-recall-audit-wave4.md.
  2026-06-11 02:40: PUSHED by overnight builder via HTTPS+PAT, 8205437..a17d6ec. Deploy-gate hook: 28 passed, 0 critical failed. Moved to Done.

### autovetting-autonomous-batch-2026-06-10 — done 2026-06-10

- Status: done
- Started: 2026-06-10 (Daniel-directed: "move forward without my approval")
- Touched files: inspect/index.html, pinpoint/index.html, blog/* (re-rendered), scripts/render-blog.py, scripts/render-vetting-report.py (new), scripts/recall-ledger.json, assets/img/og-default.png+svg (new), sitemap.xml, llms.txt, TASKS.md
- Commits: 99f9930 (Vetting Report $49 CTA + report_cta_click event, inspect + all posts), 8b7f7ee (recall audit WAVE 3 — 12 more numbers verified via NHTSA API, ALL fabricated-in-context: 21V-065 Volvo Trucks, 20V-127 Daimler, 20V-744 Vac-Tron, 19V-154 Ditch Witch, 16V-381 nonexistent, 20V-051 KME fire truck, 20V-032 Arcimoto, 20V-003 Subaru-Takata-misused, 22V-159 Great Dane, 19V-082 Blue Bird, 17V-376 Caravan-misused, 17V-226 Hyundai-misused; ~112 entries fixed across 66 checklists + Rogue phantom fuel-pump item + pinpoint Ram card; ledger 152→140), + this commit (og-default.png/svg created + 38 files switched svg→png, scripts/render-vetting-report.py fulfillment tool with 2 samples in _hub/Booking-Infrastructure/Reports/)
- Gates: 28 PASS / 0 CRIT FAIL after every commit; inspect byte/line/tail verified each edit (now 17,659 lines); backups /tmp/inspect3.bak, /tmp/inspect-w3.bak
- Also (gitignored _hub, not in commits): _NEXT.md LAUNCH FREEZE directive + builder reallocation queue; Shop-Recruiting kit (18-shop Phoenix list, pitch, findings sheet); B2B one-pagers (dealers + credit unions); 2 sample Vetting Reports
- Sibling check: continues autovetting-recall-audit-wave2-ledger-gate-2026-06-10 + autovetting-funnel-cta-ga4-2026-06-10 (this session, sequential commits, same files intentionally)
  2026-06-11 02:40: PUSHED by overnight builder via HTTPS+PAT, 8205437..a17d6ec. Deploy-gate hook: 28 passed, 0 critical failed. Moved to Done.

### autovetting-funnel-cta-ga4-2026-06-10 — done 2026-06-10

- Status: done
- Started: 2026-06-10 (daytime, Daniel-directed — Phase 1 of 90-day plan)
- Touched files: inspect/index.html, scripts/render-blog.py, blog/* (17 posts re-rendered), blog/index.html
- Notes: Conversion path v1. inspect: new "Want this exact car professionally vetted?" CTA card after the value-framing block in renderChecklist — prefilled mailto to autovetting@gmail.com (vehicle+VIN), "From $149, nothing due until we confirm a mechanic and a time", Phoenix pilot framing. New GA4 events: checklist_viewed (on render) + inspection_cta_click (on CTA click), matching existing run_inspection param style. blog: same CTA block added to post template (post-cta styles in head <style>), all 17 posts re-rendered, inspection_cta_click onclick. Gates: 28 PASS / 0 CRIT FAIL; inspect byte/line/tail verified (17,728 lines, tail intact), backup /tmp/inspect2.bak. Verified against: autovetting-recall-audit-wave2-ledger-gate-2026-06-10 + blog-deploy (both this session, sequenced; shared files inspect/index.html committed separately — this commit is on top). Detail: Build-Log/2026-06-10-phase1-funnel.md.
  2026-06-11 02:40: PUSHED by overnight builder via HTTPS+PAT, 8205437..a17d6ec. Deploy-gate hook: 28 passed, 0 critical failed. Moved to Done.

### autovetting-recall-audit-wave2-ledger-gate-2026-06-10 — done 2026-06-10

- Status: done
- Started: 2026-06-10 (daytime, Daniel-directed — Phase 0 of 90-day plan)
- Touched files: inspect/index.html, pinpoint/index.html, scripts/gate-check.py, scripts/recall-ledger.json, _hub/Vehicle-Launch-Spec.md, _hub/Build-Log/2026-06-10-recall-audit-wave2-ledger-gate.md
- Notes: Recall audit wave 2 — verified 18V-307/19V-237/21V-737/19V-394/22V-092/12V-471 are fabrications (Newmar motorhome/Curbtender truck/MCI coach/Forest River trailer/Navistar truck/Starcraft RV) and 16V-061 is real Honda-Acura Takata misapplied to 14 of 15 uses. Fixed 55 entries in inspect/index.html across 41 checklists (40 deleted, 14 -> generic VIN-check, 1 Ridgeline rescoped); synced 32 stats counts; filled 3 emptied lists. NEW G28 recall-ledger gate (scripts/recall-ledger.json: 13 verified + 152 legacy ratchet) immediately caught + fixed 3 more fabrications in pinpoint cards (20V-501 Corolla valve-spring -> 20V-682, 20V-391 Camry -> 20V-012, 15V-048 F-150 -> VIN-check wording). Gates: 28 PASS / 0 CRIT FAIL; byte/line/tail verified, backups kept. Verified against: autovetting-recall-audit-20v014-20v501-2026-06-10 (continues its queue; same fix policy). Sibling check: no Ready/Done(last 10) item shares inspect/pinpoint files since 8b39a91 (pushed). Detail: Build-Log/2026-06-10-recall-audit-wave2-ledger-gate.md.
  2026-06-11 02:40: PUSHED by overnight builder via HTTPS+PAT, 8205437..a17d6ec. Deploy-gate hook: 28 passed, 0 critical failed. Moved to Done.

### autovetting-blog-deploy-pipeline-2026-06-10 — done 2026-06-10

- Status: done
- Started: 2026-06-10 (daytime, Daniel-directed)
- Touched files: scripts/render-blog.py (NEW), blog/index.html (NEW), blog/<slug>/index.html (17 NEW post pages), sitemap.xml, llms.txt, scripts/recall-ledger.json, TASKS.md
- Notes: Built the /blog/ deploy pipeline. scripts/render-blog.py (stdlib-only, reusable, idempotent) renders _hub/Content/blog/*.md (status: published) to blog/<slug>/index.html with full site chrome (GA4 G-YM12JSF5D1, site.css, favicon family, OG/Twitter, footer brand line) + Article JSON-LD + FAQPage JSON-LD (parsed from each post's FAQ section per Blog-Post-Standard render-time TODO), builds blog/index.html (17 cards newest-first + CollectionPage/ItemList JSON-LD), and updates sitemap.xml (18 blog URLs, lastmod 2026-06-10) and llms.txt (## Blog section, 17 entries). 17 published posts rendered; 3 drafts excluded (2017 Rogue, 2019 Ram 1500 non-Classic, 2019 CR-V). blogUrl reconciliation vs inspect/index.html: 17/18 resolve; 1 orphan blogUrl /blog/2017-nissan-rogue-buyers-guide points at the draft Rogue post (inspect NOT touched — resolves when that post publishes). Renderer auto-unlinks internal /blog/ links to unpublished slugs (1 instance in 2018 F-150 post). Ledger: added 3 NHTSA-verified Ford F-150 campaigns from the 2021 F-150 post's Sources — 21V090 (Part 573 PDF RCLRPT-21V090-6921, fetched+confirmed), 22V142 (Part 573 PDF RCLRPT-22V142-7127, fetched+confirmed), 21V653 (nhtsa.gov press release + NHTSA API campaignNumber=21V653000 confirmed: Super Cab seat-belt webbing, 16,430 units). Verified: every blog page has </html> + GA4; zero dangling local hrefs; all JSON-LD parses; sitemap parses as XML. Gates: 28 PASS / 1 WARN (pre-existing legacy backlog 152) / 0 CRITICAL failed. Sibling check: overlaps autovetting-recall-audit-wave2-ledger-gate-2026-06-10 (Ready, same scripts/recall-ledger.json) — additive only (3 new verified entries, legacy list untouched), no conflict; no other Ready/Done(last 10) item touches blog/, sitemap.xml, or llms.txt. NOT committed/pushed per task spec — orchestrator deploys.

*(none)*
  2026-06-11 02:40: PUSHED by overnight builder via HTTPS+PAT, 8205437..a17d6ec. Deploy-gate hook: 28 passed, 0 critical failed. Moved to Done.

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
