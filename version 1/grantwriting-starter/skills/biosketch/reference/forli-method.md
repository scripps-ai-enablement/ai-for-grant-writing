# The Forli method

Stefano Forli (Scripps Research) built an agent that turns a set of Specific Aims plus a CV into the three biosketch sections. The `biosketch` skill follows his method; this file records the method itself, so the reasoning behind each step survives independently of the skill's wording.

The core of it is **paper selection**: matching the applicant's own publications to the scientific themes of this proposal, and then writing prose that draws only on the papers selected.

## The rule everything else rests on

> The biosketch must be tailored to the **actual aims the applicant gives you**, not to whatever program a pre-existing template was written for.

Templates get recycled from an unrelated proposal, and a recycled template arrives carrying the earlier proposal's paper choices and prose. Treat those as disposable and the template's **structure** as the only thing worth keeping. Re-derive the themes from the aims and re-select papers, even when that discards every paper the template used.

If the aims are missing, stop and ask. Never infer aims from a template: a template's aims are usually from a different proposal, and a guess there corrupts everything downstream.

## Themes

Read the aims and name the two to four scientific themes the proposal rests on. Most NIH proposals map onto their aims plus one cross-cutting theme covering infrastructure or track record, which is easy to miss because no aim states it. The themes become the buckets papers sort into and the backbone of the Contributions to Science.

## Selection

Score every plausibly relevant paper against the themes, then pick the strongest set, in this priority order:

1. **Relevance to a theme.** A perfectly positioned paper on an off-topic subject does not belong.
2. **Author position.** Last or corresponding author, then first author, over middle author.
3. **Venue.** More selective journals over less.
4. **Recency**, where papers are otherwise comparable.

Honor the applicant's own exclusions, which are judgments only they can make: a commentary rather than a full paper, a paper they would rather not foreground.

Aim for coverage. Every theme should be represented by at least one paper across the two lists. Where a theme is thin, say so instead of padding it with weak papers.

**State the mapping.** Which paper supports which aim or theme, and why it was chosen over the alternatives. This is the part the applicant most needs to check, and it is the part a draft will not reveal on its own.

## The two lists

- **Products closely related to the proposed project** — the methodological and scientific core that most directly delivers the aims. These are the papers the prose sections may reference.
- **Other significant products** — supporting infrastructure, adjacent methods and track-record work that establish breadth.

## Personal Statement

First person, at most 3,500 characters. The structure that works:

1. One or two sentences on overall expertise and training, framed toward this proposal's themes.
2. A paragraph per theme, each tying past work explicitly to the aim it supports: "...directly informs Aim 1, in which we will...".
3. A closing paragraph on leadership and resources — directorships, team expertise, commitment to open dissemination — that positions the applicant to execute.

## Contributions to Science

Up to five, each introduced by its own title rather than a number, and ordered with the contributions closest to this proposal's aims first. Each one: a short narrative of what the group did, the applicant's specific role, and a sentence connecting it to the aim it supports. Prose, not bullets; reviewers expect narrative. Keep any one paper's description brief. Where the form allows 2,000 characters, around 1,500 is the floor worth hitting.

## Consistency

The three sections are a set. When the selection changes, update the Products list, then re-scan both prose sections for any reference to a paper no longer listed and rewrite those passages. A dropped product must never survive as a reference elsewhere.

## Worked example, compressed

Aims on high-throughput docking of flexible receptors and large ligands, and on high-throughput binding free energy; the CV of a docking-methods PI.

Themes: flexible-receptor and large-ligand sampling; binding free energy; the docking-engine infrastructure that makes both feasible — the third being the cross-cutting theme no aim names.

Closely related products: the group's docking-engine paper (last author, recent), which serves the infrastructure theme and both aims; a GPU-acceleration paper for high-throughput sampling; a flexible-macrocycle docking paper (corresponding author) for Aim 1; an affinity-ranking paper and a free-energy fragment-screening paper for Aim 2.

Other significant: a parametrization toolkit, a docking-accuracy paper, a suite overview, a blind free-energy challenge paper, an affinity-maps tool.

Contributions: one on flexibility and large ligands, one on binding free energy, one on the engine and infrastructure, each drawing only on the closely related products.

This is illustrative. The papers always come from the applicant's own CV and aims.

## Source

Stefano Forli's `biosketcher` agent and its accompanying prompt and guidance notes, shared October 2026. The form requirements in `form-rules.md` come from the Biographical Sketch Common Form (OMB No. 3145-0279) and the NIH Biographical Sketch Supplement, and take precedence wherever the two differ.
