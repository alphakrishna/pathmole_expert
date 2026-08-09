# PathMole Expert Lab — Brand Kit (from official letterhead)

> Single source of truth for brand identity: name, logo, colours, type, tagline, contact.
> Derived from the client's **official letterhead** (`image/WhatsApp Image 2026-08-07 at 10.33.30 AM.webp`).
> **Last updated:** 2026-08-08 · **Status:** brand palette LOCKED (navy + magenta)

---

## 1. Name & wordmark

- **Full name:** **PathMole Expert Lab**
- **Wordmark styling:** "**Path**Mole" as one word — **Path** = navy, **Mole** = magenta; then
  "**EXPERT LAB**" in navy small-caps beneath.
- **Discipline line (under logo):** `HISTOPATHOLOGY | MOLECULAR BIOLOGY` (magenta).
- **Descriptor:** `Managed by highly experienced doctors`.
- **Icon:** microscope + DNA double-helix + a molecular/cell cluster (navy + magenta).

**Logo files (extracted from the letterhead — RASTER stopgap):**
- `image/pathmole-logo.png` — full lockup on white (371×124).
- `image/pathmole-logo-transparent.png` — same, transparent background (for soft/coloured bg).
- ⚠️ These are cropped from a raster letterhead → **low-res**. Request the **vector logo (SVG/AI/PDF)**
  from the client for crisp scaling; use these only as placeholders during the build.

> Note: the letterhead says **"Molecular Biology"**; our earlier docs say **"Molecular Diagnostics."**
> Both describe the same discipline. Use **"Molecular Diagnostics"** for the clinical/service framing
> on the site, but the logo tagline stays **"Histopathology | Molecular Biology"** verbatim.

## 2. Tagline / slogan

> **"Precision in Diagnosis. Confidence in Results."**

Use as the brand slogan — good hero sub-line and footer strap. (The letterhead also carries
"NOT VALID FOR MEDICO LEGAL PURPOSE" — that's a **report** disclaimer, **not** for the website.)

## 3. Colour palette (LOCKED — approximated from letterhead)

> Hex values are **eyeballed from the letterhead**; confirm exact values from the **logo vector /
> brand guide** if the client has one. All colours live in `:root` variables (one-edit re-theme).

| Role | Variable | Hex (approx) | Use |
|---|---|---|---|
| Brand navy | `--brand-navy` | `#232C8E` | Headings, nav, logo "Path/Expert Lab", section bands |
| Navy deep | `--brand-navy-deep` | `#1A2270` | Hover/darker navy, gradients |
| Brand magenta | `--brand-pink` | `#EC008C` | Accent, primary CTAs, links, logo "Mole", discipline line |
| Magenta deep | `--brand-pink-deep` | `#C1006F` | Button hover |
| Heading ink | `--ink-900` | `#14202B` | Long-form heading text (or use navy) |
| Body ink | `--ink-600` | `#3B4A57` | Body copy |
| Meta ink | `--ink-400` | `#7A8894` | Captions, meta |
| Surface | `--surface` | `#FFFFFF` | Page background, cards |
| Soft bg | `--bg-soft` | `#F5F7FB` | Alternating section background (cool tint) |

**Contrast / accessibility rules:**
- **Navy** is safe for text on white (high contrast) — default for headings/body-critical text.
- **Magenta** reads well as a **button/fill with white text** and for accents/links; avoid magenta
  for small body text on white (borderline AA). Verify every combo hits **WCAG AA**.

## 4. Signature visual motif

The letterhead's identity is the **angular chevron band** — a navy block with a magenta diagonal
edge (top) and a mirrored band (bottom). Translate this into the site as:
- Diagonal/angled **section dividers** or a hero accent shape (navy → magenta edge).
- A faint **microscope+DNA watermark** behind hero/section backgrounds (very low opacity), as on
  the letterhead — subtle, never competing with text.
- Keep it **restrained**: one accent, lots of whitespace (per the Aiforia polish direction).

## 5. Typography (recommendation — confirm)

- **Headings:** a geometric, confident sans — **Poppins** or **Montserrat** (matches the bold logo).
- **Body:** **Inter** (clean, legible on screen).
- Both are free Google Fonts. Placeholder in `:root`; swap if the client has brand fonts.

## 6. Confirmed contact details (from letterhead — replaces placeholders)

- **Address:** Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road,
  Opposite Fire Station, Dayanand Colony, **Sector 6, Gurugram (Haryana)**
- **Mobile:** **+91 98998 22375**
- **Email:** **pathmolelab@gmail.com** *(a professional domain email — e.g. via Zoho — is planned;
  use this Gmail until the domain mailbox is set up)*
- **WhatsApp:** **+91 98998 22375** (confirmed same as mobile).
- **Working hours:** **11:00 AM – 11:00 PM** ("11 to 11"), assumed **daily** (editable in the top bar).

> These are now the **real** values for `[PHONE]`, `[WHATSAPP]`, working hours, address, and email
> placeholders in the build. Still needed: **domain** (client providing later), **Google Maps embed**
> (client providing later — until then show a **static map-card placeholder**, not a live embed),
> **Reports Portal URL**, **social links**, and the **exact logo file** (SVG/PNG — a raster crop from
> the letterhead is a stopgap: `image/pathmole-logo.png`).

## 7. `:root` palette block (drop into `css/style.css`)

```css
:root {
  /* BRAND — from PathMole letterhead (confirm exact hex from logo vector) */
  --brand-navy:      #232C8E;
  --brand-navy-deep: #1A2270;
  --brand-pink:      #EC008C;
  --brand-pink-deep: #C1006F;

  /* INK / SURFACES */
  --ink-900: #14202B;
  --ink-600: #3B4A57;
  --ink-400: #7A8894;
  --surface: #FFFFFF;
  --bg-soft: #F5F7FB;

  /* SEMANTIC aliases (use these in components) */
  --accent:      var(--brand-pink);
  --accent-deep: var(--brand-pink-deep);
  --heading:     var(--brand-navy);

  /* TYPE */
  --font-heading: 'Poppins', 'Segoe UI', sans-serif;
  --font-body:    'Inter', Arial, sans-serif;

  /* SPACING / SHAPE */
  --radius: 12px;
  --maxw: 1160px;
}
```
