---
name: significance-checklist
description: Review a grant's Significance and Innovation sections against a writing checklist, item by item, quoting the sentence that meets each item or naming what is missing, and flag the common pitfalls. Use when asked to check, review or critique a Significance, Innovation or scientific premise section. Critique only; never rewrites the text.
---

# Significance and Innovation checklist

## Which checklist to use

If `checklists/` holds a checklist for Significance or Innovation, use it. Otherwise use `reference/checklist.md` in this skill, and say so at the top of the review. If `funder/` holds the review criteria, read how this section is scored before starting.

## Steps

1. Read the section: `drafts/significance.md` and `drafts/innovation.md` unless the author names other files. Read `drafts/aims.md` too if it exists, because these sections must argue for those aims.
2. Go through the checklist one item at a time, giving the status (met, partly met, missing) and the sentence that meets it, quoted exactly, or one line on what is missing.
3. Run two tests:
   - **The gap test.** Remove the disease or field name from the paragraph that states the gap. Does it still say what is unknown and why that blocks progress? If it only says the disease is important, it fails.
   - **The restate test.** In one sentence each, restate the need, the impact and what is new. Where you can't, say so.
4. Check for the pitfalls in `reference/checklist.md` and list any you find with the passage that shows it.
5. List the five most important problems, most serious first.

## Rules

- Describe problems; don't write replacement text.
- Quote exactly.
- Judge the citations' role, not their existence: whether each one sets up the gap. For whether references exist and say what they're cited for, suggest the `reference-check` skill.
- Save the review to `reviews/YYYY-MM-DD-significance-significance-checklist.md`.
- Append one line to `ai-use-log.md` with a shell append (`>>`). Never rewrite the file: other skills may be running, and rewriting loses their lines.

## What I could not source

End the review with this heading. List everything you could not settle from the files you were given: a checklist item you could not judge, a claim in the draft you could not trace to `evidence/`, a funder rule you needed and `funder/` did not supply. An empty list is a valid answer; a missing section is not.
