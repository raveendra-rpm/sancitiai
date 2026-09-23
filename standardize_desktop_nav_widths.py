import re

files_info = [
    'rgen.html',
    'codegen.html',
    'testai.html',
    'deploy.html'
]

for file in files_info:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update width:1400px -> width:1320px for desktop-nav
    content = re.sub(
        r'<div class="abs desktop-nav" style="left:0; right:0; margin:0 auto; top:38px; width:1400px; height:66px; z-index:50;">',
        '<div class="abs desktop-nav" style="left:0; right:0; margin:0 auto; top:38px; width:1320px; height:66px; z-index:50;">',
        content
    )
    
    # 2. Update left:560px -> left:490px for the desktop-nav-menu
    content = re.sub(
        r'<div class="abs font-disp desktop-nav-menu"\s*style="display:flex; align-items:center; left:560px; top:23px; width:600px; font-size:16px; gap:36px; color:#fff;">',
        '<div class="abs font-disp desktop-nav-menu"\n          style="display:flex; align-items:center; left:490px; top:23px; width:600px; font-size:16px; gap:36px; color:#fff;">',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated nav widths in 1440px files.")
