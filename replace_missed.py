import re

desktop_template = '''      <!-- ================= NAV ================= -->
      <div class="abs desktop-nav" style="left:57px; top:38px; width:calc(100% - 114px); height:66px; z-index:50;">
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

# Apply to testai.html
with open('testai.html', 'r', encoding='utf-8') as f:
    content = f.read()

desktop = desktop_template.format(btn_color='#BD00FF', text_color='#000000', home_color='rgba(255,255,255,.75)', legmod_color='rgba(255,255,255,.75)', rgen_color='rgba(255,255,255,.75)', codegen_color='rgba(255,255,255,.75)', testai_color='#fff', deploy_color='rgba(255,255,255,.75)')
mobile = mobile_template.format(btn_color='#BD00FF', text_color='#000000', home_active='', legmod_active='', rgen_active='', codegen_active='', testai_active='active', deploy_active='')

content = re.sub(r'<nav class="testai-nav"[^>]*>.*?</nav>', desktop, content, flags=re.DOTALL)
content = re.sub(r'<header class="ta-mob-header"[^>]*>.*?</header>\s*<!-- Navigation Drawer -->\s*<div class="ta-mob-drawer"[^>]*>.*?</div>', mobile, content, flags=re.DOTALL)
content = re.sub(r'<!-- Sticky Mobile Header -->\s*', '', content, flags=re.DOTALL)
with open('testai.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Apply to deploy.html
with open('deploy.html', 'r', encoding='utf-8') as f:
    content = f.read()

desktop = desktop_template.format(btn_color='#2AD6DF', text_color='#000000', home_color='rgba(255,255,255,.75)', legmod_color='rgba(255,255,255,.75)', rgen_color='rgba(255,255,255,.75)', codegen_color='rgba(255,255,255,.75)', testai_color='rgba(255,255,255,.75)', deploy_color='#fff')
mobile = mobile_template.format(btn_color='#2AD6DF', text_color='#000000', home_active='', legmod_active='', rgen_active='', codegen_active='', testai_active='', deploy_active='active')

content = re.sub(r'<nav class="deploy-nav"[^>]*>.*?</nav>', desktop, content, flags=re.DOTALL)
content = re.sub(r'<header class="dp-mob-header"[^>]*>.*?</header>\s*<!-- Navigation Drawer -->\s*<div class="dp-mob-drawer"[^>]*>.*?</div>', mobile, content, flags=re.DOTALL)
content = re.sub(r'<!-- Sticky Mobile Header -->\s*', '', content, flags=re.DOTALL)
with open('deploy.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("testai.html and deploy.html updated!")
