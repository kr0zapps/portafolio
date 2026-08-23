import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace the ENTIRE Archive List section to fix the broken tags.
archive_start = '<!-- Archive List -->'
archive_end = '</section>'

new_archive_section = '''<!-- Archive List -->
        <div class="mt-20 w-full">
            <div class="scroll-reveal mb-8">
                <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Otros Proyectos</h3>
                <p class="text-gray-600 dark:text-gray-400">Trabajos adicionales e integraciones de ecosistemas.</p>
            </div>

            <div class="w-full flex flex-col border-t border-gray-200 dark:border-white/10 scroll-reveal">
                
                <!-- Row 1: Fénix -->
                <a href="https://fenixselect.cl" target="_blank" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.05] transition-colors gap-6 px-4 cursor-pointer">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2026</span>
                        <img src="/portafolio/fenix-official.png" alt="Fénix Select" class="hidden md:block w-32 h-20 object-cover rounded-lg border border-gray-200 dark:border-white/10 opacity-80 group-hover:opacity-100 transition-opacity">
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

                <!-- Row 2: RSVP -->
                <a href="/portafolio/rsvp-official.png" target="_blank" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.05] transition-colors gap-6 px-4 cursor-pointer">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2026</span>
                        <img src="/portafolio/rsvp-official.png" alt="Sistema RSVP" class="hidden md:block w-32 h-20 object-cover object-top rounded-lg border border-gray-200 dark:border-white/10 opacity-80 group-hover:opacity-100 transition-opacity">
                        <div>
                            <div class="flex items-center gap-2">
                                <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Sistema RSVP & Eventos</h4>
                                <i data-lucide="arrow-up-right" class="w-4 h-4 text-gray-400 group-hover:text-[#0052FF] transition-colors"></i>
                            </div>
                            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 leading-relaxed">Plataforma integral para confirmación de asistencia, contabilizador de regalos y dashboard de métricas en tiempo real respaldado por bases de datos.</p>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-2 md:w-1/4 md:justify-end shrink-0">
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">SUPABASE</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">REACT</span>
                    </div>
                </a>

                <!-- Row 3: Landing Pages -->
                <a href="#" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.05] transition-colors gap-6 px-4 cursor-pointer">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2025</span>
                        <div class="hidden md:block w-32 h-20 bg-gray-100 dark:bg-white/5 rounded-lg border border-gray-200 dark:border-white/10 flex items-center justify-center text-gray-300 dark:text-gray-700 group-hover:bg-[#0052FF]/10 group-hover:border-[#0052FF]/20 transition-colors"><i data-lucide="layout" class="w-6 h-6 group-hover:text-[#0052FF] transition-colors"></i></div>
                        <div>
                            <div class="flex items-center gap-2">
                                <h4 class="text-xl font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Desarrollo Web de Alta Conversión</h4>
                                <i data-lucide="arrow-up-right" class="w-4 h-4 text-gray-400 group-hover:text-[#0052FF] transition-colors"></i>
                            </div>
                            <p class="text-sm text-gray-600 dark:text-gray-400 mt-2 leading-relaxed">Arquitectura y despliegue de Landing Pages corporativas ultra rápidas, optimizadas para SEO técnico y embudos de venta directos.</p>
                        </div>
                    </div>
                    <div class="flex flex-wrap gap-2 md:w-1/4 md:justify-end shrink-0">
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">ASTRO</span>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/5 border border-gray-200 dark:border-white/10 px-3 py-1 rounded-full">TAILWIND</span>
                    </div>
                </a>

            </div>
        </div>
    </section>'''

# Cut and replace
start_idx = html.find(archive_start)
end_idx = html.find(archive_end)
if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_archive_section + html[end_idx:]

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
