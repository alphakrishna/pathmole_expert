# PATHMOLE Expert — Task Checklist

> Track progress here. Mark `[x]` when done. See **PLAN.md** for context and
> **PATHMOLE-WEBSITE-GUIDE.md** for how to build each item.
> **Last updated:** 2026-08-13 · Hybrid multi-page site · specialist referral lab
> **Status:** v1 built & client text content integrated. Hero background video added.
> Site-wide styling consistency pass done (all interior pages now match the landing page:
> unified gradient icon tiles, eyebrow + two-tone section heads, closing CTA bands).
> Latest pass: chatbot upgraded (new rules + enquiry-form redirect + chat history that
> persists across page navigation and clears only on full reload; launcher restyled to the
> PathMole brand tile), and the top bar + nav polished (gradient strip, frosted sticky nav
> that shrinks on scroll, gradient link underline).
> Remaining work is mostly client-supplied assets (logo, real photos, PDF, endpoints).
>
> **NEW SCOPE (client change requests, 2026-08-14):** see the dedicated section below —
> per-topic educational "learn" pages, a Training Institute service + form, merging
> Case Studies with Research into one page, a new "Partner With Us" page + form,
> illustrations/stock imagery site-wide, and real leadership photos.

---

## Client Change Requests — 2026-08-14 (NEW SCOPE)
> Requested by the client on 14 Aug 2026. Content + assets for the new pages/forms will be
> supplied by the client (tracked in **PATHMOLE-Content-Request.md**). No invented tests,
> claims, prices or accreditations — bracketed placeholders until confirmed.

- [~] **Educational "learn about this" content lives on the LANDING CARDS — service pages stay LEAN.**
  DECISION (2026-08-16, supersedes the original "add explainers to each sub-page"): the beginner +
  intermediate "what is it" guide belongs on the EXPANDED landing "What We Do" cards. The service
  sub-pages must NOT re-explain the topics — each gets a SHORT "what it is" line then "what we
  offer", with no duplication of the landing cards or of each other.
    - DONE: trimmed `histopathology.html`, `cytopathology.html`, `molecular-diagnostics.html`
      (short intro → "What we offer") and de-duplicated the `services.html` hub (removed the
      specimen lists / workflow / molecular-application cards that repeated the sub-pages).
    - TODO: expand the landing "What We Do" cards (`index.html`) into a proper newbie + intermediate
      guide — draft plain-language copy for client approval; touches the landing-page layout.
- [~] **Training Institute service + form.** Page BUILT (`training-institute.html`) from the
  client's copy, placed at the TOP of the Services page, and linked in the footer + mobile
  menu. Uses "PATHMOLE EXPERT LLP" per client. STILL PENDING: the registration form — client
  to supply the Google Form (embed) or its field list (native form); a bracketed placeholder
  sits on the page. Not yet added to the crowded desktop top-nav (surfaced via Services + footer).
- [x] **Merge Case Studies + Research into ONE page.** DONE (2026-08-16): the Research
  content now lives as a second section ("Research & References", soft-grey) on
  `case-studies/index.html`, retitled **"Case Studies & Research"** (H1, breadcrumb, nav,
  footer, mobile menu, chatbot rule + keywords all updated). `publications.html` retired to
  a meta-refresh + JS redirect stub → `case-studies/` (noindex) so old bookmarks/newsletter
  links still land correctly; removed from NAV/footer. De-identification (DPDP) rules unchanged.
- [x] **New "Partner With Us" page + form.** DONE (2026-08-16): built `partner.html` from the
  client's supplied copy (intro, "We can partner with" list, 4 "What we offer" cards, and the
  full partnership enquiry form as a NATIVE styled form — text fields + `<select>` dropdowns for
  partner type / services / monthly volume / mode / preferred contact, `id="enquiry-form"` so the
  existing `js/main.js` validation + friendly no-endpoint message applies). Uses "PATHMOLE EXPERT
  LLP" per client. Added to desktop nav, mobile menu, footer (Explore) and a new chatbot
  `partner` rule. Form still needs a live submit endpoint (same Web3Forms/Formspree gap as the
  contact form). NO pricing anywhere.
- [ ] **Illustrations + stock imagery site-wide.** Add illustrations and licensed stock
  images everywhere visuals are needed (section art, per-topic explainers, empty
  placeholder tiles). Royalty-free/licensed sources only; keep brand palette; swap for real
  lab photos once supplied.
- [x] **Leadership photos + bios.** DONE (2026-08-16): both leadership cards (About +
  Physicians) rebuilt as premium profile blocks — circular headshot, 4 credential chips,
  one-line intro + 4 heavy highlights each, balanced in weight.
    - Dr. Ashok Yadav: confirmed name/title/bio + headshot integrated (`assets/dr-ashok-yadav.jpg`).
    - Dr. Arpan Gandhi: card rewritten from his profile (`docs/Dr-Arpan-Gandhi-Profile.md` — kept
      private in docs/) with real specializations (ocular pathology, oncology, CAP/NABL, 200+
      mentored); real photo cropped to a head-and-shoulders square (`assets/dr-arpan-gandhi.jpg`).
    - REVIEW-WITH-CLIENT: Yadav's "built and led a leading North-India lab" is the de-named
      version of the client's "Micro Path Labs, Gurugram" line (another lab entity on the
      PathMole site). Confirm whether to name it. Gandhi's CAP/NABL/200+ claims are from his
      public site — worth a quick client confirm before go-live.
- [ ] **Full test list.** Client to provide the final confirmed test list → `data/tests.js`
  (replaces the 15 samples). Still NO pricing anywhere.

---

## ⚑ DO TOMORROW — 2026-08-21
> **Activate the enquiry forms.** Contact / Partner / Training forms are fully wired to
> **Web3Forms** but delivery is OFF until the access key is pasted.
> 1. Create a free key at **web3forms.com** using **pathmolelab@gmail.com** (key arrives by email).
> 2. Paste it into `js/main.js` → `const WEB3FORMS_ACCESS_KEY = "…"` (marked with a ⚑ TODO).
> Then submit a live test from each of the 3 forms and confirm the email lands.
> _(Alternative if preferred: Formspree or an embedded Google Form.)_

## ✅ CONTENT & DESIGN LOCKED — 2026-08-20
> Client signed off. **All REVIEW-WITH-CLIENT flags below are RESOLVED = keep as currently
> implemented.** Do NOT re-open them. Confirmed final:
> - **Slides & Blocks**, **Fluid Cytology / LBC Pap Smear** (one line), cytology items stay under
>   **Histopathology**, dropped histopath placeholders (Surgical Resection / Frozen Section /
>   Special Stains) stay dropped.
> - **Flu Panel** kept as-is; **HLA-B27** stays in **Molecular Diagnostics**; oncology-molecular,
>   **IHC** and **FISH** groups stay **hidden** (commented out in `data/tests.js`).
> - **"PATHMOLE EXPERT LLP"** stays on the **Training Institute page only**.
> - Services order kept (Cytopathology + Specialised Diagnostic Support remain); **no** Training
>   Institute entry in the desktop top-nav (surfaced via Services + footer).
> - Dr. Ashok Yadav's prior lab kept **generic**; Dr. Arpan Gandhi's CAP/NABL/"200+ mentored"
>   credentials **cleared to publish**.
> - This session: **Reports Login URL** wired site-wide; **hours** → **8:00 AM – 8:00 PM**
>   everywhere; chatbot rewritten (active, menu-accurate, subdirectory links fixed).
>
> **STILL PENDING — client to supply 3 assets (only drop-in blockers):**
> - [ ] **Patient Form PDF** → `assets/pathmole-patient-form.pdf` (link live at `patients.html:88`)
> - [ ] **Lab photos** → 6 `Photo [PLACEHOLDER]` tiles in `gallery.html`
> - [ ] **Lab videos** → 2 `YouTube embed [PLACEHOLDER]` tiles in `videos.html`
>
> **Launch-infra still needing real values (not "content", handle at go-live):** form submit
> endpoint (Contact/Partner/Training still show "call us"), Training Institute registration form,
> social links + Google Maps embed (still `#`/placeholder), vector logo (PNG in use), domain +
> Zoho email, GA4 ID.

## Phase 0 — Planning & Docs
- [x] Confirm lab type (specialist Histopathology + Molecular referral lab, Gurugram)
- [x] Confirm structure (hybrid funnel) + stack (static HTML/CSS/JS on GoDaddy)
- [x] Lock rules: no pricing anywhere · chatbot = test-finder · Reports Login at top
- [x] Write PLAN.md, TASKS.md, INSTRUCTIONS.md, PATHMOLE-WEBSITE-GUIDE.md
- [x] Draft client contract (CONTRACT.md + .docx)
- [x] Palette/fonts locked from official letterhead (navy #232C8E · magenta #EC008C; Poppins/Inter) — design reference aiforia.com
- [~] Collect client content — **text content received & integrated**; assets (logo, photos, PDF, tests list) still pending

## Phase 1 — HTML Structure (built fresh per the GUIDE)
Shared head / top bar + nav / footer + chatbot mount generated from `scripts/build_pages.py`.
- [x] `index.html` — lean funnel (hero + dual CTA → what-we-do → why → philosophy → case-studies teaser → final CTA)
- [x] `about.html` — About the Lab (story, quality, clinician-centric, technology, leadership)
- [x] `services.html` — Histopathology · Cytopathology · Molecular Diagnostics (hub; each section
  now has a "Learn more →" redirect to a dedicated sub-page)
- [x] Service sub-pages (one per landing "What we do" card): `histopathology.html`,
  `cytopathology.html`, `molecular-diagnostics.html`, `diagnostic-support.html`
  (breadcrumb Home / Services / X, SERVICES nav active; landing cards + footer link straight to them)
- [x] `tests.html` — test list + info (symptoms/indications) — **NO price** (15 sample tests)
- [x] `quality.html` — Quality & Patient Safety framework
- [x] `physicians.html` — Our Team & For Clinicians
- [x] `publications.html` — Research & References
- [x] `gallery.html` — facility + equipment (placeholder images)
- [x] `videos.html` — video section
- [x] `patients.html` — patient info + downloadable Patient Form (PDF placeholder)
- [x] `faq.html` — FAQ
- [x] `careers.html` — Careers
- [x] `contact.html` — enquiry form + Google Maps placeholder + details
- [x] `404.html` — custom 404
- [x] `case-studies/index.html` — listing + de-identified case-study template

## Phase 2 — Styling (`css/style.css`)
- [x] `:root` variables (colors, fonts, spacing, radius)
- [x] Base reset + typography
- [x] Top bar + nav + mobile menu (Reports Login at top)
- [x] Hero + dual CTA (`.cta-pair`), trust bar, section layouts
- [x] Hero background **video** (muted/autoplay/loop) + navy scrim overlay + reduced-motion fallback
- [x] Cards, buttons, forms, `.tick-list`
- [x] Chatbot floating widget styles + branded launcher (PathMole "P" logo tile with white
      contrast ring so it never blends into navy backgrounds; live status dot, hover tooltip)
- [x] Top bar + nav polish (gradient top strip, frosted/blurred sticky nav that shrinks on
      scroll, two-tone gradient link underline)
- [x] Responsive breakpoints + scroll-reveal

## Phase 3 — Site JS (`js/main.js`)
- [x] Mobile menu toggle + active nav link
- [x] Smooth scroll / sticky nav behavior
- [x] Scroll-reveal (IntersectionObserver)
- [~] Enquiry form validation done — **submit endpoint (Formspree/Web3Forms) not yet wired**
- [x] Back-to-top + auto footer year
- [x] Floating premium "Back" button (bottom-left navy pill, slides in past 300px scroll, goes to
      previous page with `data-home` fallback) on every interior page — homepage excluded by design

## Phase 4 — Chatbot (`js/chatbot.js` + `data/chatbot-rules.js`)
- [x] Rules: find-test (→ tests.html), pricing (→ contact flow), info, fallback
- [x] New rules: enquiry (→ `contact.html#enquiry` form redirect), quality (→ quality.html),
      turnaround/TAT (→ contact — no invented times); enquiry added to the quick-reply menu
- [x] Contact / pricing / fallback flows also surface a "Send enquiry" button (contact form)
- [x] Floating mount on ALL pages
- [x] Menu quick-replies + free-text keyword matching
- [x] Pricing NEVER shows a price — renders Call / WhatsApp
- [x] Keyboard accessible, auto-scroll, typing indicator
- [x] Chat history persists across page navigation (sessionStorage) and clears only on a
      full page reload (reload detected via Navigation Timing API); remembers open state
- [x] Branded launcher = PathMole "P" logo tile (matches top logo/favicon) with a white
      contrast ring so it stands out on any background

## Phase 4.5 — Tests Data (`data/tests.js`)
- [x] Schema: slug, name, category, symptoms[], info — **NO price field**
- [~] Populated with 15 sample tests — **awaiting client's full confirmed list**
- [x] "For more details, contact us" note + contact block

## Phase 5 — Doctor Case-Study Newsletter (see PLAN.md §8)
**Website side (v1):**
- [x] Case-studies listing + de-identified per-study template (summary, findings, teaching point, disclaimer)
- [x] Link from nav / homepage teaser
**Email side (v1):**
- [ ] Client buys domain (GoDaddy)
- [ ] Zoho Mail free — 1 mailbox + aliases
- [ ] Configure SPF / DKIM / DMARC DNS records
- [ ] Email campaign tool (Zoho Campaigns or Brevo — free tier)
- [ ] Import ~150 referring doctors from client CSV
- [ ] Branded newsletter template linking to the website case study
- [ ] Unsubscribe + de-identification disclaimer
- [ ] Test send, then first real send
**Compliance (v1):**
- [ ] Confirm DPDP-compliant de-identification of every case study
- [ ] Confirm unsubscribe works
**v2 (post-deadline OK):**
- [ ] Third-party vendor call for OTP-system access/API
- [ ] Auto-sync doctor list; optionally gate case studies behind OTP login

## Phase 6 — Content
- [x] Replace placeholder copy with client content (Home, About, Services, Quality, Physicians, Patients)
- [x] Hero background video optimized (HandBrake 4K→1080p, 3.5 MB) + poster frame → `assets/`
- [ ] Real logo (vector) + real WebP images (facility + equipment)
- [ ] Real contact details confirmed, hours, Google Maps embed, social links
- [ ] Reporting Portal URL wired into top-of-site Reports Login
- [ ] Patient Form PDF into `assets/`
- [ ] Trust numbers, testimonials, accreditations (only if confirmed)

## Phase 7 — Polish & QA
- [~] Responsive (320 / 768 / 1280) — built responsive, needs device pass
- [x] Site-wide styling consistency pass — every interior page brought up to the landing-page
  look: unified magenta→navy gradient icon tiles, centered eyebrow + two-tone `.text-pink`
  section heads, and the closing "Refer a case" CTA band added to faq/careers/contact/case-studies
- [ ] Accessibility (contrast, keyboard, alt, ARIA) — full audit
- [ ] Cross-browser (Chrome, Firefox, Safari, Edge)
- [ ] SEO: unique title/description, canonical, one h1, sitemap, robots.txt, GA4
- [ ] Performance (WebP, lazy-load, no console errors)
- [ ] No `PLACEHOLDER` / `TODO` remaining

## Phase 8 — Deploy
- [x] Preview deploy on GitHub Pages (staging)
- [ ] ZIP → GoDaddy File Manager → `public_html/` → extract
- [ ] Point domain, verify HTTPS
- [ ] Submit sitemap in Search Console
- [ ] Final review with client

---

### Legend
`[x]` done · `[~]` partial / in progress · `[ ]` not started

### Notes / Blockers
- **2026-08-20 — CONTENT & DESIGN LOCKED (see top of file).** REVIEW-WITH-CLIENT flags below are
  RESOLVED (keep as implemented). Full tests list, Reporting Portal URL and hours are now DONE.
- **Still awaiting from client — 3 drop-in assets:** Patient Form PDF
  (`assets/pathmole-patient-form.pdf`), real lab photos (gallery), lab videos (videos page).
- **Launch-infra still needing real values (go-live):** vector logo, domain + Zoho email,
  Google Maps embed, social links, enquiry/partner/training form endpoint, Training Institute
  registration form, GA4 ID, trust numbers/testimonials/accreditations (only if confirmed).
- **Awaiting from client (NEW SCOPE, 2026-08-14):** Training Institute content + its Google
  Form (or fields for a native form); Partner-With-Us page content + form fields;
  leadership photos of Dr. Arpan Gandhi and Dr. Ashok Yadav; approval of the plain-language
  per-topic educational copy we'll draft; decision on Google-Form embed vs native form for
  the Training Institute + Partner forms.
- **REVIEW-WITH-CLIENT flags (raise at the next content review):**
  - **Histopathology test list (client-supplied 2026-08-19)** — client sent: Small Biopsy,
    Medium Biopsy, Large Biopsy, Extra Large Biopsy, Second Opinion, Cell Block, "slides Block
    issues", "Floid Cytology Lb PAP smear test". Entered into `data/tests.js` under the
    **Histopathology** category with obvious typos fixed (Opinon→Opinion, Floid→Fluid, Lb→LBC).
    CONFIRM WITH CLIENT: (1) exact name/scope of **"Slides & Blocks"** (review of referred
    slides/blocks? recuts? issuing?); (2) whether **"Fluid Cytology / LBC Pap Smear"** is ONE
    item or TWO (Fluid Cytology + LBC Pap Smear); (3) whether the cytology items (Cell Block,
    Fluid/Pap) should move to a separate **Cytopathology** group (currently all under
    Histopathology per instruction); (4) whether the earlier placeholder histopath services
    (Surgical Resection, Frozen Section, Special Stains) were dropped intentionally — they were
    REPLACED by this list. NO prices anywhere (per standing rule).
  - **Molecular test list (client-supplied 2026-08-19)** — client sent: HBV, HCV, HIV, HLAB-27,
    FluPanel, HPV, TB. Entered into `data/tests.js` under **Molecular Diagnostics** with
    abbreviations expanded (HLAB-27→HLA-B27, FluPanel→Flu Panel). These REPLACED the earlier
    placeholder molecular-oncology entries (EGFR, KRAS/NRAS/BRAF, NGS solid-tumour, MSI).
    CONFIRM WITH CLIENT: (1) exact scope/method of **"Flu Panel"** (influenza only? full
    respiratory panel? PCR?); (2) HLA-B27 is a genetic marker (not infectious) — confirm it
    belongs in this molecular group; (3) whether the oncology molecular + IHC + FISH placeholder
    entries should stay or be dropped. NO prices anywhere.
  - **"PATHMOLE EXPERT LLP"** — the Training Institute copy introduces this legal entity, but
    the whole site is branded **"PathMole Expert Lab."** Confirm with the client what the LLP
    name is / where it should appear (e.g. footer legal line, TI page only). Currently used
    only inside the TI page body, as instructed.
  - **Services-page order** — client's stated order (TI → Histopathology → Molecular) omits
    **Cytopathology** and **Specialised Diagnostic Support**. Both were KEPT on the Services
    page (after Histopathology/Molecular). Confirm whether they stay, merge, or move.
  - **Training Institute in the desktop top-nav?** — left out to avoid crowding the 7-item bar;
    confirm if the client wants a dedicated top-nav entry.
- **Dr. Ashok Yadav leadership card — UPDATE (2026-08-14):** client now confirms he
  **appears** on the site (resolves the earlier "should he appear?" question). Placeholder
  cards on `about.html` + `physicians.html` stay until the client sends the **confirmed
  name spelling & title/designation, a short bio, and a photo**.
- Raw 4K hero source (`video/`) must be **excluded** from the public repo / live upload —
  ship only `assets/hero.mp4` + `assets/hero-poster.jpg`.
- Do **not** build/replace the third-party Reporting Portal — link out only.
- Leadership on site = Dr. Arpan Gandhi confirmed; **Dr. Ashok Yadav card added as a
  PLACEHOLDER pending client confirmation** (see question above).
