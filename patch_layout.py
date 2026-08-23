import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix ThreeJS - Remove Mouse tracking
old_threejs_anim = '''            document.addEventListener('mousemove', (event) => {
                mouseX = (event.clientX - windowHalfX) * 0.001;
                mouseY = (event.clientY - windowHalfY) * 0.001;
            });'''

new_threejs_anim = '''            // Mouse tracking removed to avoid noise
            /* 
            document.addEventListener('mousemove', (event) => {
                mouseX = (event.clientX - windowHalfX) * 0.001;
                mouseY = (event.clientY - windowHalfY) * 0.001;
            });
            */'''
if old_threejs_anim in html:
    html = html.replace(old_threejs_anim, new_threejs_anim)

old_threejs_loop = '''                // Smooth mouse following
                targetX = mouseX * 1.5;
                targetY = mouseY * 1.5;
                
                particlesMesh.rotation.y += 0.05 * (targetX - particlesMesh.rotation.y);
                particlesMesh.rotation.x += 0.05 * (targetY - particlesMesh.rotation.x);
                
                // Idle gentle rotation
                particlesMesh.rotation.y += 0.001;
                particlesMesh.position.y = Math.sin(elapsedTime * 0.5) * 0.2;'''

new_threejs_loop = '''                // Smooth, gentle ambient rotation (no mouse tracking)
                particlesMesh.rotation.y += 0.0008;
                particlesMesh.rotation.x += 0.0004;
                particlesMesh.position.y = Math.sin(elapsedTime * 0.3) * 0.1;'''

if old_threejs_loop in html:
    html = html.replace(old_threejs_loop, new_threejs_loop)

# 2. Fix Card Images Layout
# FitGamer Card Image logic: Make it look like a nice phone crop
old_fitgamer_img = '''<div class="relative flex-grow flex items-end justify-center z-10 mt-auto">
                        <div class="w-full md:w-5/6 mx-auto rounded-t-2xl overflow-hidden border border-gray-200 dark:border-white/10 border-b-0 shadow-2xl transform translate-y-8 group-hover:translate-y-0 transition-transform duration-700 ease-out">
                            <img src="/portafolio/fitgamer-official.png" alt="FitGamer App" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700" style="object-position: top;"/>
                        </div>
                    </div>'''
new_fitgamer_img = '''<div class="relative flex-grow flex items-end justify-center z-10 mt-6 pt-4 h-[300px] overflow-hidden">
                        <div class="absolute bottom-0 w-full sm:w-[80%] mx-auto rounded-t-[2rem] overflow-hidden border-[6px] border-gray-100 dark:border-[#1a1c1c] shadow-2xl transform translate-y-6 group-hover:translate-y-2 transition-transform duration-700 ease-out" style="height: 110%;">
                            <img src="/portafolio/fitgamer-official.png" alt="FitGamer App" class="w-full h-full object-cover object-top opacity-95 group-hover:opacity-100 transition-opacity duration-700" />
                        </div>
                    </div>'''
html = html.replace(old_fitgamer_img, new_fitgamer_img)

# Callate Spam Card Image logic: Make it contain nicely as a landscape UI element
old_callate_img = '''<div class="relative flex-grow flex items-end justify-center z-10 mt-auto">
                        <div class="w-full rounded-2xl overflow-hidden border border-gray-200 dark:border-white/10 shadow-2xl transform scale-95 translate-y-4 group-hover:scale-100 group-hover:translate-y-0 transition-transform duration-700 ease-out">
                            <img src="/portafolio/callate-official.png" alt="Cállate Play Store" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700" style="object-position: top;"/>
                        </div>
                    </div>'''
new_callate_img = '''<div class="relative flex-grow flex items-center justify-center z-10 mt-6">
                        <div class="w-full rounded-2xl overflow-hidden border border-gray-200 dark:border-white/10 shadow-xl transform scale-[0.98] group-hover:scale-100 group-hover:-translate-y-2 transition-all duration-700 ease-out bg-gray-50 dark:bg-[#111116] p-2">
                            <img src="/portafolio/callate-official.png" alt="Cállate Play Store" class="w-full h-auto rounded-xl object-contain opacity-95 group-hover:opacity-100 transition-opacity duration-700" />
                        </div>
                    </div>'''
html = html.replace(old_callate_img, new_callate_img)

# 3. Insert RSVP Image into the Archive List
old_rsvp_row = '''<div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-default">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2026</span>
                        <div class="hidden md:block w-32 h-20 bg-gray-100 dark:bg-white/5 rounded-lg border border-gray-200 dark:border-white/10 flex items-center justify-center text-gray-300 dark:text-gray-700"><i data-lucide="users" class="w-6 h-6"></i></div>
                        <div>'''
new_rsvp_row = '''<div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-default">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2026</span>
                        <img src="/portafolio/rsvp-official.png" alt="Sistema RSVP" class="hidden md:block w-32 h-20 object-cover object-center rounded-lg border border-gray-200 dark:border-white/10 opacity-80 group-hover:opacity-100 transition-opacity">
                        <div>'''
html = html.replace(old_rsvp_row, new_rsvp_row)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
