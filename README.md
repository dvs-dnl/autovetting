# autovetting

> Master index: [INDEX.md](../INDEX.md) — map of every project under `/Users/danieldavis/Documents/Claude/`, including cross-project artifacts and shared research.

A four-step used-car research tool: pinpoint the right model, find listings, decode a VIN, get a model-specific pre-purchase inspection checklist. Built from NHTSA recall data, owner-reported failure patterns, and decades of mechanic intel.

**Live at:** [autovetting.com](https://autovetting.com)

## The four steps

| Step | Path | What it does |
|---|---|---|
| 1. Pinpoint | `/pinpoint/` | Filterable catalog of long-lived used vehicles by body type, budget, and reliability tier. |
| 2. Search | `/search/` | Watch-list tracker for listings across Craigslist, Facebook Marketplace, Cars.com, AutoTrader, and dealer inventory. |
| 3. Decode | `/decode/` | Paste a VIN; NHTSA vPIC returns year/make/model/trim/engine and hands off to the right checklist. |
| 4. Inspect | `/inspect/` | Model-specific pre-purchase checklist with recalls, common failures, and mileage-banded issues. |

## Project layout

```
/                  → homepage hub
/pinpoint/         → research catalog
/search/           → listing watch-list
/decode/           → VIN decoder
/inspect/          → inspection checklist
/garage/           → user-saved vehicles (localStorage)
/assets/
  ├─ css/site.css  → shared tokens, header, footer, buttons
  └─ img/
     └─ favicon.svg
CNAME              → autovetting.com
```

## Lineage

AutoVetting was incubated inside [TrailManual](https://trailmanual.com)'s "Used Garage" buyer's guide. Same operator, same anti-affiliate worldview, distinct brands.

## License

All rights reserved. Content not yet open-sourced; contact dvs.dnl@gmail.com for licensing inquiries.

## Project hub docs
Business plan, strategy, build logs, and all non-deployable project documentation live in `_hub/`. That folder is gitignored and never deployed to GitHub Pages.
