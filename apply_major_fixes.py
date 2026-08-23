import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Navbar: Group Logo and Links closer, add Theme Toggle
nav_pattern = r'<nav.*?</nav>'

new_nav = '''<nav class="fixed top-0 w-full z-50 bg-[#f9f9f9]/80 dark:bg-[#051424]/90 backdrop-blur-md border-b border-[#1a1c1c]/10 dark:border-white/10 transition-colors duration-300">
  <div class="flex justify-between items-center w-full px-6 md:px-16 py-4 max-w-7xl mx-auto">
    <!-- Left side: Logo + Links -->
    <div class="flex items-center gap-12">
        <div class="text-3xl font-bold tracking-tighter text-[#1a1c1c] dark:text-white transition-colors">
            kr0zapps
        </div>
        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-6">
            <a class="font-mono text-xs font-bold tracking-[0.08em] text-[#003ec7] dark:text-white border-b-2 border-[#003ec7] dark:border-white pb-1 uppercase transition-colors" href="#work">Trabajo</a>
            <a class="font-mono text-xs font-bold tracking-[0.08em] text-gray-500 dark:text-gray-400 hover:text-[#003ec7] dark:hover:text-white transition-colors duration-200 uppercase" href="#expertise">Especialidad</a>
            <a class="font-mono text-xs font-bold tracking-[0.08em] text-gray-500 dark:text-gray-400 hover:text-[#003ec7] dark:hover:text-white transition-colors duration-200 uppercase" href="#">Sobre mí</a>
        </div>
    </div>
    
    <!-- Right side: Theme Toggle -->
    <button id="theme-toggle" class="p-2 rounded-full hover:bg-black/5 dark:hover:bg-white/10 transition-colors" aria-label="Toggle Dark Mode">
        <!-- Sun icon (shows in dark mode) -->
        <span class="material-symbols-outlined text-white hidden dark:block">light_mode</span>
        <!-- Moon icon (shows in light mode) -->
        <span class="material-symbols-outlined text-[#1a1c1c] block dark:hidden">dark_mode</span>
    </button>
  </div>
</nav>'''

html = re.sub(nav_pattern, new_nav, html, flags=re.DOTALL)

# 2. Update Hero Visual Column to ThreeJS container
visual_pattern = r'<!-- Visual Column \(User Portrait Placeholder\).*?</div>\n</div>'
new_visual = '''<!-- Visual Column (3D Animation) -->
<div class="col-span-1 lg:col-span-5 relative flex justify-center lg:justify-end items-center w-full h-[400px] md:h-[600px] z-20">
    <div id="threejs-container" class="w-full h-full cursor-grab active:cursor-grabbing"></div>
</div>'''
html = re.sub(visual_pattern, new_visual, html, flags=re.DOTALL)

# 3. Update Hero Section to toggle backgrounds properly for dark/light mode
# Currently it is hardcoded to bg-[#051424]. Let's make it responsive to dark mode: `bg-[#f9f9f9] dark:bg-[#051424]`
hero_section_pattern = r'<section class="relative min-h-\[95vh\] flex flex-col justify-center px-5 md:px-16 py-32 overflow-hidden scroll-reveal bg-\[#051424\]">'
new_hero_section = '<section class="relative min-h-[95vh] flex flex-col justify-center px-5 md:px-16 py-32 overflow-hidden scroll-reveal bg-transparent transition-colors duration-500">'
html = html.replace(hero_section_pattern, new_hero_section)

# Update Hero text for light/dark mode
html = html.replace('text-white tracking-tighter', 'text-[#1a1c1c] dark:text-white tracking-tighter transition-colors')
html = html.replace('text-gray-400">Construyo', 'text-gray-500 dark:text-gray-400 transition-colors">Construyo')
html = html.replace('text-gray-400">de alto rendimiento', 'text-gray-500 dark:text-gray-400 transition-colors">de alto rendimiento')
html = html.replace('text-white">nativos y web', 'text-[#003ec7] dark:text-white transition-colors">nativos y web')
html = html.replace('text-gray-300 font-normal', 'text-gray-600 dark:text-gray-300 font-normal transition-colors')
html = html.replace('border-white/20 pl-4', 'border-[#1a1c1c]/20 dark:border-white/20 pl-4 transition-colors')

# 4. Make Marquee more visible
marquee_pattern = r'<div class="absolute bottom-0 left-0 w-full border-t border-b border-white/5 bg-\[#051424\] py-4 marquee-container z-20">'
new_marquee = '<div class="absolute bottom-0 left-0 w-full border-t border-b border-[#1a1c1c]/10 dark:border-white/10 bg-[#f3f3f3] dark:bg-[#030b14] py-6 marquee-container z-40 shadow-xl transition-colors duration-500">'
html = html.replace(marquee_pattern, new_marquee)
# Enlarge marquee text slightly and fix dark mode text
html = html.replace('text-sm font-medium text-gray-500', 'text-base font-bold text-[#1a1c1c]/70 dark:text-gray-400')

# 5. Add Scripts (Theme Toggle Logic, WebGL Shader, ThreeJS)
scripts = '''
<script is:inline>
    // Theme Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    themeToggleBtn.addEventListener('click', () => {
        const isDark = document.documentElement.classList.contains('dark');
        if (isDark) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        }
    });

    // WebGL Shader Background Logic
    const canvas = document.getElementById('glcanvas');
    if (canvas) {
        const gl = canvas.getContext('webgl');
        if (gl) {
            const vertexShaderSource = `
                attribute vec2 a_position;
                varying vec2 v_texCoord;
                void main() {
                    gl_Position = vec4(a_position, 0.0, 1.0);
                    v_texCoord = a_position * 0.5 + 0.5;
                }
            `;
            
            const fragmentShaderSource = `
precision highp float;
varying vec2 v_texCoord;
uniform float u_time;
uniform vec2 u_resolution;

float noise(vec2 p) {
    return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453);
}

void main() {
    vec2 uv = v_texCoord;
    float n = noise(uv + u_time * 0.05);
    float grain = mix(0.98, 1.0, n);
    
    // Check if body has dark class (hacky way in shader: pass uniform if needed, but we can just use CSS to mix blend mode or opacity)
    // We will just draw a clean technical grain. The CSS background of sections will overlay it.
    vec3 color = vec3(0.95, 0.95, 0.95); 
    float dist = distance(uv, vec2(0.5));
    color *= mix(1.0, 0.90, dist);
    
    gl_FragColor = vec4(color * grain, 1.0);
}
`;

            const vertexShader = gl.createShader(gl.VERTEX_SHADER);
            gl.shaderSource(vertexShader, vertexShaderSource);
            gl.compileShader(vertexShader);

            const fragmentShader = gl.createShader(gl.FRAGMENT_SHADER);
            gl.shaderSource(fragmentShader, fragmentShaderSource);
            gl.compileShader(fragmentShader);

            const program = gl.createProgram();
            gl.attachShader(program, vertexShader);
            gl.attachShader(program, fragmentShader);
            gl.linkProgram(program);
            gl.useProgram(program);

            const positionBuffer = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
            const positions = [
                -1.0, -1.0,  1.0, -1.0, -1.0,  1.0,
                -1.0,  1.0,  1.0, -1.0,  1.0,  1.0,
            ];
            gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);

            const positionLocation = gl.getAttribLocation(program, "a_position");
            gl.enableVertexAttribArray(positionLocation);
            gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

            const timeLocation = gl.getUniformLocation(program, "u_time");
            const resolutionLocation = gl.getUniformLocation(program, "u_resolution");

            function renderShader(time) {
                time *= 0.001; 
                if (canvas.width !== window.innerWidth || canvas.height !== window.innerHeight) {
                    canvas.width = window.innerWidth;
                    canvas.height = window.innerHeight;
                    gl.viewport(0, 0, canvas.width, canvas.height);
                }
                gl.uniform1f(timeLocation, time);
                gl.uniform2f(resolutionLocation, canvas.width, canvas.height);
                gl.drawArrays(gl.TRIANGLES, 0, 6);
                requestAnimationFrame(renderShader);
            }
            requestAnimationFrame(renderShader);
        }
    }

    // ThreeJS Logic
    (function() {
      const container = document.getElementById('threejs-container'); 
      if(!container) return;
      
      const scene = new THREE.Scene();
      const width = container.clientWidth || window.innerWidth;
      const height = container.clientHeight || window.innerHeight;
      const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
      renderer.setPixelRatio(window.devicePixelRatio);
      renderer.setSize(width, height);
      container.appendChild(renderer.domElement);

      const geometry = new THREE.IcosahedronGeometry(2.5, 2);
      const material = new THREE.MeshPhongMaterial({
        color: 0x0052FF,
        wireframe: true,
        transparent: true,
        opacity: 0.4,
        emissive: 0x0052FF,
        emissiveIntensity: 0.6
      });
      
      const mesh = new THREE.Mesh(geometry, material);
      scene.add(mesh);

      const particlesCount = 300;
      const posArray = new Float32Array(particlesCount * 3);
      for (let i = 0; i < particlesCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 12;
      }
      const particlesGeometry = new THREE.BufferGeometry();
      particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
      const particlesMaterial = new THREE.PointsMaterial({
        size: 0.04,
        color: 0x0052FF,
        transparent: true,
        opacity: 0.8
      });
      const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
      scene.add(particlesMesh);

      const light = new THREE.DirectionalLight(0xffffff, 1);
      light.position.set(1, 1, 1).normalize();
      scene.add(light);
      scene.add(new THREE.AmbientLight(0x404040));

      camera.position.z = 6;

      let mouseX = 0, mouseY = 0;
      window.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect();
        mouseX = ((e.clientX - rect.left) - rect.width / 2) / 100;
        mouseY = ((e.clientY - rect.top) - rect.height / 2) / 100;
      });

      function animate() {
        requestAnimationFrame(animate);
        mesh.rotation.y += 0.005;
        mesh.rotation.x += 0.002;
        
        mesh.position.x += (mouseX - mesh.position.x) * 0.05;
        mesh.position.y += (-mouseY - mesh.position.y) * 0.05;
        
        particlesMesh.rotation.y -= 0.001;
        
        renderer.render(scene, camera);
      }

      window.addEventListener('resize', () => {
        const w = container.clientWidth;
        const h = container.clientHeight;
        camera.aspect = w / h;
        camera.updateProjectionMatrix();
        renderer.setSize(w, h);
      });

      animate();
    })();
</script>
</Layout>'''
html = html.replace('</Layout>', scripts)

# Let's ensure the body background and text classes handle dark mode properly inside `Layout.astro`, but here we can add classes if needed. 
# `Layout.astro` body has: class="bg-[#f9f9f9] text-[#1a1c1c] font-sans overflow-x-hidden antialiased"
# We should update `Layout.astro` to add `dark:bg-[#051424] dark:text-white transition-colors duration-500`

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
