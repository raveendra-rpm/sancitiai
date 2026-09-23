import sys

def update_nav_btn(file_path, old_bg, old_color):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Nav
    content = content.replace(
        f'style="right:22px; top:11px; padding:0 24px; height:44px; background:{old_bg}; border-radius:999px; display:flex; align-items:center; justify-content:center; cursor:pointer;"',
        'style="right:22px; top:11px; padding:0 24px; height:44px; background:var(--cyan); border-radius:999px; display:flex; align-items:center; justify-content:center; cursor:pointer;"'
    )
    # The text span inside desktop nav
    content = content.replace(
        f'<span class="font-disp" style="color:{old_color}; font-size:16px; font-weight:bold; white-space:nowrap;">Get a free Assessment</span>',
        '<span class="font-disp" style="color:var(--ink); font-size:16px; font-weight:bold; white-space:nowrap;">Get a free Assessment</span>'
    )

    # Mobile Demo Btn
    content = content.replace(
        f'<a class="mobile-demo-btn pill" href="javascript:void(0)" id="mobileDemoBtn" onclick="scrollToAssessment(event)" style="background:{old_bg};">',
        '<a class="mobile-demo-btn pill" href="javascript:void(0)" id="mobileDemoBtn" onclick="scrollToAssessment(event)" style="background:var(--cyan);">'
    )
    content = content.replace(
        f'<span style="color:{old_color};">Get a free Assessment</span>',
        '<span style="color:var(--ink);">Get a free Assessment</span>'
    )

    # Mobile Nav Drawer CTA
    content = content.replace(
        f'<div class="mobile-nav-cta pill" onclick="scrollToAssessment(event)" style="background:{old_bg};">',
        '<div class="mobile-nav-cta pill" onclick="scrollToAssessment(event)" style="background:var(--cyan);">'
    )
    content = content.replace(
        f'<span style="color:{old_color};">Get a Free Assessment</span>',
        '<span style="color:var(--ink);">Get a Free Assessment</span>'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update codegen
update_nav_btn('codegen.html', '#0104E1', '#FFFFFF')

# Update rgen
update_nav_btn('rgen.html', '#2AD6DF', '#000000')

# Update deploy
update_nav_btn('deploy.html', '#2AD6DF', '#000000')

print("Updated nav button colors for codegen, rgen, and deploy.")
