# 全球 AI 产业链 · Design Spec (v3 — "Holographic Night")

> v3 replaces the light editorial palette with a dark, glowing command-center look. It follows the user's reference image. Layout, type scale and the label-placement rules below are unchanged.

## Art direction (v3)
- **Scene:** a deep navy-black field (#030814) with a faint 48 px grid, a purple and blue fbm nebula, and sparse stars. All of it is drawn by a full-screen shader inside the WebGL scene, so bloom can apply.
- **Globe:** the map is regenerated from Natural Earth (`tools/build_dark.py`). Ocean is dark navy, land is blue-grey relief, coastlines are glowing cyan, and borders and provinces are thin cyan lines. The hillshade comes from the heightmap. A strong blue fresnel rim plus an additive atmosphere shell surround it. About 2,600 Natural Earth populated places appear as faint cyan and amber "city light" dots.
- **Orbits:** five thin additive ellipses (cyan, blue and violet) with travelling bright heads. They fade out below a camera distance of 2.0.
- **Arcs:** thin, additive and layer-coloured (amber up / cyan mid / rose down), each with a bright white-hot particle head.
- **Buildings:** holographic, rendered as additive translucent cyan volumes with lit window grids and a faint ground halo ring.
- **Bloom:** UnrealBloomPass with threshold .62 and radius .45. Strength runs from .6 at global zoom down to .22 up close.

## Tokens (v3)
| token | value |
|---|---|
| bg | `#030814` |
| text | `#EAF3FF` / `#A9BCD8` / `#6F86A8` |
| glass | `linear-gradient(160deg, rgba(18,40,84,.62), rgba(8,18,42,.58))` + 14 px blur |
| glow border | `1px rgba(110,190,255,.28)` + `0 0 18px rgba(40,150,255,.22)` + inner glow |
| cyan accent | `#39D5FF` |
| layers | up `#FFC94A` · mid `#2FE6FF` · down `#FF7AA8` |
| region bar | gradient `#16d1c5 → #39d5ff → #8f6bff → #ff4f7a` |

## Components (v3)
- **Region cards:** glass panel, white serif title with count, EN micro caps, gradient bar, then up to 3 line icons with label and count. The icon categories are 算力 / 算法 / 芯片 / 数据 / 应用, aggregated from the 23 segments.
- **City cards:** glass with a 2 px layer-colour top edge, white text, and glowing company dots.
- **Leaders:** thin cyan elbow lines ending in a glowing dot.
- **Tabs:** dark pill bar. The active tab has a cyan gradient fill and an outer glow.
- **Story stepper:** a glass panel reading "01 / 06 · 产业故事", with a cyan 展开/收起 toggle and cyan step dots.
- **Place names:** white with a dark halo, EN subtitle in blue-grey.

---
# v2 base spec (layout, type, placement)
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
- Display: **Noto Serif SC** 700 (fallback: Songti SC, serif). Title 40/46, letter-spacing .02em.
- UI and body: **Noto Sans SC** 400/500/700 (fallback: PingFang SC, system-ui).
- Scale: 40 title · 17.5 card city · 15 company/body · 14 UI · 12 EN sub · 11.5 micro caps. Mobile ≈ 85%.
- Fonts are self-hosted subset WOFF2 in `/fonts` (~690 KB, regenerate when data changes).
- Numbers use tabular-nums.

## 4. Grid and spacing
- 8 px base. Screen margin 28 px on desktop and 14 px on mobile. Panels have 16 px internal padding.
- Fixed layout zones: title at top-left; region tabs at top-right; layer legend and filter dock at bottom-left; narrative stepper at bottom-right; info drawer on the right.

## 5. Components
- **Title block**: kicker (EN micro caps) → serif H1 → one-line subtitle → hairline → three key numbers (sites / segments / regions).
- **Region tabs**: one segmented control (全球 美国 湾区 中国 长三角 珠三角 中国台湾 东南亚 日韩 欧洲). The active tab is ink-filled. It scrolls horizontally on mobile.
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

## 8. Label placement
Cards are never hidden for overlap. Only far-side or off-screen anchors hide. Placement runs when the camera settles, using a greedy search over 8 directions × 6 radii (full card, then compact). If no spot is free, cards go into side columns (left/right, sorted by anchor y, multiple columns if needed). Previous spots are reused when still valid (hysteresis), and cards animate to new targets. Place-names yield to cards.
