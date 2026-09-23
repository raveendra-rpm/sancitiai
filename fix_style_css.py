file_path = 'assets/css/style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hidden rule with a dummy class
content = content.replace(
    '  body.has-mobile-stage .mobile-header {\n    display: none !important;\n  }',
    '  body.has-mobile-stage .mobile-header-hidden {\n    display: none !important;\n  }'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed display:none for .mobile-header in style.css.")
