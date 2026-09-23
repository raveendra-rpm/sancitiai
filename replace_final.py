import os

with open('rgen.html', 'r', encoding='utf-8') as f:
    content = f.read()

target_block = """    <!-- Header Navigation (Sticky) -->
    <header class="rg-nav">
      <a class="rg-nav-logo" href="index.html" aria-label="Sanciti AI">
        <img src="assets/img/sancitiailogo.png" alt="Sanciti AI" />
      </a>
      <div class="rg-nav-actions">
        <a class="rg-nav-demo-btn" href="javascript:void(0)" onclick="scrollToAssessment(event)">Get a Free Assessment</a>
        <button class="rg-nav-menu-toggle" aria-label="Toggle navigation" onclick="toggleRgDrawer()">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </header>

    <!-- Navigation Drawer -->
    <div class="rg-drawer" id="rgDrawer">
      <a href="index.html">Home</a>
      <a href="legmod.html">LegMod</a>
      <a href="rgen.html" class="active">RGen</a>
      <a href="codegen.html">CodeGen</a>
      <a href="testai.html">Test AI</a>
      <a href="deploy.html">Deploy</a>
      <a onclick="scrollToAssessment(event); toggleRgDrawer()" href="javascript:void(0)" style="color:#2AD6DF; font-weight:600;">Get a Free Assessment</a>
    </div>"""

replacement_block = """    <!-- ================= MOBILE HEADER (< 768px) ================= -->
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
  </header>"""

if target_block in content:
    new_content = content.replace(target_block, replacement_block)
    with open('rgen.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully replaced nav block!")
else:
    print("Target block not found precisely. Trying substring search...")
    import re
    # Just to be safe, if whitespace is weird
    idx = content.find('<!-- Header Navigation (Sticky) -->')
    idx2 = content.find('<!-- 1. Hero Section (Matching Figma Hero Section) -->')
    if idx != -1 and idx2 != -1:
        new_content = content[:idx] + replacement_block + "\n\n" + content[idx2:]
        with open('rgen.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully replaced nav block using index slicing!")
    else:
        print("Failed to find boundaries.")
