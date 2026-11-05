"""Build the deck of record from the hand-made deck it descends from.

Reads source.pptx and writes ../Using AI for Grant Writing v1.pptx.

source.pptx describes an earlier shape of the folders that ship with the deck:
an invented sample inside the starter, and no example folder beside it. The
edits below bring the deck in line with the folders as they now are. No slides
are added, removed or moved, and each edit checks the text it replaces first,
so the script stops rather than overwrite a slide that has been edited by hand
since.

Run from this folder:  python3 edit_deck.py
"""
import copy

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
add_note_after(notes(26), 6, "There are two downloads now. The starter is empty apart from the "
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

# -------------------------------------------------------- the contact slide
# A slide of contact details goes in after the title slide, which moves every
# later slide up by one. Every edit above addresses slides by their position in
# source.pptx, so this runs last, and the deck's own cross-references are
# renumbered here to match the finished deck.

retarget_note(notes(8), 12, "slide 17", "slide 18")
retarget_note(notes(28), 4, "slide 17", "slide 18")
retarget_note(notes(19), 0, "Slide 5 said", "Slide 6 said")
retarget_note(notes(20), 6, "slide 5,", "slide 6,")
retarget_note(notes(20), 6, "slide 3,", "slide 4,")
foot20 = shape(S(20), name="Footnote").text_frame.paragraphs[0]
expect(foot20.runs[0].text[:8], "Slide 5:", "20 footnote")
foot20.runs[0].text = foot20.runs[0].text.replace("Slide 5:", "Slide 6:", 1)

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
        ("grantwriting-example", " \u2014 a funded R21, with the reviews"),
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
    "a file, so it keeps working when a later version ships. The release page "
    "also carries the three folders separately for anyone who wants only one.",

    "Send the same link in the calendar invite and again on the morning of the "
    "class. The ones who arrive with the folder already unzipped are the ones "
    "who get the full hour on their own writing.",

    "The usual snag is unzipping into a folder inside a folder, so the chosen "
    "folder holds one item rather than the three. Walk the room.",
])

# Put it immediately before the hands-on slide.
slide_ids.insert(prs.slides.index(hands_on), slide_ids[-1])

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
assert not dropped, f"parts dropped: {sorted(dropped)}"
added = [n for n in new.namelist() if n not in set(src.namelist())]
changed = []
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as out:
    for info in src.infolist():
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
