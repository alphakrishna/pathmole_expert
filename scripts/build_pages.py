# -*- coding: utf-8 -*-
"""
PathMole Expert Lab — static page generator.
Generates all inner pages from ONE shared shell so the top-bar / nav / footer
stay identical to index.html. Re-run after editing the shell or page content:
    python scripts/build_pages.py
This script is a DEV TOOL — do NOT upload it to public_html (ship the .html only).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV_ITEMS = [
    ("index.html", "HOME", "home"),
    ("about.html", "ABOUT", "about"),
    ("services.html", "SERVICES", "services"),
    ("tests.html", "TESTS", "tests"),
    ("case-studies/", "RESEARCH", "case-studies"),
    ("partner.html", "PARTNER WITH US", "partner"),
    ("contact.html", "CONTACT", "contact"),
]
MOBILE_ITEMS = [
    ("index.html", "HOME"), ("about.html", "ABOUT"), ("services.html", "SERVICES"),
    ("training-institute.html", "TRAINING INSTITUTE"),
    ("tests.html", "TESTS"), ("quality.html", "QUALITY"), ("gallery.html", "GALLERY"),
    ("videos.html", "VIDEOS"), ("case-studies/", "RESEARCH"),
    ("patients.html", "PATIENTS"),
    ("physicians.html", "PHYSICIANS"), ("faq.html", "FAQ"), ("careers.html", "CAREERS"),
    ("partner.html", "PARTNER WITH US"),
    ("contact.html", "CONTACT"),
]


def nav_html(active, p):
    links = ""
    for href, label, key in NAV_ITEMS:
        cls = ' class="active"' if key == active else ""
        links += '        <li><a href="{p}{href}"{cls}>{label}</a></li>\n'.format(
            p=p, href=href, cls=cls, label=label)
    mob = ""
    for href, label in MOBILE_ITEMS:
        mob += '        <li><a href="{p}{href}">{label}</a></li>\n'.format(p=p, href=href, label=label)
    return """  <div class="top-bar">
    <div class="container top-bar-inner">
      <span class="top-bar-item">&#128222; <a href="tel:+919899822375">+91 98998 22375</a></span>
      <span class="top-bar-item hours">&#128340; Open daily, 8:00 AM &ndash; 8:00 PM</span>
      <div class="top-bar-actions">
        <a class="top-bar-cta" href="tel:+919899822375">Call Now</a>
        <a class="top-bar-cta wa" href="https://wa.me/919899822375" target="_blank" rel="noopener noreferrer">WhatsApp</a>
        <a class="top-bar-reports" href="https://lab.flabslis.com/doctor_report/6a7ec279748559c99815bded/68847dda7bf95259b914aae6" target="_blank" rel="noopener noreferrer">Reports Login &#8599;</a>
      </div>
    </div>
  </div>

  <nav class="site-nav" id="site-nav">
    <div class="container nav-inner">
      <a href="{p}index.html" class="nav-logo"><img src="{p}assets/logo.png" alt="PathMole Expert Lab" /></a>
      <ul class="nav-links">
{links}      </ul>
      <button id="menu-toggle" class="menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" /></svg>
      </button>
    </div>
    <div id="mobile-menu" class="mobile-menu">
      <ul>
{mob}        <li><a href="https://lab.flabslis.com/doctor_report/6a7ec279748559c99815bded/68847dda7bf95259b914aae6" target="_blank" rel="noopener noreferrer">REPORTS LOGIN &#8599;</a></li>
      </ul>
    </div>
  </nav>
""".format(p=p, links=links, mob=mob)


def footer_html(p):
    return """  <footer class="site-footer">
    <div class="container">
      <div class="footer-cols">
        <div class="footer-brand">
          <img src="{p}assets/logo-white-bg.png" alt="PathMole Expert Lab" />
          <p>Specialist Histopathology &amp; Molecular Diagnostics referral laboratory, Sector 6, Gurugram (Haryana).</p>
          <p style="margin-top:.6rem;font-style:italic;color:rgba(255,255,255,.5)">Precision in Diagnosis. Confidence in Care.</p>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <a href="{p}training-institute.html">Training Institute</a>
          <a href="{p}histopathology.html">Histopathology</a>
          <a href="{p}cytopathology.html">Cytopathology</a>
          <a href="{p}molecular-diagnostics.html">Molecular Diagnostics</a>
          <a href="{p}tests.html">Test List</a>
          <a href="{p}quality.html">Quality</a>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <a href="{p}about.html">About</a>
          <a href="{p}case-studies/">Case Studies &amp; Research</a>
          <a href="{p}partner.html">Partner With Us</a>
          <a href="{p}patients.html">Patients</a>
          <a href="{p}careers.html">Careers</a>
        </div>
        <div class="footer-col footer-contact">
          <h4>Contact</h4>
          <p>Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana)</p>
          <p>&#128222; <a href="tel:+919899822375">+91 98998 22375</a><br>&#9993; <a href="mailto:pathmolelab@gmail.com">pathmolelab@gmail.com</a></p>
          <p>&#128340; Open daily, 8:00 AM &ndash; 8:00 PM</p>
        </div>
      </div>
      <div class="footer-bottom">
        <span class="footer-copy">&copy; 2026 PathMole Expert Lab. All rights reserved.</span>
        <!-- Social links hidden for now: client will supply real Facebook / Instagram / LinkedIn URLs.
             To enable, uncomment this block and replace each "#" href.
        <div class="footer-social">
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0022 12z"/></svg></a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.3 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .3-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.3-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.3 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.1A6.7 6.7 0 1018.7 12 6.7 6.7 0 0012 5.3zm0 11a4.3 4.3 0 114.3-4.3 4.3 4.3 0 01-4.3 4.3zm6.9-11.3a1.6 1.6 0 11-1.6-1.6 1.6 1.6 0 011.6 1.6z"/></svg></a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M20.4 3H3.6A.6.6 0 003 3.6v16.8a.6.6 0 00.6.6h16.8a.6.6 0 00.6-.6V3.6a.6.6 0 00-.6-.6zM8.3 18.3H5.5V9.7h2.8v8.6zM6.9 8.5a1.6 1.6 0 111.6-1.6 1.6 1.6 0 01-1.6 1.6zm11.4 9.8h-2.8v-4.2c0-1 0-2.3-1.4-2.3s-1.6 1.1-1.6 2.2v4.3h-2.8V9.7h2.7v1.2h.1a3 3 0 012.6-1.4c2.8 0 3.4 1.9 3.4 4.3v4.5z"/></svg></a>
        </div>
        -->
      </div>
    </div>
  </footer>

  <button id="back-to-top" class="back-to-top" aria-label="Back to top">
    <svg fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 15.75l7.5-7.5 7.5 7.5" /></svg>
  </button>

  <button id="back-page" class="back-page" data-home="{p}index.html" aria-label="Go back to the previous page">
    <span class="back-page-ico" aria-hidden="true"><svg fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5L3 12m0 0l7.5-7.5M3 12h18" /></svg></span>
    <span>Back</span>
  </button>

  <div id="chatbot"></div>

  <script src="{p}js/main.js" defer></script>
  <script src="{p}data/chatbot-rules.js" defer></script>
  <script src="{p}js/chatbot.js" defer></script>
""".format(p=p)


def page(filename, title, desc, active, main, prefix="", extra_scripts=""):
    p = prefix
    head = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXX');
  </script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="https://[DOMAIN]/{canon}" />
  <meta property="og:title" content="{title} — PathMole Expert Lab" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:image" content="{p}assets/logo-white-bg.png" />
  <title>{title} — PathMole Expert Lab</title>
  <link rel="icon" href="{p}assets/favicon.svg" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet" media="print" onload="this.media='all'" />
  <noscript><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap" rel="stylesheet" /></noscript>
  <link rel="stylesheet" href="{p}css/style.css" />
</head>
<body>
""".format(desc=desc, title=title, p=p, canon=filename.replace("index.html", "") if filename.endswith("case-studies/index.html") else filename)

    html = head + nav_html(active, p) + "\n" + main + "\n" + footer_html(p).replace(
        '  <script src="{p}js/chatbot.js" defer></script>\n'.format(p=p),
        '  <script src="{p}js/chatbot.js" defer></script>\n{extra}'.format(p=p, extra=extra_scripts)
    ) + "\n</body>\n</html>\n"

    out = os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(out), exist_ok=True) if os.path.dirname(filename) else None
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("wrote", filename)


def phero(title, sub, active_label, prefix=""):
    crumb = '<div class="breadcrumb"><a href="{p}index.html">Home</a> / {t}</div>'.format(p=prefix, t=active_label)
    return """  <header class="page-hero">
    <div class="container page-hero-inner">
      {crumb}
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
  </header>
""".format(crumb=crumb, title=title, sub=sub)


def subhero(title, sub, prefix=""):
    """Page hero for a Services sub-page — breadcrumb Home / Services / <title>."""
    crumb = ('<div class="breadcrumb"><a href="{p}index.html">Home</a> / '
             '<a href="{p}services.html">Services</a> / {t}</div>').format(p=prefix, t=title)
    return """  <header class="page-hero">
    <div class="container page-hero-inner">
      {crumb}
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
  </header>
""".format(crumb=crumb, title=title, sub=sub)


def cta_band(prefix=""):
    return """  <section class="section cta-band">
    <div class="container">
      <h2>Refer a case or start a conversation</h2>
      <p>Tell us what you need — our team will help with sample requirements, turnaround, and reporting.</p>
      <div class="cta-pair">
        <a href="{p}contact.html#enquiry" class="btn-primary on-navy">Submit Enquiry</a>
        <a href="https://wa.me/919899822375" target="_blank" rel="noopener noreferrer" class="btn-secondary on-navy">Call / WhatsApp</a>
      </div>
    </div>
  </section>
""".format(p=prefix)


# ---------------- PAGE CONTENT ----------------
PAGES = []

# ABOUT
PAGES.append(dict(filename="about.html", title="About the Lab", active="about",
    desc="About PathMole Expert Lab — a specialist Histopathology & Molecular Diagnostics referral laboratory in Gurugram, managed by highly experienced doctors.",
    main=phero("About the Lab", "The science of histopathology and molecular diagnostics, applied to the decisions clinicians make every day.", "About") + """
  <section class="section">
    <div class="container grid grid-2" style="align-items:center">
      <div class="reveal">
        <span class="eyebrow">Our story</span>
        <h2>Where science meets clinical decision-making</h2>
        <p>Our Histopathology &amp; Molecular Biology Laboratory has been established with a simple objective: to provide dependable diagnostic information that helps clinicians make better decisions.</p>
        <p>The laboratory brings together two complementary areas of modern diagnostic medicine. <strong>Histopathology</strong> allows us to understand disease through the examination of tissues and cells. <strong>Molecular diagnostics</strong> allows us to look deeper &mdash; at DNA, RNA, microorganisms and molecular alterations that may not be visible through conventional microscopy alone. Together, these disciplines provide a more comprehensive approach to diagnosis.</p>
      </div>
      <div class="reveal">
        <figure class="about-figure">
          <img src="image/lab_photo.webp" alt="Inside PathMole Expert Lab — the histopathology and molecular diagnostics facility at Shri JP Tower, Sector 6, Gurugram." loading="lazy" width="1200" height="800" />
          <figcaption><strong>Shri JP Tower, New Railway Road</strong><span class="map-card-sub">Opp. Fire Station, Sector 6, Gurugram (Haryana)</span><p>A modern, technology-enabled laboratory with a roadmap toward digital pathology and advanced molecular testing.</p></figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container grid grid-2" style="gap:2.5rem">
      <div class="reveal">
        <div class="mini-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z"/></svg></div>
        <span class="eyebrow">Built around quality</span>
        <h2>Quality begins before the microscope</h2>
        <p>Our laboratory processes are designed around a clear set of guiding principles:</p>
        <ul class="principle-chips">
          <li>Accuracy</li>
          <li>Quality</li>
          <li>Traceability</li>
          <li>Timeliness</li>
          <li>Patient Safety</li>
        </ul>
        <p>We recognise that laboratory quality begins long before a specimen reaches the microscope or analyser. Proper specimen collection, identification, transportation, processing, testing, interpretation and reporting are all essential components of a reliable diagnostic service.</p>
      </div>
      <div class="reveal">
        <div class="mini-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div>
        <span class="eyebrow">Clinician-centric diagnostics</span>
        <h2>Reports that mean something</h2>
        <p>A laboratory report should not merely present numbers or microscopic findings. It should provide information that is meaningful in the clinical context. Our approach therefore emphasises:</p>
        <ul class="tick-list">
          <li>Clear and structured reporting</li>
          <li>Appropriate clinical correlation</li>
          <li>Communication with treating clinicians when required</li>
          <li>Defined turnaround times</li>
          <li>Appropriate test selection</li>
          <li>Quality assurance at every stage</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Technology &amp; innovation</span><h2>Modern tools, experienced minds</h2><p>Our laboratory is being developed with an emphasis on appropriate technology that improves accuracy, efficiency, traceability and diagnostic capability.</p></div>
      <div class="grid grid-4">
        <article class="card reveal"><div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"/></svg></div><h3>Histopathology systems</h3><p>Modern tissue-processing and advanced staining techniques.</p></article>
        <article class="card reveal"><div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M8 3c2 3 2 5 0 8s-2 5 0 8m8-16c-2 3-2 5 0 8s2 5 0 8M7 7h10M7 17h10"/></svg></div><h3>Molecular platforms</h3><p>Molecular amplification and PCR-based diagnostic technologies.</p></article>
        <article class="card reveal"><div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M8.25 3v1.5M4.5 8.25H3m18 0h-1.5M4.5 12H3m18 0h-1.5m-15 3.75H3m18 0h-1.5M8.25 19.5V21M12 3v1.5m0 15V21m3.75-18v1.5m0 15V21m-9-1.5h10.5a2.25 2.25 0 002.25-2.25V6.75a2.25 2.25 0 00-2.25-2.25H6.75A2.25 2.25 0 004.5 6.75v10.5a2.25 2.25 0 002.25 2.25zm.75-12h9v9h-9v-9z"/></svg></div><h3>Digital workflows</h3><p>Laboratory information systems and data-driven quality monitoring.</p></article>
        <article class="card reveal"><div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 006.16-12.12A14.98 14.98 0 009.631 8.41m5.96 5.96a14.926 14.926 0 01-5.841 2.58m-.119-8.54a6 6 0 00-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 00-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 01-2.448-2.448 14.9 14.9 0 01.06-.312m-2.24 2.39a4.493 4.493 0 00-1.757 4.306 4.493 4.493 0 004.306-1.758M16.5 9a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"/></svg></div><h3>Future-ready</h3><p>A roadmap toward digital pathology capabilities.</p></article>
      </div>
      <p class="enabler-note reveal">Technology is an enabler &mdash; it should <em>support</em>, not replace, professional expertise:<br><strong>experienced professionals + reliable processes + appropriate technology + quality culture</strong>.</p>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Leadership</span><h2>Clinical &amp; laboratory leadership</h2></div>
      <div class="grid grid-2" style="max-width:900px;margin:0 auto">
        <article class="card reveal leader-card">
          <div class="leader-head">
            <img class="leader-photo leader-photo--fill" src="assets/dr-arpan-gandhi.png" alt="Dr. Arpan Gandhi" loading="lazy" width="200" height="200">
            <div>
              <h3>Dr. Arpan Gandhi</h3>
              <div class="leader-tags"><span class="leader-tag">Senior Diagnostics Leader</span><span class="leader-tag">Healthcare Strategist</span><span class="leader-tag">Ocular Pathology Specialist</span><span class="leader-tag">Quality Systems Expert</span></div>
            </div>
          </div>
          <p>Nearly three decades in diagnostic medicine, healthcare leadership and medical education &mdash; across corporate labs, hospital networks and diagnostic startups.</p>
          <ul class="tick-list leader-points">
            <li>Subspecialty in ocular pathology &amp; oncology diagnostics</li>
            <li>CAP internal auditor since 1999 &middot; NABL quality expert</li>
            <li>Set up COVID-19 RT-PCR laboratories</li>
            <li>Mentored 200+ residents, fellows &amp; lab professionals</li>
          </ul>
        </article>
        <article class="card reveal leader-card">
          <div class="leader-head">
            <img class="leader-photo" src="assets/dr-ashok-yadav.jpg" alt="Dr. Ashok Yadav" loading="lazy" width="200" height="200">
            <div>
              <h3>Dr. Ashok Yadav</h3>
              <div class="leader-tags"><span class="leader-tag">Ph.D. Biotechnology</span><span class="leader-tag">MSc. Clinical Microbiology</span><span class="leader-tag">Quality &amp; Technology Leader</span><span class="leader-tag">Academic Mentor</span></div>
            </div>
          </div>
          <p>Over 22 years across leading pathology and diagnostic laboratories in India &mdash; pairing scientific depth with quality leadership.</p>
          <ul class="tick-list leader-points">
            <li>Built and led a leading North-India pathology &amp; diagnostic lab</li>
            <li>Expert in quality management systems &amp; advanced diagnostics</li>
            <li>10+ research publications in national &amp; international journals</li>
            <li>Faculty &amp; mentor across universities and academic institutions</li>
          </ul>
        </article>
      </div>
    </div>
  </section>
""" + cta_band()))

# SERVICES
PAGES.append(dict(filename="services.html", title="Services", active="services",
    desc="Services at PathMole Expert Lab — Histopathology, Molecular Diagnostics, and Immunohistochemistry for referring clinicians.",
    main=phero("Our Services", "Histopathology, cytopathology and molecular diagnostics &mdash; accurate, reproducible and clinically relevant reporting &mdash; alongside a training institute for the next generation of lab professionals.", "Services") + """
  <section class="section">
    <div class="container grid grid-2" style="gap:2.5rem;align-items:center">
      <div class="reveal">
        <span class="eyebrow">PathMole Training Institute</span>
        <h2>Learn. Practice. <span class="text-pink">Excel.</span></h2>
        <p>An upcoming initiative of PATHMOLE EXPERT LLP &mdash; practical, structured and industry-relevant training for healthcare and laboratory professionals, bridging theoretical knowledge with hands-on laboratory experience.</p>
        <a href="training-institute.html" class="btn-secondary" style="margin-top:1rem">Explore the Training Institute &rarr;</a>
      </div>
      <div class="reveal">
        <div class="map-card"><div class="map-card-head">Training Institute</div><div class="map-card-body"><strong>Building people who build better diagnostics</strong><p>Histopathology &amp; laboratory techniques, molecular diagnostics, quality &amp; accreditation, laboratory operations, and diagnostic leadership.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Histopathology</span>
        <h2>Tissue diagnosis you can <span class="text-pink">rely on</span></h2>
        <p>Routine and complex surgical specimens, histochemical stains and immunohistochemistry where indicated &mdash; accurate, reproducible reporting you can act on. What we offer:</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><rect x="6.5" y="2.75" width="11" height="18.5" rx="1.8" fill="#fff" fill-opacity=".13"/><path d="M6.5 6.75h11v-2.2a1.8 1.8 0 0 0-1.8-1.8H8.3a1.8 1.8 0 0 0-1.8 1.8z" fill="#fff" fill-opacity=".24"/><rect x="6.5" y="2.75" width="11" height="18.5" rx="1.8"/><path d="M6.5 6.75h11"/><circle cx="12" cy="14" r="2.9" fill="#fff" fill-opacity=".3"/><circle cx="12" cy="14" r="2.9"/></svg></div>
          <h3>Specimens</h3>
          <ul class="tick-list"><li>Routine biopsy examination</li><li>Small and large surgical specimens</li><li>Gastrointestinal biopsies</li><li>Gynecological specimens</li></ul>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.25" fill="#fff" fill-opacity=".13"/><circle cx="10.5" cy="10.5" r="6.25"/><path d="M15.4 15.4L20.5 20.5" stroke-width="2"/><circle cx="10.5" cy="10.5" r="2.4" fill="#fff" fill-opacity=".34"/><circle cx="10.5" cy="10.5" r="2.4"/></svg></div>
          <h3>Conditions</h3>
          <ul class="tick-list"><li>Head and neck specimens</li><li>Skin and soft tissue specimens</li><li>Inflammatory and infectious conditions</li><li>Benign and malignant lesions</li></ul>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.2c0 0 5.6 5.9 5.6 9.9a5.6 5.6 0 0 1-11.2 0c0-4 5.6-9.9 5.6-9.9z" fill="#fff" fill-opacity=".16"/><path d="M12 3.2c0 0 5.6 5.9 5.6 9.9a5.6 5.6 0 0 1-11.2 0c0-4 5.6-9.9 5.6-9.9z"/><path d="M9.4 13.6a2.6 2.6 0 0 0 2.6 2.6"/></svg></div>
          <h3>Techniques</h3>
          <ul class="tick-list"><li>Histochemical stains</li><li>Immunohistochemistry, where indicated</li><li>Specialised pathology consultation</li></ul>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Cytopathology</span>
        <h2>Diagnosis at the level of <span class="text-pink">cells</span></h2>
        <p>Evaluation of cells from various body sites and fluids for the detection and diagnosis of disease &mdash; a valuable, minimally invasive complement to tissue histopathology. What we offer:</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M10 11.8v4.7a2 2 0 0 0 4 0v-4.7z" fill="#fff" fill-opacity=".28"/><path d="M9 3h6"/><path d="M10 3v13.5a2 2 0 0 0 4 0V3"/><path d="M10 11.8h4"/><circle cx="12.1" cy="14.3" r=".55" fill="#fff"/></svg></div>
          <h3>Sample types</h3>
          <p>Cells from a range of body sites and fluids &mdash; guidance on collection, fixation and transport on request.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M7.7 13.7l2.6 2.6 6-6-2.6-2.6z" fill="#fff" fill-opacity=".2"/><path d="M7.7 13.7l2.6 2.6 6-6-2.6-2.6z"/><path d="M9 15l-3.5 3.5"/><path d="M15 9l3.4-3.4"/><path d="M17.1 4.2l2.7 2.7"/><path d="M10.7 12.6l1.5 1.5"/><path d="M12.5 10.8l1 1"/></svg></div>
          <h3>Minimally invasive</h3>
          <p>A gentler sampling route that can answer the clinical question with less discomfort for the patient.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M6 4.5A1.5 1.5 0 0 1 7.5 3H14l4 4v11.5A1.5 1.5 0 0 1 16.5 20h-9A1.5 1.5 0 0 1 6 18.5z" fill="#fff" fill-opacity=".13"/><path d="M14 3v4h4z" fill="#fff" fill-opacity=".28"/><path d="M6 4.5A1.5 1.5 0 0 1 7.5 3H14l4 4v11.5A1.5 1.5 0 0 1 16.5 20h-9A1.5 1.5 0 0 1 6 18.5z"/><path d="M14 3v4h4"/><path d="M8.5 13l2 2 3.5-3.6"/></svg></div>
          <h3>Clinically correlated</h3>
          <p>Findings are interpreted alongside histopathology and clinical information so results are meaningful in context.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Molecular biology &amp; molecular diagnostics</span>
        <h2>Testing beyond <span class="text-pink">the microscope</span></h2>
        <p>DNA- and RNA-based testing &mdash; infectious agents, genetic targets, mutation and marker analysis, oncology-related and targeted PCR investigations. Rapid, specific and clinically actionable. What we offer:</p>
      </div>
      <div class="grid grid-2" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3c2 3 2 5 0 8s-2 5 0 8"/><path d="M16 3c-2 3-2 5 0 8s2 5 0 8"/><path d="M8.4 6h7.2"/><path d="M8 12h8"/><path d="M8.4 18h7.2"/><circle cx="8.4" cy="6" r=".75" fill="#fff"/><circle cx="15.6" cy="6" r=".75" fill="#fff"/><circle cx="8.4" cy="18" r=".75" fill="#fff"/><circle cx="15.6" cy="18" r=".75" fill="#fff"/></svg></div>
          <h3>Molecular diagnostic applications</h3>
          <ul class="tick-list"><li>Infectious disease diagnosis</li><li>Detection of bacterial and viral pathogens</li><li>Identification of specific genetic targets</li><li>Mutation and molecular marker analysis</li><li>Oncology-related molecular testing</li><li>Targeted PCR-based investigations</li><li>Other specialised molecular assays</li></ul>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 3h7v2.2l-2 4V16.2a1.5 1.5 0 0 1-3 0V9.2l-2-4z" fill="#fff" fill-opacity=".14"/><path d="M10.9 12h2.2v4.2a1.1 1.1 0 0 1-2.2 0z" fill="#fff" fill-opacity=".32"/><path d="M8.5 3h7v2.2l-2 4V16.2a1.5 1.5 0 0 1-3 0V9.2l-2-4z"/><path d="M8.5 5.2h7"/></svg></div>
          <h3>PCR-based diagnostics</h3>
          <p>Polymerase Chain Reaction (PCR) is one of the most important technologies in modern molecular diagnostics. It allows specific regions of DNA or RNA to be amplified and detected, making it possible to identify targets that may be difficult or impossible to detect using conventional methods alone.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Specialised diagnostic support</span>
        <h2>Clinician-focused <span class="text-pink">interpretation</span></h2>
        <p>Consultation and correlation of laboratory findings with clinical information, so results are meaningful in the clinical context &mdash; not just numbers on a report. What we offer:</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M6.5 3H14l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 6 19V4.5A1.5 1.5 0 0 1 6.5 3z" fill="#fff" fill-opacity=".13"/><path d="M14 3v4h4z" fill="#fff" fill-opacity=".28"/><path d="M6.5 3H14l4 4v12a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 6 19V4.5A1.5 1.5 0 0 1 6.5 3z"/><path d="M14 3v4h4"/><path d="M8.5 12h7"/><path d="M8.5 15h7"/><path d="M8.5 18h4.5"/></svg></div>
          <h3>Decision-ready reports</h3>
          <p>Reports laid out to put the findings that guide management front and centre.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h1v3l4-3h7a2 2 0 0 0 2-2z" fill="#fff" fill-opacity=".15"/><path d="M20 6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h1v3l4-3h7a2 2 0 0 0 2-2z"/><circle cx="8.4" cy="9.5" r=".95" fill="#fff"/><circle cx="12" cy="9.5" r=".95" fill="#fff"/><circle cx="15.6" cy="9.5" r=".95" fill="#fff"/></svg></div>
          <h3>Pathologist consultation</h3>
          <p>A pathologist available to talk a case through whenever it needs discussion or clarification.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M10.5 4.2a1.7 1.7 0 1 1 3.4 0c0 .5-.2.8-.4 1.1-.2.3-.4.6-.4 1 0 .4.3.6.7.6 1.1 0 2.2-.1 3.3-.3.1 1.1.2 2.2.2 3.3 0 .4.2.7.6.7.4 0 .7-.2 1-.4.3-.2.6-.4 1.1-.4a1.7 1.7 0 1 1 0 3.4c-.5 0-.8-.2-1.1-.4-.3-.2-.6-.4-1-.4-.4 0-.6.3-.6.7 0 1.1.1 2.2.3 3.3-1.1.2-2.2.3-3.3.3-.4 0-.7-.2-.7-.6 0-.4.2-.7.4-1 .2-.3.4-.6.4-1.1a1.7 1.7 0 0 0-3.4 0c0 .5.2.8.4 1.1.2.3.4.6.4 1 0 .4-.3.6-.7.6-1.1 0-2.2-.1-3.3-.3.2-1.1.3-2.2.3-3.3 0-.4-.2-.7-.6-.7-.4 0-.7.2-1 .4-.3.2-.6.4-1.1.4a1.7 1.7 0 1 1 0-3.4c.5 0 .8.2 1.1.4.3.2.6.4 1 .4.4 0 .6-.3.6-.7 0-1.1-.1-2.2-.3-3.3 1.1-.2 2.2-.3 3.3-.3.4 0 .7.2.7.6 0 .4-.2.7-.4 1-.2.3-.4.6-.4 1.1z" fill="#fff" fill-opacity=".15"/><path d="M10.5 4.2a1.7 1.7 0 1 1 3.4 0c0 .5-.2.8-.4 1.1-.2.3-.4.6-.4 1 0 .4.3.6.7.6 1.1 0 2.2-.1 3.3-.3.1 1.1.2 2.2.2 3.3 0 .4.2.7.6.7.4 0 .7-.2 1-.4.3-.2.6-.4 1.1-.4a1.7 1.7 0 1 1 0 3.4c-.5 0-.8-.2-1.1-.4-.3-.2-.6-.4-1-.4-.4 0-.6.3-.6.7 0 1.1.1 2.2.3 3.3-1.1.2-2.2.3-3.3.3-.4 0-.7-.2-.7-.6 0-.4.2-.7.4-1 .2-.3.4-.6.4-1.1a1.7 1.7 0 0 0-3.4 0c0 .5.2.8.4 1.1.2.3.4.6.4 1 0 .4-.3.6-.7.6-1.1 0-2.2-.1-3.3-.3.2-1.1.3-2.2.3-3.3 0-.4-.2-.7-.6-.7-.4 0-.7.2-1 .4-.3.2-.6.4-1.1.4a1.7 1.7 0 1 1 0-3.4c.5 0 .8.2 1.1.4.3.2.6.4 1 .4.4 0 .6-.3.6-.7 0-1.1-.1-2.2-.3-3.3 1.1-.2 2.2-.3 3.3-.3.4 0 .7.2.7.6 0 .4-.2.7-.4 1-.2.3-.4.6-.4 1.1z"/></svg></div>
          <h3>Integrated diagnostics</h3>
          <p>Tissue and molecular results read together, so each informs the other where it matters.</p>
        </article>
      </div>
      <div class="center" style="margin-top:2.5rem"><a href="tests.html" class="btn-secondary">Browse the test list &rarr;</a></div>
    </div>
  </section>
""" + cta_band()))

# --- SERVICE SUB-PAGES (dedicated page per "What we do" card) ---

# TRAINING INSTITUTE (listed first per client — top of the services order)
PAGES.append(dict(filename="training-institute.html", title="PathMole Training Institute", active="services",
    desc="PathMole Training Institute — practical, structured and industry-relevant training for healthcare and laboratory professionals. An upcoming initiative of PATHMOLE EXPERT LLP.",
    main=subhero("PathMole Training Institute", "Learn. Practice. Excel. &mdash; building skills for the future of diagnostics.") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Building skills for the future of diagnostics</span>
        <h2>Bridging <span class="text-pink">knowledge and practice</span></h2>
        <p>The PathMole Training Institute, an upcoming initiative of <strong>PATHMOLE EXPERT LLP</strong>, is being developed to provide practical, structured, and industry-relevant training for healthcare and laboratory professionals.</p>
        <p>Modern diagnostics is changing rapidly. New technologies, evolving quality standards, molecular techniques, automation, and increasing clinical expectations require professionals to continuously update their knowledge and skills. Our aim is to bridge the gap between theoretical knowledge and practical laboratory experience through focused, hands-on learning.</p>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Who we aim to train</span><h2>Designed for <span class="text-pink">every stage of a career</span></h2><p>Our programmes will be designed for a broad range of healthcare and laboratory professionals.</p></div>
      <div class="grid grid-2" style="max-width:900px;margin:0 auto">
        <article class="card reveal"><ul class="tick-list"><li>Pathology residents and postgraduate students</li><li>Laboratory technicians and technologists</li><li>Pathologists and other healthcare professionals</li></ul></article>
        <article class="card reveal"><ul class="tick-list"><li>Medical and life-science graduates</li><li>Laboratory managers and quality professionals</li><li>Professionals interested in establishing or upgrading diagnostic laboratories</li></ul></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Proposed training areas</span><h2>Practical, <span class="text-pink">hands-on learning</span></h2></div>
      <div class="grid grid-3">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 3.75H6.912a2.25 2.25 0 00-2.15 1.588L2.35 13.177a2.25 2.25 0 00-.1.661V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 00-2.15-1.588H15M2.25 13.5h3.86a2.25 2.25 0 012.012 1.244l.256.512a2.25 2.25 0 002.013 1.244h3.218a2.25 2.25 0 002.013-1.244l.256-.512a2.25 2.25 0 012.013-1.244h3.859M12 3v8.25m0 0l-3-3m3 3l3-3"/></svg></div>
          <h3>Histopathology &amp; Laboratory Techniques</h3>
          <p>Practical exposure to specimen handling, tissue processing, embedding, microtomy, staining, quality practices, and basic histopathology workflows.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M8 3c2 3 2 5 0 8s-2 5 0 8m8-16c-2 3-2 5 0 8s2 5 0 8M7 7h10M7 17h10"/></svg></div>
          <h3>Molecular Diagnostics</h3>
          <p>Fundamentals of molecular biology, PCR-based techniques, specimen management, contamination prevention, quality control, and interpretation of molecular results.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
          <h3>Laboratory Quality &amp; Accreditation</h3>
          <p>Quality management systems, documentation, quality indicators, internal quality control, non-conformities, corrective actions, and accreditation preparedness.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div>
          <h3>Laboratory Operations &amp; Management</h3>
          <p>Practical learning in workflow design, turnaround time, inventory management, equipment planning, team management, safety, and efficient laboratory operations.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"/></svg></div>
          <h3>Diagnostic Leadership &amp; Professional Development</h3>
          <p>Programmes focused on communication, leadership, team building, decision-making, laboratory management, and developing the next generation of diagnostic professionals.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container grid grid-2" style="gap:2.5rem;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Our training philosophy</span>
        <h2>Knowledge, <span class="text-pink">paired with experience</span></h2>
        <p>We believe that the best laboratory training combines knowledge with experience. Our programmes will emphasise practical demonstrations, real-world laboratory workflows, case-based learning, quality principles, and problem-solving rather than classroom theory alone.</p>
        <p>The PathMole Training Institute will also aim to create opportunities for short-term observerships, workshops, focused certificate programmes, and continuing professional development as the initiative grows.</p>
      </div>
      <div class="reveal">
        <span class="eyebrow">Our vision</span>
        <h2>A centre of <span class="text-pink">excellence</span></h2>
        <p>To develop a centre of excellence for practical diagnostic education and laboratory professional development &mdash; helping create competent, confident, quality-conscious professionals who can contribute meaningfully to patient care.</p>
        <p style="margin-top:.8rem;font-style:italic;color:var(--ink-400)">PathMole Training Institute &mdash; building people who build better diagnostics.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Register your interest</span><h2>Join an <span class="text-pink">upcoming programme</span></h2><p>Tell us your area of interest and we&rsquo;ll keep you informed as programmes, workshops and observerships open.</p></div>
      <div class="notice reveal" style="max-width:760px;margin:0 auto 1.4rem">[PLACEHOLDER: Training Institute registration form &mdash; the client&rsquo;s Google Form will be embedded here, or a matching native form built to the client&rsquo;s field list. Pending the Google Form link / requirements list.]</div>
      <div class="center" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap"><a href="contact.html#enquiry" class="btn-primary">Enquire about training</a><a href="services.html" class="btn-ghost">&larr; Back to all services</a></div>
    </div>
  </section>
""" + cta_band()))

# HISTOPATHOLOGY
PAGES.append(dict(filename="histopathology.html", title="Histopathology", active="services",
    desc="Histopathology at PathMole Expert Lab — detailed microscopic examination of tissue for accurate, reproducible and clinically relevant diagnosis.",
    main=subhero("Histopathology", "Detailed microscopic examination of tissue &mdash; accurate, reproducible and clinically relevant diagnosis.") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Histopathology</span>
        <h2>What we <span class="text-pink">offer</span></h2>
        <p>Histopathology is the microscopic examination of tissue to identify disease and establish a diagnosis. Our service delivers accurate, reproducible tissue reporting you can act on &mdash; across the specimens, conditions and techniques below.</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 3.75H6.912a2.25 2.25 0 00-2.15 1.588L2.35 13.177a2.25 2.25 0 00-.1.661V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 00-2.15-1.588H15M2.25 13.5h3.86a2.25 2.25 0 012.012 1.244l.256.512a2.25 2.25 0 002.013 1.244h3.218a2.25 2.25 0 002.013-1.244l.256-.512a2.25 2.25 0 012.013-1.244h3.859M12 3v8.25m0 0l-3-3m3 3l3-3"/></svg></div>
          <h3>Specimens</h3>
          <ul class="tick-list"><li>Routine biopsy examination</li><li>Small and large surgical specimens</li><li>Gastrointestinal biopsies</li><li>Gynecological specimens</li></ul>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/></svg></div>
          <h3>Conditions</h3>
          <ul class="tick-list"><li>Head and neck specimens</li><li>Skin and soft tissue specimens</li><li>Inflammatory and infectious conditions</li><li>Benign and malignant lesions</li></ul>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"/></svg></div>
          <h3>Techniques</h3>
          <ul class="tick-list"><li>Histochemical stains</li><li>Immunohistochemistry, where indicated</li><li>Specialised pathology consultation</li></ul>
        </article>
      </div>
      <div class="notice reveal" style="margin-top:1.8rem"><strong>From specimen to diagnosis:</strong> Specimen Collection &rarr; Accessioning &rarr; Gross Examination &rarr; Tissue Processing &rarr; Embedding &rarr; Sectioning &rarr; Staining &rarr; Microscopy &rarr; Interpretation &rarr; Reporting. Care at every stage is what makes the final diagnosis dependable.</div>
      <div class="center" style="margin-top:2rem"><a href="services.html" class="btn-ghost">&larr; Back to all services</a></div>
    </div>
  </section>
""" + cta_band()))

# CYTOPATHOLOGY
PAGES.append(dict(filename="cytopathology.html", title="Cytopathology", active="services",
    desc="Cytopathology at PathMole Expert Lab — evaluation of cells from body sites and fluids, a minimally invasive complement to tissue histopathology.",
    main=subhero("Cytopathology", "Evaluation of cells from various body sites and fluids &mdash; a minimally invasive complement to tissue histopathology.") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Cytopathology</span>
        <h2>What we <span class="text-pink">offer</span></h2>
        <p>Cytopathology examines cells from body sites and fluids to detect and diagnose disease. We offer it as a minimally invasive complement to tissue histopathology, with findings correlated to the clinical picture.</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3a9 9 0 100 18 9 9 0 000-18zm0 5a4 4 0 100 8 4 4 0 000-8z"/></svg></div>
          <h3>Sample types</h3>
          <p>Cells from a range of body sites and fluids &mdash; guidance on collection, fixation and transport on request.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg></div>
          <h3>Minimally invasive</h3>
          <p>A gentler sampling route that can answer the clinical question with less discomfort for the patient.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg></div>
          <h3>Clinically correlated</h3>
          <p>Findings are interpreted alongside histopathology and clinical information so results are meaningful in context.</p>
        </article>
      </div>
      <div class="notice reveal" style="margin-top:1.8rem">For specimen requirements and availability, please <a href="contact.html">contact the lab</a> &mdash; our team will guide you on collection, fixation and transport.</div>
      <div class="center" style="margin-top:2rem"><a href="services.html" class="btn-ghost">&larr; Back to all services</a></div>
    </div>
  </section>
""" + cta_band()))

# MOLECULAR DIAGNOSTICS
PAGES.append(dict(filename="molecular-diagnostics.html", title="Molecular Diagnostics", active="services",
    desc="Molecular Diagnostics at PathMole Expert Lab — DNA- and RNA-based testing for rapid, specific and clinically relevant molecular results.",
    main=subhero("Molecular Diagnostics", "DNA- and RNA-based testing &mdash; rapid, specific and clinically relevant molecular results.") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Molecular biology &amp; molecular diagnostics</span>
        <h2>What we <span class="text-pink">offer</span></h2>
        <p>Molecular diagnostics examines genetic material &mdash; DNA and RNA &mdash; to detect pathogens, genetic alterations and the markers that guide treatment. Our molecular laboratory supports rapid, specific testing across the applications below.</p>
      </div>
      <div class="grid grid-2" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3c2 3 2 5 0 8s-2 5 0 8"/><path d="M16 3c-2 3-2 5 0 8s2 5 0 8"/><path d="M8.4 6h7.2"/><path d="M8 12h8"/><path d="M8.4 18h7.2"/><circle cx="8.4" cy="6" r=".75" fill="#fff"/><circle cx="15.6" cy="6" r=".75" fill="#fff"/><circle cx="8.4" cy="18" r=".75" fill="#fff"/><circle cx="15.6" cy="18" r=".75" fill="#fff"/></svg></div>
          <h3>Molecular diagnostic applications</h3>
          <ul class="tick-list"><li>Infectious disease diagnosis</li><li>Detection of bacterial and viral pathogens</li><li>Identification of specific genetic targets</li><li>Mutation and molecular marker analysis</li><li>Oncology-related molecular testing</li><li>Targeted PCR-based investigations</li><li>Other specialised molecular assays</li></ul>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 3h7v2.2l-2 4V16.2a1.5 1.5 0 0 1-3 0V9.2l-2-4z" fill="#fff" fill-opacity=".14"/><path d="M10.9 12h2.2v4.2a1.1 1.1 0 0 1-2.2 0z" fill="#fff" fill-opacity=".32"/><path d="M8.5 3h7v2.2l-2 4V16.2a1.5 1.5 0 0 1-3 0V9.2l-2-4z"/><path d="M8.5 5.2h7"/></svg></div>
          <h3>PCR-based diagnostics</h3>
          <p>Polymerase Chain Reaction (PCR) is one of the most important technologies in modern molecular diagnostics. It allows specific regions of DNA or RNA to be amplified and detected, making it possible to identify targets that may be difficult or impossible to detect using conventional methods alone.</p>
          <p style="margin-top:.8rem;font-style:italic;color:var(--ink-400)">Molecular diagnostics is powerful &mdash; its value depends on doing it correctly, with rigorous control at every stage.</p>
        </article>
      </div>
      <div class="center" style="margin-top:2.5rem;display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap"><a href="tests.html" class="btn-secondary">Browse the test list</a><a href="services.html" class="btn-ghost">&larr; Back to all services</a></div>
    </div>
  </section>
""" + cta_band()))

# SPECIALISED DIAGNOSTIC SUPPORT
PAGES.append(dict(filename="diagnostic-support.html", title="Specialised Diagnostic Support", active="services",
    desc="Specialised Diagnostic Support at PathMole Expert Lab — clinician-focused interpretation, consultation and correlation of laboratory findings.",
    main=subhero("Specialised Diagnostic Support", "Clinician-focused interpretation, consultation and correlation &mdash; results that mean something in context.") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Clinician-focused interpretation</span>
        <h2>Reports that <span class="text-pink">mean something</span></h2>
        <p>Consultation and correlation of laboratory findings with clinical information, so results are meaningful in the clinical context &mdash; not just numbers on a report. We aim to work as an extension of the clinical team, providing results that are accurate, timely, understandable and clinically relevant.</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
          <h3>Clinically relevant reports</h3>
          <p>Reports structured to communicate the information most important for decision-making.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"/></svg></div>
          <h3>Pathologist consultation</h3>
          <p>Direct professional communication when a case requires discussion or clarification.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M7.5 21L3 16.5m0 0L7.5 12M3 16.5h13.5m0-13.5L21 7.5m0 0L16.5 12M21 7.5H7.5"/></svg></div>
          <h3>Integrated diagnostics</h3>
          <p>Histopathology and molecular findings that complement each other when clinically indicated.</p>
        </article>
      </div>
      <p class="center" style="margin-top:1.6rem;font-style:italic;color:var(--ink-400)">When in doubt about the right test or specimen, speak to us before sending the sample.</p>
      <div class="center" style="margin-top:1.4rem"><a href="services.html" class="btn-ghost">&larr; Back to all services</a></div>
    </div>
  </section>
""" + cta_band()))

# TESTS
PAGES.append(dict(filename="tests.html", title="Test List", active="tests",
    desc="Test list at PathMole Expert Lab — histopathology, IHC, molecular, and FISH tests by category. Contact us for availability and details.",
    extra_scripts='  <script src="data/tests.js" defer></script>\n  <script src="js/tests.js" defer></script>\n',
    main=phero("Test List", "Tests grouped by category, with indications. For availability and specifics, please contact the lab.", "Tests") + """
  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Diagnostic menu</span><h2>Tests we <span class="text-pink">perform</span></h2><p>Grouped by discipline &mdash; histopathology, immunohistochemistry, molecular diagnostics, and FISH. Each group is illustrated and explained, with indications listed to help you choose the right test.</p></div>
      <div class="notice reveal" style="margin-bottom:2rem">This list is representative and being finalised. For confirmed availability, sample requirements, and any query &mdash; please <a href="contact.html">contact the lab</a>. Pricing is shared on enquiry.</div>
      <div id="test-list"></div>
    </div>
  </section>
""" + cta_band()))

# CONTACT
PAGES.append(dict(filename="contact.html", title="Contact", active="contact",
    desc="Contact PathMole Expert Lab — Sector 6, Gurugram. Call +91 98998 22375, WhatsApp, or send an enquiry.",
    main=phero("Contact Us", "Refer a case, ask about a test, or request a callback &mdash; we&rsquo;re here to help.", "Contact") + """
  <section class="section">
    <div class="container grid grid-2" style="align-items:stretch;gap:2.5rem">
      <div class="reveal" id="enquiry">
        <span class="eyebrow">Send an enquiry</span>
        <h2>How can we <span class="text-pink">help?</span></h2>
        <p class="lead-sm">Share a few details about the test or case and our team will get back to you promptly.</p>
        <form id="enquiry-form" class="form-card form-grid" style="margin-top:1.2rem" data-subject="New enquiry — PathMole website (Contact)" novalidate>
          <div class="field"><label for="f-name">Name *</label><input id="f-name" name="name" type="text" required /></div>
          <div class="field"><label for="f-org">Clinic / Hospital</label><input id="f-org" name="organisation" type="text" /></div>
          <div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" required /></div>
          <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" /></div>
          <div class="field"><label for="f-msg">Message *</label><textarea id="f-msg" name="message" required placeholder="Tell us about the test or case…"></textarea></div>
          <button type="submit" class="btn-primary">Send Enquiry</button>
          <p class="form-note">This form emails the lab; no health records are stored on the site.</p>
          <p class="form-status" role="status" aria-live="polite"></p>
        </form>
      </div>
      <div class="reveal contact-right">
        <span class="eyebrow">Reach us</span>
        <h2>Visit or <span class="text-pink">call</span></h2>
        <p class="lead-sm">We&rsquo;re on the 1st floor of Shri JP Tower, above Axis Bank &mdash; open every day.</p>
        <div class="info-list" style="margin:1.4rem 0 1.4rem">
          <div class="info-item"><div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/></svg></div><div><strong>Phone / WhatsApp</strong><br><a href="tel:+919899822375">+91 98998 22375</a></div></div>
          <div class="info-item"><div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></div><div><strong>Email</strong><br><a href="mailto:pathmolelab@gmail.com">pathmolelab@gmail.com</a></div></div>
          <div class="info-item"><div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div><div><strong>Hours</strong><br>Open daily, 8:00 AM &ndash; 8:00 PM</div></div>
        </div>
        <div class="map-card-embed">
          <div class="map-embed">
            <iframe
              title="PathMole Expert Lab &mdash; Shri JP Tower, Sector 6, Gurugram"
              src="https://www.google.com/maps?cid=13977963961617259124&z=17&output=embed"
              loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
          </div>
          <div class="map-info">
            <div class="map-info-text">
              <span class="map-here"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg><strong>PathMole Expert Lab</strong></span>
              <p>Building No. 1164/1, 1st Floor, Shri JP Tower (above Axis Bank), New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram, Haryana 122001</p>
            </div>
            <a class="btn-secondary" target="_blank" rel="noopener noreferrer" href="https://maps.app.goo.gl/uc3w1jgqVWJKhQPSA">Get directions &#8599;</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""" + cta_band()))

# QUALITY
PAGES.append(dict(filename="quality.html", title="Quality & Accreditation", active="",
    desc="Quality and accreditation at PathMole Expert Lab — standardised protocols, expert review, and reliable turnaround.",
    main=phero("Quality &amp; Patient Safety", "Built into every step of the diagnostic pathway &mdash; from specimen collection to the final report.", "Quality") + """
  <section class="section"><div class="container">
    <div class="reveal" style="max-width:820px;margin-bottom:2rem">
      <h2>Quality is not a department. It is a culture.</h2>
      <p>In laboratory medicine, even a technically perfect test cannot compensate for a poorly collected, identified or transported specimen. That is why we approach quality across the entire diagnostic pathway.</p>
    </div>
    <div class="section-head reveal"><span class="eyebrow">Our quality framework</span><h2>Quality at every stage</h2></div>
    <div class="grid grid-3">
      <article class="card reveal"><h3>Pre-analytical quality</h3><p>Correct patient identification, specimen collection, labelling, fixation, transportation and accessioning.</p></article>
      <article class="card reveal"><h3>Analytical quality</h3><p>Validated procedures, appropriate controls, standardised techniques and trained personnel.</p></article>
      <article class="card reveal"><h3>Post-analytical quality</h3><p>Result verification, structured reporting, timely communication and appropriate documentation.</p></article>
    </div>
  </div></section>

  <section class="section section--soft"><div class="container grid grid-2" style="gap:2.5rem">
    <div class="reveal">
      <span class="eyebrow">Our commitment</span>
      <h2>How we keep quality consistent</h2>
      <ul class="tick-list">
        <li>Reducing pre-analytical errors</li>
        <li>Maintaining specimen traceability</li>
        <li>Monitoring turnaround time</li>
        <li>Ensuring reproducibility</li>
        <li>Monitoring quality indicators</li>
        <li>Learning from errors and near misses</li>
        <li>Continuing staff education</li>
        <li>Implementing corrective and preventive actions</li>
      </ul>
    </div>
    <div class="reveal">
      <span class="eyebrow">Quality beyond compliance</span>
      <h2>Doing the right thing consistently</h2>
      <p>Accreditation and standards are important. But true laboratory quality goes beyond compliance.</p>
      <p><strong>Quality means doing the right thing consistently &mdash; even when nobody is watching.</strong></p>
      <p class="form-note" style="margin-top:1rem">[PLACEHOLDER: list specific accreditations (e.g. NABL) here ONLY once confirmed by the client.]</p>
    </div>
  </div></section>
""" + cta_band()))

# PHYSICIANS
PAGES.append(dict(filename="physicians.html", title="Physicians", active="",
    desc="The pathologists and team behind PathMole Expert Lab.",
    main=phero("Our Team &amp; For Clinicians", "Experience, expertise and commitment &mdash; working as an extension of your clinical team.", "Physicians") + """
  <section class="section"><div class="container">
    <div class="reveal" style="max-width:820px">
      <span class="eyebrow">Our team</span>
      <h2>Experience. Expertise. Commitment.</h2>
      <p>A diagnostic laboratory is only as strong as the people behind it. Our team brings together professionals with experience in pathology, laboratory operations, technical services, quality management and molecular diagnostics. We build a culture where people are encouraged to follow evidence-based practices, ask questions, communicate openly, learn continuously, take ownership of quality, and put patient safety first.</p>
    </div>
    <div class="grid grid-2" style="max-width:900px;margin:1.6rem auto 0">
      <article class="card reveal leader-card">
        <div class="leader-head">
          <img class="leader-photo leader-photo--fill" src="assets/dr-arpan-gandhi.png" alt="Dr. Arpan Gandhi" loading="lazy" width="200" height="200">
          <div>
            <h3>Dr. Arpan Gandhi</h3>
            <div class="leader-tags"><span class="leader-tag">Senior Diagnostics Leader</span><span class="leader-tag">Healthcare Strategist</span><span class="leader-tag">Ocular Pathology Specialist</span><span class="leader-tag">Quality Systems Expert</span></div>
          </div>
        </div>
        <p>Nearly three decades in diagnostic medicine, healthcare leadership and medical education &mdash; across corporate labs, hospital networks and diagnostic startups.</p>
          <ul class="tick-list leader-points">
            <li>Subspecialty in ocular pathology &amp; oncology diagnostics</li>
            <li>CAP internal auditor since 1999 &middot; NABL quality expert</li>
            <li>Set up COVID-19 RT-PCR laboratories</li>
            <li>Mentored 200+ residents, fellows &amp; lab professionals</li>
          </ul>
      </article>
      <article class="card reveal leader-card">
        <div class="leader-head">
          <img class="leader-photo" src="assets/dr-ashok-yadav.jpg" alt="Dr. Ashok Yadav" loading="lazy" width="200" height="200">
          <div>
            <h3>Dr. Ashok Yadav</h3>
            <div class="leader-tags"><span class="leader-tag">Ph.D. Biotechnology</span><span class="leader-tag">MSc. Clinical Microbiology</span><span class="leader-tag">Quality &amp; Technology Leader</span><span class="leader-tag">Academic Mentor</span></div>
          </div>
        </div>
        <p>Over 22 years across leading pathology and diagnostic laboratories in India &mdash; pairing scientific depth with quality leadership.</p>
          <ul class="tick-list leader-points">
            <li>Built and led a leading North-India pathology &amp; diagnostic lab</li>
            <li>Expert in quality management systems &amp; advanced diagnostics</li>
            <li>10+ research publications in national &amp; international journals</li>
            <li>Faculty &amp; mentor across universities and academic institutions</li>
          </ul>
      </article>
    </div>
  </div></section>

  <section class="section section--soft"><div class="container">
    <div class="section-head reveal"><span class="eyebrow">For clinicians</span><h2>Diagnostics that support clinical decisions</h2><p>We aim to work as an extension of the clinical team &mdash; providing results that are accurate, timely, understandable and clinically relevant.</p></div>
    <div class="grid grid-3">
      <article class="card reveal"><h3>Reliable testing</h3><p>Standardised laboratory processes that hold consistency and quality steady from one case to the next.</p></article>
      <article class="card reveal"><h3>Defined turnaround times</h3><p>Clear, dependable reporting timelines, so you know when to expect a result.</p></article>
      <article class="card reveal"><h3>Reports built for the clinic</h3><p>Reports built around the details that matter most to the treating clinician.</p></article>
      <article class="card reveal"><h3>Pathologist consultation</h3><p>Speak directly with the reporting pathologist whenever a case calls for a closer look.</p></article>
      <article class="card reveal"><h3>Integrated diagnostics</h3><p>Histopathology and molecular findings brought into a single, coherent picture when clinically indicated.</p></article>
      <article class="card reveal"><h3>Specimen submission</h3><p>Talk to us before you send a sample &mdash; test availability and selection, specimen requirements, fixation and transport, sample volume, turnaround times and any special handling.</p></article>
    </div>
    <p class="center" style="margin-top:1.6rem;font-style:italic;color:var(--ink-400)">When in doubt about the right test or specimen, speak to us before sending the sample.</p>
  </div></section>
""" + cta_band()))

# GALLERY
PAGES.append(dict(filename="gallery.html", title="Gallery", active="",
    desc="Facility and equipment at PathMole Expert Lab.",
    main=phero("Gallery", "Our facility and equipment.", "Gallery") + """
  <section class="section"><div class="container"><div class="grid grid-3">
""" + "".join(['    <div class="map-card reveal"><div class="map-card-head">Photo [PLACEHOLDER]</div></div>\n' for _ in range(6)]) + """  </div></div></section>
""" + cta_band()))

# VIDEOS
PAGES.append(dict(filename="videos.html", title="Videos", active="",
    desc="Videos from PathMole Expert Lab.",
    main=phero("Videos", "A closer look at our facility, our people and how we work.", "Videos") + """
  <section class="section"><div class="container"><div class="grid grid-2">
    <div class="map-card reveal"><div class="map-card-head">YouTube embed [PLACEHOLDER]</div></div>
    <div class="map-card reveal"><div class="map-card-head">YouTube embed [PLACEHOLDER]</div></div>
  </div></div></section>
""" + cta_band()))

# PATIENTS
PAGES.append(dict(filename="patients.html", title="Patients", active="",
    desc="Patient information and downloadable form for PathMole Expert Lab.",
    main=phero("For Patients", "Clear, reassuring information — and a form you can fill offline.", "Patients") + """
  <section class="section"><div class="container grid grid-2" style="align-items:center">
    <div class="reveal"><span class="eyebrow">Patient information</span><h2>Coming in for a test?</h2><p>Please carry your prescription / request form and any relevant previous reports. Accurate diagnosis begins with the right specimen and the right test.</p><p>Download the patient form, fill it offline, and bring it with you.</p>
      <a href="assets/pathmole-patient-form.pdf" download class="btn-primary">Download Patient Form (PDF)</a>
      <p class="form-note" style="margin-top:.6rem">[PLACEHOLDER: add the PDF at assets/pathmole-patient-form.pdf]</p>
    </div>
    <div class="reveal"><div class="map-card"><div class="map-card-head">Patient visual [PLACEHOLDER]</div><div class="map-card-body"><strong>Open daily, 8:00 AM &ndash; 8:00 PM</strong><p>Sector 6, Gurugram. Call +91 98998 22375 for any help.</p></div></div></div>
  </div></section>
""" + cta_band()))

# FAQ
PAGES.append(dict(filename="faq.html", title="FAQ", active="",
    desc="Frequently asked questions about PathMole Expert Lab.",
    main=phero("Frequently Asked Questions", "Quick answers — or ask our assistant any time.", "FAQ") + """
  <section class="section"><div class="container" style="max-width:800px">
    <article class="card reveal" style="margin-bottom:1rem"><h3>What are your timings?</h3><p>We&rsquo;re open daily, 8:00 AM – 8:00 PM.</p></article>
    <article class="card reveal" style="margin-bottom:1rem"><h3>Where are you located?</h3><p>Sector 6, Gurugram (Haryana) — full address on our <a href="contact.html">Contact page</a>.</p></article>
    <article class="card reveal" style="margin-bottom:1rem"><h3>How do I get pricing?</h3><p>We share pricing directly on enquiry — please <a href="contact.html">contact the lab</a>.</p></article>
    <article class="card reveal" style="margin-bottom:1rem"><h3>Are case studies patient-identifiable?</h3><p>No. Every case study is fully de-identified, with no patient name, ID, or image.</p></article>
    <article class="card reveal"><h3>How do I access reports?</h3><p>Use the <strong>Reports Login</strong> button at the top of the site. [PLACEHOLDER: portal URL.]</p></article>
  </div></section>
"""))

# CAREERS
PAGES.append(dict(filename="careers.html", title="Careers", active="",
    desc="Careers at PathMole Expert Lab.",
    main=phero("Careers", "Build your career with a specialist histopathology and molecular diagnostics laboratory.", "Careers") + """
  <section class="section"><div class="container" style="max-width:800px">
    <div class="notice reveal" style="margin-bottom:1.5rem">[PLACEHOLDER: current openings. To apply, email <a href="mailto:pathmolelab@gmail.com">pathmolelab@gmail.com</a>.]</div>
    <article class="card reveal"><h3>[PLACEHOLDER: Role title]</h3><p>[PLACEHOLDER: responsibilities and requirements.]</p><a href="mailto:pathmolelab@gmail.com?subject=Application" class="btn-ghost">Apply →</a></article>
  </div></section>
"""))

# 404
PAGES.append(dict(filename="404.html", title="Page Not Found", active="",
    desc="Page not found — PathMole Expert Lab.",
    main="""  <section class="section" style="text-align:center;padding:6rem 0">
    <div class="container">
      <span class="eyebrow">Error 404</span>
      <h1>We couldn&rsquo;t find that page</h1>
      <p style="max-width:520px;margin:1rem auto 2rem">The page may have moved. Let&rsquo;s get you back on track.</p>
      <div class="cta-pair" style="justify-content:center"><a href="index.html" class="btn-primary">Back to home</a><a href="contact.html" class="btn-secondary">Contact us</a></div>
    </div>
  </section>
"""))

# CASE STUDIES & RESEARCH INDEX (subfolder) — Case Studies + Research merged into one page
# ---- Research & References: real external standards, each with its OWN explainer page ----
REF_DISCLAIMER = ("This page summarises a widely used external standard for general educational "
    "purposes. It is not a substitute for the full guideline &mdash; for the definitive criteria, "
    "please refer to the current published version. Our diagnostic reports reference these "
    "standards as part of a commitment to internationally consistent reporting.")

# Hand-built "scene" illustrations (one per reference), in the brand navy+magenta
# palette. viewBox 400x280, primitive shapes only — same illustrative language as the
# consulting explainer pages. Decorative: aria-hidden, no invented factual claims.
ART_WHO = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#E8EAF6" opacity="0.55"/>
  <path d="M102 140 H150" stroke="#9FA8DA" stroke-width="2.5" fill="none"/>
  <path d="M150 70 V210" stroke="#9FA8DA" stroke-width="2.5" fill="none"/>
  <path d="M150 70 H197" stroke="#9FA8DA" stroke-width="2.5" fill="none"/>
  <path d="M150 140 H197" stroke="#9FA8DA" stroke-width="2.5" fill="none"/>
  <path d="M150 210 H197" stroke="#9FA8DA" stroke-width="2.5" fill="none"/>
  <path d="M223 70 H260" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M260 44 V96" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M260 44 H303" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M260 96 H303" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M223 140 H303" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M223 210 H260" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M260 184 V236" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M260 184 H303" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <path d="M260 236 H303" stroke="#C5CAE9" stroke-width="2" fill="none"/>
  <circle cx="82" cy="140" r="20" fill="#232C8E"/>
  <circle cx="82" cy="140" r="10" fill="#C5CAE9"/>
  <circle cx="210" cy="70" r="13" fill="#3949AB"/>
  <circle cx="210" cy="140" r="13" fill="#EC008C"/>
  <circle cx="210" cy="210" r="13" fill="#3949AB"/>
  <circle cx="312" cy="44" r="9" fill="#5C6BC0"/>
  <circle cx="312" cy="96" r="9" fill="#5C6BC0"/>
  <circle cx="312" cy="140" r="9" fill="#F06CAB"/>
  <circle cx="312" cy="184" r="9" fill="#5C6BC0"/>
  <circle cx="312" cy="236" r="9" fill="#5C6BC0"/>
  <circle cx="26" cy="40" r="6" fill="#C5CAE9" opacity="0.8"/>
  <circle cx="366" cy="250" r="5" fill="#F8BBD0" opacity="0.8"/>
  <circle cx="360" cy="26" r="5" fill="#9FA8DA" opacity="0.6"/>
</svg>"""

ART_HER2 = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#FCE4EC" opacity="0.6"/>
  <line x1="46" y1="212" x2="354" y2="212" stroke="#F8BBD0" stroke-width="2"/>
  <circle cx="80" cy="142" r="32" fill="#ffffff" stroke="#F8BBD0" stroke-width="2"/>
  <circle cx="80" cy="142" r="11" fill="#F8BBD0"/>
  <circle cx="160" cy="142" r="32" fill="#ffffff" stroke="#F48FB1" stroke-width="4"/>
  <circle cx="160" cy="142" r="11" fill="#F06CAB"/>
  <circle cx="240" cy="142" r="32" fill="#ffffff" stroke="#EC008C" stroke-width="6" stroke-dasharray="4 3"/>
  <circle cx="240" cy="142" r="11" fill="#EC008C"/>
  <circle cx="320" cy="142" r="32" fill="#FCE4EC" stroke="#C2186A" stroke-width="8"/>
  <circle cx="320" cy="142" r="11" fill="#C2186A"/>
  <rect x="71" y="200" width="18" height="8" rx="2" fill="#F8BBD0"/>
  <rect x="151" y="192" width="18" height="16" rx="2" fill="#F48FB1"/>
  <rect x="231" y="182" width="18" height="26" rx="2" fill="#EC008C"/>
  <rect x="311" y="170" width="18" height="38" rx="2" fill="#C2186A"/>
  <circle cx="30" cy="44" r="6" fill="#F8BBD0" opacity="0.8"/>
  <circle cx="372" cy="60" r="5" fill="#F48FB1" opacity="0.7"/>
  <circle cx="360" cy="240" r="5" fill="#F8BBD0" opacity="0.7"/>
</svg>"""

ART_LUNG = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#E8EAF6" opacity="0.55"/>
  <rect x="193" y="54" width="14" height="58" rx="6" fill="#9FA8DA"/>
  <path d="M200 108 Q172 120 156 150" stroke="#9FA8DA" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M200 108 Q228 120 244 150" stroke="#9FA8DA" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M152 148 Q118 150 110 200 Q106 232 136 232 Q156 232 156 206 L156 154 Q156 148 152 148 Z" fill="#5C6BC0"/>
  <path d="M248 148 Q282 150 290 200 Q294 232 264 232 Q244 232 244 206 L244 154 Q244 148 248 148 Z" fill="#3949AB"/>
  <path d="M44 72 Q66 94 44 116 Q22 138 44 160" stroke="#232C8E" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M76 72 Q54 94 76 116 Q98 138 76 160" stroke="#5C6BC0" stroke-width="3" fill="none" stroke-linecap="round"/>
  <line x1="49" y1="84" x2="71" y2="84" stroke="#9FA8DA" stroke-width="2.5"/>
  <line x1="49" y1="116" x2="71" y2="116" stroke="#9FA8DA" stroke-width="2.5"/>
  <line x1="49" y1="148" x2="71" y2="148" stroke="#9FA8DA" stroke-width="2.5"/>
  <circle cx="266" cy="196" r="20" fill="none" stroke="#EC008C" stroke-width="3"/>
  <circle cx="266" cy="196" r="10" fill="none" stroke="#EC008C" stroke-width="2.5"/>
  <circle cx="266" cy="196" r="3" fill="#EC008C"/>
  <line x1="266" y1="166" x2="266" y2="180" stroke="#EC008C" stroke-width="2.5"/>
  <line x1="266" y1="212" x2="266" y2="226" stroke="#EC008C" stroke-width="2.5"/>
  <line x1="236" y1="196" x2="250" y2="196" stroke="#EC008C" stroke-width="2.5"/>
  <line x1="282" y1="196" x2="296" y2="196" stroke="#EC008C" stroke-width="2.5"/>
  <circle cx="340" cy="64" r="6" fill="#C5CAE9" opacity="0.8"/>
  <circle cx="356" cy="150" r="5" fill="#F8BBD0" opacity="0.7"/>
  <circle cx="30" cy="212" r="5" fill="#9FA8DA" opacity="0.6"/>
</svg>"""

ART_MMR = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#FCE4EC" opacity="0.55"/>
  <line x1="96" y1="44" x2="96" y2="236" stroke="#232C8E" stroke-width="3"/>
  <line x1="150" y1="44" x2="150" y2="236" stroke="#5C6BC0" stroke-width="3"/>
  <line x1="96" y1="66" x2="150" y2="66" stroke="#9FA8DA" stroke-width="4"/>
  <line x1="96" y1="98" x2="150" y2="98" stroke="#9FA8DA" stroke-width="4"/>
  <line x1="96" y1="162" x2="150" y2="162" stroke="#9FA8DA" stroke-width="4"/>
  <line x1="96" y1="194" x2="150" y2="194" stroke="#9FA8DA" stroke-width="4"/>
  <line x1="96" y1="226" x2="150" y2="226" stroke="#9FA8DA" stroke-width="4"/>
  <line x1="96" y1="130" x2="117" y2="130" stroke="#EC008C" stroke-width="4"/>
  <line x1="129" y1="130" x2="150" y2="130" stroke="#EC008C" stroke-width="4"/>
  <path d="M119 125 l10 10 M129 125 l-10 10" stroke="#EC008C" stroke-width="2"/>
  <circle cx="250" cy="96" r="20" fill="#3949AB"/>
  <circle cx="250" cy="96" r="9" fill="#C5CAE9"/>
  <circle cx="306" cy="112" r="17" fill="#5C6BC0"/>
  <circle cx="306" cy="112" r="8" fill="#E8EAF6"/>
  <circle cx="252" cy="156" r="17" fill="#5C6BC0"/>
  <circle cx="252" cy="156" r="8" fill="#E8EAF6"/>
  <circle cx="304" cy="170" r="20" fill="#3949AB"/>
  <circle cx="304" cy="170" r="9" fill="#C5CAE9"/>
  <line x1="266" y1="104" x2="290" y2="112" stroke="#9FA8DA" stroke-width="2"/>
  <line x1="252" y1="116" x2="252" y2="139" stroke="#9FA8DA" stroke-width="2"/>
  <line x1="290" y1="170" x2="269" y2="160" stroke="#9FA8DA" stroke-width="2"/>
  <line x1="304" y1="150" x2="306" y2="129" stroke="#9FA8DA" stroke-width="2"/>
  <path d="M150 130 Q195 118 230 102" stroke="#F48FB1" stroke-width="2" fill="none" stroke-dasharray="4 4"/>
  <path d="M44 190 L62 197 L62 217 Q62 235 44 243 Q26 235 26 217 L26 197 Z" fill="#EC008C"/>
  <path d="M36 215 l6 6 12 -14" stroke="#ffffff" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="200" cy="46" r="6" fill="#F8BBD0" opacity="0.8"/>
  <circle cx="356" cy="238" r="5" fill="#C5CAE9" opacity="0.7"/>
</svg>"""

# Second, complementary illustration per reference — paired with the "Why it matters"
# block on the opposite side, for the alternating two-column rows.
ART_WHO2 = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#E8EAF6" opacity="0.55"/>
  <path d="M200 92 Q152 74 98 88 L98 206 Q152 192 200 210 Z" fill="#3949AB"/>
  <path d="M200 92 Q248 74 302 88 L302 206 Q248 192 200 210 Z" fill="#232C8E"/>
  <line x1="200" y1="92" x2="200" y2="210" stroke="#C5CAE9" stroke-width="3"/>
  <line x1="120" y1="112" x2="182" y2="120" stroke="#9FA8DA" stroke-width="3"/>
  <line x1="120" y1="132" x2="182" y2="140" stroke="#9FA8DA" stroke-width="3"/>
  <line x1="120" y1="152" x2="182" y2="160" stroke="#9FA8DA" stroke-width="3"/>
  <line x1="120" y1="172" x2="182" y2="180" stroke="#9FA8DA" stroke-width="3"/>
  <line x1="218" y1="120" x2="280" y2="112" stroke="#5C6BC0" stroke-width="3"/>
  <line x1="218" y1="140" x2="280" y2="132" stroke="#5C6BC0" stroke-width="3"/>
  <line x1="218" y1="160" x2="280" y2="152" stroke="#5C6BC0" stroke-width="3"/>
  <line x1="218" y1="180" x2="280" y2="172" stroke="#5C6BC0" stroke-width="3"/>
  <circle cx="268" cy="182" r="30" fill="#ffffff" opacity="0.4"/>
  <circle cx="268" cy="182" r="30" fill="none" stroke="#EC008C" stroke-width="4"/>
  <line x1="290" y1="204" x2="314" y2="228" stroke="#EC008C" stroke-width="6" stroke-linecap="round"/>
  <circle cx="58" cy="58" r="6" fill="#C5CAE9" opacity="0.8"/>
  <circle cx="348" cy="66" r="5" fill="#F8BBD0" opacity="0.7"/>
  <circle cx="40" cy="214" r="5" fill="#9FA8DA" opacity="0.6"/>
</svg>"""

ART_HER2_2 = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#FCE4EC" opacity="0.6"/>
  <ellipse cx="178" cy="140" rx="98" ry="88" fill="#ffffff" stroke="#F48FB1" stroke-width="3"/>
  <circle cx="146" cy="108" r="6" fill="#232C8E"/>
  <circle cx="212" cy="118" r="6" fill="#232C8E"/>
  <circle cx="166" cy="172" r="6" fill="#232C8E"/>
  <circle cx="158" cy="128" r="5" fill="#EC008C"/>
  <circle cx="170" cy="124" r="5" fill="#EC008C"/>
  <circle cx="164" cy="138" r="5" fill="#EC008C"/>
  <circle cx="176" cy="136" r="5" fill="#EC008C"/>
  <circle cx="198" cy="148" r="5" fill="#EC008C"/>
  <circle cx="208" cy="156" r="5" fill="#EC008C"/>
  <circle cx="198" cy="160" r="5" fill="#EC008C"/>
  <circle cx="150" cy="156" r="5" fill="#EC008C"/>
  <circle cx="160" cy="164" r="5" fill="#EC008C"/>
  <circle cx="188" cy="112" r="5" fill="#EC008C"/>
  <circle cx="290" cy="198" r="32" fill="none" stroke="#C2186A" stroke-width="4"/>
  <line x1="313" y1="221" x2="338" y2="246" stroke="#C2186A" stroke-width="6" stroke-linecap="round"/>
  <circle cx="60" cy="52" r="6" fill="#F8BBD0" opacity="0.8"/>
  <circle cx="336" cy="66" r="5" fill="#F48FB1" opacity="0.7"/>
</svg>"""

ART_LUNG_2 = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#E8EAF6" opacity="0.55"/>
  <rect x="118" y="54" width="162" height="182" rx="14" fill="#ffffff" stroke="#C5CAE9" stroke-width="2"/>
  <rect x="166" y="44" width="66" height="24" rx="8" fill="#3949AB"/>
  <circle cx="150" cy="106" r="12" fill="#EC008C"/>
  <path d="M145 106 l4 4 7 -8" stroke="#ffffff" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="172" y1="102" x2="252" y2="102" stroke="#9FA8DA" stroke-width="5" stroke-linecap="round"/>
  <line x1="172" y1="114" x2="228" y2="114" stroke="#C5CAE9" stroke-width="4" stroke-linecap="round"/>
  <circle cx="150" cy="150" r="12" fill="#EC008C"/>
  <path d="M145 150 l4 4 7 -8" stroke="#ffffff" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="172" y1="146" x2="252" y2="146" stroke="#9FA8DA" stroke-width="5" stroke-linecap="round"/>
  <line x1="172" y1="158" x2="222" y2="158" stroke="#C5CAE9" stroke-width="4" stroke-linecap="round"/>
  <circle cx="150" cy="194" r="12" fill="#5C6BC0"/>
  <path d="M145 194 l4 4 7 -8" stroke="#ffffff" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <line x1="172" y1="190" x2="252" y2="190" stroke="#9FA8DA" stroke-width="5" stroke-linecap="round"/>
  <line x1="172" y1="202" x2="234" y2="202" stroke="#C5CAE9" stroke-width="4" stroke-linecap="round"/>
  <path d="M322 98 Q340 114 322 130 Q304 146 322 162" stroke="#232C8E" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M346 98 Q328 114 346 130 Q364 146 346 162" stroke="#5C6BC0" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <line x1="326" y1="108" x2="342" y2="108" stroke="#9FA8DA" stroke-width="2"/>
  <line x1="326" y1="130" x2="342" y2="130" stroke="#9FA8DA" stroke-width="2"/>
  <line x1="326" y1="152" x2="342" y2="152" stroke="#9FA8DA" stroke-width="2"/>
  <circle cx="64" cy="70" r="6" fill="#C5CAE9" opacity="0.8"/>
  <circle cx="58" cy="212" r="5" fill="#F8BBD0" opacity="0.7"/>
</svg>"""

ART_MMR_2 = """<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <ellipse cx="200" cy="140" rx="192" ry="132" fill="#FCE4EC" opacity="0.55"/>
  <rect x="96" y="60" width="90" height="72" rx="10" fill="#3949AB"/>
  <rect x="214" y="60" width="90" height="72" rx="10" fill="#232C8E"/>
  <rect x="96" y="150" width="90" height="72" rx="10" fill="#FCE4EC" stroke="#F48FB1" stroke-width="2.5" stroke-dasharray="6 4"/>
  <rect x="214" y="150" width="90" height="72" rx="10" fill="#3949AB"/>
  <circle cx="120" cy="86" r="5" fill="#C5CAE9"/><circle cx="150" cy="98" r="5" fill="#C5CAE9"/><circle cx="164" cy="80" r="5" fill="#C5CAE9"/><circle cx="132" cy="112" r="5" fill="#C5CAE9"/>
  <circle cx="238" cy="86" r="5" fill="#C5CAE9"/><circle cx="268" cy="98" r="5" fill="#C5CAE9"/><circle cx="282" cy="80" r="5" fill="#C5CAE9"/><circle cx="250" cy="112" r="5" fill="#C5CAE9"/>
  <circle cx="120" cy="176" r="5" fill="none" stroke="#F8BBD0" stroke-width="1.5"/><circle cx="150" cy="188" r="5" fill="none" stroke="#F8BBD0" stroke-width="1.5"/><circle cx="164" cy="170" r="5" fill="none" stroke="#F8BBD0" stroke-width="1.5"/><circle cx="132" cy="202" r="5" fill="none" stroke="#F8BBD0" stroke-width="1.5"/>
  <circle cx="238" cy="176" r="5" fill="#C5CAE9"/><circle cx="268" cy="188" r="5" fill="#C5CAE9"/><circle cx="282" cy="170" r="5" fill="#C5CAE9"/><circle cx="250" cy="202" r="5" fill="#C5CAE9"/>
  <circle cx="176" cy="206" r="14" fill="#EC008C"/>
  <rect x="174" y="197" width="4" height="10" rx="2" fill="#ffffff"/>
  <circle cx="176" cy="213" r="2.3" fill="#ffffff"/>
  <circle cx="64" cy="46" r="6" fill="#F8BBD0" opacity="0.8"/>
  <circle cx="342" cy="238" r="5" fill="#C5CAE9" opacity="0.7"/>
</svg>"""

REFS = [
  dict(slug="who-classification-tumours", tag="Classification",
    title="WHO Classification of Tumours (5th ed.)",
    sub="The international reference that defines and names tumours, integrating histopathology with molecular pathology.",
    icon='<path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"/>',
    summary="The international standard that integrates histopathology with molecular pathology to define and name tumours.",
    what="The WHO Classification of Tumours &mdash; often called the &ldquo;WHO Blue Books&rdquo; &mdash; is the internationally recognised reference series published by the International Agency for Research on Cancer (IARC) under the World Health Organization. Each volume classifies the tumours of a particular organ system and defines how each entity is named, diagnosed and graded.",
    why="It gives pathologists, oncologists and laboratories a common diagnostic language, so that a diagnosis carries the same meaning across hospitals, cities and countries. The 5th edition increasingly integrates molecular and genetic findings alongside traditional microscopy &mdash; reflecting how modern diagnosis combines histopathology, immunohistochemistry and molecular pathology.",
    points=[
      "Organised by organ system across a series of volumes (the &ldquo;Blue Books&rdquo;)",
      "Defines standard tumour nomenclature, diagnostic criteria and grading",
      "Integrates morphology with immunohistochemistry and molecular findings",
      "Updated across editions to include newly recognised tumour entities",
    ],
    how="Our histopathology and molecular reports are structured to align with current WHO terminology and criteria, so that referring clinicians receive diagnoses in a form consistent with international practice.",
    art=ART_WHO, art2=ART_WHO2),

  dict(slug="asco-cap-her2", tag="Breast",
    title="ASCO–CAP HER2 Testing Guideline",
    sub="How HER2 status is determined and reported in breast (and gastric) cancer, using IHC and in-situ hybridization.",
    icon='<path stroke-linecap="round" stroke-linejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 01-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 014.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0112 15a9.065 9.065 0 00-6.23-.693L5 14.5m14.8.8l1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0112 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5"/>',
    summary="The standard for how HER2 status is tested and reported to guide HER2-targeted therapy.",
    what="Developed jointly by the American Society of Clinical Oncology (ASCO) and the College of American Pathologists (CAP), this guideline standardises how HER2 (human epidermal growth factor receptor 2) status is tested and reported &mdash; primarily in breast cancer, with related principles applied in gastric cancer.",
    why="HER2 status helps guide whether a patient may benefit from HER2-targeted therapy. Consistent testing and scoring reduce the risk of false-positive or false-negative results that could affect treatment decisions.",
    points=[
      "Defines immunohistochemistry (IHC) scoring as 0, 1+, 2+ or 3+",
      "Equivocal (2+) IHC results are reflexed to in-situ hybridization (ISH / FISH)",
      "Sets expectations for fixation, controls and interpretation",
      "Promotes clear, reproducible reporting for clinical decision-making",
    ],
    how="When HER2 testing is requested, our reporting follows the current ASCO&ndash;CAP interpretation and reflex-testing principles, so results are consistent and clinically actionable.",
    art=ART_HER2, art2=ART_HER2_2),

  dict(slug="cap-iaslc-amp-lung", tag="Lung",
    title="CAP–IASLC–AMP Molecular Testing Guideline",
    sub="Which molecular markers to test in lung cancer patients being considered for targeted therapy.",
    icon='<path stroke-linecap="round" stroke-linejoin="round" d="M8 3c2 3 2 5 0 8s-2 5 0 8m8-16c-2 3-2 5 0 8s2 5 0 8M7 7h10M7 17h10"/>',
    summary="Guidance on selecting molecular tests for lung cancer patients considered for targeted therapy.",
    what="A joint guideline from the College of American Pathologists (CAP), the International Association for the Study of Lung Cancer (IASLC) and the Association for Molecular Pathology (AMP). It defines which molecular markers should be tested in patients with lung cancer to guide selection of targeted (precision) therapies.",
    why="Lung adenocarcinoma can carry specific, treatable molecular alterations. Testing the right markers &mdash; such as EGFR mutations and ALK / ROS1 rearrangements &mdash; helps identify patients who may benefit from targeted therapy rather than standard chemotherapy alone.",
    points=[
      "Guides selection of biomarkers for targeted therapy in lung cancer",
      "Covers markers such as EGFR mutations and ALK / ROS1 rearrangements",
      "Addresses appropriate specimen handling and testing methods",
      "Supports a rational, evidence-based molecular testing pathway",
    ],
    how="For lung cases referred for molecular testing, our workflow references these recommendations to help ensure the clinically relevant markers are considered.",
    art=ART_LUNG, art2=ART_LUNG_2),

  dict(slug="cap-amp-mmr-msi", tag="Colorectal",
    title="CAP–AMP MMR / MSI Testing Guideline",
    sub="Testing tumours for mismatch-repair deficiency and microsatellite instability to inform immunotherapy and screening.",
    icon='<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z"/>',
    summary="Standards for testing mismatch-repair (MMR) and microsatellite instability (MSI) status.",
    what="A guideline from the College of American Pathologists (CAP), developed with the Association for Molecular Pathology (AMP) and partners, on testing tumours for mismatch-repair (MMR) deficiency and microsatellite instability (MSI).",
    why="MMR / MSI status can indicate whether a tumour may respond to immune checkpoint inhibitor (immunotherapy) treatment, and can flag cases that warrant screening for Lynch syndrome. It is most established in colorectal and endometrial cancers but is relevant across tumour types.",
    points=[
      "Assesses mismatch-repair (MMR) proteins by IHC and/or MSI by molecular methods",
      "Informs eligibility for immune checkpoint inhibitor (immunotherapy) treatment",
      "Helps flag cases for Lynch syndrome screening",
      "Most established in colorectal and endometrial cancers",
    ],
    how="When MMR / MSI testing is requested, our reporting reflects these principles so results are clear for both treatment and screening decisions.",
    art=ART_MMR, art2=ART_MMR_2),
]

_ARROW = ('<svg fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" '
          'style="width:15px;height:15px" aria-hidden="true"><path stroke-linecap="round" '
          'stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/></svg>')


def ref_card(r):
    return ('      <a href="../case-studies/{slug}.html" class="card ref-card reveal">'
            '<div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" '
            'stroke="currentColor" aria-hidden="true">{icon}</svg></div>'
            '<span class="case-tag">{tag}</span><h3>{title}</h3><p>{summary}</p>'
            '<span class="ref-more">Read the explainer ' + _ARROW + '</span></a>\n').format(
        slug=r["slug"], icon=r["icon"], tag=r["tag"], title=r["title"], summary=r["summary"])


def ref_detail_main(r):
    points = "".join("<li>{}</li>".format(p) for p in r["points"])
    return (
      '  <header class="page-hero">\n'
      '    <div class="container page-hero-inner">\n'
      '      <div class="breadcrumb"><a href="../index.html">Home</a> / '
      '<a href="../case-studies/">Case Studies &amp; Research</a> / {tag}</div>\n'
      '      <h1>{title}</h1>\n'
      '      <p>{sub}</p>\n'
      '    </div>\n'
      '  </header>\n'
      '  <section class="section"><div class="container" style="max-width:900px">\n'
      '    <div class="ref-lead reveal"><div class="card-icon"><svg fill="none" '
      'viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor" aria-hidden="true">{icon}</svg></div>'
      '<p class="ref-lead-text">{summary}</p></div>\n'
      '    <div class="ref-row reveal">\n'
      '      <div class="ref-row__text"><h2>What it is</h2><p>{what}</p></div>\n'
      '      <div class="ref-row__art">{art}</div>\n'
      '    </div>\n'
      '    <div class="ref-row ref-row--alt reveal">\n'
      '      <div class="ref-row__text"><h2>Why it matters</h2><p>{why}</p></div>\n'
      '      <div class="ref-row__art">{art2}</div>\n'
      '    </div>\n'
      '    <div class="ref-detail reveal">\n'
      '      <h2>Key points</h2><ul class="tick-list">{points}</ul>\n'
      '      <h2>How our reporting uses it</h2><p>{how}</p>\n'
      '      <div class="notice" style="margin-top:1.7rem">{disc}</div>\n'
      '      <div style="margin-top:2rem"><a href="../case-studies/" class="btn-ghost">'
      '&larr; Back to Case Studies &amp; Research</a></div>\n'
      '    </div>\n'
      '  </div></section>\n'
    ).format(tag=r["tag"], title=r["title"], sub=r["sub"], icon=r["icon"], summary=r["summary"],
             art=r["art"], art2=r["art2"], what=r["what"], why=r["why"], points=points, how=r["how"],
             disc=REF_DISCLAIMER) + cta_band("../")


_CASE_ICON = ('<svg fill="none" viewBox="0 0 24 24" stroke-width="1.4" stroke="currentColor" '
              'style="width:40px;height:40px" aria-hidden="true"><path stroke-linecap="round" '
              'stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 '
              '1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 '
              '0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 '
              '1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"/></svg>')

cs_main = """  <header class="page-hero">
    <div class="container page-hero-inner">
      <div class="breadcrumb"><a href="../index.html">Home</a> / Case Studies &amp; Research</div>
      <h1>Case Studies &amp; Research</h1>
      <p>De-identified cases from our bench, and the classifications and guidelines our reporting is built on. No patient name, ID, or image — ever.</p>
    </div>
  </header>
  <section class="section"><div class="container">
    <div class="section-head reveal"><span class="eyebrow">Case Studies</span><h2>De-identified cases for <span class="text-pink">referring doctors</span></h2></div>
    <div class="notice reveal" style="margin-bottom:2rem">All case studies are fully de-identified in line with the DPDP Act, 2023. [PLACEHOLDER: add real de-identified cases.]</div>
    <div class="grid case-grid">
""" + "".join(['      <a href="#" class="case-card reveal"><div class="case-thumb">' + _CASE_ICON + '</div><div class="case-body"><span class="case-tag">[Category]</span><h3>[PLACEHOLDER: case title]</h3><p>[PLACEHOLDER: teaching point.]</p><div class="case-meta">De-identified &middot; [Date]</div></div></a>\n' for _ in range(3)]) + """    </div>
  </div></section>
  <section class="section section--soft"><div class="container">
    <div class="section-head reveal"><span class="eyebrow">Research &amp; References</span><h2>The standards our reporting is <span class="text-pink">built on</span></h2><p>Widely used international classifications and guidelines our diagnostics reference &mdash; each explained on its own page. [PLACEHOLDER: the lab&rsquo;s own publications will be added here.]</p></div>
    <div class="grid grid-2">
""" + "".join(ref_card(r) for r in REFS) + """    </div>
  </div></section>
""" + cta_band("../")
PAGES.append(dict(filename="case-studies/index.html", title="Case Studies &amp; Research", active="case-studies",
    desc="De-identified histopathology and molecular case studies, plus the classifications and guidelines PathMole Expert Lab reports against.",
    prefix="../", main=cs_main))

# One dedicated explainer page per Research & Reference standard.
for _r in REFS:
    PAGES.append(dict(filename="case-studies/{}.html".format(_r["slug"]),
        title=_r["title"], active="case-studies", prefix="../",
        desc=_r["summary"], main=ref_detail_main(_r)))

# PARTNER WITH US (business development — client-supplied content + enquiry form)
PAGES.append(dict(filename="partner.html", title="Partner With Us", active="partner",
    desc="Partner with PATHMOLE EXPERT LLP — reliable Histopathology & Molecular Diagnostic services for hospitals, clinics, doctors, laboratories and healthcare institutions.",
    main=phero("Partner With Us", "Building better diagnostics, together &mdash; dependable Histopathology &amp; Molecular Diagnostic partnerships.", "Partner") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:860px">
        <span class="eyebrow">Building better diagnostics together</span>
        <h2>Strong diagnostics are built through <span class="text-pink">collaboration</span></h2>
        <p>At <strong>PATHMOLE EXPERT LLP</strong>, we believe that strong diagnostic services are built through collaboration. We welcome partnerships with hospitals, clinics, doctors, nursing homes, diagnostic centres, laboratories, healthcare organizations, and institutions seeking dependable Histopathology and Molecular Diagnostic services.</p>
        <p>Our partnership approach is built around quality, timely reporting, professional communication, confidentiality, and clinical collaboration. Whether you are looking to outsource histopathology, add molecular testing to your existing diagnostic services, strengthen your laboratory capabilities, or develop a long-term referral partnership, we would be happy to explore how we can work together.</p>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">We can partner with</span><h2>Who we <span class="text-pink">work with</span></h2></div>
      <div class="grid grid-2" style="max-width:900px;margin:0 auto">
        <article class="card reveal"><ul class="tick-list"><li>Hospitals and healthcare institutions</li><li>Individual clinicians and specialist practices</li><li>Nursing homes and day-care centres</li><li>Diagnostic laboratories and collection centres</li></ul></article>
        <article class="card reveal"><ul class="tick-list"><li>Pathology and healthcare networks</li><li>Research and academic institutions</li><li>Healthcare organizations requiring specialized diagnostic support</li></ul></article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">What we offer our partners</span><h2>A partnership built on <span class="text-pink">trust</span></h2></div>
      <div class="grid grid-4">
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z"/></svg></div>
          <h3>Reliable Diagnostic Support</h3>
          <p>Access to specialized Histopathology and Molecular Diagnostic services backed by professional oversight and quality-focused processes.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M8.625 12a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H8.25m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0H12m4.125 0a.375.375 0 11-.75 0 .375.375 0 01.75 0zm0 0h-.375M21 12c0 4.556-4.03 8.25-9 8.25a9.764 9.764 0 01-2.555-.337A5.972 5.972 0 015.41 20.97a5.969 5.969 0 01-.474-.065 4.48 4.48 0 00.978-2.025c.09-.457-.133-.901-.467-1.226C3.93 16.178 3 14.189 3 12c0-4.556 4.03-8.25 9-8.25s9 3.694 9 8.25z"/></svg></div>
          <h3>Clinician-Focused Communication</h3>
          <p>Clear reporting and professional interaction to facilitate appropriate clinical decision-making.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75"/></svg></div>
          <h3>Flexible Partnership Models</h3>
          <p>Referral, outsourcing, institutional, and customized diagnostic service arrangements based on the requirements of our partners.</p>
        </article>
        <article class="card reveal">
          <div class="card-icon"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/></svg></div>
          <h3>Quality &amp; Confidentiality</h3>
          <p>Strong emphasis on specimen integrity, traceability, patient confidentiality, quality assurance, and ethical laboratory practices.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container" style="max-width:820px">
      <div class="section-head reveal" id="enquiry"><span class="eyebrow">Let&rsquo;s work together</span><h2>Start a <span class="text-pink">partnership enquiry</span></h2><p>If you are interested in developing a diagnostic partnership with PATHMOLE EXPERT LLP, please complete the form below. Our team will review your requirements and get in touch to discuss the appropriate partnership model.</p></div>
      <form id="enquiry-form" class="form-card form-grid form-grid--2col reveal" data-subject="New partnership enquiry — PathMole website" novalidate>
        <div class="form-head">
          <div class="form-head-ico"><svg fill="none" viewBox="0 0 24 24" stroke-width="1.6" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg></div>
          <div><h3>Partnership Enquiry</h3><p>Share a few details and our team will get back to you to discuss the right partnership model.</p></div>
        </div>
        <p class="form-section-title">Contact details</p>
        <div class="field"><label for="p-name">Name *</label><input id="p-name" name="name" type="text" required placeholder="Your full name" /></div>
        <div class="field"><label for="p-role">Designation / Professional Role *</label><input id="p-role" name="designation" type="text" required placeholder="e.g. Consultant Pathologist" /></div>
        <div class="field col-full"><label for="p-org">Organization / Hospital / Clinic Name *</label><input id="p-org" name="organisation" type="text" required placeholder="Organization, hospital or clinic name" /></div>
        <div class="field"><label for="p-phone">Mobile Number *</label><input id="p-phone" name="phone" type="tel" required placeholder="+91 " /></div>
        <div class="field"><label for="p-email">Email Address *</label><input id="p-email" name="email" type="email" required placeholder="you@example.com" /></div>
        <div class="field col-full"><label for="p-city">City / Location *</label><input id="p-city" name="city" type="text" required placeholder="City / location" /></div>

        <p class="form-section-title">About your requirement</p>
        <div class="field"><label for="p-as">I am interested in partnering as *</label>
          <select id="p-as" name="partner_as" required>
            <option value="" selected disabled>Select an option…</option>
            <option>Hospital / Healthcare Institution</option>
            <option>Doctor / Clinician</option>
            <option>Diagnostic Laboratory</option>
            <option>Nursing Home / Clinic</option>
            <option>Collection Centre</option>
            <option>Research / Academic Institution</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field"><label for="p-svc">Services of Interest *</label>
          <select id="p-svc" name="services" required>
            <option value="" selected disabled>Select an option…</option>
            <option>Histopathology</option>
            <option>Molecular Diagnostics</option>
            <option>Both Histopathology &amp; Molecular Diagnostics</option>
            <option>Second Opinion / Diagnostic Consultation</option>
            <option>Other</option>
          </select>
        </div>
        <div class="field"><label for="p-vol">Approximate Monthly Sample Volume</label>
          <select id="p-vol" name="monthly_volume">
            <option value="" selected disabled>Select a range…</option>
            <option>Less than 50</option>
            <option>50&ndash;100</option>
            <option>100&ndash;250</option>
            <option>250&ndash;500</option>
            <option>500+</option>
            <option>Not yet determined</option>
          </select>
        </div>
        <div class="field"><label for="p-mode">Preferred Mode of Partnership</label>
          <select id="p-mode" name="partnership_mode">
            <option value="" selected disabled>Select an option…</option>
            <option>Sample Referral</option>
            <option>Outsourced Laboratory Services</option>
            <option>Institutional Partnership</option>
            <option>Long-term Diagnostic Collaboration</option>
            <option>Other / Discuss with us</option>
          </select>
        </div>
        <div class="field col-full"><label for="p-contact">Preferred Method of Contact</label>
          <select id="p-contact" name="preferred_contact">
            <option value="" selected disabled>Select an option…</option>
            <option>Phone</option>
            <option>WhatsApp</option>
            <option>Email</option>
          </select>
        </div>
        <div class="field col-full"><label for="p-msg">Tell us briefly about your requirement *</label><textarea id="p-msg" name="message" required placeholder="What would you like to partner on?"></textarea></div>
        <button type="submit" class="btn-primary col-full">Submit Partnership Enquiry</button>
        <p class="form-note col-full">This form emails the lab; no patient records are stored on the site. Partner with PATHMOLE &mdash; strengthening diagnostics, together.</p>
        <p class="form-status col-full" role="status" aria-live="polite"></p>
      </form>
    </div>
  </section>
""" + cta_band()))


for pg in PAGES:
    page(pg["filename"], pg["title"], pg["desc"], pg["active"], pg["main"],
         prefix=pg.get("prefix", ""), extra_scripts=pg.get("extra_scripts", ""))

print("Done.")
