import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update FitGamer Image
# Find the exact img tag for FitGamer
fitgamer_img_old = r'<img src="/fitgamer-mockup.png" alt="FitGamer App Interface" class="w-full h-auto object-cover opacity-90 grayscale group-hover:grayscale-0 transition-all duration-500" onerror="this.src=\'https://images.unsplash.com/photo-1616469829581-73993eb86b02\?q=80&w=1000&auto=format&fit=crop\';"/>'
fitgamer_img_new = r'<img src="/fitgamer-official.png" alt="FitGamer App Interface" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-all duration-500 rounded-xl" style="object-position: top;"/>'
html = re.sub(fitgamer_img_old, fitgamer_img_new, html)

# 2. Update Cállate Spam to use the official Play Store image instead of the abstract UI
callate_ui_old_start = r'<div class="w-56 h-72 bg-gray-50 dark:bg-\[#0a1220\] rounded-t-\[2.5rem\] shadow-lg flex flex-col items-center pt-8 relative border border-\[#1a1c1c\]/10 dark:border-white/10">'
# We will replace the entire container for the image in Cállate Spam
callate_container_pattern = r'<div class="relative px-8 flex items-center justify-center h-64 z-10">.*?</div>\s*</div>\s*<div class="w-full bg-\[#f9f9f9\]'

callate_container_new = '''<div class="relative px-8 pb-8 flex items-center justify-center z-10">
                <div class="w-full rounded-xl overflow-hidden border border-[#1a1c1c]/10 dark:border-white/10 bg-gray-100 dark:bg-[#0a1220]">
                    <img src="/callate-official.png" alt="Cállate Play Store" class="w-full h-auto object-cover opacity-90 group-hover:opacity-100 transition-all duration-500" style="object-position: top;"/>
                </div>
            </div>
            <div class="w-full bg-[#f9f9f9]'''
html = re.sub(callate_container_pattern, callate_container_new, html, flags=re.DOTALL)

# 3. Add Fenix Select thumbnail to the archive list
fenix_row_old = r'''<div class="flex flex-col md:flex-row md:items-center gap-2 md:gap-8 w-full md:w-2/3">
                    <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-500 w-12">2026</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <h4 class="text-lg font-bold text-\[#1a1c1c\] dark:text-white group-hover:text-\[#0052FF\] transition-colors">Fénix Select</h4>'''

fenix_row_new = '''<div class="flex flex-col md:flex-row md:items-center gap-4 md:gap-8 w-full md:w-2/3">
                    <span class="font-mono text-xs font-bold text-gray-400 dark:text-gray-500 w-12 shrink-0">2026</span>
                    <img src="/fenix-official.png" alt="Fénix Select" class="hidden md:block w-24 h-16 object-cover rounded-md border border-[#1a1c1c]/10 dark:border-white/10 opacity-80 group-hover:opacity-100 transition-opacity">
                    <div>
                        <div class="flex items-center gap-2">
                            <h4 class="text-lg font-bold text-[#1a1c1c] dark:text-white group-hover:text-[#0052FF] transition-colors">Fénix Select</h4>'''

html = re.sub(fenix_row_old, fenix_row_new, html)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
