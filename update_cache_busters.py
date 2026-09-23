import re, glob, time

html_files = glob.glob('*.html')
timestamp = str(int(time.time()))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update cache busters for css
    content = re.sub(r'assets/css/([a-zA-Z0-9_-]+)\.css\?v=[a-zA-Z0-9_-]+', r'assets/css/\1.css?v=' + timestamp, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated cache busters in {len(html_files)} HTML files.")
