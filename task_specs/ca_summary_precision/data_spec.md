## Purpose
Résumer une décision CanLII en 5-7 phrases — évalué sur la fidélité factuelle et la complétude.

## Question format
Input: décision judiciaire complète (ou extrait substantiel de 1000-3000 mots).
Output: résumé de 5-7 phrases (génération libre).

**Exemple:**
> Décision: [arrêt CanLII complet]
> Rédigez un résumé de 5 à 7 phrases couvrant: parties, contexte factuel, question juridique centrale, règle applicable, raisonnement, conclusion.

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- **Parties et contexte (15%)**: identification correcte des parties et du contexte factuel
- **Question juridique (20%)**: formulation précise de la question centrale
- **Règle (20%)**: règle applicable correctement citée (article, nom du principe)
- **Raisonnement (30%)**: synthèse fidèle du raisonnement sans déformation
- **Conclusion (15%)**: résultat correct (accueillie/rejetée/renvoyée)

## Sources pour les décisions de test
- Décisions CanLII disponibles publiquement: CSC, CA-QC, Cour fédérale, Cour du Québec
- Varier les domaines: civil, pénal, administratif, familial, travail
- Résumés de référence validés par juristes (ground truth)
- NE PAS utiliser les 60 décisions Phase 3 LexiorGPT
- NE PAS utiliser a2aj/canadian-laws

## Diversité
- Varier la longueur des décisions (1 page vs 30 pages)
- Inclure des décisions avec dissidence (résumé doit indiquer le désaccord)
- Inclure des décisions en français et en anglais
- Inclure des décisions récentes (post-2020) pour éviter données d'entraînement

## Format de sortie attendu
5-7 phrases continues (pas de liste à puces) couvrant parties → faits → question → règle → raisonnement → résultat.

## Do not use
- Résumés déjà publiés sur CanLII (risque de copie)
- Décisions de la Phase 3 d'entraînement LexiorGPT