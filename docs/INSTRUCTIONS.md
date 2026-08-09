# PATHMOLE Expert — General Instructions & Conventions

> Guidelines for building and maintaining this project. Read this before editing.
> Detailed build spec (page tree, code blocks) lives in **PATHMOLE-WEBSITE-GUIDE.md**.
> **Last updated:** 2026-08-07

---

## 1. What This Project Is

A **static, multi-page website** for **PATHMOLE Expert** — a specialist **Histopathology
& Molecular Diagnostics referral laboratory** in **Gurugram (Delhi NCR)** — plus a
**rule-based chatbot**. Audience is roughly **90% B2B / 10% B2C**: primarily **referring
doctors, hospitals, and diagnostic centres**, plus a minority of **direct walk-in patients**
(so keep patient-facing pages clear and reassuring).

Pure front-end: HTML + CSS + vanilla JavaScript. No frameworks, no build step, no backend.
**Hybrid structure:** a lean **funnel homepage** + dedicated pages for everything heavier.
**Hosted on GoDaddy** (`public_html/`). Anyone with a text editor and browser can edit it.

**How to run locally:** open any `.html` directly in a browser, or serve the folder with a
simple static server (VS Code "Live Server", or `npx serve`).

---

## 2. Two Hard Rules (never break)

1. **No pricing anywhere** — not on any page, not in `data/tests.js`, not in the chatbot.
   Every pricing question is redirected to the **contact flow** (Call / WhatsApp / enquiry).
2. **Case studies are always de-identified** (DPDP Act 2023) — no patient name, ID, photo,
   or re-identifying detail; each carries a disclaimer. Applies to the site AND the email.

Also: never build/replace the **third-party Reporting Portal** (link out only, top of site);
never store patient health data (Patient Form is **download-only**).

---

## 3. Coding Conventions

### General
- **No build tools, frameworks, or npm dependencies** for the site to run.
- Keep it **simple and readable** — editable by non-experts.
- Indent with **2 spaces**. UTF-8. Unix (LF) line endings.
- Comment section boundaries clearly in every file.

### HTML
- Semantic tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`).
- Reuse the shared blocks from the GUIDE (head / top bar + nav / footer + chatbot) on every page.
- Every page: exactly one `<h1>`, unique `<title>` + `<meta description>`, `<link rel="canonical">`.
- All images need meaningful `alt` text and should be **WebP** + lazy-loaded. No inline styles.

### CSS
- **All theme values live in `:root` CSS variables** (colors, fonts, spacing, radius).
  Re-theme by editing variables, not scattered values.
- Mobile-first: base styles for mobile, `@media (min-width: …)` for larger screens.
- Use `rem` for font sizes/spacing where possible.
- Class naming: descriptive kebab-case (`.service-card`, `.btn-primary`, `.cta-pair`).

### JavaScript
- **Vanilla JS only.** No jQuery, no libraries.
- `const`/`let`, never `var`. Small, named functions. DOM selectors at the top.
- No secrets or API keys anywhere (there's no backend).

---

## 4. How to Edit Content (for the client / non-developers)

- **Text:** open the relevant `.html` page, find the section, edit text between the tags.
  Don't touch anything inside `< >` unless you know what it does.
- **Tests:** edit **`data/tests.js`** — each test has `slug`, `name`, `category`,
  `symptoms[]`, `info`. **There is no price field — never add one.**
- **Images:** drop WebP files into `assets/` and update the `src="..."` path.
- **Colors / fonts:** edit the values at the top of `css/style.css` under `:root { … }`.
- **Contact details:** search the pages for the phone/email/address/`[PHONE]` placeholders.

---

## 5. How to Edit the Chatbot

Rule-based, no AI. It is the site's **only test-finder**. All Q&A lives in
**`data/chatbot-rules.js`** — edit answers there; don't touch the engine (`js/chatbot.js`).

Each rule looks like:
```js
{
  id: "find-test",
  label: "Find a test",                          // quick-reply button text
  keywords: ["test", "biopsy", "thyroid"],       // words that trigger via typed text
  answer: "Tell me the symptom or test name...", // the bot's reply
  action: { type: "link", href: "tests.html", text: "Browse all tests" }
}
```
- **Pricing rule:** must use `action: { type: "contact" }` (renders Call / WhatsApp) and
  must NEVER contain a price.
- Keep a **fallback** rule for no-match (routes to WhatsApp / phone).
- Keywords are matched case-insensitively; keep them lowercase and specific.

---

## 6. Placeholder Convention

While waiting for real content, use clearly marked placeholders so nothing fake ships:
- Text: `[PLACEHOLDER: service description]`
- Bracketed tokens already in the GUIDE: `[DOMAIN]`, `[PHONE]`, `[WHATSAPP]`,
  `[REPORTING_PORTAL_URL]`, `[GOOGLE_MAPS_EMBED_URL]`, `G-XXXXXXX` (GA4), social links.
- Links: `href="#"` with a `TODO` comment. Images: labeled placeholders + `TODO`.

**Never invent** tests, symptoms, prices, accreditations (NABL/CAP), or contact details —
use placeholders and wait for the client. Search for `PLACEHOLDER` / `TODO` before launch — none should remain.

---

## 7. Accessibility & Quality Bar

- Color contrast meets **WCAG AA**.
- Site and **chatbot are keyboard-navigable** (Tab, Enter, Esc to close).
- `aria-label`s on icon-only buttons (hamburger, chatbot toggle, send, back-to-top).
- Test at **320px, 768px, 1280px** before considering a section done.
- No console errors.

---

## 8. Working Style (for this project)

- **Plan before building.** Keep `PLAN.md` and `TASKS.md` current as we go.
- Build **one phase at a time** (see PLAN.md §7); don't jump ahead.
- **Homepage stays a lean funnel** — heavy content goes to its own page.
- Prefer **placeholders over invented facts**.
- Keep everything **easy to hand off**: clear structure, comments, and docs.
