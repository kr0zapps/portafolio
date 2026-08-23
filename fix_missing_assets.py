import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

github_svg_nav = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.2c3-.3 6-1.5 6-6.5a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 5 3 6.2 6 6.5a4.8 4.8 0 0 0-1 3.2v4"></path></svg>'''

github_svg_btn = '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-4 h-4 inline-block mr-2 -mt-0.5"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.2c3-.3 6-1.5 6-6.5a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 5 3 6.2 6 6.5a4.8 4.8 0 0 0-1 3.2v4"></path></svg>'''

html = html.replace('<i data-lucide="github" class="w-4 h-4"></i>', github_svg_nav)
html = html.replace('<i data-lucide="github" class="w-4 h-4 inline-block mr-2 -mt-0.5"></i>', github_svg_btn)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)

with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

layout = layout.replace('href="/favicon.svg"', 'href="/portafolio/favicon.svg"')

with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
