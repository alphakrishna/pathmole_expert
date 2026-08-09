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

  // group tests by category
  const groups = {};
  TESTS.forEach((t) => { (groups[t.category] = groups[t.category] || []).push(t); });
  const cats = order.filter((c) => groups[c]).concat(
    Object.keys(groups).filter((c) => !order.includes(c))
  );

  const esc = (s) => String(s).replace(/[&<>"]/g, (m) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[m]));

  let html = "";
  cats.forEach((cat) => {
    const items = groups[cat];
    html += `<div class="test-cat">
      <h2>${esc(cat)} <span class="count">${items.length} test${items.length > 1 ? "s" : ""}</span></h2>
      <div class="grid grid-2">`;
    items.forEach((t) => {
      const chips = (t.symptoms || []).map((s) => `<span>${esc(s)}</span>`).join("");
      html += `<article class="test-card" id="${esc(t.slug)}">
        <h3>${esc(t.name)}</h3>
        <p class="test-info">${esc(t.info || "")}</p>
        ${chips ? `<div class="test-symptoms">${chips}</div>` : ""}
      </article>`;
    });
    html += `</div></div>`;
  });
  mountEl.innerHTML = html;
})();
