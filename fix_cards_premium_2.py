import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the Bento Grid cards incredibly premium
card_pattern = r'<div class="scroll-reveal bg-\[#f3f3f3\] dark:bg-\[#0a192f\] transition-colors duration-300 border border-\[#1a1c1c\]/10\s*dark:border-white/10 hover:border-\[#1a1c1c\]/30 dark:hover:border-white/30 cursor-pointer overflow-hidden\s*rounded-\[2rem\] flex flex-col transition-colors duration-300"'

new_card = '<div class="scroll-reveal relative group bg-white dark:bg-[#081225] transition-colors duration-500 border border-[#1a1c1c]/5 dark:border-white/5 hover:border-[#1a1c1c]/20 dark:hover:border-white/20 cursor-pointer overflow-hidden rounded-[2rem] flex flex-col shadow-[0_8px_30px_rgb(0,0,0,0.04)] dark:shadow-[0_8px_30px_rgb(0,0,0,0.2)]"'

html = re.sub(card_pattern, new_card, html)

# Inject the border gradient glow element at the top of the card's inner div
html = html.replace('<div class="p-8 pb-0">', '<div class="absolute inset-0 bg-gradient-to-br from-[#003ec7]/0 via-transparent to-[#4facfe]/0 dark:group-hover:from-[#003ec7]/10 dark:group-hover:to-[#4facfe]/10 transition-colors duration-700 pointer-events-none"></div>\n  <div class="p-8 pb-0 relative z-10">')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
