import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire WORK section to fix the grid layout issue!
work_pattern = r'<!-- Projects Section -->.*?<!-- About Section -->'

new_work = '''<!-- Projects Section -->
<section class="px-5 md:px-16 py-32 max-w-7xl mx-auto w-full flex flex-col gap-12" id="work">
    <div class="scroll-reveal">
        <h2 class="text-5xl md:text-6xl font-extrabold text-[#1a1c1c] dark:text-white tracking-tighter transition-colors mb-4">Proyectos Destacados</h2>
        <p class="text-gray-600 dark:text-gray-400 max-w-xl text-lg">Sistemas complejos destilados en interfaces precisas y rendimiento brutal.</p>
    </div>

    <!-- MAIN GRID: 2 Columns on Large Screens -->
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        
        <!-- CARD 1: FitGamer -->
        <div class="group relative rounded-[1rem] bg-white dark:bg-[#060b13] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-sm flex flex-col">
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
            <div class="w-full bg-[#f9f9f9] dark:bg-[#0a1120] border-t border-[#1a1c1c]/5 dark:border-white/5 p-8 md:p-10">
                <div class="flex flex-col gap-6">
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">El Problema</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Falta de retención en apps de fitness por depender exclusivamente de la motivación a corto plazo.</p>
                    </div>
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">Decisión Técnica</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Arquitectura MVI con Jetpack Compose para flujos de estado complejos en tiempo real.</p>
                    </div>
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

        <!-- CARD 2: Cállate Spam -->
        <div class="group relative rounded-[1rem] bg-white dark:bg-[#060b13] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-sm flex flex-col">
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
            <div class="w-full bg-[#f9f9f9] dark:bg-[#0a1120] border-t border-[#1a1c1c]/5 dark:border-white/5 p-8 md:p-10">
                <div class="flex flex-col gap-6">
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">El Problema</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Llamadas spam locales no detectadas por filtros globales, causando interrupciones.</p>
                    </div>
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">Decisión Técnica</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Modelo CoreML procesando datos 100% on-device para garantizar privacidad y latencia nula.</p>
                    </div>
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

        <!-- CARD 3: RedNorte -->
        <div class="group relative rounded-[1rem] bg-white dark:bg-[#060b13] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-sm flex flex-col">
            <div class="p-8 md:p-10 pb-0 relative z-10 flex-grow">
                <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">RedNorte</h3>
                <p class="text-base text-gray-600 dark:text-gray-400 mb-6">Clínica inteligente y notificaciones SMS</p>
                <div class="flex gap-2 flex-wrap mb-10">
                    <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="server" class="w-3 h-3 mr-1.5"></i>NodeJS</span>
                    <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="database" class="w-3 h-3 mr-1.5"></i>MySQL</span>
                    <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="message-square" class="w-3 h-3 mr-1.5"></i>Microservicios</span>
                </div>
            </div>
            <div class="relative px-8 flex items-center justify-center h-64 z-10">
                <!-- Abstract Dashboard UI -->
                <div class="w-full h-56 bg-gray-50 dark:bg-[#0a1220] rounded-t-xl shadow-lg border-t border-l border-r border-[#1a1c1c]/10 dark:border-white/10 p-4 flex gap-4">
                    <!-- Sidebar -->
                    <div class="w-12 border-r border-gray-200 dark:border-gray-800 flex flex-col gap-4">
                        <div class="w-6 h-6 rounded-md bg-blue-500/20 text-blue-500 flex items-center justify-center"><i data-lucide="calendar" class="w-3 h-3"></i></div>
                        <div class="w-6 h-6 rounded-md bg-gray-200 dark:bg-gray-800"></div>
                        <div class="w-6 h-6 rounded-md bg-gray-200 dark:bg-gray-800"></div>
                    </div>
                    <!-- Calendar View -->
                    <div class="flex-grow flex flex-col gap-3 pt-2">
                        <div class="w-32 h-3 bg-gray-200 dark:bg-gray-800 rounded-full mb-2"></div>
                        <div class="w-full h-10 bg-green-50 dark:bg-green-900/10 border border-green-200 dark:border-green-500/20 rounded-md flex items-center px-3 justify-between">
                            <div class="w-16 h-2 bg-green-500/50 rounded-full"></div>
                            <i data-lucide="check-circle" class="w-3 h-3 text-green-500"></i>
                        </div>
                        <div class="w-full h-10 bg-yellow-50 dark:bg-yellow-900/10 border border-yellow-200 dark:border-yellow-500/20 rounded-md flex items-center px-3 justify-between relative overflow-hidden">
                            <div class="w-20 h-2 bg-yellow-500/50 rounded-full"></div>
                            <div class="absolute right-0 top-0 h-full bg-yellow-500 flex items-center px-2">
                                <span class="text-[8px] font-bold text-black uppercase">Reasignando</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-full bg-[#f9f9f9] dark:bg-[#0a1120] border-t border-[#1a1c1c]/5 dark:border-white/5 p-8 md:p-10">
                <div class="flex flex-col gap-6">
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">El Problema</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Gestión manual de ausencias en clínicas generando tiempos muertos y pérdida de ingresos constante.</p>
                    </div>
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">Decisión Técnica</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Clúster de microservicios con reasignación automática de listas de espera y notificación dual SMS/Email.</p>
                    </div>
                    <div class="flex gap-8 mt-2 pt-6 border-t border-[#1a1c1c]/10 dark:border-white/10">
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight"><1<span class="text-sm text-gray-400 ml-1">s</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">REASIGNACIÓN</div>
                        </div>
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight">0<span class="text-sm text-gray-400 ml-1">m</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">TIEMPO MUERTO</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- CARD 4: Cuneta App -->
        <div class="group relative rounded-[1rem] bg-white dark:bg-[#060b13] border border-[#1a1c1c]/10 dark:border-white/10 overflow-hidden shadow-sm flex flex-col">
            <div class="p-8 md:p-10 pb-0 relative z-10 flex-grow">
                <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Cuneta App</h3>
                <p class="text-base text-gray-600 dark:text-gray-400 mb-6">Reporte vial ciudadano offline-first</p>
                <div class="flex gap-2 flex-wrap mb-10">
                    <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="smartphone" class="w-3 h-3 mr-1.5"></i>React Native</span>
                    <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="map" class="w-3 h-3 mr-1.5"></i>Maps API</span>
                    <span class="flex items-center font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 text-[#1a1c1c] dark:text-white px-3 py-1.5 rounded-full"><i data-lucide="cloud" class="w-3 h-3 mr-1.5"></i>Firebase</span>
                </div>
            </div>
            <div class="relative px-8 flex items-center justify-center h-64 z-10">
                <!-- Abstract Map UI -->
                <div class="w-full h-56 bg-gray-100 dark:bg-[#0a1220] rounded-t-xl shadow-lg border-t border-l border-r border-[#1a1c1c]/10 dark:border-white/10 relative overflow-hidden flex items-center justify-center">
                    <!-- Map grid lines -->
                    <div class="absolute inset-0 opacity-10 dark:opacity-5" style="background-image: linear-gradient(#1a1c1c 1px, transparent 1px), linear-gradient(90deg, #1a1c1c 1px, transparent 1px); background-size: 20px 20px;"></div>
                    <div class="absolute inset-0 opacity-10 dark:opacity-10 dark:invert" style="background-image: linear-gradient(white 1px, transparent 1px), linear-gradient(90deg, white 1px, transparent 1px); background-size: 20px 20px;"></div>
                    
                    <!-- Map Pin 1 -->
                    <div class="absolute top-10 left-10 text-red-500 flex flex-col items-center">
                        <i data-lucide="map-pin" class="w-6 h-6 fill-red-500/20"></i>
                    </div>
                    <!-- Map Pin 2 (Active) -->
                    <div class="relative text-[#0052FF] flex flex-col items-center z-10">
                        <div class="bg-white dark:bg-black px-3 py-1.5 rounded-md shadow-lg border border-[#1a1c1c]/10 dark:border-white/10 mb-2 font-mono text-[10px] font-bold">NUEVO REPORTE</div>
                        <i data-lucide="map-pin" class="w-8 h-8 fill-[#0052FF]/20 animate-bounce"></i>
                        <div class="w-4 h-1 bg-black/20 dark:bg-white/20 rounded-full mt-1 blur-[1px]"></div>
                    </div>
                </div>
            </div>
            <div class="w-full bg-[#f9f9f9] dark:bg-[#0a1120] border-t border-[#1a1c1c]/5 dark:border-white/5 p-8 md:p-10">
                <div class="flex flex-col gap-6">
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">El Problema</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Burocracia y lentitud en el reporte ciudadano de baches y daños viales, con pérdida de datos en zonas sin red.</p>
                    </div>
                    <div>
                        <h4 class="font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 mb-2">Decisión Técnica</h4>
                        <p class="text-sm text-[#1a1c1c] dark:text-gray-300 leading-relaxed">Sincronización en segundo plano offline-first, agilizando el envío con clustering automático por GPS.</p>
                    </div>
                    <div class="flex gap-8 mt-2 pt-6 border-t border-[#1a1c1c]/10 dark:border-white/10">
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight">100<span class="text-sm text-gray-400 ml-1">%</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">OFFLINE SYNC</div>
                        </div>
                        <div>
                            <div class="text-2xl md:text-3xl font-bold text-[#1a1c1c] dark:text-white mb-1 tracking-tight">2K<span class="text-sm text-gray-400 ml-1">+</span></div>
                            <div class="text-[10px] font-mono font-bold tracking-widest text-gray-500">REPORTES</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</section>
<!-- About Section -->'''

html = re.sub(work_pattern, new_work, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
