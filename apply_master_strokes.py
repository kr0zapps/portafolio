import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update theme toggle icons to Lucide
html = html.replace(
    '<span class="material-symbols-outlined absolute left-1.5 text-[14px] text-gray-500 dark:text-gray-400 z-10 pointer-events-none">dark_mode</span>',
    '<i data-lucide="moon" class="absolute left-1.5 w-3.5 h-3.5 text-gray-500 dark:text-gray-400 z-10 pointer-events-none"></i>'
)
html = html.replace(
    '<span class="material-symbols-outlined absolute right-1.5 text-[14px] text-yellow-500 z-10 pointer-events-none">light_mode</span>',
    '<i data-lucide="sun" class="absolute right-1.5 w-3.5 h-3.5 text-yellow-500 z-10 pointer-events-none"></i>'
)

# 2. Update marquee icons
marquee_replacements = {
    '<span class="material-symbols-outlined text-sm">terminal</span>': '<i data-lucide="terminal" class="w-4 h-4"></i>',
    '<span class="material-symbols-outlined text-sm">integration_instructions</span>': '<i data-lucide="code-2" class="w-4 h-4"></i>',
    '<span class="material-symbols-outlined text-sm">dataset</span>': '<i data-lucide="database" class="w-4 h-4"></i>',
    '<span class="material-symbols-outlined text-sm">memory</span>': '<i data-lucide="cpu" class="w-4 h-4"></i>',
    '<span class="material-symbols-outlined text-sm">cloud</span>': '<i data-lucide="cloud" class="w-4 h-4"></i>'
}
for old, new in marquee_replacements.items():
    html = html.replace(old, new)

# 3. Update FitGamer tags
html = html.replace('<span class="material-symbols-outlined text-[10px] mr-1">smartphone</span>', '<i data-lucide="smartphone" class="w-3 h-3 mr-1"></i>')
html = html.replace('<span class="material-symbols-outlined text-[10px] mr-1">design_services</span>', '<i data-lucide="pen-tool" class="w-3 h-3 mr-1"></i>')
html = html.replace('<span class="material-symbols-outlined text-[10px] mr-1">monitor_heart</span>', '<i data-lucide="activity" class="w-3 h-3 mr-1"></i>')

# 4. Update Cállate Spam tags
html = html.replace('<span class="material-symbols-outlined text-[10px] mr-1">code</span>', '<i data-lucide="code" class="w-3 h-3 mr-1"></i>')
# memory already replaced if exact string matched, but let's do it specifically:
html = html.replace('<span class="material-symbols-outlined text-[10px] mr-1">memory</span>', '<i data-lucide="cpu" class="w-3 h-3 mr-1"></i>')
html = html.replace('<span class="material-symbols-outlined text-[10px] mr-1">call</span>', '<i data-lucide="phone-call" class="w-3 h-3 mr-1"></i>')

# 5. Update Tier 2 Project Links
html = html.replace('<span class="material-symbols-outlined opacity-0 group-hover:opacity-100 transition-opacity transform group-hover:translate-x-1 group-hover:-translate-y-1 text-gray-400">arrow_outward</span>', '<i data-lucide="arrow-up-right" class="w-5 h-5 opacity-0 group-hover:opacity-100 transition-all transform group-hover:translate-x-1 group-hover:-translate-y-1 text-gray-400"></i>')

# 6. Update About Me icons
html = html.replace('<span class="material-symbols-outlined mr-2 text-sm">download</span>', '<i data-lucide="download" class="w-4 h-4 mr-2"></i>')
html = html.replace('<span class="material-symbols-outlined text-lg">link</span>', '<i data-lucide="external-link" class="w-5 h-5"></i>')

# 7. Update Cállate Spam Abstract Graphic
spam_graphic_old = r'<div class="mt-8 relative h-64 md:h-80 bg-\[#f9f9f9\]-container-high/50 mx-8 rounded-t-xl overflow-hidden flex items-center justify-center">.*?</div>'
spam_graphic_new = '''<div class="mt-8 relative h-64 md:h-80 bg-[#e5e7eb] dark:bg-[#030b14] mx-8 rounded-t-xl overflow-hidden flex items-center justify-center border-t border-l border-r border-[#1a1c1c]/5 dark:border-white/5">
        <!-- Abstract Phone UI -->
        <div class="w-48 h-80 bg-white dark:bg-[#0a192f] rounded-t-[2.5rem] shadow-2xl flex flex-col items-center pt-10 relative border border-[#1a1c1c]/10 dark:border-white/10 translate-y-8 group-hover:translate-y-4 transition-transform duration-500">
            <!-- Dynamic Island / Speaker -->
            <div class="absolute top-3 w-16 h-4 bg-black rounded-full"></div>
            
            <!-- Caller Avatar -->
            <div class="w-20 h-20 rounded-full bg-red-100 dark:bg-red-900/30 border border-red-500/20 flex items-center justify-center mb-4 mt-4 relative">
                <div class="absolute inset-0 rounded-full border border-red-500/50 animate-ping opacity-20"></div>
                <i data-lucide="user-x" class="text-red-600 dark:text-red-400 w-10 h-10"></i>
            </div>
            
            <!-- Caller Info Skeletons -->
            <div class="w-24 h-3 bg-gray-200 dark:bg-gray-700 rounded-full mb-2"></div>
            <div class="w-16 h-2 bg-gray-100 dark:bg-gray-800 rounded-full mb-8"></div>
            
            <!-- ML Shield Badge -->
            <div class="bg-red-50 dark:bg-red-500/10 border border-red-200 dark:border-red-500/30 px-4 py-2 rounded-full flex items-center gap-2 shadow-sm">
                <i data-lucide="shield-alert" class="text-red-600 dark:text-red-500 w-4 h-4"></i>
                <span class="text-red-600 dark:text-red-500 text-[10px] font-mono font-bold tracking-widest">SPAM DETECTED</span>
            </div>
            
            <!-- Audio Waveform Abstract -->
            <div class="absolute bottom-6 flex items-end gap-1.5 opacity-40">
                <div class="w-1.5 h-4 bg-red-500 rounded-full"></div>
                <div class="w-1.5 h-8 bg-red-500 rounded-full"></div>
                <div class="w-1.5 h-12 bg-red-500 rounded-full"></div>
                <div class="w-1.5 h-6 bg-red-500 rounded-full"></div>
                <div class="w-1.5 h-3 bg-red-500 rounded-full"></div>
            </div>
        </div>
    </div>'''
html = re.sub(spam_graphic_old, spam_graphic_new, html, flags=re.DOTALL)


# 8. Refine Core Stack
stack_old = r'<div class="flex flex-wrap justify-center gap-4 md:gap-6">.*?</div>\s*</section>'

stack_new = '''<div class="flex flex-wrap justify-center gap-4 md:gap-6 max-w-5xl mx-auto">
        <!-- AWS -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-amazonwebservices-plain-wordmark dark:devicon-amazonwebservices-plain-wordmark text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">AWS</span>
        </div>

        <!-- Docker -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-docker-plain text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">DOCKER</span>
        </div>

        <!-- Kotlin -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-kotlin-plain text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">KOTLIN</span>
        </div>

        <!-- PHP -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-php-plain text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">PHP</span>
        </div>
        
        <!-- JavaScript -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-javascript-plain text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">JAVASCRIPT</span>
        </div>

        <!-- React -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-react-original text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">REACT</span>
        </div>

        <!-- MySQL -->
        <div class="group flex flex-col items-center justify-center gap-4 p-6 md:p-8 rounded-2xl transition-all duration-500 cursor-default w-32 md:w-40 hover:bg-[#f3f3f3] dark:hover:bg-white/5">
            <i class="devicon-mysql-plain text-[#1a1c1c]/50 dark:text-white/40 text-5xl md:text-6xl group-hover:colored transition-all duration-500 group-hover:scale-110"></i>
            <span class="font-bold text-[#1a1c1c]/50 dark:text-gray-500 font-mono text-xs tracking-widest group-hover:text-[#1a1c1c] dark:group-hover:text-white transition-colors duration-500">MYSQL</span>
        </div>
    </div>
</section>'''

html = re.sub(stack_old, stack_new, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
