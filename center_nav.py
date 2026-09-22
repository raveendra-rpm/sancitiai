import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace width: calc(100% - 114px); and left:57px; with centered 1400px
    content = re.sub(
        r'style="left:57px; top:38px; (?:right:57px;|width:\s*calc\(100% - 114px\);|width:1400px;) height:66px; z-index:50;"',
        r'style="left:50%; top:38px; transform:translateX(-50%); width:1400px; height:66px; z-index:50;"',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated desktop nav to be perfectly centered and 1400px wide.")
