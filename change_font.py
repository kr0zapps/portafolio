with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

layout = layout.replace('family=Inter:wght@400;600&', 'family=Plus+Jakarta+Sans:wght@400;500;600;700;800&')

with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)

with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('"Inter", "system-ui", "sans-serif"', '"Plus Jakarta Sans", "system-ui", "sans-serif"')
css = css.replace('"Inter", sans-serif', '"Plus Jakarta Sans", sans-serif')

with open('src/styles/global.css', 'w', encoding='utf-8') as f:
    f.write(css)
