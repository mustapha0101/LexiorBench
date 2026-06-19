## Purpose
Déterminer si les autorités québécoises ont compétence territoriale sur un défendeur dans un litige donné, selon les art. 3148 CCQ et suivants (Oui/Non + explication).

## Question format
Input: scénario décrivant un litige avec un élément d'extranéité.
Output: `Oui` (compétence des tribunaux québécois) | `Non` (pas compétents) + justification.

**Exemple:**
> "Marie (Québec) poursuit une entreprise ontarienne qui lui a vendu en ligne un produit défectueux livré à son domicile au Québec. Les tribunaux québécois ont-ils compétence?"
> → Oui — art. 3148(3) CCQ: préjudice subi au Québec

## Positif — `Oui` — critères de l'art. 3148 CCQ
- Défendeur domicilié au Québec
- Défendeur a un établissement au Québec et le litige est lié à cet établissement
- Faute commise au Québec ou préjudice subi au Québec
- Obligation née ou exécutable au Québec
- Les parties ont choisi le Québec comme for contractuel

## Positif — `Non`
- Aucun des critères de l'art. 3148 CCQ n'est rempli
- Le défendeur peut invoquer l'art. 3135 CCQ (forum non conveniens)
- Clause attributive de compétence en faveur d'un autre tribunal

## Sources légales
- CCQ art. 3148-3154 (compétence internationale des autorités du Québec)
- CCQ art. 3135 (forum non conveniens)
- CCQ art. 3148(5) (choix de for contractuel)
- Décisions CanLII: Cour supérieure QC (requêtes en déclinature de compétence)

## Diversité
- Varier: défendeurs de différentes provinces canadiennes, des États-Unis, d'Europe
- Inclure: commerce électronique, contrats de service à distance, accidents extraterritoriaux
- Inclure des cas de forum non conveniens (compétence formelle mais plus appropriée ailleurs)
- Varier la difficulté: critère évident vs critère limite

## Do not use
- US diversity jurisdiction (28 USC 1332)
- Long-arm statutes américains
- Données de a2aj/canadian-laws