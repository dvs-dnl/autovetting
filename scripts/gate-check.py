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
# G15 (CRIT) — every standard page has the same set of <nav class="nav"> hrefs
# Catches: nav drift (inspect/ had only 3 links while about/, repair/, garage/ had 5)
# ============================================================
def gate_nav_consistency():
    # Pages intentionally outside the canonical nav (private preview, sub-tools)
    EXCLUDE = {"next/index.html", "homepage-test/index.html"}
    hrefs_by_page = {}
    for p in all_html_pages():
        rel = str(p.relative_to(REPO))
        if rel in EXCLUDE:
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r'<nav class="nav">([\s\S]+?)</nav>', h)
        if not m:
            continue
        # Collect every href inside the nav block
        hrefs = tuple(sorted(set(re.findall(r'href="([^"]+)"', m.group(1)))))
        hrefs_by_page[str(p.relative_to(REPO))] = hrefs
    if not hrefs_by_page:
        critical("Nav structure consistent across pages", True)
        return
    # Find the most common shape — every other page must match it
    from collections import Counter
    canonical = Counter(hrefs_by_page.values()).most_common(1)[0][0]
    outliers = [pg for pg, h in hrefs_by_page.items() if h != canonical]
    critical("Nav structure consistent across pages",
             not outliers,
             f"canonical={list(canonical)}; outliers={outliers[:5]}")


# ============================================================
# G16 (WARN) — sections that follow a contrasting-bg module need breathing room
# Catches: 'Find your next car' butting up against pp-brief above it
# ============================================================
def gate_section_breathing_room():
    bad = []
    # Right now we only check pinpoint's vehicle-search-section — extend as patterns repeat
    p = REPO / "pinpoint/index.html"
    if p.exists():
        h = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"\.vehicle-search-section\s*\{[^}]*?padding:\s*(\d+)px", h)
        if m and int(m.group(1)) < 96:
            bad.append(f"pinpoint/index.html: vehicle-search-section padding-top is {m.group(1)}px (need >=96 after pp-brief above it)")
    warn("Section breathing-room (vehicle-search padding >= 96px)", not bad, "; ".join(bad))




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
# G17 (CRIT) — every email address on the site is the canonical contact
# Catches: generator scripts reverting to a personal address, stale templates
# ============================================================
def gate_canonical_email():
    CANONICAL = "autovetting@gmail.com"
    # NHTSA / vendor emails that legitimately appear in quoted recall text, etc.
    # Add to this set only after confirming the address is necessarily external.
    ALLOW = {CANONICAL, "support@nhtsa.dot.gov"}
    email_re = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
    bad = []
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        for m in email_re.finditer(h):
            addr = m.group(0).lower()
            if addr in ALLOW:
                continue
            # Skip schema.org / data-source URLs that happen to match email pattern
            if "schema.org" in addr or addr.endswith(".png") or addr.endswith(".webp"):
                continue
            bad.append(f"{p.relative_to(REPO)}: {addr}")
            if len(bad) >= 6:
                break
        if len(bad) >= 6:
            break
    critical("Canonical contact email (only autovetting@gmail.com)", not bad,
             "; ".join(bad))




# ============================================================
# G18 (CRIT) — footer brand line consistent across all pages
# Catches: footer wordmark drift after the icon-led standardization
# ============================================================
def gate_footer_consistency():
    EXCLUDE = {"next/index.html", "homepage-test/index.html"}
    brand_re = re.compile(r'<p class="footer-brand">([\s\S]+?)</p>')
    sigs = {}
    for p in all_html_pages():
        rel = str(p.relative_to(REPO))
        if rel in EXCLUDE:
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        m = brand_re.search(h)
        if not m:
            sigs[rel] = "MISSING"
            continue
        # Normalize whitespace for the signature
        sigs[rel] = re.sub(r"\s+", " ", m.group(1)).strip()
    if not sigs:
        critical("Footer brand line consistent across pages", True)
        return
    from collections import Counter
    canonical = Counter(sigs.values()).most_common(1)[0][0]
    outliers = [pg for pg, s in sigs.items() if s != canonical]
    critical("Footer brand line consistent across pages",
             not outliers,
             f"outliers={outliers[:5]}")


# ============================================================
# G19 (CRIT) — favicon family files exist + every page references at least one
# Catches: partial-replacement regressions (new icon lands but old <link> sticks)
# ============================================================
def gate_favicon_family():
    REQUIRED = ["assets/img/favicon.png", "assets/img/favicon-32.png",
                "assets/img/favicon-180.png", "favicon.ico"]
    missing_files = [f for f in REQUIRED if not (REPO / f).exists()]
    no_link = []
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        if not re.search(r'<link[^>]+rel="(?:icon|shortcut icon|apple-touch-icon)"', h):
            no_link.append(str(p.relative_to(REPO)))
    bad = []
    if missing_files:
        bad.append(f"missing files: {missing_files}")
    if no_link:
        bad.append(f"pages with no favicon <link>: {no_link[:5]}")
    critical("Favicon family + per-page reference", not bad, "; ".join(bad))


# ============================================================
# G20 (CRIT) — every target="_blank" anchor must carry rel containing noopener
# Catches: tabnabbing security regressions from copy-pasted external links
# ============================================================
def gate_external_link_safety():
    bad = []
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r'<a\s[^>]*target="_blank"[^>]*>', h):
            tag = m.group(0)
            rel = re.search(r'rel="([^"]*)"', tag)
            if not rel or "noopener" not in rel.group(1):
                bad.append(f"{p.relative_to(REPO)}: {tag[:100]}")
                if len(bad) >= 5:
                    break
        if len(bad) >= 5:
            break
    critical("target=_blank carries rel=noopener", not bad, "; ".join(bad))




# ============================================================
# G21 (CRIT) — every <img> has an alt attribute
# Catches: accessibility/SEO regressions (silent for sighted users)
# ============================================================
def gate_img_alt_text():
    bad = []
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        # Match any <img ...> tag — capture full opening tag
        for m in re.finditer(r"<img\b[^>]*>", h):
            tag = m.group(0)
            if "alt=" not in tag:
                bad.append(f"{p.relative_to(REPO)}: {tag[:120]}")
                if len(bad) >= 5:
                    break
        if len(bad) >= 5:
            break
    critical("Every <img> has alt attribute", not bad, "; ".join(bad))


# ============================================================
# G22 (CRIT) — no console.log / console.warn / debugger in shipped JS
# Catches: forgotten debug instrumentation
# ============================================================
def gate_no_debug_cruft():
    bad = []
    script_re = re.compile(r"<script(?:\s[^>]*)?>([\s\S]*?)</script>", re.IGNORECASE)
    # console.warn/error are legitimate runtime reporting; only flag pure-debug families
    debug_re = re.compile(r"\b(console\.(?:log|debug|info|trace)|debugger\s*;|alert\s*\()")
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        for m in script_re.finditer(h):
            tag = h[m.start():m.start() + 100]
            if 'type="application/' in tag or "googletagmanager" in tag:
                continue
            body = m.group(1)
            for dm in debug_re.finditer(body):
                # Allow console.error since it's legitimate runtime reporting
                bad.append(f"{p.relative_to(REPO)}: {dm.group(0)}")
                if len(bad) >= 5:
                    break
            if len(bad) >= 5:
                break
        if len(bad) >= 5:
            break
    critical("No debug cruft (console.log / debugger / alert)", not bad, "; ".join(bad))


# ============================================================
# G23 (WARN) — content <img>s should have loading="lazy"
# Catches: perf regressions when adding new photos to cards/sections
# ============================================================
def gate_lazy_load_imgs():
    bad = []
    # Allow eager loading on logos + favicons + the first hero image of a page
    ALLOW_EAGER = ("logo-", "favicon", "/AutoVetting-Icon.png")
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        # Find every <img ...> tag, check src + loading attrs
        for m in re.finditer(r"<img\b[^>]*>", h):
            tag = m.group(0)
            src_m = re.search(r'src="([^"]+)"', tag)
            if not src_m:
                continue
            src = src_m.group(1)
            if any(s in src for s in ALLOW_EAGER):
                continue
            if 'loading="lazy"' not in tag:
                bad.append(f"{p.relative_to(REPO)}: {src}")
                if len(bad) >= 6:
                    break
        if len(bad) >= 6:
            break
    warn("Content imgs use loading=lazy", not bad, "; ".join(bad))


# ============================================================
# G24 (CRIT) — no personal handles (dvs.dnl, dvs-dnl, etc.) in shipped HTML
# Catches: stale personal identifiers same shape as G17 canonical email
# ============================================================
def gate_no_personal_handles():
    PATTERNS = [r"\bdvs\.dnl\b", r"\bdvs-dnl(?!/autovetting)\b",
                r"\bdanieldavis@", r"\b@dvsdnl\b"]
    bad = []
    for p in all_html_pages():
        h = p.read_text(encoding="utf-8", errors="replace")
        for pat in PATTERNS:
            m = re.search(pat, h)
            if m:
                bad.append(f"{p.relative_to(REPO)}: {m.group(0)}")
                if len(bad) >= 5:
                    break
        if len(bad) >= 5:
            break
    # GitHub repo URL (dvs-dnl/autovetting) is fine; pattern above already excludes it.
    critical("No personal handles (dvs.dnl, dvs-dnl, danieldavis@)", not bad, "; ".join(bad))




# ============================================================
# G25 (CRIT) — no per-page CSS overrides of shared chrome selectors
# Catches: chrome drift (pinpoint had nav-links gap:6px, inspect had gap:24px,
# while site.css had gap:8px — three different navs across the site)
# ============================================================
def gate_no_chrome_overrides():
    # Pages completely exempt from chrome consistency — private/test variants
    EXEMPT_PAGES = {"next/index.html"}
    # Per-(page, selector) extensions that augment the baseline without redefining it
    ALLOW = {
        ("pinpoint/index.html", ".site-header"),         # sticky/blur header
        ("homepage-test/index.html", ".site-header"),    # road-bg test variant
    }
    CHROME_SELECTORS = [".site-header", ".nav", ".nav-links", ".nav-links a",
                        ".brand-logo", ".brand"]
    bad = []
    for p in all_html_pages():
        rel = str(p.relative_to(REPO))
        if rel in EXEMPT_PAGES:
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r"<style[^>]*>([\s\S]+?)</style>", h):
            css = m.group(1)
            for sel in CHROME_SELECTORS:
                # Match the selector AT THE TOP-LEVEL ONLY (not nested in @media etc.)
                pat = re.compile(r"^\s*" + re.escape(sel) + r"\s*\{", re.MULTILINE)
                if not pat.search(css):
                    continue
                if (rel, sel) in ALLOW:
                    continue
                bad.append(f"{rel}: {sel}")
                break
            if bad and bad[-1].startswith(rel):
                break
    critical("No per-page chrome overrides (let site.css drive nav/header)",
             not bad, "; ".join(bad[:5]))




# ============================================================
# G26 (CRIT) — every standard page links to /assets/css/site.css
# Catches: silent layout regressions when a page forgets the shared stylesheet
# (pinpoint had been on its own inline copy; stripping it broke the entire nav)
# ============================================================
def gate_site_css_linked():
    EXEMPT_PAGES = {"next/index.html"}  # private preview, intentional standalone CSS
    bad = []
    for p in all_html_pages():
        rel = str(p.relative_to(REPO))
        if rel in EXEMPT_PAGES:
            continue
        h = p.read_text(encoding="utf-8", errors="replace")
        if 'href="/assets/css/site.css"' not in h:
            bad.append(rel)
    critical("Every page links to /assets/css/site.css",
             not bad, "; ".join(bad[:5]))




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
    """Only score multi-engine vehicles — vinNote is meaningless on single-engine cars.
    Threshold: 15% of multi-engine checklists carry vinNote."""
    inspect = (REPO / "inspect/index.html").read_text(encoding="utf-8", errors="replace")
    # Iterate each checklist block and check (engine field, vinNote presence)
    multi = 0
    with_vin = 0
    for m in re.finditer(r"^  '([a-z0-9-]+)': \{", inspect, re.MULTILINE):
        start = m.start()
        # Walk to matching close brace
        d = 0; j = inspect.index("{", start); inStr = False; sc = ""
        while j < len(inspect):
            c = inspect[j]
            if inStr:
                if c == "\\": j += 2; continue
                if c == sc: inStr = False
                j += 1; continue
            if c in '"\'`': inStr = True; sc = c; j += 1; continue
            if c == "{": d += 1
            elif c == "}":
                d -= 1
                if d == 0: break
            j += 1
        block = inspect[start:j+1]
        eng_m = re.search(r"engine:\s*['\"]([^'\"]+)['\"]", block)
        engine = eng_m.group(1) if eng_m else ""
        # True multi-engine signal: " or " connecting two engine displacements OR
        # multiple displacement tokens (e.g., "2.0L ... 2.5L ..."). Skip drivetrain-only "FWD or AWD".
        displ_tokens = re.findall(r"\b\d+\.\d+L\b", engine)
        drivetrain_only = bool(re.search(r"^[^/]+,\s*(FWD|AWD|RWD|4WD)\s+or\s+(FWD|AWD|RWD|4WD)$", engine))
        is_multi = len(set(displ_tokens)) >= 2 and not drivetrain_only
        # EV motor variants count as multi-engine too (e.g., "Dual Motor AWD / Single Motor RWD / Performance")
        if not is_multi and ("Electric" in engine or "Motor" in engine):
            is_multi = engine.count("/") >= 1 or engine.count(" or ") >= 1
        if is_multi:
            multi += 1
            if "vinNote:" in block:
                with_vin += 1
    pct = (with_vin / multi * 100) if multi else 0
    warn(f"vinNote coverage on multi-engine ≥ 15% (currently {with_vin}/{multi} = {pct:.1f}%)",
         pct >= 15)


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
        gate_nav_consistency,
        gate_no_unsafe_apostrophes,
        gate_canonical_email,
        gate_footer_consistency,
        gate_favicon_family,
        gate_external_link_safety,
        gate_img_alt_text,
        gate_no_debug_cruft,
        gate_no_personal_handles,
        gate_lazy_load_imgs,
        gate_no_chrome_overrides,
        gate_site_css_linked,
        gate_section_breathing_room,
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
