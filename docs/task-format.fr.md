# Format des tâches

*[English version: [task-format.md](task-format.md)]*

Une tâche est un répertoire sous `tasks/` contenant quatre fichiers. Le
registre est piloté par les données : tout répertoire contenant un
`task.yaml` est une tâche (`lexior-bench list-tasks` les affiche toutes).

```
tasks/civil_rule_application_vices_caches/
├── README.md          # description, sources, note de licence
├── task.yaml          # métadonnées (validées au chargement)
├── base_prompt.txt    # gabarit d'invite
├── train.tsv          # exemples few-shot
└── test.tsv           # éléments d'évaluation
```

## task.yaml

```yaml
name: civil_rule_application_vices_caches   # doit correspondre au nom du dossier
reasoning_type: rule-application   # issue-spotting | rule-recall | rule-application |
                                   # rule-conclusion | interpretation | rhetorical-understanding
legal_domain: civil                # civil | public
language: fr
answer_type: classification       # v1 : classification seulement
labels: ["Oui", "Non"]            # uniques, non vides
metric: balanced_accuracy          # exact_match | balanced_accuracy | manual
description: >
  Application de la garantie de qualité (art. 1726 C.c.Q.).
version: 1                         # incrémenter lorsque les données changent
```

## Fichiers TSV

Compatibles LegalBench : en-tête `index	text	answer`, UTF-8, séparateur
tabulation, fins de ligne LF, sans guillemets. Validation au chargement :

- chaque `answer` doit appartenir à `labels`;
- les `index` sont uniques par partition;
- aucune cellule ne contient de tabulation ni de saut de ligne;
- aucune cellule vide.

## base_prompt.txt

Deux espaces réservés :

- `{{text}}` (requis) — remplacé par le texte de l'élément évalué;
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

L'extraction d'étiquettes (`evaluation.py`) normalise accents/casse/
ponctuation, tente d'abord une correspondance exacte sur la première ligne de
la réponse, puis une recherche de sous-chaîne avec frontières de mots (la
première occurrence l'emporte). Les réponses non analysables comptent comme
erronées et sont rapportées comme taux « non analysé ».
