/* =============================================================
   PathMole Expert Lab — tests.js
   Renders the test list from data/tests.js, grouped by category.
   NO prices anywhere. Reads TESTS + CATEGORY_ORDER.
   ============================================================= */
(function () {
  "use strict";
  const mountEl = document.getElementById("test-list");
  if (!mountEl || typeof TESTS === "undefined") return;
  const order = typeof CATEGORY_ORDER !== "undefined" ? CATEGORY_ORDER : [];

  // Per-discipline illustration (gradient tile SVG) + a plain-language line that
  // explains, at a glance, what the tests in this group actually do. These are
  // standard textbook definitions of each discipline — no lab-specific claims.
  const CATEGORY_META = {
    "Histopathology": {
      blurb: "Microscopic examination of tissues and cells to establish or confirm a diagnosis.",
      icon: '<path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35m1.6-3.9a5.5 5.5 0 11-11 0 5.5 5.5 0 0111 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M12.15 12.7a1 1 0 100-2 1 1 0 000 2z"/>',
    },
    "Immunohistochemistry": {
      blurb: "Antibody-based staining that highlights specific proteins to characterise tumours and guide treatment.",
      icon: '<path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 003 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 005.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 009.568 3z"/><path stroke-linecap="round" stroke-linejoin="round" d="M6 6h.008v.008H6V6z"/>',
    },
    "Molecular Diagnostics": {
      blurb: "DNA- and RNA-level testing that detects mutations and molecular alterations.",
      icon: '<path stroke-linecap="round" stroke-linejoin="round" d="M8 3c2 3 2 5 0 8s-2 5 0 8m8-16c-2 3-2 5 0 8s2 5 0 8M7 7h10M7 17h10"/>',
    },
    "FISH & Cytogenetics": {
      blurb: "Fluorescent probes that reveal gene amplifications and rearrangements at the chromosome level.",
      icon: '<path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456z"/>',
    },
  };
  const FALLBACK_ICON = '<path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"/>';

  // Per-TEST illustrations — same gradient-tile style as the category icons, so each
  // card gets its own at-a-glance visual. Keyed by slug; any test without an entry
  // falls back to its category icon, then the generic fallback. Purely presentational.
  const P = {
    specimen: '<path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"/>',
    review: '<path stroke-linecap="round" stroke-linejoin="round" d="M8.625 9.75a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z"/>',
    block: '<path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9"/>',
    slides: '<path stroke-linecap="round" stroke-linejoin="round" d="M6 6.878V6a2.25 2.25 0 012.25-2.25h7.5A2.25 2.25 0 0118 6v.878m-12 0c.235-.083.487-.128.75-.128h10.5c.263 0 .515.045.75.128m-12 0A2.25 2.25 0 004.5 9v.878m13.5-3A2.25 2.25 0 0119.5 9v.878m0 0a2.246 2.246 0 00-.75-.128H5.25c-.263 0-.515.045-.75.128m15 0A2.25 2.25 0 0121 12v6a2.25 2.25 0 01-2.25 2.25H5.25A2.25 2.25 0 013 18v-6c0-.98.626-1.813 1.5-2.122"/>',
    droplet: '<path stroke-linecap="round" stroke-linejoin="round" d="M12 2.25c-.5 0-8.25 8.5-8.25 13.5a8.25 8.25 0 0016.5 0c0-5-7.75-13.5-8.25-13.5z"/>',
    virus: '<circle cx="12" cy="12" r="4.25"/><path stroke-linecap="round" stroke-linejoin="round" d="M12 2.4v2.35M12 19.25v2.35M2.4 12h2.35M19.25 12h2.35M5.16 5.16l1.66 1.66M17.18 17.18l1.66 1.66M18.84 5.16l-1.66 1.66M6.82 17.18l-1.66 1.66"/>',
    dna: '<path stroke-linecap="round" stroke-linejoin="round" d="M8 3c2 3 2 5 0 8s-2 5 0 8m8-16c-2 3-2 5 0 8s2 5 0 8M7 7h10M7 17h10"/>',
    panel: '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12h3.75M9 15h3.75M9 18h3.75m3 .75H18a2.25 2.25 0 002.25-2.25V6.108c0-1.135-.845-2.098-1.976-2.192a48.424 48.424 0 00-1.123-.08m-5.801 0c-.065.21-.1.433-.1.664 0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75 2.25 2.25 0 00-.1-.664m-5.8 0A2.251 2.251 0 0113.5 2.25H15c1.012 0 1.867.668 2.15 1.586m-5.8 0c-.376.023-.75.05-1.124.08C9.095 4.01 8.25 4.973 8.25 6.108V8.25m0 0H4.875c-.621 0-1.125.504-1.125 1.125v11.25c0 .621.504 1.125 1.125 1.125h9.75c.621 0 1.125-.504 1.125-1.125V9.375c0-.621-.504-1.125-1.125-1.125H8.25z"/>',
  };
  const TEST_ICONS = {
    // Histopathology
    "small-biopsy": P.specimen,
    "medium-biopsy": P.specimen,
    "large-biopsy": P.specimen,
    "extra-large-biopsy": P.specimen,
    "second-opinion": P.review,
    "cell-block": P.block,
    "slides-blocks": P.slides,
    "fluid-cytology-lbc-pap": P.droplet,
    // Molecular Diagnostics
    "hbv-molecular": P.virus,
    "hcv-molecular": P.virus,
    "hiv-molecular": P.virus,
    "hla-b27": P.dna,
    "flu-panel": P.panel,
    "hpv-molecular": P.virus,
    "tb-molecular": P.virus,
  };

  // group tests by category
  const groups = {};
  TESTS.forEach((t) => { (groups[t.category] = groups[t.category] || []).push(t); });
  const cats = order.filter((c) => groups[c]).concat(
    Object.keys(groups).filter((c) => !order.includes(c))
  );

  const esc = (s) => String(s).replace(/[&<>"]/g, (m) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]));
  const svg = (inner) =>
    `<svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor" aria-hidden="true">${inner}</svg>`;

  let html = "";
  cats.forEach((cat) => {
    const items = groups[cat];
    const meta = CATEGORY_META[cat] || {};
    html += `<div class="test-cat">
      <div class="test-cat-head">
        <div class="test-cat-icon">${svg(meta.icon || FALLBACK_ICON)}</div>
        <div>
          <h2>${esc(cat)} <span class="count">${items.length} test${items.length > 1 ? "s" : ""}</span></h2>
          ${meta.blurb ? `<p class="test-cat-blurb">${esc(meta.blurb)}</p>` : ""}
        </div>
      </div>
      <div class="grid grid-2">`;
    items.forEach((t) => {
      const chips = (t.symptoms || []).map((s) => `<span>${esc(s)}</span>`).join("");
      const tIcon = t.icon || TEST_ICONS[t.slug] || meta.icon || FALLBACK_ICON;
      html += `<article class="test-card" id="${esc(t.slug)}">
        <div class="test-card-head">
          <span class="test-card-icon">${svg(tIcon)}</span>
          <h3>${esc(t.name)}</h3>
        </div>
        <p class="test-info">${esc(t.info || "")}</p>
        ${chips ? `<div class="test-symptoms"><span class="test-symptoms-label">Indications</span>${chips}</div>` : ""}
      </article>`;
    });
    html += `</div></div>`;
  });
  mountEl.innerHTML = html;
})();
