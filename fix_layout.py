with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Remove the glcanvas from layout
layout = layout.replace('<canvas id="glcanvas" class="fixed inset-0 w-full h-full -z-20 pointer-events-none"></canvas>', '')

with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
