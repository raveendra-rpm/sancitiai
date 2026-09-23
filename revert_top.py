import os

html_files = ['codegen.html', 'rgen.html', 'testai.html', 'deploy.html']

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert top:0 back to top:38px
    content = content.replace('top:0; width:1400px; height:66px; z-index:50;"', 'top:38px; width:1400px; height:66px; z-index:50;"')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Reverted top:0 to top:38px in all 4 pages!")
