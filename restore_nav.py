import sys

def update_nav_alignment(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change nav container width back to 1400px
    content = content.replace(
        'style="left:0; right:0; margin:0 auto; top:38px; width:1320px; height:66px; z-index:50;"',
        'style="left:0; right:0; margin:0 auto; top:38px; width:1400px; height:66px; z-index:50;"'
    )

    # Change links left offset back to 560px
    content = content.replace(
        'style="display:flex; align-items:center; left:490px; top:23px; width:600px; font-size:16px; gap:36px; color:#fff;"',
        'style="display:flex; align-items:center; left:560px; top:23px; width:600px; font-size:16px; gap:36px; color:#fff;"'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

files = ['codegen.html', 'rgen.html', 'testai.html', 'deploy.html']
for file in files:
    update_nav_alignment(file)

print("Restored 1400px width and 560px left offset to all nav bars.")
