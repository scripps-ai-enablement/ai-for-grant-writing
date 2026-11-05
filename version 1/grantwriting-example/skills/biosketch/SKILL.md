---
name: biosketch
description: Draft the Personal Statement and Contributions to Science for an NIH-style biosketch from the author's Specific Aims, CV and a fixed list of their products, choose which products to list, check every limit with a counting script, and report each claim against its source. Use when asked to draft, build or update a biosketch. Never adds a product that isn't on the author's list, and never touches the certification sections.
---

# Biosketch

This skill drafts the parts of a biosketch that are structured and checkable. The author supplies the facts; the skill selects, arranges and counts. The method is Stefano Forli's (Scripps Research), recorded in `reference/forli-method.md` and updated for the 2026 NIH forms.

## Inputs

- The Specific Aims: `drafts/aims.md`.
- The CV: `evidence/cv.md`.
- The fixed list of products: `evidence/products.md`, with full citations and identifiers.
- The form rules: `reference/form-rules.md` in this skill, and any newer instructions in `funder/`, which take precedence.

If any input is missing, stop and ask for it. Don't work from memory of the author's career.

**A biosketch from a previous proposal is not an input.** If one is supplied, use it for layout only. Its paper choices and its prose were written for different aims, so re-derive both. Never infer the aims from it.

## Steps

1. **Themes.** Read the Aims and name two to five themes the project rests on. Derive them from this application's Aims, never from a previous biosketch. One theme is usually cross-cutting, covering infrastructure or track record, and no aim will state it.
2. **Products.** Choose only from `evidence/products.md`.
   - Up to five products closely related to the proposed project, and up to five other significant products that show the author's broader contributions.
   - Rank by relevance to the themes first, then the author's role (last or corresponding, then first, over middle author), then the venue, then recency.
   - Honor any exclusion the author has stated; those are their judgment to make.
   - Never add a product that isn't on the list. If a theme has no supporting product, say so rather than padding it with a weak one.
   - Where the PubMed connector is available, resolve each product's identifiers, since a PMID or DOI is not a PMCID. Never invent one. Mark anything unresolved as unconfirmed, for the author to supply.
3. **Personal Statement.** At most 3,500 characters, first person, in three parts: one or two sentences on training and expertise framed toward the themes; then a paragraph per theme tying past work to the aim it supports ("...directly informs Aim 1, in which we will..."); then a closing paragraph on leadership and resources. Draw every fact from the CV.
4. **Contributions to Science.** At most five, each at most 2,000 characters. For a graduate student or postdoc write two or three, which is what the NIH instructions suggest for someone at that stage, and say why those were chosen; three thin contributions read worse than two real ones. Give each its own title rather than a number, and order them with the contributions closest to these Aims first. Each covers the four things the form asks for: the background that frames the problem, the central findings, the author's specific role, and the influence of the findings, this last **only where the CV or the product list records it**. Where nothing records an influence, describe the contribution without one and name the gap in the check report rather than inventing uptake. Prose, not bullets, and no figures or tables; the form forbids them.
5. **References in the prose.** In-text parenthetical references to the listed products are allowed in both sections, as `(Chen et al., 2024)` or `(Product 3)`. Full bibliographic citations and links are not: no journal, volume, pages, PMID, DOI or URL in the running text. Reference only products that appear in the two lists.
6. **Count.** Write the draft to `drafts/biosketch-draft.md` using `templates/biosketch.md`. Then run `python3 skills/biosketch/scripts/count_chars.py drafts/biosketch-draft.md` and revise until every section is within its limit and no section is missing. Never estimate a count.
7. **Check report.** Give the paper-to-theme mapping first: which product supports which theme and aim, and why it was chosen over the alternatives the CV offered. Then list each factual claim in the draft with the CV line or product it rests on. Flag any claim without a source, any product tied to a theme it doesn't support, any unconfirmed identifier, and any requirement not met.
8. **What I could not source.** End the report with this heading and list everything the inputs did not settle: missing citation elements, impacts not recorded anywhere, any number the form rules require that `funder/` and the CV between them do not supply. An empty list is a valid answer; a missing section is not.

## Do not touch

Identifying information, professional preparation, appointments and positions, Honors, and the certification section (support, foreign talent programs, research security training). Only the applicant can attest to these. Say so in the report.

Two options the Personal Statement instructions offer are also the applicant's alone: an explanation of factors that affected past productivity, and a note that they have published under another name. Don't write either one, and don't ask about the first. Mention in the report that the form allows them.

## Rules

- Write `drafts/biosketch-draft.md` with this line at the top: "AI draft from the biosketch skill. Check every line before use."
- If products change, recheck every place they are mentioned so that no dropped product survives in the text.
- Don't use em dashes or en dashes; they read as machine-written. A comma, a parenthesis or a second sentence does the same work.
- Save the check report to `reviews/YYYY-MM-DD-biosketch-biosketch.md`, matching the `YYYY-MM-DD-<section>-<skill>.md` convention in `CLAUDE.md`.
- Append one line to `ai-use-log.md` with a shell append (`>>`). Never rewrite the file: other skills may be running, and rewriting loses their lines.
