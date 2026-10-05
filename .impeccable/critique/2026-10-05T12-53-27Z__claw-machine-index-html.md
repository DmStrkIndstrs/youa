---
target: claw-machine/index.html
total_score: 21
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
target_identity: "file:/home/user/youa/claw-machine/index.html"
target_fingerprint: "sha256:8c6d0309b0e4a31774415a9eab6c4cb25919f10c9a585f642a42f5807f5c8125"
target_path: /home/user/youa/claw-machine/index.html
timestamp: 2026-10-05T12-53-27Z
slug: claw-machine-index-html
---
Method: dual-agent (A: design review · B: detector + browser evidence)

## Heuristics (21/32, n/a: 7, 10)
1 Visibility 3 — step text in left card, ~300px from the machine
2 Real world 3 — door is a flat dark slab
3 Control 2 — roster tap silently reassigns turn; re-spin not undoable
4 Consistency 3 — three loud button colours compete
5 Error prevention 2 — child-reachable buttons change game state
6 Recognition 3 — instructions are text-only for pre-readers
7 n/a — single-session teacher tool
8 Minimalism 2 — grey 14px meta text, empty roster cards, empty glass, door slab
9 Recovery 3 — kind miss path, guaranteed retry
10 n/a — teacher-led

## Specificity
Machine interior is authored (custom characters, claw, marquee, awning, chute). Side columns read as a generic web-app sidebar; the shop world stops at the machine border — three islands on mint. Detector: 0 primary findings; advisory stripes (awning, intentional); browser flagged glass gradient (literal), bulbs (ignored, literal), dark-glow (detector's own overlay, false positive).

## Priority issues
- [P1] Three floating islands; machine doesn't fill TV; top 55% of glass empty; door slab. Fix: machine as stage ~50% width, side panels as shop furniture (ticket booth wheel, prize shelf roster), raise pile, small door pocket. layout/bolder
- [P1] Character SVGs clipped (Cinnamoroll ears, Melody ears, Kuromi horns exceed viewBox 0 0 100 112). Fix: overflow visible or widen viewBox. polish
- [P1] Children can hijack turns: big red re-spin stays primary; roster cards set turn; restock anytime. Fix: demote/hide spin after pick, roster display-only (teacher mode), restock only when empty. harden
- [P2] Peaks under-celebrated: no name reveal moment, popup hides doll landing, no class finale. delight
- [P2] TV-distance legibility: 14–16px meta and roster names; wheel labels upside-down after spin. Fix: 20px min, 24px+ names, sticker-slot progress. typeset

## Personas
4-year-old: ~30 targets, no pointing cue, back dolls hidden. Mother: cue far and small; miss greying awkward. Teacher: hijack risks, roster below fold on 1024x768, absent only via settings.

## Minor
Step text wraps/jumps; coin off so slot hidden; winner slice highlight weak; grey disabled spin looks broken; mint machine shadow; 1px vertical scroll; Gowun Dodum has no 700 weight; self-host fonts.

## Questions
Machine at 70% with full-screen "next customer" interlude? Name text vs photo/symbol for pre-readers? Make the landing and the 12-prize shelf the hero?
