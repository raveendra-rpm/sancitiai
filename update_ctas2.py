import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all anchor tags that contain "Get a Free Assessment"
    # and replace their href with javascript:void(0) and add onclick
    
    def repl(m):
        a_tag = m.group(0)
        # If it already has onclick='scrollToAssessment(event)' we can just skip or fix href
        if 'scrollToAssessment' not in a_tag:
            # Replace href="#..." with href="javascript:void(0)" onclick="scrollToAssessment(event)"
            a_tag = re.sub(r'href="#[^"]*"', 'href="javascript:void(0)" onclick="scrollToAssessment(event)"', a_tag)
        else:
            # If it already has onclick, just ensure href is void
            a_tag = re.sub(r'href="#[^"]*"', 'href="javascript:void(0)"', a_tag)
        return a_tag

    # Match the entire <a> ... </a> block if it contains "Get a Free Assessment"
    content = re.sub(r'<a\b[^>]*>(?:(?!</a>).)*?Get a [fF]ree Assessment.*?</a>', repl, content, flags=re.IGNORECASE | re.DOTALL)
    
    # Also fix <a href="#codegen-playbook-mob" style="..." onclick="toggleCgDrawer()">Get a Free Assessment</a>
    # We should add scrollToAssessment there too.
    def repl2(m):
        a_tag = m.group(0)
        if 'scrollToAssessment' not in a_tag:
            # append scrollToAssessment to existing onclick
            a_tag = re.sub(r'onclick="([^"]*)"', r'onclick="\1; scrollToAssessment(event)"', a_tag)
            a_tag = re.sub(r'href="#[^"]*"', 'href="javascript:void(0)"', a_tag)
        return a_tag
    
    content = re.sub(r'<a\b[^>]*onclick="toggle[^"]*"[^>]*>(?:(?!</a>).)*?Get a [fF]ree Assessment.*?</a>', repl2, content, flags=re.IGNORECASE | re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
