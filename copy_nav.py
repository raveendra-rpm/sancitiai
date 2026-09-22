import re
import glob

# 1. Read legmod.html and extract the desktop nav
with open('legmod.html', 'r', encoding='utf-8') as f:
    legmod_content = f.read()

nav_match = re.search(r'(<div class="abs desktop-nav".*?<!-- Navigation Drawer -->)', legmod_content, re.DOTALL)
if not nav_match:
    print("Could not extract nav from legmod.html")
    exit(1)

# Extract just the desktop nav part (stop before the mobile drawer or something)
# The desktop nav is a div. It has inner divs. It ends before <!-- ================= 1. HERO SECTION
desktop_nav_match = re.search(r'(<div class="abs desktop-nav".*?</div>\s*</div>\s*</div>\s*</div>)', legmod_content, re.DOTALL)
# Actually, let's just find the exact string to replace.
# In legmod.html, the desktop nav block starts at <div class="abs desktop-nav" and ends at </div> </div>
