import re

files = {
    'legmod.html': {'stage': (8650, 9250), 'footer': (8450, 9050), 'color': 'var(--cyan)', 'mobile_footer': r'<footer class="sanciti-footer"'},
    'codegen.html': {'stage': (9356, 9956), 'footer': (9156, 9756), 'color': '#0104E1', 'mobile_footer': r'<footer class="cg-footer"'},
    'deploy.html': {'stage': (9177, 9777), 'footer': (8977, 9577), 'color': '#00FFC2', 'mobile_footer': r'<footer class="dp-footer"'},
    'rgen.html': {'stage': (9027, 9627), 'footer': (8827, 9427), 'color': '#3600B3', 'mobile_footer': r'<footer class="rg-footer"'},
    'testai.html': {'stage': (9635, 10235), 'footer': (9427, 10027), 'color': '#BD00FF', 'mobile_footer': r'<footer class="ta-footer"'}
}

desktop_form_template = '''
      <!-- ================= CENTERED PLAYBOOK (BEFORE FOOTER) ================= -->
      <div class="abs centered-playbook"
        style="left:0; top:{top}px; width:{width}px; height:600px; display:flex; flex-direction:column; align-items:center; justify-content:center; background: transparent; z-index:10;">
        <div class="abs" style="left:50%; top:50%; transform:translate(-50%, -50%); width:1000px; height:600px; background:{color}; opacity:0.15; filter:blur(200px); pointer-events:none; z-index:-1;"></div>
        <div style="text-align:center; margin-bottom:40px;">
          <p class="font-disp" style="font-size:56px; line-height:1.1; margin:0; color:rgba(255,255,255,.9);">
            <span style="font-weight:200; font-style:italic;">Modernize</span> <span style="font-weight:700;">Legacy Applications</span><br />
            <span style="font-weight:200; font-style:italic;">with</span> <span style="font-weight:700;">Enterprise-Grade AI,</span><br />
            <span style="font-weight:200; font-style:italic;">Get a</span> <span style="font-weight:700;">Free Assessment.</span>
          </p>
        </div>

        <form action="submit_form.php" method="POST"
          style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:24px 30px; width:900px;"
          onsubmit="handleAssessmentSubmit(event)">
          <input type="hidden" name="source" value="index" />
          <div style="display:flex; flex-direction:column; gap:8px;">
            <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Name</span>
            <input name="Name" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="text" required />
          </div>
          <div style="display:flex; flex-direction:column; gap:8px;">
            <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Title</span>
            <input name="Title" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="text" required />
          </div>
          <div style="display:flex; flex-direction:column; gap:8px;">
            <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Email</span>
            <input name="Email" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="email" required />
          </div>
          <div style="display:flex; flex-direction:column; gap:8px;">
            <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Contact number</span>
            <input name="Contact number" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="tel" required />
          </div>
          <div style="display:flex; flex-direction:column; gap:8px;">
            <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Company</span>
            <input name="Company" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="text" required />
          </div>

          <div style="grid-column: 1 / -1; display:flex; justify-content:center; margin-top:16px;">
            <button type="submit" class="pill"
              style="padding:14px 40px; background:{color}; border:none; border-radius:50px; text-align:center; cursor:pointer;">
              <span class="font-body" style="font-size:16px; color:rgba(7,7,14,.9); font-weight:600;">Book a free Assessment</span>
            </button>
          </div>
        </form>
      </div>
'''

mobile_form_template = '''
  <!-- ================= MOBILE PLAYBOOK SECTION ================= -->
  <section class="mobile-playbook-bottom"
    style="padding: 60px 20px 40px; background: transparent; position: relative;">
    <div style="position: absolute; left:50%; top:50%; transform:translate(-50%, -50%); width:100%; height:100%; background:{color}; opacity:0.1; filter:blur(100px); pointer-events:none; z-index:-1;"></div>
    <div style="text-align:center; margin-bottom:30px;">
      <p class="font-disp" style="font-size:32px; line-height:1.2; margin:0; color:rgba(255,255,255,.9);">
        <span style="font-weight:200; font-style:italic;">Modernize</span> <span style="font-weight:700;">Legacy
          Applications</span><br />
        <span style="font-weight:200; font-style:italic;">with</span> <span style="font-weight:700;">Enterprise-Grade
          AI,</span><br />
        <span style="font-weight:200; font-style:italic;">Get a</span> <span style="font-weight:700;">Free
          Assessment.</span>
      </p>
    </div>

    <form action="submit_form.php" method="POST"
      style="display:flex; flex-direction:column; gap:16px; width:100%; max-width:400px; margin:0 auto;"
      onsubmit="handleAssessmentSubmit(event)">
      <input type="hidden" name="source" value="index" />
      <div style="display:flex; flex-direction:column; gap:8px;">
        <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Name</span>
        <input name="Name" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="text" required />
      </div>
      <div style="display:flex; flex-direction:column; gap:8px;">
        <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Title</span>
        <input name="Title" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="text" required />
      </div>
      <div style="display:flex; flex-direction:column; gap:8px;">
        <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Email</span>
        <input name="Email" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="email" required />
      </div>
      <div style="display:flex; flex-direction:column; gap:8px;">
        <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Contact number</span>
        <input name="Contact number" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="tel" required />
      </div>
      <div style="display:flex; flex-direction:column; gap:8px;">
        <span class="font-body" style="font-size:14px; color:rgba(255,255,255,.75);">Company</span>
        <input name="Company" style="height:48px; width:100%; background:rgba(255,255,255,.9); border:none; border-radius:4px; padding:0 16px; font-size:16px; box-sizing:border-box;" type="text" required />
      </div>

      <div style="display:flex; justify-content:center; margin-top:8px;">
        <button type="submit" class="pill"
          style="width:100%; padding:14px 0; background:{color}; border:none; border-radius:50px; text-align:center; cursor:pointer;">
          <span class="font-body" style="font-size:16px; color:rgba(7,7,14,.9); font-weight:600;">Book a free Assessment</span>
        </button>
      </div>
    </form>
  </section>

'''

for filename, info in files.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine width (legmod is 1512, others 1440)
    width = 1512 if filename == 'legmod.html' else 1440

    # 1. Replace stage height
    content = content.replace(f'height: {info["stage"][0]}px', f'height: {info["stage"][1]}px')
    content = content.replace(f'height:{info["stage"][0]}px', f'height:{info["stage"][1]}px')

    # 2. Update inline footer top if it exists
    if f'top:{info["footer"][0]}px' in content:
        content = content.replace(f'top:{info["footer"][0]}px', f'top:{info["footer"][1]}px')

    # 3. Insert desktop form before the desktop footer
    desktop_footer_regex = r'(<footer[^>]*desktop-footer[^>]*>)'
    desktop_form_html = desktop_form_template.format(top=info["footer"][0], width=width, color=info["color"])
    content = re.sub(desktop_footer_regex, desktop_form_html + r'\n      \1', content)

    # 4. Insert mobile form before the mobile footer
    mobile_form_html = mobile_form_template.format(color=info["color"])
    content = re.sub(f'({info["mobile_footer"]})', mobile_form_html + r'\1', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated HTML files.')
