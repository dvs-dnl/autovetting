# Pinpoint Modal — Filter Combination Coverage Map

_Auto-generated audit of every filter combination in `/pinpoint/`. Last built 2026-06-07._

## How the filter works

The Pinpoint modal applies a **strict AND** across all active filters (`getFiltered()` in `pinpoint/index.html`). A vehicle is shown only if it matches **every** selected option:

- `use_case` — exact match
- `seats` — exact match
- `budget` — exact match
- `must_have[]` — the vehicle must contain **all** selected must-haves (pick up to 2)
- free-text search — matches name/make

This guarantees requirement #2: selecting a must-have (or seats, budget, etc.) only ever *narrows* results — a vehicle never appears unless it satisfies all active filters.

**Catalog size:** 257 vehicles.

## Filter dimensions

| Dimension | Values |
|---|---|
| Use case | Daily commute, Family hauler, Road trip, Work / hauling, Weekend fun, Outdoor / off-road, First car |
| Seats | 2, 4–5, 6, 7+ |
| Budget | Under $10k, $10–15k, $15–20k, $20–30k, $30k+ |
| Must-haves (pick 2) | 3rd row, AWD/4WD, CarPlay, Hybrid/EV, Luxury, Manual, Tow 5,000 lb |

## 1. Single-value coverage — every option has ≥1 accurate match ✅

| Filter | Option | Matches | Example |
|---|---|--:|---|
| use_case | Daily commute | 113 | Acura TSX |
| use_case | Family hauler | 40 | Toyota Highlander V6 |
| use_case | Road trip | 15 | Chevrolet Equinox LS / LT / Premier |
| use_case | Work / hauling | 26 | Honda Ridgeline RTL |
| use_case | Weekend fun | 34 | Mazda3 SKYACTIV |
| use_case | Outdoor / off-road | 23 | Toyota 4Runner SR5 |
| use_case | First car | 6 | Honda Fit LX / Sport / EX / EX-L |
| seats | 2 | 4 | Subaru BRZ Premium / Limited (2nd gen) |
| seats | 4–5 | 205 | Acura TSX |
| seats | 6 | 26 | Toyota Highlander V6 |
| seats | 7+ | 22 | Honda Odyssey LX / EX / EX-L / Touring / Elite |
| budget | Under $10k | 38 | Acura TSX |
| budget | $10–15k | 25 | Chevy Bolt EV |
| budget | $15–20k | 59 | Honda Accord LX / EX-L / Sport / Touring (10th gen) |
| budget | $20–30k | 87 | Ford F-150 XLT / Lariat |
| budget | $30k+ | 48 | Ford F-150 XLT / Lariat / King Ranch (14th gen) |
| must-have | 3rd row | 47 | Toyota Highlander V6 |
| must-have | AWD/4WD | 66 | Subaru Outback 2.5i |
| must-have | CarPlay | 140 | Honda Accord LX / EX-L / Sport / Touring (10th gen) |
| must-have | Hybrid/EV | 45 | Toyota Prius |
| must-have | Luxury | 112 | Acura TSX |
| must-have | Manual | 14 | Toyota Tacoma SR5 |
| must-have | Tow 5,000 lb | 56 | Toyota Tacoma SR5 |

## 2. Use case × Budget

| Use case \ Budget | Under $10k | $10–15k | $15–20k | $20–30k | $30k+ |
|---|--:|--:|--:|--:|--:|
| Daily commute | 26 | 12 | 25 | 32 | 18 |
| Family hauler | 2 | 1 | 9 | 18 | 10 |
| Road trip | 2 | 1 | 5 | 5 | 2 |
| Work / hauling | 3 | 2 | 5 | 11 | 5 |
| Weekend fun | 3 | 4 | 9 | 15 | 3 |
| Outdoor / off-road | 1 | 3 | 5 | 5 | 9 |
| First car | 1 | 2 | 1 | 1 | 1 |

_— = no match. All use-case × budget pairs are covered._

## 3. Use case × Seats

| Use case \ Seats | 2 | 4–5 | 6 | 7+ |
|---|--:|--:|--:|--:|
| Daily commute | 1 | 111 | — | 1 |
| Family hauler | — | 1 | 22 | 17 |
| Road trip | — | 13 | 1 | 1 |
| Work / hauling | 1 | 23 | 1 | 1 |
| Weekend fun | 2 | 31 | 1 | — |
| Outdoor / off-road | — | 20 | 1 | 2 |
| First car | — | 6 | — | — |

## 4. Use case × Must-have

| Use case \ Must | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| Daily commute | 1 | 16 | 63 | 31 | 46 | 2 | 2 |
| Family hauler | 39 | 22 | 23 | 5 | 25 | 1 | 18 |
| Road trip | 2 | 2 | 7 | 3 | 10 | 1 | 1 |
| Work / hauling | 1 | 2 | 14 | 2 | 4 | 1 | 22 |
| Weekend fun | 1 | 8 | 16 | 2 | 22 | 4 | 1 |
| Outdoor / off-road | 3 | 14 | 13 | 1 | 5 | 4 | 12 |
| First car | — | 2 | 4 | 1 | — | 1 | — |

## 5. Seats × Must-have

| Seats \ Must | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| 2 | — | — | 3 | 1 | 1 | 3 | 1 |
| 4–5 | — | 41 | 111 | 39 | 82 | 10 | 30 |
| 6 | 25 | 13 | 14 | 3 | 15 | 1 | 13 |
| 7+ | 22 | 12 | 12 | 2 | 14 | — | 12 |

## 6. Budget × Must-have

| Budget \ Must | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| Under $10k | 2 | 6 | 5 | 4 | 8 | 3 | 3 |
| $10–15k | 2 | 4 | 4 | 2 | 6 | 2 | 3 |
| $15–20k | 10 | 10 | 27 | 6 | 26 | 4 | 12 |
| $20–30k | 19 | 25 | 65 | 18 | 48 | 3 | 22 |
| $30k+ | 14 | 21 | 39 | 15 | 24 | 2 | 16 |

## 7. Must-have × Must-have (pick-2 grid)

| | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| 3rd row | · | 25 | 25 | 5 | 29 | 1 | 24 |
| AWD/4WD | 25 | · | 35 | 8 | 34 | 6 | 23 |
| CarPlay | 25 | 35 | · | 28 | 56 | 7 | 29 |
| Hybrid/EV | 5 | 8 | 28 | · | 18 | 1 | 3 |
| Luxury | 29 | 34 | 56 | 18 | · | 3 | 17 |
| Manual | 1 | 6 | 7 | 1 | 3 | · | 2 |
| Tow 5,000 lb | 24 | 23 | 29 | 3 | 17 | 2 | · |

_All 21 valid must-have pairs return at least one accurate match (e.g. `Manual + Hybrid/EV` → Honda CR-Z; `Manual + 3rd row` → 2012 Mazda5 Sport)._

## 8. Intentionally-empty combinations

These combinations return zero results **by design** — they are physically contradictory or have no accurate real-world vehicle. They are left empty rather than filled with a wrong match (which would violate requirement #1).

| Combination | Reason |
|---|---|
| Daily commute + 6 seats | Atypical — no accurate vehicle of this size fits this use case. |
| Family hauler + 2 seats | Contradictory — a family hauler cannot seat only two. |
| Road trip + 2 seats | Atypical — no accurate 2-seat vehicle fits this use case. |
| Weekend fun + 7+ seats | Atypical — no accurate vehicle of this size fits this use case. |
| Outdoor / off-road + 2 seats | Atypical — no accurate 2-seat vehicle fits this use case. |
| First car + 2 seats | Atypical — no accurate 2-seat vehicle fits this use case. |
| First car + 6 seats | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + 7+ seats | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + 3rd row | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + Luxury | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + Tow 5,000 lb | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |

_When a user lands on an empty combination, the modal shows the "No picks match those filters — Clear filters" state._

## 9. Data-accuracy corrections applied (2026-06-07)

Before this pass, many vehicles carried must-have tags they do not actually qualify for, which made them appear under filters they should not. 44 tag corrections were applied:

- **Removed false `hybrid-ev`** from 15 gas-only Chevrolets (Silverado, Tahoe, Suburban, Colorado, Equinox, Traverse, Cruze, Blazer, Trailblazer, Trax, Malibu).
- **Removed false `manual`** from 14 automatic/CVT-only models (Toyota Sienna, Ford Fusion, Mazda CX-5/CX-9/Mazda6, GMC Sierra, Honda Insight, Genesis GV70/GV80, Buick Envision, Jeep Wrangler 4xe).
- **Removed false `tow-5000`** from 13 vehicles rated under 5,000 lb (Jeep Wrangler — manual caps at 3,500; Ford Bronco/Bronco Sport, Edge, Escape, EcoSport, Mustang Mach-E, Highlander Hybrid).
- **Removed false `awd-4wd`** from the rear-drive Subaru BRZ.
- **Added missing `3-row`** to the INFINITI QX80 and Mercedes GLS (7-seaters that were under-tagged).
- **Added accurate `manual`** to the Toyota Tacoma (real 6-speed, tows >5,000) to legitimately cover `Manual + Tow`.

## 10. Vehicles added to close real gaps (17)

| Vehicle | Use case | Seats | Budget | Must-haves | Closes |
|---|---|--:|---|---|---|
| Honda CR-Z EX | Daily commute | 2 | Under $10k | Hybrid/EV, Manual | Commute+2 seats; Manual+Hybrid |
| Toyota Corolla LE / SE | First car | 4–5 | $10–15k | CarPlay | Starter+$10–15k; Starter+CarPlay |
| Honda Civic Sport | First car | 4–5 | $15–20k | CarPlay, Manual | Starter+$15–20k; Starter+Manual |
| Subaru Crosstrek Premium | First car | 4–5 | $20–30k | AWD/4WD, CarPlay | Starter+$20–30k; Starter+AWD |
| Toyota Prius c | First car | 4–5 | $10–15k | Hybrid/EV | Starter+Hybrid |
| Subaru Crosstrek Limited | First car | 4–5 | $30k+ | AWD/4WD, CarPlay | Starter+$30k+ |
| Toyota Avalon XLE | Road trip | 4–5 | $10–15k | Luxury | Road trip+$10–15k |
| Volkswagen GTI | Road trip | 4–5 | $15–20k | CarPlay, Manual | Road trip+Manual |
| Buick Enclave Essence | Road trip | 6 | $15–20k | 3rd row, Luxury, Tow 5,000 lb | Road trip+6 seats; Road trip+Tow |
| Nissan Frontier SV | Work / hauling | 4–5 | $10–15k | Tow 5,000 lb | Work+$10–15k |
| Ford F-150 XL Regular Cab | Work / hauling | 2 | $15–20k | CarPlay, Tow 5,000 lb | Work+2 seats |
| Chevrolet Silverado 1500 WT Crew | Work / hauling | 6 | $20–30k | CarPlay, Tow 5,000 lb | Work+6 seats |
| Chevrolet Suburban LS | Work / hauling | 7+ | $10–15k | 3rd row, AWD/4WD, Tow 5,000 lb | Work+7+ seats; Work+3rd row |
| Subaru Forester Premium | Family hauler | 4–5 | $20–30k | AWD/4WD, CarPlay | Family hauler+4–5 seats |
| Mazda5 Sport | Family hauler | 6 | Under $10k | 3rd row, Manual | Family hauler+Manual; 3rd row+Manual |
| Chevrolet Tahoe Z71 | Outdoor / off-road | 6 | $30k+ | AWD/4WD, 3rd row, Tow 5,000 lb, CarPlay | Outdoor+6 seats |
| Dodge Durango R/T | Weekend fun | 6 | $20–30k | 3rd row, Tow 5,000 lb, CarPlay | Weekend fun+Tow; Weekend fun+3rd row |
