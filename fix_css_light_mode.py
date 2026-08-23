import re

with open('src/styles/global.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix Glow effect in Light Mode (White glow on white background is invisible)
# We will use the electric blue color (0, 82, 255) for the glow in light mode to make it visible and premium
old_light_glow_before = '''/* The subtle border highlight */
.glow-card::before {
  background: radial-gradient(
    800px circle at var(--mouse-x) var(--mouse-y), 
    rgba(255, 255, 255, 0.1),
    transparent 40%
  );
  z-index: 3;
}'''

new_light_glow_before = '''/* The subtle border highlight */
.glow-card::before {
  background: radial-gradient(
    800px circle at var(--mouse-x) var(--mouse-y), 
    rgba(0, 82, 255, 0.15),
    transparent 40%
  );
  z-index: 3;
}'''

old_light_glow_overlay = '''/* The inner glow highlight */
.glow-card > .glow-overlay {
  background: radial-gradient(
    400px circle at var(--mouse-x) var(--mouse-y), 
    rgba(200, 200, 200, 0.1),
    transparent 40%
  );
  z-index: 1;
}'''

new_light_glow_overlay = '''/* The inner glow highlight */
.glow-card > .glow-overlay {
  background: radial-gradient(
    400px circle at var(--mouse-x) var(--mouse-y), 
    rgba(0, 82, 255, 0.05),
    transparent 40%
  );
  z-index: 1;
}'''

# Add gradient animation keyframes for the new badge
gradient_animation = '''
@keyframes gradient-xy {
    0%, 100% {
        background-size: 400% 400%;
        background-position: left center;
    }
    50% {
        background-size: 200% 200%;
        background-position: right center;
    }
}
.animate-gradient-xy {
    animation: gradient-xy 3s ease infinite;
}
'''

if 'rgba(255, 255, 255, 0.1)' in css:
    css = css.replace(old_light_glow_before, new_light_glow_before)
if 'rgba(200, 200, 200, 0.1)' in css:
    css = css.replace(old_light_glow_overlay, new_light_glow_overlay)
if 'gradient-xy' not in css:
    css += gradient_animation

with open('src/styles/global.css', 'w', encoding='utf-8') as f:
    f.write(css)
