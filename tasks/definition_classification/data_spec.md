## Purpose
Identifier si une phrase extraite d'une décision de justice définit un terme juridique (Oui/Non).

## Question format
Input: phrase extraite d'un arrêt canadien (CSC, CA-QC, Cour fédérale).
Output: `Oui` | `Non`

**Exemple:**
> "Le terme 'résidence principale' au sens de l'art. 395 CCQ désigne le lieu où une personne a son principal établissement, déterminé par l'intention de s'y établir de façon durable."
> → Oui

## Positif — `Oui`
- Phrase contient une définition explicite d'un terme: "X désigne/signifie/s'entend de Y"
- Phrase délimite la portée d'un concept juridique par des critères positifs ou négatifs
- Phrase établit un test pour identifier quand un terme s'applique

## Négatif — `Non`
- Phrase applique une règle sans définir de terme
- Phrase cite un article de loi sans en dégager une définition
- Phrase constate des faits
- Phrase exprime un raisonnement de causalité ou de conclusion

## Sources légales
- Décisions CanLII: CSC, CA-QC, Cour fédérale (section Jurisprudence)
- Arrêts de principe définissant des termes: Doré (raisonnabilité), Vavilov (caractère raisonnable), Jordan (délai raisonnable)
- Dictionnaires juridiques canadiens pour validation

## Diversité
- Varier: droit civil, droit public, droit criminel, droit fiscal
- Inclure des définitions implicites (sans le mot "désigne" mais équivalentes)
- Inclure des phrases qui ressemblent à des définitions mais n'en sont pas (trompe-l'œil)
- Équilibre Oui/Non: ~50/50

## Ne pas utiliser
- Décisions SCOTUS ou cours américaines
- Définitions législatives (lire directement dans la loi — trop facile)
- Données de a2aj/canadian-laws