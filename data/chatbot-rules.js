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
   HARD RULE: never put a price anywhere. Pricing → { type: "contact" }.
   HARD RULE: do not invent tests, turnaround times, accreditations, or numbers.
   The three real forms on the site:
     • General enquiry   → contact.html#enquiry
     • Partner enquiry   → partner.html#enquiry
     • Training enquiry  → training-institute.html#enquiry
   ============================================================= */
const CHATBOT_CONFIG = {
  greeting:
    "Hi! I'm the PathMole assistant. I know my way around the whole site — I can help you find a test, explain our services or the Training Institute, and point you to the right form (general, partner or training enquiry) or straight to the lab. What do you need?",
  phone: "+919899822375",
  whatsapp: "919899822375",
  email: "pathmolelab@gmail.com",
  // where the general "Send an enquiry" redirect points (the contact form)
  enquiryHref: "contact.html#enquiry",
  // quick-reply buttons shown first (by rule id)
  menu: ["find-test", "services", "training", "partner", "enquiry", "timings", "location", "pricing"],
  fallback:
    "I'm not sure about that one — but I can still point you the right way. You can send us an enquiry or call the lab directly, and our team will help.",
};

const CHATBOT_RULES = [
  /* ---------- Core: tests & services ---------- */
  {
    id: "find-test",
    label: "Find a test",
    keywords: ["test", "tests", "biopsy", "ihc", "immunohistochemistry", "fish", "ngs", "pcr", "mutation", "egfr", "her2", "pdl1", "pd-l1", "msi", "mmr", "panel", "marker", "markers", "stain", "staining", "symptom", "indication", "which test"],
    answer:
      "Tell me the test name or the symptom/indication, and I'll point you to it — or browse the full list by category.",
    action: { type: "link", href: "tests.html", text: "Browse all tests" },
  },
  {
    id: "services",
    label: "Our services",
    keywords: ["service", "services", "what do you do", "what you do", "histopathology", "histopath", "cytopathology", "cytology", "fnac", "pap smear", "molecular", "molecular diagnostics", "diagnostic support", "specialised", "specialized", "offer", "offerings"],
    answer:
      "We're a specialist Histopathology & Molecular Diagnostics referral lab, with cytopathology and specialised diagnostic support too. Pick an area to read more:",
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

  /* ---------- Training Institute (page + enquiry form) ---------- */
  {
    id: "training",
    label: "Training Institute",
    keywords: ["training", "institute", "course", "courses", "workshop", "workshops", "observership", "observerships", "learn", "education", "educational", "certificate", "certification", "cpd", "student", "students", "intern", "internship", "fellowship", "teaching", "upskill", "skills"],
    answer:
      "The PathMole Training Institute offers practical, hands-on learning for pathology and laboratory professionals — histopathology techniques, molecular diagnostics, quality & accreditation, lab operations and more. You can read about it or enquire about training:",
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
    keywords: ["time", "timing", "timings", "hours", "open", "close", "closing", "when", "working", "daily"],
    answer: "We're open daily, 11:00 AM – 11:00 PM.",
    action: { type: "none" },
  },
  {
    id: "location",
    label: "Location",
    keywords: ["location", "address", "where", "map", "directions", "reach", "gurugram", "gurgaon", "sector 6", "how to reach"],
    answer:
      "We're at Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana).",
    action: { type: "link", href: "contact.html", text: "Contact & directions" },
  },
  {
    id: "pricing",
    label: "Pricing",
    keywords: ["price", "cost", "charges", "fee", "fees", "rate", "rates", "how much", "pricing", "quote"],
    answer:
      "We share pricing directly so we can guide you accurately. Please contact the lab and our team will help.",
    action: { type: "contact" }, // renders Call / WhatsApp — never a price
  },
  {
    id: "turnaround",
    label: "Report timing",
    keywords: ["turnaround", "tat", "how long", "how many days", "report time", "ready", "when will", "duration", "delivery", "days"],
    answer:
      "Turnaround depends on the specimen and the test — our team will give you an accurate timeline for your case. The fastest way is to ask us directly:",
    action: { type: "contact" },
  },
  {
    id: "reports",
    label: "Reports login",
    keywords: ["report", "reports", "login", "log in", "result", "results", "portal", "download report", "online report"],
    answer:
      "Reports are available through our online reporting portal. Use the ‘Reports Login’ button at the top of the site.",
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
    keywords: ["doctor", "doctors", "pathologist", "pathologists", "team", "physician", "physicians", "leadership", "consultant", "for clinicians", "clinician", "clinicians", "arpan", "gandhi", "ashok", "yadav", "director", "founder"],
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
    keywords: ["case", "case study", "case studies", "newsletter", "blog", "research", "publication", "publications", "guideline", "guidelines", "reference", "references", "who classification", "asco", "cap"],
    answer:
      "We publish de-identified case studies for referring doctors, alongside the classifications and guidelines our reporting is built on. Have a look:",
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
    keywords: ["faq", "faqs", "question", "questions", "doubt", "doubts", "frequently", "common questions", "help"],
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
