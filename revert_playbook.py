import sys

file_path = 'testai.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Lines to revert in playbook (desktop)
content = content.replace(
    '<div class="abs" style="left:50%; top:50%; transform:translate(-50%, -50%); width:1000px; height:600px; background:var(--cyan); opacity:0.15; filter:blur(200px); pointer-events:none; z-index:-1;"></div>',
    '<div class="abs" style="left:50%; top:50%; transform:translate(-50%, -50%); width:1000px; height:600px; background:#BD00FF; opacity:0.15; filter:blur(200px); pointer-events:none; z-index:-1;"></div>'
)
content = content.replace(
    'style="padding:14px 40px; background:var(--cyan); border:none; border-radius:50px; text-align:center; cursor:pointer;">',
    'style="padding:14px 40px; background:#BD00FF; border:none; border-radius:50px; text-align:center; cursor:pointer;">'
)

# Lines to revert in playbook (mobile)
content = content.replace(
    '<div style="position: absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:100%; height:100%; background:var(--cyan); opacity:0.1; filter:blur(100px); pointer-events:none; z-index:-1;"></div>',
    '<div style="position: absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:100%; height:100%; background:#BD00FF; opacity:0.1; filter:blur(100px); pointer-events:none; z-index:-1;"></div>'
)
content = content.replace(
    'style="width:100%; padding:14px 0; background:var(--cyan); border:none; border-radius:50px; text-align:center; cursor:pointer;">',
    'style="width:100%; padding:14px 0; background:#BD00FF; border:none; border-radius:50px; text-align:center; cursor:pointer;">'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted playbook theme colors to purple in testai.html.")
