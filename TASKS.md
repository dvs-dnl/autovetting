# AutoVetting — Task Queue

**Living lifecycle tracker** for in-flight and ready-to-deploy work on autovetting.com.
Deploy gate: the hourly orchestrator pushes what's in **Ready to deploy / publish** — nothing else.

## In flight

### autovet-competitor-monitor

- Status: in flight
- Started: 2026-06-11 (weekly rotation; date sourced from this block's own first Notes entry — added 2026-09-16 by the overnight builder so a future Done promotion does not gate-block every task sharing pinpoint/index.html)
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

  2026-08-13 02:00: profiled Lemon Squad (#1) — **CYCLE 2 OPENS** (cycle 1 closed 08-06 w/ #13 + Q3 quarterly). Severity **🔴 STRATEGIC THREAT**, scoped to the CHANNEL finding.
    Output: Competitors/_Monitor/2026-08-13-lemon-squad.md; **appended to Awaiting-Daniel.md** (🔴 escalation, dated 2026-08-13 block — required before Done at this severity).
    Sibling check: no overlaps. Ready = autovetting-recall-audit-wave23-2026-08-12 (inspect/index.html + scripts/recall-ledger.json + gitignored _hub Build-Log) — orthogonal; this run wrote only Competitors/_Monitor/ + _hub/Awaiting-Daniel.md (gitignored) + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10) = recall-audit waves 15+ / vinnote / decision-execution — none touch Competitors/ and none position an AutoVet feature against Lemon Squad. No Re-sync needed.
    Key delta: first review in 12 weeks, and the FIRST TIME IN THE ENTIRE 13-SLOT ROTATION that a competitor on OUR SIDE OF THE TRANSACTION (buyer-paid) has moved. They moved on all three AutoVet wedges in one quarter. (1) 🔴 **AI-AGENT ORDERING PUBLISHED** — FAQ now answers "Can I use an AI assistant to help place an order?" with "Yes", a parameterized order URL, a worked example, AND an inline schema.org JSON-LD `Service` w/ `potentialAction`:`AddAction` + `urlTemplate` + 9 typed `PropertyValueSpecification` instruments = machine-readable booking infra so assistants can construct orders. The May profile called their AI link "a form-prefilling helper, not an intelligence layer" — right about the intelligence, WRONG ABOUT THE INTENT: the AI is in DISTRIBUTION, not the product. (2) 🟡 NEW **EV Inspection tier $249** — but "battery health" is defined as "current charge level and estimated range" (= reading the dash), no SOH/degradation/module-balance; page's own module says "No reviews available". (3) 🟡 **Marketplace API** productized — "easy to integrate API available", 3,000+ techs (up from ~2,800 in 2020), live video/voice w/ tech, white-label reports; Cars & Bids partnership still current, PrivateAuto [unverified]. (4) 🟡 **BBB STORY INVERTED**: 59 complaints/3yr, 26 closed/12mo, breakdown = Answered 38 / Resolved 17 / **Unanswered 3** / Unresolved 1, w/ detailed same-week corporate responses Feb–Jun 2026. Still D+ / unaccredited (lagging grade) but "fails to respond to complaints" is NOW FALSE and falsifiable — STRIKE from all copy. (5) 🟡 AI SUPPORT LAYER IS BACKFIRING — 4 complaints (06-10/04-23/03-12/02-10) about being trapped in automated/AI phone support; one is ENTIRELY about it. Full picture: AI on the intake edge + AI on the support edge + ZERO AI in the product. (6) Pricing: Standard/Exotic/Classic/Motorcycle/RV UNCHANGED; EV $249 NEW; Commercial $365 now listed; Verbal Vehicle Assessment $49.99 NEW; **fraud-detection $40 add-on REMOVED**; Live never went to its $69 regular price — 9 months at "intro" $59.99 + new "only pay when the session happens" framing = a tier that isn't converting. ⚠️ **List price hides a mileage surcharge** (BBB invoices: $219.99 + $27.50/41mi; totals $297.48 and $487.49) while the homepage badge still says "No hidden fees" — compare against DELIVERED totals, never $220.
    **THE COUNTER-POSITIONING ASSET IS FINALLY WRITABLE (flagged unwritten 5 runs straight: 07-29/07-30/08-03/08-06/today).** Their formalized refund-denial script, in their own words: "visual, non-invasive assessments performed at a single point in time... without disassembly, removal of parts, or internal mechanical testing... not a guarantee of future performance." The DIRECT competitor has put in writing that it disclaims exactly the forward-looking, vehicle-specific layer AutoVet's whole product is. This is SHARPER than the planned version ("seller-provided report ≠ independent inspection") because it aims at the direct competitor rather than the seller-side players. Also on record from a 2026-02 complaint: an inspector "admitted that he was not a mechanic and only planned to walk around the car to take pictures."
    Implication: escalated because the asymmetry is the point — for them this was a FAQ entry + a JSON-LD block (days, not a launch), and THE SAME IS TRUE FOR US. Decision put to Daniel as (a) publish an AI-orderable intake path + `potentialAction` markup out-of-band ahead of full booking infra, or (b) explicitly defer and accept default-setting risk — booking infra is priority 3 under the freeze and I did NOT propose re-ranking the whole order. Their EV tier is a gift not a threat (validates vehicle-specific inspection, fails to deliver it → our 245-slug library is MORE differentiated). Marketplace API means the embed race is two-sided: they have fulfillment scale we don't, our counter is the intelligence layer (recalls/generation-specific failure patterns/checklists) their API pitch conspicuously lacks.
    ⚠️ DATA-QUALITY FLAG LEFT OPEN: TrustPilot is client-rendered, returned an empty body to web_fetch; SERP metadata says "Average 3.4/5" (~2,362 reviews) but the May profile asserted TrustPilot sat in the 1.8–2.4 band. Both cannot be right; neither verified first-hand. Left explicitly [unverified] rather than picked — same failure mode as the 08-03 Competitor_Analysis.md §4 finding (an inferred figure hardening into a confident assertion). DO NOT build messaging on either number until confirmed on-page.
    Carry-forward: Wrench consolidation = NO brand merge (own name/©2026/own recruiting; only visible tie is the wrenchtotalcare.com cross-sell in Corporate nav; "Wrench Inspection Company, LLC" trademark entity exists → inspection arm likely a distinct legal entity); PrivateAuto partnership [unverified]; AutoCheck logo on /live while every other page shows CARFAX (unexplained).
    🔴 tripwires for cycle 3: actual AI IN the inspection product; a recall/TSB/reliability layer added to their report; a named marketplace integration beyond Cars & Bids; evidence the AI-order path converts OR is copied by CARCHEX/iNeedaPPi; BBB grade moving off D+.
    Weekly milestone: DONE — intel ready for Daniel's review; 🔴 Awaiting-Daniel append complete. Next in rotation: CARCHEX (#2) — **carry a specific question in: has CARCHEX also published AI-agent ordering markup? If 2 of 3 PPI incumbents have, this stops being a Lemon Squad story and becomes a CATEGORY SHIFT and the 🔴 hardens.** Standing recommendation (open since 08-03): retire slot #12 (VINsight, not a competitor) → standing buyer-side-encroachment sweep.

  2026-08-20 01:11: profiled CARCHEX (#2, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-08-20-carchex.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. Ready = autovetting-phase-copy-and-template-fix-2026-08-14 (scripts/render-blog.py + inspect/index.html + blog/*) — orthogonal; this run wrote only Competitors/_Monitor/ + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal; Done(last 10) = recall-audit waves + vinnote batches, none touch Competitors/ or position AutoVet against CARCHEX. No Re-sync needed.
    Key delta: CARRY-IN QUESTION FROM 08-13 🔴 ANSWERED: NO — CARCHEX has NOT published AI-agent ordering (no assistant FAQ, no parameterized order URL, no announcements; inspection pages untouched since 2022-02/2023-04 stamps; caveat: web_fetch strips scripts so JSON-LD absence not airtight, confidence high). 1 of 3 PPI incumbents — NOT yet a category shift; decisive data point = iNeedaPPi next week. Also: (a) inspection retreat now structural — ALL inspection links removed from header+footer nav, /vehicle-inspections/ tree orphaned and openly Lemon Squad-branded end-to-end (own order line 888-231-7965), Silver/Gold $129.95/$139.95 tiers no longer displayed anywhere = pricing stale/[unverified]; (b) BBB verified FIRST-HAND: "NOT a BBB Accredited Business", 92 complaints/3yr, 21 closed/12mo — contradicts May record "A+ accreditation maintained" (affiliate-inherited figure hardened into our record; third instance of the failure mode after 08-03 §4 and 08-13 TrustPilot); carchex.com still hosts an "A+ BBB Rating" page = falsifiable trust claim on THEIR side, do not use in copy until BBB main profile grade verified; (c) harvest mode unchanged — no press since Oct 2022 PE acquisition, ~84 employees flat, no AI/tech hiring.
    Implication: Lemon Squad's AI-order move looks like a Lemon Squad growth experiment, NOT a Wrench-platform rollout (their biggest white-label customer didn't get it) — softens the 08-13 category-shift worry pending iNeedaPPi. Warranty-broker distribution slot = starved Lemon Squad reseller page, "win that slot" thesis stronger.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: iNeedaPPi (#3) — CARRY IN: has iNeedaPPi published AI-agent ordering? (2-of-3 incumbents = category shift → 🔴 hardens.)

  2026-09-03 [scheduled task]: profiled iNeedaPPi (#3, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-09-03-ineedappi.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. Ready = autovetting-pinpoint-fueltype-schema-fix-2026-08-21 (pinpoint/index.html) + autovetting-phase-copy-and-template-fix-2026-08-14 (scripts/render-blog.py, inspect/index.html, blog/*) — both orthogonal, this run wrote only Competitors/_Monitor/ + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10, per file order) = recall-audit/vinnote/overnight-builder entries, none touch Competitors/ and none position an AutoVet feature against iNeedaPPi. No Re-sync needed.
    Key delta: CARRY-IN QUESTION FROM 08-13/08-20 ANSWERED: NO — iNeedaPPi has NOT published AI-agent ordering markup (no assistant FAQ, no parameterized order URL; caveat: fetch tooling strips <script> tags so a JSON-LD block can't be ruled out with certainty, same caveat as 08-20 CARCHEX, confidence high). Still 1 of 3 PPI incumbents — the Lemon Squad 08-13 move reads as Lemon Squad-specific, not a category shift; that 🔴 tripwire does not harden. Also: (a) price rose $169.99 → $189.99 (+11.8%), narrowing the price-leader gap vs Lemon Squad ($199–249) — undercuts baseline's "race to the floor" framing, they raised price while still expanding; (b) geographic densification — added Louisiana (Shreveport, Waskom, 6th state) plus roughly doubled named-suburb coverage within existing FL/TX/AZ/OR metros (real inspector-network scale-up, not just a press release); (c) reputation split by channel — company-cited Google/Trustindex still strong (500+/4.8★, up from 400+/4.9★ baseline) but the independent Trustpilot profile (ineedappi.ca) is thin (6 reviews) and weak (3.2/5, 66% 1-star, "hasn't replied to negative reviews"), and a Jan-2026 1-star review is near-verbatim identical to a Sept-2024 one — both allege a missed major defect that let an "not roadworthy" car pass. Recurring, specific quality-failure language, not generic venting. (d) No change: AI Triple-Check messaging, $20 Market Price Appraisal, dealer/B2B lead-gen page (untouched since 2024-07-09, no named partners), no funding event found in a fresh 2026 scan.
    Implication: no baseline escalation trigger tripped (no buyer-facing research tool, no funding, no marketplace deal, no AI-ordering). The Trustpilot pattern (near-identical missed-defect complaints 15 months apart) is a second concrete data point — after Lemon Squad's 08-13 refund-denial disclaimer language — for the still-unwritten counter-positioning asset on single-visit field-inspection blind spots (use the pattern, not the competitor's name). Acqui-hire thesis reinforced (6th state + real densification = repeatable network build-out) though the price increase implies a higher multiple than baseline assumed.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: YourMechanic / Wrench (#4, cycle 2) — carry-in: re-verify "~3 employees, consumer PPI frozen" from 06-11 baseline and the Lemon Squad/Wrench Inspection Company LLC ownership question flagged 08-13.

  2026-09-10 [scheduled task]: profiled YourMechanic / Wrench (#4, cycle 2) (🟢).
    Output: Competitors/_Monitor/2026-09-10-yourmechanic-wrench.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. Ready = autovetting-vinnote-batch-2026-09-09 (inspect/index.html, committed locally, push-blocked by the PAT issue) — orthogonal, this run wrote only Competitors/_Monitor/ + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Volvo done 09-06, next=Lincoln) + autovet-seo-content (Content/blog/, Subaru Outback done 09-09) orthogonal. Done(last 10) = recall-audit/vinnote/overnight-builder entries, none touch Competitors/ and none position an AutoVet feature against YourMechanic/Wrench. No Re-sync needed.
    Key delta: CONFIRMING re-review, no material change since 06-11 baseline. Both carry-in questions answered: (1) "~3 employees" cross-checked against a second source this run (Wrench Inc. parent = 111 employees / LeadIQ "51-200" bucket, consistent) — still accurate, consumer PPI still a maintained shell. (2) Wrench Inspection Company LLC question RESOLVED via USPTO trademark record: that LLC is the confirmed legal owner of the Lemon Squad trademark for inspection services — the inspection line of business has its own legal wrapper under the Wrench Inc. parent, consistent with (not contradicting) the 08-13 "no brand merge" finding. PPI product itself unchanged (150-point visual, no lift, no compression test, quote-based pricing, same non-guarantee disclaimer language family as Lemon Squad's 08-13 quote — now 2-for-2 incumbents using this disclaimer, strengthening the counter-positioning asset's genericness). BBB B+ / 144 complaints / not accredited recorded as a first-time explicit data point (baseline had no letter grade). No funding, M&A, executive change, or layoff signal in a fresh scan; confirmed the "Wrench Group" HVAC company (Lace AI partnership, March 2026) is the unrelated company flagged in the 06-11 baseline, not this Wrench.
    Implication: thesis holds, unchanged in either direction — 12 weeks of zero consumer-PPI product investment is itself confirmation this brand isn't re-entering buyer-side competition. No new action; both open carry-in items can be closed in Competitor_Analysis.md at the next housekeeping pass.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Bumper (Instavin) (#5, cycle 2).

  2026-09-17 [scheduled task]: profiled Bumper (Instavin / VINDATA) (#5, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-09-17-bumper.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. Ready to deploy/publish = pinpoint-dead-route-repair (09-16), pinpoint-filter-cells-B1-B4 (09-15), vinnote batches 09-09/09-11/09-12/09-14, inspect-render-and-generation-fix (09-13), inspect-key-namespace-rename (09-03), pinpoint-fueltype-schema-fix (08-21), phase-copy-and-template-fix (08-14) — all inspect/index.html or pinpoint/index.html or scripts/, none touch Competitors/; this run wrote only Competitors/_Monitor/ + TASKS.md. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal — neither references Bumper, Instavin, VINDATA, or LTVCo. Done(last 10) = recall-audit waves + vinnote batches, none position an AutoVet feature against Bumper. No Re-sync needed.
    Key delta: (1) corporate parent identified — Bumper is an LTVCo (The Lifetime Value Co.) brand alongside BeenVerified/Ownerly/PeopleLooker, confirmed via BBB "Related Businesses" + Bumper's own Zendesk help-center running on a beenverified.zendesk.com backend; explicitly NOT the H.I.G./PeopleConnect family (TruthFinder/Intelius) — disambiguation guard for future runs. (2) Reputation figures firsthand-verified/corrected: baseline's "~169 Trustpilot reviews" was stale — actual is 865 total, 2.0/5 "Poor," 64% 1-star; BBB verified firsthand for the first time (B rating, NOT accredited, 215 complaints/3yr) — substance unchanged (still billing-driven complaints, fresh through Sept 2026), figures now citable. (3) Product scope expanded past report+API baseline: "digital dashboard for car ownership" bundling insurance (Jerry)/DMV (eTags)/junk-buyback (Peddle)/marketplace/Bumper Connect telematics (Smartcar API, no hardware) — still data/software-only, June's physical-inspection escalation trigger NOT tripped. (4) CROSS-COMPETITOR FINDING: Lemon Squad appears as a named partner brand on Bumper's About page partner-logo strip (alongside Openbay+/RepairPal/CarShield/RunBuggy/Ownerly); Bumper claims 1M+ monthly visitors — a high-traffic data-report site already sends PPI-intent traffic to Lemon Squad (our #1 rotation slot, under 🔴 strategic-threat watch since 08-13). Not previously captured in the Lemon Squad file's own partnership list — flagged as a carry-forward item for that file, not actioned here. (5) No funding/M&A/exec-change/layoff signal; confirmed a same-named UK repair-financing fintech ("Bumper," $110M raised, AutoBI/Cocoon Payments) is a distinct unrelated company — name-collision guard.
    Implication: pricing/trust contrast thesis (vs. Bumper's billing reputation) now better-sourced with firsthand BBB/Trustpilot figures. The Lemon Squad↔Bumper partnership reframes Bumper from "irrelevant adjacent player" to "a distribution channel already captured by our most-escalated direct competitor" — worth a note in the Lemon Squad file's carry-forward list next time that profile is touched; no product/pricing decision changes this week. AI-on-physical-condition differentiation remains uncontested (Bumper's AI stays report-layer). Housekeeping still open (repeat from 06-18): add Bumper to Competitor_Analysis.md Indirect Competitors with LTVCo context.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Carfax (S&P Global Mobility) (#6, cycle 2) [watch with extra care — competitor AND most-likely acquirer per business plan §9/§13].

  2026-09-24 [scheduled task]: profiled Carfax (Mobility Global) (#6, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-09-24-carfax.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no true conflict. Ready to deploy/publish (menu-reroute-and-orphan-repair 09-23, menu-phantom-year-rows 09-22, checklist-generation-spans 09-21, menu-generation-and-year-gap-fix 09-17, pinpoint-dead-route-repair 09-16, pinpoint-filter-cells-B1-B4 09-15, vinnote batches 09-09..09-14, inspect-render-and-generation-fix 09-13, inspect-key-namespace-rename 09-03, pinpoint-fueltype-schema-fix 08-21, phase-copy-and-template-fix 08-14) is entirely inspect/index.html, pinpoint/index.html, or scripts/ — none touch Competitors/ and none position an AutoVet feature against Carfax. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal — neither references Carfax. Done(last 10) = menu/inspect fixes, none touch Competitors/. Verified against: 2026-06-25-carfax.md (baseline for this cycle's delta). No Re-sync needed.
    Key delta: NOT an inspection-product announcement (baseline task rule: any inspection-related Carfax announcement is 🔴 — did not trigger). The two 06-25 escalations (Future Reliability; Carfax×UVeye B2B service-lane integration) are unchanged in scope, and 06-25's standing 🔴 tripwire (Carfax×UVeye condition data reaching a consumer surface) did NOT trip — no "Verified Condition" badge or consumer-facing surfacing found. Material delta this cycle is corporate: Carfax's parent completed its spinoff from S&P Global and began trading independently as Mobility Global Inc. (NYSE: MBGL) on 2026-07-01. First standalone-company earnings (Q2, reported ~08-07): revenue $468M (+7%), CARFAX segment $312M (+8%), but flagged results modestly below its own expectations (CARFAX go-to-market underperformance) and initiated a dividend ($0.06/share) rather than signaling an acquisition-heavy posture — though analyst commentary frames the standalone structure as giving dedicated M&A capacity for "consolidating fragmented dealer software vendors." Also noted (no action): BBB/Trustpilot reputation unchanged from baseline; lobbying-program termination (Sept 2026 LDA filing) is a cost story, not competitive; a "Carfax owner adds Carproof" hit in this cycle's search is a stale historical item (mid-2010s), explicitly flagged not to reintroduce as fresh.
    Implication: sharpens (doesn't resolve) the acquirer-thesis open item flagged 06-25 — Business Plan §9/§13 rewrite should name Mobility Global (MBGL) specifically, not S&P Global, and weigh the dedicated-M&A-capacity language against this quarter's dividend-over-M&A signal. No messaging/positioning change needed this week.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: CarGurus (#7, cycle 2) [AI search rollout / inspection or trust-layer launches].

  2026-10-01 [scheduled task]: profiled CarGurus (#7, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-10-01-cargurus.md (no Awaiting-Daniel append — not 🔴).
    Sibling check: no overlaps. Ready to deploy/publish is entirely inspect/index.html, pinpoint/index.html, or scripts/ — none touch Competitors/. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) orthogonal — neither references CarGurus. Done(last 10) = menu/inspect fixes, none touch Competitors/. Verified against: 2026-06-28-cargurus.md (baseline for this cycle's delta). No Re-sync needed.
    Key delta: new consumer AI assistant "Guru" launched (conversational, embedded on-site; US first, Canada 2026-07-28) — recommends vehicles from live inventory using CarGurus' own pricing signals (Instant Market Value, days-on-lot, Deal Ratings); no condition/recall/reliability data, no booking/transaction capability found in any source. Relationship to CarGurus Discover unconfirmed (looks like a rebrand/consolidation, not a new capability tier) — flagged as housekeeping, not urgent. Also announced at the 2026-01-22 20th-anniversary press release: PriceVantage (AI dealer pricing engine) and Dealer Data Insights (~20,000 dealers) — both dealer-side, not buyer-facing. Q2 2026: revenue $251.0M +13% YoY (vs Q1's +15%), beat guidance; adj. EBITDA $84.7M/34% margin (down ~199bps YoY); $29.2M buyback (>30% of shares retired since Dec 2022). FY26 guide held at 10–13% growth. No M&A, no partnership, no inspection-adjacent signal found in this window — 06-25 Carfax-style tripwire (native per-VIN condition/reliability/recall data surfacing in Discover/Dealership Mode/Guru) did NOT trip.
    Implication: embedding thesis reinforced again (third consecutive CarGurus-family finding) — CarGurus keeps building the discovery front end (now a named conversational brand), never the condition/trust back end; a Guru result ending in "book an independent inspection" is a more natural CTA now that it's conversational. No severity or action change from 06-28 baseline.
    Weekly milestone: DONE — intel ready for Daniel's review. Next in rotation: Cars.com (#8, cycle 2) [AI search rollout / inspection or trust-layer launches].

  2026-10-08 08:13 [scheduled task]: profiled Cars.com (Cars Commerce, #8, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-10-08-cars-com.md (no Awaiting-Daniel append -- not 🔴).
    Sibling check: no overlaps. Ready to deploy/publish (recall-audit waves 24-25, vinnote batches 09-09..10-01, menu/pinpoint fixes back through 08-14) is entirely inspect/index.html, pinpoint/index.html, or scripts/recall-ledger.json -- none touch Competitors/. In-flight autovet-recall-study-under-15k (_hub/Content/_seo-research + inspect/index.html + scripts/recall-ledger.json), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) and autovet-seo-content (Content/blog/) all orthogonal -- none reference Cars.com, Cars Commerce, or AccuTrade. Done (last 10) = recall-audit/vinnote/menu fixes, none touch Competitors/. Verified against: 2026-07-02-cars-com.md (baseline for this cycle's delta). No Re-sync needed.
    Key delta: "Dealer Verified Listings" launched on the Marketplace (flagged in Q2 2026 results 08-06, rollout called central to subscription growth on the 08-07 earnings call) -- a consumer-visible "Dealer Verified Condition" badge on SRP/VDP. Confirmed via Cars Commerce's own dealer help docs: the dealer's own staff verify condition inside AccuTrade, a dealer manager role signs off, no third party or independent inspector anywhere in the workflow; bundled into the Premium Plus package as a revenue lever (15% penetration target). Same dealer-self-certified pattern as Carfax's Homegrown badge (06-25, 🟢) and CarGurus' "unbiased recommendation" (06-28) -- now a 3-for-3 marketplace pattern, sharpening the still-unwritten independence counter-positioning asset with a concrete, citable example (dealer verifies + dealer manager approves). Carson AI now ~20% of searches (scaled, not new in kind). Two leadership changes (CFO transition announced 09-30, effective 11-06; CEO already changed at baseline) -- noted, not product-relevant. Financials steady: Q2 revenue $179.9M +1% YoY, net income $14.3M +103%, adj. EBITDA 29.4% margin, FY26 guide reaffirmed -- same trajectory as 07-02 baseline.
    Implication: embedding thesis reinforced a fourth consecutive marketplace-side cycle (06-25 Carfax, 06-28 & 10-01 CarGurus, now Cars.com) -- no marketplace has shipped an independent/buyer-ordered condition layer, only seller-sourced trust badges. Escalation trigger to 🔴 (not tripped): a third-party or AI-computer-vision inspection step added to Dealer Verified Listings, or AccuTrade condition data exposed as independently-sourced rather than dealer self-report. Housekeeping (repeat, open since 06-18): Competitor_Analysis.md's pending "Marketplace/channel" archetype block should now contrast each marketplace's trust-badge source (Carfax=Carfax-sourced, CarGurus=platform-recommendation, Cars.com=dealer-sourced) against AutoVet's buyer-ordered independent model.
    Weekly milestone: DONE -- intel ready for Daniel's review (not 🔴, no Awaiting-Daniel append required). Next in rotation: AutoTrader (Cox Automotive) (#9, cycle 2) [Cox-wide acquisitions, any inspection-layer signals].


  2026-10-15 [scheduled task]: profiled AutoTrader (Cox Automotive, #9, cycle 2) (🟡).
    Output: Competitors/_Monitor/2026-10-15-autotrader-cox.md (no Awaiting-Daniel append -- not 🔴).
    Sibling check: no overlaps. In-flight autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/), and autovet-recall-study-under-15k (inspect/index.html + scripts/recall-ledger.json) all orthogonal -- grep of TASKS.md for autotrader/cox/kbb/manheim/vauto found no hits in any of those three blocks' In-flight notes. Ready to deploy/publish is entirely inspect/index.html, pinpoint/index.html, or scripts/recall-ledger.json -- none touch Competitors/. Done (last 10) = recall-audit/vinnote/menu fixes, none touch Competitors/. Verified against: 2026-07-09-autotrader-cox.md (baseline for this cycle's delta). No Re-sync needed.
    Key delta: KBB ICO's AI Remote Damage Assessment + Dynamic Condition Quiz are still NOT GA three months after the baseline ("upcoming capability" language unchanged on the same source page) -- the single biggest acquirer-tier condition-AI building block has not moved. New data point: vAuto "Test Drive" (launched 2026-08-28) previews two condition-adjacent dealer-side features -- "Common Problems" (AI-mined owner-forum issue data per make/model) and "Vehicle Journey" (service/ownership history feeding appraisal condition assessment) -- both appraisal/reconditioning tooling, not buyer-facing. No Cox-wide acquisitions found in the window (checked full PR Newswire feed Jul-Oct 2026 plus targeted M&A search); the only acquisition-shaped hits (BSC America auctions, Corcoran's Mobile Services, F&I Express) are stale (2025-07/2023-08/2018-10) and non-inspection. Other Aug-Oct releases (Secure Vehicle Transfer, Central Dispatch AI pricing, AI-shopper-gap tracker, Manheim Value Index) are wholesale/logistics/market-data, orthogonal. Confirmed an AutoTrader ChatGPT-integration story is Canadian TRADER.ca, not US AutoTrader -- same disambiguation trap as baseline, logged not actioned.
    Implication: both standing theses (embedding reinforced, acquirer thesis at baseline's "modestly weakened, watch closely" level) hold unchanged. No escalation trigger tripped. No messaging change.
    Weekly milestone: DONE -- intel ready for Daniel's review (not 🔴, no Awaiting-Daniel append required). Next in rotation: UVeye (#10, cycle 2) [funding, new partnerships, any consumer-facing moves].

### autovet-cpo-protocol-ingestion

- Status: in flight
- Started: 2026-06-14 (weekly rotation; date sourced from this block's own first Notes entry — added 2026-09-16 by the overnight builder, same reason)
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

  2026-08-16 09:20: ingested BMW CPO protocol (no fixed published inspection-point count — "360° vehicle inspection"; second OEM in the rotation after Volkswagen with no OEM-stated number).
    Output: Product/CPO-Protocols/bmw-certified.md, Product/CPO-Protocols/_runs/2026-08-16-bmw.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. In-flight autovet-competitor-monitor (Competitors/, mid-cycle-2 on Lemon Squad → CARCHEX) + autovet-seo-content (Content/blog/) orthogonal. Verified against: autovetting-recall-audit-wave18-2026-08-05 (rebuilt bmw-3series-2018's complete recall set in inspect/index.html, including 18V-465 gas + 21V-586/21V-907 diesel-scoped EGR/fuel-pump campaigns) — this protocol file independently cites and agrees with the same 21V586000/21V907000 diesel campaign pair for the 3 Series/X3/X5 diesel variants; complementary, not conflicting. No BMW slug elsewhere in In-flight/Ready/Done(last 10). No overnight-builder/vinnote/content-checklist task launching a BMW vehicle page. No Re-sync needed.
    Located and fetched the actual official BMW checklist PDF (bmwusa.com, form 23CPOCKLST 5-23, 8 sections / ~200+ check lines, no stated total) rather than relying on a dealer-page summary — same evidentiary bar as the INFINITI/Hyundai runs. Deliberately did NOT adopt the "360-point" figure that circulates on dealer marketing pages, since it does not appear in any BMW of North America corporate material — same missing-number pattern as Volkswagen (2026-08-09), now the second OEM in the rotation with this gap.
    Campaign IDs all WebSearch-verified 2026-08-16 via cars.com's NHTSA feed, each scoped to exact model/trim/build-date in an anti-fabrication guard table: 24V288000 (head/side-curtain airbag weld, 2014-15 3-Series/2-Series/4-Series), 24V527000 (driver frontal airbag inflator explosion risk, 2014-15 3-Series + wide cross-model list), 15V520000 (side-marker lighting software, 2012-15 320i/328i/335i + 328d), 24V608000 (water pump connector fire risk, cross-model incl. 328i/328xi + X3 sDrive28i/xDrive28i 2012-17), 21V907000 supersedes 18V755000 (diesel EGR cooler fire risk, 328d/X3 xDrive28d/X5 xDrive35d), 21V586000 (diesel HP fuel pump), 20V185000 (328d xDrive CV joint / rollaway risk), 25V636000 (starter relay corrosion fire risk, 2020-22 X3/X4 + cross-model), 24V764000 supersedes 24V534000 (X3 cargo rail attachment bolts, crash safety), 23V211000 (X3 seat frame weld), 21V598000 (X3 M40i brake-assist-loss software), 21V096000/20V598000/20V443000 (three distinct X3 rearview-camera FMVSS 111 campaigns, not duplicates), 20V601000 + 20V490000 (X3 xDrive30e PHEV battery fire risk, two separate campaigns), 16V683000 (driver airbag weld, X3/X4/X5 2014-15), 15V147000 (X5 HPS airbag connection, 2014-15), 14V650000 (X5 rear seat belt weld, tight 9-day build-date window 2014-09-12 to 2014-09-21 — VIN-check mandatory, not model-year assumption).
    NOT-a-recall flags written into the file with anti-fabrication guard language: N20 2.0L turbo-four timing-chain-guide degradation (3-Series/X3-era engines) — addressed via SIB 11 03 13 Customer Care Package (7yr/70k extended warranty) and the *Gelis v. BMW* class-action settlement (effective 2021-06-30), never an NHTSA safety recall, invisible to any VIN recall lookup. N63 twin-turbo V8 oil-consumption pattern (X5/5-Series/7-Series-era) — addressed via the "N63 Customer Care Package" (bulletin B001314) and the *Bang v. BMW NA* class-action settlement (2018, ~$900 reimbursement), also never a safety recall. Both flagged as the file's highest-value content angle: concrete brand-specific proof that a VIN-recall-only check misses real, documented failure patterns — direct ammunition for the independence/physical-inspection counter-positioning piece the competitor-monitor workstream has flagged unwritten across multiple runs (most recently Lemon Squad, 2026-08-13).
    Two superseded-campaign traps found in this single brand (X3 cargo rail 24V534000→24V764000; diesel EGR cooler 18V755000→21V907000) reinforce the standing "superseded by later campaign" schema-field recommendation open since the VW run (2026-08-09).
    Key buyer insight for downstream content: BMW's public checklist form defers repeatedly to a "CPO BMW Vehicle Program Center Operations Manual" for full inspection guidelines — that manual is dealer-internal and was not located publicly; the ingested file is BMW's own public summary/sign-off sheet, the most granular document available, but explicitly not the complete guideline text. Flagged for Daniel if a fuller dealer-sourced document surfaces later.
    Weekly milestone: DONE — bmw-certified.md saved + INDEX.md updated (P2 now BMW ✅; next = Mercedes-Benz). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Mercedes-Benz (second P2).

  2026-08-23 02:35: ingested Mercedes-Benz CPO protocol (165+ inspection points published, ICE only — EV count unpublished; legacy public ICR PDF on mbusa.com enumerates 164 line items, Rev 01/12 — third straight OEM where marketing count and public line-item list don't reconcile).
    Output: Product/CPO-Protocols/mercedes-benz-certified.md, Product/CPO-Protocols/_runs/2026-08-23-mercedes-benz.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. Ready = autovetting-pinpoint-fueltype-schema-fix-2026-08-21 (pinpoint/index.html) + autovetting-phase-copy-and-template-fix-2026-08-14 (scripts/render-blog.py + inspect/index.html + blog/*) — this run wrote to NEITHER task's files; no Mercedes content in either. In-flight autovet-competitor-monitor (Competitors/, next=iNeedaPPi) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10) = recall-audit waves + vinnote batches — grep of TASKS.md for mercedes/benz/glc/gle/c300/c-class found zero Mercedes task rows. Cross-referenced to: 6 existing Mercedes slugs in inspect/index.html (mercedes-c300-2018, c300-2022, gla-2020, glc-2018, gle-2020, gls-2020) — complementary, this file is their upstream protocol source. No Re-sync needed.
    Verification discipline: only 20V-626 (illuminated-star ground, 12,799 units, 2020 GLE350/450/580+GLS450/580) and 20V-430 (1-vehicle seat-bolt — scope lesson, never generalize) verified against primary Part 573 PDFs. C300 eCall x2, GLC seat-belt-latch/eCall, GLE 48V-ground/AC-drains/dashboard all quarantined [unverified] (MBUSA internal numbers only; api.nhtsa.gov unreachable this run) — recall-audit workstream must verify before any number reaches inspect/index.html.
    Content asset: M274 camshaft-adjuster/timing-chain pattern (no recall, no dedicated TSB) = second consecutive German-brand non-recall pattern failure after BMW N20/N63 (08-16) — feeds the counter-positioning piece competitor-monitor has flagged since 07-29. Also citable strict benchmarks: 5/32" tread min, 6-yr tire age replacement, 50% pad min, >60k compression test, 10%-of-value body-repair disclosure.
    Weekly milestone: DONE — mercedes-benz-certified.md saved + INDEX.md updated (P2 now BMW ✅ Mercedes-Benz ✅; next = Audi). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Audi (third P2).

  2026-08-30 02:40: ingested Audi CPO protocol (125+ inspection points — US marketing claim with NO public US line-item list; Canadian "Certified :plus" dealer guide is the only public enumeration, ~336 structural checkpoints under "300+" branding — fourth straight OEM where marketing count and public line-item list don't reconcile).
    Output: Product/CPO-Protocols/audi-certified.md, Product/CPO-Protocols/_runs/2026-08-30-audi.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. Ready = autovetting-pinpoint-fueltype-schema-fix-2026-08-21 (pinpoint/index.html — its e-tron card fuelType→"Electric" fix is CONSISTENT with this file's e-tron notes, different file tree) + autovetting-phase-copy-and-template-fix-2026-08-14 (render-blog.py/inspect/blog) — orthogonal; this run wrote to neither. In-flight autovet-competitor-monitor (Competitors/, next=iNeedaPPi) + autovet-seo-content (Content/blog/) orthogonal. Done(last 10) = recall-audit waves + vinnote batches; only Audi touch anywhere in TASKS.md is the audi-q3-2019 US-spec fix (228hp/45 TFSI) in a prior overnight-builder batch — complementary; this protocol makes no Q3 claims. Verified against: autovetting-pinpoint-fueltype-schema-fix-2026-08-21; cross-referenced to: audi-q3-2019 spec-fix note, recall-ledger 19V434 (only ledgered Audi ID). No Re-sync needed.
    Campaign IDs all verified first-hand 2026-08-30 via cars.com NHTSA feed, complete MY2018 sets with exact scopes in an anti-fabrication guard table: Q5 (6): 21V947000 (gateway module liquid ingress, 90S9), 19V737000 + 19V416000 (TWO distinct wheel-arch campaigns, 66K8/66K6 — one closed ≠ both closed), 19V277000 (brake master cylinder casting, inspect-vs-replace, 47O9), 18V369000 (caliper piston coating, 47N8/9/6), 16V955000 (2018 Q5 = pretensioner portion ONLY; airbag portion is MY2017 — guard). A4 (4): 21V874000 (74E3, PODS/passenger-airbag disable) SUPERSEDES 19V547000 (74D9) — cars repaired under 74D9 must RETURN, certified cars can carry a silently reopened recall (Audi twin of the Acura 19V-378/19V-502 trap); 18V836000 (69Y4, A4 ALLROAD only, NOT sedan — guard); 17V675000 (70G6, speaker trim). Q7 (3): 20V658000 (C-pillar padding, 70H8), 20V149000 (steering shaft bolt, 2017-2019 + 2019 Q8, inspect-vs-replace, 36A1), 19V035000 (fuel rails, 24DP). Guard also re-pins 19V434 (e-tron ONLY) and blocks reintroduction of deleted fabrication 20V-092 (Bentley).
    Key buyer insights for downstream content: (1) WEAKEST LUXURY CPO WARRANTY in the library — 1yr/20k, named-exclusions not bumper-to-bumper, NON-TRANSFERABLE since 2023-08-01, e-tron HV battery + module EXCLUDED; ConsumerAffairs quotes an Audi dealer rep: "more like a 'Silver' plan than a 'Platinum' plan". Paired with number-but-no-list transparency = strongest single-brand case yet for the independence counter-positioning asset (flagged 6 runs straight in competitor-monitor). (2) e-tron DOUBLE GAP — most expensive component neither quantitatively measured (no SOH threshold in any public checklist) nor warranty-covered. (3) Recall closure is a snapshot — the 21V874 expansion trap means "no open recalls at certification" can reopen. (4) DATA-QUALITY CATCH: $85 CPO deductible in aggregator articles contradicted by the booklet's "free of charge" (REV. 7/23) — [unverified], do NOT publish; same aggregator-hardening failure mode as 08-03/08-13/08-20.
    Open flags: audiusa.com CPO page client-rendered (empty fetch) — US "125+" corroborated via booklet + ConsumerAffairs, not the page itself; DL382 service interval + EA888 Gen-3 cooling-plastic part revisions need Mitchell1/ALLDATA before publishing numbers; 13 verified IDs NOT yet ledgered (ledger holds only 19V434) — ledger with guard-table scopes verbatim on first downstream use; Canada/US program divergence (8MY/140k km vs 5MY/60k mi, ":plus" branding) — never mix in US copy.
    Weekly milestone: DONE — audi-certified.md saved + INDEX.md updated (P2 now BMW ✅ → Mercedes-Benz ✅ → Audi ✅). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Volvo (fourth P2).

  2026-09-06 (this run): ingested Volvo CPO protocol (170+ inspection points, single tier; no published PHEV/BEV variant checklist).
    Output: Product/CPO-Protocols/volvo-certified.md, Product/CPO-Protocols/_runs/2026-09-06-volvo.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. In-flight autovet-competitor-monitor (Competitors/, currently profiling #11 Self Inspection) orthogonal. Ready = autovetting-inspect-key-namespace-rename-2026-09-03 (inspect/index.html) + autovetting-pinpoint-fueltype-schema-fix-2026-08-21 (pinpoint/index.html) + autovetting-phase-copy-and-template-fix-2026-08-14 (render-blog.py/inspect/blog) — all orthogonal, this run wrote to none of them. Done(last 10) + grep of full TASKS.md for volvo/xc60/xc90/s60/s90 found zero prior Volvo mentions anywhere. No overnight-builder/vinnote/content-checklist-authoring task active (consistent with memory: overnight-builder mount-broken since 2026-08-14). No Re-sync needed.
    Warranty structure note: 5yr/unlimited-mile coverage (upgradeable to 10yr) calculated from ORIGINAL in-service date/zero miles, not CPO purchase date — differs from most other OEMs in this library where CPO warranty clock starts at purchase; flag for downstream content so buyer-facing copy doesn't assume a fresh clock.
    Top-3-model mapping (by 2025 US sales volume): XC60 (#1, 41,105 units) — added VCM software fault 2017-2019 + Service Action S39893 + Sensus infotainment stress-test gap + transmission fluid check; XC90 (#2, 40,217 units) — added Sensus infotainment gap, water-intrusion/electrical check, 2016-2017 Park-rollaway TCM software item, door lock/battery-drain item; S60 (highest-volume sedan) — added ABS/handbrake recall (MY2023 built 2022) verification, hood-latch/door-lock check, airbag wiring-harness check, thermostat/water-pump/injector TSB items.
    Key gap for downstream content: Volvo publishes no separate PHEV (T6/T8 Recharge)/BEV inspection-point variant despite selling plug-in trims across most of the lineup since ~2016 — fifth straight OEM (after VW/BMW/Mercedes-Benz/Audi) whose national checklist is a category summary rather than a full line-item list.
    Weekly milestone: DONE — volvo-certified.md saved + INDEX.md updated (P2 now BMW ✅ → Mercedes-Benz ✅ → Audi ✅ → Volvo ✅; next = Lincoln, last P2). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: Lincoln (fifth/last P2).

  2026-09-13 (this run): ingested Lincoln CPO protocol — TWO-TIER structure: 200-point Signature Certification (≤5MY/60k, 6yr/100k warranty from original in-service date) / 139-point Select Certification (≤7MY/80k, 12mo/12k warranty from CPO purchase date).
    Output: Product/CPO-Protocols/lincoln-certified.md, Product/CPO-Protocols/_runs/2026-09-13-lincoln.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. In-flight autovet-competitor-monitor (Competitors/) + autovet-seo-content (Content/blog/) orthogonal. Ready = the three COMMITTED-NOT-PUSHED vinnote batches (09-09/09-10/09-11/09-12) + autovetting-inspect-render-and-generation-fix-2026-09-13 (all inspect/index.html) — orthogonal, this run wrote only Product/CPO-Protocols/ + TASKS.md. grep of TASKS.md for lincoln/nautilus/navigator/corsair/aviator/mkc/mkx/mkz found only stale (>2-month-old, outside any freshness window) vinNote spec-fix mentions on lincoln-nautilus-2019 and lincoln-corsair-2020 (July 2026 batches) — complementary, this protocol is their upstream source, not a conflict. No overnight-builder/content-checklist-authoring task in flight (consistent with memory: overnight-builder mount-broken since 2026-08-14). No Re-sync needed.
    Both official inspection-checklist PDFs located and fetched directly from lincoln.com (forms LCPO-INSPECT-Signature-2026, LCPO-INSPECT-SELECT-2026) — full line-item detail for both tiers, same evidentiary bar as INFINITI/BMW/Ford.
    Key finding: FIRST OEM in the library where the older/higher-mileage tier (Select) gets FEWER inspection points (139 vs 200), not just a lesser warranty — every prior multi-tier OEM (Ford, Nissan, Hyundai, Kia, Acura, INFINITI) held inspection depth constant across tiers.
    Top-3-model mapping (Nautilus #1 by 2025 volume 33,744 units, Navigator #2 ~22,185 units, Corsair — discontinued after MY2025 but 6-year highest-volume small Lincoln with existing AutoVet checklist coverage): campaign IDs WebSearch/cars.com-NHTSA-verified 2026-09-13 with exact scope in an anti-fabrication guard table: 20V414000 (Nautilus 2019-2020 + MKX 2016-2018 seat/airbag harness), 26V372000 (2019 Nautilus/Navigator/Mustang IPC blank display, REDO of 19V076), 26V377000 (2019 Nautilus lane-centering, redo of 19V031), 26V165000 (2024-25 Nautilus/2022-25 Navigator/2025 Aviator-Explorer, phased IPMA camera/ADAS loss), 26V344000 (2018-2022 Navigator/Expedition seat-belt pretensioner, REPLACES 24V099 AND 25V197), 26V402000 (2018-2021 Navigator/Expedition + 2020-21 Explorer/Aviator + 2021 F-150 park-pawl rollaway, remedy NOT yet available), 26V204000 (2021-2023 Navigator/Expedition/Super Duty wiper arms), 26V091000 (2023-2026 Corsair PHEV/2022-26 Escape HV battery, expands 24V954+25V489), 25V789000 (direct predecessor to 26V091000, same defect), 25V685000 (2020-2022 Corsair + 2016-2019 MKC block heater fire risk, remedy anticipated Sept 2026), 26V123000/26V117000/26V122000/26V301000 (Corsair rearview/wiper/EGR/park-pawl).
    Deepest supersession chain found to date in this library: Corsair PHEV HV-battery defect reissued FOUR times (24V954→25V489→25V789000→26V091000), remedy still "under development" at every step — reinforces the standing "superseded by later campaign" schema-field recommendation open since VW (08-09).
    Point-count coincidence flagged (NOT verified item-by-item): Lincoln Select's 139 points exactly matches Ford Blue Advantage's Blue Certified tier (ingested 05-31) — consistent with both brands sharing a Ford Motor Co. corporate inspection program; cross-referenced to ford-certified.md. Flagged as a possible future diff, not claimed as confirmed identical.
    Open flags for Daniel: $100 deductible sourced only from ConsumerAffairs (third-party), not a primary Lincoln warranty booklet — do not publish as certain; whether the two-tier Signature/Select split is new for 2026 vs. longstanding was not established; two cited recalls (26V402000 Navigator, 25V685000 Corsair) have remedies NOT YET AVAILABLE — downstream content must not imply a fix exists.
    Weekly milestone: DONE — lincoln-certified.md saved + INDEX.md updated. **P2 ROTATION COMPLETE** (BMW ✅ → Mercedes-Benz ✅ → Audi ✅ → Volvo ✅ → Lincoln ✅). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: **Porsche (first P3)**.

  2026-09-21 (this run): ingested Porsche CPO protocol (111 inspection points; single tier — no lite/select/EV tier, unlike Acura/INFINITI/Nissan/Hyundai/Honda/Ford). First OEM in the library where the point-count is real and OEM-printed but absent from the *current* US consumer marketing page — located and used the actual US dealer-facing PQIS inspection checklist (cars.com's OEM-checklist library, mirrored at autoipacket.com), which carries the "111+ point" language verbatim on its signed Statement of Certification; porsche.com/usa/approved-used/ and the 2022/2025 warranty PDFs describe only the 8 category names and state no number — a third distinct missing-number/mismatch pattern in this library, after VW/BMW/Volvo (no number published anywhere) and Mercedes/Audi (marketing number ≠ public line-item list).
    Output: Product/CPO-Protocols/porsche-certified.md, Product/CPO-Protocols/_runs/2026-09-21-porsche.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. In-flight autovet-competitor-monitor (Competitors/, next=Carfax) + autovet-seo-content (Content/blog/, next=re-check Toyota Highlander/Tier-2) orthogonal — neither references Porsche, 911, Cayenne, Macan, Panamera, or Taycan anywhere in TASKS.md. Ready to deploy/publish (menu-generation-and-year-gap-fix 09-17, pinpoint-dead-route-repair 09-16, pinpoint-filter-cells-B1-B4 09-15, vinnote batches 09-09..09-14, inspect-render-and-generation-fix 09-13, inspect-key-namespace-rename 09-03, pinpoint-fueltype-schema-fix 08-21, phase-copy-and-template-fix 08-14) is entirely inspect/index.html, pinpoint/index.html, scripts/, or Content/blog/ — none touch Product/CPO-Protocols/ and none carry a Porsche slug. Done(last 10) grep for porsche/911/cayenne/macan/panamera/taycan found only the pre-existing wave-16 (2026-08-03) recall-audit note about a "Porsche-conrod" number mis-pasted onto ford-escape-2013 — this run independently verified via NHTSA's own RCRIT/RCONL filings that 14V-090 (AE01) genuinely belongs to the 2014 911 GT3, confirming (not conflicting with) that wave's DEL call. No overnight-builder/vinnote/content-checklist-authoring task in flight is launching a Porsche vehicle page. Verified against: autovetting-recall-audit-wave16-2026-08-03 (14V-090 cross-reference). No Re-sync needed.
    Campaign IDs verified first-hand this run via NHTSA Part 573 filings: Macan — 20V077000/ALA2 (2015-2018 fuel pump service-cover fuel leak/fire, 70,117 units, largest population on any of the three mapped models), 23V443000/APA9 (seat belt anchor, shared w/ several Panamera variants), 22V656000/ANB4 (headlight screw cap, shared w/ Cayenne/Panamera/Cayman S, 193,000 units, FMVSS 108). Cayenne — 25V634000/ASA9 (2024-2026 HP fuel pump fastener fuel leak/fire, mailed 2025-11-19, too recent for CPO volume yet), 25V896000/ASB2 (2019-2025 rearview camera software, 172,107 units, shared w/ 911/Taycan/Panamera, still in progress — interim letters mailed 2026-02-16), 22V656000 (shared). 911 — 14V090000/AE01 (2014 GT3 only, 209 units, connecting-rod/crankcase fire, full engine replacement remedy), 21V697000/AMB9 (2020-2021 Carrera+Taycan brake booster, only 11 units — smallest population found anywhere in this library, still VIN-check mandatory), 23V715000/APB3 (bucket-seat-equipped Turbo S/GT3/GTS variants 2021-2024 only, airbag deploy logic — equipment-scoped not model-year-scoped, same "real campaign wrong variant" gap flagged since VW 08-09), 25V896000 (shared).
    NOT-a-recall content asset flagged: 2010-2016 Panamera / 2011-2019 Cayenne V8 coolant-pipe adhesive defect (active class action, invisible to VIN lookup) — third consecutive German-OEM non-recall engine/cooling pattern in this library after BMW N20/N63 (08-16) and Mercedes M274 (08-23), strengthening the still-unwritten independence/physical-inspection counter-positioning content piece the competitor-monitor workstream has flagged unwritten across many runs.
    Not-a-recall flag: IMS bearing failure (911/Boxster/Cayman lore) is scoped to M96/M97 engines (996-gen 911 1997-2008, early 997.1 2005-2008) — every one of those model years now sits outside Porsche's own 13-model-year CPO eligibility window as of 2026 (cutoff = MY2013); flagged so downstream content doesn't import an obsolete failure story onto a car that can no longer even qualify for this CPO program.
    Open flags for Daniel: electric Macan (MY2024-2025) carries three newer recalls (airbag backrest screws, over-bright headlights, rearview camera) not deep-verified this run — too new for meaningful CPO used-market volume yet; PDK clutch-pack intervals, N-rated tire part numbers, and the full non-listed-aftermarket disqualification list need Mitchell1/ALLDATA; a Florida lawsuit (GT3 sold post-training-use, allegedly mis-reinstalled undercarriage) and scattered forum complaints about CPO inspections missing aftermarket parts/windshield history are noted as directional color only, not verified systemic findings; "111-point" should be sourced to the PQIS checklist/international site in downstream content, never attributed to porsche.com/usa.
    Weekly milestone: DONE — porsche-certified.md saved + INDEX.md updated. **P3 ROTATION BEGUN** (Porsche ✅ → Jaguar/Land Rover → Mini). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: **Jaguar/Land Rover (second P3)**.

  2026-09-27 (this run): ingested Jaguar / Land Rover CPO protocol -- 165 inspection points, identical figure and identical eligibility/warranty structure published for BOTH brands (one shared JLR corporate program, not a coincidence like the Ford/Lincoln 139-point match flagged 09-13).
    Output: Product/CPO-Protocols/jaguar-land-rover-certified.md, Product/CPO-Protocols/_runs/2026-09-27-jaguar-land-rover.md.
    Sibling check: no true conflict. Protocol files are upstream of inspect/ checklists; auto-pusher does not watch Product/CPO-Protocols/. Grep of TASKS.md In-flight + Ready + Done(last 10) for jaguar/land rover/range rover/defender/discovery/evoque/velar/f-pace found zero hits outside this block itself. In-flight autovet-competitor-monitor (Competitors/, last entry 09-24 Carfax/Mobility Global, next=CarGurus) + autovet-seo-content (Content/blog/, last entry 09-23 Kia Sportage, next=Highlander-recheck or Tier-2) orthogonal -- neither references Jaguar or Land Rover. Ready to deploy/publish (menu-missing-nameplate-sweep 09-27, menu-wrangler-2024-base-row 09-26, menu-duplicate-model-rows 09-25, and the rest of the queue back through 08-14) is entirely inspect/index.html, pinpoint/index.html, or scripts/ -- none touch Product/CPO-Protocols/ and none carry a Jaguar or Land Rover slug. One existing checklist slug found via grep of inspect/index.html: land-rover-defender-2020 (complementary, not conflicting -- see data-hygiene flag below). No overnight-builder/vinnote/content-checklist-authoring task in flight is launching a Jaguar or Land Rover vehicle page. Verified against: none (no prior task touched this brand pair). Cross-referenced to: land-rover-defender-2020 (inspect/index.html). No Re-sync needed.
    Program asymmetry: Land Rover (97,176 US units, 2025) vs Jaguar (6,670 units, 2025, down 42.3% YoY) -- Jaguar has discontinued every ICE model (XE/XF/F-TYPE/E-PACE/I-PACE) under the all-electric "Reimagine" strategy and its EV relaunch has reportedly slipped past 2025 into 2026, so the Jaguar CPO population is aging with no new supply. Mapped 3 Land Rover models (Defender #1 28,389 units, Range Rover Sport #2 23,348, Range Rover #3 19,691) + Jaguar F-PACE (the brand's sole remaining high-volume nameplate) rather than 3-and-3.
    HEADLINE FINDING: NHTSA 26V248000 (filed 2026-04-16, ~170,196 units) -- DC-DC converter boost-control-microchip fault causing loss of 12V charging, power steering, and complete drive power, sweeping nearly the entire current JLR mild-hybrid/PHEV lineup across BOTH brands (Range Rover/Sport/Velar/Evoque, Discovery/Discovery Sport, Defender, Jaguar I-PACE/E-PACE). NO REMEDY EXISTS YET per NHTSA's own filing (Motor1/Claims Journal coverage) -- every CPO-eligible car on this list carries an open, currently-unfixable recall. Second cross-brand finding: 26V389000 (filed 2026-06-11, 250,857 units: Defender 97,552 + Discovery 83,620 + Range Rover 69,685) -- airbag clockspring corrosion, remedy available (lubricant gel), NHTSA states a 300-400-mile warning-lamp lead time before failure -- an inspectable early-warning signal.
    ⚠️ UNRECONCILED RECALL PAIR, flagged not merged: 26V599000 (filed 2026-09-16, F-PACE 2021-2024 + Range Rover 2019-2024 per cars.com, "electrical overload"/"fails to start" DC-DC converter defect) reads as a SECOND, DISTINCT campaign from 26V248000's "boost control microchip" defect, filed five months later -- no source found this run stating whether it supersedes, expands, or is independent of 26V248000. Routed to the recall-audit workstream rather than guessed at; do not merge unit counts or assume one closes the other.
    Campaign IDs verified this run via cars.com's NHTSA-sourced recall feeds (Range Rover Sport, Range Rover, F-PACE pages) plus independent corroboration (Motor1, Claims Journal, pickuptrucktalk.com citing NHTSA filings directly) for the two mega-recalls: 26V248000, 26V389000, 26V599000, 26V097000 (RR Sport panoramic sunroof trim), 24V450000/24V451000 (RR Sport / F-PACE oil filter housing crack -- same defect family, separate campaign numbers per nameplate, flagged not to conflate), 24V678000/24V677000 (RR Sport / F-PACE rearview camera NFSM overheat), 24V947000 (Range Rover camera water intrusion), 25V514000 (RR Sport 2014-2017 suspension knuckle -- outside current CPO eligibility window, flagged for AutoVet's non-CPO checklist coverage instead), 23V045000 (F-PACE cam carrier oil channel), 22V580000 (F-PACE missing Audio Amplifier Module -- assembly gap), 22V524000/22V525000 (F-PACE seat belt pretensioner / tail lights), 21V667000 (F-PACE seat belt ALR).
    Non-recall content asset: Ingenium 2.0L gasoline engine (F-PACE, Evoque, Discovery Sport, Velar) -- timing chain stretch, VVT solenoid faults, oil consumption (Autoblog/AutoGuide, Aug 2026); the worse Ingenium diesel balance-shaft-bearing failure is overwhelmingly a European/diesel-market issue with limited US relevance. Fourth non-recall engine/drivetrain pattern in this library after BMW N20/N63 (08-16), Mercedes M274 (08-23), Porsche coolant-pipe adhesive (09-21) -- continues building the case for the still-unwritten independence/physical-inspection counter-positioning piece.
    Reliability/independence angle -- strongest yet in this library: Land Rover ranks 2nd-worst in Consumer Reports' 2026 brand rankings; JLR North America shows Not BBB Accredited (letter grade/complaint counts NOT independently confirmed this run -- re-verify before publishing); a Trustpilot 1.4/5 figure surfaced only via a search snippet, not fetched directly -- flagged [unverified], do not publish as certain. Unlike the German-brand non-recall patterns, here a documented, OEM-acknowledged, currently-OPEN 170k-unit recall does the independence argument's work without needing a forum-sourced pattern.
    Cross-file data-hygiene flag (NOT fixed this run, outside Product/CPO-Protocols/ scope): inspect/index.html's existing land-rover-defender-2020 entry states stats.recalls: 2 but ships an empty recalls: [] array. This protocol's verified 26V389000 + 26V248000 are the real candidates to populate it -- flagged for the recall-audit workstream, same pattern as the still-open Mazda CX-5 15V461 fabrication (flagged 09-16).
    Open flags for Daniel: BBB letter grade/complaint counts and the Trustpilot rating need independent re-verification before publishing; neither brand publishes numeric reconditioning thresholds (tire tread/brake pad/tire age) on its consumer CPO page -- likely a Mitchell1/ALLDATA or dealer-internal gap, not confirmed absent; JLR's "Pathfinder" factory diagnostic tool is a dependency for clockspring/DC-DC-converter remedies, same factory-tool-gap pattern as Lexus Techstream/INFINITI CONSULT III Plus; Jaguar's EV relaunch timeline should be reconfirmed at the next Jaguar-adjacent touch.
    Weekly milestone: DONE -- jaguar-land-rover-certified.md saved + INDEX.md updated. **P3 now Porsche ✅ → Jaguar/Land Rover ✅**; next = Mini (last P3). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: **Mini (third/last P3)**.

  2026-10-04 09:40: ingested MINI CPO protocol (230 inspection points; a third-party review states 197, unreconciled).
    Output: Product/CPO-Protocols/mini-certified.md, Product/CPO-Protocols/_runs/2026-10-04-mini.md.
    Sibling check: no overlaps. Grep of TASKS.md In-flight + Ready + Done(last 10) for mini/cooper/countryman/clubman/bmw found zero hits outside this block's own prior P3 notes and the already-ingested bmw-certified.md (read-only reused for the warranty-architecture comparison, not a conflict). In-flight autovet-competitor-monitor (Competitors/) + autovet-seo-content (Content/blog/) orthogonal -- neither references MINI or any of its nameplates. No overnight-builder/vinnote/content-checklist-authoring task in flight is launching a MINI vehicle page. No Re-sync needed.
    Finding: warranty structure ("1yr/unlimited after the 4yr/50k New Vehicle Limited Warranty expires") and the 3-approval sign-off chain are architecturally identical to BMW's own CPO program (ingested 08-16) -- confirmed shared BMW Group CPO design across both marques.
    Non-recall content asset: R56-era N14 turbo engine (2007-2010 Cooper S Hardtop + R55 Clubman) timing-chain-tensioner wear, resolved via nationwide class action (Skeen v. BMW of North America, D.N.J. 2:13-cv-1531) rather than an NHTSA recall -- 7yr/100k extended timing-chain warranty. Invisible to a VIN recall lookup; mapped as an AutoVet depth-add for both nameplates.
    Weekly milestone: DONE -- mini-certified.md saved + INDEX.md updated. **P3 ROTATION COMPLETE** (Porsche ✅ → Jaguar/Land Rover ✅ → Mini ✅). Full P0-P3 rotation (20 OEMs) now complete. Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: **Toyota** (loop restart -- re-verify published figures for drift, P0 files are 4+ months old).

  2026-10-11 09:50 [scheduled task]: ingested Toyota CPO protocol (loop-restart re-verification -- 160 inspection points (Gold) / 136 (Silver), unchanged from 2026-05-22).
    Output: Product/CPO-Protocols/toyota-certified.md, Product/CPO-Protocols/_runs/2026-10-11-toyota.md.
    Sibling check: Verified against: autovet-recall-study-under-15k (its 2026-10-06/10-09/10-10 runs independently verified NHTSA campaign numbers on toyota-corolla-2014/2020/2021 in inspect/index.html + scripts/recall-ledger.json -- a different file tree; this run cross-referenced its 23V865000 (2021 Corolla OCS airbag) finding into toyota-certified.md's Corolla section rather than re-deriving it, so the two files now agree). No true conflict: protocol files are upstream of inspect/ checklists, and the vehicle-launch freeze (DANIEL-DECISIONS-2026-07-29) means no overnight-builder/content-checklist-authoring task is in flight to coordinate a launch with. In-flight autovet-competitor-monitor (Competitors/, last entry 10-08 Cars.com) + autovet-seo-content (Content/blog/, last entry 10-07 Subaru Forester) orthogonal -- neither references Toyota/RAV4/Camry/Corolla. Ready to deploy/publish (recall-audit waves 24-25, vinnote batches) all touch inspect/index.html or scripts/recall-ledger.json, none touch Product/CPO-Protocols/. Done(last 10) grep for toyota/rav4/camry/corolla found only stale (>2-month-old) recall-audit wave-15/16 touches on toyota-tacoma-2012/4runner-2008/toyota-highlander-2010 in inspect/index.html -- different file tree, not a conflict. No Re-sync needed.
    Drift result: no drift in published figures (160/136 points, 6yr/85k Gold + 10yr/60-125k Silver eligibility, warranty terms all confirmed against a second independent dealer source). One correction (powertrain-warranty start date = TCUV purchase date, not original in-service date) and one resolved ambiguity (Silver point count = 136, not 130). Two real content gaps closed in the Camry mapping: added 21V890000 (brake power-assist, 2018-2019, ~227,490 units) and 20V012000/20V682000 (Denso low-pressure fuel pump, 2018-2020) -- both were already flagged for RAV4 in the 05-22 file but never carried over to Camry despite the identical defect family applying.
    Flags for Daniel: roadside-assistance term conflict (1yr/25k brochure vs 7yr/100k some dealer pages) still unresolved. Three MY2026-only recalls found (RAV4 PHEV ECU software, Camry combination-meter, Corolla headlamp aim) are outside the current mapped model-year ranges -- flagged for the next Toyota touch once they roll into the Gold-tier window.
    Weekly milestone: DONE -- toyota-certified.md re-verified + INDEX.md updated (no re-ingestion needed; loop-restart pass begun). Auto-pusher does not watch Product/CPO-Protocols/. Next in rotation: **Honda** (loop-restart re-verification).

### autovet-seo-content

- Status: in flight
- Started: 2026-06-17 (weekly rotation; date sourced from this block's own first Notes entry — added 2026-09-16 by the overnight builder, same reason)
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

  2026-08-12 14:20: drafted 2015 Ford Edge (2nd-gen CD4, 2015-2018 pre-refresh) pillar post — Tier-1 #19, the only uncovered Tier-1 vehicle with NO active sibling conflict. Buyer story = three-engine fork where NEITHER coolant-risk engine is "the safe one" (2.0T EcoBoost open-deck coolant intrusion, named in the 2025 class action covering 2015-2018 Edge / 3.5L Cyclone V6 timing-chain-driven INTERNAL water pump dumping coolant into the crankcase / 2.7T Sport = hard-life risk not systemic defect), plus the AWD PTU and the open-but-unfixable brake recall.
    Output: Content/blog/2026-08-12-2015-ford-edge-buyers-guide.md (2,540 words body, status: draft), Content/_seo-research/2026-08-12-2015-ford-edge.md. Also updated Content/_seo-research/top-500-vehicles.md (seed row 19 rewritten, Escape + Edge added to the Already-covered table).
    Recalls WebSearch-verified 2026-08-12, 5 campaigns, all with scope stated: 25V-544 / Ford 25S87 (rear brake jounce hose rupture, 2015-2018 Edge + 2016-2018 MKX, 499,129 units, 64 complaints / 2 crashes, filed Aug 2025) — **HEADLINE FINDING: the remedy is NOT AVAILABLE. Ford told NHTSA April 2026, then slipped to September 2026; owner letters mailed 2026-01-13 in phases with a second letter promised when the fix exists. So every 2015 Edge on the market today carries an open safety recall that no dealer can close.** Nothing on page 1 of the SERP says this; it is the post's timeliness hook and a red flag ("a seller who says the recalls are all done"). Also cited: 25V-572 / Ford 25S89 (rearview camera distorted/inverted/blank, ~1.5M 2015-2019 Ford/Lincoln incl. Edge, Sept 2025; suspect part built 2015-04-01 to 2017-06-30 so very early 2015 builds may be out of scope — VIN not model year); 22V-413 (shift-cable bushing rollaway, 2015-2018 Edge among ~2.9M — ALREADY LEDGER-VERIFIED here via recall-audit wave 15, reused not re-derived); 19V-632 / Ford 19S26 (steering-gear motor bolt corrosion, 2015-2016 Edge, 20 SALT-BELT STATES + DC ONLY, began Oct 2019). DISAMBIGUATION carried explicitly: 20V-692 / Ford 20S63 (link-shaft bracket, loss of motive power / loss of Park) covers the **2014** Edge ONLY (1st gen) plus 2014-2016 Explorer + 2014-2015 Taurus, 2.0L/2.3L FWD, ~15,587 units — the post names it as NOT-applicable so a seller cannot wave it as completed recall work (same pattern as Tucson 07-08 and Grand Cherokee 07-29).
    ZERO TSB numbers cited — 6F35 shudder and EcoBoost coolant bulletins described by CONDITION only, with a "have a dealer run the VIN" instruction instead of a number. PTU 30k-mile interval attributed to independent-shop consensus and explicitly contrasted against Ford's fill-for-life position, NOT presented as an OEM spec. 2.0L coolant intrusion framed as class-action ALLEGATION, not defect or recall. Failure-mileage claims sourced, not invented (Cyclone class-action plaintiff Edge engine failure ~95,000 mi; EcoBoost intrusion reports clustering 60s-90s of thousands with stated wide spread).
    CATALOG CORRECTION embedded (3rd in 5 runs): top-500 seed row 19 says "2.0T water pump (internal), PTU on AWD; 3.5L is the safer pick" — INVERTED. The buried timing-chain-driven water pump belongs to the 3.5L/3.7L Cyclone Duratec V6 (2018 class action, coolant into the crankcase, invisible because it never hits the ground), NOT the 2.0T; the 2.0T's coolant problem is a different mechanism (open-deck block/head sealing, coolant into the combustion chamber). "3.5L is the safer pick" is wrong on the water-pump axis. Replacement text drafted in the research file. Following Tucson (no Theta II) 07-08 and Escape (no PowerShift DCT) 08-05, this is the third seed row written from popular-summary knowledge that inherited its errors — RECOMMEND a full seed-row audit at the 2027-05 annual refresh rather than one-post-at-a-time fixes.
    Ford Blue Advantage 139/172-point protocol referenced from Product/CPO-Protocols/ford-certified.md, paraphrased not reprinted (business-plan §4.5 legal note), with the "we follow the same standard, we don't republish their document" line kept.
    Sibling check: no conflict — Ford Edge is the ONLY clean Tier-1. grep of inspect/index.html returns ZERO ford-edge-* slugs, so there is no checklist for this post to stomp and nothing mid-correction. Every higher-ranked uncovered Tier-1 IS inside the 14-day window: #2 Silverado (2014 blog post already exists AND recall-audit wave 23 rebuilt chevy-silverado-2014 TODAY 08-12), #12 GMC Sierra (wave 20 touched sierra-2014 on 08-08, and seed row 12 itself flags it as duplicate-Silverado content), #20 Toyota Highlander (wave 21 rewrote highlander-2014's powertrain generation, wave 23 found highlander-2020 written against the wrong generation TODAY, wave 24 queue continues) — all avoided per the skill's "pick a different vehicle" rule. In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) orthogonal. Ready = autovetting-recall-audit-wave23-2026-08-12 (inspect/index.html + scripts/recall-ledger.json) — orthogonal, this run wrote only Content/blog/ + Content/_seo-research/ + TASKS.md, and 22V-413 was READ from that workstream's verified ledger rather than re-derived. Verified against: autovetting-recall-audit-wave23-2026-08-12, autovetting-recall-audit-wave15-2026-08-03 (22V-413 scope). No Re-sync needed.
    ⚠️ ACCEPTED RULE VIOLATION, flagged for Daniel: selection rule 3 (avoid back-to-back same manufacturer) is broken — last post was 2013 Ford Escape on 08-05, this is Ford again. Taken deliberately because every non-Ford Tier-1 alternative sits inside an active recall-audit conflict window. Mesh diversity should be restored next run: Subaru Outback, Mazda CX-5 and Honda Pilot are all Tier-2, uncovered, and untouched by the audit.
    VERIFICATION PASS (subagent, independent WebSearch re-check of every campaign number against the Part 573 filings): ZERO fabricated campaign numbers — all 5 NHTSA IDs and all 4 Ford internal IDs confirmed real, Ford-owned, and correctly scoped. Four factual errors were found and FIXED before this block was written: (1) CRITICAL — the draft gave 25V-572's suspect-part window as 04/2015-06/2017 and told buyers an early 2015 Edge might be out of scope; that window is the Lincoln MKC/Navigator/Expedition line in the Part 573. The EDGE window is 06/25/2014-09/04/2018, the entire 2nd-gen run, so NO 2015 Edge is out of scope — the post said the opposite of the truth. Rewritten, and Edge-specific unit count (515,004) substituted. (2) 25V-544's owner-letter date was transposed from the camera recall — 25V-544 interim letters went out Sept 2025, the Jan 13 2026 date belongs to 25V-572. Fixed. (3) "64 complaints and two crashes" came from press coverage; the Part 573 says 64 warranty claims / 16 customer complaints / no accidents Ford is aware of. Post now gives both framings and attributes each. (4) "AWD standard on Sport" was wrong — the 2015 Edge Sport was sold FWD and AWD. Fixed, and turned into a buyer warning. Also added the disposition of the 2018 Cyclone class action (largely dismissed/resolved 2024) so the post isn't citing live litigation as a finding against Ford. LESSON, generalizable: **a Part 573 lists suspect-part date windows PER NAMEPLATE — reading the first window in the document and applying it to your vehicle produces a confident, precisely-dated, completely wrong claim.** Same shape as the model-year-vs-production-date trap logged in wave 22. Add to the fabrication-adjacent watchlist: this class of error passes every number-checking gate because the number is real.
    Weekly milestone: DONE — draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: a NON-Ford Tier-2 (Subaru Outback / Mazda CX-5 / Honda Pilot) to break the Ford run; Toyota Highlander (#20) once the recall-audit generation-boundary sweep clears it; then re-rank top-500 — Tier 1 is now 100% covered except Highlander.

  2026-08-26 03:11: drafted 2014 GMC Sierra 1500 pillar post -- Tier-1 #12, the last clean uncovered Tier-1 vehicle. Original target was the 2018 Toyota Camry (top-500 seed row #6, "highest-ranked fully-uncovered" per the prior run's notes) -- before drafting, found `Content/blog/2026-05-31-2018-toyota-camry-buyers-guide.md` already exists (status: published), an 18-post gap in the `top-500-vehicles.md` "Already covered" table that only started tracking from 2026-06-17 onward. Re-ranked against the actual blog directory instead of the tracking table: every Tier-1 rank 1-19 is already covered. Pivoted to GMC Sierra 1500 (#12) before any drafting occurred -- the only remaining uncovered Tier-1 rank besides Toyota Highlander (#20, excluded: recall-audit's generation-boundary sweep is still unresolved on Highlander per wave 23 (08-12), risk of citing soon-to-be-rewritten data).
    Output: Content/blog/2026-08-26-2014-gmc-sierra-1500-buyers-guide.md (2,634 words body, status: draft), Content/_seo-research/2026-08-26-2014-gmc-sierra-1500.md.
    Recalls: reused the complete, already-verified 16-campaign set from inspect/index.html gmc-sierra-2014 (recall-audit wave 20, 2026-08-08 rebuild) rather than re-deriving -- same precedent as the Ford Edge post's 22V-413 reuse. Not independently re-verified against static.nhtsa.gov this run; that inheritance is stated explicitly in the post's footer and the research file. Two "repair-of-a-repair" pairs called out as the post's differentiation angle vs. the existing Silverado post: 16V-651/17V-437 (incomplete airbag-software remedy) and 16V-209/21V-245 (wrong replacement seat-belt cable). AFM lifter failure mileage window (60k-130k) sourced from independent forum/repair consensus, not a single bulletin -- no TSB number fabricated. Ongoing federal AFM/DFM lifter litigation (E.D. Michigan, no class/settlement as of March 2026) mentioned but explicitly scoped as possibly not covering this generation's L83/L86 engines (the suit's press coverage centers on newer L84/L87 DFM engines) -- flagged as an open question, not asserted either way. No Takata campaign found on this slug's verified set; stated as "not confirmed" rather than "does not exist."
    CATALOG/TRACKING CORRECTION flagged for Daniel (not fixed this run, outside scope): `top-500-vehicles.md`'s "Already covered" table is missing 18 posts dated 2026-05-27 through 2026-06-10 (both Corolla years, Camry, Civic, Tacoma, both Ram 1500 variants, Nissan Altima, Honda Accord x2, Acura TSX, Lexus RX350, Chrysler Pacifica, Toyota Prius, Mazda Miata, Honda CR-V, Ford F-150 x2) -- recommend a one-time backfill so future runs don't re-approach an already-covered vehicle.
    Interlinks to 2014-chevrolet-silverado (mechanical twin, primary cross-link) + 2021-ford-f150 + 2019-ram-1500 + 2019-ram-1500-classic (half-ton comparison set, all confirmed present in /blog/).
    Sibling check: no blocking overlap. Only prior touch on this slug is recall-audit wave 20 (2026-08-08, Done) -- 18 days old, outside the skill's 14-day window, and it's the source of the verified recall data reused above rather than a conflict. In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/) orthogonal. Ready = autovetting-pinpoint-fueltype-schema-fix-2026-08-21 (pinpoint/index.html JSON-LD fuelType) + autovetting-phase-copy-and-template-fix-2026-08-14 (CTA copy/templates) -- both orthogonal, neither touches a Sierra slug or Content/blog/. No overnight-builder/vinnote/content-checklist-authoring task launching a Sierra. Verified against: autovetting-recall-audit-wave20-2026-08-08 (gmc-sierra-2014 recall rebuild). No Re-sync needed.
    Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Toyota Highlander (#20) once recall-audit wave 24's generation-boundary sweep clears it; otherwise a Tier-2 vehicle (Subaru Outback / Mazda CX-5 / Honda Pilot -- none touched by any audit) to begin Tier-2 coverage now that Tier-1 is fully covered except Highlander.

  2026-09-02 03:15: drafted 2016 Honda Pilot (3rd-gen YF3/YF4, launch year) pillar post -- first Tier-2 vehicle, per the 2026-08-26 run's recommendation. Toyota Highlander (#20, last Tier-1 gap) remains blocked -- no wave-24 entry exists in TASKS.md, so the recall-audit generation-boundary sweep is still unresolved. Of the three untouched-by-any-audit Tier-2 candidates (Subaru Outback / Mazda CX-5 / Honda Pilot), picked Pilot for relevance: THREE separate, currently-live safety stories converge on this one model year.
  Output: Content/blog/2026-09-02-2016-honda-pilot-buyers-guide.md (2,165 words body, status: draft), Content/_seo-research/2026-09-02-2016-honda-pilot.md. Also updated Content/_seo-research/top-500-vehicles.md (added the Pilot row to Already Covered; updated Suggested Next Picks to note Pilot is done, Outback/CX-5 remain).
  Recalls/investigation WebSearch- and NHTSA-Part-573-verified 2026-09-02, all three fetched and read directly from static.nhtsa.gov (not aggregator copy): (1) 26V365 (reported 2026-06-04, ~2 months before this run) -- rear subframe corrosion, 2016-2022 Pilot + 2017-2023 Ridgeline + 2019-2023 Passport + 2014-2020 Acura MDX, 880,514 units, 22 named salt-belt states + DC, remedy (reinforcement kit) available now, owner letters mailed starting 2026-07-07 -- HEADLINE FINDING, timeliness hook. (2) 23V-751 (Nov 2023) -- connecting rod bearing/crankshaft-grind defect; the 2016 Pilot portion is scoped by PRODUCTION DATE, not model year: only Pilots built MAY 10, 2016 -- JUN 3, 2016 (a ~3.5-week window) are in scope, alongside 2018-2019 Pilot + Acura TLX/MDX + Odyssey + Ridgeline -- this narrow-window fact does not appear on any consumer-facing recall-tracker page we found; flagged as the post's key disambiguation, VIN-check not model-year-check. (3) PE25008 (opened 2025-08-20) -- OPEN federal investigation (NOT a recall), ~1.4M Honda/Acura J35 V6 vehicles incl. 2016-2020 Pilot, 414 bearing-failure complaints; NHTSA's own investigation record states this is a DIFFERENT root cause than 23V-751's crankshaft defect -- post explicitly separates the two rather than conflating them (a gap found in every aggregator source checked). (4) 21V-932 (Nov 2021) -- hood latch striker, 2016-2019 Pilot, 724,826 units, remedy available since Jan 2022 (old enough that a used-market car should have it closed already). (5) 16V-417 (Jun 2016) -- fuel tank leak, only 14 units of 2016 Pilot -- included for completeness, framed as low-probability. CORRECTION embedded (same pattern as Tucson/Escape/Edge in prior runs): Honda's Dec-2023 fuel-pump recall is 2017-2020 Pilot ONLY -- explicitly flagged as NOT applicable to a 2016, since at least one aggregator lists it under 2016 Pilot recalls. TSB 17-015 (2016-17 Pilot, torque-converter judder, root cause = transmission fluid heat degradation not a hardware fault, remedy = software update) confirmed via a Ridgeline-forum thread citing the bulletin directly -- real bulletin ID, not fabricated. VCM oil-consumption figures ("~1 qt/1,000-1,500 mi") and the engine-mount-wear claim are explicitly sourced to owner-forum/repair-community consensus, not cited as a manufacturer figure -- no TSB number invented for either. Honda 182-point HondaTrue checklist referenced from Product/CPO-Protocols/honda-certified.md, paraphrased/summarized only (not reprinted), consistent with the Ford/business-plan-§4.5 pattern used in every prior post. Interlinks to 2020-ford-explorer, 2015-jeep-grand-cherokee, 2019-honda-crv, 2017-chrysler-pacifica (all four confirmed present in /blog/ by directory listing before linking).
  Sibling check: no overlaps -- Verified against: no active workstream touches a Honda Pilot, Subaru Outback, or Mazda CX-5 slug anywhere in TASKS.md (grep of the full file for pilot/outback/cx-5/cx5 found zero In-flight or Ready hits and only stale Done entries >18 days old, e.g. wave 18's 2026-08-05 subaru-outback-2015 recall rebuild and wave 17's cross-make-collision note on the same slug -- both outside the 14-day window and both in inspect/index.html, a different file tree from this run's Content/blog/ + Content/_seo-research/ output). In-flight autovet-competitor-monitor (Competitors/, last entry 2026-08-20 CARCHEX, next=iNeedaPPi) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, last entry 2026-08-30 Audi, next=Volvo) orthogonal -- neither references Honda, Pilot, or any J35-platform vehicle. No overnight-builder/vinnote/content-checklist-authoring task appears anywhere in TASKS.md for this run's window (consistent with memory's note that overnight-builder has been mount-broken since 2026-08-14). Ready = autovetting-pinpoint-fueltype-schema-fix-2026-08-21 (pinpoint/index.html) + autovetting-phase-copy-and-template-fix-2026-08-14 (scripts/render-blog.py, inspect/index.html, blog/*/index.html rendered output) -- both orthogonal; this run touched neither pinpoint/index.html nor any rendered blog/*/index.html output, only the Content/ source tree. No Re-sync needed.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Subaru Outback or Mazda CX-5 (both still untouched by any audit) to continue Tier-2 coverage; re-check whether recall-audit wave 24 has landed and cleared Toyota Highlander (#20) before defaulting back to Tier-2.

  2026-09-09 10:03 [scheduled task]: drafted 2015 Subaru Outback (5th-gen BS, launch year) pillar post -- second Tier-2 vehicle. Picked over Mazda CX-5 (the other remaining untouched Tier-2 candidate) because the content story is materially stronger: an active class-action settlement (Yaeger v. Subaru, FB25 oil consumption) plus 4 concrete NHTSA recalls plus 612 owner complaints already catalogued, versus the CX-5's own checklist rating of "no significant failure modes." Toyota Highlander (#20, last Tier-1 gap) still has no wave-24 entry in TASKS.md, so it remains blocked pending the recall-audit generation-boundary sweep -- deferred again, consistent with the 08-26 and 09-02 runs.
  Output: Content/blog/2026-09-09-2015-subaru-outback-buyers-guide.md (~1,300 words body, status: draft), Content/_seo-research/2026-09-09-2015-subaru-outback.md.
  Recalls reused verbatim from the site's own already-verified inspect/index.html subaru-outback-2015 checklist + scripts/recall-ledger.json (not re-derived): 14V-577 (accessory trailer hitch, WQN-50), 15V-366 (brake light switch / EyeSight, WQS-54), 15V-502 (propeller shaft seal / trans oil leak fire risk, WQU-56), 16V-251 (ESC brake fluid moisture, WTC-64). CATALOG CORRECTION carried forward from wave 18 (2026-08-05): explicitly excluded two campaign numbers previously fabricated on this exact slug and since deleted from the ledger -- 14V-787 (mislabeled Takata; Subaru's real Takata scope for this platform is 2003-2005 only) and 20V-696 (mislabeled Denso fuel pump; the real campaign is 20V-218, scoped to 2019 models). Yaeger v. Subaru settlement details (filed 2014 D.N.J., final approval 2016-08-31, covers 2011-2015 FB-engine models) independently WebSearch-confirmed 2026-09-09, not sourced from the site. No claims left [unverified] -- every recall/TSB number and the settlement citation traces to either the site's own ledger or an independent web source. Interlinks to 2016-honda-pilot + 2019-chevrolet-equinox + 2018-hyundai-tucson (all confirmed present in /blog/ by directory listing before linking).
  Sibling check: Verified against: no overlaps. Grep of TASKS.md In-flight + Ready + Done(last 10) for outback/subaru/cx-5/cx5 found only stale Done entries outside the 14-day window (recall-audit wave 18's 2026-08-05 subaru-outback-2015 recall rebuild -- the source of the verified data reused above, not a conflict) plus the 2026-09-06 Volvo CPO-protocol note's unrelated grep hit. In-flight autovet-competitor-monitor (Competitors/, last entry 2026-09-03 iNeedaPPi) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, last entry 2026-09-06 Volvo) orthogonal -- neither references Subaru or Outback. No overnight-builder/vinnote/content-checklist-authoring task in Ready touches Content/blog/ or a subaru-outback slug (Ready = key-namespace-rename, fueltype-schema-fix, phase-copy-fix, and the 2026-09-09 vinnote batch -- all inspect/index.html or pinpoint/index.html, all disjoint from this run's output files). No Re-sync needed.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Mazda CX-5 to close out the currently-flagged Tier-2 pair; re-check whether Toyota Highlander (#20) has cleared the recall-audit generation-boundary sweep before defaulting back to Tier-2.


  2026-09-16 03:10 [scheduled task]: drafted 2016 Mazda CX-5 (KE, 1st-gen 2013-2016, final model year) pillar post -- closes out the "currently-flagged Tier-2 pair" tracked across the 2026-08-26/09-02/09-09 runs (Honda Pilot 09-02, Subaru Outback 09-09, Mazda CX-5 today). Picked model year 2016 specifically, not the site's existing mazda-cx5-2013 inspect-checklist slug, for two reasons: (1) the Mazda CPO protocol file (Product/CPO-Protocols/mazda-certified.md) flags "2016 KE had the heaviest recall activity of the generation" -- the richest verified-recall story in the 1st-gen run; (2) mazda-cx5-2013 carries a known unresolved site data-hygiene defect (campaign 15V461, an FCA/Jeep Uconnect recall mis-pasted onto the Mazda slug, flagged in Top-100-Vehicles-Priority.md lines 60/242 as needing adjudication) -- a different model year avoids any risk of this post inheriting or cross-referencing that fabrication. Confirmed via grep of inspect/index.html: only mazda-cx5-2013 and mazda-cx5-2017 exist as checklist slugs -- mazda-cx5-2016 is genuinely new ground, not a reuse of existing verified data. Toyota Highlander (#20, last Tier-1 gap) remains blocked -- still no wave-24 recall-audit entry in TASKS.md -- deferred again, consistent with the three prior runs.
  Output: Content/blog/2026-09-16-2016-mazda-cx5-buyers-guide.md (1,861 words incl. frontmatter, status: draft), Content/_seo-research/2026-09-16-2016-mazda-cx5.md.
  Recalls WebSearch-verified 2026-09-16, independently derived (no existing inspect/index.html mazda-cx5-2016 checklist to reuse): 16V064000 / Mazda 9216B (fuel filler pipe rupture / fire risk, 2014-2016 CX-5, 268,799 units, built 2013-06-27 to 2016-02-02); 16V203000 / Mazda 9316D (front strut lower bolt loosening -> steering knuckle separation, shared campaign with 2016 CX-3 / 2013-2014 Mazda2 / 2013-2015 CX-9, only ~578 units total across all four nameplates -- explicitly framed in the post as a narrow fastener-torque issue, not systemic, to counter "years to avoid" listicles that imply otherwise); 20V063000 / Mazda 4320A (LED DRL sulfur-corrosion flicker/failure, 2016 CX-5 only, built 2014-11-03 to 2015-12-07, ~36,760 units, not identified until 2020). Also noted 16E002000 (equipment-level recall, replacement-windshield Smart City Brake Support bracket, tape-only mounting) as applicable only if the car has had glass replaced, kept distinct from anecdotal "weak glass" cracking complaints. HEADLINE FINDING / post differentiator: Mazda TSB 04-001/18 -- rear EPB caliper may not release fully, causing brake drag/overheat/rapid pad wear -- scoped to 2016 CX-5 units built before September 9, 2016 (VIN lower than JM3KE******866136), identifiable by a caliper lot-number stamp (697+ = updated part). It's a dealer bulletin, not an open safety recall, so it will not surface on a standard NHTSA VIN check -- no bulletin number fabricated for anything else: MZD Connect infotainment issues, transmission shudder/hesitation, and AWD rear-differential noise are all described by condition only, left unnumbered, consistent with the anti-fabrication guard already documented in Product/CPO-Protocols/mazda-certified.md for this make. No CPO protocol content reprinted verbatim (business-plan Sec 4.5); referenced as "OEM-aligned" only.
  Sibling check: Verified against: no overlaps. Grep of TASKS.md In-flight + Ready + Done(last 10) for cx-5/cx5/mazda within the 14-day window (since 2026-09-02) found only one hit -- the 2026-09-13 vinnote-queue-hygiene entry, which removed mazda-cx5-2013 from the vinnote queue as "already had a vinNote" (different file tree, inspect/index.html, and a different model year than this post's 2016 pick -- not a content conflict). In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Mazda protocol already ingested 2026-07-05, read-only reused this run) orthogonal. Ready to deploy/publish section holds no Content/blog/ or Mazda-slug entries. No overnight-builder/vinnote/content-checklist-authoring task in flight touching a Mazda CX-5 slug. No Re-sync needed.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: re-check whether Toyota Highlander (#20) has cleared the recall-audit generation-boundary sweep (wave 24 still hasn't landed as of this run); otherwise rank further into Tier-2 (Honda Accord, Subaru Forester, Mazda3, Hyundai Elantra, Kia Sportage are all untouched) since Pilot/Outback/CX-5 closes the previously-flagged Tier-2 trio. Flagging for Daniel (not fixed this run, outside scope): mazda-cx5-2013's 15V461 fabrication is still unresolved in inspect/index.html / scripts/recall-ledger.json per Top-100-Vehicles-Priority.md -- a future recall-audit wave should adjudicate it.

  2026-09-23 03:12 [scheduled task]: drafted 2018 Kia Sportage (QL, 4th-gen 2017-2022, facelift-spec) pillar post -- Tier-2. Before picking, re-verified the prior run's "untouched" candidate list (Honda Accord, Subaru Forester, Mazda3, Hyundai Elantra, Kia Sportage) against the ACTUAL Content/blog/ directory rather than trusting top-500-vehicles.md's tracking table -- caught that Honda Accord is already covered TWICE (2026-05-30-2014-honda-accord-buyers-guide.md, 2026-06-03-2018-honda-accord-buyers-guide.md), both from the untracked 2026-05-27--06-10 batch first flagged as a tracking gap on 2026-08-26. Removed Accord from candidates; corrected top-500-vehicles.md's Suggested-next-picks note accordingly and re-flagged the recurring backfill recommendation for Daniel. Skipped Mazda3 to avoid a third consecutive Mazda-adjacent touch (CX-5 posted 09-16; today's autovetting-menu-reroute-and-orphan-repair-2026-09-23 Ready block also restructures mazda3-2018/2019 menu routing in inspect/index.html -- different file tree, routing only, not a content conflict, but avoided anyway for manufacturer diversity per selection rule 3). Picked Kia Sportage over Subaru Forester/Hyundai Elantra: strongest documented story of the three -- a real, currently active Theta II engine class-action settlement that names 2011-2018-and-some-2019 Sportage explicitly, plus four VIN-verifiable NHTSA recalls specific to this model year.
  Output: Content/blog/2026-09-23-2018-kia-sportage-buyers-guide.md (~1,720 words incl. frontmatter, status: draft), Content/_seo-research/2026-09-23-2018-kia-sportage.md. Also updated Content/_seo-research/top-500-vehicles.md (added the Sportage row to Already Covered; corrected Suggested Next Picks to remove Accord, explain the correction, and note remaining untouched Tier-2: Forester, Mazda3, Elantra).
  Recalls WebSearch-verified 2026-09-23, cross-checked against cars.com's NHTSA-sourced recall listing for the 2018 model year specifically: 17V-224 / Kia SC147 (Knock Sensor Detection System product-improvement campaign -- software monitors engine vibration for early rod-bearing wear, forces ~1,800 RPM limp mode, extends long-block warranty); 18V907000 / Kia SC172 (fuel pipe damaged/misaligned during an engine replacement performed under 17V-224/warranty/KSDS, 2011-2018 Sportage -- this recall's own scope text is what confirms 17V-224 applied to Sportage, not just Optima/Sorento as Product/CPO-Protocols/kia-certified.md's "top 3 models" section implies); 21V137000 / Kia SC206 (HECU electrical short, engine-compartment fire risk, 2017-2021 Sportage, park-outside advisory); 22V703000 / Kia SC249 (tow hitch harness moisture/debris short -> fire, 2017-2022 Sportage, tow-hitch-equipped only). Theta II class-action settlement scope (2011-2018-and-certain-2019 Sportage, Theta II 2.0L/2.4L GDI, lifetime powertrain warranty + reimbursement) independently WebSearch-confirmed against topclassactions.com and Hyundai Motor America's own media-center release, not sourced from the site. CATALOG CORRECTION / clarification embedded (same pattern as prior runs' seed-row fixes): confirmed both 2018 Sportage engines -- 2.4L Theta II GDI (LX/EX) AND 2.0L Theta II T-GDI turbo (SX/SX Turbo) -- are Theta II family, correcting the common online framing that treats "Theta II" as an Optima/Sonata-only term and under-warns turbo-trim Sportage shoppers. No TSB number fabricated for transmission complaints (none found tied to a documented failure pattern this run -- treated as normal wear, not a named defect). Kia/Hyundai anti-theft ("Kia Boyz") software eligibility for the 2018 Sportage specifically left EXPLICITLY UNVERIFIED in the post -- sources gave inconsistent year-cutoff language for Sportage -- post directs buyers to Kia's own VIN-check tool rather than asserting a cutoff. No CPO protocol content reprinted verbatim (business-plan Sec 4.5); Product/CPO-Protocols/kia-certified.md's 164-point category structure and its explicit "OEM checklist gap AutoVet adds" framing (KSDS + oil-consumption as a hard gate, not a checklist nicety) paraphrased and extended to the Sportage, since that file's own worked examples only cover Optima/Sorento/Soul by name. Interlinks to 2018-hyundai-tucson + 2019-chevrolet-equinox + 2019-toyota-rav4 + 2016-honda-pilot (all confirmed present in /blog/ by directory listing before linking).
  Sibling check: Verified against: no overlaps. Grep of TASKS.md In-flight + Ready + Done(last 10) for sportage/kia found zero content-authoring hits within the 14-day window -- only a stale (2026-06-28, >80 days old) autovet-cpo-protocol-ingestion note about a "Kia Sportage 2023" vinnote-queue mention (different model year, different file tree, no overlap) and today's autovetting-menu-reroute-and-orphan-repair-2026-09-23 Ready block, which touches mazda3/highlander/civic/etc. menu routing but carries zero Sportage or Kia references (confirmed via targeted grep of that block). In-flight autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, Kia protocol already ingested 2026-06-28, read-only reused this run) orthogonal. Ready to deploy/publish section (menu-reroute 09-23, menu-phantom-year-rows 09-22, checklist-generation-spans 09-21, menu-generation-and-year-gap-fix 09-17, pinpoint-dead-route-repair 09-16, and the vinnote/inspect-render batches 09-09 through 09-14) is entirely inspect/index.html, pinpoint/index.html, or scripts/ -- none touch Content/blog/, Content/_seo-research/, or a Kia Sportage slug. No overnight-builder/vinnote/content-checklist-authoring task in flight is launching a Kia Sportage page. No Re-sync needed.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: re-check whether Toyota Highlander (#20) has cleared the recall-audit generation-boundary sweep (wave 24 still hasn't landed as of this run, now 6 runs deferred since 08-26); otherwise continue Tier-2 with Subaru Forester, Mazda3, or Hyundai Elantra (all still genuinely untouched, verified against the blog directory this run, not just the tracking table). Flagging for Daniel again (not fixed this run, outside scope, now a 3rd-run recurrence): the top-500-vehicles.md "Already covered" table's pre-06-17 tracking gap should get a one-time backfill so future runs stop needing to independently re-derive it from the blog directory.


  2026-09-30 12:23 [scheduled task]: drafted 2021 Hyundai Elantra (7th-gen CN7, launch year) pillar
  post -- Tier-2. Of the three untouched Tier-2 candidates flagged since 09-16 (Subaru Forester,
  Mazda3, Hyundai Elantra), picked Elantra: launch year of an all-new platform with three distinct
  powertrains (2.0L MPI Nu / 1.6T Gamma II N Line DCT / 1.6L Kappa Hybrid), a cluster of FOUR
  separate seat-belt-pretensioner recall waves (21V796000 10/13/21, 22V123000 3/3/22, 22V218000
  4/1/22, 22V354000 5/19/22) that no aggregator page totals up, a Hybrid-only unintended-acceleration
  recall (23V589000, ~38,000 US units, MCU software fault) that does NOT apply to the gas trims, and
  a documented Forward Collision-Avoidance Assist phantom-braking/non-engagement owner-complaint
  pattern (57 combined NHTSA complaints per carcomplaints.com/lemberglaw, not an open recall).
  Also four other verified recalls: 21V302000 (4/28/21, seat-recliner weld), 21V00M000 (12/28/21,
  windshield bonding), 22V632000 (8/18/22, airbag emblem weld), 24V879000 (11/21/24, rearview
  camera, gas+Hybrid).
  Output: Content/blog/2026-09-30-2021-hyundai-elantra-buyers-guide.md (~1,900 words body,
  status: draft), Content/_seo-research/2026-09-30-2021-hyundai-elantra.md.
  CATALOG NOTE: the Hyundai CPO protocol file's (Product/CPO-Protocols/hyundai-certified.md) Nu-engine
  "stall/fire" flag (Recall 203 / 21V-301) does NOT apply to this car -- that campaign covers the
  outgoing 2019-2020 AD-generation Elantra's Nu engine, a different platform despite sharing the "Nu"
  family name. Independently confirmed via NHTSA's own recallsByVehicle API: zero 21V-301 hits for
  2021 or 2022 model-year Elantra. Flagged in the post so a seller/forum thread can't wave that
  recall at a CN7 buyer.
  No claims left unverified except: no TSB number found for the FCA phantom-braking pattern or the
  dashboard-warning-light/power-steering owner-complaint pattern (both described as NHTSA
  owner-complaint patterns, not confirmed defects or recalls, per the site's anti-fabrication
  convention).
  Sibling check: no overlaps. In-flight autovet-competitor-monitor (Competitors/, last entry 09-24
  Carfax, next=CarGurus) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, last entry 09-27
  Jaguar/Land Rover, next=Mini) orthogonal -- neither references Hyundai or Elantra anywhere in
  TASKS.md. Toyota Highlander (#20, last Tier-1 gap) still blocked -- no wave-24 recall-audit entry
  exists in TASKS.md, now 8 runs deferred since 08-26. Grep of TASKS.md In-flight + Ready + Done
  (last 10) for elantra/hyundai found only the standalone hyundai-elantra-2021/2022 vinNote entries
  already present in inspect/index.html (a different file tree, read-only reused as background
  context, not a conflict) and the 07-08 Hyundai Tucson post (different model, no overlap). No
  autovet-content-checklist-authoring or autovetting-overnight-builder task in flight is launching a
  Hyundai Elantra page. No Re-sync needed.
  **RUN INTERRUPTED, RECOVERED 2026-10-07:** the device bridge to Daniel's computer disconnected on
  2026-09-30 after the blog post was written but before this TASKS.md entry could be appended live or
  before Content/_seo-research/2026-09-30-2021-hyundai-elantra.md's write could be confirmed -- see
  claude/2026-09-30-autovet-seo-content-run-findings.md in the AutoVetting project for the original
  incident report. The 2026-10-07 run confirmed Content/blog/2026-09-30-2021-hyundai-elantra-buyers-guide.md
  existed intact, found Content/_seo-research/2026-09-30-2021-hyundai-elantra.md genuinely missing
  from disk, reconstructed it verbatim from the project-doc backup, and appended this block -- all
  before starting its own pick.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch
  Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Subaru
  Forester or Mazda3 (both still untouched Tier-2); re-check whether Toyota Highlander (#20) has
  cleared the recall-audit generation-boundary sweep (still no wave-24 entry as of this run).


  2026-10-07 10:15 [scheduled task]: drafted 2019 Subaru Forester (5th-gen SK, launch year) pillar
  post -- Tier-2. Before picking, recovered backlog from an interrupted prior run: the 2026-09-30
  Hyundai Elantra draft existed in Content/blog/ but had no TASKS.md Notes entry and was missing its
  Content/_seo-research/ file (device bridge disconnected mid-run per
  claude/2026-09-30-autovet-seo-content-run-findings.md in the AutoVetting project). Confirmed the
  blog post intact, reconstructed the missing research file from that doc's backup content, appended
  the missing Notes block above (dated 2026-09-30, marked recovered), and updated
  top-500-vehicles.md's Already-covered table + Suggested-next-picks note for the Elantra before
  starting today's own pick.
  Picked Subaru Forester over Mazda3 -- the two remaining untouched Tier-2 candidates since 09-16.
  Forester's story is cleaner: 2019 is a true single-powertrain launch year (2.5L direct-injection
  FB25 + Lineartronic CVT, standard AWD, no turbo trim -- the XT was discontinued for this
  generation), with three independently NHTSA-verified recalls and a real, model-year-specific CVT
  TSB, plus two clean disambiguation opportunities against recalls that get mis-attributed to this
  car online.
  Output: Content/blog/2026-10-07-2019-subaru-forester-buyers-guide.md (~1,750 words body,
  status: draft), Content/_seo-research/2026-10-07-2019-subaru-forester.md.
  Recalls independently verified 2026-10-07 via api.nhtsa.gov/recalls/campaignNumber (not aggregator
  copy): 19V856000 (PCV valve separation / loss of power, 2/12/2019, shared w/ 2019 Ascent +
  Crosstrek, 51,613 units combined), 19V065000 (EPS connector short / loss of power-steering assist,
  6/2/2019, shared w/ 2019 Crosstrek, 10,417 units combined), 21V263000 (rear stabilizer bracket
  bolts loosen/detach, 4/15/2021, shared w/ 2018-2019 Crosstrek, 408,271 units combined).
  TWO DISAMBIGUATIONS, both independently confirmed via direct NHTSA campaignNumber lookups rather
  than trusting aggregator text: (1) 21V587000 (low-pressure fuel pump), the recall
  Product/CPO-Protocols/subaru-certified.md's own Forester section scopes to "2018 SK-gen Forester" --
  re-pulled its full Make/Model/ModelYear list this run and confirmed 2019 Forester is genuinely NOT
  in it (2018 only). Not cited in the post. (2) 23V755000, which a pickuptrucktalk.com aggregator page
  attributes to 2019-2023 Forester as a "backup camera/inhibitor switch" recall -- verified via
  NHTSA's own RCRIT filing + justia's recall database that this is actually a 2023 Outback/Legacy
  automatic-transmission park/neutral-start-interlock-switch campaign with zero Forester involvement.
  Not cited. Same aggregator page's cited PCV recall numbers ("19V-858/19V-844") also don't match the
  real campaign (19V856000) -- not used.
  TSB 16-103-16R (NHTSA doc #10202815, published 10/27/2021, CVT fluid seepage) confirmed real and
  specific to 2019 Forester via carcomplaints.com's TSB archive -- the post's headline finding.
  Bulletin 16-117-18 (CVT warranty extended 5yr/60k -> 10yr/100k) confirmed scoped to 2018
  model-year CVT Subarus; whether it (or a successor bulletin) reaches 2019 Foresters was NOT
  independently confirmed this run -- left in the post as a buyer question for the dealer, not
  asserted as fact. EyeSight phantom-braking and infotainment-freeze owner-complaint patterns
  described by condition only, no TSB number fabricated for either. Explicitly disambiguated the FB25
  engine from Yaeger v. Subaru (2011-2015 FB-engine class period, pre-direct-injection design) --
  the 2019 Forester's FB25 is the updated DI engine introduced with this generation, outside that
  settlement.
  Interlinks to 2015-subaru-outback + 2016-mazda-cx5 + 2016-honda-pilot + 2019-toyota-rav4 +
  2018-hyundai-tucson (all confirmed present in /blog/ by directory listing before linking).
  Sibling check: no overlaps. Grep of TASKS.md In-flight + Ready + Done(last 10) for
  forester/subaru/cx-5/mazda3 found only stale Done entries well outside the 14-day window (menu
  routing on mazda3-2018/2019 from 09-23, orthogonal inspect/index.html routing work, not a content
  conflict) and the Subaru CPO protocol file (read-only reused for the 21V-587 disambiguation above,
  itself read-only background, not a conflict). In-flight autovet-competitor-monitor (Competitors/,
  last entry 09-24 Carfax) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, last entry 09-27
  Jaguar/Land Rover) orthogonal -- neither references Subaru or Forester anywhere in TASKS.md. No
  autovet-content-checklist-authoring or autovetting-overnight-builder task in flight is launching a
  Subaru Forester page. No Re-sync needed.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch
  Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: Mazda3
  (last remaining untouched Tier-2 candidate from the 09-16/09-23/09-30 list); re-check whether Toyota
  Highlander (#20) has cleared the recall-audit generation-boundary sweep (still no dedicated wave-24
  Highlander content fix found in TASKS.md as of this run, though 09-17's menu-routing fix did split
  toyota-highlander-2014/2020 into correct generation-specific menu rows -- that's a routing fix, not
  confirmation the checklist *content* itself is generation-clean, so still deferred out of caution).

  2026-10-14 10:20 [scheduled task]: drafted 2018 Mazda3 (BM/BN, final model year of the 2014-2018
  generation) pillar post -- Tier-2. Last remaining untouched Tier-2 candidate flagged since
  09-16/09-23/09-30/10-07 (Subaru Forester posted 10-07; Mazda3 was the only name left on that list).
  Picked 2018 specifically because it carries the busiest single-model-year recall set in the whole
  BM/BN generation: four separate NHTSA campaigns, two of them extremely narrow (144 and 210 units),
  giving a real VIN-check-vs-broad-risk story to tell, plus a clean hatchback-vs-sedan disambiguation
  opportunity no aggregator source states plainly.
  Output: Content/blog/2026-10-14-2018-mazda3-buyers-guide.md (~1,770 words body, status: draft),
  Content/_seo-research/2026-10-14-2018-mazda3.md. Also updated Content/_seo-research/top-500-vehicles.md
  (added the Mazda3 row to Already Covered; Suggested Next Picks note records that the previously-flagged
  Tier-2 pair is now fully closed and flags Highlander re-check / unverified Tier-2-Tier-3 candidates for
  next run, to be confirmed against the actual blog directory rather than assumed).
  Recalls independently verified 2026-10-14 via api.nhtsa.gov/recalls/recallsByVehicle (not aggregator
  copy), cross-checked against Part 573 PDFs where unit counts mattered: 19V272000 (wiper relay/BCM
  fault, 2016-2018 Mazda3, 187,880 units -- the headline/broadest recall here); 17V745000 (incorrect
  exhaust valve spring, engine-stall risk, 2018 Mazda3 ONLY, just 144 units built Oct 9-18 2017);
  21V875000 (Denso low-pressure fuel pump impeller crack/deform, shared campaign across Mazda3/6/CX-3/
  CX-5/CX-9/MX-5/Mazda2, 121,038 units total, but the 2018 Mazda3's own slice is only 210 units built
  May 7-Oct 1 2018); 23V487000 (rearview-camera wiring-harness-fastener wear, confirmed via the Part 573
  PDF to apply ONLY to the 2014-2018 Mazda3 5-door HATCHBACK -- 141,491 of a 227,335-unit combined
  Mazda3+CX-3 campaign -- the sedan is not in scope at all, a real and checkable disambiguation no
  aggregator source states). DISAMBIGUATION embedded (same pattern as every prior run's seed-correction):
  19V-497 (2.5L cylinder-deactivation PCM -> valvetrain interference), which Product/CPO-Protocols/
  mazda-certified.md's own Mazda3 section already scopes to "2019-2020 Mazda3," is explicitly flagged in
  the post as belonging to the next, redesigned BP-generation car -- not this BM/BN-generation 2018 car --
  so a reader can't confuse the two generations' recall sets. No campaign number fabricated or estimated;
  the two coil-spring TSBs (02-015-18-3499, 02-014-18-3503) and the oil-consumption bulletin (MT-005-20)
  are all confirmed real via carcomplaints.com's TSB archive. Carbon-buildup cleaning cost ($350-480) and
  MAZDA CONNECT screen-replacement cost (~$1,000+) are both sourced to samarins.com, not invented or
  presented as OEM figures. No Mazda CPO protocol content reprinted verbatim (business-plan Sec 4.5);
  Product/CPO-Protocols/mazda-certified.md's category list and Mazda3-specific mapping paraphrased and
  extended, consistent with every prior OEM-protocol citation on this site. Interlinks to 2017-honda-civic
  + 2021-toyota-corolla + 2021-hyundai-elantra + 2016-mazda-cx5 (all four confirmed present in /blog/ by
  directory listing before linking).
  Sibling check: Verified against: no overlaps. Grep of TASKS.md In-flight + Ready + Done(last 10) for
  mazda3/mazda-3/mazda found only stale, orthogonal hits well outside the 14-day window: the 2026-07-05
  Mazda CPO-protocol-ingestion run (read-only reused above for the 19V-497 generation-scoping disambiguation,
  not a conflict), the 2026-09-16 Mazda CX-5 content post (different vehicle, different file, >14 days old),
  and several 09-22/09-23/09-25/09-26 menu-routing/duplicate-row fixes on mazda3-2018/2019 in
  inspect/index.html (a different file tree -- dropdown routing, not blog content -- and all now well
  outside the 14-day window from today's 2026-10-14 run date). In-flight autovet-competitor-monitor
  (Competitors/) + autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, last entry 10-11 Toyota
  loop-restart, next=Honda) orthogonal -- neither references Mazda3 anywhere in TASKS.md. Ready to
  deploy/publish (recall-audit wave-25, 2026-10-04, COMMITTED NOT PUSHED) touched mazda-cx5-2013's
  15V-461 false-citation fix in inspect/index.html + scripts/recall-ledger.json -- a different vehicle
  (CX-5, not Mazda3) and a different file tree than this run's Content/blog/ + Content/_seo-research/
  output; read-only cross-referenced, not a conflict. No autovet-content-checklist-authoring or
  autovetting-overnight-builder task is in flight anywhere in TASKS.md (consistent with the active
  vehicle-launch freeze, DANIEL-DECISIONS-2026-07-29 [freeze], which applies to overnight-builder/
  vinNote launches, not to this orthogonal content workstream). No Re-sync needed.
  Weekly milestone: DONE -- draft ready for Daniel's editorial review (auto-pusher does not watch
  Content/blog/; drafts stay private until Daniel approves + migrates). Next pick candidates: the
  previously-flagged Tier-2 pair (Subaru Forester, Mazda3) is now fully closed -- re-check whether Toyota
  Highlander (#20, last Tier-1 gap) has cleared the recall-audit generation-boundary sweep before
  defaulting to further Tier-2/Tier-3 picks (Nissan Sentra, Kia Forte, Chevrolet Trax, Subaru Crosstrek,
  Hyundai Santa Fe are candidates but NOT yet verified against the actual Content/blog/ directory --
  confirm there first, not just against this tracking table, per the recurring tracking-gap lesson).


### autovet-recall-study-under-15k

- Status: in flight
- Started: 2026-10-05 (02:00 MST overnight builder; `[freeze]` priority 2 per `DANIEL-DECISIONS-2026-07-29` — priority 1, the recall-audit waves, closed 10-03 at `unverified_legacy` = 0 and the `verified` tier was audited 10-04. Launch freeze still active, so no vehicle launch was available; night 16 without one.)
- Task: the original-data study "The most-recalled used cars under $15,000" (`_hub/Build-Log/_NEXT.md` item 4) — measure NHTSA campaign counts for every vehicle in the inspection catalog priced at or under $15,000, then publish as a pillar post plus a downloadable table. Measurement accumulates in one file; the post is built from it when the queue is empty.
- Touched files: `_hub/Content/_seo-research/recall-study-under-15k.md` (gitignored, the dataset), `_hub/Build-Log/2026-10-05.md` + `2026-10-06.md` + `2026-10-08.md` + `2026-10-09.md` + `2026-10-10.md` + `2026-10-11.md` + `2026-10-12.md` + `2026-10-13.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`
- Notes:

    2026-10-05 02:00 [scheduled task]: **48 of 51 vehicles measured against NHTSA, 225 campaign numbers recorded with the number list kept per vehicle so every row is auditable. The study is NOT publishable yet, and the reason is a finding: the count NHTSA returns depends on which model string you guess, and on the 2014 Silverado the difference is 6 versus 20.** No HTML touched; tracked diff is `TASKS.md` only.

    **The universe had to be defined before it could be measured, and defining it surfaced a live filter bug.** A "$15k" study needs a price field, and the Pinpoint cards carry two that disagree: the filter bucket `budget` and the displayed `price` contradict each other on **45 of 344 cards (13%)** — a $19,000 Golf filed `10-15k`, an $18,000 Frontier and a $17,000 C-HR filed `under-10k`, a $38,000 X5 filed `20-30k`. The chips filter on `budget`; the card shows `price`; so "under $10k" returns cars at nearly twice that. Same family as the orphan-vehicle bug (invisible to the filter) inverted: visible to the wrong filter. Which field is authoritative is a content call, so it is escalated, not guessed. For the study the resolution is forced — **`price` defines the universe**, because `price` is the number a buyer reads. Universe = cards whose `inspectUrl` resolves to a real checklist and whose `price` <= $15,000, deduplicated by slug, lowest-priced card kept: **n = 51**, model years 2011-2021.

    **Method, and the three traps in `recallsByVehicle`, all hit live.** One query per vehicle through the sandbox fetch path (`curl` to `api.nhtsa.gov` still exits 56 from both shells, re-tested; cloud proxy: `connect_rejected ... organization policy`), recording every campaign number and not just the count. (1) **Model-string fragmentation.** 2014 Silverado 1500: `model=silverado 1500` returns **6**, `model=silverado` returns **14**, and the sets are **disjoint**; a `silverado 2500` control returns 2, also disjoint, so matching is exact and NHTSA holds three strings for one truck. Honest count is the union, **20** — a one-query study would have published 6 and ranked this truck 31st of 48 instead of 1st. Wave 25 saw this from the other side (it looked like 8 misattributions and was nothing) and wrote the rule; this is the first time the rule has moved a number we were about to publish. (2) **The catalog endpoint does not agree with the recall endpoint** — `products/vehicle/models` for Chevrolet 2014 lists `SILVERADO 1500` and `SILVERADO 2500` and no bare `SILVERADO`, the very string with 14 campaigns. (3) **HTTP 400 is not zero** — `buick/encore/2018`, `buick/enclave/2018` and `bmw/3 SERIES/2018` all 400 while all three appear in their own make-year catalog; retried uppercase and with `issueType=r`, still 400, recorded as unmeasured and never as 0. Lexus was the recoverable case: `RX 350` 400s, **`RX350`** returns 1.

    **Provisional ranking:** 2014 Silverado 1500 **20** (union) · 2013 Ford Escape **18** · 2011 Subaru Forester **16** · 2013 Nissan Altima **12** · 2012 Jeep Wrangler **10** · 2016 Chevrolet Malibu **9**. Six vehicles — 12% of the universe — carry 85 of 225 campaigns (38%); eleven carry one each. That non-uniformity is the study's thesis and why it is worth publishing once the numbers are sound.

    **A by-product that answers the question 10-04 put to Daniel.** Against the model-year count, **31 of 48 pages understate and 7 match exactly** — understating is expected, since `stats.recalls` counts rows we display and waves 24-25 reduced many to the single standard VIN-check row, but some gaps are large and new: Silverado 3 vs 20, Cherokee 1 vs 7, Compass 1 vs 6, Sorento 2 vs 8, Malibu 3 vs 9. The other direction matters more for credibility: **10 pages ship more recall rows than their model year has campaigns**, headed by `toyota-corolla-2014` (5 vs 2) and `lexus-rx350-2011` (3 vs 1). Those are a verification queue and **not** findings — **confound recorded: checklist slugs span generations, NHTSA counts are per model year**, so a slug covering 2010-2012 can legitimately carry three model years of campaigns. Nothing was edited on the strength of a delta.

    **Found while validating the universe, not fixed, escalated: 17 of 311 Pinpoint `inspectUrl` links fall through to `renderComingSoon`, and 5 of them should not.** Cause is uniform — the `model=` parameter carries the trim while `CHECKLISTS`/`VEHICLE_MENU` store the model without it. For 11 there is no checklist for that vehicle at any year, so coming-soon is the honest page and nothing is broken. For **5 the checklist exists and the buyer is told it does not**: `Avalon Hybrid XLE`→`Avalon` (2022), `Corolla Hybrid LE`→`Corolla` (2023), `Highlander Hybrid XLE AWD`→`Highlander` (2023), `Crosstrek Sport`→`Crosstrek` (2023), `Golf Alltrack S`→`Golf` (2019). **One must NOT be repointed:** `Toyota Prius c` 2018 → `Prius` resolves, but the Prius c is a different, smaller, Yaris-based car; sending that buyer to the Prius liftback checklist is worse than the honest fallback. Left alone deliberately so a future run does not "fix" it. Not applied tonight — it is a `pinpoint/index.html` content diff, tonight's assignment is the study, and the Golf Alltrack row is a judgment call about whether the Alltrack wagon is served by the Mk7.5 Golf checklist.

    **Method note for whoever continues this: do not approximate `findChecklistByYMMT` with a regex.** Link resolution was simulated in node against the live `CHECKLISTS` and `VEHICLE_MENU` objects, evaluated out of the HTML. An earlier regex pass answered the same question with "286 of 311 links broken" — it had parsed 32 of 245 checklist headers because field order varies, and every header it missed looked like a dead link. The real answer is 17.

    Sibling check: no blocking overlap, and nothing to re-sync. This run modifies **one tracked file, `TASKS.md`**, and reads `pinpoint/index.html`, `inspect/index.html` and `scripts/recall-ledger.json` without writing them (worktree blobs unchanged; their `MM` status is the pre-existing stale index noise recorded on 10-03 and 10-04). Everything written is under `_hub/`, excluded by `.gitignore:31`. Ready blocks 09-09 -> 10-04 all touch `inspect/index.html` or `scripts/recall-ledger.json` and are ancestors of `main`, not concurrent siblings; wave 25 (`7a6af33`/`1bed111`) is the direct parent and this run consumes its ledger output read-only. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal — `autovet-seo-content` also writes `Content/_seo-research/` but per-vehicle research files, not this dataset file. **`Started:` audit clean** — all 30 blocks across In-flight, Ready and Done (last 10) carry a `- Started:` date, 0 missing. Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovet-seo-content.

    **Scanner: PASS** (641 files, exit 0, run against the mounted path; the file count was read, not just the exit code). **Correction to the 10-01 gate-bug note, which conflated two different failures.** Run exactly as the prompt spells it, `python3 /Users/danieldavis/.../scan_for_secrets.py /Users/danieldavis/.../autovetting` exits **2** — python cannot find the script, so a wrong *script* path fails closed, which 10-01 reported as a silent pass. The real vacuous pass is narrower and still open: **right script, unresolvable target** — `python3 $HOME/mnt/.../scan_for_secrets.py /Users/danieldavis/.../autovetting` prints `OK: scanned 0 file(s)` and exits **0**. So the ask stands, sharpened: **`scan_for_secrets.py` should exit non-zero when it scans 0 files.** Note also that piping the mandated command to `tail`/`head` masks exit 2 behind the pipe's status. **Syntax-check: N/A** — no HTML modified, verified by `href`-inventory and line-count equality rather than asserted. **Dead-links: verified** — no deployed file changed, so no link could change. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-04 baseline; the one warn is the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`.

    **PUSH: blocked. Day 27, 26 commits stuck, `origin/main` still at `0dfa937` while `main` is at `1bed111`.** `GET /user` with the stored PAT returns 401 again (prefix `ghp_krkG...`, `expires` still reads 2027-05-19, credentials file mtime still 2026-05-30 — revoked, not expired). No commit was built tonight: the only tracked change is this TASKS.md block, and a hand-built commit carrying nothing deployable is not worth adding to a 26-deep unpushed stack. **Useful for the next run that does need one:** `GIT_INDEX_FILE=/tmp/ix git add …` sidesteps the stale `.git/index.lock` entirely, so the 10-03/10-04 `hash-object`/`mktree`/`commit-tree` hand-build is no longer necessary — only the ref write is, since `HEAD.lock` still blocks `update-ref`. The locks themselves are still undeletable (`Operation not permitted`, the sandbox deletion block per the 10-04 diagnosis); the delete-permission prompt was again **not** fired at 02:00.

    **Next run — tranche 2, in order.** (A) Resolve the 3 HTTP-400 vehicles via `campaignNumber` on their shipped numbers or another string form (`3-SERIES`, `330I`). (B) Union-check every fragmentation-prone model string — `Rogue Sport`, `Silverado 1500`, `Mazda3`/`Mazda6`, `CR-V`/`HR-V`, `4Runner` — until that is done **every number in the table is a lower bound and the ranking is provisional**. (C) Per-number `campaignNumber` checks on the 10 over-citing slugs, `toyota-corolla-2014` and `lexus-rx350-2011` first. **No pillar post until A and B close** — a ranked table built on lower bounds is wrong in exactly the way wave 24 was wrong: plausible, specific, unverifiable.

    2026-10-06 02:00 [scheduled task]: **Tranche 2 closed A and C; B cannot be closed, and that is the finding — the union of NHTSA model strings is UNDISCOVERABLE, so every count in this study is a lower bound with no discoverable upper bound and the "most-recalled" ranking is not publishable from this API. Separately, C turned up one live content defect and it is fixed: `toyota-corolla-2021` told buyers their only critical check was a recall their car is not in, while omitting the 999,901-unit airbag campaign it IS in.** All 51 vehicles now measured, 231 campaign numbers.

    **A — the 3 unmeasured are resolved, and the 10-05 rule "HTTP 400 is not zero" needed amending.** A 400 is uninterpretable *alone*, but a **same-string different-year control** makes it readable. `model=enclave` 400s for 2018 and returns **6** for 2011; `model=encore` 400s for 2018 and returns **4** for 2015 — both strings are valid, so both 400s are **true zeros for MY2018**. Two controls fix the meaning: `buick&lacrosse&2018` returns 3 (the make is fine) and `buick&zzzqqnotacar&2018` also 400s, so **a 400 does not distinguish "no such string" from "string exists, no campaigns this year"** — only the year-control does. `buick-enclave-2018` = **0**, `buick-encore-2018` = **0**. **`bmw-3series-2018` is a 5-string vehicle:** `3 SERIES` and `320i` 400, `330i` 1, `340i` 1, `330e` 2, **`328d` 4** — union **6** (`18V465, 18V652, 18V755, 21V586, 21V907, 25V700`). All four numbers that page ships in prose are in the `328d` set, so **the BMW page's recall citations are genuine and correctly scoped** (its author labelled them "(328d only)"); the measurement just could not see them. BMW enters the table tied at 6; top 6 unchanged.

    **B — the union is undiscoverable, proved three ways, and this is the blocking result.** (1) **Fragmentation is not orthographic** — `mazda 3`, `crv`, `4 runner`, `wrangler unlimited` and `malibu limited` all 400, so `mazda3`/`cr-v`/`4runner`/`wrangler`/`malibu` are canonical and those five rows are **not** lower bounds. That narrows the problem to two real mechanisms, bare-vs-suffixed (Silverado) and trim-level (BMW). (2) **The recall-model catalog does not enumerate the strings the recall endpoint answers on, even filtered to recall-bearing models** — `products/vehicle/models?modelYear=2014&make=chevrolet&issueType=r` returns 51 models including `SILVERADO 1500/2500/3500` and **no bare `SILVERADO`**, the string holding 14 campaigns. (3) **The strings are visible only from inside the campaigns, which is circular** — `campaignNumber=14V301` lists `CHEVROLET SILVERADO 2014` (bare), but reaching that record required already knowing to query bare `silverado`. **To discover the string you need a campaign; to find the campaign you need the string.** Guessing until a 400 proves nothing (see A). The error is not small: Silverado 6 vs 20, rank 31 vs rank 1.

    **So tranche-2 item D resolves to a decision, not to more measurement.** Three options, no work done on any: **(1) reframe and publish** — drop "most-recalled", publish recall *exposure* as an explicit floor under a stated reproducible rule, and make the Silverado 6-vs-20 and the BMW 5-string case the editorial centrepiece ("the recall count you look up is probably wrong, and here is why" is a better AutoVetting piece than a ranking, and it is defensible); **(2) get the complete data** — NHTSA's `FLAT_RCL.zip` flat file has no model-string problem at all and needs **egress to nhtsa.gov**, the same single blocker as criterion 5; **(3) shelve the ranking**, keep the dataset as internal research. **Recommend 1 now, 2 when egress opens.** Escalated to Awaiting-Daniel; nothing published until he picks.

    **C — the whole "page over-cites NHTSA" column was a counting artifact, resolved for 8 of 10 slugs with no network.** `stats.recalls` equals the number of recall **rows displayed**, and waves 24-25 added a generic `Open recalls — VIN check` row to most slugs — that row is counted. Every "+1" in the 10-05 gap table is that row: Forester 17=16+1, Fusion 5=4+1, TSX 4=3+1, Sentra 4=3+1, Frontier 3=2+1, Kicks 2=1+1. `lexus-rx350-2011` (+2) is the same artifact plus `LSC 90G`, a **Lexus service campaign** and not an NHTSA number, correctly absent from the API. `nissan-pathfinder-2017` (+2) is **correct editorial** — the extra is `16V-244`, titled "OCS Software (2013–2016)", on an R52 slug whose own trim field reads "2013-2020": disclosed, and the generation-span confound exactly as predicted. **Worth recording as site behaviour: `stats.recalls` is a displayed-row count, not a campaign count, and the launch spec calls it "recall count" — a wording mismatch.**

    **The one real defect, verified and fixed: `toyota-corolla-2021`.** Its summary read *"The only critical buyer check is the 2020 model year Denso fuel pump recall (20V-682)."* Against `campaignNumber`: **`20V682` is genuine** (Toyota Denso low-pressure fuel pump, 1,525,742 units) and its vehicle list carries **`TOYOTA COROLLA 2020`** and no 2021 Corolla — the parenthetical "(2020)" was accurate, the framing was not, and a 2021 buyer was pointed at a campaign they are not in. **`23V865` is genuine and IS the 2021 Corolla's campaign** — occupant-classification software, front passenger airbag may not deploy as intended, **999,901 units**, list includes `TOYOTA COROLLA 2021` — and it was **absent from the page entirely.** Fixed: `23V-865` added as a structured recall row with text drawn from the API record, `stats.recalls` 2 -> 3, summary rewritten to separate the two model years. Ledger `verified` **238 -> 239** (`23V865`, makes `["Toyota","Lexus"]`, API URL as source). **This is the inverse of wave 24's failure mode — not a false claim shipped but a true one missing — and it is the first defect of that kind this study has produced.**

    **`toyota-corolla-2014` escalated, not edited.** It ships `stats.recalls: 5` with **no `recalls` array at all** — zero campaign numbers anywhere in the slug, so there is nothing for a reader or an auditor to check. NHTSA's MY2014 count is 2; the slug spans 2014-2019, so 5 *might* be a generation total; by the site's own displayed-row convention it should read 0. The displayed number is wrong either way, but which number is right depends on what `stats.recalls` is supposed to mean, so it is Daniel's call rather than a guess. Its summary does correctly debunk the Takata-on-this-generation claim.

    **Tranche 3.** (A) and (B) are blocked on the two decisions above. **Runnable now with no network: audit `stats.recalls` against displayed row count across all 245 slugs** — `toyota-corolla-2014` surfaced only because it happened to sit in the gap table, and a slug whose stat is wrong *downward* would never appear there, so one pass closes the class. **Runnable at one query each: the 31 under-citing slugs are a freshness queue**, and tonight shows under-citing can hide a live airbag campaign — order by gap, Silverado (3 vs 20), Cherokee (1 vs 7), Compass (1 vs 6), Sorento (2 vs 8), Malibu (3 vs 9).

    Sibling check: no blocking overlap. Ready blocks 09-09 -> 10-04 all touch `inspect/index.html` or `scripts/recall-ledger.json` and are **ancestors of `main`, not concurrent siblings** — wave 25 (`7a6af33`/`1bed111`) is the direct parent, and tonight consumes its ledger output and extends it by one entry. The 09-09 -> 10-01 vinNote blocks touch `inspect/index.html` but edit `vinNote:` fields only; this diff adds one `recalls` row, changes one `stats.recalls` integer and one `summary` string on a single slug, and the two sets do not intersect. Waves 24-25 edited `recalls` arrays, but on other slugs (`toyota-corolla-2021` was untouched by both) and they are ancestors regardless. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal. **`Started:` audit clean** — every block across In-flight, Ready and Done (last 10) carries a `- Started:` date, 0 missing, so no gate-block risk on the shared files. No Re-sync needed. Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (643 files, exit 0, run against the mounted path; the file count was read, not just the exit code). The 10-05 correction holds and is re-confirmed: the prompt's literal `/Users/...` path exits **2** (python cannot open the script) so a wrong *script* path fails closed; the open gap is still **right script, unresolvable target**, which prints `OK: scanned 0 file(s)` and exits **0**. **Ask unchanged: `scan_for_secrets.py` should exit non-zero when it scans 0 files.** **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory md5 `f8554c34...` before and after, **byte-identical** (85 hrefs); no link added, removed or changed, no `/decode/` link, NHTSA cited as prose only. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-04/10-05 baseline; **G28 passed with the new `23V-865` citation in place because the number was ledgered first**, so the recall-ledger rule was satisfied rather than side-stepped. **CHECKLISTS integrity:** 245 keys before and after, key set identical (verified by evaluating both objects in node, not by regex, per the 10-05 method note). **Menu wiring:** `VEHICLE_MENU` byte-equal before and after, so no route could change. **Line diff: +3 / -2** (18,145 -> 18,146 lines in `inspect/index.html`; 3 lines added are the new `recalls` row, the `summary` string and the `stats.recalls` integer, 2 removed are the prior `summary` and `stats.recalls` lines). **Truncation guard:** ends `</html>`. **Ledger JSON parses; `verified` 238 -> 239, `unverified_legacy` 0 -> 0.** **Commit: `eee03dc`** (parented on wave 25's `1bed111`; tree diff is exactly 3 paths — `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`. `git diff-tree` confirms nothing under `_hub/` entered the tree, and `pinpoint/index.html` was deliberately excluded — its worktree blob equals HEAD and its `MM` status is the stale index noise recorded on 10-03/10-04/10-05.) Built with `GIT_INDEX_FILE=/tmp/ix-final` per the 10-05 note, which sidesteps `index.lock` cleanly; only the ref write still needs doing by hand, because `HEAD.lock` continues to block `update-ref`. This hash line is a one-line follow-up commit, since a commit cannot contain its own hash.

    **PUSH: still blocked. Day 28, 27 commits stuck, `origin/main` still at `0dfa937`.** `GET /user` with the stored PAT returns **401** again, re-tested tonight (prefix `ghp_krkG...`, `expires` still reads 2027-05-19, credentials-file mtime still 2026-05-30 — revoked, not expired). **NHTSA egress unchanged:** `curl` to `api.nhtsa.gov` exits **56** from both shells (cloud proxy: `CONNECT tunnel failed, response 403`); all 14 queries tonight went through the sandbox fetch path, one URL per call. The `.git` locks are still undeletable (`Operation not permitted`, the sandbox deletion block per the 10-04 diagnosis) and the delete-permission prompt was again **not** fired at 02:00. Tonight's commit used the 10-05 workaround — `GIT_INDEX_FILE` to sidestep `index.lock`, ref written directly because `HEAD.lock` still blocks `update-ref`.

    **The deployment gap now has a safety edge worth naming.** The 2021 Corolla fix is live-site-relevant: until `git push origin main` runs with a working PAT, autovetting.com keeps telling 2021 Corolla buyers their only critical check is a 2020 fuel-pump recall and keeps omitting a 999,901-unit airbag campaign that applies to their car — alongside the 36 false citations wave 24 removed and the CX-5 correction from wave 25. One push with a live token fixes 27 vehicle pages.


    2026-10-08 02:00 [scheduled task]: **Tranche 3 ran the no-network audit, and the `stats.recalls` question Daniel was asked on 10-06 is not a one-slug wording problem — it is 245 slugs, and the live label is a claim the site cannot support. Separately, the two worst instances of the class are fixed with verified data: `nissan-altima-2013` and `honda-pilot-2016` went from a recall count with nothing listed to 12 and 8 named, NHTSA-sourced campaigns.**

    **The audit (all 245 slugs, no network, `CHECKLISTS` evaluated out of the HTML per the 10-05 method note).** Before tonight's edits: `stat == displayed rows` on 150 slugs, **mismatched on 95** — 87 over-stating, 8 under-stating. **59 slugs rendered a recall count of 1 or more with zero recall rows on the page**, 4 of them with no `recalls` array at all (`nissan-altima-2013` 6, `toyota-corolla-2014` 5, `honda-pilot-2016` 4, `nissan-altima-2019` 2). A further 99 shipped a count with rows that are **only** the generic `Open recalls — VIN check` row, so no campaign number a reader could check. **Only 59 of 245 slugs carried a single named campaign number.** `toyota-corolla-2014` surfaced on 10-06 because it happened to sit in the gap table; it is one of 59, not an outlier.

    **And the 10-05 "under-citing" column was measuring the wrong field, which corrects a conclusion in this block.** `chevrolet-silverado-2014` was logged as 3-vs-20. It **displays 15 named campaigns**; the 3 is only its `stats.recalls`. Same for `chevrolet-malibu-2016` (stat 3, one generic row). So the under-citing column was the identical counting artifact as the over-citing column 10-06 resolved, read from the other end — the freshness queue built on it (Silverado, Cherokee, Compass, Sorento, Malibu) is **not** a queue of thin content, and three of those five are honest generic-row pages. The real queue is the 57 slugs that show a number against an empty list.

    **The finding that outranks the field definition: the label.** `inspect/index.html:17767-17768` renders this number under **"Open recalls"**. An open recall is one unremedied on a specific VIN — no static page can know that for any car, so the label is wrong on all 245 slugs under *every* candidate meaning of the field (campaign count, displayed-row count, generation total). It also contradicts the site's own standing advice, which is to run the VIN precisely because only NHTSA knows what is open. **Recommendation, which does not need the field definition settled: relabel to "Recalls listed" and make the field equal the displayed row count** (already the convention on 152 of 245 slugs). That is a one-line renderer change plus a derived-value pass, it makes every page self-auditing, and it is honest whatever Daniel decides the number should count. Not applied — it is a copy change on every vehicle page. Escalated.

    **Fixed tonight, with primary sources: the two slugs with the largest unsupported counts.** `nissan-altima-2013` (`stats.recalls` 6, no `recalls` array) now ships **12 named campaigns** from `recallsByVehicle?make=nissan&model=altima&modelYear=2013` (Count 12). The editorial find is a cascade: **four separate secondary-hood-latch campaigns re-opened and re-scoped over six years** — `14V-565` (2013) → `15V-116` (2013-2015) → `16V-029` (2013-2015) → `20V-315`, which covers **all 2013-2018 Altimas, 1,831,818 units**, owner letters June 2021, confirmed by `campaignNumber=20V315000`. A closed earlier wave does not clear the later ones, and that is now stated on the page. Five more are front-passenger occupant-classification campaigns (`13V-069`, `14V-138`, `15V-681`, `16V-244`, `16V-911`) that can switch the passenger airbag off. `stats.recalls` 6 → 12 (= displayed rows). `honda-pilot-2016` (stat 4, no array) now ships **8** from `recallsByVehicle` (Count 8), including **two separate fuel-tank replacements** (`16V-417` and the Pilot-specific `17V-219`, so a closed 16V-417 does not clear 17V-219), `23V-751` connecting-rod-bearing engine seizure — 248,999 units, scope confirmed by `campaignNumber=23V751000` as 2016 + 2018-2019 Pilot with **the 2017 car not in it** — and `26V-365`, opened **2026-04-06**, 880,514 units, rear subframe corrosion limited to 22 salt-belt states plus DC, scope confirmed by `campaignNumber=26V365000`. stat 4 → 8. One summary sentence added to each slug naming the pattern; both summaries previously mentioned no recall at all.

    **One self-caught attribution error, which is the 10-04 lesson working.** The first draft of the `23V-858` row repeated NHTSA's own wording that it expands `20V-314` and `21V-215`. `campaignNumber=20V314000` was then checked: 135,995 units across Accord/Civic/Fit/HR-V/Insight/NSX/RDX/RLX and **no Pilot**. True of the campaign chain, misleading on a Pilot page, so the numbers were removed from the prose rather than ledgered — the point of G28 is not to let a real number imply a scope it does not have.

    **Ledger: `verified` 239 → 257**, 18 new numbers, each with its `campaignNumber` API URL as source and makes recorded. `16V-244` and `23V-858` were already verified and were reused, not re-added. `20V-314` deliberately **not** added. `unverified_legacy` 0 → 0. Unledgered-number sweep across `inspect/index.html`, `index.html` and `pinpoint/index.html`: **NONE**.

    Sibling check: no blocking overlap, nothing to re-sync. Tracked files touched: `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`. `pinpoint/index.html` untouched and clean in `git status` this run (the `MM` index noise logged 10-03 → 10-06 no longer shows against explicit paths). Ready blocks 09-09 → 10-06 all touch `inspect/index.html` or `scripts/recall-ledger.json` and are **ancestors of `main`, not concurrent siblings**; `eee03dc`/`e69c8ed` (wave-25 follow-on, 2021 Corolla) is the direct parent and tonight extends its ledger. The vinNote blocks edit `vinNote:` fields only; tonight adds two `recalls` arrays, changes two `stats.recalls` integers and two `summary` strings on two slugs — disjoint from every one of them, and neither slug was touched by waves 24, 25 or the 10-06 Corolla fix. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal. **`Started:` audit clean — 31 blocks across In-flight, Ready and Done (last 10), 0 missing.** Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (650 files, exit 0, file count read not just the exit code). The two-failure distinction holds a third run: the prompt-literal `/Users/...` path exits **2** (python cannot open the script — fails closed, correct), while **right script, unresolvable target** still prints `OK: scanned 0 file(s)` and exits **0**. **Ask unchanged: `scan_for_secrets.py` should exit non-zero when it scans 0 files.** **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0, run after each of the two edit passes). **Dead-links: verified** — `href` inventory md5 `f8554c34…` **byte-identical** to the 10-06 baseline, 85 hrefs, no link added or changed, no `/decode/` link; NHTSA cited as prose and campaign numbers only. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-04/10-05/10-06 baseline, the one warn still the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`; **G28 passed with 18 new citations because every number was ledgered before it shipped.** **CHECKLISTS integrity:** 245 keys before and after, key *sequence* identical, verified by evaluating both the HEAD blob and the worktree file in node. **`VEHICLE_MENU` byte-identical**, so no route could change. **Truncation guard:** ends `</html>`. **Ledger JSON parses.**

    **Post-edit audit for the record:** `stat == displayed rows` now 152 of 245; mismatched 93 (85 over, 8 under); slugs with a count and zero rows **59 → 57**; slugs with at least one named campaign **59 → 61**; slugs with no `recalls` array at all **4 → 2** (`toyota-corolla-2014`, held for Daniel since 10-06, and `nissan-altima-2019`).

    **Commit: `5432c3f`** (parented on `e69c8ed`; `git diff-tree` confirms the tree is exactly three paths — `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md` — and that nothing under `_hub/` entered it. Worktree == HEAD verified by `git show | cmp` on all three. Built with `GIT_INDEX_FILE=/tmp/ix-1008` per the 10-05 note.) **PUSH: refused, Day 29, 29 commits stuck, `origin/main` still at `0dfa937`.** `GET /user` with the stored PAT returns **401** again (prefix `ghp_krkG...`, `expires` still reads 2027-05-19, credentials-file mtime still 2026-05-30 — revoked, not expired). No `git push` was attempted: with no usable credential the only way to make one succeed is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans outright. **Lock state improved, which is new.** `refs/heads/main.lock` held `15010b3` — an orphan from the 09-16 run, now an ancestor of HEAD, so obsolete — and `HEAD.lock` was a 0-byte file from 09-15. Both were moved aside (not deleted; deletion is still `Operation not permitted` and no interactive grant fires at 02:00) to `.git/stale-main-lock-20260916` and `.git/stale-HEAD-lock-20260915`, after confirming no git process was running. **`git update-ref` then worked normally for the first time since 09-16, so the hand-built ref write is no longer needed** — only the stale-lock move is. The `MM` index status on the three files is the usual `GIT_INDEX_FILE` artifact, not a worktree difference.

    **Next run.** The 57-slug queue is the work, and it is ordered by claimed count with nothing to show: `ford-bronco-2021` (6), `jeep-wrangler-4xe-2021` (5), `ford-f150-lightning-2022` (5), `honda-odyssey-2018` (4), `rivian-r1t-2022` (4), `ford-mustang-mach-e-2021` (4). One `recallsByVehicle` call each, 2-3 slugs a night at tonight's rate. `nissan-altima-2019` and `toyota-corolla-2014` are the two with no array left and both are cheap once Daniel answers, but **neither answer is needed to keep draining the queue** — adding verified rows is correct under every candidate definition. Do **not** rebuild the 10-05 gap table against `stats.recalls`; it measures the stat, not the content.
    2026-10-09 02:00 [scheduled task]: **the 57-slug queue was two defects wearing one number, and the larger one was a key-name mismatch, not missing content. 29 vehicle pages were rendering `undefined / undefined / undefined` under the heading "NHTSA Recalls (verify completion via VIN)" — 31 rows across 29 slugs, all fixed tonight. `ford-bronco-2021` additionally went from nothing readable to 20 named, ledgered campaigns.**

    **The defect.** `renderChecklist` reads `r.number`, `r.title`, `r.desc` (`inspect/index.html:17838-17840`). Thirty-one recall rows were authored in a second, older shape — `{campaign, description, severity, remedy}` — so every one of their three fields interpolated as the string `undefined` into live HTML. Verified by evaluating the template against `CHECKLISTS`, not by reading it: `ford-bronco-2021` produced `<number>undefined</number><title>undefined</title><desc>undefined</desc>` twice. The content was never missing — all 31 rows carry full, legible prose, including one real campaign number (`22V-412` on `ford-mustang-mach-e-2021`, already ledgered) and `19V-434` on `audi-e-tron-2019`. Nothing was researched to fix this; it is a rename.

    **It also explains the 10-08 queue, and corrects its ordering.** 10-08 reported "57 slugs showing a number against an empty list" and headed the next-run queue with `ford-bronco-2021` (6), `jeep-wrangler-4xe-2021` (5), `ford-f150-lightning-2022` (5), `rivian-r1t-2022` (4), `ford-mustang-mach-e-2021` (4). None of those five is in the 57 — each has a non-empty `recalls` array whose rows did not render. Two populations were being counted as one. Measured on the HEAD blob: **stat > 0 with an empty array = 57; stat > 0 with nothing that renders = 86.** Tonight closes the 29-slug gap between those two numbers: **86 → 57.** The 57 is untouched and is still the real content queue, correctly ordered now: `toyota-corolla-2014` (5), `ford-f250-2019` (3), then fourteen slugs at 2 (`gmc-terrain-2018`, `nissan-titan-2017`, `volvo-xc40-2019`, `chevrolet-silverado-2022`, `gmc-sierra-2022`, `bmw-x7-2019`, `cadillac-escalade-2021`, `audi-q7-2018` …). `honda-odyssey-2018`, also on the 10-08 queue, is in neither set — it ships a well-formed generic row.

    **Normalized the data, did not make the renderer tolerant.** A `r.number || r.campaign` fallback would have fixed all 29 pages in one line and kept two schemas alive to drift again. All 31 rows were rewritten to the single canonical shape instead: `campaign` → `number`, `severity` → `title` (as `Severity: <level>`), `description` + `remedy` → `desc`. No fact added, none dropped; the rewrite was done by evaluating each object literal in node and re-emitting it, never by retyping prose. **No gate was added** — the mismatch is invisible to every current check, including G28, which regex-matches campaign numbers against raw file text and so never noticed that `22V-412` was sitting in a field the page cannot print. A one-line G29 (`every row in every recalls array has number/title/desc`) would make this class unshippable. Proposed in Awaiting-Daniel, not built: new gates need Daniel.

    **`ford-bronco-2021`: 0 readable rows → 20 named campaigns, with the editorial find being a cascade.** `recallsByVehicle?make=ford&model=bronco&modelYear=2021` returns **Count 20**; the campaign list was pulled twice on independent fetches and came back identical in content and order before anything was written. **Seven of the twenty are the same rearview-camera defect, reopened across four years** — `22V-825` → `23V-165` → `23V-598` → `25V-315` → `25V-312` → `25V-888` → `26V-124` (the last opened 2026, APIM overheat) — so "the camera recall was done" is not an answer on this truck, and each row now says which of the seven it is. The two that cost money: `24V-635`, 2.7L EcoBoost intake-valve fracture causing engine failure, which makes the 8th-digit `P` read on this slug's existing `vinNote` a cost question and not trivia; and `26V-299`, roof-and-pillars, which **is** the campaign behind the unnumbered "MIC Hardtop" row this page had been shipping since before the ledger existed. `stats.recalls` 6 → 20 (= displayed rows, the 10-08 convention). Summary rewritten to name the cascade and both expensive campaigns; it previously named no campaign at all.

    **Ledger: `verified` 257 → 277**, 20 new numbers, none previously present, `unverified_legacy` 0 → 0. **Source recorded is the `recallsByVehicle` year/make/model query rather than `campaignNumber`** — a deliberate choice, flagged here because it departs from the file's recent convention: the ledger `_doc`'s own CAUTION is that membership proves a campaign exists and never that it belongs on the vehicle citing it, and `recallsByVehicle` is the endpoint that answers the second question. Both are the NHTSA API, which is what SECRETS-POLICY-era ledger rule requires. If Daniel wants `campaignNumber` URLs on these 20 as well, that is one run.

    Sibling check: no blocking overlap, nothing to re-sync. Tracked files touched: `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`. `pinpoint/index.html` untouched. Every Ready block 09-09 → 10-06 that touches `inspect/index.html` or `scripts/recall-ledger.json` is an ancestor of `main`, not a concurrent sibling; `5432c3f`/`484f5f4` (10-08 Altima + Pilot) is the direct parent and tonight extends the same ledger and the same renderer contract. The vinNote blocks edit `vinNote:` only — disjoint from the 31 rows rewritten here, and no slug touched tonight was touched by waves 24/25, the 10-06 Corolla fix or the 10-08 pair. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal. **`Started:` audit clean — 31 blocks across In-flight, Ready and Done (last 10), 0 missing.** Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (652 files, exit 0, file count read and not just the exit code — the standing ask that `scan_for_secrets.py` exit non-zero when it scans 0 files is unchanged). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0; run after each edit pass — the first pass of the summary rewrite put a double-quoted phrase inside a double-quoted string and node caught it before anything was committed, which is the hazard the task prompt names). **Dead-links: verified** — `href` inventory md5 `174faa1f…`, **byte-identical to the HEAD blob**, 18 distinct internal paths, no link added or changed, no `/decode/` link; NHTSA cited as prose and campaign numbers only. **Deploy gate: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-04 → 10-08 baseline, the one warn still the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`; **G28 passed with 20 new citations because all 20 were ledgered before they shipped.** **CHECKLISTS integrity:** 245 keys before and after, key *sequence* identical, verified by evaluating both the HEAD blob and the worktree file in node. **`VEHICLE_MENU` byte-identical** (146,131 bytes), so no route could change. **Truncation guard:** ends `</html>`. **Ledger JSON reparses**, diff vs HEAD is +180/-1 — a clean append, no reformat. **Post-fix audit:** rows rendering `undefined` **31 → 0**; slugs with at least one named campaign **61 → 64**; `stat == displayed rows` 153; recall rows total 393 → 411.

    **Commit: `dcfb965`.** **PUSH: refused, Day 30, 30 commits stuck, `origin/main` still at `0dfa937`.** `GET /user` with the stored PAT returns **401** (prefix `ghp_krkG...`, `expires` still reads 2027-05-19, credentials file untouched since 2026-05-30 — revoked, not expired). No `git push` was attempted: with no usable credential the only way to make one succeed is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. A fresh `.git/HEAD.lock` (0 bytes, dated 10-08) and an `.git/index.lock` created by this run's own `git diff` were moved aside to `.git/stale-HEAD-lock-20261009` and `.git/stale-index-lock-20261009` rather than deleted — deletion in the mount is still `Operation not permitted` and no interactive grant fires at 02:00. **Correction to the 10-09 catalog-task finding:** the credentials file *is* readable from the mount, at `~/mnt/Claude/.credentials/github-config.json`; that task reported it absent because it looked for the literal `/Users/...` path, which does not exist inside the device shell. The blocker is the token's validity, not its reachability.

    **Next run.** Drain the 57-slug queue in the corrected order above, `toyota-corolla-2014` first (it is also the slug held for Daniel since 10-06 — but adding verified rows is correct under every candidate definition of the field, so it does not need his answer). Two or three slugs a night at tonight's rate. Do **not** rebuild the gap table against `stats.recalls`, and do **not** treat the 10-08 queue list as the queue — five of its six entries were undefined-row slugs, fixed tonight.

    2026-10-10 02:00 [scheduled task]: **Three slugs drained off the 57-slug queue — `toyota-corolla-2014`, `ford-f250-2019`, `gmc-terrain-2018` — 11 campaign numbers added, every one returned by NHTSA for that exact vehicle before it was written and ledgered before it shipped. Queue 57 → 54. Slugs carrying at least one named campaign 64 → 67. Rows that render as `undefined`: 0 before, 0 after.**

    **Method, unchanged from 10-09 and deliberately so.** One `recallsByVehicle?make=&model=&modelYear=` query per slug through the sandbox fetch path (`curl` to `api.nhtsa.gov` still exits 56 from both shells — re-tested tonight). `recallsByVehicle` is the endpoint that answers the question the ledger `_doc` cares about: not "does this campaign exist" but "does it belong on the car citing it". Rows were written in the canonical `{number, title, desc}` shape only — the schema the renderer reads at `inspect/index.html:17860-17862` — so none of tonight's 11 can repeat the 10-09 key-name defect. **Second source on the three numbers whose value is their narrow scope:** `13V-505`, `20V-576` and `18V-340` were each re-queried through `campaignNumber`, which confirmed 13V-505 reaches the 2014 Corolla (with the 2013-2014 Camry and 2013 Avalon), 20V-576 is **4x4 only** (F-250/F-350, SRW and DRW), and 18V-340 is **certain 2018 GMC Terrain only**. Those three constraints are the content, so they were not taken on one fetch.

    **`toyota-corolla-2014` (stat 5, no `recalls` array at all) now ships 2 named campaigns, and the 10-06 hold is moot for this slug.** NHTSA returns 2 for MY2014: **`13V-505`** wiper-switch short circuit, which disables the wipers and is an FMVSS 104 failure, **2014 only** — it does not reach the 2015-2019 cars this slug also covers; and **`20V-024`**, the airbag-ECU noise campaign covering **2011-2019 Corolla**, i.e. every year on this page. The generation span is handled in the row text rather than by splitting the slug. `stats.recalls` 5 → 2, the displayed-row convention 10-09 applied to the Bronco. **What that does and does not settle:** the slug now shows a number that matches what a reader can count, so the page is no longer self-contradicting and does not need Daniel's answer to be correct. The definition question he was asked on 10-06 is still open for the 85 slugs that over-state, and the generation-union count for 2014-2019 Corolla is still **unmeasured** — it would take five more model-year queries, and nothing tonight assumes it is 2.

    **`ford-f250-2019`: 4 campaigns, and two of them are this-truck-specific rather than Super-Duty-wide.** `20V-576` front-axle wheel-end yoke possibly not welded to the axle tube (2019 F-250/F-350 **4x4**) and `19V-688` passenger-side rear axle shaft fracture on **electronic-locking-differential** trucks — a broken shaft means the truck cannot be held in Park and can roll away if the parking brake is not set. Plus `18V-894` block-heater cable corrosion/fire (2017-2019 Super Duty) and `19V-633` manual seat-recliner missing a third pawl (2019-2020 Super Duty). **The editorial find is `18V-894`'s two-stage remedy:** dealers first *disabled* the cable and only later replaced it, so a Super Duty whose block heater simply does not work may be parked at the interim fix rather than the finished one — that is in the row, because it is the kind of thing a buyer reads as a dead accessory. `stats.recalls` 3 → 4.

    **`gmc-terrain-2018`: 5 campaigns, three of them multi-model GM, and the ledger says only what was verified.** `17V-516` right-front intermediate driveshaft fracture/separation (2018 Terrain, 2018 Equinox, 2017-2018 Acadia), `18V-358` high-pressure fuel pump detaching and damaging the HP fuel line, `18V-340` airbag sensing module failing to power down and inoperative at restart (**2018 Terrain specifically**), `18V-576` rear caliper piston coating cutting rear braking, `20V-668` start/stop accumulator endcap missing bolts. For `18V-358`, `18V-576` and `20V-668` the API says "several GM models" without enumerating them, so `makes` was recorded as `["GMC"]` with the component note stating the Terrain was confirmed in scope by `recallsByVehicle` — **the full GM make list was not inferred.** That is the 08-03 / 10-04 failure mode (a hedge hardening into a confident record) and the cheapest place to not repeat it is here. `stats.recalls` 2 → 5.

    **Ledger: `verified` 277 → 288**, 11 new numbers, none previously present (checked in both hyphenated and unhyphenated form), `unverified_legacy` 0 → 0. Diff is **+90/-0** — a clean append, no reformat.

    **Record fix, worth one line because it would have compounded.** Last night's 10-09 note had been appended directly under the bare `## Ready to deploy / publish` header — no `###` block, no `Started:`, detached from the in-flight block where 10-05, 10-06 and 10-08 of this same workstream live. Moved verbatim into this block's Notes, nothing reworded. Nothing in the Ready section lost a block; the note never had one.

    Sibling check: no blocking overlap, nothing to re-sync. Tracked files touched: `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`. `pinpoint/index.html` untouched (its `MM` status is the documented stale-index noise; worktree blob equals HEAD, verified by `hash-object`). Every Ready and Done block that touches `inspect/index.html` or `scripts/recall-ledger.json` is an ancestor of `main`, not a concurrent sibling — `dcfb965` / `945d24f` (10-09) is the direct parent and tonight extends the same renderer contract and the same ledger. The vinNote blocks touch `vinNote:` only, disjoint from the three `recalls` arrays and three `stats.recalls` integers changed here; none of the three slugs was touched by waves 24/25 or by the 10-08 pair. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal. **`Started:` audit clean — 31 blocks across In-flight, Ready and Done (last 10), 0 missing.** Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (654 files, exit 0 — run against the mounted path, and the file count was read and not just the exit code; the standing ask that `scan_for_secrets.py` exit non-zero when it scans 0 files is unchanged). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory md5 `f8554c34…`, **byte-identical to the HEAD blob**, 18 distinct internal paths, no link added or changed, no `/decode/` link; NHTSA cited as campaign numbers and prose only. **Deploy gate: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-03 → 10-09 baseline, the one warn still the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`; **G28 passed with 11 new citations because all 11 were ledgered before they shipped.** **CHECKLISTS integrity:** 245 keys before and after, key *sequence* identical, verified by evaluating both the HEAD blob and the worktree file in node. **`VEHICLE_MENU` md5 `0f8605e7…` before and after**, byte-equal, so no route could change. **Truncation guard:** ends `</html>`. **Ledger JSON reparses.** `inspect/index.html` diff vs HEAD **+42/-5** (18,188 → 18,225 lines). **Post-edit audit:** queue (stat > 0, empty array) **57 → 54**; slugs with a named campaign **64 → 67**; `stat == displayed rows` **153 → 156**; recall rows total **411 → 422**; rows rendering `undefined` **0 → 0**.

    **Commit: `da51f74`.** **PUSH: refused, Day 31.** `GET /user` with the stored PAT returns **401** again (prefix `ghp_krkG...`, file untouched since 2026-05-30, `expires` still reads 2027-05-19 — revoked, not expired). No `git push` was attempted: the only way to make one succeed without a valid credential is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. `git add` succeeded despite `unable to unlink '.git/objects/**/tmp_obj_*': Operation not permitted` warnings — the documented FUSE delete block, harmless to correctness, and no new `.lock` had to be parked tonight.

    **Next run.** Keep draining the queue, now 54, in the same order — the fourteen slugs claiming 2: `nissan-titan-2017`, `volvo-xc40-2019`, `chevrolet-silverado-2022`, `gmc-sierra-2022`, `bmw-x7-2019`, `cadillac-escalade-2021`, `audi-q7-2018`, `porsche-cayenne-2019`, `porsche-macan-2017`, `ram-2500-2019`, `tesla-model-y-2022`, `chevrolet-tahoe-2021`, `gmc-yukon-2021`, `land-rover-defender-2020`, `nissan-altima-2019` — then the thirty-eight at 1. Three slugs a night at tonight's rate. Second-source via `campaignNumber` only the numbers whose scope is the claim (year-specific or trim/drivetrain-specific); a model-year query is sufficient for the rest.

    2026-10-11 02:00 [scheduled task]: **three more slugs off the recall-content queue — `nissan-titan-2017`, `volvo-xc40-2019`, `chevrolet-silverado-2022`. 13 campaign numbers added, every one returned by `recallsByVehicle` for that exact vehicle before it was written and ledgered before it shipped. Queue 54 → 51.** `stats.recalls` corrected to match countable rows on all three: Titan **2 → 3**, XC40 **2 → 4**, Silverado 1500 **2 → 6** — every one of the three was *under*-stating, the opposite direction from the 10-06 over-statement hold, which is worth recording because it means the 85-slug stat question is not one-directional.

    **The near-miss worth the most tonight: `22V-827` was checked and deliberately NOT shipped.** The 22V-903 daytime-running-light row initially carried the clause "expands the earlier 22V-827", lifted straight from the NHTSA summary. The deploy gate caught it — G28 pattern-matches campaign numbers out of the raw file text, so a number appearing only in prose is a shipped citation as far as the gate is concerned. Rather than ledger it to clear the gate, I queried `campaignNumber?campaignNumber=22V827000`: **it covers MY2021 Escalade / Escalade ESV / Suburban / Tahoe / Yukon / Yukon XL and does not include the 2022 Silverado 1500 at all.** Ledgering it would have put a number on a truck it does not belong to — the exact 10-03/10-04 failure mode — so the clause was removed instead. The expansion relationship is NHTSA bookkeeping and carries nothing a buyer can act on. **G28 earned its keep as a prose check, not just a row check.**

    **`nissan-titan-2017`: 3 campaigns, and two of the three turn on something other than the year.** `19V-495` alternator harness damaged at engine installation → short, engine stall, fire risk — **2017-2019 gasoline light-duty Titan only, not the Cummins Titan XD**, which dovetails exactly with the vinNote already on that page (Nissan encodes this powertrain in the **4th** VIN digit, not the 8th: `A` = 5.6L VK56VD gas, `B` = 5.0L Cummins). The 4th digit therefore decides whether this campaign can apply at all. `17V-268` rear seat-belt D-ring bolt trim-cap head-impact (FMVSS 201) is **Crew Cab only** — King Cab and Single Cab trucks are outside scope, so this one turns on body style. Both second-sourced via `campaignNumber`. `18V-240` is the quiet one: accessories cut load capacity and the FMVSS 110 modification label was never applied — a label-only remedy, but it means **the door-jamb payload figure can overstate what the truck may legally carry**, which is the kind of thing a buyer towing at the limit should know.

    **`volvo-xc40-2019`: 4 campaigns, and one is a stop-driving order.** `18V-554` — brake pedals possibly not riveted correctly, pedal can move out of position and reduce braking; **Volvo told owners to stop driving and had cars inspected where they sat or towed in.** Estimated **71 vehicles**, so most XC40s will never have been in it, but it is the only stop-drive order on this car and it has to read closed by VIN. Second-sourced via `campaignNumber`. `18V-535` rear seat back missing its lock strikers is checkable by hand with the seat folded and latched, which is rare for a recall and is said so in the row. `20V-144` (AEB may not detect or engage) and `18V-800` (connectivity module sends no GPS to emergency responders after a crash) are both multi-model Volvo software campaigns; **the ledger records `makes: ["Volvo"]` with a note that the 2019 XC40 was confirmed in scope by `recallsByVehicle` — the full Volvo line list was deliberately not inferred**, same discipline as the 10-10 GM entries.

    **`chevrolet-silverado-2022`: 6 campaigns, and the top two are the most expensive and the most misleading rows this queue has produced.** `25V-274` — connecting-rod and/or crankshaft manufacturing defects on the **6.2L V8 only** (2021-2024), engine damage and failure; dealer inspects and repairs or replaces, and trucks that *pass* get higher-viscosity oil, a new filler cap and a new filter. On a 6.2L truck this is an engine, and it is the single costliest item anywhere in the library; 5.3L and 3.0L trucks are not in scope, so the engine decides it. Second-sourced via `campaignNumber`. Then the pair: `24V-797` transmission control valve can fail and **lock the rear wheels**, **diesel-engine trucks only** — and `26V-083`, which exists because **trucks repaired under 24V-797 may have been repaired incorrectly**, leaving the same wheel-lock failure live. **So "the transmission recall was done" answers 24V-797 and not 26V-083, and both have to read closed** — a second instance of the two-stage-remedy pattern found on the F-250's block heater on 10-10, and it now looks like a class worth watching rather than a one-off. `26V-083` VINs became searchable 2026-02-12 with letters 2026-03-06, so a truck sold before that will not have had it. `22V-463` only applies if the truck actually carries the accessory sport bar, which is visible from the bed. `22V-873` (airbag module shipped in manufacturing mode) was **remedied pre-sale at the GM plant with no owner letters mailed** — it is listed so a used buyer recognises it as already settled instead of chasing it, which is the honest handling of a record that is in scope but closed.

    **Ledger: `verified` 288 → 301**, 13 new numbers, none previously present, `unverified_legacy` 0 → 0. Diff **+104/-0**, a clean append. One process note: the 13 entries were first written with **hyphenated keys** (`19V-495`) and G28 CRITICAL-failed on all 13, because the gate strips the hyphen from the HTML number and compares against the ledger key **as stored** — the stored form must be unhyphenated. Caught, rekeyed, and the whole `verified` map was rebuilt from the HEAD blob with the 13 appended in order so the diff stayed a clean append rather than a 1,626-line reorder. **Incidental find, not fixed:** one legacy entry, **`23V093`, is stored as a bare string rather than an object**, so it carries no `source` or `verified` field and satisfies G28 on key membership alone. It is the only one of 301. Flagged rather than changed — the ledger's entry schema is not mine to alter.

    Sibling check: no blocking overlap, nothing to re-sync. Tracked files touched: `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`. Every Ready and Done block touching `inspect/index.html` or `scripts/recall-ledger.json` is an ancestor of `main`, not a concurrent sibling — `da51f74` / `b0a0a4c` (10-10) is the direct parent and tonight extends the same renderer contract and the same ledger. None of the three slugs was touched by waves 24/25, by the 10-08 pair, by the 10-09 key-name fix or by the 10-10 batch; the vinnote blocks touch `vinNote:` only, disjoint from the three `recalls` arrays and three `stats.recalls` integers changed here. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal. **`Started:` audit clean — 31 blocks across In-flight, Ready and Done (last 10), 0 missing.** Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (656 files, exit 0 — count read, not just the exit code; 655 last night plus one untracked stray, see below). **Syntax-check: PASS** (Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory md5 `f8554c34…`, **byte-identical to the HEAD blob**, no link added or changed. **Deploy gate: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-03 → 10-10 baseline, the one warn still the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`; **G28 passed with 13 new citations, after first failing and being right to.** **CHECKLISTS integrity:** 245 keys before and after. **`VEHICLE_MENU` md5 `1e723e3d…` byte-equal** to HEAD, so no route could change. **Truncation guard:** ends `</html>`. **Ledger JSON reparses** (301 verified). `inspect/index.html` diff vs HEAD **+22/-6**. **Post-edit audit:** queue (stat > 0, empty array) **54 → 51**; `stat == displayed rows` **134 → 137** on a like-for-like recount of the same metric against the HEAD blob (last night's "156" was computed over a wider denominator — the figure moved +3, which is the claim that matters); rows missing `number`/`title`/`desc` **0 → 0**, so nothing tonight can repeat the 10-09 `undefined` defect.

    **Commit: `5926608`.** **PUSH: refused, Day 32.** `GET /user` with the stored PAT returns **401** (prefix `ghp_krkG...`, credentials file untouched since 2026-05-30, `expires` still reads 2027-05-19 — revoked, not expired). No `git push` attempted: the only way to make one succeed without a valid credential is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. **35 commits now stuck**, `origin/main` still at `0dfa937`.

    **Two housekeeping items, both cheap and both getting worse slowly.** (1) The stale-lock tax is compounding: tonight both `.git/index.lock` **and** `.git/HEAD.lock` (dated 10-10 09:22) had to be parked under new names before `commit` would run, and `.git/` now holds **several hundred** zero-byte `HEAD.lock.*` corpses going back to 2026-05-27 plus a growing litter of un-unlinkable `.git/objects/**/tmp_obj_*`. Each is harmless alone; together they are the reason a commit costs two extra steps a night. The root cause is that the mounted folder does not permit deletion, so git cannot clean up after itself. (2) An **empty untracked file** sits in the repo root with a newline in its name (`,b.C[c].recalls.map(...)` — a heredoc mishap from an earlier run). It is why the scanner now counts 656 rather than 655. It cannot be deleted for the same reason, and the risk is that a future `git add -A` stages it; tonight's commit used explicit paths. Neither is a blocker and neither was escalated as a decision.

    **Next run.** Keep draining the queue, now **51**, in the same order — the twelve slugs still claiming 2: `gmc-sierra-2022`, `bmw-x7-2019`, `cadillac-escalade-2021`, `audi-q7-2018`, `porsche-macan-2017`, `tesla-model-y-2022`, `chevrolet-tahoe-2021`, `gmc-yukon-2021`, `land-rover-defender-2020`, `ram-2500-2019`, `porsche-cayenne-2019`, `nissan-altima-2019` — then the thirty-nine at 1. Three a night at tonight's rate. `gmc-sierra-2022` is next and will overlap heavily with tonight's Silverado (`25V-274`, `24V-797`, `26V-083`, `22V-903`, `22V-463` are all multi-make GM campaigns already ledgered), so expect it to be cheap — but **query `recallsByVehicle` for the Sierra itself rather than reusing the Silverado result**, because membership in `verified` proves a campaign exists and never that it belongs on the vehicle citing it. Second-source via `campaignNumber` only where scope is the claim.


    2026-10-12 02:00 [scheduled task]: **three more slugs off the recall-content queue — `gmc-sierra-2022`, `bmw-x7-2019`, `cadillac-escalade-2021`. 26 campaign numbers added, every one returned by `recallsByVehicle` for that exact vehicle before it was written and ledgered before it shipped. Queue 51 → 48.** `stats.recalls` corrected to match countable rows on all three: Sierra 1500 **2 → 6**, X7 **2 → 11**, Escalade **2 → 9** — all three *under*-stating, same direction as 10-11. Ledger `verified` **301 → 320** (19 new keys; 7 of the 26 rows cite campaigns already ledgered from the 10-11 Silverado batch). `stat == displayed rows` **159 → 162** like-for-like against the HEAD blob; rows missing `number`/`title`/`desc` **0 before, 0 after**.

    **`22V-827` closes the loop on the 10-11 near-miss.** Last night the `22V-903` row was about to carry NHTSA's own clause "expands the earlier 22V-827", G28 CRITICAL-failed on the bare number in prose, and rather than ledger it to clear the gate it was queried: it covers MY2021 Escalade / Escalade ESV / Suburban / Tahoe / Yukon / Yukon XL and **not** the 2022 Silverado 1500. Tonight the 2021 Escalade is the vehicle on the bench and `22V-827` is **in scope** — now a ledgered, cited row on the page it actually belongs to, with the 10-11 exclusion recorded in its own ledger `component` note so a later audit does not read the two as contradicting. The Sierra's `22V-903` row shipped **without** the expansion clause, same as the Silverado: accurate at NHTSA, misleading on a truck that is not in the campaign it points at.

    **The two-stage-remedy pattern is now a class, not a coincidence — four instances in three nights across three manufacturers.** `24V-576` → `25V-644` (X7): BMW remedied the starter-overheat fire risk in Aug 2024 with a **software update**, concluded in Sep 2025 that software was not enough, and opened a second campaign that **replaces the starter** and explicitly includes cars already repaired under the first (145,102 vehicles, owner letters 2026-02-09). So an X7 whose history shows "starter recall — completed" is showing the wrong one; both rows ship and the `25V-644` row says so outright. `24V-797` → `26V-083` (Sierra) is the same shape carried over from the Silverado. Prior: F-250 block heater (10-10), Silverado transmission (10-11). **Content implication worth its own asset: a completed recall is not the same as a closed VIN**, because a manufacturer can re-open the same defect under a new number while the old row still reads "remedy available — completed."

    **Editorial findings.** *Sierra 1500 2022* — one of six campaigns is actually Sierra-specific: `25V-060` (chrome grille deflector attachments fracture, deflector detaches, 70,768 trucks) is the only one whose campaign record lists a single make/model/year; the other five are shared GM full-size, which is why last night's Silverado work made tonight cheap. Each was still queried against the Sierra itself, and **the rule paid for itself immediately** — `22V-873` (airbag module left in manufacturing mode) is on the Silverado and is **not** returned for the Sierra, so it was not carried across, while `25V-060` is on the Sierra and was never on the Silverado. Membership in `verified` proves a campaign exists, never that it belongs on the vehicle citing it. *Escalade 2021* — the existing `vinNote` (`L` = 6.2L L87 V8, `T` = 3.0L LM2 Duramax) **partitions the two costliest campaigns exactly**: `25V-274` (connecting-rod/crankshaft → engine replacement) is 6.2L gas only, `24V-797` (control valve → rear wheels lock) is diesel only, and no Escalade is in both; both rows now name the digit that puts the car in scope. Cleanest case in the library of a vinNote and a recall row answering the same question — and an argument for reading the vinNote *before* writing recall rows. Also two **separate** third-row seat-belt campaigns (`21V-190` pinched/misrouted webbing, `22V-617` malformed buckle rivet), so "the seat-belt recall was done" is an incomplete answer; and `25V-619` is a **service-history** defect rather than a build defect — an earlier tank replacement may have fitted the wrong tank, 12 vehicles campaign-wide, but the population is "diesel Escalades that have had tank work done", which a buyer can identify from records. *X7 2019* — two of eleven turn on an option rather than the year (`19V-135` business-lounge seat only, unsold cars quarantined at the time; `19V-541` X5 xDrive50i + X7 xDrive40i with **5 vehicles** campaign-wide), and three are FMVSS software (`21V-096`/`19V-684` both FMVSS 111 reverse-camera, different mechanisms; `22V-267` FMVSS 118 sunroof-with-no-fob). `19V-684` is the test-drive line: a blank reverse screen is a software question before it is a camera question, because the previous owner may have set it that way.

    **Method.** One `recallsByVehicle` query per slug through the sandbox fetch path; `curl` to `api.nhtsa.gov` still fails from both shells (re-tested — cloud proxy `CONNECT tunnel failed, 403 / connect_rejected, organization policy`). Rows authored in the canonical `{number, title, desc}` shape only. **Second-sourced via `campaignNumber`** the five numbers whose value is their scope: `25V-060`, `22V-827`, `25V-644`, `19V-541`, `25V-619`. Multi-model campaigns record `makes` as the queried make only with a component note that the slug's vehicle was confirmed in scope by `recallsByVehicle`; the full make list was deliberately **not** inferred. Ledger keys written unhyphenated from the start (10-11 lesson held) and appended by text insertion ahead of the `verified` closing brace, so the diff is **+152/-0** and the file reparses. Carried forward unfixed, both pre-existing: `23V093` is still a bare string rather than an object and satisfies G28 on key membership alone (1 of 320), and the empty untracked file with a newline in its name is still in the repo root — tonight's commits used explicit paths so it was not staged. `.git/HEAD.lock` (10-10 09:22) had to be parked under a new name again; the mount still forbids deletion so git cannot clean up after itself.

    Sibling check: no blocking overlap, nothing to re-sync. Touched `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md` and the gitignored `_hub/Build-Log/2026-10-12.md`. Every Ready block that shares `inspect/index.html` or `scripts/recall-ledger.json` (recall-audit waves 24-25, vinnote batches 09-09 → 10-01, menu sweeps) is an **ancestor of `main`**, not a concurrent sibling — this run is a descendant of the 10-11 batch (`5926608`) and consumes its ledger output additively, appending keys without touching one. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal. One note on the TASKS.md commit: the CPO task's own 2026-10-11 09:50 block was sitting **uncommitted** in the worktree when this run started and therefore rides along in tonight's `docs(tasks)` commit — it is that task's faithful record, unedited, flagged here only so the authorship is not mistaken. **`Started:` audit clean — 31 blocks across In-flight, Ready and Done (last 10), 0 missing.** Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (660 files, exit 0 — file count read, not just the exit code; run against the mounted path, and not piped, so exit 2 could not hide behind a pipe). **Syntax-check: PASS** (Script 2 OK / Script 5 OK on `inspect/index.html`). **Dead-links: verified** — `href` inventory md5 `f8554c34…`, byte-identical to the HEAD blob; no link added or changed. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-03 → 10-11 baseline, the one warn is the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`. **G28 self-check: 273 distinct campaign tokens in deployed HTML, 0 unledgered.** CHECKLISTS 245 keys (HEAD 245); `VEHICLE_MENU` byte-equal to HEAD; `inspect/index.html` +41/-6; truncation guard ends `</html>`.

    **PUSH: blocked. Day 33.** `GET /user` with the stored PAT returns 401 again (prefix `ghp_krkG...`, `expires` still reads 2027-05-19, credentials file untouched since 2026-05-30 — revoked, not expired). No `git push` attempted: the only way to make one succeed without a valid credential is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. Commits tonight: **three** — `53e8580` (content), `7af1560` (hash record) and `7ad78f1` (corrective restore). **The correction is a process finding worth recording:** `7af1560` was built with `GIT_INDEX_FILE` pointing at a *copy of* `.git/index` taken before `53e8580`, because the 10-05 workaround for the undeletable `.git/index.lock` copies the real index aside and the real index is therefore never advanced by a commit made through it. Staging `TASKS.md` on that stale copy silently reverted `inspect/index.html` and `scripts/recall-ledger.json` to their pre-`53e8580` blobs — a 33-insertion/188-deletion commit that looked like a docs commit. The worktree was never wrong and `git status` caught it immediately. `7ad78f1` rebuilds the index with `git read-tree HEAD` and restores both files; HEAD is now byte-identical to `53e8580` for the content files, verified by an empty `git diff 53e8580 HEAD --` on both paths, and `git diff HEAD` is empty. **Rule for whoever continues this: with the `GIT_INDEX_FILE` workaround, seed the temp index with `git read-tree HEAD`, never with `cp .git/index` — and diff `--cached` against HEAD before every commit.** All gates were re-run against the final HEAD state and pass unchanged (scanner 661 files exit 0, syntax Script 2/5 OK, gate 28/1/0, queue 48). **38 commits now stuck**, `origin/main` still at `0dfa937`. Among them wave 24's removal of 36 false recall citations and wave 25's CX-5 correction — those wrong campaign numbers are **still live on autovetting.com**, and so is the understatement these three nights have been closing. One `git push origin main` with a working token ships all of it. **G29** (10-09) still awaiting Daniel: tonight's 26 rows would pass it, and the 10-11 near-miss plus tonight's confirmation both argue for extending its text-matching to **prose** rather than rows alone.

    **Next run.** Queue **48**. Nine slugs still claiming 2, in order: `audi-q7-2018`, `chevrolet-tahoe-2021`, `gmc-yukon-2021`, `land-rover-defender-2020`, `nissan-altima-2019`, `porsche-cayenne-2019`, `porsche-macan-2017`, `ram-2500-2019`, `tesla-model-y-2022` — then the thirty-nine at 1. `audi-q7-2018` is next. **`chevrolet-tahoe-2021` and `gmc-yukon-2021` both overlap tonight's Escalade heavily** (`22V-827`, `24V-797`, `25V-274`, `25V-619` are all multi-make GM and already ledgered) — expect them cheap, and query `recallsByVehicle` for each vehicle itself anyway. Tonight's `22V-873` and `25V-060` results are the standing proof of why: both real, both ledgered, and neither belongs on the sibling truck.

    2026-10-13 02:00 [scheduled task]: **three more slugs off the recall-content queue — `audi-q7-2018`, `chevrolet-tahoe-2021`, `gmc-yukon-2021`. 33 campaign rows added, every one returned by `recallsByVehicle` for that exact vehicle before it was written and ledgered before it shipped. Queue 48 → 45.** `stats.recalls` corrected to match countable rows on all three: Q7 **2 → 3**, Tahoe **2 → 16**, Yukon **2 → 14** — all three *under*-stating, same direction as 10-11 and 10-12. Ledger `verified` **320 → 330** (10 new keys; 23 of the 33 rows cite campaigns already ledgered from the 10-11 Silverado and 10-12 Escalade batches), `unverified_legacy` 0 → 0. `stat == displayed rows` **140 → 143** like-for-like against the HEAD blob; total recall rows **461 → 494**; rows missing `number`/`title`/`desc` **0 before, 0 after**.

    **The headline is that the 10-05 study's fragmentation trap moved to a new axis — wheelbase — and this time it changed what reached a page.** `model=yukon` returns **13** campaigns, `model=yukon xl` returns **12**, and **neither set is a superset of the other**: `20V-792` is Yukon XL only, while `21V-579` and `21V-064` are short-wheelbase Yukon only. Union = **14**. The `gmc-yukon-2021` checklist covers both bodies — its own summary says the XL "adds extra length" and its `vinNote` says the engine encoding "holds on the Yukon XL as well" — so the honest count is the union, and the three rows that differ **name the wheelbase that puts a truck in scope**. A single `model=yukon` query would have shipped 13 rows and silently dropped the **624,216-vehicle** front-row-centre seat-belt-bracket campaign from every long-wheelbase truck on the page. Second-sourced: `20V792000` lists 17 combinations including 2021 Tahoe, Suburban and **Yukon XL** and **no plain 2021 Yukon**; `21V579000` (2 units) and `21V064000` (18 units) each list the 2021 Tahoe and 2021 Yukon and nothing else. Prior nights proved the rule on tables; tonight is the first time it moved rows onto a deployed page.

    **Three of these are service-induced rather than build defects, and the generalisation inverts a buyer heuristic.** `21V-579` — a **dealer technician** miscalibrated the brake control module (stability control, traction control, ABS, towing brake performance), 2 vehicles. `20V-735` — front seats **removed for a repair during assembly**, attachment bolts possibly not reinstalled, 94 vehicles. `25V-619` — an **earlier tank replacement** may have fitted the wrong diesel tank, 12 vehicles (carried from the 10-12 Escalade; the Tahoe is in scope, the Yukon is **not** — re-checked, the campaign record lists only 2022 and 2024 Yukon). **For this class, more repair history means more exposure, not less** — the opposite of how a thick service file normally reads. Pairs with the 10-12 asset ("a completed recall is not the same as a closed VIN") as the second finding in two nights about recall records not meaning what a buyer assumes; both belong in the same content piece.

    **The vinNote partitions the costly campaigns and spares the engine the checklists fear most.** Same shape as the 10-12 Escalade finding, now on the T1XX `D`/`L`/`T` codes both pages already document: `25V-274` (connecting rod / crankshaft → engine replacement) is **6.2L L87 (`L`) only**; `24V-797` (control valve → rear wheels lock) and `25V-619` are **3.0L Duramax (`T`) only**; and **`D`, the 5.3L L84 DFM lifter engine both checklists warn about hardest, is in neither.** The engine with the worst wear reputation carries the least recall exposure on the expensive campaigns. Both rows name the digit, and the `24V-797` row states the partition outright.

    **Other findings.** (a) **Over-the-air remedies break service-history reasoning** — `21V-455` (power steering assist can cut out), `21V-421` (airbag warning lamp) and `22V-827` (daytime running lights) can all be remedied OTA, leaving **no dealer service-record entry**, so a clean history neither proves nor disproves them and only the VIN lookup answers; said plainly in all three rows. (b) **Four campaigns have populations under 100** — `21V-579` (2), `21V-210` (5), `21V-064` (18), `20V-735` (94); `21V-210` is the narrowest row in the library, **5 vehicles, 2021 Tahoe only**, a second-row centre belt latch trapped under the trim bezel (FMVSS 208), shipped so the one buyer looking at one of them can find out. (c) **`20V-811` is a fastener-supply mix-up, not a design fault** — 470 vehicles across **18 different 2021 GM model lines**, which is the signature: unpredictable by model, answerable only by VIN. (d) **Q7 2018** — one of three is Q7-specific (`20V-658`, C-pillar deformation element, 94,144 units, 2018-2020 Q7 only); `19V-035` (fuel rails leak, 74,881) spans Q7/A6/A7/A8; `20V-149` (steering shaft bolt loosens → loss of steering control) covers 2017-2019 Q7 + 2019 Q8 at **229 vehicles campaign-wide** — the most severe consequence on that page attached to its smallest population, and undetectable on a test drive.

    **Found, not fixed, escalated: G28 does not look at the deployed blog.** G28 reads exactly three pages (`inspect/index.html`, `index.html`, `pinpoint/index.html`). A sweep of every deployed HTML file found **22 distinct campaign numbers on 11 `blog/` pages that are not in the ledger at all** (plus two gitignored `_hub/` files, which do not deploy) — never gate-checked in either direction. Spot-checked three via `campaignNumber` before assigning severity and **all three are real and correctly attributed** (`19V-184` → 2019 Equinox/Terrain on the Equinox post; `20V-693` → 2020 Explorer/Aviator on the Explorer post; `21V-649` → 2016-2021 Malibu + XT4 on the Malibu post), so this is an **unguarded surface, not a known defect** — 🟡, not the wave-24 situation. Deliberately not fixed: auditing 22 numbers across 10 posts is its own wave, and **widening G28's page set before that audit would CRITICAL-fail the gate immediately** and block a push stack already 42 deep. Escalated to `Awaiting-Daniel.md` as a sequenced proposal — audit first, then widen.

    **Method.** One `recallsByVehicle` query per slug through the sandbox fetch path, plus a fourth for `model=yukon xl` once the slug's own copy showed it covers both bodies; `curl` to `api.nhtsa.gov` still fails from both shells (re-tested — cloud proxy `CONNECT tunnel failed, 403 / connect_rejected, organization policy`). Rows authored in the canonical `{number, title, desc}` shape only. **Second-sourced via `campaignNumber`**: `19V035000`, `20V149000`, `20V658000`, `20V792000`, `21V210000`, `21V579000`, `21V064000`, `20V735000`, `20V811000`, `25V619000`. Multi-model campaigns record `makes` as the queried make only with a component note that the slug's vehicle was confirmed in scope by `recallsByVehicle`; the full make list was deliberately **not** inferred. Ledger keys unhyphenated from the start and appended by text insertion ahead of the `verified` closing brace, so the diff is **+80/-0** and the file reparses. **The 10-12 stale-index rule held:** the `GIT_INDEX_FILE` temp index was seeded with `git read-tree HEAD`, never `cp .git/index`, and `git diff --cached HEAD` was checked before committing — it showed exactly the two content files at `+42/-6` and `+80/-0`, matching the worktree, so no corrective commit was needed. Both `.git/HEAD.lock` and `.git/index.lock` (dated 10-12 09:24) had to be parked under new names again; `.git/` now holds **162** zero-byte `HEAD.lock.*` corpses. Carried forward unfixed, both pre-existing: `23V093` is still a bare string rather than an object and satisfies G28 on key membership alone (1 of 330), and the empty untracked file with a newline in its name is still in the repo root — tonight's commit used explicit paths so it was not staged.

    Sibling check: no blocking overlap, nothing to re-sync. Touched `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md` and the gitignored `_hub/Build-Log/2026-10-13.md` + `_hub/Awaiting-Daniel.md`. Every Ready block that shares `inspect/index.html` or `scripts/recall-ledger.json` (recall-audit waves 24-25, vinnote batches 09-09 → 10-01, menu sweeps) is an **ancestor of `main`**, not a concurrent sibling — this run is a descendant of the 10-12 batch (`d2f74e1`) and consumes its ledger output additively, appending keys without touching one. None of the three slugs was touched by waves 24/25 or by the 10-08 → 10-12 batches; the vinnote blocks touch `vinNote:` only, disjoint from the three `recalls` arrays and three `stats.recalls` integers changed here. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal — note that the G28 blog finding above concerns **deployed** `blog/*/index.html` output, not that task's gitignored markdown sources, so it is a finding about the gate's scope and not a conflict with that task. **`Started:` audit clean — 31 blocks across In-flight, Ready and Done (last 10), 0 missing.** Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (662 files, exit 0 — file count read, not just the exit code; run unpiped so exit 2 could not hide behind a pipe). **Syntax-check: PASS** (Script 2 OK / Script 5 OK on `inspect/index.html`). **Dead-links: verified** — `href` inventory **byte-identical to the HEAD blob**, 18 distinct internal paths, no link added or changed, no `/decode/` link. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-03 → 10-12 baseline, the one warn still the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`. **G28 self-check in the gate's own scope: 282 distinct campaign tokens, 0 unledgered.** CHECKLISTS **245 keys before and after, key sequence identical**, verified by evaluating both the HEAD blob and the worktree file in node; `VEHICLE_MENU` **JSON-equal to HEAD**; `inspect/index.html` **+42/-6** (18,271 → 18,307 lines); truncation guard ends `</html>`; ledger reparses at `verified` 330.

    **Commit: `6f5e3d9`.** **PUSH: refused, Day 34.** `GET /user` with the stored PAT returns **401** (prefix `ghp_krkG...`, credentials file untouched since 2026-05-30, `expires` still reads 2027-05-19 — revoked, not expired). No `git push` attempted: the only way to make one succeed without a valid credential is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. **42 commits now stuck**, `origin/main` still at `0dfa937`. Among them wave 24's removal of 36 false recall citations and wave 25's CX-5 correction — those wrong campaign numbers are **still live on autovetting.com** — plus four nights of recall-row work (12 slugs, 83 campaign rows) correcting pages that currently understate their recall count. One `git push origin main` with a working token ships all of it. **G29** (10-09) still awaiting Daniel; tonight's 33 rows would pass it.

    **Next run.** Queue **45**. Six slugs still claiming 2, in order: `land-rover-defender-2020`, `nissan-altima-2019`, `porsche-cayenne-2019`, `porsche-macan-2017`, `ram-2500-2019`, `tesla-model-y-2022` — then the thirty-nine at 1. `land-rover-defender-2020` is next. **Carry the wheelbase lesson in:** `ram-2500-2019` is the next slug where a model string is likely to fragment (`2500` vs `2500 HD` vs a bare `ram`), and the 10-05 study already flagged `Silverado 1500` / `Rogue Sport` / `Mazda3` / `CR-V` / `4Runner` as the known-prone set. **Before writing rows for a slug whose own copy covers more than one body, trim or nameplate, query each string and ship the union.**


    2026-10-14 02:00 [scheduled task]: **three more slugs off the recall-content queue — `land-rover-defender-2020`, `nissan-altima-2019`, `porsche-cayenne-2019`. 23 campaign rows added, every one returned by `recallsByVehicle` for that exact vehicle before it was written and ledgered before it shipped. Queue 45 -> 42.** `stats.recalls` corrected to match countable rows on all three: Defender **2 -> 8**, Altima **2 -> 7**, Cayenne **2 -> 8**. All three displayed **zero** rows against a stat of 2, so all three were *under*-stating, same direction as 10-11, 10-12 and 10-13. Ledger `verified` **330 -> 350** (20 new keys; 3 of the 23 rows cite campaigns already ledgered), `unverified_legacy` 0 -> 0. `stat == displayed rows` **165 -> 168**; total recall rows **494 -> 517**; rows missing `number`/`title`/`desc` **0 before, 0 after**.

    **Method upgrade worth adopting permanently: stop guessing fragmentation variants and ask NHTSA for the model list.** `products/vehicle/models?modelYear=Y&make=M&issueType=r` returns every model string NHTSA holds for a make and year in **one** query. Run on all three makes before any recall query, it proved both outcomes in a single night: **Land Rover 2020 holds one Defender string** (`DEFENDER`) even though the slug's trim line reads "Defender 90 / 110 / 130", so 8 is provably the complete set and no variant queries were wasted; **Porsche 2019 holds three Cayenne strings** (`CAYENNE`, `CAYENNE TURBO`, `CAYENNE E-HYBRID`), which guessing would likely have missed. Nissan 2019 holds one `ALTIMA`.

    **The fragmentation trap moved to trim/powertrain, and this time it drops the fire risks.** `model=cayenne` returns **6** campaigns; `model=cayenne turbo` returns **1** that is not among them (`20V-270`, fuel line quick connector leak, 2,253 units, Turbo and Turbo S Hybrid bodies only); `model=cayenne e-hybrid` returns **2**, one of which is not among them (`23V-841`, 220V/240V charging cable overheats the outlet or cable, 41,345 units, Cayenne E-Hybrid 2019-2024 in scope). Union = **8**. **The two campaigns a single query drops are the two fire risks on the page** — worse than the 10-13 Yukon case, which dropped one seat-belt campaign. **And the axis is unreliable in both directions:** `19V-112` is returned under `model=cayenne` even though its summary names the **Cayenne Turbo**, the exact opposite of how `20V-270` is filed. So the tempting shortcut "query the narrowest string and stop" is also wrong; the union is the only defensible answer.

    **Supersession is the named mechanism behind the 10-12 asset, with three instances in one night.** `19V-735` **supersedes `19V-115`** (brake-pad wear warning, FMVSS 135) and its record explicitly covers vehicles **already repaired** under it; `26V-599` **expands `26V-248`** (DC-DC converter), so a Defender remedied under the first returns to scope under the second; and for the record `25V-644` superseded `24V-576` on the 10-12 X7 batch — same shape, noticed but not named. A buyer holding paperwork that says the earlier campaign was completed is **still in scope**. Both pairs ship with the relationship stated in the row, and `19V-115` is shipped *deliberately although closed*, because it is on the car's record and its completion is exactly what misleads. `26V-599` adds a second point: interim owner letters are **expected 2026-11-13**, so it is right now an **open recall with no remedy available** — "the recalls are clear" cannot be true for this vehicle today.

    **The engine partition inverts again, and lands on the engine the checklist recommends.** *Defender* — `21V-424` (PCM switches off, engine stalls, 163 vehicles) is **six-cylinder only**, i.e. the **P400 3.0T I6 MHEV** that this checklist calls "preferred" and rates **low risk**. *Altima* — the two engine families carry **one engine-specific campaign each and they are different ones**: `25V-437` (VC-Turbo bearings, 443,899 units) is 2.0L only, `19V-316` (fuel pump lock ring, FMVSS 301) is 2.5L front-drive only; the existing `vinNote` already asserted the VC-Turbo "bearing-recall risk that the 2.5L does not share", so the campaign record **confirms the vinNote was right** and the vinNote earned its keep before the rows were written. 10-13 found the worst-*wear* engine carrying the least *recall* exposure; tonight the best-regarded engine carries the stall recall. **Wear reputation and recall exposure are orthogonal, and a checklist that recommends an engine on reliability grounds is not recommending it on recall grounds.**

    **Three recalls whose remedy is not a repair to the car** — the sharpest instances yet of the records-don't-mean-what-buyers-assume thread, because in each the VIN status and the car can legitimately disagree. `23V-841` — **the remedy is a loose object**: the recalled part is the portable charging cable, so a VIN reading remedied means a cable was issued *to somebody*, not that the right cable is in the car being sold (row says: open the frunk and look). `24E-102` — **the recall is on an aftermarket accessory**: Raised Air Intake part VPLEP0543, 485 units, applies only if a previous owner bolted it on, so **no build sheet or spec check will ever surface it** (written in the house pattern already used for `17E-061`/`18E-107`). `21V-584` — **the remedy is a mailed letter**: the owner's manual overstates the third row's LATCH anchors (FMVSS 225), a correction insert is posted, nothing is done to the vehicle and **no service record is ever created**. `21V-424`, `26V-248` and `26V-599` can also be remedied over the air, so the 10-13 OTA finding holds on a second manufacturer.

    **Found, not fixed, escalated: G28 cannot see equipment ("E") campaigns — and unlike the 10-13 blog gap, this one is safe to close now.** G28's token regex is `\d{2}V-?\d{3}`, so `24E-102` does not match and ships unchecked in either direction. **Blast radius measured and it is zero:** three E-campaign numbers exist in deployed HTML — `17E-061`, `18E-107` and tonight's `24E-102` — and **all three are already ledgered**, so widening to `\d{2}[VE]-?\d{3}` is a one-character change that **passes immediately**. That is the opposite of the 10-13 blog finding (22 unledgered numbers, widening would CRITICAL-fail and block the push stack), and the contrast is the useful part: the blog item needs an audit wave first, this one needs nothing. Not applied tonight because a gate change is Daniel's call per the standing preference; escalated as a yes/no with no preparatory work behind it.

    **Other editorial findings.** (a) **A tire recall on a seven-year-old car is the one class a used buyer can usually discount** — `21V-169` (over-cured Continental tires, 36,141 units) is real, but the original tires on a 2019 Altima are long gone; the row says so and adds the useful part, that a VIN still showing it open means **nobody logged an inspection**, not that the tires on the car are bad. First row in the library that tells a buyer a campaign is probably moot. (b) **`19V-112` is now the narrowest row in the library at one vehicle campaign-wide** (shock absorber forks, Cayenne Turbo), taking the record from `21V-210`'s five. (c) **Two separate camera campaigns on each of two cars** — Altima `19V-654` (the display setting can be switched off and *persists*) + `23V-628` (harness damage); Cayenne `19V-111` (display delay) + `25V-896` (no image in reverse), six years apart. `19V-654` is also the test-drive line: a blank reverse screen is a **settings** question before it is a hardware question. (d) **Two separate fuel-delivery campaigns on the 2019 Altima** — `18V-922` (retainer clip) and `19V-316` (lock ring), different mechanisms, same model year. (e) **`19V-235` is the rare recall a buyer can verify in the car park** — mislocated brake switch bracket holds the switch on, so brake lights stay lit with nobody braking *and* the shifter can leave Park without the pedal pressed. (f) **`23V-044` is a platform campaign, not a Defender fault** (blocked cam carrier oil channel, spanning Range Rover Sport/Range Rover/Discovery/Velar) — said in the row so the Defender is not blamed for a shared engine's campaign.

    **Repo state — the stale index is fixed at its root.** Both `.git/HEAD.lock` and `.git/index.lock` were parked under new names, after which **`git reset` succeeded** and refreshed the real `.git/index` from HEAD. `git status` now reports plain `M` instead of the `MM` noise carried since 10-03, and **the `GIT_INDEX_FILE` workaround was not needed** — tonight's commit was an ordinary `git add` + `git commit`. This closes the hazard that produced the bad `7af1560` commit on 10-12 (a temp index seeded from `cp .git/index` silently reverted two content files). `git diff --cached HEAD` was still checked before committing and showed exactly the two content paths. Git still cannot unlink its own locks in the mount, so `HEAD.lock` and `refs/heads/main.lock` were re-created and parked again; `.git/` now holds **167** zero-byte lock corpses. The structural fix is `device_request_delete_permission` on the Claude folder — **not requested tonight**, because that prompt needs a person to answer it and nobody is awake at 02:00; flagged for Daniel instead. Carried forward unfixed, both pre-existing: `23V093` is still a bare string rather than an object and satisfies G28 on key membership alone (1 of 350), and the empty untracked file with a newline in its name is still in the repo root — tonight's commit used explicit paths so it was not staged.

    Sibling check: no blocking overlap, nothing to re-sync. Touched `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md` and the gitignored `_hub/Build-Log/2026-10-14.md` + `_hub/Awaiting-Daniel.md`. Every Ready and Done block that shares `inspect/index.html` or `scripts/recall-ledger.json` is an **ancestor of `main`**, not a concurrent sibling — this run is a descendant of the 10-13 batch (`a393b62`) and consumes its ledger output additively, appending 20 keys without touching one (diff **+160/-0**). None of the three slugs was touched by waves 24/25 or by the 10-08 -> 10-13 batches; the vinnote blocks touch `vinNote:` only, disjoint from the three `recalls` arrays and three `stats.recalls` integers changed here. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`, gitignored) are orthogonal; the 10-13 G28 blog finding concerns **deployed** `blog/*/index.html` output, not that task's gitignored markdown sources, so it remains a finding about gate scope rather than a conflict. **`Started:` audit clean — 40 blocks across In-flight (4), Ready (26) and Done last 10 (10), 0 missing.** Note the Done section uses `####` headings, which a `###`-only scan silently skips — all 10 Done blocks share `inspect/index.html` or `scripts/recall-ledger.json`, so a missed Started date there would gate-block every future task on this file; re-checked at `####` depth and all 10 carry one. Verified against: autovetting-recall-audit-wave-25-2026-10-04, autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (666 files, exit 0 — file count read, not just the exit code; run unpiped so exit 2 could not hide behind a pipe). **Syntax-check: PASS** (official node recipe, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory **byte-identical to the HEAD blob** (29 hrefs, 18 distinct internal paths, md5 `632ecf00...`); no link added, removed or changed; no `/decode/` link. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — identical to the 10-03 -> 10-13 baseline, the one warn still the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`. **G28 self-check in the gate's own scope: 304 distinct campaign tokens in `inspect/index.html` plus 10 in `pinpoint/index.html`, 0 unledgered.** **CHECKLISTS integrity:** 245 keys before and after, **key sequence identical**, verified by evaluating both the HEAD blob and the worktree file in node rather than by regex. **`VEHICLE_MENU` JSON-equal to HEAD**, so no route could change. `inspect/index.html` **+32/-5** (18,307 -> 18,334 lines); truncation guard ends `</html>`; ledger reparses at `verified` 350.

    **Commit: `c91961b`** (parented on `a393b62`; tree diff is exactly 2 paths — `inspect/index.html` and `scripts/recall-ledger.json`. `git diff-tree` confirms nothing under `_hub/` entered the tree). **PUSH: refused, Day 35.** `GET /user` with the stored PAT returns **401** (prefix `ghp_krkG...`, `expires` still reads 2027-05-19, credentials file untouched since 2026-05-30 — revoked, not expired). No `git push` was attempted: the only way to make one succeed without a valid credential is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. **43 commits now stuck**, `origin/main` still at `0dfa937`. **G29** (10-09) still awaiting Daniel; tonight's 23 rows would pass it.

    **Next run.** Queue **42**. Three slugs still claiming 2, in order: `porsche-macan-2017`, `ram-2500-2019`, `tesla-model-y-2022` — then the thirty-nine at 1. `porsche-macan-2017` is next. **Carry the method in, not just the lesson: start every slug with `products/vehicle/models?modelYear=Y&make=M&issueType=r`.** Two named candidates ahead where it pays immediately — **`porsche-macan-2017`**, because the 2019 Porsche list already showed `MACAN` and `MACAN TURBO` as separate strings (check 2017's own list), and **`ram-2500-2019`**, where `2500` vs `2500 HD` vs a bare `ram` was flagged on 10-13.

    2026-10-15 02:00 [scheduled task]: **two more slugs off the recall-content queue — `porsche-macan-2017` and `ram-2500-2019`. 19 NHTSA campaign rows added**, every one returned by `recallsByVehicle` for that exact vehicle before it was written and ledgered before it shipped. `stats.recalls` 2 -> 7 (Macan) and 2 -> 12 (Ram); both displayed zero rows against a stat of 2, so both were *under*-stating. Queue **42 -> 40**. Ledger `verified` **350 -> 367** (17 new; `25V-010` and `20V-191` were already ledgered and left untouched), `unverified_legacy` 0 -> 0. Two slugs rather than three, deliberately: the Ram carries 12 campaigns and the Macan needed seven `campaignNumber` second-sources to settle scope in both directions. The third queued slug, `tesla-model-y-2022`, was scouted and left for tomorrow with its data in hand — it is a 20-row page.

    **The index is wrong in BOTH directions on the same vehicle, and the proof is inside one record.** The 2017 Macan holds four strings (`MACAN` 6 campaigns / `MACAN S` 4 / `MACAN TURBO` 3 / `MACAN GTS` 4, union **7**) and the sets are not nested. The base string misses `17V-133` (occupant sensor mat, FMVSS 208, 17,871 units, **GTS-only for MY2017**, returned under `MACAN GTS` alone). The trim strings miss `20V-077` (fuel pump flange cracked by its own service cover, **70,117 units**, fire risk) and `16V-680` (front anti-roll bar links -> oversteer, 243 units), both indexed under the bare `MACAN` string only. Decisive: **`16V-680`'s own summary names "2017 Macan, Macan S, Macan GTS, and Macan Turbo" while its model index carries a single row, `MACAN, 2017`** — the record contradicts its own index in the same API response. The union is the only defensible answer, not merely the safest.

    **The mirror failure — summary year-ranges OVER-attribute — and the sibling check is what caught it.** `autovet-cpo-protocol-ingestion` verified Macan campaigns first-hand on 2026-07-05 and recorded `22V-656` (low-beam headlight adjustment-screw caps, FMVSS 108, **222,858 units**), which appeared in **none** of tonight's four queries. Checked directly rather than assumed: its summary covers "certain **2003-2020** Macan, Cayenne, Panamera, and Cayman S vehicles" but its per-model-year rows — read end to end across two fetch windows — hold `2015 Macan S`, `2015 Macan Turbo` and `2018 Macan S` and **no 2017 Macan row of any trim**. **Deliberately not shipped.** So trim strings under-attribute while summary ranges over-attribute, and **a campaign another task verified first-hand for the *model* is not verified for the *model year*** — the model-year rows are the gate. Second, opposite reason for the existing "never reuse another slug's result" rule.

    **Supersession recurs three times tonight, on two manufacturers, and in each case the later campaign re-covers cars the earlier one fixed.** (a) Macan occupant sensor mat: `17V-133` (Jun 2017, GTS only, 17,871) then `21V-131` (Oct 2021, **all four 2017 trims**, 39,547) — same component, same remedy, so a 2017 GTS repaired in 2017 is back in scope four years later. (b) Macan fuel pump flange: `17V-289` (Jul 2017, 51,497) then `20V-077` (Apr 2020, 70,117) — same part three years apart, and the later, larger one is the fragmented one. (c) Ram curtain airbag inflator: `25V-010` (letters 2025-02-13, 6,066, FCA 05C/09C/10C) then `25V-824` (letters 2025-12-18, 1,589, FCA C2C/C7C/C8C) — same rupture, same remedy, ten months apart, and `25V-824`'s VINs only became searchable 2025-12-04, so a history report printed before that date cannot show it. "The recall was done" is a sentence about one campaign, not about a component.

    **The recommended engine carries the recalls again — third night in four.** `ram-2500-2019` rates the 6.7L Cummins **low risk** and calls it "legendary for durability." Three of the truck's four fire-or-stall campaigns sit on the Cummins driveline and none touch the 6.4L HEMI: `21V-880` (HPFP fails, engine stalls, **222,410 units**, Cummins only), `19V-498` (diesel fuel lines leak into the engine bay, 499 units, diesel only), `20V-043` (the six-speed **68RFE** pushes fluid out of the dipstick tube and the record states it could reach **the turbocharger**, 87,431 units — 68RFE and turbo are the Cummins driveline; the 2019 HEMI 2500 runs the eight-speed). The fourth, `19V-635` (front calipers built with the wrong assembly fluid, seals swell, brakes drag and overheat, 5,495 units), is the only engine-agnostic one and the only one whose remedy is a real mechanical repair. 10-14 found the *preferred* engine carrying the stall recall; tonight the *legendary* one carries three of four. **Wear reputation and recall exposure are orthogonal** — and the checklists state the first while implying the second.

    **Ram 2019 does not fragment; the 10-13 question is closed in one call.** `products/vehicle/models?modelYear=2019&make=ram&issueType=r` returns seven distinct strings (`1500`, `1500 CLASSIC`, `2500`, `3500`, `4500`, `5500`, `PROMASTER`, `PROMASTER CITY`) and exactly **one** 2500 string — no `2500 HD`, no bare `RAM`. 12 is provably complete.

    **Other editorial findings.** (a) **Fitment-dependent rows, factory-option flavour:** `20V-207` (Ram accessory bed step, 37,580 units) and `18V-844` (Macan optional ski bag, 142 units) apply only if the part is on the vehicle — unlike `24E-102` (10-14, aftermarket) these are factory options, so a VIN can read open on a car that never had one or closed because somebody removed it. Both rows say to look at the car. (b) **OTA holds on a fourth manufacturer:** `20V-191` (Ram rearview camera) is a radio software update applicable over the air, so a clean dealer history neither proves nor disproves it. (c) **A quieter version of the same problem:** `22V-140`'s defect is that the ESC warning lamp may fail to illuminate during a fault, so on an unremedied truck **a dark ESC light is not evidence the system works** — worth closing before trusting a clean dash on a test drive.

    Sibling check: no blocking overlap, nothing to re-sync. Touched `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md` and the gitignored `_hub/Build-Log/2026-10-15.md` + `_hub/Awaiting-Daniel.md`. In-flight `autovet-competitor-monitor` (`Competitors/`, AutoTrader/Cox 10-15), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/` + per-vehicle `Content/_seo-research/`, 2018 Mazda3 10-14) are orthogonal by file tree. The cpo-ingestion block *does* carry Macan campaign IDs (2026-07-05) — read-only cross-referenced, and it produced tonight's `22V-656` finding rather than a conflict. Ready blocks 09-09 -> 10-04 all touch `inspect/index.html` or `scripts/recall-ledger.json` but are ancestors of `main`, not concurrent siblings; `c91961b`/`d6eeccf` (10-14) is the direct parent and this run consumes its ledger output read-only. Done (last 10) grep for `macan` / `ram-2500` / `2500` found no block touching either slug's rows. **`Started:` audit clean** — all 31 `###` blocks carry a `- Started:` date, 0 missing. Verified against: autovet-cpo-protocol-ingestion (`22V-656` cross-reference), autovetting-recall-audit-wave-25-2026-10-04.

    **Scanner: PASS** (671 files, exit 0 — run with output redirected to a file, not piped, so a non-zero exit could not be masked). **Syntax-check: PASS** (official node recipe on `inspect/index.html`: Script 2 OK, Script 5 OK, exit 0). **Dead-links: verified** — the diff adds no `href` at all, so no new route can be dead. **Row integrity:** both slugs re-parsed out of the HTML after the edit — `stat == displayed rows` (7 == 7, 12 == 12) and **0 rows missing `number`, `title` or `desc`**, so the proposed G29 gate would pass on all 19. **`VEHICLE_MENU` untouched** (no `{ model:` line in the diff), so no route could change. `inspect/index.html` +25/-4 (18,334 -> 18,355 lines), truncation guard ends `</html>`. Ledger diff **+138/-0**, purely additive.

    **Commit: `a49ca8e`** (parented on `d6eeccf`; `git diff-tree` confirms the tree diff is exactly 2 paths — `inspect/index.html` and `scripts/recall-ledger.json`, nothing under `_hub/` entered the tree). **PUSH: refused, Day 36** — `GET /user` with the stored PAT returns **401** (prefix `ghp_krkG...`, credentials file untouched since 2026-05-30). No `git push` attempted: the only way to make one succeed without a valid credential is to put a token in the remote URL, which SECRETS-POLICY Rule 1 bans. **45 commits now stuck**, `origin/main` still at `0dfa937`.

    **Next run.** Queue **40**. One slug still claiming 2 — **`tesla-model-y-2022`** — then the thirty-nine at 1. **Already scouted, and it is the worst case the study has produced.** (1) **There is no canonical `MODEL Y` string at all**: the 2022 Tesla model list holds `MODEL Y 7-SEAT` and `MODEL Y  5-SEAT` and nothing named plainly `MODEL Y` — NHTSA partitions this vehicle by **seat count**, a dimension with no relationship to any defect. (2) **`MODEL Y  5-SEAT` contains two spaces** between `Y` and `5-SEAT`; any exact-match pipeline keyed on a cleanly-typed string silently returns nothing for half the population. (3) **`model=model y` returns 20 campaigns against a `stats.recalls` of 2** — the largest understatement in the library, on a page that reads `overallRisk: 'low'` and hand-waves with "Verify all NHTSA recalls are closed." The 20: `21V-912`, `22V-037`, `22V-045`, `22V-050`, `22V-063`, `22V-235`, `22V-296`, `22V-702`, `22V-844`, `23V-085`, `23V-130`, `23V-385`, `23V-838`, `24V-051`, `24V-153`, `24V-376`, `24V-554`, `24V-935`, `26V-283`, `26V-507`. Confirm the union against both seat strings before writing, and pin down why `model=model y` (20) already exceeds what either seat string can hold alone — that implies substring matching, a difference from the exact-match behaviour recorded on the Silverado on 10-05. Most of the 20 are software/ADAS campaigns with OTA remedies, so that page is where the "no service record is ever created" thread gets its fullest treatment. **Budget the whole night for it.** Carry the method in — `products/vehicle/models` first, every slug — and carry tonight's second lesson in too: **a campaign verified first-hand for the model is not verified for the model year.**

## Ready to deploy / publish



### autovetting-recall-audit-wave-25-2026-10-04 — ready 2026-10-04 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-10-04 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 `[freeze]`. Wave 24 closed `unverified_legacy` at zero, so last night's note put the data study next — but wave 24's own closing caution in the ledger `_doc` ("membership in verified proves a campaign exists, NOT that it belongs on the vehicle you are about to cite it on") had never been tested, and testing it needs no network. Publishing an original-data study off an unaudited dataset is the failure this run prevents. The launch freeze is still active, so no vehicle launch was available.)
- Status: ready to deploy. PUSH still blocked: the PAT is still dead (401, re-tested tonight). Day 26.
- Backlog-ref: `scripts/recall-ledger.json` -> `verified` (237 entries as of wave 24), cross-checked against the 64 checklists in `inspect/index.html` that carry campaign numbers.
- Task: audit the `verified` tier the way wave 24 audited `unverified_legacy` — confirm every campaign number in deployed HTML belongs on the vehicle citing it, and correct what does not.
- Touched files: `inspect/index.html`, `scripts/recall-ledger.json`, `_hub/Build-Log/2026-10-04.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-10-04 02:00 [scheduled task]: **The verified tier is nearly clean — 1 misattribution in 185 numbers, against 36-for-36 in the tier wave 24 audited.** Two checks ran. (1) **Make-vs-slug, all 185 campaign numbers / 226 citation instances across 64 checklists, no network needed** — numbers collected in both hyphenated and unhyphenated forms (the wave-24 lesson) and compared to the ledger `makes` array through a corporate-family alias map (Lexus/Toyota, Acura/Honda, GM brands, FCA brands, Ford/Lincoln). Unledgered: **0** (G28 holding). Mismatches: **1**. (2) **Per-model-year citation check, first tranche of a 64-checklist queue** — 13 attempted highest-citation-count first, **123 of 123 runnable citations across 12 checklists confirmed**; `bmw-3series-2018` not run (`model=3 series` returns HTTP 400 — retry `3-series` / `330i`).

    **The one finding: `15V-461` was shipping on `mazda-cx5-2013`.** `15V461` is the FCA Uconnect remote-access recall — Chrysler, 1,416,903 units, Ram/Chrysler/Dodge/Jeep 2013-2015, no Mazda in it. It sat on the 2013 CX-5 twice (a structured `recalls` row and a prose `desc`) as **"HID Headlamps (Grand Touring) — HID headlamp aim may not meet FMVSS standards"**; the title and failure mode are invented, there is no CX-5 HID campaign. The same number is cited **correctly** on `jeep-grand-cherokee-2014`, confirmed against that car's own NHTSA list — so the number is fine and the *usage* was wrong, which is precisely what a number-only gate cannot see. Remedy is Daniel's ratified one for this failure mode (`[recall-19v268]` / `[recall-19v258]`, and what wave 24 applied to all 36): the false claim removed, and rather than leave the slug with no numbered campaign it now carries the one it actually has — **`16V-644`**, the 2013-2016 CX-5 liftgate-strut corrosion recall (Mazda 9916H, 580,455 units, free dealer replacement of both supports), which `recallsByVehicle` returns as the 2013 CX-5's *only* campaign. Added to `verified` with `makes: ["Mazda"]` and the API URL as source; `verified` 237 -> 238. `stats.recalls` corrected 3 -> 1 (stale since wave 24 removed `14V-292` and `20V-579` from this slug).

    **Second correction, prose only: `ford-escape-2013`.** The genuine `20V-331` row said the cars "were already repaired under 15V-246, 16V-643 or 17V-210". `16V-643` is on the Escape's list; `15V-246` and `17V-210` are Ford door-latch campaigns covering the **Fiesta, Fusion and MKZ** — other models in the same 20V-331 population, never the Escape. Narrowed to `16V-643`, with a parenthetical naming what the other two actually cover so a future run does not restore them. No structured recall row changed; both numbers are now absent from deployed HTML.

    **A methodology trap that nearly produced a false wave-24-sized finding, and the rule that kills it.** `recallsByVehicle` matches `model` **exactly**, and NHTSA's model strings are not ours: `model=silverado 1500` for 2014 returns 6 campaigns, `model=sierra 1500` returns 9, while both pages cite 15-16. Read naively that is 8-9 misattributions per truck. It is nothing — all eight shared numbers were then checked individually against `campaignNumber` and all eight are genuine 2014 Silverado/Sierra campaigns filed by GM under model `SILVERADO` / `SIERRA` without the `1500`: `13V315`, `13V488`, `14V152`, `14V246`, `14V301`, `14V374`, `14V446`, `15V640`. (`16V209` is filed under both `SILVERADO` and `SIERRA 1500` — the inconsistency in miniature.) **Rule for future waves: an absence in `recallsByVehicle` is not evidence, it is a prompt to check that number against `campaignNumber`, which is authoritative.** Wave 24 had this right by accident, having only ever used `campaignNumber`. Same class of false positive: `05V-225` on `toyota-tacoma-2012` is absent from the 2012 list because it is the 2001-2004 Tacoma ball-joint campaign — and the checklist item is titled "Lower ball joints (wear item, not a recall on this truck)" and says so explicitly. Correct editorial; left alone; it will trip any automated make/year gate forever.

    **The `.git` locks were never stuck — the diagnosis changes, not the workaround.** Since 09-15 every run has logged "the locks refuse removal" and asked Daniel to `rm` them. Tonight's `rm` gave the reason: `Operation not permitted` — the sandbox's **file-deletion block**, which applies to every file in a connected folder until the user approves deletion for that folder. The locks are ordinary empty files and nothing holds them. Fix is `rm .git/HEAD.lock .git/index.lock` from Daniel's terminal, or approving the delete-permission prompt in a waking session. That prompt was deliberately **not** fired at 02:00.

    **Freshness delta (criterion 5) recorded, not applied** — the per-YMM queries also return campaigns the pages do not cite: `26V011` (Escape 2013), `10V023` (Highlander 2010), `25V572` (Edge 2017), `14V007` (Sierra 2014), `20V475`/`20V699`/`22V406`/`23V411` (Grand Cherokee 2014), `13E010` (Wrangler 2012, equipment), `19E068` (Ridgeline 2012, equipment). Also, spot-checking wave 24's headline: `20V066` **is** genuinely the 2018 Odyssey's power-outlet wiring campaign — the number wave 24 found on the Tesla Model 3 — and `26V227`/`26V332`/`26V423` are new on that car too. Adding recall rows is content work, so none of it entered tonight's diff; next run decides add-with-verified-text vs leave to the VIN-check row.

    Sibling check: no blocking overlap. Every Ready and Done block touching `inspect/index.html` or `scripts/recall-ledger.json` is an ancestor of this commit, not a concurrent sibling — wave 24 (`ed85aeb`, 10-03) is the direct parent and this is the continuation of that same queue into the `verified` tier. The 09-09 -> 10-01 vinNote blocks touch `inspect/index.html` but edit `vinNote:` fields only; this diff touches one `recalls` row, one `stats.recalls` integer and two `desc` strings, and the two sets do not intersect. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. **`Started:` audit clean** — every block across In-flight, Ready and Done (last 10) carries a `- Started:` date, so no gate-block risk on the shared files. No Re-sync needed. Verified against: autovetting-recall-audit-wave-24-2026-10-03, autovetting-vinnote-batch-2026-10-01.

    **Scanner: PASS** (634 files, exit 0, run against the mounted path per the 10-01 gate-bug note; the literal `/Users/...` path still scans 0 files and still exits 0, so the count was read and not just the exit code). **Syntax-check: PASS** (official node recipe, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory byte-identical to the pre-run snapshot; no link added, removed or changed, no `/decode/` link. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** (same as the 10-03 baseline; the one warn is the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`). **CHECKLISTS integrity:** 245 keys before and after, key set identical. **Menu wiring:** `VEHICLE_MENU` md5 `a5dd26a0...` before and after, byte-equal, so no route could change. **Line count 18,145 before and after. Truncation guard:** ends `</html>`. **Ledger JSON parses; `verified` 237 -> 238, `unverified_legacy` 0 -> 0.** **Commit: `7a6af33`** (parented on wave 24's `a310f02`; tree diff is exactly 3 paths — `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`; `pinpoint/index.html` deliberately excluded, its worktree blob equals HEAD and its `MM` status is stale index noise). Hand-built with `hash-object` / `mktree` / `commit-tree` and `main` advanced by writing the ref file, because the `.git` locks are still in place — see the diagnosis above.

    **PUSH: still blocked. Day 26, 25 commits stuck, `origin/main` still at `0dfa937`.** The CX-5 false recall citation is live on autovetting.com right now, alongside the 36 wave 24 removed. One `git push origin main` with a working token fixes 26 vehicle pages.


### autovetting-recall-audit-wave-24-2026-10-03 — ready 2026-10-03 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-10-03 (02:00 MST overnight builder; priority-1 workstream per DANIEL-DECISIONS-2026-07-29 `[freeze]` = "finish recall-audit waves (89 unverified)". The launch freeze is still active, so no vehicle launch was available — and `[freeze]` names the recall audit as priority 1 and demotes vinNote batches to "fill-in work only", so the audit is what ran rather than another vinNote drain.)
- Status: ready to deploy. PUSH still blocked: the PAT is still dead (401, re-tested tonight). Day 25.
- Backlog-ref: `scripts/recall-ledger.json` -> `unverified_legacy` (36 entries, the tail of the 89 the `[freeze]` decision named); audit queue order per wave-23 notes, "oldest-first through the remaining 36: 14V292, 14V327, 15V258".
- Task: close the recall audit — verify every remaining `unverified_legacy` campaign number against a primary source, and remove from deployed HTML anything that does not hold up.
- Touched files: `inspect/index.html`, `scripts/recall-ledger.json`, `_hub/Build-Log/2026-10-03.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-10-03 02:00 [scheduled task]: **`unverified_legacy` is at ZERO and the audit the `[freeze]` decision made priority 1 is closed. The finding is not that some numbers failed verification — it is that ALL 36 FAILED, and all 36 were live on the inspect pages.** Every one was checked against `api.nhtsa.gov/recalls/campaignNumber`, and not a single one matched the vehicle whose checklist shipped it. 36 claims removed across 25 checklists. **`verified` 218 -> 237, `unverified_legacy` 36 -> 0.**

    **The blocker that made this possible, and it changes what future runs can do.** `curl` to `api.nhtsa.gov` and `vpic.nhtsa.dot.gov` still fails from both shells (exit 56 local, exit 56 cloud — re-tested tonight, and the cloud proxy names it explicitly: `connect_rejected ... organization policy`). But the sandbox's own fetch path **does** reach `api.nhtsa.gov/recalls/campaignNumber`, which is one of the two primary sources the ledger's own `_doc` sanctions. That is the first time a run has had scriptable-enough access to NHTSA recall data since the egress block began. **It also means launch-spec criterion 5 (recall data refreshed within 30 days) is no longer strictly unrunnable** — it is runnable one campaign number at a time through that path, which is slow but real. Previous runs recorded criterion 5 as blocked; that should be revised to "blocked for bulk refresh, available per-number".

    **Method.** One query per campaign number against `api.nhtsa.gov/recalls/campaignNumber?campaignNumber=NNVNNN`, then the API's `Manufacturer` / `Component` / `Make` / `ModelYear` compared against the slug the number actually ships on and against the title and description shipped with it. For every number that returned nothing, the query was repeated in the 9-digit form (`15V554000`) and an adjacent number (`20V582`) was queried as a control — the control returned a record, so the empty results are real absences and not a query-format artifact.

    **An early grep in this run reported all 36 numbers as absent from deployed HTML, and that was wrong.** The ledger stores numbers unhyphenated (`15V258`); the HTML writes them hyphenated (`15V-258`). gate-check normalizes, the grep did not. The error surfaced because removing the numbers from the ledger made G28 CRITICAL-fail and name all 17 — i.e. the gate caught the run's own mistake. Worth knowing for any future audit: **search both forms.**

    **Finding 1 — 5 campaign numbers do not exist in NHTSA's database at all.** `15V-554` shipped on `ford-f150-2015` as "Transmission Shift Cable Bushing"; `18V-027` on `nissan-murano-2018` as "Occupant Classification System"; `18V-575` on `mazda3-2014` as "Fuel Pump (i-Stop Models)"; `19V-965` on `honda-crv-2015` as "Seat Belt Latch"; `20V-583` on `chevrolet-bolt-ev-2020` as "Battery Module Software". Each carried a plausible title, a plausible failure mode and a "verify completion" instruction. This is the same class as the 76+ fabricated entries that caused the ledger to exist.

    **Finding 2 — 12 numbers are real campaigns against a different class of vehicle.** `18V-226` is a **Keystone RV** fuel-system campaign, shipped on BOTH `kia-sportage-2017` and `kia-stinger-2018` as "Brake Booster Vacuum Hose". `19V-133` is an **Indian/Triumph-class motorcycle** campaign (Triumph, electrical wiring), shipped on `toyota-camry-2018` as "Pre-Collision System Calibration". `21V-485` is a **Prevost motorcoach** seat-belt-fastener campaign, shipped on THREE Ford trucks (`ford-explorer-2020`, `ford-bronco-sport-2021`, `ford-f150-2021`) as a "Fuel Injector Seal" fire risk. Also `15V-258` / `15V-303` (Starcraft and Forest River RV label campaigns, both on `ford-f150-2015`), `18V-228` (Indian Motorcycle, on `toyota-rav4-2016`), `18V-585` (Trailstar trailer wheel lugs, on `honda-odyssey-2018`), `19V-243` (Osco / Kenworth-Peterbilt brake lights, on `jeep-wrangler-2018`), `19V-777` and `21V-485` (Prevost, on `chevrolet-malibu-2016` and the Fords), `20V-418` (Thor Motor Coach, on `honda-odyssey-2018`), `21V-009` (Heartland RV axles, on `honda-odyssey-2018`), `21V-394` (**Pierce fire apparatus** diesel fuel rail, on `subaru-outback-2020` as "EyeSight Camera").

    **Finding 3 — 19 are real passenger-car campaigns pasted onto the wrong car.** `20V-066` is the **Honda Odyssey** third-row power-outlet wiring recall (2018-2020 Odyssey) — shipped on `tesla-model3-2019` as "Touchscreen eMMC Wear". `22V-899` is a **Kia** traction-battery coolant campaign — shipped on `ford-maverick-2022` as a rear-axle-bolt torque defect, in a checklist item, in the `recalls` array, AND inside the vinNote. `18V-004` is an **Audi** Takata passenger-inflator campaign — shipped on `toyota-camry-2018` as "Seat Recliner Mechanism". `18V-013` is the **Subaru** Takata equivalent — shipped on `kia-sorento-2016` as "Brake Booster Check Valve". `18V-139` is a **Land Rover** HVAC campaign — shipped on `chevrolet-malibu-2016` as "Steering Gear Seals". Three cases are the right make with the wrong everything else: `19V-075` is a Ford 2011-2013 transmission-control-module campaign, shipped on `ford-f150-2015` as "Rear Axle Shaft Bearing"; `21V-625` is a 2021-2022 Ford/Lincoln fuel-pump-control-module campaign, shipped on `ford-bronco-2021` as a 7-speed-manual clutch damper spring; `21V-650` is the GM 2020-2022 traction-battery campaign, shipped on `chevrolet-bolt-ev-2020` as "Onboard Charging Module". Remainder: `14V-292` (Jaguar software -> `mazda-cx5-2013`), `14V-327` (Stahl upfitter bodies on Ford chassis -> `mazda3-2014`), `17V-225` (Ford 2017 transmission -> `ram-1500-classic-2019`), `17V-718` (Toyota hybrid propulsion -> `subaru-wrx-2018`), `19V-415` (Audi seats -> `ram-1500-2019`), `20V-286` (Toyota front lower control arm -> `bmw-x1-2018`), `20V-579` (VW seat belts -> `mazda-cx5-2013`), `21V-020` (Nissan brake-light switch -> `tesla-model3-2019`), `21V-056` (Mercedes-Benz back-up lights -> `hyundai-palisade-2020`), `21V-711` (Ford windshield -> `ford-mustang-mach-e-2021`), `23V-123` (BMW service brakes -> `honda-odyssey-2018`).

    **The remedy applied is Daniel's, not a new judgment.** DANIEL-DECISIONS-2026-07-29 ratified exactly this for two numbers that failed the same way — `[recall-19v268]` and `[recall-19v258]`: *"DELETE — remove ... from all N checklists; replace each with the standard honest 'run the VIN, check open campaigns' guidance; update recall-ledger.json."* Both were executed and neither number is in the HTML today, so the precedent is live. Applied here to all 36: the 37 structured `recalls` entries were deleted across 25 arrays and each array that lost an entry now carries the standard `{ number: 'Multiple', title: 'Open recalls — VIN check', ... }` row (or the `campaign:`-shape equivalent where that slug uses the other schema); 18 prose assertions inside inspection items, item titles, `source:` fields and one vinNote were rewritten to say that AutoVetting could not confirm a campaign number and that the VIN lookup is the source of truth. **No inspection item was deleted** — the underlying things to check survive; only the false campaign citations are gone.

    **Ledger disposition.** The 19 real passenger-car campaigns are now under `verified` with their ACTUAL makes, components and the API URL as source, dated 2026-10-03 — the research is preserved and a future run can cite `20V-066` correctly on the Odyssey, where it genuinely applies. The 17 that are nonexistent or belong to another vehicle class are deliberately in **neither** tier, which is the ratchet: G28 CRITICAL-fails if any of them is ever shipped again. `_doc` records all of this plus the caveat below.

    **A gate weakness that let this run for months, and it is one line of `gate-check.py`.** G28 asks only whether a campaign number appears in the ledger. It never checks the number against the make or model year of the checklist shipping it. That is why 36 wrong numbers sat behind a passing CRITICAL gate — `unverified_legacy` whitelisted them by number, and nothing compared `19V-133` to "Toyota Camry". **Proposed: G28 should compare the ledgered `makes` array against the slug's `make` and fail on a mismatch.** Not implemented — it changes the deploy gate's behaviour for every project push path, so it is Daniel's call. The `makes` data it would need is now populated for all 237 verified entries.

    **Still blocked, and these are the same three as every night.** (1) **The PAT** — Day 25, now 23 commits stuck, `origin/main` still at `0dfa937`. (2) **NHTSA bulk egress** — still two hosts on an allowlist; the per-number fetch path above is a workaround, not a fix. (3) **The `.git` locks** (`HEAD.lock` 09-15, `index.lock` 09-14) still refuse removal, so tonight's commit was hand-built with `git hash-object` / `mktree` / `commit-tree` and `main` advanced by writing the ref file.

    Sibling check: no blocking overlap. Every Ready and Done block that touches `inspect/index.html` or `scripts/recall-ledger.json` is an ancestor of this commit, not a concurrent sibling — the recall-audit waves 2026-08-01 through 2026-08-12 are the direct predecessors of this work and this run is the closing wave of that same queue. The 09-09 -> 10-01 vinNote blocks touch `inspect/index.html` but edit `vinNote:` fields only; this diff touches `recalls` arrays, four item `desc`/`title`/`source` fields and one vinNote sentence, and the two sets do not intersect except in the single Maverick vinNote line, where only the recall sentence changed and the VIN-digit content is untouched. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. **`Started:` audit clean** — all 28 blocks across In-flight, Ready and Done (last 10) carry a `- Started:` date, 0 missing, so no gate-block risk on `inspect/index.html` or `scripts/recall-ledger.json`. No Re-sync needed. Verified against: autovetting-vinnote-batch-2026-10-01, autovetting-recall-audit-wave-23-2026-08-12.

    **Scanner: PASS** (632 files, exit 0 — run against the mounted path `$HOME/mnt/Claude/Projects/autovetting`, per the 10-01 gate-bug note; the prompt's literal `/Users/...` path still scans 0 files and still exits 0, so the file count was read and not just the exit code). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, **byte-identical** (md5 `f8554c34...` before and after); no link added, removed or changed, no `/decode/` link added, nhtsa.gov cited as prose only. **Deploy gate `scripts/gate-check.py`: 28 passed, 1 warned, 0 CRITICAL failed** — an improvement on the 10-01 baseline of 27/2/0: the recall-audit-backlog warn is now `unverified_legacy in use: 0` and passes, the only remaining warn is the pre-existing `loading=lazy` note on `homepage-test-bc/index.html`. **Intermediate state worth recording: after the ledger edit but before the HTML edit, G28 CRITICAL-failed and named all 17 retired numbers — that failure was the gate working, and it is what corrected this run's bad grep.** **CHECKLISTS integrity:** 245 keys before and after, key set identical. **Menu wiring:** `VEHICLE_MENU` byte-equal to the pre-run snapshot (md5 `1e723e3d...`), so no route could change. **Line diff vs pre-run snapshot: -60 / +45** (net 18,161 -> 18,146 lines in `inspect/index.html`). **Truncation guard:** ends `</html>`. **Commit: `ed85aeb`** (parented on 10-01's `0c94a68`; tree diff is exactly 3 paths — `inspect/index.html`, `scripts/recall-ledger.json`, `TASKS.md`; `git diff-tree` confirmed nothing under `_hub/` entered the tree, and `pinpoint/index.html` was deliberately excluded because its worktree blob equals HEAD and its `MM` status is stale index noise, not a change). This hash line was added in a one-line follow-up commit, since a commit cannot contain its own hash.

    **PUSH: still blocked. Day 25, and the count is now 23 commits.** Nothing in this run has reached the live site, which is the one piece of good news in it — **all 36 false recall citations are still live on autovetting.com right now**, and they stay live until `git push origin main` runs with a working PAT. That raises the stakes on the token: the push is no longer just a backlog, it is the fix for 36 incorrect safety claims on 25 vehicle pages.

### autovetting-vinnote-batch-2026-10-01 — ready 2026-10-01 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-10-01 (02:00 MST overnight builder; launch freeze DANIEL-DECISIONS-2026-07-29 still active, so no vehicle launch is available. Took the sanctioned Step-3 alternative: drain the vinNote queue.)
- Status: ready to deploy. PUSH still blocked: the PAT is still dead (401, re-tested tonight). Day 23.
- Backlog-ref: `_hub/Content/vinnote-queue.md` priorities 103/104/105 (top of queue after the 09-30 drain).
- Task: drain 3 vinNote entries (launch-spec criterion 3, VIN decoding intelligence)
- Touched files: `inspect/index.html`, `_hub/Content/vinnote-queue.md` (gitignored), `_hub/Build-Log/2026-10-01.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-10-01 02:00 [scheduled task]: **3 vinNotes added — `jeep-gladiator-2020`, `chevrolet-bolt-ev-2020`, `subaru-outback-2020`. vinNotes 119 -> 122 (49.8% of 245). Every claim confirmed by single-variable NHTSA vPIC decode. Tonight also found a defect in this task's own required pre-push gate — see the scanner note below, it is the most important line in this block.**

    **THE REQUIRED SECRETS GATE HAS BEEN PASSING VACUOUSLY FROM THIS SHELL, AND THAT IS A GATE BUG, NOT A RUN NOTE.** The command this task's prompt mandates verbatim is `python3 /Users/danieldavis/Documents/Claude/Projects/scan_for_secrets.py /Users/danieldavis/Documents/Claude/Projects/autovetting`. Run exactly as written from the local-device shell it returns **`OK: scanned 0 file(s); no secrets detected`** and **exit 0** — a PASS. The reason is the path: inside the mounted-folder shell the repo is at `$HOME/mnt/Claude/Projects/autovetting`, and `/Users/danieldavis/...` resolves to nothing, so the scanner walks an empty tree and exits 0 on it. **A gate that cannot find the repo reports the same exit code as a gate that found no secrets**, which means the one control standing between this task and the 2026-05-29 PAT-leak chain can be satisfied by a typo in a path. Re-run against the mounted path it scans **629 files, exit 0** — that is tonight's real result and the one recorded below. **Two things are needed: (a) `scan_for_secrets.py` should exit non-zero when it scans 0 files**, so an unresolvable path fails closed instead of open, and **(b) this task's prompt should spell the path as `$HOME/mnt/Claude/Projects/...` or resolve it at runtime.** Until (a) lands, every future run must read the file count and not just the exit code. No push was at risk tonight (the PAT is dead), but this has been latent for as long as the task has run from this shell.

    **The deliverable, and how each claim was proved.** Method throughout, unchanged: construct a VIN for the target year, hold every position constant except one, vary that one character, and read what vPIC returns — so a character is only reported as carrying the powertrain when changing it, and nothing else, changes what vPIC reports back. vPIC is reachable only through the sandbox's own fetch path (see egress note); `curl` to `vpic.nhtsa.dot.gov` fails from both shells, re-tested tonight (exit 56 local, 56 cloud).

    **`subaru-outback-2020` — the engine is at position 6, and this is a NEW cause of criterion-3 failure.** On a constructed `4S4BTACC0L3` Outback VIN, position 6 `A` returns the 2.5L four at **182 hp** (vPIC `EngineModel: U5`), and `G` and `H` both return the 2.4L turbo at **260 hp** (vPIC `EngineModel: U4`); other characters there return error 14. **Three controls were run, and they are what make this a measurement rather than a guess:** changing **position 8** left the engine at 2.5L/182 hp — so the 8th digit, the one the launch spec names, carries nothing about the engine on this car; changing **position 7** left it at 2.5L; changing **position 9** (the check digit) left it at 2.5L. Position 5 was probed too and returns error 8 (no detailed data), i.e. it is part of the model identifier. This is buyer-decisive, not trivia: `A` is the FB25D oil-consumption-and-CVT-fluid inspection, `G`/`H` is the FA24F XT, which keeps the CVT question under more torque and adds turbo upkeep.

    **`jeep-gladiator-2020` — position 8 IS the engine character here, and the finding is what it will answer for.** `G` = 3.6L Pentastar V6, gasoline, 6-cyl, V-shaped. Two controls: changing **position 9** left it at 3.6L (check digit), and changing **position 7** moved the reported trim **Sport -> Rubicon** while the engine held at 3.6L, so trim and engine are encoded separately. **But off the same 2020 Gladiator VIN, `M` returns a 3.0L diesel V6 and `J` returns a 6.4L gasoline V8** — neither of which Jeep built in a 2020 Gladiator. vPIC is reading Chrysler's shared engine table and does not validate the combination. **A decode that returns an engine is therefore not evidence that engine was offered**, which is the opposite of how the 8th digit is usually taught, and the note says so.

    **`chevrolet-bolt-ev-2020` is the fifth manufacturer-specific failure of criterion 3's wording, same cause as the ID.4.** Position 8 carries nothing: substituting any other character returns error 14 rather than a different powertrain, because every U.S. 2020 Bolt EV is the same single front motor and the same 66 kWh pack. **Position 5 carries trim** — `Y` = LT, `Z` = Premier, both still returning `ElectrificationLevel: BEV` with the rest of the VIN unchanged; a control at position 6 left trim at LT and the car electric, so position 5 is the trim character and not a neighbour effect. The note's point is that on a Bolt the VIN is not where the buying decision lives: what decides the car is whether the battery-pack remedy for **22V-076** was performed on that specific VIN, which is a lookup and not an encoding. **22V-076 is ledgered** (`scripts/recall-ledger.json` -> `verified` -> `22V076`, component "High-voltage battery pack fire risk (LG cell defect)", source `nhtsa.gov/press-releases/recall-all-chevy-bolt-vehicles-fire-risk`, verified 2026-06-12), and gate-check's recall-ledger gate passed with the citation in place, so the recall-ledger rule is satisfied rather than side-stepped.

    **Criterion 3's wording has now failed on six manufacturers across three distinct causes.** Toyota (09-13) encodes the engine at position 5; **Subaru (tonight) at position 6**; VW's MEB cars (09-29) and the Bolt (tonight) encode no engine anywhere because a BEV has no engine family; the Buick Envision (09-30) encodes none because it has a single engine with nothing to fork. **The proposed one-line spec edit is unchanged and now has six data points behind it:** reword criterion 3 from "8th-digit engine code mapping" to **"the VIN position that actually forks this vehicle's powertrain or drive layout, identified and verified per manufacturer."** Still not edited — the spec is Daniel's contract document. Escalated again in Awaiting-Daniel.

    **A content inaccuracy found and deliberately NOT edited.** `jeep-gladiator-2020` carries `engine: '3.6L Pentastar V6 (285hp) / 3.0L EcoDiesel V6 (260hp)'` on a `year: 2020` entry, and its summary reasons from both. **The 3.0L EcoDiesel did not reach the Gladiator until the 2021 model year** — it was announced in August 2020 as a 2021 addition — so a 2020 Gladiator is Pentastar-only and the stated second engine does not exist on this model year. That is a **stated spec on a stated model year**, i.e. exactly the class Decision 1 governs, so it is escalated rather than silently corrected. Tonight's vinNote asserts only that `G` = 3.6L and that `M` decoding to a diesel is a decoder artifact, so nothing shipped depends on the resolution.

    Sibling check: no blocking overlap. Ready blocks 09-09 -> 09-30 all touch `inspect/index.html` but are the direct ancestors of this commit, not concurrent siblings; they edit `VEHICLE_MENU` rows, keys, recalls or the render path, while this diff adds three top-level `vinNote` string fields and nothing else — 245 `CHECKLISTS` keys before and after with an identical key set, `VEHICLE_MENU` byte-unchanged (md5 `183b6264...` before and after, 1,356 rows), and a +3/-0 line diff in which all three added lines are `vinNote:` fields. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. `Started:` audit clean across all 27 blocks — 0 missing, no gate-block risk on `inspect/index.html`. No Re-sync needed. Verified against: autovetting-vinnote-batch-2026-09-30.

    **Scanner: PASS** (629 files, exit 0 — against the mounted path; see the gate-bug note above, the prompt's literal path scans 0 files and still exits 0). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, **byte-identical** (33 hrefs, md5 `7bed31f2...` before and after); no link added, removed or changed, nhtsa.gov is cited as prose with no anchor, and no `/decode/` link was added. **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** — unchanged from the 09-30 baseline; the recall-ledger CRITICAL gate passed with the new 22V-076 citation, and the vinNote-coverage warn moved 41/100 -> **43/100 (43.0%)**. **CHECKLISTS integrity:** 245 keys before and after, key set identical, all 3 added lines are `vinNote:` fields, 0 lines removed. **Menu wiring:** `VEHICLE_MENU` byte-equal to the pre-run snapshot, so no route could change; no route re-test needed. **Line diff vs pre-run snapshot: exactly +3, -0.** **Truncation guard:** 18,160 lines, ends `</html>`. **Commit: `0c94a68`** (parented on 09-30's `711f5c3`; `main` fast-forwarded by writing the ref file directly, since the stale `.git` locks still block `git update-ref`). Diff is exactly 2 files, +3 lines in `inspect/index.html`. Commit built with `inspect/index.html` + `TASKS.md` only; `git ls-tree -r` returns nothing under `_hub/` — the 09-25 `update-index --add` ignore-bypass guard was applied.

    **PUSH: still blocked. Day 23, and the count is now 22 commits.** `GET /user` and `GET /repos/dvs-dnl/autovetting` with the stored PAT both return **401**, re-tested tonight from the local-device shell. Prefix still `ghp_krkG...`, `expires` still reads 2027-05-19, `rotated_on` still 2026-05-29, file mtime still 2026-05-30 — the credentials file has not been touched since the 09-25 handoff, so the token was revoked, not expired. `origin/main` still at `0dfa937`; `main` carries everything, so the recovery is still a single `git push origin main` once a live PAT is in the credentials store.

    **NHTSA egress: unchanged, re-tested from both shells tonight.** `vpic.nhtsa.dot.gov` fails with `curl` exit 56 from the local-device shell **and** exit 56 from the cloud container; `api.nhtsa.gov` likewise. `api.github.com` answers from the same shells, so this remains host-specific policy, not an outage. Tonight's verification again went through the sandbox's own fetch path, which does reach vPIC, so all three vehicles' claims are primary-source verified. **That path is still not scriptable, so launch-spec criterion 5 (NHTSA recall/complaint refresh within 30 days) still cannot be run by script**, and every checklist's recall data keeps aging. Two hosts on the egress allowlist is the whole fix; no workaround attempted.

### autovetting-vinnote-batch-2026-09-30 — ready 2026-09-30 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-09-30 (02:00 MST overnight builder; launch freeze DANIEL-DECISIONS-2026-07-29 still active, so no vehicle launch is available. Took the sanctioned Step-3 alternative: drain the vinNote queue.)
- Status: ready to deploy. PUSH still blocked: the PAT is still dead (401, re-tested tonight). Day 22.
- Backlog-ref: `_hub/Content/vinnote-queue.md` priorities 100/101/102 (top of queue after the 09-29 drain).
- Task: drain 3 vinNote entries (launch-spec criterion 3, VIN decoding intelligence)
- Touched files: `inspect/index.html`, `_hub/Content/vinnote-queue.md` (gitignored), `_hub/Build-Log/2026-09-30.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-09-30 02:00 [scheduled task]: **3 vinNotes added — `chevrolet-suburban-2021`, `buick-envision-2021`, `ford-explorer-2020`. vinNotes 116 -> 119 (48.6% of 245). Every code confirmed by single-variable NHTSA vPIC decode. Two of the three carry a finding beyond the fill-in: one closes out the T1XX platform claim, one is a fourth failure of the launch spec's 8th-digit premise.**

    **Method, unchanged from 09-29 and stated because it is what makes each claim checkable.** Construct a VIN for the target year, hold every position constant except one, vary that one character, read what vPIC returns. A character is only reported as an engine code when changing it — and nothing else — changes the powertrain vPIC reports back.

    **`chevrolet-suburban-2021` — 8th digit, and the claim the last two nights were building toward.** `D` = 5.3L **L84** V8, `L` = 6.2L **L87** V8, `T` = 3.0L **LM2** Duramax turbodiesel I6, each returned with its engine-family string off a constructed Suburban VIN (`1GNSKCK_0MR`) rather than inherited from the Tahoe. That is now the **third independent nameplate** decoded — Tahoe and Yukon on 09-29, Suburban tonight — which is what finally licenses the note to state the encoding as platform-wide across GM's T1XX full-size SUVs instead of per-model. The 09-29 vPIC labelling quirk reproduced exactly (`L87 - DI DFM, ALUM, GEN 5` vs `L84 - DI, ALUM, GEN 5, VAR 2`), so the note carries the same explicit caution: the omission is a database artifact, not evidence an L84 lacks DFM. Suburban-specific addition: the long-wheelbase body puts more load on the rear air springs and their lines, so that is where the air-ride check bites hardest.

    **`ford-explorer-2020` — 8th digit, verified with two controls.** `H` = 2.3L EcoBoost turbo four, `C` = 3.0L EcoBoost turbo V6, `B` = 3.3L naturally aspirated V6, each returned off `1FMSK8D_5LG` as 2.3L/4-cyl, 3.0L/6-cyl and 3.3L/6-cyl; characters outside that set return `14 - Unable to provide information for some of the characters`. **Two controls were run and are worth recording, because they are what separates "position 8 is the engine" from "position 8 co-varies with something else":** changing **position 9** left the engine at 2.3L (it is the check digit, not powertrain data), and changing **position 7** moved the reported trim XLT -> Limited while the engine held at 2.3L (trim and engine are encoded separately). **One stated limit:** the 3.3L hybrid was not isolated — `B` returned 3.3L with `ElectrificationLevel` empty on both position-7 values tested, so displacement alone will not separate a hybrid from the gas V6. The note says so rather than guessing a hybrid character.

    **`buick-envision-2021` is the fourth manufacturer-specific failure of criterion 3's wording, and the second of a new kind.** On the 2nd-gen Envision the 8th digit carries **nothing**: substituting any other character there returns error 14 rather than a different powertrain, and there is nothing for it to fork — every U.S. 2021 Envision is the same single 2.0L turbo with the 9-speed automatic. Measured instead, one position at a time: **position 6 is the fork, and it carries the drive layout** — `R` = FWD, `S` = AWD (vPIC `DriveType: FWD/Front-Wheel Drive` and `AWD/All-Wheel Drive`, rest of VIN unchanged). Probes at positions 4 and 5 were run as controls: position 4 `F` -> `A` left DriveType at AWD, and position 5 `Z` -> `X` invalidated the pattern outright, so position 6 is the drive character and not a neighbour effect. This is buyer-relevant rather than trivia: an AWD Envision adds a rear drive unit and clutch-pack coupling with their own service history, and can produce driveline shudder a front-drive car cannot.

    **Criterion 3's wording has now failed on four manufacturers and two distinct causes, which is enough to call it a spec bug rather than a run of exceptions.** Toyota (09-13) encodes the engine at position 5. VW's MEB cars (09-29) and this Envision encode no engine anywhere — the first because a BEV has no engine family, the second because a single-engine model has nothing to distinguish — and in both the position that *does* carry buyer-relevant information is the drive layout (ID.4 position 4, Envision position 6). The proposed one-line spec edit is unchanged from 09-29: reword criterion 3 from "8th-digit engine code mapping" to **"the VIN position that actually forks this vehicle's powertrain or drive layout, identified and verified per manufacturer."** Still not edited — the spec is Daniel's contract document. Escalated again in Awaiting-Daniel with tonight's second data point.

    **A content inaccuracy found and deliberately NOT edited.** `buick-envision-2021` carries `engine: '2.0T LTG I4 (228 hp) with 9-speed automatic'`, and its Engine section reasons from that code ("Same LTG engine as Blazer"). The 2nd-gen 2021 Envision uses the **LSY** 2.0L turbo, not the 1st-gen's LTG; the two are different engine families with different oil-consumption histories, so the cross-reference to the Blazer is doing real work in the inspection copy and may be doing it wrongly. **vPIC returns no `EngineModel` string for this vehicle, so I could not verify the correct family from the primary source available tonight** — which is precisely why it is escalated rather than edited. Tonight's vinNote asserts nothing about engine family: it says "2.0L turbo" and nothing more, so nothing shipped depends on the answer.

    Sibling check: no blocking overlap. Ready blocks 09-09 -> 09-29 all touch `inspect/index.html` but are the direct ancestors of this commit, not concurrent siblings; they edit `VEHICLE_MENU` rows, keys, recalls or the render path, while this diff adds three top-level `vinNote` string fields and nothing else — 245 `CHECKLISTS` keys before and after with an identical key set, `VEHICLE_MENU` byte-unchanged, and a +3/-0 line diff in which all three added lines are `vinNote:` fields. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. `Started:` audit clean across all 26 blocks — 0 missing, no gate-block risk on `inspect/index.html`. No Re-sync needed. Verified against: autovetting-vinnote-batch-2026-09-29.

    **Scanner: PASS** (624 files, exit 0). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, **byte-identical** (`f8554c34...` before and after); no link added, removed or changed, and nhtsa.gov is cited as prose with no anchor and no `/decode/` link. **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** — unchanged from the 09-29 baseline; the vinNote-coverage warn moved 39/100 -> **41/100 (41.0%)**. **CHECKLISTS integrity:** 245 keys before and after, key set identical, all 3 added lines are `vinNote:` fields, 0 lines removed. **Menu wiring:** `VEHICLE_MENU` block byte-equal to the pre-run snapshot (md5 `1e723e3d...`), so no route could change; no route re-test needed. **Line diff vs pre-run snapshot: exactly +3, -0.** **Truncation guard:** 18,157 lines, ends `</html>`. **Commit: `711f5c3`** (parented on 09-29's `b145cde`; `main` fast-forwarded by writing the ref file directly, since the stale `.git` locks still block `git update-ref`). Diff is exactly 2 files, +3 lines in `inspect/index.html`. Commit built with `inspect/index.html` + `TASKS.md` only; `git ls-tree -r` returns nothing under `_hub/` — the 09-25 `update-index --add` ignore-bypass guard was applied.

    **PUSH: still blocked. Day 22, and the count is now 21 commits.** `GET /user` and `GET /repos/dvs-dnl/autovetting` with the stored PAT both return **401**, re-tested tonight from the local-device shell. Prefix still `ghp_krkG...`, `expires` still reads 2027-05-19, `rotated_on` still 2026-05-30 — the credentials file has not been touched since the 09-25 handoff, so the token was revoked, not expired. `origin/main` still at `0dfa937`; `main` carries everything, so the recovery is still a single `git push origin main` once a live PAT is in the credentials store.

    **NHTSA egress: unchanged from 09-29, and re-confirmed tonight.** `vpic.nhtsa.dot.gov` still fails from the local-device shell (`curl` exit 56, no HTTP response) while `api.github.com` answers from the same shell — host-specific policy, not an outage. Tonight's verification again went through the sandbox's own fetch path, which does reach vPIC, so all three vehicles' codes are primary-source verified. **That path is still not scriptable, so launch-spec criterion 5 (NHTSA recall/complaint refresh within 30 days) still cannot be run by script**, and every checklist's recall data keeps aging. Two hosts on the egress allowlist is the whole fix; no workaround attempted.

### autovetting-vinnote-batch-2026-09-29 — ready 2026-09-29 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-09-29 (02:00 MST overnight builder; launch freeze DANIEL-DECISIONS-2026-07-29 still active, so no vehicle launch is available. Took the sanctioned Step-3 alternative: drain the vinNote queue.)
- Status: ready to deploy. PUSH still blocked: the PAT is still dead (401, re-tested tonight). Day 21.
- Backlog-ref: `_hub/Content/vinnote-queue.md` priorities 97/98/99 (top of queue after the 09-28 drain).
- Task: drain 3 vinNote entries (launch-spec criterion 3, VIN decoding intelligence)
- Touched files: `inspect/index.html`, `_hub/Content/vinnote-queue.md` (gitignored), `_hub/Build-Log/2026-09-29.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-09-29 02:00 [scheduled task]: **3 vinNotes added — `chevrolet-tahoe-2021`, `gmc-yukon-2021`, `volkswagen-id4-2021`. vinNotes 113 -> 116 (47.3% of 245). Every code confirmed by single-variable NHTSA vPIC decode. One of the three is a correction to the launch spec's own premise.**

    **The deliverable, and how each code was proved.** Method throughout: construct a VIN for the target year, hold every other position constant, vary one position, and read what vPIC returns — so the character is shown to select the powertrain rather than co-vary with the VDS. **Tahoe (T1XX, 8th digit):** `D` = 5.3L **L84** V8, `L` = 6.2L **L87** V8, `T` = 3.0L **LM2** Duramax turbodiesel I6, each returned by vPIC with its engine-family string. **Yukon:** the same three characters, but re-decoded on a GMC VIN (`1GKS…`) rather than inferred from the Chevrolet — `D`/`L`/`T` returned L84 / L87 / LM2 independently, which is what licenses the note to say the encoding is platform-wide and holds on the Yukon XL. The buyer-facing fork is that `D` and `L` are both Dynamic Fuel Management cylinder-deactivation engines, so a gas T1XX is a lifter car either way, while `T` has no deactivation at all and swaps the lifter question for DPF/DEF and regen history.

    **Worth recording, because it would have become a wrong note: vPIC's own descriptor text spells out `DFM` on the L87 string (`L87 - DI DFM, ALUM, GEN 5`) and omits it from the L84 string (`L84 - DI, ALUM, GEN 5, VAR 2`).** Read literally that says the 5.3L has no cylinder deactivation, which contradicts this checklist's own DFM lifter item and is wrong. It is a labelling artifact of the database. The note states the quirk explicitly so the next reader of a raw vPIC dump does not "correct" the 5.3L into a non-DFM engine.

    **`volkswagen-id4-2021` is a criterion-3 correction, not a fill-in.** The launch spec asks for the 8th-digit engine code. **On a 2021 ID.4 the 8th digit carries nothing:** it is invariant at `2` across VW's MY2021 pattern, and substituting any other character returns `14 - Unable to provide information for some of the characters in the VIN` rather than a different powertrain. A BEV has no engine family to fork, so the habit does not transfer. Measured instead: **position 4 is the fork, and it carries trim and drive layout together** — varying position 4 alone, `D` = 1st Edition RWD, `R` = Pro RWD, `K` = Pro S RWD, `T` = Pro S RWD, **`U` = Pro S AWD** (vPIC `DriveType: AWD/All-Wheel Drive`, `ElectrificationLevel: BEV`). That makes position 4 the character that confirms single- vs dual-motor before a window sticker, which matters because AWD arrived partway through MY2021 and the 1st Edition was never built with it. This is the third instance of the 8th-digit premise failing for a specific manufacturer (Toyota, 2026-09-13; now VW's MEB cars) — see Awaiting-Daniel.

    **A content inaccuracy found and deliberately NOT edited.** `volkswagen-id4-2021` carries `engine: 'Rear-wheel drive 201 hp (62 kWh) / 295 hp (82 kWh) …'` on a `year: 2021` entry. Every MY2021 US ID.4 shipped with the 82 kWh pack; the 62 kWh Standard is a later US model year. That is a **stated spec on a stated model year**, i.e. the class of edit Decision 1 governs, so it is escalated rather than silently corrected. The vinNote asserts nothing about pack size.

    Sibling check: no blocking overlap. Ready blocks 09-09 -> 09-28 all touch `inspect/index.html` but are the direct ancestors of this commit, not concurrent siblings; they edit `VEHICLE_MENU` rows, keys, recalls or the render path, while this diff adds three top-level `vinNote` string fields and nothing else — a field-by-field compare of all 245 `CHECKLISTS` entries shows **0 non-`vinNote` differences** and `VEHICLE_MENU` is byte-unchanged. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. `Started:` audit clean across all 25 blocks — 0 missing, no gate-block risk on `inspect/index.html`. No Re-sync needed. Verified against: autovetting-vinnote-batch-2026-09-28.

    **Scanner: PASS** (623 files, exit 0). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, **byte-identical**; no link added, removed or changed (this diff adds string fields, not markup, and cites nhtsa.gov as prose, with no `/decode/` anchor). **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** — unchanged from the 09-28 baseline; the vinNote-coverage warn moved 37/100 -> **39/100 (39.0%)**. **CHECKLISTS integrity:** 245 keys before and after, key set identical, **0 non-`vinNote` field diffs**. **Menu wiring:** `VEHICLE_MENU` byte-equal to the pre-run snapshot, so no route could change; no route re-test needed. **Line diff vs pre-run snapshot: exactly +3, -0.** **Truncation guard:** 18,154 lines, ends `</html>`. **Commit: `b145cde`** (parented on 09-28's `fd25497`; `main` fast-forwarded by writing the ref file directly, since the stale `.git` locks still block `git update-ref`). Diff is exactly 2 files, +3 lines in `inspect/index.html`. Commit built with `inspect/index.html` + `TASKS.md` only; `git ls-tree -r` returns nothing under `_hub/` — the 09-25 `update-index --add` ignore-bypass guard was applied.

    **PUSH: still blocked, and tonight a SECOND blocker appeared — see below.** `GET /user` with the stored PAT returns **401 Bad credentials**; prefix still `ghp_krkG...`, `expires` still reads 2027-05-19, file mtime still 2026-05-30, so the credentials file has not been touched since the 09-25 handoff — the token was revoked, not expired. **20 commits now stuck**; `origin/main` still at `0dfa937`. `main` carries everything, so the recovery is still a single `git push origin main`. **Day 21 with nothing deployed.**

    **NEW TONIGHT — every `nhtsa.gov` host is now blocked by the session egress policy, from both shells.** `vpic.nhtsa.dot.gov`, `api.nhtsa.gov` and `www.nhtsa.gov` all fail at CONNECT (`gateway answered 403 to CONNECT`) in the cloud container and fail DNS resolution in the local-device shell; `api.github.com` answers 200 from the same shells, so this is host-specific policy, not a network outage. Tonight's verification went through the sandbox's own fetch path instead, which does reach vPIC — so the codes above are primary-source verified. **But that path is not scriptable**, which means **launch-spec criterion 5 (NHTSA recall/complaint refresh within 30 days) cannot be run by script tonight** and the `scripts/` NHTSA pullers will fail if invoked. Escalated. This does not block vinNote work, which is per-vehicle and can be verified by fetch.

### autovetting-vinnote-batch-2026-09-28 — ready 2026-09-28 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-09-28 (02:00 MST overnight builder; launch freeze DANIEL-DECISIONS-2026-07-29 still active, so no vehicle launch is available. This run first disposed of the item the 09-27 handoff put first — i91-b — then took the sanctioned Step-3 alternative.)
- Status: ready to deploy. PUSH still blocked: the PAT is still dead (401, re-tested tonight). Day 20.
- Backlog-ref: 2026-09-27 handoff, "QUEUED FOR THE NEXT RUN" item i91-b ("This should be the next run's first job") + `_hub/Content/vinnote-queue.md` priorities 94/95/96.
- Task: verify-or-refuse i91-b, then drain 3 vinNote entries (launch-spec criterion 3, VIN decoding intelligence)
- Touched files: `inspect/index.html`, `_hub/Content/vinnote-queue.md` (gitignored), `_hub/Build-Log/2026-09-28.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-09-28 02:00 [scheduled task]: **i91-b REFUSED as a verified no-op — no diff made. 3 vinNotes added, every 8th-digit code confirmed against NHTSA vPIC. vinNotes 110 -> 113.**

    **i91-b does nothing to the live page. Its mechanism is real, but only inside the catalog task's own harness (reconciled below).** The claim routed in on 09-27 was "one character, +31 deep links": change `c.year === year` to `String(c.year) === String(year)` in `findChecklistByYMMT` Path 2, because it pits a stored number against a URL-derived string. Both halves fail on inspection — `c.year` is a **number** in all 245 `CHECKLISTS` entries (246 numeric `year:` matches, **0** quoted), and the sole caller at line 18122 passes `parseInt(year, 10)`, also a number. `grep` returns exactly one definition and one call site, so there is no second caller supplying a string. Measured rather than argued: `CHECKLISTS`, `VEHICLE_MENU` and the function were extracted from the installed file into a harness and the full 338-link deep-link inventory run through a current and a `String()`-patched variant. **288/338 resolve before, 288/338 after: 0 links gained, 0 routes changed.** Shipping it would have been an empty commit that retired a real complaint and entered "+31" into the record as verified — the failure mode the recall audit spent the summer unwinding. Routed back to the catalog task's channel so it stops being re-flagged (its line number is now **17719**, not 17367 or 17720).

    **The real cross-linking defect was located, and it is not a router bug.** Scoped to the surface criterion 7 actually governs: of the **311 `inspectUrl` fields in `pinpoint/index.html`, 17 are dead**, because `model=` carries the trim (`model=Corolla LE`, `model=F-150 XL Regular Cab`). The obvious repair — longest-prefix-match the model against that year+make's menu rows, corroborated against the row's own `trim` string — was built and tested, and **the test killed it**: `2018 Toyota Prius c` scored corroborated=true and routed to `toyota-prius-2016` purely because the letter `c` occurs inside *Eco* / *Touring* / *Limited*, which hands an NHP10 buyer the ZVW50's checklist — the wrong-car class the 09-26 Wrangler fix removed; meanwhile all three links that *should* route (`Corolla Hybrid LE`, `Highlander Hybrid XLE AWD`, `Crosstrek Sport`) scored corroborated=false because their trim strings do not list those trims. False-positive on the dangerous case, false-negative on every safe one, so **the router was left alone.** Of the 17, **13 are genuine coverage gaps** (freeze-blocked: 2016 CR-Z, 2012 Mazda 5, 2021 Accent, 2020 Camaro, 2024 GR Corolla, 2018 Forester in the SJ gap, 2018 Ram DS, 2014 Suburban, 2024 Crosstrek, 2024 WRX, 2019 GTI, 2019 Golf Alltrack, 2022 Avalon Hybrid) and the other 4 are "is the Hybrid the same inspection as the base car" content calls, i.e. Decision 1. **Nothing in this class is decision-free.**

    **The deliverable: 3 vinNotes, primary-source verified.** `hyundai-elantra-2021`, `ford-bronco-2021`, `cadillac-escalade-2021` — queue priorities 94/95/96, drained at the sanctioned 1-3/run rate. Every letter->engine mapping was confirmed by decoding a constructed partial VIN through the **NHTSA vPIC `DecodeVinValues`** API with position 8 as the single variable: Elantra `G` = 2.0L MPI Nu ("MPI NU PE", decoded **clean**), `F` = 1.6L T-GDI Gamma II (trim "N Line"), `J` = 1.6L GDI Kappa (`ElectrificationLevel: Mild HEV`); Bronco `H` = 2.3L 4-cyl "TIVCT", `P` = 2.7L 6-cyl; Escalade `L` = 6.2L **L87** gasoline, `T` = 3.0L **LM2** diesel. A single-variable control (`KMHLM4A`+`F`, the 2.0L car's VDS with only position 8 changed) returns 1.6 T-GDI, confirming the 8th digit alone selects the engine rather than co-varying with the VDS. **Worth recording: I expected the 3.0L Duramax to be `M`. It is `T`** (vPIC and dieselhub agree; `LZ0` = "8") — written from memory, that note would have shipped a wrong code for the diesel. **No campaign numbers cited in any note**, per the recall-ledger rule; **no `/decode/` links**, per the launch spec; phrasing follows the current `mazda-mx5-2016` form.

    **Reconciled against the catalog task's own contradicting measurement — the +7 is its harness, not the page.** Its Run 96 log (same date) re-measured i91-b as **+7 (258 -> 265 of 308)**, "ceiling unchanged at 265", which contradicts tonight's 0. Rather than out-assert it, reproduced it: the pinpoint 311-link set was run through both function variants twice, changing only how `year` is passed. With `parseInt(year, 10)` — **what line 18122 actually does** — 294/311 before and after, **gained 0**. With the raw query string and no `parseInt` — 287/311 -> 294/311, **gained exactly 7**. The seven are **2019 Genesis G70, 2016 Chrysler 300, 2017 Porsche Macan, 2022 Rivian R1T, 2020 Land Rover Defender, 2022 Genesis GV70, 2019 Porsche Cayenne**, and **all seven resolve on the live page today.** So i91-b is real inside that task's resolver harness and absent from the site; the action item transfers to it — **apply `parseInt(year, 10)` in the harness** and its 258/308 should reach its own 265 ceiling with no change to `inspect/index.html`. Same artifact explains the earlier +31, measured before the 266-row sweep absorbed most of it.

    **Checked and NOT escalated: the 20 `key: ""` menu rows.** Tonight's audit counted 20 `VEHICLE_MENU` rows with an empty-string key, which a naive dangling-key count reports as 0 because `""` is falsy and skipped before the `CHECKLISTS` lookup. Checked the record before writing it up as a defect: the **09-25 findings doc already documents them** — it deleted one malformed `{ model: 'Mazda6', key: '' }` row that sat beside a working route for the same model, and recorded that "the ~20 other `key: ''` rows are the supported coming-soon pattern and were left alone." So this is intended behaviour: the falsy key short-circuits, Path 2 finds no year match, and the shopper gets Coming Soon. Recorded as a verified census only — **exactly 20 rows, unchanged by tonight's diff** (2008 Honda CR-V; 2009/2010 Subaru Forester; 2010/2011 Acura MDX; 2010 Jeep Wrangler JK 3.8L; 2012 VW GTI Mk6; 2013 Kia Sportage; 2013/2014/2016 VW Jetta+GLI; 2014 Chevrolet Volt; 2014-2017 Honda Odyssey ×4; 2015-2017 Subaru Crosstrek ×3; 2017 Chevrolet Equinox). None carries the Mazda6 signature (a working route for the same model beside it), so the test that justified that deletion clears all 20.

    Sibling check: no blocking overlap. Ready blocks 09-09 -> 09-27 all touch `inspect/index.html` but are the direct ancestors of this commit, not concurrent siblings; they edit `VEHICLE_MENU` rows, keys, recalls or the render path, while this diff adds three top-level `vinNote` string fields and touches nothing else — a field-by-field compare of all 245 `CHECKLISTS` entries shows **0 non-`vinNote` differences** and `VEHICLE_MENU` is byte-unchanged. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. `Started:` audit clean across all 24 blocks — no gate-block risk on `inspect/index.html`. No Re-sync needed. Verified against: autovetting-menu-missing-nameplate-sweep-2026-09-27.

    **Scanner: PASS** (621 files, exit 0). **Syntax-check: PASS** (official node recipe on the installed file, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, **byte-identical**; no link added, removed or changed (this diff adds string fields, not markup, and cites nhtsa.gov as prose rather than an anchor). **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** — unchanged from the 09-27 baseline; the vinNote-coverage warn moved 34/100 -> **37/100 (37.0%)**. **CHECKLISTS integrity:** 245 keys before and after, key set identical, 0 non-`vinNote` field diffs. **Menu wiring:** 1,356 rows unchanged, 0 orphan checklists; the 20 empty-key rows above are pre-existing and unchanged. **Route test:** all 338 deep links re-resolved before and after, **0 route resolutions changed**. **Truncation guard:** 18,151 lines, ends `</html>`. **Commit: `fd25497`** (parented on 09-27's `63c7680`; `main` fast-forwarded by writing the ref file directly, since the stale `.git` locks still block `git update-ref`). Diff is exactly 2 files, +3 lines in `inspect/index.html`. Commit built with `inspect/index.html` + `TASKS.md` only; `git ls-tree -r` returns nothing under `_hub/` — the 09-25 `update-index --add` ignore-bypass guard was applied.

    **PUSH: still blocked. Re-tested, not re-diagnosed.** `GET /user` with the stored PAT returns **401 Bad credentials**; prefix still `ghp_krkG...` and the `expires` field still reads 2027-05-19, so the credentials file has not been touched since the 09-25 handoff — the token was revoked, not expired. **19 commits now stuck**; `origin/main` still at `0dfa937`. `main` carries everything after the 09-27 fast-forward, so the recovery is still a single `git push origin main`. **Day 20 with nothing deployed.**

### autovetting-menu-missing-nameplate-sweep-2026-09-27 — ready 2026-09-27 (COMMITTED TO `main`, NOT PUSHED)

- Started: 2026-09-27 (02:00 MST overnight builder; launch freeze DANIEL-DECISIONS-2026-07-29 still active, so no vehicle launch is available. This run took the target the 09-26 handoff proposed for it: "sweep every year block for nameplates the make actually sold that year and is missing from the menu.")
- Status: ready to deploy. **`main` now carries this commit and the 8 stranded builder-ref commits** — see the repo-state note below. PUSH still blocked: the PAT is still dead (401, re-tested tonight).
- Backlog-ref: 2026-09-26 handoff — "Next run's proposed target: sweep every year block for nameplates the make actually sold that year and is missing from the menu. No decision needed for any row whose correct-generation checklist already exists — which is what made tonight's fix shippable."
- Task: close every VEHICLE_MENU nameplate gap that needs no decision (launch-spec criterion 7, cross-linking)
- Touched files: `inspect/index.html`, `_hub/Build-Log/2026-09-27.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-09-27 02:00 [scheduled task]: **266 menu rows added across 145 (year, make) blocks. Menu rows 1,090 -> 1,356. `CHECKLISTS` byte-unchanged; no row deleted, altered or re-pointed.**

    **The sweep is the deliverable, and it is exhaustive and reproducible.** For all 245 checklists x 17 year blocks: parse the generation span the 09-21 run wrote into each `trim` (243 of 245 carry one), and flag every (year, make) block that omits a nameplate whose own checklist span covers that year. The naive form of that query returns **426** hits — and shipping it would have been the fabrication pattern the recall audit spent the summer unwinding, because most of those 426 are the *wrong-generation* question (a row for that model exists and points elsewhere), which is Decision 1's territory. Two filters reduce it to what is actually decision-free:

    1. **The nameplate must be absent from the block entirely** — a true gap that returns nothing to a shopper, not a wrong answer competing with a right one. 426 -> 273.
    2. **Exactly one checklist may claim that year** — where two compete, picking one is a decision. 273 -> **266**, excluding 7 (2008-2014 Toyota Sequoia, where `toyota-sequoia-2016` and `toyota-sequoia-2022` both claim the years; the 09-13 run already found the 2022 Sequoia was authored as the 2023 car, so this span pair needs an audit, not a coin toss).

    Every added row reuses an existing checklist key and copies its `trim` **verbatim from an existing menu row for that same key** — all 111 keys had one, so no trim string was authored or inferred. Nothing new was written about any car.

    **What shoppers were getting.** The 2024 Ford block had no `F-150` row at all (only `F-150 Lightning`), so a 2024 F-150 search returned nothing while `ford-f150-2021` (2021-present) sat unreachable. The 2024 Toyota block had no `RAV4` and no `RAV4 Hybrid` (only `RAV4 Prime`). The 2023 Jeep block — the gap the 09-26 handoff spotted by hand — had no `Wrangler`, `Wrangler 4xe`, `Grand Cherokee` or `Renegade`. Those are among the highest-volume used searches in the U.S., and they were dead ends.

    **A defect this run introduced and then caught, worth recording because the fix was to the rule, not the row.** The first pass compared model names by exact lowercase, so it treated `RX 350` and `RX350` as different nameplates and added an `RX 350` row to 2015 Lexus, which already served that car as `RX350` — two dropdown entries, same checklist, same car. The near-duplicate audit caught it before commit. Rather than delete the one row, the gap test now compares model names **normalised** (non-alphanumerics stripped), which is the rule that prevents the next occurrence rather than this one. 267 -> 266 rows, 146 -> 145 blocks. The file was restored from `HEAD~1` and the sweep re-run from scratch, not patched.

    Sibling check: no blocking overlap. Ready blocks 09-09 -> 09-26 all touch `inspect/index.html` but are the direct ancestors of this commit, not concurrent siblings; they edit `CHECKLISTS` (vinNote, recalls, keys, trim) or the render path, while this diff adds `VEHICLE_MENU` rows only and leaves `CHECKLISTS` byte-identical (245 keys, verified by re-parse). In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. `Started:` audit clean across all 22 blocks — no gate-block risk on `inspect/index.html`. No Re-sync needed. Verified against: autovetting-menu-wrangler-2024-base-row-2026-09-26.

    **Scanner: PASS** (617 files, exit 0). **Syntax-check: PASS** (official node recipe, Script 2 OK / Script 5 OK, exit 0, run on the installed file). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, byte-identical; no link added, removed or changed (this diff adds data rows, not markup). **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** — unchanged from the 09-26 baseline. **Menu wiring: PASS** — 1,356 rows, 0 dangling keys, 0 empty make arrays, 0 orphan checklists. **Route test: 266/266** new routes resolve through a verbatim port of `findChecklistByYMMT` to the intended checklist, and **0 pre-existing route resolutions changed**. **Duplicate model rows still 8**, and **near-duplicate nameplate groups still 8** — the same sets, asserted set-equal before and after; none added on either measure. **Truncation guard:** 18,148 lines, ends `</html>`. Commit built with `inspect/index.html` + `TASKS.md` only; `git ls-tree -r` returns nothing under `_hub/` — the 09-25 `update-index --add` ignore-bypass guard was applied.

    **Side effect worth naming:** re-sorting the 145 touched blocks alphabetically also normalised 3 pre-existing out-of-order Mazda blocks (2017, 2019, 2020 — `MX-5 Miata` had been listed first). Unsorted blocks 5 -> 2 (2016 and 2018 Mazda remain, untouched by this run). Display order only; no route changes.

    **Left for a decision, not guessed at:** (a) the 7 Sequoia years above; (b) `volkswagen-passat-2018` and `volkswagen-golf-2018` are the only 2 checklists with no generation span in `trim`, so they are invisible to this sweep and to every future one — adding a span is a one-line fix but it asserts a year range, so it needs the facelift rule; (c) the Lexus RX is now spelled `RX 350` in 2013-2014 rows and `RX350` in 2015-2019 rows, because that is how the two checklists name themselves — normalising it is its own diff.

    **REPO STATE REPAIRED TONIGHT (no decision consumed, and it changes what the push costs you).** The 09-16 -> 09-26 runs each built a commit object and anchored it at `refs/heads/builder-2026-09-NN` because the stale `.git` lock files stop `git update-ref` from moving `main`. Eight commits were therefore sitting off `main`, reachable only by ref name. Verified `refs/heads/builder-2026-09-26` (`3b9be89`) is a strict descendant of `main` (`88deccd`) via `git merge-base --is-ancestor`, and that the working tree was already byte-identical to `3b9be89` (`git diff HEAD` empty), then fast-forwarded `main` by writing the ref file directly — a plain file write, which the sandbox permits, unlike the unlink `git update-ref` needs. `main` went `88deccd` -> `3b9be89`, then -> tonight's commit. **The whole backlog is now one `git push origin main`, with no ref archaeology.** Reversible by writing `88deccdc9d2b39c4a5d887e0ef2d5d819b6ab324` back into `.git/refs/heads/main`. The lock files themselves remain unremovable from this sandbox ("Operation not permitted") — they still freeze the index, which is why the commit is still built via `git commit-tree` on a separate index.

    **PUSH: still blocked. Re-tested, not re-diagnosed.** `GET /user` with the stored PAT returns **401 Bad credentials**; `GET /repos/dvs-dnl/autovetting` returns 401 while the same repo answers 200 unauthenticated; token prefix is still `ghp_krkG...`, so the credentials file has not been touched since 09-25. Its own `expires` field still reads 2027-05-19, so the token was revoked, not expired. Also ruled out rather than assumed: no `~/.ssh` exists, `github.com` does not resolve from this shell, `gh` is not installed, and the only other GitHub-shaped entry in `.credentials/` is a `/next/` page passphrase — that PAT is the single credential. **18 commits now stuck**; `origin/main` still at `0dfa937`. **Day 19 with nothing deployed.** Notified Daniel by push notification tonight rather than by Awaiting-Daniel alone, since 18 consecutive appends there have not reached him.

### QUEUED FOR THE NEXT RUN — routed in from the catalog task's channel (2026-09-27)

- Started: 2026-09-27 (opened by the overnight builder after reading the catalog task's run log; both items are its findings, not this task's)
- Status: queued, not started. Deliberately NOT bundled into tonight's diff — different outcome, and nothing can deploy anyway.
- Task: take the two `inspect/index.html` items the catalog job has been unable to route here
- Notes:

    **i91-b — CLOSED 2026-09-28 as a verified no-op. Do not re-open without new evidence.** Tested on 2026-09-28: `c.year` is a number in all 245 checklists and the sole caller passes `parseInt(year, 10)`, so the comparison already succeeds and the `String()` patch gains **0** of 338 deep links and changes **0** routes. The mechanism is real only inside the catalog task's resolver harness, which omits the `parseInt`: pass the year as a raw string and the patch gains exactly the +7 its Run 96 log reports; pass it through `parseInt` as line 18122 does and it gains 0. **The fix belongs in that harness, not in `inspect/index.html`.** Routed back to the catalog task's channel; its line number is now **17719**. The real dead-link cause is the trim carried in `model=` on 17 of 311 `pinpoint` `inspectUrl` fields, and a prefix-matching router was built, tested and **rejected** (it routes `2018 Toyota Prius c` to the Prius checklist) — see the 2026-09-28 Ready block.

    **i95-a — NOT the free fix the catalog log believes it is; do not just restore the cell.** It asks to restore `2021|Acura|MDX -> acura-mdx-2018`. But that checklist's `trim` reads `(YD3, 3rd gen, 2014-2020)` — it says it stops at 2020, which is why tonight's span-driven sweep correctly did not add a 2021 MDX row. Restoring the cell would hand a 2021 shopper a page that states it does not cover their car. The catalog task is very likely right on the fact (MY2021 was the last YD3; the 4th gen arrived as a MY2022 car), so the real fix is to **widen that checklist's span to 2014-2021 and then let the sweep add the row** — but that edits a stated year range, which is exactly the facelift rule Decision 1 governs. **Escalate, do not silently do.** Same shape applies to i93's `2024|Chrysler|Pacifica` and `2024|Dodge|Durango` suggestions: check each target's span before adding the cell.

### autovetting-menu-wrangler-2024-base-row-2026-09-26 — ready 2026-09-26 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Started: 2026-09-26 (02:00 MST overnight builder; launch freeze DANIEL-DECISIONS-2026-07-29 still active, so no vehicle launch is available. Awaiting-Daniel section B holds no freeze-exempt work; this run took item 2 of the 09-25 handoff — "add the missing 2024 base-Jeep-Wrangler menu row" — the one queued item needing no decision.)
- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-26`, parented on 09-25's `8563ab5`; it is NOT on `main` — the `.git` lock files are still unremovable from this sandbox. PUSH still blocked: the PAT is still dead.)
- Backlog-ref: 2026-09-25 handoff item 2 — "The 2024 Jeep block has no base Wrangler row… The fix is to *add* a 2024 base-Wrangler row; queued for next run as its own diff. No decision needed."
- Task: make `/inspect/?year=2024&make=Jeep&model=Wrangler` return the base JL checklist instead of the plug-in hybrid's (launch-spec criterion 7, cross-linking)
- Touched files: `inspect/index.html`, `_hub/Build-Log/2026-09-26.md` (gitignored), `_hub/Awaiting-Daniel.md` (gitignored), `TASKS.md`
- Notes:

    2026-09-26 02:00 [scheduled task]: **1 menu row added + 1 relabelled. Menu rows 1,089 -> 1,090. Nothing else in the file touched.** The 2024 Jeep block's only Wrangler row was labelled `Wrangler` but pointed at `jeep-wrangler-4xe-2021`, so a 2024 base-JL shopper was handed the PHEV checklist — correct generation, wrong car, invisible to every range check (both keys state JL, 2018–present / 2021–present). Added the base row -> `jeep-wrangler-2018` and relabelled the PHEV row to **`Wrangler 4xe`**, which is the form the 2021 and 2022 blocks already use (set by the 09-25 run). The relabel is not a second change: leaving the old label in place alongside the new row would have created exactly the duplicate-model-row defect 09-25 was sweeping, and relabelling *without* adding the base row was rejected on 09-25 because it turns a wrong answer into a dead route. Both halves ship together or neither works.

    Trim string on the new row is `Sport / Sport S / Sahara / Rubicon (JL)` — copied verbatim from the existing 2019 and 2020 JL rows rather than from the 2021/2022 rows, whose `… / 4xe / Unlimited (JL)` form advertises the PHEV on the base row and now has its own row to sit on. No trim was invented; MY2024 also sold Willys / High Altitude / Rubicon X / 392, which this form omits as the sibling rows do.

    Route probes before -> after: `2024 Jeep Wrangler` **`jeep-wrangler-4xe-2021` -> `jeep-wrangler-2018`** (the fix); `2024 Jeep Wrangler 4xe` **null -> `jeep-wrangler-4xe-2021`** (new, and the 4xe stays reachable from its 2021/2022 rows regardless, so nothing was ever at orphan risk); `2021`/`2022 Jeep Wrangler` + `Wrangler 4xe`, `2024 Gladiator`, `2024 Grand Cherokee` all unchanged.

    Sibling check: no blocking overlap. Ready blocks 09-16 -> 09-25 all touch `inspect/index.html` but are the direct ancestors of this commit (parented on `8563ab5`), not concurrent siblings. Those workstreams edit `CHECKLISTS` (vinNote, recalls, keys, trim) or the render path; this diff is one `VEHICLE_MENU` row, and the audit below shows `CHECKLISTS` untouched (245 keys, 1,601 items, 110 vinNotes, all unchanged). In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal. `Started:` audit clean across all 3 In-flight blocks and all 25 Done blocks — no gate-block risk on `inspect/index.html`. No Re-sync needed. Verified against: autovetting-menu-duplicate-model-rows-2026-09-25.

    **Scanner: PASS** (614 files, exit 0). **Syntax-check: PASS** (official node recipe, Script 2 OK / Script 5 OK, exit 0). **Dead-links: verified** — full `href` inventory diffed against the pre-run snapshot, byte-identical; no link added, removed or changed. **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** — unchanged by this diff. **Menu wiring: PASS** — 1,090 rows, 0 dangling keys, 0 empty make arrays, 0 orphan checklists, duplicate model rows still 8 (all decision-blocked, none added). **Line-level diff vs pre-run snapshot: exactly 1 line changed into 2**, no other line altered. **Truncation guard:** 17,796 lines, ends `</html>`. Commit built with `inspect/index.html` + `TASKS.md` only, and `git ls-tree -r <ref> | grep '^_hub/'` returns nothing — the 09-25 `update-index --add` ignore-bypass guard was applied.

    **PUSH: still blocked. Re-tested, not re-diagnosed: the 09-25 finding holds and nothing has changed.** `GET /user` with the stored PAT still returns **401 Bad credentials**; token prefix is still `ghp_krkG...`, i.e. the file has not been touched since. **17 commits now stuck**; `origin/main` still at `0dfa937`, tonight's chain ends at the commit anchored at `refs/heads/builder-2026-09-26`. Day 18 with nothing deployed.

    New finding, flagged not folded in: **the 2023 Jeep block has no Wrangler row at all** (and no Grand Cherokee row either) — `?year=2023&make=Jeep&model=Wrangler` resolves to nothing, though Jeep sold the MY2023 JL and the MY2023 WL. That is the missing-row/year-gap class the 09-17 run handled as its own sweep, not the wrong-target class fixed tonight, and a partial pass would leave nobody able to say which year blocks had been checked. Queued as next run's target: sweep every year block for makes whose model list is missing a nameplate the make sold that year. Also noted in passing, not acted on: the 2020 JL base row's trim string lists `4xe`, which was not sold in the US until MY2021.

### autovetting-menu-duplicate-model-rows-2026-09-25 — ready 2026-09-25 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Started: 2026-09-25
- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-25`, parented on 09-24's `cf62a28`; it is NOT on `main` — the `.git` lock files are still unremovable from this sandbox. PUSH still blocked.)
- Backlog-ref: 2026-09-24 handoff — "next run sweeps the whole menu for duplicate model rows inside a single year block. No decision needed."
- Touched files: `inspect/index.html`, `_hub/Build-Log/2026-09-25.md`, `_hub/Awaiting-Daniel.md`, `TASKS.md`
- Notes:

    2026-09-25 03:12 [scheduled task]: **PUSH BLOCKER RE-DIAGNOSED — the five-run "scope" diagnosis was wrong.** Tested the PAT against the GitHub API instead of inferring from a push rejection: `GET /user` returns **401 Bad credentials**, as does every repo including `dvs-dnl/trailmanual`, which the credentials file's own `scope` field claims to cover. Unauthenticated calls to the same endpoints return 200, so the network is fine and this is not the proxy, not the `.git` locks, and not scope — the token is revoked/expired/deleted at GitHub's end despite its stated `expires: 2027-05-19`. Token shape verified clean (40 chars, `ghp_[A-Za-z0-9]{36}`, no whitespace). **Blast radius is every project sharing `~/Documents/Claude/.credentials/github-config.json`** — trailmanual, commonladder, iammeek, ai-tools are almost certainly failing silently too, since 09-09. The single fix is regenerating the PAT; adjusting a grant cannot help. Also established: `dvs-dnl/autovetting` is a public repo (unauth reads 200).

    2026-09-25 03:12: **completed the duplicate-menu sweep 09-24 queued. Real count is 12**, across 1,090 rows / 17 year blocks. **Fixed 4, none consuming a decision.** (1) Deleted the malformed 2014 Mazda `{ model: 'Mazda6', key: '' }` row that sat beside a working `mazda-mazda6-2018` route — the dropdown listed "Mazda6" and "Mazda6 (coming soon)" together; same shape as the duplicate Mazda3 deleted 09-23. Rows 1090→1089. Distinguished deliberately from the ~20 legitimate `key: ''` coming-soon rows, which are a supported pattern (`renderComingSoon`) and were left alone. (2–4) Relabelled three rows whose model string was wrong but whose route was right: **2021 Jeep Grand Cherokee** WL row → **"Grand Cherokee L"** (our own trim string already stated "2021 WL is sold only as the three-row Grand Cherokee L"; 2022 and 2024 GC rows deliberately untouched since the WK2 is gone by then), and the **2021 + 2022 Jeep Wrangler** PHEV rows → **"Wrangler 4xe"**. Verified non-breaking before editing: `findChecklistByYMMT` returns the first model-name match in a block, so `?year=2021&make=Jeep&model=Wrangler` → `jeep-wrangler-2018`, `?year=2021&make=Jeep&model=Grand Cherokee` → `jeep-grand-cherokee-2014`, `?year=2014&make=Mazda&model=Mazda6` → `mazda-mazda6-2018` all resolve to the surviving row before and after. All three relabelled keys confirmed still reachable — no orphan created. Duplicates 12→8.

    **Left the remaining 8 alone on purpose:** each is two checklists for the *same generation*, which is exactly what the open decisions govern. **Decision 1 (facelift rule), 7 rows** — 2022 + 2024 Hyundai Elantra (both CN7), 2022 Kia Stinger (both CK), 2023 + 2024 Honda Passport, 2024 Kia Telluride (both 1st-gen ON), 2024 Tesla Model Y. **Decision 2 (2019 GM naming split), 1 row** — 2019 Chevrolet Silverado 1500 (`chevrolet-silverado-2014` K2XX out of its own 2014–2018 range, alongside the T1XX car; GM really did sell both that year as the "Silverado 1500 LD", so this is Decision 2's substance, not a phantom).

    **Two defects found in passing, neither acted on, both handed off.** (a) Contradictory generation spans inside two of the duplicate pairs — `honda-passport-2019` says "2019-2025" while `honda-passport-2023` says "2nd gen, 2022–present"; `tesla-model-y-2021` says "2020-2025, before the Juniper refresh" while `tesla-model-y-2022` says "2022–present". Wrong whichever way Decision 1 lands, so fixable independently. (b) **The 2024 Jeep block has no base Wrangler row** — its only Wrangler row points at `jeep-wrangler-4xe-2021`, so a 2024 base-JL buyer is handed the PHEV checklist. Same class as the 09-24 Challenger find: correct generation, wrong checklist, invisible to every range check. Left the label as `Wrangler` deliberately — renaming it for consistency would have turned a wrong answer into a dead route. The fix is to *add* a 2024 base-Wrangler row; queued for next run as its own diff.

    Sibling check: no blocking overlap. Ready blocks 09-16 → 09-24 all touch `inspect/index.html` but are the direct ancestors of this commit (parented on `cf62a28`), not concurrent siblings — this diff applies on top of them. In-flight `autovet-competitor-monitor` (`Competitors/`), `autovet-cpo-protocol-ingestion` (`Product/CPO-Protocols/`) and `autovet-seo-content` (`Content/blog/`) are orthogonal — none writes `inspect/index.html`. Done (last 10) swept for missing `- Started:` fields: none missing. No Re-sync needed. Verified against: autovetting-menu-phantom-2024-rows-2026-09-24.

    Run interruption: the device bridge dropped after the read-only sweep and before any edit, then reconnected; no partial state was written during the gap.

    **Scanner: PASS** (612 files, exit 0). **Syntax-check: PASS.** **Dead-links: verified** (no new hrefs added). Deploy gate: **27 passed, 2 warned, 0 CRITICAL failed** — unchanged by this diff.

    **Near-miss, and a standing guard for this task's commit pattern.** `_hub/` is gitignored and `dvs-dnl/autovetting` is public, but `git update-index --add` — which this task must use because the `.git` locks block a normal `git add` — **does not consult `.gitignore`**. Passing the build log and Awaiting-Daniel to it produced commit object `8819e51` carrying 1,517 lines of internal planning material (competitor analysis, CPO protocols, the Daniel handoffs). Caught on diff review before the ref was anchored; rebuilt as `d4e804c` with `inspect/index.html` + `TASKS.md` only, and the bad object is unreferenced. Audited the entire stuck chain and `origin/main`: **zero `_hub/` paths in any commit, ever** — no leak has occurred. Future runs: pass only tracked, non-ignored paths to `update-index --add`, and run `git ls-tree -r --name-only <ref> | grep '^_hub/'` before `update-ref`.

    **PUSH: blocked, but the diagnosis above supersedes the prior five.** **16 commits now stuck**; `origin/main` still at `0dfa937`, tonight's chain ends at the commit anchored at `refs/heads/builder-2026-09-25`.

### autovetting-menu-phantom-2024-rows-2026-09-24 — ready 2026-09-24 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-24`, parented on 09-23's `9cf14ee`; it is NOT on `main` — the .git lock files are still unremovable from this sandbox. PUSH still blocked, unchanged since 09-09. Do not re-diagnose; the 09-21 push-by-hash test settled it as the token.)
- Started: 2026-09-24 (02:00 MST overnight builder; launch freeze still active. Awaiting-Daniel section B holds no freeze-exempt work — B.1–B.4 closed 09-15, B.5/B.7 need a new Inspect checklist — so the run took item 1 of the 09-23 handoff: the three out-of-range rows that "look like phantom model years, not wrong generations" and which 09-23 deliberately left unverified.)
- Task: verify and delete the three phantom 2024 `VEHICLE_MENU` rows, and keep the checklist one of them was the only route to reachable (launch-spec criterion 7, cross-linking)
- Touched files: inspect/index.html, _hub/Build-Log/2026-09-24.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-24 02:00: **3 phantom menu rows deleted + 1 re-route that had to come with them. Out-of-range menu rows 24 -> 21. Menu rows 1,093 -> 1,090.**
    **Re-derived the 24 independently before touching anything** — same parser logic run fresh against the current file; it reproduced the 09-23 figure exactly (24 rows, 245 checklists, 243 parseable spans, 1,093 menu rows), including the `toyota-sequoia-2022` literal-escape case 09-23 recorded (tonight's parser normalises `\u2013` as well as the en-dash, so the 2024 Sequoia row is in the list rather than silently dropped).
    **Each of the three verified per row, to the standard the 09-22 deletions met, plus a second independent US-market check.** 09-23 named all three from a single search and explicitly refused to act on it. "Production ended" and "no US model year was sold" are not the same claim, so every row got a named production-date source AND an EPA-certification check (every model year sold in the US must be certified):
    - **2024 Chrysler 300** -> `chrysler-300-2016` (LD, 2011-2022). Final 300C off the Brampton line **8 Dec 2023**, a Velvet Red MY2023, per Stellantis' own announcement. No MY2024 EPA listing. DELETED.
    - **2024 Dodge Challenger** -> `dodge-challenger-2023` (LC, 2008-2023). Challenger production ended at Brampton **22 Dec 2023**, final car a MY2023 SRT Demon 170; Stellantis announced MY2023 as the final model year in Nov 2021. No MY2024 EPA listing. DELETED.
    - **2024 Kia Stinger** -> `kia-stinger-2022` (CK, 2018-2023). Kia ended production **April 2023**; Kia's own release titles the run-out car "THE LAST OF THEM: 2023 Stinger Tribute." No MY2024 Stinger on fueleconomy.gov. DELETED. **This is the one that needed the second check** — a secondary source claimed some markets "marketed those cars as 2023 or 2024 Tribute models," which is exactly the inference-hardening-into-assertion shape this project keeps catching (08-03 §4, 08-13 TrustPilot, 08-20 CARCHEX BBB). Not accepted either way; EPA certification and Kia's own press release settle it as a 2023.
    **The Challenger deletion would have orphaned a checklist, and it was caught BEFORE the edit rather than by the gate afterwards.** `dodge-challenger-2023` was reachable from **exactly one** menu row — the phantom 2024 one. Deleting it alone takes `gate-check.py` G-orphan to CRITICAL FAIL and blocks the entire backlog at deploy time: the identical defect 09-22 shipped with the Trax row and 09-23 had to repair. Fix is not to keep a phantom year alive: **the 2023 Dodge Challenger row was re-pointed from `dodge-challenger-2018` to `dodge-challenger-2023`**, which is where it always should have gone. Both checklists state LC 2008-2023, so neither is out of range and **no range check could ever see this** — the 2023 dropdown was handing buyers the 2018-era checklist while the purpose-built MY2023 entry, whose own trim string names the **Last Call editions** that exist only in that model year, sat unreachable behind a car that was never built. Trim on the re-pointed row taken from the target checklist's own trim list rather than from the deleted 2024 row: the usual rule is to copy the form the target generation's sibling rows use, this key has no sibling rows, and its only prior menu row was the phantom one being deleted.
    **Reachability checked for the other two before deleting:** `chrysler-300-2016` keeps its 2016 and 2015 rows; `kia-stinger-2022` keeps its 2022 row. Neither deletion orphans anything.
    The 2024 Chrysler and 2024 Dodge entries were each that make's **only** 2024 row, so both make keys were removed with them rather than left as `'Chrysler': []` — same call the 09-22 run made on INFINITI. An empty make in the dropdown is a dead end, not a smaller bug.
    Sibling check: Verified against: autovetting-menu-reroute-and-orphan-repair-2026-09-23 (direct parent; this run consumes its handoff item 1 and its orphan-repair lesson — zero row-level overlap, none of tonight's four rows is one that run added or deleted), autovetting-menu-phantom-year-rows-2026-09-22 (the prior phantom-deletion pass; same change class, disjoint row set), autovetting-checklist-generation-spans-2026-09-21 (spans are read, not modified), autovetting-menu-generation-and-year-gap-fix-2026-09-17, autovetting-pinpoint-dead-route-repair-2026-09-16, autovetting-pinpoint-filter-cells-B1-B4-2026-09-15, autovetting-vinnote-batch-2026-09-09/09-10/09-11/09-12/09-14, autovetting-inspect-render-and-generation-fix-2026-09-13, autovetting-inspect-key-namespace-rename-2026-09-03, autovetting-phase-copy-and-template-fix-2026-08-14 — all touch inspect/index.html, all unpushed, all present in this working tree; tonight's commit is parented on `9cf14ee` so every one stays in the chain. No conflict: those workstreams edit `CHECKLISTS` (vinNote, recalls, keys, trim) and the byte-identity check below proves the entire `CHECKLISTS` region is unchanged. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal. **`Started:` audit clean** across all In-flight and Done (last 10) blocks — no gate-block risk on inspect/index.html. No Re-sync needed.
    Gates: **Syntax-check: PASS** (official node recipe on inspect/index.html, Script 2 OK / Script 5 OK, exit 0). **Scanner: PASS** (`scan_for_secrets.py`, 610 files, no secrets detected, exit 0). **Dead-links: verified N/A** — full `href` inventory diffed against the pre-run snapshot, byte-identical; no link added, removed or changed. **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** (unchanged from 09-23). **Read-back: PASS 245/245** — every entry parses and carries year/make/model/trim/sections; **1,601 items and 110 vinNotes, both unchanged**. **`CHECKLISTS` region byte-identical to the pre-run file** — nothing outside `VEHICLE_MENU` was touched. **Line-level diff vs pre-run snapshot: exactly 3 lines removed, 1 line changed**, no other line altered. **Menu wiring: PASS** — 1,090 rows, **0 dangling keys, 0 empty make arrays, 0 orphan checklists**. **Truncation guard:** 17,796 lines, ends `</html>`.
    Milestone: the no-decision subset of Tier D is **closed for the second and final time** — 09-22 closed it for phantom rows visible without verification, 09-23 closed the re-route subset, and tonight clears the last three that needed research. **All 21 survivors now require a Daniel decision (1 or 2) or a checklist the freeze blocks. There is no further `VEHICLE_MENU` work available to this task without one of those.**
    New finding, flagged not folded in: **the 2022 dropdown carries two "Stinger" rows** (`kia-stinger-2018` and `kia-stinger-2022`). Both state CK 2018-2023, so both are in range and **no range check can see it** — same defect class as the 2018 Mazda3 duplicate 09-23 deleted, and like that one it surfaced by accident. Next run should sweep `VEHICLE_MENU` for duplicate model rows within a single year block, since two have now been found by luck and nobody knows the count.
    **PUSH: still blocked, not re-diagnosed.** Per the 09-21 settled finding the blocker is the token, not the `.git` locks. **15 commits now stuck**; `origin/main` still at `0dfa937`, tonight's chain ends at `cf62a28` (anchored at `refs/heads/builder-2026-09-24`). Chain intact: `cf62a28 -> 9cf14ee -> 3e22675 -> f73cd97 -> 45222cd -> 15010b3 -> 88deccd`.

### autovetting-menu-reroute-and-orphan-repair-2026-09-23 — ready 2026-09-23 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-23`, parented on 09-22's `3e22675`; it is NOT on `main` — the .git lock files are still unremovable from this sandbox. PUSH still blocked, unchanged since 09-09. Do not re-diagnose; the 09-21 push-by-hash test settled it as the token.)
- Started: 2026-09-23 (02:00 MST overnight builder; launch freeze still active. Awaiting-Daniel section B holds no freeze-exempt work — B.1–B.4 closed 09-15, B.5/B.7 need a new Inspect checklist — so the run took item 1 of the 09-22 handoff: "re-routes with an existing correct target… that subset can ship without waiting on anyone.")
- Task: re-route the out-of-range `VEHICLE_MENU` rows that have a correct-generation checklist already in the file, and repair the orphan the 09-22 run left behind (launch-spec criterion 7, cross-linking)
- Touched files: inspect/index.html, _hub/Build-Log/2026-09-23.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-23 02:00: **4 out-of-range rows fixed + 1 orphan checklist re-reached. Out-of-range menu rows 28 → 24.**
    **Re-derived the 28 independently before touching anything.** Same parser logic run fresh against the current file; it reproduced the 09-22 figure exactly — 28 rows, 243 of 245 checklists carrying a parseable generation span, the two unparseable ones still `volkswagen-passat-2018` and `volkswagen-golf-2018`. One parser correction was needed to get there: `toyota-sequoia-2022` writes its span with literal `–` escape sequences rather than the en-dash character, which renders correctly in the browser but is invisible to a naive text scan. A parser that misses it reports 27 and silently drops the 2024 Sequoia row from the blocked list.
    **Swept all 28 for the shape the 09-22 handoff named — an in-range, correct-generation checklist that already exists. Exactly four qualify, and all four shipped:**
    · **2020 Kia Sorento** → `kia-sorento-2016` ✅ (UM 3rd gen, 2016-2020). Was routing to `kia-sorento-2021` (MQ4, 2021–present). **This corrects a 09-22 judgment:** that run's handoff recorded "no UM checklist exists" and filed the row as needing a new build. The UM checklist has been in the file all along. Verified: MQ4 debuted March 2020 globally and reached US dealerships as the MY2021 redesign; US MY2020 is UM.
    · **2015 Lexus RX 350** → `lexus-rx350-2011` ✅ (AL10 3rd gen, 2010-2015). Was routing to `lexus-rx350-2019` (AL20, 2016-2022). Verified: AL10 ran MY2010–2015, AL20 began at MY2016.
    · **2014 Acura MDX** → `acura-mdx-2018` ✅ (YD3 3rd gen, 2014-2020). Was routing to `acura-mdx-2022` (YD4, 2022–present). This is the row the 09-22 handoff named as "the cleanest of these"; it needed no decision and it needed none on re-examination.
    · **2018 Mazda3** — **deleted, not re-routed.** The row pointed at `mazda3-2019` (BP, 2019-2023), but 2018 already carried a second, correct `Mazda3` row pointing at `mazda3-2014` (BM/BN, 2014-2018). Re-routing would have produced two identical rows; the dropdown was showing **"Mazda3" twice in 2018** with different trims and one of them wrong. Deletion is the only fix that does not create a duplicate. Decision 1's own text exempts this row explicitly ("Mazda3 2018 (BM is correct)"), so no decision was needed. Deep-link behaviour is unchanged: `findChecklistByYMMT` takes the **first** matching menu row, which was already the correct `mazda3-2014` one — so `/inspect/?year=2018&make=Mazda&model=Mazda3` (a live Pinpoint link) resolved correctly before and resolves correctly now.
    Trim strings on the three re-routed rows were replaced with the form the target generation's sibling rows already use, verbatim — one form per generation, the same rule the 09-22 Sierra addition followed. The three old trim strings all described the *wrong* generation's trims (the 2015 RX row advertised "Executive," which is not a US RX trim in any year).
    **Separately: repaired a CRITICAL deploy-gate failure the 09-22 run introduced.** Deleting the phantom "2023 Chevrolet Trax" row removed the **only** menu route to `chevrolet-trax-2024`, orphaning that checklist — `gate-check.py` G-orphan went CRITICAL FAIL and **would have blocked the entire 14-commit backlog at deploy time the moment the PAT is fixed.** Added the missing **2024 Chevrolet Trax** row → `chevrolet-trax-2024` ✅; the checklist's own trim string states "2nd gen, 2024–present" and the 09-22 run's own research established GM skipped MY2023 for the MY2024 VSS-F car, so the correct year row is 2024 and it was simply never added. Trim copied from the deleted 2023 row verbatim (`LS / LT / RS / ACTIV`). Gate now **27 passed, 2 warned, 0 CRITICAL failed**.
    Sibling check: Verified against: autovetting-menu-phantom-year-rows-2026-09-22 (direct parent; this run consumes its handoff list and **repairs the orphan it created** — the only file-level overlap, and the row-level set diff below proves none of tonight's four fixes touches a row that run deleted or added), autovetting-checklist-generation-spans-2026-09-21 (spans are read, not modified), autovetting-menu-generation-and-year-gap-fix-2026-09-17 (the other `VEHICLE_MENU` row edit in the chain; zero row-level overlap), autovetting-pinpoint-dead-route-repair-2026-09-16, autovetting-pinpoint-filter-cells-B1-B4-2026-09-15, autovetting-vinnote-batch-2026-09-09/09-10/09-11/09-12/09-14, autovetting-inspect-render-and-generation-fix-2026-09-13, autovetting-inspect-key-namespace-rename-2026-09-03 — all touch inspect/index.html, all unpushed, all present in this working tree; tonight's commit is parented on `3e22675` so every one stays in the chain. No conflict: those workstreams edit `CHECKLISTS` (vinNote, recalls, keys, trim) and the field-level diff below proves `CHECKLISTS` is byte-identical after this run. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal. **`Started:` audit clean** across all In-flight and Done (last 10) blocks — no gate-block risk on inspect/index.html. No Re-sync needed.
    Gates: **Syntax-check: PASS** (official node recipe on inspect/index.html, Script 2 OK / Script 5 OK, exit 0). **Scanner: PASS** (`scan_for_secrets.py`, 605 files, no secrets detected, exit 0). **Dead-links: verified N/A** — full `href` inventory diffed against the pre-run snapshot, byte-identical; no link added, removed or changed. **Deploy gate `scripts/gate-check.py`: 27 passed, 2 warned, 0 CRITICAL failed** (was 26/2/**1 CRITICAL FAIL** before this run). **Read-back: PASS 245/245** — every entry parses and carries year/make/model/trim/sections; **1,601 items and 110 vinNotes, both unchanged**. **Field-level diff vs pre-run snapshot: PASS** — `CHECKLISTS` key set identical and **0 of 245 checklist objects changed**; menu row-level set diff = exactly **4 removed, 4 added**, no other row altered. **Menu wiring: PASS** — 1,093 rows, **0 dangling keys, 0 empty make arrays, 0 orphan checklists**. **Truncation guard:** 17,799 lines, ends `</html>`.
    Milestone: the re-route subset of Tier D is **closed** — all 28 out-of-range rows have been swept and the four with an existing correct target are fixed. Each of the 24 survivors now needs a Daniel decision (1, 2 or 3), or a checklist the freeze blocks. **Three of the 24 look like phantom model years rather than wrong generations** (2024 Chrysler 300, 2024 Dodge Challenger, 2024 Kia Stinger — all three nameplates appear to have ended at MY2023) and are queued for verification next run, not acted on tonight, to keep this diff one change class.
    **PUSH: still blocked, not re-diagnosed.** Per the 09-21 settled finding the blocker is the token, not the `.git` locks. **14 commits now stuck**; `origin/main` still at `0dfa937`, tonight's chain ends at `9cf14ee` (anchored at `refs/heads/builder-2026-09-23`).

### autovetting-menu-phantom-year-rows-2026-09-22 — ready 2026-09-22 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-22`, parented on 09-21's `f73cd97`; it is NOT on `main` — the .git lock files are still unremovable from this sandbox. PUSH still blocked, unchanged since 09-09. Do not re-diagnose; the 09-21 push-by-hash test settled it as the token.)
- Started: 2026-09-22 (02:00 MST overnight builder; launch freeze still active. Awaiting-Daniel section B holds no freeze-exempt work — B.1–B.4 closed 09-15, B.5/B.7 need a new Inspect checklist — so the run took Tier D, the target the 09-21 handoff named explicitly as "the biggest thing on the board.")
- Task: delete the `VEHICLE_MENU` rows that offer a model year the manufacturer never sold in the US, and add the missing 2014 GMC Sierra 1500 row (launch-spec criterion 7, cross-linking)
- Touched files: inspect/index.html, _hub/Build-Log/2026-09-22.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-22 02:00: **10 phantom menu rows deleted + 1 missing year row added. Nothing else in the file touched.**
    Out-of-range menu rows **38 → 28**. Menu rows **1,102 → 1,093**. The ten deleted rows offered buyers a car that was never built: selecting the year returned a real, authoritative-looking checklist for a different generation of a vehicle that did not exist in that model year.
    **Re-derived the 38 independently before touching anything** rather than trusting the 09-21 figure — same parser logic run fresh against the current file, and it reproduced all 38 rows exactly. The nine 09-21 judgments held.
    Deleted (each verified by web search this run, source named): **2021 Acura MDX** (4th-gen YD4 went on sale Feb 2021 as a MY2022; Acura skipped MY2021 entirely) · **2021 INFINITI QX60** (L50 ended MY2020, L51 launched MY2022; Infiniti skipped MY2021, as Nissan did with the Pathfinder) · **2022 + 2023 Mazda6** (Mazda ended Mazda6 production at the close of MY2021; 18,504 sold in its final year) · **2014 Acura TLX** (first TLX was MY2015, built from July 2014, replacing the TL and TSX) · **2015 Lexus UX** (UX is an all-new MY2019 nameplate; NA production began Q4 2018) · **2020 Kia Seltos** (US Seltos is MY2021–present; global production from 2019 did not reach the US market) · **2021 Genesis GV70** (production began 2021, first sold as MY2022) · **2020 Ram 1500 TRX** (TRX debuted as a MY2021; production started Dec 2020) · **2023 Chevrolet Trax** (GM ended the 1st gen after MY2022 and skipped MY2023 while developing the VSS-F 2nd gen for MY2024).
    The 2021 INFINITI row was the make's only 2021 entry, so the empty `'INFINITI': []` key was removed with it — an empty make in the dropdown is a dead end, not a smaller bug.
    Added: **2014 GMC Sierra 1500** → `gmc-sierra-2014` ✅. The K2XX platform entered production for MY2014 and the checklist states 2014-2018, but the menu's Sierra rows started at 2015 — the year-gap the 09-17 run was closing, and the sibling Chevrolet Silverado already had its 2014 row. Trim string matches the 2015–2019 Sierra rows verbatim (`SLE / SLT / Denali (K2XX)`) — one form, not two.
    **Scope held deliberately.** The remaining 28 rows are a different change class and each needs its own per-row judgment: they route a year to a car that *does* exist, just in the wrong generation, so the fix is a re-route or a delete depending on whether a correct-generation checklist exists. Several are blocked on Decision 1 (facelift rule), Decision 2 (2019 GM naming split) or the launch freeze (`toyota-avalon-2018` ×4 and `mercedes-benz-gla-2020` ×3 have no correct target checklist to re-route to). Folding them in would have mixed delete-because-phantom with re-route-because-wrong-generation in one diff and cost the clean field-level proof below.
    Sibling check: Verified against: autovetting-checklist-generation-spans-2026-09-21 (this run is the direct consumer of its spans and of the Tier D list it handed off — the spans are read, not modified), autovetting-menu-generation-and-year-gap-fix-2026-09-17 (the only other `VEHICLE_MENU` row edit in the chain: it deleted 6 wrong-generation rows and added 19 year-rows; **zero overlap** — none of tonight's 10 deletions or 1 addition touches a row that run created or removed, confirmed by row-level set diff), autovetting-pinpoint-dead-route-repair-2026-09-16, autovetting-pinpoint-filter-cells-B1-B4-2026-09-15, autovetting-vinnote-batch-2026-09-09/09-10/09-11/09-12/09-14, autovetting-inspect-render-and-generation-fix-2026-09-13, autovetting-inspect-key-namespace-rename-2026-09-03 — all touch inspect/index.html, all unpushed, all present in this working tree; tonight's commit is parented on 09-21's `f73cd97` so every one stays in the chain. No conflict: those workstreams edit `CHECKLISTS` (vinNote, recalls, keys, trim), and the field-level diff below proves `CHECKLISTS` is byte-identical after this run. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal. **`Started:` audit clean** across all 14 Done (last 10) blocks and all 3 In-flight blocks — no gate-block risk on inspect/index.html. No Re-sync needed.
    Gates: **Syntax-check: PASS** (official node recipe on inspect/index.html, Script 2 OK / Script 5 OK, exit 0). **Scanner: PASS** (`scan_for_secrets.py`, 602 files, no secrets detected, exit 0). **Read-back: PASS 245/245** — every entry parses and carries year/make/model/trim/sections; 1,601 items, unchanged. **Field-level diff vs pre-run snapshot: PASS** — `CHECKLISTS` key set identical and **0 of 245 checklist objects changed**; menu row-level set diff = exactly **10 removed, 1 added, 0 trim changes on surviving rows**. **Menu wiring: PASS** — 1,093 rows, **0 dangling keys, 0 empty make arrays**. **Truncation guard:** 17,798 lines, ends `</html>`. **Dead-links: verified N/A** — `href` inventory diffed against the pre-run file, byte-identical; no link added, removed or changed.
    Milestone: the zero-decision subset of Tier D is **closed**. Every remaining out-of-range row now requires either a Daniel decision or a checklist that the freeze blocks — there is no further menu work available without one of those.
    **PUSH: still blocked, not re-diagnosed.** Per the 09-21 settled finding the blocker is the token, not the `.git` locks. **13 commits now stuck**; `origin/main` still at `0dfa937`, tonight's chain ends at `3e22675` (anchored at `refs/heads/builder-2026-09-22`).

### autovetting-checklist-generation-spans-2026-09-21 — ready 2026-09-21 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-21`, parented on 09-17's commit; it is NOT on `main` — the .git lock files are still unremovable from this sandbox. PUSH still blocked, unchanged since 09-09.)
- Started: 2026-09-21 (02:00 MST overnight builder; launch freeze still active. Awaiting-Daniel section B holds no freeze-exempt work — B.1–B.4 closed 09-15, B.5/B.7 both need a new Inspect checklist — so the run took the target the 09-17 handoff named.)
- Task: give every Inspect checklist a machine-parseable US-market generation year span in its `trim` string, so the generation range-check can see every resolving route instead of half of them (launch-spec criterion 7, cross-linking)
- Touched files: inspect/index.html, _hub/Build-Log/2026-09-21.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-21 02:00: **116 generation spans authored + 1 open-ended convention normalised = 117 `trim` fields changed. Nothing else in the file touched.**
    Checklists stating a parseable span **127 → 243 of 245**. Range-check visibility on Pinpoint routes **141/294 → 292/294 (48.0% → 99.3%)**.
    Across the 151 newly-visible routes the out-of-range check found **zero new mis-routing** — the only hit is the already-escalated #281 Silverado 1500 WT Crew 2019 (Decision 2, 09-17). The half that had never been checkable was clean.
    **HEADLINE FINDING, and it is not the spans:** with 243 of 245 entries stating their own years, crossing `VEHICLE_MENU` year rows against the target checklist's span became possible for the first time. **38 menu rows across 32 checklists route a model year outside the target's stated generation span** — the same defect class as the 09-16 🔴, on a much larger surface than Pinpoint (the menu exercises every year in the dropdown, not just years a card links to). 11 checklists / 12 rows surfaced by tonight's spans; 21 checklists / 26 rows pre-existing and invisible until this check existed. Nine of the 38 are rows for **model years that never existed** (2021 MDX, 2021 QX60, 2022/2023 Mazda6, 2014 TLX, 2015 UX, 2020 Seltos, 2021 GV70, 2020 TRX, 2023 Trax). Full list + per-row judgments in Build-Log/2026-09-21.md.
    NOT acted on: fixing those means deleting/re-routing menu rows — a different change class, several blocked on Decision 1 (facelift rule) or Decision 2 (2019 GM naming split), and the Avalon/GLA rows are freeze-blocked because the correct target checklist does not exist. Handed off as Tier D rather than folded into a diff that is currently 117 `trim` fields and nothing else.
    Verification: two independent WebSearch passes over 50 generations **before** any file was touched, plus a third pass on four cases the menu cross-check flagged. **Verification changed the answer 9 times** — cx5-2017 KF (drafted 2017–present, actual 2017-2025), lexus-es-2019 (2019-2025), audi-q5-2018 (2018-2025), malibu-2016 (2016-2025 not 2024), outback-2020 BT (2020-2025), telluride-2020 (2020-2025; Kia skipped MY2026 entirely), model-y-2021 (2020-2025), qx60-2018 L50 (2014-2020 — MY2013 was the JX35), kicks-2019 P15 (2018-2024, the P15 ran on for 2025 as the Kicks Play). Each would have shipped as a fabricated year.
    REFUSED 2, both Volkswagen: `volkswagen-passat-2018` (the US car was never the European B8/MQB — it is the NMS, MY2012–2019 with a 2016 facelift then a MY2020–2022 reskin, and sources split on whether the facelift starts a generation; no defensible single span for a 2018) and `volkswagen-golf-2018` (the trim list mixes Golf and GTI, whose US Mk7.5 runs differ — one span cannot be right for both). These are the only 2 routes the range-check still cannot see; that is the cost of not inventing a fact to make a gate go green.
    Catalog corrections made in passing, flagged not silent: removed **M340i** from `bmw-3series-2018` (a G20 trim, 2020+; the F30's top trim was the 340i); `ford-fusion-2017` "6th gen" → "2nd-gen North American Fusion"; `nissan-frontier-2018` dropped the wrong "3rd gen" ordinal, kept D40; `honda-passport-2019` "2nd gen" → "crossover-era Passport" rather than silently renumbering it 3rd (Daniel's call).
    Flagged, NOT swept: `toyota-rav4-2019` (in the pre-existing ranged set) states "2019–2024"; verified the XA50 ran through MY2025, so it now disagrees with its own hybrid sibling. Re-verifying the 127 pre-existing spans is a separate scoped job — a half-sweep would leave nobody able to say which had been checked.
    Sibling check: Verified against: autovetting-menu-generation-and-year-gap-fix-2026-09-17, autovetting-pinpoint-dead-route-repair-2026-09-16, autovetting-pinpoint-filter-cells-B1-B4-2026-09-15, autovetting-vinnote-batch-2026-09-09/09-11/09-12/09-14, autovetting-inspect-render-and-generation-fix-2026-09-13, autovetting-inspect-key-namespace-rename-2026-09-03 — all touch inspect/index.html, all unpushed and all present in this working tree; tonight's commit is parented on 09-17's so every one stays in the chain. No conflict: field-level diff proves only `trim` changed, and none of those workstreams edits `trim` (they touch vinNote, recalls, VEHICLE_MENU rows and key namespaces). The one prior `trim` edit in Done — wave-20's mazda-cx5-2017 "dropped Signature" correction — is preserved verbatim; I appended years to the corrected list, not the original. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all orthogonal. `Started:` audit clean across all 14 Done blocks and all 3 In-flight blocks. No Re-sync needed.
    Gates: **Syntax-check: PASS** (official node recipe, Script 2 OK / Script 5 OK, exit 0). **Scanner: PASS** (597 files, no secrets, exit 0). **Read-back: PASS 245/245**, 0 entries missing a core field. **Field-level diff vs pre-run snapshot: PASS** — 117 trim fields changed, 0 unintended, 0 year/make/model changes, 0 entries added or removed. **Self-consistency: PASS 245/245** — no entry's own `year` sits outside its own stated span. **VEHICLE_MENU wiring unchanged** — 1,102 key refs → 245 real keys, 0 dangling (21 non-resolving refs are pre-existing `key: ''` coming-soon placeholders). **Truncation guard:** 17,806 lines, ends `</html>`. **Dead-links: N/A** — no href added, removed or changed.
    Coverage limit, stated plainly: **91 of the 292 checkable routes sit on an open-ended `-present` span**, so a too-*new* year cannot be caught on those. Inherent to a generation still in production; it shrinks on its own as each generation ends.
    Milestone: the 09-17 handoff target is **closed** — every checklist states its generation span except the two deliberately refused, and the range-check is no longer half-blind. Next: Tier D (the 38 menu rows) and Tier E (re-verify the 127 pre-existing spans).
    **PUSH BLOCKER SETTLED (open since 09-09).** Attempted `git push origin <commit>:refs/heads/main` by hash — that needs no local ref to move, so the unremovable `.git` locks were irrelevant to the attempt. GitHub answered `Invalid username or token. Password authentication is not supported for Git operations.` **The token is the blocker; the lock files are not.** Token = prefix `ghp_krkG...`, rotated 2026-05-29, expires 2027-05-19; its own `scope` field names trailmanual/commonladder/iammeek/ai-tools and NOT autovetting (possibly stale, worth checking at regeneration). Retired a bad test in the process: `git ls-remote` succeeds on autovetting and trailmanual, but both are public so git never asks for a credential and the askpass helper never fires — the prior "read works, write fails" evidence measured nothing. **12 commits now stuck**; `origin/main` still at `0dfa937`, tonight's chain ends at `f73cd97` (anchored at `refs/heads/builder-2026-09-21`).

### autovetting-menu-generation-and-year-gap-fix-2026-09-17 — ready 2026-09-17 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)
- Status: ready to deploy (commit object built via `git commit-tree` on a separate index and anchored at `refs/heads/builder-2026-09-17`, parented on 09-16's `15010b3` (chain: this commit → 15010b3 → 88deccd); it is NOT on `main` — the .git lock files are still unremovable from this sandbox. PUSH still blocked, unchanged since 09-09.)
- Started: 2026-09-17 (02:00 MST overnight builder; launch freeze still active. Awaiting-Daniel section B still holds no freeze-exempt work — B.5/B.7 both need a new Inspect checklist — so the run took the VEHICLE_MENU slot 09-16 proposed as section B's replacement.)
- Task: fix the 6 `VEHICLE_MENU` rows that served the wrong generation, and add the 19 year-rows that make existing correct-generation checklists reachable (launch-spec criterion 7, cross-linking)
- Touched files: inspect/index.html, pinpoint/index.html, _hub/Build-Log/2026-09-17.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-17 02:00: **six wrong-generation menu rows deleted + 19 year-rows added + 9 Pinpoint routes repaired.**
    Resolving cards **285 → 294** of 311 with an `inspectUrl` (91.6% → 94.5%); dead routes **26 → 17**; duplicate menu rows **19 → 13**.
    Part 1 — deleted (not re-ordered) the shadowing older-generation row on: Toyota Highlander 2020/2021/2022 (`toyota-highlander-2014`, XU50 ended MY2019 → now `toyota-highlander-2020`), Chevrolet Silverado 1500 2020 + GMC Sierra 1500 2020 (K2XX survived into MY2019 only as the LD / Limited → now the T1XX keys), Jeep Grand Cherokee 2022 (WK2 ended MY2021 → now `jeep-grand-cherokee-2021`). Deleted rather than re-ordered because that generation was not on sale in that model year — the row offers the buyer a car that did not exist. Side effect: card #260, which names XU70 in its own title, was silently being handed the 2014 checklist and is now correct.
    Part 2 — 19 rows added: Civic 2018-2021 → `honda-civic-2017`; Camry 2021-2023 → `toyota-camry-2018`; Highlander 2023 → `toyota-highlander-2020`; Corolla 2023 → `toyota-corolla-2021`; Sienna 2020 → `toyota-sienna-2015`; Avalon 2013-2015 → `toyota-avalon-2018`; F-150 2023 → `ford-f150-2021`; Palisade 2023 → `hyundai-palisade-2020`; Crosstrek 2020-2023 → `subaru-crosstrek-2018`. Each verified three ways: year block exists, no pre-existing row for that model+year (so no new duplicate), and the target checklist's own `trim` states a range containing the year. Also corrected `hyundai-palisade-2020`'s under-scoped trim string ("1st gen, 2020–2022" → "1st gen LX2, 2020–2025; facelift for 2023") so a 2023 arrival is not told the checklist stops before their car — a factual range correction, not a facelift-policy call, since only one Palisade checklist exists.
    Part 3 — trim stripped from the `model` param (year never touched) on 9 cards, both occurrences each (VEHICLES entry + the matching `Car` JSON-LD `url`): #272 Civic Sport, #273 Crosstrek Premium, #276 Avalon XLE, #295 Camry XSE, #298 Highlander XLE AWD, #318 F-150 PowerBoost Hybrid XLT, #329 Civic Si Sedan, #332 Sienna XLE, #336 Palisade SEL AWD.
    REFUSED 2 that would have resolved cleanly: #330 Corolla Hybrid LE 2023 (the E210 checklist's vinNote frames the two *gasoline* engines as "the inspection story"; site convention gives hybrids their own checklist — the 2023 menu row still went in, since a 2023 gas Corolla should get it) and #309 Crosstrek Sport 2023 (title says GU, year says 2023 — cannot both be true; and the Sport's 2.5L FB25 is not in the GT checklist's trim list). #334 Highlander Hybrid 2023 stays dead per 09-16 — XU70 hybrid has no checklist, Tier B, freeze-blocked.
    NEW FINDING (🟡): the generation range-check surfaced exactly 1 out-of-range route in 141 checkable cards — #281 "Silverado 1500 WT Crew" 2019 → `chevrolet-silverado-2014` (K2XX, 2014–2018). 09-16 filed 2019 Silverado as "arguable" because both generations were on sale; that is right about the year but this card is decidable — the MY2019 K2XX carryover was Double Cab only, so a 2019 **Crew** Cab is T1XX. NOT acted on: the only lever tonight was re-ordering the 2019 row, which would mis-route legitimate LD Double Cab lookups instead. Clean fix is a naming split (`Silverado 1500` vs `Silverado 1500 LD`; `Sierra 1500` vs `Sierra 1500 Limited`) — queued for Daniel in Awaiting-Daniel next to the still-open facelift rule.
    Sibling check: Verified against: autovetting-pinpoint-dead-route-repair-2026-09-16 (pinpoint/index.html) and autovetting-pinpoint-filter-cells-B1-B4-2026-09-15 (pinpoint/index.html) — direct overlaps, both unpushed and both present in this working tree; tonight's commit is parented on 09-16's `15010b3` so both stay in the chain. Field-level JSON-LD diff and line-level diff accounting confirm no sweep: pinpoint 35/35, of which 26 are 09-16's and 9 are mine. Ready-section entries touching inspect/index.html (vinnote-batches 09-09..09-14, inspect-render-and-generation-fix 09-13, key-namespace-rename 09-03, phase-copy-and-template-fix 08-14) all edit CHECKLISTS content or the render path, not VEHICLE_MENU rows — no line collision. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) orthogonal. Every Done (last 10) block carries a `- Started:` date (09-16 added the three that were missing) — no gate-block risk. No Re-sync needed.
    Gates: **Syntax-check: PASS** (official node recipe both files — inspect Script 2/5 OK, pinpoint Script 2/4 OK, exit 0 each). **Resolver gate: PASS**, 294/311 via a faithful reimplementation of `findChecklistByYMMT` (both paths, `parseInt` call-site semantics) against live CHECKLISTS (245) + VEHICLE_MENU (17 years). **Before/after route diff: PASS** — all 311 routes re-resolved on pre- and post-edit files: 9 newly resolving, 1 generation-corrected, **0 regressions**. **Intent gate: PASS 19/19** (every new row resolves to the key it was authored for). **Menu integrity: PASS** — 1,102 rows, 21 intentionally keyless, 0 pointing at a non-existent checklist key. **JSON-LD: PASS** — 1 block, 308 items before and after, 9 differ, `url`-only, 0 non-url fields touched. **Dead-links: verified** — 0 href attributes added/removed/changed in either file. **Scanner: PASS** (594 files, exit 0). Diff vs parent `15010b3`: inspect 20/7 (19 new rows + 6 deleted rows + Palisade trim line), pinpoint 10/10 (9 VEHICLES lines + the minified JSON-LD line), TASKS.md 112/0. Commit hash recorded in `_hub/Build-Log/2026-09-17.md` (kept out of TASKS.md, which is inside the commit and would otherwise change the hash it names). `git diff` between commit and working tree is empty for all three files.
    Coverage limit, stated plainly: 153 of the 294 resolving cards route to a checklist whose `trim` states no parseable year range, so the out-of-range check still cannot see mis-routing on them. Unchanged from 09-16 and proposed as the next run's target.
    Milestone: Tier A from the 09-16 handoff is **closed** — every card behind a menu year-gap is fixed except the two deliberately refused. Remaining 17 dead = 8 Tier B (needs a new checklist, freeze-blocked; Corolla Hybrid 2023 joins tonight) + 8 Tier C (nameplate absent, honest coming-soon) + 1 card-data defect (#309).

### autovetting-pinpoint-dead-route-repair-2026-09-16 — ready 2026-09-16 (COMMIT OBJECT BUILT, REF NOT ON main, NOT PUSHED)

- Status: ready to deploy (commit object `15010b3` built and anchored at `refs/heads/builder-2026-09-16`; it is NOT on `main` — see the git-lock note below. PUSH still blocked, unchanged since 09-09.)
- Started: 2026-09-16 (02:00 MST overnight builder; launch freeze still active, so alternate path. Awaiting-Daniel section B held no remaining freeze-exempt items — B.1-B.4 were drained 09-15 and B.5/B.7 are freeze-blocked — so this run took the 09-15 finding: dead `inspectUrl` routes.)
- Touched files: pinpoint/index.html, _hub/Build-Log/2026-09-16.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-16 02:00: **25 dead Pinpoint -> Inspect deep-links repaired.** Launch-spec criterion 7
  (cross-linking) was failing silently: cards deep-linked to
  `/inspect/?year=&make=&model=` with the trim baked into the model param
  (`model=Highlander Hybrid XLE AWD`), which can never match `VEHICLE_MENU`'s
  `model: 'Highlander'` — `findChecklistByYMMT` needs exact case-insensitive equality on
  all three params. Those cards rendered the coming-soon page on vehicles whose checklist
  we already wrote.
  **Resolving cards 260 -> 285 of 311 (83.6% -> 91.6%). Dead routes 51 -> 26.**

  **Correction to the 09-15 figure.** Run 09-15 reported 227 resolve / 84 dead. The real
  numbers were 260 / 51. That resolver reimplemented Path 1 (`VEHICLE_MENU`) only and
  omitted Path 2, the direct case-insensitive match on stored checklist year/make/model,
  which carries 33 cards on its own. The 84 was an overcount; the underlying defect was real.

  **The fix rule, and why it cannot invent a generation:** strip trim from `model`, never
  touch `year`. The site's own `VEHICLE_MENU` year->key mapping still decides which
  generation that year gets. A card whose year is absent from the menu was left alone —
  that is a menu edit, a different change class, scoped below rather than guessed.

  **3 candidates deliberately NOT fixed** (the strip would have produced a wrong route):
  Toyota Prius c 2018 (NHP10 is a different car from the Prius liftback; `model=Prius`
  would route a Prius c buyer to the ZVW50 checklist); VW Golf Alltrack S 2019 (4Motion
  wagon; `volkswagen-golf-2018` is the Mk7.5 hatch and carries nothing on the Haldex rear
  drive); Toyota Avalon Hybrid XLE 2022 (the menu maps 2019-2022 to `toyota-avalon-2018`,
  whose own trim string reads "4th gen XX40, 2013-2018" — routing a 2022 XX50 there is a
  **menu wrong-generation bug**, flagged in Awaiting-Daniel, not propagated here).

  **Both occurrences per card updated** — the `VEHICLES` entry and the matching `Car`
  JSON-LD `url` in the single-line ItemList on line 1010. The JSON-LD diff was verified
  item-by-item as **url-only**: 24 items differ, 0 non-url fields changed, 308 items before
  and after. (The 25th card, Mazda3, has no `Car` item.)

  Sibling check: overlaps `autovetting-pinpoint-filter-cells-B1-B4-2026-09-15` (Ready,
  committed `88deccd`) and `autovetting-pinpoint-fueltype-schema-fix-2026-08-21` (Ready) on
  `pinpoint/index.html`. **No conflict** — this run changes only `inspectUrl` strings and the
  matching JSON-LD `url` values; 88deccd added `VEHICLES` entries (none of which are in this
  batch, all 7 already resolved) and the fueltype fix touches `fuelType` only. Diff is 26/26
  lines, 0 `fuelType` touches, 0 `VEHICLES` additions or deletions.
  Verified against: autovetting-pinpoint-filter-cells-B1-B4-2026-09-15,
  autovetting-pinpoint-fueltype-schema-fix-2026-08-21.
  Re-sync needed against: (none)

  Also added missing `- Started:` fields to the three In-flight blocks that share
  `pinpoint/index.html` — `autovet-competitor-monitor` (2026-06-11),
  `autovet-cpo-protocol-ingestion` (2026-06-14), `autovet-seo-content` (2026-06-17). Each
  date is sourced from that block's own first dated Notes entry, not invented. Without them,
  the first of those blocks to reach Done would gate-block every future task touching
  `pinpoint/index.html` indefinitely.

  Gates: **Syntax-check: PASS** (official node recipe on pinpoint/index.html — Script 2 OK,
  Script 4 OK, exit 0). **JSON-LD parse: PASS** (1 ld+json block, 308 items).
  **Resolver gate: PASS 25/25** — each card re-resolved through a faithful reimplementation
  of `findChecklistByYMMT` (both paths, `parseInt` year semantics) against the live
  `CHECKLISTS` (245 keys) and `VEHICLE_MENU` (17 years) and matched its intended key.
  **Generation cross-check: PASS** — every target checklist whose trim string states a year
  range contains the card's year. **Dead-links: verified** — 0 new `href` attributes; every
  changed URL targets `/inspect/`, which exists. **Scanner: PASS** (589 files, no secrets, exit 0).

  Commit: `15010b3` — **object built, but it is NOT on `main`.** `.git/HEAD.lock` was left
  behind by 09-15's `88deccd` and cannot be unlinked from the builder sandbox, so no ref
  update that dereferences HEAD can run here. Worked around with `git commit-tree` +
  anchored at `refs/heads/builder-2026-09-16` so the object survives a `git gc --prune=now`.
  The commit also carries 09-15's 68 staged TASKS.md lines, which had no commit of their own.
  **Daniel: one command puts it on main —**
  `rm -f .git/HEAD.lock .git/refs/heads/main.lock && git update-ref refs/heads/main 15010b3 && git branch -d builder-2026-09-16`

### autovetting-pinpoint-filter-cells-B1-B4-2026-09-15 — ready 2026-09-15 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally as 88deccd; PUSH BLOCKED — stored PAT still rejected, unchanged since 09-09)
- Started: 2026-09-15 (02:00 MST overnight builder; launch-freeze alternate path = Awaiting-Daniel section B, taken BEFORE the vinNote queue per run #19 anomaly 2)
- Touched files: pinpoint/index.html, _hub/Build-Log/2026-09-15.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-09-15 02:00: ROUTING CHANGE APPLIED. Run #19 asked the builder to read section B of
  Awaiting-Daniel.md before falling through to vinnote-queue.md; five productive nights had gone
  straight to the queue and left 11 freeze-exempt fills idle for a fifth week. This run read
  section B first. Drained B.1-B.4 — all 7 named cells — and did NOT touch the vinNote queue
  (stays at 135, top still hyundai-elantra-2021).
  Delivered 7 Pinpoint cards, 337 -> 344. work-hauling/2 under-10k + 10-15k (Silverado 1500 WT
  Regular Cab 2014-2015 / 2016-2018 -> chevrolet-silverado-2014) and 20-30k (F-150 XL Regular Cab
  4x4 2019-2020 -> ford-f150-2018); road-trip/7+/15-20k (Sienna LE 2015-2017 ->
  toyota-sienna-2015); road-trip/6/30k+ (Enclave Avenir 2020-2022 -> buick-enclave-2018, Avenir
  chosen over Traverse High Country because Avenir is on the Filter-Schema top-trim marker list so
  the card earns the luxury chip by rule); work-hauling/7+ 20-30k + 30k+ (Expedition XLT 2018-2019
  and Expedition MAX Limited 2020-2021 -> ford-expedition-2018). B.1 also resolves B.6 (the
  Silverado reg-cab partial) — same work, no separate task.
  Every cost anchor web-verified before shipping, not written from memory: 4.3L EcoTec3 V6 tow
  7,200 lb (GM MY2014 figure); 5.3L AFM lifter $2,800 one bank / ~$7,000 with cam damage
  (CarComplaints 2015 avg $6,500) and the risk spans the WHOLE 2014-2018 run, which the 10-15k
  tagline says explicitly because "newer is safer" is the wrong instinct here; 2019 F-150 3.3L
  Ti-VCT tow 7,700 lb; EcoBoost cam phasers $800-2,500 alone, $3,200-5,500 with the timing kit;
  Sienna class-action power-door cable coverage = 10 years from first use, no mileage cap, so
  lapsed on a 2015, ~$1,500/side after; Enclave 5,000 lb tow ONLY with the Trailering Package
  (1,500 lb without); Shift-to-Park = shifter microswitch, TSB 19-NA-206, p/n 84733196;
  2018 Expedition 9,300 lb properly equipped.
  SPEC ERROR IN THE INSTRUCTIONS: B.4 asked for "Ford Expedition XL Fleet" cards. The 2018+
  Expedition has NO XL trim — XLT / Limited / Platinum only. Built XLT and MAX Limited instead.
  Third bad identifier from that section after ford-expedition-2020 and toyota-sienna-2017; the
  standing key-resolution fix catches dead slugs but not a trim that never existed. Used the trim
  fact as content: 2018 XLT ships base SYNC not SYNC 3, so no carplay chip and the tagline says to
  check. Same discipline dropped carplay from the F-150 XL card (SYNC 3 optional, not standard)
  and from the Sienna card (no CarPlay before MY2019).
  Sibling check: no conflict. Only other block touching pinpoint/index.html is Ready =
  autovetting-pinpoint-fueltype-schema-fix-2026-08-21, which edits the JSON-LD Car block; this run
  appended only to the VEHICLES array. Verified by diff: 88deccd is 56 added lines / 0 deletions /
  0 fuelType touches, so that task's work was not swept in. In-flight siblings orthogonal —
  autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/), autovet-seo-content (Content/blog/). Done(last 10): the one block
  touching pinpoint/index.html is the 2026-08-11 sitemap/pinpoint entry and it HAS
  `- Started: 2026-08-11` — Started-date gate clear, nothing to backfill. No Re-sync needed.
  Verified against: _hub/Filter-Schema.md (enums), _hub/Awaiting-Daniel.md run #19 section B.
  Cell matrix: work-hauling/2 0/0/1/0/0 -> 1/1/1/1/0; road-trip/7+ 0/0/0/3/3 -> 0/0/1/3/3;
  road-trip/6 1/1/1/1/0 -> 1/1/1/1/1; work-hauling/7+ 0/1/0/0/0 -> 0/1/0/1/1. Reachable-empty
  36 -> 29.
  Functional read-back: 344 entries parse; 7/7 new entries pass Filter-Schema enum validation;
  0 entries anywhere still using old type/purpose fields.
  Resolver gate: reimplemented findChecklistByYMMT against live VEHICLE_MENU (17 years) +
  CHECKLISTS (245 keys) — 7/7 new inspectUrls resolve to the intended key; all 9 run-#19 wire-to
  keys resolve; both create-new keys still correctly absent.
  Syntax-check: PASS (Script 2 OK, Script 4 OK). Dead-links: verified (0 new hrefs).
  Scanner: PASS (587 files, exit 0).
  NEW RED FINDING, logged to Awaiting-Daniel: 84 of 311 Pinpoint inspectUrls (27%) dead-route to
  the coming-soon renderer, and 75 of those have a checklist that already exists — trim baked into
  the model param, or a year absent from VEHICLE_MENU. Launch-spec criterion 7 failing silently on
  a quarter of the catalog. NOT auto-swept: naive candidate matches are wrong-generation in several
  cases. Recommended as the next Step-3 alternate-path workstream ahead of the vinNote queue.
  NEW RED ANOMALY, logged to Awaiting-Daniel: .git is unlink-restricted from the builder sandbox —
  writes succeed, deletes return Operation not permitted. Blocked the first commit on a 25.8h-old
  stale index.lock; worked around with GIT_INDEX_FILE=/tmp/alt.index. 1,402 orphan tmp_obj_* files
  in .git/objects dating to 2026-08-10, plus undeletable HEAD.lock / index.lock /
  objects/maintenance.lock, and anomaly 8's stale ref cannot be cleared from here. Plausible
  confound for the PAT diagnosis; NOT re-diagnosed. Cheap discriminator for Daniel: one git push
  from his own terminal.
  Follow-on to that anomaly: 88deccd created .git/HEAD.lock and could not unlink it, so the SECOND
  commit of this run (this TASKS.md entry) failed with "cannot lock ref 'HEAD'". Exactly one commit
  per session is possible — likely why every recent night shows precisely one. TASKS.md is STAGED
  BUT UNCOMMITTED; its content is on disk and correct (orchestrator reads the file, not git) and
  will ride along on the next commit. Cleanup sequence for Daniel is in Awaiting-Daniel.md.
  PUSH BLOCKED — 9 commits now unpushed. Not re-diagnosed; PAT unchanged since May 30.

### autovetting-vinnote-batch-2026-09-14 — ready 2026-09-14 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally; PUSH BLOCKED — stored PAT still rejected, unchanged since 09-09)
- Started: 2026-09-14 (02:00 MST overnight builder; launch-freeze alternate path = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-09-14.md (gitignored), TASKS.md
- Notes:
  2026-09-14 02:00: drained queue priorities 90/91/93 — rivian-r1t-2022, mercedes-benz-c300-2022,
  ford-bronco-sport-2021. Two of the three carried spec errors that were fixed alongside the vinNote.
  (1) LOOK-AHEAD ERROR — `rivian-r1t-2022` was authored with 2023 hardware. Stored engine string offered
  "Quad-motor (835 hp) or Dual-motor (665 hp); 135 kWh or 149 kWh battery"; the dual-motor R1T did not
  reach a customer until May/June 2023 (Rivian newsroom + Electrek + InsideEVs), and the 149 kWh Max pack
  is likewise MY2023. Every MY2022 R1T is quad-motor on the 135 kWh Large pack. Engine string corrected.
  SECOND look-ahead error in two runs (after toyota-sequoia-2022 on 09-13) — the pattern is now recurrent
  enough that very-new entries should be treated as suspect by default.
  (2) SPEC ERROR — `mercedes-benz-c300-2022` engine read "2.0T M254 PHEV mild hybrid I4", which is both
  self-contradictory and wrong: the US 2022 W206 C300 has no plug-in variant. Corrected to
  "2.0T M254 I4 (255 hp) with 48V EQ Boost mild hybrid (ISG)". The entry's own summary field was already
  correct, so only `engine` was wrong.
  (3) vinNotes: the Rivian and Mercedes notes both exist mainly to STOP an 8th-digit read. Rivian puts
  trim/series in digit 8 and the motor in digit 6 (A=quad, B=dual) — a domestic-brand habit applied to a
  Rivian VIN gives a wrong answer. Mercedes nominally has an engine character at digit 8, but the US 2022
  C-Class shipped one powertrain, so the useful read is positions 4-5 (4G = RWD, 4H = 4MATIC). Ford is the
  conventional case: digit 8, 6 = 1.5L EcoBoost I3, 9 = 2.0L EcoBoost I4 (Badlands/First Edition only,
  and the digit doubles as the tell for the twin-clutch rear drive unit).
  Sibling check: no conflict. Every other block touching inspect/index.html is this same task's prior
  vinNote batches, all sitting in Ready (COMMITTED, NOT PUSHED) behind the same PAT blocker — sequential,
  same file, no divergence. In-flight siblings are orthogonal: autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/), autovet-seo-content (Content/blog/), autovet-competitor-monitor (Competitors/).
  Started-date gate: checked all Done blocks touching inspect/index.html — none missing `- Started:`.
  No Re-sync needed.
  Functional read-back: 245 keys / 0 missing sections / 1,601 items / vinNotes 107 -> 110 (baseline exact).
  itemsToCheck drift on all three entries left untouched — standing content decision with Daniel.
  Syntax-check: PASS. Dead-links: verified (no new hrefs). Scanner: PASS.
  PUSH BLOCKED — 8 commits now unpushed. Not re-diagnosed; PAT unchanged since May 30.

### autovetting-inspect-render-and-generation-fix-2026-09-13 — ready 2026-09-13 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally as 8a01144; PUSH BLOCKED — stored PAT still rejected, unchanged since 09-09)
- Started: 2026-09-13 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain, which surfaced two live defects)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-09-13.md (gitignored), TASKS.md, _hub/Awaiting-Daniel.md (gitignored)
- Notes:
  2026-09-13 02:00: went to the queue for tundra-2022 / sequoia-2022 vinNotes and found two
  defects that matter more than the vinNotes.
  (1) LOOK-AHEAD ERROR — `toyota-sequoia-2022` was authored as the 2023 car. The 2022 Sequoia is
  the FINAL 2nd-gen XK60 with the 5.7L 3UR-FE V8 (381 hp / 401 lb-ft, 6-speed auto); the 3rd-gen
  XK70 i-FORCE MAX hybrid starts at MY2023. Corroborated three ways: Toyota press/press-cycle
  coverage, NHTSA campaign scopes (new-platform Tundra campaigns run 2022-2025 while the matching
  Sequoia scopes run 2023-2025), and this repo's own `toyota-sequoia-2016` entry, which already
  says "2nd gen XK60, 2008-2022". Entry fully rewritten to the V8 car: 11 items, cost-anchored on
  cam-tower oil leak ($1,200-3,500), secondary air injection P244x ($1,300-1,500 indie /
  $2,000-4,000+ dealer), and the Limited/Platinum-only rear load-levelling air suspension
  (compressor $2,600-2,700). Same failure mode as the 2018 Avalon and 2020 Highlander findings.
  (2) LIVE RENDER BUG — `toyota-prius-2012`, `mazda-cx5-2013` and `ford-escape-2013` stored their
  content under `categories:` while the renderer only ever reads `c.sections` (3 call sites, no
  fallback). Those three pages threw a TypeError instead of rendering. Renamed the key; 30
  inspection items are now reachable, including the Escape's **Critical** 1.6L EcoBoost
  engine-fire item, which has been unreachable to buyers. This class of defect is invisible to the
  "245 keys -> 245 rows, 1:1" coverage check, which counts keys and never renders them.
  Also: vinNote added to sequoia-2022 + tundra-2022, sourced to Toyota's Part 565 filings
  (NHTSA MID K6-00 and 23-008) — engine position is the 5th digit on the 2nd-gen Sequoia and the
  4th on the TNGA-F Tundra, NOT the 8th on either; tundra-2022 engine string corrected
  3.5L -> 3.4L V35A-FTS per the same filing; tundra-2022 stats.itemsToCheck 12 -> 6 to match reality.
  Queue 140 -> 138.
  Commit: 8a01144. Sibling check: overlaps autovet-competitor-monitor / autovet-cpo-protocol-ingestion /
  autovet-seo-content (all in-flight, not Done — Done-sibling gate does not apply; all three lack
  `- Started:` and are flagged in Awaiting-Daniel).
  Verified against: autovetting-vinnote-batch-2026-09-12, autovetting-vinnote-batch-2026-09-11.
  Re-sync needed against:
  Syntax-check: PASS. Scanner: PASS (580 files). Dead-links: verified (/decode/ exists).
  Functional CHECKLISTS read-back: PASS — brace-matched the real literal out of the file and
  parsed it with `new Function` (never eval): 245 keys, 0 entries missing `.sections`, 1,601 items
  survive a `c.sections.map(s => s.items...)` replay of the renderer's own access pattern.
  PUSH BLOCKER — UNCHANGED, DANIEL ACTION STILL REQUIRED. Write-tested again this run (not
  read-tested): `git push --dry-run` with the stored PAT via GIT_ASKPASS returns "remote: Invalid
  username or token." The `Claude/` mount WAS present this run and `.credentials/` read fine, so
  readability is no longer in question — the token itself (`ghp_krkG...`, unchanged) is rejected.
  7 commits now unpushed.


### autovetting-vinnote-batch-2026-09-12 — ready 2026-09-12 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally as 416c6ec; PUSH BLOCKED — GitHub still rejects the stored PAT, unchanged since 09-09)
- Started: 2026-09-12 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-09-12.md (gitignored), TASKS.md, _hub/Awaiting-Daniel.md (gitignored)
- Notes:
  2026-09-12 02:00 [scheduled task]: mount check PASS (Claude/ sibling present, so .credentials/
  readable this run). Drained pri 85 toyota-highlander-2014, pri 87 toyota-tacoma-2024,
  pri 88 dodge-challenger-2023. vinNote count 102 -> 105; queue 143 -> 140 rows;
  inspect/index.html 1,417,016 -> 1,421,798 bytes (+4,782), 17,760 -> 17,763 lines (+3).
  Three-way reconciliation clean: 245 CHECKLISTS slugs - 105 with vinNote = 140 queue rows.
  THEME OF THIS BATCH: the inverse of 09-11. That batch was three single-engine cars where the
  honest note was what the VIN CANNOT tell you; all three tonight have a real decodable engine
  split, so each note converts a character position into a buying decision.
  (1) toyota-highlander-2014 — genuine three-way split on the 5th digit: A = 2.7L 1AR-FE four
      (185hp, FWD-only base LE, gone after 2016), K = 3.5L 2GR-FE V6 (270hp) w/ U660E 6-speed,
      C = 2GR-FXE Highlander Hybrid. The hybrid is the real catch: on a 2014 it shipped ONLY in
      Limited / Limited Platinum — identical badges to a gas V6 Limited — so trim tells a buyer
      nothing once the sticker is gone. C = eCVT + NiMH pack, replacement ~$2,500-4,000
      reman-to-dealer. The A four is the second deliberate catch (FWD-only, slowest 3rd-gen,
      wrong truck for towing). Sourced from reman-engine per-year listings (VIN A 1AR-FE /
      VIN K 2GR-FE / VIN C 2GR-FXE), corroborated by a United Autos Parts "3.5L VIN K (5th
      digit)" transmission listing and a real 2014 VIN sample 5TDDKRFH7ES... (5th char K).
  (2) dodge-challenger-2023 — the true 8th-digit case: G = 3.6 Pentastar (305hp), T = 5.7 HEMI
      (375hp), J = 6.4 HEMI 392 (485hp), 9 = 6.2 supercharged Hellcat. Leverage: the 5.7 and 6.4
      both run MDS and carry the collapsed-lifter risk this checklist already details
      ($4,000-7,000 cam-and-lifter job, more if debris circulated); the Pentastar has NO MDS and
      no lifter exposure at all — so the 8th digit tells a buyer before driving whether the car's
      headline failure mode is even on the table.
      TRAP DOCUMENTED: circulating decoder tables call Z the Hellcat engine code, and a Z IS
      present in a Hellcat VIN — but at POSITION 6 (series/trim group), not the engine field.
      Verified against a real 2023 SRT Hellcat VIN 2C3CDZC9XPH512357: pos6 = Z, pos8 = 9,
      pos10 = P (2023); a 2023-specific reman listing independently gives "6.2L VIN 9 8th digit."
      Note instructs counting to the 8th character deliberately.
  (3) toyota-tacoma-2024 — 5th digit D = gas 2.4L T24A-FTS turbo four w/ 8-speed auto; i-FORCE MAX
      hybrid listed as C or F. Worth decoding because i-FORCE MAX was OPTIONAL on TRD Sport /
      TRD Off-Road / Limited and standard only on TRD Pro + Trailhunter, so trim will not tell a
      used buyer whether there is a 48hp motor and traction battery in the driveline. TWO HEDGES
      WRITTEN INTO THE NOTE rather than papered over: (a) the 4th gen also offered a 6-speed manual
      with the gas 2.4T and these characters encode the engine-AND-TRANSMISSION pairing, so the
      character for that combination is NOT documented in available sources — note says confirm,
      do not assume; (b) the C/F hybrid codes come from community decoder tables (tacoma4g), not
      Toyota, and the note says so. Note then redirects to the decode that actually matters on a
      first-year TNGA-F redesign with no long-term failure record: recall lookup at nhtsa.gov/
      recalls plus whether the 5yr/60k powertrain warranty is still live.
  ⚠️ SYNTAX GATE FALSE-PASS CAUGHT THIS RUN — new hazard instance, logged in full in the
  Build-Log. First write embedded the link as <a href="/decode/"> with UNESCAPED inner double
  quotes inside a double-quoted JS string (house pattern is href=\"/decode/\"; a Python
  non-raw string ate the backslashes). THE SCRIPT-BLOCK SYNTAX GATE PASSED ON THE BROKEN FILE,
  because "...<a href=" /decode/ ">..." is syntactically legal JS — string / identifier / string,
  three division operators. It compiles and only dies at RUNTIME with
  "ReferenceError: decode is not defined", which would have silently killed CHECKLISTS and taken
  the inspect page's JS with it. Nastier than truncation: nothing about the file looks wrong.
  Caught by a FUNCTIONAL READ-BACK (isolate the CHECKLISTS literal, eval it, assert each vinNote
  is a retrievable string containing the decode anchor). Reverted from a byte-identical pre-edit
  backup (vinNote count confirmed back to 102), rewrote with \\" in the generator plus a
  pre-insert assertion that no note contains an unescaped ". PERMANENT ADDITION to this task's
  routine: syntax check is necessary but NOT sufficient — after editing CHECKLISTS, eval the
  object literal (use a quote/escape-aware brace match to isolate it; a naive [\s\S]*?\n}; regex
  truncates it) and read the touched fields back. A note that cannot be read back is not shipped.
  Verification: Syntax-check: PASS (scripts 2,5). Functional read-back: PASS (lens 1252/1545/1816,
  exactly 2 quote chars each = the href pair, decode anchor present in all three). JSON-LD: PASS
  (2 blocks re-parse). Insert count asserted == 1 per slug, no pre-existing vinNote overwritten.
  Byte/line deltas recorded above; tail intact through </html>. Slug count unchanged at 245.
  Dead-links: verified — only new href is /decode/, and decode/index.html exists.
  Scanner: PASS (578 files, exit 0).
  Sibling check: no true conflict. Ready blocks sharing inspect/index.html are
  autovetting-vinnote-batch-2026-09-09, -2026-09-10 and -2026-09-11 (same task, same file,
  strictly additive vinNote fields on different slugs — no slug touched twice; tonight's three
  slugs are absent from all three prior batches),
  autovetting-inspect-key-namespace-rename-2026-09-03 (already pushed as 0dfa937; touches key
  literals, not vinNote fields) and autovetting-phase-copy-and-template-fix-2026-08-14
  (scripts/render-blog.py + blog/*, inspect only for phase copy). In-flight
  autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) are orthogonal.
  Done(last 10) = autovetting-ga-swap-06S3EWDPXK only, which HAS a Started date — no
  missing-Started gate fix required this run. No slug collision anywhere.
  Verified against: autovetting-vinnote-batch-2026-09-11, autovetting-vinnote-batch-2026-09-10,
  autovetting-vinnote-batch-2026-09-09.
  Re-sync needed against:
  Commit: 416c6ec.
  PUSH BLOCKER — UNCHANGED, DANIEL ACTION STILL REQUIRED. Write-tested, not read-tested
  (anonymous ls-remote proves nothing on a public repo): `git push --dry-run` with the stored
  PAT via GIT_ASKPASS returns "remote: Invalid username or token. Password authentication is
  not supported for Git operations." The token file is UNCHANGED since 09-11 — still prefix
  ghp_krkG, rotated_on 2026-05-29 — so the PAT has not been regenerated and every future run
  will fail identically until it is. origin is correctly HTTPS (fixed 09-11, still fixed).
  6 commits now unpushed; remote HEAD still 0dfa937.


### autovetting-vinnote-batch-2026-09-11 — ready 2026-09-11 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally as e644151; PUSH BLOCKED — GitHub rejects the stored PAT)
- Started: 2026-09-11 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-09-11.md (gitignored), TASKS.md
- Notes:
  2026-09-11 02:00 [scheduled task]: mount check PASS. Drained pri 82 honda-crv-2015,
  pri 83 toyota-sienna-2015, pri 84 lexus-gx460-2015. vinNote count 99 -> 102; queue
  146 -> 143 rows; inspect/index.html 1,412,705 -> 1,417,016 bytes (+4,311),
  17,756 -> 17,759 lines (+3).
  THEME OF THIS BATCH: all three are single-engine-in-the-VIN cars, so the honest note is
  what the VIN CANNOT tell you plus what you must decode instead. That is a different shape
  from the usual "letter X = engine Y" note and is the correct output for these three —
  inventing an engine-code split would have been fabrication.
  (1) honda-crv-2015 — the 5th digit reads "M" on a 2015 CR-V, but carpartplanet lists the
      SAME "2.4L VIN M 5th digit" code for a 2013 CR-V, i.e. the engine character does NOT
      separate the port-injected K24Z7/5AT (2012-14) from the direct-injected K24W/CVT
      (2015-16). The 10th digit (model year: D/E vs F/G) is the discriminator. Note carries
      the HCF-2 vs ATF-DW1 fluid trap (wrong-fluid = walk-away) and SB 15-046 CVT judder,
      anchored at a $3,500-5,000 CVT replacement. Drivetrain from chassis code at positions
      4-6: RM3 front-drive / RM4 AWD (4th-gen model codes per Wikipedia; US cars are 2.4 only).
  (2) toyota-sienna-2015 — 5th digit always "K" (2GR-FE): 2015 has no engine choice at all
      (2.7L four gone by 2013; 296-hp 2GR-FKS/8AT arrives 2017). The decode that matters is
      FWD vs AWD, because an AWD 2015 Sienna HAS NO SPARE TIRE (rear driveshaft + exhaust
      occupy the well) and ships P235/55RF18 run-flats — cost-anchored at ~$200-250/tire vs
      ~$130-160 conventional, plus the check for a previous owner having swapped to
      conventional tires, which leaves the van with neither a reserve nor a spare.
      DEFECT CAUGHT: the checklist's engine field read "3.5L 2GR-FE V6 (296hp)" — that is the
      2017+ 2GR-FKS figure. Corrected to "266 hp / 245 lb-ft" (Edmunds / US News 2015 specs).
      One-string data fix, logged here rather than deferred.
  (3) lexus-gx460-2015 — 5th digit "M" on every GX460 ever built (4.6L 1UR-FE is the only
      engine across the whole 2010-2022 J150 run). The decode that matters is GX460 vs GX470:
      the J120 GX470's 4.7L 2UZ-FE is timing-BELT driven (90k belt + water pump, ~$1,200-2,000,
      walk-away if undocumented and overdue) where the 1UR-FE is chain. Note also flags two
      things the VIN will NOT tell you — KDSS presence (inspect the accumulators at the sway
      bars for weeping) and Takata involvement (assigned by VIN + build date; run nhtsa.gov/
      recalls), the latter cross-referencing this checklist's existing critical Takata item.
  Verification: anchored inserts on the slug key block (not on an engine-string literal —
  the 09-10 non-breaking-space near-miss); insert count asserted == 1 per slug; byte and line
  deltas recorded above; tail intact through </html>; both JS blocks pass the script gate;
  both JSON-LD blocks re-parse. Only new href added is /decode/, which exists.
  Sibling check: no true conflict. Ready blocks sharing inspect/index.html are
  autovetting-vinnote-batch-2026-09-09 and -2026-09-10 (same task, same file, strictly
  additive vinNote fields on different slugs — no slug touched twice),
  autovetting-inspect-key-namespace-rename-2026-09-03 (already pushed as 0dfa937; touches key
  literals, not vinNote fields) and autovetting-phase-copy-and-template-fix-2026-08-14
  (scripts/render-blog.py + blog/*, inspect only for phase copy). In-flight
  autovet-competitor-monitor (Competitors/) + autovet-cpo-protocol-ingestion
  (Product/CPO-Protocols/) + autovet-seo-content (Content/blog/) are orthogonal.
  Done(last 10) = recall-audit waves + earlier vinnote batches; no slug collision.
  Verified against: autovetting-vinnote-batch-2026-09-10, autovetting-vinnote-batch-2026-09-09.
  Re-sync needed against:
  Commit: e644151.
  PUSH BLOCKER — DIAGNOSIS CORRECTED TONIGHT. The 09-09/09-10 theory ("credentials
  folder is outside the mount, no token readable") is WRONG: the PAT reads fine from the
  scheduled-run sandbox. Two separate problems, one fixed and one needing Daniel.
  FIXED THIS RUN: `origin` was an SSH remote (git@github.com:...) and port 22 is
  unreachable from the sandbox; set to https://github.com/dvs-dnl/autovetting.git. That
  change is committed to .git/config and persists.
  STILL BLOCKED: over HTTPS with GIT_ASKPASS, GitHub answers "Invalid username or token.
  Password authentication is not supported for Git operations." — GitHub's own response,
  so the credential arrived and was REJECTED. Retried with HTTP Basic via
  http.extraheader: also 401. Anonymous `git ls-remote` over HTTPS SUCCEEDS (public repo),
  which is what made 09-09 look like an egress failure; it is not. api.github.com is
  blocked from the sandbox (403 at the proxy) so the token's scopes/expiry could not be
  read back. Token file claims expires 2027-05-19, rotated_on 2026-05-29; the 09-03 push
  succeeded on this same file and 09-09 was the first rejection, so it was revoked in that
  window. ACTION: regenerate the PAT (prefix ghp_krkG) with repo scope and replace only the
  `token` value in ~/Documents/Claude/.credentials/github-config.json. Logged to
  _hub/Awaiting-Daniel.md as a 🔴 blocking item.
  Queued behind this blocker: 48b9c9c, 7eea056, 8e10f7d, e644151 (remote HEAD = 0dfa937).
  Syntax-check: PASS. Dead-links: verified. Scanner: PASS.


### autovetting-inspect-key-namespace-rename-2026-09-03 — ready 2026-09-03

- Status: ready to deploy (edited locally)
- Started: 2026-09-03 (Cowork session — catalog builder Run 73 follow-up, at Daniel's request)
- Touched files: inspect/index.html
- Notes:
  Renames the 26 checklist keys that used a non-canonical make prefix, so the
  key namespace uses one prefix per make: chevy-* -> chevrolet-* (14),
  vw-* -> volkswagen-* (6), mercedes-* -> mercedes-benz-* (6).
  Cosmetic / data-hygiene only — NOT a defect fix. Verified beforehand that
  this was never a live-site bug: checklist keys are hardcoded literals and are
  never derived from make/model at runtime, so nothing user-facing changed
  behaviour. The value is interop — external consumers of the key namespace
  (the vehicle catalog) no longer need a make-alias table.
  CRITICAL detail for review: the rename was applied to BOTH sides — the
  CHECKLISTS object keys AND the 1,068 VEHICLE_MENU `key:` literals. Renaming
  only one side would have silently dropped all 26 vehicles to
  renderComingSoon().
  Integrity verified: 139 replacements; 1,406,561 -> 1,407,277 bytes, and the
  +716 delta matches the arithmetically expected delta exactly; line count
  unchanged at 17,753; 245 unique checklist keys before and after; 1,068 menu
  literals / 245 unique before and after; ZERO dangling menu keys and ZERO
  orphan checklists; no residual chevy-*/vw-*/mercedes-* keys; all 139 changed
  lines contain a renamed key and nothing else changed; both JS blocks pass
  `node --check` and both JSON-LD blocks re-parse; tail intact through </html>.
  Left deliberately unrenamed: 6 nameplate-drift keys (silverado/sierra ->
  base 1500, gx460, rx350, mx5) and 2 make-absorbed keys (mazda3-*). Those
  encode a naming question, not a prefix inconsistency, and stay handled by
  _hub/Content/vehicle-catalog/inspect-key-aliases.json.
  Full detail: _hub/Content/vehicle-catalog/BUILD-LOG/2026-09-03.md

### autovetting-pinpoint-fueltype-schema-fix-2026-08-21 — ready 2026-08-21

- Status: ready to deploy (edited locally, not committed)
- Started: 2026-08-21 (Cowork session — catalog builder Run 62, acting on Run 61's data-quality report)
- Touched files: pinpoint/index.html
- Notes:
  Corrects the schema.org `fuelType` field on 43 of the 308 JSON-LD `Car` items.
  This is live structured data that search engines consume, so the errors were
  public-facing. Groups: 13 Chevrolet cards falsely marked "Hybrid" (Camaro SS 1LE,
  Silverado 1500, Tahoe, Suburban, Colorado, Cruze, Blazer, Trailblazer, Trax —
  none is a hybrid) set to "Gasoline"; 10 battery-electric cards marked
  "Gasoline"/"Hybrid" (2x Tesla, LEAF, Mustang Mach-E, F-150 Lightning, ID.4,
  e-tron, R1T, IONIQ 6, EV6) set to "Electric"; Prius c and Prius L Eco set to
  "Hybrid". Vocabulary extended beyond the previous three values: new "PHEV"
  (Prius Prime, RAV4 Prime, Wrangler 4xe) and "Diesel" (Colorado, Canyon,
  Gladiator, Ram 2500). The 11 mixed-powertrain cards now carry multi-value
  arrays, e.g. "fuelType":["Gasoline","Hybrid"] — valid JSON-LD, and the only
  accurate encoding for a card covering both gas and hybrid trims.
  No page JavaScript reads fuelType (0 occurrences outside the JSON-LD block),
  so the arrays cannot affect rendering. Integrity verified: 351,325 -> 351,521
  bytes, line count unchanged at 4,407, everything outside the JSON-LD block
  byte-identical, block re-parses, still exactly 308 Car items, 0 missing fuelType.
  Full detail: _hub/Content/vehicle-catalog/BUILD-LOG/2026-08-21-run62.md

### autovetting-phase-copy-and-template-fix-2026-08-14 — ready 2026-08-14

- Status: ready to deploy (committed locally)
- Started: 2026-08-14 (Cowork session — orchestrator flagged 27 phase-content violations after 47-day push gap)
- Touched files: scripts/render-blog.py, inspect/index.html, blog/*/index.html (26 files total)
- Notes:
  Same fix as 2026-06-27, extended to the source template. Previous fix only
  patched output HTML, so new blog renders regenerated the banned copy every
  night. Both output and source are now aligned on "Get an inspection quote".
  All 27 critical gates pass locally.

### autovetting-vinnote-batch-2026-09-10 — ready 2026-09-10 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally; PUSH BLOCKED — same GitHub PAT rejection as 09-09)
- Started: 2026-09-10 (02:00 MST overnight builder, Run 81; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-09-10.md (gitignored), TASKS.md
- Notes:
  2026-09-10 02:00 [scheduled task]: mount check PASS. Drained pri 79 toyota-rav4-2016 +
  pri 80 toyota-sequoia-2016. vinNote count 97 -> 99; inspect/index.html 1,409,233 ->
  1,412,705 bytes (+3,472), 17,755 -> 17,757 lines (+2).
  (1) toyota-rav4-2016 -- CLOSES THE 09-09 ANTI-FABRICATION SKIP. The 09-09 run left this row
      queued because it could not source which 8th-digit letter separates 2AR-FE gas from
      2AR-FXE hybrid. Reason found: there is no 8th-digit letter -- TOYOTA ENCODES ENGINE IN
      THE 5TH DIGIT. Same class of structural correction as 09-09's Nissan-4th-digit finding;
      the spec's "8th-digit engine code" wording is a Honda/GM convention, wrong for several
      makes. Sourced from the OEM's own NHTSA filings: vPIC coding docs A5/H5-00 (RAV4 /
      RAV4 HYBRID) and K6-00 (Sequoia) both label position 5 "5th Digit Engine Type" and
      position 8 "Line & Make / Series"; cross-checked against parts catalogues ("2.5L VIN F,
      5th digit 2AR-FE" / "VIN J, 5th digit 2AR-FXE"). Mapping: F = 2AR-FE gas (176 hp, 6AT,
      FWD or mechanical AWD), J = 2AR-FXE hybrid (194 hp combined, eCVT, AWD-i).
      COVERAGE GAP flagged in the note: 2016 is the RAV4 Hybrid's FIRST U.S. model year, but
      the checklist's engine field is gas-only while its trim field claims all of 2013-2018 --
      so a hybrid buyer is looking at a checklist that does not describe the car. Note carries
      the delta (no propshaft/rear diff/transfer case, eCVT has no fluid history, substitute
      traction-battery vent + DTC checks; 8yr/100k pack warranty expired on every 2016,
      $3,000-8,000 new / $1,500-3,500 refurbished).
  (2) toyota-sequoia-2016 -- Y = 5.7L 3UR-FE gas V8 (381 hp), W = 5.7L 3UR-FBE flex-fuel (E85).
      Same engine mechanically, so no frame-rust/timing-chain guidance changes; the digit's
      value is that the flex-fuel truck carries one pattern the gas truck does not. Toyota TSB
      T-SB-0166-19 (read first-hand from the NHTSA PDF, supersedes T-SB-0058-13): 2009-2018
      Sequoia / 2009-2019 Tundra 3UR-FBE, extended crank + MIL with P0171/P0174/P0172/P0175/
      P1604 from a mislearned fuel alcohol density. Repair is NOT a reflash alone -- ECM
      reprogram PLUS fuel pump assembly replacement PLUS fuel-density learning reset, 2.2-hour
      dealer op (EG1904), covered by the Federal Emission Warranty 96 months/80,000 miles,
      which has expired on every 2016 -> customer-pay on a W truck. No dollar figure invented;
      the note gives the part and the published labor time and stops.
  DEFECT CAUGHT AND CORRECTED MID-RUN: the Sequoia note first landed on the WRONG VEHICLE.
  The insert anchored on the literal string "engine: '5.7L 3UR-FE V8 (381 hp) with 6-speed
  automatic'," and a uniqueness assertion confirmed exactly one occurrence -- but that
  occurrence belongs to toyota-land-cruiser-2018, not toyota-sequoia-2016. The Sequoia's line
  is byte-different: a NON-BREAKING SPACE (U+00A0) sits between "381" and "hp". A uniqueness
  check proves an anchor is unique, NOT that it belongs to the intended entity. Reverted and
  re-applied anchored on the slug key block; verified land-cruiser-2018 carries no vinNote and
  total file size is byte-identical to the pre-fix state. Would otherwise have shipped a
  flex-fuel TSB warning onto a vehicle Toyota never built a flex-fuel version of. TWO RULES FOR
  FUTURE RUNS: anchor per-slug edits on the SLUG KEY, never a field value (powertrain strings
  repeat across Land Cruiser / Sequoia / Tundra); and \xa0 exists in this file's data strings,
  so ASCII-space regex/grep over inspect/index.html silently mismatches.
  QUEUE HYGIENE (unplanned, blocking): reconciled vinnote-queue.md against the live file --
  (a) 21 rows pointed at slugs that NO LONGER EXIST, orphaned by the 2026-09-03 key rename
  (0dfa937: chevy-* -> chevrolet-*, vw-* -> volkswagen-*, mercedes-* -> mercedes-benz-*); the
  queue was never updated, so any future run drawing one would have failed to find its slug.
  All 21 rewritten to canonical names and re-verified present. (b) 3 rows already had vinNotes
  (chrysler-300-2016 pri 81, mazda-cx5-2013 pri 86, plus the two done this run) -- removed.
  (c) toyota-highlander-2020 was missing a vinNote but ABSENT from the queue entirely (added
  after the 2026-06-04 generation) -- appended as pri 228. Queue 151 -> 146 rows and the
  invariant now holds exactly: 245 checklists, 99 with vinNote, 146 without, 146 queued, zero
  rows pointing at a missing slug, zero already-done rows.
  Sibling check: no blocking overlap -- Verified against: autovetting-vinnote-batch-2026-09-09
  (inspect/index.html, committed 48b9c9c, unpushed) touches nissan-titan-2017 / nissan-armada-2017
  only; autovetting-inspect-key-namespace-rename-2026-09-03 (0dfa937, already in origin/main)
  covered chevy-/vw-/mercedes- prefixes only; autovetting-phase-copy-and-template-fix-2026-08-14
  (scripts/render-blog.py, inspect/index.html, blog/*/index.html) touches no toyota-* slug.
  Grep of the full TASKS.md for rav4 / sequoia / land.cruiser / highlander returns no In-flight
  or Ready hit on toyota-rav4-2016, toyota-sequoia-2016 or toyota-land-cruiser-2018; only stale
  recall-audit Done entries (waves 20/21, 2026-08) whose findings this run reused rather than
  contradicted -- both summaries' "Takata does not cover this car" lines are wave-21 corrections
  and were left untouched. In-flight autovet-competitor-monitor (Competitors/, YourMechanic
  09-10), autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lincoln) and
  autovet-seo-content (Content/blog/, Subaru Outback 09-09) all orthogonal. Every Done (last 10)
  block naming inspect/index.html carries a - Started: date (checked; no backfill needed).
  No Re-sync needed. Additive per-slug data on disjoint slugs.
  Syntax-check: PASS (node validator, exit 0 -- Script 2 OK, Script 5 OK; both JSON-LD blocks
  reparse; tail intact through </html>). Dead-links: verified (only /decode/ added; directory
  exists). Scanner: PASS (574 files, exit 0).
  Full detail: _hub/Build-Log/2026-09-10.md

### autovetting-vinnote-batch-2026-09-09 — ready 2026-09-09 (COMMITTED, NOT PUSHED)

- Status: ready to deploy (committed locally as 48b9c9c; PUSH BLOCKED — GitHub PAT rejected)
- ⚠️ Push blocker: `git push` over HTTPS returned "Invalid username or token. Password
  authentication is not supported for Git operations." The PAT in
  ~/Documents/Claude/.credentials/github-config.json (prefix `ghp_krkG...`, rotated 2026-05-29,
  nominal expiry 2027-05-19) is no longer accepted by github.com. This same credential pushed
  successfully on 2026-09-03, so it has been revoked or invalidated since. SSH origin is
  unusable from the scheduled-run sandbox (port 22 / host-key verification blocked) and
  api.github.com is not reachable from the sandbox either, so the token could not be
  independently validated. Deploy path: Daniel runs push-deploy.sh from his own Terminal
  (SSH works there), or regenerates the PAT at github.com/settings/tokens and updates that
  one credential file. Logged in _hub/Awaiting-Daniel.md.
- Started: 2026-09-09 (02:00 MST overnight builder; launch-freeze alternate work = vinNote queue drain)
- Touched files: inspect/index.html, _hub/Content/vinnote-queue.md (gitignored), _hub/Build-Log/2026-09-09.md (gitignored), TASKS.md
- Notes:
  2026-09-09 02:00: FIRST PRODUCTIVE OVERNIGHT-BUILDER RUN SINCE 2026-08-12 — the folder
  mount that had been failing this task resolved; repo mounted, git worked, run completed
  end to end. Launch freeze still active and no new-vehicle launch queued, so took the
  Step-3 alternate path. Drained pri 77 nissan-titan-2017 + pri 78 nissan-armada-2017.
  Queue 151 -> 149 rows; vinNote count 95 -> 97.
  (1) nissan-titan-2017 -- STRUCTURAL CORRECTION to the standing rule: the 8th digit is the
      WRONG digit on this truck. Nissan encodes Titan / Titan XD powertrain in the 4TH digit:
      'A' = 5.6L VK56VD gas V8, 'B' = 5.0L Cummins V8 turbodiesel. Confirmed across multiple
      OEM/reman parts catalogues listing 2017 Titan XD engines as "5.6L (VIN A, 4th digit)"
      and "5.0L (VIN B, 4th digit, diesel)". Cummins was Titan XD only, never the half-ton
      Titan, so the same digit also disambiguates WHICH truck the listing is (different
      frames, payload, brakes, pricing behind one nameplate). Inspection consequence in the
      note: Cummins XD = DEF/DPF regen history, two fuel filters, stored-emissions scan;
      gas VK56VD = none of that, 7-speed fluid history + PRO-4X suspension/skid-plate wear.
  (2) nissan-armada-2017 -- SINGLE powertrain (structural note, no letter invented). Every
      U.S. 2017 Armada is the 5.6L VK56VD + 7-speed; no V6/diesel/hybrid/cylinder-deactivation,
      so the 8th digit sorts nothing. Note redirects to the generation break instead: 2017 is
      an all-new Y62 truck (global Nissan Patrol), not a facelift of the outgoing TA60, so a
      2017 shares little beyond the badge with a 2015 (frame, suspension, interior electronics,
      service procedures all differ) and older Armada TSBs/forum advice are non-transferable.
      Confirm 10th VIN digit 'H' = 2017 rather than trusting a listing title.
  Anti-fabrication: toyota-rav4-2016 (pri 79) was the third candidate and was DELIBERATELY
  SKIPPED — could not source, from a record-quality source, which 8th-digit letter separates
  the 2AR-FE gas car from the 2AR-FXE hybrid for MY2016. Row left in the queue rather than
  asserting a letter on inference. Next run: pri 79 only if sourceable, else pri 80
  toyota-sequoia-2016.
  Sibling check: no blocking overlap. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/, next=Lincoln), autovet-seo-content
  (Content/blog/) all orthogonal. Ready holds two blocks that DO name inspect/index.html —
  autovetting-inspect-key-namespace-rename-2026-09-03 and
  autovetting-phase-copy-and-template-fix-2026-08-14 — but both are already in origin/main
  (key rename = 0dfa937; origin/main..HEAD was 0 at start of run) and neither touches a
  nissan-* slug: the rename covered chevy-*/vw-*/mercedes-* prefixes only. Additive per-slug
  data on DISJOINT slugs. All Done (last 10) blocks carry a - Started: date (checked; no
  backfill needed). No Re-sync needed.
  Syntax-check: PASS (node validator, exit 0). NOTE: this run initially FAILED the gate —
  both inserted vinNote lines were written without a trailing comma, terminating the
  CHECKLISTS object literal early ("Unexpected identifier 'overallRisk'"). Caught before
  staging, fixed, re-run clean. Recording it because it is direct evidence the pre-commit
  validator is load-bearing, not ceremonial.
  Truncation guard: 17,754 lines before and after; git diff on inspect/index.html is exactly
  2 insertions(+), 0 deletions; tail intact through </html>.
  Dead-links: verified (only /decode/, which exists and is already linked from ~90 other
  vinNotes). Scanner: PASS (569 files, no secrets, exit 0).

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
### autovetting-ga-swap-06S3EWDPXK — ready 2026-08-14

- Status: ready to deploy (committed locally as 4456031; awaiting auto-pusher)
- Started: 2026-08-14 (Cowork session — user provided new GA snippet in chat)
- Touched files: 52 HTML files (all pages), scripts/render-blog.py, scripts/gate-check.py
- Notes:
  Site-wide swap of Google Analytics measurement ID from G-YM12JSF5D1 -> G-06S3EWDPXK.
  User pasted the new snippet in chat. 52 HTML files updated; verified 0 files reference
  the old ID, 52 reference the new one. Also updated GA_ID constant in render-blog.py
  so future blog renders emit the correct tag, and refreshed a stale comment in
  scripts/gate-check.py (G3) that named the wrong incident ID.
  Old .bak snapshots in pinpoint/ still contain the old tag - not shipped, gate ignores
  them, safe to leave for rollback history.
  G3 gate confirms single-ID consistency; all 27 critical gates pass.

#### autovetting-recall-audit-wave23-2026-08-12 — ready (pushed directly)

- Status: ready
- Started: 2026-08-12 (02:00 MST overnight builder)
- Task: recall-audit wave 23 — the generation-boundary sweep promoted to priority 1 by the wave-22
  queue. Launch freeze remains active (DANIEL-DECISIONS-2026-07-29 "KEEP FREEZE"; reallocation order =
  recall audit -> under-$15k study -> booking infra), so no vehicle was launched; priority 1 in that
  ordering is this workstream. Three parts: (a) systematic generation/facelift-boundary sweep of the
  CHECKLISTS records, (b) complete-set rebuild of chevy-silverado-2014 (wave-22 queue item 2), (c) the
  VEHICLE_MENU 4Runner misrouting flagged by the 2026-08-11 run and left for this track.
- Touched files: inspect/index.html, scripts/recall-ledger.json, _hub/Build-Log/2026-08-12.md
  (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-08-12 02:00: **10 generation-boundary errors found, 10 confirmed, 10 corrected** — a 10-for-10
  hit rate on the first systematic pass, from a candidate list of 10 read off all 245 slugs.
  1. toyota-avalon-2018 — written as the 5th-gen XX50. Real car = 4th-gen XX40 with the PORT-INJECTED
     2GR-FE (268 hp) + 6-speed U660E, not the 2GR-FKS (301 hp) + 8AT. The vinNote's headline buyer
     instruction was "GDI carbon buildup at 80-100k miles (walnut blast, $400-600)" — a service that
     does not apply to a port-injected engine. Same class as wave 22's vw-jetta-2018 DQ200 anchor.
     Rewrote trim/engine/summary/vinNote + powertrain, hybrid (2AR-FXE 200hp, not A25A-FXS 215hp) and
     infotainment items (2018 = Entune App Suite, NO CarPlay — that arrives with the 2019 redesign).
  2. toyota-highlander-2020 — engine read "2.4T I4 (265 hp)" and the summary asserted "no optional V6".
     The 2020-2022 XU70 is a 3.5L 2GR-FKS V6 (295 hp) + 8AT; the 2.4T is MY2023+. XSE dropped from the
     2020 trim list (added 2021). Mirror image of wave 21's highlander-2014 finding — same nameplate,
     same error, opposite direction.
  3. mercedes-gla-2020 — written as the H247 2nd gen (M260, 221 hp, 8G-DCT, MBUX). US 2020 GLA is the
     X156 1st gen (M270, 208 hp, 7G-DCT, COMAND); H247 is MY2021. The "$2,000-$5,000 mechatronic"
     anchor was priced against a transmission the car does not have. Fixed trim/engine/summary, both
     transmission + valve-cover items and their sources, renamed the MBUX section to COMAND.
  4. honda-crv-2015 — a facelift boundary INSIDE one generation, and a new sub-signature. Record said
     "K24Z7 + 5-speed automatic" with a full 5-speed shift-quality item and an ATF-DW1 anchor; the 2015
     refresh replaced BOTH with the direct-injected K24W and a CVT on HCF-2. Also missed the defining
     defect of the refreshed car: CVT judder per Honda SB 15-046 (3 modes; software update + fluid).
     Replaced the transmission item outright, fixed engine-item title, trim (SE dropped after 2014,
     Touring added 2015), engine and summary.
  5. infiniti-qx60-2018 — trim was the 2022+ L51 lineup ("Pure/Luxe/Sensory/Autograph"); the 2018 is
     1st-gen L50, a SINGLE trim with Premium / Premium Plus / Deluxe Touring packages. Summary opened
     by describing the 2022+ car as its subject. Dropped an unverifiable CVT part number (JF016E).
     NOTE: this trim string was mirrored into SIX VEHICLE_MENU rows + the checklist — all 7 moved.
  6. infiniti-qx80-2018 — "Base/Luxe/ProACTIV/Sensory/Autograph"; Luxe/Premium Select/Sensory are the
     2021 lineup. 2018 = QX80 and QX80 Limited. Trim-only fix; engine was correct.
  7. audi-q3-2019 — right generation (2019 IS the first US F3 year) but "184 hp" is the European 35
     TFSI figure; US cars are 228 hp / 45 TFSI / quattro standard. Split the "2nd gen 8U/F3" code that
     named both generations at once.
  8. chevy-blazer-2019 — listed a 2.0T that did not exist until MY2020, and spent its lead powertrain
     item on 2.0T oil consumption. 2019 = 2.5L (193 hp) or 3.6L V6 (308 hp) only. Item scoped to
     2020+; trim corrected to 2LT/3LT.
  9. jeep-wrangler-2018 — listed the 3.0L EcoDiesel (a 2020+ JL option), and did not mention that 2018
     is a TWO-WRANGLER year: Jeep sold the outgoing JK alongside the JL for the full model year.
  10. jeep-grand-cherokee-2021 — written as a two-row WL with Trailhawk and a 4xe. For 2021 the WL was
     sold ONLY as the three-row Grand Cherokee L; two-row WL + Trailhawk + 4xe are all 2022, and the
     2021 two-row on the market is a WK2 carryover. V6 corrected to 290 hp (WL) from 293 (WK2); 4xe
     recall item scoped to 2022+.
  **chevy-silverado-2014 complete-set rebuild — 3 of 3 fabricated.** 14V-293 "Engine Oil Cooler Line"
  = FCA Jeep Grand Cherokee / Dodge Durango adaptive cruise control; 16V-065 "Brake Fluid Pressure
  Sensor" = TOYOTA/LEXUS curtain-shield-airbag control module (MY2003-2006 Land Cruiser / Tundra /
  Sequoia / 4Runner / LX470 / GX470); 14V-355 "Front Seat Belt" = GM but LaCrosse/Lucerne/DeVille/DTS/
  Impala/Monte Carlo, passenger cars only (wave-19 right-parent-wrong-model signature). **14V-293 is
  the important one: it has been ledgered VERIFIED with makes ["Jeep","Dodge"] since wave 20 and sat on
  a Chevrolet slug through two later audit waves without G28 saying a word — because G28 checks that a
  number is ledgered, not that it BELONGS to the vehicle it sits on.** Second confirmed instance after
  14V-346 in wave 22; the proposed makes-mismatch gate is now demonstrated, not hypothetical. Replaced
  with the complete verified 15-campaign set (13V-315, 13V-488, 14V-152, 14V-246, 14V-301, 14V-374,
  14V-446, 15V-640, 16V-209, 16V-651, 17V-414, 17V-437, 19V-645, 19V-761, 21V-245) — all fifteen were
  ALREADY ledgered verified from the gmc-sierra-2014 work, so zero new ledger risk. Notables: the real
  oil-cooler-line fire recall is 14V-152 and it is the TRANSMISSION line not the engine's; 16V-651 and
  17V-437 are the same airbag defect twice because the first remedy was incomplete (a closed 16V-651
  does NOT imply a closed 17V-437 — written into both the entries and the vinNote); 14V-246 carries a
  GM do-not-drive advisory, preserved verbatim. vinNote line telling buyers to "verify all three listed
  recalls" corrected.
  **VEHICLE_MENU misrouting (flagged 2026-08-11, confirmed + fixed).** The 2010/2011/2012 4Runner rows
  routed to toyota-4runner-2008 — the 4th-gen N210 checklist — though the 5th-gen N280 launched MY2010.
  A 2011 buyer was handed X-REAS suspension, a 4.7L V8, 4th-gen dash cracking and recall 11V-113 (whose
  population is 2003-2009), none of which exists on their truck. Repointed all three to
  toyota-4runner-2018 (its vinNote confirms one unchanged powertrain across the N280 generation). Also
  removed a duplicate 2016 4Runner row with an empty key. **NEW SURFACE: VEHICLE_MENU maps year ->
  checklist independently of what the checklist says about itself, so it can misroute a generation
  boundary even when the checklist record is perfectly correct — invisible to any check that reads only
  the checklist. Wave 24 should sweep it in full.**
  Ledger: 14V293 kept verified + do-not-add note (naming the GM slugs it must never return to, pointing
  at 14V-152, and recording why G28 passed it twice); 16V065 and 14V355 promoted unverified_legacy ->
  verified with full populations, Part 573 PDF sources and do-not-add notes. 16V065's note also flags
  that it is a LEGITIMATE candidate for the toyota-4runner-2008 / toyota-sequoia-2016 /
  lexus-gx460-2015 predecessor eras — check years before adding. **Ledger 218 verified / 36
  unverified_legacy (was 216 / 38).**
  Wave 24 queue: (1) CONTINUE the generation-boundary sweep — 10/10 tonight was nowhere near
  exhaustive; already-noticed unverified candidates = kia-stinger-2018 (2.0T is Theta II not Lambda),
  mercedes-c300-2022 (M254 called a "PHEV"; it is a 48V mild hybrid), acura-mdx-2022 (YD3 = 3rd gen),
  honda-hrv-2023 (RU4 = 2nd gen), toyota-venza-2021, nissan-titan-2017, mitsubishi-outlander-2017.
  (2) Sweep VEHICLE_MENU for misrouting in full. (3) acura-tsx-2014 18V-661/19V-378/19V-502 (carried
  unreached from waves 21, 22, 23). (4) Oldest-first through the remaining 36: 14V292, 14V327, 15V258.
  (5) TWO gates now evidence-backed: (a) fail any recall ID that is neither 'Multiple' nor
  \d{2}[VE]-?\d{3} (wave 21), (b) **fail any recall entry whose ledger `makes` does not include the
  slug's `make` (wave 22) — recommend (b) FIRST, it is cheaper and closes the demonstrated hole.**
  (6) Signature list gains two: (e) mid-generation FACELIFT boundaries, which carry no generation label
  to flag them (honda-crv-2015); (f) VEHICLE_MENU year->checklist misrouting.
  Editing pattern worth keeping: exact-string replacement with a per-edit occurrence assert and a
  fail-fast that collects ALL mismatches before writing anything — 3 of 48 edits failed their assert on
  the first attempt and the file was never touched. Two failures were format drift (honda-crv-2015 is
  stored pretty-printed, one field per line, unlike most slugs); the third was the QX60 trim string
  appearing 7 times. Also: python len() = chars, wc -c = bytes; they will not agree on this file and
  that is not a truncation signal — compare line counts and the closing </html>.
  Sibling check: no true conflict. In-flight autovet-competitor-monitor (Competitors/),
  autovet-cpo-protocol-ingestion (Product/CPO-Protocols/), autovet-seo-content (Content/blog/) all
  orthogonal file-wise. Ready holds recall-audit waves 16-22 (same two files — this run is their direct
  continuation) plus autovetting-overnight-builder-2026-08-11-pinpoint-backlog, which touched
  pinpoint/index.html + sitemap.xml, neither of which this run went near. All Done (last 10) blocks
  carry a `- Started:` field — no backfill needed. Verified against:
  autovetting-recall-audit-wave22-2026-08-10. No Re-sync needed.
  NOT carried by this run: an unstaged .gitignore edit adding `bridges/` (dated 2026-08-12) was present
  in the working tree from another task. Left unstaged deliberately — this run committed only
  inspect/index.html and scripts/recall-ledger.json by explicit path.
  Syntax-check: PASS (node validator, scripts 2 and 5 OK, run after each of the three edit passes).
  Structural: 245 slugs before and after; line-count deltas asserted exactly (+12 recall array, -1 dead
  menu row); recall-ledger.json re-parses as valid JSON; file ends </html>.
  Dead-links: verified (no new href values introduced this run).
  Gate-check: 27 passed / 2 warned / 0 CRITICAL (both warnings pre-existing — recall backlog ratchet now
  36, down from 38; homepage-test-bc/index.html loading=lazy).
  Scanner: PASS (512 files, exit 0).
  Commit: e5f891f.

#### autovetting-overnight-builder-2026-08-11-pinpoint-backlog — ready (pushed directly)

- Status: ready
- Started: 2026-08-11 (02:00 MST overnight builder)
- Task: launch freeze remains active (DANIEL-DECISIONS-2026-07-29, "KEEP FREEZE" — reallocation order recall-audit -> under-$15k study -> booking-infra; vinNote batches fill-in only). This run's assignment protocol asked for a new vehicle launch, but a new vehicle launch means a new Inspect checklist, which is explicitly freeze-blocked per _hub/Awaiting-Daniel.md ("all five section-A targets require a new Inspect checklist and are blocked by the launch freeze — now 9 weeks old"). Judgment call: did NOT launch a vehicle. Instead shipped the Pinpoint-only backlog _hub/Awaiting-Daniel.md explicitly flagged as "NOT freeze-blocked — shippable tonight" and unshipped for five consecutive weekly-index runs (Section B items 3-5 + Section D + Section E.3). Recall-audit wave 23 (generation-boundary sweep) remains the standing priority-1 workstream and was NOT touched by this run to avoid duplicating/conflicting with that specialized track.
- Touched files: pinpoint/index.html, sitemap.xml, _hub/Build-Log/2026-08-11.md (gitignored), _hub/Awaiting-Daniel.md (gitignored), TASKS.md
- Notes:
  2026-08-11 02:00: FOUR items closed, all Pinpoint-only (no new Inspect checklist authored, so none freeze-blocked):
  1. Section D (Durango re-tag, carried 5 runs): re-tagged 'Dodge Durango R/T' (seats 6, budget 20-30k) and
     'Dodge Durango GT AWD' (seats 7+, budget 20-30k) from use_case 'weekend-fun' to 'road-trip' — a third
     Durango card ('Dodge Durango SXT/GT/R/T/SRT') was already correctly 'family-hauler', so this was a pure
     re-tag of an inconsistency within one nameplate, not a judgment call. Fills the empty
     road-trip/6/20-30k and road-trip/7+/20-30k cells.
  2. Section B item 4 (Sequoia older-year): added 'Toyota Sequoia SR5 (2008–2012, pre-facelift)' card,
     outdoor/7+/15-20k, pointed at the existing toyota-sequoia-2016 checklist (its trim field already covers
     "2nd gen XK60, 2008–2022" via the standard inspectUrl year=2016 direct-match path — no VEHICLE_MENU
     edit needed). Fills the empty outdoor/7+/15-20k cell.
  3. Section B item 5 (Enclave/Traverse 6-pass road-trip): added 'Buick Enclave Preferred (2018,
     high-mileage)' (road-trip/6/under-10k) and 'Chevrolet Traverse LS / LT (2018–2019)'
     (road-trip/6/10-15k), both pointed at the existing 2nd-gen buick-enclave-2018 /
     chevrolet-traverse-2018 checklists (same generation as the existing $22k family-hauler cards, framed at
     the cheaper/higher-mileage end of that same generation's used-market range). Fills both empty
     road-trip/6/under-10k and road-trip/6/10-15k cells.
  4. Section B item 3 (4Runner 3rd-row, "highest-priority finisher" of the config-gap items): added FOUR
     cards spanning all four empty budget tiers — 'Toyota 4Runner SR5 Premium 3rd Row (2010–2012)'
     (under-10k), '...(2013–2015)' (10-15k), 'Toyota 4Runner Limited 3rd Row (2016–2018)' (15-20k), and
     '...(2019–2021)' (20-30k) — all outdoor/6/[tier], all pointed at the existing toyota-4runner-2018
     checklist (5th-gen N280, vinNote confirms single engine across the generation). Did NOT touch
     VEHICLE_MENU for these years: VEHICLE_MENU's 2010–2012 Toyota/4Runner entries currently route to key
     'toyota-4runner-2008' (a 4th-gen/N210 checklist), which looks like exactly the class of
     generation-boundary bug wave 23 is sweeping for — flagging rather than fixing, since that's the
     recall-audit track's territory and out of scope here. All four new cards instead reuse the direct
     inspectUrl year=2018 match (same technique as the pre-existing Sequoia $28k card, whose inspectUrl also
     doesn't match its own 2008–2022 years field) — closes all four outdoor/6/[under-10k..20-30k] cells
     without going near the VEHICLE_MENU mismatch.
  5. Section E.3 (/decode/ sitemap): removed the /decode/ <url> entry from sitemap.xml. /decode/ is
     noindex + meta-refresh to /inspect/ (canonical /inspect/) — submitting it in the sitemap at priority
     0.9 contradicted that to crawlers. Mirrors the /next/ robots cleanup already done 2026-07-30 (no
     /next/ entry was ever added back to the sitemap either).
  Not touched this run (deliberately, to keep scope reviewable): Section E.1 (coalesce recall-audit waves
  16-21 Ready->Done — belongs to the recall-audit track's own bookkeeping, not this run's files), Section
  E.6 (29 no-must-have-chip cards spot-check — open-ended, no concrete target list yet).
  Sibling check: no true conflict. In-flight autovet-competitor-monitor (Competitors/), autovet-cpo-protocol-
  ingestion (Product/CPO-Protocols/), and autovet-seo-content (Content/blog/) are all orthogonal file-wise.
  Ready = recall-audit waves 16-22 (inspect/index.html + scripts/recall-ledger.json) — this run touched
  neither of those files, only pinpoint/index.html + sitemap.xml, so no overlap even though both tracks
  share the "overnight builder" label. Done (last 10) = vinnote-batches + recall-audit on inspect/index.html
  — none touch pinpoint/index.html or sitemap.xml. Verified against: _hub/Awaiting-Daniel.md weekly-index
  run #14 (2026-08-10), _hub/Filter-Schema.md, _hub/Pinpoint-Filter-Coverage.md. No Re-sync needed.
  Recall numbers: none cited or touched — this run made zero contact with inspect/index.html or
  scripts/recall-ledger.json.
  Syntax-check: PASS (node script-block check, exit 0). Dead-links: verified (all 304 inspectUrl values in
  pinpoint/index.html start with /inspect/; sitemap.xml re-validated as well-formed XML after the removal).
  Scanner: PASS (509 files, exit 0). Gate: scripts/gate-check.py — 27 pass / 2 warn (both pre-existing:
  recall backlog ratchet 38, homepage-test-bc lazy-load — unrelated to this run) / 0 CRITICAL; pre-push hook
  ran the same gate a second time before accepting the push, same result. Commit: 2e7a35c (pushed
  e9f288e..2e7a35c). Detail: _hub/Build-Log/2026-08-11.md.

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
  -> 216 verified / 38 unverified. Commit: cc8883a.
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


