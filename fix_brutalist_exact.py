with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's find the exact boundaries for Tier 1
start_marker = "<!-- FitGamer (Tier 1) -->"
end_marker = "<!-- Tier 2 (Compact Cards) -->"

if start_marker in html and end_marker in html:
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    
    before = html[:start_idx]
    after = html[end_idx:]
    
    new_tier1 = '''<!-- Proyectos Principales (Tier 1) -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-16">
    
    <!-- FitGamer (Sober Brutalist Card) -->
    <div class="group relative rounded-[1rem] bg-white dark:bg-[#060b13] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer flex flex-col" onclick="document.querySelectorAll('.cs-content').forEach(el => el.classList.toggle('expanded'))">
        
        <div class="p-8 md:p-10 pb-0 relative z-10 flex-grow">
            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">FitGamer</h3>
            <p class="text-base text-gray-600 dark:text-gray-400 mb-6">Gamificación extrema para fitness</p>
            
            <div class="flex gap-2 flex-wrap mb-10">
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="smartphone" class="w-3 h-3 mr-1.5"></i>Kotlin</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="pen-tool" class="w-3 h-3 mr-1.5"></i>Compose</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="activity" class="w-3 h-3 mr-1.5"></i>HealthConnect</span>
            </div>
        </div>

        <div class="relative px-8 pb-8 flex items-center justify-center z-10">
            <div class="w-full rounded-xl overflow-hidden border border-[#1a1c1c]/10 dark:border-white/10 bg-gray-100 dark:bg-[#0a1220]">
                <img src="/fitgamer-mockup.png" alt="FitGamer App Interface" class="w-full h-auto object-cover opacity-90 grayscale group-hover:grayscale-0 transition-all duration-500" onerror="this.src='https://images.unsplash.com/photo-1616469829581-73993eb86b02?q=80&w=1000&auto=format&fit=crop';"/>
            </div>
        </div>
        
        <!-- Expanded Content -->
        <div class="cs-content w-full bg-[#f9f9f9] dark:bg-[#0a1120] border-t border-[#1a1c1c]/5 dark:border-white/5 relative z-20 expanded" id="cs-fitgamer">
            <div class="p-8 md:p-10">
                <div class="flex flex-col gap-6">
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">El Problema</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Falta de retención en apps de fitness por depender exclusivamente de la motivación pura a corto plazo.</p>
                    </div>
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">Decisión Técnica</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Arquitectura MVI con Jetpack Compose para manejar flujos de estado complejos en tiempo real.</p>
                    </div>
                    <!-- Sober Stats -->
                    <div class="flex gap-8 mt-2 pt-6 border-t border-[#1a1c1c]/10 dark:border-white/10">
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight">4.9<span class="text-sm text-gray-400 ml-1">/5</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">PLAY STORE</div>
                        </div>
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight">60<span class="text-sm text-gray-400 ml-1">fps</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">ANIMATIONS</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Cállate Spam (Sober Brutalist Card) -->
    <div class="group relative rounded-[1rem] bg-white dark:bg-[#060b13] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-sm hover:shadow-md transition-all duration-300 cursor-pointer flex flex-col" onclick="document.querySelectorAll('.cs-content').forEach(el => el.classList.toggle('expanded'))">
        
        <div class="p-8 md:p-10 pb-0 relative z-10 flex-grow">
            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Cállate Spam</h3>
            <p class="text-base text-gray-600 dark:text-gray-400 mb-6">Filtro ML on-device para llamadas</p>
            
            <div class="flex gap-2 flex-wrap mb-10">
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="code" class="w-3 h-3 mr-1.5"></i>Swift</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="cpu" class="w-3 h-3 mr-1.5"></i>CoreML</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="phone-call" class="w-3 h-3 mr-1.5"></i>CallKit</span>
            </div>
        </div>

        <div class="relative px-8 flex items-center justify-center h-64 z-10">
            <!-- Abstract Phone UI inside the card -->
            <div class="w-56 h-72 bg-gray-50 dark:bg-[#0a1220] rounded-t-[2.5rem] shadow-lg flex flex-col items-center pt-8 relative border border-[#1a1c1c]/10 dark:border-white/10">
                <div class="absolute top-3 w-16 h-4 bg-gray-300 dark:bg-black rounded-full"></div>
                <div class="w-16 h-16 rounded-full bg-red-50 dark:bg-red-900/10 border border-red-200 dark:border-red-500/20 flex items-center justify-center mb-5 mt-4 relative">
                    <i data-lucide="user-x" class="text-red-500 w-8 h-8 relative z-10"></i>
                </div>
                
                <div class="w-28 h-2 bg-gray-200 dark:bg-gray-800 rounded-full mb-3"></div>
                <div class="w-20 h-2 bg-gray-100 dark:bg-gray-800/50 rounded-full mb-8"></div>
                
                <div class="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-500/20 px-4 py-2 rounded-full flex items-center gap-2">
                    <i data-lucide="shield-alert" class="text-red-500 w-3.5 h-3.5"></i>
                    <span class="text-red-500 text-[10px] font-mono font-bold tracking-widest uppercase">ML BLOCKED</span>
                </div>
            </div>
        </div>
        
        <!-- Expanded Content -->
        <div class="cs-content w-full bg-[#f9f9f9] dark:bg-[#0a1120] border-t border-[#1a1c1c]/5 dark:border-white/5 relative z-20 expanded" id="cs-spam">
            <div class="p-8 md:p-10">
                <div class="flex flex-col gap-6">
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">El Problema</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Llamadas spam locales no detectadas por filtros globales, causando interrupciones constantes.</p>
                    </div>
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">Decisión Técnica</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Modelo CoreML procesando datos 100% on-device para garantizar privacidad y latencia nula.</p>
                    </div>
                    <!-- Sober Stats -->
                    <div class="flex gap-8 mt-2 pt-6 border-t border-[#1a1c1c]/10 dark:border-white/10">
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight">99.8<span class="text-sm text-gray-400 ml-1">%</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">PRECISIÓN</div>
                        </div>
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight"><5<span class="text-sm text-gray-400 ml-1">ms</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">LATENCIA</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
'''
    html = before + new_tier1 + after

# Now let's fix the Tier 2 section to include the new card.
old_tier2_start = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">'
if old_tier2_start in html:
    new_card = '''
        <!-- Landing Page CTA Card -->
        <div class="group bg-white dark:bg-[#060b13] p-8 rounded-[1rem] border border-[#1a1c1c]/10 dark:border-white/10 hover:border-[#1a1c1c]/30 dark:hover:border-white/30 transition-all duration-300 flex flex-col justify-between shadow-sm hover:shadow-md cursor-pointer">
            <div>
                <div class="w-10 h-10 rounded-full bg-[#1a1c1c] dark:bg-white flex items-center justify-center mb-6">
                    <i data-lucide="layout-template" class="text-white dark:text-[#1a1c1c] w-5 h-5"></i>
                </div>
                <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white mb-2">Desarrollo a Medida</h4>
                <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed mb-6">¿Necesitas una Landing Page, un Dashboard o un sitio corporativo? Construyo cualquier tipo de web enfocada en conversión y rendimiento perfecto.</p>
            </div>
            <a href="mailto:contacto@kr0zapps.com" class="inline-flex items-center text-sm font-bold text-[#1a1c1c] dark:text-white hover:opacity-70 transition-opacity uppercase tracking-wider font-mono">
                Solicitar Cotización <i data-lucide="arrow-up-right" class="w-4 h-4 ml-1"></i>
            </a>
        </div>
'''
    html = html.replace(old_tier2_start, old_tier2_start + "\n" + new_card)

# Now fix the Theme Toggle Button
old_toggle_start = '<button id="theme-toggle"'
old_toggle_end = '</button>'
if old_toggle_start in html:
    start_idx = html.find(old_toggle_start)
    end_idx = html.find(old_toggle_end, start_idx) + len(old_toggle_end)
    
    before_toggle = html[:start_idx]
    after_toggle = html[end_idx:]
    
    new_toggle = '''<button id="theme-toggle" class="relative flex items-center w-14 h-7 bg-[#e5e5e5] dark:bg-[#1a1c1c] rounded-full p-1 transition-colors duration-300 border border-[#1a1c1c]/10 dark:border-white/10 shrink-0">
    <!-- Moon (visible in dark mode, on the left) -->
    <i data-lucide="moon" class="absolute left-1.5 w-3.5 h-3.5 text-white opacity-0 dark:opacity-100 transition-opacity duration-300 pointer-events-none"></i>
    <!-- Sun (visible in light mode, on the right) -->
    <i data-lucide="sun" class="absolute right-1.5 w-3.5 h-3.5 text-[#1a1c1c] opacity-100 dark:opacity-0 transition-opacity duration-300 pointer-events-none"></i>
    <!-- Thumb -->
    <div class="theme-toggle-thumb absolute w-5 h-5 bg-white dark:bg-[#2a2d2d] rounded-full shadow-sm transform transition-transform duration-300 top-1/2 -translate-y-1/2 left-1 dark:translate-x-7 z-20"></div>
</button>'''
    html = before_toggle + new_toggle + after_toggle

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
