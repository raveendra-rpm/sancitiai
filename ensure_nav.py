import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's completely replace the desktop nav with the one from legmod.html
    # First, extract legmod.html desktop nav
    with open('legmod.html', 'r', encoding='utf-8') as lf:
        legmod = lf.read()
    
    legmod_nav = re.search(r'<div class="abs desktop-nav".*?</nav>', legmod, re.DOTALL)
    # Actually, the desktop nav in legmod.html ends with </div> \n </div> \n </div> \n </div>
    # It's safer to just replace the inline style of the container.
    content = re.sub(
        r'<div class="abs desktop-nav" style="[^"]*">',
        '<div class="abs desktop-nav" style="left:50%; top:38px; transform:translateX(-50%); width:1400px; height:66px; z-index:50;">',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
