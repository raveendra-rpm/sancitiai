import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for desktop playbook links
    content = re.sub(
        r'href="#(codegen|deploy|lm|rg|testai)-playbook"',
        r'href="javascript:void(0)" onclick="scrollToAssessment(event)"',
        content
    )
    
    # Pattern for mobile playbook links
    content = re.sub(
        r'href="#(codegen|deploy|lm|rg|testai)-playbook-mob"',
        r'href="javascript:void(0)" onclick="scrollToAssessment(event)"',
        content
    )
    
    # Also catch href="#lead-form" from rgen.html
    content = re.sub(
        r'href="#lead-form"',
        r'href="javascript:void(0)" onclick="scrollToAssessment(event)"',
        content
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
