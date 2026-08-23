import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the project section adapt to dark mode nicely and look more professional
# Fix FitGamer tags
html = html.replace('>Kotlin</span>', '><span class="material-symbols-outlined text-[10px] mr-1">smartphone</span>Kotlin</span>')
html = html.replace('>Compose</span>', '><span class="material-symbols-outlined text-[10px] mr-1">design_services</span>Compose</span>')
html = html.replace('>HealthConnect</span>', '><span class="material-symbols-outlined text-[10px] mr-1">monitor_heart</span>HealthConnect</span>')

# Fix Cállate Spam tags
html = html.replace('>Swift</span>', '><span class="material-symbols-outlined text-[10px] mr-1">code</span>Swift</span>')
html = html.replace('>CoreML</span>', '><span class="material-symbols-outlined text-[10px] mr-1">memory</span>CoreML</span>')
html = html.replace('>CallKit</span>', '><span class="material-symbols-outlined text-[10px] mr-1">call</span>CallKit</span>')

# Make the Tier 2 projects look more professional (like the reference HTML)
tier2_pattern = r'<a class="scroll-reveal group block p-6 rounded-2xl border border-\[#1a1c1c\]/10 bg-gradient-to-br from-surface-container to-surface-container-low hover:border-\[#003ec7\]/30 transition-all duration-300 transform hover:-translate-y-1".*?</a>'

new_cuentaapp = '''<a class="scroll-reveal group block p-8 border border-[#1a1c1c]/10 dark:border-white/10 bg-transparent hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300" href="#">
    <div class="flex justify-between items-start mb-6">
        <h4 class="font-bold text-[#1a1c1c] dark:text-white font-mono uppercase tracking-[0.2em] text-xs transition-colors">CuentaApp</h4>
        <span class="material-symbols-outlined text-gray-500 group-hover:text-[#003ec7] dark:group-hover:text-white transition-colors text-sm">arrow_outward</span>
    </div>
    <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed transition-colors">Gestión financiera y división de gastos automatizada.</p>
</a>'''

new_fenix = '''<a class="scroll-reveal group block p-8 border border-[#1a1c1c]/10 dark:border-white/10 bg-transparent hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300" href="https://fenixselect.cl" target="_blank">
    <div class="flex justify-between items-start mb-6">
        <h4 class="font-bold text-[#1a1c1c] dark:text-white font-mono uppercase tracking-[0.2em] text-xs transition-colors">Fenix Select</h4>
        <span class="material-symbols-outlined text-gray-500 group-hover:text-[#003ec7] dark:group-hover:text-white transition-colors text-sm">arrow_outward</span>
    </div>
    <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed transition-colors">Plataforma e-commerce B2B de alto rendimiento.</p>
</a>'''

new_diseno = '''<a class="scroll-reveal group block p-8 border border-[#1a1c1c]/10 dark:border-white/10 bg-transparent hover:bg-[#1a1c1c]/5 dark:hover:bg-white/5 transition-all duration-300" href="#">
    <div class="flex justify-between items-start mb-6">
        <h4 class="font-bold text-[#1a1c1c] dark:text-white font-mono uppercase tracking-[0.2em] text-xs transition-colors">Diseño de Interfaces</h4>
        <span class="material-symbols-outlined text-gray-500 group-hover:text-[#003ec7] dark:group-hover:text-white transition-colors text-sm">arrow_outward</span>
    </div>
    <p class="text-sm text-gray-600 dark:text-gray-400 leading-relaxed transition-colors">Sistemas de diseño escalables y componentes UI.</p>
</a>'''

html = re.sub(tier2_pattern, new_cuentaapp, html, count=1, flags=re.DOTALL)
html = re.sub(tier2_pattern, new_fenix, html, count=1, flags=re.DOTALL)
html = re.sub(tier2_pattern, new_diseno, html, count=1, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
