# Task format

*[Version française : [task-format.fr.md](task-format.fr.md)]*

A task is a directory under `tasks/` containing v2 task metadata, prompt/spec
files, explanatory samples, and optional benchmark splits. The registry is
data-driven: every directory with a `task.yaml` is a task
(`lexior-bench list-tasks` shows them all).

```
tasks/territorial_jurisdiction/
├── task.yaml          # v2 metadata, validated at load time
├── base_prompt.txt    # prompt template
├── data_spec.md       # generation and validation specification
├── sample.tsv         # explanatory examples for review
├── train.tsv          # empty placeholder until validation
└── test.tsv           # empty placeholder until validation
```

## task.yaml

```yaml
name: territorial_jurisdiction     # must match the folder name
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
  Do Quebec authorities have personal jurisdiction over this defendant?
law_as_of: "2026-01-01"
legal_sources:
  - Code civil du Québec art. 3148
```

## TSV files

`sample.tsv`, `train.tsv`, and `test.tsv` use UTF-8, tab-separated, LF line
endings, no quoting. `sample.tsv` documents the task before promotion to final
benchmark splits. `train.tsv` and `test.tsv` may contain only the header until
the task is validated.

Headers:

- `sample.tsv`: `index	text	answer	source_model`
- `train.tsv` and `test.tsv`: `index	text	answer`

Validation enforced at load time:

- `index` values are unique within a split;
- cells must not contain tabs or newlines;
- no empty cells in non-empty rows;
- classification labels are inferred from `labels` when present, otherwise
  from `sample.tsv` answers.

## base_prompt.txt

Two placeholders:

- `{{text}}` (required except for cross-task metrics) — replaced by the item text;
- `{{examples}}` (optional) — replaced by few-shot blocks rendered from
  `train.tsv` as `Situation : <text>\nRéponse : <answer>`, separated by blank
  lines. Prompts without `{{examples}}` (pure LegalBench style) pass through
  unchanged.

## Metrics

- `exact_match` — share of items whose extracted label equals the reference.
- `balanced_accuracy` — mean per-class recall (recommended for unbalanced
  label sets; equals accuracy when classes are balanced).
- `manual` — no automatic score; items appear in `transcript.md` for human
  grading.
- `llm_judge` — deferred human/model-judge scoring for generation-heavy tasks.
- `parity_analysis` — cross-task metric, currently not scored automatically.

Label extraction (`evaluation.py`) normalizes accents/case/punctuation, then
tries an exact match on the first response line, then a word-boundary
substring search (earliest occurrence wins). Unmatched responses count as
wrong and are reported as the unparsed rate.
