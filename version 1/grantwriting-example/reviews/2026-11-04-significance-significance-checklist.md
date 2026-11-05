# Significance and Innovation: significance-checklist review

- **Date:** 2026-11-04
- **Skill:** `skills/significance-checklist/SKILL.md`
- **Checklist used:** `checklists/` holds only its README, so this review uses the checklist stored in the skill, `skills/significance-checklist/reference/checklist.md`.
- **Funder criteria:** `funder/PAR-09-219.md`, Section V, the Significance and Innovation criteria this application was reviewed under. `funder/nih-scoring.md` notes that for due dates on or after 25 January 2025 the two are scored together as one factor; this review uses the 2012 criteria, as the folder does.
- **Sections reviewed:** `drafts/significance.md` and `drafts/innovation.md`, which the skill reads together, with `drafts/aims.md` for alignment. `drafts/approach.md` and `drafts/figures/` were read only for the figure item, the buried-innovation pitfall and passages that contradict these two sections.
- **Not used:** web search or fetch. Every link in the drafts is unchecked.

This is a critique. It quotes the drafts exactly and describes problems; it does not offer replacement text.

## How the funder scores these sections

PAR-09-219 tells reviewers that an R21 "need not have extensive background material or preliminary information" and that they "will focus their evaluation on the conceptual framework, the level of innovation, and the potential to significantly advance our knowledge or understanding." It also says that "projects designed to increase knowledge in a well-established area will not be considered for R21 awards." A short background is therefore not a fault here; an unclear gap and an unclear novelty are.

| PAR-09-219 criterion question | Where the draft answers it | Status |
|---|---|---|
| **Significance:** an important problem or a critical barrier to progress? | Problem: "there are few clinically useful genomic predictors". Barrier: "no effective method for integrating the knowledge that this represents with experimental data has been released" | Problem stated; barrier asserted, not argued |
| How will knowledge, capability or practice be improved? | "significantly better predictors", "adapted to clinical use", "a pattern and toolset" | Answered, overclaimed |
| How will completion change the concepts, methods or technologies that drive the field? | "a pattern and toolset for translating genomic data into clinically relevant knowledge using the power of crowdsourcing" | Answered |
| Exploratory, high risk/high impact? | Impact claimed; risk never named. Neither "risk" nor "exploratory" appears in either section | Half answered |
| Will it lead to subsequent or extended research? | "They will also prime further basic research into the underlying mechanisms driving the discovered signatures." | Partly answered |
| Interoperability and data sharing, when relevant? | Not in Significance | Not addressed in this section |
| **Innovation:** challenge or shift a paradigm? | "alters the process ... from a passive one ... to an active one" | Answered, hedged |
| Novel to one field, or novel in a broad sense? | Not in Innovation | Not answered |
| Refinement, improvement or new application? | Not in Innovation | Not answered |
| Develop or employ novel computational tools in this area? | "a mechanism to rapidly, inexpensively and directly capture targeted biological knowledge from domain experts" | Answered in general terms; the tool is not named |

## Checklist summary

| # | Item | Status |
|---|---|---|
| 1 | Background tells a coherent story, citing what is directly relevant | Partly met |
| 2 | Rigor of the key prior studies is addressed | Missing |
| 3 | A figure summarizes current thinking and where the problem sits | Missing |
| 4 | Ends on the specific need this project addresses | Partly met |
| 5 | The gap is a specific unknown, and the text says why it blocks progress | Partly met |
| 6 | Evidence the need is real, and why it exists | Partly met |
| 7 | Significance stated plainly enough to find quickly | Partly met |
| 8 | Who benefits and what changes in the field | Met |
| 9 | Tied to the funder's mission | Partly met |
| 10 | What is new is stated in the first paragraph | Partly met |
| 11 | Contrasted with what exists, and why it is better | Partly met |
| 12 | Builds on established principles, treats prior work with respect | Partly met |
| 13 | Tied to the aims and to the gap named in Significance | Partly met |
| 14 | Fits the funding opportunity | Partly met |

## Checklist, item by item

### Scientific premise

**1. The background tells a coherent story of where the field stands, citing what is directly relevant. Partly met.**

The first Significance paragraph is a coherent arc with three relevant citations: predictors are wanted, few are clinically useful, the best known covers only some tumors, and a 2012 contest shows the problem is open.

> "Despite extended and intense research in a variety of areas, there are few clinically useful genomic predictors."

The part of the story that explains *why* predictors fail is not here. It is in Innovation ("The predictors generated with this approach consistently have problems in secondary and tertiary validation studies and in the stability of the genes selected using different training datasets [4].") and on the Aims page ("This is, in part, because the combinatorial space of independent variables generated by genome-scale methods is so large."). The opening sentence, "Many studies attempt to use gene expression information to predict the progression of various types of cancer as well as other complex diseases.", has no citation.

**2. The rigor of the key prior studies is addressed. Missing.**

Significance does not say how strong the evidence is for anything the proposal builds on. Innovation comes closest, but it describes the weakness of existing predictors, which is the problem, not the strength of the work the proposal rests on, and the sentence carries no citation:

> "In doing so, they have made minor improvements in predictive accuracy but yield far more consistent results in terms of the genes that are identified for the same phenotype but different datasets."

The evidence the proposal leans on most, that players' gene choices improve predictors, is one week of play in The Cure, reported in Approach. Its dataset is not named and the analysis is not in this folder (`evidence/preliminary-data.md`). PAR-09-219 as stored in `funder/` does not ask for an assessment of the rigor of prior research, so this item is judged against the built-in checklist only.

**3. A figure is planned that summarizes current thinking and shows where the problem sits. Missing.**

Neither section has or mentions a figure. The two figures in the Research Strategy, both in Approach, are "Figure 1. A round of The Cure" and "Figure 2. Genes selected by game players" (`drafts/figures/README.md`); neither shows the state of the field. The five-step "standard paradigm" that opens Innovation is given in prose only. The Research Strategy "may not exceed 6 pages, including tables, graphs, figures, diagrams, and charts" (PAR-09-219), so whether a figure fits is the author's call.

**4. It ends on the specific need or problem this project addresses. Partly met.**

The background paragraph ends on a general verdict rather than the need:

> "Though there has unquestionably been progress in the past decade, it has been incremental at best."

The specific need arrives in the next paragraph, after "We suggest that a fundamentally new methodology is needed to make significant strides on this difficult problem." The section as a whole ends on the educational value of games.

### Significance

**5. The gap is a specific unknown, and the text says why it blocks progress. Partly met.**

The closest sentence names a missing method rather than an unknown, and does not say why its absence keeps predictors inaccurate:

> "Since 2002, more than 126,000 publications related to breast cancer have been added to PubMed (http://tinyurl.com/bc-pubs) but, to date, no effective method for integrating the knowledge that this represents with experimental data has been released."

The proposal does state a specific unknown, but on the Aims page: "What is not known is whether the emerging paradigm of scientific crowdsourcing through games can be extended to help address the challenge of translating genome-scale data into useful predictive models." Its reason for why the gap blocks progress is in Innovation: "We contend that this is due in part to the lack of relevant structured knowledge to compute with." Neither appears in Significance.

**6. There is evidence that the need is real, and an explanation of why it exists. Partly met.**

The evidence that the need is real is the Oncotype DX limitation [2] and the SAGE contest:

> "As a case in point, in the summer of 2012, ten years after the first major attempts to produce genomic predictors of breast cancer prognosis [3], SAGE Bionetworks launched a large-scale public contest to spur research in this area because suitably accurate predictors still had not been found (http://tinyurl.com/sage-bcc)."

The contest is the strongest piece and rests on a shortened link alone. Why the need exists is not explained in Significance (see item 1).

**7. The significance is stated plainly enough that a reviewer can find it quickly. Partly met.**

It can be found, but it is the fourth sentence of the second paragraph and four more impact claims follow it:

> "If successful, this contribution will result in significantly better predictors of breast cancer progression and has the potential to make major, disruptive improvements in genomic medicine."

**8. It says who benefits and what changes in the field if the project succeeds. Met.**

Patients: "Better disease predictors will be adapted to clinical use to personalize and thereby improve patient treatment." Basic researchers: "They will also prime further basic research into the underlying mechanisms driving the discovered signatures." Methods developers: "At a purely methodological level, this work will result in a pattern and toolset for translating genomic data into clinically relevant knowledge using the power of crowdsourcing." Learners: "the crowdsourcing mechanism we employ (games) provides an outstanding educational avenue for biologists from related disciplines, for students, and for interested members of the general public." The beneficiaries are named; the scale claimed for them is the problem (see Overreach).

**9. It ties the work to the funder's mission. Partly met.**

The toolset sentence matches PAR-09-219's support for "development of new computational tools and technologies" and its wish that approaches be "generalizable, scalable, extensible, and interoperable". The section never says the work is exploratory or high-risk, and it opens on a decade-old clinical problem, "ten years after the first major attempts", with the new area, the method, second. A reviewer could read that framing as the kind of project the announcement excludes: "projects designed to increase knowledge in a well-established area".

### Innovation

**10. What is new is stated in the first paragraph. Partly met.**

It is in the first paragraph, but as its last sentence, after about 250 words on existing methods, and it is hedged:

> "The proposed research is innovative, in our opinion, because it alters the process of assembling genomic predictors informed by community knowledge from a passive one that is entirely dependent on the growth of external, general purpose databases to an active one that offers the potential to rapidly generate focused knowledge bases oriented specifically around solving the problem at hand."

The section never names the method. Neither "game" nor "crowdsourcing" appears in `drafts/innovation.md`. A reviewer reading Innovation alone learns that knowledge will be captured "from domain experts" but not how.

**11. It is contrasted with what exists, and the text says why it is better. Partly met.**

The contrast with computational methods is specific: the five-step paradigm, then the knowledge-based methods [5]–[8], then "passive" databases against an "active" knowledge base. Two things are missing. First, there is no contrast with the existing scientific games that the Aims page describes ("Crowdsourcing through games has recently been used successfully to rapidly inject large-scale human knowledge and reasoning ('human computation') into frameworks for solving biological problems involving massive search spaces including: protein structure determination, multiple sequence alignment, and RNA structure design."), so the reader is not told whether the new thing is games in biology or games for building genomic predictors. Second, the only reason given that it is better is scale, and that is asserted:

> "The diversity of prior knowledge and intuition captured by expanding the pool of contributing scientists will provide predictors that are more effective than could be achieved by prior methods."

**12. It builds on established principles and treats prior work with respect. Partly met.**

The knowledge-based methods get a fair hearing: "These methods guide the search for predictive gene sets towards groups that are biologically meaningful." Other prior work is dismissed without evidence:

> "While previous studies from major institutions might legitimately be able to draw on the expertise of upwards of 10 scientists, we will be able to elegantly tap into a hive mind that is one or even two orders of magnitude larger."

The principle the method depends on, that crowd contributions can be weighted for quality and aggregated, is denied here ("should such an army of minds somehow be raised there are no established techniques for processing the diverse and noisy knowledge that they could offer") and affirmed in Approach. See problem 3.

**13. It is tied to the aims and to the gap named in Significance. Partly met.**

"The proposed research seeks to provide a mechanism to rapidly, inexpensively and directly capture targeted biological knowledge from domain experts that can be used immediately to improve the inference of genomic predictors." maps onto both aims in general terms, but neither aim is named and Aim 1's game is never mentioned. The gaps do not line up: Significance says "no effective method for integrating the knowledge that this represents with experimental data has been released"; Innovation says such methods exist [5]–[8] and are held back by "the lack of relevant structured knowledge to compute with". The endpoint also shifts: Innovation's predictors are "of breast cancer metastasis", where Significance and the Aims say "progression".

**14. It fits the funding opportunity. Partly met.**

It fits PAR-09-219's interest in new computational tools and in work that will "exceed the current state of the art". It does not answer the Innovation criterion's question "Are the concepts, approaches or methodologies, instrumentation, or interventions novel to one field of research or novel in a broad sense?", and it does not address the generalizability the announcement asks of every project. The Aims page does ("The resultant open source software and validated design patterns will also allow other researchers to apply this new methodology within other biological contexts."); Innovation does not carry it forward.

## The gap test

Significance has two paragraphs. Both were tested, because the first carries the problem and the second the only gap sentence.

**Paragraph 1: fails.** With "cancer", "breast cancer", "Oncotype DX®" and "ER-positive, lymph node-negative" removed, it says that gene-expression predictors are wanted, few are clinically useful, the best-known one covers only some patients, a contest was launched because accurate predictors had not been found, and progress has been "incremental at best". That says the problem is still open. It does not say what is unknown or what keeps the predictors inaccurate.

**The gap sentence in paragraph 2: partial pass.** With "breast cancer" removed, "no effective method for integrating the knowledge that this represents with experimental data has been released" still names something missing. But it names the absence of a method, which is the absence of the proposed solution, rather than an unknown; it does not say why that absence is what keeps predictors inaccurate; and the publication count beside it measures the size of the field rather than the gap.

The sentence in the application that passes cleanly is on the Aims page ("What is not known is whether ..."). Nothing in Significance corresponds to it.

## The restate test

These restatements test whether the draft can be summarized. They are not proposed text.

- **Need.** Genomic predictors of breast cancer progression are still not accurate enough for most patients, and nothing yet brings what biologists know to bear on building them. *Possible, but only by joining a sentence from each paragraph; Significance links the two with "We suggest" rather than an argument.*
- **Impact.** *Could not restate in one sentence without choosing.* Significance lists six outcomes without ranking them: better predictors, "major, disruptive improvements in genomic medicine", clinical use, further basic research, "a pattern and toolset", and education. The one that matches the Aims' expected outcomes and a two-year R21, the toolset, is fourth.
- **What is new.** A game that collects targeted, gene-level judgments from many biologists and feeds them into predictor inference, in place of general-purpose curated databases. *Possible only by combining Innovation with the Aims page; Innovation itself never says "game".*

## Pitfalls

- **The disease, not the gap: present, mild.** Paragraph 1 does not dwell on disease burden; it sells how long the problem has been open ("ten years after the first major attempts", "incremental at best"). The publication count does the same job in paragraph 2: "Since 2002, more than 126,000 publications related to breast cancer have been added to PubMed".
- **The literature dump: not found.** Significance cites three references and two links; Innovation cites five references.
- **Overreach: present.** "If successful, this contribution will result in significantly better predictors of breast cancer progression and has the potential to make major, disruptive improvements in genomic medicine." "Better disease predictors will be adapted to clinical use to personalize and thereby improve patient treatment." "The predictors inferred using this approach will be fundamentally different from those produced through other means because they will represent the distributed biological insights of an unprecedented number of biologists." These are claimed for a project capped at two years and $275,000 in direct costs (PAR-09-219), whose own Aims page says only that the work "is expected to generate better predictors".
- **Unearned "novel" or "first": present.** "In this proposal, we introduce a novel, crowdsourcing-based approach that taps into massive, unused reservoirs of biological knowledge and human intuition." Significance offers no contrast with other crowdsourcing, and "unused" sits against Innovation's own account of methods driven by structured prior knowledge. Innovation's "an unprecedented number of biologists" has no source.
- **Buried innovation: present.** Innovation never names games or crowdsourcing. Significance mentions games once, in parentheses, in its last sentence: "the crowdsourcing mechanism we employ (games)". The concrete new pieces, judging players by "embedded challenges with known answers", weighting by player ability and aggregating by voting, appear only on the Aims page and in Approach.
- **Novelty for its own sake: not found as such.** Innovation gives a reason the method matters ("the lack of relevant structured knowledge to compute with"). The weaker link is why a larger crowd yields better predictors, which is asserted (item 11).

## The citations' role

This judges what each citation does for the gap, not whether it exists. `evidence/references.md` records that [1]–[8] exist and match the citations as submitted; whether each supports its sentence is unchecked, because no full text is in the folder. Run the `reference-check` skill for that.

| Citation | Cited for | Role in setting up the gap |
|---|---|---|
| [1] Ross et al. 2008 | Oncotype DX "is among the most widely used" | Background. Shows what has worked; sets up the gap only by contrast |
| [2] Weigelt et al. 2012 | the ER-positive, lymph node-negative limit; research "remains highly active" | The one citation in Significance that bears on the need. It is used to show activity, not to explain why signatures fail, although its title is "Challenges translating breast cancer gene signatures into the clinic" |
| [3] van 't Veer et al. 2002 | "the first major attempts" | A date marker for "ten years after". Does not bear on the gap |
| tinyurl.com/sage-bcc | the 2012 contest and why it was launched | The strongest evidence the need is real. Not in evidence/ |
| tinyurl.com/bc-pubs | 126,000 publications since 2002 | Shows the literature is large, not that it is unused or that leaving it unused blocks progress. Not in evidence/ |
| [4] Xu and Wong 2010 | problems in validation and gene-set stability | The citation that most directly explains why predictors fail, the "why it blocks progress" half of the gap. It is in Innovation, not Significance |
| [5, 6] Dutkowski and Ideker 2011; Winter et al. 2012 | methods using protein-protein interaction networks | The contrast: what exists |
| [7, 8] Bild et al. 2006; Su et al. 2009 | methods using "pathway databases" | The contrast. The titles ("Oncogenic pathway signatures...", "...probabilistic inference of pathway activity") do not settle whether either uses a pathway database; reference-check should look |
| none | "minor improvements in predictive accuracy but ... far more consistent results" | A specific result with no citation attached |
| none | "upwards of 10 scientists" | A characterization of other groups with no source |

Approach cites "[5, 8, 20]" for the same knowledge-based methods that Innovation cites as [5]–[8]. The two sets differ, and [20] (Chuang et al. 2007, "Network-based classification of breast cancer metastasis") is the only one whose title names breast cancer.

## Problems, most serious first

The first five are the most important.

1. **Significance never says what is unknown or why it blocks progress.** Paragraph 1 shows predictors are still inadequate; paragraph 2 asserts that a method is missing and announces the authors' approach. A reviewer scoring "a critical barrier to progress in the field" from this section finds the problem and the solution but not the barrier between them. The application's specific unknown is on the Aims page ("What is not known is whether the emerging paradigm of scientific crowdsourcing through games can be extended ...") and its causal argument is in Innovation ("We contend that this is due in part to the lack of relevant structured knowledge to compute with."), with the key citation for it, [4].

2. **The impact claimed is out of proportion to a two-year exploratory R21, and the risk is never named.** "will result in significantly better predictors", "major, disruptive improvements in genomic medicine" and "will be adapted to clinical use to personalize and thereby improve patient treatment" are stated with certainty, while PAR-09-219 asks "Does this represent exploratory, high risk/high high impact research?" Neither section mentions risk. Opening on a decade-old clinical problem also invites the reading the announcement excludes: "projects designed to increase knowledge in a well-established area".

3. **The sections contradict each other on what already exists.** Significance says "to date, no effective method for integrating the knowledge that this represents with experimental data has been released" and calls the knowledge "massive, unused reservoirs". Innovation says "methods driven by structured prior knowledge in the form of protein-protein interaction networks [5, 6] and pathway databases [7, 8] have been introduced" and "yield far more consistent results"; the Aims page says "Knowledge-based techniques are useful for targeting this search"; and Approach says "Many technical approaches now exist that use these databases to help infer expression-based cancer predictors with improved performance [5, 8, 20]." Separately, Innovation says "there are no established techniques for processing the diverse and noisy knowledge that they could offer", while Approach says "Such techniques have repeatedly been shown to generate high quality data from crowdsourcing applications on tasks ranging from general text annotation [23] to medical image annotation [21]" and that they "provide a body of techniques that can be adapted". A reviewer reads the denials first and the citations later.

4. **Innovation does not name the method or contrast it with the nearest precedent.** "Game" and "crowdsourcing" never appear in it; the innovation sentence is the last of a long paragraph and is qualified "in our opinion"; and the only contrast is with computational pipelines. The scientific games the Aims page cites for protein structure, sequence alignment and RNA design are not mentioned, so the funder's question "novel to one field of research or novel in a broad sense?" goes unanswered, and the reader has to work out from the Aims page that the novelty is extending games to building genomic predictors.

5. **The scale argument that carries Innovation rests on numbers the folder cannot support.** "literally hundreds or thousands of biologists", "upwards of 10 scientists", "one or even two orders of magnitude larger" and "an unprecedented number of biologists" have no source. The only participation figure for the authors' own game, The Cure, is that "more than 120 players registered" in the first week (Approach), and Approach also reports that "in preliminary studies this effect was observed with the majority of game-play happening quickly after launch." The step from a larger crowd to better predictors is asserted ("will provide predictors that are more effective than could be achieved by prior methods") rather than argued.

Lesser problems:

6. **Two load-bearing facts rest on shortened links.** The SAGE contest and the PubMed count are supported only by tinyurl.com addresses, which a reviewer cannot read before clicking, and the count gives no search query. Neither source is in `evidence/`.
7. **The set-up and the method do not quite meet.** The publication count sets up a gap in integrating the literature, but the method captures what players know. Approach says the game supplies "Extensive information from the Gene Ontology, RefSeq, Entrez Gene and PubMed", which may be the bridge; Significance does not say so.
8. **Six impacts, unranked, ending on education.** The outcome the Aims page promises, "a re-usable framework for capturing and applying community intelligence in biology", is fourth in Significance as "a pattern and toolset", and the section closes on "an outstanding educational avenue".
9. **The endpoint changes name.** Predictors are of breast cancer "progression" (Significance, Aims), "prognosis" (Significance), "metastasis" (Innovation) and "10-year survival" (Approach, Preliminary Data). A reviewer may ask which one the project targets.
10. **Boilerplate and tone.** "Despite extended and intense research in a variety of areas", "has the potential to make major, disruptive improvements in genomic medicine" and "an outstanding educational avenue" are boilerplate. "incremental at best", "elegantly tap into a hive mind", "army of minds" and "upwards of 10 scientists" read as dismissive of other groups, which bears on item 12.
11. **No figure for the premise** (item 3).

## What I would have asked the author

The author was not available, so these were not asked. The review proceeds on the answers noted.

1. The request named only Significance. The skill reviews Significance and Innovation together, so both are reviewed here. Was Innovation wanted?
2. Which outcome do the predictors target: progression, prognosis, metastasis or 10-year survival?
3. Was Innovation's "there are no established techniques for processing the diverse and noisy knowledge" meant to exclude the crowdsourcing quality methods that Aim 2 cites [21, 23] and says "can be adapted"?
4. What PubMed search produced the 126,000 count, and where does "upwards of 10 scientists" come from?
5. Is a figure planned for the premise, and how much of the 6-page Research Strategy is free?
6. The rules limit review to the author's own drafts. The folder's README names Andrew Su as PI and Benjamin Good as Co-Investigator on this application; the review proceeds because the request calls it "my Significance section" and the folder holds one proposal.

## What I could not source

1. **The SAGE Bionetworks contest:** its timing, its scale and the motive the draft gives it ("because suitably accurate predictors still had not been found"). The only source is http://tinyurl.com/sage-bcc; not in evidence/. `evidence/preliminary-data.md` lists the challenge page as "not in this folder".
2. **"more than 126,000 publications related to breast cancer have been added to PubMed" since 2002:** the only source is http://tinyurl.com/bc-pubs; the query and count are not in evidence/.
3. **Uncited claims in Significance:** "Many studies attempt to use gene expression information to predict the progression of various types of cancer as well as other complex diseases", "there are few clinically useful genomic predictors", "incremental at best", "no effective method for integrating the knowledge that this represents with experimental data has been released" and "massive, unused reservoirs of biological knowledge and human intuition". Not in evidence/.
4. **Whether the cited papers support their sentences:** [1] for Oncotype DX being "among the most widely used", [2] for the ER-positive, lymph node-negative limit, [3] as "the first major attempts", [4] for the validation and stability problems, and [5]–[8] as methods using interaction networks and pathway databases. `evidence/references.md` confirms the records exist; no full text is in the folder, so support is unchecked.
5. **"they have made minor improvements in predictive accuracy but yield far more consistent results"** and **"they have not yet produced substantially greater accuracy than other approaches"** (Innovation): no citation attached; not in evidence/.
6. **The Innovation numbers:** "upwards of 10 scientists", "literally hundreds or thousands of biologists", "one or even two orders of magnitude larger" and "an unprecedented number of biologists". Not in evidence/. The only participation figure for The Cure is the first-week count in Approach, and its game logs and survey are "not in this folder" (`evidence/preliminary-data.md`).
7. **The rigor of the evidence the proposal builds on (item 2):** the preliminary result (65% against 55% accuracy) cannot be judged because the dataset is not named and the analysis is not in the folder. PAR-09-219 as stored does not ask for this assessment, so the item rests on the built-in checklist alone.
8. **Page budget:** whether the Research Strategy fits PAR-09-219's 6-page limit, and so whether a premise figure would fit, cannot be judged from Markdown.
