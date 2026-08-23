import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Sobre Mi (Remove lies, set "Titulado")
about_section_pattern = r'<!-- About Section -->.*?<!-- Tech Stack Section -->'
about_html = re.search(about_section_pattern, html, flags=re.DOTALL).group(0)

# Replace the title and description
about_html = re.sub(
    r'<p class="font-mono text-\[#003ec7\] dark:text-\[#4facfe\] font-bold uppercase tracking-\[0.2em\] text-sm mb-8 transition-colors">Software Engineer</p>',
    '<p class="font-mono text-[#003ec7] dark:text-[#4facfe] font-bold uppercase tracking-[0.2em] text-sm mb-8 transition-colors">Ingeniero de Software Titulado</p>',
    about_html
)

about_html = re.sub(
    r'<p class="text-xl text-gray-700 dark:text-gray-300 leading-relaxed font-medium mb-6 transition-colors">.*?</p>\s*<p class="text-gray-600 dark:text-gray-400 leading-relaxed mb-6 transition-colors">.*?</p>',
    '''<p class="text-xl text-gray-700 dark:text-gray-300 leading-relaxed font-medium mb-6 transition-colors">
        Soy un Ingeniero de Software titulado apasionado por el desarrollo de aplicaciones. Me enfoco en escribir código limpio y construir soluciones funcionales que resuelvan problemas reales.
    </p>''',
    about_html,
    flags=re.DOTALL
)

# Remove the stats grid
about_html = re.sub(r'<div class="grid grid-cols-2 md:grid-cols-3 gap-6 mt-12">.*?</div>\s*</div>\s*</div>\s*</section>', '</div>\n    </div>\n</section>', about_html, flags=re.DOTALL)

html = html[:html.find('<!-- About Section -->')] + about_html + html[html.find('<!-- Tech Stack Section -->'):]


# 2. Fix Tech Stack (Only specific 7 technologies, flex wrap)
stack_start = html.find('<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 md:gap-6">')
stack_end = html.find('</section>', stack_start)

new_stack = '''<div class="flex flex-wrap justify-center gap-4 md:gap-6">
        <!-- AWS -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-amazonwebservices-plain-wordmark colored dark:devicon-amazonwebservices-plain-wordmark text-[#1a1c1c] dark:text-white text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">AWS</span>
        </div>

        <!-- Docker -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-docker-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Docker</span>
        </div>

        <!-- Kotlin -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-kotlin-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">Kotlin</span>
        </div>

        <!-- PHP -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-php-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">PHP</span>
        </div>
        
        <!-- JavaScript -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-javascript-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">JavaScript</span>
        </div>

        <!-- React -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-react-original colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">React</span>
        </div>

        <!-- MySQL -->
        <div class="group flex flex-col items-center justify-center gap-4 p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300 transform hover:-translate-y-1 cursor-default w-40 md:w-48">
            <i class="devicon-mysql-plain colored text-6xl group-hover:scale-110 transition-transform duration-300"></i>
            <span class="font-bold text-[#1a1c1c] dark:text-white font-mono text-sm tracking-wide">MySQL</span>
        </div>
    </div>
'''

html = html[:stack_start] + new_stack + html[stack_end:]

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
