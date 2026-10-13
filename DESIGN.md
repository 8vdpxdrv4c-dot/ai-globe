# 全球 AI 产业链 · Design Spec

## 1. Art direction — "Editorial Cartography"
A printed infographic poster brought to life, in the spirit of FT/Bloomberg visual journalism. The globe is a light relief map sitting on a **warm paper ground** (a soft radial wash from paper to pale sky). Ink-navy serif headlines. Colour carries meaning only: three layer hues (gold / teal / copper). Everything else is neutral ink and paper. There is no glow, no neon and no dark glass.

## 2. Tokens
| token | value | use |
|---|---|---|
| `--paper` | `#F5F2EB` | page ground |
| `--sky` | `#E6EDF2` | ground gradient edge |
| `--ink` | `#14233A` | titles, primary text |
| `--ink-2` | `#4A5568` | body |
| `--ink-3` | `#8A94A3` | captions, EN sub-labels |
| `--rule` | `rgba(20,35,58,.12)` | hairlines, borders |
| `--surface` | `rgba(255,255,255,.92)` | cards, dock, drawer |
| `--up` | `#B8860B` (gold) | upstream: chips, devices, manufacturing, energy |
| `--mid` | `#0F8C86` (teal) | midstream: compute, cloud, models |
| `--down` | `#C2602F` (copper) | downstream: applications, robots |
| radius | 6 (chip), 10 (card), 14 (panel) | |
| shadow | `0 1px 2px rgba(20,35,58,.06), 0 8px 24px rgba(20,35,58,.08)` | one elevation level only |

## 3. Type
- Display: **Noto Serif SC** 700 (fallback: Songti SC, serif). Title 34/40, letter-spacing .02em.
- UI and body: **Noto Sans SC** 400/500/700 (fallback: PingFang SC, system-ui).
- Scale: 34 title · 15 card title · 13 body · 12 UI · 11 caption · 10 micro EN (uppercase, tracking .08em).
- Numbers use tabular-nums.

## 4. Grid and spacing
- 8 px base. Screen margin 28 px on desktop and 14 px on mobile. Panels have 16 px internal padding.
- Fixed layout zones: title at top-left; region tabs at top-right; layer legend and filter dock at bottom-left; narrative stepper at bottom-right; info drawer on the right.

## 5. Components
- **Title block**: kicker (EN micro caps) → serif H1 → one-line subtitle → hairline → three key numbers (sites / segments / regions).
- **Region tabs**: one segmented control (全球 美国 湾区 中国 长三角 珠三角 台湾 东南亚 日韩 欧洲). The active tab is ink-filled. It scrolls horizontally on mobile.
- **Layer legend** (always visible): three toggle pills with a coloured dot and live count. It is both the legend and the main filter.
- **Filter dock**: a single "筛选" button opens a popover with the 23 segment chips grouped by layer, region chips, and switches for arcs and auto-rotate. The active-filter count shows as a badge. On mobile the popover becomes a bottom sheet.
- **Narrative stepper**: one card at a time. Step number, serif heading, 3-line body, prev/next buttons and dots. Each step flies the camera.
- **Map cards** (poster style): white, 1 px rule border, 3 px layer-colour top edge. CN city name in bold, EN city name in micro caps, then a vertical list of companies, each with a coloured dot, max 5 plus "+N". Single-company cards show company / EN / segment tag.
  - Global zoom shows **region cluster cards** only (region, site count, top segments).
  - Regional zoom shows **city cards**.
  - A thin ink leader line runs to a 5 px ring dot.
- **Info drawer**: right-side white sheet, 360 px. Contains layer and segment tags, serif company name, EN name, a key-value table, description, and supply-chain relationships as linked chips. On mobile it is a bottom sheet.

## 6. Motion
- Camera flights use 2.2 s ease-in-out-cubic. UI uses 240 ms with cubic-bezier(.2,.8,.2,1).
- Cards fade and scale (0.96 → 1) when they appear. There are no bouncy or infinite UI animations.
- Only data moves: arcs carry a slow dash of light along their path.

## 7. Hierarchy
1. Title. 2. Globe and data (cards, buildings). 3. Region tabs. 4. Legend/filter. 5. Narrative.

Chrome uses at most about 18% of the viewport on desktop. Arcs are hairlines at 35% opacity, so they never compete with cards.
