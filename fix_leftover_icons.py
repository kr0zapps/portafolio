import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Leftover 1: arrow_downward
html = html.replace('<span class="material-symbols-outlined text-base group-hover:translate-y-1 transition-transform duration-300">arrow_downward</span>', '<i data-lucide="arrow-down" class="w-4 h-4 group-hover:translate-y-1 transition-transform duration-300"></i>')

# Leftover 2: arrow_outward in freelancer section
html = html.replace('<span class="material-symbols-outlined text-gray-500 group-hover:text-[#003ec7] dark:group-hover:text-white transition-colors text-sm">arrow_outward</span>', '<i data-lucide="arrow-up-right" class="w-4 h-4 text-gray-500 group-hover:text-[#003ec7] dark:group-hover:text-white transition-colors"></i>')

# Leftover 3: emoji_events (trophy)
html = html.replace('<span class="material-symbols-outlined text-[#0052FF] text-2xl" style="font-variation-settings: \'FILL\' 1;">emoji_events</span>', '<i data-lucide="trophy" class="w-6 h-6 text-[#0052FF] fill-[#0052FF]/20"></i>')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
