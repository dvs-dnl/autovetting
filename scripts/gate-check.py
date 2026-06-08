#!/usr/bin/env python3
"""
gate-check.py — pre-push regression gates for autovetting.

Codifies the actual regressions we've hit so they can never re-ship silently.
Run before any push:

    python3 ~/Documents/Claude/Projects/autovetting/scripts/gate-check.py

Exits 0 if all CRITICAL gates pass, 1 otherwise. WARN gates print but never block.

See AutoVet/Pre-Push-Gates.md for the human-readable rationale of each gate.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
os.chdir(REPO)

CRITICAL_FAIL = []
WARN = []
PASSED = []


def critical(name, ok, detail=""):
    if ok:
        PASSED.append(("CRIT", name))
    else:
        CRITICAL_FAIL.append((name, detail))


def warn(name, ok, detail=""):
    if ok:
        PASSED.append(("WARN", name))
    else:
        WARN.append((name, detail))


def all_html_pages():
    """Top-level + section index.html files (skip third-party, _hub, and meta-refresh redirect pages)."""
    out = []
    for p in REPO.rglob("index.html"):
        s = str(p.relative_to(REPO))
        if s.startswith(".git") or s.startswith("_hub/") or "node_modules" in s:
            continue
        # Skip pages that are just redirects (decode/ → /inspect/)
        head_snippet = p.read_text(encoding="utf-8", errors="replace")[:2000]
        if 'http-equiv="refresh"' in head_snippet:
            continue
        out.append(p)
    return sorted(out)


# ============================================================
# G1 (CRIT) — every inline <script> parses as valid JS
# Catches: apostrophe bugs in single-quoted strings, missing array commas
# ============================================================
def gate_inline_js_syntax():
    script_re = re.compile(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", re.IGNORECASE)
    bad = []
    for p in all_html_pages():
        html = p.read_text(encoding="utf-8", errors="replace")
        for i, m in enumerate(script_re.finditer(html), 1):
            tag_open = html[m.start():m.start() + 100]
            # Skip non-JS script types (application/ld+json, application/json, text/template, etc.)
            if 'type="application/' in tag_open or 'type="text/template' in tag_open:
                continue
            if "googletagmanager" in tag_open:
                continue
            body = m.group(1)
            if len(body.strip()) < 50:
                continue
            # Use node to syntax-check via `new Function(body)`
            r = subprocess.run(
                ["node", "-e", "new Function(require('fs').readFileSync('/dev/stdin','utf8'))"],
                input=body, capture_output=True, text=True, timeout=15,
            )
            if r.returncode != 0:
                bad.append(f"{p.relative_to(REPO)} script #{i}: {r.stderr.strip().splitlines()[0]}")
    critical("Inline JS syntax (apostrophes, commas)", not bad, "; ".join(bad[:5]))


# ============================================================
# G2 (CRIT) — every JSON-LD block is valid JSON
# Catches: malformed schema markup, trailing commas
# ============================================================
def gate_jsonld_valid():
    ld_re = re.compile(r"<script type=\"application/ld\+json\">([\s\S]*?)</script>", re.IGNORECASE)
    bad = []
    for p in all_html_pages():
        html = p.read_text(encoding="utf-8", errors="replace")
        for i, m in enumerate(ld_re.finditer(html), 1):
            try:
                json.loads(m.group(1))
            except Exception as e:
                bad.append(f"{p.relative_to(REPO)} ld#{i}: {e}")
    critical("JSON-LD blocks valid JSON", not bad, "; ".join(bad[:3]))


# ============================================================
# G3 (CRIT) — exactly one GA measurement ID across the whole site
# Catches: stray legacy GA IDs from copy-paste (the G-06S3EWDPXK incident)
# ============================================================
def gate_ga_id_uniform():
    ids = set()
    per_file = {}
    for p in all_html_pages():
        html = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"G-[A-Z0-9]{8,}", html):
            ids.add(m.group(0))
            per_file.setdefault(str(p.relative_to(REPO)), set()).add(m.group(0))
    if len(ids) <= 1:
        critical("GA tag consistency (single ID site-wide)", True)
    else:
        offenders = [f for f, s in per_file.items() if s != max(per_file.values(), key=len)]
        critical("GA tag consistency (single ID site-wide)", False,
                 f"found IDs {sorted(ids)}; outliers: {offenders[:5]}")


# ============================================================
# G14 (CRIT) — homepage + pinpoint IIFE evaluates without ReferenceError
# Catches: identifier referenced but never defined (the INSPECT_CATALOG incident)
# ============================================================
def gate_runtime_idents_resolve():
    bad = []
    for rel in ("index.html", "pinpoint/index.html", "homepage-test/index.html"):
        p = REPO / rel
        if not p.exists():
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        # Pull the largest inline <script> (skip ld+json/json), wrap in a stub DOM, eval
        script_re = re.compile(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", re.IGNORECASE)
        biggest = ""
        for m in script_re.finditer(h):
            tag = h[m.start():m.start() + 100]
            if 'type="application/' in tag or "googletagmanager" in tag:
                continue
            if len(m.group(1)) > len(biggest):
                biggest = m.group(1)
        if not biggest:
            continue
        # Eval with a minimal DOM stub. Any thrown ReferenceError → undefined identifier.
        stub = """
            var window={location:{href:'',search:'',pathname:'/'},matchMedia:()=>({matches:false}),
                addEventListener:()=>{},setTimeout:setTimeout,clearTimeout:clearTimeout,
                URLSearchParams:URLSearchParams,requestAnimationFrame:()=>{},getComputedStyle:()=>({})};
            var document={getElementById:()=>null,querySelector:()=>null,querySelectorAll:()=>[],
                createElement:()=>({appendChild:()=>{},setAttribute:()=>{},style:{},classList:{add:()=>{},remove:()=>{},toggle:()=>{}}}),
                addEventListener:()=>{},body:{addEventListener:()=>{}}};
            var localStorage={getItem:()=>null,setItem:()=>{},removeItem:()=>{}};
            var navigator={userAgent:''};
        """
        # Pass via stdin to avoid argv-too-long on large IIFEs
        r = subprocess.run(
            ["node", "-e", "require('vm').runInNewContext(require('fs').readFileSync('/dev/stdin','utf8'))"],
            input=stub + biggest, capture_output=True, text=True, timeout=15,
        )
        if r.returncode != 0:
            err = r.stderr.strip().splitlines()[0] if r.stderr else "(no stderr)"
            if "ReferenceError" in err or "is not defined" in err:
                bad.append(f"{rel}: {err}")
    critical("Homepage/pinpoint IIFE has no undefined identifiers", not bad, "; ".join(bad))




# ============================================================
# G4 (CRIT) — every CHECKLISTS slug is reachable via VEHICLE_MENU
# Catches: orphan checklists (the 80-orphan incident)
# ============================================================
def gate_no_orphan_checklists():
    inspect = (REPO / "inspect/index.html").read_text(encoding="utf-8", errors="replace")
    defined = set(re.findall(r"^  '([a-z0-9-]+)': \{", inspect, re.MULTILINE))
    # Extract VEHICLE_MENU body
    ms = inspect.find("const VEHICLE_MENU = {")
    if ms < 0:
        critical("CHECKLISTS reachability via VEHICLE_MENU", False, "VEHICLE_MENU not found")
        return
    o = inspect.find("{", ms)
    d, i, in_s, sc = 1, o + 1, False, ''
    while i < len(inspect) and d > 0:
        c = inspect[i]
        if in_s:
            if c == '\\':
                i += 2; continue
            if c == sc:
                in_s = False
        elif c in '"\'`':
            in_s = True; sc = c
        elif c == '{':
            d += 1
        elif c == '}':
            d -= 1
        i += 1
    body = inspect[o:i]
    wired = set(re.findall(r"\bkey:\s*['\"]([a-z0-9-]+)['\"]", body))
    orphans = defined - wired
    critical("No orphan CHECKLISTS (every key reachable)", not orphans,
             f"{len(orphans)} orphan(s): {sorted(orphans)[:5]}")


# ============================================================
# G5 (CRIT) — JSON-LD ItemList covers every Pinpoint VEHICLES entry
# Catches: structured-data drift after new catalog entries
# ============================================================
def gate_jsonld_covers_vehicles():
    pinpoint = (REPO / "pinpoint/index.html").read_text(encoding="utf-8", errors="replace")
    # Count VEHICLES entries
    ms = pinpoint.find("var VEHICLES = [")
    if ms < 0:
        warn("JSON-LD covers all VEHICLES entries", False, "VEHICLES array not found")
        return
    o = pinpoint.find("[", ms)
    d, i, in_s, sc = 1, o + 1, False, ''
    while i < len(pinpoint) and d > 0:
        c = pinpoint[i]
        if in_s:
            if c == '\\':
                i += 2; continue
            if c == sc:
                in_s = False
        elif c in '"\'`':
            in_s = True; sc = c
        elif c == '[':
            d += 1
        elif c == ']':
            d -= 1
        i += 1
    arr = pinpoint[o:i]
    # Count top-level objects
    d, in_s, sc, n = 0, False, '', 0
    for k in range(1, len(arr) - 1):
        c = arr[k]
        if in_s:
            if c == '\\': continue
            if c == sc: in_s = False
            continue
        if c in '"\'`':
            in_s = True; sc = c; continue
        if c == '{':
            if d == 0: n += 1
            d += 1
        elif c == '}':
            d -= 1
    vehicles_n = n
    # Highest JSON-LD position
    positions = [int(m.group(1)) for m in re.finditer(r'"position":(\d+)', pinpoint)]
    max_pos = max(positions) if positions else 0
    critical("JSON-LD covers all VEHICLES entries",
             max_pos >= vehicles_n,
             f"VEHICLES={vehicles_n}, ld max position={max_pos}")


# ============================================================
# G6 (CRIT) — brief module integrity on homepage + pinpoint
# Catches: regressions to the slot-wheel structure
# ============================================================
def gate_brief_module_intact():
    required_reels = ['"type"', '"budget"', '"priority"', '"answer"']
    bad = []
    for rel in ("index.html", "pinpoint/index.html"):
        p = REPO / rel
        if not p.exists():
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        if 'class="pp-brief-section"' not in h:
            bad.append(f"{rel}: no .pp-brief-section")
            continue
        for r in required_reels:
            if f'data-pp-reel={r}' not in h.replace("'", '"'):
                bad.append(f"{rel}: missing reel {r}")
        if "var FRAMES = [" not in h:
            bad.append(f"{rel}: no FRAMES array")
        if "setInterval(" not in h:
            bad.append(f"{rel}: no setInterval loop")
        # G6b: seamless loop logic — counter must not modulo
        if re.search(r"current\s*=\s*\(current\s*\+\s*1\)\s*%\s*FRAMES\.length", h):
            bad.append(f"{rel}: loop uses % FRAMES.length (visible reset)")
    critical("Brief module intact + seamless on homepage + pinpoint", not bad, "; ".join(bad))


# ============================================================
# G7 (CRIT) — banned: single-quoted JS strings with inner apostrophes
# Catches: Toyota's / Honda's bugs that breaks entire IIFE
# ============================================================
def gate_no_unsafe_apostrophes():
    bad = []
    for p in (REPO / "pinpoint/index.html", REPO / "inspect/index.html", REPO / "index.html"):
        if not p.exists(): continue
        h = p.read_text(encoding="utf-8", errors="replace")
        # Find lines like  field: 'word's other' (apostrophe inside single quotes, between letters)
        for line_no, line in enumerate(h.splitlines(), 1):
            if re.search(r"(?:tagline|summary|trim|name|model|make):\s*'[^']*[A-Za-z]'[A-Za-z]", line):
                bad.append(f"{p.relative_to(REPO)}:{line_no}: {line.strip()[:120]}")
                if len(bad) >= 5: break
        if len(bad) >= 5: break
    critical("No single-quoted JS strings with inner apostrophes", not bad, " | ".join(bad))


# ============================================================
# G8 (WARN) — logo + favicon path references resolve
# Catches: broken image links from path typos
# ============================================================
def gate_asset_paths_resolve():
    missing = []
    seen = set()
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r'(?:href|src)="(/assets/img/[^"]+)"', h):
            path = m.group(1)
            if path in seen: continue
            seen.add(path)
            target = REPO / path.lstrip("/")
            if not target.exists():
                missing.append(f"{p.relative_to(REPO)} → {path}")
    warn("Logo / favicon / image paths resolve", not missing, "; ".join(missing[:6]))


# ============================================================
# G9 (WARN) — exactly one <h1> per page
# Catches: drift toward duplicate page titles (SEO + a11y)
# ============================================================
def gate_single_h1():
    bad = []
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        n = len(re.findall(r"<h1\b", h, re.IGNORECASE))
        if n != 1:
            bad.append(f"{p.relative_to(REPO)}: {n}")
    warn("Single <h1> per page", not bad, "; ".join(bad))


# ============================================================
# G10 (WARN) — viewport meta + overflow-x safety net on body
# Catches: mobile bleed regressions
# ============================================================
def gate_viewport_overflow():
    bad = []
    for rel in ("index.html", "pinpoint/index.html", "homepage-test/index.html",
                "inspect/index.html", "decode/index.html", "search/index.html"):
        p = REPO / rel
        if not p.exists(): continue
        h = p.read_text(encoding="utf-8", errors="replace")
        if 'name="viewport"' not in h:
            bad.append(f"{rel}: missing viewport meta")
        # overflow-x: hidden may live in inline CSS or shared site.css; only flag the top three
        if rel in ("index.html", "pinpoint/index.html", "homepage-test/index.html"):
            if "overflow-x: hidden" not in h:
                bad.append(f"{rel}: missing inline overflow-x:hidden")
    warn("Viewport meta + mobile-bleed safety net", not bad, "; ".join(bad))


# ============================================================
# G11 (WARN) — homepage Step 01 form has no Body type field
# Catches: the field re-appearing if generator scripts re-add it
# ============================================================
def gate_no_step01_body_type():
    bad = []
    for rel in ("index.html", "homepage-test/index.html"):
        p = REPO / rel
        if not p.exists(): continue
        h = p.read_text(encoding="utf-8", errors="replace")
        if 'id="pp-type"' in h or 'for="pp-type"' in h:
            bad.append(f"{rel}: pp-type reference present")
    warn("No Body type field in Step 01 Pinpoint form", not bad, "; ".join(bad))


# ============================================================
# G12 (WARN) — INSPECT_CATALOG year coverage on homepage matches VEHICLE_MENU
# Catches: the 7-year vs 17-year stale-stub drift
# ============================================================
def gate_inspect_catalog_sync():
    bad = []
    inspect = (REPO / "inspect/index.html").read_text(encoding="utf-8", errors="replace")
    vm_years = set(int(y) for y in re.findall(r"^  (\d{4}):\s*\{", inspect, re.MULTILINE))
    for rel in ("index.html", "homepage-test/index.html"):
        p = REPO / rel
        if not p.exists(): continue
        h = p.read_text(encoding="utf-8", errors="replace")
        cat_years = set(int(y) for y in re.findall(r"^    (\d{4}):\s*\{", h, re.MULTILINE))
        missing = vm_years - cat_years
        if len(missing) > 2:  # tolerate a couple, flag drift
            bad.append(f"{rel}: missing {len(missing)} VEHICLE_MENU year(s) ({sorted(missing)[:5]})")
    warn("Homepage INSPECT_CATALOG mirrors VEHICLE_MENU year coverage", not bad, "; ".join(bad))


# ============================================================
# G13 (WARN) — vinNote coverage ratio (informational target ≥ 25%)
# ============================================================
def gate_vinnote_coverage():
    inspect = (REPO / "inspect/index.html").read_text(encoding="utf-8", errors="replace")
    slugs = re.findall(r"^  '([a-z0-9-]+)': \{", inspect, re.MULTILINE)
    has = len(re.findall(r"\bvinNote:", inspect))
    pct = has / len(slugs) * 100 if slugs else 0
    warn(f"vinNote coverage ≥ 25% (currently {has}/{len(slugs)} = {pct:.1f}%)", pct >= 25)


# ============================================================
# Run + report
# ============================================================
def main():
    gates = [
        gate_inline_js_syntax,
        gate_jsonld_valid,
        gate_ga_id_uniform,
        gate_runtime_idents_resolve,
        gate_no_orphan_checklists,
        gate_jsonld_covers_vehicles,
        gate_brief_module_intact,
        gate_no_unsafe_apostrophes,
        gate_asset_paths_resolve,
        gate_single_h1,
        gate_viewport_overflow,
        gate_no_step01_body_type,
        gate_inspect_catalog_sync,
        gate_vinnote_coverage,
    ]
    for g in gates:
        try:
            g()
        except Exception as e:
            critical(g.__name__, False, f"check itself errored: {e}")

    print("\n=== autovetting pre-push gates ===\n")
    for kind, name in PASSED:
        print(f"  [{kind} PASS]  {name}")
    for name, detail in WARN:
        print(f"  [WARN     ]  {name}")
        if detail:
            print(f"               → {detail}")
    for name, detail in CRITICAL_FAIL:
        print(f"  [CRIT FAIL]  {name}")
        if detail:
            print(f"               → {detail}")
    print(f"\nResult: {len(PASSED)} passed, {len(WARN)} warned, {len(CRITICAL_FAIL)} CRITICAL failed.\n")
    sys.exit(1 if CRITICAL_FAIL else 0)


if __name__ == "__main__":
    main()
