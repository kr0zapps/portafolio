import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Proyectos Destacados headers and Cards
projects_section_pattern = r'<!-- Projects Section -->.*?<!-- Stack Section \(IDE Style\) -->'
projects_section = re.search(projects_section_pattern, html, flags=re.DOTALL).group(0)

# Fix h2 title
projects_section = projects_section.replace('text-[#1a1c1c] tracking-tighter', 'text-[#1a1c1c] dark:text-white tracking-tighter transition-colors')

# Fix FitGamer / Cállate Spam cards bg
projects_section = projects_section.replace('bg-[#f3f3f3]', 'bg-[#f3f3f3] dark:bg-[#0a192f] transition-colors duration-300')
projects_section = projects_section.replace('bg-[#f9f9f9]', 'bg-[#f9f9f9] dark:bg-[#061020] transition-colors duration-300')

# Fix text in cards
projects_section = projects_section.replace('text-[#1a1c1c] mb-2', 'text-[#1a1c1c] dark:text-white mb-2 transition-colors')
projects_section = projects_section.replace('text-[#434656]', 'text-gray-600 dark:text-gray-400 transition-colors')
projects_section = projects_section.replace('border-[#1a1c1c]/10', 'border-[#1a1c1c]/10 dark:border-white/10')
projects_section = projects_section.replace('hover:border-[#1a1c1c]/30', 'hover:border-[#1a1c1c]/30 dark:hover:border-white/30')

html = html[:html.find('<!-- Projects Section -->')] + projects_section + html[html.find('<!-- Stack Section (IDE Style) -->'):]

# 2. Fix Tech Stack Section
# Find the exact start and end of the IDE section
stack_start = html.find('<!-- Stack Section (IDE Style) -->')
# Find the end of the file or the end of the main tag
main_end = html.find('</main>')

new_tech_stack = '''<!-- Tech Stack Section -->
<section class="px-5 md:px-16 py-32 max-w-7xl mx-auto w-full scroll-reveal" id="expertise">
    <div class="mb-16">
        <h2 class="text-6xl font-extrabold text-[#1a1c1c] dark:text-white tracking-tighter transition-colors">Stack Tecnológico</h2>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Mobile -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-[#f9f9f9] dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-12 h-12 rounded-full bg-[#003ec7]/10 dark:bg-[#003ec7]/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-[#003ec7] dark:text-[#4facfe] text-2xl">smartphone</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-xl transition-colors">Mobile Nativo</h3>
            </div>
            <ul class="flex flex-col gap-4">
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-[#003ec7]"></span> Kotlin & Compose</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-orange-500"></span> Swift & SwiftUI</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-[#4facfe]"></span> React Native</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span> CoreML & HealthKit</li>
            </ul>
        </div>
        
        <!-- Web -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-[#f9f9f9] dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-12 h-12 rounded-full bg-blue-500/10 dark:bg-blue-500/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-blue-600 dark:text-blue-400 text-2xl">web</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-xl transition-colors">Web & Frontend</h3>
            </div>
            <ul class="flex flex-col gap-4">
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-[#4facfe]"></span> React & Next.js</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-orange-600"></span> Astro & Vite</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-600"></span> TypeScript</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-teal-400"></span> TailwindCSS</li>
            </ul>
        </div>

        <!-- Infra -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-[#f9f9f9] dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-12 h-12 rounded-full bg-orange-500/10 dark:bg-orange-500/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-orange-600 dark:text-orange-400 text-2xl">dns</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-xl transition-colors">Backend & Infra</h3>
            </div>
            <ul class="flex flex-col gap-4">
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-green-500"></span> Node.js</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-yellow-500"></span> AWS & Serverless</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-[#4facfe]"></span> Docker</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-700"></span> PostgreSQL</li>
            </ul>
        </div>

        <!-- Tools -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-[#f9f9f9] dark:bg-[#0a192f] hover:bg-[#f3f3f3] dark:hover:bg-[#112240] transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-12 h-12 rounded-full bg-purple-500/10 dark:bg-purple-500/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-purple-600 dark:text-purple-400 text-2xl">build</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-xl transition-colors">Herramientas</h3>
            </div>
            <ul class="flex flex-col gap-4">
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-red-500"></span> Git & GitHub</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-pink-500"></span> Figma</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-[#4facfe]"></span> VS Code / Cursor</li>
                <li class="flex items-center gap-3 text-[#1a1c1c] dark:text-gray-300 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-gray-500"></span> CI / CD</li>
            </ul>
        </div>
    </div>
</section>
'''

html = html[:stack_start] + new_tech_stack + html[main_end:]

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
