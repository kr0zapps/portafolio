# Especificación Técnica (SPEC.md) - Portafolio Web Personal

## 1. Visión General del Proyecto
Portafolio web personal estático de alto rendimiento, moderno y minimalista, diseñado para destacar proyectos reales en producción (móvil, web y herramientas de software) desarrollados por un desarrollador chileno autodidacta.

- **Objetivo Principal**: Mostrar habilidades técnicas, capacidad de resolución de problemas y experiencia práctica para reclutadores, clientes freelance y la comunidad tecnológica.
- **Plataforma de Despliegue**: GitHub Pages (Static Site Generation - SSG).
- **Stack Base**: [Astro](https://astro.build/) + [Tailwind CSS](https://tailwindcss.com/).

---

## 2. Perfil y Propuesta de Valor
- **Identidad**: Desarrollador de Software Autodidacta (Chile 🇨🇱).
- **Enfoque**: Desarrollo orientado a producto, aplicaciones móviles en producción, aplicaciones web responsivas y sistemas de gestión eficientes.
- **Narrativa clave**: De la curiosidad y autoaprendizaje a la creación y publicación de aplicaciones reales en Google Play y plataformas web para clientes.

---

## 3. Catálogo de Proyectos a Destacar

| # | Proyecto | Tipo | Plataforma / Estado | Tecnologías Clave | Aspectos Destacados |
|---|---|---|---|---|---|
| 1 | **FitGamer** | App Móvil | Google Play (Activa) | Mobile (React Native / Flutter / Android), UI/UX | Gamificación aplicada al fitness y seguimiento de hábitos deportivos. |
| 2 | **Cállate Spam** | App Móvil (Legado) | Google Play | Android / Native Call APIs, BroadcastReceivers | Intercepción y filtrado inteligente de llamadas no deseadas/spam telefónico. |
| 3 | **CuentaApp** | App / Web | Producción / Demo | Frontend/Backend, Base de Datos, Charts | Gestión y control financiero personal/empresarial con métricas y reportes. |
| 4 | **Webs Freelance** (fenixselect.cl, RedNorte) | Web Solutions | Producción / Clientes | Web Standards, Performance, SEO, Responsive UI | Soluciones corporativas y comerciales reales orientadas a conversión y presencia digital. |
| 5 | **Catálogo UI/UX Minipyme** | Web / Design System | Producción / Showcase | Tailwind CSS, Component Architecture | Sistema de catálogo y experiencia de usuario optimizada para pequeños negocios. |

---

## 4. Arquitectura de Información y Secciones

El portafolio se estructurará como una **Single Page Application (SPA) con navegación por anclas suaves (Smooth Scroll)** y compatibilidad total con GitHub Pages:

1. **Header / Navbar**:
   - Logo / Monograma personal.
   - Navegación rápida: `Sobre mí`, `Proyectos`, `Habilidades`, `Contacto`.
   - Botón directo para descargar / ver CV o enlace a GitHub/LinkedIn.
2. **Hero Section**:
   - Saludo y presentación de impacto: Desarrollador de Software Autodidacta.
   - Badges de estatus (ej. *"Disponible para nuevos proyectos / oportunidades"*).
   - Botones de llamada a la acción (CTA): `Ver Proyectos` y `Contactar`.
   - Micro-interacciones o píldoras tecnológicas principales.
3. **Featured Projects (Proyectos Destacados)**:
   - Filtros por categoría (`Todos`, `Mobile`, `Web`, `Fintech & Apps`).
   - Cards interactivas con:
     - Capturas / mockups visuales o badges de plataforma.
     - Indicador de estado (Google Play, En Producción, Legado, Código Abierto).
     - Tags de tecnologías usadas.
     - Enlaces a Google Play, demo en vivo o repositorio si corresponde.
4. **About Me & Skills (Sobre Mí & Stack Tecnológico)**:
   - Breve historia del camino autodidacta, disciplina y resolución de problemas.
   - Grid de Habilidades categorizadas:
     - **Mobile Development**: Android, Kotlin/React Native/Flutter, Google Play Console.
     - **Frontend & Web**: HTML5/CSS3, JavaScript/TypeScript, Astro, React, Tailwind CSS.
     - **Backend & Data**: APIs REST, Node.js, SQL/NoSQL, Firebase/Supabase.
     - **Herramientas & Metodologías**: Git/GitHub, SDD, UI/UX Design, Figma.
5. **Freelance & Trayectoria**:
   - Mención de trabajos freelance y casos de éxito de clientes reales (Fenix Select, RedNorte, Pymes).
6. **Contact & Socials (Contacto)**:
   - Enlaces directos a GitHub, LinkedIn, Correo electrónico y WhatsApp.
   - Mensaje de cierre invitando a conversar sobre proyectos o vacantes.
7. **Footer**:
   - Copyright, año actual dinámico, mención al stack (Hecho con Astro + Tailwind CSS) y enlace al código fuente.

---

## 5. Sistema de Diseño (Generado con Stitch MCP: Cybernetic Minimalist)

Diseño **Cybernetic Minimalist** de ultra-alta fidelidad, combinando minimalismo moderno, profundidad atmosférica y glassmorphism:

- **Fondo Base (Background / Canvas)**: `#090d16` y `#0f131c` (Deep Dark Slate).
- **Superficies & Cards**: `#181b25` y `#1c1f29` con `backdrop-blur-md`, bordes ultra-delgados de 1px en gradiente (`#38bdf8` a `#6366f1` al 30% de opacidad) y hover reactivo que ilumina el borde a Cyan al 100%.
- **Paleta de Acentos**:
  - **Cybernetic Cyan (`#38bdf8`)**: Acento principal, glow sutil en botones principales (`box-shadow: 0 0 20px rgba(56, 189, 248, 0.2)`), enlaces interactivos y foco de inputs.
  - **Electric Indigo (`#6366f1`)**: Gradientes secundarios, badges de stacks y elementos decorativos.
  - **Live Green (`#22c55e`)**: Indicador de estado "Disponible para proyectos" con animación de pulso (*live pulse dot*).
  - **Google Play Accent (`#00e676` / `#34a853`)**: Integrado en tarjetas móviles en contenedor glassmorphism.
- **Tipografía**:
  - **Titulares**: `Geist` / `Space Grotesk` (geométrico, nítido y de alta jerarquía).
  - **Cuerpo de Texto**: `Inter` (máxima legibilidad y ritmo vertical).
  - **Badges, Datos y Código**: `JetBrains Mono` (espaciado técnico de precisión).
- **Efectos Visuales**:
  - Ambient glow radial en la cabecera (degradados difusos de Cyan e Indigo de fondo).
  - Malla de fondo sutil (Grid Pattern SVG con opacidad baja).
  - Glassmorphic Navbar fija con desenfoque de fondo y borde inferior iluminado.

---

## 6. Arquitectura Técnica y Estructura de Componentes

```text
portafolio/
├── public/
│   ├── favicon.svg
│   ├── og-image.png
│   └── projects/           # Mockups, capturas e iconos de proyectos
├── src/
│   ├── components/
│   │   ├── Header.astro       # Navbar glassmorphic con logo, links y status
│   │   ├── Hero.astro         # Hero con ambient glow, status pill animado y CTAs
│   │   ├── Projects.astro     # Grid filtrable de proyectos
│   │   ├── ProjectCard.astro  # Card de proyecto con efecto hover glow y badges Play Store
│   │   ├── Skills.astro       # Categorías interactivas de habilidades (Mobile, Web, Backend, Tools)
│   │   ├── About.astro        # Trayectoria autodidacta y propuesta de valor
│   │   ├── Experience.astro   # Clientes freelance y casos de éxito
│   │   ├── Contact.astro      # Sección de contacto con glassmorphism
│   │   └── Footer.astro       # Footer con créditos y links
│   ├── data/
│   │   ├── projects.ts        # Tipado y datos completos de los proyectos
│   │   └── skills.ts          # Lista clasificada de habilidades con iconos
│   ├── layouts/
│   │   └── Layout.astro       # Layout base con fuentes Geist, Inter, JetBrains Mono y SEO
│   ├── styles/
│   │   └── global.css         # Utilidades Tailwind, animaciones de glow y custom grid
│   └── pages/
│       └── index.astro        # Página de inicio ensamblada
├── astro.config.mjs           # Configuración Astro (base GitHub Pages)
├── tailwind.config.mjs        # Configuración de tema con paleta Cybernetic Minimalist
├── package.json
├── SPEC.md                    # Especificación técnica
└── TASKS.md                   # Plan de ejecución paso a paso
```

---

## 7. Requerimientos para GitHub Pages
- Configuración en `astro.config.mjs`:
  - `site`: URL del dominio o GitHub Pages (ej. `https://<usuario>.github.io`).
  - `base`: Subdirectorio si aplica (ej. `/portafolio` o `/` si es un repo tipo `<usuario>.github.io`).
- Generación 100% estática (`output: 'static'`).
- Script de build: `npm run build` (genera directorio `dist/`).
- Workflow de GitHub Actions (`.github/workflows/deploy.yml`) para despliegue automatizado.

---

## 8. Criterios de Aceptación
1. **Rendimiento**: Puntuación > 95 en Lighthouse (Performance, Accessibility, Best Practices, SEO).
2. **Responsividad**: Perfecto funcionamiento y adaptación en móviles, tablets y escritorio.
3. **Cero dependencias innecesarias de JS en runtime**: Carga instantánea aprovechando la arquitectura de islas de Astro.
4. **Veracidad y Enfoque**: Los 5 proyectos clave destacados con sus insignias, capturas y enlaces respectivos.
