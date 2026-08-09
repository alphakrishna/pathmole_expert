/* =============================================================
   PathMole Expert Lab — chatbot.js (engine)
   Rule-based, floating on all pages. Reads CHATBOT_RULES +
   CHATBOT_CONFIG from data/chatbot-rules.js. Do NOT edit answers
   here — edit the rules file. Keyboard accessible (Enter, Esc).
   ============================================================= */
(function () {
  "use strict";
  if (typeof CHATBOT_RULES === "undefined" || typeof CHATBOT_CONFIG === "undefined") return;
  const mount = document.getElementById("chatbot");
  if (!mount) return;

  const cfg = CHATBOT_CONFIG;
  const ruleById = (id) => CHATBOT_RULES.find((r) => r.id === id);

  /* ---------- Build UI ---------- */
  mount.innerHTML = `
    <button class="chatbot-launcher" id="cb-launcher" aria-label="Open chat assistant" aria-expanded="false">
      <svg fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M8 10h8M8 14h5m-9 6l3-3h9a3 3 0 003-3V7a3 3 0 00-3-3H6a3 3 0 00-3 3v13z"/></svg>
      <span>Ask us</span>
    </button>
    <div class="chatbot-panel" id="cb-panel" role="dialog" aria-label="PathMole chat assistant" aria-modal="false">
      <div class="chatbot-header">
        <span class="dot"></span>
        <div><strong>PathMole Assistant</strong><small>Typically replies with a link</small></div>
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

  function addMsg(text, who) {
    const el = document.createElement("div");
    el.className = "chat-msg " + (who || "bot");
    el.textContent = text;
    body.appendChild(el);
    scrollDown();
  }

  function addActions(nodes) {
    const wrap = document.createElement("div");
    wrap.className = "chat-actions";
    nodes.forEach((n) => wrap.appendChild(n));
    body.appendChild(wrap);
    scrollDown();
  }

  function chip(text, cls, onClick, href) {
    const el = document.createElement(href ? "a" : "button");
    el.className = "chat-chip" + (cls ? " " + cls : "");
    el.textContent = text;
    if (href) { el.href = href; if (/^https?:/.test(href)) { el.target = "_blank"; el.rel = "noopener noreferrer"; } }
    if (onClick) el.addEventListener("click", onClick);
    return el;
  }

  function renderAction(action) {
    if (!action || action.type === "none") return;
    if (action.type === "link") {
      addActions([chip(action.text || "Open", "pink", null, action.href)]);
    } else if (action.type === "contact") {
      addActions([
        chip("📞 Call", null, null, "tel:" + cfg.phone),
        chip("WhatsApp", "wa", null, "https://wa.me/" + cfg.whatsapp),
        chip("Contact page", "pink", null, "contact.html"),
      ]);
    }
  }

  function showMenu() {
    const chips = (cfg.menu || []).map((id) => {
      const r = ruleById(id);
      return r ? chip(r.label, null, () => handleRule(r)) : null;
    }).filter(Boolean);
    if (chips.length) addActions(chips);
  }

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
        addActions([
          chip("📞 Call", null, null, "tel:" + cfg.phone),
          chip("WhatsApp", "wa", null, "https://wa.me/" + cfg.whatsapp),
        ]);
      }
    }, 250);
  }

  /* ---------- Open / close ---------- */
  function open() {
    panel.classList.add("open");
    launcher.setAttribute("aria-expanded", "true");
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
})();
