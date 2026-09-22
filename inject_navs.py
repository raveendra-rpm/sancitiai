import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract Mobile Nav
mob_nav_match = re.search(r'(<!-- ================= MOBILE HEADER.*?<!-- ================= MOBILE HERO SECTION)', idx_content, re.DOTALL | re.IGNORECASE)
mob_nav_raw = mob_nav_match.group(1).replace('<!-- ================= MOBILE HERO SECTION', '').strip()

# Extract Desktop Nav
desk_nav_match = re.search(r'(<!-- ================= NAV ================= -->\s*<div class="abs desktop-nav".*?</div>\s*</div>)', idx_content, re.DOTALL | re.IGNORECASE)
desk_nav_raw = desk_nav_match.group(1)

def set_active(nav_html, filename):
    page_name = filename.replace('.html', '')
    
    # Reset all actives
    nav_html = nav_html.replace('mobile-nav-item active', 'mobile-nav-item ')
    # The desktop nav in index.html doesn't use active class, but uses color:#fff for active, color:rgba(255,255,255,.75) for inactive
    # Let's just use what's in index.html for desktop nav, since user said 'same'
    
    # Set active for mobile
    if page_name == 'index':
        nav_html = nav_html.replace('href="index.html" class="mobile-nav-item "', 'href="index.html" class="mobile-nav-item active"')
    elif page_name == 'legmod':
        nav_html = nav_html.replace('href="legmod.html" class="mobile-nav-item "', 'href="legmod.html" class="mobile-nav-item active"')
    elif page_name == 'rgen':
        nav_html = nav_html.replace('href="rgen.html" class="mobile-nav-item "', 'href="rgen.html" class="mobile-nav-item active"')
    elif page_name == 'codegen':
        nav_html = nav_html.replace('href="codegen.html" class="mobile-nav-item "', 'href="codegen.html" class="mobile-nav-item active"')
    elif page_name == 'testai':
        nav_html = nav_html.replace('href="testai.html" class="mobile-nav-item "', 'href="testai.html" class="mobile-nav-item active"')
    elif page_name == 'deploy':
        nav_html = nav_html.replace('href="deploy.html" class="mobile-nav-item "', 'href="deploy.html" class="mobile-nav-item active"')
        
    return nav_html

files = ['legmod.html', 'rgen.html', 'codegen.html', 'testai.html', 'deploy.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # REPLACE DESKTOP NAV
    # Find existing desktop nav
    content = re.sub(r'<!-- ================= NAV ================= -->\s*<div class="abs desktop-nav".*?</div>\s*</div>', desk_nav_raw, content, flags=re.DOTALL)
    
    # REPLACE MOBILE NAV
    mob_nav_configured = set_active(mob_nav_raw, file)
    
    # Depending on the file, the mobile nav might be different
    if file == 'legmod.html':
        content = re.sub(r'<!-- Header Navigation.*?</div>\s*</div>', mob_nav_configured, content, flags=re.DOTALL | re.IGNORECASE)
    elif file == 'rgen.html':
        content = re.sub(r'<header class="rg-nav">.*?</nav>\s*</div>', mob_nav_configured, content, flags=re.DOTALL | re.IGNORECASE)
    else:
        # testai, deploy, codegen might have mobile-header or cg-mob-header
        content = re.sub(r'<header class="cg-mob-header">.*?</nav>\s*</div>', mob_nav_configured, content, flags=re.DOTALL | re.IGNORECASE)
        content = re.sub(r'<!-- ================= MOBILE HEADER.*?</header>', mob_nav_configured, content, flags=re.DOTALL | re.IGNORECASE)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated nav across all files.")
