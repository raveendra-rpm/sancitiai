import re

files = {
    'codegen.html': {'color': '#0104E1', 'text_color': '#FFFFFF', 'mobile_footer': r'<footer class="cg-mob-footer sanciti-footer">'},
    'deploy.html': {'color': '#00FFC2', 'text_color': 'rgba(7,7,14,.9)', 'mobile_footer': r'<footer class="sanciti-footer mobile-footer">'},
    'testai.html': {'color': '#BD00FF', 'text_color': 'rgba(7,7,14,.9)', 'mobile_footer': r'<footer class="sanciti-footer mobile-footer">'}
}

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
          <span class="font-body" style="font-size:16px; color:{text_color}; font-weight:600;">Book a free Assessment</span>
        </button>
      </div>
    </form>
  </section>

'''

for filename, info in files.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already injected
    if 'mobile-playbook-bottom' not in content:
        # Insert mobile form before the mobile footer
        mobile_form_html = mobile_form_template.format(color=info["color"], text_color=info["text_color"])
        # Because we only have 1 instance of the mobile footer, we can safely replace it
        content = content.replace(info["mobile_footer"], mobile_form_html + info["mobile_footer"])
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Injected mobile form into {filename}')
    else:
        print(f'Mobile form already present in {filename}')

print('Done.')
