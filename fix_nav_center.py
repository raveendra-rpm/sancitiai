import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the desktop nav style
    content = re.sub(
        r'<div class="abs desktop-nav" style="left:50%; top:38px; transform:translateX\(-50%\); width:1400px; height:66px; z-index:50;">',
        '<div class="abs desktop-nav" style="left:0; right:0; margin:0 auto; top:38px; width:1400px; height:66px; z-index:50;">',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
