# Annotation workflow (jurist-in-the-loop)

*[Version française : [annotation-workflow.fr.md](annotation-workflow.fr.md)]*

Gold answers in the seed tasks are **drafts** until a jurist validates them.
The loop: push draft items to an annotation tool → jurists validate/correct in
the web UI → pull validated answers back into the TSVs → review with
`git diff` → commit.

The TSVs remain the **single source of truth**; the annotation tools are
interchangeable adapters. Two providers ship in v1 — **Argilla** and **Label
Studio** — with the same annotation schema, so you can evaluate both on the
same data and keep the one your jurists prefer. Select with `--provider` or
the `LEXIOR_ANNOTATION_PROVIDER` env var (default: `argilla`).

## Annotation schema (identical in both tools)

Per item, annotators see the text and the proposed (draft) answer, and fill:

| Question | Values | Meaning |
|---|---|---|
| `answer_ok` | Correcte / Incorrecte | Is the proposed answer right? |
| `corrected_answer` | free text | The right answer if Incorrecte — must be one of the task's labels, verbatim |
| `item_status` | Validé / À réviser / Rejeté | Validé = final; À réviser = unsure, discuss; Rejeté = remove the item |

## Pull rules

- Only **Validé** items are applied. Final answer = `corrected_answer` when
  `answer_ok == Incorrecte` and a correction is given, otherwise the original.
- **Rejeté** items are dropped from the TSV.
- Unannotated and **À réviser** rows keep their current TSV values — partial
  annotation never loses items.
- Corrections that are not in the task's labels are warned about and skipped.
- First validated response wins; multi-annotator aggregation is out of scope
  for v1.
- TSVs are rewritten in place; **git is the history**. Always run `--dry-run`
  first, and review with `git diff tasks/` after a real pull.

Items carry the external id `{task}-{split}-{index}`, so re-pushing updates
records instead of duplicating them (safe after editing TSVs).

## Argilla (default)

```sh
docker compose -f docker/argilla/docker-compose.yml up -d
# UI: http://localhost:6900 — login argilla / 12345678
uv run lexior-bench annotate push --provider argilla --tasks all
# ... annotate in the UI (datasets lexior-bench-<task> in workspace lexior-bench) ...
uv run lexior-bench annotate pull --provider argilla --tasks all --dry-run
uv run lexior-bench annotate pull --provider argilla --tasks all
git diff tasks/
```

Env vars: `ARGILLA_API_URL` (default `http://localhost:6900`),
`ARGILLA_API_KEY` (default `argilla.apikey`).

### Argilla on Hugging Face Spaces (production path)

For a hosted setup jurists can reach without your machine: deploy the official
[Argilla Space template](https://huggingface.co/new-space?template=argilla/argilla-template-space),
then point the CLI at it — no code change:

```powershell
$env:ARGILLA_API_URL = "https://<owner>-<space>.hf.space"
$env:ARGILLA_API_KEY = "<the API key configured in the Space>"
uv run lexior-bench annotate push --tasks all
```

## Label Studio

```sh
docker compose -f docker/labelstudio/docker-compose.yml up -d
# UI: http://localhost:8080 — create an account on first visit, then copy your
# access token from "Account & Settings".
$env:LABEL_STUDIO_API_KEY = "<your token>"      # PowerShell
uv run lexior-bench annotate push --provider labelstudio --tasks all
# ... annotate in the UI (projects lexior-bench-<task>) ...
uv run lexior-bench annotate pull --provider labelstudio --tasks all --dry-run
uv run lexior-bench annotate pull --provider labelstudio --tasks all
git diff tasks/
```

Env vars: `LABEL_STUDIO_URL` (default `http://localhost:8080`),
`LABEL_STUDIO_API_KEY` (required).

## Comparing the two

Push the same tasks to both stacks and have jurists try each UI. Things to
weigh, from setting both up on this project:

- **Setup**: Label Studio is one container; Argilla needs four (server,
  worker, Elasticsearch ~1 GB heap, Redis).
- **Auth**: Argilla ships a predictable default user/API key (good for local
  loops); Label Studio requires creating an account and copying a token.
- **Review ergonomics**: Argilla has first-class suggestions (the draft answer
  is pre-selected for the annotator), record status filters and progress
  tracking per dataset; Label Studio has a more general-purpose labeling UI,
  fine-grained interface layout control (XML), and broad export options.
- **Hosting**: Argilla has an official free HF Spaces template (see above);
  Label Studio is typically self-hosted.
