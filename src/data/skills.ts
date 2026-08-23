export interface SkillCategory {
  title: string;
  skills: string[];
  iconName?: string;
}

export const skills: SkillCategory[] = [
  {
    title: 'Mobile Development',
    iconName: 'smartphone',
    skills: ['Android', 'Kotlin', 'React Native', 'Flutter', 'Google Play Console']
  },
  {
    title: 'Frontend & Web',
    iconName: 'layout',
    skills: ['HTML5/CSS3', 'JavaScript/TypeScript', 'Astro', 'React', 'Tailwind CSS']
  },
  {
    title: 'Backend & Data',
    iconName: 'database',
    skills: ['APIs REST', 'Node.js', 'PostgreSQL', 'Firebase', 'Supabase']
  },
  {
    title: 'Herramientas & Métodos',
    iconName: 'wrench',
    skills: ['Git/GitHub', 'Spec-Driven Development', 'UI/UX Design', 'Figma']
  }
];
