# Format des tâches

*[English version: [task-format.md](task-format.md)]*

Une tâche est un répertoire sous `tasks/` contenant les métadonnées v2, les
fichiers d'invite/spécification, des exemples explicatifs et des partitions
optionnelles de benchmark. Le
registre est piloté par les données : tout répertoire contenant un
`task.yaml` est une tâche (`lexior-bench list-tasks` les affiche toutes).

```
tasks/territorial_jurisdiction/
├── task.yaml          # métadonnées v2, validées au chargement
├── base_prompt.txt    # gabarit d'invite
├── data_spec.md       # spécification de génération et validation
├── sample.tsv         # exemples explicatifs pour revue
├── train.tsv          # espace réservé vide jusqu'à validation
└── test.tsv           # espace réservé vide jusqu'à validation
```

## task.yaml

```yaml
name: territorial_jurisdiction     # doit correspondre au nom du dossier
reasoning_type: rule_application   # issue_spotting | rule_recall | rule_application |
                                   # rule_conclusion | rule_application_conclusion |
                                   # interpretation | rhetorical | cross_task_metric
jurisdiction: quebec               # quebec | federal_ca | both
language: fr
answer_type: classification        # classification | generation |
                                   # classification_and_generation | cross_task_metric
answer_detail: >
  Multi-class (Compétence établie / Compétence douteuse / Absence de compétence)
metric: balanced_accuracy          # exact_match | balanced_accuracy | manual |
                                   # llm_judge | parity_analysis
sample_size: 10
purpose: >
  Les autorités québécoises ont-elles compétence sur ce défendeur?
law_as_of: "2026-01-01"
legal_sources:
  - Code civil du Québec art. 3148
```

## Fichiers TSV

`sample.tsv`, `train.tsv` et `test.tsv` utilisent UTF-8, le séparateur
tabulation, des fins de ligne LF et aucun guillemet. `sample.tsv` documente la
tâche avant sa promotion vers les partitions finales. `train.tsv` et
`test.tsv` peuvent ne contenir que l'en-tête jusqu'à validation.

En-têtes :

- `sample.tsv` : `index	text	answer	source_model`
- `train.tsv` et `test.tsv` : `index	text	answer`

Validation au chargement :

- les `index` sont uniques par partition;
- aucune cellule ne contient de tabulation ni de saut de ligne;
- aucune cellule vide dans les lignes non vides;
- les étiquettes de classification sont inférées depuis `labels` lorsque le
  champ existe, sinon depuis les réponses de `sample.tsv`.

## base_prompt.txt

Deux espaces réservés :

- `{{text}}` (requis sauf pour les métriques inter-tâches) — remplacé par le
  texte de l'élément;
- `{{examples}}` (optionnel) — remplacé par les blocs few-shot générés depuis
  `train.tsv` au format `Situation : <texte>\nRéponse : <réponse>`, séparés
  par des lignes vides. Les invites sans `{{examples}}` (style LegalBench pur)
  passent telles quelles.

## Métriques

- `exact_match` — proportion d'éléments dont l'étiquette extraite égale la
  référence.
- `balanced_accuracy` — moyenne des rappels par classe (recommandée pour les
  jeux d'étiquettes déséquilibrés; égale l'exactitude quand les classes sont
  équilibrées).
- `manual` — aucun score automatique; les éléments figurent dans
  `transcript.md` pour notation humaine.
- `llm_judge` — notation différée humaine ou par juge LLM pour les tâches
  génératives.
- `parity_analysis` — métrique inter-tâches, sans score automatique pour le
  moment.

L'extraction d'étiquettes (`evaluation.py`) normalise accents/casse/
ponctuation, tente d'abord une correspondance exacte sur la première ligne de
la réponse, puis une recherche de sous-chaîne avec frontières de mots (la
première occurrence l'emporte). Les réponses non analysables comptent comme
erronées et sont rapportées comme taux « non analysé ».
