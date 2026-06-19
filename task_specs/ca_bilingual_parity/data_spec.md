## Purpose
Métrique transversale — mesurer si le modèle répond de manière équivalente en français et en anglais sur les mêmes questions.
NOTE: ce n'est pas une tâche standalone — c'est une métrique implémentée au niveau du runner.

## Implementation
1. Sélectionner un sous-ensemble de tâches existantes (ex: learned_hands_housing, civil_rule_recall_ccq)
2. Créer des versions EN des questions déjà en FR (traduction fidèle)
3. Exécuter chaque version (FR et EN) sur le modèle
4. Calculer l'écart de balanced_accuracy entre FR et EN
5. Signaler un écart > 5 points comme "parité insuffisante"

## Format des données
Ajouter un fichier `test_en.tsv` aux tâches sélectionnées, avec les mêmes questions traduites fidèlement en anglais. Le `test.tsv` original (en FR) reste la source principale.

## Seuil
- Écart ≤ 5 points → parité acceptable
- Écart 5-10 points → avertissement
- Écart > 10 points → parité insuffisante, signaler dans le rapport benchmark

## Tâches prioritaires pour la parité
- learned_hands_* (issue-spotting bilingue)
- civil_rule_recall_ccq (règles du CCQ en FR + EN)
- supply_chain_disclosure_* (textes bilingues soumis aux entreprises)
- canadian_*_recall (lois fédérales bilingues)

## Do not use
- Traductions automatiques sans révision (risque d'introduire des biais de traduction)
- Données de a2aj/canadian-laws