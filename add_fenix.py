import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the 3rd row in the archive (Dashboards de Gestión) with Fenix Select
old_row3 = '''<!-- Row 3 -->
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
            </div>'''

new_row3 = '''<!-- Row 3 -->
            <a href="https://fenixselect.cl" target="_blank" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-[#1a1c1c]/10 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-4 px-2 cursor-pointer">
                <div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-8 w-full md:w-2/3">
                    <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-500 w-12">2026</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <h4 class="text-lg font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Fénix Select</h4>
                            <i data-lucide="arrow-up-right" class="w-4 h-4 text-gray-400 group-hover:text-[#0052FF] transition-colors"></i>
                        </div>
                        <p class="text-sm text-gray-600 dark:text-gray-400 mt-1 leading-relaxed">Frontend para e-commerce de licores premium. Arquitectura de UI con animaciones fluidas, carrito lateral dinámico y diseño de lujo.</p>
                    </div>
                </div>
                <div class="flex flex-wrap gap-2 md:w-1/3 md:justify-end">
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">HTML/CSS</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">BOOTSTRAP</span>
                    <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white bg-gray-100 dark:bg-white/10 px-2.5 py-1 rounded-sm">JS</span>
                </div>
            </a>'''

if old_row3 in html:
    html = html.replace(old_row3, new_row3)
else:
    print("Warning: old_row3 not found.")

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
