import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any sequence of </section> tags with just one </section> before the next section
html = re.sub(r'(</section>\s*)+<!-- Tech Stack \(Bento Grid\) -->', r'</section>\n\n    <!-- Tech Stack (Bento Grid) -->', html)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
