---
name: aims-checklist
description: Review a grant's Specific Aims page against a writing checklist, item by item, quoting the sentence that meets each item or naming what is missing, then run a 60-second reviewer test. Use when asked to check, review or critique an Aims page. Critique only; never rewrites the page.
---

# Aims page checklist

## Which checklist to use

If `checklists/` holds a checklist for the Aims page, use it: it reflects the standard the author was taught or the funder sets. Otherwise use `reference/checklist.md` in this skill, and say so at the top of the review.

If `funder/` holds the announcement or instructions, note the mechanism and the page limit, and check the page against them.

## Steps

1. Read the Aims page: `drafts/aims.md` unless the author names another file.
2. Go through the checklist one item at a time. For each item give:
   - **status**: met, partly met, or missing;
   - **evidence**: the sentence that meets it, quoted exactly, or one line saying what is missing.
3. Run the 60-second reviewer test. From the page alone, answer each question in one sentence:
   - What is the problem?
   - What don't we know?
   - What is the hypothesis?
   - What will be done?
   - What do we gain if it works?

   Where the page doesn't let you answer, say so plainly. That is a finding, not a failure of the test.
4. List the five most important problems, most serious first, each in one or two sentences.

## Rules

- Describe problems; don't write replacement text. The author fixes the page.
- Quote exactly. Never paraphrase inside quotation marks.
- Don't add references, data or claims that aren't on the page or in `evidence/`.
- Save the review to `reviews/YYYY-MM-DD-aims-aims-checklist.md`.
- Append one line to `ai-use-log.md` with a shell append (`>>`). Never rewrite the file: other skills may be running, and rewriting loses their lines.

## Output

A table of checklist items (item, status, evidence), the five answers from the reviewer test, then the numbered list of problems.

## What I could not source

End the review with this heading. List everything you could not settle from the files you were given: a checklist item you could not judge, a claim in the draft you could not trace to `evidence/`, a funder rule you needed and `funder/` did not supply. An empty list is a valid answer; a missing section is not.
