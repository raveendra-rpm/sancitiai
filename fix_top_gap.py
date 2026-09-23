import os

html_files = ['codegen.html', 'rgen.html', 'testai.html', 'deploy.html']

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change top:38px to top:0
    content = content.replace('top:38px;', 'top:0;')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Changed top:38px to top:0 in all 4 pages!")
