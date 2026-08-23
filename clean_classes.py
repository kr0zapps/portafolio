with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'bg-surface': 'bg-[#f9f9f9]',
    'text-on-surface-variant': 'text-[#434656]',
    'text-on-surface': 'text-[#1a1c1c]',
    'border-on-surface': 'border-[#1a1c1c]',
    'bg-surface-container-low': 'bg-[#f3f3f3]',
    'bg-surface-container-highest': 'bg-[#e2e2e2]',
    'bg-surface-container': 'bg-[#eeeeee]',
    'bg-electric-blue': 'bg-[#0052FF]',
    'text-electric-blue': 'text-[#0052FF]',
    'text-primary': 'text-[#003ec7]',
    'border-primary': 'border-[#003ec7]',
    'bg-primary': 'bg-[#003ec7]',
    'text-technical-gray': 'text-[#888888]',
    'bg-canvas-white': 'bg-white',
    
    'px-margin-desktop': 'px-16',
    'px-margin-mobile': 'px-5',
    'py-margin-desktop': 'py-16',
    'py-section-gap': 'py-32',
    'gap-gutter': 'gap-6',
    
    # Header translations
    'font-headline-md text-headline-md': 'text-3xl font-semibold',
    'dark:bg-surface/80': '',
    'dark:border-on-primary-fixed/10': '',
    'dark:text-on-primary-fixed-variant': '',
    'dark:text-electric-blue': '',
    'dark:text-on-secondary-container': '',
    'dark:hover:text-electric-blue': '',
    'dark:text-primary-fixed': '',
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Fix the specific "Cállate Spam" icon
html = html.replace('>block<', '>shield<')
html = html.replace('material-symbols-outlined text-9xl', 'material-symbols-outlined text-[128px]')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
