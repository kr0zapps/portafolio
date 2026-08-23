with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken bg classes
html = html.replace('bg-[#f9f9f9]-container-highest/50', 'bg-[#e2e2e2]/50')
html = html.replace('bg-[#f9f9f9]-container-low', 'bg-[#f3f3f3]')
html = html.replace('text-[128px]', 'text-9xl style="font-size: 128px; line-height: 1;"') # Force the size just in case

# Make 'nativos y web' gradient text
html = html.replace('<span class="font-extrabold text-[#1a1c1c]">nativos y web</span>', '<span class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-[#0052FF] to-[#001452]">nativos y web</span>')

# Add a subtle glow behind the IDE
html = html.replace('<div class="relative z-10 w-full max-w-4xl mx-auto rounded-xl overflow-hidden shadow-2xl border border-white/10 bg-[#1e1e1e]">', '<div class="absolute inset-0 bg-[#0052FF]/5 blur-[100px] rounded-full pointer-events-none"></div><div class="relative z-10 w-full max-w-4xl mx-auto rounded-xl overflow-hidden shadow-2xl border border-white/10 bg-[#1e1e1e] group">')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
