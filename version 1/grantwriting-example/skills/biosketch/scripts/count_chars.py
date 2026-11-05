#!/usr/bin/env python3
"""Count characters (with spaces) in each section of a biosketch draft.

Usage: python3 count_chars.py drafts/biosketch-draft.md

Sections are found by their "## " headings. The Personal Statement is limited
to 3,500 characters and each "Contribution" section to 2,000, and there may be
at most five contributions. Lists of products are counted for information only.
The required sections are also checked for presence, since a short biosketch
can be an incomplete one. Exits with status 1 if any limit is exceeded, any
required section is missing, or there are too many contributions, so a script
or agent can tell pass from fail.

The prose sections may carry parenthetical references to listed products, such
as "(Chen et al., 2024)". They may not carry full bibliographic citations or
links, so those are reported as warnings.
"""
import re
import sys

LIMITS = {"personal statement": 3500, "contribution": 2000}
MAX_CONTRIBUTIONS = 5

# Markers of a full bibliographic citation or a link, which the Supplement
# does not allow in the running text. A bare parenthetical author-year is fine.
BIBLIOGRAPHIC = re.compile(
    r"PMID|PMCID|PMC\d|doi:|DOI:|https?://|\[\d+\]|\d{4};\s*\d+|\d+\(\d+\):\s*\d+",
    re.IGNORECASE,
)


def sections(text):
    current, body = None, []
    for line in text.splitlines():
        if line.startswith("## "):
            if current is not None:
                yield current, "\n".join(body).strip()
            current, body = line[3:].strip(), []
        elif current is not None:
            body.append(line)
    if current is not None:
        yield current, "\n".join(body).strip()


def limit_for(title):
    t = title.lower()
    for key, limit in LIMITS.items():
        if t.startswith(key):
            return limit
    return None


def check_structure(titles):
    """Report required sections that are missing. Length is not the only way to fail."""
    missing = []
    lowered = [t.lower() for t in titles]
    if not any(t.startswith("personal statement") for t in lowered):
        missing.append("Personal Statement")
    if not any("closely related" in t for t in lowered):
        missing.append("Products closely related to the proposed project")
    if not any("other significant" in t for t in lowered):
        missing.append("Other significant products")
    if not any(t.startswith("contribution") for t in lowered):
        missing.append("at least one Contribution to Science")
    return missing


def main(path):
    text = open(path, encoding="utf-8").read()
    over = False
    titles = [t for t, _ in sections(text)]
    missing = check_structure(titles)
    for name in missing:
        print(f"MISSING SECTION: {name}")
    n_contrib = sum(1 for t in titles if t.lower().startswith("contribution"))
    too_many = n_contrib > MAX_CONTRIBUTIONS
    if too_many:
        print(f"TOO MANY CONTRIBUTIONS: {n_contrib}, limit {MAX_CONTRIBUTIONS}")
    for title, body in sections(text):
        # Collapse line breaks inside paragraphs the way a form field would.
        flat = re.sub(r"\s*\n\s*", " ", body)
        n = len(flat)
        limit = limit_for(title)
        if limit is None:
            print(f"{title}: {n} characters (no limit)")
            continue
        status = "OK" if n <= limit else f"OVER by {n - limit}"
        over = over or n > limit
        print(f"{title}: {n} / {limit} characters - {status}")
        if limit == 2000 and n < 1500:
            print(f"  note: short. The method suggests around 1,500 characters here.")
        hit = BIBLIOGRAPHIC.search(flat)
        if hit:
            print(
                f"  warning: '{title}' contains {hit.group(0)!r}, which looks like a full "
                "citation or a link. Parenthetical product references only."
            )
    return 1 if (over or missing or too_many) else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
