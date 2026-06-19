## Purpose
Extraire et identifier tous les valeurs numériques significatives (dates, délais, montants, pourcentages, années) dans un texte juridique canadien, avec leur signification légale.

## Question format
Input: extrait d'une décision judiciaire ou d'un article de loi.
Output: liste structurée des valeurs numériques et leur signification (extraction).

**Exemple:**
> "Le demandeur dispose de 3 ans à compter de la connaissance du préjudice pour intenter son recours (art. 2925 CCQ). L'indemnité accordée est de 15 000$ dont 5 000$ pour préjudice moral. La décision est rendue le 12 mars 2023."
> → Délai de prescription: 3 ans (art. 2925 CCQ) | Indemnité totale: 15 000$ | Dont préjudice moral: 5 000$ | Date du jugement: 12 mars 2023

## Types de valeurs à extraire
- **Délais**: prescription, préavis, délai de dénonciation, délai d'appel
- **Montants**: dommages-intérêts, amendes, seuils de compétence (100 000$ Cour du Québec)
- **Dates**: date du jugement, date des faits, date de la demande
- **Pourcentages**: taux d'intérêt, taux de réduction, quote-part
- **Durées**: durée d'un contrat, durée d'une garantie, durée d'une peine

## Sources
- Articles du CCQ contenant des valeurs précises: art. 1604 (réduction de 50% faute de la victime), art. 2925 (3 ans), art. 1623 (pénalité contractuelle)
- Décisions de petites créances QC (montants précis, dates importantes)
- Seuils légaux: aide juridique, compétence des tribunaux, franchise d'assurance
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier: extraits courts (1-2 valeurs) vs extraits complexes (8+ valeurs)
- Inclure des valeurs imbriquées (ex: "3 ans moins 1 jour" = calcul requis)
- Inclure des valeurs dont la signification légale est non-évidente
- Varier les domaines: bail (délais TAL), travail (seuils LNT), succession (calculs de parts)

## Format de sortie attendu
Liste structurée: [Type de valeur]: [valeur] — [signification légale + source si applicable]

## Do not use
- Textes juridiques américains (dollars US, federal thresholds)
- Données de a2aj/canadian-laws