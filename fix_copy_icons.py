import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Title
old_hero_title = r'INTERFACES QUE<br/>\s*<span class="text-transparent bg-clip-text bg-gradient-to-r from-\[\#0052FF\] to-blue-400 dark:from-white dark:to-gray-500">COBRAN VIDA\.</span>'
new_hero_title = 'DESARROLLO<br/>\n                <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#0052FF] to-blue-400 dark:from-white dark:to-gray-500">FRONTEND.</span>'
html = re.sub(old_hero_title, new_hero_title, html)

# 2. Update Hero Bio
old_hero_bio = 'Soy Jonathan Vidal, especialista en transmutar diseño complejo en código hiper-optimizado. No solo construyo aplicaciones; creo ecosistemas digitales que se sienten fluidos, rápidos y excepcionales.'
new_hero_bio = 'Soy Jonathan Vidal, titulado de Duoc UC. Me especializo en el desarrollo de Landing Pages optimizadas, Dashboards interactivos y aplicaciones web. Disfruto transformar buenas ideas en interfaces limpias, rápidas y fáciles de usar.'
html = html.replace(old_hero_bio, new_hero_bio)

# 3. Update Bento Grid Title & Bio
old_bento_title = 'Arquitectura UI & Sistemas Core'
new_bento_title = 'Desarrollo Frontend & UI'
html = html.replace(old_bento_title, new_bento_title)

old_bento_bio = 'Desarrollo de e-commerce premium, dashboards analíticos complejos y sistemas transaccionales. Experto en control de estado global, integraciones en tiempo real y diseño pixel-perfect de alta conversión.'
new_bento_bio = 'Creación de Landing Pages orientadas a conversión, Dashboards de gestión y sitios web interactivos. Enfoque práctico en el rendimiento, diseño limpio y buena experiencia de usuario.'
html = html.replace(old_bento_bio, new_bento_bio)


# 4. Inject Icons into Project Tags
# Mapping of Tag Name to Devicon class and color
icon_map = {
    'Kotlin': 'devicon-kotlin-plain colored',
    'Compose': 'devicon-android-plain text-[#3DDC84]',
    'HealthConnect': 'devicon-google-plain colored',
    'Swift': 'devicon-swift-plain text-[#F05138]',
    'CoreML': 'devicon-apple-original dark:text-white',
    'CallKit': 'devicon-apple-original dark:text-white',
    'HTML/CSS': 'devicon-html5-plain colored',
    'JS': 'devicon-javascript-plain colored',
    'Bootstrap': 'devicon-bootstrap-plain colored',
    'React': 'devicon-react-original colored',
    'Supabase': 'devicon-supabase-plain colored',
    'Tailwind': 'devicon-tailwindcss-plain colored',
    'NODE.JS': 'devicon-nodejs-plain colored',
    'MYSQL': 'devicon-mysql-plain colored',
    'FIREBASE': 'devicon-firebase-plain colored',
    'ASTRO': 'devicon-astro-plain text-[#1a1c1c] dark:text-white'
}

# Find all tag spans
def replace_tag(match):
    full_span = match.group(0)
    tag_text = match.group(1).strip()
    
    # Capitalization fixes for matching
    lookup = tag_text
    if lookup.upper() == 'NODE.JS': lookup = 'NODE.JS'
    elif lookup.upper() == 'MYSQL': lookup = 'MYSQL'
    elif lookup.upper() == 'FIREBASE': lookup = 'FIREBASE'
    elif lookup.upper() == 'ASTRO': lookup = 'ASTRO'
    
    icon_class = icon_map.get(lookup, icon_map.get(lookup.upper(), ''))
    
    if icon_class:
        # Add flex and icon
        new_span = full_span.replace('class="font-mono', 'class="font-mono flex items-center gap-1.5')
        new_span = new_span.replace(f'>{tag_text}<', f'><i class="{icon_class} text-sm"></i>{tag_text}<')
        return new_span
    return full_span

html = re.sub(r'<span class="font-mono text-\[10px\] font-bold tracking-widest uppercase bg-gray-100[^>]+>([^<]+)</span>', replace_tag, html)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
