# PATHMOLE Expert — Website

Static website for **PATHMOLE Expert**, a specialist **Histopathology & Molecular
Diagnostics referral laboratory** in **Gurugram (Delhi NCR)**. Audience: referring
doctors, hospitals, and diagnostic centres (B2B/referral). Launch target: **17 Aug 2026**.

Stack: static **HTML / CSS / vanilla JS**, no framework, no build step. Hosted on
**GoDaddy** (`public_html/`). Includes a rule-based chatbot (the site's test-finder) and a
de-identified doctor case-study newsletter.

## Folder layout

```
.                         ← website build lives here (index.html, css/, js/, data/, assets/ …)
├── docs/                 ← all project documentation
│   ├── PATHMOLE-WEBSITE-GUIDE.md        # BUILD source of truth (page tree + code blocks)
│   ├── PLAN.md                          # high-level context, decisions, costs
│   ├── TASKS.md                         # progress checklist
│   ├── INSTRUCTIONS.md                  # conventions / how to edit
│   ├── test-categories-reference.md     # domain reference: typical tests per category + refs
│   ├── design-reference-aiforia.md      # design analysis of aiforia.com + adapted structure
│   ├── brand-assets.md                  # brand kit: name, logo, colours, tagline, contact
│   └── reference-drarpangandhi-guide.md # reference only (a prior site's guide)
├── contract/             ← commercial paperwork
│   ├── CONTRACT.md
│   ├── PATHMOLE-Expert-Contract.docx
│   └── make_contract_docx.py            # regenerates the .docx (needs python-docx)
└── README.md             ← this file
```

## Two hard rules
1. **No pricing anywhere** (site or chatbot) — pricing always routes to the contact flow.
2. **Case studies are always de-identified** (DPDP Act 2023).

**Start here:** `docs/PATHMOLE-WEBSITE-GUIDE.md`. **Status:** v1 built — all 15 pages, brand
styling (navy + magenta), chatbot, and test list are live in the repo root. Awaiting client
assets (vector logo, domain, Maps link, Reporting Portal URL, form endpoint, GA4, real content)
before launch.

> Inner pages are generated from one shared shell via `scripts/build_pages.py` (a dev tool — do
> NOT upload it to `public_html`). Edit page content there and re-run `python scripts/build_pages.py`.
> `index.html` is hand-built. Ship the `.html`, `css/`, `js/`, `data/`, `assets/`, `sitemap.xml`,
> `robots.txt`, `.htaccess` — not `docs/`, `contract/`, `scripts/`, or `image/`.
