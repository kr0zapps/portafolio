export type ProjectType = 'Mobile' | 'Web' | 'Fintech & Apps' | 'Todos';

export interface Project {
  id: string;
  title: string;
  type: ProjectType;
  platform: string;
  status: 'Activa' | 'Legado' | 'Producción' | 'Demo' | 'Showcase';
  description: string;
  techStack: string[];
  link?: string;
  github?: string;
  badges: string[];
  image: string; // URL o placeholder
}

export const projects: Project[] = [
  {
    id: 'fitgamer',
    title: 'FitGamer',
    type: 'Mobile',
    platform: 'Google Play',
    status: 'Activa',
    description: 'Gamificación aplicada al fitness y seguimiento de hábitos deportivos. Convierte tus entrenamientos en misiones.',
    techStack: ['React Native', 'TypeScript', 'Firebase'],
    link: '#',
    badges: ['Google Play'],
    image: 'https://placehold.co/600x400/0f131c/38bdf8?text=FitGamer',
  },
  {
    id: 'callate-spam',
    title: 'Cállate Spam',
    type: 'Mobile',
    platform: 'Google Play',
    status: 'Legado',
    description: 'Intercepción y filtrado inteligente de llamadas no deseadas o spam telefónico en Android.',
    techStack: ['Android', 'Java', 'Call APIs'],
    link: '#',
    badges: ['Google Play', 'Legacy'],
    image: 'https://placehold.co/600x400/0f131c/6366f1?text=Callate+Spam',
  },
  {
    id: 'cuentaapp',
    title: 'CuentaApp',
    type: 'Fintech & Apps',
    platform: 'Web/Mobile',
    status: 'Producción',
    description: 'Gestión y control financiero personal y empresarial con métricas y reportes interactivos.',
    techStack: ['React', 'Node.js', 'PostgreSQL', 'Tailwind'],
    link: '#',
    badges: ['Fintech'],
    image: 'https://placehold.co/600x400/0f131c/22c55e?text=CuentaApp',
  },
  {
    id: 'webs-freelance',
    title: 'Webs Corporativas',
    type: 'Web',
    platform: 'Web',
    status: 'Producción',
    description: 'Soluciones corporativas (fenixselect.cl, RedNorte) orientadas a conversión, SEO y presencia digital.',
    techStack: ['Astro', 'Tailwind CSS', 'Figma'],
    link: '#',
    badges: ['Freelance', 'SEO'],
    image: 'https://placehold.co/600x400/0f131c/e2e8f0?text=Webs+Freelance',
  },
  {
    id: 'catalogo-ui',
    title: 'Catálogo UI/UX',
    type: 'Web',
    platform: 'Web',
    status: 'Showcase',
    description: 'Sistema de catálogo y experiencia de usuario optimizada diseñado para impulsar minipymes.',
    techStack: ['Next.js', 'Tailwind CSS', 'Framer Motion'],
    link: '#',
    github: '#',
    badges: ['Design System'],
    image: 'https://placehold.co/600x400/0f131c/38bdf8?text=UI+Catalog',
  }
];
