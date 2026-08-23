import re

with open('src/pages/index.astro', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Marquee Container and Text
marquee_container_pattern = r'<div class="absolute bottom-0 left-0 w-full border-t border-b border-white/5 bg-\[#051424\] py-4 marquee-container \s*z-20">'
new_marquee_container = '<div class="absolute bottom-0 left-0 w-full border-t border-b border-[#1a1c1c]/10 dark:border-white/10 bg-white dark:bg-[#030b14] py-6 marquee-container z-40 shadow-xl transition-colors duration-500">'

html = re.sub(marquee_container_pattern, new_marquee_container, html, flags=re.DOTALL)

# Also fix the text inside the marquee
html = html.replace('text-base font-bold text-[#1a1c1c]/70 dark:text-gray-400', 'text-base font-bold text-gray-500 dark:text-gray-300')
html = html.replace('text-sm font-medium text-gray-500', 'text-base font-bold text-gray-500 dark:text-gray-300') # just in case old pattern was there

# 2. Fix ThreeJS Logic (Static position, Spherical particles)
threejs_old_logic_pattern = r'const particlesCount = 300;.*?animate\(\);\n    \}\)\(\);'

new_threejs_logic = '''const particlesCount = 300;
      const posArray = new Float32Array(particlesCount * 3);
      for (let i = 0; i < particlesCount; i++) {
        // Generate points in a sphere instead of a cube
        const radius = 3 + Math.random() * 6; // Spread between 3 and 9
        const theta = Math.random() * 2 * Math.PI;
        const phi = Math.acos((Math.random() * 2) - 1);
        posArray[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
        posArray[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
        posArray[i * 3 + 2] = radius * Math.cos(phi);
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

      camera.position.z = 7; // Moved back slightly to fit the particles

      function animate() {
        requestAnimationFrame(animate);
        // Static rotation, no mouse tracking
        mesh.rotation.y += 0.003;
        mesh.rotation.x += 0.001;
        
        particlesMesh.rotation.y -= 0.001;
        particlesMesh.rotation.x -= 0.0005;
        
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
    })();'''

html = re.sub(threejs_old_logic_pattern, new_threejs_logic, html, flags=re.DOTALL)

with open('src/pages/index.astro', 'w', encoding='utf-8') as f:
    f.write(html)
