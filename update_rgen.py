import os
import re

with open('rgen.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inline margin: 0 auto; with margin: 0; for the 4 stage cards
new_content = content.replace('<div style="width: 100%; max-width: 334px; margin: 0 auto;">', '<div style="width: 100%; max-width: 334px; margin: 0;">')

with open('rgen.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated HTML inline styles")
