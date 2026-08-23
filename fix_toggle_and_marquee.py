import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Theme Toggle
old_toggle = r'<button id="theme-toggle".*?</button>'
new_toggle = '''<button id="theme-toggle" class="relative flex items-center justify-between w-16 h-8 p-1 rounded-full bg-gray-200 dark:bg-gray-800 transition-colors duration-300 focus:outline-none border border-gray-300 dark:border-gray-600" aria-label="Toggle Dark Mode">
        <span class="material-symbols-outlined text-[16px] text-gray-500 dark:text-gray-400 z-10 ml-1">dark_mode</span>
        <span class="material-symbols-outlined text-[16px] text-yellow-500 z-10 mr-1">light_mode</span>
        <div class="absolute left-1 top-1 w-6 h-6 bg-white dark:bg-gray-200 rounded-full shadow-md transform transition-transform duration-300 dark:translate-x-8"></div>
    </button>'''
html = re.sub(old_toggle, new_toggle, html, flags=re.DOTALL)

# 2. Fix Marquee White Bar (Make it frosted glass instead of solid colors)
marquee_pattern = r'<div class="absolute bottom-0 left-0 w-full border-t border-b border-\[#1a1c1c\]/10 dark:border-white/10 bg-white dark:bg-\[#030b14\] py-6 marquee-container z-40 shadow-xl transition-colors duration-500">'
new_marquee = '<div class="absolute bottom-0 left-0 w-full border-t border-b border-[#1a1c1c]/10 dark:border-white/10 bg-[#1a1c1c]/5 dark:bg-white/5 backdrop-blur-lg py-6 marquee-container z-40 shadow-sm transition-colors duration-500">'
html = html.replace(marquee_pattern, new_marquee)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
