import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove WebGL Shader script
webgl_pattern = r'// WebGL Shader Background Logic.*?// ThreeJS Logic'
html = re.sub(webgl_pattern, '// ThreeJS Logic', html, flags=re.DOTALL)

# 2. Re-write the Tech Stack section (from id="expertise" to </main>)
tech_stack_pattern = r'<section class="px-5 md:px-16 py-32 max-w-5xl mx-auto w-full scroll-reveal" id="expertise">.*?</section>\n</main>'

new_tech_stack = '''<section class="px-5 md:px-16 py-32 max-w-7xl mx-auto w-full scroll-reveal" id="expertise">
    <div class="mb-16">
        <h2 class="text-6xl font-extrabold text-[#1a1c1c] dark:text-white tracking-tighter transition-colors">Stack Tecnológico</h2>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Mobile -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a0a0a]/50 hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-10 h-10 rounded-full bg-[#003ec7]/10 dark:bg-[#003ec7]/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-[#003ec7] dark:text-[#4facfe]">smartphone</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-lg transition-colors">Mobile Nativo</h3>
            </div>
            <ul class="flex flex-col gap-3">
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-[#003ec7]"></span> Kotlin & Compose</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-gray-400"></span> Swift & SwiftUI</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span> React Native</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span> CoreML & HealthKit</li>
            </ul>
        </div>
        
        <!-- Web -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a0a0a]/50 hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-10 h-10 rounded-full bg-blue-500/10 dark:bg-blue-500/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-blue-600 dark:text-blue-400">web</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-lg transition-colors">Web & Frontend</h3>
            </div>
            <ul class="flex flex-col gap-3">
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> React & Next.js</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-orange-500"></span> Astro & Vite</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-600"></span> TypeScript</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-teal-400"></span> TailwindCSS</li>
            </ul>
        </div>

        <!-- Infra -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a0a0a]/50 hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-10 h-10 rounded-full bg-orange-500/10 dark:bg-orange-500/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-orange-600 dark:text-orange-400">dns</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-lg transition-colors">Backend & Infra</h3>
            </div>
            <ul class="flex flex-col gap-3">
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-green-500"></span> Node.js</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-yellow-500"></span> AWS & Serverless</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-400"></span> Docker</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-700"></span> PostgreSQL</li>
            </ul>
        </div>

        <!-- Tools -->
        <div class="group p-8 border border-[#1a1c1c]/10 dark:border-white/10 rounded-2xl bg-white dark:bg-[#0a0a0a]/50 hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300">
            <div class="flex items-center gap-3 mb-6">
                <div class="w-10 h-10 rounded-full bg-purple-500/10 dark:bg-purple-500/20 flex items-center justify-center">
                    <span class="material-symbols-outlined text-purple-600 dark:text-purple-400">build</span>
                </div>
                <h3 class="font-bold text-[#1a1c1c] dark:text-white text-lg transition-colors">Herramientas</h3>
            </div>
            <ul class="flex flex-col gap-3">
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-red-500"></span> Git & GitHub</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-pink-500"></span> Figma</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> VS Code / Cursor</li>
                <li class="flex items-center gap-3 text-gray-600 dark:text-gray-400 font-mono text-sm transition-colors"><span class="w-1.5 h-1.5 rounded-full bg-gray-600"></span> CI / CD</li>
            </ul>
        </div>
    </div>
</section>
</main>'''

html = re.sub(tech_stack_pattern, new_tech_stack, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
