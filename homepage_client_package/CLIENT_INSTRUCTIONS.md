# Sanciti AI - Home Page Update Package

This package contains the updated Home Page files matching the new Figma design (for both Desktop and Mobile versions).

## Files Included:
1. index.html - Complete updated home page (Desktop Section 1 Playbook, Hero rings with chroma-key canvas, Section 2 One Platform, and Mobile Playbook section).
2. submit_form.php - Form processing script for the Playbook download form.
3. ssets/css/style.css - Stylesheet containing the new playbook layouts, form styling, button styling, badge styling, and responsive breakpoints.
4. ssets/js/script.js - Client-side scripts and handlers.
5. ssets/img/Home page new/ - All newly added assets:
   - Cover mockup_Desktop 1.png (3D Book mockup)
   - Final Video 2.mp4 (5 glowing rings animation)
   - 
ings_transparent.png (Instant transparent ring placeholder)
   - Main Video 1.png
   - Frame 75.png
   - Ellipse 2.png
   - claude_certified_badge.png

## How to Apply:
### Option A: Direct Replacement (Recommended if matching the same project structure)
Simply copy the files into your project root:
- Replace index.html
- Replace ssets/css/style.css
- Replace ssets/js/script.js
- Copy ssets/img/Home page new/ into your ssets/img/ directory.

### Option B: Merging Changes
If you have custom modifications in index.html or style.css:
- **HTML (Desktop)**: Section 1 (#playbook-desktop) and Section 2 (.desktop-hero) at lines 636–758 of index.html.
- **HTML (Mobile)**: Mobile Playbook section at lines 63–130 of index.html.
- **CSS**: The .claude-partner-badge, .mobile-playbook-*, .desktop-playbook-*, .desktop-form-*, and #heroRingsCanvas classes at the bottom of ssets/css/style.css (lines 4740–4901).
