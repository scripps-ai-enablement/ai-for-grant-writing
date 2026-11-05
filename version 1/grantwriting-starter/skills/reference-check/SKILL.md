---
name: reference-check
description: Check every citation in a draft against the source. Confirm the paper exists, record its PMID or DOI, and judge whether it actually supports the sentence that cites it, using the PubMed connector where available. Use when asked to check, verify or audit references or citations. Never fixes a citation by substituting a different paper.
---

# Reference check

Two things go wrong with citations in an AI-assisted draft, and they are not
equally hard.

**A reference that does not exist** is the easy case. It fails the first lookup,
tools catch it, and newer models invent far fewer of them than the models that
produced the alarming numbers in the 2023 literature. Treat it as a real but
diminishing problem.

**A real paper cited for a claim it does not make** is the hard case, and it has
not gone away. It survives every check except reading the paper. The citation is
correctly formatted, the authors and year are right, the paper exists and is
relevant to the topic, and the sentence it is attached to says something the
paper never established. This also happens to people writing without any AI at
all, which is part of why it is hard to spot.

So this skill spends most of its effort on support rather than on existence.

## Steps

1. Read the draft the author names. Extract every citation together with the
   sentence it supports. Handle numbered references, author-year citations and
   reference lists.
2. For each citation, find the paper:
   - With the PubMed connector, search by PMID or DOI if given, otherwise by
     title and first author.
   - Without a connector, look in `evidence/`, then use web search if available.
   - **Never confirm a paper from memory.** If you cannot look it up, mark it
     "not checked" rather than guessing. An unchecked citation reported honestly
     is useful; a confirmed one that was never checked is worse than nothing.
3. Record, for each citation:
   - **found**: yes, no, or ambiguous (several candidates);
   - **identifier**: PMID and DOI where found;
   - **details match**: do authors, year, title and journal match the draft?
   - **support**: does the abstract, or the full text where it is in
     `evidence/`, support the sentence that cites it? Answer supports, partly,
     does not, or cannot tell from the abstract;
   - **in evidence/**: whether the author has the paper in the folder.
4. Summarize in this order, strongest signal first: citations whose paper does
   not support the sentence, citations that need the full text to judge,
   citations whose details do not match, and citations not found.

## Rules

- Never replace a missing or wrong reference with a different paper. Report the
  problem and let the author decide. Substituting a plausible paper is how a
  citation problem becomes invisible.
- Quote the cited sentence exactly.
- "Cannot tell from the abstract" is an honest answer and the correct one more
  often than it feels. Use it rather than reasoning from the title.
- An abstract supporting a sentence is weaker evidence than it looks. Where the
  draft leans hard on a paper, say that the abstract is not enough and the
  author should read it.
- Save the result to `reviews/YYYY-MM-DD-<section>-reference-check.md`, where
  `<section>` is the draft's name, or `full` when several were checked together.
- Append one line to `ai-use-log.md` with a shell append (`>>`). Never rewrite
  that file: another run may be in progress, and rewriting loses its lines.

## Output

A table with one row per citation: the citation as written, found, identifier,
details match, support, in `evidence/`. Then the summary.

## What I could not source

End with this heading and list everything the available files and tools did not
settle: citations you could not look up, support you could not judge without the
full text, identifiers the draft did not supply. An empty list is a valid
answer; a missing section is not.
