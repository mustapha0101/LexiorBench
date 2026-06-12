# Ajouter une tâche

*[English version: [adding-a-task.md](adding-a-task.md)]*

1. **Créer le dossier** `tasks/<nom>/` — minuscules, traits de soulignement,
   préfixé par le domaine (`civil_` / `public_`), p. ex.
   `civil_rule_recall_prescription`.

2. **Rédiger `task.yaml`** (voir [task-format.fr.md](task-format.fr.md)).
   `name` doit égaler le nom du dossier; choisir l'un des six
   `reasoning_type`; lister les `labels` exacts que les réponses devront
   employer.

3. **Rédiger `base_prompt.txt`** en français avec `{{examples}}` et
   `{{text}}`. Terminer par une consigne de répondre par exactement une
   étiquette (cela maintient le taux « non analysé » près de zéro), suivie de
   `Situation : {{text}}` et `Réponse :`.

4. **Rédiger `train.tsv` (~4 lignes, une par étiquette si possible) et
   `test.tsv` (8 lignes et plus)** — en-tête `index	text	answer`, UTF-8,
   tabulations, pas de tabulation ni de saut de ligne dans les cellules.
   Règles de contenu : texte français original; ne citer que des sources
   législatives publiques; tout extrait de jugement doit être fictif; aucune
   doctrine protégée par le droit d'auteur.

5. **Rédiger le `README.md` de la tâche** : description, sources, jeu
   d'étiquettes, l'avertissement « ébauches en attente de validation » et la
   note CC BY 4.0 (copier celui d'une tâche existante).

6. **Valider** : `uv run lexior-bench list-tasks` (le chargeur exécute la
   validation complète) et `uv run pytest` (la suite charge chaque tâche
   réelle).

7. **Test rapide** : `uv run lexior-bench run --model ollama:lexiorgpt
   --tasks <nom> --limit 2`, puis lire `results/<run_id>/transcript.md` pour
   vérifier l'invite générée.

8. **Faire valider** : `uv run lexior-bench annotate push --tasks <nom>`,
   faire réviser chaque élément par un juriste, puis `annotate pull` et
   committer le diff.

## Importer une tâche LegalBench

Les tâches de [LegalBench](https://github.com/HazyResearch/legalbench) (ou de
tout fork conservant sa structure) peuvent être importées au lieu d'être
rédigées à la main — depuis l'interface web (Tâches → Importer) ou le CLI :

```sh
uv run lexior-bench import-task https://github.com/HazyResearch/legalbench/tree/main/tasks/canada_tax_court_outcomes
```

L'importateur convertit leurs TSV multilignes entre guillemets vers notre
format strict, suggère le type de raisonnement d'après le README, récupère le
jeu d'évaluation complet depuis Hugging Face lorsque le dépôt ne contient que
les exemples few-shot, et inscrit la **source et la licence d'origine** dans
le README et le task.yaml de la tâche importée. Attention à la licence :
plusieurs tâches LegalBench sont en CC BY-NC (non commercial) — différent du
CC BY 4.0 de ce dépôt — vérifiez avant toute redistribution.
