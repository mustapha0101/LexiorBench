# Lexior Bench

*[English version: [README.md](README.md)]*

**Lexior Bench** est un banc d'essai d'évaluation de modèles de langage (LLM)
pour le **droit québécois** — tradition civiliste, langue française — inspiré
de [LegalBench](https://github.com/HazyResearch/legalbench). Il fournit un
cadre de tâches, six tâches initiales couvrant les six types de raisonnement
juridique (repérage de questions, rappel de règles, application de règles,
conclusion, interprétation, compréhension rhétorique), des dorsaux de modèles
interchangeables et un **flux d'annotation avec juriste dans la boucle**
(Argilla ou Label Studio) pour valider les réponses de référence.

- Code : licence MIT. Données des tâches (`tasks/`) : CC BY 4.0.
- Code en anglais; contenu des tâches et rapports en français.

## Installation

Nécessite Python 3.10–3.12 et [uv](https://docs.astral.sh/uv/).

```sh
uv sync --extra openai --extra anthropic --extra dev   # noyau + dorsaux API + tests
uv sync --extra hf                                     # optionnel : dorsal transformers local (torch volumineux)
```

## Démarrage rapide

```sh
# Lister les tâches du banc d'essai
uv run lexior-bench list-tasks

# Évaluer votre modèle Ollama sur tout (évaluation + rapport inclus)
uv run lexior-bench run --model ollama:lexiorgpt --tasks all

# Comparer à un modèle de référence; test rapide avec 2 éléments par tâche
uv run lexior-bench run --model ollama:lexiorgpt --model ollama:mistral:7b-instruct-q4_K_M --tasks all --limit 2

# Autres dorsaux (clés via OPENAI_API_KEY / ANTHROPIC_API_KEY / HF_TOKEN)
uv run lexior-bench run --model openai:gpt-4o-mini --tasks type:rule-recall
uv run lexior-bench run --model anthropic:claude-opus-4-8 --tasks civil_rule_recall_ccq
uv run lexior-bench run --model hf:intelliwork/lexiorgpt-qwen25-7b-v3-merged --tasks all

# Réévaluer / régénérer le rapport d'un run existant
uv run lexior-bench evaluate --run results\20260611-173548
uv run lexior-bench report   --run results\20260611-173548
```

Chaque exécution écrit `results/<run_id>/` avec `run.json`, `results.json`,
`scores.json`, `report.md` (classement par tâche, type de raisonnement et
domaine juridique) et `transcript.md` (chaque invite/réponse avec ✓/✗).

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
