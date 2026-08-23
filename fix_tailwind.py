import json
import re

# We already have the colors from the cat output, I will just dump them into CSS format.
colors = {
    "on-secondary-container": "#636262",
    "on-surface-variant": "#434656",
    "on-primary-fixed-variant": "#0038b6",
    "surface-container": "#eeeeee",
    "on-surface": "#1a1c1c",
    "surface-tint": "#004ced",
    "secondary-fixed": "#e5e2e1",
    "secondary": "#5f5e5e",
    "on-primary": "#ffffff",
    "technical-gray": "#888888",
    "surface-container-lowest": "#ffffff",
    "tertiary-fixed-dim": "#ffb4a1",
    "primary": "#003ec7",
    "surface-container-highest": "#e2e2e2",
    "electric-blue": "#0052FF",
    "primary-fixed-dim": "#b7c4ff",
    "tertiary": "#952200",
    "primary-fixed": "#dde1ff",
    "on-error-container": "#93000a",
    "canvas-white": "#FFFFFF",
    "inverse-on-surface": "#f1f1f1",
    "on-tertiary-container": "#ffddd5",
    "secondary-fixed-dim": "#c8c6c5",
    "surface-container-high": "#e8e8e8",
    "surface-variant": "#e2e2e2",
    "on-secondary": "#ffffff",
    "outline": "#737688",
    "error": "#ba1a1a",
    "tertiary-container": "#bf3003",
    "surface-container-low": "#f3f3f3",
    "on-error": "#ffffff",
    "on-primary-fixed": "#001452",
    "surface": "#f9f9f9",
    "surface-bright": "#f9f9f9",
    "inverse-primary": "#b7c4ff",
    "error-container": "#ffdad6",
    "outline-variant": "#c3c5d9",
    "secondary-container": "#e2dfde",
    "surface-dim": "#dadada",
    "on-secondary-fixed": "#1c1b1b",
    "tertiary-fixed": "#ffdbd2",
    "on-primary-container": "#dfe3ff",
    "primary-container": "#0052ff",
    "on-tertiary-fixed": "#3c0800",
    "on-tertiary": "#ffffff",
    "on-tertiary-fixed-variant": "#891e00",
    "on-background": "#1a1c1c",
    "on-secondary-fixed-variant": "#474746",
    "inverse-surface": "#2f3131",
    "background": "#f9f9f9"
}

spacing = {
    "column-gap": "32px",
    "margin-desktop": "64px",
    "section-gap": "128px",
    "margin-mobile": "20px",
    "base": "8px",
    "gutter": "24px"
}

fonts = {
    "display-xl-mobile": '"Inter", sans-serif',
    "headline-md": '"Inter", sans-serif',
    "body-lg": '"Inter", sans-serif',
    "code-mono": '"JetBrains Mono", monospace',
    "headline-lg": '"Inter", sans-serif',
    "body-md": '"Inter", sans-serif',
    "display-xl": '"Inter", sans-serif',
    "label-caps": '"JetBrains Mono", monospace'
}

css_vars = []
for k, v in colors.items():
    css_vars.append(f'  --color-{k}: {v};')

for k, v in spacing.items():
    css_vars.append(f'  --spacing-{k}: {v};')

for k, v in fonts.items():
    css_vars.append(f'  --font-{k}: {v};')

css_vars_str = "\n".join(css_vars)

# We also need to map the typography settings like font-size, line-height, letter-spacing to utilities or text-* values.
# Tailwind v4 handles this via `@theme` properties or custom utilities.
# For simplicity, we can define them as utilities in global.css.

typography_utils = """
@utility text-display-xl-mobile {
  font-size: 64px;
  line-height: 60px;
  letter-spacing: -0.04em;
  font-weight: 800;
}
@utility text-headline-md {
  font-size: 32px;
  line-height: 36px;
  letter-spacing: -0.02em;
  font-weight: 600;
}
@utility text-body-lg {
  font-size: 18px;
  line-height: 28px;
  font-weight: 400;
}
@utility text-code-mono {
  font-size: 14px;
  line-height: 20px;
  font-weight: 450;
}
@utility text-headline-lg {
  font-size: 64px;
  line-height: 64px;
  letter-spacing: -0.03em;
  font-weight: 700;
}
@utility text-body-md {
  font-size: 16px;
  line-height: 24px;
  font-weight: 400;
}
@utility text-display-xl {
  font-size: 120px;
  line-height: 110px;
  letter-spacing: -0.05em;
  font-weight: 800;
}
@utility text-label-caps {
  font-size: 12px;
  line-height: 16px;
  letter-spacing: 0.08em;
  font-weight: 600;
}
"""

with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    original_css = f.read()

# Insert the vars inside @theme
new_css = original_css.replace('@theme {', '@theme {\n' + css_vars_str + '\n  --bg-grid-pattern: linear-gradient(to right, #e2e2e2 1px, transparent 1px), linear-gradient(to bottom, #e2e2e2 1px, transparent 1px);')

new_css += typography_utils

with open('src/styles/global.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

with open('src/layouts/Layout.astro', 'r', encoding='utf-8') as f:
    layout = f.read()

# Remove the scripts
layout = re.sub(r'<script src="https://cdn\.tailwindcss\.com\?plugins=forms,container-queries"></script>', '', layout)
layout = re.sub(r'<script is:inline>\s*tailwind\.config = \{.*?\s*\}\s*</script>', '', layout, flags=re.DOTALL)

with open('src/layouts/Layout.astro', 'w', encoding='utf-8') as f:
    f.write(layout)
