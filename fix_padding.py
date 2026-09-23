import re, time

# 1. codegen, legmod, rgen
files_1 = ['assets/css/codegen-mobile.css', 'assets/css/legmod-mobile.css', 'assets/css/rgen-mobile.css']
for file in files_1:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace ONLY the first occurrence (which is inside the body rule)
    content = content.replace('padding-top: 0 !important;', 'padding-top: 64px !important;', 1)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. testai, deploy
files_2 = ['assets/css/testai-mobile.css', 'assets/css/deploy-mobile.css']
for file in files_2:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace padding: 0 !important; with padding: 0 !important; \n    padding-top: 64px !important;
    # But only for the first occurrence (body rule)
    content = content.replace('padding: 0 !important;', 'padding: 0 !important;\n    padding-top: 64px !important;', 1)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Update HTML cache busters
import glob
html_files = glob.glob('*.html')
timestamp = str(int(time.time()))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'assets/css/([a-zA-Z0-9_-]+)\.css\?v=[a-zA-Z0-9_-]+', r'assets/css/\1.css?v=' + timestamp, content)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed mobile padding-top in all 5 CSS files and updated HTML cache busters.")
