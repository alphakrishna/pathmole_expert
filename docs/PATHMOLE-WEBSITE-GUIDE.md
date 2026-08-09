# PATHMOLE Expert — Website Build & Update Guide
> Single source of truth for building and maintaining the PATHMOLE Expert website.
> Conventions adapted from the proven drarpangandhi.com guide, rebuilt fresh for a
> diagnostics-lab brand.
> **Last updated:** 2026-08-08 · **Status:** Structure locked · Brand palette locked (navy + magenta)

---

## Project Overview

**Client:** PATHMOLE Expert — a specialist **Histopathology & Molecular Diagnostics
referral laboratory** in **Gurugram, Haryana (Delhi NCR)**. Principals: **Dr. Arpan Gandhi**
(~3 decades in pathology, laboratory medicine, and quality systems) & **Mr. Ashok Yadav**
(20+ years in diagnostic laboratory operations). Launch: **17 Aug 2026**.

**What the lab does (shapes the whole site):** mostly a **specialist referral facility** —
roughly **90% B2B / 10% B2C**. Primary audience = **referring clinicians, hospitals, and
diagnostic centres**; a ~10% minority are **direct walk-in patients** (so keep the Patients
page + downloadable form and patient-facing copy clear and reassuring). It unites two
complementary disciplines on one platform:
- **Histopathology** — *"What does the disease look like?"* (tissue morphology, biopsy,
  cytology, immunohistochemistry / IHC).
- **Molecular Diagnostics** — *"What is driving it?"* (molecular / mutation panels,
  PCR/FISH-type testing) — oncology-leaning, precision-diagnosis focus.

Positioning: quality-driven, technology-enabled, fast turnaround, responsive clinician
support; future roadmap includes **digital pathology** and advanced molecular testing.
So the site leads with **diagnostic capability, quality/TAT, and clinician trust** — not
consumer/price messaging. (Reference labs to study: CORE Diagnostics Gurugram, Oncquest,
Unipath, MedGenome; global — NeoGenomics, Foundation Medicine, Aiforia.)

**Website:** `https://[DOMAIN]` (client buying a new domain + email on GoDaddy)
**Type:** Static HTML/CSS/JS — no framework, no build tool, no npm. **Built fresh.**
**Hosted on:** GoDaddy (files uploaded via File Manager as a ZIP into `public_html/`)
**Stack:** Vanilla HTML5 · Vanilla CSS (`css/style.css`) · Vanilla JS (`js/main.js`) ·
rule-based chatbot (`js/chatbot.js` + `data/chatbot-rules.js`) · Google Fonts

**Tone:** Clinical · Precise · Trustworthy · Modern. Institutional lab voice
("At PATHMOLE Expert…"), not a personal voice. Credible for referring doctors first,
reassuring for patients second.

**Two hard rules for this project:**
1. **No pricing** anywhere — not on any page, not in the chatbot. Pricing questions are
   always redirected to the lab's contact flow (call / WhatsApp / enquiry).
2. **Case studies are always de-identified** (DPDP Act, 2023) — no patient name, ID,
   photo, or re-identifying detail.

---

## Site Architecture (Hybrid: lean funnel homepage + dedicated pages)

The **homepage is a clean, concise funnel** — each section moves the visitor one step
toward the two CTAs. Everything heavier lives on its own page.

```
/
├── index.html                  ← Home (lean funnel — see Section Map)
├── about.html                  ← About the Lab (founders, vision, quality philosophy)
├── services.html               ← Services (Histopathology & Molecular Diagnostics)
├── tests.html                  ← Test list + info (symptoms, details, contact-for-clarity)
├── quality.html                ← Quality & Accreditation (NABL/CAP, SOPs, TAT)
├── physicians.html             ← Physicians / Team
├── publications.html           ← Research & Publications
├── gallery.html                ← Gallery (facility + equipment/machines + info)
├── videos.html                 ← YouTube video section
├── patients.html               ← Patient info + downloadable Patient Form (PDF)
├── faq.html                    ← FAQ
├── careers.html                ← Careers / openings
├── contact.html                ← Contact (Google Maps location(s), enquiry form, details)
├── 404.html                    ← Custom 404
│
├── case-studies/
│   ├── index.html              ← Case-study listing (feeds the doctor newsletter)
│   └── [slug].html             ← Individual de-identified case study
│
├── css/style.css               ← Single global stylesheet (:root variables)
├── js/
│   ├── main.js                 ← Nav, mobile menu, scroll, reveal, enquiry form, back-to-top
│   └── chatbot.js              ← Rule-based chatbot engine (floating, all pages)
├── data/
│   ├── tests.js                ← Test list data (name, category, symptoms, info) — NO prices
│   └── chatbot-rules.js        ← Editable chatbot Q&A / quick replies
├── assets/                     ← Images (WebP), favicon, patient-form PDF
├── robots.txt · sitemap.xml · .htaccess
```

> **Reports Login** is NOT a page we build — it is a **top-of-site** button that links out
> (new tab) to the lab's existing third-party Reporting Portal (OTP login).

---

## Home (index.html) — Funnel Section Map

Keep it lean. This is the whole homepage, top to bottom:

| # | Section | ID / Class | Purpose |
|---|---|---|---|
| — | Top bar | `.top-bar` | Phone · Hours · Call Now · WhatsApp · **Reports Login ↗** |
| — | Nav | `.site-nav` | Logo + links + mobile menu |
| 1 | Hero | `.hero` | Headline + one-line mission + **dual CTA** (Enquiry / Call·WhatsApp) |
| 2 | Trust bar | `.trust-bar` | Accreditations / key numbers strip |
| 3 | Services | `.services` | A few cards → services.html / tests.html |
| 4 | Why Choose Us | `#why` | 3–4 short highlights (accuracy, TAT, accreditation) |
| 5 | Case Studies teaser | `#case-studies` | Latest de-identified case studies → case-studies/ |
| 6 | Final CTA | `#cta` | **[Submit Enquiry]  [Call / WhatsApp]** side by side |
| — | Footer | `.site-footer` | Links + social + copyright |
| — | Chatbot | `.chatbot` | Floating widget (all pages) |

> Nothing else goes on the homepage. About, Quality, Gallery, Videos, Patients, FAQ,
> Testimonials, Careers, Physicians each live on their own page.

---

## The Two CTAs (used in Hero and Final CTA)

Always side by side. Enquiry scrolls to / opens the enquiry form; the second is call+WhatsApp.

```html
<div class="cta-pair">
  <a href="contact.html#enquiry" class="btn-primary">Submit Enquiry</a>
  <a href="https://wa.me/[WHATSAPP]" target="_blank" rel="noopener noreferrer" class="btn-secondary">Call / WhatsApp</a>
</div>
```

---

## Styling & Colours — LOCKED (PathMole brand: navy + magenta)

> Palette is finalised from the **official letterhead** — full brand kit in **`brand-assets.md`**;
> structure/polish direction in **`design-reference-aiforia.md`** (reference: aiforia.com).
> Rules: never hardcode colours/fonts (variables only); mobile-first; **WCAG AA** contrast.

**Brand:** navy `#232C8E` (headings/structure) + magenta `#EC008C` (accent/CTAs), on white with a
cool soft-grey alt background. Polished, Aiforia-like, whitespace-heavy, card-and-grid layout.
Signature motif = **angular navy→magenta chevron bands** + faint microscope/DNA watermark.

```css
:root {
  /* BRAND — PathMole letterhead (confirm exact hex from logo vector) */
  --brand-navy:      #232C8E;   /* headings, nav, bands */
  --brand-navy-deep: #1A2270;
  --brand-pink:      #EC008C;   /* accent, CTAs, links */
  --brand-pink-deep: #C1006F;

  /* INK / SURFACES */
  --ink-900: #14202B;   --ink-600: #3B4A57;   --ink-400: #7A8894;
  --surface: #FFFFFF;   --bg-soft: #F5F7FB;

  /* SEMANTIC aliases — use these in components */
  --accent: var(--brand-pink);   --accent-deep: var(--brand-pink-deep);
  --heading: var(--brand-navy);

  /* FONTS */
  --font-heading: 'Poppins', 'Segoe UI', sans-serif;
  --font-body:    'Inter', Arial, sans-serif;

  /* SPACING / RADIUS */
  --radius: 12px;   --maxw: 1160px;
}
```
> Accessibility: navy is safe for text on white; use magenta as **button fill with white text** and for
> accents/links — avoid magenta for small body text on white (borderline AA). Verify every combo.

---

## Standard Head Block (every page)

> Replace GA4 ID with the client's. Update per-page title/description/canonical/og.
> Inner-folder pages (case-studies/*) add `../` to asset paths.

```html
<head>
  <meta charset="UTF-8" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXX');
  </script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="PAGE DESCRIPTION HERE" />
  <link rel="canonical" href="https://[DOMAIN]/PAGE-SLUG.html" />
  <meta property="og:title" content="PAGE TITLE — PATHMOLE Expert" />
  <meta property="og:description" content="PAGE DESCRIPTION HERE" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="assets/og-cover.webp" />
  <title>PAGE TITLE — PATHMOLE Expert</title>
  <link rel="icon" href="assets/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'" />
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet" /></noscript>
  <link rel="stylesheet" href="css/style.css" />
</head>
```

---

## Standard Top Bar + Nav (every page) — Reports Login at the TOP

```html
<div class="top-bar">
  <div class="container top-bar-inner">
    <span class="top-bar-item">📞 <a href="tel:[PHONE]">[PHONE]</a></span>
    <span class="top-bar-item">🕒 [WORKING HOURS]</span>
    <div class="top-bar-actions">
      <a class="top-bar-cta" href="tel:[PHONE]">Call Now</a>
      <a class="top-bar-cta wa" href="https://wa.me/[WHATSAPP]" target="_blank" rel="noopener noreferrer">WhatsApp</a>
      <a class="top-bar-reports" href="[REPORTING_PORTAL_URL]" target="_blank" rel="noopener noreferrer">Reports Login ↗</a>
    </div>
  </div>
</div>

<nav class="site-nav">
  <div class="container nav-inner">
    <a href="index.html" class="nav-logo"><img src="assets/logo.svg" alt="PATHMOLE Expert" /></a>
    <ul class="nav-links">
      <li><a href="index.html" data-nav-link>HOME</a></li>
      <li><a href="about.html" data-nav-link>ABOUT</a></li>
      <li><a href="services.html" data-nav-link>SERVICES</a></li>
      <li><a href="tests.html" data-nav-link>TESTS</a></li>
      <li><a href="case-studies/" data-nav-link>CASE STUDIES</a></li>
      <li><a href="publications.html" data-nav-link>RESEARCH</a></li>
      <li><a href="contact.html" data-nav-link>CONTACT</a></li>
    </ul>
    <button id="menu-toggle" class="menu-toggle" aria-label="Toggle navigation menu">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" /></svg>
    </button>
  </div>
  <div id="mobile-menu" class="mobile-menu">
    <ul>
      <li><a href="index.html">HOME</a></li>
      <li><a href="about.html">ABOUT</a></li>
      <li><a href="services.html">SERVICES</a></li>
      <li><a href="tests.html">TESTS</a></li>
      <li><a href="gallery.html">GALLERY</a></li>
      <li><a href="videos.html">VIDEOS</a></li>
      <li><a href="case-studies/">CASE STUDIES</a></li>
      <li><a href="publications.html">RESEARCH</a></li>
      <li><a href="patients.html">PATIENTS</a></li>
      <li><a href="physicians.html">PHYSICIANS</a></li>
      <li><a href="faq.html">FAQ</a></li>
      <li><a href="careers.html">CAREERS</a></li>
      <li><a href="contact.html">CONTACT</a></li>
      <li><a href="[REPORTING_PORTAL_URL]" target="_blank" rel="noopener noreferrer">REPORTS LOGIN ↗</a></li>
    </ul>
  </div>
</nav>
```
> Add `class="active"` to the current page's link. Inner-folder pages use `../`.

---

## Standard Footer + Chatbot Mount (every page)

```html
<footer class="site-footer">
  <div class="container footer-inner">
    <p class="footer-copy">&copy; 2026 PATHMOLE Expert</p>
    <div class="footer-links">
      <a href="[FACEBOOK]" target="_blank" rel="noopener noreferrer">Facebook</a>
      <a href="[INSTAGRAM]" target="_blank" rel="noopener noreferrer">Instagram</a>
      <a href="[LINKEDIN]" target="_blank" rel="noopener noreferrer">LinkedIn</a>
    </div>
  </div>
</footer>

<div class="dev-credit">
  <a href="https://mail.google.com/mail/?view=cm&fs=1&to=krishna191217@gmail.com&su=Web%20Development%20Enquiry" target="_blank" rel="noopener noreferrer">Designed &amp; built by <strong>Krishna Singh</strong> &middot; Get in touch &rarr;</a>
</div>

<button id="back-to-top" class="back-to-top" aria-label="Back to top">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 15.75l7.5-7.5 7.5 7.5" /></svg>
</button>

<!-- Floating chatbot (all pages) -->
<div id="chatbot" class="chatbot" aria-live="polite"></div>

<script src="js/main.js" defer></script>
<script src="data/chatbot-rules.js" defer></script>
<script src="js/chatbot.js" defer></script>
```

---

## Feature: Tests Page (`tests.html`) — info only, NO prices

A page listing all tests with helpful context. Each test entry has:
- **Name** + category (Histopathology / Molecular / Cytology / IHC …)
- **What it's for** / associated **symptoms or indications**
- **Other info** (sample type, prep, turnaround — if the client provides it)
- A clear line: *"For more details, please contact us at [PHONE] / WhatsApp."*
- **No price.**

Test data lives in **`data/tests.js`** (non-devs edit here; note there is NO price field):
```js
const TESTS = [
  {
    slug: "histopathology-biopsy",
    name: "Histopathology — Biopsy",
    category: "Histopathology",
    symptoms: ["Lump / swelling", "Suspicious lesion", "Post-surgical specimen"],
    info: "Microscopic examination of tissue to diagnose disease."
  },
  // ...add tests here — NO pricing
];
```
A page-wide note and a contact block sit at the bottom: *"Pricing and specific queries —
contact the lab."* → Call / WhatsApp buttons.

---

## Feature: Rule-Based Chatbot (floating, all pages) — the test-finder

**Role:** guide users to the right test or info with a **concise answer**, then **redirect
to the relevant page** for more detail. It is the ONLY "find a test" tool (no search box).

**Behaviour rules:**
- **Find a test:** user describes a symptom/test → bot gives a short answer and a button to
  the matching entry on `tests.html`.
- **Pricing:** bot NEVER gives a price. It replies with a short line and routes to the
  **contact flow**: e.g. *"For pricing, please contact the lab."* + **Call / WhatsApp** buttons.
- **Other info** (timings, location, services, reports login, careers): concise answer +
  link to the relevant page.
- **Fallback** (no match): direct to WhatsApp / phone.

Engine in `js/chatbot.js`; **all Q&A in `data/chatbot-rules.js`** (non-devs edit here):
```js
{
  id: "find-test",
  label: "Find a test",
  keywords: ["test", "biopsy", "thyroid", "symptom", "which test"],
  answer: "Tell me the symptom or test name and I'll point you to the right page.",
  action: { type: "link", href: "tests.html", text: "Browse all tests" }
},
{
  id: "pricing",
  label: "Pricing",
  keywords: ["price", "cost", "charges", "fees", "rate", "how much"],
  answer: "We share pricing directly. Please contact the lab and we'll help you.",
  action: { type: "contact" }   // renders Call / WhatsApp buttons
}
```
Keep a **fallback** rule. Keywords lowercase, specific, matched case-insensitively.

---

## Feature: Case Studies → Doctor Newsletter

Case studies are the site's "blog" AND the source of the doctor email newsletter.

**Hard gate (DPDP Act, 2023):** every case study is **fully de-identified** — no patient
name, ID, photo, or re-identifying detail; each carries a short disclaimer.

**Add a case study:**
1. Duplicate an existing `case-studies/[slug].html`; rename to the new slug.
2. Update head (title/description/canonical/og). Write de-identified content: title,
   clinical summary, findings, teaching point, disclaimer.
3. Add a card at the TOP of `case-studies/index.html` (newest first).
4. Add the URL to `sitemap.xml`; upload to GoDaddy.
5. **Newsletter:** in the email tool (Zoho Campaigns / Brevo free), duplicate the template,
   add a teaser + "Read the full case study" button linking to the new page, send to the
   "Referring Doctors" list. Unsubscribe link required and automatic. (See `PLAN.md §8`.)

---

## Feature: Patients Page + Patient Form (download only)

- `patients.html` gives patient-facing info and a **downloadable PDF** form filled offline:
```html
<a href="assets/pathmole-patient-form.pdf" download class="btn-primary">Download Patient Form (PDF)</a>
```
- **No online submission or storage of patient data** — keeps the site static and clear of
  DPDP data-handling. The enquiry form (contact.html) only emails the lab; no health records stored.

---

## Feature: Contact Page + Google Maps Location(s)

- `contact.html`: enquiry form (emails the lab — e.g. Formspree/Web3Forms), phone, WhatsApp,
  address, working hours.
- **Google Maps embed** for the lab location(s). **Client will send the maps link later** — until
  then render a **static map-card placeholder** (address + "Map coming soon" + a "Get directions"
  button linking to a Google Maps search of the address), NOT a broken/empty iframe. Swap in the real
  embed when provided:
```html
<!-- Placeholder until [GOOGLE_MAPS_EMBED_URL] is provided -->
<div class="map-card">
  <div class="map-card-body">
    <strong>PathMole Expert Lab</strong>
    <p>Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road,<br>
       Opposite Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana)</p>
    <a class="btn-secondary" target="_blank" rel="noopener noreferrer"
       href="https://www.google.com/maps/search/?api=1&query=PathMole+Expert+Lab+Sector+6+Gurugram">Get directions ↗</a>
  </div>
</div>
<!-- Real embed (swap in later):
<div class="map-embed"><iframe src="[GOOGLE_MAPS_EMBED_URL]" loading="lazy" title="PathMole Expert Lab"></iframe></div>
-->
```
- Enquiry form target: `[Formspree/Web3Forms endpoint]` (front-end only, no backend).

---

## SEO Rules (Crawl → Index → Rank)

Every page: unique `<title>` (`Topic — PATHMOLE Expert`), unique `<meta description>`,
`<link rel="canonical">`, exactly one `<h1>`, proper `<h2>/<h3>`, descriptive `alt` on images.
- Add every page (incl. each case study) to `sitemap.xml`; keep `robots.txt` open to Googlebot;
  submit sitemap in Search Console once.
- Target keywords: `pathology lab [city]`, `histopathology [city]`, `molecular diagnostics India`,
  `IHC test`, `cytology test`, `NABL accredited lab`, `[city] diagnostic laboratory`.
- Mobile-first, WebP + lazy-load, substantive content.

---

## Deploy to GoDaddy

1. ZIP the updated files. 2. GoDaddy → Hosting → File Manager → `public_html/`.
3. Upload ZIP → Extract (files land directly in `public_html/`).
4. Always upload: changed HTML, `css/style.css`, `js/*.js`, `data/*.js` (if catalog/chatbot
   changed), new images, `sitemap.xml` (if pages added).

---

## Things to NEVER Do

- Never show a **price** anywhere (site or chatbot) — always redirect pricing to the contact flow.
- Never publish a case study (site or email) that isn't **fully de-identified** (DPDP).
- Never invent tests, symptoms, accreditations (NABL/CAP), or contact details — use placeholders.
- Never store patient health data on the site (Patient Form is download-only).
- Never build/replace the third-party Reporting Portal — only link out to it (top of site).
- Never overload the homepage — it stays a lean funnel; heavy content goes to its own page.
- Never hardcode colours/fonts — variables only (finalized from client references).
- Never add a framework, npm package, or build step. Never use PNG/JPG — always WebP.
- Never ship with `PLACEHOLDER`/`TODO` remaining — clear before launch.
