import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Mobile Header + Drawer
mob_nav_match = re.search(r'(<!-- ================= MOBILE HEADER ================= -->.*?</nav>\s*</div>)', content, re.DOTALL)
if mob_nav_match:
    with open('nav_mobile.html', 'w', encoding='utf-8') as out:
        out.write(mob_nav_match.group(1))
    print("Mobile nav extracted")

# Extract Desktop Nav
desk_nav_match = re.search(r'(<!-- ================= NAV ================= -->.*?</div>\s*</div>)', content, re.DOTALL)
if desk_nav_match:
    with open('nav_desktop.html', 'w', encoding='utf-8') as out:
        out.write(desk_nav_match.group(1))
    print("Desktop nav extracted")
