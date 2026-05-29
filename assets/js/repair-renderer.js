/* ============================================================
   AutoVetting — Repair Guide Renderer
   Reads inline <script id="guideData" type="application/json">
   and populates the guide page DOM.
   Shared across all /repair/<slug>/ guide pages.
   ============================================================ */
(function () {
  'use strict';

  // ----- Load data -----
  var dataEl = document.getElementById('guideData');
  if (!dataEl) { console.error('repair-renderer: no #guideData element'); return; }
  var data;
  try { data = JSON.parse(dataEl.textContent); }
  catch (e) { console.error('repair-renderer: JSON parse failed', e); return; }

  // ----- Escape helper -----
  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ----- Breadcrumb category label -----
  var catLabels = { safety: 'Safety', fluids: 'Fluids', electrical: 'Electrical', filters: 'Filters', maintenance: 'Maintenance' };
  var crumbCat = document.getElementById('crumbCategory');
  if (crumbCat && data.category) crumbCat.textContent = catLabels[data.category] || data.category;

  // ----- Hero: title, summary, meta strip -----
  var titleEl = document.getElementById('title');
  if (titleEl) titleEl.textContent = data.title;

  var summaryEl = document.getElementById('summary');
  if (summaryEl) summaryEl.textContent = data.summary;

  var meta = document.getElementById('metaStrip');
  if (meta) {
    function pill(label, cls) {
      var p = document.createElement('span');
      p.className = 'rg-pill' + (cls ? ' ' + cls : '');
      p.innerHTML = '<span class="dot"></span>' + esc(label);
      return p;
    }
    if (data.safety_critical) meta.appendChild(pill('Safety critical', 'safety'));
    var diffLabels = ['', 'Beginner', 'Beginner', 'Intermediate', 'Advanced', 'Pro'];
    meta.appendChild(pill('Difficulty: ' + (diffLabels[data.difficulty] || data.difficulty) + ' (' + data.difficulty + '/5)'));
    meta.appendChild(pill('Time: ' + data.time_hours.low + '–' + data.time_hours.high + ' hrs'));
    meta.appendChild(pill('Parts: $' + data.cost_usd.low + '–$' + data.cost_usd.high));
  }

  // ----- Honest answer -----
  var aeoEl = document.getElementById('aeoAnswer');
  if (aeoEl) aeoEl.textContent = data.aeo_answer;

  // ----- Symptoms -----
  var symList = document.getElementById('symptomsList');
  if (symList && data.symptoms) {
    data.symptoms.forEach(function (s) {
      var li = document.createElement('li');
      li.textContent = s;
      symList.appendChild(li);
    });
  }

  // ----- Tools -----
  var reqList = document.getElementById('toolsRequired');
  var optList = document.getElementById('toolsOptional');
  if (reqList && data.tools_required) {
    data.tools_required.forEach(function (t) {
      var li = document.createElement('li');
      li.innerHTML = '<strong>' + esc(t.name) + '</strong>' +
        (t.note ? '<span class="rg-tool-note">' + esc(t.note) + '</span>' : '');
      (t.required === false ? optList : reqList).appendChild(li);
    });
    if (optList && !optList.children.length) {
      optList.innerHTML = '<li style="color:var(--slate-400);font-style:italic">None</li>';
    }
  }

  // ----- Parts -----
  var partsGrid = document.getElementById('partsGrid');
  if (partsGrid && data.parts) {
    data.parts.forEach(function (p) {
      var card = document.createElement('div');
      card.className = 'rg-part' + (p.tier ? ' ' + p.tier : '');
      var html = '';
      if (p.tier) html += '<span class="rg-part-tier ' + esc(p.tier) + '">' + esc(p.tier) + '</span>';
      html += '<div class="rg-part-name">' + esc(p.name) + '</div>';
      if (p.part_number || p.vendor)
        html += '<div class="rg-part-meta">' +
          (p.part_number ? 'PN: ' + esc(p.part_number) : '') +
          (p.part_number && p.vendor ? ' &middot; ' : '') +
          (p.vendor ? esc(p.vendor) : '') + '</div>';
      if (p.price_estimate_usd) html += '<div class="rg-part-price">~$' + p.price_estimate_usd + '</div>';
      if (p.note) html += '<div class="rg-part-note">' + esc(p.note) + '</div>';
      card.innerHTML = html;
      partsGrid.appendChild(card);
    });
  }

  // ----- Torque table -----
  var torqueSection = document.getElementById('torque');
  var torqueBody = document.getElementById('torqueBody');
  var torqueUnit = 'ft_lb';

  function renderTorque() {
    if (!torqueBody) return;
    torqueBody.innerHTML = '';
    (data.torque_specs || []).forEach(function (t) {
      var tr = document.createElement('tr');
      var val = torqueUnit === 'ft_lb' ? (t.ft_lb + ' ft-lb') : (t.nm + ' Nm');
      tr.innerHTML = '<td>' + esc(t.fastener) + '</td>' +
        '<td class="rg-torque-value">' + val + '</td>' +
        '<td class="rg-torque-notes">' + esc(t.notes || '') + '</td>';
      torqueBody.appendChild(tr);
    });
    // update torque pills in steps
    document.querySelectorAll('.rg-step-pill.torque').forEach(function (pill) {
      var key = pill.getAttribute('data-key');
      var spec = (data.torque_specs || []).find(function (s) { return s.key === key; });
      if (spec) {
        var val = torqueUnit === 'ft_lb' ? spec.ft_lb + ' ft-lb' : spec.nm + ' Nm';
        pill.textContent = spec.fastener + ': ' + val;
      }
    });
  }

  if (torqueSection) {
    if (!data.torque_specs || !data.torque_specs.length) {
      torqueSection.style.display = 'none';
      // also hide torque from TOC
      document.querySelectorAll('.rg-toc a[href="#torque"]').forEach(function (a) {
        a.parentElement.style.display = 'none';
      });
    } else {
      var unitFtLb = document.getElementById('unitFtLb');
      var unitNm = document.getElementById('unitNm');
      if (unitFtLb) unitFtLb.addEventListener('click', function () {
        torqueUnit = 'ft_lb';
        unitFtLb.classList.add('on');
        if (unitNm) unitNm.classList.remove('on');
        renderTorque();
      });
      if (unitNm) unitNm.addEventListener('click', function () {
        torqueUnit = 'nm';
        unitNm.classList.add('on');
        if (unitFtLb) unitFtLb.classList.remove('on');
        renderTorque();
      });
      renderTorque();
    }
  }

  // ----- Step walker -----
  var storageKey = 'av_repair_' + data.id;
  var done = (function () {
    try { var r = localStorage.getItem(storageKey); return r ? JSON.parse(r) : {}; }
    catch (e) { return {}; }
  })();
  function saveProgress() {
    try { localStorage.setItem(storageKey, JSON.stringify(done)); } catch (e) {}
  }

  function torquePillHTML(key) {
    if (!data.torque_specs) return '';
    var spec = data.torque_specs.find(function (s) { return s.key === key; });
    if (!spec) return '';
    var val = torqueUnit === 'ft_lb' ? spec.ft_lb + ' ft-lb' : spec.nm + ' Nm';
    return '<span class="rg-step-pill torque" data-key="' + esc(key) + '">' + esc(spec.fastener) + ': ' + val + '</span>';
  }

  var stepsEl = document.getElementById('steps');
  if (stepsEl && data.steps) {
    data.steps.forEach(function (step, i) {
      var li = document.createElement('li');
      li.className = 'rg-step' + (done[i] ? ' done' : '');
      li.setAttribute('data-idx', i);

      var pills = '';
      if (step.torque) pills += torquePillHTML(step.torque);
      if (step.warn) pills += '<span class="rg-step-pill warn">' + esc(step.warn) + '</span>';

      li.innerHTML =
        '<div class="rg-step-num"><span>' + (i + 1) + '</span></div>' +
        '<div class="rg-step-body">' +
          '<div class="rg-step-headline">' +
            '<input type="checkbox" class="rg-step-checkbox"' + (done[i] ? ' checked' : '') + ' aria-label="Mark step ' + (i + 1) + ' complete">' +
            '<span>' + esc(step.headline) + '</span>' +
          '</div>' +
          (pills ? '<div class="rg-step-pills">' + pills + '</div>' : '') +
          '<div class="rg-step-prose">' + esc(step.body) + '</div>' +
        '</div>';

      var cb = li.querySelector('.rg-step-checkbox');
      cb.addEventListener('change', function () {
        if (cb.checked) done[i] = true; else delete done[i];
        li.classList.toggle('done', !!done[i]);
        saveProgress();
        updateProgress();
      });
      stepsEl.appendChild(li);
    });
  }

  function updateProgress() {
    var total = data.steps ? data.steps.length : 0;
    var doneCount = Object.keys(done).length;
    var pct = total ? Math.round(doneCount / total * 100) : 0;
    var curStep = document.getElementById('curStep');
    var totalStep = document.getElementById('totalStep');
    var pctLabel = document.getElementById('pctLabel');
    var progressFill = document.getElementById('progressFill');
    var miniCount = document.getElementById('miniCount');
    var miniFill = document.getElementById('miniFill');
    if (curStep) curStep.textContent = doneCount;
    if (totalStep) totalStep.textContent = total;
    if (pctLabel) pctLabel.textContent = pct + '%';
    if (progressFill) progressFill.style.width = pct + '%';
    if (miniCount) miniCount.textContent = doneCount + ' / ' + total;
    if (miniFill) miniFill.style.width = pct + '%';
  }
  updateProgress();

  var resetBtn = document.getElementById('resetBtn');
  if (resetBtn) resetBtn.addEventListener('click', function () {
    if (!confirm('Reset all progress for this guide?')) return;
    done = {};
    saveProgress();
    document.querySelectorAll('.rg-step').forEach(function (s) {
      s.classList.remove('done');
      var cb = s.querySelector('.rg-step-checkbox');
      if (cb) cb.checked = false;
    });
    updateProgress();
  });

  var printBtn = document.getElementById('printBtn');
  if (printBtn) printBtn.addEventListener('click', function () {
    document.body.classList.toggle('rg-print');
    printBtn.textContent = document.body.classList.contains('rg-print') ? 'Exit print mode' : 'Print mode';
  });

  // ----- Verify -----
  var verifyList = document.getElementById('verifyList');
  if (verifyList && data.verify) {
    data.verify.forEach(function (v) {
      var li = document.createElement('li');
      li.textContent = v;
      verifyList.appendChild(li);
    });
  }

  // ----- Common mistakes -----
  var mistakesList = document.getElementById('mistakesList');
  if (mistakesList && data.common_mistakes) {
    data.common_mistakes.forEach(function (m) {
      var li = document.createElement('li');
      li.textContent = m;
      mistakesList.appendChild(li);
    });
  }

  // ----- Related guides -----
  var relatedGrid = document.getElementById('relatedGrid');
  if (relatedGrid && data.related_guides) {
    data.related_guides.forEach(function (r) {
      var a = document.createElement('a');
      a.href = '/repair/' + r.slug + '/';
      a.textContent = r.label;
      relatedGrid.appendChild(a);
    });
    if (!data.related_guides.length) {
      document.getElementById('related').style.display = 'none';
    }
  }

  // ----- Last updated -----
  var lastUpdated = document.getElementById('lastUpdated');
  if (lastUpdated) lastUpdated.textContent = data.last_updated || '';

  // ----- Page title -----
  document.title = data.title + ' — AutoVetting Repair Guides';

  // ----- TOC active-state on scroll -----
  var tocLinks = document.querySelectorAll('.rg-toc a');
  var sections = Array.from(tocLinks).map(function (a) {
    return document.querySelector(a.getAttribute('href'));
  }).filter(Boolean);
  function onScroll() {
    var pos = window.scrollY + 120;
    var current = sections[0];
    sections.forEach(function (s) { if (s.offsetTop <= pos) current = s; });
    tocLinks.forEach(function (a) {
      a.classList.toggle('active', a.getAttribute('href') === '#' + (current ? current.id : ''));
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
