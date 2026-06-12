# Adding a task

*[Version française : [adding-a-task.fr.md](adding-a-task.fr.md)]*

1. **Create the folder** `tasks/<name>/` — lowercase, underscores, prefixed by
   legal domain (`civil_` / `public_`), e.g. `civil_rule_recall_prescription`.

2. **Write `task.yaml`** (see [task-format.md](task-format.md)). `name` must
   equal the folder name; pick one of the six `reasoning_type` values; list
   the exact `labels` answers must use.

3. **Write `base_prompt.txt`** in French with `{{examples}}` and `{{text}}`.
   End with an instruction to answer with exactly one label (this keeps the
   unparsed rate near zero) followed by `Situation : {{text}}` and
   `Réponse :`.

4. **Write `train.tsv` (~4 rows, one per label if possible) and `test.tsv`
   (8+ rows)** — header `index	text	answer`, UTF-8, tabs, no tabs/newlines
   inside cells. Content rules: original French text; cite only public legal
   sources (statutes); any judgment excerpts must be fictional; no copyrighted
   doctrine.

5. **Write the task `README.md`**: description, sources, label set, the
   draft-pending-validation warning and the CC BY 4.0 note (copy one from an
   existing task).

6. **Validate**: `uv run lexior-bench list-tasks` (the loader runs the full
   validation) and `uv run pytest` (the suite loads every real task).

7. **Smoke-test**: `uv run lexior-bench run --model ollama:lexiorgpt --tasks
   <name> --limit 2`, then read `results/<run_id>/transcript.md` to sanity-
   check the rendered prompt.

8. **Get it validated**: `uv run lexior-bench annotate push --tasks <name>`,
   have a jurist review every item, then `annotate pull` and commit the diff.
