import re

desktop_template = '''      <!-- ================= NAV ================= -->
      <div class="abs desktop-nav" style="left:57px; top:38px; width:1400px; height:66px; z-index:50;">
        <div class="abs"
          style="left:0; top:0; width:100%; height:100%; background:rgba(30, 30, 30, 0.65); backdrop-filter:blur(16px); -webkit-backdrop-filter:blur(16px); border:1px solid rgba(255, 255, 255, 0.15); border-radius:4px;">
        </div>
        <a class="abs" href="index.html"
          style="left:59px; top:17px; display:flex; align-items:center; z-index:10;">
          <img alt="Sanciti AI" src="assets/img/sancitiailogo.png"
            style="height:32px; width:auto; object-fit:contain;" />
        </a>
        <div class="abs font-disp desktop-nav-menu"
          style="display:flex; align-items:center; left:560px; top:23px; width:600px; font-size:16px; gap:36px; color:#fff;">
          <span class="nav-link" style="color:#fff; cursor:pointer;" onclick="window.location.href='index.html';">Home</span>
          <span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href='legmod.html';">LegMod</span>
          <span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href='rgen.html';">RGen</span>
          <span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href='codegen.html';">CodeGen</span>
          <span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href='testai.html';">Test AI</span>
          <span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href='deploy.html';">Deploy</span>
        </div>
        <div class="abs pill"
          style="right:22px; top:11px; padding:0 24px; height:44px; background:var(--cyan); border-radius:999px; display:flex; align-items:center; justify-content:center; cursor:pointer;"
          onclick="scrollToAssessment(event)">
          <span class="font-disp" style="color:var(--ink); font-size:16px; font-weight:bold; white-space:nowrap;">Get a free Assessment</span>
        </div>
      </div>'''

mobile_template = '''  <!-- ================= MOBILE HEADER (< 768px) ================= -->
  <header class="mobile-header" id="mobileHeader">
    <div class="mobile-header-inner">
      <a class="mobile-logo" href="index.html" aria-label="Sanciti AI">
        <img alt="Sanciti AI" src="assets/img/sancitiailogo.png" />
      </a>
      <div class="mobile-header-right">
        <a class="mobile-demo-btn pill" href="#playbook" id="mobileDemoBtn" onclick="scrollToAssessment(event)" style="background:var(--cyan);">
          <span style="color:var(--ink);">Get a free Assessment</span>
        </a>
        <button class="mobile-menu-toggle" id="mobileMenuToggle" aria-label="Toggle navigation" aria-expanded="false"
          onclick="toggleMobileMenu()">
          <span class="hamburger-bar"></span>
          <span class="hamburger-bar"></span>
          <span class="hamburger-bar"></span>
        </button>
      </div>
    </div>
    <!-- Mobile Navigation Drawer -->
    <div class="mobile-nav-drawer" id="mobileNavDrawer">
      <nav class="mobile-nav-links font-disp">
        <a href="index.html" class="mobile-nav-item active">Home</a>
        <a href="legmod.html" class="mobile-nav-item ">LegMod</a>
        <a href="rgen.html" class="mobile-nav-item ">RGen</a>
        <a href="codegen.html" class="mobile-nav-item ">CodeGen</a>
        <a href="testai.html" class="mobile-nav-item ">Test AI</a>
        <a href="deploy.html" class="mobile-nav-item ">Deploy</a>
        <div class="mobile-nav-cta pill" onclick="scrollToAssessment(event)" style="background:var(--cyan);">
          <span style="color:var(--ink);">Get a Free Assessment</span>
        </div>
      </nav>
    </div>
  </header>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Desktop
content = re.sub(r'      <!-- ================= NAV ================= -->\s*<div class="abs desktop-nav".*?</div>\s*</div>', desktop_template, content, flags=re.DOTALL)

# Replace Mobile
content = re.sub(r'  <!-- ================= MOBILE HEADER \(< 768px\) ================= -->\s*<header class="mobile-header" id="mobileHeader">.*?</header>', mobile_template, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")
