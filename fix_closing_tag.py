import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the missing </section> that was accidentally removed
html = html.replace('<!-- Tech Stack (Bento Grid) -->', '</section>\n\n    <!-- Tech Stack (Bento Grid) -->')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
