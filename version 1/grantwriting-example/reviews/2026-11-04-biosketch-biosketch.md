# Biosketch check report: Benjamin M. Good

Skill: `skills/biosketch/SKILL.md`, run 2026-11-04. Draft: `drafts/biosketch-draft.md`.

Inputs read: `drafts/aims.md`, `evidence/cv.md`, `evidence/products.md`, the skill's `reference/form-rules.md`, `reference/forli-method.md`, `templates/biosketch.md` and `scripts/count_chars.py`, and `funder/README.md` and `funder/PAR-09-219.md` for any newer biosketch instructions. Identifiers and abstracts for the ten PubMed-indexed products were retrieved from PubMed through the connector on 2026-11-04.

**Form rules applied.** `funder/` holds the 2009 announcement (PAR-09-219) and the scoring scale, and nothing on the biosketch format; `funder/README.md` says so. The draft therefore follows the skill's stored 2026 NIH rules (Common Form plus NIH Supplement, verified 2 November 2026), not the 2012 PHS 398 biosketch this application was submitted with. If the author needs the 2012 format, its instructions are not in `funder/`. `checklists/` is empty; this skill does not use a checklist.

**Not used.** `evidence/biosketches/good-2012.md` was not opened. The skill treats a previous biosketch as layout only, and the template supplied the layout. The CV's "Research experience" lines are the author's sentences from that biosketch, and were used as facts, not copied as prose. The grouping in `products.md` ("Listed in 2012 as most relevant", P1 to P5) was not used for selection; the selection below was re-derived from the Aims and differs from it.

**Count** (`python3 skills/biosketch/scripts/count_chars.py drafts/biosketch-draft.md`, exit status 0):

```
Personal Statement: 2812 / 3500 characters - OK
Products closely related to the proposed project: 1201 characters (no limit)
Other significant products: 1213 characters (no limit)
Contribution: Games and volunteer systems for capturing biological knowledge: 1871 / 2000 characters - OK
Contribution: Measuring and using community-generated annotation: 1994 / 2000 characters - OK
```

No bibliographic-citation warnings. A search of the draft found no en or em dashes.

In the draft, products are numbered 1 to 10 across the two lists and the prose refers to them as "(Product N)". Author-year references would have been ambiguous (three "Good et al., 2012" papers, and The Cure has no recorded authors). **Product N in the draft is not P-number N in `products.md`**; the table below maps them.

## 1. Themes

Derived from `drafts/aims.md` only.

- **T1. Games and volunteer systems that recruit biologists and capture their knowledge.** Aim 1.
- **T2. Assessing and aggregating community contributions** (data quality, participant weighting, voting, confidence). Aim 2, first hypothesis.
- **T3. Predictive models from molecular data, improved by structured knowledge.** Aim 2, final hypothesis, and the long-term goal.
- **T4 (cross-cutting). Open, web-based software for community knowledge**, the "open source software and validated design patterns" and "re-usable framework" the Aims promise as outcomes. No aim states it.

## 2. Paper-to-theme mapping

### Products closely related to the proposed project

| Draft | products.md | Themes, aims | Why chosen |
|---|---|---|---|
| Product 1 | P16, The Cure (2012) | T1, T3; Aim 1 | The prototype of the game Aim 1 will build, and the only product that is a game for building cancer predictors. Ranked first on relevance despite no recorded authors or identifier (see section 4). |
| Product 2 | P1, Games with a scientific purpose (2011), [DOI](https://doi.org/10.1186/gb-2011-12-12-135) | T1; Aim 1 | First author (1 of 2), Genome Biology. The PubMed abstract is one sentence about Foldit, so this may be a short commentary rather than a research article. Whether to foreground it is the author's call; `products.md` states no exclusions. Chosen over P15 (Dizeez), which has no record for the cited item and has Good as middle author. |
| Product 3 | P4, Fast, cheap and out of control (2006), PMID 17094234 | T1, T2; Aims 1 and 2 | First author (1 of 8). Reports volunteers recruited with token prizes building an ontology, with the result assessed, which bears on both recruiting biologists (Aim 1) and judging what they produce (Aim 2). Preferred over P8 for this list as the fuller, PubMed-indexed paper with reported results. |
| Product 4 | P10, Social tagging in the life sciences (2009), [DOI](https://doi.org/10.1186/1471-2105-10-313) | T2; Aim 2 | First author (1 of 3). According to its PubMed abstract, agreement between aggregated tags and MeSH "could be increased through voting", which bears directly on Aim 2's hypothesis that voting yields accurate confidence estimates. Placed here over P3 on relevance, although P3's venue is more selective. |
| Product 5 | P2, Mining the Gene Wiki (2011), [DOI](https://doi.org/10.1186/1471-2164-12-603) | T2, T3; Aim 2 | First author (1 of 5). Turns community-written text into structured annotations with measured precision, and the abstract reports they improve gene set enrichment analyses: community knowledge improving analysis of genomic data, which is Aim 2's premise. Chosen over P11 (AMIA 2011), which has no record. |

### Other significant products

| Draft | products.md | Themes, aims | Why chosen |
|---|---|---|---|
| Product 6 | P3, The Gene Wiki in 2011 (NAR), [DOI](https://doi.org/10.1093/nar/gkr925) | T4, T2 | First author (1 of 4), most selective venue on the list. Shows the scale of the community resource and word-level quality scoring (WikiTrust). Less directly tied to an aim than P2 or P10, so it sits here. |
| Product 7 | P12, Semantic Wiki Links (2012), [DOI](https://doi.org/10.1093/database/bar060) | T4, T2 | First author (1 of 4). Infrastructure for structured community contribution. |
| Product 8 | P8, Ontology engineering using volunteer labor (WWW 2007), DOI 10.1145/1242572.1242787 | T1 | First author (1 of 2), but a two-page conference paper. Kept partly because the CV does not say whether P4 or P8 documents the "game-like system for ontology engineering"; listing both keeps that work on the sketch. Drop it if the author confirms P4 is the one. |
| Product 9 | P6, A new perspective on V3 phenotype prediction (2003), [DOI](https://doi.org/10.1089/088922203762688658) | T3; Aim 2 | The only listed product on predictive classifiers from molecular data. Middle author (2 of 4) and 2003. Included so that T3 has at least one product; see the thin-theme flag below. |
| Product 10 | P13, SNPedia-Gene Wiki mashup (2012), [DOI](https://doi.org/10.1186/2041-1480-3-S1-S6) | T4, T2 | First author. Gene-disease knowledge integrated as linked open data, closer to disease prediction than the Web-tooling alternatives. |

### Not selected

- **P5**, The Life Sciences Semantic Web is full of creeps! (2006, first author). A review (PubMed article type) on semantic web adoption; T4 only. The strongest dropped alternative; it lost to P13 on relevance.
- **P7**, iHOPerator (2006, first author). Web tooling; T4 only, lower relevance.
- **P9**, Bio2RDF (2008, middle author 3 of 4). T4 only, lower relevance and author position.
- **P11**, Mining GO annotations from Gene Wiki hyperlinks (AMIA 2011). No record found (`products.md`), so not citable and accessible as given.
- **P14**, Quantifying GO annotation accuracy over time (2012, middle author). No record found. It would bear directly on T2 if a record existed. Its "won best paper award" note is unverified and is in any case an Honors matter.
- **P15**, Dizeez (2012 workshop item, middle author). No record for the cited item. The later PLoS One article (2013) is a separate product not on the list, and was not added.

**Coverage.** Every theme has at least one product. **T3 is thin**: the only support is a 2003 middle-author HIV classifier paper and The Cure. No listed product builds a genomic or cancer predictor. I did not pad it.

### Contributions to Science: why two

Good is a Research Associate (since 2011), Ph.D. 2009, and the CV describes his current work as "As a post-doc". I treated him as at the postdoc stage, for which the NIH instructions suggest two or three. The verified products form two substantial lines, games and volunteer knowledge capture (Products 1, 2, 3, 8) and measuring and using community annotation (Products 4 to 7, 10), both first-author work tied to an aim. A third line was weaker on both available options: machine learning rests on one middle-author paper (P6), and semantic web and Web tooling (P5, P7, P9) is less related to these Aims and would have taken list slots from more relevant products. Ordered with games first, since the project is a game.

## 3. Claims and their sources

"CV" means `evidence/cv.md`; "abstract" means the product's PubMed abstract, retrieved 2026-11-04. **All findings in the Contributions come from the products' PubMed abstracts, not from the CV**, because the CV records no findings. Check each number against the paper.

### Personal Statement

1. B.S. cognitive science, M.S. evolutionary and adaptive systems, Ph.D. bioinformatics. CV, Education.
2. Research "focused on acquiring and validating structured knowledge from large groups of biologists through web-based community intelligence applications". CV, Research experience (his sentence).
3. Developed a game-like system for ontology engineering as a graduate student. CV, Research experience. Which product documents it is not recorded (flag 4.1).
4. Studied ontology development by volunteers without expert curation (Products 3, 8). Titles of P4 and P8; P4 abstract.
5. Co-authored an article on games with a scientific purpose (Product 2). P1 title and authors.
6. Designed and implemented The Cure, a web-based game for building predictors of breast cancer survival from gene expression and copy number data, released September 2012 (Product 1). CV ("designed and implemented ... serious game for predicting cancer outcome based on molecular data"); `products.md` P16 description and release month.
7. Aim 1 framing. `drafts/aims.md`, Aim 1.
8. Investigated open, Web-based document classification. CV. Tying this to P10 (Product 4) is my inference from P10's title.
9. Led efforts to extract ontology-based gene annotations from Gene Wiki text (Product 5) and to motivate direct community contribution (Products 6, 7), "since my postdoctoral fellowship". CV ("As a post-doc I have successfully lead in efforts..."). The CV dates the postdoc 2010 to 2011 and the Research Associate post from 2011, so "since" covers both. The assignment of Products 6 and 7 to "direct contribution" is my mapping.
10. Aim 2 framing (weighting by ability, voting, confidence). `drafts/aims.md`, Aim 2.
11. Trained in machine learning during the M.S. and as a research associate at UC San Diego. CV.
12. Before the Ph.D., led projects from a Coccidioides immitis genome database to sequence-based HIV co-receptor classifiers (Product 9). CV. "Led" is the CV's word; on P6 he is 2 of 4 authors (flag 4.5).
13. Second half of Aim 2. `drafts/aims.md`.
14. Expertise in HCI design, semantic web, biomedical ontologies; professional Web and client-server software development. CV, Expertise.
15. Building a semantic network in Wikipedia (Product 7); linking genes to diseases with a SNPedia-Gene Wiki mashup (Product 10). Titles of P12 and P13.
16. Open source software and validated design patterns for others to apply in other biological contexts. `drafts/aims.md`, paragraph 2.
17. Early career knowledge-based intelligent systems gave a foundation in knowledge-based computing. CV. "As a knowledge engineer and an expert system consultant" joins that line to the 1998 to 2000 positions; the CV does not state the link outright.
18. Co-founded Freeform Information in 2009. CV, Positions (2009 to 2010).
19. 36 peer-reviewed articles. CV, Publications (as of October 2012, from the Personnel Justification).
20. Research Associate at The Scripps Research Institute since 2011. CV.

Left out deliberately: the CV's "the first serious game for predicting cancer outcome". It is a priority claim nothing in `evidence/` supports, so the draft describes the game without "first". The author may restore it with support.

### Contribution: Games and volunteer systems for capturing biological knowledge

1. Ontology building expensive and labor-intensive under most existing methods. P4 abstract.
2. Games have brought human knowledge and reasoning to protein structure determination, multiple sequence alignment and RNA structure design. `drafts/aims.md`, paragraph 1 (the author's own background claim; its citations in the Aims were not checked here).
3. "My work in this area asks whether..." Framing; no fact.
4. Game-like system for ontology engineering. CV.
5. Two days, conference on circulatory and respiratory health, 68 volunteers untrained in knowledge engineering, targeted web-based interface, 661 terms, 245 hyponym and 340 synonym relationships, linked to an existing upper ontology. P4 abstract.
6. "Rudimentary" ontology; three t-shirts, four coffee mugs, one chocolate moose; quantitative and qualitative assessment. P4 abstract.
7. A second paper on ontology engineering using volunteer labor (Product 8). P8 title only; not in PubMed, so its content was not read.
8. With Andrew Su, wrote on games with a scientific purpose; Foldit shows games recruit, engage and organize citizens. P1 authors and abstract.
9. The Cure. As Personal Statement claim 6.
10. First author of each paper. `products.md` author positions; PubMed author lists for P1 and P4; P8 from the Crossref check in `products.md`.
11. Aim 1. `drafts/aims.md`.

### Contribution: Measuring and using community-generated annotation

1. Ontology-based gene annotations are important tools for genome-scale data; collecting them is costly. P2 abstract.
2. Social tagging systems and Wikipedia can produce annotation at low cost. P2 abstract (Wikipedia as "a low-cost, mass-collaborative platform"); P10 abstract (social tagging creates public metadata repositories). "Its quality and uses must be established" and "My work measures, aggregates and structures such contributions" are framing.
3. CiteULike and Connotea; coverage, density, inter-annotator agreement, agreement with MeSH; agreement low; voting increased agreement with MeSH. P10 abstract.
4. Led efforts to extract annotations and motivate direct contribution. CV.
5. Gene Wiki covers more than 10,000 human genes. P2 and P3 abstracts.
6. 2,983 Disease Ontology and 11,022 Gene Ontology candidate annotations; precision 90-93% and 48-64%; improved gene set enrichment analyses. P2 abstract.
7. Improvements to the sync system; the paper introduced WikiTrust, word-level quality. P3 abstract. Good's own role in WikiTrust is not recorded (flag 4.6).
8. Method for editors to embed computable semantic relations. P12 abstract.
9. Gene Wiki+ integrates Gene Wiki and SNPedia; 8,047 gene-disease relationships; 479 in both. P13 abstract.
10. First author of each paper. `products.md`; PubMed author lists.
11. Aim 2. `drafts/aims.md`.

**Influence.** Neither contribution states an influence on the field. Nothing in the CV or `products.md` records uptake, use, citation or adoption for any product, so the form's fourth element is absent from both. This is the largest gap in the Contributions (see the final section).

## 4. Flags

1. **Game-like system unattributed.** The CV says he developed "a novel game-like system for ontology engineering" in published graduate work, but not in which product. P4's abstract describes "a targeted, web-based interface" and prizes, not a game. The draft states the system from the CV and keeps it separate from the P4 results.
2. **The Cure (Product 1)** has no authors or credit list, no persistent identifier, and an unchecked URL. The Common Form requires authors and requires products to be citable and accessible.
3. **Unconfirmed identifiers.** P8's DOI is from the Crossref check recorded in `products.md`; P8 is not in PubMed, so this run could not resolve it, and the draft marks it unconfirmed. P4's URL is from `products.md` and was not checked; P4 has no PMCID or DOI. All other PMIDs, PMCIDs and DOIs in the draft match the PubMed records.
4. **Thin theme.** T3 (predictive models) rests on Product 9 and Product 1 only. For an application whose Aim 2 infers genomic predictors, the Investigator criterion is exposed here.
5. **Role wording on P6.** The CV says he led the HIV classifier project; P6 lists him 2 of 4. The draft uses the CV's "led". Confirm.
6. **WikiTrust.** Product 6's abstract says the paper introduced WikiTrust, and co-author de Alfaro is outside the Su group. The draft attributes WikiTrust to "the same paper", not to Good. Confirm what his part was.
7. **Product 2 may be a short commentary**, judging by its one-sentence abstract. Keep or drop is the author's judgment.
8. **Citations corrected to the records**, each a departure from the submitted text in `products.md`:
   - P1: issue (12) added from PubMed.
   - P2, P10: "(1)" dropped, since the records have no issue; P2 initials expanded to Howe DG, Lin SM, Kibbe WA.
   - P3: Nucleic Acids Res 2012;40(Database issue):D1255-61, online 2011 Nov 10; Clarke EL. The 2012 issue year is from the check line in `products.md`, since the connector returned only the online date.
   - P4: initials from PubMed (Tranfield EM, Tan PC, Singhera GK, Okon EB), Pac Symp Biocomput 2006:128-39.
   - P8: proceedings title per the Crossref check in `products.md`.
   - P12: Clarke EL; Database (Oxford) 2012:bar060.
   - **P13: Clarke EL restored as second author.** The submitted citation omits him; the PubMed record lists four authors.
   - P6: the submitted initials (Pillai SK, Good BM) are kept, since the record's single initials do not contradict them.
9. **Requirements not met under the 2026 rules:**
   - No ORCID iD (CV: "not recorded"); the Common Form requires one linked to eRA Commons. This is identifying information and was not touched.
   - The Personal Statement asks for ongoing and completed projects from the last three years; the CV records none ("Ongoing: none. Completed: none."), so none are listed.
   - Collaborators and environment are thin, because the CV records no resources and does not state Good's role on this project.
10. **Project role.** The draft does not name his role on this application, because the CV does not record it.

## Not touched

Identifying information, professional preparation, appointments and positions, Honors, and the certification section (current and pending support, malign foreign talent recruitment programs, research security training) were not drafted. Only the applicant can attest to these. The CV's honors and positions are in `evidence/cv.md` for the author to enter.

The Personal Statement instructions also let the applicant explain factors that affected past productivity, and note whether they have published under another name. Both are the applicant's to decide, and neither was written.

## What I would have asked the author

The author was not available, so the draft proceeds on the files as they stand.

1. Which paper describes the game-like ontology engineering system: P4, P8, or another?
2. Who are the authors or credited contributors of The Cure? Is the URL live or archived, and does it have a persistent identifier?
3. What is your ORCID iD?
4. Is there any recorded influence for these lines of work, with a source that can go into `evidence/` (Gene Wiki use, The Cure participation, adoption or reuse)?
5. What was your role on the HIV classifier project (P6) and on WikiTrust?
6. Do you want Product 2, a short piece, foregrounded?
7. Do you have a product on predictive modeling of genomic or cancer data that is not on the fixed list? The CV counts 36 articles; the list holds 15.
8. Is this sketch for the 2012 PHS 398 format or the 2026 SciENcv forms? If 2012, put those instructions in `funder/`.
9. What is your role on this project?

## What I could not source

- **Influence of any contribution.** No uptake, use, citation, adoption or reuse is recorded in `evidence/cv.md` or `evidence/products.md` for any product.
- **The Cure (P16):** authors or credit list, persistent identifier, and whether `http://genegames.org/cure/` is accessible. Player numbers and results are not in the CV or product list. The Aims describe a proof-of-concept experiment, but the skill limits facts to the CV and product list.
- **Which product documents the "game-like system for ontology engineering"** named in the CV.
- **P8 DOI** (10.1145/1242572.1242787): not resolvable through PubMed. It rests on the Crossref check recorded in `products.md`.
- **P4 URL:** not checked in this run. P4 has no PMCID or DOI.
- **P3 issue year (2012):** from `products.md`. PubMed returned the online date (2011-11-10) with volume 40, Database issue, D1255-61.
- **ORCID iD**, required for NIH on the 2026 Common Form.
- **Ongoing and completed research support** in the last three years: the CV records none. Whether that is complete is for the author to confirm.
- **Good's role on this application**, and the collaborators and resources the Personal Statement asks about.
- **Good's role in WikiTrust**, and his role on P6 beyond the CV's "led".
- **Any product on genomic or cancer predictors.** None is on the fixed list, so T3 is thin.
- **2012 biosketch instructions.** `funder/` has none, so the 2026 rules were applied.
- **P11, P14 and P15:** no record found for the items as cited, so they were not selected. P14's best paper award is unverified.
- **Support for "the first serious game"** (CV): none in `evidence/`, so the claim was left out of the draft.
