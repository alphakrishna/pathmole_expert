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
    ("case-studies/", "CASE STUDIES", "case-studies"),
    ("publications.html", "RESEARCH", "publications"),
    ("contact.html", "CONTACT", "contact"),
]
MOBILE_ITEMS = [
    ("index.html", "HOME"), ("about.html", "ABOUT"), ("services.html", "SERVICES"),
    ("tests.html", "TESTS"), ("quality.html", "QUALITY"), ("gallery.html", "GALLERY"),
    ("videos.html", "VIDEOS"), ("case-studies/", "CASE STUDIES"),
    ("publications.html", "RESEARCH"), ("patients.html", "PATIENTS"),
    ("physicians.html", "PHYSICIANS"), ("faq.html", "FAQ"), ("careers.html", "CAREERS"),
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
      <span class="top-bar-item hours">&#128340; Open daily, 11:00 AM &ndash; 11:00 PM</span>
      <div class="top-bar-actions">
        <a class="top-bar-cta" href="tel:+919899822375">Call Now</a>
        <a class="top-bar-cta wa" href="https://wa.me/919899822375" target="_blank" rel="noopener noreferrer">WhatsApp</a>
        <a class="top-bar-reports" href="#" target="_blank" rel="noopener noreferrer">Reports Login &#8599;</a>
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
{mob}        <li><a href="#" target="_blank" rel="noopener noreferrer">REPORTS LOGIN &#8599;</a></li>
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
          <a href="{p}services.html">Histopathology</a>
          <a href="{p}services.html">Cytopathology</a>
          <a href="{p}services.html">Molecular Diagnostics</a>
          <a href="{p}tests.html">Test List</a>
          <a href="{p}quality.html">Quality</a>
        </div>
        <div class="footer-col">
          <h4>Explore</h4>
          <a href="{p}about.html">About</a>
          <a href="{p}case-studies/">Case Studies</a>
          <a href="{p}publications.html">Research</a>
          <a href="{p}patients.html">Patients</a>
          <a href="{p}careers.html">Careers</a>
        </div>
        <div class="footer-col footer-contact">
          <h4>Contact</h4>
          <p>Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana)</p>
          <p>&#128222; <a href="tel:+919899822375">+91 98998 22375</a><br>&#9993; <a href="mailto:pathmolelab@gmail.com">pathmolelab@gmail.com</a></p>
          <p>&#128340; Open daily, 11:00 AM &ndash; 11:00 PM</p>
        </div>
      </div>
      <div class="footer-bottom">
        <span class="footer-copy">&copy; 2026 PathMole Expert Lab. All rights reserved.</span>
        <div class="footer-social">
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0022 12z"/></svg></a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.3 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .3-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.3-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.3 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.1A6.7 6.7 0 1018.7 12 6.7 6.7 0 0012 5.3zm0 11a4.3 4.3 0 114.3-4.3 4.3 4.3 0 01-4.3 4.3zm6.9-11.3a1.6 1.6 0 11-1.6-1.6 1.6 1.6 0 011.6 1.6z"/></svg></a>
          <a href="#" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M20.4 3H3.6A.6.6 0 003 3.6v16.8a.6.6 0 00.6.6h16.8a.6.6 0 00.6-.6V3.6a.6.6 0 00-.6-.6zM8.3 18.3H5.5V9.7h2.8v8.6zM6.9 8.5a1.6 1.6 0 111.6-1.6 1.6 1.6 0 01-1.6 1.6zm11.4 9.8h-2.8v-4.2c0-1 0-2.3-1.4-2.3s-1.6 1.1-1.6 2.2v4.3h-2.8V9.7h2.7v1.2h.1a3 3 0 012.6-1.4c2.8 0 3.4 1.9 3.4 4.3v4.5z"/></svg></a>
        </div>
      </div>
    </div>
  </footer>

  <button id="back-to-top" class="back-to-top" aria-label="Back to top">
    <svg fill="none" viewBox="0 0 24 24" stroke-width="1.8" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 15.75l7.5-7.5 7.5 7.5" /></svg>
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
    main=phero("About the Lab", "Where science meets clinical decision-making &mdash; dependable diagnostic information that helps clinicians make better decisions.", "About") + """
  <section class="section">
    <div class="container grid grid-2" style="align-items:center">
      <div class="reveal">
        <span class="eyebrow">Our story</span>
        <h2>Where science meets clinical decision-making</h2>
        <p>Our Histopathology &amp; Molecular Biology Laboratory has been established with a simple objective: to provide dependable diagnostic information that helps clinicians make better decisions.</p>
        <p>The laboratory brings together two complementary areas of modern diagnostic medicine. <strong>Histopathology</strong> allows us to understand disease through the examination of tissues and cells. <strong>Molecular diagnostics</strong> allows us to look deeper &mdash; at DNA, RNA, microorganisms and molecular alterations that may not be visible through conventional microscopy alone. Together, these disciplines provide a more comprehensive approach to diagnosis.</p>
      </div>
      <div class="reveal">
        <div class="map-card"><div class="map-card-head">Facility photo &mdash; [PLACEHOLDER]</div>
        <div class="map-card-body"><strong>Sector 6, Gurugram</strong><p>A modern, technology-enabled laboratory with a roadmap toward digital pathology and advanced molecular testing.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container grid grid-2" style="gap:2.5rem">
      <div class="reveal">
        <span class="eyebrow">Built around quality</span>
        <h2>Quality begins before the microscope</h2>
        <p>Our laboratory processes are designed around the principles of <strong>Accuracy &middot; Quality &middot; Traceability &middot; Timeliness &middot; Patient Safety</strong>.</p>
        <p>We recognise that laboratory quality begins long before a specimen reaches the microscope or analyser. Proper specimen collection, identification, transportation, processing, testing, interpretation and reporting are all essential components of a reliable diagnostic service.</p>
      </div>
      <div class="reveal">
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
        <article class="card reveal"><h3>Histopathology systems</h3><p>Modern tissue-processing and advanced staining techniques.</p></article>
        <article class="card reveal"><h3>Molecular platforms</h3><p>Molecular amplification and PCR-based diagnostic technologies.</p></article>
        <article class="card reveal"><h3>Digital workflows</h3><p>Laboratory information systems and data-driven quality monitoring.</p></article>
        <article class="card reveal"><h3>Future-ready</h3><p>A roadmap toward digital pathology capabilities.</p></article>
      </div>
      <p class="center" style="margin-top:1.6rem;font-style:italic;color:var(--ink-400)">Technology is an enabler &mdash; it should support, not replace, professional expertise: <strong>experienced professionals + reliable processes + appropriate technology + quality culture</strong>.</p>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal"><span class="eyebrow">Leadership</span><h2>Clinical &amp; laboratory leadership</h2></div>
      <div class="grid" style="max-width:760px;margin:0 auto">
        <article class="card reveal">
          <h3>Dr. Arpan Gandhi</h3>
          <p style="color:var(--accent);font-weight:600;margin-bottom:.6rem">Director &ndash; Laboratory Services | Diagnostic Medicine &amp; Laboratory Leadership</p>
          <p>With nearly three decades of experience in diagnostic medicine and laboratory services, Dr. Gandhi has worked across pathology, laboratory operations, quality, clinical collaboration, education and diagnostic leadership. His focus is on building laboratory systems that combine clinical expertise, operational excellence, technology and quality.</p>
        </article>
      </div>
    </div>
  </section>
""" + cta_band()))

# SERVICES
PAGES.append(dict(filename="services.html", title="Services", active="services",
    desc="Services at PathMole Expert Lab — Histopathology, Molecular Diagnostics, and Immunohistochemistry for referring clinicians.",
    main=phero("Our Services", "Histopathology, cytopathology and molecular diagnostics &mdash; accurate, reproducible and clinically relevant.", "Services") + """
  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Histopathology</span>
        <h2>Seeing disease through tissue</h2>
        <p>Histopathology remains one of the most important pillars of diagnostic medicine. Examination of tissue under the microscope allows the pathologist to identify disease patterns, establish diagnoses and provide information that can influence treatment. Our histopathology service is designed to provide accurate, reproducible and clinically relevant tissue diagnosis.</p>
      </div>
      <div class="grid grid-3" style="margin-top:1.6rem">
        <article class="card reveal"><ul class="tick-list"><li>Routine biopsy examination</li><li>Small and large surgical specimens</li><li>Gastrointestinal biopsies</li><li>Gynecological specimens</li></ul></article>
        <article class="card reveal"><ul class="tick-list"><li>Head and neck specimens</li><li>Skin and soft tissue specimens</li><li>Inflammatory and infectious conditions</li><li>Benign and malignant lesions</li></ul></article>
        <article class="card reveal"><ul class="tick-list"><li>Histochemical stains</li><li>Immunohistochemistry, where indicated</li><li>Specialised pathology consultation</li></ul></article>
      </div>
      <div class="notice reveal" style="margin-top:1.8rem"><strong>From specimen to diagnosis:</strong> Specimen Collection &rarr; Accessioning &rarr; Gross Examination &rarr; Tissue Processing &rarr; Embedding &rarr; Sectioning &rarr; Staining &rarr; Microscopy &rarr; Interpretation &rarr; Reporting. Quality at every stage contributes to the quality of the final diagnosis.</div>
    </div>
  </section>

  <section class="section section--soft">
    <div class="container grid grid-2" style="gap:2.5rem;align-items:center">
      <div class="reveal">
        <span class="eyebrow">Cytopathology</span>
        <h2>Diagnosis at the level of cells</h2>
        <p>Evaluation of cells from various body sites and fluids for the detection and diagnosis of disease &mdash; a valuable, minimally invasive complement to tissue histopathology.</p>
      </div>
      <div class="reveal">
        <span class="eyebrow">Specialised diagnostic support</span>
        <h2>Clinician-focused interpretation</h2>
        <p>Consultation and correlation of laboratory findings with clinical information, so results are meaningful in the clinical context &mdash; not just numbers on a report.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reveal" style="max-width:820px">
        <span class="eyebrow">Molecular biology &amp; molecular diagnostics</span>
        <h2>Looking beyond what the microscope can see</h2>
        <p>Modern diagnostic medicine increasingly depends on understanding disease at the molecular level. Molecular diagnostics examines genetic material such as DNA and RNA to detect specific pathogens, genetic alterations and other molecular targets. Our molecular biology laboratory is designed to support the growing need for rapid, specific and clinically relevant molecular testing.</p>
      </div>
      <div class="grid grid-2" style="margin-top:1.6rem">
        <article class="card reveal"><h3>Molecular diagnostic applications</h3><ul class="tick-list"><li>Infectious disease diagnosis</li><li>Detection of bacterial and viral pathogens</li><li>Identification of specific genetic targets</li><li>Mutation and molecular marker analysis</li><li>Oncology-related molecular testing</li><li>Targeted PCR-based investigations</li><li>Other specialised molecular assays</li></ul></article>
        <article class="card reveal"><h3>PCR-based diagnostics</h3><p>Polymerase Chain Reaction (PCR) is one of the most important technologies in modern molecular diagnostics. It allows specific regions of DNA or RNA to be amplified and detected, making it possible to identify targets that may be difficult or impossible to detect using conventional methods alone.</p><p style="margin-top:.8rem;font-style:italic;color:var(--ink-400)">Molecular diagnostics is powerful &mdash; its value depends on doing it correctly, with rigorous control at every stage.</p></article>
      </div>
      <div class="center" style="margin-top:2.5rem"><a href="tests.html" class="btn-secondary">Browse the test list</a></div>
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
    <div class="container grid grid-2" style="align-items:start;gap:2.5rem">
      <div class="reveal" id="enquiry">
        <span class="eyebrow">Send an enquiry</span>
        <h2>How can we help?</h2>
        <form id="enquiry-form" class="form-grid" style="margin-top:1.2rem" novalidate>
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
      <div class="reveal">
        <span class="eyebrow">Reach us</span>
        <h2>Visit or call</h2>
        <div class="info-list" style="margin:1.2rem 0">
          <div class="info-item"><div class="card-icon">&#128205;</div><div><strong>Address</strong><br>Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opp. Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana)</div></div>
          <div class="info-item"><div class="card-icon">&#128222;</div><div><strong>Phone / WhatsApp</strong><br><a href="tel:+919899822375">+91 98998 22375</a></div></div>
          <div class="info-item"><div class="card-icon">&#9993;</div><div><strong>Email</strong><br><a href="mailto:pathmolelab@gmail.com">pathmolelab@gmail.com</a></div></div>
          <div class="info-item"><div class="card-icon">&#128340;</div><div><strong>Hours</strong><br>Open daily, 11:00 AM &ndash; 11:00 PM</div></div>
        </div>
        <div class="map-card">
          <div class="map-card-head">Map coming soon</div>
          <div class="map-card-body">
            <strong>PathMole Expert Lab</strong>
            <p>Building No. 1164/1, 1st Floor, Shri JP Tower, New Railway Road, Opposite Fire Station, Dayanand Colony, Sector 6, Gurugram (Haryana)</p>
            <a class="btn-secondary" target="_blank" rel="noopener noreferrer" href="https://www.google.com/maps/search/?api=1&query=PathMole+Expert+Lab+Sector+6+Gurugram">Get directions &#8599;</a>
          </div>
        </div>
        <!-- Real embed (swap in when [GOOGLE_MAPS_EMBED_URL] arrives):
        <div class="map-embed"><iframe src="[GOOGLE_MAPS_EMBED_URL]" loading="lazy" title="PathMole Expert Lab"></iframe></div>
        -->
      </div>
    </div>
  </section>
"""))

# QUALITY
PAGES.append(dict(filename="quality.html", title="Quality & Accreditation", active="",
    desc="Quality and accreditation at PathMole Expert Lab — standardised protocols, expert review, and reliable turnaround.",
    main=phero("Quality &amp; Patient Safety", "Quality is not a department &mdash; it is a culture, applied across the entire diagnostic pathway.", "Quality") + """
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
    <div class="grid" style="max-width:760px;margin:1.6rem auto 0">
      <article class="card reveal">
        <h3>Dr. Arpan Gandhi</h3>
        <p style="color:var(--accent);font-weight:600;margin-bottom:.6rem">Director &ndash; Laboratory Services | Diagnostic Medicine &amp; Laboratory Leadership</p>
        <p>With nearly three decades of experience in diagnostic medicine and laboratory services, Dr. Gandhi has worked across pathology, laboratory operations, quality, clinical collaboration, education and diagnostic leadership. His focus is on building laboratory systems that combine clinical expertise, operational excellence, technology and quality.</p>
      </article>
    </div>
  </div></section>

  <section class="section section--soft"><div class="container">
    <div class="section-head reveal"><span class="eyebrow">For clinicians</span><h2>Diagnostics that support clinical decisions</h2><p>We aim to work as an extension of the clinical team &mdash; providing results that are accurate, timely, understandable and clinically relevant.</p></div>
    <div class="grid grid-3">
      <article class="card reveal"><h3>Reliable testing</h3><p>Standardised laboratory processes designed to maintain consistency and quality.</p></article>
      <article class="card reveal"><h3>Defined turnaround times</h3><p>Clear expectations regarding reporting timelines.</p></article>
      <article class="card reveal"><h3>Clinically relevant reports</h3><p>Reports structured to communicate the information most important for decision-making.</p></article>
      <article class="card reveal"><h3>Pathologist consultation</h3><p>Direct professional communication when a case requires discussion or clarification.</p></article>
      <article class="card reveal"><h3>Integrated diagnostics</h3><p>Histopathology and molecular findings that complement each other when clinically indicated.</p></article>
      <article class="card reveal"><h3>Specimen submission</h3><p>Contact us about test availability, specimen requirements, fixation and transport, sample volume, turnaround times, test selection and special requirements.</p></article>
    </div>
    <p class="center" style="margin-top:1.6rem;font-style:italic;color:var(--ink-400)">When in doubt about the right test or specimen, speak to us before sending the sample.</p>
  </div></section>
""" + cta_band()))

# PUBLICATIONS / RESEARCH
PAGES.append(dict(filename="publications.html", title="Research & References", active="publications",
    desc="Research, guidelines, and references that inform diagnostics at PathMole Expert Lab.",
    main=phero("Research &amp; References", "The classifications and guidelines our reporting is built on.", "Research") + """
  <section class="section"><div class="container">
    <div class="notice reveal" style="margin-bottom:2rem">These are widely used international standards our diagnostics reference. [PLACEHOLDER: add the lab&rsquo;s own publications/case studies here.]</div>
    <div class="grid grid-2">
      <article class="card reveal"><span class="case-tag">Classification</span><h3>WHO Classification of Tumours, 5th ed.</h3><p>The international standard integrating histopathology with molecular pathology.</p></article>
      <article class="card reveal"><span class="case-tag">Breast</span><h3>ASCO–CAP HER2 Testing Guideline (2023)</h3><p>Standard for HER2 IHC/FISH interpretation and reporting.</p></article>
      <article class="card reveal"><span class="case-tag">Lung</span><h3>CAP–IASLC–AMP Molecular Testing Guideline</h3><p>EGFR/ALK and NGS testing for lung cancer therapy selection.</p></article>
      <article class="card reveal"><span class="case-tag">Colorectal</span><h3>CAP–AMP MMR/MSI Testing Guideline (2022)</h3><p>Mismatch-repair / microsatellite instability testing standards.</p></article>
    </div>
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
    main=phero("Videos", "Watch and learn about our lab.", "Videos") + """
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
    <div class="reveal"><span class="eyebrow">Patient information</span><h2>Coming in for a test?</h2><p>Please carry your prescription / request form and any relevant previous reports whenever applicable. Accurate diagnosis begins with the right specimen and the right test.</p><p>Download the patient form, fill it offline, and bring it with you.</p>
      <a href="assets/pathmole-patient-form.pdf" download class="btn-primary">Download Patient Form (PDF)</a>
      <p class="form-note" style="margin-top:.6rem">[PLACEHOLDER: add the PDF at assets/pathmole-patient-form.pdf]</p>
    </div>
    <div class="reveal"><div class="map-card"><div class="map-card-head">Patient visual [PLACEHOLDER]</div><div class="map-card-body"><strong>Open daily, 11 AM – 11 PM</strong><p>Sector 6, Gurugram. Call +91 98998 22375 for any help.</p></div></div></div>
  </div></section>
""" + cta_band()))

# FAQ
PAGES.append(dict(filename="faq.html", title="FAQ", active="",
    desc="Frequently asked questions about PathMole Expert Lab.",
    main=phero("Frequently Asked Questions", "Quick answers — or ask our assistant any time.", "FAQ") + """
  <section class="section"><div class="container" style="max-width:800px">
    <article class="card reveal" style="margin-bottom:1rem"><h3>What are your timings?</h3><p>We&rsquo;re open daily, 11:00 AM – 11:00 PM.</p></article>
    <article class="card reveal" style="margin-bottom:1rem"><h3>Where are you located?</h3><p>Sector 6, Gurugram (Haryana) — full address on our <a href="contact.html">Contact page</a>.</p></article>
    <article class="card reveal" style="margin-bottom:1rem"><h3>How do I get pricing?</h3><p>We share pricing directly on enquiry — please <a href="contact.html">contact the lab</a>.</p></article>
    <article class="card reveal" style="margin-bottom:1rem"><h3>Are case studies patient-identifiable?</h3><p>No. Every case study is fully de-identified, with no patient name, ID, or image.</p></article>
    <article class="card reveal"><h3>How do I access reports?</h3><p>Use the <strong>Reports Login</strong> button at the top of the site. [PLACEHOLDER: portal URL.]</p></article>
  </div></section>
"""))

# CAREERS
PAGES.append(dict(filename="careers.html", title="Careers", active="",
    desc="Careers at PathMole Expert Lab.",
    main=phero("Careers", "Join a growing specialist laboratory.", "Careers") + """
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

# CASE STUDIES INDEX (subfolder)
cs_main = """  <header class="page-hero">
    <div class="container page-hero-inner">
      <div class="breadcrumb"><a href="../index.html">Home</a> / Case Studies</div>
      <h1>Case Studies</h1>
      <p>De-identified cases from our bench, shared with referring doctors. No patient name, ID, or image — ever.</p>
    </div>
  </header>
  <section class="section"><div class="container">
    <div class="notice reveal" style="margin-bottom:2rem">All case studies are fully de-identified in line with the DPDP Act, 2023. [PLACEHOLDER: add real de-identified cases.]</div>
    <div class="grid case-grid">
""" + "".join(["""      <a href="#" class="case-card reveal"><div class="case-thumb"></div><div class="case-body"><span class="case-tag">[Category]</span><h3>[PLACEHOLDER: case title]</h3><p>[PLACEHOLDER: teaching point.]</p><div class="case-meta">De-identified &middot; [Date]</div></div></a>
""" for _ in range(3)]) + """    </div>
  </div></section>
"""
PAGES.append(dict(filename="case-studies/index.html", title="Case Studies", active="case-studies",
    desc="De-identified histopathology and molecular case studies from PathMole Expert Lab.",
    prefix="../", main=cs_main))


for pg in PAGES:
    page(pg["filename"], pg["title"], pg["desc"], pg["active"], pg["main"],
         prefix=pg.get("prefix", ""), extra_scripts=pg.get("extra_scripts", ""))

print("Done.")
