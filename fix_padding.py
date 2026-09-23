import os

html_files = ['codegen.html', 'rgen.html', 'testai.html', 'deploy.html']
css_files = {
    'codegen.html': 'assets/css/codegen.css',
    'rgen.html': 'assets/css/rgen.css',
    'testai.html': 'assets/css/testai.css',
    'deploy.html': 'assets/css/deploy.css'
}

for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update data-width to 1512
    content = content.replace('data-width="1440"', 'data-width="1512"')

    # 2. Revert nav bar to 1400px
    content = content.replace(
        'style="left:0; right:0; margin:0 auto; top:38px; width:1328px; height:66px; z-index:50;"',
        'style="left:0; right:0; margin:0 auto; top:38px; width:1400px; height:66px; z-index:50;"'
    )

    # 3. Revert link offset to 560px
    content = content.replace(
        'left:531px;',
        'left:560px;'
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

    # 4. Inject the CSS centering rule
    css_file = css_files[html_file]
    stage_class = '.' + html_file.split('.')[0] + '-stage'
    
    css_injection = f'''
/* --- Dynamic Stage Centering Fix --- */
{stage_class} {{ width: 1512px !important; }}
{stage_class} > * {{ transform: translateX(36px); }}
{stage_class} > .desktop-nav,
{stage_class} > .mobile-header,
{stage_class} > .mobile-header-hidden {{ transform: none !important; }}
'''
    
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
        
    if "Dynamic Stage Centering Fix" not in css_content:
        with open(css_file, 'a', encoding='utf-8') as f:
            f.write(css_injection)

print("Applied 1512px stage + 36px translate fix + 1400px nav to all 4 pages!")
