import re
import sys

def main():
    with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update branding
    content = content.replace('JONATHAN S. VIDAL (KROSA)', 'KR0ZAPPS')
    content = content.replace('DEV_PORTFOLIO', 'kr0zapps')

    # 2. Add IDs for navigation
    content = content.replace('<section class="mb-32">', '<section id="sobre-mi" class="mb-32">')
    content = content.replace('<section>', '<section id="proyectos">')
    
    # Let's add ID for stack to the grid if possible, or just the section
    
    # 3. Add background glowing orb
    orb_html = '''
  <main class="flex-grow px-margin-md py-margin-lg max-w-container-max mx-auto w-full relative overflow-hidden">
    <!-- Ambient Background Orb -->
    <div class="absolute top-[-20%] left-1/2 -translate-x-1/2 w-[60vw] h-[600px] bg-gradient-to-b from-[#1a1a2e] to-transparent rounded-full blur-[120px] opacity-40 -z-10 pointer-events-none mix-blend-screen animate-pulse" style="animation-duration: 8s;"></div>
'''
    content = content.replace('<main class="flex-grow px-margin-md py-margin-lg max-w-container-max mx-auto w-full">', orb_html)

    # 4. Add entrance animation (Staggered fade up)
    style_block = '''
<style>
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
  }
  
  /* Apply animation to cards/groups */
  .group, .bento-grid > div, .bento-grid > a {
    animation: fadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    opacity: 0;
  }
  
  /* Staggering the grid children */
  .bento-grid > :nth-child(1) { animation-delay: 0.05s; }
  .bento-grid > :nth-child(2) { animation-delay: 0.15s; }
  .bento-grid > :nth-child(3) { animation-delay: 0.25s; }
  .bento-grid > :nth-child(4) { animation-delay: 0.35s; }
  .bento-grid > :nth-child(5) { animation-delay: 0.45s; }
  .bento-grid > :nth-child(6) { animation-delay: 0.55s; }
  .bento-grid > :nth-child(7) { animation-delay: 0.65s; }
  
  /* Make the background image of FitGamer pop more on hover */
  .group:hover .bg-\\[url\\(.*?\\)\\] {
    filter: grayscale(0%) contrast(1.15) brightness(1) !important;
  }
</style>
'''
    if '<style>' not in content:
        content = content.replace('</Layout>', style_block + '\n</Layout>')

    with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched index.astro!")

if __name__ == '__main__':
    main()
