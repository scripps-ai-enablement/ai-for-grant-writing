# Grant writing seminar workspace

Materials for *Using AI for Grant Writing*, a 90-minute seminar in TRBIO 431,
Developing a Grant Proposal, at Scripps Research. Each version ships two
deliverables together: a slide deck, and a starter folder students download and
open as a Cowork folder in the Claude desktop app.

## Versioning

Significant changes to the deck or the starter go in a new numbered version
directory. Do not overwrite or revise an earlier version in place.

- Create `version N/` alongside the existing ones, copy forward whatever is
  being revised, and make the changes there.
- The highest-numbered directory holds the current materials. Earlier
  directories stay intact as the record of what was taught.
- Keep a version's deck and its starter in the same directory. Each deck
  describes the folder that ships with it, down to file names and exercises.
- Carry the version into the deck's filename.
- Ship the starter as both an unzipped folder and a `.zip` beside it. Students
  download the zip; the folder is what the repository tracks and what the zip
  is rebuilt from.

Small corrections, such as a typo, a broken link or a date, are made in place in
the current version.

## Publishing

The materials are public at
`github.com/scripps-ai-enablement/ai-for-grant-writing`. Releasing a version
means tagging it and attaching that version's two zips to the release. Slide 27
links to `releases/latest/download/`, which resolves to the newest release, so
the deck does not name a tag and needs no edit when a later version ships.
Rebuild the zips from the folders before attaching them, and check that the file
lists match.

Two things stay out of the repository, enforced by `.gitignore`: `instructor-only/`
in every version, and `archive/`, which holds drafts that predate the repository.

## Keep the two deliverables consistent

The deck walks students through the starter: which skills it holds, which files
go where, and what each exercise asks for. A change to one usually requires a
change to the other. Adding a skill means revisiting the slides that list the
skills and the folder contents; promising an exercise on a slide means checking
that the starter supports it.

## Building the deck

The `.pptx` is the artifact of record. Decks here have been produced both by a
python-pptx generator script and by editing in PowerPoint directly, so
regenerating from a script discards any edits made in the file. Check which is
newer before running a generator, and when merging hand-made edits, preserve the
author's own slides and wording rather than rewriting them.

Check a rendered deck rather than trusting the file. Convert to PDF, render the
pages to PNG, and look at every slide that changed: text overflowing a card,
clipped lines and collisions with footnotes are invisible in the XML and obvious
in the image. Declared font sizes also do not tell you what the audience sees,
because shrink-on-overflow applies a scale at render time.

Body text has an 18pt floor and captions and footnotes a 14pt floor, measured at
rendered size. When text does not fit at a legible size, cut or split it rather
than shrinking the type.

## Accuracy

Verify claims against primary sources and cite them, in the speaker notes and in
anything students receive. Agency rules carry dates and stored copies age: NIH
biosketch form requirements, federal AI policies and Scripps Research policy have
all changed within the life of these materials. Fetch the current source rather
than relying on a remembered figure, and say in the notes when a number is
observational or contested.

## This file and the starters' files

Each starter folder holds its own `CLAUDE.md`. Those govern a student working on
their own proposal, and they ship to students. This one governs the workspace
where the seminar is built and does not ship.
