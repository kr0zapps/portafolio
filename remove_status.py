import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# The exact block to remove:
target_block = '''<div class="scroll-reveal" style="transition-delay: 100ms;">
                <div class="relative inline-flex mb-8 group cursor-default">
                    <!-- Animated Gradient Glow Behind -->
                    <div class="absolute -inset-0.5 bg-gradient-to-r from-[#0052FF] via-purple-500 to-[#0052FF] rounded-full blur opacity-40 group-hover:opacity-75 animate-gradient-xy transition duration-500"></div>
                    
                    <!-- Inner Pill -->
                    <div class="relative inline-flex items-center gap-3 px-6 py-2.5 rounded-full bg-white dark:bg-[#030712] border border-gray-200/50 dark:border-white/10">
                        <div class="flex items-center justify-center w-2 h-2 relative">
                            <span class="absolute w-2 h-2 bg-green-500 rounded-full animate-ping"></span>
                            <span class="relative w-1.5 h-1.5 bg-green-500 rounded-full"></span>
                        </div>
                        <span class="font-mono text-[10px] font-bold tracking-widest text-[#1a1c1c] dark:text-white uppercase">Status: <span class="text-[#0052FF] dark:text-[#4facfe]">Disponible</span></span>
                    </div>
                </div>
            </div>'''

if target_block in html:
    html = html.replace(target_block, '')
    print("Block removed successfully.")
else:
    print("Could not find exact block, attempting regex.")
    html = re.sub(r'<div class="scroll-reveal" style="transition-delay: 100ms;">.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
