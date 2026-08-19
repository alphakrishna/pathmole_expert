/* =============================================================
   PathMole Expert Lab — Test list data (NO PRICES — never add a price field)
   Edit here to manage the tests shown on tests.html.
   Each test: { slug, name, category, symptoms[], info }
   Categories used for grouping (see CATEGORY_ORDER below):
     "Histopathology" · "Molecular Diagnostics"

   LIVE MENU: client-supplied 2026-08-19 — these are the ONLY tests the lab is offering
   right now. The former placeholder Immunohistochemistry and FISH & Cytogenetics groups
   are commented out below (kept for easy re-enable when the lab adds them).
   A couple of names are pending client confirmation — see docs/TASKS.md REVIEW-WITH-CLIENT.
   ============================================================= */
const CATEGORY_ORDER = [
  "Histopathology",
  "Molecular Diagnostics",
  // DISABLED 2026-08-19 — lab not offering these yet (client-confirmed). Re-enable when live:
  // "Immunohistochemistry",
  // "FISH & Cytogenetics",
];

const TESTS = [
  /* ---- Histopathology ----
     Client-supplied menu (2026-08-19). Typos corrected; two names kept close to the
     client's wording and PENDING CONFIRMATION (see docs/TASKS.md REVIEW-WITH-CLIENT flag):
       • "Slides & Blocks" — exact service name / scope unconfirmed.
       • "Fluid Cytology / LBC Pap Smear" — kept as one line; confirm if it's two tests,
         and whether the cytology items belong under a separate Cytopathology group. */
  {
    slug: "small-biopsy",
    name: "Small Biopsy",
    category: "Histopathology",
    symptoms: [],
    info: "Histopathological examination of a small biopsy specimen.",
  },
  {
    slug: "medium-biopsy",
    name: "Medium Biopsy",
    category: "Histopathology",
    symptoms: [],
    info: "Histopathological examination of a medium biopsy specimen.",
  },
  {
    slug: "large-biopsy",
    name: "Large Biopsy",
    category: "Histopathology",
    symptoms: [],
    info: "Histopathological examination of a large specimen.",
  },
  {
    slug: "extra-large-biopsy",
    name: "Extra Large Biopsy",
    category: "Histopathology",
    symptoms: [],
    info: "Histopathological examination of an extra-large / major resection specimen.",
  },
  {
    slug: "second-opinion",
    name: "Second Opinion",
    category: "Histopathology",
    symptoms: [],
    info: "Expert review and second opinion on a histopathology case.",
  },
  {
    slug: "cell-block",
    name: "Cell Block",
    category: "Histopathology",
    symptoms: [],
    info: "Cell block preparation and examination.",
  },
  {
    slug: "slides-blocks",
    name: "Slides & Blocks",
    category: "Histopathology",
    symptoms: [],
    info: "Referred slides and paraffin blocks.",
  },
  {
    slug: "fluid-cytology-lbc-pap",
    name: "Fluid Cytology / LBC Pap Smear",
    category: "Histopathology",
    symptoms: [],
    info: "Fluid cytology and liquid-based (LBC) Pap smear examination.",
  },

  /* ---- Immunohistochemistry — DISABLED 2026-08-19 ----
     Lab not offering these yet (client-confirmed). Kept commented for easy re-enable.
  {
    slug: "ihc-diagnostic-panel",
    name: "IHC — Diagnostic / Lineage Panel",
    category: "Immunohistochemistry",
    symptoms: ["Tumour of unknown origin", "Lymphoma workup"],
    info: "Antibody panels to identify cell type and tumour lineage.",
  },
  {
    slug: "ihc-er-pr",
    name: "IHC — ER / PR (Breast)",
    category: "Immunohistochemistry",
    symptoms: ["Breast carcinoma", "Hormone receptor status"],
    info: "Hormone receptor status to guide breast cancer management.",
  },
  {
    slug: "ihc-her2",
    name: "IHC — HER2",
    category: "Immunohistochemistry",
    symptoms: ["Breast carcinoma", "Gastric carcinoma"],
    info: "HER2 protein expression; equivocal results may reflex to FISH.",
  },
  {
    slug: "ihc-pdl1",
    name: "IHC — PD-L1",
    category: "Immunohistochemistry",
    symptoms: ["Immunotherapy eligibility", "Lung / other tumours"],
    info: "Predictive marker to help assess immunotherapy suitability.",
  },
  {
    slug: "ihc-mmr",
    name: "IHC — Mismatch Repair (MLH1/MSH2/MSH6/PMS2)",
    category: "Immunohistochemistry",
    symptoms: ["Colorectal / endometrial", "Lynch screening"],
    info: "MMR protein panel for Lynch screening and immunotherapy assessment.",
  },
  ---- end disabled Immunohistochemistry ---- */

  /* ---- Molecular Diagnostics ----
     Client-supplied menu (2026-08-19). Abbreviations expanded; confirm "Flu Panel" scope
     and method with client (see docs/TASKS.md REVIEW-WITH-CLIENT flag). */
  {
    slug: "hbv-molecular",
    name: "Hepatitis B Virus (HBV)",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of Hepatitis B virus (HBV).",
  },
  {
    slug: "hcv-molecular",
    name: "Hepatitis C Virus (HCV)",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of Hepatitis C virus (HCV).",
  },
  {
    slug: "hiv-molecular",
    name: "HIV",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of HIV.",
  },
  {
    slug: "hla-b27",
    name: "HLA-B27",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "HLA-B27 molecular testing.",
  },
  {
    slug: "flu-panel",
    name: "Flu Panel",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular influenza (flu) panel.",
  },
  {
    slug: "hpv-molecular",
    name: "Human Papillomavirus (HPV)",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of Human Papillomavirus (HPV).",
  },
  {
    slug: "tb-molecular",
    name: "Tuberculosis (TB)",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of Mycobacterium tuberculosis (TB).",
  },
  {
    slug: "ebv-molecular",
    name: "Epstein-Barr Virus (EBV)",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of Epstein-Barr virus (EBV).",
  },
  {
    slug: "bcr-abl",
    name: "BCR-ABL",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "Molecular detection of the BCR-ABL fusion transcript.",
  },
  {
    slug: "torch-pcr",
    name: "TORCH by PCR",
    category: "Molecular Diagnostics",
    symptoms: [],
    info: "PCR detection of TORCH infections (Toxoplasma, Rubella, Cytomegalovirus, Herpes simplex and others).",
  },

  /* ---- FISH & Cytogenetics — DISABLED 2026-08-19 ----
     Lab not offering these yet (client-confirmed). Kept commented for easy re-enable.
  {
    slug: "her2-fish",
    name: "HER2 FISH",
    category: "FISH & Cytogenetics",
    symptoms: ["Breast / gastric", "IHC equivocal (2+)"],
    info: "Gene amplification testing, typically reflexed from equivocal HER2 IHC.",
  },
  {
    slug: "alk-ros1-fish",
    name: "ALK / ROS1 FISH",
    category: "FISH & Cytogenetics",
    symptoms: ["Lung adenocarcinoma", "Fusion detection"],
    info: "Break-apart FISH for ALK/ROS1 rearrangements.",
  },
  ---- end disabled FISH & Cytogenetics ---- */
];
