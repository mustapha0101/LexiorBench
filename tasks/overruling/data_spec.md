## Purpose
Identifier si une phrase extraite d'une décision judiciaire canadienne (CSC, CA) renverse un précédent jurisprudentiel (Oui/Non).

## Question format
Input: phrase extraite d'un arrêt canadien.
Output: `Oui` | `Non`

**Exemple:**
> "Dans la mesure où notre décision dans Doré c. Barreau du Québec [2012] 1 RCS 395 entre en conflit avec le présent arrêt, Doré est infirmé."
> → Oui

## Positif — `Oui`
- Phrase contient des mots de revirement: "est infirmé", "n'est plus le droit", "nous revenons sur", "est remplacé par", "notre décision antérieure dans X ne fait plus droit"
- Phrase signale explicitement que la Cour s'écarte d'un précédent antérieur

## Négatif — `Non`
- Phrase distingue un précédent sans le renverser ("dans X, les faits étaient différents")
- Phrase applique un précédent à de nouveaux faits
- Phrase critique un précédent sans officiellement le renverser
- Phrase discute de l'évolution du droit sans déclarer de revirement

## Sources légales
- Décisions CSC: Vavilov (renversant Dunsmuir), Jordan (renversant Morin), Henry (renversant Evans)
- Décisions CA-QC disponibles sur CanLII (section Cour d'appel du Québec)
- Arrêts importants avec revirement explicite

## Diversité
- Inclure des revirements en droit criminel, droit administratif, droit civil
- Inclure des formulations variées du revirement (pas toujours "est infirmé")
- Inclure des Non trompeurs: phrases contenant le nom d'un arrêt précédent mais sans revirement
- Équilibre Oui/Non: ~50/50 avec les Non soigneusement construits

## Ne pas utiliser
- Décisions SCOTUS
- Données de a2aj/canadian-laws