## Purpose
Comparer deux clauses portant sur le même sujet et identifier laquelle est la plus avantageuse pour une partie désignée, avec justification selon le droit québécois ou canadien.

## Question format
Input: deux clauses sur le même sujet + indication de la partie (acheteur, vendeur, locataire, employé, etc.).
Output: identification de la clause la plus avantageuse + justification (génération libre).

**Exemple:**
> Clause A: "Le vendeur garantit le bien contre tout vice caché pendant 1 an à compter de la livraison."
> Clause B: "Le vendeur exclut toute garantie légale ou conventionnelle sur le bien vendu."
> Quelle clause est la plus avantageuse pour l'acheteur selon le CCQ?
> → Clause A (garantie légale CCQ art. 1726 vs exclusion potentiellement nulle sous art. 1733 si dol)

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- Identification correcte de la clause plus avantageuse (25%)
- Justification ancrée dans le droit applicable (CCQ, LPC, loi fédérale) avec citation (40%)
- Anticipation des risques ou nuances (ex: validité conditionnelle de la clause B) (25%)
- Clarté et structure de la réponse (10%)

## Sources pour les paires de clauses
- Modèles de contrats québécois: baux résidentiels et commerciaux, contrats de vente, contrats de service, contrats d'emploi
- CCQ arts. 1375-1707 (obligations), 1726-1731 (vices cachés), 2089 (non-concurrence)
- Loi sur la protection du consommateur (RLRQ c P-40.1)
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier les paires: garantie vs exclusion, arbitrage vs tribunal, délai court vs long
- Varier la partie avantageuse: parfois la Clause A est meilleure, parfois la Clause B
- Inclure des cas ambigus où les deux clauses ont des avantages différents
- Varier les domaines: vente, bail, emploi, service, franchise

## Format de sortie attendu
```
La clause [A/B] est la plus avantageuse pour [la partie] car [justification avec citation légale].
[Nuance: La clause [B/A] présente toutefois l'avantage de... / Le risque est que...]
```

## Do not use
- Droit américain ou droit anglais