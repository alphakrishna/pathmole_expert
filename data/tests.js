/* =============================================================
   PathMole Expert Lab — Test list data (NO PRICES — never add a price field)
   Edit here to manage the tests shown on tests.html.
   Each test: { slug, name, category, symptoms[], info }
   Categories used for grouping (see CATEGORY_ORDER below):
     "Histopathology" · "Immunohistochemistry" · "Molecular Diagnostics" · "FISH & Cytogenetics"

   ⚠️ REPRESENTATIVE placeholder catalogue based on standard histopath + molecular
   offerings — the CLIENT must confirm the actual test menu before launch.
   (Cytopathology is intentionally excluded — out of scope.)
   ============================================================= */
const CATEGORY_ORDER = [
  "Histopathology",
  "Immunohistochemistry",
  "Molecular Diagnostics",
  "FISH & Cytogenetics",
];

const TESTS = [
  /* ---- Histopathology ---- */
  {
    slug: "histopathology-biopsy",
    name: "Histopathology — Biopsy",
    category: "Histopathology",
    symptoms: ["Lump / swelling", "Suspicious lesion", "Endoscopic biopsy"],
    info: "Microscopic (H&E) examination of tissue to establish or confirm a diagnosis.",
  },
  {
    slug: "histopathology-resection",
    name: "Histopathology — Surgical Resection",
    category: "Histopathology",
    symptoms: ["Post-surgical specimen", "Tumour staging"],
    info: "Examination of resection specimens with synoptic (CAP-style) reporting where applicable.",
  },
  {
    slug: "frozen-section",
    name: "Frozen Section (Intraoperative)",
    category: "Histopathology",
    symptoms: ["Intraoperative margin", "Rapid diagnosis"],
    info: "Rapid tissue diagnosis during surgery — subject to prior arrangement.",
  },
  {
    slug: "special-stains",
    name: "Special Stains (Histochemistry)",
    category: "Histopathology",
    symptoms: ["Fungal / AFB workup", "Amyloid", "Fibrosis / iron"],
    info: "PAS, GMS, ZN/AFB, Congo red, reticulin, trichrome and other special stains.",
  },

  /* ---- Immunohistochemistry ---- */
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

  /* ---- Molecular Diagnostics ---- */
  {
    slug: "egfr-mutation",
    name: "EGFR Mutation Analysis",
    category: "Molecular Diagnostics",
    symptoms: ["Lung adenocarcinoma", "Targeted therapy selection"],
    info: "Detects EGFR mutations relevant to TKI therapy selection.",
  },
  {
    slug: "kras-nras-braf",
    name: "KRAS / NRAS / BRAF Mutation Panel",
    category: "Molecular Diagnostics",
    symptoms: ["Colorectal carcinoma", "Anti-EGFR therapy"],
    info: "RAS/RAF status to guide targeted therapy in colorectal and other cancers.",
  },
  {
    slug: "ngs-solid-tumor",
    name: "NGS — Solid Tumour Panel",
    category: "Molecular Diagnostics",
    symptoms: ["Comprehensive profiling", "Multiple targets"],
    info: "Next-generation sequencing panel for comprehensive tumour profiling.",
  },
  {
    slug: "msi-testing",
    name: "MSI / MMR by Molecular Methods",
    category: "Molecular Diagnostics",
    symptoms: ["Microsatellite instability", "Immunotherapy"],
    info: "PCR/NGS-based microsatellite instability testing.",
  },

  /* ---- FISH & Cytogenetics ---- */
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
];
