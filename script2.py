import re

with open('assets/css/codegen-mobile.css', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(r'(\.cg-mob-frame76-glow\s*{[^}]*)opacity:\s*1;', r'\1opacity: 0.3;', content)

with open('assets/css/codegen-mobile.css', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done replacing opacities in codegen-mobile.css')
