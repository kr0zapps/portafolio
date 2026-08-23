import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

archive_section = '''
    <!-- Other Projects (Archive List) -->
    <div class="mt-32 w-full">
        <div class="scroll-reveal mb-12">
            <h3 class="text-3xl font-bold tracking-tight text-[#1a1c1c] dark:text-white mb-2">Otros Proyectos</h3>
            <p class="text-sm text-gray-600 dark:text-gray-400">Trabajos adicionales, integraciones y desarrollos a medida.</p>
        </div>

        <div class="w-full flex flex-col border-t border-[#1a1c1c]/10 dark:border-white/10 scroll-reveal">
            
            <!-- Row 1 -->
            <div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-[#1a1c1c]/10 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-4 px-2 cursor-default">
                <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-8 w-full md:w-2/3">
                    <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-500 w-12">2026</span>
                    <div>
                        <h4 class="text-lg font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Sistema de Eventos y Bodas</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mt-1 leading-relaxed">Plataforma integral: confirmación de asistencia (RSVP), notificaciones, contabilizador de regalos y dashboard financiero en tiempo real.</p>
                    </div>
                </div>
                <div class="flex flex-wrap gap-2 md:w-1/3 md:justify-end">
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">SUPABASE</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">POSTGRESQL</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">REACT</span>
                </div>
            </div>

            <!-- Row 2 -->
            <div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-[#1a1c1c]/10 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-4 px-2 cursor-default">
                <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-8 w-full md:w-2/3">
                    <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-500 w-12">2025</span>
                    <div>
                        <h4 class="text-lg font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Desarrollo Web a Medida</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mt-1 leading-relaxed">Creación de Landing Pages corporativas, embudos de conversión (funnels) y portafolios altamente optimizados para cualquier nicho de negocio.</p>
                    </div>
                </div>
                <div class="flex flex-wrap gap-2 md:w-1/3 md:justify-end">
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">ASTRO</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">TAILWIND</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">VERCEL</span>
                </div>
            </div>

            <!-- Row 3 -->
            <div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-[#1a1c1c]/10 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-4 px-2 cursor-default">
                <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-8 w-full md:w-2/3">
                    <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-500 w-12">2025</span>
                    <div>
                        <h4 class="text-lg font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Dashboards de Gestión</h4>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mt-1 leading-relaxed">Paneles de administración internos con gráficos de métricas complejas, autenticación segura y control de inventarios.</p>
                    </div>
                </div>
                <div class="flex flex-wrap gap-2 md:w-1/3 md:justify-end">
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">NODE.JS</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">API REST</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">JWT</span>
                </div>
            </div>

        </div>
    </div>
</section>
<!-- About Section -->
'''

html = html.replace('</section>\n<!-- About Section -->', archive_section)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
