#!/usr/bin/env python3
"""
render-blog.py — renders _hub/Content/blog/*.md (status: published) to blog/<slug>/index.html,
builds blog/index.html, and updates sitemap.xml + llms.txt.

No external dependencies. Markdown support is scoped to the constructs the pillar posts
actually use (see _hub/Content/Blog-Post-Standard.md): #/##/### headings, bold/italic,
inline links, ul/ol lists, pipe tables, hr, raw-HTML passthrough (<sup>, <a>, comments).

Pipeline rules:
- Posts with `status: draft` are skipped.
- Internal /blog/<slug> links pointing at a non-published slug are rendered as plain
  text (no dangling links on deployed pages); links to published slugs are normalized
  to a trailing slash.
- External markdown links (http*) get target="_blank" rel="noopener noreferrer";
  raw <a> tags in Sources already carry these per the authoring standard.
- Emits Article + FAQPage JSON-LD per post (FAQ parsed from '## Frequently asked questions').

Run from anywhere: python3 scripts/render-blog.py
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC = REPO / "_hub" / "Content" / "blog"
OUT = REPO / "blog"
SITE = "https://autovetting.com"
TODAY = date.today().isoformat()
GA_ID = "G-YM12JSF5D1"

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def human_date(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{MONTHS[m - 1]} {d}, {y}"


# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text):
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return {}, text
    meta = {}
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        line = lines[i]
        if line and not line[0].isspace():
            m = re.match(r'^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$', line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val:
                    meta[key] = val.strip('"').strip("'")
        i += 1
    return meta, "\n".join(lines[i + 1:])


# ---------------------------------------------------------------- inline md
PUBLISHED_SLUGS = set()  # filled in main()


def _internal_link(m):
    text, href = m.group(1), m.group(2)
    bm = re.match(r'^/blog/([a-z0-9-]+)/?$', href.split("?")[0].split("#")[0])
    if bm:
        if bm.group(1) not in PUBLISHED_SLUGS:
            return text  # target not deployed: render as plain text
        href = f"/blog/{bm.group(1)}/"
    return f'<a href="{href}">{text}</a>'


def inline(s):
    s = re.sub(r'\[([^\]]+)\]\((/[^)\s]*)\)', _internal_link, s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)\s]+)\)',
               r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', s)
    s = re.sub(r'\*\*([^*]+(?:\*[^*]+)*)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', s)
    return s


# ---------------------------------------------------------------- block md
def md_to_html(body):
    lines = body.split("\n")
    out, para = [], []
    i = 0

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para).strip()) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush_para(); i += 1; continue
        if s.startswith("<!--"):
            flush_para(); out.append(s); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            flush_para()
            lvl = len(m.group(1))
            txt = inline(m.group(2).strip())
            if lvl == 1:
                i += 1; continue  # H1 is rendered from frontmatter title
            anchor = re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', m.group(2)).lower()).strip('-')
            out.append(f'<h{lvl} id="{anchor}">{txt}</h{lvl}>')
            i += 1; continue
        if re.match(r'^-{3,}$', s) or re.match(r'^\*{3,}$', s):
            flush_para(); out.append("<hr>"); i += 1; continue
        if s.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            if len(rows) >= 2 and all(re.match(r'^:?-+:?$', c) for c in rows[1]):
                head, body_rows = rows[0], rows[2:]
            else:
                head, body_rows = None, rows
            t = ["<table>"]
            if head:
                t.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
            t.append("<tbody>")
            for r in body_rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        if s.startswith("> "):
            flush_para()
            q = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                q.append(lines[i].strip().lstrip("> ").strip())
                i += 1
            out.append("<blockquote><p>" + inline(" ".join(q)) + "</p></blockquote>")
            continue
        if re.match(r'^[-*]\s+', s) or re.match(r'^\d+\.\s+', s):
            flush_para()
            ordered = bool(re.match(r'^\d+\.\s+', s))
            items = []
            while i < len(lines):
                ls = lines[i].strip()
                if re.match(r'^[-*]\s+', ls) and not ordered:
                    items.append(re.sub(r'^[-*]\s+', '', ls))
                elif re.match(r'^\d+\.\s+', ls) and ordered:
                    items.append(re.sub(r'^\d+\.\s+', '', ls))
                elif ls and lines[i][0].isspace() and items:
                    items[-1] += " " + ls  # wrapped continuation line
                else:
                    break
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it)}</li>" for it in items) + f"</{tag}>")
            continue
        para.append(s)
        i += 1
    flush_para()
    return "\n".join(out)


# ---------------------------------------------------------------- FAQ / text
def strip_text(s):
    s = re.sub(r'<sup>[^<]*</sup>', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = s.replace("**", "").replace("*", "")
    return re.sub(r'\s+', ' ', s).strip()


def extract_faq(body):
    m = re.search(r'^## Frequently asked questions\s*$(.*?)(?=^## |\Z)',
                  body, re.M | re.S)
    if not m:
        return []
    section = m.group(1)
    faqs = []
    for qm in re.finditer(r'^### (.+?)\s*$(.*?)(?=^### |\Z)', section, re.M | re.S):
        q = strip_text(qm.group(1))
        ans_lines = [l.strip() for l in qm.group(2).split("\n")
                     if l.strip() and not l.strip().startswith("<!--")]
        a = strip_text(" ".join(ans_lines))
        if q and a:
            faqs.append((q, a))
    return faqs


# ---------------------------------------------------------------- chrome
HEAD_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=__GA__"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '__GA__');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/img/favicon-180.png">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="__URL__">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
  <!-- Open Graph / Twitter -->
  <meta property="og:title" content="__TITLE__">
  <meta property="og:description" content="__DESC__">
  <meta property="og:url" content="__URL__">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="AutoVetting">
  <meta property="og:image" content="https://autovetting.com/assets/img/og-default.svg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@autovetting">
__JSONLD__<style>
  .blog-wrap { max-width: 760px; margin: 0 auto; padding: 44px 24px 90px; }
  .post-crumbs { font-size: 14px; color: var(--slate-500); margin-bottom: 20px; }
  .post-crumbs a { color: var(--electric); text-decoration: none; }
  .post-crumbs a:hover { text-decoration: underline; }
  .post h1 { font-size: 34px; font-weight: 800; letter-spacing: -0.025em; color: var(--navy); line-height: 1.2; margin-bottom: 12px; }
  .post-meta { font-size: 14px; color: var(--slate-500); margin-bottom: 30px; padding-bottom: 18px; border-bottom: 1px solid var(--slate-200); }
  .post h2 { font-size: 24px; font-weight: 700; color: var(--navy); margin: 38px 0 14px; padding-bottom: 8px; border-bottom: 2px solid var(--electric); display: inline-block; }
  .post h2:first-of-type { margin-top: 8px; }
  .post h3 { font-size: 19px; font-weight: 700; color: var(--navy); margin: 28px 0 10px; }
  .post h4 { font-size: 16.5px; font-weight: 700; color: var(--navy); margin: 22px 0 8px; }
  .post p { font-size: 16.5px; line-height: 1.75; color: #1E293B; margin: 0 0 16px; }
  .post ul, .post ol { margin: 0 0 18px; padding-left: 26px; }
  .post li { font-size: 16.5px; line-height: 1.7; color: #1E293B; margin-bottom: 8px; }
  .post a { color: var(--electric); }
  .post sup { font-size: 11px; color: var(--slate-500); }
  .post hr { border: none; border-top: 1px solid var(--slate-200); margin: 34px 0; }
  .post table { width: 100%; border-collapse: collapse; margin: 0 0 20px; font-size: 15px; }
  .post th { background: var(--slate-100); text-align: left; padding: 9px 11px; border: 1px solid var(--slate-200); color: var(--navy); }
  .post td { padding: 9px 11px; border: 1px solid var(--slate-200); vertical-align: top; line-height: 1.55; }
  .post blockquote { border-left: 3px solid var(--electric); padding-left: 16px; margin: 0 0 16px; }
  .post blockquote p { color: var(--slate-500); }
  .blog-hero { padding: 52px 24px 44px; background: linear-gradient(135deg, var(--navy) 0%, var(--navy-2) 100%); color: var(--white); text-align: center; }
  .blog-hero h1 { font-size: 38px; font-weight: 800; letter-spacing: -0.025em; margin-bottom: 12px; }
  .blog-hero p { font-size: 18px; color: var(--slate-300); max-width: 600px; margin: 0 auto; }
  .blog-card { display: block; padding: 20px 22px; border: 1px solid var(--slate-200); border-radius: var(--radius-lg); margin-bottom: 14px; text-decoration: none; background: var(--white); box-shadow: var(--shadow-sm); transition: box-shadow .15s, border-color .15s; }
  .blog-card:hover { box-shadow: var(--shadow-md); border-color: var(--electric); }
  .blog-card .bc-date { font-size: 13px; font-weight: 600; color: var(--slate-500); text-transform: uppercase; letter-spacing: .04em; }
  .blog-card h2 { font-size: 20px; font-weight: 700; color: var(--navy); margin: 5px 0 6px; line-height: 1.3; }
  .blog-card p { font-size: 15px; color: var(--slate-500); line-height: 1.6; margin: 0; }
  .blog-card .bc-more { display: inline-block; margin-top: 10px; font-size: 14px; font-weight: 600; color: var(--electric); }
  .post-cta { margin: 42px 0 8px; padding: 22px 24px; border: 1px solid rgba(124,108,255,.35); border-radius: 14px; background: rgba(124,108,255,.07); }
  .post-cta h2 { margin: 0 0 8px; font-size: 20px; }
  .post-cta p { margin: 0 0 14px; }
  .post-cta-btn { display: inline-block; padding: 11px 18px; border-radius: 9px; background: var(--accent, #7c6cff); color: #fff !important; font-weight: 600; text-decoration: none; }
</style>
</head>
<body>

<header class="site-header">
  <nav class="nav">
    <a href="/" class="brand"><img src="/assets/img/logo-dark.png" class="brand-logo" height="40" alt="AutoVetting"></a>
    <div class="nav-links">
      <a href="/pinpoint/" class="nav-step"><span class="nav-step-num">1</span> Pinpoint</a>
      <a href="/search/" class="nav-step"><span class="nav-step-num">2</span> Search</a>
      <a href="/inspect/" class="nav-step"><span class="nav-step-num">3</span> Inspect</a>
      <span class="nav-divider" aria-hidden="true"></span>
      <a href="/repair/">Guides</a>
      <a href="/maintenance/">Maintenance</a>
      <a href="/garage/">My Garage</a>
      <a href="/about/">About</a>
    </div>
  </nav>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <p class="footer-brand">
    <img class="footer-icon" src="/assets/img/favicon-180.png" alt="" width="28" height="28">
    <span class="footer-wordmark">Auto<span class="vet-color">Vetting</span><sup>&trade;</sup></span>
    <span class="footer-tag">&mdash; Know before you buy.</span>
  </p>
  <p style="margin-top:8px">
    <a href="/">Home</a> &middot;
    <a href="/blog/">Blog</a> &middot;
    <a href="/repair/">Repair Guides</a> &middot;
    <a href="/garage/">My Garage</a> &middot;
    <a href="/inspect/">Inspect</a>
  </p>
</footer>

</body>
</html>
"""


def jsonld_block(obj):
    return ('<script type="application/ld+json">\n'
            + json.dumps(obj, indent=1, ensure_ascii=False)
            + "\n</script>\n")


def render_head(title, desc, url, jsonld_objs):
    h = HEAD_TMPL.replace("__GA__", GA_ID)
    h = h.replace("__TITLE__", html.escape(title, quote=True))
    h = h.replace("__DESC__", html.escape(desc, quote=True))
    h = h.replace("__URL__", url)
    h = h.replace("__JSONLD__", "".join(jsonld_block(o) for o in jsonld_objs))
    return h


def trim_dek(desc, limit=170):
    if len(desc) <= limit:
        return desc
    cut = desc[:limit].rsplit(" ", 1)[0].rstrip(",;: ")
    return cut + "…"


# ---------------------------------------------------------------- main
def cta_block(p):
    from urllib.parse import quote
    subj = quote(f"Inspection request: {p['title']}")
    body = quote("Hi AutoVetting,\n\nI would like this car professionally vetted:\n\n"
                 f"Vehicle: {p['title']}\nVIN: \nListing link: \nZIP code: \nPhone: \nTimeline: \n\n"
                 "Please send me next steps.")
    onclick = ("if(typeof gtag==='function')gtag('event','inspection_cta_click',"
               "{vehicle:'" + p["slug"] + "',page:'blog'})")
    return (
        '    <div class="post-cta">\n'
        '      <h2>Want this exact car professionally vetted?</h2>\n'
        '      <p>Send us the listing &mdash; we arrange an independent pre-purchase inspection '
        'and walk you through the findings. From $149, nothing due until we confirm a mechanic '
        'and a time. Piloting in Phoenix; other US metros by arrangement.</p>\n'
        f'      <a class="post-cta-btn" href="mailto:autovetting@gmail.com?subject={subj}&amp;body={body}" '
        f'onclick="{onclick}">Request an inspection</a>\n'
        '    </div>'
    )


def main():
    posts = []
    skipped = []
    for f in sorted(SRC.glob("*.md")):
        meta, body = parse_frontmatter(f.read_text(encoding="utf-8"))
        if meta.get("status") != "published":
            skipped.append((f.name, meta.get("status", "?")))
            continue
        slug = meta.get("slug") or re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f.stem)
        posts.append({
            "file": f.name, "slug": slug,
            "title": meta.get("title", slug),
            "date": meta.get("date", TODAY),
            "modified": meta.get("modified", meta.get("date", TODAY)),
            "desc": meta.get("description", ""),
            "body": body,
        })

    PUBLISHED_SLUGS.clear()
    PUBLISHED_SLUGS.update(p["slug"] for p in posts)

    # ---- per-post pages
    for p in posts:
        url = f"{SITE}/blog/{p['slug']}/"
        article_ld = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": p["title"],
            "description": p["desc"],
            "datePublished": p["date"],
            "dateModified": p["modified"],
            "author": {"@type": "Organization", "name": "AutoVetting Editorial",
                       "url": SITE + "/"},
            "publisher": {"@type": "Organization", "name": "AutoVetting",
                          "url": SITE,
                          "logo": {"@type": "ImageObject",
                                   "url": SITE + "/assets/img/logo-dark.png"}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
            "image": SITE + "/assets/img/logo-dark.png",
        }
        lds = [article_ld]
        faqs = extract_faq(p["body"])
        if faqs:
            lds.append({
                "@context": "https://schema.org",
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in faqs
                ],
            })
        body_html = md_to_html(p["body"])
        meta_line = (f'By AutoVetting Editorial &middot; Published {human_date(p["date"])}'
                     + (f' &middot; Updated {human_date(p["modified"])}'
                        if p["modified"] != p["date"] else ""))
        page = (render_head(f'{p["title"]} — AutoVetting', p["desc"], url, lds)
                + '\n<main class="blog-wrap">\n'
                + '  <nav class="post-crumbs"><a href="/blog/">Blog</a> &middot; '
                + 'Used-Car Buyer&rsquo;s Guides</nav>\n'
                + '  <article class="post">\n'
                + f'    <h1>{inline(p["title"])}</h1>\n'
                + f'    <p class="post-meta">{meta_line}</p>\n'
                + body_html + "\n"
                + cta_block(p) + "\n"
                + "  </article>\n</main>\n"
                + FOOTER)
        outdir = OUT / p["slug"]
        outdir.mkdir(parents=True, exist_ok=True)
        (outdir / "index.html").write_text(page, encoding="utf-8")

    # ---- listing page (newest first)
    posts_sorted = sorted(posts, key=lambda p: (p["date"], p["slug"]), reverse=True)
    items_ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "AutoVetting Blog — Used-Car Buyer's Guides",
        "url": SITE + "/blog/",
        "description": "Honest, source-backed buyer's guides for specific used vehicles: known issues, recalls to verify by VIN, what to pay, and what to inspect before purchase.",
        "mainEntity": {
            "@type": "ItemList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1,
                 "url": f"{SITE}/blog/{p['slug']}/", "name": p["title"]}
                for i, p in enumerate(posts_sorted)
            ],
        },
    }
    cards = []
    for p in posts_sorted:
        cards.append(
            f'    <a class="blog-card" href="/blog/{p["slug"]}/">\n'
            f'      <span class="bc-date">{human_date(p["date"])}</span>\n'
            f'      <h2>{html.escape(p["title"])}</h2>\n'
            f'      <p>{html.escape(trim_dek(p["desc"]))}</p>\n'
            f'      <span class="bc-more">Read the guide &rarr;</span>\n'
            f'    </a>'
        )
    index_desc = ("Honest, source-backed used-car buyer's guides: known issues, "
                  "recalls to verify by VIN, what to pay, and what to inspect "
                  "before purchase.")
    index_page = (render_head("Blog — AutoVetting Used-Car Buyer's Guides",
                              index_desc, SITE + "/blog/", [items_ld])
                  + '\n<section class="blog-hero">\n'
                  + "  <h1>The AutoVetting Blog</h1>\n"
                  + "  <p>Honest, source-backed buyer&rsquo;s guides for specific used "
                  + "vehicles &mdash; known issues, recalls to verify by VIN, what to "
                  + "pay, and what to inspect before purchase.</p>\n"
                  + "</section>\n\n"
                  + '<main class="blog-wrap" style="padding-top:36px">\n'
                  + "\n".join(cards)
                  + "\n</main>\n" + FOOTER)
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(index_page, encoding="utf-8")

    # ---- sitemap.xml
    sm_path = REPO / "sitemap.xml"
    sm = [l for l in sm_path.read_text(encoding="utf-8").split("\n")
          if "autovetting.com/blog" not in l]
    blog_lines = [f"  <url><loc>{SITE}/blog/</loc><lastmod>{TODAY}</lastmod>"
                  f"<changefreq>weekly</changefreq><priority>0.8</priority></url>"]
    for p in posts_sorted:
        blog_lines.append(
            f"  <url><loc>{SITE}/blog/{p['slug']}/</loc><lastmod>{TODAY}</lastmod>"
            f"<changefreq>monthly</changefreq><priority>0.7</priority></url>")
    close = sm.index("</urlset>")
    sm = sm[:close] + blog_lines + sm[close:]
    sm_path.write_text("\n".join(sm), encoding="utf-8")

    # ---- llms.txt
    llms_path = REPO / "llms.txt"
    llms = llms_path.read_text(encoding="utf-8")
    llms = re.sub(r'## Blog\n.*?(?=\n## )', '', llms, flags=re.S)  # idempotent
    blog_sec = ["## Blog", "",
                ("Source-backed buyer's guides for specific used vehicles. Each guide "
                 "covers known issues, NHTSA recalls to verify by VIN, best and worst "
                 "configurations, market pricing, and inspection priorities."), ""]
    blog_sec += [f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {trim_dek(p['desc'], 200)}"
                 for p in posts_sorted]
    blog_sec.append("")
    marker = "## Data Sources"
    if marker in llms:
        llms = llms.replace(marker, "\n".join(blog_sec) + "\n" + marker, 1)
    else:
        llms = llms.rstrip() + "\n\n" + "\n".join(blog_sec)
    llms_path.write_text(llms, encoding="utf-8")

    print(f"Rendered {len(posts)} posts:")
    for p in posts_sorted:
        print(f"  {p['date']}  /blog/{p['slug']}/")
    print(f"Skipped (not published): {skipped}")
    print("Updated: blog/index.html, sitemap.xml, llms.txt")


if __name__ == "__main__":
    main()
