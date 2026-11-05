# build/

`../Using AI for Grant Writing v1.pptx` is the artifact of record. It is
produced from `source.pptx` by `edit_deck.py`, and `source.pptx` is a deck that
was built and edited by hand in PowerPoint. `research-ai-slack-qr.png` is the
QR code the script places on the contact slide.

Run the script from this folder:

```
python3 edit_deck.py
```

It reads `source.pptx` and overwrites the deck one level up. Each edit checks
the text it is about to replace, so the script stops rather than overwrite a
slide that has moved. Anything edited in the `.pptx` by hand is discarded by a
rerun, so check which of the two files is newer before running it.

The script adds two slides and removes or moves none. Eighteen of
`source.pptx`'s parts differ in the output, and nine are new: the two slides,
their relationships and their notes, and the QR image, which both of them share.
Every other part keeps `source.pptx`'s bytes, so the author's own slides carry
their original XML.

## What the script changes

Slide numbers below are positions in `source.pptx`. The contact slide goes in
second, so every slide after the title is one higher in the finished deck; its
closing copy goes on the end, which shifts nothing.

`source.pptx` describes an earlier shape of the folders: an invented sample
inside the starter, and no `grantwriting-example` beside it. Most of the edits
bring the deck in line with the folders as they now are.

- **a contact slide, twice:** email address, the LISTSERV command that
  subscribes to research-ai, and a QR code for the Slack workspace. One copy is
  second in the deck, for the introduction; the other is last, after the
  questions, to leave up while the room clears. Both are built by the same
  function and are identical on screen, so the room recognises the second one.
  Only the speaker notes differ.
- **8, 19, 20 and 28:** the deck refers to its own slides by number in five
  places, four in speaker notes and one in slide 20's footnote, which the
  audience sees. Each is raised by one to match the finished deck.
- **18:** the footnote sent students without a draft to an invented sample in
  the starter. It now sends them to the example folder, and the notes that
  described the sample describe the 2012 R21 instead.
- **26:** step 1 gains a second link, so the starter and the example are both
  downloaded. Both links point at `releases/latest/download/` in the public
  repository, which resolves to the newest release, so a later version needs no
  edit here. The footnote tells students without a draft to choose
  `grantwriting-example` in step 3. Step 3 itself is unchanged. The notes gain a
  paragraph on the two downloads.
- **19 and 20:** the notes located the dinner demo in a numbered directory one
  level up. They now point at `demo/`, beside the deck.
- **27:** a notes paragraph lists the placeholder files in the starter and what
  the example adds.
- **30:** a notes paragraph for students in the example, pointing to the saved
  Aims review.
- **32:** the notes on the sample's planted gaps describe the gaps in the
  example instead, all of which the saved biosketch report names.
- **33:** a notes paragraph on the example's saved panel.
- **theme:** hyperlink text takes its colour from the theme's `<a:hlink>` rather
  than from the run's own fill, so the theme colour is the orange the two links
  on slide 26 are styled in. They are the only hyperlinks in the deck.

## Checked

Rendered to PDF with LibreOffice and inspected at full size, keeping the slide
numbering used above. Slides 18 and 26 each hold one-line text in every box,
with nothing clipped. Measured from the PDF, the edited text is 14pt in the
footnotes and 20pt in the steps, at or above the floors in the workspace
`CLAUDE.md`. Slide 26's two links carry the release URLs as PDF link
annotations, and they render in the deck's orange with an underline, which is
what separates them from the plain orange the slide uses for file names.

The contact slide sets type at 44pt for the heading, 26pt and 22pt for the two
text entries, and 16pt and 14pt for the kicker, the three labels and the caption
under the code. Its boxes carry no shrink-on-overflow, so those are the rendered
sizes. Both copies render pixel-identically, and the QR code was decoded back
out of each rendered page at 150 dpi, returning the Slack invite URL. That is
the check that matters: a code that survives PowerPoint but not the projector is
no use.

The same measurement found text below the floors on two of the author's slides,
which the script does not touch: slide 3 has labels at 10.1-12.4pt and
three-column text at 13.3pt, and slide 4 has step text at 12pt. They are left as
they are.
