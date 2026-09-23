files_to_fix = ['assets/css/legmod-mobile.css', 'assets/css/rgen-mobile.css']

for file in files_to_fix:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We replace "#scaler,\n  .mobile-header {" with "#scaler,\n  .mobile-header-hidden {"
    # Just in case, let's use a simpler replace
    content = content.replace(
        '  #scaler,\n  .mobile-header {\n    display: none !important;\n  }',
        '  #scaler,\n  .mobile-header-hidden {\n    display: none !important;\n  }'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed mobile-header display issue in legmod and rgen CSS.")
