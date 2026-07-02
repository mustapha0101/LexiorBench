# Lexior Bench

*[Version française : [README.fr.md](README.fr.md)]*

**Lexior Bench** is an LLM evaluation benchmark for **Quebec and Canadian law**
in French, modeled on
[LegalBench](https://github.com/HazyResearch/legalbench). It ships a task
framework, seed tasks covering the v2 legal reasoning taxonomy
(`issue_spotting`, `rule_recall`, `rule_application`, `rule_conclusion`,
`rule_application_conclusion`, `interpretation`, `rhetorical`, and
`cross_task_metric`), pluggable model backends, and a
**jurist-in-the-loop annotation pipeline** (Argilla or Label Studio) to
validate gold answers.

- Code: MIT license. Task data (`tasks/`): CC BY 4.0.
- Code in English; task content and reports in French.

## Current V2 State

The current workspace contains a v2 draft inventory of 128 Canadian/Quebec
legal tasks. Each task folder uses the v2 metadata taxonomy:

- `reasoning_type`: `issue_spotting`, `rule_recall`, `rule_application`,
  `rule_conclusion`, `rule_application_conclusion`, `interpretation`,
  `rhetorical`, or `cross_task_metric`
- `answer_type`: `classification`, `generation`,
  `classification_and_generation`, or `cross_task_metric`
- `jurisdiction`: `quebec`, `federal_ca`, or `both`
- `metric`: `balanced_accuracy`, `llm_judge`, or `parity_analysis`

`sample.tsv` files are explanatory examples for understanding and reviewing each
task. They are not the final benchmark split. Empty `train.tsv` and `test.tsv`
placeholders are present so validated examples can be added later. Use
`TASK_SAMPLE_QA.txt` to review every task name with all sample Q&A rows in one
file. See `tasks/_generation_report.md` and `tasks/CATALOG.md` for the v2
inventory, and `suggested_tasks/` for proposed future coverage.

The task inventory has been cleaned to use Canadian/Quebec naming. Imported or
foreign dataset names are not used as active task names; the privacy tasks are
named by legal/privacy topic instead.

Sample generation is provider-neutral. Use
`scripts/generate_samples_structured.py` with
`--generation-model <provider:model>` or `LEXIOR_GENERATION_MODEL`; the shared
prompt is `prompts/generation_system_prompt.md`.

## Install

Requires Python 3.10–3.12 and [uv](https://docs.astral.sh/uv/).

```sh
uv sync --extra openai --extra anthropic --extra dev   # core + API backends + tests
uv sync --extra hf                                     # optional: local transformers backend (large torch download)
```

## Quick start

```sh
# Web interface: tasks, runs, results and annotation without shell commands
uv run lexior-bench web            # http://127.0.0.1:8000 (FR/EN)

# List the benchmark tasks
uv run lexior-bench list-tasks

# After validated test rows exist, run your Ollama model on everything
uv run lexior-bench run --model ollama:lexiorgpt --tasks all

# Compare against a baseline; smoke-test with 2 items per task
uv run lexior-bench run --model ollama:lexiorgpt --model ollama:mistral:7b-instruct-q4_K_M --tasks all --limit 2

# Other backends (API keys via OPENAI_API_KEY / ANTHROPIC_API_KEY / HF_TOKEN)
uv run lexior-bench run --model openai:gpt-4o-mini --tasks type:rule_recall
uv run lexior-bench run --model anthropic:claude-opus-4-8 --tasks civil_rule_recall_ccq
uv run lexior-bench run --model hf:intelliwork/lexiorgpt-qwen25-7b-v3-merged --tasks all

# Re-score / re-report an existing run
uv run lexior-bench evaluate --run results\20260611-173548
uv run lexior-bench report   --run results\20260611-173548
```

Each run writes `results/<run_id>/` with `run.json`, `results.json`,
`scores.json`, `report.md` (leaderboard by task, reasoning type, and
jurisdiction) and `transcript.md` (every prompt/response with ✓/✗).

## Annotation (jurist-in-the-loop)

Task TSVs are the single source of truth; annotation tools are interchangeable
push/pull adapters. Two providers are supported: **Argilla** and **Label
Studio** (select with `--provider` or `LEXIOR_ANNOTATION_PROVIDER`).

```sh
# Argilla (UI at http://localhost:6900, argilla / 12345678)
docker compose -f docker/argilla/docker-compose.yml up -d
uv run lexior-bench annotate push --provider argilla --tasks all
# ... jurists validate/correct in the web UI ...
uv run lexior-bench annotate pull --provider argilla --tasks all --dry-run
uv run lexior-bench annotate pull --provider argilla --tasks all
git diff tasks/   # review the applied corrections

# Label Studio (UI at http://localhost:8080; set LABEL_STUDIO_API_KEY)
docker compose -f docker/labelstudio/docker-compose.yml up -d
uv run lexior-bench annotate push --provider labelstudio --tasks all
```

See [docs/annotation-workflow.md](docs/annotation-workflow.md) for the full
loop, the annotation schema, and Argilla on Hugging Face Spaces as a
production path.

## Documentation

- [docs/web-ui.md](docs/web-ui.md) — the local web interface
- [docs/task-format.md](docs/task-format.md) — task.yaml, TSV and prompt format
- [docs/adding-a-task.md](docs/adding-a-task.md) — how to add a new task
- [docs/annotation-workflow.md](docs/annotation-workflow.md) — jurist validation loop

## Tests

```sh
uv run pytest
```

Unit tests run offline (no Docker, no Ollama, no API keys). Loading every real
seed task is part of the suite, so data errors fail the build.
