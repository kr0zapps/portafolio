with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('text-technical-gray/20">block</span>', 'text-technical-gray/20">shield</span>')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(content)
