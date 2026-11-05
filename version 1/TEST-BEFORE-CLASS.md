# Test before class

Run this on the same app and account the students will use, ideally a
student-like account rather than yours. It takes about fifteen minutes and
covers two things: the live demo (slides 20-22) and the grant project students
open afterwards (slides 26-30).

Documented: projects are created from Projects > + > "Use an existing folder",
and hold a folder, an Instructions box and a memory
([help center](https://support.claude.com/en/articles/14116274)). Skills
uploaded under Customize > Skills trigger on their description
([help center](https://support.claude.com/en/articles/12512180)).
Only observed: that the desktop app reads a project folder's `CLAUDE.md` into
every conversation. The checks below settle it for the students' account.

Write down the app version (Claude menu, About) and whether the message box
shows "Chat" and "Cowork" options. If it shows neither, the account has the
merged experience; the slides still apply.

Use a new conversation for every run. Projects have memory, and a run can
carry what an earlier one in the same project learned.

## The demo

Follow `demo/README.md`. What to check at each layer:

1. **A prompt** (plain chat): a typical dinner that ignores the kitchen. In
   test runs, chicken in the oven for four.
2. **+ CLAUDE.md** (project from `demo/dinner-demo/`): vegetarian, 30 minutes,
   no oven, one dinner, built from `pantry.md`. Before asking about dinner,
   ask "What rules are you following in this project?" It should quote
   `CLAUDE.md`. It should not open `skills/`.
3. **+ a skill**: the list has "Already have", store sections in order, and a
   closing line on whether the check passed.

If layer 2 cannot quote the rules, the app is not reading `CLAUDE.md`. Paste
its contents into the project's Instructions box, rerun, and say in class that
the Instructions box is where standing rules go on this account.

## The grant project

Create a project from the unzipped `grantwriting-starter`, Instructions empty.

1. Ask "What rules are you following in this project? Quote the first one."
   Pass: it quotes "Never write or rewrite the Specific Aims, the hypothesis,
   the Significance or the Approach." If not, use the Instructions-box fallback
   above and change step 3 on slide 26.
2. The starter's drafts are empty, so run this one in a second project made
   from `grantwriting-example.zip`, unzipped somewhere new so the version
   folder's copy keeps its saved reviews. That is also where students with no
   draft of their own will work. In a new conversation there: "Follow
   skills/aims-checklist/SKILL.md to check my Aims page." This has to pass.
   Pass means it opens the `SKILL.md` and its
   checklist, gives a table of items with quoted sentences, runs the 60-second
   reviewer test, saves a review to `reviews/`, appends one line to
   `ai-use-log.md`, and ends with "What I could not source". If it fails, fix
   folder access before class: check that the folder was selected rather than
   individual files, and that the unzip did not leave a folder inside a folder.

## One more worth checking

Upload `skills/biosketch` as a zip under Customize > Skills, toggle it on, then
ask "draft my biosketch" in a conversation outside the project. That is the
"keep it" step in exercise 4. On an Enterprise account an owner can turn the
upload option off; if it is missing, ask IT before class. Delete the uploaded
copy afterwards for a clean test next time.
