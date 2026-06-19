## Purpose
Génerer une analyse IRAC complète (Issue, Règle, Application, Conclusion) à partir d'un extrait d'une décision CanLII.

## Question format
Input: extrait de décision judiciaire canadienne (500-2000 mots).
Output: analyse IRAC structurée en 4 parties (génération libre).

**Exemple de question:**
> Décision: [extrait d'un arrêt de la Cour d'appel du Québec sur la responsabilité médicale]
> Rédigez une analyse IRAC complète couvrant: Issue (question juridique centrale), Règle (article de loi ou principe applicable avec citation), Application (raisonnement pas à pas), Conclusion (résultat et dispositif).

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- **Issue (25%)**: question juridique bien identifiée, précise, centrée sur le litige réel
- **Règle (25%)**: article de loi ou principe correctement cité (CCQ, Charte, loi fédérale), source précise
- **Application (35%)**: raisonnement étape par étape, faits liés à la règle, anticipation des arguments opposés
- **Conclusion (15%)**: résultat cohérent avec le raisonnement, dispositif correct

## Sources pour les décisions d'entrée
- Décisions CanLII: CSC, CA-QC, Cour du Québec, Cour supérieure QC
- Domaines: responsabilité civile (CCQ 1457), bail résidentiel, droit du travail, droit administratif
- NE PAS utiliser les 60 décisions de la Phase 3 de l'entraînement LexiorGPT
- NE PAS utiliser les données de a2aj/canadian-laws

## Diversité
- Varier les domaines: civil, pénal, administratif, famille, travail
- Varier la complexité: décisions de 1 page vs 15 pages
- Inclure des décisions en français et en anglais (bilingue)
- Inclure des décisions avec dissidence (le modèle doit choisir le raisonnement majoritaire)

## Format de sortie attendu
```
**Issue:** [question juridique]
**Règle:** [article/principe + citation précise]
**Application:** [raisonnement structuré, 3-5 paragraphes]
**Conclusion:** [résultat + dispositif]
```

## Do not use
- Décisions américaines
- Décisions des 60 arrêts Phase 3 LexiorGPT