/* =============================================================
   PathMole Expert Lab — Chatbot rules (edit answers here)
   Rule-based only. No AI, no backend.
   Each rule: { id, label, keywords[], answer, action }
   action types:
     { type: "link",  href, text }        → one link button
     { type: "links", items:[{href,text}] } → several link buttons
     { type: "contact" }                  → Call / WhatsApp / enquiry-form buttons
     { type: "enquiry" }                  → link to the general enquiry form
     { type: "none" }                     → answer only
   Answers may use "\n" for line breaks — the bubble renders them (white-space: pre-wrap),
   so short bulleted lists are fine.
   HARD RULE: never put a price anywhere. Pricing → { type: "contact" }.
   HARD RULE: do not invent tests, turnaround times, accreditations, or numbers.
     Only the tests actually on the menu (see data/tests.js) may be named.
   The three real forms on the site:
     • General enquiry   → contact.html#enquiry
     • Partner enquiry   → partner.html#enquiry
     • Training enquiry  → training-institute.html#enquiry
   Links use root-relative hrefs (e.g. "tests.html"); the engine adds "../" automatically
   on pages inside /case-studies/, so keep them root-relative here.
   ============================================================= */
const CHATBOT_CONFIG = {
  greeting:
    "Hi, I'm the PathMole assistant 👋\nAsk me about a test, our services, timings or the Training Institute — I'll give you the answer right here and point you to the right page or form. What can I help you find?",
  phone: "+919899822375",
  whatsapp: "919899822375",
  email: "pathmolelab@gmail.com",
  // where the general "Send an enquiry" redirect points (the contact form)
  enquiryHref: "contact.html#enquiry",
  // quick-reply buttons shown first (by rule id)
  menu: ["find-test", "services", "training", "partner", "enquiry", "timings", "location", "pricing"],
  fallback:
    "I didn't quite catch that — but I can still help. I know about our tests, services, timings, location, the Training Institute and partnerships. Try a keyword like “HPV”, “biopsy”, “timings” or “partner”, or reach the team directly:",
};

const CHATBOT_RULES = [
  /* ---------- Core: tests & services ---------- */
  {
    id: "find-test",
    label: "Find a test",
    keywords: ["test", "tests", "test list", "test menu", "which test", "find a test", "find test", "list of tests", "all tests", "browse tests", "tests offered", "test page", "catalogue", "catalog", "symptom", "indication", "pcr", "panel"],
    answer:
      "Happy to help you find a test! A few of the ones we're asked for most:\n\n🔬 Histopathology — biopsies (small samples up to major resections), cell blocks & second opinions\n🧫 Cytology — Pap smear / LBC and fluid cytology\n🧬 Molecular (PCR) — HPV, Hepatitis B & C, HIV, Tuberculosis, HLA-B27, EBV, BCR-ABL, TORCH\n\nThat's just a snapshot — the full menu, grouped by category, is on the Tests page. Or tell me a specific test or symptom (e.g. “HPV”, “biopsy”, “hepatitis”) and I'll point you right to it.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "Browse all tests" },
        { href: "molecular-diagnostics.html", text: "Molecular Diagnostics" },
        { href: "histopathology.html", text: "Histopathology" },
      ],
    },
  },
  {
    id: "services",
    label: "Our services",
    keywords: ["service", "services", "what do you do", "what you do", "histopathology", "histopath", "cytopathology", "cytology", "fnac", "molecular", "molecular diagnostics", "diagnostic support", "specialised", "specialized", "offer", "offerings", "department", "departments"],
    answer:
      "We're a specialist Histopathology & Molecular Diagnostics referral lab, with cytopathology and specialised diagnostic support alongside. Pick an area to read more:",
    action: {
      type: "links",
      items: [
        { href: "services.html", text: "All services" },
        { href: "histopathology.html", text: "Histopathology" },
        { href: "cytopathology.html", text: "Cytopathology" },
        { href: "molecular-diagnostics.html", text: "Molecular Diagnostics" },
        { href: "diagnostic-support.html", text: "Diagnostic Support" },
      ],
    },
  },

  /* ---------- Specific tests / conditions (real menu only) ----------
     These win when a user types the bare term (e.g. "HPV", "biopsy", "TB"), giving a
     confident, specific answer instead of a generic redirect. Each links to the Tests
     page plus the matching landmark case study for extra depth. */
  {
    id: "test-hpv-cervical",
    label: "HPV / cervical screening",
    keywords: ["hpv", "human papillomavirus", "papilloma", "cervical", "cervix", "pap", "pap smear", "lbc", "smear"],
    answer:
      "Yes — for cervical screening we offer HPV molecular (PCR) testing along with Pap smear / LBC cytology. Used together, they're the modern standard for catching cervical disease early. Pricing and sample requirements are shared on enquiry.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "case-studies/landmark-cervical-hpv-pap.html", text: "The Pap & HPV story" },
      ],
    },
  },
  {
    id: "test-hepatitis-liver",
    label: "Hepatitis B & C",
    keywords: ["hepatitis", "hbv", "hcv", "hep b", "hep c", "hepb", "hepc", "liver", "jaundice", "cirrhosis"],
    answer:
      "We offer molecular (PCR) testing for Hepatitis B (HBV) and Hepatitis C (HCV) — the viruses behind most chronic liver disease and liver cancer. Detecting and monitoring them molecularly helps guide treatment.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "case-studies/landmark-hepatitis-liver-cancer.html", text: "Hepatitis & liver cancer" },
      ],
    },
  },
  {
    id: "test-hiv",
    label: "HIV testing",
    keywords: ["hiv", "aids", "viral load", "retroviral", "arv"],
    answer:
      "Yes — we offer molecular HIV testing. Molecular (nucleic-acid) methods can detect the virus earlier than antibody tests and help measure viral load to monitor treatment.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "case-studies/landmark-hiv-molecular.html", text: "HIV: discovery to testing" },
      ],
    },
  },
  {
    id: "test-tb",
    label: "Tuberculosis (TB)",
    keywords: ["tb", "tuberculosis", "koch", "mtb", "afb", "mycobacterium"],
    answer:
      "We offer molecular (PCR) detection of Mycobacterium tuberculosis (TB) — faster and more sensitive than older methods, which supports earlier diagnosis.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "case-studies/landmark-tuberculosis-molecular.html", text: "TB: Koch to molecular" },
      ],
    },
  },
  {
    id: "test-hla-b27",
    label: "HLA-B27",
    keywords: ["hla", "b27", "hla-b27", "spondylitis", "ankylosing", "spondyloarthritis", "sacroiliitis"],
    answer:
      "Yes — we offer HLA-B27 testing, commonly used when investigating ankylosing spondylitis and related spondyloarthritis.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "case-studies/landmark-hla-b27-spondylitis.html", text: "HLA-B27 & spondylitis" },
      ],
    },
  },
  {
    id: "test-biopsy",
    label: "Biopsy / histopathology",
    keywords: ["biopsy", "biopsies", "tissue", "resection", "specimen", "histology", "tumour", "tumor", "cancer", "carcinoma", "malignancy", "growth", "lump", "mass", "granuloma", "second opinion", "cell block"],
    answer:
      "Our core strength is histopathology — expert examination of biopsies from small samples right up to major resection specimens, plus cell blocks and second-opinion review on outside cases. It remains the gold standard for a tissue diagnosis.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "histopathology.html", text: "About histopathology" },
        { href: "case-studies/landmark-carcinoma-biopsy.html", text: "Why the biopsy is gold standard" },
      ],
    },
  },
  {
    id: "test-other-molecular",
    label: "EBV / BCR-ABL / TORCH",
    keywords: ["ebv", "epstein", "epstein-barr", "bcr", "abl", "bcr-abl", "philadelphia", "leukaemia", "leukemia", "torch", "toxoplasma", "rubella", "cmv", "cytomegalovirus", "herpes", "flu panel", "influenza"],
    answer:
      "Yes — our molecular menu also includes Epstein-Barr virus (EBV), BCR-ABL, TORCH by PCR and an influenza (flu) panel. Tell me which one and I'll point you to it, or see the full molecular menu.",
    action: {
      type: "links",
      items: [
        { href: "tests.html", text: "See the test menu" },
        { href: "molecular-diagnostics.html", text: "Molecular Diagnostics" },
      ],
    },
  },

  /* ---------- Training Institute (page + enquiry form) ---------- */
  {
    id: "training",
    label: "Training Institute",
    keywords: ["training", "institute", "course", "courses", "workshop", "workshops", "observership", "observerships", "learn", "education", "educational", "certificate", "certification", "cpd", "student", "students", "intern", "internship", "fellowship", "teaching", "upskill", "skills"],
    answer:
      "The PathMole Training Institute offers practical, hands-on learning for pathology and laboratory professionals — histopathology techniques, molecular diagnostics, quality & accreditation, lab operations and more. Read about it or send a training enquiry:",
    action: {
      type: "links",
      items: [
        { href: "training-institute.html", text: "Explore training" },
        { href: "training-institute.html#enquiry", text: "Enquire about training" },
      ],
    },
  },

  /* ---------- Partner With Us (page + enquiry form) ---------- */
  {
    id: "partner",
    label: "Partner with us",
    keywords: ["partner", "partnership", "partnering", "collaborate", "collaboration", "outsource", "outsourcing", "referral partner", "tie up", "tie-up", "associate", "institution", "hospital tie", "b2b", "work together", "empanel", "empanelment"],
    answer:
      "We partner with hospitals, clinics, doctors, laboratories and healthcare institutions for Histopathology & Molecular Diagnostic services. Read the details or start a partnership enquiry and our team will get in touch:",
    action: {
      type: "links",
      items: [
        { href: "partner.html", text: "Partnership details" },
        { href: "partner.html#enquiry", text: "Start a partnership enquiry" },
      ],
    },
  },

  /* ---------- Forms hub — routes to whichever form fits ---------- */
  {
    id: "forms",
    label: "Forms & enquiries",
    keywords: ["form", "forms", "which form", "apply", "application", "register", "registration", "sign up", "signup", "fill", "submit form"],
    answer:
      "Here are the forms on the site — pick the one that fits, and the lab will get back to you:",
    action: {
      type: "links",
      items: [
        { href: "contact.html#enquiry", text: "General enquiry" },
        { href: "partner.html#enquiry", text: "Partner enquiry" },
        { href: "training-institute.html#enquiry", text: "Training enquiry" },
        { href: "patients.html", text: "Patient form (PDF)" },
      ],
    },
  },
  {
    id: "enquiry",
    label: "Send an enquiry",
    keywords: ["enquiry", "enquire", "inquiry", "inquire", "message", "refer", "referral", "refer a case", "get in touch", "reach out", "send an enquiry"],
    answer:
      "You can send us an enquiry and our team will get back to you — it takes a minute:",
    action: { type: "enquiry", text: "Open the enquiry form" },
  },

  /* ---------- Practical info ---------- */
  {
    id: "timings",
    label: "Timings",
    keywords: ["time", "timing", "timings", "hours", "open", "close", "closing", "when", "working", "daily", "weekend", "sunday"],
    answer: "We're open every day, 8:00 AM – 8:00 PM (including weekends).",
    action: { type: "none" },
  },
  {
    id: "location",
    label: "Location",
    keywords: ["location", "address", "where", "map", "directions", "reach", "gurugram", "gurgaon", "sector 6", "how to reach", "haryana"],
    answer:
      "You'll find us at:\nBuilding No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana).\n\nHappy to share directions — the contact page has the map and details.",
    action: { type: "link", href: "contact.html", text: "Contact & directions" },
  },
  {
    id: "pricing",
    label: "Pricing",
    keywords: ["price", "cost", "charges", "fee", "fees", "rate", "rates", "how much", "pricing", "quote"],
    answer:
      "We share pricing directly so we can guide you accurately for your specific test and sample. Drop us a message or call and the team will help right away:",
    action: { type: "contact" }, // renders Call / WhatsApp — never a price
  },
  {
    id: "turnaround",
    label: "Report timing",
    keywords: ["turnaround", "tat", "how long", "how many days", "report time", "ready", "when will", "duration", "delivery", "days"],
    answer:
      "Turnaround depends on the specimen and the test — some are quick, others (like complex histopathology) take longer. Tell us the test and we'll give you an accurate timeline for your case:",
    action: { type: "contact" },
  },
  {
    id: "reports",
    label: "Reports login",
    keywords: ["report", "reports", "login", "log in", "result", "results", "portal", "download report", "online report", "collect report"],
    answer:
      "Reports are available through our online reporting portal — just tap the “Reports Login ↗” button at the top of any page. If you're a referring doctor and need portal access set up, contact the lab and we'll help.",
    action: { type: "none" },
  },

  /* ---------- About the lab & people ---------- */
  {
    id: "about",
    label: "About the lab",
    keywords: ["about", "who are you", "who is", "company", "story", "mission", "vision", "background", "overview", "history", "why choose"],
    answer:
      "PathMole Expert Lab is a specialist Histopathology & Molecular Diagnostics referral laboratory in Sector 6, Gurugram. Here's more about us:",
    action: { type: "link", href: "about.html", text: "About PathMole" },
  },
  {
    id: "team",
    label: "Our team",
    keywords: ["doctor", "doctors", "pathologist", "pathologists", "team", "physician", "physicians", "leadership", "consultant", "for clinicians", "clinician", "clinicians", "director", "founder"],
    answer:
      "Our lab is led by experienced pathologists, and we work closely with referring clinicians. Meet the team:",
    action: { type: "link", href: "physicians.html", text: "Our team & for clinicians" },
  },
  {
    id: "quality",
    label: "Quality & safety",
    keywords: ["quality", "accreditation", "accredited", "safety", "standard", "standards", "reliable", "reliability", "accuracy", "assurance"],
    answer:
      "Quality and patient safety sit at the centre of everything we do. Here's our quality framework:",
    action: { type: "link", href: "quality.html", text: "Quality & patient safety" },
  },
  {
    id: "case-studies",
    label: "Case studies & research",
    keywords: ["case", "case study", "case studies", "newsletter", "blog", "research", "publication", "publications", "guideline", "guidelines", "reference", "references", "who classification", "asco", "cap", "landmark"],
    answer:
      "We share landmark cases that shaped modern diagnostics, alongside the classifications and guidelines our reporting is built on. Have a look:",
    action: { type: "link", href: "case-studies/", text: "Case studies & research" },
  },

  /* ---------- Patients ---------- */
  {
    id: "patient-form",
    label: "Patient info & form",
    keywords: ["patient", "patients", "patient form", "download form", "requisition", "prepare", "before test", "before my test", "visit", "coming in", "what to bring", "prescription"],
    answer:
      "Coming in for a test? Please carry your prescription/request form and any relevant previous reports. You can download the patient form and fill it offline:",
    action: { type: "link", href: "patients.html", text: "Patients page & form" },
  },

  /* ---------- Careers, FAQ, media ---------- */
  {
    id: "careers",
    label: "Careers",
    keywords: ["career", "careers", "job", "jobs", "hiring", "vacancy", "vacancies", "work with you", "recruitment", "apply for job", "opening", "openings"],
    answer: "We'd love to hear from you. Current openings are listed on our Careers page:",
    action: { type: "link", href: "careers.html", text: "See careers" },
  },
  {
    id: "faq",
    label: "FAQ",
    keywords: ["faq", "faqs", "frequently", "common questions"],
    answer: "Many common questions are answered on our FAQ page:",
    action: { type: "link", href: "faq.html", text: "Read the FAQ" },
  },
  {
    id: "gallery",
    label: "Gallery",
    keywords: ["gallery", "photos", "photo", "facility", "facilities", "equipment", "infrastructure", "images", "pictures", "lab photos", "inside"],
    answer: "Take a look at our facility and equipment:",
    action: { type: "link", href: "gallery.html", text: "View the gallery" },
  },
  {
    id: "videos",
    label: "Videos",
    keywords: ["video", "videos", "watch", "clip", "clips"],
    answer: "You can watch our videos here:",
    action: { type: "link", href: "videos.html", text: "Watch videos" },
  },

  /* ---------- Contact catch-all ---------- */
  {
    id: "contact",
    label: "Contact us",
    keywords: ["contact", "call", "phone", "whatsapp", "email", "talk", "speak", "reach you", "number"],
    answer: "Happy to help — reach us here:",
    action: { type: "contact" },
  },
];
