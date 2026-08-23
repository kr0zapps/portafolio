import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Nav Bar Background & Colors
html = html.replace('bg-[#f9f9f9]/80 dark:bg-[#f9f9f9]/80 backdrop-blur-md border-b border-[#1a1c1c]/10', 'bg-[#051424]/90 backdrop-blur-md border-b border-white/10')
html = html.replace('text-[#1a1c1c] ">', 'text-white ">') # Logo
html = html.replace('text-[#003ec7] dark:text-[#0052FF] border-b-2 border-[#003ec7]', 'text-white border-b-2 border-white') # Active Link
html = html.replace('text-[#434656]  hover:text-[#003ec7]', 'text-gray-400 hover:text-white') # Inactive Links

# 2. Remove "Disponible" from Nav
disponible_nav_pattern = r'<div class="flex items-center gap-2">\s*<div class="w-2 h-2 rounded-full bg-\[#0052FF\] animate-pulse shadow-\[0_0_8px_#0052FF\]"></div>\s*<span class="font-mono text-xs font-bold tracking-\[0\.08em\] text-\[#003ec7\].*?</span>\s*</div>'
html = re.sub(disponible_nav_pattern, '', html, flags=re.DOTALL)

# 3. Update Hero Section Background
html = html.replace('<section class="relative min-h-[90vh] flex flex-col justify-center px-5 md:px-16 py-32 overflow-hidden scroll-reveal">', 
                    '<section class="relative min-h-[95vh] flex flex-col justify-center px-5 md:px-16 py-32 pb-48 overflow-hidden scroll-reveal bg-[#051424]">')

# 4. Inject "Disponible" Pill above H1
pill_html = '''<div class="inline-flex items-center gap-3 px-5 py-2 rounded-full border border-white/10 bg-white/5 backdrop-blur-md w-fit mb-8 shadow-lg">
  <span class="relative flex h-2.5 w-2.5">
    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#00f2fe] opacity-75"></span>
    <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-[#00f2fe]"></span>
  </span>
  <span class="font-mono text-[10px] font-bold tracking-widest text-white uppercase">Disponible para proyectos</span>
</div>\n'''
html = html.replace('<h1 class="text-6xl md:text-[120px] font-extrabold leading-[0.9]', pill_html + '<h1 class="text-6xl md:text-[120px] font-extrabold leading-[0.9]')

# 5. Update Hero Text Colors
html = html.replace('text-[#1a1c1c] tracking-tighter leading-none', 'text-white tracking-tighter leading-none')
html = html.replace('text-[#888888]">Construyo', 'text-gray-400">Construyo')
html = html.replace('text-[#888888]">de alto rendimiento', 'text-gray-400">de alto rendimiento')
html = html.replace('bg-gradient-to-r from-[#0052FF] to-[#001452]', 'bg-gradient-to-r from-[#4facfe] to-[#00f2fe]') # Brighter cyan for dark mode
html = html.replace('text-[#434656] font-normal max-w-lg border-l border-[#1a1c1c]/20', 'text-gray-300 font-normal max-w-lg border-l border-white/20')

# 6. Add Floating Badges to the Phone and make phone border fit dark mode
html = html.replace('border-surface-container-high bg-white', 'border-white/5 bg-[#0a0a0a]')
badge_html = '''
<!-- Floating overlapping badge (Reference style) -->
<div class="absolute -left-8 md:-left-16 bottom-16 bg-[#051424]/80 backdrop-blur-xl border border-white/10 p-4 md:p-5 rounded-2xl shadow-2xl z-20 flex flex-col gap-1 transform -rotate-3 hover:rotate-0 transition-transform duration-300">
  <span class="text-3xl md:text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-[#4facfe] to-[#00f2fe]">+500k</span>
  <span class="font-mono text-[10px] text-gray-300 uppercase tracking-widest font-bold">Descargas Orgánicas</span>
</div>
<div class="absolute -right-6 md:-right-10 top-24 bg-[#051424]/80 backdrop-blur-xl border border-white/10 p-4 rounded-2xl shadow-2xl z-20 flex flex-col gap-1 transform rotate-6 hover:rotate-0 transition-transform duration-300">
  <div class="flex items-center gap-2 mb-1">
    <span class="material-symbols-outlined text-green-400 text-sm">verified</span>
    <span class="text-sm font-bold text-white">Top #10</span>
  </div>
  <span class="font-mono text-[9px] text-gray-400 uppercase tracking-widest font-bold">Health & Fitness</span>
</div>
'''
html = html.replace('<div class="relative w-full aspect-[9/19] rounded-[2rem]', badge_html + '<div class="relative w-full aspect-[9/19] rounded-[2rem]')

# 7. Add Curved Divider at bottom of Hero
divider_html = '''
<div class="absolute bottom-0 left-0 w-full overflow-hidden leading-none z-10" style="transform: translateY(1px);">
    <svg class="relative block w-full h-[60px] md:h-[100px]" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
        <path d="M985.66,92.83C906.67,72,823.78,31,743.84,14.19c-82.26-17.34-168.06-16.33-250.45.39-57.84,11.73-114,31.07-172,41.86A600.21,600.21,0,0,1,0,27.35V120H1200V95.8C1132.19,118.92,1055.71,111.31,985.66,92.83Z" fill="#f9f9f9"></path>
    </svg>
</div>
</section>
'''
html = html.replace('</section>', divider_html)

# 8. Hide the original marquee by removing it (it doesn't fit the dark hero cleanly unless we recolor it, let's just remove it for sobriety)
marquee_pattern = r'<!-- Marquee Ticker -->.*?</div>\s*</div>\s*</div>'
html = re.sub(marquee_pattern, '', html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
