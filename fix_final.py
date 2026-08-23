import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the white bar issue: remove pt-[104px] from <main>
html = html.replace('<main class="pt-[104px]">', '<main>')

# 2. Fix the gradient text
html = html.replace('<span class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-[#4facfe] to-[#00f2fe]">nativos y web</span>', '<span class="font-extrabold text-white">nativos y web</span>')

# 3. Completely remove the SVG waves
svg_wave_pattern = r'<div class="absolute bottom-0 left-0 w-full overflow-hidden leading-none z-10" style="transform: translateY\(1px\);">\s*<svg.*?</svg>\s*</div>'
html = re.sub(svg_wave_pattern, '', html, flags=re.DOTALL)

# 4. Replace the Visual Column with a Person Placeholder
visual_col_pattern = r'<!-- Visual Column.*?<!-- Marquee Ticker -->'
new_visual_col = '''<!-- Visual Column (User Portrait Placeholder) -->
<div class="col-span-1 lg:col-span-5 relative flex justify-center lg:justify-end perspective-1000 w-full max-w-lg mx-auto lg:max-w-none">
    <div class="relative w-[320px] h-[320px] md:w-[400px] md:h-[400px] rounded-full border border-white/10 bg-white/5 overflow-hidden shadow-2xl flex items-center justify-center backdrop-blur-sm">
        <span class="material-symbols-outlined text-[150px] md:text-[200px] text-gray-500/50">person</span>
    </div>
</div>
<!-- Marquee Ticker -->'''
html = re.sub(visual_col_pattern, new_visual_col, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
