import os

with open('rgen.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
match = re.search(r'<!-- Header Navigation \(Sticky\) -->.*?</div>\s*<!-- Navigation Drawer -->.*?</div>', content, re.DOTALL)
if match:
    print("Found the nav block!")
    start = match.start()
    end = match.end()
    
    # We also need to add the mobile header script? Or is it in script.js?
    # Actually, toggleMobileMenu is in script.js. 
    # toggleRgDrawer is in script.js but we will stop using it.
    
    mobile_header_html = '''<!-- ================= MOBILE HEADER (< 768px) ================= -->
  <header class="mobile-header" id="mobileHeader">
    <div class="mobile-header-inner">
      <a class="mobile-logo" href="index.html" aria-label="Sanciti AI">
        <img alt="Sanciti AI" src="assets/img/sancitiailogo.png" />
      </a>
      <div class="mobile-header-right">
        <a class="mobile-demo-btn pill" href="javascript:void(0)" id="mobileDemoBtn" onclick="scrollToAssessment(event)" style="background:var(--cyan);">
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
        <a href="index.html" class="mobile-nav-item ">Home</a>
        <a href="legmod.html" class="mobile-nav-item ">LegMod</a>
        <a href="rgen.html" class="mobile-nav-item active">RGen</a>
        <a href="codegen.html" class="mobile-nav-item ">CodeGen</a>
        <a href="testai.html" class="mobile-nav-item ">Test AI</a>
        <a href="deploy.html" class="mobile-nav-item ">Deploy</a>
        <div class="mobile-nav-cta pill" onclick="scrollToAssessment(event)" style="background:var(--cyan);">
          <span style="color:var(--ink);">Get a free Assessment</span>
        </div>
      </nav>
    </div>
  </header>'''
    
    new_content = content[:start] + mobile_header_html + content[end:]
    
    with open('rgen.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replaced rg-nav with standard mobile-header!")
else:
    print("Could not find the rg-nav block!")

