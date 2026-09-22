import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find <a ...> ... Get a Free Assessment ... </a>
    # We will just replace href="#<something>" with href="javascript:void(0)" onclick="scrollToAssessment(event)"
    
    # 1. Update anchor tags that have href="#..." and text "Get a Free Assessment" or similar
    content = re.sub(
        r'href="#[^"]*"(>.*?Get a [fF]ree Assessment.*?</a|>[^<]*<span[^>]*>Get a [fF]ree Assessment)',
        r'href="javascript:void(0)" onclick="scrollToAssessment(event)"\1',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
