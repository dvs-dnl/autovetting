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
  2026-06-25 02:00: profiled Carfax (S&P Global Mobility) (🔴 STRATEGIC THREAT).
    Output: Competitors/_Monitor/2026-06-25-carfax.md; appended to Awaiting-Daniel.md (🔴 escalation, dated 2026-06-25 block).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal; Ready = vinnote-batches on inspect/index.html (orthogonal); Done(last 10) = recall-audit waves 9-11 + deprice-CTAs, none touch Competitors/ and none position an AutoVet feature against Carfax specifically. No Re-sync needed.
    Key delta: TWO inspection/forward-looking moves from our most-likely acquirer, both hitting AutoVet's claimed white space. (1) Carfax "Future Reliability" (Apr 7 2026): FREE, consumer-facing, VIN-SPECIFIC forward reliability prediction, top of every report under a new "Past/Present/Future" header -> invalidates our "Carfax=what happened, AutoVet=what happens next" line. (2) Carfax x UVeye integration (Jun 23 2026): AI computer-vision condition inspection (tires/underbody/exterior) + Carfax service/recall data in one workflow, B2B/dealer service-lane only for now -> the "inspection layer + history" bundle the biz plan assumed required acquiring AutoVet; Carfax is renting it via partnership. Converges two tracked competitors (#6 Carfax + #10 UVeye).
    Implication: re-message Carfax contrast (records/paper-trail vs. actual-car-condition + independence + booking); revisit acquirer thesis 9/13 ("Carfax lacks inspection tech" now weaker); set standing watch for any consumer-facing surfacing of Carfax x UVeye condition data. Homegrown badge (May 2026) = 🟢 supporting evidence for our "independent vs dealer-captured" angle, no action. Decisions a/b/c queued in Awaiting-Daniel.
    Weekly milestone: DONE — intel ready for Daniel's review; 🔴 Awaiting-Daniel append complete (required before Done for 🔴 severity). Next in rotation: CarGurus (#7) [AI search rollout / inspection or trust-layer launches].

  2026-06-28 06:40: profiled CarGurus (#7) (🟡).
    Output: Competitors/_Monitor/2026-06-28-cargurus.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Kia run 06-28) + autovet-seo-content (Content/blog/) orthogonal; Ready empty; Done(last 10) = vinnote-batches on inspect/index.html (06-25..06-28) + recall-audit — none touch Competitors/ and none position an AutoVet feature against CarGurus. No Re-sync needed.
    Key delta: BASELINE — CarGurus had no dedicated profile (only marketplace-embedding white-space mentions in Competitor_Analysis.md §White Space Dim 4). Deltas: (1) completed CarOffer/Digital-Wholesale wind-down (abandoned 2025-12-31) — narrowing to AI SaaS, RETREATING from services/inspection. (2) AI conversational search shipped (mid-2025) + expanded 2026-02-11 with CarGurus Discover (AI shopping assistant) + Dealership Mode ("pros/cons" + "unbiased recommendation," dealer-lot-scoped). (3) Q1'26 healthy: rev $244M +15% YoY, adj EBITDA $80.2M/33%, $175M buyback; FY margin guided down 1.5-2.5pts. NO inspection/condition product, NO native per-VIN recall/reliability layer (still hands off to paid CARFAX links) -> AutoVet white space Dim 1-4 intact.
    Implication: embedding thesis REINFORCED not threatened (CarGurus = better discovery front door = better embed target for condition+booking back end). Watch "unbiased recommendation" framing (nearest advisory encroachment, but dealer-captured -> strengthens AutoVet "independent" angle). Escalation trigger to 🔴 = if Discover/Dealership Mode begins surfacing native per-VIN condition/reliability/recall data. Housekeeping: add CarGurus + Cars.com/AutoTrader as named "Marketplace/channel" archetype block in Competitor_Analysis.md (same gap flagged for Bumper 06-18).
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Cars.com (#8) [AI search rollout / inspection or trust-layer launches].

  2026-07-02 03:00: profiled Cars.com (Cars Commerce, #8) (🟡).
    Output: Competitors/_Monitor/2026-07-02-cars-com.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Mazda next) + autovet-seo-content (Content/blog/) orthogonal; Ready empty; Done(last 10) = vinnote-batch-2026-07-01 (genesis-gv80/kia-sorento/kia-telluride in inspect/index.html) + prior vinnote batches + recall-audit — none touch Competitors/ and none position an AutoVet feature against Cars.com. No Re-sync needed.
    Key delta: BASELINE — Cars.com had no dedicated profile (only marketplace white-space mentions in Competitor_Analysis.md § point-of-sale + White Space Dim 4). Deltas: (1) Carson™ consumer AI shopping engine (2025-11-06) — open-text natural-language search, Cars.com's direct analogue to CarGurus Discover; users 2x return / 3x saves / +30% SRP→VDP / 2x leads. (2) VIN-specific AI video ad solution (announced 2026-04-27) — dealer-facing demand-gen, 47% influenced-sales lift; ad-tech, not condition/trust. (3) Q1'26 stable: rev $180.2M +1% YoY, net income $5.0M, adj EBITDA $51.0M/28.3%; FY26 flat-to-+2% — growing far slower than CarGurus (+15%). NO consumer inspection/condition product, NO native per-VIN reliability/recall layer (still just NHTSA VIN lookup on cars.com/recalls). Closest adjacency = Accu-Trade VIN appraisal, but that's DEALER-side trade valuation + a 2022 asset, not buyer PPI — AutoVet white space Dim 1/2/4 intact.
    Implication: embedding thesis REINFORCED (same conclusion as CarGurus 06-28) — marketplace = AI discovery front door (Carson) + VIN demand-gen; AutoVet = condition/recall/booking back end. VIN-granular infra across all marketplaces = good embed plumbing but the axis to watch. Escalation trigger to 🔴 = if Carson/VDP surfaces native per-VIN condition/reliability/recall beyond the NHTSA link, or Accu-Trade condition scoring goes consumer-side. Housekeeping (repeat of 06-18/06-28): add Cars.com + CarGurus + AutoTrader as a named "Marketplace/channel" archetype block in Competitor_Analysis.md — still open.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: AutoTrader (Cox Automotive) (#9) [Cox-wide acquisitions / any inspection-layer signals].

  2026-07-09 04:00: profiled AutoTrader (Cox Automotive, #9) (🟡).
    Output: Competitors/_Monitor/2026-07-09-autotrader-cox.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lexus) + autovet-seo-content (Content/blog/) orthogonal; Ready empty; Done(last 10) = vinnote-batches 2026-07-07/07-08 on inspect/index.html (subaru-impreza/toyota-4runner/honda-fit spec fixes) + recall-audit — none touch Competitors/ and none position an AutoVet feature against AutoTrader/Cox. No Re-sync needed.
    Key delta: BASELINE — AutoTrader/Cox had no dedicated profile (only "acquirer not competitor" note in Competitor_Analysis.md). Deltas: (1) AutoTrader "AI Mode" consumer conversational shopping (NADA 2026, live inventory + KBB insights, filter pre-fill) — the Cox analogue to CarGurus Discover (06-28) / Cars.com Carson (07-02); leans on KBB valuation, NO native per-VIN condition/reliability/recall. (2) KBB ICO AI Remote Damage Assessment + Dynamic Condition Quiz ("coming soon," NADA 2026) — AI condition-from-CONSUMER-PHOTOS, but it is the trade-in/sell-side funnel (seller getting an appraisal), NOT buyer PPI; still the closest acquirer-tier condition-AI building block yet. (3) Cox full ownership of AiM (2025-09-08) — ~700 physical wholesale-inspection staff into Manheim; Cox now OWNS physical inspection. (4) vAuto x UVeye AI service-lane inspection (2026) — UVeye now inside BOTH acquirer ecosystems (Carfax 06-25 + Cox/vAuto); B2B service-lane only. (5) Fullpath acquisition = marketing CDP, orthogonal 🟢.
    Implication: embedding thesis REINFORCED (AI Mode = better discovery front door, no condition back end = embed target). Acquirer thesis MODESTLY WEAKENED — "Cox lacks inspection tech" now weaker (owns AiM + building KBB condition-AI + UVeye in-ecosystem); but ALL Cox condition AI points sell-side/dealer/wholesale, NOT buyer-side — AutoVet buyer-PPI white space intact. Re-anchor messaging on buyer-side + independence + booking, NOT "unique AI condition." Escalation to 🔴 = KBB/vAuto condition AI surfaced buyer-side on an AutoTrader VDP, or Cox acquires a consumer PPI company. Housekeeping (repeat 06-18/06-28/07-02): add "Marketplace/channel" archetype block (AutoTrader+CarGurus+Cars.com) to Competitor_Analysis.md — still open.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: UVeye (#10) [funding / new partnerships / any consumer-facing moves — currently B2B-only; note UVeye now appears in both Carfax and Cox ecosystems].

  2026-07-29 16:40: profiled UVeye (#10) (🟡 — high side; first standalone profile).
    Output: Competitors/_Monitor/2026-07-29-uveye.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Acura done 07-29, next=Infiniti) + autovet-seo-content (Content/blog/) orthogonal; Ready empty; Done(last 10) = vinnote-batches on inspect/index.html (07-29 = prius-prime/cx5/xt5) — none touch Competitors/ or position AutoVet against UVeye. No Re-sync needed.
    Key delta: Scan to Sold (launched 2026-06-02, adoption expanding through Jul) = UVeye's FIRST buyer-VISIBLE surface — drive-thru scan auto-generates retail listing assets (AI-polished photos, 360° video, interior imagery) pushed via Cox vAuto IMS to online listings shoppers browse; CEO quote: "extends the trust... to the shoppers browsing the same vehicles online." Shopper sees scan-derived IMAGERY, not the condition/defect report → 07-09 🔴 trigger brushed, NOT tripped. Also: Subaru of America OEM partnership (NADA 2026; 600+ retailers; OEM programs now GM/Toyota/BMW/Subaru); $191M Series D ext (Oct 2025, Woven Capital = Toyota's fund; ~$380.5M total; CarMax/GM also on cap table); scale 1,000+ systems / 3.5M vehicles/mo; Amazon + JLR named customers; MVT trucking deal 🟢; repositioned as "vehicle data intelligence" platform (inspection→recon quotes→BDC→merchandising).
    Implication: buyer-side PPI white space intact (UVeye sells nothing to buyers; every scan dealer/seller-side) but narrowing at the retail surface — write the "seller-provided imagery ≠ independent inspection / paid by you, not the dealer" counter-positioning before scan-derived listing "transparency" normalizes. Acquirer thesis: "they'd need to buy AutoVet for inspection tech" now dead (UVeye = condition layer in BOTH acquirer ecosystems, Toyota-funded); live rationale = buyer-side funnel + independence + booking. Refined 🔴 triggers in profile: shopper-facing condition DATA (not imagery) on any consumer surface incl. Carfax reports (Forbes 06-23 "won't immediately" = the tell); any buyer-orderable UVeye product. Housekeeping: add UVeye to Competitor_Analysis.md as "condition-data supplier / acquirer-ecosystem layer" archetype when the marketplace-archetype block (open since 06-18) is written.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Self Inspection (#11) [funding follow-ons, product evolution].


  2026-07-30 01:10: profiled Self Inspection (#11) (🟡 — high side; BASELINE profile, none existed — prior record = Business Plan §3 seed-round line only).
    Output: Competitors/_Monitor/2026-07-30-self-inspection.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Infiniti) + autovet-seo-content (Content/blog/) orthogonal; Ready empty; Done(last 10) = vinnote-batches on inspect/index.html (07-29 = prius-prime/cx5/xt5) — none touch Competitors/ or position AutoVet against Self Inspection. No Re-sync needed.
    Key delta: $10M strategic round 2026-07-16 LED BY SHERYL SANDBERG (Sandberg Bernthal Venture Partners) + strategics U.S. AutoForce (tires) and Westlake Financial (doubling down from Feb-2025 $3M seed; ~$13M total). Repositioned as "System of Record for Vehicle Condition" / new "Vehicle Condition Intelligence" category — CEO quote is the explicit Carfax-analog play ("Vehicle history became standard… vehicle condition is going the same way"). Scale: 1M+ inspections; Stellantis Financial Services customer (lease-end + corp fleet); phone-only capture + AI damage/repair-cost detection + expert-review layer + OBD2; 7 B2B verticals incl Tires (explains AutoForce check) and MARKETPLACES — marketplace product delivers condition reports TO BUYERS pre-purchase (further across the buyer-visible line than UVeye Scan-to-Sold imagery, 07-29) but seller/platform-commissioned, photo-based, no physical PPI, not buyer-orderable. NA + Europe expansion funded.
    Implication: buyer-side PPI white space intact but narrowing from a THIRD direction (UVeye=dealer hardware, Cox=sell-side KBB AI, Self Inspection=lender/marketplace software rails + Sandberg-amplified "condition = the new history report" narrative). Counter-positioning piece ("seller-provided condition report ≠ independent inspection — paid by you, not the dealer") now MORE urgent — second consecutive week this surfaced. Physical-inspection moat holds (no underbody/lift/test-drive from photos+OBD2). Lender channel (biz plan §3 note) now has an entrenched default. 🔴 triggers set in profile: buyer-orderable product; "Self Inspection Verified" on a major consumer marketplace at browse level; acquirer-ecosystem integration (Carfax/Cox); consumer-PPI marketing. Housekeeping: add to Competitor_Analysis.md as "condition-data software rail" when archetype block (open since 06-18) is written; Business Plan §3 + funding table now stale ($3M → +$10M).
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: VINsight.ai (#12) [competitive direct comparison; what they're shipping].

  2026-08-03 16:20: profiled VINsight.ai (#12) (🟡 — low side; BASELINE first-hand review, no prior _Monitor profile).
    Output: Competitors/_Monitor/2026-08-03-vinsight-ai.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. Ready = autovetting-recall-audit-wave15-2026-08-03 (inspect/index.html + scripts/recall-ledger.json + gitignored _hub Build-Log/Landing-Page) — orthogonal, this run wrote only to Competitors/_Monitor/ + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, INFINITI done 08-03, next=Volkswagen) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10) = recall-audit waves 13/14 + decision-execution 07-30 + vinnote batches — none touch Competitors/ and none position an AutoVet feature against VINsight. No Re-sync needed.
    Key delta: THE DELTA IS A CORRECTION TO OUR OWN RECORD, not a competitor move — nothing at VINsight changed. Competitor_Analysis.md §4 describes a company that does not exist as written. §4 calls VINsight.ai "the most directly comparable competitor," buyer-facing, synthesizing "VIN data, NHTSA recalls, and vehicle history" for "tech-forward used car buyers," threat=Medium. Actual site (verified 2026-08-03): meta-description on every page reads "AI-powered vehicle inspection and damage analysis for DEALERS AND RESELLERS"; homepage = "repair estimates for smarter dealership decisions"; the three shipped features are Damage Detection (photo scratches/dents/panel/corrosion), Instant Estimates (parts/labor/overhead repair cost), Market Insights (VIN profit margin + regional demand) = a dealer RECON-COST/MARGIN tool. NO recall layer, NO reliability layer, NO checklist, NO booking, NO buyer product, NO pricing page anywhere. Solo founder Robert Billings (About page is first-person singular). Traction signals ALL NULL: no funding (no Crunchbase/Tracxn record), no press, no reviews (G2/Capterra/SoftwareWorld hits are the NZ WINERY SaaS — name collision), no LinkedIn company page, no named customers, no job postings, footer still © 2025. Threat Medium -> LOW; not a competitor at all (different buyer, different job).
    Incidental finds: (a) vinsight.dev "Live Vehicle Intelligence" — separate near-identical name, OBD2 score cards for "rental fleets, dealerships, and BUYERS"; relationship to vinsight.ai unconfirmed, page client-rendered and unretrievable, marked [unverified], carried forward. (b) VINspectorAI (vinspectorai.com, launched 2025-09-10, Chicago, CEO Nicolas Bogdan) — consumer-facing AI VIN-HISTORY verification w/ risk scores + "hidden accident detection," free tier; closer to AutoVet's buyer-facing positioning than VINsight.ai actually is, but records-derived (Carfax/Bumper archetype), self-published PR only, no independent coverage — queued for slot #13.
    Implication: (1) AutoVet now has NO known direct competitor — §4 was the last name carrying a "direct overlap" label; every tracked player sits on the seller/dealer/lender/marketplace side, buyer side uncontested. (2) THIRD CONSECUTIVE WEEK the same conclusion: the moat is WHO PAYS, not AI. VINsight is the cheapest proof — one engineer shipped damage-detection-from-photos alone; AI condition analysis is not defensible and must not be the headline claim. The counter-positioning copy ("a seller-provided condition report is not an independent inspection — you paid for this one") flagged 07-29, 07-30 and now 08-03 is the highest-leverage unwritten asset in this workstream. (3) Strike the partnership/acqui-hire framing in §4. (4) DATA-QUALITY NOTE: §4 was written from inference not from the site — its own hedges ("Appears to be," "Likely targeting," "unclear / likely absent") hardened into a confident Medium rating; same failure mode the recall audit has been unwinding all summer. Spot-check CarEdge/Autocheck/RepairPal against live sites during the archetype rewrite.
    Housekeeping queued: rewrite Competitor_Analysis.md §4 + matrix row ~line 292 (Medium -> Low, dealer-side, no checklist/booking/education — note this removes the last "Yes/Likely" row opposite AutoVet's core dimensions and strengthens the "Reading the matrix" para at line 299); the "Marketplace/channel" archetype block OPEN SINCE 06-18 (6 weeks, 5 profiles) should be upgraded to a restructure BY SIDE OF THE TRANSACTION (seller-side condition suppliers UVeye/Self Inspection/VINsight | records Carfax/Bumper/VINspectorAI | marketplaces CarGurus/Cars.com/AutoTrader | buyer-side AutoVet, alone); recommend RETIRING slot #12 and replacing it with a standing buyer-side-encroachment sweep.
    Retrieval gaps: vinsight.ai/report?vin=... (sample report — the only page showing actual output quality) and vinsight.dev are client-rendered, returned empty bodies to web_fetch; Chrome escalation attempted and BLOCKED by site permissions in scheduled-run context. Both left [unverified] rather than guessed.
    🔴 triggers set in profile: buyer-facing product / consumer pricing; institutional funding or a team beyond the founder; marketplace or acquirer-tier integration; addition of an NHTSA recall or reliability layer; vinsight.dev shipping a buyer-orderable OBD2 product.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: #13 New entrants (start with VINspectorAI). #13 CLOSES THE FIRST FULL ROTATION CYCLE -> that run must also generate Competitors/_Monitor/QUARTERLY-SUMMARY-2026-Q3.md.

  2026-08-06 01:09: profiled #13 New entrants (🟡) — VINspectorAI first-hand + GetVIN baseline + 30-day funding scan. CYCLE 1 COMPLETE (13/13).
    Output: Competitors/_Monitor/2026-08-06-new-entrants.md + Competitors/_Monitor/QUARTERLY-SUMMARY-2026-Q3.md (rotation-complete quarterly, per task spec). No Awaiting-Daniel append — not 🔴.
    Sibling check: no overlaps. Ready = recall-audit waves 16/17/18 (inspect/index.html + scripts/recall-ledger.json, pushed directly) — orthogonal, this run wrote only Competitors/_Monitor/ + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Volkswagen) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10) = recall-audit/decision-execution/vinnote — none touch Competitors/. No Re-sync needed.
    Key delta: VINspectorAI (vinspectorai.com, launched 2025-09-10, Chicago) = first CONSUMER-buyer-facing AI entrant reviewed first-hand — records-derived "AI That Finds What Carfax Misses," $12.95 consumer / $5.90 dealer-volume vs Carfax $39.99, free VIN + free RECALL CHECK tier, Good Buy/Caution/High Risk verdicts. Real finding = SEO-surface collision: they ship a free 50-point interactive inspection-checklist page + printable PDF, per-state VIN pages, and a Vehicle Stats hub (NHTSA complaints/recalls by brand/model) — programmatic SEO against AutoVet's exact content queries. Traction near-null (TrustPilot 3 reviews vs "5M+ reports" claim; no funding/press). NO physical inspection, NO booking. GetVIN (get.vin, ~Oct 2025) = second records entrant, resells CARFAX+NMVTIS+auction photos w/ AI chat over report; active daily; Low. Funding scan: NOTHING new in 30 days beyond Self Inspection $10M (already profiled 07-30) — no funded buyer-side PPI entrant exists anywhere (Tracxn category census confirms all B2B). vinsight.dev still client-rendered/[unverified], carried forward.
    Implication: buyer-side white space intact after full 13-slot census — FOURTH consecutive week: moat = WHO PAYS, not AI. New pressure is top-of-funnel (records AI colonizing checklist/recall-check SERPs at $0-13) — recall-audit accuracy is the competitive counter, and the independence counter-positioning page ("seller-provided report ≠ independent inspection, paid by YOU") is now flagged 4 runs straight = highest-leverage unwritten asset. Quarterly summary consolidates: acquirer thesis §9/§13 needs rewrite (Carfax/Cox can rent/build condition tech; surviving rationale = buyer funnel + independence brand + booking); Competitor_Analysis.md restructure by SIDE OF TRANSACTION now has full census.
    🔴 tripwires consolidated in QUARTERLY-SUMMARY-2026-Q3.md (Carfax consumer condition data; Cox buyer-side; marketplace "Verified" badges; any funded buyer-paid entrant; records player bundling PPI booking).
    Weekly milestone: DONE — intel + quarterly ready for Daniel's review. Next in rotation: Lemon Squad (#1, CYCLE 2) [carry-forward: verify Wrench consolidation status + Lemon Squad Live traction]. Recommendation standing: retire slot #12 (VINsight, not a competitor) -> standing buyer-side-encroachment sweep.

### autovet-cpo-protocol-ingestion

- Status: in flight
- Task: weekly OEM CPO protocol ingestion (one manufacturer/week) into Product/CPO-Protocols/
- Notes:
  2026-06-14 09:34: ingested Nissan CPO protocol (167 inspection points; also 139 EV / 84 Certified Select tiers).
    Output: Product/CPO-Protocols/nissan-certified.md, Product/CPO-Protocols/_runs/2026-06-14-nissan.md.
    Sibling check: no true conflict. In-flight autovet-competitor-monitor touches Competitors/ only (orthogonal). Verified against / cross-referenced to: autovetting-recall-audit-wave7-2026-06-14, autovetting-recall-audit-wave6-2026-06-13, autovetting-recall-audit-wave4-2026-06-11 — those waves verified Nissan campaigns 23V-093 / 22V-875 / 17V-663 (Rogue-only) / 16V-244 (2013-2016 OCS) in inspect/index.html + scripts/recall-ledger.json; this protocol file is upstream and reuses those verified IDs (complementary, not conflicting). No Re-sync needed.
    Weekly milestone: DONE — nissan-certified.md saved + INDEX.md updated; protocol ready for downstream consumption (overnight-builder / content-checklist authoring). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Hyundai.

  2026-06-21 09:00: ingested Hyundai CPO protocol (173 inspection points; also 179 for EV/PHEV/HEV).
    Output: Product/CPO-Protocols/hyundai-certified.md, Product/CPO-Protocols/_runs/2026-06-21-hyundai.md.
    Sibling check: no true conflict. In-flight autovet-competitor-monitor (Competitors/) + autovet-seo-content (Content/blog/) are orthogonal. Cross-referenced to: autovetting-recall-audit-wave11-2026-06-19 (which deleted the 20V-242 Hyundai/Kia fabrication — this protocol reuses only verified Hyundai engine campaign IDs: Theta II KSDS/15V-568/17V-226/20V-746, Nu 2.0L 21V-301, ABS-fire 23V-651/20V-061 — and explicitly flags 20V-242 not to reintroduce). Protocol is upstream of inspect/ checklists = complementary. Noted for next (Kia) run: autovetting-vinnote-batch Ready blocks touched Kia Sportage 2023 (no overlap with this Hyundai file).
    Weekly milestone: DONE — hyundai-certified.md saved + INDEX.md updated (P0 now Toyota→Honda→Ford→Chevrolet/GM→Nissan→Hyundai ✅; next = Kia, last P0). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Kia.

  2026-06-28 09:00: ingested Kia CPO protocol (165 inspection points standard / 135 points CPO Lite tier).
    Output: Product/CPO-Protocols/kia-certified.md, Product/CPO-Protocols/_runs/2026-06-28-kia.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists. Cross-referenced to: autovetting-vinnote-batch-2026-06-28 (Done; touched kia-stinger-2022 in inspect/index.html with an 8AT spec fix) — complementary, this protocol covers Optima/K5, Sorento, Soul (not Stinger), no overlap. In-flight autovet-competitor-monitor (Competitors/) + autovet-seo-content (Content/blog/) orthogonal; Ready empty. Reused only WebSearch-verified Kia campaign IDs: 16V-514 + 17V-224/SC147 (Theta II KSDS 15yr-150k), 21V-259/SC209 (Soul/Seltos Nu engine fire), 23V-877 (HECU park-outside fire); explicitly flagged 20V-242 NOT to reintroduce (deleted in recall-audit wave 11). No Re-sync needed.
    Weekly milestone: DONE — kia-certified.md saved + INDEX.md updated. P0 ROTATION COMPLETE (Toyota→Honda→Ford→Chevrolet/GM→Nissan→Hyundai→Kia ✅). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Subaru (first P1).

  2026-06-28 22:38: ingested Subaru CPO protocol (152 inspection points; single-tier program, no lite tier).
    Output: Product/CPO-Protocols/subaru-certified.md, Product/CPO-Protocols/_runs/2026-06-28-subaru.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists. No In-flight/Ready task is launching a Subaru vehicle (grep of TASKS.md for subaru/outback/forester/crosstrek/impreza/ascent/legacy/wrx found only the BRZ vinnote note + recall-audit references, no active Subaru launch). Cross-referenced to: autovetting-recall-audit-wave9-2026-06-17 (established 18V-772 as the REAL valve-spring recall, deleted fabricated 18V-114), wave5-2026-06-12 (deleted 15V-117 mis-pasted on Outback), wave3 (20V-003 Subaru-Takata-misused), and the 2026-06-10 audit (21V-587 WRG-21 fuel pump verified for Impreza/Legacy/Outback; deleted 20V-501 / 18V-307 Subaru fabrications). Protocol reuses ONLY WebSearch-verified IDs (21V-587/WRG-21, 19V-744/WUP-01, 18V-772, 16V-694/WTK-71, by-VIN Takata) and embeds an anti-fabrication guard listing the deleted IDs not to reintroduce. In-flight autovet-competitor-monitor (Competitors/) + autovet-seo-content (Content/blog/) orthogonal; Ready empty. No Re-sync needed.
    Weekly milestone: DONE — subaru-certified.md saved + INDEX.md updated (P1 now Subaru ✅; next = Mazda). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Mazda (P1).

  2026-07-05 08:30: ingested Mazda CPO protocol (160 inspection points; single-tier program, no lite tier).
    Output: Product/CPO-Protocols/mazda-certified.md, Product/CPO-Protocols/_runs/2026-07-05-mazda.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists. No In-flight/Ready task is launching a Mazda vehicle (grep of TASKS.md for mazda/cx-5/cx-9/cx-30/mazda3/mazda6/miata/mx-5 found only: vinnote-batch-2026-07-05 which PRUNED a stale mazda3-2019 row (already populated) + a mazda-cx30-2020 vinNote batch (07-02) + the older mx-5-nd launch + recall-audit references — all touch inspect/index.html, none launch a Mazda checklist that would consume this Mazda protocol). Cross-referenced to (WebSearch-verified IDs reused): recall-audit wave 6/10 + the 2026-06-10 systemic audit — 19V-272 (correct Mazda3 wiper, NOT 16V-433), 21V-875/Mazda 5321K (Denso fuel pump MY2018-2019 CX-5/Mazda3/CX-9/Mazda6/MX-5), 20V-346/Mazda 4420F (CX-30 brake caliper bolts). Protocol embeds an anti-fabrication guard listing the deleted/mis-pasted IDs NOT to reintroduce (16V-433, 21V-088, 20V-501, 18V-411/18V-307). In-flight autovet-competitor-monitor (Competitors/, next=AutoTrader) + autovet-seo-content (Content/blog/) orthogonal; Ready empty. No Re-sync needed.
    Weekly milestone: DONE — mazda-certified.md saved + INDEX.md updated (P1 now Subaru ✅ → Mazda ✅; next = Lexus). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Lexus (P1).

  2026-07-29 (backfill note): DISCOVERED the 2026-07-12 run wrote a complete lexus-certified.md (161 points, L/Certified single tier) but terminated before ALL bookkeeping — no _runs summary, no INDEX.md entry, no TASKS.md note (siblings through 07-29 still said "next=Lexus"). File verified complete (121 lines, sources + anti-fabrication guard intact); content NOT modified. Backfilled 2026-07-29: INDEX.md entry, _runs/2026-07-12-lexus.md (marked BACKFILLED), this note. Open Lexus flags carried forward: 70k-vs-80k eligibility ceiling unresolved; Techstream dependency. Lexus milestone now DONE as of 2026-07-29.

  2026-07-29 16:05: ingested Acura CPO protocol (182 inspection points Precision Certified / 167 EV / 112 Precision Used lite tier).
    Output: Product/CPO-Protocols/acura-certified.md, Product/CPO-Protocols/_runs/2026-07-29-acura.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists. Grep of TASKS.md for acura/mdx/rdx/tlx/ilx/integra: only touches are vinnote-batch-2026-07-06 (acura-mdx-2018 row PRUNED as stale, already populated) and vinnote-batch-2026-07-04 (acura-rdx-2019 vinNote authored — single-engine K20C4, FWD-vs-SH-AWD decode) — both Done, both inspect/index.html, complementary not conflicting; this protocol cross-references the rdx-2019 block and is consistent with it (K20C4 single engine confirmed both places). In-flight autovet-competitor-monitor (Competitors/, next=UVeye) + autovet-seo-content (Content/blog/, Jeep GC 07-29) orthogonal; Ready empty; Done(last 10) = vinnote-batches on inspect/index.html (07-29 batch = prius-prime/cx5/xt5, no Acura). Verified against: autovetting-vinnote-batch-2026-07-04, autovetting-vinnote-batch-2026-07-06; cross-referenced to: acura-rdx-2019 vinNote block. No Re-sync needed.
    Campaign IDs all WebSearch-verified 2026-07-29: 23V-751 (rod bearing, 2015-20 TLX V6 + 2016-20 MDX, Honda XG1/GG0, inspect-vs-replace outcome documentation required), 20V-314 -> 21V-215 (Denso fuel pump, 2019-20 MDX/MDX-SH/RDX/TLX + 2019 ILX; 2024 expansion = Honda KGC/KGD, NHTSA # left [unverified] — live VIN lookup mandated instead), 16V-640 (2015 TLX V6 9AT sensor-cluster failsafe-neutral). Anti-fabrication catch: initial guess 16V-599 was WRONG (disproven in verification; real = 16V-640) — guard line added to protocol file. Described-not-numbered: 9AT transmission-warmer coolant/ATF intermix warranty extension (2015-16 TLX / 2016 MDX), VCM TSBs, 8DCT judder TSBs.
    Key buyer insight for downstream content: TIER TRAP — Acura "certified" spans 182-pt/7yr-powertrain (Precision Certified, 2021-2026 MY <80k) vs 112-pt/6-mo (Precision Used, 2016-2026 MY, NO mileage cap); every certified 2015-2020 TLX is the lite tier.
    Weekly milestone: DONE — acura-certified.md saved + INDEX.md updated (P1 now Subaru ✅ → Mazda ✅ → Lexus ✅ → Acura ✅). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Infiniti (P1).

  2026-08-03 15:40: ingested INFINITI CPO protocol (167 inspection points INFINITI CPO / 84 points on BOTH Select tiers).
    Output: Product/CPO-Protocols/infiniti-certified.md, Product/CPO-Protocols/_runs/2026-08-03-infiniti.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. Ready = autovetting-recall-audit-wave15-2026-08-03 (inspect/index.html + scripts/recall-ledger.json, Toyota Tacoma/4Runner/Highlander slugs + _hub Landing-Page archive) — no INFINITI overlap, and this run deliberately wrote to NEITHER of that task's files. In-flight autovet-competitor-monitor (Competitors/, next=VINsight.ai) + autovet-seo-content (Content/blog/) orthogonal; Done(last 10) = recall-audit waves 13/14 (acura-tsx-2014, ford-fusion-2017) + vinnote batches, no INFINITI content. grep of TASKS.md for infiniti/q50/qx60/qx50/qx80/q60/g37 found only the infiniti-qx80-2018 vinNote row (line ~433, single-engine VK56VD structural note, Done) — complementary and consistent with this file. grep of inspect/index.html: ZERO INFINITI slugs exist, so no downstream checklist can conflict today. Verified against: autovetting-recall-audit-wave15-2026-08-03; cross-referenced to: infiniti-qx80-2018 vinNote block. No Re-sync needed.
    Located the actual OEM checklist PDF (©2016 form IN-17955) rather than dealer-page summaries, so item-level detail is firmer than several earlier files in this library. Three tiers captured: INFINITI CPO (167pt, ≤5yr/60k, up to 6yr/75k or 6yr/unlimited, $0 deductible, ~1,800 components, CARFAX Buyback) / INFINITI CPO Select (84pt, ≤10MY/100k, 12mo/12k POWERTRAIN only, $100 deductible, ~600 components, NO Buyback) / Certified Pre-Owned Select for non-INFINITI trade-ins (84pt, 6mo/6k powertrain).
    Campaign IDs all WebSearch-verified 2026-08-03 with exact scope written into an anti-fabrication guard table: 16V-430 (Direct Adaptive Steering ECU reflash, 2014-16 Q50/Q50 Hyb), 17V-476 (FPCM stall, 2016-18 Q50 + 2017 Q60, 2.0L ONLY), 17V-571 (driver airbag inflator weld, 2017 Q50/Q50 Hyb only), 16V-244 (OCS), 24V-470 (driveshaft fracture/rollaway, 2WD ONLY, 2014-18 Q50 + M56/M35 Hyb/Q70/Q70L), 14V-583 (TPS unintended accel, HYBRIDS only), 21V-234 (2021 Q50/Q60 ECM), 21V-402 (steering knuckle heat-treat, 2021 Q50/QX50/GT-R + 2020 Murano/QX60), 19V-654, 21V-599, 21V-774 (HPCM shutdown, 2014-17 QX60 HYBRID), 19V-807 (ABS actuator fire — SUPERSEDES + expands 18V-601 and re-captures cars previously inspected-and-passed under it), L51 cluster 23V-814/23V-108/22V-111/23V-268/24V-176/24V-154/25V-173, and QX80 14V-683 / 14V-129 (2014 20-inch-wheel GAWR label, label-only remedy) / 21V-373 / 24V-747 / 24V-748 / 25V-821.
    ⚠️ LEDGER CONFLICT FOUND — QUEUED FOR RECALL-AUDIT WAVE 16: scripts/recall-ledger.json records 16V244 as makes:["Nissan"] with component string ending "— NOT 2017+ and NOT Infiniti" (verified 2026-06-11). NHTSA campaign text explicitly covers 2014-2017 INFINITI Q50, 2014-2016 Q50 Hybrid / QX60 / QX60 Hybrid, 2013 JX35 and 2014-2017 Rogue, and prescribes a DIFFERENT remedy on the INFINITI cars (OCS ECU REPLACEMENT vs. the ACU/OCS reflash used on the Nissan sedans). Both halves of the exclusion appear wrong. NO edit made to the ledger or inspect/index.html by this run (those files were mid-flight in Ready). If the exclusion string was written to block a specific past mis-paste, the fix should NARROW it, not delete it.
    Key buyer insights for downstream content: (1) ITEM 13 BLIND SPOT — the only timing item on the whole 167-point form says "timing BELT replaced per OEM maintenance schedule"; every current INFINITI engine is chain-driven, so that item is N/A'd on every car and the inspection contains ZERO timing-chain coverage on a brand whose VQ35 / VK56VD / VR30DDTT all have documented chain wear. Cleanest example in the library of a checklist that is technically complete and practically blind. (2) POINT-COUNT INFLATION — 7 items diesel/manual-only (29,30,31,38,46,83,84) + 7 hybrid-only (47-53); real count on an automatic gasoline Q50 is ~150. (3) QX60 CVT WARRANTY EXTENSION 22I2299CVT (Nissan 22N2299CVT), 2015-2018, 72mo/70k -> 96mo/94k, from the ~$277.7M class settlement — NOT a recall, so invisible to a VIN recall lookup, and the 96-month clock has now expired for most of that population. (4) THREE-TIER TRAP sharper than Acura's — "Certified Pre-Owned Select" names TWO different products, and with a 5yr top-tier ceiling virtually every "certified" INFINITI older than a 2021 MY on a 2026 lot is a lite tier.
    Open flags carried forward: eligibility discrepancy UNRESOLVED (2016 checklist form says 72 months / 70,000 mi; current consumer warranty page says 5 yr / 60,000 mi — same class as the Lexus 70k-vs-80k flag); ITB20-002a (VR30DDTT +0.5 qt oil capacity / new dipstick p/n) is forum-sourced, marked [unverified-primary], do NOT publish as verified; CONSULT III Plus + INFINITI-specific battery tester dependency (items 6-8, 37, hybrid block) — same factory-tool gap as Lexus Techstream; RECALL-SET COMPLETENESS CAVEAT — cars.com lists 14 total campaigns for Q50 and 19 for QX60, this run captured page 1 (10 each) plus the QX80's complete set of 8, so a future model-year-slug run must pull page 2.
    Weekly milestone: DONE — infiniti-certified.md saved + INDEX.md updated (P1 now Subaru ✅ → Mazda ✅ → Lexus ✅ → Acura ✅ → Infiniti ✅). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Volkswagen (last P1, then P2 opens with BMW).

  2026-08-09 10:15: ingested Volkswagen CPO protocol (100+ inspection points — NO fixed published count; single tier, no lite tier and no EV tier).
    Output: Product/CPO-Protocols/volkswagen-certified.md, Product/CPO-Protocols/_runs/2026-08-09-volkswagen.md.
    Sibling check: no true conflict; ALIGNED with the recall audit. Ready = autovetting-recall-audit-wave21-2026-08-09 (inspect/index.html + gitignored _hub Build-Log/Awaiting-Daniel + TASKS.md) — orthogonal file-wise (this run wrote only Product/CPO-Protocols/ + TASKS.md) and complementary in content: wave 21's queue lists vw-jetta-2018 / volkswagen-passat-2018 / vw-atlas-2018 for wave-22 Takata verification, which this ingestion RESOLVES IN ADVANCE (see below). In-flight autovet-competitor-monitor (Competitors/, next=Lemon Squad #1 cycle 2) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10) = recall-audit waves 15-20 + decision-execution 07-30 + vinnote batches — none author a VW checklist that would consume this protocol; no overnight-builder/content-checklist task is launching a VW vehicle. Verified against: autovetting-recall-audit-wave21-2026-08-09, autovetting-recall-audit-wave20-2026-08-08; cross-referenced to: vw-jetta-2018, volkswagen-passat-2018, vw-atlas-2018, vw-tiguan-2018, vw-golf-2018. No Re-sync needed.
    ⚠️ WAVE-22 CROSS-REFERENCE — VW TAKATA SCOPE RESOLVED FROM THE PRIMARY SOURCE, NEGATIVELY. Pulled NHTSA's VW-specific FAQ (nhtsa.gov/takata-recall-spotlight/faqs-takata-desiccated-inflators-and-volkswagen-recalls, last updated 2021-02-03): under the 2020 agreement VW recalls desiccated Takata PSAN (SDI-D) inflators in SELECT BEETLE, BEETLE CONVERTIBLE, AND PASSAT ONLY, phased — Group 1 = MY2012-2014 Beetle/Beetle Conv (defect report by 2020-12-31), Group 2 = MY2015-2016 Beetle/Beetle Conv (by 2023-01-01), Group 3 = MY2017-2019 Beetle/Beetle Conv PLUS 2011-2014 PASSAT (by 2025-01-01). Therefore: vw-jetta-2018 = Jetta absent from the agreement in every year -> expect FALSE; volkswagen-passat-2018 = desiccated Passat scope stops at 2014, out of scope by four model years -> expect FALSE; vw-atlas-2018 = Atlas launched MY2018 and appears on no Takata list -> expect FALSE (wave-20/21 "phantom recall" signature). CAVEAT written into the protocol file: the desiccated agreement is ADDITIONAL to the earlier non-desiccated VW campaigns, so "absent from the FAQ" is not proof of no involvement for pre-2016 cars — check those by VIN before writing a negation. Also of note for wave 22: the 2011-2014 Passats sit in Group 3 precisely BECAUSE their inflators were installed as newer like-for-like replacement parts during the earlier recalls — a Passat whose airbag was already "fixed" is the car in this recall.
    Campaign IDs read first-hand from cars.com NHTSA feeds (provenance gate satisfied — both URLs surfaced in WebSearch before fetching). Verified this run: Jetta 24V-110 (VW 20UF, suction-jet-pump seal -> EVAP fuel leak/fire; EXPANDS AND REPLACES 16V-647; GLI ONLY for 2019-2020 Jetta), 23V-604 (28H7, ignition switch stall, CONVENTIONAL IGNITION SWITCH ONLY), 23V-619 (90W7), 22V-815 (45J6/45J8 TPMS), 22V-514 (91DV eMMC camera), 26V-185 (90Z5, 2025 Jetta+Taos instrument panel), 26V-138 (97TC, 2025-26 Jetta transmission ground wire/fire); Tiguan 21V-732 (51H5), 22V-176 (42L8 rear knuckle corrosion), 22V-226 (66N5, ACCESSORY SPOILER ONLY), 21V-853 (19Q4 brake pipe nut), 25V-082 (91NY camera) + 26V-321 (91NF, recall OF that repair, 2024 Tiguans already fixed under 25V-082), 25V-854 (74HE PODS/passenger airbag), 25V-526 (42E7 tie-rod bolt). THREE items deliberately shipped WITHOUT numbers, marked [unverified] rather than guessed: early-Tiguan rear coil spring fracture, 2016-2018 Passat internal-use/FMVSS non-compliance, 2015 Passat non-desiccated Takata involvement.
    Anti-fabrication guard written into the file: 19V-258 (deleted 2026-07-30, commit 1d86463, from all four VW slugs) never to be re-added; NO unnumbered Takata claim on any VW slug outside Beetle/Beetle Conv/2011-2014 Passat; do NOT cite 16V-647 as the live fuel-system remedy; do NOT broaden 24V-110 (GLI), 23V-604 (conventional ignition), or 22V-226 (accessory spoiler) past their equipment scope.
    Key findings for downstream content: (1) THE MISSING NUMBER — VW is the FIRST OEM in this rotation publishing no fixed point count and no line-item checklist, just "100+" and five named areas (engine starting / transmission malfunction+noise / brakes incl. STOPPING DISTANCE / steering noise-effort-vibration-pulling / maintenance catch-up). Prior ten brands all state a number (152-182). Some dealer assets advertise "112-point" — that figure is dealer-authored, appears nowhere in VW of America materials, and MUST NOT be shipped as VW's number. Honest VW framing is "there is no published list to hold your dealer to." (2) WEAKEST CPO VALUE PROP MEASURED SO FAR — 2yr/24,000mi WITH A $50 PER-VISIT DEDUCTIBLE and NO long powertrain term at all (vs Mazda 7/100k @ $0, Hyundai/Kia 10/100k, Toyota 7/100k); MY19 gets only 1yr/12k; eligibility <6MY / 75,000mi; HV battery 8yr/100k with a 70% capacity FLOOR. Carfax's independent review reaches the same verdict (deductible + less rigorous inspection); a documented auto-fraud case has a VW dealer conceding the CPO inspection missed prior collision damage. (3) TWO SUPERSESSION TRAPS IN ONE BRAND (16V-647->24V-110, 25V-082->26V-321) where "all recalls performed" is true and useless -> RECOMMEND a general "superseded by later campaign" field in the checklist engine rather than one-off handling (same pattern hit FCA/Toyota in waves 19-20). (4) EQUIPMENT-SCOPED RECALLS NEED AN EQUIPMENT FIELD — three VW campaigns scope by trim/variant/accessory, not model year; the schema expresses scope in years, which is exactly the "real campaign, wrong variant" failure mode waves 19-20 unwound. (5) 21V-732 IS A CONTENT ASSET — a 2018 Tiguan recall that only exists on a car ALREADY CRASHED AND REPAIRED (incorrect roof reinforcement fitted during roof-damage repair, degrades roof integrity + side-curtain deployment) and can sit inside a valid CPO certification; cleanest argument in the library for "history report + independent physical inspection, not either alone," and it pairs with the independence counter-positioning piece the competitor-monitor has flagged unwritten four weeks running. Worth its own post post-freeze. (6) NO EV TIER — ID.4 runs the same 100+ inspection with no published battery-SOH item while the warranty turns on a 70% floor; AutoVet adds measured SOH + DC-fast-charge taper. (7) TDI emissions-modification status (2009-2016 diesels) has no OEM checklist counterpart; vw.com/en/emissions.html lookup added as an AutoVet step.
    Retrieval gap: the motorwebs "Volkswagen 112-Point Inspection" dealer asset surfaced in search but returned an empty body to web_fetch (client-rendered). Left unretrieved rather than inferred, and the 112 figure is not adopted.
    Weekly milestone: DONE — volkswagen-certified.md saved + INDEX.md updated. **P1 ROTATION COMPLETE** (Subaru ✅ → Mazda ✅ → Lexus ✅ → Acura ✅ → Infiniti ✅ → Volkswagen ✅); P0 completed 2026-06-28. Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: **BMW (first P2)**.

### autovet-seo-content

- Status: in flight
- Task: weekly programmatic SEO pillar post (one top-500 vehicle/week) into Content/blog/ + research log in Content/_seo-research/
- Notes:
  2026-06-17 11:00: drafted 2019 Chevrolet Equinox pillar post (Tier-1 #4, highest-ranked fully-uncovered vehicle; 1.5L turbo oil-consumption + timing-chain cold-start rattle story).
    Output: Content/blog/2026-06-17-2019-chevrolet-equinox-buyers-guide.md (1,975 words, status: draft), Content/_seo-research/2026-06-17-2019-chevrolet-equinox.md.
    Recalls cited are all WebSearch-verified — 20V668 (GM N202313440, start-stop accumulator / loss-of-propulsion, 2018-2020 Equinox), 18V576 (rear brake caliper coating, 2018-2019), 19V184 (rear-right head-restraint welds). Two claims left [unverified] rather than fabricated: fuel-tank-seam recall campaign number + the timing-chain TSB ID. Interlinks to 2019-honda-crv + 2017-nissan-rogue posts.
    Sibling check: no overlaps. In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) are orthogonal; Ready empty; Done(last 10) recall-audit waves 4-9 + deprice-CTAs touch inspect/ + 18 existing blog posts, none a Chevrolet Equinox slug. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Toyota RAV4 (#11), Ford Explorer (#7), Hyundai Tucson (#17, recent recall news).

  2026-06-24 10:00: drafted 2020 Ford Explorer (6th-gen U625) pillar post — Tier-1 #7, highest-ranked fully-uncovered vehicle; launch-year build-quality + 10-speed transmission + rear-axle/rollaway recall cluster story.
    Output: Content/blog/2026-06-24-2020-ford-explorer-buyers-guide.md (~2,400 words, status: draft), Content/_seo-research/2026-06-24-2020-ford-explorer.md.
    Recalls cited are all WebSearch-verified 2026-06-24 — 20V693/20S65 (driveshaft weld-seam, rollaway-in-Park, 2020 Explorer/Aviator AWD), 22V255/22S27 (rear-axle bolt, superseded), 23V675/23S55 (~238k MY2020-22, rear-axle bolt re-recall — the one to confirm a VIN received), 23V069 (PCM-reset park-system damage). Transmission TSB IDs left [unverified] (described condition, not fabricated number). Internal-water-pump myth explicitly corrected as a 5th-gen (2011-2019) issue, NOT 2020. Interlinks to 2017-chrysler-pacifica + 2021-ford-f150 posts.
    Sibling check: no blocking overlap. Recall-audit wave 8 (2026-06-16, within 14d, Done) touched explorer-2020 in inspect/index.html — it DELETED a fabricated 21V-641 "Transmission Fluid Leak" recall; this post is aligned (does NOT cite 21V-641; all recalls independently verified). In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-competitor-monitor (Competitors/) orthogonal; Ready blocks (vinnote batches on 2023 Honda/Kia/Mazda slugs) no Explorer overlap. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Toyota RAV4 (#11), Hyundai Tucson (#17, recent recall news), Ford Escape (#18).

  2026-06-28 23:43: drafted 2019 Chevrolet Malibu (9th gen, 2016-2025) pillar post — Tier-1 #8, highest-ranked fully-uncovered vehicle; discontinued-model fleet/rental-dump value angle + the 2019-introduced GM CVT (1.5T trims) slipping / lost-forward-gear story as the make-or-break buyer issue.
    Output: Content/blog/2026-06-28-2019-chevrolet-malibu-buyers-guide.md (1,583 words body, status: draft), Content/_seo-research/2026-06-28-2019-chevrolet-malibu.md.
    Powertrain WebSearch-verified 2026-06-28: 1.5T (160hp, L/LS/RS/LT) = CVT new for 2019; 2.0T (250hp, Premier) = 9-speed auto; Hybrid 1.8L (182hp combined, final year 2019); all FWD. Recall cited is WebSearch-verified — 21V649000 / GM N212333380 (rear seat belt retractor fasteners, 2016-2021 Malibu + 2019-2021 Cadillac XT4). CVT slip/lost-forward-gear left as a TSB (clutch regulator valve in valve body) with the specific bulletin number marked [unverified] rather than fabricated. Explicitly excluded the 2016-only EBCM brake recall (does not apply to 2019). Interlinks to 2019-nissan-altima + 2018-toyota-camry + 2019-chevrolet-equinox posts (all confirmed present in /blog/).
    Sibling check: no overlaps. In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Subaru run 06-28) orthogonal; Ready empty; Done(last 10) = vinnote-batch-2026-06-28 (kia-stinger/vw-taos/nissan-pathfinder in inspect/index.html) + recall-audit — none touch a Chevrolet Malibu slug or Content/blog/. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Toyota RAV4 (#11), Hyundai Tucson (#17, recent recall news), Ford Escape (#18, PowerShift DCT / EcoBoost coolant-intrusion story).

  2026-07-01 10:05: drafted 2019 Toyota RAV4 (5th-gen XA50) pillar post — Tier-1 #11, highest-ranked fully-uncovered vehicle; launch-year story = low-speed 8-speed transmission hesitation (software/ECM fix, NOT a CVT failure — gas RAV4 is an 8AT, only the hybrid is eCVT; correcting a widespread web factual error) + the multi-year-expanded fuel-pump recall + the fuel-tank-won't-fill quirk.
    Output: Content/blog/2026-07-01-2019-toyota-rav4-buyers-guide.md (1,963 words body, status: draft), Content/_seo-research/2026-07-01-2019-toyota-rav4.md.
    Recalls WebSearch-verified 2026-07-01: 20V-012 / Toyota 20TA02 (Denso low-pressure fuel pump, engine stall, 2019-2020 RAV4; expanded through ~Jan 2025 amendment — post stresses re-checking VIN against latest amendment), 19V-576 / Toyota K0N (backup camera not activating in reverse, FMVSS 111, 2019 RAV4 + Hybrid, began Sept 2019). TSB T-SB-0107-19 (low-speed hesitation ECM reprogram) cited by real bulletin ID. Fuel-tank-fill CSP/warranty-enhancement number left [unverified] (described condition, not fabricated). Toyota 160-point Gold CPO protocol referenced (Product/CPO-Protocols/toyota-certified.md, incl. its 2019+ RAV4-HV transaxle/MGR listening line). Interlinks to 2019-honda-crv + 2019-chevrolet-equinox + 2018-toyota-camry (all confirmed present in /blog/).
    Sibling check: no overlaps. In-flight autovet-competitor-monitor (Competitors/, next=Cars.com) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Mazda) orthogonal; Ready empty; Done(last 10) = vinnote-batches + recall-audit on inspect/index.html + pinpoint-relax — none touch a Toyota RAV4 slug or Content/blog/. No RAV4 launch in overnight-builder/vinnote queues. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Hyundai Tucson (#17, recent recall news), Ford Escape (#18, PowerShift DCT / EcoBoost coolant-intrusion), Jeep Grand Cherokee (#16).

  2026-07-08 06:04: drafted 2018 Hyundai Tucson (3rd-gen TL, 2016-2021) pillar post — Tier-1 #17, highest-ranked fully-uncovered vehicle; recent recall news. Buyer story split by drivetrain: 2.0L Nu (164hp/6AT, SE/SEL/SEL+/Sport) = reliable-but-oil-consumption; 1.6T Gamma (175hp/7-speed dry DCT "EcoShift", Value/Limited) = the make-or-break risk (low-speed shudder/hesitation, $3-5k repair).
    Output: Content/blog/2026-07-08-2018-hyundai-tucson-buyers-guide.md (1,908 words body, status: draft), Content/_seo-research/2026-07-08-2018-hyundai-tucson.md.
    Recalls WebSearch-verified 2026-07-08: 20V-543 / Hyundai Recall 195 (ABS/HECU engine-fire "park outside", expanded 2020-12-30 to include 2016-2018 Tucson; 652,024 units 2016-2021, 12 fires, fuse-kit+SW remedy) = the CORRECT campaign for a 2018. Explicitly flagged 22V-056 (2014-15 Tucson + 2016-18 Santa Fe) and 23V-651 (2010-15 Tucson) as NOT-applicable-to-2018 so a seller can't point at the wrong campaign. CATALOG CORRECTION embedded: US 3rd-gen Tucson has NO 2.4L Theta II and NO CVT (same Kia/Hyundai mislabel pattern as prior vinnote fixes) — top-500 seed note's "Theta II rod-bearing" line is wrong for the Tucson; risk is Nu oil consumption + DCT. Nu oil-consumption campaign/warranty-extension number left [unverified] (warranty/service-campaign, not a confirmable NHTSA safety-recall # for the 2018 2.0L); 1.6T DCT reprogram noted as 2016-2017-scoped (Campaign 149 / TSB 16-01-038) with 2018 handled via TSB-class SW, bulletin # [unverified]. Referenced Hyundai 173-pt OEM CPO protocol (Product/CPO-Protocols/hyundai-certified.md, incl. its Tucson DCT drive-cycle + oil-sludge gate). Interlinks to 2019-honda-crv + 2019-toyota-rav4 + 2019-chevrolet-equinox + 2017-nissan-rogue (all confirmed present in /blog/).
    Sibling check: no true conflict. Only recent Tucson touch = autovetting-vinnote-batch-2026-06-27 (Done, within 14d) which corrected hyundai-tucson-2022 (NX4, 4th gen) transmission spec in inspect/index.html — DIFFERENT generation + different file tree (inspect/ not Content/blog/); this post covers the 3rd-gen TL, cleanly distinct and factually aligned (also affirms no-CVT). In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lexus) orthogonal; Ready empty; Done(last 10) = vinnote-batches on inspect/index.html + recall-audit — none touch a Hyundai Tucson slug in Content/blog/. No Tucson launch in overnight-builder/vinnote queues. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Ford Escape (#18, PowerShift DCT / EcoBoost coolant-intrusion), Jeep Grand Cherokee (#16), Ford Edge (#19).

  2026-07-29 15:31: drafted 2015 Jeep Grand Cherokee (WK2, 2011-2021; post-2014 refresh) pillar post -- Tier-1 #16, highest-ranked fully-uncovered vehicle; FIRST Jeep post (diversifies the mesh, which skewed Toyota/Honda/Ford/Chevy). Buyer story = three-engine fork (3.6L Pentastar V6 value pick / 5.7L Hemi tow pick / 3.0L EcoDiesel high-risk emissions-settlement pick) + air-suspension + TIPM, gated by two must-confirm recalls.
    Output: Content/blog/2026-07-29-2015-jeep-grand-cherokee-buyers-guide.md (1,832 words body, status: draft), Content/_seo-research/2026-07-29-2015-jeep-grand-cherokee.md.
    Recalls WebSearch-verified 2026-07-29 and DISAMBIGUATED (aggregators mislabel these): 16V-240 / FCA S27 (monostable gear-selector rollaway, 2014-2015 Grand Cherokee + 2012-2014 Charger/300, the Anton-Yelchin recall) = headline; 15V-461 / FCA R40 (Uconnect radio remote-hacking, 2014-2015 GC among ~1.4M units, the Miller/Valasek "first cybersecurity recall") -- NOTE one prominent source mislabels 15V-461 as a TIPM fuel-pump recall; authoritative source confirms it is the radio-security campaign. Takata by-VIN (no single campaign #). CORRECTION embedded: alternator recall 17V-435 covers 2011-2014 GC and generally EXCLUDES MY2015 (buyer trap corrected). TIPM fuel-pump-relay stall left as a described known-issue / inspection priority with campaign # [unverified] rather than fabricated (avoided reusing 15V-461, which is NOT the TIPM number). EcoDiesel 2014-2016 emissions settlement (approved emissions modification + extended warranty + ~$3k payment) framed as both risk flag and negotiation lever. No FCA/Jeep CPO protocol file exists yet (rotation done Toyota->...->Lexus/Mazda) -- CTA notes OEM-aligned protocol forthcoming. Interlinks to 2020-ford-explorer + 2017-chrysler-pacifica (Stellantis sibling) + 2010-lexus-rx350 (all confirmed present in /blog/).
    Sibling check: no overlaps. No Jeep/Grand Cherokee slug anywhere in TASKS.md (In-flight, Ready [empty], Done last 10). In-flight autovet-competitor-monitor (Competitors/, next=UVeye) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) orthogonal; Done(last 10) = vinnote-batches + recall-audit on inspect/index.html, none touch a Grand Cherokee slug or Content/blog/. No overnight-builder/vinnote/content-checklist task launching a Grand Cherokee. No Re-sync needed.
    Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Ford Escape (#18, PowerShift DCT / EcoBoost coolant-intrusion), Ford Edge (#19, 2.0T water pump / PTU), Toyota Highlander (#20, clean-reliability palate-cleanser).

  2026-08-05 09:20: drafted 2013 Ford Escape (C520 3rd-gen launch year) pillar post — Tier-1 #18, highest-ranked fully-uncovered vehicle; buyer story = three-engine fork (2.5L iVCT safe pick / 1.6L EcoBoost fire-recall-cluster + coolant intrusion / 2.0L EcoBoost crossover pipe) gated by the 17-campaign verified recall set.
    Output: Content/blog/2026-08-05-2013-ford-escape-buyers-guide.md (1,597 words body, status: draft), Content/_seo-research/2026-08-05-2013-ford-escape.md.
    Recalls: cited ONLY the wave-16-verified 17-campaign set from inspect/index.html ford-escape-2013 + scripts/recall-ledger.json (13V-583/13V-584/12V-336/12V-431/12V-551 as the five 1.6L must-be-closed; 22V-413+18V-471 dual bushing campaigns; 14V-597 RCM; 14V-495/15V-813 2.0L splices; latch set 16V-643/20V-331/14V-239; 14V-237/14V-164/13V-085/12V-319). No-Takata-on-this-car flag carried into the post verbatim from the checklist. Coolant-intrusion TSB + 6F35 shudder bulletin numbers left [unverified] (described condition, not fabricated).
    CATALOG CORRECTION embedded: top-500 seed row 18 says "PowerShift DCT (2013-2019)" — WRONG for Escape (DPS6 = Focus/Fiesta; every 2013-2019 Escape = 6F35 conventional 6AT; also no 1.5T in 2013 — 1.6T until MY2017). Post corrects it explicitly (same pattern as Tucson no-Theta-II fix, 07-08); fix seed row at annual refresh. Ford Blue Advantage 139/172-pt protocol referenced (Product/CPO-Protocols/ford-certified.md) with note that a 2013 is past CPO eligibility. Interlinks to 2019-honda-crv + 2019-toyota-rav4 + 2019-chevrolet-equinox + 2018-hyundai-tucson + 2020-ford-explorer (all confirmed present in /blog/).
    Sibling check: no blocking overlap — ALIGNED with recall audit. Recall-audit wave 16 (2026-08-03, Ready→Done, within 14d) rebuilt ford-escape-2013 in inspect/index.html (deleted 4 fabricated numbers incl. the GM-ignition + Porsche-conrod mis-pastes, added 22V-413); this post is the downstream consumer of that verified set and cites nothing outside it (Explorer-post precedent, 06-24). Wave 18 part 1 (Ready, 08-05) touched sentra/pathfinder/mustang/bmw/outback — no Escape; wave-18 part 2 queue (outlander/kicks/qx60/ioniq5/carnival) — no Escape. In-flight autovet-competitor-monitor (Competitors/, next=VINspectorAI #13 + Q3 summary) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Volkswagen) orthogonal. No overnight-builder/vinnote/content-checklist task launching an Escape. Verified against: autovetting-recall-audit-wave16-2026-08-03, autovetting-recall-audit-wave18-2026-08-05. No Re-sync needed.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Ford Edge (#19, 2.0T internal water pump / PTU), Toyota Highlander (#20, palate-cleanser), then re-rank top-500 for next uncovered Tier-1.

## Ready to deploy / publish

#### autovetting-recall-audit-wave22-2026-08-10 — ready (pushed directly)

- Status: ready
- Started: 2026-08-10 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 22 — close the Takata sweep (the six slugs wave 21 left unverified) and resolve queued number 14V-346
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-10.md (gitignored), TASKS.md
- Notes:
  2026-08-10 02:00: recall-audit WAVE 22. SEVEN slugs corrected. The systemic Takata sweep opened by
  wave 21 is now CLOSED: the last six slugs carrying an unverified Takata claim were checked against
  manufacturer and NHTSA primary sources and ALL SIX ARE FALSE, taking the sweep to 24 false / 1 true
  across 25 affirmative "this car is in the Takata recall" claims. Ledger 213 verified / 39 unverified
  -> 216 verified / 38 unverified. Commit: __COMMIT__.
  Sibling check: no true conflict. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) and autovet-seo-content (Content/blog/) are all
  orthogonal file-wise. Ready = recall-audit waves 16-21, all sharing inspect/index.html +
  scripts/recall-ledger.json but ALL ALREADY PUSHED DIRECTLY (wave 21 = commit 02fd8d2) and strictly
  additive-then-superseded by this wave, which continues their own written queue. Verified against:
  autovetting-recall-audit-wave21-2026-08-09, autovetting-recall-audit-wave20-2026-08-08;
  cross-referenced to: autovet-cpo-protocol-ingestion 2026-08-09 (Volkswagen), which independently
  resolved the VW Takata scope from NHTSA's desiccated-inflator FAQ and reached the same three negative
  verdicts this wave reached from the filed Part 573. No Re-sync needed.
  FALSE (6, corrected): vw-jetta-2018 (Jetta in no VW Takata campaign after ~MY2014, and in none of
  24V-834), volkswagen-passat-2018 (FALSE BY FOUR MODEL YEARS — 24V-834 lists the 2012-2014 US Passat),
  vw-atlas-2018 (Atlas in no Takata campaign in any year), chevy-cruze-2017 (no Cruze of any year is on
  the GM affected-vehicle list, which runs to the 2007-2014 trucks/SUVs + Vibe/Astra/Saab),
  nissan-armada-2017 (no Armada of any year on the Nissan list: Maxima 01-03, Pathfinder 02-04, Sentra
  02-06, Versa 07-11/07-12), infiniti-qx80-2018 (QX80 Takata scope is MY2014 only — the Oct-2014
  driver-inflator campaign covering the 2013 QX56 and 2014 QX80, ~1,900 vehicles, a build defect not the
  propellant-degradation recall).
  THE VW TRAP WAVE 21 WARNED ABOUT WAS REAL AND NEARLY PRODUCED A WRONG ANSWER. Secondary coverage of
  24V-834 uniformly reports it as covering "2005 through 2018" incl. "2017 Passat wagons" — which would
  put a 2018 Passat one model year from scope. The FILED Part 573 lists a "2017-2017 PASSAT WAGON" whose
  PRODUCTION DATES ARE OCT 21 2005 - NOV 06 2006. It is a model-year field on a B6 car; the US Passat
  scope is MY2012-2014 and the 2018 is FOUR years outside, not one. Research trap now written into the
  ledger note for 24V834: where a Part 573 model-year field and its production dates disagree, the
  production dates describe the car.
  NET GAIN, not just a deletion: vw-atlas-2018's fabricated Takata item was crowding out a real and
  poorly-known airbag recall — 23V-215 (VW 69FB), a PODS wiring contact fault that switches the front
  passenger airbag OFF while the seat is occupied; 2018-2021 Atlas (143,038 US) + 2020 Atlas Cross Sport
  (15 US), and VW had NO REMEDY AVAILABLE at announcement in April 2023, so many changed hands unrepaired.
  Added with a physical check (watch the PASSENGER AIRBAG OFF indicator go out) alongside the VIN check.
  14V-346 RESOLVED (queue item 3): shipped on chevy-silverado-2014 as "Front Passenger Airbag (Takata)".
  NHTSA's own notification letter (RCRN-14V346-4931.pdf, GM recall 14294) says 14V-346 is ALL 2010-2014
  CHEVROLET CAMARO vehicles, for knee contact moving the ignition key out of RUN. Wrong model AND wrong
  defect — wave-19 "right parent, wrong model" signature plus an invented defect label. Deleted;
  stats.recalls 4->3; vinNote "all four listed recalls" -> "all three". Also settled the scope question
  rather than leaving it implied: GM lists the 2007-2013 Silverado 1500 LD and the 2007-2014 2500/3500 HD,
  so a 2014 1500 (this slug) is outside Takata scope while a 2014 HD is inside — now in the vinNote.
  14V-293 / 16V-065 / 14V-355 on that slug remain unverified -> wave 23.
  GENERATION-BOUNDARY SWEEP PROMOTED TO WAVE-23 PRIORITY 1 — this wave found a second instance without
  looking for one. vw-jetta-2018 was authored against the 2019 A7 car: trim "(A7 gen)", a 228hp GLI (the
  2018 GLI is 210hp) and a "DQ200 dry-clutch 7-speed DSG" carrying an $1,800-$3,500 mechatronic cost
  anchor. The US 2018 Jetta is the final MK6; S/SE/SEL use an Aisin six-speed torque-converter automatic
  and only the GLI has a dual-clutch — the WET-clutch DQ250. The DQ200 was never fitted to a US Jetta, so
  the headline powertrain item described a transmission the car does not have and warned about a
  dry-clutch symptom. Same shape as toyota-highlander-2014 (wave 21). Corrected. volkswagen-passat-2018
  had a milder version (DSG advice applied to four-cylinder cars that use the Aisin TF-62SN; only the 3.6
  VR6 got a DSG). Corrected.
  GATE RECOMMENDATION STRENGTHENED: wave 21 proposed failing any recall entry whose ID is neither
  'Multiple' nor \d{2}[VE]-?\d{3}. Support that, and add a second rule — 14V-346 WAS visible to G28 and
  PASSED, because G28 checks that a number is ledgered, not that it belongs to the vehicle it sits on. A
  ledger `makes` vs slug `make` mismatch check would have caught 14V-346 and the wave-19/20 "right parent,
  wrong model" fabrications too.
  Ledger: 14V346 moved unverified->verified with a do-not-add note naming the slug it came off; 23V215 and
  24V834 added verified with primary-source URLs; the 2017-Passat-Wagon trap written into the 24V834 note.
  NON-BLOCKING FOR DANIEL: the Ready section now holds SEVEN consecutive already-pushed recall-audit
  blocks (waves 16-22) while the newest Done block is wave 15 (2026-08-03). The hourly orchestrator is
  supposed to move Ready -> Done after a push and appears not to have since 2026-08-03. Concrete data
  point for the suspected orchestrator stall; not blocking (these waves push directly, gate is passing).
  Edit safety: exact-string substitution scoped to each slug's brace-matched block, count == 1 asserted
  PER SUBSTITUTION WITHIN THE BLOCK plus a uniqueness assertion on the block itself; no write until all 29
  matched. Block-scoping mattered: `recalls: [{ campaign: 'Takata', description: 'Airbag inflator
  fragmentation', ... }]` is byte-identical on nissan-armada-2017 and infiniti-qx80-2018 (the same
  collision wave 21 hit) and a file-wide replace would have silently corrected the wrong slug.
  Syntax-check: PASS. Dead-links: verified. Scanner: PASS (505 files, exit 0). Gate: 27 pass / 2 warn /
  0 CRITICAL; recall-backlog ratchet 39 -> 38. Truncation guard: 17,741 lines / 1,397,866 bytes, tail
  intact. stats.recalls == recalls.length asserted on all 7 touched slugs (7/7 OK).
  Detail: _hub/Build-Log/2026-08-10.md.

#### autovetting-recall-audit-wave21-2026-08-09 — ready (pushed directly)

- Status: ready
- Started: 2026-08-09 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 21 — the two items wave 20 queued: (0) toyota-highlander-2014 powertrain-generation rewrite, (1) systemic Takata sweep across every slug carrying a Takata claim
- Touched files: inspect/index.html, _hub/Build-Log/2026-08-09.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-08-09 02:00: recall-audit WAVE 21. NINETEEN slugs corrected. The Takata sweep queued by wave 20
  found that the Takata claim on this site is a batch-authored TEMPLATE, not a set of findings: of the 19
  affirmative "this car is in the Takata recall" claims checked tonight, 18 were false and 1 (lexus-gx460-
  2015) was true. 16 of the 19 were critical-risk items, several the first item on the page.
  ZERO campaign numbers added or deleted -> scripts/recall-ledger.json UNTOUCHED (213 verified / 39
  unverified_legacy). That is the finding: this whole class shipped WITHOUT campaign numbers — as
  { campaign: 'Takata' }, { number: 'Takata Airbag' }, or prose in summary/vinNote/topComplaintArea —
  so G28, the ledger and every number-verification wave 1-20 were structurally unable to see it.
  Sources of truth (all fetched 2026-08-09): toyota.com/recall/takata (affected-vehicle table + DSF/DSC
  nationwide, E04/ELG regional, F0L driver campaigns); mopar.com Takata recall page (per-brand model/year
  list under the 2026 FCA stop-drive advisory); American Honda Takata fact sheet (hondanews.com).
  FALSE (18, corrected): toyota-corolla-2014 (scope ends 2013), toyota-rav4-2016 + toyota-rav4-2019 (RAV4
  scope is the 2004-2005 driver inflator, F0L, and Toyota states it is the only Toyota driver-inflator
  campaign), toyota-sequoia-2016 + toyota-sequoia-2022 (scope is the 2002-2007 first-gen), toyota-avalon-
  2018 / toyota-land-cruiser-2018 / toyota-highlander-2020 (not on Toyota's list in ANY year), lexus-is-
  2018 (IS scope ends 2013), lexus-rx350-2019 (RX not on the Lexus list), chrysler-300-2016 (FALSE BY ONE
  YEAR — 300 scope is 2005-2015), dodge-charger-2018 (2006-2015), dodge-challenger-2018 + dodge-challenger-
  2023 (2008-2014), dodge-durango-2018 (2004-2009), honda-crv-2015 (CR-V scope 2002-2011), honda-fit-2018
  (Fit scope 2009-2014), honda-hrv-2018 (HR-V not on Honda's list in any year).
  TRUE (1, strengthened not deleted): lexus-gx460-2015 — Lexus lists 2010-2017 GX460 (2017 partial); the
  shipped "through 2019" ceiling was wrong but the involvement is real. Rewritten to say involvement is
  assigned by VIN and build date, humidity-zone cars pulled in earlier, and to require the campaign read
  as COMPLETED rather than accept a verbal assurance.
  CORROBORATED (no edit needed): jeep-wrangler-2012 genuinely in scope (FCA lists 2007-2016 Wrangler);
  honda-ridgeline-2012 genuinely in scope (2006-2014); the wave-20 negation on jeep-grand-cherokee-2014 is
  correct (the WK2 is absent from FCA's list).
  Nothing was silently deleted — each false claim became a monitor-risk VIN-check item that NAMES the real
  scope and says the claim is wrong (wave-20 pattern; a buyer who read the false version elsewhere needs
  to be told it is false). Where the Takata claim was bolted onto a real check (three FCA slugs, "Hemi oil
  history + Takata recall check") the real half was kept and promoted, since MDS lifter failure IS the
  walk-away item there. 9 pseudo-entries in recalls arrays rewritten as VIN-check entries; stats.recalls
  re-synced to array length on every slug touched (several were already out of sync — sequoia-2016 claimed
  5 against an array of 1).
  ITEM 0 (highlander): engine field, summary, the GDI carbon item and the transmission item rewritten
  together — MY2014 is 2GR-FE / 270 hp / port injection / U660E six-speed (2.7L 1AR-FE on base FWD LE),
  not the 2017-facelift 2GR-FKS / 295 hp / 8-speed. The headline monitor item was a $400-800 walnut-blast
  decarbon the car cannot need; replaced with the seepage checks this engine actually earns. No vinNote
  exists on the slug so none needed correcting — and none was invented. Awaiting-Daniel item marked
  RESOLVED.
  Wave-22 queue: (1) finish the sweep — vw-jetta-2018 / volkswagen-passat-2018 / vw-atlas-2018 (VW is the
  one manufacturer with a DESICCATED-inflator recall, so verify against the NHTSA VW FAQ, do not assume a
  late car is safe), chevy-cruze-2017, nissan-armada-2017 + infiniti-qx80-2018 (secondary sources conflate
  the Takata campaigns with a later non-Takata Armada/QX80 recall — get Nissan's own list); (2) generation-
  boundary sweep, start with the 2014-2016 Toyota slugs; (3) oldest-first 14V292/14V327/14V346 (on chevy-
  silverado-2014, which also carries a Takata mention — resolve both together)/14V355; (4) acura-tsx-2014
  numbers check. NEW GATE PROPOSED: fail any recall entry whose number/campaign field is neither
  'Multiple' nor a \d{2}[VE]-?\d{3} match, the same way an unledgered number fails.
  Sibling check: In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal. Ready = wave20/wave19/
  wave18 (already pushed f4905ae/d6d6550/6a2b3ba), same file but additive on disjoint slugs; Verified
  against: autovetting-recall-audit-wave20-2026-08-08. Done (last 10) all carry - Started: (checked, no
  backfill needed). Working tree was clean at start of run. No Re-sync needed.
  Syntax-check: PASS (run after each of the two edit passes). Dead-links: verified (no links added).
  Scanner: PASS (502 files, exit 0). Gate-check: 27 pass / 2 warn / 0 CRIT (G28 clean; warns are the
  standing backlog ratchet at 39 and the homepage-test-bc lazy-loading warn). Truncation guard: 17,741
  lines / 1,392,329 bytes (was 17,744 / 1,381,974 — 3 lines fewer because several replacement items are
  4 lines where the originals were 5), tail intact.
  Process note: both passes ran as exact-string substitution with a count==1 assertion per substitution
  and no write until all 66 matched. Four ambiguity failures were caught by the assertion rather than by
  eyeball — most usefully { campaign: 'Takata', description: 'Airbag inflator fragmentation', ... }, which
  is BYTE-IDENTICAL across toyota-land-cruiser-2018, nissan-armada-2017 and infiniti-qx80-2018. A regex
  edit would have silently corrected the wrong slug.

#### autovetting-recall-audit-wave20-2026-08-08 — ready (pushed directly)

- Status: ready
- Started: 2026-08-08 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 20 — oldest-first sweep of the three oldest unverified numbers (14V028 / 14V153 / 14V290) and complete-set rebuilds of the slugs carrying them: toyota-highlander-2014, jeep-grand-cherokee-2014, gmc-sierra-2014
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-08.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-08-08 02:00: recall-audit WAVE 20. TWELVE fabrications deleted across 3 slugs — a 100% failure
  rate, no numbered recall on any of the three survived verification. Deleted: highlander 14V-153
  (= GM electric power steering, Malibu/Maxx/HHR/Cobalt/Aura/Ion/G6, 1,360,895 units, GM N140115 —
  cross-MAKE), 19V-291 (= BMW 2019 X3/X4 instrument panel / passenger airbag — cross-MAKE), 15V-025
  (unresolvable) and a "Multiple / Takata Airbag Inflator" entry; grand-cherokee 14V-028 (= COTTRELL
  AUTO-TRANSPORTER battery-equalizer potting compound, 779 units — wrong VEHICLE CLASS), 15V-313
  (= FCA Takata DRIVER inflator for Ram/Durango/Aspen/300/Charger/Magnum/Dakota/Mitsubishi Raider —
  right corporate parent, wrong model, shipped as "HVAC Fan Wiring"), 16V-391 (unresolvable; the real
  monostable-shifter campaign is 16V-240), 21V-448 + 18V-182 (unresolvable) and a "Multiple / Takata
  (select builds)" entry; sierra 14V-290 + 16V-586 (both unresolvable).
  HEADLINE FIX: the 2014 Highlander shipped a CRITICAL-risk inspection item asserting "The 3rd-gen
  Highlander is included in the Takata airbag recall", a matching recall entry, and a summary line telling
  buyers to confirm the Takata remedy. It has five NHTSA campaigns and NONE is Takata. Item rewritten
  around 14V-576 (fuel delivery pipe leak, fire) and the summary sentence corrected. This is the SECOND
  slug to carry a phantom Takata claim (subaru-forester-2011, wave 16) -> NEW SIGNATURE "recall invented
  for a car that has no campaign of that kind at all", which no number-verification pass can catch because
  there is no number to check; a systemic Takata sweep is wave-21 priority 1.
  Complete verified sets added (cars.com per-MY NHTSA feeds, WebSearch provenance): highlander
  14V-576/14V-272/14V-274/14V-051/18E-107 (5); grand-cherokee 18V-332/16V-240/14V-643/17V-435/14V-634/
  17V-741/14V-154/17V-572/13V-483/14V-636/14V-293/14V-391/15V-461/13V-289/17E-061 (15, incl. THREE
  overlapping alternator campaigns and two recalls-of-a-repair); sierra 14V-246 (NHTSA do-not-drive)/
  14V-152/17V-414 (~690,685 trucks)/15V-640/19V-761/19V-645/16V-651/17V-437/16V-209/21V-245/14V-446/
  14V-374/14V-301/13V-488/13V-315/18V-267 (16, three of them repairs of earlier repairs). stats.recalls
  re-synced to array length 6/16/17. VIN-check closing line on all 3, carrying the explicit "this car is
  NOT in the Takata campaign" correction on the two slugs that had falsely claimed it.
  Ledger: verified 173 -> 213 (36 citable adds + 2 promotions out of unverified_legacy, 14V-293 and
  15V-461, both confirmed in the Grand Cherokee feed + 4 do-not-add records for the fabrications that
  resolved to real unrelated campaigns); unverified_legacy 51 -> 39. Wave-21 queue: (0) toyota-highlander-
  2014 powertrain-generation rewrite — see Awaiting-Daniel; (1) systemic Takata sweep; (2) oldest-first
  14V292/14V327/14V346/14V355 then ledger order.
  OPEN FOR DANIEL (appended to Awaiting-Daniel, not fixed this run): toyota-highlander-2014 is authored
  against the 2017+ facelift powertrain — engine field reads 2GR-FKS / 295hp / 8-speed and the headline
  monitor-risk item is GDI intake-valve carbon, but MY2014 is 2GR-FE / 270hp / port injection / 6-speed
  U660E. Fixing it means rewriting engine + summary + inspection item + vinNote together; a partial fix
  would leave the slug internally inconsistent, so it is queued rather than half-done.
  Sibling check: In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal. Working tree carried one
  sibling edit at start of run — an uncommitted .gitignore widening (push-*.sh -> push*.sh); left in place
  and carried in tonight's commit with attribution, same handling as waves 17/18. Ready = wave19/wave18p2/
  wave18p1 (already pushed d6d6550/6a2b3ba/fd4ddbf), same files but additive on disjoint slugs; Verified
  against: autovetting-recall-audit-wave19-2026-08-07. Done (last 10) all carry - Started: (checked, no
  backfill needed). No Re-sync needed.
  Syntax-check: PASS. Dead-links: verified (no links added). Scanner: PASS (498 files, exit 0).
  Gate-check: 27 pass / 2 warn / 0 CRIT (G28 clean). Truncation guard: 17,744 lines / 1,381,974 bytes
  (was 17,717 / 1,370,286), tail intact.
  Process note: the post-edit residual grep caught 16V-391 surviving in a source: field on a prose
  inspection item OUTSIDE the recalls array — G28 would have CRIT-failed at push time. Re-grep every
  deleted number across the WHOLE file, not just the array you rewrote.

#### autovetting-recall-audit-wave19-2026-08-07 — ready (pushed directly)

- Status: ready
- Started: 2026-08-07 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 19 — oldest-first sweep of the three oldest unverified numbers (12V499 / 13V252 / 13V561) and complete-set rebuilds of the slugs carrying them: honda-ridgeline-2012, jeep-wrangler-2012, lexus-rx350-2011
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-07.md (gitignored), TASKS.md
- Notes:
  2026-08-07 02:00: recall-audit WAVE 19. EIGHT fabrications deleted across 3 slugs — every numbered
  recall on all three failed verification except 16V-061 on the Ridgeline (which also had its
  "2007-2014 Ridgeline" scope note confirmed correct). Deleted: ridgeline 12V-499 (unresolvable) +
  15V-441 (= KTM 1290 Super Duke R MOTORCYCLE fuel-tank leak — wrong VEHICLE CLASS, the wave-17
  signature); wrangler 13V-252 (= 1993-98 Grand Cherokee / 2002-07 Liberty fuel-tank rear-impact recall,
  1.56M units — real Jeep campaign, wrong model AND era), 14V-373 (= Dodge Journey / Grand Caravan /
  Town & Country ignition switch, FCA R03), 15V-340 (= Ford/Lincoln/Mercury electric power steering
  assist, 15S18, 393,623 units — cross-MAKE collision), 17V-525 + 18V-079 (unresolvable); rx350
  13V-561 (unresolvable — the 2011 RX 350 has exactly one NHTSA recall, 11V-377).
  NEW SIGNATURE: "real campaign, wrong model within the same corporate parent" (13V-252, 14V-373) —
  harder to catch than cross-make because the manufacturer name matches. ALSO NEW: a number invented for
  an issue that was never a recall at all — the Pentastar left-bank cylinder-head defect was a warranty
  extension/TSB, never an NHTSA campaign; the inspection item (P0302, TSB 09-005-12) was kept, only the
  fake number removed.
  HEADLINE FIX: the 2012 Ridgeline was MISSING 22V-430 — rear frame corrosion at the fuel-tank
  mounting-band surface, 2006-2014, 22 salt-belt states + DC, ~112k trucks, tank can detach and leak,
  Honda has repurchased severely corroded vehicles. It was absent while the fabricated "Hood Latch" entry
  occupied its place.
  Complete verified sets added (cars.com per-MY NHTSA feeds, WebSearch provenance): ridgeline
  22V-430/19V-501/19V-500/19V-182/18V-662/18V-268/18V-041/17V-029/16V-061/12V-432/12V-025 (11);
  wrangler 13V-234 (power steering line wearing through the trans cooler line — the one campaign a JK
  buyer can act on) + 14V-631 mirror-connector fire + Takata 19V-018/18V-021/16V-352 + four
  RIGHT-HAND-DRIVE-only campaigns explicitly scoped as such in the copy (19V-680/16V-288/13V-176 and
  11V-528 retained as the superseded predecessor of 13V-176) (9); rx350 11V-377 brake actuator VDIM
  calibration, with LSC 90G relabelled as a Toyota Limited Service Campaign rather than a recall and
  scoped to 2010 builds (1 + 1). stats.recalls re-synced to array length 12/10/3. VIN-check closing line
  retained on all 3.
  Ledger: verified 149 -> 173 (20 citable adds + 4 do-not-add records for the fabrications that resolved
  to real unrelated campaigns); unverified_legacy 59 -> 51. Wave-20 queue: 14V028/14V153/14V290, then
  ledger order.
  Sibling check: In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal; working tree carried no
  sibling edits tonight (clean at start of run). Ready = wave18p2/wave18p1/wave17 (already pushed
  6a2b3ba/fd4ddbf/6143b3f), same files but additive on disjoint slugs; Verified against:
  autovetting-recall-audit-wave18p2-2026-08-06. Done (last 10) all carry - Started: (checked, no backfill
  needed). No Re-sync needed.
  Syntax-check: PASS. Dead-links: verified (no links added). Scanner: PASS (496 files, exit 0).
  Gate-check: 27 pass / 2 warn / 0 CRIT (G28 clean). Truncation guard: 17,717 lines / 1,370,286 bytes
  (was 17,704 / 1,365,333), tail intact. Commit: d6d6550 (content), pushed with the docs commit.

#### autovetting-recall-audit-wave18p2-2026-08-06 — ready (pushed directly)

- Status: ready
- Started: 2026-08-06 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 18 (part 2 of 2) — complete-set rebuilds for the remaining 5 collision slugs (outlander/kicks/qx60/ioniq5/carnival). Collision-cleanup arc CLOSED: all 10 wave-17 collision slugs rebuilt.
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-06.md (gitignored), TASKS.md
- Notes:
  2026-08-06 02:00: recall-audit WAVE 18 part 2. Purely additive — the 5 slugs carried only the VIN-check
  placeholder after wave 17. Sets added (cars.com per-year NHTSA feeds, WebSearch provenance):
  outlander-2017 17V-609/18V-620/18V-621/20V-403/26V-252 (26V-252 = nationwide expansion of regional
  25V-507); kicks-2019 19V-654 (sole campaign); qx60-2018 19V-807 only (18V-601 re-recall/expansion;
  16V-244 confirmed not applicable — OCS scope stops at 2014-2016 QX60); ioniq5-2022 22V-324 + 24V-868
  (replaces 24V-204, prior-remedy cars need the new fix); carnival-2022 21V-277/21V-908/23V-179/23V-236/
  24V-025/26V-232. stats.recalls re-synced 6/2/2/3/7; VIN-check closing line retained on all 5.
  Ledger verified 134->149 (13 citable + 2 cite-the-successor predecessor notes 25V507/24V204);
  unverified_legacy unchanged at 59. Wave-19 queue: oldest-first 12V499/13V252/13V561.
  Sibling check: In-flight autovet-competitor-monitor (Competitors/ + TASKS.md notes only — its
  2026-08-06 01:09 cycle-1-complete Notes block was uncommitted and rides in tonight's docs commit with
  attribution, same handling as wave 17), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/),
  autovet-seo-content (Content/blog/) orthogonal. Ready = wave18p1/wave17 (already pushed fd4ddbf/
  6143b3f), same files but additive on disjoint slugs; Verified against:
  autovetting-recall-audit-wave18-2026-08-05. Done (last 10) all carry - Started: (checked, no backfill
  needed). No Re-sync needed.
  Syntax-check: PASS. Dead-links: verified (no links added). Scanner: PASS (495 files, exit 0).
  Gate-check: 27 pass / 2 warn / 0 CRIT (G28 clean — 25V-507/18V-601/24V-204 prose citations ledgered
  pre-gate). Truncation guard: 17,704 lines / 1,365,333 bytes (was 17,689 / 1,361,375), tail intact.
  Process note: first edit attempt aborted safely on sentinel assert (placeholder text matched twice in a
  fixed 9,000-char window — adjacent-slug bleed); redone with bracket-balanced first-array-after-slug
  targeting. Commit: 6a2b3ba (content), pushed with this docs commit.

#### autovetting-recall-audit-wave18-2026-08-05 — ready (pushed directly)

- Status: ready
- Started: 2026-08-05 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 18 (part 1 of 2) — complete-set rebuilds for the first 5 collision slugs (sentra/pathfinder/mustang/bmw-3series/outback), incl. verification of the Outback's two surviving numbers (both failed)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-05.md (gitignored), TASKS.md
- Notes:
  2026-08-05 02:00: recall-audit WAVE 18 part 1. THREE more fabrications deleted: sentra 14V-344
  ("Takata Airbag") = Mazda Takata regional campaign — cross-make collision #6; outback 14V-787 +
  20V-696 BOTH unresolvable to real campaigns (Subaru Takata scope = 2003-05 only; Subaru Denso pump =
  20V-218, 2019 MY) — the plausible-theme-wrong-number signature. Complete verified sets added:
  sentra 17V-253/18V-551/21V-135; pathfinder 18V-601+19V-807 (scoped 16V-244 entry retained, scope
  re-verified); mustang 17V-814/18V-213; bmw-3series 18V-465 gas + 21V-586/21V-907 328d-diesel-scoped;
  outback 14V-577/15V-366/15V-502/16V-251 (16V-292 excluded — 2016-only build window). stats.recalls
  re-synced 4/4/3/4/5; VIN-check closing line on all 5. Ledger unverified 62->59, verified 116->132
  (13 citable + 3 do-not-add). Sources: cars.com per-year NHTSA feeds via WebSearch provenance gate.
  Remainder queued: outlander-2017/kicks-2019/qx60-2018/ioniq5-2022/carnival-2022 rebuilds, then
  oldest-first 12V499/13V252/13V561.
  Sibling check: In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) orthogonal; working tree carried no
  sibling edits tonight. Ready = wave17/wave16 (already pushed 6143b3f/b7b2114), same files but
  additive on disjoint slugs; Verified against: autovetting-recall-audit-wave17-2026-08-04. Done
  (last 10) all carry - Started: (checked, no backfill needed). No Re-sync needed.
  Syntax-check: PASS. Dead-links: verified (no links added). Scanner: PASS (485 files, exit 0).
  Truncation guard: 17,689 lines / 1,361,375 bytes (was 17,675 / 1,357,640), tail intact. Process
  note: first edit attempt used stale slug indices after earlier in-file replacements shifted offsets —
  caught by old-length anomaly, restored from HEAD, redone with per-iteration lookup + sentinel asserts.
  Commit: fd4ddbf (content), pushed with this docs commit.
  2026-08-05 02:55: G28 pre-push gate CRIT-failed on 18V-755/25V-700 cited in the 21V-907 prose but not
  ledgered (the known scope-only-citation gate behavior) — both added to verified with superseded/expansion
  scope notes (132->134). Fixup commit below; gates then clean.

*Tasks finished locally and verified. The hub orchestrator only pushes what's in this section.*

#### autovetting-recall-audit-wave17-2026-08-04 — ready (pushed directly)

- Status: ready
- Started: 2026-08-04 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 17 — nissan-frontier-2018 rebuild (both numbers fake) + the wave-16 cross-MAKE collision sweep across all 68 unverified_legacy numbers
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-04.md (gitignored), TASKS.md
- Notes:
  2026-08-04 02:00: recall-audit WAVE 17. Net: 12 fabricated entries deleted across 11 slugs (7 distinct
  fake numbers), complete verified 2018 Frontier set added (18V-551 ignition switch + 19V-654 back-up
  camera, cars.com/NHTSA feed via WebSearch provenance), ledger unverified 68->62 / verified 108->116.
  Sweep found 5 cross-make collisions, all fabricated: 16V-028 (Autocar refuse-truck brake pin) on
  bmw-3series-2018 + ford-mustang-2018; 17V-148 (72-van Mercedes Metris BSM) on subaru-outback-2015 +
  mitsubishi-outlander-2017; 17V-224 (Kia GDI engine debris) on nissan-sentra-2017 + nissan-kicks-2019;
  14V-400 (GM 6.7M-unit ignition) on nissan-pathfinder-2017 + infiniti-qx60-2018; 22V-714 (Micro Bird
  bus) on hyundai-ioniq5-2022 + kia-carnival-2022. 12V-395 on the Frontier = Roadtrek motorhome awning
  rivets. Deleted entries replaced with the standard VIN-check line where arrays would empty;
  stats.recalls re-synced on all 11 slugs. Real Pathfinder/QX60 CVT-contamination checklist items
  untouched (TSB/class action, not a recall). Complete-set rebuilds for the 10 collision slugs = wave-18
  queue in Build-Log/2026-08-04.md. No cross-make collisions remain in the unverified set.
  Sibling check: In-flight autovet-competitor-monitor (Competitors/ + TASKS.md notes only) orthogonal —
  its uncommitted 2026-08-03 16:20 VINsight Notes block is included in tonight's docs commit with
  attribution; autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) upstream-complementary (17V-224
  Kia scope matches its Kia protocol, now also ledgered); autovet-seo-content (Content/blog/) orthogonal.
  Ready = wave16 (already pushed as b7b2114). Done (last 10) all carry - Started: (checked, no backfill
  needed). No Re-sync needed. Verified against: autovetting-recall-audit-wave16-2026-08-03.
  Syntax-check: PASS. Dead-links: verified (no links added). Scanner: PASS (480 files, exit 0).
  Truncation guard: 17,675 lines / 1,357,640 bytes, tail intact. Commit: 6143b3f (content), pushed with this docs commit.

#### autovetting-recall-audit-wave16-2026-08-03 — ready (pushed directly)

- Status: ready
- Started: 2026-08-03 (15:45 MST, manually-triggered second run of the day; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 16 — drain the wave-15 queue (2010 Highlander complete set, ford-escape-2013 / 22V-413, oldest-first 11V-260) plus the 16V-244 ledger conflict raised by the Infiniti CPO run
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-03.md (gitignored), TASKS.md
- Notes:
  2026-08-03 15:45: recall-audit WAVE 16. Wave 15 fired at 02:00 the same day; this run is the direct
  continuation of the queue it wrote. Net: 6 fabricated entries + 1 false Takata claim deleted across 3
  slugs, 39 verified entries added, 1 checklist item rewritten, 1 wrong ledger entry corrected. All three
  wave-15 queue items closed.
  (1) toyota-highlander-2010 — the pull wave 15 was blocked on. Complete set is 8 campaigns; the slug had
  one. Added 15V-689 (power window master switch short/melt, Toyota C0M), 14V-168 (spiral cable / FFC,
  driver airbag deactivated), 13V-014 (SET occupant-sensing recalibration), 16V-396 + 14V-743 (SET
  accessory seat heaters — remedy is disconnect-and-refund, so a remedied car has dead seat heaters by
  design), 13V-123 + 10V-035 (SET / Gulf States load-capacity labels). 10V-036 deliberately NOT added
  (2006-2009 Sienna only) and 10V-017 KEPT despite being absent from the cars.com feed — wave 15 verified
  it against campaign text; both calls are now written into the page, not just a build log. Five of eight
  campaigns are regional-distributor actions, so the VIN-check entry leads with delivery region.
  (2) ford-escape-2013 — FOUR fabricated numbers plus a Takata campaign this vehicle does not have.
  14V-350 claimed "Steering Shaft Coupler" = GM 2000-2005 Impala/Monte Carlo + 1997-2005 Malibu + Alero /
  Intrigue / Grand Am / Grand Prix ignition-key campaign, 6,729,742 units DEL. 14V-090 claimed "MyFord
  Touch Software" = PORSCHE 2014 911 GT3 connecting-rod / crankcase fire (AE01) DEL. 17V-243 claimed
  "Fuel Injector / Engine Stall" = MERCEDES-BENZ 2016-2017 C300 EPS rack, 3 units DEL. 16V-449 claimed
  "Power Liftgate / Brake Fluid" = GM 2016 Equinox / Terrain certification labels DEL. The "Multiple —
  Takata Airbag (select builds)" entry DEL: no Takata campaign exists on the 2013 Escape. Complete
  verified set added — 17 campaigns, the highest count on the site, four of them separate 1.6L EcoBoost
  fire-risk actions (12V-336, 12V-431, 12V-551, 13V-583) plus 13V-584 which exists because the 12V-336
  repair was sometimes done wrong. 22V-413 added (closing the wave-15 queue item) together with its
  predecessor 18V-471 — a 2013 Escape is in scope for BOTH shift-cable campaigns. Also 14V-597 + 14V-237
  (restraint module), 14V-495 + 15V-813 (MAP splice stall), 14V-239 + 16V-643 + 20V-331 (doors/latches),
  14V-164, 13V-085, 12V-319. Rewrote the "Multiple active recall campaigns" checklist item, which sourced
  itself to 13V-583, 14V-090, 14V-350 and described an HVAC campaign that does not exist.
  (3) subaru-forester-2011 — both numbered recalls fabricated. 11V-260 claimed "Brake Line Corrosion
  (salt belt)": defect real, number not — 11V-260 files as an AMERICAN HONDA campaign; the actual Forester
  campaign is 14V-311 (WQK-47) with follow-up 14V-830 (WQQ-52) for repairs done before 2014-12-23 under
  incomplete dealer instructions. Both added, DEL. 14V-668 claimed "Brake Pedal Bracket" = INFINITI Takata
  driver-inflator on 2013 QX56 / 2014 QX80 (R1414) DEL. Complete set added — 16 campaigns, ten of them
  Takata passenger-inflator actions issued per zone and tranche, three of which (20V-001/002/003)
  re-replace inflators a prior recall already replaced. Also 22V-838, 12V-099, 16V-738 (TURBO ONLY),
  12V-602, 19V-297 (replacement-part switches only).
  (4) LEDGER CORRECTION — 16V-244, the conflict raised by autovet-cpo-protocol-ingestion earlier today.
  Ledger said makes:["Nissan"] and "— NOT 2017+ and NOT Infiniti"; both halves wrong. Campaign covers
  2014-2017 Rogue, 2016-2017 Maxima, 2014-2017 Infiniti Q50, 2014-2016 QX60/QX60 Hybrid/Q50 Hybrid and the
  2013 JX35, and the remedy DIFFERS by model (ACU+OCS reflash vs OCS ECU replacement). Rewritten with full
  scope and the remedy split; narrowed and corrected, not deleted. Flag closed.
  (5) SYSTEMIC SWEEP (wave-15 item) — first hit, queued not fixed: nissan-frontier-2018 carries 14V-168 as
  "Fuel Tank Strap", but 14V-168 is the Toyota spiral-cable campaign verified on the Highlander in this
  same run — a cross-MAKE collision. Same slug also carries 12V-395, a 2012 number on a 2018 truck. Fixing
  both needs the complete 2018 Frontier set = wave 17. 14V-168's ledger note now reads "TOYOTA ONLY" and
  names the Frontier entry as a known collision.
  stats.recalls re-synced to array length on all three slugs (Highlander 2->9, Escape 6->18,
  Forester 3->17).
  Ledger: unverified_legacy 75 -> 68 (11V260, 14V668, 14V350, 14V090, 17V243, 16V449, 14V168 removed);
  verified 72 -> 108 (34 campaign entries added with sources, plus 10V036 / 15V246 / 17V210 ledgered as
  SCOPE-ONLY PROSE CITATIONS with explicit do-not-add-as-an-entry notes, and 16V244 corrected).
  Wave 17 queue: (a) nissan-frontier-2018 complete set — 14V-168 + 12V-395; (b) SYSTEMIC — sweep the
  remaining 68 for cross-MAKE collisions (same number, two makes) before going oldest-first; it is the
  highest-yield signature found so far (this wave alone: a Porsche, a Mercedes, two GM and one Infiniti
  number sitting on Ford/Subaru slugs); (c) resume oldest-first 12V499, 13V252, 13V561; (d) three
  campaigns found this wave (13V-584, 20V-331, 14V-830) exist ONLY because an earlier remedy was performed
  incorrectly — "verify recall complete" is under-specified for these, consider a standing convention.
  Sibling check: no blocking conflict. Only Done siblings sharing inspect/index.html + recall-ledger.json
  are the wave-15/14/13 recall-audit blocks and the vinnote batches; this run is the direct continuation
  of wave 15's own queue and touches three slugs none of them touched (toyota-highlander-2010 was READ by
  wave 15 but its complete-set pull was blocked and left unwritten). Verified against:
  autovetting-recall-audit-wave15-2026-08-03. Coalesced the wave-15 Ready block into Done (already pushed
  as bfe6463) so Ready holds only this run. All Done (last 10) blocks carry a - Started: field; none
  needed backfilling. In-flight autovet-competitor-monitor (Competitors/, next = VINsight.ai),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Infiniti completed 15:40 today, next = VW) and
  autovet-seo-content (Content/blog/) are orthogonal — this commit also carries the Infiniti run's
  uncommitted TASKS.md in-flight note, which touches no file this task touches. No Re-sync needed.
  Syntax-check: PASS. Truncation guard: 17,678 lines / 1,356,319 bytes (was 17,645 / 1,336,451), tail
  intact. Ledger: valid JSON, 108 verified / 68 unverified_legacy. Dead-links: verified (no links added or
  changed). Gate-check: 27 pass / 2 warn / 0 CRITICAL (G28 initially CRIT-failed on the three scope-only
  prose citations; resolved by ledgering them, per the known gate quirk). Scanner: PASS (474 files,
  exit 0).
  Commit: b7b2114.


## Done (last 10)

#### autovetting-recall-audit-wave15-2026-08-03 — ready (pushed directly)

- Status: ready
- Started: 2026-08-03 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 15 — clear the wave-14 queue (22V-413 Fusion year scope; _hub archive sweep) and resume top-down through the oldest unverified_legacy numbers
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-03.md (gitignored), _hub/Product/Landing-Page/index.html + ARCHIVED-DO-NOT-REUSE.md (gitignored), TASKS.md
- Notes:
  2026-08-03 02:00: recall-audit WAVE 15. No run fired 2026-08-02 (no Build-Log entry, no commit) — this
  run picks up the wave-14 queue as written. Net: 8 fabricated entries deleted across 3 slugs, 11 verified
  entries added across 2, 1 checklist item + 2 prose descriptions rewritten, all 3 queued wave-14 items
  closed.
  (1) 22V-413 QUEUE ITEM RESOLVED — wave 14 was right to exclude it. Part 573 scope confirmed as 2013-2019
  Escape, 2013-2018 C-Max, 2013-2016 FUSION, 2013-2021 Transit Connect, 2015-2018 Edge (~2.9M, 6F35). The
  Fusion years stop at 2016, so nothing added to ford-fusion-2017. Ledger component string for 22V413
  rewritten to name years per nameplate (it previously said "Fusion" with no years — the exact ambiguity
  that would have caused a future re-add) and now cites the Part 573 PDF directly.
  (2) toyota-tacoma-2012 — WORST SINGLE-SLUG RESULT SO FAR: all five numbered recalls were fabrications,
  none present in the truck's actual 7-campaign NHTSA set. 05V-449 (no such applicable campaign; the real
  ball-joint recall is 05V-225/campaign 50J, 2001-2004 Tacoma + 2002-2004 Tundra/Sequoia + 2001-2002
  4Runner) DEL. 14V-053 claimed as "Center Console Trim" = the Prius inverter IPM campaign (2010-2014
  Prius / 2012-2014 Prius v) DEL. 14V-657 claimed as "Tire Information Label" = a YAMAHA MOTORCYCLE recall
  DEL. 15V-394 claimed as "Seat Belt Pretensioner" = NAVISTAR International Durastar/Workstar + IC Bus
  grid-heater cable DEL. 20V-697 claimed as "Air Bag Module" = LION ELECTRIC school-bus wheelchair belt
  anchors DEL. Three commercial-vehicle campaign numbers on one light-duty pickup = list generated without
  ever touching NHTSA. Complete verified set added (7): 14V-054 (brake actuator, VSC/ABS/TRAC inoperative —
  the only factory Toyota campaign on this truck), 17V-425, 14V-475, 13V-494, 13V-123, 13V-014, 12V-158
  (six of the seven are Southeast/Gulf States distributor or accessory campaigns; region + accessory scope
  written into each description, and the VIN-check line rewritten to say so). Also rewrote the checklist
  item "Lower ball joints (early-recall era)" — it asserted a 2005-2008 second-gen ball-joint recall that
  does not exist and sourced itself to 05V-449; now titled "wear item, not a recall on this truck", states
  the correct 05V-225 scope, and the check separates ball-joint from tie-rod play.
  (3) toyota-4runner-2008 — both numbers wrong. 08V-528 claimed as "Floor Mat / Accelerator, large Toyota
  recall" = CHRYSLER, 712 MY2009 Sebring/Caliber/Avenger/Journey/Patriot/Compass PCM adhesive circuit-board
  crack DEL. 14V-312 claimed as "Differential Pinion Nut" = real Toyota but the Takata passenger inflator
  campaign for 2002-2004 Sequoia/Lexus SC + 2003-2004 Corolla/Matrix/Tundra/Vibe (844,277 units), no
  4Runner DEL. The truck DOES have a real floor-mat campaign we were not citing: 11V-113 (Toyota 90L /
  Lexus 90LG, 2003-2009 4Runner + 2008-2011 LX570 + 2006-2010 RAV4) — added. Complete set also added
  16V-396 + 14V-743 (SET accessory seat heaters, copper-strand short/fire; remedy is disconnect-and-refund,
  so an open one may just mean the heat was switched off) and 10V-035 (GST load-capacity labels). 10V-036
  appears in the 2008 4Runner feed but scopes to 2006-2009 Sienna only — deliberately NOT added, noted in
  the Build-Log so a later run doesn't add it.
  (4) toyota-highlander-2010 — 14V-053 mis-paste, SECOND SIGHTING ("Hybrid Inverter, Hybrid models only").
  Campaign covers 2010-2014 Prius + 2012-2014 Prius v only; Highlander Hybrid is not in it. DEL. 14V053
  stays verified for toyota-prius-2012 where it is correct, but its ledger note now reads "Prius/Prius v
  ONLY — do not apply to any non-Prius slug". 10V-017 on the same slug CHECKED OUT (CTS accelerator-pedal
  friction lever genuinely covers the 2010 Highlander) — moved to verified, and its description rewritten
  because it was conflating the pedal-mechanism recall with the floor-mat campaigns of the same era. The
  Highlander complete-set pull was blocked this run (cars.com URL for that year unreachable) — queued for
  wave 16.
  (5) _hub ARCHIVE SWEEP (wave-14 collateral item) CLOSED — _hub/Product/Landing-Page/index.html carried
  15V-128, 05V-449, 08V-528, 14V-312, 14V-657, 15V-394, 20V-697, 18V-114, 18V-307, 19V-237, 20V-014. It
  now opens with an ARCHIVED / DO-NOT-REUSE banner naming all of them and pointing at inspect/index.html +
  the ledger as source of truth; folder also gets ARCHIVED-DO-NOT-REUSE.md. Every other _hub hit for a
  deleted number is a Build-Log, a CPO-protocol anti-fabrication guard or an Awaiting-Daniel entry
  DOCUMENTING the deletion — correct, left alone. Path is gitignored (.gitignore:31), ships nothing.
  stats.recalls re-synced to array length on all three slugs (Tacoma 6->8, 4Runner 3->5, Highlander 3->2).
  Ledger: unverified_legacy 82 -> 75 (05V449, 08V528, 10V017, 14V312, 14V657, 15V394, 20V697 removed);
  verified 59 -> 72 (10V017, 10V035, 11V113, 12V158, 13V014, 13V123, 13V494, 14V054, 14V475, 14V743,
  16V396, 17V425 added with sources, plus 05V225 — the real Toyota ball-joint campaign, ledgered because
  the rewritten Tacoma item cites it for scope; gate G28 correctly caught it as unledgered on first run).
  Wave 16 queue: (a) 2010 Highlander complete set (blocked this run); (b) ford-escape-2013 is in scope for
  22V-413 (2013-2019 Escape) and does not list it — pull the Escape's complete set and add properly;
  (c) resume oldest-first through the remaining 75: 11V260 (subaru-forester-2011), 12V395
  (nissan-frontier-2018 — a 2012 number on a 2018 truck, flag it), 12V499, 13V252, 13V561; (d) SYSTEMIC —
  three of this wave's five Tacoma numbers were commercial-vehicle campaigns (motorcycle, Class-6 truck,
  school bus), so sweep for other non-light-duty numbers sitting on car slugs.
  Sibling check: no blocking conflict. Only Done siblings sharing inspect/index.html + recall-ledger.json
  are autovetting-recall-audit-wave14-2026-08-01 and wave13-2026-07-31 — this run is the direct
  continuation of wave 14's own queue, additive and non-overlapping (wave 14 touched acura-tsx-2014 +
  ford-fusion-2017; wave 15 touches toyota-tacoma-2012, toyota-4runner-2008, toyota-highlander-2010 only).
  Verified against: autovetting-recall-audit-wave14-2026-08-01. Coalesced the wave-14 Ready block into Done
  (already pushed as 02cb107) so Ready holds only this run. All Done (last 10) blocks carry a - Started:
  field; none needed backfilling. In-flight autovet-competitor-monitor (Competitors/, next = VINsight.ai),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next = Infiniti) and autovet-seo-content
  (Content/blog/) are orthogonal. No Re-sync needed.
  Syntax-check: PASS. Truncation guard: 17,645 lines / 1,336,451 bytes (was 17,642 / 1,332,580), tail
  intact. Ledger: valid JSON, 72 verified / 75 unverified_legacy. Dead-links: verified (no links added or
  changed). Gate-check: 27 pass / 2 warn / 0 CRITICAL. Scanner: PASS (470 files, exit 0).
  Commit: bfe6463.

#### autovetting-recall-audit-wave14-2026-08-01 — ready (pushed directly)

- Status: ready
- Started: 2026-08-01 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Task: recall-audit wave 14 — drain the two numbers wave 13 left queued (15V-128 on acura-tsx-2014, 19V-006 on ford-fusion-2017)
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-01.md (gitignored), TASKS.md
- Notes:
  2026-08-01 02:00: Both queued numbers resolved as fabrications on primary-source lookup; both vehicles
  yielded a clean complete NHTSA set to replace them with. Net: 2 fabricated entries deleted, 7 verified
  entries added.
  (1) 15V-128 on acura-tsx-2014 (claimed "Hood Latch Inspection") = Forest River Wildcat 2015 fifth-wheel
  trailer GVWR certification-label nonconformance, 94 units, recalled 2015-03-04. Wrong industry entirely.
  Complete 2014 Acura TSX set = exactly 3 campaigns, all Takata passenger frontal inflator, no hood latch:
  18V-661, 19V-378 (replacement inflator installed incorrectly; Honda M4O/P4R/T4Q/W4P), 19V-502
  (remedy-part inflators also degrade; Honda F5F/Q5E). Deleted + all 3 added. The 19V-378/19V-502 pair is
  the buyer-useful bit: a prior Takata repair does NOT close either one, and the page now says so.
  (2) 19V-006 on ford-fusion-2017 (claimed "Fuel Injector O-ring (2.0T)") = Ferrari North America Takata
  passenger frontal inflator campaign (2019-01-08, California/458/FF/F12/488/GTC4Lusso). Wrong
  manufacturer. Complete 2017 Ford Fusion set = exactly 4 campaigns, none fuel-related: 16V-874 (seat-back
  pivot pin welds, 25 units, Ford 16S43), 17V-427 (torque converter weld studs, 2.0L + 6F35, Ford 17S16),
  18V-167 (steering wheel retaining bolt, 2014-2018, 1.30M units, Ford 18S08), 23V-162 (front brake jounce
  hoses, 2013-2018 non-hybrid, 1.28M units, Ford 23S12). Deleted + all 4 added; the vague "Four recalls
  possible" Documentation item rewritten to name them and flag 18V-167 + 23V-162 as the two that matter on
  a used lot. 18V-390 (already verified, wave 13) is the 17S16-S2 expansion but covers Edge/MKZ not Fusion
  — correctly NOT added. 22V-413 deliberately NOT added to the Fusion despite its ledger nameplate list
  (absent from the complete 2017 set = its Fusion years are likely earlier) — queued for wave 15.
  stats.recalls re-synced to array length on both slugs (TSX 2->4, Fusion 2->5).
  Ledger: unverified_legacy 84 -> 82 (15V128, 19V006 removed); verified 52 -> 59.
  Collateral (not shipped): _hub/Product/Landing-Page/index.html still holds 2 copies of the fabricated
  15V-128 entry. That path is gitignored (.gitignore:31 _hub/) so it deploys nothing, but it is a
  pre-audit snapshot that would reintroduce deleted numbers if reused — queued for wave 15 to mark
  ARCHIVED or delete.
  Sibling check: no blocking conflict. Only Done sibling sharing inspect/index.html + recall-ledger.json is
  autovetting-recall-audit-wave13-2026-07-31 (Done, yesterday) — this run is the direct continuation of its
  own wave-15 queue, additive and non-overlapping (different slugs: wave 13 touched Accord/Edge/GM/Ford
  clusters, wave 14 touches acura-tsx-2014 + ford-fusion-2017 only).
  Verified against: autovetting-recall-audit-wave13-2026-07-31. All Done (last 10) blocks carry a
  - Started: field; none needed backfilling. In-flight autovet-competitor-monitor (Competitors/, next =
  VINsight.ai), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next = Infiniti) and
  autovet-seo-content (Content/blog/) are orthogonal. Ready was empty. No Re-sync needed.
  Syntax-check: PASS. Truncation guard: 17,642 lines / 1,332,580 bytes, tail intact. Dead-links: verified
  (no links added or changed). Gate-check: 27 pass / 2 warn / 0 CRITICAL. Scanner: PASS.
  Commit: 02cb107.


#### autovetting-recall-audit-wave13-2026-07-31 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-31 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 [freeze] = "finish recall-audit waves")
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-07-31.md (gitignored), TASKS.md
- Commit: f7a15cb (work); this docs(tasks) record follows in a same-cadence follow-on push.
- Notes:
  2026-07-31 02:00: recall-audit WAVE 13. Launch freeze still active; no new-vehicle launch queued and
  vinNotes are fill-in-only under the ratified [freeze] priorities, so this run took priority (1),
  the recall-audit backlog. Started from the three numbers wave 12 left queued as "not dispositive"
  (16V-617 / 14V-595 / 18V-117); all three resolved as fabrications, and chasing them surfaced a
  fourth and larger one. 19 fabricated entries deleted across 16 slugs; 9 verified campaigns added.
  (1) 20V-012 [NEW FINDING] — real Toyota/Lexus Denso fuel-pump campaign (ledger-verified, correct on
      toyota-camry-2018) was ALSO pasted onto 10 GM/Ford slugs (chevy-equinox-2018, chevy-malibu-2016,
      buick-enclave-2018, buick-encore-2018, chevrolet-traverse-2018, chevrolet-trax-2019,
      gmc-acadia-2017, chevy-colorado-2018, gmc-canyon-2018, ford-fusion-2017) plus toyota-4runner-2008
      where it was labelled "Brake Booster Pump" (right make, wrong defect, and MY2008 is outside the
      2018-2020 scope). One number / three manufacturers / two defects = dispositive; same GM cluster as
      the ratified 19V-268 deletions. Deleted x11; kept on Camry + the pinpoint Camry card.
  (2) 16V-617 — REAL but it is FORD: 2017 Escape power-window closing force, Ford 16C12
      (static.nhtsa.gov/odi/rcl/2016/RCLRPT-16V617-8413.pdf). Was on our site as "Ignition Switch
      Software" on 3 GM slugs (chevy-malibu-2016, buick-encore-2018, chevrolet-trax-2019). Deleted x3.
  (3) 14V-595 — REAL but it is an ELKHART COACH / RICON WHEELCHAIR-LIFT recall on 2006-2014 Ford
      E-350/E-450 (platform side plate may crack). Was on honda-accord-2014 as "Electric Parking Brake
      Software" in BOTH the recalls array and a High-Attention checklist item. Exact wave-11 13V-261
      pattern. Deleted both. Corroborated by pulling the COMPLETE NHTSA set for a 2014 Accord = four
      campaigns only (23V-858, 20V-769, 17V-418, 15V-121) — no parking-brake campaign exists.
      Replaced with the real ones: 17V-418 (battery-sensor water intrusion / fire, Honda KG0),
      20V-769 (salt-belt drive shafts), 23V-858 (Denso fuel pump); the fabricated checklist item was
      rewritten as a 17V-418-anchored open-campaign check.
  (4) 15V-128 (hood latch) on honda-accord-2014 — collateral: not in the complete 2014 Accord set.
      Deleted from the Accord. Still on acura-tsx-2014 from the same 2026-05-30 batch run — NOT deleted
      blind (single-slug, no TSX source pulled); queued for wave 14.
  (5) 18V-117 — NO SUCH CAMPAIGN. Absent from every recall index searched (neighbours 18V-116/098/156/390
      all resolve) and absent from the complete 8-recall 2017 Edge set. Claimed as "side airbag" across
      three unrelated platforms (CD4 crossover / CD4 sedan / U553 body-on-frame). Deleted x3
      (ford-edge-2017, ford-fusion-2017, ford-expedition-2018).
  (6) 19V-006 on ford-edge-2017 — absent from the complete 2017 Edge set. Deleted + PTU-item prose
      rewritten. The ford-fusion-2017 instance is LEFT IN PLACE (no Fusion source pulled) — queued
      for wave 14. Edge gained the six real campaigns instead: 17V-123 (17C02 driver airbag),
      17V-205 (17C05 pano-roof header, FMVSS 214), 18V-390 (17S16-S2 torque converter, 2.0L),
      20V-469 (20S42 front brake hoses), 22V-413 (22S43 shift bushing, roll-away), 25V-544 (25S87 rear
      jounce hose — remedy parts not due until Aug 2026, i.e. live for anyone shopping an Edge now).
  Housekeeping: stats.recalls re-synced to recalls-array length on 11 slugs; any array emptied by a
  deletion received the standard honest "run the VIN at nhtsa.gov/recalls" entry. Ledger:
  unverified_legacy 87 -> 84 (16V617/14V595/18V117 removed; 15V128 + 19V006 deliberately retained,
  still in use), verified 44 -> 52 (8 new entries with per-campaign source + Ford/Honda internal numbers).
  Method note recorded in the Build-Log: pulling a vehicle's COMPLETE NHTSA set proves absence rather
  than failure-to-find AND supplies the real campaigns to put in place of what is deleted — adopt as the
  default for waves 14+.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/, next=VINsight.ai),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Infiniti) and autovet-seo-content
  (Content/blog/) are all orthogonal. Ready empty. Done(last 10) overlap on inspect/index.html +
  scripts/recall-ledger.json = autovetting-decision-execution-2026-07-30 (which executed the ratified
  19V-268/19V-258 deletions) — same audit workstream, disjoint campaign numbers and mostly disjoint slugs;
  Verified against: autovetting-decision-execution-2026-07-30. Remaining Done siblings are vinnote batches
  (additive per-slug vinNote fields, no recalls arrays touched). Every Done block checked for
  - Started: — all present, no backfill needed. No Re-sync needed.
  Syntax-check: PASS (node validator on inspect/index.html, exit 0; truncation guard 17,637 lines /
  1,330,907 bytes, tail </script></body></html> intact; recall-ledger.json re-parsed OK).
  Gate-check: 27 pass / 2 warn / 0 CRITICAL (backlog ratchet now 84; homepage-test-bc lazy-load warn).
  Dead-links: verified (no links added or changed — recall entries are plain prose, nhtsa.gov as text).
  Scanner: PASS (465 files, no secrets, exit 0).

#### autovetting-decision-execution-2026-07-30 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-30 (02:00 MST overnight builder; DECISION-EXECUTION run — first run after the 2026-07-29 Decision Queue ratification)
- Touched files: next/index.html, robots.txt, inspect/index.html, scripts/recall-ledger.json, index.html, blog/ (6 new post dirs + blog/index.html), sitemap.xml, llms.txt, _hub/Content/blog/ (6 drafts flipped, gitignored), _hub/Business Plan/Used_Car_Inspection_Platform_Business_Plan.md (gitignored), _hub/Go-To-Market/GTM_Strategy.md (gitignored), _hub/Competitors/Competitor_Analysis.md (gitignored), _hub/Architecture-Research-2026-05-24.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), _hub/Build-Log/2026-07-30.md (gitignored), TASKS.md
- Commit: 1d86463 (work); this docs(tasks) record follows in a same-cadence follow-on push.
- Notes:
  2026-07-30 02:00: executed the ratified run-order directives from _hub/DANIEL-DECISIONS-2026-07-29.md.
  [next-page]: next/index.html -> 14-line noindex meta-refresh+canonical redirect stub to /inspect/;
  robots.txt /next/ Disallow removed. [recall-19v268] deleted x6 (chevy-equinox-2018, buick-enclave-2018,
  buick-encore-2018, chevrolet-traverse-2018, gmc-acadia-2017, chevrolet-trax-2019) + [recall-19v258]
  deleted x4 (vw-jetta-2018, vw-tiguan-2018, volkswagen-passat-2018, vw-golf-2018); standard honest
  VIN-check entry inserted where the array lacked one; recall-ledger unverified_legacy 89 -> 87.
  [drafts]: 6 drafts flipped to published (Equinox/Explorer/Malibu/RAV4/Tucson/Grand Cherokee; Rogue/
  Ram DT/CR-V already live), render-blog.py -> 26 posts, sitemap+llms.txt updated; blogUrl cross-links
  added to the 6 same-generation checklists (18 -> 24); wrong-generation slugs deliberately not linked.
  [carfax-remessaging]: ratified line adopted verbatim on homepage (new why-card) + Business Plan
  SS3.6/4.3/9/13 (SS5 audited: no Carfax positioning, N/A) + GTM_Strategy + Competitor_Analysis (5 old-line
  instances rewritten; repo grep clean). [arch-cleanup]: Architecture-Research SS6 marked mooted.
  Awaiting-Daniel updated (EXECUTED block + 06-25 Carfax memo -> RESOLVED, watch stays).
  BLOCKED: [sprint-inbox] standing instruction — Gmail connector invalidated; Daniel must reconnect.
  Sibling check: no blocking overlap. In-flight autovet-seo-content owns Content/blog/ drafts — flip is
  Daniel-ratified publish approval of that task's outputs (complementary; Verified against:
  autovet-seo-content notes 06-17..07-29). In-flight autovet-competitor-monitor owns Competitors/_Monitor/;
  Competitor_Analysis.md edits are Daniel-ratified remessaging, consistent with that task's 06-25/07-29
  implications (Verified against: autovet-competitor-monitor). Done(last 10) = vinnote batches on
  inspect/index.html — disjoint slugs (recall arrays on GM/VW slugs vs vinNote slugs); all carry
  - Started: dates (checked, no backfill needed). No Re-sync needed.
  Syntax-check: PASS (node validator: inspect/index.html, index.html, next/index.html, blog/index.html
  + 6 new post pages, exit 0; truncation guard 17,642 lines / tail </html>). Gate-check: 27 pass / 2 warn
  / 0 CRITICAL. Dead-links: verified (6 blogUrl targets exist as rendered dirs; /inspect/ exists).
  Scanner: PASS (463 files, no secrets, exit 0).

#### autovetting-vinnote-batch-2026-07-29 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-29 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-29.md (gitignored), TASKS.md
- Commit: 639ae6e (work); this docs(tasks) record follows in a same-cadence follow-on push.
- Notes:
  2026-07-29 02:00: Launch freeze still active (most recent Awaiting-Daniel item = 2026-06-25 Carfax
  strategic-threat memo, a positioning decision, not a build one; no "lift freeze" reply present). No
  new-vehicle launch queued, so drained the next genuinely-missing Strong-tier vinNote rows: pri 74
  toyota-prius-prime-2017, 75 mazda-cx5-2017, 76 cadillac-xt5-2017. Each verified missing via a
  per-block check first. Queue 156 -> 153 rows; vinNote count 92 -> 95. Facts verified 2026-07-29:
  (1) toyota-prius-prime-2017 (ZVW52) -- SINGLE powertrain (structural note). Only the 1.8L 2ZR-FXE
      Atkinson hybrid + 8.8 kWh plug-in. Per NHTSA vPIC W5(A)-00 Toyota Prius VIN coding the 8th digit
      encodes the 2ZR-FXE hybrid variant, not an engine choice. NO Prime-specific 8th-digit letter
      invented (the NHTSA table is standard ZVW51/55, not the ZVW52 Prime) -> note redirects to the VDS
      check (confirm genuine ZVW52 plug-in Prime vs a standard ZVW50/51 liftback).
  (2) mazda-cx5-2017 (KF) -- SINGLE 2.5L NA + look-ahead CORRECTION. 2017 had only the 2.5L SkyActiv-G
      PY-VPS (187hp); the 2.5T turbo + Signature trim are MY2019+. Fixed catalog fields: trim (dropped
      Signature), engine (dropped 2.5T), summary (removed the turbo sentence), + all 8 VEHICLE_MENU trim
      labels. vinNote routes to 10th-digit year (H=2017) and scopes Denso fuel-pump recall 21V-875
      (2018-2019 only, WebSearch-verified, matches mazda-certified protocol) out of range for 2017.
  (3) cadillac-xt5-2017 (LGX) -- 8th digit 'S' = 3.6L LGX V6 (RPO LGX, ~310hp, 8AT), the sole 2017
      engine; 'S' confirmed across multiple OEM parts listings ("3.6L VIN S 8th digit opt LGX"). Note
      warns vs confusing XT5 LGX with the SRX's older LF1/LFX and ties AFM lifter/timing-chain life to
      oil-change history.
  Anti-fabrication: VIN letters asserted only where source-confirmed (XT5 'S'). Prius Prime + CX-5 2017
  are single-engine -> structural notes, no letter invented; CX-5 look-ahead turbo/Signature corrected
  rather than propagated.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/, next=UVeye),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lexus), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html -- additive
  per-slug data on DISJOINT slugs, every recent sibling carries a - Started: date (checked; no missing-
  Started backfill needed). No Re-sync needed.
  Syntax-check: PASS (node validator, exit 0; re-run after menu-label fix; truncation guard 17,639 lines).
  Dead-links: verified (no new links; vinNotes plain prose, nhtsa.gov as text). Scanner: PASS (445 files,
  no secrets, exit 0).

#### autovetting-vinnote-batch-2026-07-10 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-10 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-10.md (gitignored), TASKS.md
- Commit: e419bd5
- Notes:
  2026-07-10 02:00: Launch freeze still active (most recent Awaiting-Daniel item = 2026-06-25 Carfax
  strategic-threat memo, a positioning decision, not a build one). No new-vehicle launch queued, so
  drained the next genuinely-MISSING Strong-tier vinNote rows. Queue top was pri-70 toyota-avalon-2018
  but that slug ALREADY has a vinNote (stale queue row) -> pruned without re-authoring, then authored
  the next 3 genuinely-missing Strong rows (71 lexus-is-2018, 72 infiniti-qx80-2018,
  73 mitsubishi-outlander-2017). Each verified missing via per-block check first. Queue 158 -> 154 slugs
  (removed 4). vinNote count 89 -> 92. All facts WebSearch-verified 2026-07-10:
  (1) lexus-is-2018 (XE30) -- REAL fork. IS300 RWD = 2.0L turbo 8AR-FTS (241hp), VIN engine char 'A'
      (carpartplanet/AMSOIL confirm). IS300 AWD + IS350 = 3.5L V6 2GR-FKS, VIN char 'Z' (eBay OEM engine
      listing "3.5L VIN Z 2GRFKS AWD"). AWD IS300 detunes V6 to 260hp/6AT; IS350 = 311hp. Corrected in
      note: the field's "2GR-FSE 260hp" describes 2014-2015 IS350; for 2018 every V6 IS is the 2GR-FKS.
  (2) infiniti-qx80-2018 (Z62) -- SINGLE engine (structural note). Every 2018 QX80 = 5.6L VK56VD V8
      (400hp) + 7AT; VIN engine char 'A' = VK56VD (AMSOIL/carpartplanet). Shared w/ Armada+Titan, no
      cyl deactivation. Real decode = 2WD vs All-Mode 4WD + HBMC/air-susp + 22" pkg + Takata. Flagged
      not to confuse Z62 with the 2025 twin-turbo-V6 redesign.
  (3) mitsubishi-outlander-2017 -- REAL fork + 2 catalog corrections. ES/SE/SEL = 2.4L MIVEC four
      (166hp, 4J12) + Jatco CVT; GT = 3.0L SOHC V6 (224hp, 6B31) + conventional 6-speed AUTOMATIC (NOT
      a CVT) -> CVT-fluid check applies only to the four-cyl cars. Correction (a): US Outlander PHEV was
      NOT a 2017 (launched here as a 2018 model; US launch delayed to summer 2017) -> the field's "PHEV
      Hybrid" line is not a US-2017 option. Correction (b): the '4B12/W' 2.4 code online is the Outlander
      SPORT, not the regular Outlander (4J12) -> only the V6 code ('X') asserted w/ door-jamb verify
      caveat; NO 2.4 letter invented.
  Anti-fabrication: VIN engine letters asserted only where source-confirmed (IS 'A'/'Z', QX80 'A'). For
  single-engine QX80 the structural point was made; for the Outlander 2.4 no letter invented (4J12-vs-
  4B12 model ambiguity) and the note says so.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/, next=UVeye),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lexus), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html -- all additive
  per-slug data on DISJOINT slugs, every recent sibling carries a - Started: date (checked; no missing-
  Started backfill needed). No Re-sync needed.
  Syntax-check: PASS (node validator, Scripts 2 & 5 OK, exit 0; truncation guard: 17,636 lines / 5 closing
  </script> / tail = </html>). Dead-links: verified (no new links; vinNotes plain prose). Scanner: PASS
  (441 files, no secrets, exit 0).

#### autovetting-vinnote-batch-2026-07-09 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-09 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-09.md (gitignored), TASKS.md
- Commit: 7658225
- Notes:
  2026-07-09 02:00: Launch freeze still active (most recent Awaiting-Daniel item = 2026-06-25 Carfax
  strategic-threat memo, a positioning decision, not a build one). No new-vehicle launch queued, so
  drained the next 3 Strong-tier vinNote rows (67 mazda-mazda6-2018, 68 toyota-chr-2018,
  69 toyota-highlander-hybrid-2018). Each verified genuinely MISSING vinNote via per-block check first.
  Queue 161 -> 158 rows. vinNote count 86 -> 89. All facts WebSearch-verified 2026-07-09:
  (1) mazda-mazda6-2018 (GJ) -- REAL two-engine fork. NA 2.5L SkyActiv-G (PY-VPS, 187hp) on
      Sport/Touring; turbo 2.5T SkyActiv-G (PY-VPTS, 227hp@87 / 250hp@93) on Grand Touring / GT Reserve
      / Signature (Mazda USA 2018 press kit; Cars.com first drive). 8th VIN char encodes engine but the
      specific turbo-vs-NA letter was NOT source-confirmed this run -> forked the note via confirmed
      engine-family codes + trim->engine map + physical turbo/intercooler tell; no VIN letter invented.
  (2) toyota-chr-2018 (AX10) -- SINGLE powertrain (2.0L 3ZR-FAE Valvematic 144hp US, CVT, FWD only) ->
      structural note. CORRECTED latent error: engine code read 3ZR-FBE (flex-fuel/LPG variant) in the
      engine field + an item title; both fixed to 3ZR-FAE, the actual US engine (AMSOIL; motorreviewer;
      cararac). Global 3ZR-FBE was 2 (both in-block); 0 remain.
  (3) toyota-highlander-hybrid-2018 (XU50) -- SINGLE hybrid powertrain (3.5L 2GR-FXS D-4S V6 + eCVT +
      AWD-e, 306hp combined) -> structural note. CORRECTED latent error: 6 in-block "2GR-FKS" (the
      GAS-model code) -> 2GR-FXS (hybrid-specific variant): engine field, summary, stats, 2 item titles,
      1 source (U.S. News 2017/2018 HL Hybrid specs; JDM listings "Highlander Hybrid 2GR-FXS").
      Scoped to the hybrid block ONLY -- the 39 remaining 2GR-FKS mentions (Tacoma/Avalon/RX350/Camry
      V6 etc.) are legit gas references, left untouched (verified via diff).
  Anti-fabrication: NO 8th-digit engine letter asserted where unconfirmed -- all three notes made the
  honest structural/family-code point instead. Two latent engine-spec errors corrected in passing
  (C-HR FBE->FAE; HL-Hybrid FKS->FXS), each multi-source verified + block-scoped.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/, next=AutoTrader),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lexus), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html -- all additive
  per-slug data with Started dates present (checked; no missing-Started backfill needed). No Re-sync needed.
  Syntax-check: PASS (node validator, all scripts OK; no truncation, 17,633 lines / tail ends at </html>).
  Dead-links: verified (no new links; vinNotes plain prose). Scanner: PASS (439 files, no secrets).
  Remote main == local HEAD confirmed via HTTPS ls-remote pre-push (ahead-14 is only a stale origin/main
  tracking ref; SSH remote unfetched, runs push via explicit HTTPS URL).

#### autovetting-vinnote-batch-2026-07-08 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-08 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-08.md (gitignored), TASKS.md
- Commit: 8260f15
- Notes:
  2026-07-08 02:00: Launch freeze still active (most recent Awaiting-Daniel item = 2026-06-25 Carfax
  strategic-threat memo, a positioning decision, not a build one). No new-vehicle launch queued, so
  drained the next 3 Strong-tier vinNote rows (64 subaru-impreza-2018, 65 toyota-4runner-2018,
  66 honda-fit-2018). Each verified genuinely MISSING vinNote via per-block check first. Queue 164 -> 161
  rows. vinNote count 83 -> 86. All facts WebSearch-verified 2026-07-08:
  (1) subaru-impreza-2018 (5th-gen GK/GT) -- SINGLE engine: direct-injection 2.0L FB20 boxer (152hp) is
      the only powertrain. Subaru carries the engine family in VIN positions 4-5 (FB), NOT the 8th digit
      (8th = occupant-restraint code; cars101 + Subaru VIN-codes wikibook). Real variable = transmission:
      5-speed manual standard only on 2.0i base + 2.0i Sport, all other trims Lineartronic CVT; all AWD.
      CORRECTED latent error: engine field said "6-speed manual" -> 2018 Impreza manual is a 5-SPEED
      (Subaru of America 2018 press kit; U.S. News 2018 specs). Fixed 6->5-speed.
  (2) toyota-4runner-2018 (5th-gen N280) -- SINGLE engine: 4.0L 1GR-FE V6 (270hp) + 5-speed auto only.
      Toyota encodes the engine in the 5th VIN char (U = 1GR-FE), NOT the 8th (8th = model line; NHTSA
      4Runner VIN coding file, AMSOIL, carpartplanet "VIN U 5th digit 1GR-FE"). Real variable = drivetrain
      (SR5/TRD Off-Road part-time 4WD; Limited full-time 4WD w/ locking center diff; SR5/Limited also 2WD).
  (3) honda-fit-2018 (GK gen) -- ENGINE-CODE CORRECTION (latent fabrication): checklist said L15B7 in the
      engine field, summary, AND one item title. The US GK Fit uses the NA 1.5L L15B1 (130hp DOHC i-VTEC);
      L15B7 is the turbocharged Civic/CR-V 1.5T and appears in a Fit only as an aftermarket swap (AMSOIL
      2015 Fit L15B1; Honda L-engine Wikipedia; Axion "L15B7 swap kit" for GK5 = confirms not stock).
      Corrected all 3 in-block L15B7 -> L15B1, scoped to the Fit block only (the 15 remaining global L15B7
      mentions are legit Civic/CR-V/Accord 1.5T and were left untouched). Single engine -> Honda carries
      model/engine in 6th VIN char, 8th digit encodes grade/body not powertrain; real variable = trans
      (6MT lower trims vs CVT), verify HCF-2 fluid history.
  Anti-fabrication: NO 8th-digit engine letter asserted for any slug -- all three single-engine, so the
  honest structural point was made instead of inventing a letter. Two engine-spec errors corrected in
  passing (Impreza 6->5-speed; Fit L15B7->L15B1), each multi-source WebSearch-verified before changing.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/, next=AutoTrader),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lexus), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html -- all additive
  per-slug data with Started dates present (checked; no missing-Started backfill needed). No Re-sync needed.
  Syntax-check: PASS (node validator, all scripts OK). Dead-links: verified (no new links added; vinNotes
  are plain prose). Scanner: PASS (434 files, no secrets). Gate-check: 27 pass / 2 warn / 0 CRIT.

#### autovetting-vinnote-batch-2026-07-07 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-07 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-07.md (gitignored), TASKS.md
- Commit: 4efac49
- Notes:
  2026-07-07 02:00: Launch freeze still active (most recent Awaiting-Daniel item = 2026-06-25 Carfax
  strategic-threat memo, a positioning decision, not a build one). No new-vehicle launch queued, so
  drained the next genuinely-MISSING vinNote entries — the two rows the 07-06 run explicitly kept at
  queue top (55 lexus-rx350-2019, 58 lincoln-nautilus-2019) plus the next Strong entry (63 honda-hrv-2018).
  Each verified missing via precise per-block check first. Queue 167 -> 164 rows. vinNote count 80 -> 83.
  All facts WebSearch-verified 2026-07-07:
  (1) lexus-rx350-2019 (4th-gen AL20) -- SINGLE engine. RX350 8th VIN digit = 'Z' = 3.5L 2GR-FKS V6
      (295 hp), the only engine this badge carried (RX350 / 3-row RX350L / FWD / AWD); Toyota VIN-code
      tables + JDM Engine Direct "VIN Z 2GRFKS" confirm. vinNote disambiguates the hybrid: RX450h is a
      SEPARATE model (2GR-FXS Atkinson V6 + electric drive, different VIN engine char) -> "RX350 hybrid"
      is a contradiction.
  (2) lincoln-nautilus-2019 (1st gen) -- REAL fork. '9' = 2.0L EcoBoost turbo four (250 hp),
      source-confirmed (Turbo Auto Parts "2.0L VIN 9 8th digit turbo"). The 2.7L EcoBoost V6 (335 hp,
      twin-turbo Nano, shared w/ Edge ST) carries a different char; a '9' confirms the four not the V6.
      ONLY the '9' asserted -- no commerce source for the specific 2.7T letter this run, so the fork is
      made usable via the confirmed '9' rather than inventing the V6 letter. ALSO corrected a latent
      fabrication: checklist labeled the 2.0T as "LTG" w/ XT4/Blazer comparison + source "GM LTG pattern"
      -- LTG is GM's Ecotec 2.0T; the Nautilus 2.0T is a FORD EcoBoost. Fixed item title (2.0T LTG ->
      2.0T EcoBoost), desc (dropped GM/XT4/Blazer -> Ford 2.0L EcoBoost oil-consumption + PCV/turbo-seal),
      source (GM LTG pattern -> Ford 2.0L EcoBoost), and summary clause ("same LTG concerns" removed).
      Scoped so the 3 legitimate "GM LTG pattern" sources on real GM checklists were left untouched.
  (3) honda-hrv-2018 (RU gen) -- SINGLE engine + engine-code fix. Engine field read "1.8L L15B i-VTEC";
      L15B is Honda's 1.5L TURBO family and never went in the RU HR-V. The 2018 HR-V uses the NA 1.8L
      SOHC i-VTEC R18Z9 (141 hp; Honda Info Center / hondanews / motorreviewer). Fixed L15B -> R18Z9.
      Single engine -> Honda 8th digit encodes grade/restraint not powertrain (identical LX-Touring);
      real decode is transmission (CVT standard, verify HCF-2; 6-speed manual only on lower FWD trims).
  Anti-fabrication: specific 8th-digit letters asserted only where source-confirmed this run (RX350 'Z',
  Nautilus '9'). For the Nautilus 2.7T (no source this run) and single-engine HR-V, made the accurate
  structural point rather than inventing a letter. Two latent engine-spec errors corrected in passing
  (Nautilus GM-LTG mislabel -> Ford EcoBoost; HR-V L15B -> R18Z9), per no-fabrication + look-ahead-
  correction discipline.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all
  orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html but DISJOINT slugs
  (UX/Ram/Crosstrek 07-06, Forester/G70/Insight 07-05, etc.) -- additive JS data on different keys, no
  shared-slug conflict; every recent inspect/index.html Done sibling carries a - Started: date. No
  Re-sync needed.
  Syntax-check: PASS (new Function per-script gate, exit 0, Scripts 2 & 5 OK; truncation guard: 17627
  lines / 5 closing </script> present / brace-eval clean). Dead-links: verified (only new href is
  /decode/, an existing page; source names in prose only). Scanner: PASS (scanned 431 files, no secrets).
  Commit: 4efac49.

#### autovetting-vinnote-batch-2026-07-06 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-06 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-06.md (gitignored), TASKS.md
- Commit: e1feed6
- Notes:
  2026-07-06 02:00: Launch freeze still active (most recent Awaiting-Daniel item = 2026-06-25 Carfax
  strategic-threat memo, a positioning decision, not a build one). No new-vehicle launch queued, so
  drained the vinNote queue's next genuinely-missing entries. Cross-checked the queue against the live
  file FIRST: rows 60/61/62 (acura-mdx-2018, toyota-tundra-2018, mazda-cx9-2018) were ALREADY populated
  by a prior run and stale -> pruned, not re-authored. NOTE: rows 55 (lexus-rx350-2019) and 58
  (lincoln-nautilus-2019) are genuinely MISSING and were KEPT at queue top for next run (an initial
  coarse 80-line grep false-positived them as populated; a precise per-block check corrected this).
  Queue 173 -> 167 rows (3 authored + 3 stale pruned). vinNote count 77 -> 80. All engine codes +
  model-year facts WebSearch-verified 2026-07-06:
  (1) lexus-ux-2019 (1st-gen MZAA/MZAH) -- CORRECTED an engine-code error: the UX250h hybrid was listed
      as "2.0L A25A-FXS" but A25A is the 2.5L Camry/RAV4 hybrid engine; the UX250h uses the 2.0L
      M20A-FXS (AMSOIL/carpartplanet/EngineDNA confirm). Fixed engine field A25A->M20A. vinNote: model
      badge is the decode (UX200 = gas M20A-FKS, FWD-only; UX250h = M20A-FXS hybrid, 181 hp comb.,
      FWD or E-Four AWD); a UX200 is never AWD; any "2.5L" on a UX is mislabeled.
  (2) ram-2500-2019 (5th-gen DS) -- REAL 8th-digit fork, both source-confirmed: 'J' = 6.4L 392 HEMI V8
      (410 hp; SP Precision crate-engine "VIN J 14-21", norcaldiesel) vs 'L' = 6.7L Cummins turbodiesel
      I6 (Winnipeg Engine "6.7 Cummins VIN code L"). vinNote also clarifies the 2500 for 2019 gets the
      Standard-Output 6.7 (370 hp/850 lb-ft); the High-Output (up to 1,000 lb-ft) was 3500-exclusive
      that year, so a 2500 listed with "1,000 lb-ft" is a 3500 or re-tune.
  (3) subaru-crosstrek-2018 (2nd-gen GT) -- CORRECTED two errors: engine code FB20B (1st-gen port-inj)
      -> FB20D (2nd-gen direct-inj, 152 hp; Wikipedia/motorreviewer), and dropped a "2.0L PHEV Hybrid
      (148hp system)" LOOK-AHEAD -- the Crosstrek Hybrid (FB20 + Toyota PHEV system) is a 2019 MY
      CARB-compliance car (Subaru media / Wikipedia), so a 2018 is gas-only. Single engine -> 8th digit
      does not fork it (FB-family Subarus encode emissions market there); real decode is transmission
      (2.0i/Premium 6MT-or-CVT, Limited CVT-only; Subaru press kit).
  Anti-fabrication: asserted specific 8th-digit letters only where a source confirmed them this run
  (Ram 'J'/'L'). For single-engine UX/Crosstrek, made the accurate structural point rather than
  inventing a letter. Two latent engine-spec errors corrected (UX A25A->M20A; Crosstrek FB20B->FB20D +
  PHEV year), consistent with the project no-fabrication + look-ahead-correction discipline.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Mazda note appended 07-05), autovet-seo-content
  (Content/blog/) all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html
  but DISJOINT slugs (Forester/G70/Insight 07-05, RDX/Passport/RAV4 07-04, etc.) -- additive JS data,
  different keys, no shared-slug conflict; every recent inspect/index.html Done sibling carries a
  - Started: date. No Re-sync needed.
  Syntax-check: PASS (new Function per-script gate, exit 0, Scripts 2 & 5 OK; truncation guard: 17624
  lines / closing </script> present / brace-eval clean). Dead-links: verified (no new href added;
  source names in prose only). Scanner: PASS (scanned 430 files, no secrets). Commit: e1feed6.

#### autovetting-vinnote-batch-2026-07-05 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-05 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-05.md (gitignored), TASKS.md
- Commit: fe09b2a
- Notes:
  2026-07-05 02:00: Drained the vinNote queue's next three genuinely-missing entries (pri 52/53/54).
  Cross-checked the queue against the live file first: rows 50 (hyundai-kona-2019) and 51 (mazda3-2019)
  were ALREADY populated by a prior run and stale in the queue -> pruned, not re-authored
  (queue 178 -> 173 rows). Added vinNote to three checklists in inspect/index.html (count 74 -> 77);
  all engine codes + model facts WebSearch-verified 2026-07-05:
  (1) subaru-forester-2019 (5th-gen SK) -- single engine 2.5L FB25D NA + Lineartronic CVT on all trims
      (no XT turbo, no manual), so the 8th digit does NOT separate engines; on these Subarus it encodes
      only the emissions market: 'A' = federal/49-state, 'C' = California (same FB25D). vinNote reframes
      the decision points as trim + EyeSight recalibration + CVT fluid history.
  (2) genesis-g70-2019 (1st-gen IK) -- REAL 8th-digit split, both confirmed: 'A' = 2.0L Theta II T-GDI
      turbo four (252 hp; eBay OEM "2.0L VIN A 8th Digit" + Bumper decoder) vs 'E' = 3.3L Lambda II
      twin-turbo V6 (365 hp; carpartplanet/reman-engine "3.3L VIN E 8th digit"). vinNote also corrects a
      latent prose inaccuracy: "Lambda" applies only to the 3.3T V6 -- the 2.0T is a Theta II engine
      (different family) -- so read the 8th digit, not the trim name.
  (3) honda-insight-2019 (3rd-gen ZE4) -- single powertrain (two-motor 1.5L i-MMD hybrid, 151 hp comb.,
      eCVT) across LX/EX/Touring; Honda's 8th VIN char encodes grade/restraint, NOT an engine family, and
      mechanicals are identical across trims, so nothing to decode. vinNote redirects to trim + Honda
      Sensing recalibration + IPU battery health.
  Anti-fabrication: only asserted specific 8th-digit characters where a source confirmed them this run
  (G70 'A'/'E'; Forester 'A'/'C' emissions). For single-engine Insight, made the accurate structural point
  (Honda 8th char != engine code) rather than inventing a letter. Per project no-fabrication discipline.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all
  orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html but DISJOINT slugs
  (RDX/Passport/RAV4 07-04, Sonata/Venue/CT5 07-03, etc.) -- additive JS data, different keys, no
  shared-slug conflict; every recent inspect/index.html Done sibling carries a - Started: date. No Re-sync.
  Syntax-check: PASS. Dead-links: verified (no new href; nhtsa.gov in prose only). Scanner: PASS. Commit: fe09b2a.

#### autovetting-vinnote-batch-2026-07-04 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-04 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-04.md (gitignored), TASKS.md
- Commit: 986f263 (content); this docs(tasks) record follows in a same-cadence follow-on push.
- Notes:
  2026-07-04 02:00: Drained the vinNote queue's first three genuinely-missing entries (pri 46/48/49).
  Cross-checked the queue against the live file first: rows 44 (highlander-2020), 45 (model3-2019) and
  47 (lexus-es-2019) were ALREADY populated by a prior run and stale in the queue -> pruned, not re-authored
  (queue 184 -> 178 rows). Added vinNote to three checklists in inspect/index.html (count 71 -> 74);
  all engine codes + model facts WebSearch-verified 2026-07-04:
  (1) acura-rdx-2019 (3rd-gen TC1/TC2) -- single engine 2.0T K20C4 (272 hp) + 10AT, so the 8th digit is
      uniform across all 2019 RDX; the decision-relevant VIN split is FWD vs torque-vectoring SH-AWD
      (model portion, not 8th digit). Points to the 23V-858 Denso fuel-pump recall already in the checklist.
  (2) honda-passport-2019 (2nd-gen) -- single engine 3.5L J35Y6 V6 (280 hp) + 9-speed ZF (9HP); 8th digit
      uniform, real split is FWD vs i-VTM4 AWD. Notes it is mechanically a 2-row Pilot (shared 9HP -> test).
  (3) toyota-rav4-2019 (XA50) -- here the 8th digit DOES split gas A25A-FKS (203 hp, 8AT) vs hybrid
      A25A-FXS (219 hp comb., eCVT), both verified; vinNote stresses gas-vs-hybrid decode and flags that
      "CVT" on a gas RAV4 = wrong listing (gas car is a conventional 8AT).
  Anti-fabrication: for the two single-engine models (RDX, Passport) did NOT assert a specific 8th-digit
  character -- could not confirm the exact letter from an authoritative source this run (decoder pages
  JS-rendered/empty; NHTSA vPIC provenance-blocked for web_fetch). vinNotes anchored on verified engine
  codes + drivetrain distinction instead, per project no-fabrication discipline.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Mazda next), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html but DISJOINT slugs
  (Sonata/Venue/CT5 07-03, CX-30/Palisade/Corsair 07-02, etc.) -- additive JS data, different keys, no
  shared-slug conflict; every recent inspect/index.html Done sibling carries a - Started: date. No Re-sync.
  Syntax-check: PASS. Dead-links: verified (only new href is /inspect/, exists). Scanner: PASS. Commit: 986f263.


#### autovetting-vinnote-batch-2026-07-03 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-03 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-03.md (gitignored), TASKS.md
- Commit: a3db7c2 (content); this docs(tasks) record follows in a same-cadence follow-on push.
- Notes:
  2026-07-03 02:00: Drained vinnote-queue priorities 41/42/43 (queue top 41 -> 44 = toyota-highlander-2020).
  Added vinNote to three checklists in inspect/index.html (count 68 -> 71); all 8th-digit encodings + model-year
  facts WebSearch-verified 2026-07-03:
  (1) hyundai-sonata-2020 (DN8) -- 8th digit 'A' = 2.5L Smartstream MPI (191 hp); '2' = 1.6T GDI (180 hp);
      'J' = 2.0L GDI Hybrid. LOOK-AHEAD FIX: the "2.5T (290 hp) N Line" + "wet DCT" content is MY2021, not 2020
      (N Line announced Nov 2020, on sale Dec 2020 as a 2021). The 2020 1.6T uses an 8-speed torque-converter
      auto, NOT a DCT. Corrected trim, engine, summary, powertrain item, and VEHICLE_MENU trim (x4).
  (2) hyundai-venue-2020 (QX) -- 8th digit '3' = 1.6L Smartstream Gamma MPI (121 hp), only engine, FWD-only, IVT.
      No look-ahead errors; vinNote added cleanly.
  (3) cadillac-ct5-2020 -- 8th digit 'K' = 2.0T LSY (237 hp); 'W' = 3.0TT LGY V6 (335 hp / 360 hp CT5-V).
      LOOK-AHEAD FIX: the "CT5-V Blackwing 6.2L supercharged (668 hp)" engine + "Blackwing" trim + Blackwing
      belt item are MY2022+, not 2020 (2020 CT5-V = 3.0TT 360 hp). Also base four is LSY, not the Blazer's LTG.
      Corrected trim, engine, summary, 2.0T item (LTG->LSY, dropped wrong Blazer oil-consumption assertion),
      removed the inapplicable Blackwing belt item (itemsToCheck 10->9), fixed VEHICLE_MENU trim (x3).
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Mazda next), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html but DISJOINT slugs
  (CX-30/Palisade/Corsair 07-02, GV80/Sorento/Telluride 07-01, etc.) -- additive JS data, different keys,
  no shared-slug conflict; every recent inspect/index.html Done sibling carries a - Started: date. No Re-sync.
  Syntax-check: PASS. Dead-links: verified (no new href). Scanner: PASS. Commit: a3db7c2.


#### autovetting-vinnote-batch-2026-07-02 — ready (pushed directly)

- Status: ready to deploy (committed + pushed directly by overnight builder via HTTPS PAT)
- Started: 2026-07-02 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-07-02.md (gitignored), TASKS.md
- Commit: ba26757 (content); this docs(tasks) record follows in a same-cadence follow-on push.
- Notes:
  2026-07-02 02:00: Drained vinnote-queue priorities 38/39/40 (queue top 38 -> 41 = hyundai-sonata-2020).
  Added vinNote to three checklists in inspect/index.html (count 65 -> 68); all 8th-digit encodings
  WebSearch-verified 2026-07-02:
  (1) mazda-cx30-2020 -- 8th digit 'L' = 2.5L SkyActiv-G NA (186 hp); 'M' = later cyl-deactivation build.
      LOOK-AHEAD FIX: the 2.5 Turbo (227 hp) is a 2021+ addition, not 2020 -- corrected engine field,
      summary, trim label (x6 incl VEHICLE_MENU), and the "2.5T Turbo oil maintenance" item.
  (2) hyundai-palisade-2020 -- 8th digit 'E' = 3.8L Lambda II GDI V6 (291 hp); single engine, no Theta II
      (exempt from Theta II fire recalls). Calligraphy trim is 2021+. GOTCHA: this entry's engine line has a
      non-breaking space in "291 hp" that looks byte-identical to kia-telluride-2023 (shared 3.8L Lambda II);
      first replacement pass mis-targeted the Telluride, caught in verification + re-targeted to the NBSP line.
  (3) lincoln-corsair-2020 -- 8th digit '9' = 2.0T EcoBoost (250 hp); 'H' = 2.3T EcoBoost (295 hp).
      LOOK-AHEAD FIX: the 2.5L Grand Touring PHEV is a 2021 MY vehicle, not 2020 -- corrected engine field,
      summary, and the PHEV battery item ("2021+ Grand Touring only"). A genuine 2020 Corsair is gas-only.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Mazda next), autovet-seo-content (Content/blog/)
  all orthogonal; Ready empty; Done(last 10) = prior vinnote-batches on inspect/index.html but DISJOINT slugs
  (GV80/Sorento/Telluride 07-01, Trailblazer/Seltos/Sienna 06-30, etc.) -- additive JS data, different keys,
  no shared-slug conflict; every recent inspect/index.html Done sibling carries a - Started: date. No Re-sync.
  Syntax-check: PASS (twice). Dead-links: verified (no new href). Scanner: PASS. Commit: ba26757.
