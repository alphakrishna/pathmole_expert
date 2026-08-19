/* =============================================================
   PathMole Expert Lab — main.js
   Nav shadow · mobile menu · scroll reveal · back-to-top ·
   news-strip dismiss · enquiry form (front-end only).
   Vanilla JS. No dependencies.
   ============================================================= */
(function () {
  "use strict";

  /* ---------- Sticky nav shadow ---------- */
  const nav = document.getElementById("site-nav");
  const onScroll = () => {
    if (nav) nav.classList.toggle("scrolled", window.scrollY > 8);
    const btt = document.getElementById("back-to-top");
    if (btt) btt.classList.toggle("show", window.scrollY > 400);
    const bp = document.getElementById("back-page");
    if (bp) bp.classList.toggle("show", window.scrollY > 300);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile menu ---------- */
  const toggle = document.getElementById("menu-toggle");
  const menu = document.getElementById("mobile-menu");
  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      const open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    menu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  /* ---------- Back to top ---------- */
  const backTop = document.getElementById("back-to-top");
  if (backTop) {
    backTop.addEventListener("click", () =>
      window.scrollTo({ top: 0, behavior: "smooth" })
    );
  }

  /* ---------- Back (previous page) ---------- */
  const backPage = document.getElementById("back-page");
  if (backPage) {
    // Use browser history when there is one, otherwise fall back to the
    // page's declared parent (data-home) so the button never dead-ends.
    backPage.addEventListener("click", () => {
      if (history.length > 1) history.back();
      else window.location.href = backPage.getAttribute("data-home") || "index.html";
    });
  }

  /* ---------- News strip: rotate highlights ---------- */
  const newsStrip = document.getElementById("news-strip");
  const newsText = document.getElementById("news-text");
  const newsCopy = document.getElementById("news-copy");
  if (newsStrip && newsText && newsCopy) {
    // Each item is a real, existing page — nothing invented. The first item is
    // already rendered in the HTML, so the rotation starts from index 1.
    const NEWS = [
      { text: "In-house Training Institute — hands-on pathology education few diagnostic labs offer.", cta: "Explore →", href: "training-institute.html" },
      { text: "Histopathology, cytopathology and molecular testing — under one roof.", cta: "See services →", href: "services.html" },
      { text: "Reporting built on WHO, ASCO–CAP and CAP–AMP guidelines.", cta: "See research →", href: "case-studies/" },
      { text: "Led by pathologists with decades of diagnostic experience.", cta: "Meet the team →", href: "physicians.html" },
      { text: "Access your test reports online — secure and convenient.", cta: "Reports login →", href: "#" },
      { text: "Refer cases or set up a lab tie-up — partner with us.", cta: "Partner with us →", href: "partner.html" }
    ];
    let idx = 0;
    let paused = false;
    setInterval(() => {
      if (paused || newsStrip.style.display === "none") return;
      idx = (idx + 1) % NEWS.length;
      newsStrip.classList.add("is-swapping");
      setTimeout(() => {
        newsCopy.innerHTML = NEWS[idx].text;
        newsStrip.classList.remove("is-swapping");
      }, 400);
    }, 7000);

    /* ---------- "See all updates" popup (page-level modal) ---------- */
    const newsAll = document.getElementById("news-all");
    const newsPanel = document.getElementById("news-panel");
    const newsList = document.getElementById("news-list");
    if (newsAll && newsPanel && newsList) {
      NEWS.forEach((it) => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = it.href;
        a.innerHTML = it.text + '<span class="news-item-cta">' + it.cta + "</span>";
        li.appendChild(a);
        newsList.appendChild(li);
      });
      const setPanel = (open) => {
        newsPanel.hidden = !open;
        newsAll.setAttribute("aria-expanded", open ? "true" : "false");
        newsText.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.classList.toggle("news-open", open); // lock page scroll behind the popup
        paused = open; // hold the rotation still while the popup is open
      };
      const toggle = () => setPanel(newsPanel.hidden);
      newsAll.addEventListener("click", toggle);
      newsText.addEventListener("click", toggle);
      // Close on the × button or by clicking the dimmed backdrop.
      newsPanel.addEventListener("click", (e) => {
        if (e.target.closest("[data-news-close]") || e.target.id === "news-modal-x") setPanel(false);
      });
      document.addEventListener("keydown", (e) => {
        if (e.key === "Escape" && !newsPanel.hidden) setPanel(false);
      });
    }
  }

  /* ---------- Scroll reveal ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    // Reveal on the way DOWN only. An element animates in as it enters from the
    // bottom; once scrolled past (it exits via the top) we keep it revealed, so
    // scrolling back up never re-triggers it. It only re-arms when it sits fully
    // below the viewport again (top > 0) — off-screen, so there's no flicker —
    // meaning a later downward scroll replays the animation.
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
          } else if (e.boundingClientRect.top > 0) {
            e.target.classList.remove("in");
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("in"));
  }

  /* ---------- CTA band accent line: fills/empties in lockstep with scroll ----------
     Mapped across the whole scroll range from where the band first appears at the
     viewport bottom (45%) to the very bottom of the page (100%). Every scroll tick
     up or down moves the line proportionally — no flat/saturated stretch. */
  const ctaBands = Array.prototype.slice.call(document.querySelectorAll(".cta-band"));
  const reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (ctaBands.length && !reduceMotion) {
    const docEl = document.documentElement;
    let lineTicking = false;
    const updateCtaLines = () => {
      lineTicking = false;
      const vh = window.innerHeight || docEl.clientHeight;
      const scrollY = window.scrollY || docEl.scrollTop;
      const maxScroll = (docEl.scrollHeight || document.body.scrollHeight) - vh;
      ctaBands.forEach((el) => {
        const absTop = el.getBoundingClientRect().top + scrollY; // band's offset from doc top
        const start = absTop - vh;                                // scrollY where band starts to appear
        const denom = Math.max(1, maxScroll - start);             // travel until page bottom
        let p = (scrollY - start) / denom;
        p = p < 0 ? 0 : p > 1 ? 1 : p;
        el.style.setProperty("--line-fill", (45 + p * 55).toFixed(1) + "%");
      });
    };
    const onLineScroll = () => {
      if (!lineTicking) { lineTicking = true; requestAnimationFrame(updateCtaLines); }
    };
    window.addEventListener("scroll", onLineScroll, { passive: true });
    window.addEventListener("resize", onLineScroll, { passive: true });
    updateCtaLines();
  }

  /* ---------- Enquiry form (front-end only) ----------
     Set FORM_ENDPOINT to a Web3Forms / Formspree URL to go live.
     Until then, the form validates and shows a friendly message. */
  const FORM_ENDPOINT = ""; // TODO: paste Web3Forms/Formspree endpoint
  const form = document.getElementById("enquiry-form");
  if (form) {
    const status = form.querySelector(".form-status");
    form.addEventListener("submit", async (ev) => {
      ev.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      const setStatus = (msg, ok) => {
        if (!status) return;
        status.textContent = msg;
        status.className = "form-status " + (ok ? "ok" : "err");
      };
      if (!FORM_ENDPOINT) {
        setStatus(
          "Thanks! Form delivery isn't connected yet — meanwhile, please call or WhatsApp us at +91 98998 22375.",
          true
        );
        form.reset();
        return;
      }
      try {
        const res = await fetch(FORM_ENDPOINT, {
          method: "POST",
          headers: { Accept: "application/json" },
          body: new FormData(form),
        });
        if (res.ok) {
          setStatus("Thank you — your enquiry has been sent. We'll be in touch shortly.", true);
          form.reset();
        } else {
          setStatus("Something went wrong. Please call or WhatsApp us at +91 98998 22375.", false);
        }
      } catch (_) {
        setStatus("Network error. Please call or WhatsApp us at +91 98998 22375.", false);
      }
    });
  }
})();
