import re, glob

html_files = [
    'legmod.html',
    'rgen.html',
    'codegen.html',
    'testai.html',
    'deploy.html'
]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the full mobile header string
    match = re.search(r'<!-- ================= MOBILE HEADER \(< 768px\) ================= -->\s*(?:<!-- ================= MOBILE HEADER \(< 768px\) ================= -->\s*)?<header class="mobile-header" id="mobileHeader">.*?</header>', content, re.DOTALL)
    
    if match:
        header_str = match.group(0)
        
        # Remove it from its current location inside mobile-container
        content = content.replace(header_str, '')
        
        # Insert it right after the body tag / noscript tag
        # The best place is right before <!-- ================= MOBILE CONTAINER (<= 768px Fluid Responsive) ================= -->
        insertion_point = r'<!-- ================= MOBILE CONTAINER \(<= 768px Fluid Responsive\) ================= -->'
        
        content = re.sub(insertion_point, header_str + '\n\n    ' + insertion_point, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Moved mobile-header outside mobile-container in all 5 files.")
