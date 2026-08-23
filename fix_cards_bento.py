import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. FIX CARDS IMAGES LAYOUT (FitGamer and Cállate Spam)
# Replace FitGamer Image Block
old_fitgamer_img = r'<div class="relative flex-grow flex items-end justify-center z-10 mt-6 pt-4 h-\[300px\] overflow-hidden">.*?</div>\s*</div>'
new_fitgamer_img = '''<div class="relative flex-grow w-full mt-8 flex justify-center items-start overflow-hidden px-4 md:px-8">
                        <img src="/portafolio/fitgamer-official.png" alt="FitGamer App" class="w-[85%] sm:w-[70%] h-auto rounded-t-3xl shadow-[0_-10px_40px_rgba(0,0,0,0.15)] group-hover:-translate-y-3 transition-transform duration-700 ease-out" />
                    </div>'''
html = re.sub(old_fitgamer_img, new_fitgamer_img, html, flags=re.DOTALL)

# Replace Cállate Spam Image Block
old_callate_img = r'<div class="relative flex-grow flex items-center justify-center z-10 mt-6">.*?</div>\s*</div>'
new_callate_img = '''<div class="relative flex-grow w-full mt-8 flex justify-center items-center px-4 md:px-8 pb-8">
                        <img src="/portafolio/callate-official.png" alt="Cállate Play Store" class="w-full h-auto rounded-xl shadow-2xl group-hover:scale-105 group-hover:-translate-y-2 transition-all duration-700 ease-out ring-1 ring-gray-200 dark:ring-white/10" />
                    </div>'''
html = re.sub(old_callate_img, new_callate_img, html, flags=re.DOTALL)

# 2. FIX ARCHIVE ROWS CLICKABLE
# RSVP Row is currently a <div class="group flex flex-col...
html = html.replace('<div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-default">', 
                    '<a href="/portafolio/rsvp-official.png" target="_blank" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.05] transition-colors gap-6 px-4 cursor-pointer">')
# Close the </a> for RSVP (it was a </div>)
html = re.sub(r'(Sistema RSVP & Eventos.*?</div>\s*</div>)\s*</div>', r'\1</a>', html, flags=re.DOTALL)

# Landing Pages Row is currently a <div
html = html.replace('''<div class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.02] transition-colors gap-6 px-4 cursor-default">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2025</span>
                        <div class="hidden md:block w-32 h-20 bg-gray-100 dark:bg-white/5 rounded-lg border border-gray-200 dark:border-white/10 flex items-center justify-center text-gray-300 dark:text-gray-700"><i data-lucide="layout" class="w-6 h-6"></i></div>''', 
                    '''<a href="#" class="group flex flex-col md:flex-row md:items-center justify-between py-6 border-b border-gray-200 dark:border-white/10 hover:bg-gray-50 dark:hover:bg-white/[0.05] transition-colors gap-6 px-4 cursor-pointer">
                    <div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-3/4">
                        <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-600 w-12 shrink-0">2025</span>
                        <div class="hidden md:block w-32 h-20 bg-gray-100 dark:bg-white/5 rounded-lg border border-gray-200 dark:border-white/10 flex items-center justify-center text-gray-300 dark:text-gray-700 group-hover:bg-[#0052FF]/10 transition-colors"><i data-lucide="layout" class="w-6 h-6 group-hover:text-[#0052FF]"></i></div>''')
html = re.sub(r'(Desarrollo Web de Alta Conversión.*?</div>\s*</div>)\s*</div>', r'\1</a>', html, flags=re.DOTALL)


# 3. FIX BENTO GRID FRONTEND TITLE/DESC AND ESCAPING
html = html.replace('Ingeniería Frontend', 'Arquitectura UI & Sistemas Core')
html = html.replace('Interfaces reactivas construidas con precisión quirúrgica. Renderizado híbrido, animaciones fluidas a 60fps y estado inmutable.', 'Desarrollo de e-commerce premium, dashboards analíticos complejos y sistemas RSVP. Experto en control de estado global, integraciones en tiempo real y diseño pixel-perfect de alta conversión.')

# Fix the &#123; showing up as text. Use Astro's standard {'{'} syntax to escape braces in JSX/Astro!
# The code currently has: Component = () =&gt; &amp;#123; (Wait, I used &amp;#123;)
# Let's clean the mock code block entirely to make sure it's perfect.
old_mock_code = r'<div class="font-mono text-xs text-gray-500 dark:text-gray-400 flex flex-col gap-2">.*?</div>\s*</div>\s*</div>'
new_mock_code = '''<div class="font-mono text-xs text-gray-500 dark:text-gray-400 flex flex-col gap-2">
                        <div><span class="text-blue-500">export const</span> <span class="text-yellow-500">Component</span> = () =&gt; {'{'}</div>
                        <div class="pl-4">const [state, setState] = useState(0);</div>
                        <div class="pl-4 mt-2">return (</div>
                        <div class="pl-8 text-green-500"><span class="text-gray-500">&lt;</span>div className<span class="text-gray-500">=</span>"grid brutalist"<span class="text-gray-500">&gt;</span></div>
                        <div class="pl-12 text-gray-800 dark:text-gray-200 font-bold">Arquitectura de Precisión</div>
                        <div class="pl-8 text-green-500"><span class="text-gray-500">&lt;/</span>div<span class="text-gray-500">&gt;</span></div>
                        <div class="pl-4">)</div>
                        <div>{'}'}</div>
                    </div>
                </div>
            </div>'''
html = re.sub(old_mock_code, new_mock_code, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
