import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update navigation href for Sobre Mi
html = html.replace('href="#">Sobre mí</a>', 'href="#about">Sobre mí</a>')

# 2. Extract and replace Tech Stack Section
stack_start = html.find('<!-- Tech Stack Section -->')
if stack_start == -1:
    # fallback
    stack_start = html.find('<section class="px-5 md:px-16 py-32 max-w-7xl mx-auto w-full scroll-reveal" id="expertise">')
main_end = html.find('</main>')

new_tech_stack = '''<!-- Tech Stack Section -->
<section class="px-5 md:px-16 py-32 max-w-7xl mx-auto w-full scroll-reveal" id="expertise">
    <div class="mb-16 flex flex-col md:flex-row md:items-end justify-between gap-8">
        <div>
            <h2 class="text-5xl md:text-6xl font-extrabold text-[#1a1c1c] dark:text-white tracking-tighter transition-colors mb-4">Core Stack</h2>
            <p class="text-gray-600 dark:text-gray-400 max-w-xl text-lg">Tecnologías en las que me especializo para construir sistemas robustos, escalables y con rendimiento nativo.</p>
        </div>
    </div>
    
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 md:gap-6">
        <!-- Tech Items -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-kotlin-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Kotlin</span>
        </div>
        
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-swift-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Swift</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-react-original colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">React Native</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-typescript-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">TypeScript</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-nextjs-plain dark:devicon-nextjs-original text-[#1a1c1c] dark:text-white text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Next.js</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-tailwindcss-original colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Tailwind CSS</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-nodejs-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Node.js</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-postgresql-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">PostgreSQL</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-amazonwebservices-plain-wordmark colored dark:devicon-amazonwebservices-plain-wordmark text-[#1a1c1c] dark:text-white text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">AWS</span>
        </div>

        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default">
            <i class="devicon-docker-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Docker</span>
        </div>
    </div>
</section>
'''

html = html[:stack_start] + new_tech_stack + html[main_end:]


# 3. Create Sobre Mi Section
about_section = '''
<!-- About Section -->
<section class="px-5 md:px-16 py-32 max-w-7xl mx-auto w-full border-t border-[#1a1c1c]/10 dark:border-white/10 transition-colors" id="about">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start scroll-reveal">
        <div class="lg:col-span-5">
            <h2 class="text-6xl font-extrabold text-[#1a1c1c] dark:text-white tracking-tighter mb-4 transition-colors">Jonathan Vidal</h2>
            <p class="font-mono text-[#003ec7] dark:text-[#4facfe] font-bold uppercase tracking-[0.2em] text-sm mb-8 transition-colors">Software Engineer</p>
            
            <div class="flex gap-4">
                <a href="#" class="inline-flex items-center justify-center bg-[#1a1c1c] dark:bg-white text-white dark:text-[#1a1c1c] px-6 py-3 rounded-xl font-bold hover:bg-[#003ec7] dark:hover:bg-[#4facfe] dark:hover:text-white transition-colors duration-300">
                    <span class="material-symbols-outlined mr-2 text-sm">download</span> Descargar CV
                </a>
                <a href="https://linkedin.com" target="_blank" class="inline-flex items-center justify-center border border-[#1a1c1c]/20 dark:border-white/20 text-[#1a1c1c] dark:text-white px-4 py-3 rounded-xl hover:bg-[#1a1c1c]/5 dark:hover:bg-white/10 transition-colors duration-300">
                    <span class="material-symbols-outlined text-lg">link</span>
                </a>
            </div>
        </div>
        
        <div class="lg:col-span-7 prose prose-lg dark:prose-invert">
            <p class="text-xl text-gray-700 dark:text-gray-300 leading-relaxed font-medium mb-6 transition-colors">
                Especialista en la construcción de ecosistemas digitales completos, desde interfaces móviles nativas con rendimiento de 60fps hasta arquitecturas backend escalables en la nube.
            </p>
            <p class="text-gray-600 dark:text-gray-400 leading-relaxed mb-6 transition-colors">
                Mi enfoque no es solo escribir código, sino diseñar soluciones de ingeniería que soporten el crecimiento exponencial de las empresas. Tengo experiencia directa transformando ideas complejas en productos reales y mantenibles, aplicando principios de Clean Architecture y las mejores prácticas de la industria.
            </p>
            <div class="grid grid-cols-2 md:grid-cols-3 gap-6 mt-12">
                <div class="border-l-2 border-[#003ec7] dark:border-[#4facfe] pl-4 transition-colors">
                    <p class="text-4xl font-extrabold text-[#1a1c1c] dark:text-white transition-colors">5+</p>
                    <p class="font-mono text-xs text-gray-500 dark:text-gray-400 uppercase tracking-widest mt-1">Años Exp.</p>
                </div>
                <div class="border-l-2 border-[#003ec7] dark:border-[#4facfe] pl-4 transition-colors">
                    <p class="text-4xl font-extrabold text-[#1a1c1c] dark:text-white transition-colors">12</p>
                    <p class="font-mono text-xs text-gray-500 dark:text-gray-400 uppercase tracking-widest mt-1">Proyectos</p>
                </div>
                <div class="border-l-2 border-[#003ec7] dark:border-[#4facfe] pl-4 transition-colors">
                    <p class="text-4xl font-extrabold text-[#1a1c1c] dark:text-white transition-colors">100%</p>
                    <p class="font-mono text-xs text-gray-500 dark:text-gray-400 uppercase tracking-widest mt-1">Delivery</p>
                </div>
            </div>
        </div>
    </div>
</section>
'''

# Insert About section right after Work (Projects) section
# Find end of projects section
expertise_idx = html.find('<!-- Tech Stack Section -->')
html = html[:expertise_idx] + about_section + html[expertise_idx:]

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
