with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the specific lines with escaped braces for Astro
html = html.replace('import</span> { <span', 'import</span> &#123; <span')
html = html.replace('SystemCore</span> } <span', 'SystemCore</span> &#125; <span')
html = html.replace('&gt; {</p>', '&gt; &#123;</p>')
html = html.replace('initialize</span>({</p>', 'initialize</span>(&#123;</p>')
html = html.replace('<p class="pl-8">});</p>', '<p class="pl-8">&#125;);</p>')
html = html.replace('<p class="pl-4">}</p>', '<p class="pl-4">&#125;</p>')
html = html.replace('<p>}</p>', '<p>&#125;</p>')
html = html.replace('PerformanceCore</span> {</p>', 'PerformanceCore</span> &#123;</p>')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
