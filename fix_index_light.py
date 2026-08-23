import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the Badge! We'll give it a "bkn" (cool) glowing animated gradient border
old_badge = '''<span class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-gray-200 dark:border-white/10 bg-white/50 dark:bg-white/5 backdrop-blur-md mb-8">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                    </span>
                    <span class="font-mono text-xs font-bold tracking-widest text-gray-600 dark:text-gray-300 uppercase">Disponible para proyectos</span>
                </span>'''

new_badge = '''<div class="relative inline-flex mb-8 group cursor-default">
                    <!-- Animated Gradient Glow Behind -->
                    <div class="absolute -inset-0.5 bg-gradient-to-r from-[#0052FF] via-purple-500 to-[#0052FF] rounded-full blur opacity-40 group-hover:opacity-75 animate-gradient-xy transition duration-500"></div>
                    
                    <!-- Inner Pill -->
                    <div class="relative inline-flex items-center gap-3 px-6 py-2.5 rounded-full bg-white dark:bg-[#030712] border border-gray-200/50 dark:border-white/10">
                        <div class="flex items-center justify-center w-2 h-2 relative">
                            <span class="absolute w-2 h-2 bg-green-500 rounded-full animate-ping"></span>
                            <span class="relative w-1.5 h-1.5 bg-green-500 rounded-full"></span>
                        </div>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white uppercase">Status: <span class="text-[#0052FF] dark:text-[#4facfe]">Disponible</span></span>
                    </div>
                </div>'''

if old_badge in html:
    html = html.replace(old_badge, new_badge)
else:
    print("Warning: Old badge not found. Check exact formatting.")

# 2. Fix ThreeJS particles in light mode. Currently set to 0x000000 with 0.1 opacity.
# Make it a cool blue with higher opacity so it's super visible and animated in light mode.
old_three_theme = '''const updateParticleColor = () => {
                const isDark = document.documentElement.classList.contains('dark');
                material.color.setHex(isDark ? 0xffffff : 0x000000);
                material.opacity = isDark ? 0.3 : 0.1;
            };'''

new_three_theme = '''const updateParticleColor = () => {
                const isDark = document.documentElement.classList.contains('dark');
                // In dark mode: white particles, 0.3 opacity.
                // In light mode: electric blue particles, 0.5 opacity for a highly visible cool animation.
                material.color.setHex(isDark ? 0xffffff : 0x0052FF);
                material.opacity = isDark ? 0.3 : 0.5;
            };'''

if old_three_theme in html:
    html = html.replace(old_three_theme, new_three_theme)
else:
    print("Warning: ThreeJS theme logic not found.")

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
