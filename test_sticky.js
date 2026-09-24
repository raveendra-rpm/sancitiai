// Sticky Header Logic for Scaled Stage
function updateStickyHeader() {
    const scaler = document.getElementById('scaler');
    if (!scaler || scaler.style.display === 'none') return;
    
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
        // We want the element to stick at top: 0 visually.
        const scaledScrollY = scrollY / scale;
        const translateY = Math.max(0, scaledScrollY - origTop);
        
        // Apply transform
        nav.style.transform = 'translateY(' + translateY + 'px)';
        
        // Ensure it stays on top of everything
        nav.style.zIndex = '9999';
    });
}

// Add event listeners for scroll and resize
window.addEventListener('scroll', () => {
    requestAnimationFrame(updateStickyHeader);
});
window.addEventListener('resize', () => {
    requestAnimationFrame(updateStickyHeader);
});
