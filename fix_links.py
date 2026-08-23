import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Nav fix: "Sobre mí" points to the top
html = html.replace('href="#about"', 'href="#"')

# Split by cards to safely modify each project without affecting others
parts = html.split('<!-- CARD ')

if len(parts) >= 5:
    # FITGAMER (Index 1)
    # Reemplazar los "#" por la URL de la Play Store
    parts[1] = parts[1].replace('href="#"', 'href="https://play.google.com/store/apps/details?id=com.fitgamer.app&hl=es_CL"')
    
    # CÁLLATE SPAM (Index 2)
    # Reemplazar botón magnético superior
    parts[2] = re.sub(
        r'<a href="#" target="_blank" class="magnetic-btn[^>]+>.*?</a>',
        '<div class="w-12 h-12 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center border border-gray-200 dark:border-white/10 text-gray-400 dark:text-gray-600 shrink-0 cursor-not-allowed opacity-60" title="Descontinuado"><i data-lucide="ban" class="w-5 h-5"></i></div>',
        parts[2], flags=re.DOTALL
    )
    # Reemplazar botón overlay central
    parts[2] = re.sub(
        r'<a href="#" target="_blank" class="px-6 py-3 bg-white text-black font-bold[^>]+>Ver Proyecto</a>',
        '<span class="px-6 py-3 bg-red-500/90 text-white font-bold rounded-full transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 shadow-xl cursor-not-allowed tracking-wide">Descontinuado</span>',
        parts[2]
    )

    # SISTEMA RSVP (Index 4)
    # Reemplazar botón magnético superior
    parts[4] = re.sub(
        r'<a href="#" target="_blank" class="magnetic-btn[^>]+>.*?</a>',
        '<div class="w-12 h-12 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center border border-gray-200 dark:border-white/10 text-gray-400 dark:text-gray-600 shrink-0 cursor-not-allowed opacity-60" title="Vista Previa"><i data-lucide="eye" class="w-5 h-5"></i></div>',
        parts[4], flags=re.DOTALL
    )
    # Reemplazar botón overlay central
    parts[4] = re.sub(
        r'<a href="#" target="_blank" class="px-6 py-3 bg-white text-black font-bold[^>]+>Ver Proyecto</a>',
        '<span class="px-6 py-3 bg-white/50 dark:bg-black/50 text-gray-600 dark:text-gray-300 backdrop-blur-md font-bold rounded-full transform translate-y-4 group-hover:translate-y-0 transition-all duration-500 shadow-xl cursor-not-allowed tracking-wide">Vista Previa</span>',
        parts[4]
    )

html = '<!-- CARD '.join(parts)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
