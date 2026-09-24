import os

with open('assets/js/script.js', 'a', encoding='utf-8') as f:
    f.write('''

// ================= STICKY DESKTOP HEADER LOGIC =================
// Keeps the .desktop-nav visible on screen when scrolling inside the scaled #stage
function updateStickyHeader() {
    const scaler = document.getElementById('scaler');
    if (!scaler || scaler.style.display === 'none') {
        // If mobile layout, reset any transform on desktop nav just in case
        document.querySelectorAll('.desktop-nav').forEach(nav => {
            nav.style.transform = '';
        });
        return;
    }
    
    const viewport = Math.max(320, document.documentElement.clientWidth || window.innerWidth);
    const stage = document.getElementById('stage');
    if (!stage) return;
    
    let designWidth = stage.dataset.width ? parseFloat(stage.dataset.width) : 1512;
    const scale = viewport / designWidth;
    
    const navs = document.querySelectorAll('.desktop-nav');
    const scrollY = window.scrollY || document.documentElement.scrollTop;
    
    navs.forEach(nav => {
        // Find original top position
        let origTop = nav.dataset.origTop;
        if (!origTop) {
            origTop = parseFloat(getComputedStyle(nav).top) || 0;
            nav.dataset.origTop = origTop;
        }
        
        // Calculate the translation needed to act as position: sticky
        const scaledScrollY = scrollY / scale;
        const translateY = Math.max(0, scaledScrollY - origTop);
        
        // Apply transform. 
        // Note: For deploy.html, codegen.html, rgen.html, testai.html we had CSS translateX(36px).
        // Since we are overriding transform, we must preserve any necessary centering.
        // Wait! .abs.desktop-nav in HTML has margin: 0 auto; left: 0; right: 0;. 
        // But in CSS we wrote: .codegen-stage > .desktop-nav { transform: none !important; } earlier to remove the 36px shift!
        // So 	ranslateY(...) is perfectly safe here.
        nav.style.transform = 'translateY(' + translateY + 'px)';
        nav.style.zIndex = '9999';
    });
}

window.addEventListener('scroll', () => {
    requestAnimationFrame(updateStickyHeader);
});
window.addEventListener('resize', () => {
    requestAnimationFrame(updateStickyHeader);
});
// Run once on load
setTimeout(updateStickyHeader, 100);

''')

print("Added sticky header logic to script.js")
