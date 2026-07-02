## Purpose
Vérifier si un énoncé portant sur le Code civil du Québec est vrai ou faux.

## Question format
**Input:** Un énoncé affirmatif sur une règle du CCQ (formation du contrat, responsabilité civile,
prescription, vices cachés, capacité, etc.) — entre 20 et 60 mots.
**Output:** `Vrai` | `Faux`

## Label criteria

### Vrai
- L'énoncé reflète fidèlement le texte ou l'effet juridique d'un article du CCQ
- L'énoncé paraphrase correctement un article sans en trahir le sens ni inverser une condition

### Faux
- L'énoncé contient un délai ou seuil erroné (ex : 5 ans au lieu de 3 ans)
- L'énoncé attribue à une règle un effet opposé à celui du CCQ (ex : inverse qui supporte le fardeau)
- L'énoncé confond deux régimes juridiques (ex : contractuel vs extracontractuel)
- L'énoncé applique une règle de common law inexistante au Québec
- L'énoncé omet une condition essentielle qui renverse la portée de la règle

## Legal sources (verified via lexior-ccq MCP — 2026-06-19)
- **Art. 1385 CCQ** — formation du contrat par échange de consentement; condition de forme
- **Art. 1386–1392 CCQ** — offre et acceptation; caducité de l'offre
- **Art. 1457 CCQ** — responsabilité civile extracontractuelle (faute, préjudice, lien causal)
- **Art. 1458 CCQ** — responsabilité contractuelle; interdiction de cumul des régimes
- **Art. 1470 CCQ** — exonération par cause étrangère / force majeure
- **Art. 1726 CCQ** — garantie contre les vices cachés; exclusion des vices apparents
- **Art. 1728–1729 CCQ** — connaissance du vice par le vendeur; présomption (vendeur professionnel)
- **Art. 2921–2922 CCQ** — définition de la prescription extinctive; délai de droit commun 10 ans
- **Art. 2925 CCQ** — prescription de 3 ans pour droits personnels et réels mobiliers
- **Art. 2926 CCQ** — préjudice graduel: délai à partir de la première manifestation
- **Art. 2929 CCQ** — prescription de 1 an pour l'action en diffamation

## Diversity requirements
- **Vary CCQ domains** (minimum 3 different books/titles represented per 10 examples):
  obligations/contrats (arts. 1385+), responsabilité (1457+), vices cachés (1726+),
  prescription (2921+), preuve/modes de preuve
- **Vary error type for Faux** (4 categories, at least one each per 10 examples):
  wrong delay/threshold, reversed obligation direction, regime confusion, concept absent from CCQ
- **Vary difficulty**:
  40% straightforward (paraphrase of a single article),
  40% nuanced (reformulation that requires knowing a nuance or exception),
  20% edge case (combining 2 articles or knowing an exception to the exception)
- **Label balance**: strictly 50% Vrai / 50% Faux — never deviate by more than 1

## Do not use
- Common law concepts (consideration, promissory estoppel, statute of limitations)
- Federal statutes (this task is Quebec/CCQ only)
- Verbatim copy of CCQ article text without any reformulation (too trivially easy)
- Data from a2aj/canadian-laws training set (data leakage risk)
- Scenarios that require factual context beyond the legal rule itself
