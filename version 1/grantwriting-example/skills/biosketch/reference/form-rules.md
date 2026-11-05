# Biosketch form rules (NIH)

Verified 2 November 2026 against the NIH forms directory and the official instruction PDFs. Check them again before relying on them: NIH revises both. Put newer instructions in `funder/`; they take precedence over this file.

Since 25 January 2026 NIH biosketches are prepared in SciENcv and submitted as two documents: the **Biographical Sketch Common Form** and the **NIH Biographical Sketch Supplement** (OMB Nos. 0925-0001 and 0925-0002). There is no downloadable blank template; SciENcv produces a single combined PDF. NIH's leniency period ended 8 May 2026, and the Common Form validations are now hard errors (NOT-OD-26-079).

Sources, each fetched and read rather than recalled:

- NIH, [Biographical Sketch Common Form](https://grants.nih.gov/grants-process/write-application/forms-directory/biographical-sketch-common-form) (page updated May 2026), and its [instructions PDF](https://grants.nih.gov/sites/default/files/Common%20Form%20NIH%20Biographical%20Sketch_FINAL.pdf)
- NIH, [NIH Biographical Sketch Supplement](https://grants.nih.gov/grants-process/write-application/forms-directory/nih-biographical-sketch-supplement), and its [instructions PDF](https://grants.nih.gov/sites/default/files/NIH%20Biographical%20Sketch%20Supplement_FINAL.pdf)
- [NOT-OD-26-018](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-018.html), implementation for due dates on or after 25 January 2026
- [NOT-OD-26-079](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-079.html), end of the leniency period

## Biographical Sketch Common Form

Sections: identifying information, position title, organization and location, professional preparation, appointments and positions, products, and certification. For NIH there is **no page limit** on the Common Form.

- **Identifying information.** Name, and a persistent identifier that for NIH must be an **ORCID iD linked to the eRA Commons Personal Profile**.
- **No personal information anywhere in the sketch**: no home address, home or cell phone, personal email, driver's licence, marital status or hobbies.
- **Professional preparation.** Reverse chronological by start date, every postdoctoral and fellowship appointment listed separately, down to the baccalaureate. Each entry: organization, location (city, state or province, country; N/A where there is no state or province), degree if applicable, start date, month and year received or expected, and field of study.
- **Appointments and positions.** Reverse chronological by start date, current appointment first, including every titled academic, professional or institutional position, paid or not, full-time, part-time or voluntary. Appointments outside the primary organization are listed for the three years before submission. Each entry: start year, end year, title, organization, department, location.
- **Products.** Up to five closely related to the proposed project, and up to five other significant products. Each must be citable and accessible, and follows the NIH Policy on Use of Hypertext. Each needs authors, product title, date of publication or release, website URL, other persistent identifier if available, and the remaining citation information (for a paper: journal, volume, issue, pages).
  - A product can be a publication, conference paper or presentation, a website, a technology or technique, an invention, patent, patent application or licence, or data, a database, a dataset, a physical collection, audio or video, software, a model, an educational aid or curriculum, an instrument, research material, an intervention, or a new business.
  - "Et al." after one or more authors is allowed in place of the full author list.
  - **Where `products.md` is missing a required element**, do not invent it and do not write N/A on the author's behalf. Reproduce what the list gives and name the missing element in the "What I could not source" section, so the author supplies it. N/A is an assertion that the element does not apply, which only the author can make.
  - **PMCIDs are not interchangeable with PMIDs or DOIs.** Resolve them through the PubMed connector where it is available, and mark any identifier that could not be resolved as unconfirmed rather than carrying it over silently.
- **Certification.** The applicant certifies that the information is current, accurate and complete including current, pending and other support; that they are not party to a malign foreign talent recruitment program (42 U.S.C. § 19232); and that they completed research security training within the 12 months before submission (42 U.S.C. § 19234). The signature must be dated within 12 months of submission, and misrepresentation carries criminal and civil liability. **This section is for the applicant alone.**

## NIH Biographical Sketch Supplement

Four required sections: Personal Statement, Honors, Contributions to Science, and Certification.

- **Personal Statement**: at most 3,500 characters. Describes why the applicant is well suited to their role: training, previous experimental work on this or related topics, technical expertise, collaborators and environment, past performance including ongoing and completed projects from the last three years. The instructions also invite two things a draft will not know to ask for: an explanation of factors that affected past productivity (family care, illness, disability, military service), and a note of whether the applicant has published under another name. Both are the applicant's to decide.
- **Honors**: at most 15 entries. Students, postdocs and junior faculty are told to include scholarships, traineeships, fellowships and development awards. If there are none, the form takes "Nothing to Report" and the current year. **This is the applicant's section**, not the skill's.
- **Contributions to Science**: up to five, each at most 2,000 characters, each no longer than half a page. For each one the instructions ask for four things: the historical background framing the problem, the central findings, the influence of those findings on the progress of science or their application to health or technology, and the applicant's specific role. Figures, tables and graphics are not allowed. Graduate students and postdocs "may wish to consider highlighting two or three they consider most significant" rather than five. Contributions may mention products still under development, such as manuscripts not yet accepted, and need not relate to the proposed project.
- **References.** In-text **parenthetical** references to any of the ten products listed in the Common Form's Products section are allowed, in both the Personal Statement and the Contributions to Science. The instructions name two recommended styles, lead author and year, `(Collins et al., 2026)`, or the PMCID or PMID, `(PMCID0123456)`. **Full bibliographic citations and hyperlinked references are not allowed** in the Supplement. So a journal, volume or pages in the running text is not acceptable.

The influence requirement deserves care. The form asks for impact, which is exactly the kind of claim a model will supply from nowhere if the CV does not record it. Where the applicant's own files do not establish influence, describe the contribution without it and say so in the report.

## Counting

Characters are counted with spaces. `scripts/count_chars.py` counts each section of the draft against these limits, reports any required section that is missing, and flags text that looks like a full bibliographic citation rather than a parenthetical reference.
