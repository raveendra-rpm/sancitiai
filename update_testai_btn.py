import sys

file_path = 'testai.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace desktop nav button
content = content.replace(
    'background:#BD00FF;',
    'background:var(--cyan);'
)

# Replace the text color
content = content.replace(
    'color:#000000;',
    'color:var(--ink);'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated testai.html nav button colors.")
