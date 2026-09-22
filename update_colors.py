with open('codegen.html', 'r', encoding='utf-8') as f:
    content = f.read()
# Replace text color for button in codegen
content = content.replace('color:rgba(7,7,14,.9); font-weight:600;">Book a free Assessment', 'color:#FFFFFF; font-weight:600;">Book a free Assessment')
with open('codegen.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('rgen.html', 'r', encoding='utf-8') as f:
    content2 = f.read()
# Replace background color for form and button
content2 = content2.replace('background:#3600B3;', 'background:#2AD6DF;')
# Replace text color for button
content2 = content2.replace('color:rgba(7,7,14,.9); font-weight:600;">Book a free Assessment', 'color:#FFFFFF; font-weight:600;">Book a free Assessment')
with open('rgen.html', 'w', encoding='utf-8') as f:
    f.write(content2)
print("Updated codegen.html and rgen.html")
