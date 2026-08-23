with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace custom typography classes with standard Tailwind v4 ones

replacements = {
    # Hero Title
    'font-display-xl-mobile md:font-display-xl text-display-xl-mobile md:text-display-xl': 'text-6xl md:text-[120px] font-extrabold leading-[0.9] tracking-tighter',
    
    # Hero subtitle
    'font-body-lg text-body-lg text-on-surface-variant': 'text-lg text-[#434656] font-normal',
    
    # Buttons
    'font-code-mono text-code-mono': 'font-mono text-sm font-medium',
    
    # Nav links
    'font-label-caps text-label-caps': 'font-mono text-xs font-bold tracking-[0.08em]',
    
    # Section titles
    'font-headline-md text-headline-md text-on-surface': 'text-3xl font-semibold tracking-tight text-[#1a1c1c]',
    
    # Project subtitle
    'font-body-md text-on-surface-variant': 'text-base text-[#434656]',
    
    # KPIS block
    'font-display-xl-mobile text-electric-blue': 'text-5xl md:text-6xl font-extrabold tracking-tighter text-[#0052FF]',
    
    # Small labels
    'font-label-caps text-[10px]': 'font-mono text-[10px] font-bold tracking-widest',
    'font-label-caps uppercase text-sm': 'font-mono text-xs font-bold uppercase tracking-widest',
    
    # Other instances of display-xl-mobile
    'font-display-xl-mobile text-on-surface': 'text-6xl font-extrabold tracking-tighter text-[#1a1c1c]',
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Fix translations just in case anything was missed
html = html.replace('>Work<', '>Trabajo<')
html = html.replace('>Expertise<', '>Especialidad<')
html = html.replace('>About<', '>Sobre mí<')
html = html.replace('>Available<', '>Disponible<')
html = html.replace('View Selected Work', 'Ver Trabajos')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
