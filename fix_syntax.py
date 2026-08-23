with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the malformed class string
html = html.replace('text-9xl style="font-size: 128px; line-height: 1;" text-[#888888]/20">shield</span>^', 'text-9xl text-[#888888]/20" style="font-size: 128px; line-height: 1;">shield</span>')
html = html.replace('text-9xl style="font-size: 128px; line-height: 1;" text-[#888888]/20">shield</span>', 'text-9xl text-[#888888]/20" style="font-size: 128px; line-height: 1;">shield</span>')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
