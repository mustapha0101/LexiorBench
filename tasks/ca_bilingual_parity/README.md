# ca_bilingual_parity

This is **not a standalone task** — it is a cross-task metric implemented at the runner level.

## What it measures
Run any existing classification task twice:
1. With the original French input
2. With an English translation of the same input

Compare `balanced_accuracy` scores across both runs. A gap > 5 percentage points flags
a bilingual parity failure for that task.

## Implementation
Planned: `src/lexiorbench/runner.py` — `--parity` flag.
No `sample.tsv` is generated for this task.
