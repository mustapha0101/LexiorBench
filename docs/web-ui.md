# Web interface

*[Version française : [web-ui.fr.md](web-ui.fr.md)]*

A local web UI covering the whole loop without shell commands: browse and
create tasks, launch benchmark runs with live progress, read results, and
drive the annotation push/pull.

```sh
uv run lexior-bench web            # opens http://127.0.0.1:8000
uv run lexior-bench web --port 9000 --no-browser
```

The interface is bilingual (FR default — toggle in the header). It binds to
`127.0.0.1` and has no authentication: it is a **local, single-user tool** —
don't expose it on a network. If a `.env` file exists at the repo root, the
`web` command loads it into the environment (handy for
`LABEL_STUDIO_API_KEY`); the rest of the CLI does not.

## Pages

- **Tasks** — list, inspect, create (full form with validation: name, type,
  labels, prompt template, train/test items), edit items of existing tasks
  (rewrites the TSVs — git keeps the history), delete a task.
- **Run** — pick models (installed Ollama models are detected live; other
  backends via `openai:…` / `anthropic:…` / `hf:…` lines, with API-key
  indicators), pick tasks, set limit/max_tokens, then watch the progress bar.
  One run at a time; evaluation + report are produced automatically.
- **Results** — all runs newest-first; per-run leaderboard (task / reasoning
  type / legal domain), unparsed rates, and the full transcript with ✓/✗ and
  raw responses.
- **Annotation** — per task: push to Argilla/Label Studio, preview a pull
  (dry-run change summary), apply a pull. Same semantics as the CLI
  (see [annotation-workflow.md](annotation-workflow.md)).

## Out of scope (use the CLI / files)

Multiple queued runs, remote access/auth, editing a task's labels or prompt
after creation (edit `task.yaml` / `base_prompt.txt` directly), bumping the
task `version` field, multi-annotator management.
