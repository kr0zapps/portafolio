# Portafolio Web Personal - Plan de Ejecución (TASKS.md)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Astro project with minimal template in root (`package.json`)
- [x] T002 Install Tailwind CSS, lucide-astro, and fontsource dependencies

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**🚨 CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 [P] Configure `tailwind.config.mjs` with Cybernetic Minimalist tokens
- [x] T004 [P] Configure `src/styles/global.css` with glassmorphism and background grid
- [x] T005 Setup `src/layouts/Layout.astro` with fonts and global styles

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Core Navigation & Hero (Priority: P1) 🚀 MVP

**Goal**: User can see the main landing page, navigation, and hero section.

**Independent Test**: Build and view index page with Header, Hero, and Footer visible.

### Implementation for User Story 1

- [x] T006 [P] [US1] Create `src/components/Header.astro` with glassmorphic navbar
- [x] T007 [P] [US1] Create `src/components/Footer.astro` with credits
- [x] T008 [US1] Create `src/components/Hero.astro` with ambient glow and CTAs
- [x] T009 [US1] Integrate Header, Hero, and Footer in `src/pages/index.astro`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Projects Showcase (Priority: P2)

**Goal**: User can browse the portfolio projects.

**Independent Test**: Projects section renders data correctly on the index page.

### Implementation for User Story 2

- [x] T010 [P] [US2] Create data model in `src/data/projects.ts`
- [x] T011 [P] [US2] Create `src/components/ProjectCard.astro` component
- [x] T012 [US2] Create `src/components/Projects.astro` grid with filters (depends on T010, T011)
- [x] T013 [US2] Add Projects section to `src/pages/index.astro`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Skills & Experience (Priority: P3)

**Goal**: User can read about the developer's skills and trajectory.

**Independent Test**: Skills, About, and Experience sections render correctly.

### Implementation for User Story 3

- [x] T014 [P] [US3] Create data model in `src/data/skills.ts`
- [x] T015 [P] [US3] Create `src/components/Skills.astro` component
- [x] T016 [P] [US3] Create `src/components/About.astro` component
- [x] T017 [P] [US3] Create `src/components/Experience.astro` component
- [x] T018 [US3] Add Skills, About, and Experience sections to `src/pages/index.astro`

**Checkpoint**: All core UI user stories should now be independently functional

---

## Phase 6: User Story 4 - Contact & Deploy (Priority: P4)

**Goal**: User can contact the developer and site is ready for deploy.

**Independent Test**: Contact form renders, build completes, actions workflow is ready.

### Implementation for User Story 4

- [x] T019 [P] [US4] Create `src/components/Contact.astro`
- [x] T020 [US4] Add Contact section to `src/pages/index.astro`
- [x] T021 [US4] Configure `astro.config.mjs` for GitHub Pages (site, base)
- [x] T022 [US4] Create GitHub Actions workflow in `.github/workflows/deploy.yml`

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T023 Run `npm run build` to verify Lighthouse/performance expectations and catch TS errors.
- [x] T024 Code cleanup and refactoring (if needed)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 -> P2 -> P3 -> P4)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2)
- **User Story 4 (P4)**: Can start after Foundational (Phase 2)

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready
