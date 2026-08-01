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

## Ready to deploy / publish

*Tasks finished locally and verified. The hub orchestrator only pushes what's in this section.*

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

## Done (last 10)

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
