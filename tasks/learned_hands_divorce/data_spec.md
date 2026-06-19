## Purpose
Identifier si ce scénario soulève une question de droit du divorce ou de séparation (Loi sur le divorce, CCQ).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Je suis marié depuis 8 ans et je veux divorcer. Mon conjoint refuse de signer. Peut-on forcer un divorce au Canada?"
> → Oui

## Positif — `Oui`
- Divorce (Loi sur le divorce, LRC 1985 c 3 (2e suppl.))
- Séparation de corps (CCQ art. 493-515)
- Partage du patrimoine familial lors de la rupture (CCQ art. 414-430)
- Prestation compensatoire entre ex-époux (CCQ art. 427-430)
- Pension alimentaire entre ex-époux (Loi sur le divorce art. 15.2)

## Négatif — `Non`
- Garde d'enfants ou pension alimentaire pour enfants (domaine séparé — learned_hands_family)
- Union de fait sans régime d'union civile (pas de divorce possible)
- Litige successoral entre ex-conjoints

## Sources légales
- Loi sur le divorce (LRC 1985 c 3 (2e suppl.))
- CCQ art. 493-515 (séparation de corps)
- CCQ art. 414-430 (patrimoine familial)
- Décisions CanLII: Cour supérieure QC (chambre de la famille)

## Diversité
- Inclure: motif unique (échec du mariage ≥ 1 an), faute (adultère, cruauté)
- Inclure: divorce par consentement mutuel vs divorce contesté
- Inclure: partage de la maison familiale, du REER, du RRQ
- Inclure des unions de fait (Oui si union civile, Non si pure union de fait)

## Ne pas utiliser
- Divorce laws from US states
- Données de a2aj/canadian-laws