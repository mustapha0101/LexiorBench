## Purpose
Identifier une fausse prémisse juridique dans une question et expliquer pourquoi elle est incorrecte, en citant le droit canadien ou québécois applicable.

## Question format
Input: question contenant une fausse prémisse juridique.
Output: identification de la fausse prémisse + correction avec citation légale (classification + génération).

**Exemple:**
> "Selon l'art. 1720 CCQ, la garantie légale contre les vices cachés dure 5 ans. Mon recours est-il prescrit après 4 ans?"
> → Fausse prémisse: le délai de prescription des vices cachés n'est pas 5 ans mais 3 ans (art. 2925 CCQ). La garantie légale (art. 1726 CCQ) est distincte de la prescription (art. 2925 CCQ).

## Classes
- `Oui` (fausse prémisse présente): la question contient une erreur factuelle sur le droit
- `Non` (prémisse correcte): la question est factuellement correcte sur le droit

## Critères d'évaluation
- Identification de la prémisse erronée (25%)
- Citation correcte de l'article ou du principe qui corrige l'erreur (35%)
- Explication claire de pourquoi c'est une erreur (25%)
- Réponse à la question réelle (si elle en a une) (15%)

## Types de fausses prémisses à inclure
- Mauvais délai de prescription (art. 2925 CCQ est 3 ans, pas 5 ans)
- Référence à une loi abrogée (C.c.B.-C. → CCQ 1994)
- Confusion entre régimes juridiques (SAAQ vs responsabilité civile ordinaire)
- Mauvais tribunal compétent (Cour du Québec < 100 000$ vs Cour supérieure ≥ 100 000$)
- Droits inexistants en droit québécois (dépôt de garantie de loyer interdit CCQ 1904)

## Sources légales
- CCQ (toutes les matières)
- LPC, LNT, C.p.c., Charte québécoise
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier les domaines: bail, responsabilité civile, succession, contrat, procédure
- Inclure des erreurs subtiles (différence d'un an dans un délai)
- Inclure des erreurs grossières (loi inexistante, droit impossible)
- Inclure ~30% de `Non` (questions avec prémisse correcte)

## Do not use
- Fausses prémisses sur le droit américain ou européen
- Questions sans enjeu légal clair