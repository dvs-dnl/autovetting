#!/usr/bin/env python3
"""
render-vetting-report.py — generate a $49 AutoVetting Vetting Report (fulfillment tool).

Usage:
    python3 scripts/render-vetting-report.py <checklist-key> [--vin VIN] [--price 18500] \
        [--buyer "Name"] [--listing URL] [--out path.html]

Pulls the vehicle's checklist from inspect/index.html (single source of truth) and renders a
print-ready HTML report to _hub/Booking-Infrastructure/Reports/ (gitignored — reports are
per-customer deliverables, never deployed).

Manual fulfillment steps the operator MUST do before sending:
  1. Run the VIN at nhtsa.gov/recalls; fill the "VIN-specific recall status" box.
  2. Sanity-check cost ranges against current local quotes if time allows.
  3. Print to PDF (browser) and email to the buyer.
"""
import argparse
import html
import json
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_checklists():
    src = (REPO / "inspect" / "index.html").read_text(encoding="utf-8")
    i = src.index("const CHECKLISTS = {")
    start = src.index("{", i)
    depth = 0
    for j in range(start, len(src)):
        c = src[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    blob = src[start:end]
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write("const CHECKLISTS = " + blob + ";\n")
        f.write("process.stdout.write(JSON.stringify(CHECKLISTS));\n")
        tmp = f.name
    out = subprocess.run(["node", tmp], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def esc(s):
    return html.escape(str(s or ""))


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "")


SEV_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key")
    ap.add_argument("--vin", default="")
    ap.add_argument("--price", type=float, default=0)
    ap.add_argument("--buyer", default="")
    ap.add_argument("--listing", default="")
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    cls = load_checklists()
    if a.key not in cls:
        near = [k for k in cls if a.key.split("-")[0] in k][:8]
        sys.exit(f"Unknown key '{a.key}'. Close matches: {near}")
    c = cls[a.key]

    ledger = json.loads((REPO / "scripts" / "recall-ledger.json").read_text())
    verified = set(ledger.get("verified", {}))

    vehicle = f"{c['year']} {c['make']} {c['model']}"
    today = date.today().isoformat()

    # ---- items, ordered by severity
    items = []
    for sec in c.get("sections", []):
        for it in sec.get("items", []):
            items.append((sec.get("title", ""), it))
    items.sort(key=lambda x: SEV_ORDER.get((x[1].get("risk") or "medium").lower(), 2))

    rows = []
    for sec_title, it in items:
        risk = (it.get("risk") or "medium").title()
        cost = strip_tags(it.get("cost", ""))
        rows.append(
            f"<tr><td><strong>{esc(strip_tags(it.get('title')))}</strong>"
            f"<br><span class='dim'>{esc(sec_title)}</span></td>"
            f"<td class='sev sev-{risk.lower()}'>{esc(risk)}</td>"
            f"<td>{esc(strip_tags(it.get('desc'))[:340])}</td>"
            f"<td>{esc(cost)}</td></tr>"
        )

    # ---- recalls: only assert ledger-verified ones; rest noted generically
    rec_rows, unverified_present = [], False
    for r in c.get("recalls", []):
        num = (r.get("number") or "").replace("-", "")
        if r.get("number") == "Multiple" or num in verified:
            rec_rows.append(
                f"<tr><td>{esc(r.get('number'))}</td><td>{esc(r.get('title'))}</td>"
                f"<td>{esc(strip_tags(r.get('desc')))}</td></tr>"
            )
        else:
            unverified_present = True
    unv_note = (
        "<p class='dim'>Additional campaigns may apply to this model; the VIN check below is "
        "authoritative.</p>" if unverified_present else ""
    )

    neg = []
    for sec_title, it in items[:6]:
        cost = strip_tags(it.get("cost", ""))
        if cost and cost.lower() not in ("standard", ""):
            neg.append(
                f"<li>If <strong>{esc(strip_tags(it.get('title')))}</strong> shows up in the "
                f"inspection: typical exposure is <strong>{esc(cost)}</strong> — ask for that "
                f"off the price or a pre-sale repair with receipts.</li>"
            )
    if not neg:
        neg.append(
            "<li>Use the inspection findings sheet: every Severity 3+ item with a repair "
            "estimate is a line-item discount request.</li>"
        )

    price_block = (
        f"<p>At your target price of <strong>${a.price:,.0f}</strong>, a $150 pre-purchase "
        f"inspection is {150 / a.price * 100:.2f}% of the purchase — and the median negotiation "
        f"win from documented findings exceeds it many times over.</p>" if a.price else ""
    )

    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>AutoVetting Vetting Report — {esc(vehicle)}</title>
<meta name="robots" content="noindex">
<style>
 body {{ font-family: Inter, -apple-system, Segoe UI, sans-serif; color:#16213a; margin:40px auto; max-width:820px; padding:0 24px; }}
 h1 {{ font-size:26px; margin-bottom:2px; }} h2 {{ font-size:18px; margin-top:30px; border-bottom:2px solid #7c6cff; padding-bottom:4px; }}
 .brand {{ color:#7c6cff; font-weight:800; }} .dim {{ color:#69708c; font-size:12px; }}
 table {{ border-collapse:collapse; width:100%; font-size:13px; margin-top:10px; }}
 th,td {{ border:1px solid #d9ddec; padding:7px 9px; text-align:left; vertical-align:top; }}
 th {{ background:#f1f2fb; }}
 .sev {{ font-weight:700; white-space:nowrap; }} .sev-critical {{ color:#c0203c; }} .sev-high {{ color:#d4622a; }}
 .sev-medium {{ color:#9a7b14; }} .sev-low {{ color:#2e7d4f; }}
 .fillbox {{ border:2px dashed #7c6cff; border-radius:10px; padding:14px 16px; background:#faf9ff; }}
 .meta td {{ border:none; padding:2px 14px 2px 0; }}
 footer {{ margin-top:36px; font-size:11px; color:#69708c; }}
 @media print {{ body {{ margin:10mm; }} }}
</style></head><body>
<h1><span class="brand">AutoVetting</span> Vetting Report</h1>
<p class="dim">Prepared {today} · autovetting.com · This report is advisory and is not a substitute for a physical pre-purchase inspection.</p>
<table class="meta"><tr><td><strong>Vehicle</strong></td><td>{esc(vehicle)} ({esc(c.get('trim',''))})</td></tr>
<tr><td><strong>VIN</strong></td><td>{esc(a.vin) or '<em>provided by buyer</em>'}</td></tr>
<tr><td><strong>Buyer</strong></td><td>{esc(a.buyer) or '—'}</td></tr>
<tr><td><strong>Listing</strong></td><td>{esc(a.listing) or '—'}</td></tr>
<tr><td><strong>Overall risk profile</strong></td><td><strong>{esc(c.get('overallRiskLabel', c.get('overallRisk','')))}</strong></td></tr></table>

<h2>1. The verdict in one paragraph</h2>
<p>{esc(strip_tags(c.get('summary','')))}</p>
{price_block}

<h2>2. VIN-specific recall status</h2>
<div class="fillbox"><strong>Operator: complete before sending.</strong> Run the VIN at
<strong>nhtsa.gov/recalls</strong> and record results here.<br><br>
Open recalls found: ______________________________________________<br><br>
Closed/completed: ______________________________________________<br><br>
Checked by: ____________  Date: ____________</div>
<p>Known campaigns for this model generation (verified against NHTSA primary records):</p>
<table><tr><th>Campaign</th><th>Component</th><th>What it means</th></tr>{''.join(rec_rows) or '<tr><td colspan=3>None verified at model level — VIN check above is authoritative.</td></tr>'}</table>
{unv_note}

<h2>3. What to inspect, in priority order</h2>
<table><tr><th>Item</th><th>Severity</th><th>Why it matters</th><th>Typical cost if found</th></tr>
{''.join(rows)}</table>

<h2>4. Negotiation talking points</h2>
<ul>{''.join(neg)}</ul>
<p>General rule: never negotiate on feelings — negotiate on the findings sheet. Documented faults
with repair estimates convert to dollars; vibes do not.</p>

<h2>5. Recommended next step</h2>
<p>Book the independent pre-purchase inspection (from $149 arranged through AutoVetting — reply to
your report email). If the seller resists an independent inspection, that is itself a finding.</p>

<footer>© {today[:4]} AutoVetting · Sources: NHTSA recall records (verified campaign numbers per
scripts/recall-ledger.json), model-generation failure patterns from the AutoVetting checklist
corpus. VIN data fields completed manually by the operator at fulfillment time.</footer>
</body></html>"""

    outdir = REPO / "_hub" / "Booking-Infrastructure" / "Reports"
    outdir.mkdir(parents=True, exist_ok=True)
    out = Path(a.out) if a.out else outdir / f"{a.key}-{(a.vin or 'sample').lower()}.html"
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out} ({len(doc.encode())} bytes; {len(rows)} items, {len(rec_rows)} verified recalls)")


if __name__ == "__main__":
    main()
