# version 1

| Path | What it is | Ships to students |
|---|---|---|
| `Using AI for Grant Writing v1.pptx` | The deck, and the artifact of record | Presented |
| `grantwriting-starter/`, `.zip` | The starter: rules, skills, and a one-line placeholder for each part of a proposal | Yes |
| `grantwriting-example/`, `.zip` | The same folder filled with a 2012 R21 (PAR-09-219), with all five skills run on it | Yes |
| `demo/` | The dinner demo for slides 21-23 | Instructor |
| `TEST-BEFORE-CLASS.md` | Pre-class checks on the app and the account the students will use | Instructor |
| `build/` | The deck this one descends from, the script that produces it, the QR code it places, and what was checked | No |

The starter and the example hold identical `CLAUDE.md` and `skills/` folders.
They differ only in whether the drafts are filled in: students with a proposal
of their own work in the starter, and students without one work in the example,
which is also where anyone can look to see where each part of an application
goes.

## Publishing

Slide 26's two download links point at
`github.com/scripps-ai-enablement/ai-for-grant-writing/releases/latest/download/`,
which always resolves to the newest release, so the deck does not name a tag and
does not have to be re-edited when a later version ships. Publishing a version
means attaching its two zips to a new release there.
