import re

# 1. Update Layout.astro for SEO
with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

seo_tags = """
        <!-- SEO & Open Graph / Social Cards -->
        <meta property="og:title" content="Jonathan Vidal | Soluciones Digitales" />
        <meta property="og:description" content="Analista Programador / Full Stack Developer. Transformando problemas complejos en soluciones simples, rápidas y escalables." />
        <meta property="og:type" content="website" />
        <meta property="og:url" content="https://kr0zapps.github.io/portafolio/" />
        <meta property="og:image" content="https://kr0zapps.github.io/portafolio/og-image.png" />
        
        <meta name="twitter:card" content="summary_large_image" />
        <meta name="twitter:title" content="Jonathan Vidal | Soluciones Digitales" />
        <meta name="twitter:description" content="Transformando problemas complejos en soluciones simples." />
        <meta name="twitter:image" content="https://kr0zapps.github.io/portafolio/og-image.png" />
"""

if "og:title" not in layout:
    layout = layout.replace('<meta name="generator"', f'{seo_tags}\n\t\t<meta name="generator"')

with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)


# 2. Update index.astro for Sobre Mi section
with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    index = f.read()

# Fix Navbar Link
index = index.replace('href="#" class="text-sm font-medium text-gray-500', 'href="#sobre-mi" class="text-sm font-medium text-gray-500')

# Inject About Me section
sobre_mi_section = """
            <!-- SOBRE MÍ SECTION -->
            <section id="sobre-mi" class="relative max-w-5xl mx-auto px-6 py-24 md:py-32 border-t border-gray-200/50 dark:border-white/5 scroll-mt-20">
                <div class="max-w-3xl">
                    <h2 class="text-4xl md:text-5xl font-extrabold tracking-tight text-[#1a1c1c] dark:text-white mb-8">
                        Ingeniería <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#0052FF] to-blue-400">con propósito.</span>
                    </h2>
                    <div class="space-y-6 text-lg md:text-xl text-gray-600 dark:text-gray-400 leading-relaxed font-medium">
                        <p>
                            Soy Jonathan Vidal, Analista Programador titulado del Duoc UC. Lo que comenzó como curiosidad por la tecnología se transformó en una vocación por construir productos digitales que realmente funcionen.
                        </p>
                        <p>
                            Más allá de los lenguajes y frameworks, mi filosofía de trabajo es simple: <strong class="text-gray-900 dark:text-gray-200">las mejores soluciones son aquellas que los usuarios disfrutan usar y que las empresas pueden escalar sin fricción.</strong> Combino diseño funcional con arquitecturas limpias, ya sea en una Landing Page ultrarrápida o en un sistema transaccional complejo.
                        </p>
                        <p>
                            Actualmente estoy abierto a nuevas oportunidades donde pueda aportar valor técnico y seguir creciendo como profesional.
                        </p>
                    </div>
                    
                    <div class="mt-12 flex flex-wrap gap-4">
                        <a href="/portafolio/CV_Jonathan_Vidal.pdf" target="_blank" download class="inline-flex items-center justify-center gap-2 px-8 py-4 bg-[#1a1c1c] dark:bg-white text-white dark:text-[#1a1c1c] rounded-full font-bold tracking-wide transition-all hover:-translate-y-1 shadow-lg hover:shadow-xl dark:hover:bg-gray-100">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                            Descargar CV (PDF)
                        </a>
                        <a href="mailto:kr0zapps@gmail.com" class="inline-flex items-center justify-center gap-2 px-8 py-4 bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 text-[#1a1c1c] dark:text-white rounded-full font-bold tracking-wide transition-all hover:-translate-y-1 hover:bg-gray-200 dark:hover:bg-white/10">
                            Hablemos
                        </a>
                    </div>
                </div>
            </section>
            
            <!-- OTROS PROYECTOS SECTION -->
"""

# Find where to inject (right before "Otros Proyectos" header or after Bento grid)
# The "Otros Proyectos" header is: <h2 class="text-2xl md:text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-12">Otros Proyectos</h2>
if 'id="sobre-mi"' not in index:
    index = index.replace('<h2 class="text-2xl md:text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-12">Otros Proyectos</h2>', sobre_mi_section + '<h2 class="text-2xl md:text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-12 mt-12">Otros Proyectos</h2>')

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(index)
