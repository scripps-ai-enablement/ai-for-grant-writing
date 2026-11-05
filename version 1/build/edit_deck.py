"""Build the deck of record from the hand-made deck it descends from.

RETIRED: do not run. From 5 November 2026 the deck is edited by hand in
PowerPoint, and a rerun would overwrite it and discard those edits. See
README.md in this folder.

Reads source.pptx and writes ../Using AI for Grant Writing v1.pptx.

source.pptx describes an earlier shape of the folders that ship with the deck:
an invented sample inside the starter, and no example folder beside it. The
edits below bring the deck in line with the folders as they now are, add the
contact and download slides, and remove the repetition the hands-on half had
accumulated. Each edit checks the text it replaces first, so the script stops
rather than overwrite a slide that has been edited by hand since.

Run from this folder:  python3 edit_deck.py --force
"""
import copy
import sys

if "--force" not in sys.argv:
    raise SystemExit("edit_deck.py is retired: the deck is now edited by hand, and a "
                     "rerun would discard those edits. See README.md. Pass --force to "
                     "run it anyway.")

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Emu, Pt

SRC = "source.pptx"
QR = "research-ai-slack-qr.png"
DOWNLOAD_QR = "downloads-qr.png"
SHORT_LINK = "https://tinyurl.com/trbio431-ai"   # -> /releases/latest
OUT = "../Using AI for Grant Writing v1.pptx"


def shape(slide, name=None, shape_id=None):
    for sh in slide.shapes:
        if (name and sh.name == name) or (shape_id and sh.shape_id == shape_id):
            return sh
    raise KeyError(name or shape_id)


def expect(actual, wanted, where):
    if actual != wanted:
        raise SystemExit(f"{where}: expected {wanted!r}, found {actual!r}. "
                         "The source has changed; update this script.")


def set_para(para, text):
    """Replace a paragraph's text, keeping its first run's formatting."""
    runs = para.runs
    runs[0].text = text
    for r in runs[1:]:
        r._r.getparent().remove(r._r)


def add_run_after(run, text):
    """Clone a run (formatting included) after itself, with new text."""
    new = copy.deepcopy(run._r)
    run._r.addnext(new)
    new.find("{http://schemas.openxmlformats.org/drawingml/2006/main}t").text = text
    return new


def retarget_note(notes, index, old, new):
    """Replace a phrase inside one notes paragraph, keeping its runs."""
    para = notes.paragraphs[index]
    expect(old in para.text, True, f"notes paragraph {index}")
    for run in para.runs:
        if old in run.text:
            run.text = run.text.replace(old, new)
            return
    raise SystemExit(f"notes paragraph {index}: {old!r} is split across runs; "
                     "update this script.")


def add_note_after(notes, index, text):
    """Insert an empty spacer paragraph and a text paragraph after
    paragraph `index`, copying the notes' own paragraph formatting."""
    paras = notes.paragraphs
    model = paras[index]._p
    spacer = next(p._p for p in paras if not p.runs)
    new_spacer, new_text = copy.deepcopy(spacer), copy.deepcopy(model)
    model.addnext(new_spacer)
    new_spacer.addnext(new_text)
    runs = new_text.findall("{http://schemas.openxmlformats.org/drawingml/2006/main}r")
    runs[0].find("{http://schemas.openxmlformats.org/drawingml/2006/main}t").text = text
    for r in runs[1:]:
        new_text.remove(r)


def drop_note(notes, index):
    """Remove one notes paragraph and the empty spacer that follows it."""
    p = notes.paragraphs[index]._p
    spacer = p.getnext()
    p.getparent().remove(p)
    if spacer is not None and not spacer.findall(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}r"):
        spacer.getparent().remove(spacer)


def drop_shape(slide, shape_id):
    sh = shape(slide, shape_id=shape_id)
    sh._element.getparent().remove(sh._element)


def drop_slide(slide):
    """Take a slide out of the deck. Its part, and its notes, are no longer
    reachable from the presentation, so they are not written."""
    for sld_id in list(prs.slides._sldIdLst):
        if prs.part.related_part(sld_id.rId) is slide.part:
            prs.slides._sldIdLst.remove(sld_id)
            prs.part.drop_rel(sld_id.rId)
            return slide.part
    raise SystemExit("slide to drop is not in the deck")


prs = Presentation(SRC)
S = lambda n: prs.slides[n - 1]
notes = lambda n: S(n).notes_slide.notes_text_frame

# ------------------------------------------------------------------ slide 18
foot = shape(S(18), shape_id=15).text_frame.paragraphs[0]
expect(foot.runs[0].text, "Bring up a draft now if you have one, any section. No draft? "
       "The folder ships with an invented sample, and everything runs on that.", "18 footnote")
set_para(foot, "Bring up a draft now if you have one, any section. No draft? Use the example "
         "folder: a real 2012 R21, every skill already run on it.")

n18 = notes(18).paragraphs
expect(n18[6].text[:52], "If people have a draft, now is the moment to open it", "18 notes P4")
expect(n18[8].text[:34], "The sample is an invented F31 on w", "18 notes P5")
set_para(n18[6], "If people have a draft, now is the moment to open it. Anyone without one "
         "works in the example folder instead. It holds a real application rather than a "
         "planted one: the R21 that Andrew Su and I submitted in October 2012 under "
         "PAR-09-219, which was not funded.")
set_para(n18[8], "It proposes a game, The Cure, in which biologists pick genes to build "
         "predictors of breast cancer survival. The text is as submitted, mistakes included, "
         "and reviews/ already holds one run of each skill, so anyone working there can run "
         "a skill and compare their run with the saved one. What the skills find is real: "
         "the text says twenty genes where Figure 2 lists eighteen, for one.")

# -------------------------------------------------------------- slides 19, 20
# The demo files sit in demo/ beside the deck, not in a numbered directory one
# level up. Point the notes at where a reader of this folder will find them.
retarget_note(notes(19), 6, "in version 8/demo/dinner-demo/", "in demo/dinner-demo/")
retarget_note(notes(20), 0, "in version 8/demo/", "in demo/")

# ------------------------------------------------------------------ slide 26
step1 = shape(S(26), name="Step 1 text").text_frame.paragraphs[0]
r0, r1 = step1.runs
expect((r0.text, r1.text), ("Download the starter folder and unzip it", " [link]"), "26 step 1")
# The download has a slide of its own now, so step 1 only says what to do with
# the file. r1 carries the rust the deck uses for file names; keep it for the
# folder name and clone r0's navy for the tail.
r0.text = "Unzip "
r1.text = "grantwriting-seminar"
r1.font.name = "Courier New"          # file names on the light slides
tail = copy.deepcopy(r0._r)
r1._r.addnext(tail)
tail.find("{http://schemas.openxmlformats.org/drawingml/2006/main}t").text = (
    ", the folder you just downloaded")

step3 = shape(S(26), name="Step 3 text").text_frame.paragraphs[0]
expect(step3.runs[1].text, "grantwriting-starter", "26 step 3")
expect(step3.runs[2].text, ". Leave Instructions empty. ", "26 step 3 tail")
step3.runs[2].text = " inside it. Leave Instructions empty. "

foot26 = shape(S(26), name="Footnote").text_frame.paragraphs[0]
expect(foot26.runs[0].text, "What you just watched, with your grant in place of dinner.", "26 footnote")
set_para(foot26, "What you just watched, with your grant in place of dinner. "
         "No draft? In step 3, choose grantwriting-example instead.")

n26 = notes(26).paragraphs
expect(n26[8].text[:13], "Walk the room", "26 notes")
add_note_after(notes(26), 6, "The bundle holds two project folders. The starter is empty apart from the "
               "rules and the skills, for anyone with a draft of their own. The example is the "
               "same folder filled with the 2012 R21 and the reviews each skill produced on it. "
               "Anyone without a draft makes their project from the example in step 3, and "
               "everyone can open it to see where each part of an application goes.")

# ------------------------------------------------------------------ slide 27
n27 = notes(27)
expect(n27.paragraphs[0].text[:24], "No hidden folders and no", "27 notes")
add_note_after(n27, 0, "In the starter, drafts/ and evidence/ hold one-line placeholders, each "
               "saying what goes in it: aims.md, significance.md, innovation.md, approach.md and "
               "summary.md in drafts/, and cv.md, products.md and references.md in evidence/. "
               "The example has all of them filled, plus the project summary, facilities, "
               "personnel and resource sharing sections, both biosketches and summaries of the "
               "letters of support.")

# ------------------------------------------------------------------ slide 30
n30 = notes(30)
expect(n30.paragraphs[8].text[:28], "The last instruction matters", "30 notes")
add_note_after(n30, 6, "Anyone in the example folder skips the first step: the Aims page is "
               "already there, and reviews/2026-11-04-aims-aims-checklist.md is a saved run to "
               "compare against. Its most serious problem was that the page never says what will "
               "be done. Ask whether their run agrees.")

# ------------------------------------------------------------------ slide 32
n32 = notes(32).paragraphs
expect(n32[8].text[:30], "On the sample inputs there are", "32 notes")
set_para(n32[8], "In the example the gaps are real. The CV records no ORCID iD; three products "
         "on the list (P11, P14, P15) have no record anyone could find; the prototype game has "
         "no author list or identifier; and evidence/biosketches/ holds the 2012 biosketch, "
         "which the skill must treat as layout only. The saved run in reviews/ names all of "
         "them. A run that quietly fills them in has just demonstrated the failure mode this "
         "whole session is about.")

# ------------------------------------------------------------------ slide 33
n33 = notes(33)
expect(n33.paragraphs[6].text[:30], "If someone's draft is early or", "33 notes")
add_note_after(n33, 6, "In the example, drafts/summary.md holds two sentences taken from the "
               "submitted project summary, standing in for the author's own, and the saved panel "
               "is in reviews/.")

# ------------------------------------------------- notes that had drifted
# Speaker notes that described an earlier version of their own slide.

n3 = notes(3).paragraphs
expect(n3[4].text.endswith("and the second line of the band is the one to dwell on: "
                           "recombining what exists is what it does by construction."),
       True, "3 notes")
set_para(n3[4], "AI is an excellent partner for exploring ideas. That does not automatically "
         "make it a good judge of which ideas are original, feasible or important: recombining "
         "what exists is what it does by construction.")

# Slide 5 follows the mechanism directly once it changes places with slide 4.
n5 = notes(5).paragraphs
expect(n5[0].text, "The right column is one property wearing five coats, and it is the "
       "mechanism from two slides ago seen from the outside.", "5 notes")
set_para(n5[0], "The right column is one property wearing four coats, and it is the mechanism "
         "from the slide before seen from the outside.")

n14 = notes(14).paragraphs
expect(n14[0].text[:40], "One slide, four lines, and the second is", "14 notes")
expect(n14[2].text, "The last row is the line of principle.", "14 notes P2")
set_para(n14[0], "The last three slides as a rule of thumb, for the jobs that were not on the "
         "list. Mechanical work goes to the model: it is consistent at volume, and a wrong "
         "answer can be caught. Delegating still means checking, and at volume that means "
         "sampling. You can check three citations over coffee. Nobody checks two hundred by "
         "hand, so you sample twelve, and if two fail you have not found two problems, you "
         "have found out the set is unreliable.")
set_para(n14[2], "The second row is the line of principle: creative and personal work, and "
         "work that teaches you something, stays yours.")

n36 = notes(36).paragraphs
expect("the caveats from the second slide" in n36[2].text, True, "36 notes")
retarget_note(notes(36), 2, "the caveats from the second slide", "the caveats on slide 17")

# ------------------------------------------- slides 7 and 8: self-automators
# Slide 7 is the self-automator warning. Slide 8's notes told it again; keep
# them to centaurs and cyborgs, and move the one new point, the NIH rule, to
# slide 7.
n8 = notes(8).paragraphs
expect(n8[8].text[:30], "Self-automators did the whole ", "8 notes P4")
expect(n8[10].text[:24], "The plus side is real. I", "8 notes P5")
expect(n8[12].text[:40], "For you: self-automating is defensible f", "8 notes P6")
expect(notes(7).paragraphs[8].text[:30], "To be fair to the authors, the", "7 notes P4")
add_note_after(notes(7), 8, "For you: self-automating is defensible for the mechanical jobs, "
               "like page and character limits. For a trainee it is the worst trade there is, "
               "because the point of an F31 is your training, and it runs into NIH's rule that "
               "applications substantially developed by AI will not be considered "
               "(NOT-OD-25-132, slide 18).")
for index in (12, 10, 8):
    drop_note(notes(8), index)

# -------------------------------------------------- slides 15 and 18: Part 2
# Two agendas for the same hour. Slide 18's cards replace slide 15's list and
# take over its place and its title; slide 15 is dropped below.
title18 = shape(S(18), shape_id=3).text_frame.paragraphs[0]
expect(title18.text, "The next hour, on your own writing", "18 title")
set_para(title18, "Part 2: the next hour, on your own writing")
expect(notes(18).paragraphs[2].text[:30], "The hour starts with a live de", "18 notes P2")
add_note_after(notes(18), 2, "Two slides come before the demo: signing in on the Scripps "
               "account, and the four lines nobody crosses.")
part2_list = S(15)

# ------------------------------------------------------------------ slide 16
# Policy 708's confidentiality rule is the first row of slide 17.
policy16 = shape(S(16), shape_id=9)
expect(policy16.text_frame.text, "Scripps Research Policy treats a funding proposal as "
       "confidential material, so it goes only into approved tools.", "16 policy line")
drop_shape(S(16), 9)

# ------------------------------------------------------------------ slide 19
# The three layers are set out in full on slide 23, after the demo. Here they
# are only named, with where each run happens, so the demo shows the rest.
for sid in (4, 5, 6, 7, 12, 13, 19, 20, 27, 28):
    drop_shape(S(19), sid)
for sid, old, new in ((11, "What you type", "A new chat, outside any project"),
                      (18, "Standing rules for a project",
                       "A new conversation in the dinner-demo project"),
                      (26, "A written method for one job",
                       "The same project, naming the shopping-list skill")):
    box = shape(S(19), shape_id=sid)
    expect(box.text_frame.text, old, f"19 layer text {sid}")
    set_para(box.text_frame.paragraphs[0], new)
    box.width = Emu(11695176 - 250000 - box.left)
n19 = notes(19).paragraphs
expect(n19[2].text[:30], "A prompt lasts one request. CL", "19 notes P1")
set_para(n19[2], "Name the three layers and leave it there: a prompt, a project's CLAUDE.md, "
         "and a skill. What each one is, how long it lasts and where it lives comes out of the "
         "demo, and the table after it puts the three side by side.")

# ---------------------------------------------------------- slides 29 to 31
# Slide 29 explained what a skill is, which the demo has already shown. Its one
# instruction, open the files before running them, moves to the exercise, and
# what a skill folder can hold moves to the biosketch slide, which shows it.
first30 = shape(S(30), shape_id=7).text_frame.paragraphs
expect(first30[1].text[:24], "Put your Aims page in dr", "30 First box")
opener = copy.deepcopy(first30[1]._p)
first30[1]._p.addprevious(opener)
set_para(shape(S(30), shape_id=7).text_frame.paragraphs[1],
         "Open skills/aims-checklist/SKILL.md, and the 22-item standard in reference/.")
expect(notes(30).paragraphs[0].text[:30], "This is the demo's third layer", "30 notes P0")
add_note_after(notes(30), 0, "Have them open skills/aims-checklist/SKILL.md before running it. "
               "It is about a page: which checklist to use, four steps, the rules, and the "
               "closing section on what it could not source. reference/checklist.md is the "
               "standard it holds the page to: 22 items from the opening paragraph to the "
               "closing one, then a 60-second reviewer test.")

n31 = notes(31)
expect(n31.paragraphs[0].text[:30], "This is why the biosketch is n", "31 notes P0")
expect(n31.paragraphs[4].text[:30], "Everything from the demo still", "31 notes P2")
add_note_after(n31, 4, "Nothing here is specific to grants. A lab analysis pipeline, a house "
               "style for figures, a release checklist for a dataset: same structure, same "
               "parts.")
add_note_after(n31, 0, "It is also the first skill on screen with more than a SKILL.md. A skill "
               "folder can hold reference documents, templates and scripts beside the "
               "instructions, and they are read only when the skill runs. The Aims checklist "
               "already had one, its reference/ standard.")
what_a_skill_is = S(29)

# Held by object for the moves at the end, after the inserts have renumbered.
agentic, nature, sign_in, next_hour = S(4), S(5), S(16), S(18)

# -------------------------------------------------------- the contact slide
# A slide of contact details goes in after the title slide, which moves every
# later slide up by one. Every edit above addresses slides by their position in
# source.pptx, so this runs last, and the deck's own cross-references are
# renumbered here to match the finished deck. Slide 5 keeps its number: the
# contact slide moves it up one and the swap with slide 4 below moves it back.

retarget_note(notes(28), 4, "slide 17", "slide 18")
retarget_note(notes(20), 6, "slide 3,", "slide 4,")

NAVY = RGBColor(0x14, 0x21, 0x3D)       # the dark slides' background
CREAM = RGBColor(0xF7, 0xF5, 0xEF)      # headings on it
ORANGE = RGBColor(0xE8, 0xA0, 0x6A)     # kickers, labels, things you type
MUTED = RGBColor(0xC9, 0xD1, 0xE0)      # body text
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
MARGIN = 812750                         # the left margin the deck uses
RIGHT = 11379250                        # and the right edge it stops at
COL = 7200000                           # the text column, left of the code
CARD = 2700000                          # the white plate the code sits on
CARD_X = RIGHT - CARD
CARD_Y = 2950000
PAD = 240000                            # the code's quiet zone on the plate

PAPER = RGBColor(0xEC, 0xE8, 0xDD)      # the light slides' background
INK = RGBColor(0x14, 0x21, 0x3D)        # headings and body on it
STEEL = RGBColor(0x2E, 0x6F, 0x95)      # kickers
RUST = RGBColor(0xB4, 0x52, 0x1A)       # file names and things you type
GREY = RGBColor(0x5A, 0x62, 0x72)       # footnotes
CARD_FILL = RGBColor(0xFF, 0xFD, 0xF8)  # the cards on the light slides
CARD_LINE = RGBColor(0xDE, 0xD8, 0xCA)


def text_box(slide, left, top, width, height, parts, size, bold=False,
             font="Arial", spacing=1.25):
    """A text box in the deck's own style. `parts` is (text, colour) pairs."""
    box = slide.shapes.add_textbox(Emu(left), Emu(top), Emu(width), Emu(height))
    frame = box.text_frame
    frame.word_wrap = True
    frame.margin_left = frame.margin_right = 0
    frame.margin_top = frame.margin_bottom = 0
    para = frame.paragraphs[0]
    para.line_spacing = spacing
    for part in parts:
        text, colour = part[0], part[1]
        run = para.add_run()
        run.text = text
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = part[2] if len(part) > 2 else font
        run.font.color.rgb = colour
    return box


def seed_notes(slide, model):
    """Give a new slide a notes body. The notes master carries no placeholders,
    so a new notes slide comes without one; clone it from a slide that has it."""
    body = copy.deepcopy(model.notes_slide.notes_placeholder._element)
    nvpr = body.find(".//{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr")
    nvpr.set("id", "10")
    slide.notes_slide.shapes._spTree.append(body)
    frame = slide.notes_slide.notes_text_frame
    frame.clear()
    return frame


def plate(slide, shape_kind, left, top, width, height, colour, line=None):
    """A filled shape with no shadow, outlined only when asked."""
    sp = slide.shapes.add_shape(shape_kind, Emu(left), Emu(top),
                                Emu(width), Emu(height))
    sp.fill.solid()
    sp.fill.fore_color.rgb = colour
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line
        sp.line.width = Pt(1)
    sp.shadow.inherit = False
    return sp


# The notes master carries no placeholders, so both copies borrow a notes body
# from a slide that has one. Hold the reference now: it survives the reordering
# below, which a slide number would not.
notes_model = S(18)
hands_on = S(26)       # found by object, not by number, after the inserts below


def contact_slide(speaker_notes):
    """Contact details, the mailing-list command and the Slack code. Built
    twice, identical on screen, so the room recognises it the second time."""
    slide = prs.slides.add_slide(prs.slides[0].slide_layout)
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = NAVY
    plate(slide, MSO_SHAPE.RECTANGLE, 0, 0, 152391, 6857954, ORANGE)

    text_box(slide, MARGIN, 812750, 10883421, 309802,
             [("CONTACT \u00b7 RESOURCES", ORANGE)], 16, bold=True)
    text_box(slide, MARGIN, 1198745, 10883421, 700000,
             [("Where to find help", CREAM)], 44, font="Georgia")

    text_box(slide, MARGIN, 2600000, COL, 300000, [("EMAIL", ORANGE)], 14, bold=True)
    text_box(slide, MARGIN, 2950000, COL, 520000,
             [("bgood@scripps.edu", CREAM)], 26)
    text_box(slide, MARGIN, 4050000, COL, 300000,
             [("RESEARCH-AI MAILING LIST", ORANGE)], 14, bold=True)
    text_box(slide, MARGIN, 4400000, COL, 1000000,
             [("Email ", MUTED), ("listserv@scripps.edu", ORANGE),
              (" with ", MUTED), ("subscribe research-ai", ORANGE),
              (" in the body of the message", MUTED)], 22)

    text_box(slide, CARD_X, 2600000, CARD, 300000, [("SLACK", ORANGE)], 14, bold=True)
    qr_card = plate(slide, MSO_SHAPE.ROUNDED_RECTANGLE,
                    CARD_X, CARD_Y, CARD, CARD, WHITE)
    qr_card.adjustments[0] = 0.05
    slide.shapes.add_picture(QR, Emu(CARD_X + PAD), Emu(CARD_Y + PAD),
                             Emu(CARD - 2 * PAD), Emu(CARD - 2 * PAD))
    text_box(slide, CARD_X, CARD_Y + CARD + 110000, CARD, 600000,
             [("Scan to join the Research AI workspace", MUTED)], 14)

    seed_notes(slide, notes_model).text = "\n\n".join(speaker_notes)
    return slide


contact_slide([
    "Thirty seconds here, in the introduction. The same slide closes the deck, "
    "so this is the first of two passes and the short one.",

    "Email is the one that always works. Say it as well as showing it.",

    "The mailing list runs on LISTSERV, so the command goes in the body of the "
    "message and the subject line is ignored: one line reading subscribe "
    "research-ai, and nothing else in it.",

    "The code decodes to https://join.slack.com/t/research-aihq/shared_invite/"
    "zt-444y0klbl-0Hu7f_ERWT52uD9l_v8IpQ. Shared invite links can be set to "
    "expire, so open it in a browser before class and generate a new code from "
    "Slack if it has lapsed.",

    "Leave the slide up while people get their phones out. Ten seconds is not "
    "long enough for the back of the room to focus on a code this size.",
])

# add_slide appends, so move that first copy from the end into second place.
slide_ids = prs.slides._sldIdLst
slide_ids.insert(1, slide_ids[-1])

# The closing copy stays where add_slide puts it, after the questions slide.
contact_slide([
    "The second slide again, at the end. The same three routes, now that they "
    "have a project and a draft of their own to get stuck on.",

    "Leave it up through the questions and while the room clears. This is the "
    "slide people photograph, and the code needs a few steady seconds.",

    "If the Slack invite has lapsed, the code is dead and the two email "
    "addresses are the only live routes on the slide. Worth knowing before "
    "someone tells you in the corridor.",
])

# ------------------------------------------------------- the download slide
# One slide whose whole job is getting the files onto 20 laptops: the short
# link big enough to read from the back and type, and the same link as a code
# for anyone who would rather use their phone. It goes immediately before the
# hands-on slide, whose position is found from the slide itself rather than by
# number, since the contact slide has already moved everything down by one.

download = prs.slides.add_slide(prs.slides[0].slide_layout)
download.background.fill.solid()
download.background.fill.fore_color.rgb = PAPER

text_box(download, MARGIN, 812750, 10883421, 309802,
         [("HANDS-ON \u00b7 GET THE FILES", STEEL)], 16, bold=True)
text_box(download, MARGIN, 1198745, 10883421, 700000,
         [("Download the folder", INK)], 40, font="Georgia")

text_box(download, MARGIN, 2450000, COL, 300000,
         [("TYPE THIS, OR SCAN THE CODE", RUST)], 14, bold=True)
link = text_box(download, MARGIN, 2800000, COL, 800000,
                [("tinyurl.com/trbio431-ai", RUST)], 36)
link.text_frame.paragraphs[0].runs[0].hyperlink.address = SHORT_LINK

text_box(download, MARGIN, 3850000, COL, 400000,
         [("One zip. Unzip it and you have three folders:", INK)], 20)
for row, (name, what) in enumerate((
        ("grantwriting-starter", " \u2014 for your own draft"),
        ("grantwriting-example", " \u2014 a real R21, with the reviews"),
        ("dinner-demo", " \u2014 the demo you just watched"))):
    text_box(download, MARGIN, 4320000 + row * 450000, COL, 400000,
             [(name, RUST, "Courier New"), (what, INK)], 20)

plate(download, MSO_SHAPE.ROUNDED_RECTANGLE, CARD_X, 2450000, CARD, CARD,
      CARD_FILL, line=CARD_LINE).adjustments[0] = 0.05
download.shapes.add_picture(DOWNLOAD_QR, Emu(CARD_X + PAD), Emu(2450000 + PAD),
                            Emu(CARD - 2 * PAD), Emu(CARD - 2 * PAD))

text_box(download, MARGIN, 5950000, 10883421, 400000,
         [("Everything in the next four steps happens inside that folder.", GREY)], 14)

seed_notes(download, notes_model).text = "\n\n".join([
    "This is the slide to be patient on. Put it up, read the link out, and "
    "wait until the room has stopped typing before moving on.",

    "The link is short so that it can be typed on a laptop, which is where the "
    "folder has to end up. The code is the same link, for anyone who would "
    "rather send it to their own phone and mail it on.",

    "tinyurl.com/trbio431-ai points at the repository's latest release, not at "
    "a file, so it keeps working when a later version ships. The bundle is the "
    "only thing attached to it, so there is nothing on that page to choose "
    "between except GitHub's own source archives, which it adds by itself.",

    "Send the same link in the calendar invite and again on the morning of the "
    "class. The ones who arrive with the folder already unzipped are the ones "
    "who get the full hour on their own writing.",

    "The usual snag is unzipping into a folder inside a folder, so the chosen "
    "folder holds one item rather than the three. Walk the room.",
])

# Put it immediately before the hands-on slide.
slide_ids.insert(prs.slides.index(hands_on), slide_ids[-1])

# ------------------------------------------------------ moves and removals
# By object, now that the inserts are done. The Part 2 cards take the place of
# the list they replace, ahead of the sign-in and the floor slides, which keep
# their numbers. The nature of generative AI follows the mechanism directly, and
# the move from chat to agents comes after it.


def sld_id(slide):
    for entry in slide_ids:
        if prs.part.related_part(entry.rId) is slide.part:
            return entry
    raise SystemExit("slide is not in the deck")


slide_ids.insert(prs.slides.index(sign_in), sld_id(next_hour))
slide_ids.insert(prs.slides.index(agentic), sld_id(nature))

removed = set()
for gone in (part2_list, what_a_skill_is):
    for part in (gone.part, gone.notes_slide.part):
        name = str(part.partname).lstrip("/")
        folder, base = name.rsplit("/", 1)
        removed |= {name, f"{folder}/_rels/{base}.rels"}
    drop_slide(gone)

# python-pptx re-serializes every XML part on save. Keep the source's bytes for
# every part whose content did not change, so the author's slides carry the
# same XML and only the edited parts differ.
import io
import zipfile

from lxml import etree


# Hyperlink text is coloured from the theme's <a:hlink>, which overrides the
# run's own fill, so the two links on slide 26 would come out the theme blue
# rather than the orange the placeholders were styled in. Set the theme colour
# instead. They are the only hyperlinks in the deck, so nothing else moves.
LINK_RGB = b"B4521A"
THEME = "ppt/theme/theme1.xml"
OLD_HLINK = b'<a:hlink><a:srgbClr val="0000FF"/></a:hlink>'


def retheme(data, name):
    if name != THEME:
        return data
    if OLD_HLINK not in data:
        raise SystemExit(f"{THEME}: hyperlink colour not where expected. "
                         "The source has changed; update this script.")
    return data.replace(OLD_HLINK, b'<a:hlink><a:srgbClr val="%s"/></a:hlink>' % LINK_RGB)


def canon(data, name):
    """Content of a part, ignoring serialization. Relationship and content-type
    entries are compared as sets, since python-pptx reorders them."""
    try:
        root = etree.fromstring(data)
    except etree.XMLSyntaxError:
        return data
    if name.endswith(".rels") or name == "[Content_Types].xml":
        return sorted(etree.tostring(c, method="c14n") for c in root)
    return etree.tostring(root, method="c14n")


buf = io.BytesIO()
prs.save(buf)
src, new = zipfile.ZipFile(SRC), zipfile.ZipFile(buf)
dropped = set(src.namelist()) - set(new.namelist())
assert dropped == removed, f"parts dropped: {sorted(dropped ^ removed)}"
added = [n for n in new.namelist() if n not in set(src.namelist())]
changed = []
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as out:
    for info in src.infolist():
        if info.filename in removed:
            continue
        old_b, new_b = src.read(info.filename), new.read(info.filename)
        same = canon(old_b, info.filename) == canon(new_b, info.filename)
        data = retheme(old_b if same else new_b, info.filename)
        out.writestr(info, data)
        if not same or data != old_b:
            changed.append(info.filename)
    for name in added:
        out.writestr(name, new.read(name))
print("wrote", OUT)
print("changed parts:", ", ".join(changed))
print("added parts:", ", ".join(added))
