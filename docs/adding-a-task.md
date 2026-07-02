# Adding a task

*[Version française : [adding-a-task.fr.md](adding-a-task.fr.md)]*

1. **Create the folder** `tasks/<name>/` — lowercase with underscores, using a
   descriptive task name such as `territorial_jurisdiction`.

2. **Write `task.yaml`** (see [task-format.md](task-format.md)). `name` must
   equal the folder name; pick one v2 `reasoning_type`, `answer_type`, and
   `jurisdiction`; list exact `labels` when useful for classification tasks.

3. **Write `base_prompt.txt`** in French with `{{examples}}` and `{{text}}`.
   End with an instruction to answer with exactly one label (this keeps the
   unparsed rate near zero) followed by `Situation : {{text}}` and
   `Réponse :`.

4. **Write `sample.tsv`** — header `index	text	answer	source_model`, UTF-8,
   tabs, no tabs/newlines inside cells. These rows explain the task during
   review. Add empty `train.tsv` and `test.tsv` placeholders with header
   `index	text	answer`; fill them only after the task is validated. Content
   rules: original French text; cite only public legal sources; any judgment
   excerpts must be fictional; no copyrighted doctrine.

5. **Write the task `README.md`**: description, sources, label set, the
   draft-pending-validation warning and the CC BY 4.0 note (copy one from an
   existing task).

6. **Validate**: `uv run lexior-bench list-tasks` (the loader runs the full
   validation) and `uv run pytest` (the suite loads every real task).

7. **After validated `test.tsv` rows exist, smoke-test**:
   `uv run lexior-bench run --model ollama:lexiorgpt --tasks <name> --limit 2`,
   then read `results/<run_id>/transcript.md` to sanity-check the rendered
   prompt.

8. **Get it validated**: `uv run lexior-bench annotate push --tasks <name>`,
   have a jurist review every item, then `annotate pull` and commit the diff.

## Importing a LegalBench task

Tasks from [LegalBench](https://github.com/HazyResearch/legalbench) (or any
fork keeping its structure) can be imported instead of written by hand —
either from the web UI (Tasks → Import) or the CLI:

```sh
uv run lexior-bench import-task https://github.com/HazyResearch/legalbench/tree/main/tasks/canada_tax_court_outcomes
```

The importer converts their quoted multi-line TSVs to our strict format,
suggests the reasoning type from the README, fetches the full evaluation
split from Hugging Face when the repo only ships the few-shot demos, and
writes the **original source and license** into the imported task's README
and task.yaml. Watch the license: many LegalBench tasks are CC BY-NC
(non-commercial) — different from this repo's CC BY 4.0 — so check before
redistributing an imported task.
