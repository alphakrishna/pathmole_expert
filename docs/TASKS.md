# PATHMOLE Expert — Task Checklist

> Track progress here. Mark `[x]` when done. See **PLAN.md** for context and
> **PATHMOLE-WEBSITE-GUIDE.md** for how to build each item.
> **Last updated:** 2026-08-07 · Hybrid multi-page site · specialist referral lab

---

## Phase 0 — Planning & Docs
- [x] Confirm lab type (specialist Histopathology + Molecular referral lab, Gurugram)
- [x] Confirm structure (hybrid funnel) + stack (static HTML/CSS/JS on GoDaddy)
- [x] Lock rules: no pricing anywhere · chatbot = test-finder · Reports Login at top
- [x] Write PLAN.md, TASKS.md, INSTRUCTIONS.md, PATHMOLE-WEBSITE-GUIDE.md
- [x] Draft client contract (CONTRACT.md + .docx)
- [ ] **Receive client's styling reference website links** *(current blocker)*
- [ ] Finalize palette/fonts in the GUIDE once references arrive
- [ ] Collect client content (see PLAN.md §10 — Still needed)

## Phase 1 — HTML Structure (build fresh per the GUIDE)
Shared blocks first (head / top bar + nav / footer + chatbot mount), then each page.
- [ ] `index.html` — lean funnel (hero + dual CTA → trust bar → services → why → case-studies teaser → final CTA)
- [ ] `about.html` — About the Lab (founders, vision, quality philosophy)
- [ ] `services.html` — Histopathology & Molecular Diagnostics
- [ ] `tests.html` — test list + info (symptoms/indications, details) — **NO price**
- [ ] `quality.html` — Quality & Accreditation (NABL/CAP goals, SOPs, TAT)
- [ ] `physicians.html` — Physicians / Team
- [ ] `publications.html` — Research & Publications
- [ ] `gallery.html` — facility + equipment/machines + info
- [ ] `videos.html` — YouTube section
- [ ] `patients.html` — patient info + downloadable Patient Form (PDF)
- [ ] `faq.html` — FAQ
- [ ] `careers.html` — Careers
- [ ] `contact.html` — enquiry form + Google Maps location(s) + details
- [ ] `404.html` — custom 404
- [ ] `case-studies/index.html` — listing (newest first)
- [ ] `case-studies/[slug].html` — de-identified case-study template

## Phase 2 — Styling (`css/style.css`)
- [ ] `:root` variables (colors, fonts, spacing, radius) — from client references
- [ ] Base reset + typography
- [ ] Top bar + nav + mobile menu (Reports Login at top)
- [ ] Hero + dual CTA (`.cta-pair`), trust bar, section layouts
- [ ] Cards, buttons, forms
- [ ] Chatbot floating widget styles
- [ ] Responsive breakpoints (320 / 768 / 1280) + scroll-reveal

## Phase 3 — Site JS (`js/main.js`)
- [ ] Mobile menu toggle + active nav link
- [ ] Smooth scroll / sticky nav behavior
- [ ] Scroll-reveal (IntersectionObserver)
- [ ] Enquiry form validation + submit (Formspree/Web3Forms — emails the lab)
- [ ] Back-to-top + auto footer year

## Phase 4 — Chatbot (`js/chatbot.js` + `data/chatbot-rules.js`)
- [ ] Rules: find-test (→ tests.html), pricing (→ contact flow), info, fallback
- [ ] Floating mount on ALL pages
- [ ] Menu quick-replies + free-text keyword matching
- [ ] Pricing NEVER shows a price — renders Call / WhatsApp
- [ ] Keyboard accessible, auto-scroll, typing indicator

## Phase 4.5 — Tests Data (`data/tests.js`)
- [ ] Schema: slug, name, category, symptoms[], info — **NO price field**
- [ ] Populate from client's tests list
- [ ] "For more details, contact us at [PHONE] / WhatsApp" note + contact block

## Phase 5 — Doctor Case-Study Newsletter (see PLAN.md §8)
**Website side (v1):**
- [ ] Case-studies listing + de-identified per-study template (summary, findings, teaching point, disclaimer)
- [ ] Link from nav / homepage teaser
**Email side (v1):**
- [ ] Client buys domain (GoDaddy)
- [ ] Zoho Mail free — 1 mailbox + aliases (one inbox, up to 4 addresses)
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
- [ ] Replace placeholder copy with client content (About, Services, Quality, Publications, Physicians)
- [ ] Real logo + WebP images (facility + equipment)
- [ ] Real contact details, hours, Google Maps embed, social links
- [ ] Reporting Portal URL wired into top-of-site Reports Login
- [ ] Patient Form PDF into `assets/`

## Phase 7 — Polish & QA
- [ ] Responsive (320 / 768 / 1280)
- [ ] Accessibility (contrast, keyboard, alt, ARIA)
- [ ] Cross-browser (Chrome, Firefox, Safari, Edge)
- [ ] SEO: unique title/description, canonical, one h1, sitemap, robots.txt, GA4
- [ ] Performance (WebP, lazy-load, no console errors)
- [ ] No `PLACEHOLDER` / `TODO` remaining

## Phase 8 — Deploy
- [ ] ZIP → GoDaddy File Manager → `public_html/` → extract
- [ ] Point domain, verify HTTPS
- [ ] Submit sitemap in Search Console
- [ ] Final review with client

---

### Notes / Blockers
- **Blocked on:** client's styling reference links; client content (see PLAN.md §10).
- Do **not** build/replace the third-party Reporting Portal — link out only.
- Confirm second client's name/title (Dr. Ashok vs Mr. Ashok Yadav) before signing.
