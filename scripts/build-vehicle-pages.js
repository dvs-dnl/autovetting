#!/usr/bin/env node
/*
 * build-vehicle-pages.js — one indexable page per inspection checklist.
 *
 * Why: every vehicle checklist used to live only at /inspect/?year=…&make=…&model=…,
 * and all of those URLs share inspect/index.html's canonical (/inspect/). Google folded
 * them into /inspect/ ("Alternate page with proper canonical tag"), so no vehicle
 * checklist could be indexed on its own.
 *
 * What it does (all derived from CHECKLISTS + VEHICLE_MENU in inspect/index.html):
 *   1. writes inspect/<key>/index.html for every CHECKLISTS key (self-canonical,
 *      vehicle title + description, checklist rendered into the HTML)
 *   2. writes inspect/checklist.css (the inspect page's own <style>, shared by all pages)
 *   3. lists every vehicle page in sitemap.xml (right after the /inspect/ line)
 *   4. rewrites internal links /inspect/?year=Y&make=M&model=X (and ?vehicle=) to
 *      /inspect/<key>/ wherever a checklist exists — in deployable HTML and in the
 *      blog markdown sources (_hub/Content/blog/*.md) so render-blog.py keeps them
 *   5. turns pages for keys that no longer exist into noindex redirects to /inspect/
 *
 * Usage:
 *   node scripts/build-vehicle-pages.js          # write
 *   node scripts/build-vehicle-pages.js --check  # exit 1 if anything is out of date
 *
 * The pre-push gate (scripts/gate-check.py) runs --check. Never hand-edit the
 * generated pages: edit the checklist in inspect/index.html and re-run this script.
 */
'use strict';
const fs = require('fs');
const path = require('path');

const REPO = path.resolve(__dirname, '..');
const SITE = 'https://autovetting.com';
const CHECK = process.argv.includes('--check');
const MARK = '<!-- generated: scripts/build-vehicle-pages.js — do not edit; edit inspect/index.html and re-run -->';
const RETIRED = '<!-- retired: scripts/build-vehicle-pages.js -->';
const today = (() => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; })();

const rd = p => fs.readFileSync(path.join(REPO, p), 'utf8');
const exists = p => fs.existsSync(path.join(REPO, p));
const problems = [];
const changed = [];
function put(rel, content) {
  const cur = exists(rel) ? rd(rel) : null;
  if (cur === content) return false;
  if (CHECK) { problems.push(`out of date: ${rel}`); return true; }
  fs.mkdirSync(path.dirname(path.join(REPO, rel)), { recursive: true });
  fs.writeFileSync(path.join(REPO, rel), content);
  changed.push(rel);
  return true;
}

// ---------- 1. load data ----------
const src = rd('inspect/index.html');
const L = src.split('\n');
const a = L.findIndex(l => /^const CHECKLISTS = \{/.test(l));
const v = L.findIndex(l => /^const VEHICLE_MENU = \{/.test(l));
if (a < 0 || v < 0) { console.error('CHECKLISTS / VEHICLE_MENU not found in inspect/index.html'); process.exit(2); }
let b = v; while (b < L.length && !/^\};/.test(L[b])) b++;
const { CHECKLISTS: CH, VEHICLE_MENU: VM } = new Function(L.slice(a, b + 1).join('\n') + '\nreturn {CHECKLISTS, VEHICLE_MENU};')();
const KEYS = Object.keys(CH).sort();

// years the menu routes to each checklist (used to resolve ?vehicle= links)
const years = {};
for (const y of Object.keys(VM)) for (const mk of Object.keys(VM[y])) for (const e of VM[y][mk] || [])
  if (e && e.key && CH[e.key]) (years[e.key] = years[e.key] || new Set()).add(+y);

// same routing as findChecklistByYMMT() in inspect/index.html, returning the key
function findKey(year, make, model) {
  const mk = (make || '').toLowerCase(), md = (model || '').toLowerCase();
  const ym = VM[String(year)];
  if (ym) {
    const mkKey = Object.keys(ym).find(k => k.toLowerCase() === mk);
    if (mkKey) {
      const e = (ym[mkKey] || []).find(e => (e.model || '').toLowerCase() === md);
      if (e && e.key && CH[e.key]) return e.key;
    }
  }
  for (const k of KEYS) {
    const c = CH[k];
    if (c.year === Number(year) && (c.make || '').toLowerCase() === mk && (c.model || '').toLowerCase() === md) return k;
  }
  return null;
}

// ---------- 2. page shell, taken from inspect/index.html so it never drifts ----------
const cut = (s, from, to, incl) => { const i = s.indexOf(from); const j = s.indexOf(to, i); if (i < 0 || j < 0) throw new Error(`template anchor missing: ${from}`); return s.slice(i, incl ? j + to.length : j); };
const headTop = src.slice(0, src.indexOf('<title>'));
const canonEnd = src.indexOf('>', src.indexOf('<link rel="canonical"')) + 1;
const headMid = src.slice(canonEnd, src.indexOf('<style>')).replace(/^\s*\n/, '\n');
const css = cut(src, '<style>', '</style>').slice('<style>'.length).replace(/^\n/, '');
const header = cut(src, '<header class="site-header">', '</header>', true);
const footer = cut(src, '<footer class="site-footer">', '</footer>', true);
const repairBlock = cut(src, '<div class="checklist-section-block">\n      <div class="checklist-section-header">\n        <div class="checklist-section-title">After you buy', '<div class="value-framing-card"').trimEnd();

const esc = s => String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const text = s => String(s == null ? '' : s).replace(/<[^>]*>/g, '').replace(/&nbsp;/g, ' ').replace(/&[a-z]+;/g, m => ({ '&amp;': '&', '&mdash;': '—', '&ndash;': '–', '&rsquo;': '’', '&lsquo;': '‘', '&ldquo;': '“', '&rdquo;': '”', '&rarr;': '→' }[m] || ' ')).replace(/\s+/g, ' ').trim();
const clip = (s, n) => s.length <= n ? s : s.slice(0, s.lastIndexOf(' ', n - 1)).replace(/[,;:—–-]+$/, '') + '…';
const url = k => `/inspect/${k}/`;

function page(k) {
  const c = CH[k];
  const name = `${c.year} ${c.make} ${c.model}`;
  const title = `${name} Pre-Purchase Inspection Checklist — AutoVetting`;
  const desc = clip(text(c.summary), 155);
  const canon = SITE + url(k);
  const veh = `${c.year} ${c.make} ${c.model}`;
  const subj = encodeURIComponent(`Inspection request: ${veh}`);
  const body = encodeURIComponent(`Hi AutoVetting,\n\nI would like this car professionally vetted:\n\nVehicle: ${veh}\nVIN: not yet known\nListing link: \nZIP code: \nPhone: \nTimeline: \n\nPlease send me next steps.`);
  const rsubj = encodeURIComponent(`Vetting Report request: ${veh}`);
  const rbody = encodeURIComponent(`Hi AutoVetting,\n\nPlease prepare the Vetting Report for:\n\nVehicle: ${veh}\nVIN: \nListing link: \n\nPlease reply with next steps.`);
  const ga = ev => `if(typeof gtag==='function')gtag('event','${ev}',{vehicle:'${esc(veh).replace(/'/g, '')}',page:'inspect_vehicle'})`;
  const crumbs = { '@context': 'https://schema.org', '@type': 'BreadcrumbList', itemListElement: [
    { '@type': 'ListItem', position: 1, name: 'Home', item: SITE + '/' },
    { '@type': 'ListItem', position: 2, name: 'Inspect', item: SITE + '/inspect/' },
    { '@type': 'ListItem', position: 3, name, item: canon }] };
  const siblings = KEYS.filter(x => x !== k && CH[x].make === c.make).sort((x, y) => CH[x].year - CH[y].year || CH[x].model.localeCompare(CH[y].model));
  const blog = c.blogUrl ? c.blogUrl.replace(/\/?$/, '/') : '';
  const recalls = (c.recalls || []).filter(r => r && (r.number || r.title));

  return `${headTop}<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}">
<link rel="canonical" href="${canon}">
${headMid.trim()}

<link rel="stylesheet" href="/inspect/checklist.css">
<script type="application/ld+json">${JSON.stringify(crumbs)}</script>
<meta property="og:title" content="${esc(title)}">
<meta property="og:description" content="${esc(desc)}">
<meta property="og:url" content="${canon}">
<meta property="og:type" content="article">
<meta property="og:image" content="${SITE}/assets/img/og-default.png">
<meta property="og:site_name" content="AutoVetting">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${esc(title)}">
<meta name="twitter:description" content="${esc(desc)}">
<meta name="twitter:image" content="${SITE}/assets/img/og-default.png">
${MARK}
</head>
<body>

${header}

<section class="hero">
  <div class="hero-inner">
    <p class="eyebrow">Pre-Purchase Inspection Checklist</p>
    <h1 class="hero-title">${esc(name)} pre-purchase inspection checklist</h1>
    <p class="hero-sub">What to check before you buy, built from NHTSA recall data, owner-reported failures, and mechanic intel. Print it or bring it to your mechanic.</p>
  </div>
</section>

<section class="checklist-section" id="checklist-section">
  <div id="checklist-content">
    <div class="checklist-actions">
      <div class="actions-label">Pre-purchase inspection · ${esc(name)}</div>
      <div class="actions-buttons">
        <a class="checklist-action-btn" href="/inspect/">Check another vehicle</a>
        <button class="checklist-action-btn primary" type="button" onclick="window.print()">Print / PDF</button>
      </div>
    </div>
    <div class="checklist-meta-card">
      <div class="checklist-meta-header">
        <div>
          <div class="checklist-vehicle-title">${esc(name)}</div>
          <div class="checklist-vin">${c.trim || ''}</div>
        </div>
        <div class="risk-badge risk-${esc(c.overallRisk)}">
          <span class="dot"></span> ${c.overallRiskLabel || ''}
        </div>
      </div>
      <p class="checklist-summary">${c.summary || ''}</p>
      <div class="checklist-stats">
        <div class="stat"><div class="stat-label">Items to check</div><div class="stat-value">${c.stats.itemsToCheck}</div></div>
        <div class="stat"><div class="stat-label">Open recalls</div><div class="stat-value">${c.stats.recalls}</div></div>
        <div class="stat"><div class="stat-label">NHTSA complaints</div><div class="stat-value">${c.stats.ownerComplaints}</div></div>
        <div class="stat"><div class="stat-label">Top concern</div><div class="stat-value" style="font-size:14px; line-height:1.3">${c.stats.topComplaintArea}</div></div>
      </div>
    </div>
${c.sections.map(s => `    <div class="checklist-section-block">
      <div class="checklist-section-header"><h2 class="checklist-section-title">${s.title}</h2></div>
      <div class="checklist-items">
${(s.items || []).map(it => `        <div class="checklist-item">
          <div class="item-risk-marker item-risk-${esc(it.risk)}"></div>
          <div class="item-content">
            <div class="item-header">
              <div class="item-title-link"><h3 class="item-title">${it.title}</h3></div>
              <div class="item-risk-label ${esc(it.risk)}">${it.riskLabel || ''}</div>
            </div>
            <div class="item-desc">${it.desc || ''}</div>
            <div class="item-check">${it.check || ''}</div>
            <div class="item-meta">
              <span><strong>Est. cost:</strong> ${it.cost || ''}</span>
              <span><strong>Source:</strong> ${it.source || ''}</span>
            </div>
          </div>
        </div>`).join('\n')}
      </div>
    </div>`).join('\n')}
${recalls.length ? `    <div class="checklist-section-block">
      <div class="checklist-section-header"><h2 class="checklist-section-title">NHTSA Recalls (verify completion via VIN)</h2></div>
      <div class="recalls-list">
${recalls.map(r => `        <div class="recall-item">
          <div class="recall-number">${r.number || ''}</div>
          <div class="recall-title">${r.title || ''}</div>
          <div class="recall-desc">${r.desc || ''}</div>
        </div>`).join('\n')}
      </div>
    </div>` : ''}
${c.vinNote ? `    <div class="checklist-section-block">
      <div class="checklist-section-header"><h2 class="checklist-section-title">What the VIN tells you</h2></div>
      <div class="item-check" style="padding:16px">${c.vinNote}</div>
    </div>` : ''}
${blog ? `    <div class="checklist-section-block">
      <div class="checklist-section-header"><h2 class="checklist-section-title">Buyer&rsquo;s guide</h2></div>
      <div class="item-check" style="padding:16px">Known issues, pricing, and best configurations: <a href="${blog}">read the ${esc(c.year + ' ' + c.make + ' ' + c.model)} buyer&rsquo;s guide &rarr;</a></div>
    </div>` : ''}
    ${repairBlock.trim()}
${siblings.length ? `    <div class="checklist-section-block">
      <div class="checklist-section-header"><h2 class="checklist-section-title">More ${esc(c.make)} checklists</h2></div>
      <div class="item-check" style="padding:16px">
${siblings.map(x => `        <a href="${url(x)}">${esc(CH[x].year + ' ' + CH[x].model)}</a>`).join(' &middot;\n')}
      </div>
    </div>` : ''}
    <div class="checklist-meta-card" id="vetting-cta" style="margin-top:16px;">
      <div class="checklist-meta-header">
        <div>
          <div class="checklist-vehicle-title">Want this exact car professionally vetted?</div>
          <div class="checklist-vin">Independent pre-purchase inspection &mdash; we arrange it and walk you through the findings.</div>
        </div>
      </div>
      <p class="checklist-summary">Send us the listing and we reply within 1 business day. Nothing due until we confirm a mechanic and a time. Piloting in Phoenix; other US metros by arrangement.</p>
      <div class="actions-buttons">
        <a class="checklist-action-btn primary" href="mailto:autovetting@gmail.com?subject=${subj}&amp;body=${body}" onclick="${ga('inspection_cta_click')}">Get an inspection quote</a>
        <a class="checklist-action-btn" href="mailto:autovetting@gmail.com?subject=${rsubj}&amp;body=${rbody}" onclick="${ga('report_cta_click')}">Get the full Vetting Report</a>
      </div>
      <div class="checklist-vin" style="margin-top:10px;">The Vetting Report: this VIN&rsquo;s full recall status, known-failure cost ranges, negotiation talking points, and inspection priorities &mdash; delivered within 24 hours.</div>
    </div>
  </div>
</section>

${footer}
</body>
</html>
`;
}

// ---------- 3. write pages + shared css ----------
put('inspect/checklist.css', `/* ${MARK.slice(5, -4)} */\n${css}`);
let pagesChanged = 0;
const pageChanged = {};
for (const k of KEYS) { pageChanged[k] = put(`inspect/${k}/index.html`, page(k)); if (pageChanged[k]) pagesChanged++; }

// retire pages whose key is gone (unlink is blocked on the Cowork mount, so overwrite)
const stub = `<!DOCTYPE html>\n<html lang="en"><head><meta charset="UTF-8">${RETIRED}\n<meta name="robots" content="noindex">\n<link rel="canonical" href="${SITE}/inspect/">\n<meta http-equiv="refresh" content="0; url=/inspect/">\n<title>Inspection checklists — AutoVetting</title></head>\n<body><a href="/inspect/">Inspection checklists</a></body></html>\n`;
const retired = [];
for (const d of fs.readdirSync(path.join(REPO, 'inspect'), { withFileTypes: true })) {
  if (!d.isDirectory() || CH[d.name]) continue;
  const rel = `inspect/${d.name}/index.html`;
  if (!exists(rel)) continue;
  const cur = rd(rel);
  if (cur.includes(MARK)) { put(rel, stub); retired.push(d.name); }
}

// ---------- 4. sitemap ----------
const smOld = rd('sitemap.xml');
const vehLine = /^\s*<url><loc>https:\/\/autovetting\.com\/inspect\/[a-z0-9-]+\/<\/loc>.*$/;
const oldMod = {};
for (const l of smOld.split('\n')) { const m = l.match(/\/inspect\/([a-z0-9-]+)\/<\/loc><lastmod>([\d-]+)</); if (m) oldMod[m[1]] = m[2]; }
const smLines = smOld.split('\n').filter(l => !vehLine.test(l));
const at = smLines.findIndex(l => l.includes('<loc>https://autovetting.com/inspect/</loc>'));
const ins = KEYS.map(k => `  <url><loc>${SITE}${url(k)}</loc><lastmod>${pageChanged[k] || !oldMod[k] ? today : oldMod[k]}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>`);
smLines.splice(at < 0 ? smLines.indexOf('</urlset>') : at + 1, 0, ...ins);
if (CHECK) {
  const have = Object.keys(oldMod).sort().join(','), want = KEYS.join(',');
  if (have !== want) problems.push('out of date: sitemap.xml (vehicle URLs)');
} else put('sitemap.xml', smLines.join('\n'));

// ---------- 5. internal links ----------
const linkFiles = [];
(function walk(dir) {
  for (const d of fs.readdirSync(path.join(REPO, dir), { withFileTypes: true })) {
    const rel = dir ? `${dir}/${d.name}` : d.name;
    if (d.isDirectory()) {
      if (['.git', '_hub', 'node_modules'].includes(d.name) || (dir === 'inspect' && CH[d.name])) continue;
      walk(rel);
    } else if (d.name.endsWith('.html') && rel !== 'inspect/index.html') linkFiles.push(rel);
  }
})('');
if (exists('_hub/Content/blog')) for (const f of fs.readdirSync(path.join(REPO, '_hub/Content/blog'))) if (f.endsWith('.md')) linkFiles.push(`_hub/Content/blog/${f}`);
if (exists('llms.txt')) linkFiles.push('llms.txt');

const T = `[^&"'\`\\s<>#)\\]]+`;
// One regex, two forms. Quoted URLs (HTML attributes, JS strings, JSON-LD) are matched whole,
// spaces included (model=Golf Alltrack S), so an unresolvable one is consumed and left alone
// instead of being cut at the space. Unquoted URLs (markdown links) must end at a terminator,
// and are skipped when a space + word follows (a model name that continues past the space).
const reLink = new RegExp(
  `(["'])((?:https://autovetting\\.com)?)/inspect/\\?year=(\\d{4})(?:&amp;|&)make=([^&"'<>]+)(?:&amp;|&)model=([^&"'<>]+?)((?:(?:&amp;|&)[a-z]+=[^&"'<>]*)*)\\1` +
  `|/inspect/\\?year=(\\d{4})(?:&amp;|&)make=(${T})(?:&amp;|&)model=(${T})((?:(?:&amp;|&)[a-z]+=${T.slice(0, -1)}*)*)(?=$|[\\s"'<>)\\]#])(?! [A-Za-z0-9])`, 'gm');
const reVeh = /\/inspect\/\?vehicle=(\d{4})-([a-z0-9-]+)/g;
// ?vehicle=2019-chevrolet-equinox → the checklist whose menu years include 2019
function vehKey(y, rest) {
  const c = KEYS.filter(k => k.replace(/-\d{4}$/, '') === rest);
  return c.find(k => years[k] && years[k].has(y)) || c.find(k => CH[k].year === y) || null;
}
const dec = s => { try { return decodeURIComponent(s.replace(/\+/g, ' ')); } catch (e) { return s; } };
let linksFixed = 0;
const linkReport = [];
for (const rel of linkFiles) {
  const cur = rd(rel);
  let n = 0;
  let out = cur.replace(reLink, (m, q, host, y1, mk1, md1, x1, y2, mk2, md2) => {
    const k = q ? findKey(+y1, dec(mk1), dec(md1)) : findKey(+y2, dec(mk2), dec(md2));
    if (!k) return m;
    n++;
    return q ? q + host + url(k) + q : url(k);
  });
  out = out.replace(reVeh, (m, y, rest) => { const k = vehKey(+y, rest); if (!k) return m; n++; return url(k); });
  if (n) { linksFixed += n; linkReport.push(`${rel} (${n})`); put(rel, out); }
}

// ---------- report ----------
if (CHECK) {
  if (problems.length) {
    console.log(`${problems.length} out-of-date item(s); ${linksFixed} internal link(s) still use /inspect/?…`);
    problems.slice(0, 8).forEach(p => console.log('  ' + p));
    console.log('Fix: node scripts/build-vehicle-pages.js, then commit the result.');
    process.exit(1);
  }
  console.log(`vehicle pages in sync: ${KEYS.length} pages, sitemap, links`);
} else {
  console.log(`checklists: ${KEYS.length} | pages written: ${pagesChanged} | retired: ${retired.length}${retired.length ? ' (' + retired.join(', ') + ')' : ''}`);
  console.log(`links rewritten: ${linksFixed} in ${linkReport.length} file(s)`);
  linkReport.forEach(r => console.log('  ' + r));
  console.log(`files changed: ${changed.length}`);
}
