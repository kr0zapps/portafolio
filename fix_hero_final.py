import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the "Disponible" Pill
pill_pattern = r'<div class="inline-flex items-center gap-3 px-5 py-2 rounded-full border border-white/10 bg-white/5 backdrop-blur-md w-fit mb-8 shadow-lg">.*?</div>'
html = re.sub(pill_pattern, '', html, flags=re.DOTALL)

# 2. Re-establish the Hero structure (without the curve, without badges)
# We will just replace the entire Visual Column and SVG wave.

# Let's find the entire <section ... id="hero" or similar>... wait, it doesn't have an ID.
# It starts at `<section class="relative min-h-[95vh]` and ends before `<!-- Projects Section -->`
hero_pattern = r'<!-- Hero Section -->.*?<!-- Projects Section -->'
def generate_new_hero():
    return '''<!-- Hero Section -->
<section class="relative min-h-[95vh] flex flex-col justify-center px-5 md:px-16 py-32 overflow-hidden scroll-reveal bg-[#051424]">
<div class="absolute inset-0 bg-grid-pattern grid-bg opacity-40 z-0"></div>
<div class="grid grid-cols-1 lg:grid-cols-12 gap-12 relative z-10 w-full max-w-7xl mx-auto items-center pb-24">
<!-- Text Column -->
<div class="col-span-1 lg:col-span-7 flex flex-col gap-8">
<h1 class="text-6xl md:text-[100px] lg:text-[120px] font-extrabold leading-[0.9] tracking-tighter text-white">
<span class="font-light text-gray-400">Construyo sistemas</span> <br/>
<span class="font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-[#4facfe] to-[#00f2fe]">nativos y web</span> <br/>
<span class="font-light text-gray-400">de alto rendimiento</span>
</h1>
<p class="text-lg text-gray-300 font-normal max-w-lg border-l border-white/20 pl-4 py-1">
                        Ingeniería de software con precisión suiza. Diseñado para escalar, construido para dominar el mercado.
                    </p>
<div class="pt-4 flex items-center gap-4">
<button class="group bg-[#0052FF] text-[#ffffff] font-mono text-xs font-bold tracking-widest px-8 py-4 rounded-full uppercase hover:bg-[#003ec7] transition-all duration-300 flex items-center gap-3 shadow-[0_4px_14px_0_rgba(0,82,255,0.39)] hover:shadow-[0_6px_20px_rgba(0,82,255,0.23)] hover:-translate-y-0.5">
                            Ver proyectos <span class="material-symbols-outlined text-base group-hover:translate-y-1 transition-transform duration-300">arrow_downward</span>
</button>
</div>
</div>
<!-- Visual Column (Code Snippet instead of AI image) -->
<div class="col-span-1 lg:col-span-5 relative flex justify-center lg:justify-end perspective-1000 w-full max-w-lg mx-auto lg:max-w-none">
<!-- Gallery Shadow for 3D feel -->
<div class="absolute inset-0 bg-black/10 blur-[80px] rounded-full scale-75 translate-y-12 z-0"></div>
<!-- Tilt Container -->
<div class="relative z-10 w-full tilt-card cursor-pointer" id="tilt-container">
<div class="relative w-full rounded-2xl border border-white/10 bg-[#0a0a0a] overflow-hidden shadow-2xl font-mono text-xs sm:text-sm text-gray-300 leading-relaxed">
    <div class="flex items-center gap-2 px-4 py-3 border-b border-white/5 bg-[#051424]">
        <div class="w-3 h-3 rounded-full bg-[#ff5f56]"></div>
        <div class="w-3 h-3 rounded-full bg-[#ffbd2e]"></div>
        <div class="w-3 h-3 rounded-full bg-[#27c93f]"></div>
        <span class="ml-2 text-white/40 text-[10px] tracking-wider uppercase">core_engine.ts</span>
    </div>
    <div class="p-6 flex flex-col gap-1 overflow-hidden opacity-90">
        <p><span class="text-[#c586c0]">import</span> { <span class="text-[#4fc1ff]">SystemCore</span> } <span class="text-[#c586c0]">from</span> <span class="text-[#ce9178]">'@kr0zapps/engine'</span>;</p>
        <br/>
        <p><span class="text-[#c586c0]">export</span> <span class="text-[#569cd6]">class</span> <span class="text-[#4ec9b0]">PerformanceCore</span> {</p>
        <p class="pl-4"><span class="text-[#c586c0]">private</span> <span class="text-[#9cdcfe]">engine</span> = <span class="text-[#569cd6]">new</span> <span class="text-[#4ec9b0]">SystemCore</span>();</p>
        <br/>
        <p class="pl-4"><span class="text-[#c586c0]">public</span> <span class="text-[#569cd6]">async</span> <span class="text-[#dcdcaa]">boot</span>(): <span class="text-[#4ec9b0]">Promise</span>&lt;<span class="text-[#4ec9b0]">void</span>&gt; {</p>
        <p class="pl-8"><span class="text-[#c586c0]">await</span> <span class="text-[#9cdcfe]">this</span>.<span class="text-[#9cdcfe]">engine</span>.<span class="text-[#dcdcaa]">initialize</span>({</p>
        <p class="pl-12"><span class="text-[#9cdcfe]">architecture</span>: <span class="text-[#ce9178]">'native-first'</span>,</p>
        <p class="pl-12"><span class="text-[#9cdcfe]">latency</span>: <span class="text-[#b5cea8]">0.01</span></p>
        <p class="pl-8">});</p>
        <p class="pl-8"><span class="text-[#4fc1ff]">console</span>.<span class="text-[#dcdcaa]">log</span>(<span class="text-[#ce9178]">'System deployed. 🚀'</span>);</p>
        <p class="pl-4">}</p>
        <p>}</p>
    </div>
</div>
</div>
</div>
</div>
<!-- Marquee Ticker -->
<div class="absolute bottom-0 left-0 w-full border-t border-b border-white/5 bg-[#051424] py-4 marquee-container z-20">
<div class="flex whitespace-nowrap animate-marquee w-fit">
<div class="flex items-center gap-12 px-6">
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">terminal</span> TypeScript</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">integration_instructions</span> React Native</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">dataset</span> Node.js</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">memory</span> WebGL</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">cloud</span> AWS</span>
</div>
<div class="flex items-center gap-12 px-6">
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">terminal</span> TypeScript</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">integration_instructions</span> React Native</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">dataset</span> Node.js</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">memory</span> WebGL</span>
<span class="font-mono text-sm font-medium text-gray-500 uppercase flex items-center gap-2"><span class="material-symbols-outlined text-sm">cloud</span> AWS</span>
</div>
</div>
</div>
</section>
<!-- Projects Section -->'''

html = re.sub(hero_pattern, generate_new_hero(), html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
