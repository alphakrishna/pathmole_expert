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

  /* ---------- News strip dismiss ---------- */
  const newsClose = document.getElementById("news-close");
  if (newsClose) {
    newsClose.addEventListener("click", () => {
      const strip = document.getElementById("news-strip");
      if (strip) strip.style.display = "none";
    });
  }

  /* ---------- Scroll reveal ---------- */
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    const io = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            obs.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("in"));
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
