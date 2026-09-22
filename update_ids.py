import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add id="centered-playbook" to <div class="abs centered-playbook" if not present
    content = re.sub(r'<div class="abs centered-playbook"(?!.*id="centered-playbook")', r'<div id="centered-playbook" class="abs centered-playbook"', content)
    
    # Same if it's class="centered-playbook abs" (unlikely, but just in case)
    content = re.sub(r'<div class="centered-playbook abs"(?!.*id="centered-playbook")', r'<div id="centered-playbook" class="centered-playbook abs"', content)

    # Add id="mobile-playbook-bottom" to <section class="mobile-playbook-bottom" if not present
    content = re.sub(r'<section class="mobile-playbook-bottom"(?!.*id="mobile-playbook-bottom")', r'<section id="mobile-playbook-bottom" class="mobile-playbook-bottom"', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Updated IDs in HTML files.")
