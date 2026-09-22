import re

files = {
    'index.html': {'color': 'var(--cyan)', 'text_color': 'var(--ink)'},
    'codegen.html': {'color': '#0104E1', 'text_color': '#FFFFFF'},
    'deploy.html': {'color': '#2AD6DF', 'text_color': '#000000'},
    'legmod.html': {'color': 'var(--cyan)', 'text_color': 'var(--ink)'},
    'rgen.html': {'color': '#2AD6DF', 'text_color': '#000000'},
    'testai.html': {'color': '#BD00FF', 'text_color': '#000000'}
}

# The desktop template
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
          <span class="nav-link" style="color:{home_color}; cursor:pointer;" onclick="window.location.href='index.html';">Home</span>
          <span class="nav-link" style="color:{legmod_color}; cursor:pointer;" onclick="window.location.href='legmod.html';">LegMod</span>
          <span class="nav-link" style="color:{rgen_color}; cursor:pointer;" onclick="window.location.href='rgen.html';">RGen</span>
          <span class="nav-link" style="color:{codegen_color}; cursor:pointer;" onclick="window.location.href='codegen.html';">CodeGen</span>
          <span class="nav-link" style="color:{testai_color}; cursor:pointer;" onclick="window.location.href='testai.html';">Test AI</span>
          <span class="nav-link" style="color:{deploy_color}; cursor:pointer;" onclick="window.location.href='deploy.html';">Deploy</span>
        </div>
        <div class="abs pill"
          style="right:22px; top:11px; padding:0 24px; height:44px; background:{btn_color}; border-radius:999px; display:flex; align-items:center; justify-content:center; cursor:pointer;"
          onclick="scrollToAssessment(event)">
          <span class="font-disp" style="color:{text_color}; font-size:16px; font-weight:bold; white-space:nowrap;">Get a free Assessment</span>
        </div>
      </div>'''

# The mobile template
mobile_template = '''  <!-- ================= MOBILE HEADER (< 768px) ================= -->
  <header class="mobile-header" id="mobileHeader">
    <div class="mobile-header-inner">
      <a class="mobile-logo" href="index.html" aria-label="Sanciti AI">
        <img alt="Sanciti AI" src="assets/img/sancitiailogo.png" />
      </a>
      <div class="mobile-header-right">
        <a class="mobile-demo-btn pill" href="#playbook" id="mobileDemoBtn" onclick="scrollToAssessment(event)" style="background:{btn_color};">
          <span style="color:{text_color};">Get a free Assessment</span>
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
        <a href="index.html" class="mobile-nav-item {home_active}">Home</a>
        <a href="legmod.html" class="mobile-nav-item {legmod_active}">LegMod</a>
        <a href="rgen.html" class="mobile-nav-item {rgen_active}">RGen</a>
        <a href="codegen.html" class="mobile-nav-item {codegen_active}">CodeGen</a>
        <a href="testai.html" class="mobile-nav-item {testai_active}">Test AI</a>
        <a href="deploy.html" class="mobile-nav-item {deploy_active}">Deploy</a>
        <div class="mobile-nav-cta pill" onclick="scrollToAssessment(event)" style="background:{btn_color};">
          <span style="color:{text_color};">Get a Free Assessment</span>
        </div>
      </nav>
    </div>
  </header>'''

nav_patterns = {
    'codegen.html': (r'      <!-- ================= NAV BAR \(top: 38px, width: 1400px\) ================= -->\s*<nav class="codegen-nav" id="desktopNav">.*?</nav>', r'    <!-- Sticky Mobile Header -->\s*<header class="cg-mob-header">.*?</nav>\s*</div>'),
    'deploy.html': (r'      <!-- ================= NAV ================= -->\s*<nav class="deploy-nav" id="desktopNav">.*?</nav>', r'    <!-- Sticky Mobile Header -->\s*<header class="dp-mob-header">.*?</nav>\s*</div>'),
    'legmod.html': (r'      <!-- ================= NAV ================= -->\s*<nav class="legmod-nav" id="desktopNav">.*?</nav>', r'    <!-- Sticky Mobile Header -->\s*<header class="lm-mob-header">.*?</nav>\s*</div>'),
    'rgen.html': (r'      <!-- ================= NAV BAR \(top: 38px, width: 1400px\) ================= -->\s*<nav class="rgen-nav" id="desktopNav">.*?</nav>', r'    <!-- Sticky Mobile Header -->\s*<header class="rg-mob-header">.*?</nav>\s*</div>'),
    'testai.html': (r'      <!-- ================= NAV ================= -->\s*<nav class="testai-nav" id="desktopNav">.*?</nav>', r'    <!-- Sticky Mobile Header -->\s*<header class="ta-mob-header">.*?</nav>\s*</div>'),
}

for filename, patterns in nav_patterns.items():
    info = files[filename]
    
    # Generate parameterized templates
    desktop = desktop_template.format(
        btn_color=info['color'], text_color=info['text_color'],
        home_color='#fff' if filename == 'index.html' else 'rgba(255,255,255,.75)',
        legmod_color='#fff' if filename == 'legmod.html' else 'rgba(255,255,255,.75)',
        rgen_color='#fff' if filename == 'rgen.html' else 'rgba(255,255,255,.75)',
        codegen_color='#fff' if filename == 'codegen.html' else 'rgba(255,255,255,.75)',
        testai_color='#fff' if filename == 'testai.html' else 'rgba(255,255,255,.75)',
        deploy_color='#fff' if filename == 'deploy.html' else 'rgba(255,255,255,.75)'
    )
    
    mobile = mobile_template.format(
        btn_color=info['color'], text_color=info['text_color'],
        home_active='active' if filename == 'index.html' else '',
        legmod_active='active' if filename == 'legmod.html' else '',
        rgen_active='active' if filename == 'rgen.html' else '',
        codegen_active='active' if filename == 'codegen.html' else '',
        testai_active='active' if filename == 'testai.html' else '',
        deploy_active='active' if filename == 'deploy.html' else ''
    )

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop replacement
    content = re.sub(patterns[0], desktop, content, flags=re.DOTALL)
    
    # Mobile replacement
    content = re.sub(patterns[1], mobile, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Replaced nav in {filename}")

