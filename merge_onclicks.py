import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    def merge_onclicks(m):
        full_tag = m.group(0)
        # Find all onclick attributes
        onclicks = re.findall(r'onclick="([^"]*)"', full_tag)
        if len(onclicks) > 1:
            merged = "; ".join(onclicks)
            # Remove all existing onclicks
            full_tag = re.sub(r'\s*onclick="[^"]*"', '', full_tag)
            # Insert the merged onclick
            full_tag = full_tag.replace('href=', f'onclick="{merged}" href=')
        return full_tag

    content = re.sub(r'<a\b[^>]*onclick="[^"]*"[^>]*onclick="[^"]*"[^>]*>', merge_onclicks, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
