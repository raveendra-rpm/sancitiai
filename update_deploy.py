with open('deploy.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the wrong mint green with the correct cyan accent color
content = content.replace('background:#00FFC2;', 'background:#2AD6DF;')

with open('deploy.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated deploy.html colors")
