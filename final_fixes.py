import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Neon Glow
html = html.replace('<div class="absolute inset-0 bg-gradient-to-br from-red-500/0 to-orange-500/0 dark:group-hover:from-red-500/10 dark:group-hover:to-orange-500/10 transition-colors duration-700 pointer-events-none"></div>', '')
html = html.replace('<div class="absolute inset-0 bg-gradient-to-br from-[#0052FF]/0 to-purple-500/0 dark:group-hover:from-[#0052FF]/10 dark:group-hover:to-purple-500/10 transition-colors duration-700 pointer-events-none"></div>', '')
html = html.replace('<div class="absolute inset-0 bg-gradient-to-br from-[#003ec7]/0 via-transparent to-[#4facfe]/0 dark:group-hover:from-[#003ec7]/10 dark:group-hover:to-[#4facfe]/10 transition-colors duration-700 pointer-events-none"></div>', '')

# 2. Fix the switch toggle
old_toggle_start = '<button id="theme-toggle"'
old_toggle_end = '</button>'
if old_toggle_start in html:
    start_idx = html.find(old_toggle_start)
    end_idx = html.find(old_toggle_end, start_idx) + len(old_toggle_end)
    before = html[:start_idx]
    after = html[end_idx:]
    new_toggle = '''<button id="theme-toggle" class="relative flex items-center w-14 h-7 bg-[#e5e5e5] dark:bg-[#1a1c1c] rounded-full p-1 transition-colors duration-300 border border-[#1a1c1c]/10 dark:border-white/10 shrink-0">
    <i data-lucide="moon" class="absolute left-1.5 w-3.5 h-3.5 text-white opacity-0 dark:opacity-100 transition-opacity duration-300 pointer-events-none"></i>
    <i data-lucide="sun" class="absolute right-1.5 w-3.5 h-3.5 text-[#1a1c1c] opacity-100 dark:opacity-0 transition-opacity duration-300 pointer-events-none"></i>
    <div class="theme-toggle-thumb absolute w-5 h-5 bg-white dark:bg-[#2a2d2d] rounded-full shadow-sm transform transition-transform duration-300 top-1/2 -translate-y-1/2 left-1 dark:translate-x-7 z-20"></div>
</button>'''
    html = before + new_toggle + after

# 3. Add Landing Page CTA
old_tier2 = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
new_card = '''
        <!-- Landing Page CTA Card -->
        <div class="group bg-white dark:bg-[#060b13] p-8 rounded-[1rem] border border-[#1a1c1c]/10 dark:border-white/10 hover:border-[#1a1c1c]/30 dark:hover:border-white/30 transition-all duration-300 flex flex-col justify-between shadow-sm hover:shadow-md cursor-pointer">
            <div>
                <div class="w-10 h-10 rounded-full bg-[#1a1c1c] dark:bg-white flex items-center justify-center mb-6">
                    <i data-lucide="layout-template" class="text-white dark:text-[#1a1c1c] w-5 h-5"></i>
                </div>
                <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white mb-2">Desarrollo a Medida</h4>
                <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed mb-6">¿Necesitas una Landing Page, un Dashboard o un sitio corporativo? Construyo web de alta conversión.</p>
            </div>
            <a href="mailto:contacto@kr0zapps.com" class="inline-flex items-center text-sm font-bold text-[#1a1c1c] dark:text-white hover:opacity-70 transition-opacity uppercase tracking-wider font-mono">
                Cotizar Proyecto <i data-lucide="arrow-up-right" class="w-4 h-4 ml-1"></i>
            </a>
        </div>
'''
if old_tier2 in html:
    html = html.replace(old_tier2, old_tier2 + "\n" + new_card)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
