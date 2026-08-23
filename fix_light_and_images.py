import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Image paths to include /portafolio/ since that's the base path the server uses
html = html.replace('src="/fitgamer-official.png"', 'src="/portafolio/fitgamer-official.png"')
html = html.replace('src="/callate-official.png"', 'src="/portafolio/callate-official.png"')
html = html.replace('src="/fenix-official.png"', 'src="/portafolio/fenix-official.png"')

# 2. Fix Three.js blending for light mode
old_three_theme = '''const updateParticleColor = () => {
                const isDark = document.documentElement.classList.contains('dark');
                // In dark mode: white particles, 0.3 opacity.
                // In light mode: electric blue particles, 0.5 opacity for a highly visible cool animation.
                material.color.setHex(isDark ? 0xffffff : 0x0052FF);
                material.opacity = isDark ? 0.3 : 0.5;
            };'''

new_three_theme = '''const updateParticleColor = () => {
                const isDark = document.documentElement.classList.contains('dark');
                // Fix for light mode: AdditiveBlending makes colors disappear on white backgrounds.
                // We switch to NormalBlending in light mode, and Additive in dark mode.
                material.blending = isDark ? THREE.AdditiveBlending : THREE.NormalBlending;
                // Use stark blue for light mode, white for dark mode
                material.color.setHex(isDark ? 0xffffff : 0x0052FF);
                // Boost opacity heavily in light mode to make it super visible
                material.opacity = isDark ? 0.4 : 0.8;
                // Make particles slightly bigger in light mode so they stand out more against white
                material.size = isDark ? 0.02 : 0.035;
            };'''

if old_three_theme in html:
    html = html.replace(old_three_theme, new_three_theme)
else:
    print("WARNING: Could not find ThreeJS theme logic.")

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
