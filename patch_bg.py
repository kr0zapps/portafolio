import re

def patch_layout():
    with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    animated_bg = '''
    <div class="fixed inset-0 z-[-1] overflow-hidden bg-[#050505] pointer-events-none">
        <!-- Animated Glow Orbs -->
        <div class="absolute top-[-20%] left-[-10%] w-[50vw] h-[50vw] rounded-full bg-indigo-900/10 blur-[100px] animate-[aurora_15s_ease-in-out_infinite_alternate]"></div>
        <div class="absolute bottom-[-20%] right-[-10%] w-[60vw] h-[60vw] rounded-full bg-slate-800/20 blur-[120px] animate-[aurora_20s_ease-in-out_infinite_alternate-reverse]"></div>
        
        <!-- Drifting Grid -->
        <div class="absolute inset-[-100%] bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGNpcmNsZSBjeD0iMSIgY3k9IjEiIHI9IjEiIGZpbGw9InJnYmEoMjU1LDI1NSwyNTUsMC4wNykiLz48L3N2Zz4=')] [mask-image:linear-gradient(to_bottom,white,transparent_80%)] animate-[drift_40s_linear_infinite]"></div>
    </div>
    <style is:global>
        @keyframes aurora {
            0% { transform: translate(0, 0) scale(1); }
            50% { transform: translate(5%, 5%) scale(1.1); }
            100% { transform: translate(-5%, -5%) scale(0.9); }
        }
        @keyframes drift {
            0% { transform: translateY(0); }
            100% { transform: translateY(30px); /* Matches the SVG height to loop perfectly */ }
        }
    </style>
'''
    if 'fixed inset-0 z-[-1]' not in content:
        content = content.replace('<slot />', animated_bg + '\n\t\t<slot />')
        content = content.replace('<html lang="en" class="dark">', '<html lang="es" class="dark">')
        
    with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
        f.write(content)

def patch_index():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the case-sensitive Jonathan text
    content = re.sub(r'Jonathan S\. Vidal \(krosa\)', 'kr0zapps', content, flags=re.IGNORECASE)
    
    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    patch_layout()
    patch_index()
    print("Patched layouts and index successfully")
