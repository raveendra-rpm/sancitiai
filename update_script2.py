with open('assets/js/script.js', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('function scrollToAssessment(e) {')

# Find the matching closing brace
stack = []
end_idx = -1
for i in range(start_idx, len(content)):
    if content[i] == '{':
        stack.append('{')
    elif content[i] == '}':
        stack.pop()
        if len(stack) == 0:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    new_func = '''function scrollToAssessment(e) {
    if (e) e.preventDefault();
    if (typeof closeMobileMenu === 'function') closeMobileMenu();
    if (typeof toggleCgDrawer === 'function') toggleCgDrawer(true);
    if (typeof toggleTaDrawer === 'function') toggleTaDrawer(true);
    if (typeof toggleDpDrawer === 'function') toggleDpDrawer(true);
    if (typeof toggleRgDrawer === 'function') toggleRgDrawer(true);
    if (typeof toggleLmDrawer === 'function') toggleLmDrawer(true);

    const isMobile = window.innerWidth <= 768;
    
    if (isMobile) {
        const targetIds = ['mobile-playbook-bottom', 'codegen-playbook-mob', 'testai-playbook-mob', 'deploy-playbook-mob', 'rg-playbook', 'lm-playbook', 'playbook'];
        let target = null;
        for (const id of targetIds) {
            target = document.getElementById(id);
            if (target) break;
        }
        
        if (target) {
            const topPos = Math.max(0, target.offsetTop - (window.innerHeight / 2) + (target.offsetHeight / 2));
            window.scrollTo({ top: topPos, behavior: 'smooth' });
        }
    } else {
        const viewport = Math.max(320, document.documentElement.clientWidth || window.innerWidth);
        const stage = document.getElementById('stage');
        let designWidth = 1512;
        if (stage && stage.dataset.width) {
            designWidth = parseFloat(stage.dataset.width);
        } else {
            if (window.location.pathname.includes('codegen') || window.location.pathname.includes('testai') || window.location.pathname.includes('deploy')) {
                designWidth = 1440;
            }
        }
        
        const scale = viewport / designWidth;
        
        const targetIds = ['centered-playbook', 'codegen-playbook', 'testai-playbook', 'deploy-playbook', 'lead-form', 'lm-playbook', 'playbook-desktop'];
        let target = null;
        for (const id of targetIds) {
            target = document.getElementById(id);
            if (target) break;
        }
        
        if (target) {
            let el = target;
            let offsetTop = 0;
            while(el && el.id !== 'stage' && el.id !== 'scaler') {
                offsetTop += el.offsetTop;
                el = el.offsetParent;
            }
            
            const scaledTop = offsetTop * scale;
            const scaledHeight = target.offsetHeight * scale;
            const topPos = Math.max(0, scaledTop - (window.innerHeight / 2) + (scaledHeight / 2));
            window.scrollTo({ top: topPos, behavior: 'smooth' });
        }
    }
}'''
    content = content[:start_idx] + new_func + content[end_idx+1:]
    
    with open('assets/js/script.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced successfully")
else:
    print("Could not find function")
