# Plan de Implementación Técnica (plan.md)

## 1. Arquitectura y Stack
- **Framework**: Astro (SSG - Static Site Generation).
- **Estilos**: Tailwind CSS v4 (`@tailwindcss/vite`).
- **Diseño**: "Cybernetic Minimalist" (Glassmorphism, Dark Slate `#090d16`, Cybernetic Cyan `#38bdf8`, Indigo `#6366f1`).
- **Iconografía**: `lucide-astro`.
- **Tipografía**: `Geist` (Titulares), `Inter` (Cuerpo), `JetBrains Mono` (Etiquetas/Código).
- **Despliegue**: GitHub Pages (via GitHub Actions).

## 2. Modelo de Datos
- **Proyectos (`src/data/projects.ts`)**: Array de objetos con `id`, `title`, `type`, `platform`, `description`, `techStack`, `badges`, `link`.
- **Habilidades (`src/data/skills.ts`)**: Categorías estructuradas (`Mobile`, `Web`, `Backend`, `Tools`).

## 3. Fases de Desarrollo
- **Fase 1**: Scaffolding e Inicialización (Completado).
- **Fase 2**: Configuración del Sistema de Diseño y Estilos.
- **Fase 3**: Capa de Datos Tipados y Contenido.
- **Fase 4**: Layout Base y Arquitectura Global.
- **Fase 5**: Desarrollo de Componentes UI de Alto Impacto (`Header`, `Hero`, `ProjectCard`, `Projects`, `Skills`, `About`, `Contact`, `Footer`).
- **Fase 6**: Integración, Testing y Verificación.

## 4. Restricciones Técnicas
- **Cero dependencias innecesarias de JS en runtime** (aprovechar arquitectura de islas de Astro solo si es necesario).
- **Rendimiento**: Lighthouse score > 95.
- **Compatibilidad**: Diseño responsivo (Mobile-first a Desktop fluid grid).
