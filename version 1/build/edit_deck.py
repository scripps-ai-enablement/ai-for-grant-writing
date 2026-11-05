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
r0.text = "Download the starter folder"
a = add_run_after(r1, " [link]")                      # orange, like the first link
b = copy.deepcopy(r0._r); a.addprevious(b)            # navy text between the links
b.find("{http://schemas.openxmlformats.org/drawingml/2006/main}t").text = " and the example"
c = copy.deepcopy(r0._r); a.addnext(c)
c.find("{http://schemas.openxmlformats.org/drawingml/2006/main}t").text = ", and unzip both"

# The two placeholders become the download links. /releases/latest/download/
# always resolves to the newest release, so the deck does not name a tag and
# does not have to be re-edited when a later version ships.
RELEASES = ("https://github.com/scripps-ai-enablement/ai-for-grant-writing"
            "/releases/latest/download/")
links = [r for r in step1.runs if r.text == " [link]"]
expect(len(links), 2, "26 step 1 placeholders")
for run, zip_name in zip(links, ("grantwriting-starter.zip", "grantwriting-example.zip")):
    run.text = " (zip)"
    run.hyperlink.address = RELEASES + zip_name

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
    for text, colour in parts:
        run = para.add_run()
        run.text = text
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = font
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


def plate(slide, shape_kind, left, top, width, height, colour):
    """A filled shape with no outline and no shadow."""
    sp = slide.shapes.add_shape(shape_kind, Emu(left), Emu(top),
                                Emu(width), Emu(height))
    sp.fill.solid()
    sp.fill.fore_color.rgb = colour
    sp.line.fill.background()
    sp.shadow.inherit = False
    return sp


contact = prs.slides.add_slide(prs.slides[0].slide_layout)
contact.background.fill.solid()
contact.background.fill.fore_color.rgb = NAVY
plate(contact, MSO_SHAPE.RECTANGLE, 0, 0, 152391, 6857954, ORANGE)

text_box(contact, MARGIN, 812750, 10883421, 309802,
         [("CONTACT \u00b7 RESOURCES", ORANGE)], 16, bold=True)
text_box(contact, MARGIN, 1198745, 10883421, 700000,
         [("Where to find help", CREAM)], 44, font="Georgia")

COL = 7200000
text_box(contact, MARGIN, 2600000, COL, 300000, [("EMAIL", ORANGE)], 14, bold=True)
text_box(contact, MARGIN, 2950000, COL, 520000,
         [("bgood@scripps.edu", CREAM)], 26)
text_box(contact, MARGIN, 4050000, COL, 300000,
         [("RESEARCH-AI MAILING LIST", ORANGE)], 14, bold=True)
text_box(contact, MARGIN, 4400000, COL, 1000000,
         [("Email ", MUTED), ("listserv@scripps.edu", ORANGE),
          (" with ", MUTED), ("subscribe research-ai", ORANGE),
          (" in the body of the message", MUTED)], 22)

CARD = 2700000
CARD_X = RIGHT - CARD
CARD_Y = 2950000
PAD = 240000
text_box(contact, CARD_X, 2600000, CARD, 300000, [("SLACK", ORANGE)], 14, bold=True)
qr_card = plate(contact, MSO_SHAPE.ROUNDED_RECTANGLE,
                CARD_X, CARD_Y, CARD, CARD, WHITE)
qr_card.adjustments[0] = 0.05
contact.shapes.add_picture(QR, Emu(CARD_X + PAD), Emu(CARD_Y + PAD),
                           Emu(CARD - 2 * PAD), Emu(CARD - 2 * PAD))
text_box(contact, CARD_X, CARD_Y + CARD + 110000, CARD, 600000,
         [("Scan to join the Research AI workspace", MUTED)], 14)

seed_notes(contact, S(18)).text = "\n\n".join([
    "Thirty seconds now, as the introduction, and the same slide again at the "
    "end, as the answer to what to do when you get stuck next week.",

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

# add_slide appends, so move it from the end into second place.
slide_ids = prs.slides._sldIdLst
slide_ids.insert(1, slide_ids[-1])

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
