# Product

<!-- impeccable:product-schema 1 -->

> Interview substitution: the structured interview was declined and the user said to proceed ("너가 뽑을수 있는 최고의 디자인으로"). Every fact below comes from the user's chat messages or the uploaded lesson plan (`'내 아이 수업보기' 교수학습 과정안`, HWP + PDF). Lines marked *(inferred)* are not confirmed.

## Platform

web

## Stack

delegated: static single-file HTML/CSS/JS with no build step, so the teacher can open one link or file on any classroom device; also published as a claude.ai artifact.

## Users

- **The teacher (the user's mother).** A kindergarten teacher running a parents' open class ("내 아이 수업보기"). She drives the screen, sets up names and absences, and voices the lines from her lesson plan.
- **The children of 새들1반.** Twelve of them: 강하율, 권민석, 김다연, 김연우, 김온유, 김주원, 박소윤, 백시안, 변정현, 서로희, 진하성, 한윤재.
  - Each child takes a turn as the 도전자 (challenger) who taps the screen.
  - The other children play 가게 주인 (shopkeeper), 응원단 (cheer squad) and 다음 손님 (next customer).
  - Most cannot read yet *(inferred from age)*.
  - Age is unresolved: the lesson plan says 4세 and the user said 6세.
- **Parents (may or may not take part).** The lesson plan pairs each child with their mother as the 기계 도우미 (machine helper), but the user said mothers may not join in. On-screen copy must not assume a parent is there.

## Product Purpose

- **What it is:** a digital 인형뽑기 가게 (claw-machine shop) for the class's play theme "우리 동네 이웃이 되어 놀아요" (being neighbours in our neighbourhood).
- **How a turn works:** a name wheel picks whose turn it is. The child, helped by their mother, picks a doll. The claw grabs it, and the class celebrates.
- **What success means:**
  - Every present child gets a turn and leaves with a prize, together with their mother.
  - A miss feels playful, not sad, and always leads to a retry.
  - The teacher never loses control of whose turn it is.

## Front page: 우리동네 map

- The site opens on a map redrawn from the class's "우리동네최고" bulletin board (root `index.html`, built from `town/src/app.html`).
- Its 14 places are the ones the user listed: 병원, 인형뽑기 가게, 도서관, 경찰서, 소방서, 문정유치원, 광신프로그레스 아파트, 골드클래스 아파트, 한성아파트, 오네뜨아파트 (next to 한성), 다이소, 마트, 과일가게 and 미용실.
- Tapping a place opens its inside (each apartment opens as a cut-away home: kitchen, living room and bedroom), where everything can be tapped and answers in a speech bubble. Some things count up as they are tapped: the 마트 cart counts items; 다이소 items cost 1000–5000원 and the child pays at the counter by tapping 1000원 bills until the total is met.
- Every speech bubble is also read aloud in the device's own Korean voice at natural pitch, slightly slower; a header button turns the voice off.
- A pedestrian light by the slanted road opens a 횡단보도 game: cars drive past on red; on green they stop at the line and the child crosses with a raised hand.
- 마트, 과일가게 and 다이소 all price their goods (1000–5000원) and the child pays at the counter with 1000원 bills.
- The 인형뽑기 가게 opens the claw game. The game shows a 우리동네 button only when it was opened from the map.

## Positioning

- It is built around one specific class: their names, their roles from the lesson plan, the teacher's own success and failure lines, and the characters these children asked for.
- A generic claw game or a generic name picker has none of that.

## Operating Context

- **Session:** 2026-10-30 (Fri) 14:15–14:50, in the 새들1반 classroom, during the "놀이" block of the lesson plan.
  - The plan's physical 과자뽑기 (snack-grab) game is a separate activity. This app is the screen version the children asked for.
- **Device:** a shared classroom screen (TV, interactive whiteboard or projector) or a tablet, used by touch *(inferred: device not confirmed)*.
- **Audience:** viewers sit 2–4 m away, including parents at the back.
- **Network:** may be restricted. Web fonts can fail to load.
- **Lines from the plan:**
  - Success: "엄마와 힘을 합쳐서 성공했네요!" ("You did it by joining forces with mum!"). This is the teacher's spoken line only. On screen it is replaced by class-cheer wording at the user's request.
  - Failure: "이번에는 아쉽게도 … 잡지 못했네요! 다른 방법을 생각해 볼까요?" ("Unfortunately you couldn't catch it this time! Shall we think of another way?")
  - After a failure, give the child another chance.

## Capabilities and Constraints

- **Turn picking:** a name wheel picks the turn. Children who already succeeded leave the wheel. A child marked absent (name cleared) is left out.
- **The grab:** tap a doll, the claw carries it to the chute, and it comes out of the prize door.
- **Outcomes:** success shows "성공~~~!" and a miss shows "꽝~~!" (user's wording). The retry is guaranteed to succeed by default. The miss rate can be set.
- **Teacher-only settings:** names, absences, miss rate, guaranteed retry, skip-winners, optional coin step, sound, restock, and a two-step reset.
- **Characters:** the dolls are hand-drawn tributes to characters the children love, chosen by the user: Cinnamoroll, Kuromi, My Melody, Pompompurin, Hello Kitty, Pochacco and Keroppi, plus a bear. They are not official artwork.
- **Persistence:** state is saved in the browser's localStorage on that device only.
- **Not decided:** the device model and screen size, and whether the coin step is used in class.

## Brand Commitments

- User-pinned:
  - The name wheel sits on the **left** ("왼쪽에 돌림판").
  - The words "성공~~~!" and "꽝~~!".
  - Sanrio-style characters, with 시나모롤 and 쿠로미 first.
- The lesson-plan wording for success and failure lines and for the roles is used as written.

## Evidence on Hand

- Lesson plan: the uploaded HWP and PDF (same content), with objectives, roles, the teacher's lines and the schedule.
- The class list of 12 names, given by the user.
- There are no photos, logos or official character artwork. None must be fabricated or implied to be official.

## Product Principles

1. **Every child succeeds, cheered on by the class.** A miss is a beat in the story, never the ending. The copy never assumes a parent is helping.
2. **One thing at a time for pre-readers.** Each moment has one obvious target, cued by picture and motion, not text alone.
3. **The teacher stays in control.** Nothing a child can tap may steal a turn or reset the game.
4. **Readable from the back of the room.** Names and outcomes are legible at classroom distance on a shared screen.
5. **Works on whatever is in the room.** One file, touch first, no network dependency for core play.

## Accessibility & Inclusion

- **Users:** pre-reading children aged 4–6, so tap targets must be large and cues pictorial.
- **Text:** sized for a shared screen at 2–4 m.
- **Sound:** can be turned off.
- **Motion:** honours reduced-motion settings.
- **Failure states:** must avoid singling a child out in front of parents.
