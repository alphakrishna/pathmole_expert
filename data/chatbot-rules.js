/* =============================================================
   PathMole Expert Lab — Chatbot rules (edit answers here)
   Rule-based only. No AI, no backend.
   Each rule: { id, label, keywords[], answer, action }
   action types:
     { type: "link", href, text }   → shows a link button
     { type: "contact" }            → shows Call / WhatsApp buttons
     { type: "none" }               → answer only
   HARD RULE: never put a price anywhere. Pricing → { type: "contact" }.
   ============================================================= */
const CHATBOT_CONFIG = {
  greeting:
    "Hi! I'm the PathMole assistant. I can help you find a test, learn about our services, or reach the lab. What do you need?",
  phone: "+919899822375",
  whatsapp: "919899822375",
  // quick-reply buttons shown first (by rule id)
  menu: ["find-test", "services", "timings", "location", "reports", "pricing"],
  fallback:
    "I'm not sure about that one. The quickest way is to message or call the lab directly — our team will help.",
};

const CHATBOT_RULES = [
  {
    id: "find-test",
    label: "Find a test",
    keywords: ["test", "biopsy", "histopathology", "molecular", "ihc", "fish", "ngs", "mutation", "egfr", "her2", "symptom", "which test", "panel"],
    answer:
      "Tell me the test name or the symptom/indication, and I'll point you to it. You can also browse the full list by category.",
    action: { type: "link", href: "tests.html", text: "Browse all tests" },
  },
  {
    id: "services",
    label: "Our services",
    keywords: ["service", "services", "histopathology", "molecular", "diagnostics", "what do you do", "ihc", "immunohistochemistry"],
    answer:
      "We're a specialist Histopathology & Molecular Diagnostics referral lab — including IHC and predictive marker panels.",
    action: { type: "link", href: "services.html", text: "See our services" },
  },
  {
    id: "timings",
    label: "Timings",
    keywords: ["time", "timing", "hours", "open", "close", "when", "working"],
    answer: "We're open daily, 11:00 AM – 11:00 PM.",
    action: { type: "none" },
  },
  {
    id: "location",
    label: "Location",
    keywords: ["location", "address", "where", "map", "directions", "reach", "gurugram", "sector 6"],
    answer:
      "We're at Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana).",
    action: { type: "link", href: "contact.html", text: "Contact & directions" },
  },
  {
    id: "reports",
    label: "Reports login",
    keywords: ["report", "reports", "login", "result", "results", "portal", "download"],
    answer:
      "Reports are available through our online reporting portal. Use the ‘Reports Login’ button at the top of the site.",
    action: { type: "none" },
  },
  {
    id: "patient-form",
    label: "Patient form",
    keywords: ["form", "patient form", "download form", "requisition"],
    answer: "You can download the patient form from our Patients page and fill it offline.",
    action: { type: "link", href: "patients.html", text: "Patients page" },
  },
  {
    id: "case-studies",
    label: "Case studies",
    keywords: ["case", "case study", "case studies", "newsletter", "blog"],
    answer: "We publish de-identified case studies for referring doctors. Have a look:",
    action: { type: "link", href: "case-studies/", text: "View case studies" },
  },
  {
    id: "careers",
    label: "Careers",
    keywords: ["career", "careers", "job", "jobs", "hiring", "vacancy"],
    answer: "We'd love to hear from you. Current openings are listed on our Careers page.",
    action: { type: "link", href: "careers.html", text: "See careers" },
  },
  {
    id: "pricing",
    label: "Pricing",
    keywords: ["price", "cost", "charges", "fee", "fees", "rate", "how much", "rates", "pricing"],
    answer:
      "We share pricing directly so we can guide you accurately. Please contact the lab and our team will help.",
    action: { type: "contact" }, // renders Call / WhatsApp — never a price
  },
  {
    id: "contact",
    label: "Contact us",
    keywords: ["contact", "call", "phone", "whatsapp", "email", "talk", "enquiry", "reach"],
    answer: "Happy to help — reach us here:",
    action: { type: "contact" },
  },
];
