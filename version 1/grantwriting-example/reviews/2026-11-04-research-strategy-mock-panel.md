# Mock review panel: Research Strategy and supporting sections

- **Date:** 2026-11-04
- **Skill:** `skills/mock-panel/SKILL.md`
- **Drafts read:** every file in `drafts/`: `aims.md`, `significance.md`, `innovation.md`, `approach.md` (with both figures), `summary.md`, `project-summary.md`, `facilities.md`, `personnel.md`, `resource-sharing.md`. `biosketch-draft.md` is excluded by the skill, and it is not in `drafts/` anyway.
- **Also read:** `funder/` (all three files), `evidence/` (all files, including both biosketches, for the Investigator(s) criterion), `checklists/README.md`.
- **Critique only.** No draft text was changed and no replacement text is offered.

## Before starting

**Review criteria.** `funder/PAR-09-219.md` defines an Overall Impact score and five scored core criteria (Significance, Investigator(s), Innovation, Approach, Environment), and `funder/nih-scoring.md` gives the 9-point scale (1 exceptional, 9 poor, whole numbers only). Each reviewer scores against those. The announcement also tells R21 reviewers how to weight things, and the panel followed it: "reviewers will focus their evaluation on the conceptual framework, the level of innovation, and the potential to significantly advance our knowledge or understanding. Reviewers will place less emphasis on methodological details and certain indicators traditionally used in evaluating the scientific merit of R01 applications, including supportive preliminary data."

**Criteria in force today.** `funder/nih-scoring.md` notes that for due dates on or after 25 January 2025 NIH uses a simplified framework (NOT-OD-24-010). The scores here use the 2012 criteria the application was reviewed against. A resubmission now would need re-scoring.

**Checklists.** `checklists/` is empty apart from its README, so no course checklist was applied.

**The author's two sentences.** `drafts/summary.md` holds two sentences, copied word for word from the Project Summary according to the comment at its top. The panel used them as the author's summary.

**What I would have asked the author.** The author was not available, so I went ahead with what the folder holds. I would have asked:
1. Are the two sentences in `summary.md` still how you would summarize the proposal, or were they copied in to fill the file? The comparison at the end is only as good as those sentences.
2. Did you want the whole application read, or only the Research Strategy? I read everything in `drafts/`.
3. Which dataset do the 65% and 55% cross-validation figures come from, and is it the same data that produced the players' in-game scores? Reviewer 1's main point depends on the answer.
4. Does Figure 2 hold eighteen genes or twenty?

The folder's README records how the application fared. The panel did not use that, and the scores below are not a prediction of it.

---

## Reviewer 1: the expert

Works on knowledge-guided genomic outcome predictors and on crowdsourcing in biology, which is the applicants' niche.

### Retelling

The team built a pilot game, The Cure, in which players pick five genes from a 25-gene board and are scored by how well decision trees built on those genes predict breast cancer survival. They want two years to turn it into a polished game for biologists (Aim 1) and to build methods that weight players by skill, pool their gene choices and feed them to a classifier (Aim 2), on the claim that crowd-chosen genes will beat data alone. The application never says better than what, on which endpoint, or by how much.

### Need, impact, what is new

- **Need:** Expression-based predictors of breast cancer outcome are few and unstable across datasets, and knowledge-guided methods are limited by what general-purpose databases hold.
- **Impact if it works:** A demonstrated way to turn many biologists' gene choices into features that measurably improve outcome prediction, released as reusable software.
- **What is new:** Collecting targeted, problem-specific prior knowledge from many biologists through a game and weighting it by player skill, where existing methods take priors passively from curated networks and pathway databases.

### Strengths

1. **The gap is located where an expert would put it: in the priors, not the classifier.** The Innovation section sets out the standard pipeline step by step, "(1) assemble a discovery/training dataset, (2) rank attributes according to some univariate statistic, (3) select the top N arbitrarily, (4) select a classification algorithm, (5) evaluate performance in cross-validation experiments and on external test datasets", and gives a fair account of what knowledge-based methods have and have not done: "In doing so, they have made minor improvements in predictive accuracy but yield far more consistent results in terms of the genes that are identified for the same phenotype but different datasets." It does not oversell the competition, so the opening for a new source of priors is believable.
2. **A working pilot, tested beyond its training data.** The game already exists and drew play ("more than 120 players registered and collectively played more than 2000 games"), and the gene combinations were tested in "(1) the training dataset used in the game, (2) a validation cohort from the same study, and (3) an independent validation set from a completely different study." For an R21, where preliminary data are optional, that is more than reviewers expect, and the instinct to test on an independent study is the right one.
3. **The quality-control toolkit is the right one, and the applicants name their own main threat.** Aim 1 adds "embedded challenges with known answers that we can use to judge player proficiency", and Aim 2 draws on crowdsourcing practice in which results are "assessed based on the contributor's performance on tasks where the answer is known and on the degree of consensus that exists between different responses to the same task from different contributors." The Aim 2 pitfalls paragraph raises overfitting unprompted: "it is conceivable that highly motivated players could identify those datasets, use them to select gene sets that would overfit them and then use these gene sets to score well in the game without contributing any knowledge of value." That candor counts in its favor.

### Weaknesses, most serious first

1. **Neither the pilot nor the plan separates knowledge from score-chasing.** Players are scored "by using labeled training data to infer and test decision tree classifiers that predict survival time using expression and CNV data from just the selected genes", and "The better the gene set performs in generating predictive decision trees, the higher the score." A player with no biology can climb by trial and error, so a gene's selection frequency may encode the training labels rather than anyone's knowledge. The pilot then reports "an accuracy of 65% in 10-fold cross-validation" for the top genes without saying whether that cross-validation ran on the data that produced the players' scores. If it did, the result is circular. Several other gaps leave the result unreadable:
   - The only baseline is "randomly selected genes (55%)", not the univariate ranking the Innovation section names as the standard paradigm, so the pilot does not show that players beat step (2) of that pipeline.
   - No class balance is given, so 65% cannot be read against the majority-class rate.
   - The "exhaustive search through the top 10 genes" does not say how many combinations were searched or whether the ten kept were chosen using the validation cohorts.
   - The draft has a comparison to hand, "players that declared knowledge of cancer" against everyone else, and does not report it.

   The applicants treat overfitting only as deliberate cheating, "Though conceivable, in our opinion the chances of this are very low", but the scoring makes it the default way to play. Part of the fallback rests on "new datasets that we will have advanced access to", and the summary of that letter in `evidence/` does not mention datasets or advance access. This is the central hypothesis, and as designed it cannot fail cleanly.
2. **There is no benchmark for success, and the endpoint shifts.** The target is "predictors of breast cancer progression" in the Aims, "10-year survival" and "survival time" in the Preliminary Data, "breast cancer metastasis" in Innovation and "breast cancer prognosis" in the Aim 2 Expected Outcomes. No subtype is named, although Significance faults the leading test because "its effective application is limited to ER-positive, lymph node-negative tumors". Aim 2 is expected to produce "a functional computational framework for merging the knowledge extracted collectively from the player community with genomic data to generate accurate predictors of breast cancer prognosis". It gives no accuracy to reach, no comparator (a data-only pipeline, or the network and pathway methods cited as [5-8, 20]) and no named test set. The announcement asks "Are potential problems, alternative strategies, and benchmarks for success presented?" For both aims, the answer is no.
3. **Skill weighting is borrowed from tasks that have right answers, and the timeline gives it little real data.** The feasibility argument rests on tasks "ranging from general text annotation [23] to medical image annotation [21]", where a correct label exists. Which genes predict breast cancer outcome is exactly what nobody knows, and the draft never says what the "embedded challenges with known answers" would be for a gene-selection task. Real play arrives late: "Broad deployment and promotion" occupies months 13-18 only, and "Generate hybrid predictor" runs in months 13-24. The pilot already showed "the majority of game-play happening quickly after launch", so the data for weighting and for the hybrid predictor would arrive in one burst in the second year. Aim 2 work before month 13 would rest on simulations built from assumptions such as "we know that, almost without question, the distribution of time spent per player on game play will follow a power law".

### Scores

| Criterion | Score | Reason |
|---|---|---|
| Significance | 3 | An important, well-framed problem, but the path to clinical use is asserted rather than argued |
| Investigator(s) | 3 | Strong record in community intelligence (two Su R01s on BioGPS and the Gene Wiki; Good built The Cure). No key person brings breast cancer biology or outcome statistics; that expertise sits in letters with no defined role |
| Innovation | 2 | Actively capturing problem-specific priors from a crowd is a real shift from passive database priors |
| Approach | 6 | The central test cannot separate knowledge from score feedback, and there are no success benchmarks |
| Environment | 2 | The compute described and the BioGPS audience suit the project well |
| **Overall Impact** | **5** | High-value idea; the design as written cannot show that the crowd contributed knowledge |

---

## Reviewer 2: the adjacent reader

Works in cancer genomics, so is at home with expression profiling, classifiers, cross-validation and prognosis, but has never worked on crowdsourcing or games.

### Retelling

They want to build an online game in which biologists pick sets of genes, and to use the genes players favor to build better gene-expression predictors of breast cancer outcome. A pilot drew over 120 players in a week and a predictor using the players' genes did well in a public prognosis challenge, but I could not follow how, in the new work, player choices get weighted and combined into the final predictor.

### Need, impact, what is new

- **Need:** Few gene-expression predictors are clinically useful, and existing ways of adding prior knowledge depend on general-purpose databases.
- **Impact if it works:** Better breast cancer outcome predictors, and a method other groups could reuse for other diseases.
- **What is new:** A game as the instrument for collecting biologists' judgments about which genes matter.

### Strengths

1. **The pilot game is concrete enough to picture.** "In this game the player competes with a computer opponent to select the highest scoring set of five genes from a board containing 25 different genes." Together with Figure 1, an outsider to games can see what a player does and what data a round produces.
2. **The validation logic in Aim 2 is familiar and sound.** "Different approaches will be tested empirically by training the models on discovery datasets and evaluating them on multiple independent test datasets (see the datasets mentioned in the letter of support from Obi Griffith)." The letter, as summarized in `evidence/`, says the database of "nearly 1400 publicly available breast cancer expression data with clinical outcomes" has already been shared. A genomics reader trusts this part.
3. **Recruitment starts from an audience the team already has.** "we will leverage the BioGPS website to directly solicit players via postings on the home page (which is viewed 2 million times per year by more than 125,000 unique visitors) and direct emails to the more than 5,000 registered users [18]." For a reader who cannot judge game design, this gives the question of whether anyone will play a concrete answer.

### Weaknesses, most serious first

1. **The core machinery of Aim 2 is named, not described.** The hypothesis is "that factors pertaining to participant's abilities can be detected and used to appropriately weight data quality, that aggregation strategies such as voting can be used to compute accurate confidence estimates in assertions made by the community". I could not tell what an "assertion" is in a game where players pick genes, or what players would be voting on. The methods do not resolve it: "In (B) we will use voting schemes modeled after prior studies regarding the assembly of high quality data from crowdsourcing [23]", and "In this phase we will explore a variety of strategies to construct the most effective predictor based on all available data." The "hybrid predictor" is never defined, and the nearest model is a pointer, "(See 'Network Guided Forests' for a related example [5].)", with no explanation. From the page I cannot rebuild the path from game logs to a predictor, and that path is the half of the proposal I am best placed to judge.
2. **Game and crowdsourcing terms are used without definition.** "'human computation'" gets only a parenthesis, and "game mechanic", "'sticky'", "'reskinned'", "embedded challenges with known answers", "inter-player agreement" and "Social data such as this" are never defined. The "computer opponent" is never explained: how does it choose its genes, and does beating it say anything about the player? The image in Figure 1 shows "Barney's score: 55" against "Your score: 50", and the caption says only "A round of The Cure", so I cannot read it. A genomics reviewer on the panel would be guessing at half the Approach.
3. **The preliminary numbers are hard to follow, and one does not match its figure.** "Genes with selection frequencies greater than or equal to 80% from players that declared knowledge of cancer are depicted in Figure 2." The next paragraph says "The twenty genes listed in Figure 2", but the figure lists eighteen. "Using the top 10 genes" does not say top 10 by which ranking, the dataset behind the 65% figure is never named, and "10 different unique gene combinations that, when aggregated" does not say how they were aggregated. Brevity is expected in an R21, but here I cannot tell what result was obtained.

### Scores

| Criterion | Score | Reason |
|---|---|---|
| Significance | 3 | A clear clinical need, and the method could carry to other diseases |
| Investigator(s) | 3 | Established bioinformatics group with community-annotation projects. Cancer outcome expertise comes from letters, not personnel |
| Innovation | 2 | New to the field, as far as the draft shows |
| Approach | 5 | Aim 1 is clear; Aim 2's weighting, voting and hybrid predictor are not described well enough to judge |
| Environment | 2 | Adequate computing and an existing user community |
| **Overall Impact** | **4** | Promising and novel, but half the plan could not be evaluated from the page |

---

## Reviewer 3: the generalist

A scientist from an unrelated area, reading for why it matters, what is new and what a result would mean.

### Retelling

Gene-based tests that predict how a breast cancer will progress are rare, and this group wants to recruit hundreds or thousands of biologists through an online game, along the lines of Foldit for protein folding, to help choose which genes such tests should use. Their pilot game attracted over 120 players in its first week, and a predictor built with the players' genes came within 3% of the best entry in a public breast cancer prediction contest.

### Need, impact, what is new

- **Need:** Despite a decade of work, few gene-expression predictors are good enough for the clinic.
- **Impact if it works:** Better prognostic tests for breast cancer patients, and a general way to put many scientists' knowledge to work on data problems.
- **What is new:** Pooling many biologists' judgments through a game, where earlier science games tackled protein structure, sequence alignment and RNA design.

### Strengths

1. **The question is stated plainly and is a real unknown.** "What is not known is whether the emerging paradigm of scientific crowdsourcing through games can be extended to help address the challenge of translating genome-scale data into useful predictive models." A non-specialist knows from that sentence what the project is testing.
2. **The precedent makes the idea plausible to an outsider.** "Foldit, EteRNA and Phylo have demonstrated that many people are interested in playing serious, biological games and that these games can result in tangible contributions to important biological challenges." With player counts for each, this turns an odd-sounding idea into an extension of something that has worked.
3. **The pilot has an external, competitive benchmark.** "The predictor scored 69% correct on survival concordance index in an external test dataset, just 3% behind the best submitted predictor". For a generalist this is the most persuasive sentence in the application: an outside contest, an outside test set and a ranking against other teams.

### Weaknesses, most serious first

1. **I cannot tell what a successful result would look like, or whether the pilot result supports the idea.** The promise is large: "If successful, this contribution will result in significantly better predictors of breast cancer progression and has the potential to make major, disruptive improvements in genomic medicine." The draft never says better than what, or by how much. The strongest pilot result does not settle it either. The game's genes "were included in a predictor submitted to the SAGE Breast Cancer Prognosis challenge", and I do not know what else that predictor contained or whether the players' genes helped it, and "just 3% behind the best" means data-only entries did better. The pilot result I found most persuasive may not be evidence for the hypothesis.
2. **The draft overclaims, and claims low risk in a mechanism that asks for high risk.** Phrases such as "we will be able to elegantly tap into a hive mind that is one or even two orders of magnitude larger", "should such an army of minds somehow be raised", and "Better disease predictors will be adapted to clinical use to personalize and thereby improve patient treatment" read as salesmanship in a two-year exploratory grant. Some numbers that carry the argument have no source: "upwards of 10 scientists" and "a pace exceeding 1 million articles per year". The risk statements work against the mechanism: "we feel strongly that this event is very unlikely" and "we are very confident that all phases of the work described in this specific aim will be achieved". The announcement "solicits high risk/high impact research", and a reviewer reading these lines learns that the applicants have not said what the risks are.
3. **The evidence that experts will play, and keep playing, is thin, and the drop-off has already been seen.** Expertise is self-reported at registration: "nearly half of the players self-reported having PhDs and half claimed knowledge of cancer biology". Interest fell quickly: "Indeed, in preliminary studies this effect was observed with the majority of game-play happening quickly after launch". The response is a hope: "we feel that our chances of making a compelling and 'sticky' game are very good." Aim 1 will measure "the number of distinct players, the amount of time spent playing per player, the number of games played and player demographics", but sets no number that would count as success. The one player quoted, 'shenyijie', shows that someone enjoyed the game, not that they knew anything about breast cancer. The whole project hinges on sustained play by people with real knowledge, and the page does not show how the team would know whether it had that.

### Scores

| Criterion | Score | Reason |
|---|---|---|
| Significance | 3 | Matters clearly, but the clinical payoff is overstated for a two-year exploratory project |
| Investigator(s) | 2 | The team built the pilot and runs large community resources |
| Innovation | 2 | A genuinely new use of science games |
| Approach | 4 | The plan is understandable, but success is never defined and the engagement risk is waved away |
| Environment | 2 | Suitable |
| **Overall Impact** | **4** | Exciting idea with a pilot; I cannot tell what the grant would prove |

---

## Panel summary

### Scores side by side

| Criterion | Expert | Adjacent | Generalist |
|---|---|---|---|
| Significance | 3 | 3 | 3 |
| Investigator(s) | 3 | 3 | 2 |
| Innovation | 2 | 2 | 2 |
| Approach | 6 | 5 | 4 |
| Environment | 2 | 2 | 2 |
| **Overall Impact** | **5** | **4** | **4** |

Averaged and multiplied by 10, as `funder/nih-scoring.md` describes, the three impact scores give 43. Three readers are not a study section, so take the spread as the useful signal: Innovation is uniform at 2, and Approach widens from 4 to 6 as the reader's expertise grows. The closer a reviewer works to the methods, the less the plan convinces them.

### Where the retellings differ, from each other and from the author's sentences

The author's two sentences (`drafts/summary.md`) are that games "attract large numbers of biologist players that, through the actions they take in these games, contribute the knowledge needed to build state of the art predictors of breast cancer progression", and that the work "will produce a reusable framework for capturing and applying community intelligence in biology."

1. **The endpoint.** Each reader names a different one: the author says "progression", the expert "survival" (and notes that the endpoint is never fixed), the adjacent reader "outcome", and the generalist "how a breast cancer will progress". The draft itself uses progression, survival time, 10-year survival, metastasis and prognosis. The page never settles which outcome the predictor predicts, or for which subtype.
2. **What players contribute.** The author says "knowledge". The expert retells it as "gene choices" that may track the score feedback, and the adjacent reader as "the genes players favor". Only the generalist carries "knowledge" through. The page asserts that choices equal knowledge, but specialists do not come away believing it.
3. **How strong the pilot is.** The generalist retold the SAGE result as the players' predictor coming within 3% of the best entry, the adjacent reader as doing "well", and the expert left it out of the retelling altogether. The draft's "were included in a predictor" leaves open what else that predictor held, so each reader drew a different conclusion from the same sentence.
4. **The phrase "state of the art".** No reviewer retold the project as producing state-of-the-art predictors. None could, because no comparator or target is named.
5. **The reusable framework.** This is half of the author's summary, and none of the three retellings carries it. The expert mentions reusable software only under impact. Neither aim has a deliverable or a test for reuse. The one concrete instance, the organ transplant version, appears only under potential problems and is not in the timeline.
6. **Aim 2's mechanism.** The expert could retell it (weight players by skill, pool their choices, feed the result to a classifier). The adjacent reader could not. A reader who knows the field but not crowdsourcing loses the thread exactly where the computational contribution sits.

### The three weaknesses most likely to sink the proposal, most serious first

1. **The central hypothesis has no test that separates player knowledge from the game's own score feedback** (Expert W1, Adjacent W3, Generalist W1). Players are scored by classifiers trained on labeled outcome data. Neither the pilot nor the plan compares crowd-chosen genes with data-driven selection, reports knowledgeable players against the rest, or makes clear that evaluation data were kept apart from scoring data. Until it does, a positive result could equally mean the players learned the training labels.
2. **No benchmarks for success** (Expert W2, Generalist W1). The endpoint and subtype are unfixed, no comparator is named, and there is no target accuracy, player count or hours of play. The announcement asks for benchmarks explicitly, and without them neither aim can be judged to have succeeded or failed.
3. **The engagement risk is asserted away rather than managed** (Generalist W3, Expert W3, with Generalist W2 compounding it). Expertise is self-reported, the drop-off after launch is already documented, real play arrives only in year 2, and the mitigations are confidence statements. Combined with the overclaiming, this tells a high-risk/high-impact panel that the applicants have not looked hard at their own risk.

### Additional review criteria and considerations (not scored)

These come from Section V of `funder/PAR-09-219.md`, which asks reviewers to address them without scoring them.

- **Protections for Human Subjects.** The plan collects "player demographics including age, sex, occupation, and education", runs "focused user-group studies" with "test subjects", and the pilot used a registration survey. Nothing in `drafts/` mentions consent or institutional review. Whether the application had a human subjects section is not in this folder.
- **Software sharing plan.** The announcement requires "A software dissemination plan, with appropriate timelines" and lists goals reviewers are told to apply. The draft says code "will be shared under a Creative Commons license" without naming which one, so a reviewer cannot tell whether goal 2 is met (commercialization of enhanced versions must be permitted). It says nothing on transferability (goal 3) or on handling others' improvements (goal 5), and its only timeline is "even as it is being developed". The data plan, "The collected data will be shared through websites associated with the project website", names no repository or format. The plan does commit to anonymizing personal data.
- **Budget.** The budget is not in this folder, so it cannot be judged against the $275,000 two-year cap. The Personnel Justification lists two people: Su at 1.2 calendar months and Good at 10, with Good "responsible for the design, implementation and evaluation of both the game prototypes and the algorithms". One person carrying both aims is a feasibility question reviewers would raise.
- **Letters.** As summarized in `evidence/letters-of-support.md`, two letters do not quite match what the draft cites them for. The draft cites Josh Peay as a source of "consultation with professional game designers", and his letter offers "mentoring" after a career described as programmer to technical director. The Leyland-Jones letter commits to evaluating "the predictive models of breast cancer recurrence that will be generated by your work", while the draft cites it for "new datasets that we will have advanced access to".

### Smaller items any reader would catch

- "The twenty genes listed in Figure 2" introduces a figure that lists eighteen.
- The Project Narrative begins "The proposed research is relative to public health", which is the wrong word.
- "This phase is of research is particularly important" (Aim 2, Phase 2) is garbled.
- The Cure scores on "expression and CNV data", but the new game is "based on RNA expression levels in tumor samples". Dropping copy number is not explained.
- In Su's biosketch, the P01 AG007996 entry reads "Lotz (PI)" and then "Role: PI".

---

## What I could not source

1. **The preliminary data.** The game logs, the registration survey, the analysis and the identity of every dataset are not in `evidence/`; `evidence/preliminary-data.md` says so. These claims are unverified: the 120 players and 2000 games, the PhD and cancer-knowledge fractions, the 65% and 55% accuracies, the FDR < 0.05 combinations, and whether the cross-validation used the data that scored players.
2. **The SAGE challenge result.** The 69% concordance index, "just 3% behind the best submitted predictor", "significantly above the median" and "hundreds of submitted models" all rest on a results page that is not in this folder. No statistical test is named for "significantly", and the draft does not say what else the submitted predictor contained.
3. **Figure 2.** It lists eighteen genes and the text says twenty. I could not tell which is right.
4. **Numbers in the drafts with no source in `evidence/`:**
   - "more than 126,000 publications" (a tinyurl)
   - "a pace exceeding 1 million articles per year" (no citation)
   - "upwards of 10 scientists" (no citation)
   - the SAGE contest launch (a tinyurl)
   - Su's "cited more than 7000 times" (Personnel Justification)
5. **Figures attributed to references whose full text is not in `evidence/`:**
   - The BioGPS traffic and user counts are cited to [18], a 2009 paper, for figures stated in the present tense.
   - Foldit's "more than 300,000 players" is cited to [12-14].
   - EteRNA's "more than 38,000 registered players" is cited to [16], a magazine article that `evidence/references.md` records as not fully verified.
   - Phylo's "more than 12,000 players" is cited to [17].
6. **Citation support.** No citation's support for its sentence was checked, because the full texts are not here and this panel is not a reference check. Two pairings are not evident from the titles in `evidence/references.md`, and I have left them unchecked rather than judged:
   - [19], a zero-curation model for ontology development, is cited for partnering with conferences to run contests.
   - [5], protein networks as logic functions, is cited for "Network Guided Forests".
7. **The letters of support.** Only summaries are in `evidence/`. I could not confirm from the full letters what Leyland-Jones commits on datasets or advance access, or what role Peay would take.
8. **Human subjects.** No human subjects section is in `drafts/`, so I could not tell whether one was submitted or whether the pilot survey had review.
9. **The budget.** It is not in the folder, so the panel could not judge the cost against the FOA limits, or whether programmer or designer effort was funded.
10. **Page limit.** The announcement caps the Research Strategy at 6 pages. The Markdown in `drafts/` carries no pagination, so compliance could not be judged.
11. **The software license.** Which Creative Commons license was intended is not stated.
12. **Current criteria.** The scores use PAR-09-219. The simplified framework that `funder/nih-scoring.md` describes for due dates from 25 January 2025 is not set out in full in `funder/`, so the panel did not re-score under it.
13. **The author's own summary.** The sentences in `drafts/summary.md` are copied from the Project Summary, and the author was not available to confirm they are still their own.
14. **Folder description.** `README.md` and `drafts/README.md` describe a `biosketch-draft.md` in `drafts/`, and `README.md` describes one review from each of five skills in `reviews/`. Neither was present when this review was written. This does not affect the panel.
