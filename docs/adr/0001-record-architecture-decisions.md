# 0001. Record architecture decisions

- Status: Accepted
- Date: 2026-11-15

## Context
pitchstack is a public repo where I (Balthazar Paixao) learn and practise the
data platform and data management skills needed to lead data at a football
club. Over 27 weeks I will make choices that are expensive to reverse: table
format, modelling approach, semantic layer. Two people will read the reasoning
later: me in week 27, writing the platform blueprint, and anyone reviewing the
repo to judge how I make decisions. Without a record, I would not be able to
explain in May why I chose one option over another in December.

## Options considered
1. **ADRs as Markdown files in `docs/adr/`.** Pros: versioned with the code,
   reviewed in the same PR as the change, public with the repo, easy to
   migrate to another format or platform. Cons: plain styling.
2. **A wiki or Notion page.** Pros: richer styling. Cons: lives apart from the
   code, and adds another link, account and login to maintain.
3. **No record.** Pros: nothing to write. Cons: decisions and the learning
   behind them are not tracked.

## Decision
I will record decisions as Markdown files in `docs/adr/`, one file per
decision. A decision is significant, and gets an ADR, if it is expensive to
reverse, had two or more real alternatives, or would make a reader ask "why
this?" in six months. Example that needs one: the table format and catalog
(ADR-0003). Example that does not: the ruff line length.

## Consequences
- Good: in week 27 I can write the blueprint from recorded reasoning, and each
  decision can be explained with the options that were rejected.
- Cost: about 30 minutes per ADR, 6 ADRs planned (0001–0006), so roughly
  3 hours of the 105 (estimate, about 3%).
- What would make me revisit this: two significant decisions in a row made
  without an ADR, or ADRs regularly taking more than 30 minutes.