import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the 3D column responsive: absolute and behind text on mobile, normal grid column on lg
visual_col_pattern = r'<!-- Visual Column \(3D Animation\).*?</div>\s*</div>'
new_visual_col = '''<!-- Visual Column (3D Animation) -->
<div class="absolute inset-0 z-0 opacity-40 lg:opacity-100 lg:relative lg:col-span-1 lg:col-span-5 flex justify-center lg:justify-end items-center w-full h-full lg:h-[600px] pointer-events-none lg:pointer-events-auto">
    <div id="threejs-container" class="w-full h-[500px] lg:h-full cursor-grab active:cursor-grabbing"></div>
</div>'''
html = re.sub(visual_col_pattern, new_visual_col, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
