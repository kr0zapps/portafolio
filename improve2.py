with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the button premium
old_btn = 'class="bg-[#0052FF] text-[#ffffff] font-mono text-sm font-medium px-6 py-3 rounded-none uppercase hover:bg-[#003ec7] transition-colors duration-150 flex items-center gap-2"'
new_btn = 'class="group bg-[#0052FF] text-[#ffffff] font-mono text-xs font-bold tracking-widest px-8 py-4 rounded-full uppercase hover:bg-[#003ec7] transition-all duration-300 flex items-center gap-3 shadow-[0_4px_14px_0_rgba(0,82,255,0.39)] hover:shadow-[0_6px_20px_rgba(0,82,255,0.23)] hover:-translate-y-0.5"'

old_span = 'Ver proyectos <span class="material-symbols-outlined text-sm">arrow_downward</span>'
new_span = 'Ver proyectos <span class="material-symbols-outlined text-base group-hover:translate-y-1 transition-transform duration-300">arrow_downward</span>'

html = html.replace(old_btn, new_btn)
html = html.replace(old_span, new_span)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
