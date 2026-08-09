# PATHMOLE Expert — Project Plan

> Website for a specialist Histopathology & Molecular Diagnostics **referral lab**.
> **Status:** Structure locked · Styling pending client references · **Last updated:** 2026-08-07
> Build source of truth: **`PATHMOLE-WEBSITE-GUIDE.md`** (this PLAN is the higher-level context).

---

## 1. Project Overview

**Client / Brand:** PATHMOLE Expert — a new **Histopathology & Molecular Biology
laboratory** in **Gurugram, Haryana (Delhi NCR)**. Principals: **Dr. Arpan Gandhi**
(~3 decades in pathology, laboratory medicine, quality systems) and **Mr. Ashok Yadav**
(20+ years in diagnostic laboratory operations).

**What kind of lab this is (important — shapes the whole site):**
- Mostly a **specialist referral facility** — roughly **90% B2B / 10% B2C**. The primary
  audience is **referring clinicians, hospitals, and diagnostic centres** across Gurugram
  and Delhi NCR; a ~10% minority are **direct walk-in patients**, so patient-facing pages
  (Patients + downloadable form, reassurance content) still carry real weight — just not the lead.
- Brings **two complementary disciplines onto one platform**:
  - **Histopathology** — *"What does the disease look like?"* (tissue morphology, biopsy,
    cytology, immunohistochemistry / IHC).
  - **Molecular Diagnostics** — *"What is driving it?"* (molecular / mutation panels,
    PCR/FISH-type testing) — oncology-leaning, precision-diagnosis focus.
- Positioned as **quality-driven, technology-enabled, fast turnaround, responsive
  clinician support**. Future roadmap: **digital pathology** and advanced molecular testing.
- **Launch: 17 Aug 2026.**

**Goal:** A modern, credibility-first website that (a) earns the trust of referring
doctors, (b) makes it easy to enquire / refer / contact, and (c) powers a **de-identified
doctor case-study newsletter**. Content comes from the client; we build structure + placeholders.

**Key decisions (locked):**
| Decision | Choice |
|---|---|
| Structure | **Hybrid** — lean **funnel homepage** + dedicated pages for everything heavier |
| Tech stack | **Static HTML / CSS / vanilla JS** — no framework, no build step, no npm |
| Hosting | **GoDaddy** (File Manager → ZIP into `public_html/`) |
| Codebase | **Built fresh** with a **new clinical lab identity** |
| Styling / palette | **PENDING** the client's reference-site links (kept in `:root` variables) |
| Pricing | **NO pricing anywhere** (site or chatbot) — always redirected to the contact flow |
| Test-finder | The **rule-based chatbot** is the ONLY test-finder (no search box) |
| Reports Login | **Top-of-site** button → links out to the third-party Reporting Portal |
| Case studies | Always **de-identified** (DPDP Act 2023); feed the doctor newsletter |
| Patient Form | **Download-only PDF** — no online storage of patient data |

**Non-goals (v1):**
- No backend / database / server-side code (enquiry form emails the lab via Formspree/Web3Forms).
- No AI / LLM chatbot — rules only.
- No CMS — content edited directly in HTML.
- We do **not** build or replace the third-party Reporting Portal — we only link to it.

---

## 2. Tech & Hosting

- **HTML5 + CSS3 + Vanilla JavaScript** — no framework, no build tools.
- **Fonts:** Google Fonts (finalized once client references arrive).
- **Icons:** inline SVG (no icon library dependency).
- **Hosting:** **GoDaddy** shared hosting (`public_html/`), client's new domain + email.
- **Responsive:** mobile-first, works down to ~320px width.
- **Accessibility:** semantic HTML, alt text, keyboard-navigable chatbot, WCAG AA contrast.
- **Images:** WebP + lazy-load. **SEO:** canonical, sitemap, GA4, unique title/description per page.

---

## 3. File & Folder Structure

Repo root is reserved for the **website build**; project docs live in `docs/`, commercial
paperwork in `contract/`. Full site tree is in `PATHMOLE-WEBSITE-GUIDE.md`.

```
PATHMOLE Website proejct/
├── docs/
│   ├── PATHMOLE-WEBSITE-GUIDE.md        # BUILD source of truth (structure + code blocks)
│   ├── PLAN.md                          # This file — high-level context & decisions
│   ├── TASKS.md                         # Progress checklist
│   ├── INSTRUCTIONS.md                  # Conventions / how to edit
│   └── reference-drarpangandhi-guide.md # Reference only (Dr. Arpan's personal-site guide)
├── contract/
│   ├── CONTRACT.md                      # Client agreement (markdown)
│   ├── PATHMOLE-Expert-Contract.docx    # Word version
│   └── make_contract_docx.py            # Generator for the .docx
│
└── (website build — created fresh per the GUIDE:)
    index.html · about.html · services.html · tests.html · quality.html ·
    physicians.html · publications.html · gallery.html · videos.html ·
    patients.html · faq.html · careers.html · contact.html · 404.html ·
    case-studies/ · css/ · js/ · data/ · assets/ · robots.txt · sitemap.xml · .htaccess
```

---

## 4. Site Map (hybrid funnel)

**Homepage (`index.html`) — lean funnel only:**
Top bar (Phone · Hours · Call · WhatsApp · **Reports Login ↗**) → Nav → Hero + **dual CTA**
(Submit Enquiry / Call·WhatsApp) → Trust bar → Services → Why Choose Us → Case-Studies
teaser → Final CTA → Footer → floating Chatbot.

**Dedicated pages (everything heavier):** About the Lab · Services (Histopathology &
Molecular) · **Tests** (info only, no price) · Quality & Accreditation · Physicians/Team ·
Research & Publications · Gallery (facility + equipment) · Videos · Patients (+ PDF form) ·
FAQ · Careers · Contact (Google Maps location) · Case Studies (index + per-study).

> Positioning note: audience is ~90% **referring doctors** — lead with diagnostic
> capability, quality/TAT, and clinician support (not consumer/price messaging). But keep
> the ~10% **walk-in patients** served: clear Patients page, downloadable form, and
> reassuring, plain-language copy where patients will land.

---

## 5. Chatbot Design (rule-based — the test-finder)

**Type:** quick-reply menu buttons + free-text keyword matching. No AI, no API, no backend.
Floating on **all pages**.

- **Find a test:** user describes a symptom/test → short answer + button to the matching
  entry on `tests.html`. This is the ONLY test-finder (no search box).
- **Pricing:** bot NEVER gives a price → short line + **Call / WhatsApp** (contact flow).
- **Other info** (timings, location, services, reports login, careers) → concise answer + link.
- **Fallback:** direct to WhatsApp / phone.

Engine in `js/chatbot.js`; all Q&A in `data/chatbot-rules.js` (non-devs edit here).

---

## 6. Design / Branding

- **New clinical lab identity**, built fresh (not reused from Dr. Arpan's personal site).
- **Palette & fonts PENDING** the client's reference-site links. Until they arrive: neutral
  placeholder styling, all theme values in `:root` CSS variables so re-theming is one edit.
- **Feel:** clinical, precise, trustworthy, modern; institutional lab voice
  ("At PATHMOLE Expert…"), credible for doctors and reassuring for patients.
- **Reference labs to study** (specialist referral model, not consumer chains): CORE
  Diagnostics (Gurugram), Oncquest, Unipath, iGenetic, MedGenome; global: NeoGenomics,
  Foundation Medicine, Caris, Tempus, Aiforia (digital pathology).

---

## 7. Build Phases

- **Phase 0 — Planning & docs** *(done)*: PLAN, TASKS, INSTRUCTIONS, WEBSITE-GUIDE, contract.
- **Phase 0.5 — Styling references** *(current blocker)*: receive client's reference links,
  finalize palette/fonts section of the GUIDE.
- **Phase 1 — Structure:** all HTML pages with placeholder content (per the GUIDE).
- **Phase 2 — Styling:** `css/style.css`, responsive + themed from references.
- **Phase 3 — Interactivity:** `js/main.js` (nav, scroll, reveal, enquiry form, back-to-top).
- **Phase 4 — Chatbot:** `js/chatbot.js` + `data/chatbot-rules.js` (test-finder).
- **Phase 5 — Content pass:** swap placeholders for client copy, tests data, images.
- **Phase 6 — Polish & QA:** responsive, a11y, cross-browser, SEO meta, performance.
- **Phase 7 — Deploy:** ZIP → GoDaddy `public_html/`; submit sitemap in Search Console.

---

## 8. Feature: Doctor Case-Study Newsletter

**What it is:** broadcast **de-identified** case studies to the lab's **referring doctors**
— keeping them engaged with interesting cases run at the lab. Case studies go **live on the
website** *and* out as an **email newsletter** linking back to the site. This is a core
engagement channel given the B2B/referral model.

**Confirmed scope & decisions:**
| Item | Decision |
|---|---|
| Audience | ~**150 referring doctors** (emails from the client's one-time CSV) |
| Channel (v1) | **Email only** (WhatsApp/SMS deferred) |
| Where content lives | **Public Case Studies section** + email that links to it |
| Region | **India** → **DPDP Act 2023** + medical de-identification |
| Timeframe | First sends within the launch window (deadline **17 Aug 2026**) |

### 8.1 Critical rule — privacy
Every case study is **de-identified**: no patient name, ID, photo, or re-identifying detail;
each carries a short disclaimer. This is a **legal/ethical gate**, not optional.

### 8.2 v1 vs v2 (decoupled from the third-party portal)
The existing OTP login + report portal was built by a **third party**; getting access needs
a vendor call. **Do not block the deadline on that integration.**
- **v1 (by 17 Aug):** Public case-study pages + free email tool. Doctor list = **one-time CSV**.
- **v2 (after the call):** auto-sync the doctor list; optionally gate case studies behind OTP.

### 8.3 Email architecture & tooling (₹0/month)
- **One inbox + up to 4 addresses** via **Zoho Mail** free (1 mailbox + free aliases, all
  land in one inbox), single platform.
- **Bulk sending** via **Zoho Campaigns** free (3 campaigns/mo, 2,000 contacts, 6,000
  emails/mo) OR **Brevo** free (300 emails/day, unlimited campaigns, adds a footer). 150
  doctors is well within limits.
- **Deliverability (free, essential):** configure **SPF / DKIM / DMARC** DNS records.

### 8.4 Cost — free vs paid (India)
| Item | Free / Paid | Cost |
|---|---|---|
| Website build + GoDaddy hosting | Included / client's plan | — |
| Case-study section + chatbot (static) | **Free** | ₹0 |
| Mailboxes/aliases (Zoho Mail free) | **Free** | ₹0 |
| Email campaign tool (Zoho Campaigns / Brevo free) | **Free** for 150 doctors | ₹0 |
| **Domain name** (client buys — GoDaddy) | **Paid** | ₹500–1,300/yr |
| Third-party OTP-system API (v2) | **Paid** (vendor) | TBD on call |

---

## 9. Commercial (agreed)

Total **₹26,000** · **₹7,000** advance (received, non-refundable) · **₹19,000** balance
before go-live · **₹2,000/month** optional maintenance. Post-launch: bugs free for 14 days,
then a ₹1,000 charge, then covered by maintenance. Full terms in `contract/CONTRACT.md`
(+ `PATHMOLE-Expert-Contract.docx`). Two clients: **Dr. Arpan Gandhi & Mr. Ashok Yadav**.

> Note: the signed contract lists the second client as "Dr. Ashok"; the lab blogs name him
> "Mr. Ashok Yadav". Confirm the correct name/title before final signing.

---

## 10. Open Questions (need client input)

**Answered:**
- [x] Lab type & disciplines → specialist Histopathology + Molecular referral lab, Gurugram
- [x] Structure → hybrid funnel; stack → static HTML/CSS/JS on GoDaddy
- [x] No pricing anywhere; chatbot is the test-finder; Reports Login at top
- [x] Newsletter scope → ~150 doctors, email only; email stack = Zoho (₹0)
- [x] Client is buying the **domain + email** (GoDaddy)

**Still needed:**
- [ ] **Styling reference website links** (blocks palette/fonts finalization) — *in progress*
- [ ] Logo, brand colours, brand guidelines
- [ ] Tests list (names, categories, symptoms/indications, sample/prep — **no prices**)
- [ ] Content for About, Services, Quality, Publications, Physicians
- [ ] Photos for Gallery (facility + equipment) and YouTube video links
- [ ] Referring-doctor list (name + email) for the newsletter (CSV)
- [ ] The downloadable Patient Form (PDF)
- [ ] Contact details, working hours, Google Maps location(s), social links
- [ ] Reporting Portal URL (for the top-of-site Reports Login link)
- [ ] Confirm second client's correct name/title (Dr. Ashok vs Mr. Ashok Yadav)
- [ ] Schedule the third-party vendor call for v2 integration
