with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '@custom-variant dark' not in css:
    css = css.replace('@import "tailwindcss";', '@import "tailwindcss";\n@custom-variant dark (&:where(.dark, .dark *));\n')
    with open('src/styles/global.css', 'w', encoding='utf-8') as f:
        f.write(css)
