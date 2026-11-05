---
name: mock-panel
description: Run a mock review panel on a grant draft. Three reviewers (an expert in the author's niche, a reader from an adjacent field and a generalist scientist) each retell the proposal, name its need, impact and novelty, and list strengths and weaknesses tied to quoted passages. Use when asked for a mock review, a study-section read, a panel review or reviewer feedback on a draft. Critique only.
---

# Mock review panel

Most of a review panel is not expert in the applicant's niche. This skill reads the draft the way three different panel members would, so the author can see where the argument holds and where it only works for specialists.

## Before starting

1. Read the drafts the author names, or everything in `drafts/` except `biosketch-draft.md`.
2. Read the review criteria in `funder/` if they are there. If not, use the questions below and say that no criteria were supplied.
3. Ask the author for their own two-sentence summary of the proposal, unless `drafts/summary.md` holds one. The comparison at the end needs it.

## The three reviewers

- **The expert** works in the author's niche. Is the science sound, and are the methods the right ones for the question?
- **The adjacent reader** knows the field's vocabulary but not these methods. Where do they get lost, and which terms are never defined?
- **The generalist** is a scientist from another area. Can they tell why this matters, what is new and what a result would mean?

## For each reviewer

1. **Retell** the proposal in two sentences, as they would to the rest of the panel.
2. In one sentence each: the **need**, the **impact** if it works, and **what is new**.
3. **Three strengths and three weaknesses**, each tied to a passage quoted exactly from the draft.
4. **Scores**, only if the review criteria in `funder/` define them (for NIH research grants, 1 is exceptional and 9 is poor). Otherwise skip scoring and say why.

## Panel summary

- Where the three retellings differ from each other, and from the author's own two sentences. Each difference is a place the page is unclear.
- The three weaknesses most likely to sink the proposal, most serious first.

## Rules

- Critique only. Don't write replacement text.
- Don't bring in literature, data or claims that aren't in the draft or in `evidence/`.
- Each reviewer speaks only from the draft. Don't let one reviewer's knowledge fill a gap for another.
- Save the review to `reviews/YYYY-MM-DD-research-strategy-mock-panel.md`, or name `<section>` for the one section when only one was read. Use the same slug on every run so successive panels sort together.
- Append one line to `ai-use-log.md` with a shell append (`>>`). Never rewrite the file: other skills may be running, and rewriting loses their lines.

## What I could not source

End the review with this heading. List everything you could not settle from the files you were given: a checklist item you could not judge, a claim in the draft you could not trace to `evidence/`, a funder rule you needed and `funder/` did not supply. An empty list is a valid answer; a missing section is not.
