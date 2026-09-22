import re

with open('codegen.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace opacity for glows
def repl(match):
    prefix = match.group(1)
    val = float(match.group(2))
    new_val = round(val / 3, 2)
    return f'{prefix}opacity:{new_val};'

# Match opacity inside style tags of div or img with class cg-glow-img, cg-ambient-glow, or cg-sec-glow
new_content = re.sub(r'((?:cg-glow-img|cg-ambient-glow|cg-sec-glow)[^>]*style="[^"]*)opacity:\s*([\d.]+);', repl, content)

with open('codegen.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done replacing opacities in codegen.html')
