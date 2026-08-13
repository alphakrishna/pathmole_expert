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

---

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
- **Awaiting from client:** vector logo, domain, real photos/videos, full tests list,
  Patient Form PDF, Google Maps embed link, Reporting Portal URL, form endpoint,
  GA4 ID, trust numbers, testimonials, accreditations, case studies.
- **QUESTION FOR CLIENT — Dr. Ashok Yadav leadership card:** the client's content doc
  named only Dr. Arpan Gandhi, but the contract names two principals — likely the client
  forgot to include Dr. Ashok Yadav's details. A **placeholder** leadership card for him
  has been added to `about.html` and `physicians.html`. **Ask the client:** (a) should he
  appear on the site? (b) confirmed name spelling & title/designation, (c) short bio
  (expertise, years of experience, role). Fill or remove the placeholder once confirmed.
- Raw 4K hero source (`video/`) must be **excluded** from the public repo / live upload —
  ship only `assets/hero.mp4` + `assets/hero-poster.jpg`.
- Do **not** build/replace the third-party Reporting Portal — link out only.
- Leadership on site = Dr. Arpan Gandhi confirmed; **Dr. Ashok Yadav card added as a
  PLACEHOLDER pending client confirmation** (see question above).
