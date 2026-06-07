# Pinpoint Modal — Filter Combination Coverage Map

_Auto-generated audit of every filter combination in `/pinpoint/`. Last built 2026-06-07._

## How the filter works

The Pinpoint modal applies a **strict AND** across all active filters (`getFiltered()` in `pinpoint/index.html`). A vehicle is shown only if it matches **every** selected option: `use_case`, `seats`, `budget`, and **all** selected `must_have` items (pick up to 2), plus the free-text search. Selecting any filter only ever narrows results.

**Catalog size:** 307 vehicles.

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
| use_case | Daily commute | 117 | Acura TSX |
| use_case | Family hauler | 45 | Toyota Highlander V6 |
| use_case | Road trip | 25 | Chevrolet Equinox LS / LT / Premier |
| use_case | Work / hauling | 34 | Honda Ridgeline RTL |
| use_case | Weekend fun | 41 | Mazda3 SKYACTIV |
| use_case | Outdoor / off-road | 31 | Toyota 4Runner SR5 |
| use_case | First car | 14 | Honda Fit LX / Sport / EX / EX-L |
| seats | 2 | 5 | Subaru BRZ Premium / Limited (2nd gen) |
| seats | 4–5 | 240 | Acura TSX |
| seats | 6 | 30 | Toyota Highlander V6 |
| seats | 7+ | 32 | Honda Odyssey LX / EX / EX-L / Touring / Elite |
| budget | Under $10k | 38 | Acura TSX |
| budget | $10–15k | 31 | Chevy Bolt EV |
| budget | $15–20k | 67 | Honda Accord LX / EX-L / Sport / Touring (10th gen) |
| budget | $20–30k | 110 | Ford F-150 XLT / Lariat |
| budget | $30k+ | 61 | Ford F-150 XLT / Lariat / King Ranch (14th gen) |
| must-have | 3rd row | 58 | Toyota Highlander V6 |
| must-have | AWD/4WD | 92 | Subaru Outback 2.5i |
| must-have | CarPlay | 183 | Honda Accord LX / EX-L / Sport / Touring (10th gen) |
| must-have | Hybrid/EV | 52 | Toyota Prius |
| must-have | Luxury | 120 | Acura TSX |
| must-have | Manual | 24 | Toyota Tacoma SR5 |
| must-have | Tow 5,000 lb | 70 | Toyota Tacoma SR5 |

## 2. Use case × Budget

| Use case \ Budget | Under $10k | $10–15k | $15–20k | $20–30k | $30k+ |
|---|--:|--:|--:|--:|--:|
| Daily commute | 26 | 12 | 25 | 36 | 18 |
| Family hauler | 2 | 1 | 9 | 20 | 13 |
| Road trip | 2 | 2 | 6 | 11 | 4 |
| Work / hauling | 3 | 2 | 8 | 14 | 7 |
| Weekend fun | 3 | 4 | 9 | 19 | 6 |
| Outdoor / off-road | 1 | 5 | 5 | 8 | 12 |
| First car | 1 | 5 | 5 | 2 | 1 |

_All use-case × budget pairs are covered._

## 3. Use case × Seats

| Use case \ Seats | 2 | 4–5 | 6 | 7+ |
|---|--:|--:|--:|--:|
| Daily commute | 1 | 114 | 1 | 1 |
| Family hauler | — | 1 | 22 | 22 |
| Road trip | — | 19 | 1 | 5 |
| Work / hauling | 1 | 28 | 4 | 1 |
| Weekend fun | 3 | 36 | 1 | 1 |
| Outdoor / off-road | — | 28 | 1 | 2 |
| First car | — | 14 | — | — |

## 4. Use case × Must-have

| Use case \ Must | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| Daily commute | 2 | 17 | 67 | 33 | 47 | 3 | 2 |
| Family hauler | 44 | 25 | 28 | 6 | 27 | 1 | 19 |
| Road trip | 6 | 7 | 16 | 4 | 15 | 2 | 3 |
| Work / hauling | 1 | 5 | 20 | 3 | 4 | 2 | 30 |
| Weekend fun | 2 | 12 | 23 | 2 | 22 | 9 | 3 |
| Outdoor / off-road | 3 | 22 | 19 | 2 | 5 | 4 | 13 |
| First car | — | 4 | 10 | 2 | — | 3 | — |

## 5. Seats × Must-have

| Seats \ Must | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| 2 | — | — | 4 | 1 | 1 | 4 | 1 |
| 4–5 | — | 60 | 141 | 44 | 86 | 19 | 37 |
| 6 | 26 | 14 | 16 | 4 | 15 | 1 | 16 |
| 7+ | 32 | 18 | 22 | 3 | 18 | — | 16 |

## 6. Budget × Must-have

| Budget \ Must | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| Under $10k | 2 | 6 | 5 | 4 | 8 | 3 | 3 |
| $10–15k | 2 | 7 | 6 | 2 | 6 | 3 | 3 |
| $15–20k | 10 | 12 | 32 | 7 | 26 | 6 | 15 |
| $20–30k | 25 | 35 | 88 | 21 | 54 | 8 | 27 |
| $30k+ | 19 | 32 | 52 | 18 | 26 | 4 | 22 |

## 7. Must-have × Must-have (pick-2 grid)

| | 3rd row | AWD/4WD | CarPlay | Hybrid/EV | Luxury | Manual | Tow 5,000 lb |
|---|--:|--:|--:|--:|--:|--:|--:|
| 3rd row | · | 32 | 36 | 6 | 33 | 1 | 28 |
| AWD/4WD | 32 | · | 58 | 10 | 35 | 10 | 32 |
| CarPlay | 36 | 58 | · | 34 | 64 | 16 | 41 |
| Hybrid/EV | 6 | 10 | 34 | · | 20 | 1 | 4 |
| Luxury | 33 | 35 | 64 | 20 | · | 3 | 17 |
| Manual | 1 | 10 | 16 | 1 | 3 | · | 3 |
| Tow 5,000 lb | 28 | 32 | 41 | 4 | 17 | 3 | · |

_All 21 valid must-have pairs return at least one accurate match._

## 8. Intentionally-empty combinations

Zero results **by design** — physically contradictory or no accurate real-world vehicle. Left empty rather than filled with a wrong match.

| Combination | Reason |
|---|---|
| Family hauler + 2 seats | Contradictory — a family hauler cannot seat only two. |
| Road trip + 2 seats | Atypical — no accurate 2-seat vehicle fits this use case. |
| Outdoor / off-road + 2 seats | Atypical — no accurate 2-seat vehicle fits this use case. |
| First car + 2 seats | Atypical — no accurate 2-seat vehicle fits this use case. |
| First car + 6 seats | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + 7+ seats | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + 3rd row | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + Luxury | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |
| First car + Tow 5,000 lb | Atypical — a first car is rarely a 3-row / luxury / tow rig / 6–7-seater. |

## 9. Data-accuracy corrections (2026-06-07)

44 must-have tags were corrected so vehicles only appear under filters they truly satisfy: removed false `hybrid-ev` from 15 gas Chevrolets, false `manual` from 14 automatic/CVT-only models, false `tow-5000` from 13 sub-5,000-lb vehicles (incl. Jeep Wrangler, which caps at 3,500 with the manual), and false `awd-4wd` from the RWD Subaru BRZ; added missing `3-row` to the QX80 and GLS, and accurate `manual` to the Tacoma.

## 10. Vehicles added to close gaps & build depth

The catalog grew from 240 → **307** vehicles across two passes: **17** to close genuine gaps, then **50** to deepen thin cells. Coverage of every realistic combination now has multiple accurate options.

### Depth-building batch (50 vehicles)

| Vehicle | Use case | Seats | Budget | Must-haves |
|---|---|--:|---|---|
| Mazda3 i Touring | First car | 4–5 | $10–15k | Manual |
| Honda Fit EX | First car | 4–5 | $10–15k | CarPlay |
| Hyundai Accent SE | First car | 4–5 | $10–15k | CarPlay |
| Toyota Corolla Hatchback SE | First car | 4–5 | $15–20k | CarPlay, Manual |
| Kia Forte GT-Line | First car | 4–5 | $15–20k | CarPlay |
| Subaru Impreza Sport Hatch | First car | 4–5 | $15–20k | AWD/4WD, CarPlay |
| Toyota Prius L Eco | First car | 4–5 | $15–20k | Hybrid/EV |
| Mazda CX-30 2.5 S | First car | 4–5 | $20–30k | AWD/4WD, CarPlay |
| Toyota Camry XSE | Road trip | 4–5 | $20–30k | CarPlay, Luxury |
| Honda Accord Touring 2.0T | Road trip | 4–5 | $20–30k | CarPlay, Luxury |
| Subaru Outback Onyx XT | Road trip | 4–5 | $20–30k | AWD/4WD, CarPlay |
| Toyota Highlander XLE AWD | Road trip | 7+ | $30k+ | 3rd row, AWD/4WD, CarPlay, Tow 5,000 lb |
| Kia Telluride EX AWD | Road trip | 7+ | $30k+ | 3rd row, AWD/4WD, CarPlay, Tow 5,000 lb |
| Chrysler Pacifica Limited | Road trip | 7+ | $20–30k | 3rd row, CarPlay, Luxury |
| Honda Odyssey Elite | Road trip | 7+ | $20–30k | 3rd row, CarPlay, Luxury |
| Volkswagen Golf Alltrack S | Road trip | 4–5 | $15–20k | AWD/4WD, CarPlay, Manual |
| Subaru Legacy Limited | Road trip | 4–5 | $10–15k | AWD/4WD |
| Toyota Avalon Hybrid XLE | Road trip | 4–5 | $20–30k | Hybrid/EV, CarPlay, Luxury |
| Subaru Forester 2.5i Premium (SJ) | Outdoor / off-road | 4–5 | $10–15k | AWD/4WD |
| Jeep Cherokee Trailhawk (KL) | Outdoor / off-road | 4–5 | $10–15k | AWD/4WD |
| Toyota RAV4 Adventure AWD | Outdoor / off-road | 4–5 | $20–30k | AWD/4WD, CarPlay |
| Ford Bronco Sport Badlands | Outdoor / off-road | 4–5 | $20–30k | AWD/4WD, CarPlay |
| Subaru Crosstrek Sport (GU) | Outdoor / off-road | 4–5 | $20–30k | AWD/4WD, CarPlay |
| Toyota RAV4 Hybrid XSE AWD | Outdoor / off-road | 4–5 | $30k+ | AWD/4WD, Hybrid/EV, CarPlay |
| Jeep Wrangler Unlimited Sahara (JL) | Outdoor / off-road | 4–5 | $30k+ | AWD/4WD, CarPlay |
| Toyota 4Runner TRD Off-Road Premium | Outdoor / off-road | 4–5 | $30k+ | AWD/4WD, CarPlay, Tow 5,000 lb |
| Toyota Tacoma TRD Off-Road 6MT | Work / hauling | 4–5 | $20–30k | AWD/4WD, CarPlay, Tow 5,000 lb, Manual |
| Ford Ranger XLT FX4 | Work / hauling | 4–5 | $20–30k | CarPlay, Tow 5,000 lb |
| GMC Sierra 1500 Pro Double Cab | Work / hauling | 6 | $15–20k | Tow 5,000 lb |
| Ram 1500 Tradesman Quad Cab | Work / hauling | 6 | $15–20k | Tow 5,000 lb |
| Chevrolet Colorado WT Extended | Work / hauling | 4–5 | $15–20k | CarPlay, Tow 5,000 lb |
| Ford F-150 PowerBoost Hybrid XLT | Work / hauling | 6 | $30k+ | Hybrid/EV, CarPlay, Tow 5,000 lb |
| Honda Ridgeline RTL-E AWD | Work / hauling | 4–5 | $20–30k | AWD/4WD, CarPlay, Tow 5,000 lb |
| Nissan Frontier Pro-4X (3rd gen) | Work / hauling | 4–5 | $30k+ | AWD/4WD, CarPlay, Tow 5,000 lb |
| Ford Mustang GT Premium | Weekend fun | 4–5 | $20–30k | CarPlay, Manual |
| Mazda MX-5 Miata Club | Weekend fun | 2 | $20–30k | CarPlay, Manual |
| Chevrolet Camaro SS 1LE | Weekend fun | 4–5 | $20–30k | CarPlay, Manual |
| Toyota GR Corolla Core | Weekend fun | 4–5 | $30k+ | AWD/4WD, CarPlay, Manual |
| Jeep Grand Cherokee SRT | Weekend fun | 4–5 | $30k+ | AWD/4WD, CarPlay, Tow 5,000 lb |
| Dodge Durango GT AWD | Weekend fun | 7+ | $20–30k | 3rd row, AWD/4WD, CarPlay, Tow 5,000 lb |
| Subaru WRX Premium (VB) | Weekend fun | 4–5 | $30k+ | AWD/4WD, CarPlay, Manual |
| Volkswagen Atlas SE 4Motion | Daily commute | 6 | $20–30k | 3rd row, AWD/4WD, CarPlay |
| Honda Civic Si Sedan | Daily commute | 4–5 | $20–30k | CarPlay, Manual |
| Toyota Corolla Hybrid LE | Daily commute | 4–5 | $20–30k | Hybrid/EV, CarPlay |
| Honda Accord Hybrid EX-L | Daily commute | 4–5 | $20–30k | Hybrid/EV, CarPlay, Luxury |
| Toyota Sienna XLE (gas, 3rd gen) | Family hauler | 7+ | $20–30k | 3rd row, CarPlay |
| Kia Carnival SX | Family hauler | 7+ | $30k+ | 3rd row, CarPlay, Luxury |
| Toyota Highlander Hybrid XLE AWD | Family hauler | 7+ | $30k+ | 3rd row, AWD/4WD, Hybrid/EV, CarPlay |
| Volkswagen Atlas SEL Premium | Family hauler | 7+ | $20–30k | 3rd row, AWD/4WD, CarPlay, Tow 5,000 lb |
| Hyundai Palisade SEL AWD | Family hauler | 7+ | $30k+ | 3rd row, AWD/4WD, CarPlay, Luxury |
