import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Navbar Rewrite
old_nav = r'<nav class="fixed top-6 left-1/2 -translate-x-1/2 z-50 px-4 md:px-6 py-3 rounded-full bg-white/70 dark:bg-\[\#0a0a10\]/70 backdrop-blur-xl border border-gray-200/50 dark:border-white/10 shadow-\[0_8px_32px_rgba\(0,0,0,0\.04\)\] flex items-center gap-4 md:gap-8 transition-all duration-500 w-\[90%\] md:w-auto justify-between md:justify-center">.*?</nav>'

new_nav = '''<nav class="fixed top-6 left-1/2 -translate-x-1/2 z-50 p-2 rounded-full bg-white/70 dark:bg-[#0a0a10]/70 backdrop-blur-xl border border-gray-200/50 dark:border-white/10 shadow-lg flex items-center gap-3 transition-all duration-500 w-[90%] md:w-auto justify-between md:justify-center">
        <!-- Logo -->
        <a href="#" class="font-bold tracking-widest uppercase text-xs hover:text-[#0052FF] transition-colors shrink-0 pl-4">KR0ZAPPS</a>
        
        <!-- Divider -->
        <div class="hidden md:block h-4 w-[1px] bg-gray-300 dark:bg-gray-700 mx-2"></div>
        
        <!-- Links (Segmented Control style) -->
        <div class="hidden md:flex items-center gap-1 text-sm font-medium shrink-0">
            <a href="#work" class="px-5 py-2 rounded-full text-gray-600 dark:text-gray-400 hover:text-[#1a1c1c] dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/10 transition-all active:scale-95">Trabajo</a>
            <a href="#stack" class="px-5 py-2 rounded-full text-gray-600 dark:text-gray-400 hover:text-[#1a1c1c] dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/10 transition-all active:scale-95">Ingeniería</a>
            <a href="#about" class="px-5 py-2 rounded-full text-gray-600 dark:text-gray-400 hover:text-[#1a1c1c] dark:hover:text-white hover:bg-black/5 dark:hover:bg-white/10 transition-all active:scale-95">Sobre mí</a>
        </div>
        
        <!-- Divider -->
        <div class="hidden md:block h-4 w-[1px] bg-gray-300 dark:bg-gray-700 mx-2"></div>
        
        <!-- Theme Toggle -->
        <button id="theme-toggle" class="relative w-14 h-8 rounded-full bg-gray-200 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 focus:outline-none overflow-hidden flex items-center transition-colors shrink-0 mr-1 group">
            <div id="theme-slider" class="absolute left-1 w-6 h-6 rounded-full bg-white dark:bg-black shadow-sm flex items-center justify-center transition-transform duration-300 transform dark:translate-x-6 group-hover:scale-95">
                <i data-lucide="sun" class="w-3.5 h-3.5 text-orange-500 dark:opacity-0 transition-opacity absolute"></i>
                <i data-lucide="moon" class="w-3.5 h-3.5 text-blue-400 opacity-0 dark:opacity-100 transition-opacity absolute"></i>
            </div>
        </button>
    </nav>'''

html = re.sub(old_nav, new_nav, html, flags=re.DOTALL)


# 2. Fix Project Card Clickability (Remove pointer-events-none that blocked clicks)
html = html.replace('pointer-events-none">', '">')
html = html.replace('pointer-events-auto ', '')
html = html.replace('pointer-events-none', '')

# Replace magnetic div with a tag
html = html.replace('<div class="magnetic-btn', '<a href="#" class="magnetic-btn')
html = html.replace('</div>\n                    </div>\n                    \n                    <p', '</a>\n                    </div>\n                    \n                    <p')

# Re-fix Fenix URL on magnetic btn since the generic replacement wiped it, or rather it was already an <a> tag!
# Let's clean up double <a> tags if any happened.
html = html.replace('<a href="#" class="magnetic-btn w-12 h-12 rounded-full', '<a href="#" target="_blank" class="magnetic-btn w-12 h-12 rounded-full')
html = html.replace('<a href="https://fenixselect.cl" target="_blank" class="magnetic-btn w-12 h-12 rounded-full', '<a href="https://fenixselect.cl" target="_blank" class="magnetic-btn w-12 h-12 rounded-full')

# Fix "Ver Proyecto" Overlay buttons
html = re.sub(r'<span class="px-6 py-3 bg-white text-black font-bold rounded-full transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 shadow-xl(.*?)">Ver Proyecto</span>', r'<a href="#" target="_blank" class="px-6 py-3 bg-white text-black font-bold rounded-full transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 shadow-xl hover:scale-105 active:scale-95\1">Ver Proyecto</a>', html)

html = re.sub(r'<span class="px-6 py-3 bg-white text-black font-bold rounded-full transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 shadow-xl(.*?)">Visitar Web</span>', r'<a href="https://fenixselect.cl" target="_blank" class="px-6 py-3 bg-white text-black font-bold rounded-full transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 shadow-xl hover:scale-105 active:scale-95\1">Visitar Web</a>', html)


with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
