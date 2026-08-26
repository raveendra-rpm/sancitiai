// Scale the fixed 1512px stage to fit any viewport, preserving 1:1 fidelity of the Figma design.
function fitStage() {
    const stage = document.getElementById('stage');
    const scaler = document.getElementById('scaler');
    if (!stage || !scaler) return;
    const viewport = Math.max(320, window.innerWidth);
    const scale = viewport / 1512;
    const isMobile = window.innerWidth <= 768;

    if (isMobile) {
        stage.style.transform = 'scale(' + scale + ') translateY(-1790px)';
        stage.style.transformOrigin = 'top left';
        scaler.style.height = (Math.max(0, stage.getBoundingClientRect().height - (1790 * scale))) + 'px';
    } else {
        stage.style.transform = 'scale(' + scale + ')';
        stage.style.transformOrigin = 'top left';
        scaler.style.height = (stage.getBoundingClientRect().height) + 'px';
    }
    scaler.style.width = '100%';
}
window.addEventListener('resize', fitStage);
window.addEventListener('load', fitStage);
fitStage();
setTimeout(fitStage, 400);

// Scroll reveal
const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add('in');
            io.unobserve(e.target);
        }
    });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach((el, i) => {
    el.style.transitionDelay = (i % 6) * 60 + 'ms';
    io.observe(el);
});

// Smooth Drag-to-scroll & Wheel-scroll for the horizontally scrollable certifications strip
document.querySelectorAll('.cert-scroll').forEach((strip) => {
    let isDown = false, startX = 0, startScroll = 0, velX = 0, lastX = 0, momentumID = null;

    function getScale() {
        const viewport = Math.max(320, window.innerWidth);
        return viewport / 1512;
    }

    strip.addEventListener('mousedown', (e) => {
        isDown = true;
        strip.classList.add('dragging');
        if (momentumID) cancelAnimationFrame(momentumID);
        const scale = getScale();
        startX = e.pageX / scale;
        lastX = startX;
        startScroll = strip.scrollLeft;
        velX = 0;
    });

    window.addEventListener('mouseup', () => {
        if (!isDown) return;
        isDown = false;
        strip.classList.remove('dragging');
        
        // Apply smooth momentum deceleration
        function step() {
            if (Math.abs(velX) > 0.5) {
                strip.scrollLeft += velX;
                velX *= 0.92;
                momentumID = requestAnimationFrame(step);
            }
        }
        momentumID = requestAnimationFrame(step);
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const scale = getScale();
        const currentX = e.pageX / scale;
        const walk = currentX - startX;
        strip.scrollLeft = startScroll - walk;
        velX = -(currentX - lastX) * 1.1;
        lastX = currentX;
    });
});


// Agent carousel controller. Uses the in-page animated slide layer so text
// alignment stays responsive and editable while keeping the existing effects.
(function () {
    const track = document.getElementById('agentTrack');
    const carousel = document.getElementById('agentCarousel');
    if (!track || !carousel) return;

    const slides = Array.from(track.querySelectorAll('.agent-slide'));
    let idx = 0;
    let timer;

    function show(i) {
        idx = (i + slides.length) % slides.length;
        track.style.transform = 'translateX(' + (-idx * 1512) + 'px)';
        slides.forEach((slide, slideIndex) => {
            slide.classList.toggle('is-active', slideIndex === idx);
        });
    }

    function restartTimer() {
        clearInterval(timer);
        timer = setInterval(() => show(idx + 1), 3600);
    }

    function next() {
        show(idx + 1);
        restartTimer();
    }

    // Click anywhere on the animation to move immediately to the next agent.
    carousel.addEventListener('click', next);

    // Keyboard: right/space/enter = next agent, left = previous.
    window.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
            e.preventDefault();
            next();
        } else if (e.key === 'ArrowLeft') {
            e.preventDefault();
            show(idx - 1);
            restartTimer();
        }
    });

    // Existing nav links can still call this.
    window.goToAgentSlide = function (i) {
        if (typeof show === 'function') {
            show(i);
            restartTimer();
        }
        const states = ['state-legmod', 'state-rgen', 'state-codegen', 'state-testai', 'state-deploy'];
        if (typeof setOrchestratorState === 'function' && states[i]) {
            setOrchestratorState(states[i]);
        }
        const orch = document.getElementById('orchestrator');
        if (orch) {
            const viewport = Math.max(320, window.innerWidth);
            const scale = Math.min(1, viewport / 1512);
            const isMobile = window.innerWidth <= 768;
            if (isMobile) {
                const scaler = document.getElementById('scaler');
                const topPos = (scaler ? scaler.offsetTop : 0) + ((8613 - 1790) * scale) - 70;
                window.scrollTo({ top: topPos, behavior: 'smooth' });
            } else {
                const topPos = 8613 * scale;
                window.scrollTo({ top: topPos, behavior: 'smooth' });
            }
        }
    };

    show(0);
    restartTimer();
})();

// State Handlers for Orchestrator section
function setOrchestratorState(state, e) {
    if (e) e.stopPropagation();
    const container = document.getElementById('orchestrator-container');
    if (!container) return;
    
    container.classList.remove('state-legmod', 'state-deploy', 'state-rgen', 'state-codegen', 'state-testai');
    container.classList.add(state);

    // Sync mobile tabs
    document.querySelectorAll('.orch-tab-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-state') === state);
    });
}

function resetOrchestratorState() {
    const container = document.getElementById('orchestrator-container');
    if (container && !container.classList.contains('state-legmod')) {
        container.classList.remove('state-deploy', 'state-rgen', 'state-codegen', 'state-testai');
        container.classList.add('state-legmod');

        // Sync mobile tabs
        document.querySelectorAll('.orch-tab-btn').forEach(btn => {
            btn.classList.toggle('active', btn.getAttribute('data-state') === 'state-legmod');
        });
    }
}

// Global click listener to reset state when clicking outside the active box
document.addEventListener('click', (e) => {
    const container = document.getElementById('orchestrator-container');
    if (!container || container.classList.contains('state-legmod')) return;

    const whiteCircle = document.getElementById('circle-white');
    const cyanCircle = document.getElementById('circle-cyan');
    const blueCircle = document.getElementById('circle-blue');
    const purpleCircle = document.getElementById('circle-purple');
    
    const textDeploy = document.getElementById('text-deploy');
    const textRgen = document.getElementById('text-rgen');
    const textCodegen = document.getElementById('text-codegen');
    const textTestai = document.getElementById('text-testai');

    if (container.classList.contains('state-deploy')) {
        if (whiteCircle && !whiteCircle.contains(e.target) && (!textDeploy || !textDeploy.contains(e.target))) {
            resetOrchestratorState();
        }
    } else if (container.classList.contains('state-rgen')) {
        if (cyanCircle && !cyanCircle.contains(e.target) && (!textRgen || !textRgen.contains(e.target))) {
            resetOrchestratorState();
        }
    } else if (container.classList.contains('state-codegen')) {
        if (blueCircle && !blueCircle.contains(e.target) && (!textCodegen || !textCodegen.contains(e.target))) {
            resetOrchestratorState();
        }
    } else if (container.classList.contains('state-testai')) {
        if (purpleCircle && !purpleCircle.contains(e.target) && (!textTestai || !textTestai.contains(e.target))) {
            resetOrchestratorState();
        }
    }
});

// =========================================================================
// Responsive Mobile Header & Menu Interactions (< 768px)
// =========================================================================

function toggleMobileMenu() {
    const toggle = document.getElementById('mobileMenuToggle');
    const drawer = document.getElementById('mobileNavDrawer');
    if (!toggle || !drawer) return;
    
    const isOpen = toggle.classList.toggle('is-open');
    drawer.classList.toggle('is-open', isOpen);
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    document.body.style.overflow = isOpen ? 'hidden' : '';
}

function closeMobileMenu() {
    const toggle = document.getElementById('mobileMenuToggle');
    const drawer = document.getElementById('mobileNavDrawer');
    if (!toggle || !drawer) return;
    
    toggle.classList.remove('is-open');
    drawer.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
}

function mobileAgentClick(i, e) {
    if (e) e.preventDefault();
    closeMobileMenu();
    if (window.goToAgentSlide) {
        window.goToAgentSlide(i);
    }
}

function scrollToAssessment(e) {
    if (e) e.preventDefault();
    closeMobileMenu();
    const isMobile = window.innerWidth <= 768;
    if (isMobile) {
        const playbook = document.getElementById('playbook');
        if (playbook) {
            const topPos = playbook.offsetTop - 70;
            window.scrollTo({ top: topPos, behavior: 'smooth' });
        }
    } else {
        const viewport = Math.max(320, window.innerWidth);
        const scale = Math.min(1, viewport / 1512);
        const topPos = 990 * scale;
        window.scrollTo({ top: topPos, behavior: 'smooth' });
    }
}

// Close mobile menu when clicking outside mobile header
document.addEventListener('click', (e) => {
    const header = document.getElementById('mobileHeader');
    const drawer = document.getElementById('mobileNavDrawer');
    if (header && !header.contains(e.target) && drawer && drawer.classList.contains('is-open')) {
        closeMobileMenu();
    }
});

// Close mobile menu if window is resized above 768px
window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        closeMobileMenu();
    }
});

function scrollToEntCard(index, isMobile) {
    const containerSelector = isMobile ? '.mobile-enterprise-slider-wrapper' : '.cert-scroll';
    const dotsSelector = isMobile ? '#mobile-ent-dots .slider-dot' : '#desktop-ent-dots .slider-dot';
    
    const container = document.querySelector(containerSelector);
    if (!container) return;

    // Card widths plus gaps
    const cardWidth = isMobile ? (195 + 16) : (432 + 25);
    container.scrollTo({
        left: index * cardWidth,
        behavior: 'smooth'
    });

    const dots = document.querySelectorAll(dotsSelector);
    dots.forEach((dot, i) => {
        if (i === index) {
            dot.classList.add('active');
            dot.style.background = '#2ad6df';
        } else {
            dot.classList.remove('active');
            dot.style.background = '#105b7a';
        }
    });
}

function scrollToTeamCard(index) {
    const container = document.querySelector('.mobile-teams-cards');
    if (!container) return;

    const cardWidth = 280 + 16; // width + gap
    container.scrollTo({
        left: index * cardWidth,
        behavior: 'smooth'
    });

    const dots = document.querySelectorAll('#mobile-team-dots .slider-dot');
    dots.forEach((dot, i) => {
        if (i === index) {
            dot.classList.add('active');
            dot.style.background = '#2ad6df';
        } else {
            dot.classList.remove('active');
            dot.style.background = '#105b7a';
        }
    });
}


function scrollToProvenCard(index) {
    const container = document.querySelector('.mobile-proven-slider');
    if (!container) return;

    const cards = container.querySelectorAll('.mobile-proven-card');
    if (cards.length === 0) return;

    // We can use the width of the card + gap
    const cardWidth = cards[0].offsetWidth + 16;
    container.scrollTo({
        left: index * cardWidth,
        behavior: 'smooth'
    });

    const dots = document.querySelectorAll('#mobile-proven-dots .slider-dot');
    dots.forEach((dot, i) => {
        if (i === index) {
            dot.classList.add('active');
            dot.style.background = '#2ad6df';
        } else {
            dot.classList.remove('active');
            dot.style.background = '#105b7a';
        }
    });
}

