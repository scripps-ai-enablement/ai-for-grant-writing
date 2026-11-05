# Live demo: three layers of context

A demonstration for the start of the hands-on hour, run live by the instructor
before students open the grant project. It has nothing to do with grants on
purpose, so the only thing to watch is what each layer of context changes.

`dinner-demo/` is the project folder. Keep this README outside it.

## Run it

Use a new conversation for each layer.

1. **A prompt.** A new chat, not in a project. Ask:
   "What should I make for dinner tonight? Include a shopping list."
2. **+ CLAUDE.md.** Projects > + > Use an existing folder > `dinner-demo`.
   Leave Instructions empty. Open `CLAUDE.md` and `pantry.md` on screen, then
   ask the same question in a new conversation in the project.
3. **+ a skill.** Open `skills/shopping-list/SKILL.md` on screen. In a new
   conversation in the project, ask the same question with one line added:
   "Follow skills/shopping-list/SKILL.md."

## What to point at

- Layer 1 has to guess who is eating, what is in the kitchen and how you cook,
  so it gives the most typical dinner.
- Layer 2 follows the standing rules without being told again, and reads
  `pantry.md` because `CLAUDE.md` says to. It sees the skill and leaves it
  alone, because no one named it.
- Layer 3 makes the list the same way every time: the "Already have" section,
  store sections in a fixed order, and a closing line saying whether its own
  check passed.

## Test runs, 4 November 2026

Run as fresh agent sessions with Claude Opus 5.5, outside the desktop app, so
treat them as a preview, not a promise. Rerun on a student-like account before
class (see `../TEST-BEFORE-CLASS.md`).

- **Layer 1:** sheet-pan lemon-garlic chicken thighs with potatoes and green
  beans, about 45 minutes in a 425°F oven, serving four. The list included
  chicken. It offered a vegetarian swap and asked what was at home.
- **Layer 2 (two runs):** a chickpea, spinach and coconut curry over rice,
  30 minutes, one burner and the rice cooker, built from `pantry.md`. Both
  said little or nothing needed buying. Both listed the skill's folder and
  did not open it, saying it had not been named.
- **Layer 3 (two runs):** the same kind of curry, with the list grouped under
  "Already have" and store sections, and a closing line such as "Check passed:
  each of the 19 ingredients appears once, 2 on the list and 17 under Already
  have."

The second pair of runs used an earlier `pantry.md` without salt and oil, so
the skill put both on the list. They have since been added, and the lime
removed, so the list has something real to buy.
