## Purpose
Déterminer si une personne dispose d'un droit d'action privé (recours civil) en vertu d'une loi canadienne ou québécoise particulière.

## Question format
Input: scénario décrivant une situation légale + loi potentiellement applicable.
Output: `Oui` | `Non`

**Exemple:**
> "Toute personne qui a subi des pertes par suite d'un comportement contraire à la présente partie peut, devant tout tribunal compétent, réclamer le recouvrement de ses pertes."
> → Oui

## Positif — `Oui`
- La loi crée explicitement un droit d'action pour les particuliers (recours civil)
- La loi prévoit une indemnisation privée (LPC art. 271, Loi sur la concurrence art. 36)
- Le demandeur fait partie de la classe visée par la disposition

## Positif — `Non`
- La loi prévoit uniquement des sanctions pénales ou administratives (pas de recours civil)
- La loi confère le droit d'action uniquement à un organisme public (pas aux particuliers)
- Le demandeur ne fait pas partie de la classe visée

## Sources légales
- Loi sur la protection du consommateur (RLRQ c P-40.1) art. 271-272
- Loi sur la concurrence (LRC 1985 c C-34) art. 36
- Loi sur les valeurs mobilières (RLRQ c V-1.1) — recours civil
- Loi sur la protection des renseignements personnels dans le secteur privé (Loi 25) — droit de recours

## Diversité
- Varier les lois: LPC, Loi sur la concurrence, lois environnementales, Loi 25, lois sur l'emploi
- Inclure: recours collectifs (art. 575 C.p.c.) vs recours individuels
- Inclure des Non: lois purement réglementaires sans volet civil
- Inclure des cas limites: lois ambiguës sur l'existence d'un recours privé

## Ne pas utiliser
- US private rights of action under Section 1983 or Bivens
- Données de a2aj/canadian-laws