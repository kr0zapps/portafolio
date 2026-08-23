import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Marquee White Bar using a more flexible regex
marquee_pattern = r'<div class="absolute bottom-0 left-0 w-full border-t border-b border-\[#1a1c1c\]/10 dark:border-white/10 bg-white dark:bg-\[#030b14\] py-6 marquee-container z-40 shadow-xl transition-colors duration-500">'
# Actually, let's just do a string replace on a substring to be safe
html = html.replace('bg-white dark:bg-[#030b14] py-6 marquee-container z-40 shadow-xl', 'bg-[#1a1c1c]/5 dark:bg-white/5 backdrop-blur-lg py-6 marquee-container z-40 shadow-none')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
