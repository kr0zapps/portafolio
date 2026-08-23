import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire Tier 1 Cards section with an ultra-premium layout
old_tier1 = r'<!-- Proyectos Principales \(Tier 1\) -->.*?<!-- Proyectos Secundarios \(Tier 2\) -->'

new_tier1 = '''<!-- Proyectos Principales (Tier 1) -->
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
    
    <!-- FitGamer (Ultra Premium Card) -->
    <div class="group relative rounded-[2rem] bg-[#f9f9f9] dark:bg-[#030712] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-700 cursor-pointer" onclick="document.getElementById('cs-fitgamer').classList.toggle('expanded')">
        
        <!-- Glow effect -->
        <div class="absolute inset-0 bg-gradient-to-br from-[#0052FF]/0 to-purple-500/0 dark:group-hover:from-[#0052FF]/10 dark:group-hover:to-purple-500/10 transition-colors duration-700 pointer-events-none"></div>
        
        <!-- Inner Ring -->
        <div class="absolute inset-0 rounded-[2rem] ring-1 ring-inset ring-black/5 dark:ring-white/5 pointer-events-none"></div>

        <div class="p-8 md:p-10 pb-0 relative z-10">
            <h3 class="text-3xl md:text-4xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-3">FitGamer</h3>
            <p class="text-lg text-gray-600 dark:text-gray-400 mb-6">Gamificación extrema para fitness</p>
            
            <div class="flex gap-2 flex-wrap mb-10">
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-[#0052FF]/10 text-[#0052FF] px-3 py-1.5 rounded-full border border-[#0052FF]/20"><i data-lucide="smartphone" class="w-3 h-3 mr-1.5"></i>Kotlin</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-[#0052FF]/10 text-[#0052FF] px-3 py-1.5 rounded-full border border-[#0052FF]/20"><i data-lucide="pen-tool" class="w-3 h-3 mr-1.5"></i>Compose</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-[#0052FF]/10 text-[#0052FF] px-3 py-1.5 rounded-full border border-[#0052FF]/20"><i data-lucide="activity" class="w-3 h-3 mr-1.5"></i>HealthConnect</span>
            </div>
        </div>

        <div class="mt-4 relative px-8 pb-8 flex items-center justify-center z-10">
            <div class="relative w-full rounded-2xl overflow-hidden shadow-2xl ring-1 ring-black/10 dark:ring-white/10 group-hover:-translate-y-2 group-hover:scale-[1.02] transition-transform duration-700">
                <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent z-10 pointer-events-none"></div>
                <img src="/fitgamer-mockup.png" alt="FitGamer App Interface" class="w-full h-auto object-cover relative z-0" onerror="this.src='https://images.unsplash.com/photo-1616469829581-73993eb86b02?q=80&w=1000&auto=format&fit=crop';"/>
            </div>
        </div>
        
        <!-- Expanded Content (Hidden by default) -->
        <div class="cs-content w-full bg-white dark:bg-[#050b14] border-t border-[#1a1c1c]/10 dark:border-white/10 relative z-20" id="cs-fitgamer">
            <div class="p-8 md:p-10">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="font-mono text-xs font-bold uppercase tracking-widest text-[#1a1c1c] dark:text-white mb-3">El Problema</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mb-6 leading-relaxed">Las apps de fitness tradicionales sufren de una retención bajísima después del primer mes porque depender de la motivación pura no es escalable.</p>
                        
                        <h4 class="font-mono text-xs font-bold uppercase tracking-widest text-[#1a1c1c] dark:text-white mb-3">Decisión Técnica</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">Arquitectura MVI (Model-View-Intent) con Jetpack Compose para manejar flujos de estado complejos en tiempo real durante los entrenamientos.</p>
                    </div>
                    <div class="grid grid-cols-2 gap-4 h-max">
                        <div class="bg-[#f9f9f9] dark:bg-[#0a1220] p-5 rounded-xl border border-[#1a1c1c]/5 dark:border-white/5">
                            <div class="text-3xl font-extrabold text-[#0052FF] mb-1">4.9<span class="text-lg text-gray-400">/5</span></div>
                            <div class="text-xs font-mono font-bold tracking-widest text-gray-500">PLAY STORE</div>
                        </div>
                        <div class="bg-[#f9f9f9] dark:bg-[#0a1220] p-5 rounded-xl border border-[#1a1c1c]/5 dark:border-white/5">
                            <div class="text-3xl font-extrabold text-[#0052FF] mb-1">60<span class="text-lg text-gray-400">fps</span></div>
                            <div class="text-xs font-mono font-bold tracking-widest text-gray-500">RENDER ANIMATIONS</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Cállate Spam (Ultra Premium Card) -->
    <div class="group relative rounded-[2rem] bg-[#f9f9f9] dark:bg-[#030712] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-xl hover:shadow-2xl transition-all duration-700 cursor-pointer" onclick="document.getElementById('cs-spam').classList.toggle('expanded')">
        
        <!-- Glow effect -->
        <div class="absolute inset-0 bg-gradient-to-br from-red-500/0 to-orange-500/0 dark:group-hover:from-red-500/10 dark:group-hover:to-orange-500/10 transition-colors duration-700 pointer-events-none"></div>
        
        <!-- Inner Ring -->
        <div class="absolute inset-0 rounded-[2rem] ring-1 ring-inset ring-black/5 dark:ring-white/5 pointer-events-none"></div>

        <div class="p-8 md:p-10 pb-0 relative z-10">
            <h3 class="text-3xl md:text-4xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-3">Cállate Spam</h3>
            <p class="text-lg text-gray-600 dark:text-gray-400 mb-6">Filtro ML on-device para llamadas</p>
            
            <div class="flex gap-2 flex-wrap mb-10">
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-red-500/10 text-red-600 dark:text-red-400 px-3 py-1.5 rounded-full border border-red-500/20"><i data-lucide="code" class="w-3 h-3 mr-1.5"></i>Swift</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-red-500/10 text-red-600 dark:text-red-400 px-3 py-1.5 rounded-full border border-red-500/20"><i data-lucide="cpu" class="w-3 h-3 mr-1.5"></i>CoreML</span>
                <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-red-500/10 text-red-600 dark:text-red-400 px-3 py-1.5 rounded-full border border-red-500/20"><i data-lucide="phone-call" class="w-3 h-3 mr-1.5"></i>CallKit</span>
            </div>
        </div>

        <div class="mt-4 relative px-8 flex items-center justify-center h-64 z-10">
            <!-- Abstract Phone UI inside the card -->
            <div class="w-56 h-72 bg-white dark:bg-[#0a1220] rounded-t-[2.5rem] shadow-2xl flex flex-col items-center pt-8 relative border border-[#1a1c1c]/10 dark:border-white/10 group-hover:-translate-y-4 transition-transform duration-700 ring-1 ring-black/5 dark:ring-white/5">
                
                <div class="absolute top-3 w-16 h-4 bg-black rounded-full"></div>
                
                <div class="w-16 h-16 rounded-full bg-red-100 dark:bg-red-900/30 border border-red-500/20 flex items-center justify-center mb-5 mt-4 relative">
                    <div class="absolute inset-0 rounded-full border border-red-500/50 animate-ping opacity-30"></div>
                    <i data-lucide="user-x" class="text-red-600 dark:text-red-400 w-8 h-8 relative z-10"></i>
                </div>
                
                <div class="w-28 h-3 bg-gray-200 dark:bg-gray-800 rounded-full mb-3"></div>
                <div class="w-20 h-2 bg-gray-100 dark:bg-gray-800/50 rounded-full mb-8"></div>
                
                <div class="bg-red-50 dark:bg-red-500/10 border border-red-200 dark:border-red-500/30 px-4 py-2 rounded-full flex items-center gap-2 shadow-sm">
                    <i data-lucide="shield-alert" class="text-red-600 dark:text-red-500 w-3.5 h-3.5"></i>
                    <span class="text-red-600 dark:text-red-500 text-[10px] font-mono font-bold tracking-widest uppercase">ML BLOCKED</span>
                </div>
            </div>
        </div>
        
        <!-- Expanded Content -->
        <div class="cs-content w-full bg-white dark:bg-[#050b14] border-t border-[#1a1c1c]/10 dark:border-white/10 relative z-20" id="cs-spam">
            <div class="p-8 md:p-10">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="font-mono text-xs font-bold uppercase tracking-widest text-[#1a1c1c] dark:text-white mb-3">El Problema</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mb-6 leading-relaxed">Aumento masivo de llamadas spam locales no detectadas por filtros genéricos globales, causando interrupciones constantes.</p>
                        
                        <h4 class="font-mono text-xs font-bold uppercase tracking-widest text-[#1a1c1c] dark:text-white mb-3">Decisión Técnica</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">Implementación de un modelo CoreML procesando datos 100% on-device para garantizar privacidad total y latencia nula.</p>
                    </div>
                    <div class="grid grid-cols-2 gap-4 h-max">
                        <div class="bg-[#f9f9f9] dark:bg-[#0a1220] p-5 rounded-xl border border-[#1a1c1c]/5 dark:border-white/5">
                            <div class="text-3xl font-extrabold text-red-500 mb-1">99.8<span class="text-lg text-gray-400">%</span></div>
                            <div class="text-xs font-mono font-bold tracking-widest text-gray-500">PRECISIÓN LOCAL</div>
                        </div>
                        <div class="bg-[#f9f9f9] dark:bg-[#0a1220] p-5 rounded-xl border border-[#1a1c1c]/5 dark:border-white/5">
                            <div class="text-3xl font-extrabold text-red-500 mb-1"><5<span class="text-lg text-gray-400">ms</span></div>
                            <div class="text-xs font-mono font-bold tracking-widest text-gray-500">LATENCIA CALLKIT</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- Proyectos Secundarios (Tier 2) -->'''

html = re.sub(old_tier1, new_tier1, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
