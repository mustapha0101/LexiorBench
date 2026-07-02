# Lexior Bench

*[English version: [README.md](README.md)]*

**Lexior Bench** est un banc d'essai d'évaluation de modèles de langage (LLM)
pour le **droit québécois et canadien** en français, inspiré de
[LegalBench](https://github.com/HazyResearch/legalbench). Il fournit un
cadre de tâches, un inventaire v2 couvrant la taxonomie de raisonnement
juridique (`issue_spotting`, `rule_recall`, `rule_application`,
`rule_conclusion`, `rule_application_conclusion`, `interpretation`,
`rhetorical`, `cross_task_metric`), des dorsaux de modèles interchangeables et
un **flux d'annotation avec juriste dans la boucle**
(Argilla ou Label Studio) pour valider les réponses de référence.

- Code : licence MIT. Données des tâches (`tasks/`) : CC BY 4.0.
- Code en anglais; contenu des tâches et rapports en français.

## État v2 actuel

L'espace de travail actuel contient un inventaire v2 provisoire de 128 tâches
juridiques canadiennes et québécoises. Chaque dossier de tâche utilise la
taxonomie v2 :

- `reasoning_type` : `issue_spotting`, `rule_recall`, `rule_application`,
  `rule_conclusion`, `rule_application_conclusion`, `interpretation`,
  `rhetorical` ou `cross_task_metric`
- `answer_type` : `classification`, `generation`,
  `classification_and_generation` ou `cross_task_metric`
- `jurisdiction` : `quebec`, `federal_ca` ou `both`
- `metric` : `balanced_accuracy`, `llm_judge` ou `parity_analysis`

Les fichiers `sample.tsv` servent d'exemples explicatifs pour comprendre et
réviser les tâches. Ils ne constituent pas encore la partition finale du
benchmark. Des fichiers `train.tsv` et `test.tsv` vides sont présents pour y
ajouter les exemples validés plus tard. Utilisez `TASK_SAMPLE_QA.txt` pour
réviser tous les noms de tâches avec toutes les questions/réponses d'exemple
dans un seul fichier. Consultez `tasks/_generation_report.md` et
`tasks/CATALOG.md` pour l'inventaire v2, ainsi que `suggested_tasks/` pour la
couverture proposée.

L'inventaire a été nettoyé afin d'utiliser des noms canadiens/québécois. Les
noms de jeux de données étrangers ou importés ne sont pas utilisés comme noms
actifs; les tâches de confidentialité sont nommées par thème juridique.

La génération d'exemples est neutre quant au fournisseur. Utilisez
`scripts/generate_samples_structured.py` avec
`--generation-model <provider:model>` ou `LEXIOR_GENERATION_MODEL`; l'invite
partagée est `prompts/generation_system_prompt.md`.

## Installation

Nécessite Python 3.10–3.12 et [uv](https://docs.astral.sh/uv/).

```sh
uv sync --extra openai --extra anthropic --extra dev   # noyau + dorsaux API + tests
uv sync --extra hf                                     # optionnel : dorsal transformers local (torch volumineux)
```

## Démarrage rapide

```sh
# Interface web : tâches, exécutions, résultats et annotation sans commandes shell
uv run lexior-bench web            # http://127.0.0.1:8000 (FR/EN)

# Lister les tâches du banc d'essai
uv run lexior-bench list-tasks

# Après l'ajout de lignes validées dans test.tsv, évaluer votre modèle Ollama
uv run lexior-bench run --model ollama:lexiorgpt --tasks all

# Comparer à un modèle de référence; test rapide avec 2 éléments par tâche
uv run lexior-bench run --model ollama:lexiorgpt --model ollama:mistral:7b-instruct-q4_K_M --tasks all --limit 2

# Autres dorsaux (clés via OPENAI_API_KEY / ANTHROPIC_API_KEY / HF_TOKEN)
uv run lexior-bench run --model openai:gpt-4o-mini --tasks type:rule_recall
uv run lexior-bench run --model anthropic:claude-opus-4-8 --tasks civil_rule_recall_ccq
uv run lexior-bench run --model hf:intelliwork/lexiorgpt-qwen25-7b-v3-merged --tasks all

# Réévaluer / régénérer le rapport d'un run existant
uv run lexior-bench evaluate --run results\20260611-173548
uv run lexior-bench report   --run results\20260611-173548
```

Chaque exécution écrit `results/<run_id>/` avec `run.json`, `results.json`,
`scores.json`, `report.md` (classement par tâche, type de raisonnement et
territoire) et `transcript.md` (chaque invite/réponse avec ✓/✗).

## Annotation (juriste dans la boucle)

Les fichiers TSV des tâches demeurent la source de vérité; les outils
d'annotation sont des adaptateurs interchangeables (sélection par `--provider`
ou `LEXIOR_ANNOTATION_PROVIDER`).

```sh
# Argilla (interface : http://localhost:6900, argilla / 12345678)
docker compose -f docker/argilla/docker-compose.yml up -d
uv run lexior-bench annotate push --provider argilla --tasks all
# ... les juristes valident/corrigent dans l'interface web ...
uv run lexior-bench annotate pull --provider argilla --tasks all --dry-run
uv run lexior-bench annotate pull --provider argilla --tasks all
git diff tasks/   # revue des corrections appliquées

# Label Studio (interface : http://localhost:8080; définir LABEL_STUDIO_API_KEY)
docker compose -f docker/labelstudio/docker-compose.yml up -d
uv run lexior-bench annotate push --provider labelstudio --tasks all
```

Voir [docs/annotation-workflow.fr.md](docs/annotation-workflow.fr.md) pour le
flux complet, le schéma d'annotation et Argilla sur Hugging Face Spaces comme
voie de production.

## Documentation

- [docs/web-ui.fr.md](docs/web-ui.fr.md) — l'interface web locale
- [docs/task-format.fr.md](docs/task-format.fr.md) — format task.yaml, TSV et invites
- [docs/adding-a-task.fr.md](docs/adding-a-task.fr.md) — ajouter une nouvelle tâche
- [docs/annotation-workflow.fr.md](docs/annotation-workflow.fr.md) — boucle de validation par juristes

## Tests

```sh
uv run pytest
```

Les tests unitaires s'exécutent hors ligne (sans Docker, Ollama ni clés API).
Le chargement de chaque tâche réelle fait partie de la suite : toute erreur de
données fait échouer la construction.
