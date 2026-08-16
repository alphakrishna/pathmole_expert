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
      html += `<article class="test-card" id="${esc(t.slug)}">
        <h3>${esc(t.name)}</h3>
        <p class="test-info">${esc(t.info || "")}</p>
        ${chips ? `<div class="test-symptoms"><span class="test-symptoms-label">Indications</span>${chips}</div>` : ""}
      </article>`;
    });
    html += `</div></div>`;
  });
  mountEl.innerHTML = html;
})();
