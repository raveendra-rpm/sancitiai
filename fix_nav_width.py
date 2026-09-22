import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the fixed width with right:57px
    content = content.replace(
        'style="left:57px; top:38px; width:1400px; height:66px; z-index:50;"',
        'style="left:57px; top:38px; right:57px; height:66px; z-index:50;"'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Fixed navigation widths.")
