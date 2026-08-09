# PATHMOLE Expert — Design Reference & Adapted Structure (from Aiforia.com)

> **Reference site:** https://www.aiforia.com/ (client-provided).
> **Purpose:** analyse Aiforia's structure/design and adapt a **similar structure** for PATHMOLE.
> **Last updated:** 2026-08-08 · **Status:** structure proposal (md-only; not built yet)

---

## Why this reference fits

Aiforia is a **B2B medtech / digital-pathology** company — the same clinical-credibility,
trust-first world PATHMOLE lives in (~90% B2B referral). What it does well and we should borrow:
- **Clinical-clean aesthetic:** light background, dark text, ONE accent colour, lots of whitespace.
- **Card + grid modules** that repeat cleanly and stay responsive.
- **Trust signals up front:** customer logos, certifications, publications, testimonials.
- **Credibility content** (Resource Library / case studies) treated as a first-class section.
- **Single clear conversion goal** ("Request a demo") echoed top, middle, and bottom.

What we should **NOT** copy (Aiforia is a *software product* company; PATHMOLE is a *service lab*):
- Product/AI-tool mega-menus, "AI development tool", investor/veterinary sections.
- Anything implying tech we don't offer. Our conversion goal is **Enquiry / Call / WhatsApp**, not "demo".
- Their pink/magenta accent is a *brand* choice — see "Visual direction" for our palette decision.

---

## 1. Aiforia section → PATHMOLE equivalent (mapping)

| # | Aiforia homepage section | → PATHMOLE adaptation |
|---|---|---|
| 1 | Hero: headline + subtext + "Request a demo" | **Hero** + one-line mission + **dual CTA** (Submit Enquiry / Call·WhatsApp) |
| 2 | NEWS banner (single announcement) | **Latest case study / announcement strip** (links to newest de-identified case study) |
| 3 | "Versatile offering" — 4 solution cards | **What We Do** — 2 discipline cards: **Histopathology** & **Molecular Diagnostics** (+ optional IHC / Quality) |
| 4 | "What makes Aiforia unique?" — 4 feature cards | **Why Choose PATHMOLE** — 4 cards: accuracy, fast TAT, expert pathologists, technology/quality |
| 5 | Customer video testimonials | **Trusted by clinicians** — referring-doctor testimonials *(placeholder until client provides)* |
| 6 | Resource Library — 6 blog/case cards | **Case Studies teaser** — grid of newest de-identified studies → `case-studies/` (feeds newsletter) |
| 7 | Customer logo wall | **Trust bar** — accreditations / partner-hospital strip *(only real, confirmed logos — no invention)* |
| 8 | "Request a demo" form | **Final CTA** — Enquiry form + **Call / WhatsApp** buttons |
| 9 | Upcoming events | **Skip for v1** (revisit later if the lab does CMEs/events) |

---

## 2. Adapted Homepage Section Map (top → bottom)

> This **extends our current "lean funnel"** homepage toward Aiforia's fuller marketing page.
> Still one clear path to the two CTAs — just a few more trust modules. (Decision flagged below.)

| # | Section | Class / ID | Contents |
|---|---|---|---|
| — | Top bar | `.top-bar` | Phone · Hours · Call · WhatsApp · **Reports Login ↗** (mirrors Aiforia's "Login") |
| — | Nav | `.site-nav` | Logo + links + mobile menu (see §3) |
| 1 | Hero | `.hero` | Headline + mission line + **dual CTA** + clinical visual |
| 2 | Announcement strip | `.news-strip` | Latest case study / notice → links out *(optional, dismissible)* |
| 3 | What We Do | `.services` | 2–4 cards: Histopathology · Molecular Diagnostics (· IHC · Quality) → `services.html` |
| 4 | Why Choose Us | `#why` | 4 icon cards: Accuracy · Fast TAT · Expert pathologists · Technology & quality |
| 5 | Trust bar | `.trust-bar` | Accreditation / partner-hospital logos or key numbers *(placeholders only)* |
| 6 | Testimonials | `#testimonials` | 2–3 referring-clinician quotes *(placeholder)* |
| 7 | Case Studies teaser | `#case-studies` | Grid of newest de-identified studies → `case-studies/` |
| 8 | Final CTA | `#cta` | **[Submit Enquiry]  [Call / WhatsApp]** + short reassurance line |
| — | Footer | `.site-footer` | Multi-column (see §4) |
| — | Chatbot | `.chatbot` | Floating widget (all pages) |

> **DECIDED (2026-08-08):** client wants to **"go a little deeper"** with a **polished, Aiforia-like
> finish** — so we build the **full section map above** (all of §1–§8), not the stripped lean version.
> Keep each section tight and card-based so "deeper" still reads clean, not cluttered.

---

## 3. Navigation (adapted from Aiforia's mega-menu)

Aiforia uses 5 mega-menus. We're smaller — use **simple links**, not mega-menus:

- **Utility (top bar):** Call · WhatsApp · **Reports Login ↗** (≈ Aiforia "Login") · optional "Contact"
- **Main nav:** HOME · ABOUT · SERVICES · TESTS · CASE STUDIES · RESEARCH · CONTACT
- **Mobile menu (full):** add GALLERY · VIDEOS · PATIENTS · PHYSICIANS · QUALITY · FAQ · CAREERS · REPORTS LOGIN ↗

*(If Services ever needs a dropdown: Histopathology / Molecular Diagnostics / IHC — but start with a plain link to `services.html`.)*

---

## 4. Footer (adapted from Aiforia's multi-column footer)

Aiforia's footer = link columns + contact addresses + secondary/legal links + social + certifications.
PATHMOLE version:

- **Column 1 — Services:** Histopathology · Molecular Diagnostics · IHC · Tests · Quality
- **Column 2 — Explore:** About · Case Studies · Research/Publications · Patients · Careers
- **Column 3 — Contact:** Address(es) · Phone · WhatsApp · Email · Working hours
- **Bottom bar:** © 2026 PATHMOLE Expert · Privacy · social icons · (certification logos once confirmed)
- Keep the existing **"Designed & built by Krishna Singh"** dev-credit line.

---

## 5. Visual direction (borrow the *feel*, decide the palette)

**Borrow from Aiforia:**
- Light/white background, high-contrast **dark text**, **ONE accent** used sparingly on CTAs/links.
- Generous whitespace; card-and-grid layout; subtle shadows/rounded corners.
- Clear type hierarchy: large hero H1 → section H2s → small card titles.
- Imagery = real **histology/molecular visuals** + facility/equipment photos (WebP), not stock fluff.
- Text-style CTAs with arrow motifs ("Read more →", "Learn more →") alongside solid primary buttons.

**Palette — LOCKED to the PathMole brand (see `brand-assets.md`):**
- The lab's own logo/letterhead is **navy + magenta** — so Aiforia's magenta accent actually *matches*
  the real brand. We use **navy (`#232C8E`) for headings/structure** and **magenta (`#EC008C`) for the
  accent/CTAs**. Full palette + `:root` block live in **`docs/brand-assets.md`** — don't duplicate here.
- Signature motif from the letterhead: **angular navy→magenta chevron bands** + a faint microscope/DNA
  watermark. Use these as section dividers / hero accent for the "polished finish."

---

## 6. Decisions & remaining questions

**Resolved (2026-08-08):**
- [x] **Homepage depth:** go **deeper** — full Aiforia-style section map (§2), polished finish.
- [x] **Palette:** **navy + magenta**, locked to the PathMole letterhead (`brand-assets.md`).
- [x] **Fonts:** Poppins (headings) + Inter (body) placeholder — matches the bold logo; confirm if brand fonts exist.

**Still needed from client:**
- [ ] Are there **more reference links** coming, or is Aiforia the single style anchor?
- [ ] Confirm which **trust signals are real** (accreditations, partner logos, testimonials) — we only
      show confirmed ones; everything else stays a labelled placeholder.
- [ ] The **logo file** (SVG/PNG), domain, working hours, Google Maps, Reports Portal URL, social links.

> The GUIDE's "Styling & Colours" section is now finalised from `brand-assets.md`; we can move from
> ground-up planning into **Phase 1 (structure)** once the logo file + remaining assets arrive.
