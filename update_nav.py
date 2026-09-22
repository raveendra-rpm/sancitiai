import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the dynamic right-anchored width with the fixed center-anchored width from legmod.html
    content = content.replace(
        'style="left:57px; top:38px; right:57px; height:66px; z-index:50;"',
        'style="left:50%; top:38px; transform:translateX(-50%); width:1400px; height:66px; z-index:50;"'
    )
    # Also replace in case it still has the old 1400px without transform
    content = content.replace(
        'style="left:57px; top:38px; width:1400px; height:66px; z-index:50;"',
        'style="left:50%; top:38px; transform:translateX(-50%); width:1400px; height:66px; z-index:50;"'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated desktop nav panels to match legmod.html.")
