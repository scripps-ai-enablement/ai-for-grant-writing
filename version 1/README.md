# version 1

| Path | What it is | Ships to students |
|---|---|---|
| `Using AI for Grant Writing v1.pptx` | The deck, and the artifact of record | Presented |
| `grantwriting-seminar.zip` | All three student folders in one download, which is what slide 27 links to | Yes |
| `grantwriting-starter/`, `.zip` | The starter: rules, skills, and a one-line placeholder for each part of a proposal | Yes |
| `grantwriting-example/`, `.zip` | The same folder filled with a 2012 R21 (PAR-09-219), with all five skills run on it | Yes |
| `demo/dinner-demo/`, `.zip` | The three-layer demo from slides 21-23 | Yes |
| `demo/README.md` | How to run that demo live, and what each layer produced in testing | Instructor |
| `TEST-BEFORE-CLASS.md` | Pre-class checks on the app and the account the students will use | Instructor |
| `build/` | The deck this one descends from, the script that produces it, the QR code it places, and what was checked | No |

The starter and the example hold identical `CLAUDE.md` and `skills/` folders.
They differ only in whether the drafts are filled in: students with a proposal
of their own work in the starter, and students without one work in the example,
which is also where anyone can look to see where each part of an application
goes.

## Publishing

Slide 27 shows one short link, `tinyurl.com/trbio431-ai`, which redirects to
`github.com/scripps-ai-enablement/ai-for-grant-writing/releases/latest`. It
points at the release page rather than at a file, so it survives both a new
version and a change of file names, and it is short enough to be typed from the
back of a room onto a laptop, which is where the folder has to end up.

Publishing a version means rebuilding the four zips from the folders and
attaching them to a new release. `grantwriting-seminar.zip` is the one students
are told to take; the other three are there for anyone who wants a single
folder.
