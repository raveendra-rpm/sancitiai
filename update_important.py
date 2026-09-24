import os

with open('assets/js/script.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = "nav.style.transform = 'translateY(' + translateY + 'px)';"
new_str = "nav.style.setProperty('transform', 'translateY(' + translateY + 'px)', 'important');"

content = content.replace(old_str, new_str)

with open('assets/js/script.js', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated script.js to use setProperty with important")
