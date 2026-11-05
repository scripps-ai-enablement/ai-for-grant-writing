# Grant writing starter

A folder for working on one grant proposal with Claude as a reviewer and an
assistant, not as the author. It holds your drafts, your sources, the funder's
rules, and five skills for the parts of grant writing where AI earns its place.

Use it on your Scripps Claude account. A funding proposal is confidential
material, and so is your unpublished data.

## Three layers of context

Claude knows only what it is shown. This folder gives you three ways to show it
more, and each one is a text file you can read:

- **A prompt** is what you type. It lasts one request.
- **`CLAUDE.md`** holds the standing rules for this folder. Every request in the
  project follows them.
- **A skill** is a written method for one job, in `skills/`. It runs when you
  name it.

## Open it as a project

1. Download this folder and unzip it somewhere you can find again.
2. In the Claude desktop app, find **Projects** in the left sidebar and click
   **+**. If your message box shows "Chat" and "Cowork", switch to Cowork first.
3. Choose **Use an existing folder**, and pick this folder.
4. Name the project. Leave the Instructions box empty, because `CLAUDE.md` in
   this folder holds the rules. Click **Create**.
5. Read `CLAUDE.md`, then open `skills/` and look at one of the `SKILL.md`
   files before you ask for anything.

A project keeps the folder, its rules and Claude's memory of your work in it
together, so every new conversation in the project starts from the same setup.
Start a new conversation for each run if you want to compare runs cleanly.

Nothing to install. Everything is in the folder, in plain sight.

## The five skills

Each skill is a folder in `skills/` with a `SKILL.md` inside it. Ask for one by
pointing at its file:

| Skill | Ask for it like this |
|---|---|
| `biosketch` | "Follow `skills/biosketch/SKILL.md` to draft my biosketch" |
| `aims-checklist` | "Follow `skills/aims-checklist/SKILL.md` to check my Aims page" |
| `significance-checklist` | "Follow `skills/significance-checklist/SKILL.md` to check my Significance section" |
| `mock-panel` | "Follow `skills/mock-panel/SKILL.md` and run a mock panel on my draft" |
| `reference-check` | "Follow `skills/reference-check/SKILL.md` and check the references in this section" |

In this folder a skill runs only when you name it, so you always know which
method was used. To have one run when you ask in plain words, either upload it
to your account (see "Make a skill permanent" below) or add a rule to
`CLAUDE.md`, such as: "When I ask for a check of my Aims page, follow
`skills/aims-checklist/SKILL.md`."

What each skill does:

- **biosketch** drafts the Personal Statement and Contributions to Science from
  your Aims, CV and a fixed list of your products, counts characters with a
  script, and reports every claim against its source.
- **aims-checklist** works through an Aims checklist item by item, quoting the
  sentence that meets each one or naming what is missing, then runs a
  60-second reviewer test.
- **significance-checklist** does the same for the scientific premise, the
  significance argument and the innovation claim, plus a gap test and the
  common pitfalls.
- **mock-panel** reads your draft as three reviewers — an expert in your niche,
  a reader from an adjacent field, and a generalist — each retelling your
  proposal with strengths and weaknesses tied to quoted passages.
- **reference-check** looks each citation up and asks the question you cannot
  answer by looking: does this paper support the sentence citing it?

Only `biosketch` writes text you might submit, and it does that because the form
is rigid and every claim in it traces back to your own CV. The other four
critique and never rewrite, because the words in your Aims and your Significance
section need to be yours.

## Put your own work in

Apart from the rules and the skills, this folder starts empty. Each file below
holds one comment line saying what goes in it. Paste your own text over it.
You don't need all of them at once: each skill's `SKILL.md` names the files it
reads.

| File | What it is |
|---|---|
| `drafts/aims.md` | Your Specific Aims. The biosketch method and both checklists hang on these |
| `drafts/significance.md` | Your Significance section |
| `drafts/innovation.md` | Your Innovation section |
| `drafts/approach.md` | Your Approach, preliminary data included. Figures go in `drafts/figures/` |
| `drafts/summary.md` | Two sentences of your own on what the proposal does and why it matters |
| `evidence/cv.md` | Your CV, in any readable format |
| `evidence/products.md` | The fixed list of papers, software and datasets the biosketch skill may choose from |
| `evidence/references.md` | Every paper your drafts cite, with a PMID or DOI. `evidence/README.md` says what else belongs there |

To see a full folder, open `grantwriting-example`, which is distributed
alongside this one. It holds a real NIH R21 application from 2012, laid out as
this folder would be, with every skill already run on it. It shows where each
part of an application goes, and what the reviews and the log look like after a
few runs. You can also open it as a project and run the skills on it yourself.

Two more folders change what the skills do. Put the funding announcement and
the instructions for your mechanism in `funder/`, and they take precedence over
the rules stored inside the skills. Put any checklist you have been given in
`checklists/`, and the checklist skills will use yours instead of their own.

Reviews land in `reviews/`, dated. `ai-use-log.md` gets one line per run, which
is what your disclosure statement comes from.

## Change a skill

A skill is a folder with a `SKILL.md` file in it. The file opens with a name and
one line saying when to use it, and the rest is instructions. Alongside it go
reference documents, templates and scripts.

Open `skills/biosketch/SKILL.md` and change something: the number of
contributions, the order of the selection criteria, a habit of your own writing
it should respect. Run it again and watch what moved. That loop is the point.
If you find yourself explaining the same thing to Claude twice, that is the
moment to write it down as a skill.

The script inside the biosketch skill is worth understanding too. A model
estimates character counts and is confident while being wrong; a script counts.
Any time you need an exact answer, have the skill run code rather than reason.

## Make a skill permanent

The skills here work in this folder. To have one available in every
conversation, upload it to your account:

1. Zip a single skill folder, for example `skills/biosketch`, so that the zip
   contains `biosketch/SKILL.md` at its top level.
2. Go to Customize > Skills on claude.ai, click "+", then "Create skill", then
   "Upload a skill".
3. Upload the zip and toggle the skill on.

An uploaded skill triggers on its own description, so you can then just say
"draft my biosketch" anywhere. The copy in this folder stays the one you edit;
re-upload when you change it. If the upload option is missing, your
organization has turned off user-created skills; ask IT.

Sources:
[Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork);
[Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Rules worth keeping in your head

- **Approved accounts only.** Scripps Research Policy 708 keeps confidential
  material out of non-approved AI tools, and a funding proposal is confidential.
- **Your own work only.** A classmate's draft does not go into an AI tool, even
  to help them.
- **Verify everything.** NIH and the HHS Office of Research Integrity said in
  May 2026 that presenting AI-generated, non-existent references as real could
  constitute data fabrication, and that applications substantially developed by
  AI are not considered the applicant's original ideas and will not be
  considered. In practice what you are checking for is a real source that does
  not say what you claimed it said.
- **Disclose.** NIH asks researchers to describe how AI tools were used. The log
  in this folder holds what two honest sentences need.
- **Know your funder's rules.** They differ and they change. Check each cycle.

Sources:
[NIH and HHS ORI, "Helpful Reminders to Ensure Integrity of NIH-Supported
Research When Using Artificial Intelligence," 14 May 2026](https://www.grants.nih.gov/news-events/nih-extramural-nexus-news/2026/05/helpful-reminders-to-ensure-integrity-of-nih-supported-research-when-using-artificial-intelligence);
[NOT-OD-25-132](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-25-132.html).
