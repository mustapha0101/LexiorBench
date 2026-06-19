## Purpose
Recall the content of the Code civil du Québec — determine if a stated rule is Vrai or Faux.

## Question format
Input: declarative statement about a CCQ rule (obligations, prescription, capacity, property, successions).
Output: `Vrai` | `Faux`

**Example:**
> "Au Québec, la prescription extinctive de droit commun est de dix ans."
> → Faux (correct answer is 3 years, art. 2925 CCQ)

## Positive — `Vrai`
- Statement accurately states a current CCQ rule
- Paraphrase is acceptable if substantively correct

## Positive — `Faux`
- Wrong number (prescriptions, delays, percentages)
- Describes an abrogated rule (C.c.B.-C. → CCQ 1994)
- Confuses CCQ with federal law or common law rule
- States an exception as if it were the general rule

## Legal sources
- CCQ (all 5 books): Personnes, Famille, Successions, Biens, Obligations, Priorités et hypothèques, Preuve, Prescription, DIP, Droit international privé
- Annotated CCQ (Wilson & Lafleur, or Barreau du Québec collection)
- lexior-ccq MCP for article text

## Diversity guidelines
- Cover all 5 books proportionally
- Prioritize: obligations (art. 1371-1707), prescription (art. 2875-2933), biens (art. 899-1008), successions (art. 613-898)
- Include subtle errors: off-by-one on delay periods, confused article numbers
- Include rules changed since 1994 (old C.c.B.-C. vs current CCQ)

## Do not use
- Rules from the Code de procédure civile (separate code)
- Federal legislation
- Rules that vary by regulation (use the statutory text only)