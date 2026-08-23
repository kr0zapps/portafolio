import re

with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove Material Symbols link
html = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?family=Material\+Symbols\+Outlined.*?" rel="stylesheet"/>', '', html)

with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(html)
