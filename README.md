# autovetting

A four-step used-car research tool — Pinpoint the right model, Search listings smart, Decode the VIN, then Inspect with a model-specific pre-purchase checklist. Built from NHTSA recall data, owner-reported failure patterns, and decades of mechanic intel.

**Live at:** [autovetting.com](https://autovetting.com)

## The four steps

| Step | Path | What it does |
|---|---|---|
| 1. Pinpoint | `/pinpoint/` | Filterable database of long-lived used vehicles by body type, budget, and reliability tier. |
| 2. Search | `/search/` | Listing-hunt playbook for Craigslist, Facebook Marketplace, Cars.com, dealer inventory. *(scaffold — content in progress)* |
| 3. Decode | `/decode/` | Paste a VIN, NHTSA vPIC returns year/make/model/trim/engine, hands off to the right checklist. |
| 4. Inspect | `/inspect/` | Model-specific pre-purchase checklist with recalls, common failures, mileage-banded issues, and book-a-shop CTA. |

## Project layout

```
/                  → homepage hub
/pinpoint/         → research tool (ported from TrailManual Used Garage)
/search/           → listing playbook (Phase 1 scaffold)
/decode/           → VIN decoder
/inspect/          → inspection checklist + booking + shop network application
/assets/
  ├─ css/site.css  → shared tokens, header, footer, buttons
  ├─ js/           → (reserved)
  └─ img/
     └─ favicon.svg
CNAME              → autovetting.com
```

## Status

Phase 1 — content + lead capture. Inspection booking goes live with the Phoenix-area shop network rollout (summer 2026).

The free research tools (Pinpoint / Search / Decode / Inspect) are the loss leader. The paid product is a confidence-adding pre-purchase inspection performed by a vetted local independent shop — book inside the same flow.

## Stack

Currently a static multi-page site. Will migrate to Astro 6 + Sveltia CMS as the content count grows (see `Projects/AutoVet/Architecture-Research-2026-05-24.md` in the maintainer's working tree).

## Lineage

AutoVetting was incubated inside [TrailManual](https://trailmanual.com)'s "Used Garage" buyer's guide. Same operator, same anti-affiliate worldview, distinct brands.

## License

All rights reserved. Content not yet open-sourced; contact dvs.dnl@gmail.com for licensing inquiries.
