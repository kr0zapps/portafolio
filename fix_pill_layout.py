import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

old_toggle = r'<button id="theme-toggle" class="relative flex items-center justify-between w-16 h-8 p-1.*?</button>'

new_toggle = '''<button id="theme-toggle" class="relative w-16 h-8 rounded-full bg-gray-300 dark:bg-gray-700 transition-colors duration-300 focus:outline-none border border-gray-400 dark:border-gray-600 flex items-center" aria-label="Toggle Dark Mode">
        <span class="material-symbols-outlined absolute left-1.5 text-[14px] text-gray-500 dark:text-gray-400 z-10 pointer-events-none">dark_mode</span>
        <span class="material-symbols-outlined absolute right-1.5 text-[14px] text-yellow-500 z-10 pointer-events-none">light_mode</span>
        <div class="absolute left-1 w-6 h-6 bg-white dark:bg-[#1a1c1c] rounded-full shadow-md transform transition-transform duration-300 dark:translate-x-8 z-20"></div>
    </button>'''

html = re.sub(old_toggle, new_toggle, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
