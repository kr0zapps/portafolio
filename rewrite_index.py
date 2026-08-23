import sys

new_index = """---
import Layout from '../layouts/Layout.astro';
---

<Layout title="Jonathan Vidal - Software Engineer">
    
    <!-- Dynamic Glowing Grid Overlay -->
    <div class="fixed inset-0 pointer-events-none z-[-1]">
        <!-- Subtle grain texture -->
        <div class="absolute inset-0 opacity-[0.03] dark:opacity-[0.06] mix-blend-overlay" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.65%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E');"></div>
        <!-- ThreeJS Canvas -->
        <div id="threejs-canvas" class="absolute inset-0 opacity-40 dark:opacity-60"></div>
    </div>

    <!-- Navigation -->
    <nav class="fixed top-6 left-1/2 -translate-x-1/2 z-50 px-6 py-3 rounded-full bg-white/70 dark:bg-[#0a0a10]/70 backdrop-blur-xl border border-gray-200/50 dark:border-white/10 shadow-[0_8px_32px_rgba(0,0,0,0.04)] flex items-center gap-8 transition-all duration-500">
        <a href="#" class="font-bold tracking-widest uppercase text-xs hover:text-[#0052FF] transition-colors">kr0zapps</a>
        <div class="h-4 w-[1px] bg-gray-300 dark:bg-gray-700"></div>
        <div class="flex items-center gap-6 text-sm font-medium">
            <a href="#work" class="text-gray-600 dark:text-gray-400 hover:text-black dark:hover:text-white transition-colors">Trabajo</a>
            <a href="#stack" class="text-gray-600 dark:text-gray-400 hover:text-black dark:hover:text-white transition-colors">Ingeniería</a>
            <a href="#about" class="text-gray-600 dark:text-gray-400 hover:text-black dark:hover:text-white transition-colors">Sobre mí</a>
        </div>
        <div class="h-4 w-[1px] bg-gray-300 dark:bg-gray-700"></div>
        <!-- Theme Toggle -->
        <button id="theme-toggle" class="relative w-12 h-6 rounded-full bg-gray-200 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 focus:outline-none overflow-hidden flex items-center transition-colors">
            <div id="theme-slider" class="absolute left-1 w-4 h-4 rounded-full bg-white dark:bg-black shadow-sm flex items-center justify-center transition-transform duration-300 transform dark:translate-x-6">
                <i data-lucide="sun" class="w-2.5 h-2.5 text-orange-500 dark:opacity-0 transition-opacity absolute"></i>
                <i data-lucide="moon" class="w-2.5 h-2.5 text-blue-400 opacity-0 dark:opacity-100 transition-opacity absolute"></i>
            </div>
        </button>
    </nav>

    <!-- Hero Section -->
    <main class="relative min-h-[100svh] flex flex-col justify-center items-center px-6 pt-24 pb-12 overflow-hidden">
        <div class="w-full max-w-[90rem] mx-auto flex flex-col items-start relative z-10">
            
            <div class="scroll-reveal" style="transition-delay: 100ms;">
                <span class="inline-flex items-center gap-3 px-4 py-2 rounded-full border border-gray-200 dark:border-white/10 bg-white/50 dark:bg-white/5 backdrop-blur-md mb-8">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-green-500"></span>
                    </span>
                    <span class="font-mono text-xs font-bold tracking-widest text-gray-600 dark:text-gray-300 uppercase">Disponible para proyectos</span>
                </span>
            </div>

            <h1 class="scroll-reveal text-[clamp(4rem,10vw,12rem)] leading-[0.85] font-extrabold tracking-tighter text-[#1a1c1c] dark:text-white" style="transition-delay: 200ms;">
                INGENIERÍA<br/>
                <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#1a1c1c] to-gray-500 dark:from-white dark:to-gray-500">DE PRECISIÓN.</span>
            </h1>

            <div class="scroll-reveal mt-12 grid grid-cols-1 md:grid-cols-2 gap-12 w-full border-t border-gray-200 dark:border-white/10 pt-12" style="transition-delay: 300ms;">
                <p class="text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-xl font-medium leading-relaxed">
                    Soy Jonathan Vidal, desarrollador Full Stack especializado en construir interfaces impecables, ecosistemas backend escalables y aplicaciones nativas que redefinen la experiencia de usuario.
                </p>
                <div class="flex flex-col sm:flex-row gap-6 md:justify-end items-start">
                    <a href="#work" class="group relative px-8 py-4 bg-[#1a1c1c] dark:bg-white text-white dark:text-[#1a1c1c] rounded-full font-bold tracking-wide overflow-hidden transition-transform hover:scale-105 active:scale-95">
                        <span class="relative z-10 flex items-center gap-2">Explorar Trabajo <i data-lucide="arrow-down" class="w-4 h-4 group-hover:translate-y-1 transition-transform"></i></span>
                    </a>
                    <a href="https://github.com" target="_blank" class="group px-8 py-4 bg-white/50 dark:bg-white/5 border border-gray-200 dark:border-white/10 text-[#1a1c1c] dark:text-white rounded-full font-bold tracking-wide backdrop-blur-md hover:bg-gray-100 dark:hover:bg-white/10 transition-colors">
                        Ver GitHub
                    </a>
                </div>
            </div>
        </div>
    </main>

    <!-- Work Section -->
    <section id="work" class="px-6 py-32 w-full max-w-[90rem] mx-auto flex flex-col gap-12">
        <div class="scroll-reveal flex flex-col gap-4 mb-8">
            <h2 class="text-5xl md:text-7xl font-extrabold tracking-tighter text-[#1a1c1c] dark:text-white">Proyectos Destacados</h2>
            <p class="text-xl text-gray-600 dark:text-gray-400 max-w-2xl">Sistemas complejos destilados en interfaces precisas y rendimiento brutal.</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 w-full" id="cards-wrapper">
            
            <!-- CARD 1: FitGamer -->
            <div class="glow-card scroll-reveal group relative rounded-3xl bg-white dark:bg-[#0a0a10] border border-gray-200 dark:border-white/10 overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-700 flex flex-col min-h-[600px]">
                <div class="glow-overlay hidden dark:block"></div>
                <div class="p-10 relative z-10 flex flex-col h-full">
                    <div class="flex justify-between items-start mb-6">
                        <div>
                            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2 group-hover:translate-x-2 transition-transform duration-500">FitGamer</h3>
                            <p class="text-gray-600 dark:text-gray-400">Gamificación extrema para fitness</p>
                        </div>
                        <a href="#" class="w-12 h-12 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center border border-gray-200 dark:border-white/10 group-hover:rotate-45 group-hover:bg-[#1a1c1c] group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-all duration-500">
                            <i data-lucide="arrow-up-right" class="w-5 h-5"></i>
                        </a>
                    </div>
                    
                    <div class="flex gap-2 flex-wrap mb-10">
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Kotlin</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Compose</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">HealthConnect</span>
                    </div>

                    <div class="relative flex-grow flex items-end justify-center z-10 mt-auto">
                        <div class="w-full md:w-5/6 mx-auto rounded-t-2xl overflow-hidden border border-gray-200 dark:border-white/10 border-b-0 shadow-2xl transform translate-y-8 group-hover:translate-y-0 transition-transform duration-700 ease-out">
                            <img src="/fitgamer-official.png" alt="FitGamer App" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700" style="object-position: top;"/>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CARD 2: Cállate Spam -->
            <div class="glow-card scroll-reveal group relative rounded-3xl bg-white dark:bg-[#0a0a10] border border-gray-200 dark:border-white/10 overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-700 flex flex-col min-h-[600px]">
                <div class="glow-overlay hidden dark:block"></div>
                <div class="p-10 relative z-10 flex flex-col h-full">
                    <div class="flex justify-between items-start mb-6">
                        <div>
                            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2 group-hover:translate-x-2 transition-transform duration-500">Cállate Spam</h3>
                            <p class="text-gray-600 dark:text-gray-400">Filtro ML on-device para llamadas</p>
                        </div>
                        <a href="#" class="w-12 h-12 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center border border-gray-200 dark:border-white/10 group-hover:rotate-45 group-hover:bg-[#1a1c1c] group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-all duration-500">
                            <i data-lucide="arrow-up-right" class="w-5 h-5"></i>
                        </a>
                    </div>
                    
                    <div class="flex gap-2 flex-wrap mb-10">
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Swift</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">CoreML</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">CallKit</span>
                    </div>

                    <div class="relative flex-grow flex items-end justify-center z-10 mt-auto">
                        <div class="w-full rounded-2xl overflow-hidden border border-gray-200 dark:border-white/10 shadow-2xl transform scale-95 translate-y-4 group-hover:scale-100 group-hover:translate-y-0 transition-transform duration-700 ease-out">
                            <img src="/callate-official.png" alt="Cállate Play Store" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-opacity duration-700" style="object-position: top;"/>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CARD 3: RedNorte -->
            <div class="glow-card scroll-reveal group relative rounded-3xl bg-white dark:bg-[#0a0a10] border border-gray-200 dark:border-white/10 overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-700 flex flex-col min-h-[600px]">
                <div class="glow-overlay hidden dark:block"></div>
                <div class="p-10 relative z-10 flex flex-col h-full">
                    <div class="flex justify-between items-start mb-6">
                        <div>
                            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2 group-hover:translate-x-2 transition-transform duration-500">RedNorte</h3>
                            <p class="text-gray-600 dark:text-gray-400">Clínica Inteligente & SMS</p>
                        </div>
                        <a href="#" class="w-12 h-12 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center border border-gray-200 dark:border-white/10 group-hover:rotate-45 group-hover:bg-[#1a1c1c] group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-all duration-500">
                            <i data-lucide="arrow-up-right" class="w-5 h-5"></i>
                        </a>
                    </div>
                    
                    <div class="flex gap-2 flex-wrap mb-10">
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Node.js</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Microservicios</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">MySQL</span>
                    </div>

                    <div class="relative flex-grow flex items-center justify-center z-10 mt-auto px-4 md:px-8">
                        <!-- Custom Minimal Dashboard UI -->
                        <div class="w-full bg-gray-50 dark:bg-[#0d0d14] rounded-2xl border border-gray-200 dark:border-white/10 shadow-2xl p-4 md:p-6 transform scale-95 group-hover:scale-100 transition-transform duration-700 ease-out">
                            <div class="flex items-center justify-between border-b border-gray-200 dark:border-gray-800 pb-4 mb-4">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 rounded-full bg-[#0052FF]/10 flex items-center justify-center"><i data-lucide="calendar" class="w-5 h-5 text-[#0052FF]"></i></div>
                                    <div>
                                        <div class="h-2 w-20 bg-gray-300 dark:bg-gray-700 rounded-full mb-1"></div>
                                        <div class="h-1.5 w-12 bg-gray-200 dark:bg-gray-800 rounded-full"></div>
                                    </div>
                                </div>
                                <div class="px-3 py-1 rounded-full bg-green-500/10 border border-green-500/20 text-green-600 dark:text-green-400 text-xs font-mono font-bold flex items-center gap-2">
                                    <span class="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span> ONLINE
                                </div>
                            </div>
                            <div class="flex flex-col gap-3">
                                <div class="w-full h-12 rounded-xl bg-gray-100 dark:bg-white/5 flex items-center justify-between px-4">
                                    <div class="h-2 w-32 bg-gray-300 dark:bg-gray-600 rounded-full"></div>
                                    <i data-lucide="check" class="w-4 h-4 text-gray-400"></i>
                                </div>
                                <div class="w-full h-12 rounded-xl bg-[#0052FF]/5 border border-[#0052FF]/20 flex items-center justify-between px-4 relative overflow-hidden group/item">
                                    <div class="absolute inset-0 bg-[#0052FF]/10 translate-x-[-100%] group-hover/item:translate-x-0 transition-transform duration-500"></div>
                                    <div class="h-2 w-24 bg-[#0052FF]/50 rounded-full relative z-10"></div>
                                    <div class="flex items-center gap-2 relative z-10">
                                        <span class="text-[10px] font-bold text-[#0052FF] uppercase tracking-wider">SMS Enviado</span>
                                        <i data-lucide="message-square" class="w-3.5 h-3.5 text-[#0052FF]"></i>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CARD 4: CuentaApp -->
            <div class="glow-card scroll-reveal group relative rounded-3xl bg-white dark:bg-[#0a0a10] border border-gray-200 dark:border-white/10 overflow-hidden shadow-sm hover:shadow-2xl transition-all duration-700 flex flex-col min-h-[600px]">
                <div class="glow-overlay hidden dark:block"></div>
                <div class="p-10 relative z-10 flex flex-col h-full">
                    <div class="flex justify-between items-start mb-6">
                        <div>
                            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2 group-hover:translate-x-2 transition-transform duration-500">CuentaApp</h3>
                            <p class="text-gray-600 dark:text-gray-400">Control Financiero & Gráficos</p>
                        </div>
                        <a href="#" class="w-12 h-12 rounded-full bg-gray-100 dark:bg-white/5 flex items-center justify-center border border-gray-200 dark:border-white/10 group-hover:rotate-45 group-hover:bg-[#1a1c1c] group-hover:text-white dark:group-hover:bg-white dark:group-hover:text-black transition-all duration-500">
                            <i data-lucide="arrow-up-right" class="w-5 h-5"></i>
                        </a>
                    </div>
                    
                    <div class="flex gap-2 flex-wrap mb-10">
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">React</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Chart.js</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest uppercase bg-gray-100 dark:bg-white/5 px-3 py-1.5 rounded-full border border-gray-200/50 dark:border-white/5">Firebase</span>
                    </div>

                    <div class="relative flex-grow flex items-center justify-center z-10 mt-auto px-4 md:px-12">
                        <!-- Custom Interactive Chart UI -->
                        <div class="w-full h-48 flex items-end justify-between gap-2 md:gap-4 relative group/chart">
                            <!-- Horizontal Guide lines -->
                            <div class="absolute inset-0 flex flex-col justify-between opacity-10 pointer-events-none border-b border-gray-300 dark:border-white/50">
                                <div class="w-full h-[1px] bg-gray-400 dark:bg-white"></div>
                                <div class="w-full h-[1px] bg-gray-400 dark:bg-white"></div>
                                <div class="w-full h-[1px] bg-gray-400 dark:bg-white"></div>
                            </div>
                            
                            <!-- Bars -->
                            <div class="w-full bg-green-500/10 rounded-t-lg h-[40%] relative group-hover/chart:h-[50%] transition-all duration-700 ease-out"><div class="absolute bottom-0 w-full rounded-t-lg bg-green-500/80 h-[20%] group-hover/chart:h-[100%] transition-all duration-700"></div></div>
                            <div class="w-full bg-red-500/10 rounded-t-lg h-[25%] relative group-hover/chart:h-[30%] transition-all duration-700 ease-out delay-75"><div class="absolute bottom-0 w-full rounded-t-lg bg-red-500/80 h-[100%] transition-all duration-700"></div></div>
                            <div class="w-full bg-green-500/10 rounded-t-lg h-[70%] relative group-hover/chart:h-[80%] transition-all duration-700 ease-out delay-100"><div class="absolute bottom-0 w-full rounded-t-lg bg-green-500/80 h-[40%] group-hover/chart:h-[100%] transition-all duration-700"></div></div>
                            <div class="w-full bg-red-500/10 rounded-t-lg h-[45%] relative group-hover/chart:h-[40%] transition-all duration-700 ease-out delay-150"><div class="absolute bottom-0 w-full rounded-t-lg bg-red-500/80 h-[100%] transition-all duration-700"></div></div>
                            <div class="w-full bg-green-500/10 rounded-t-lg h-[90%] relative group-hover/chart:h-[100%] transition-all duration-700 ease-out delay-200"><div class="absolute bottom-0 w-full rounded-t-lg bg-green-500/80 h-[60%] group-hover/chart:h-[100%] transition-all duration-700"></div></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <!-- Archive List -->
        <div class="mt-20 w-full">
            <div class="scroll-reveal mb-8">
                <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Otros Proyectos</h3>
                <p class="text-gray-600 dark:text-gray-400">Trabajos adicionales e integraciones de ecosistemas.</p>
            </div>

            <div class="w-full flex flex-col border-t border-gray-200 dark:border-white/10 scroll-reveal">
                
                <!-- Row 1: Fénix -->
                <a href="https://fenixselect.cl" target="_blank" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-pointer">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2026</span>
                        <img src="/fenix-official.png" alt="Fénix Select" class="hidden md:block w-32 h-20 object-cover rounded-lg border border-gray-200 dark:border-white/10 opacity-70 group-hover:opacity-100 transition-opacity">
                        <div>
                            <div class="flex items-center gap-2">
                                <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Fénix Select (E-Commerce Premium)</h4>
                                <i data-lucide="arrow-up-right" class="w-4 h-4 text-gray-400 group-hover:text-[#0052FF] transition-colors"></i>
                            </div>
                            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 leading-relaxed">Frontend para e-commerce de licores premium. Arquitectura de UI con animaciones fluidas, carrito dinámico (Offcanvas) y diseño brutalista de lujo.</p>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-2 md:w-1/4 md:justify-end shrink-0">
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">HTML/CSS</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">JS</span>
                    </div>
                </a>

                <!-- Row 2 -->
                <div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-default">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2026</span>
                        <div class="hidden md:block w-32 h-20 bg-gray-100 dark:bg-white/5 rounded-lg border border-gray-200 dark:border-white/10 flex items-center justify-center text-gray-300 dark:text-gray-700"><i data-lucide="users" class="w-6 h-6"></i></div>
                        <div>
                            <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Sistema RSVP & Eventos</h4>
                            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 leading-relaxed">Plataforma integral para confirmación de asistencia, contabilizador de regalos y dashboard de métricas en tiempo real respaldado por bases de datos.</p>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-2 md:w-1/4 md:justify-end shrink-0">
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">SUPABASE</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">REACT</span>
                    </div>
                </div>

                <!-- Row 3 -->
                <div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-default">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2025</span>
                        <div class="hidden md:block w-32 h-20 bg-gray-100 dark:bg-white/5 rounded-lg border border-gray-200 dark:border-white/10 flex items-center justify-center text-gray-300 dark:text-gray-700"><i data-lucide="layout" class="w-6 h-6"></i></div>
                        <div>
                            <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Desarrollo Web de Alta Conversión</h4>
                            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 leading-relaxed">Arquitectura y despliegue de Landing Pages corporativas ultra rápidas, optimizadas para SEO técnico y embudos de venta directos.</p>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-2 md:w-1/4 md:justify-end shrink-0">
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">ASTRO</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">TAILWIND</span>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- Tech Stack (Bento Grid) -->
    <section id="stack" class="px-6 py-32 w-full max-w-[90rem] mx-auto border-t border-gray-200 dark:border-white/10">
        <div class="scroll-reveal flex flex-col gap-4 mb-16">
            <h2 class="text-5xl md:text-7xl font-extrabold tracking-tighter text-[#1a1c1c] dark:text-white">Arquitectura & Stack</h2>
            <p class="text-xl text-gray-600 dark:text-gray-400 max-w-2xl">Dominio absoluto del ciclo de vida del software.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[300px]">
            
            <!-- Box 1: Frontend (Spans 2 columns on desktop) -->
            <div class="scroll-reveal md:col-span-2 md:row-span-2 rounded-3xl bg-gray-50 dark:bg-[#0a0a10] border border-gray-200 dark:border-white/10 p-10 flex flex-col justify-between overflow-hidden relative group">
                <div class="absolute inset-0 bg-gradient-to-br from-white/50 to-transparent dark:from-white/[0.03] dark:to-transparent pointer-events-none"></div>
                <div class="relative z-10">
                    <div class="w-12 h-12 rounded-2xl bg-white dark:bg-black border border-gray-200 dark:border-white/10 flex items-center justify-center mb-6 shadow-sm"><i data-lucide="layout-template" class="w-6 h-6 text-[#1a1c1c] dark:text-white"></i></div>
                    <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Ingeniería Frontend</h3>
                    <p class="text-gray-600 dark:text-gray-400 max-w-sm">Interfaces reactivas construidas con precisión quirúrgica. Renderizado híbrido, animaciones fluidas a 60fps y estado inmutable.</p>
                </div>
                
                <div class="relative z-10 flex gap-4 mt-8 flex-wrap">
                    <div class="px-4 py-3 bg-white dark:bg-black rounded-xl border border-gray-200 dark:border-white/10 flex items-center gap-3 shadow-sm group-hover:-translate-y-1 transition-transform duration-300">
                        <i class="devicon-react-original colored text-2xl"></i><span class="font-mono text-xs font-bold">React</span>
                    </div>
                    <div class="px-4 py-3 bg-white dark:bg-black rounded-xl border border-gray-200 dark:border-white/10 flex items-center gap-3 shadow-sm group-hover:-translate-y-1 transition-transform duration-300 delay-75">
                        <i class="devicon-tailwindcss-plain colored text-2xl"></i><span class="font-mono text-xs font-bold">Tailwind</span>
                    </div>
                    <div class="px-4 py-3 bg-white dark:bg-black rounded-xl border border-gray-200 dark:border-white/10 flex items-center gap-3 shadow-sm group-hover:-translate-y-1 transition-transform duration-300 delay-150">
                        <i class="devicon-astro-plain text-[#1a1c1c] dark:text-white text-2xl"></i><span class="font-mono text-xs font-bold">Astro</span>
                    </div>
                </div>

                <!-- Abstract UI Code Block -->
                <div class="absolute -right-12 -bottom-12 w-96 h-80 bg-white dark:bg-black border border-gray-200 dark:border-white/10 rounded-2xl shadow-2xl p-6 opacity-50 dark:opacity-80 group-hover:scale-105 group-hover:-translate-x-4 transition-transform duration-700 ease-out hidden md:block rotate-[-5deg]">
                    <div class="flex gap-2 mb-4">
                        <div class="w-3 h-3 rounded-full bg-red-400"></div><div class="w-3 h-3 rounded-full bg-yellow-400"></div><div class="w-3 h-3 rounded-full bg-green-400"></div>
                    </div>
                    <div class="font-mono text-xs text-gray-500 dark:text-gray-400 flex flex-col gap-2">
                        <div><span class="text-blue-500">export const</span> <span class="text-yellow-500">Component</span> = () => {</div>
                        <div class="pl-4">const [state, setState] = useState(0);</div>
                        <div class="pl-4 mt-2">return (</div>
                        <div class="pl-8 text-green-500"><span class="text-gray-500">&lt;</span>div className<span class="text-gray-500">=</span>"grid brutalist"<span class="text-gray-500">&gt;</span></div>
                        <div class="pl-12">Performance Absoluta</div>
                        <div class="pl-8 text-green-500"><span class="text-gray-500">&lt;/</span>div<span class="text-gray-500">&gt;</span></div>
                        <div class="pl-4">)</div>
                        <div>}</div>
                    </div>
                </div>
            </div>

            <!-- Box 2: Backend -->
            <div class="scroll-reveal rounded-3xl bg-[#1a1c1c] border border-gray-800 p-10 flex flex-col relative overflow-hidden group">
                <div class="relative z-10 flex flex-col h-full">
                    <div class="w-12 h-12 rounded-2xl bg-black border border-gray-800 flex items-center justify-center mb-6"><i data-lucide="server" class="w-6 h-6 text-green-400"></i></div>
                    <h3 class="text-2xl font-bold tracking-tight text-white mb-2">Backend & Datos</h3>
                    <p class="text-gray-400 text-sm">Microservicios, APIs robustas y bases de datos relacionales en la nube.</p>
                    
                    <!-- Terminal effect -->
                    <div class="mt-auto pt-8 font-mono text-[10px] text-green-500 opacity-80 group-hover:opacity-100 transition-opacity flex flex-col gap-1">
                        <div>> node server.js --cluster</div>
                        <div>[OK] API Gateway listening on 8080</div>
                        <div>> SELECT * FROM scale;</div>
                        <div class="flex items-center gap-1"><span class="w-2 h-4 bg-green-500 animate-pulse"></span></div>
                    </div>
                </div>
                
                <div class="absolute top-6 right-6 flex gap-2">
                    <i class="devicon-nodejs-plain colored text-2xl opacity-40 group-hover:opacity-100 transition-opacity"></i>
                    <i class="devicon-mysql-plain text-white opacity-40 group-hover:opacity-100 transition-opacity"></i>
                </div>
            </div>

            <!-- Box 3: Native Apps -->
            <div class="scroll-reveal rounded-3xl bg-gray-50 dark:bg-[#0a0a10] border border-gray-200 dark:border-white/10 p-10 flex flex-col justify-between relative overflow-hidden group">
                <div class="relative z-10">
                    <div class="w-12 h-12 rounded-2xl bg-white dark:bg-black border border-gray-200 dark:border-white/10 flex items-center justify-center mb-6"><i data-lucide="smartphone" class="w-6 h-6 text-[#1a1c1c] dark:text-white"></i></div>
                    <h3 class="text-2xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Nativo & Móvil</h3>
                    <p class="text-gray-600 dark:text-gray-400 text-sm">Ejecución a nivel de sistema. Swift, Kotlin y machine learning on-device.</p>
                </div>

                <div class="absolute -bottom-8 -right-8 w-40 h-64 border-4 border-gray-200 dark:border-[#1a1c1c] rounded-[2rem] bg-white dark:bg-black transform rotate-12 group-hover:rotate-6 group-hover:-translate-y-4 transition-transform duration-700 ease-out shadow-2xl flex flex-col">
                    <div class="w-12 h-1 bg-gray-200 dark:bg-[#1a1c1c] rounded-full mx-auto mt-2"></div>
                    <div class="flex-grow flex items-center justify-center">
                        <i class="devicon-swift-plain text-[#1a1c1c] dark:text-white text-4xl opacity-20 group-hover:opacity-100 transition-opacity"></i>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Footer -->
    <footer class="w-full bg-white dark:bg-[#030712] border-t border-gray-200 dark:border-white/10 px-6 py-12 mt-16">
        <div class="max-w-[90rem] mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
            <div class="font-mono text-xs font-bold tracking-[0.1em] text-[#1a1c1c] dark:text-white uppercase flex flex-col md:flex-row gap-2 md:gap-8">
                <span>© 2026 KR0ZAPPS.</span>
                <span class="text-gray-400 dark:text-gray-600">SISTEMAS DE ALTO RENDIMIENTO.</span>
            </div>
            <div class="flex items-center gap-8 font-mono text-[10px] font-bold uppercase tracking-widest text-gray-500 dark:text-gray-400">
                <a class="hover:text-[#0052FF] transition-colors" href="https://github.com" target="_blank">Github</a>
                <a class="hover:text-[#0052FF] transition-colors" href="#">LinkedIn</a>
                <a class="hover:text-[#0052FF] transition-colors" href="mailto:hola@kr0zapps.com">Email</a>
            </div>
        </div>
    </footer>

    <!-- Interactive Logic -->
    <script is:inline>
        // Theme Toggle
        const themeToggleBtn = document.getElementById('theme-toggle');
        const themeSlider = document.getElementById('theme-slider');
        
        themeToggleBtn.addEventListener('click', () => {
            const isDark = document.documentElement.classList.contains('dark');
            if (isDark) {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('theme', 'light');
            } else {
                document.documentElement.classList.add('dark');
                localStorage.setItem('theme', 'dark');
            }
        });

        // Glow effect for cards
        document.getElementById("cards-wrapper").onmousemove = e => {
            for(const card of document.getElementsByClassName("glow-card")) {
                const rect = card.getBoundingClientRect(),
                      x = e.clientX - rect.left,
                      y = e.clientY - rect.top;

                card.style.setProperty("--mouse-x", `${x}px`);
                card.style.setProperty("--mouse-y", `${y}px`);
            }
        }

        // Scroll Reveal
        document.addEventListener("DOMContentLoaded", () => {
            const reveals = document.querySelectorAll(".scroll-reveal");
            const revealOnScroll = () => {
                const windowHeight = window.innerHeight;
                reveals.forEach(el => {
                    const elementTop = el.getBoundingClientRect().top;
                    if (elementTop < windowHeight - 50) {
                        el.classList.add("visible");
                    }
                });
            };
            window.addEventListener("scroll", revealOnScroll);
            revealOnScroll(); // Trigger immediately
        });
    </script>

    <!-- ThreeJS Interactive Background -->
    <script is:inline>
        (function() {
            const container = document.getElementById('threejs-canvas');
            if(!container) return;

            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: "high-performance" });
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2)); // Limit pixel ratio for performance
            renderer.setSize(window.innerWidth, window.innerHeight);
            container.appendChild(renderer.domElement);

            // Particles Geometry
            const particlesCount = 800;
            const posArray = new Float32Array(particlesCount * 3);
            
            for(let i=0; i < particlesCount; i++) {
                // Spread particles across a wide area
                posArray[i*3] = (Math.random() - 0.5) * 15; // x
                posArray[i*3+1] = (Math.random() - 0.5) * 15; // y
                posArray[i*3+2] = (Math.random() - 0.5) * 5; // z
            }

            const geometry = new THREE.BufferGeometry();
            geometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

            const material = new THREE.PointsMaterial({
                size: 0.02,
                color: 0x666666,
                transparent: true,
                opacity: 0.6,
                blending: THREE.AdditiveBlending
            });

            const particlesMesh = new THREE.Points(geometry, material);
            scene.add(particlesMesh);

            camera.position.z = 4;

            // Mouse interaction
            let mouseX = 0;
            let mouseY = 0;
            let targetX = 0;
            let targetY = 0;

            const windowHalfX = window.innerWidth / 2;
            const windowHalfY = window.innerHeight / 2;

            document.addEventListener('mousemove', (event) => {
                mouseX = (event.clientX - windowHalfX) * 0.001;
                mouseY = (event.clientY - windowHalfY) * 0.001;
            });

            // Handle theme change to update particle colors
            const updateParticleColor = () => {
                const isDark = document.documentElement.classList.contains('dark');
                material.color.setHex(isDark ? 0xffffff : 0x000000);
                material.opacity = isDark ? 0.3 : 0.1;
            };
            
            // Watch for theme changes via mutation observer
            const observer = new MutationObserver(updateParticleColor);
            observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
            updateParticleColor(); // Init

            const clock = new THREE.Clock();

            function animate() {
                requestAnimationFrame(animate);
                const elapsedTime = clock.getElapsedTime();

                // Smooth mouse following
                targetX = mouseX * 1.5;
                targetY = mouseY * 1.5;
                
                particlesMesh.rotation.y += 0.05 * (targetX - particlesMesh.rotation.y);
                particlesMesh.rotation.x += 0.05 * (targetY - particlesMesh.rotation.x);
                
                // Idle gentle rotation
                particlesMesh.rotation.y += 0.001;
                particlesMesh.position.y = Math.sin(elapsedTime * 0.5) * 0.2;

                renderer.render(scene, camera);
            }

            animate();

            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        })();
    </script>
</Layout>
"""

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(new_index)
