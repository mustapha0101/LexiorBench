## Purpose
Identifier si un scénario factuel soulève une question de responsabilité civile extracontractuelle selon l'art. 1457 CCQ.

## Question format
Input: court scénario factuel en français.
Output: `Oui` | `Non`

**Exemple:**
> "Lors d'une dispute de voisinage, Marc pousse violemment son voisin, qui chute et se fracture le poignet."
> → Oui

## Positif — `Oui`
- Scénario implique une faute (action ou omission), un préjudice (corporel, matériel, moral) et un lien de causalité
- Responsabilité du fait d'autrui (employeur, parent, gardien)
- Trouble de voisinage (art. 976 CCQ)
- Responsabilité du gardien d'une chose (art. 1465 CCQ)

## Négatif — `Non`
- Scénario de responsabilité contractuelle pure (art. 1458 CCQ) sans faute extracontractuelle distincte
- Préjudice sans faute identifiable (accident pur)
- Scénario de droit criminel sans dimension civile
- Scénario hors QC ou hors droit civil

## Sources légales
- Art. 1457, 1458, 1459, 1463, 1465, 1467, 1468, 976 CCQ
- Décisions CanLII: Cour du Québec, Cour supérieure QC, CA-QC (responsabilité civile)
- Droit québécois de l'obligation (Lluelles & Moore)

## Diversité
- Varier: dommages corporels, matériels, moraux
- Inclure: accidents de la route, chutes sur trottoir, erreurs médicales, nuisances de voisinage
- Inclure des scénarios mixtes (faute contractuelle + extracontractuelle)
- Inclure des défenses plausibles (consentement, force majeure)

## Ne pas utiliser
- Jurisprudence américaine ou common law
- Scénarios en droit pénal sans dimension civile
- Données de a2aj/canadian-laws (source d'entraînement de LexiorGPT)