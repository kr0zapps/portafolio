import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Cállate Spam Abstract Graphic
spam_graphic_old = r'<div class="mt-8 relative h-64 md:h-80 bg-\[#e2e2e2\]/50 mx-8 rounded-t-xl overflow-hidden flex items-center\njustify-center">.*?</div>'

# Fallback pattern if newlines differ
spam_graphic_old2 = r'<div class="mt-8 relative h-64 md:h-80 bg-\[#e2e2e2\]/50 mx-8 rounded-t-xl overflow-hidden flex items-center\s*justify-center">\s*<span class="material-symbols-outlined text-9xl text-\[#888888\]/20" style="font-size: 128px; line-height:\s*1;">shield</span>\s*</div>'

spam_graphic_new = '''<div class="mt-8 relative h-64 md:h-80 bg-[#e5e7eb]/50 dark:bg-[#030b14]/50 mx-8 rounded-t-xl overflow-hidden flex items-center justify-center border-t border-l border-r border-[#1a1c1c]/5 dark:border-white/5">
        <!-- Abstract Phone UI -->
        <div class="w-48 h-80 bg-white dark:bg-[#0a192f] rounded-t-[2.5rem] shadow-2xl flex flex-col items-center pt-10 relative border border-[#1a1c1c]/10 dark:border-white/10 translate-y-8 hover:-translate-y-2 transition-transform duration-500">
            <!-- Dynamic Island / Speaker -->
            <div class="absolute top-3 w-16 h-4 bg-black rounded-full"></div>
            
            <!-- Caller Avatar -->
            <div class="w-16 h-16 rounded-full bg-red-100 dark:bg-red-900/30 border border-red-500/20 flex items-center justify-center mb-4 mt-2 relative">
                <div class="absolute inset-0 rounded-full border border-red-500/50 animate-ping opacity-20"></div>
                <i data-lucide="user-x" class="text-red-600 dark:text-red-400 w-8 h-8"></i>
            </div>
            
            <!-- Caller Info Skeletons -->
            <div class="w-24 h-3 bg-gray-200 dark:bg-gray-700 rounded-full mb-2"></div>
            <div class="w-16 h-2 bg-gray-100 dark:bg-gray-800 rounded-full mb-8"></div>
            
            <!-- ML Shield Badge -->
            <div class="bg-red-50 dark:bg-red-500/10 border border-red-200 dark:border-red-500/30 px-3 py-1.5 rounded-full flex items-center gap-2 shadow-sm">
                <i data-lucide="shield-alert" class="text-red-600 dark:text-red-500 w-3 h-3"></i>
                <span class="text-red-600 dark:text-red-500 text-[10px] font-mono font-bold tracking-widest">ML BLOCKED</span>
            </div>
            
            <!-- Audio Waveform Abstract -->
            <div class="absolute bottom-6 flex items-end gap-1 opacity-40">
                <div class="w-1 h-3 bg-red-500 rounded-full"></div>
                <div class="w-1 h-6 bg-red-500 rounded-full"></div>
                <div class="w-1 h-10 bg-red-500 rounded-full"></div>
                <div class="w-1 h-5 bg-red-500 rounded-full"></div>
                <div class="w-1 h-2 bg-red-500 rounded-full"></div>
            </div>
        </div>
    </div>'''

html = re.sub(spam_graphic_old2, spam_graphic_new, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
