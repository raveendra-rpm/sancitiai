import re

files_info = {
    'legmod.html': {'color': 'var(--cyan)', 'text_color': 'var(--ink)', 'active': 'LegMod'},
    'rgen.html': {'color': '#2AD6DF', 'text_color': '#000000', 'active': 'RGen'},
    'codegen.html': {'color': '#0104E1', 'text_color': '#FFFFFF', 'active': 'CodeGen'},
    'testai.html': {'color': '#BD00FF', 'text_color': '#000000', 'active': 'Test AI'},
    'deploy.html': {'color': '#2AD6DF', 'text_color': '#000000', 'active': 'Deploy'}
}

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract Mobile Nav from index.html
mob_nav_match = re.search(r'(<!-- ================= MOBILE HEADER \(< 768px\) ================= -->\s*<header class="mobile-header".*?</header>)', index_content, re.DOTALL)
if not mob_nav_match:
    print("Could not find mobile nav in index.html")
    exit(1)
mob_nav_template = mob_nav_match.group(1)

# Extract Desktop Nav from index.html
desk_nav_match = re.search(r'(<!-- ================= NAV ================= -->\s*<div class="abs desktop-nav".*?</div>\s*</div>)', index_content, re.DOTALL)
if not desk_nav_match:
    print("Could not find desktop nav in index.html")
    exit(1)
desk_nav_template = desk_nav_match.group(1)

for file, info in files_info.items():
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Customize Desktop Nav Template
    curr_desk = desk_nav_template
    # Replace background color in CTA
    curr_desk = re.sub(r'background:var\(--cyan\);', f'background:{info["color"]};', curr_desk)
    # Replace text color in CTA
    curr_desk = re.sub(r'color:var\(--ink\);', f'color:{info["text_color"]};', curr_desk)
    
    # Fix active state
    curr_desk = curr_desk.replace('<span class="nav-link" style="color:#fff; cursor:pointer;" onclick="window.location.href=\'index.html\';">Home</span>', '<span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href=\'index.html\';">Home</span>')
    curr_desk = curr_desk.replace(f'<span class="nav-link" style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href=\'{file}\';">{info["active"]}</span>', f'<span class="nav-link" style="color:#fff; cursor:pointer;" onclick="window.location.href=\'{file}\';">{info["active"]}</span>')
    
    # 2. Customize Mobile Nav Template
    curr_mob = mob_nav_template
    # Replace background in mobile CTA
    curr_mob = re.sub(r'style="background:var\(--cyan\);"', f'style="background:{info["color"]};"', curr_mob)
    # Replace text color in mobile CTA
    curr_mob = re.sub(r'<span style="color:var\(--ink\);">Get a free Assessment</span>', f'<span style="color:{info["text_color"]};">Get a free Assessment</span>', curr_mob)
    curr_mob = re.sub(r'<span style="color:var\(--ink\);">Get a Free Assessment</span>', f'<span style="color:{info["text_color"]};">Get a Free Assessment</span>', curr_mob)
    
    # Fix active state in mobile nav
    curr_mob = curr_mob.replace('<a href="index.html" class="mobile-nav-item active">Home</a>', '<a href="index.html" class="mobile-nav-item ">Home</a>')
    curr_mob = curr_mob.replace(f'<a href="{file}" class="mobile-nav-item ">{info["active"]}</a>', f'<a href="{file}" class="mobile-nav-item active">{info["active"]}</a>')

    # Replace Desktop Nav in file
    content = re.sub(r'<!-- ================= NAV ================= -->\s*<div class="abs desktop-nav".*?</div>\s*</div>', curr_desk, content, flags=re.DOTALL)
    
    # Replace Mobile Nav in file
    # For legmod:
    content = re.sub(r'<!-- ================= MOBILE CONTAINER \(<= 768px Fluid Responsive\) ================= -->\s*<div id="mobile-container">\s*<!-- Ambient Glows -->.*?<header class="lm-nav">.*?</header>\s*<!-- Navigation Drawer -->.*?</div>\s*<!-- ================= END LM NAV ================= -->', curr_mob, content, flags=re.DOTALL)
    
    # For other pages, they might have cg-mob-header etc.
    # Let's use a more robust replacement for mobile header:
    if file == 'legmod.html':
        content = re.sub(r'<!-- Header Navigation \(Sticky 64px\) -->.*?<!-- Navigation Drawer -->.*?</div>', curr_mob, content, flags=re.DOTALL)
    elif file == 'codegen.html':
        content = re.sub(r'<header class="cg-mob-header">.*?</header>\s*<!-- Navigation Drawer -->\s*<div class="cg-mob-drawer".*?</div>', curr_mob, content, flags=re.DOTALL)
    elif file == 'testai.html':
        content = re.sub(r'<header class="ta-mob-header">.*?</header>\s*<!-- Navigation Drawer -->\s*<div class="ta-mob-drawer".*?</div>', curr_mob, content, flags=re.DOTALL)
    elif file == 'deploy.html':
        content = re.sub(r'<header class="dp-mob-header">.*?</header>\s*<!-- Navigation Drawer -->\s*<div class="dp-mob-drawer".*?</div>', curr_mob, content, flags=re.DOTALL)
    elif file == 'rgen.html':
        content = re.sub(r'<!-- ================= MOBILE HEADER \(< 768px\) ================= -->\s*<header class="mobile-header".*?</header>', curr_mob, content, flags=re.DOTALL)
        
    # fallback for remaining old mobile headers
    content = re.sub(r'<header class="mobile-header" id="mobileHeader">.*?</header>', curr_mob, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated navs in all files.")
