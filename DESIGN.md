---
name: 인형뽑기 가게 (새들1반)
description: A classroom birch-ply cubby unit turned into a claw-machine shop, read from the back of the room.
colors:
  plum-ink: "#34264A"
  plum-ink-soft: "#5B4D6E"
  mint-wall: "#E3EFE7"
  birch: "#EFD09C"
  birch-hi: "#F7E2BB"
  birch-lo: "#D6AE72"
  ply-dark: "#B98A51"
  ply-light: "#F5DDB3"
  strawberry: "#EF4F7A"
  strawberry-deep: "#B8285A"
  bin-sunflower: "#FFC83D"
  bin-sky: "#74C4F2"
  bin-pink: "#FF94B8"
  bin-leaf: "#86CF6E"
  bin-lilac: "#BBA3F5"
  bin-tomato: "#FF8A5C"
  back-sunflower: "#FFE6A3"
  back-sky: "#CDEAFB"
  back-pink: "#FFD8E6"
  back-leaf: "#D9F1CE"
  back-lilac: "#E5DBFD"
  back-tomato: "#FFDBCB"
  bay-sky: "#D3ECFA"
  bay-lilac: "#E8DEFF"
  deck-plum: "#2E2240"
  led-ground: "#1C1328"
  led-amber: "#FFD76A"
  led-blush: "#F7C6DA"
  paper: "#FFFFFF"
typography:
  display:
    fontFamily: "Bagel Local, Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, sans-serif"
    fontSize: "clamp(1.6rem, 5.8vmin, 4.3rem)"
    fontWeight: 400
    lineHeight: 1
  shout:
    fontFamily: "Bagel Local, Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, sans-serif"
    fontSize: "min(6rem, calc(var(--mw) * .155))"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif"
    fontSize: "calc(var(--mw) * .11)"
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif"
    fontSize: "calc(clamp(1rem, 2.6vmin, 1.9rem) * 1.15)"
    fontWeight: 400
    lineHeight: 1.1
  led:
    fontFamily: "Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif"
    fontSize: "calc(var(--mw) * .058)"
    fontWeight: 400
    lineHeight: 1.12
  body:
    fontFamily: "Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Jua Local, Jua, Apple SD Gothic Neo, Malgun Gothic, Noto Sans KR, sans-serif"
    fontSize: "clamp(1rem, min(2.6vmin, 1.55vw), 1.8rem)"
    fontWeight: 400
    lineHeight: 1.1
rounded:
  flip: "0.2em"
  tag: "0.5em"
  guest: "0.9em"
  input: "10px"
  plaque: "12px"
  bay: "14px"
  rail: "16px"
  sheet: "22px"
  unit: "24px"
  pill: "999px"
spacing:
  gutter: "clamp(6px, 1vmin, 14px)"
  ring: "clamp(6px, .8vmin, 10px)"
  sheet-gap: "14px"
  field-gap: "10px"
  roster-gap: "8px"
components:
  button-spin:
    backgroundColor: "{colors.strawberry-deep}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    height: "2.5em"
    padding: "0 0.8em"
  button-big:
    backgroundColor: "{colors.strawberry-deep}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0.3em 1.1em 0.36em"
    height: "48px"
  button-sun:
    backgroundColor: "{colors.bin-sunflower}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.pill}"
    padding: "0.25em 0.9em"
    height: "44px"
  button-ghost:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
    height: "44px"
  button-warn-armed:
    backgroundColor: "{colors.strawberry-deep}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
    height: "44px"
  knob:
    backgroundColor: "{colors.birch}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.pill}"
    size: "clamp(44px, 5.4vmin, 60px)"
  name-tag:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "0.26em 0.45em 0.26em 0.28em"
  guest-tag:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.guest}"
    padding: "1em 1.2em"
  plaque:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.plaque}"
    padding: "0.32em 0.8em 0.32em 0.55em"
  flip-digit:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.flip}"
    height: "1.42em"
    padding: "0 0.12em"
  led-screen:
    backgroundColor: "{colors.led-ground}"
    textColor: "{colors.led-amber}"
    typography: "{typography.led}"
    padding: "0.25em 0.55em"
  settings-sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sheet}"
    padding: "20px clamp(16px, 3vw, 28px) 24px"
  input-text:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.plum-ink}"
    rounded: "{rounded.input}"
    padding: "6px 10px"
    height: "44px"
---

# Design System: 인형뽑기 가게 (새들1반)

## Overview

**Creative North Star: "The Class Cubby Shop"**

The whole screen is one piece of classroom furniture seen front-on: a birch-plywood cubby unit with rounded corners and a visible layered ply edge, hung on a pale mint wall. Its openings are bays: the name wheel on the left, a glossy strawberry toy claw machine with a sky-blue glass in the centre, and the children's twelve cubbies on the right. Every surface is something a kindergarten room already owns: laminated white name tags with a punched hole and a picture symbol, a hand-cut paper sign with each syllable in a different bin colour, a taped paper notice, an EVA puzzle-mat floor, and a flip scoreboard.

Everything is outlined in plum ink, like a picture book, and filled with flat classroom-bin colour. Depth comes from the furniture: the ply edge rings each opening, and the openings are recessed with inner shadows. Objects that sit on the furniture (tags, sign pieces, buttons, the machine) cast a soft plum shadow. Type is chunky rounded Korean, sized for a shared screen read from 2–4 m. Motion is reserved for cueing the single thing a pre-reader should do next.

The first viewport is one unit edge to edge with no page chrome. The machine's height sets its size, so the centre bay takes about 33–40% of the width, depending on the screen. On portrait or narrow screens the unit stacks into one column.

**Key Characteristics:**
- One birch-ply furniture unit fills the viewport; bays are recessed openings, not floating cards.
- Plum-ink outlines (2–4px) on every interactive or placed object.
- Six classroom-bin colours, used in a fixed rotation (sunflower, sky, pink, leaf, lilac, tomato).
- Self-hosted Jua for everything and Bagel Fat One for signage only, so play works offline.
- One pointing motion cue at a time; no glows.

## Colors

The palette is a classroom: warm birch wood, a mint wall, plum ink, and six saturated bin colours with paler cubby-back tints, plus one strawberry red reserved for the machine and the main actions.

### Primary
- **Strawberry** (strawberry): the claw-machine cabinet body. It is the only large saturated field on screen.
- **Deep Strawberry** (strawberry-deep): the main actions (spin, "put it in my cubby"), drawn as a vertical gradient from a lighter berry stop into this colour, with white text. Also the armed destructive state in teacher settings, and the text caret colour.

### Secondary
- **Classroom Bins** (bin-sunflower, bin-sky, bin-pink, bin-leaf, bin-lilac, bin-tomato): the six bin colours. They fill the wheel slices, the sign syllables, the picture-symbol discs on name tags, the success shout letters and the confetti, always in this order. Sunflower also does the small jobs: the claw carriage, the chute label, the restock button, the tape, the "won" corner on a tag, the armed swap pill, and text selection.
- **Cubby Backs** (back-sunflower … back-tomato): pale tints of each bin colour, used as the back wall of the matching cubby. Cubby i takes bin i mod 6.

### Tertiary
- **Machine Deck and LED** (deck-plum, led-ground, led-amber, led-blush): the machine's control deck and its LED cue screen. The amber is the main line and the blush is the second line. These colours only appear inside the machine.

### Neutral
- **Plum Ink** (plum-ink): all text, every outline, the focus ring, and the hue of every shadow. It is never pure black.
- **Soft Plum** (plum-ink-soft): secondary text (roles line, hints, roster numbers) and quiet pill outlines.
- **Mint Wall** (mint-wall): the page behind the furniture.
- **Birch family** (birch, birch-hi, birch-lo, ply-dark, ply-light): the plywood face in a vertical gradient, plus the light and dark ply laminations. Birch-lo also fills every punched tag hole.
- **Bay Backs** (bay-sky, bay-lilac): the back walls of the wheel bay (sky) and the machine bay (lilac).
- **Paper** (paper): name tags, the plaque, flip digits and the settings sheet.

### Named Rules
**The Bin Rotation Rule.** Bin colours are assigned by position in the fixed sequence sunflower, sky, pink, leaf, lilac, tomato. A child's colour comes from their index, so the wheel slice, tag disc and cubby back match. Never pick bin colours ad hoc.

**The Plum Not Black Rule.** Outlines, text and shadow tints are plum ink (#34264A at varying alpha). Near-black appears only inside the machine (the door mouth and coin slot), where it reads as a hole.

**The One Strawberry Rule.** Strawberry belongs to the machine and to the primary action of the moment. Nothing else on the furniture is red.

## Typography

**Display Font:** Bagel Fat One (self-hosted as "Bagel Local", a subset of signage glyphs only), falling back to Jua
**Body Font:** Jua (self-hosted as "Jua Local", a KS X 1001 subset), falling back to Apple SD Gothic Neo, Malgun Gothic and Noto Sans KR
**Label Font:** Jua

**Character:** Jua is a round, friendly, single-weight Hangul face that stays legible at classroom distance. Bagel Fat One is a fat, bouncy face that only appears on signage: the shop sign, the crown marquee and the "성공~~~!" / "꽝~~!" shout.

### Hierarchy
- **Display** (400, clamp(1.6rem, 5.8vmin, 4.3rem), 1): the shop sign. Each syllable sits in its own hand-cut paper tile.
- **Shout** (400, min(6rem, 15.5% of the machine width), 1, -0.02em): the outcome word on the paper notice. Each letter is filled with a bin colour and stroked in plum ink (0.045em).
- **Headline** (400, 11% of the machine width, 1.05, -0.02em): the child's name on the outcome notice. The face-out guest tag uses the same voice at 3.5em of its own base size.
- **Title** (400, ~1.15× the cubby-head size): bay headings such as "우리 반 사물함" and the settings sheet titles (1.7rem / 1.25rem).
- **LED** (400, 5.8% of the machine width, 1.12, balanced wrap): the machine's one-line cue. The second line is 4.1% with a 1rem floor.
- **Body** (400, 1.05rem, 1.45, max 60ch): teacher settings copy and hints.
- **Label** (400, clamp(1rem, min(2.6vmin, 1.55vw), 1.8rem), 1.1): names on cubby tags. On narrow screens the size drops as low as 0.9rem.

### Named Rules
**The Single Weight Rule.** Everything is weight 400. Hierarchy comes from size, colour and the tile or tag that holds the text, never from bold.

**The Signage Face Rule.** Bagel Fat One is only for signage: the sign, the marquee and the shout. Its font subset only contains those glyphs, so using it for any other text silently falls back to Jua.

**The Name Fits Its Tag Rule.** A name never wraps or truncates with an ellipsis on a cubby tag. JS (`fitNames`) shrinks the name in 0.06em steps, down to 0.62em, until it fits.

## Layout

The unit fills the viewport (100% height, a padding of `gutter` all round). It has two rows: the top rail and the bays. The rail is a three-column grid: the class plaque on the left, the sign centred, and the round knobs (fullscreen, teacher settings) on the right. The bays use the grid `1fr auto 1fr`. The centre column is sized by the machine. JS sets the machine width to the smaller of (bay height × 0.72) and 44% of the bays' width (40% below 1200px). The 0.72 ratio is the machine's own width-to-height ratio. In practice the centre bay takes about 33–40% of the width, and the wheel and cubby bays share the rest equally.

Every position inside the machine is computed in JS in pixels and passed in as custom properties: `--mw` (machine width), `--gw`/`--gh` (glass size), `--dw`/`--dh` (doll size), `--claw-w`, `--rail-h` and `--rope-w`. Machine internals scale as fractions of `--mw`. Container-query units are deliberately not used, so older classroom browsers work.

The cubby bay is a 3×4 grid of equal cubbies below a header row (title on the left, flip score on the right). Below 1200px it becomes 2×6. When the screen is portrait or narrower than 900px, the unit stacks into one column: wheel bay (wheel and slot side by side), then the machine bay (machine up to 560px wide and limited by the viewport height), then a 4-column cubby grid with rows at least 150px tall. At 600px and below, the rail wraps the sign onto its own line, the wheel stacks above the slot, and the cubbies go to 3 columns.

The spacing rhythm comes from two fluid units: `gutter` (around the furniture) and `ring` (the ply edge width, also the base of every bay's inner padding). Bay padding is `ring` plus a small vmin term. The settings sheet uses fixed px steps (14 / 10 / 8).

### Named Rules
**The One Furniture Rule.** Every surface is part of the unit or sits on it. There are no free-floating cards on the wall, and no sidebars.

**The Height-Bound Machine Rule.** The machine's width comes from the height available to it, never from a fixed column percentage. Its internals are measured in pixels in JS, not in container units.

## Elevation & Depth

This is a hybrid of carpentry and contact shadows. The furniture itself is drawn with the inset `ply` ring: a dark line, a light lamination band and another dark line, inside a birch-hi edge. Openings add an inset `recess` shadow from the top and left, so the bays read as holes in the wood. Objects placed on the furniture cast short, soft, plum-tinted drop shadows. There are no glows, coloured light or blur halos anywhere.

### Shadow Vocabulary
- **Ply Edge** (`--ply`, a stack of four inset rings built from `ring`): the unit, the rail, the cubby header and every bay.
- **Recess** (`--recess`, inset shadows from the top and left in plum at .34/.2): openings only (the wheel, machine and cubby bays).
- **Resting** (`--depth-1`: `0 2px 3px rgba(52,38,74,.16), 0 8px 18px rgba(52,38,74,.14)`): tags, sign tiles, the plaque, knobs, flip digits and the coin.
- **Lifted** (`--depth-2`: `0 3px 6px rgba(52,38,74,.2), 0 18px 34px rgba(52,38,74,.2)`): the unit, the machine cabinet, the spin button, the face-out guest tag, the outcome notice and the settings sheet.
- **Press Lip** (`inset 0 -.16em 0 rgba(52,38,74,.4)`): the bottom lip on pill buttons. On `:active` the button moves down (2–3px) and the lip thins.
- **Screen Well** (`inset 0 3px 8px rgba(0,0,0,.55)`): the LED screen and the door mouth inside the machine.

### Named Rules
**The No Glow Rule.** Depth is wood, recess and contact shadow. Nothing glows, including the LED. Attention comes from one motion cue, not from light.

## Shapes

The shapes are rounded, hand-made and slightly imperfect. The furniture uses clean radii that step down as you move inward: unit 24px, rail 16px, bays 14px, plaque 12px. Paper objects are cut by hand. Each sign tile has its own uneven elliptical `border-radius` and a small tilt (between -4° and +4°). The outcome notice has asymmetric corners, two strips of tilted sunflower tape and a curled bottom-right corner. The plaque tilts -2°. Tags carry a punched hole (a birch-lo circle with an ink ring) centred on the top edge. A won tag gets a sunflower corner fold. Buttons are full pills (999px) or circles (knobs and coin). An absent child's cubby shows a dashed outline in place of the tag.

## Components

### Buttons
Tactile, toy-like and pressable.
- **Shape:** full pill (999px), 3–3.5px plum outline.
- **Primary (spin / big):** a strawberry gradient (#CF3A69 → strawberry-deep) with paper-white Jua text and a press lip. The spin button is 2.5em tall and stretches the slot width, with an inline refresh SVG. The big button on the notice is at least 48px tall.
- **Sunflower (restock):** sunflower fill with plum text, at least 44px tall.
- **Ghost (settings rows):** paper fill with a 2.5px ink outline, at least 44px tall. The warn variant swaps the outline and text to strawberry-deep and fills it once armed (two-step reset).
- **Hover / Focus / Active:** hover (fine pointers only) brightens primaries to 1.07 and tints ghosts #FFF4DC. Focus is a 4px plum outline with a 3px offset. Active moves the button down 2–3px over 120ms.

### Knobs
Round birch knobs on the rail: a radial birch gradient, a 3px ink ring, a stroked plum SVG icon at 46% of the knob, and a size of clamp(44px, 5.4vmin, 60px). Hover lifts the knob 1px.

### Name Tag (chip)
A laminated white tag. It has a 160° paper-to-lavender gradient (#F2EFF6), a 2.5px ink border, a 0.5em radius, the resting shadow and a punched hole at the top. Inside are a bin-coloured disc holding the picture-symbol SVG, then the name (fitted, see Typography). Absent children get a "쉬어요" outlined pill. A won tag gets the sunflower corner fold.

### Guest Tag (signature)
When a child is picked, their name tag flies from the cubby to the slot under the wheel and is shown face-out at full size. The card shows the symbol disc (4.8em), the name (3.5em), the greeting line and the roles line in soft plum. It has a 3.5px border, a 0.9em radius and the lifted shadow, and a "다른 친구로" swap pill in the top-right that turns sunflower when armed.

### Claw Machine (signature)
A strawberry cabinet: a horizontal gradient with highlights at both edges and a 3.5px ink outline. On top is a marquee crown with chasing bulbs and Bagel lettering in sunflower. The sky-blue glass has a white bezel and two diagonal sheen bands. Inside are a pink prize mound, a sunflower claw carriage on a plum rail, a translucent chute with a tilted sunflower "출구" label, and a dark plum deck holding the LED cue screen and the prize door, whose flap swings open. The machine stands on an EVA puzzle-mat floor with ink feet and a soft floor shadow.

### Outcome Notice
A paper sign taped over the glass (#FFFDF8 paper, 3.5px ink border, uneven corners, curled corner). It shows the shout ("성공~~~!" with bin-coloured letters, or "꽝~~!"), the doll, the name, a line, a sub-line in soft plum and the big button. The notice rises in (320ms). The miss shout stamps in. The doll on a success notice hops.

### Flip Scoreboard
White flip digits (1.42em tall, 0.2em radius, a 2.5px ink border and a hairline across the middle) using tabular numerals. They read "성공 N / 12" in the cubby header.

### Name Wheel
A birch-rimmed wheel (an ink outer ring plus ply rings) with bin-coloured slices. Each name is set character by character along its slice, with a picture symbol at the rim. A tap spins about six turns. A drag or flick throws the wheel in the direction of the flick, starting at the finger's own speed. The winning slice gets a 5px ink stroke and the pointer ticks as slices pass.

### Inputs / Fields (teacher settings)
Paper fill, a 2.5px ink border, a 10px radius and at least 44px height. Selects use a custom plum chevron. Checkboxes are 28px with a strawberry accent. The settings sheet is paper with a 4px ink border, a 22px radius and the lifted shadow, over a plum scrim (rgba(52,38,74,.5)).

### Motion
Easing is `cubic-bezier(0.23, 1, 0.32, 1)` (ease-out) for state changes and `cubic-bezier(0.77, 0, 0.175, 1)` (ease-in-out) for loops. Only one pointing cue runs at a time. In the idle phase, a hand bobs over the spin button. In the ready phase, a hand bobs over the glass while the dolls wiggle in turn. The marquee bulbs chase only while the wheel spins and the claw plays. Reduced motion stops every loop, removes swing, cuts the number of wheel turns and skips confetti.

## Do's and Don'ts

### Do:
- **Do** draw every placed or tappable object with a plum-ink outline (2–4px) and a flat fill.
- **Do** take colour per child from the fixed bin rotation, so the wheel slice, tag disc and cubby back always match.
- **Do** make new surfaces part of the birch unit, framed with the `ply` ring and recessed when they are openings.
- **Do** keep tap targets at 44px or more (48px for primary actions) and press them down 2–3px on `:active`.
- **Do** run only one pointing motion cue at a time, and stop it under reduced motion.
- **Do** size machine internals from JS-measured pixels (`--mw`, `--gw`), not container-query units.
- **Do** fit names to their tags by shrinking them, never by wrapping or adding an ellipsis.
- **Do** use inline SVG for every icon and symbol, stroked or outlined in plum.

### Don't:
- **Don't** use glows, coloured light or neon halos. Depth comes from wood, recess and soft plum contact shadows.
- **Don't** use pure black for text or outlines. Near-black is only for holes inside the machine.
- **Don't** set Bagel Fat One on anything but signage. Its subset has no other glyphs.
- **Don't** use bold weights. Jua and Bagel are single-weight (400).
- **Don't** float cards on the wall or add sidebars outside the unit.
- **Don't** load fonts from the network. Both faces are self-hosted subsets inlined at build time.
