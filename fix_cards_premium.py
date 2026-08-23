import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the Bento Grid cards incredibly premium
# 1. FitGamer Card
fitgamer_old = r'<!-- FitGamer \(Tier 1\) -->.*?<!-- Cǭllate Spam \(Tier 1\) -->'
# Let's use a simpler replace strategy for the card container classes
html = html.replace(
    '<div class="scroll-reveal bg-[#f3f3f3] dark:bg-[#0a192f] transition-colors duration-300 border border-[#1a1c1c]/10 \ndark:border-white/10 hover:border-[#1a1c1c]/30 dark:hover:border-white/30 cursor-pointer overflow-hidden \nrounded-[2rem] flex flex-col transition-colors duration-300"',
    '<div class="scroll-reveal relative group bg-white dark:bg-[#061020] transition-colors duration-500 border border-[#1a1c1c]/5 dark:border-white/5 hover:border-[#1a1c1c]/20 dark:hover:border-white/20 cursor-pointer overflow-hidden rounded-[2rem] flex flex-col shadow-xl hover:shadow-2xl dark:shadow-none"'
)

# And similarly for Cállate Spam
html = html.replace(
    '<div class="scroll-reveal bg-[#f3f3f3] dark:bg-[#0a192f] transition-colors duration-300 border border-[#1a1c1c]/10 \ndark:border-white/10 hover:border-[#1a1c1c]/30 dark:hover:border-white/30 cursor-pointer overflow-hidden \nrounded-[2rem] flex flex-col transition-colors duration-300"',
    '<div class="scroll-reveal relative group bg-white dark:bg-[#061020] transition-colors duration-500 border border-[#1a1c1c]/5 dark:border-white/5 hover:border-[#1a1c1c]/20 dark:hover:border-white/20 cursor-pointer overflow-hidden rounded-[2rem] flex flex-col shadow-xl hover:shadow-2xl dark:shadow-none"'
)

# Inject the border gradient glow element at the top of the card's inner div
html = html.replace('<div class="p-8 pb-0">', '<div class="absolute inset-0 bg-gradient-to-br from-blue-500/0 via-transparent to-purple-500/0 dark:group-hover:from-blue-500/10 dark:group-hover:to-purple-500/10 transition-colors duration-500 pointer-events-none"></div>\n  <div class="p-8 pb-0 relative z-10">')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
