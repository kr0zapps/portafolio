import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the specific react mock code block safely
html = html.replace('Component = () => {', 'Component = () =&gt; &#123;')
html = html.replace('<div>}</div>', '<div>&#125;</div>')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
