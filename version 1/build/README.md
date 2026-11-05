# build/

**Retired. Do not run `edit_deck.py`.** From 5 November 2026 the deck,
`../Using AI for Grant Writing v1.pptx`, is edited by hand in PowerPoint. A
rerun would overwrite it from `source.pptx` and discard every hand edit since.
This folder is kept as the record of how the deck reached the state it was in
when hand editing began; the deck itself is the artifact of record.

Until then, the deck was produced from `source.pptx` by `edit_deck.py`, and
`source.pptx` is a deck that was built and edited by hand in PowerPoint. The two
`.png` files are the QR codes the script placed: `research-ai-slack-qr.png` on
the contact slide, and `downloads-qr.png`, which encodes
`tinyurl.com/trbio431-ai`, on the download slide.

The script read `source.pptx` and overwrote the deck one level up. Each edit
checked the text it was about to replace, so the script stopped rather than
overwrite a slide that had moved.

The script adds three slides, removes two and moves two. Twenty-five of
`source.pptx`'s parts differ in the output, fourteen are new (the three slides,
their relationships and their notes, and the two QR images, one of which is
shared by the two copies of the contact slide) and the two removed slides' parts
are left out. Every other part keeps `source.pptx`'s bytes, so the author's own
slides carry their original XML.

## What the script changes

Slide numbers below are positions in `source.pptx`. The finished deck has 37
slides. The contact slide goes in second, which moves every later slide up one.
Slides 4 and 5 change places. Slide 18 takes the place of slide 15, which is
removed, so slides 16 and 17 keep their finished numbers (17 and 18) and
everything from 19 to 25 lands on its own number. The download slide goes in
before 26, and slide 29 is removed, so 26 to 28 run one higher and 30 onward
land on their own numbers. The closing copy of the contact slide goes last.

`source.pptx` describes an earlier shape of the folders: an invented sample
inside the starter, and no `grantwriting-example` beside it. Most of the edits
bring the deck in line with the folders as they now are.

- **a contact slide, twice:** email address, the LISTSERV command that
  subscribes to research-ai, and a QR code for the Slack workspace. One copy is
  second in the deck, for the introduction; the other is last, after the
  questions, to leave up while the room clears. Both are built by the same
  function and are identical on screen, so the room recognises the second one.
  Only the speaker notes differ.
- **7, 19, 20, 28 and 36:** the deck refers to its own slides by number in
  speaker notes and in slide 20's footnote, which the audience sees. Each now
  names the finished deck's slide. The references to slide 5, the nature of
  generative AI, keep their number, because the swap with slide 4 puts it back
  in fifth place.
- **18:** the footnote sent students without a draft to an invented sample in
  the starter. It now sends them to the example folder, and the notes that
  described the sample describe the 2012 R21 instead.
- **a download slide, before 26:** the short link set large enough to read from
  the back of the room and type, and the same link as a QR code for anyone who
  would rather use their phone. It names the three folders in the bundle. The
  download used to be step 1 of the slide that follows, where the room was
  reading the next three steps while still downloading.
- **26:** step 1 no longer carries the download, only what to do with the file,
  and step 3 says to choose the starter inside the unzipped folder. The footnote
  tells students without a draft to choose `grantwriting-example` in step 3. The
  notes gain a paragraph on the downloads.
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
  than from the run's own fill, so the theme colour is the rust the deck uses for
  file names and things you type. The short link on the download slide is the
  only hyperlink in the deck.

### Removing repetition

- **15 and 18:** two agendas for the same hour. Slide 18's three cards replace
  slide 15's list, take its place, and take the "Part 2" title, so the hour is
  introduced once, ahead of the sign-in and the floor slides. The notes gain a
  line saying those two come before the demo. Slide 15 is removed.
- **16:** the closing line on Policy 708 repeated the first row of slide 17,
  and is removed.
- **19:** the three layers were set out in a table before the demo and again,
  in the same terms, on slide 23 after it. The headers and the "how long it
  lasts" and "where it lives" columns are removed; each layer keeps its name and
  says where its run happens. The notes no longer define the layers in advance.
- **29:** "What a skill is" repeated what the dinner demo had shown, and is
  removed. Its one instruction, open the skill's files before running it, is the
  first item in slide 30's First box, and its notes move to slide 30 (what is
  in the Aims skill) and slide 31 (what else a skill folder can hold, and that
  nothing in it is specific to grants).
- **7 and 8:** slide 8's notes retold slide 7's account of self-automators.
  They now keep to centaurs and cyborgs, and the one new point, the NIH rule on
  applications substantially developed by AI, moves to slide 7's notes.

### Order

- **4 and 5:** the nature of generative AI now follows the mechanism directly,
  and the move from chat to agents comes after it.

### Notes that had drifted from their slides

- **3:** the notes pointed at the second line of a band that has one line.
- **5:** "five coats" for a column of four, and "two slides ago" for the slide
  before.
- **14:** the notes described four lines and a last row; the slide has two
  if/then rows. They now walk through those, keeping the point about sampling.
- **26:** "two downloads now" for what is one bundle holding two project
  folders.
- **36:** "the caveats from the second slide" are on slide 17.

## Checked

Rendered to PDF with LibreOffice and inspected at full size, keeping the slide
numbering used above. Slides 18 and 26 each hold one-line text in every box,
with nothing clipped. Measured from the PDF, the edited text is 14pt in the
footnotes and 20pt in the steps, at or above the floors in the workspace
`CLAUDE.md`.

The download slide sets the link at 36pt, which fits on one line with room to
spare, the heading at 40pt, the folder list at 20pt, and the kicker, the label
and the footnote at 16pt and 14pt. The link carries its URL as a PDF link
annotation. `tinyurl.com/trbio431-ai` was followed end to end and lands on the
release page, and the bundle downloads from there and unzips to the three
folders the slide names.

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

After the edits that remove repetition, the finished deck was rendered the same
way. Slides 16, 17, 19 and 30 keep their text inside their boxes; slide 30's
First box is the fullest, and its third item ends above the box's lower edge.
Every reference by number, in the notes and on the slides, was listed from the
finished deck and checked against the slide it names.
