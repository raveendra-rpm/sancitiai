import re

files = ['legmod.html', 'rgen.html', 'codegen.html', 'testai.html', 'deploy.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Get the page name for the link
    page_name = file.replace('.html', '')
    
    # 1. Reset all desktop nav links to .75 opacity
    content = re.sub(r'style="color:#fff; cursor:pointer;" onclick="window\.location\.href=\'([a-z]+)\.html\';"', r'style="color:rgba(255,255,255,.75); cursor:pointer;" onclick="window.location.href=' + r"'\1.html'" + r';"', content)
    
    # 2. Set the current page to #fff
    content = re.sub(r'style="color:rgba\(255,255,255,\.75\); cursor:pointer;" onclick="window\.location\.href=\'' + page_name + r'\.html\';"', r'style="color:#fff; cursor:pointer;" onclick="window.location.href=\'' + page_name + r'.html\';"', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
