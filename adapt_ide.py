import re

def adapt_to_astro():
    with open(r'C:\Users\krosa\.gemini\antigravity\brain\bcf03b51-6e3f-449c-8208-4f0888e10dfe\ide_screen.html', 'r', encoding='utf-8') as f:
        html = f.read()

    tw_config_match = re.search(r'<script id="tailwind-config">(.*?)</script>', html, re.DOTALL)
    tw_config = tw_config_match.group(1) if tw_config_match else ""

    styles_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    styles = styles_match.group(1) if styles_match else ""

    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    body = body_match.group(1) if body_match else ""

    body = body.replace('kr0zapps Portfolio — Proyectos & Stack IDE', 'kr0zapps')
    body = body.replace('© 2024 KR0ZAPPS. ENGINEERED FOR PRECISION.', '© 2026 KR0ZAPPS. INGENIERÍA DE PRECISIÓN.')
    body = body.replace('Found the 3D Interaction', '¡Encontraste la interacción 3D!')
    body = body.replace('ACHIEVEMENT UNLOCKED', 'LOGRO DESBLOQUEADO')
    
    # Also replace any href="#" to valid section tags if we had any
    
    layout_astro = f"""---
import '../styles/global.css';

interface Props {{
	title: string;
	description?: string;
}}

const {{ title, description = "kr0zapps - Construyo sistemas nativos y web de alto rendimiento" }} = Astro.props;
---

<!doctype html>
<html lang="es" class="scroll-smooth">
	<head>
		<meta charset="UTF-8" />
		<meta name="description" content={{description}} />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="generator" content={{Astro.generator}} />
		
		<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
		<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
		<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
        <script is:inline>
            {tw_config}
        </script>
	</head>
	<body class="bg-[#f9f9f9] text-[#1a1c1c] font-sans overflow-x-hidden antialiased">
		<slot />
	</body>
</html>
"""

    with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
        f.write(layout_astro)

    global_css = f"""@import "tailwindcss";

@theme {{
  --font-sans: "Inter", "system-ui", "sans-serif";
  --font-mono: "JetBrains Mono", "monospace";
}}

{styles}
"""
    with open('src/styles/global.css', 'w', encoding='utf-8') as f:
        f.write(global_css)

    index_astro = f"""---
import Layout from '../layouts/Layout.astro';
---

<Layout title="kr0zapps | Software Engineer">
  {body}
</Layout>
"""
    index_astro = index_astro.replace('<script>', '<script is:inline>')
    
    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(index_astro)

if __name__ == '__main__':
    adapt_to_astro()
