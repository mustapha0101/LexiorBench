# Task format

*[Version française : [task-format.fr.md](task-format.fr.md)]*

A task is a directory under `tasks/` containing four files. The registry is
data-driven: every directory with a `task.yaml` is a task
(`lexior-bench list-tasks` shows them all).

```
tasks/civil_rule_application_vices_caches/
├── README.md          # description, sources, license note
├── task.yaml          # metadata (validated at load time)
├── base_prompt.txt    # prompt template
├── train.tsv          # few-shot examples
└── test.tsv           # evaluation items
```

## task.yaml

```yaml
name: civil_rule_application_vices_caches   # must match the folder name
reasoning_type: rule-application   # issue-spotting | rule-recall | rule-application |
                                   # rule-conclusion | interpretation | rhetorical-understanding
legal_domain: civil                # civil | public
language: fr
answer_type: classification       # v1: classification only
labels: ["Oui", "Non"]            # unique, non-empty
metric: balanced_accuracy          # exact_match | balanced_accuracy | manual
description: >
  Application de la garantie de qualité (art. 1726 C.c.Q.).
version: 1                         # bump when the data changes materially
```

## TSV files

LegalBench-compatible: header `index	text	answer`, UTF-8, tab-separated,
LF line endings, no quoting. Validation enforced at load time:

- every `answer` must be one of `labels`;
- `index` values are unique within a split;
- cells must not contain tabs or newlines;
- no empty cells.

## base_prompt.txt

Two placeholders:

- `{{text}}` (required) — replaced by the test item's text;
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

Label extraction (`evaluation.py`) normalizes accents/case/punctuation, then
tries an exact match on the first response line, then a word-boundary
substring search (earliest occurrence wins). Unmatched responses count as
wrong and are reported as the unparsed rate.
