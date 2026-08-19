/* =============================================================
   PathMole Expert Lab — chatbot.js (engine)
   Rule-based, floating on all pages. Reads CHATBOT_RULES +
   CHATBOT_CONFIG from data/chatbot-rules.js. Do NOT edit answers
   here — edit the rules file. Keyboard accessible (Enter, Esc).

   Chat history persists across page navigation (sessionStorage)
   and is cleared only on a full page reload.
   ============================================================= */
(function () {
  "use strict";
  if (typeof CHATBOT_RULES === "undefined" || typeof CHATBOT_CONFIG === "undefined") return;
  const mount = document.getElementById("chatbot");
  if (!mount) return;

  const cfg = CHATBOT_CONFIG;
  const ruleById = (id) => CHATBOT_RULES.find((r) => r.id === id);

  /* ---------- Link base path ----------
     Rules use root-relative hrefs like "tests.html" / "case-studies/".
     On pages inside /case-studies/ those would resolve one level too deep,
     so prefix "../" there. Absolute/protocol/anchor links pass through. */
  const BASE = /\/case-studies\//.test(location.pathname) ? "../" : "";
  function resolveHref(href) {
    if (!href) return href;
    if (/^(https?:|tel:|mailto:|#|\/|\.\.\/)/.test(href)) return href;
    return BASE + href;
  }

  /* ---------- History persistence ----------
     - Link navigation between pages KEEPS the transcript.
     - A full reload CLEARS it (fresh session).
     We detect a reload via the Navigation Timing API. */
  const STORE_KEY = "pm_chat_history";
  const OPEN_KEY = "pm_chat_open";

  function isReload() {
    try {
      const nav = performance.getEntriesByType("navigation")[0];
      if (nav && nav.type) return nav.type === "reload";
      // Fallback for older browsers (deprecated API)
      return performance.navigation && performance.navigation.type === 1;
    } catch (e) {
      return false;
    }
  }

  let history = [];
  let wasOpen = false;
  if (isReload()) {
    try { sessionStorage.removeItem(STORE_KEY); sessionStorage.removeItem(OPEN_KEY); } catch (e) {}
  } else {
    try { history = JSON.parse(sessionStorage.getItem(STORE_KEY)) || []; } catch (e) { history = []; }
    try { wasOpen = sessionStorage.getItem(OPEN_KEY) === "1"; } catch (e) { wasOpen = false; }
  }

  function persist() {
    try { sessionStorage.setItem(STORE_KEY, JSON.stringify(history)); } catch (e) {}
  }
  function persistOpen(open) {
    try { sessionStorage.setItem(OPEN_KEY, open ? "1" : "0"); } catch (e) {}
  }

  /* ---------- Build UI ---------- */
  mount.innerHTML = `
    <button class="chatbot-launcher" id="cb-launcher" aria-label="Open chat assistant" aria-expanded="false">
      <span class="cb-tip">Ask us</span>
      <span class="cb-ico" aria-hidden="true">
        <svg viewBox="0 0 64 64" fill="none" aria-hidden="true">
          <!-- PathMole brand mark: P + magenta molecular dot -->
          <path d="M20 16h13c6.6 0 11 3.7 11 9.6 0 6-4.4 9.8-11 9.8h-6.2V48H20V16zm12 13.6c2.6 0 4.2-1.4 4.2-3.9 0-2.4-1.6-3.8-4.2-3.8h-5.2v7.7H32z" fill="#fff"/>
          <circle cx="45" cy="44" r="6" fill="#EC008C"/>
          <circle cx="45" cy="44" r="2.4" fill="#fff"/>
        </svg>
      </span>
      <span class="cb-badge" aria-hidden="true"></span>
    </button>
    <div class="chatbot-panel" id="cb-panel" role="dialog" aria-label="PathMole chat assistant" aria-modal="false">
      <div class="chatbot-header">
        <span class="dot"></span>
        <div><strong>PathMole Assistant</strong><small>Ask me about tests, services &amp; more</small></div>
        <button class="chatbot-close" id="cb-close" aria-label="Close chat">&times;</button>
      </div>
      <div class="chatbot-body" id="cb-body"></div>
      <form class="chatbot-input" id="cb-form" autocomplete="off">
        <input type="text" id="cb-input" placeholder="Type your question…" aria-label="Type your question" />
        <button type="submit" aria-label="Send"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M6 12L3.3 4.3a.6.6 0 01.8-.8l16 8a.6.6 0 010 1l-16 8a.6.6 0 01-.8-.8L6 12zm0 0h7"/></svg></button>
      </form>
    </div>`;

  const launcher = document.getElementById("cb-launcher");
  const panel = document.getElementById("cb-panel");
  const closeBtn = document.getElementById("cb-close");
  const body = document.getElementById("cb-body");
  const form = document.getElementById("cb-form");
  const input = document.getElementById("cb-input");
  let greeted = false;

  /* ---------- Helpers ---------- */
  function scrollDown() { body.scrollTop = body.scrollHeight; }

  function chip(text, cls, onClick, href) {
    const el = document.createElement(href ? "a" : "button");
    el.className = "chat-chip" + (cls ? " " + cls : "");
    el.textContent = text;
    if (href) { el.href = href; if (/^https?:/.test(href)) { el.target = "_blank"; el.rel = "noopener noreferrer"; } }
    if (onClick) el.addEventListener("click", onClick);
    return el;
  }

  /* Build the chip nodes for a serialisable action entry */
  function buildActionNodes(entry) {
    switch (entry.kind) {
      case "link":
        return [chip(entry.text || "Open", "pink", null, resolveHref(entry.href))];
      case "links":
        return (entry.items || []).map((it) => chip(it.text || "Open", "pink", null, resolveHref(it.href)));
      case "contact":
        return [
          chip("📞 Call", null, null, "tel:" + cfg.phone),
          chip("WhatsApp", "wa", null, "https://wa.me/" + cfg.whatsapp),
          chip("Send enquiry", "pink", null, resolveHref(cfg.enquiryHref || "contact.html#enquiry")),
        ];
      case "fallback":
        return [
          chip("📞 Call", null, null, "tel:" + cfg.phone),
          chip("WhatsApp", "wa", null, "https://wa.me/" + cfg.whatsapp),
          chip("Send enquiry", "pink", null, resolveHref(cfg.enquiryHref || "contact.html#enquiry")),
        ];
      case "menu":
        return (cfg.menu || []).map((id) => {
          const r = ruleById(id);
          return r ? chip(r.label, null, () => handleRule(r)) : null;
        }).filter(Boolean);
      default:
        return [];
    }
  }

  /* Render a stored entry to the DOM (no recording) */
  function renderEntry(entry) {
    if (entry.t === "msg") {
      const el = document.createElement("div");
      el.className = "chat-msg " + (entry.who || "bot");
      el.textContent = entry.text;
      body.appendChild(el);
    } else if (entry.t === "action") {
      const nodes = buildActionNodes(entry);
      if (nodes.length) {
        const wrap = document.createElement("div");
        wrap.className = "chat-actions";
        nodes.forEach((n) => wrap.appendChild(n));
        body.appendChild(wrap);
      }
    }
    scrollDown();
  }

  /* Record (persist) + render a new entry */
  function record(entry) {
    history.push(entry);
    persist();
    renderEntry(entry);
  }

  function addMsg(text, who) { record({ t: "msg", who: who || "bot", text: text }); }

  function renderAction(action) {
    if (!action || action.type === "none") return;
    if (action.type === "link") {
      record({ t: "action", kind: "link", text: action.text || "Open", href: action.href });
    } else if (action.type === "links") {
      record({ t: "action", kind: "links", items: action.items || [] });
    } else if (action.type === "enquiry") {
      record({ t: "action", kind: "link", text: action.text || "Open the enquiry form", href: cfg.enquiryHref || "contact.html#enquiry" });
    } else if (action.type === "contact") {
      record({ t: "action", kind: "contact" });
    }
  }

  function showMenu() { record({ t: "action", kind: "menu" }); }

  function handleRule(rule) {
    addMsg(rule.label, "user");
    setTimeout(() => { addMsg(rule.answer, "bot"); renderAction(rule.action); }, 250);
  }

  function match(text) {
    const q = text.toLowerCase();
    let best = null, bestScore = 0;
    CHATBOT_RULES.forEach((r) => {
      let score = 0;
      (r.keywords || []).forEach((k) => { if (q.includes(k.toLowerCase())) score += k.length; });
      if (score > bestScore) { bestScore = score; best = r; }
    });
    return bestScore > 0 ? best : null;
  }

  function handleText(text) {
    addMsg(text, "user");
    const rule = match(text);
    setTimeout(() => {
      if (rule) { addMsg(rule.answer, "bot"); renderAction(rule.action); }
      else {
        addMsg(cfg.fallback, "bot");
        record({ t: "action", kind: "fallback" });
      }
    }, 250);
  }

  /* ---------- Restore prior transcript (from another page) ---------- */
  if (history.length) {
    history.forEach(renderEntry);
    greeted = true;
  }

  /* ---------- Open / close ---------- */
  function open() {
    panel.classList.add("open");
    launcher.setAttribute("aria-expanded", "true");
    persistOpen(true);
    if (!greeted) {
      greeted = true;
      addMsg(cfg.greeting, "bot");
      showMenu();
    }
    setTimeout(() => input.focus(), 100);
  }
  function close() {
    panel.classList.remove("open");
    launcher.setAttribute("aria-expanded", "false");
    persistOpen(false);
    launcher.focus();
  }

  launcher.addEventListener("click", () => (panel.classList.contains("open") ? close() : open()));
  closeBtn.addEventListener("click", close);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape" && panel.classList.contains("open")) close(); });

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const val = input.value.trim();
    if (!val) return;
    input.value = "";
    handleText(val);
  });

  /* If the panel was open on the previous page, re-open it (without
     re-greeting, since the transcript is already restored). */
  if (wasOpen) {
    panel.classList.add("open");
    launcher.setAttribute("aria-expanded", "true");
    scrollDown();
  }
})();
