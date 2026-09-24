// Scale the fixed stage (1512px default or data-width such as 1440px / 393px) to fit any viewport, preserving 1:1 fidelity of the Figma design.
function fitStage() {
    const isMobile = window.innerWidth <= 768;
    const mobileContainer = document.getElementById('mobile-container');
    const stage = document.getElementById('stage');
    const scaler = document.getElementById('scaler');

    if (isMobile && mobileContainer) {
        if (scaler) scaler.style.display = 'none';
        return;
    }

    if (scaler) scaler.style.display = 'block';
    if (!stage || !scaler) return;
    const viewport = Math.max(320, document.documentElement.clientWidth || window.innerWidth);
    const designWidth = stage.dataset.width ? parseFloat(stage.dataset.width) : 1512;
    const scale = viewport / designWidth;
    const mobileOffset = stage.dataset.mobileOffset !== undefined ? parseFloat(stage.dataset.mobileOffset) : (stage.dataset.width ? 0 : 1790);

    if (isMobile && mobileOffset > 0) {
        stage.style.transform = 'scale(' + scale + ') translateY(-' + mobileOffset + 'px)';
        stage.style.transformOrigin = 'top left';
        scaler.style.height = (Math.max(0, stage.getBoundingClientRect().height - (mobileOffset * scale))) + 'px';
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

function toggleMobileDrawer() {
    const drawer = document.getElementById('mobileDrawer');
    if (drawer) {
        drawer.classList.toggle('active');
    }
}

function toggleLmDrawer() {
    const drawer = document.getElementById('lmDrawer');
    if (drawer) {
        drawer.classList.toggle('active');
    }
}





// RGen Mobile Cert Scroll Handler
function handleMobileCertScroll(container) {
    const dots = document.querySelectorAll('#mobile-cert-dots .slider-dot');
    if (!dots.length) return;
    
    // Calculate which card is most visible
    const scrollLeft = container.scrollLeft;
    const cardWidth = 280 + 16; // width + gap
    const index = Math.round(scrollLeft / cardWidth);
    
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

// =========================================================================
// Corporate / Business Email Validation System
// Blocks personal/consumer email providers (Gmail, Yahoo, Hotmail, Outlook, etc.)
// =========================================================================

const PERSONAL_EMAIL_DOMAINS = [
    'gmail.com', 'googlemail.com',
    'yahoo.com', 'yahoo.co.in', 'yahoo.co.uk', 'yahoo.ca', 'yahoo.fr', 'yahoo.de', 'yahoo.it', 'yahoo.es', 'yahoo.com.br', 'yahoo.co.jp', 'ymail.com', 'rocketmail.com',
    'hotmail.com', 'outlook.com', 'live.com', 'msn.com', 'passport.com', 'hotmail.co.uk', 'hotmail.fr', 'hotmail.de', 'hotmail.it', 'hotmail.es',
    'outlook.co.uk', 'outlook.fr', 'outlook.de', 'outlook.in', 'live.co.uk',
    'icloud.com', 'me.com', 'mac.com',
    'aol.com', 'aim.com',
    'protonmail.com', 'proton.me', 'pm.me',
    'zoho.com', 'zohomail.com',
    'mail.com', 'email.com', 'usa.com', 'post.com',
    'gmx.com', 'gmx.net', 'gmx.de', 'gmx.at', 'gmx.ch',
    'yandex.com', 'yandex.ru', 'ya.ru',
    'tutanota.com', 'tuta.io', 'tuta.com',
    'fastmail.com', 'fastmail.fm',
    'rediffmail.com',
    'inbox.com', 'qq.com', '163.com', '126.com', 'sina.com',
    'sbcglobal.net', 'att.net', 'verizon.net', 'comcast.net', 'cox.net', 'charter.net', 'bellsouth.net', 'earthlink.net', 'juno.com',
    'tempmail.com', 'guerrillamail.com', '10minutemail.com', 'mailinator.com', 'throwawaymail.com', 'trashmail.com', 'yopmail.com'
];

window.isCorporateEmail = function (email) {
    if (!email || typeof email !== 'string') return false;
    email = email.trim().toLowerCase();
    const parts = email.split('@');
    if (parts.length !== 2) return false;
    const domain = parts[1].trim();
    if (!domain || domain.indexOf('.') === -1) return false;
    for (let i = 0; i < PERSONAL_EMAIL_DOMAINS.length; i++) {
        const p = PERSONAL_EMAIL_DOMAINS[i];
        if (domain === p || domain.endsWith('.' + p)) {
            return false;
        }
    }
    return true;
};

window.validateEmailField = function (input, isBlur) {
    if (!input) return true;
    const val = input.value.trim();
    if (!val) {
        if (isBlur && input.hasAttribute('required')) {
            window.showEmailError(input, 'Work email address is required.');
            return false;
        }
        window.clearEmailError(input);
        return true;
    }

    const basicEmailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!basicEmailRegex.test(val)) {
        if (isBlur) {
            window.showEmailError(input, 'Please enter a valid email address.');
        }
        return false;
    }

    if (!window.isCorporateEmail(val)) {
        window.showEmailError(input, '✕ Must be Business email.');
        return false;
    }

    window.clearEmailError(input);
    return true;
};

window.showEmailError = function (input, msg) {
    input.classList.add('corp-email-invalid');
    input.style.setProperty('border', '1.5px solid #ff5252', 'important');
    input.style.setProperty('box-shadow', '0 0 10px rgba(255, 82, 82, 0.45)', 'important');

    let errorEl = input.parentNode.querySelector('.corp-email-error-msg');
    if (!errorEl) {
        errorEl = document.createElement('div');
        errorEl.className = 'corp-email-error-msg';
        errorEl.style.color = '#ff6b6b';
        errorEl.style.fontSize = '13px';
        errorEl.style.marginTop = '6px';
        errorEl.style.fontFamily = "'Inter', sans-serif";
        errorEl.style.lineHeight = '1.35';
        errorEl.style.textAlign = 'left';
        errorEl.style.fontWeight = '400';
        input.parentNode.appendChild(errorEl);
    }
    errorEl.textContent = msg;
    errorEl.style.display = 'block';
};

window.clearEmailError = function (input) {
    input.classList.remove('corp-email-invalid');
    input.style.removeProperty('border');
    input.style.removeProperty('box-shadow');
    const errorEl = input.parentNode.querySelector('.corp-email-error-msg');
    if (errorEl) {
        errorEl.style.display = 'none';
    }
};

window.showFormSubmitError = function (form, msg) {
    if (!form) return;
    const message = msg || '✕ Your submission failed because of an error.';
    let errBox = form.querySelector('.form-submit-error-msg');
    if (!errBox) {
        errBox = document.createElement('div');
        errBox.className = 'form-submit-error-msg';
        errBox.style.color = '#ff6b6b';
        errBox.style.fontSize = '13.5px';
        errBox.style.marginTop = '10px';
        errBox.style.fontFamily = "'Inter', sans-serif";
        errBox.style.fontWeight = '400';
        errBox.style.lineHeight = '1.4';
        errBox.style.textAlign = 'left';
        errBox.style.width = '100%';

        const submitBtn = form.querySelector('button[type="submit"]') || form.querySelector('button');
        if (submitBtn) {
            if (submitBtn.parentElement && submitBtn.parentElement !== form) {
                submitBtn.parentElement.style.flexDirection = 'column';
                submitBtn.parentElement.style.alignItems = 'flex-start';
                submitBtn.parentElement.appendChild(errBox);
            } else {
                submitBtn.insertAdjacentElement('afterend', errBox);
            }
        } else {
            form.appendChild(errBox);
        }
    }
    errBox.textContent = message;
    errBox.style.display = 'block';
};

window.clearFormSubmitError = function (form) {
    if (!form) return;
    const errBox = form.querySelector('.form-submit-error-msg');
    if (errBox) {
        errBox.style.display = 'none';
    }
};

window.validateCorporateEmailForm = function (form) {
    if (!form) return true;
    const emailInput = form.querySelector('input[type="email"], input[name="Email"], input[name="email"]');
    if (emailInput) {
        if (!window.validateEmailField(emailInput, true)) {
            window.showFormSubmitError(form, '✕ Your submission failed because of an error.');
            emailInput.focus();
            return false;
        }
    }
    window.clearFormSubmitError(form);
    return true;
};

// Auto-initialize corporate email listeners on ALL pages and forms
function initCorporateEmailValidation() {
    const emailInputs = document.querySelectorAll('input[type="email"], input[name="Email"], input[name="email"]');
    emailInputs.forEach(input => {
        input.addEventListener('input', () => {
            const form = input.closest('form');
            if (input.value.trim() !== '') {
                const isValid = window.validateEmailField(input, false);
                if (isValid && form) {
                    window.clearFormSubmitError(form);
                }
            } else {
                window.clearEmailError(input);
                if (form) {
                    window.clearFormSubmitError(form);
                }
            }
        });

        input.addEventListener('blur', () => {
            if (input.value.trim() !== '') {
                const isValid = window.validateEmailField(input, true);
                const form = input.closest('form');
                if (!isValid && form) {
                    window.showFormSubmitError(form, '✕ Your submission failed because of an error.');
                }
            }
        });
    });

    // Also attach a global capture submit listener for forms
    document.addEventListener('submit', (e) => {
        const form = e.target;
        if (form && form.tagName === 'FORM') {
            const emailInput = form.querySelector('input[type="email"], input[name="Email"], input[name="email"]');
            if (emailInput && !window.validateEmailField(emailInput, true)) {
                e.preventDefault();
                e.stopImmediatePropagation();
                window.showFormSubmitError(form, '✕ Your submission failed because of an error.');
                emailInput.focus();
                return false;
            }
        }
    }, true);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCorporateEmailValidation);
} else {
    initCorporateEmailValidation();
}




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
        nav.style.setProperty('transform', 'translateY(' + translateY + 'px)', 'important');
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

