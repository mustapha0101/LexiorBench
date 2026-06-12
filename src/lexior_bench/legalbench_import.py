"""Import tasks from a LegalBench-style GitHub repository.

LegalBench task folders contain base_prompt.txt, README.md and train.tsv
(few-shot demos); the evaluation split usually lives on Hugging Face
(nguha/legalbench) and is fetched through the public datasets-server API.
Differences bridged here:

- their TSVs are csv-quoted with real newlines inside cells → parsed with the
  csv module and whitespace-normalized to fit our strict single-line format;
- there is no task.yaml → metadata is suggested from the README prose and
  confirmed by the user at import time;
- the original license/attribution (often CC BY-NC) is preserved in the
  imported task's README instead of the repo's default CC BY notice.
"""

from __future__ import annotations

import csv
import io
import re
from dataclasses import dataclass, field

import httpx

from .tasks import Example, TaskError

GITHUB_TREE_RE = re.compile(
    r"^https?://github\.com/([^/]+)/([^/]+)/(?:tree|blob)/([^/]+)/(.+?)/?$"
)
HF_ROWS_URL = "https://datasets-server.huggingface.co/rows"
HF_DATASET = "nguha/legalbench"

# LegalBench reasoning-type names → ours
REASONING_TYPE_MAP = {
    "issue-spotting": "issue-spotting",
    "rule-recall": "rule-recall",
    "rule-application": "rule-application",
    "rule-conclusion": "rule-conclusion",
    "interpretation": "interpretation",
    "rhetorical-analysis": "rhetorical-understanding",
    "rhetorical-understanding": "rhetorical-understanding",
}

README_TEMPLATE = """# {name}

**Type de raisonnement :** {reasoning_type} · **Domaine :** {legal_domain} · **Langue :** {language}

{description}

**Étiquettes :** {labels}

## Provenance

Tâche importée d'un dépôt de type LegalBench : <{url}>

- **Source originale :** {source}
- **Licence originale :** {license}

> ⚠️ Cette tâche importée conserve la licence d'origine indiquée ci-dessus,
> qui peut différer de la licence CC BY 4.0 applicable aux autres données du
> dépôt (notamment les licences non commerciales). Vérifiez-la avant toute
> redistribution.
"""


@dataclass
class ImportDraft:
    name: str
    url: str
    base_prompt: str
    description: str
    source: str
    license: str
    suggested_reasoning_type: str | None
    labels: list[str]
    train: list[Example]
    test: list[Example]
    test_from_hf: bool = False
    task_type: str = ""
    warnings: list[str] = field(default_factory=list)


def _get(url: str) -> httpx.Response:
    """GET with a small backoff retry for rate limits and transient errors."""
    import time

    for attempt in range(4):
        response = httpx.get(url, timeout=30.0, follow_redirects=True)
        if response.status_code in (429, 502, 503) and attempt < 3:
            time.sleep(2 * (attempt + 1))
            continue
        return response
    return response


def sanitize_name(name: str) -> str:
    """Map a LegalBench folder name onto our task-name charset."""
    sanitized = re.sub(r"[^a-z0-9_]+", "_", name.lower()).strip("_")
    return re.sub(r"_+", "_", sanitized)


def list_task_folders(url: str) -> list[tuple[str, str]]:
    """List (folder_name, folder_url) under a GitHub tasks/ tree URL."""
    match = GITHUB_TREE_RE.match(url.strip())
    if not match:
        raise TaskError(
            f"unsupported URL {url!r} (expected https://github.com/<owner>/<repo>/tree/<branch>/<path>)"
        )
    owner, repo, branch, path = match.groups()
    response = _get(f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}")
    response.raise_for_status()
    return [
        (entry["name"], f"https://github.com/{owner}/{repo}/tree/{branch}/{path}/{entry['name']}")
        for entry in response.json()
        if entry.get("type") == "dir"
    ]


def _fetch_text(url: str) -> str | None:
    response = _get(url)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.text


def normalize_cell(text: str) -> str:
    """Collapse internal whitespace/newlines so cells fit our strict TSV format."""
    return " ".join(text.split())


def parse_legalbench_tsv(content: str) -> list[Example]:
    """Parse a LegalBench TSV (csv-quoted, possibly multi-line cells)."""
    reader = csv.DictReader(io.StringIO(content), delimiter="\t")
    if reader.fieldnames is None or not {"text", "answer"} <= set(reader.fieldnames):
        raise TaskError(f"TSV must have 'text' and 'answer' columns, got {reader.fieldnames}")
    examples = []
    for position, row in enumerate(reader):
        text = normalize_cell(row.get("text") or "")
        answer = normalize_cell(row.get("answer") or "")
        if not text or not answer:
            continue
        index = normalize_cell(row.get("index") or "") or str(position)
        examples.append(Example(index=index, text=text, answer=answer))
    return examples


def parse_readme(readme: str) -> dict:
    """Pull description, source, license and reasoning type out of README prose."""

    def grab(label: str) -> str:
        match = re.search(rf"\*\*{label}\*\*\s*:?\s*(.+)", readme)
        return match.group(1).strip() if match else ""

    description = ""
    heading = re.search(r"^###\s+(.+)$", readme, re.MULTILINE)
    if heading:
        description = heading.group(1).strip()

    reasoning_raw = grab("Legal reasoning type").lower().strip(". ")
    return {
        "description": description,
        "source": grab("Source") or "inconnu / unknown",
        "license": grab("License") or "non précisée / unspecified",
        "reasoning_type": REASONING_TYPE_MAP.get(reasoning_raw),
        "task_type": grab("Task type"),
    }


def fetch_hf_split(task_name: str, split: str) -> list[Example]:
    """Fetch a split from the LegalBench Hugging Face dataset (paginated JSON)."""
    examples: list[Example] = []
    offset, total = 0, None
    while total is None or offset < total:
        response = _get(
            f"{HF_ROWS_URL}?dataset={HF_DATASET}&config={task_name}"
            f"&split={split}&offset={offset}&length=100"
        )
        response.raise_for_status()
        payload = response.json()
        total = payload["num_rows_total"]
        for entry in payload["rows"]:
            row = entry["row"]
            text = normalize_cell(str(row.get("text") or ""))
            answer = normalize_cell(str(row.get("answer") or ""))
            if not text or not answer:
                continue
            index = normalize_cell(str(row.get("index") or "")) or str(len(examples))
            examples.append(Example(index=index, text=text, answer=answer))
        offset += 100
    return examples


def build_draft(url: str, include_hf: bool = True) -> ImportDraft:
    """Fetch and assemble everything needed to review/import one task."""
    match = GITHUB_TREE_RE.match(url.strip())
    if not match:
        raise TaskError(
            f"unsupported URL {url!r} (expected https://github.com/<owner>/<repo>/tree/<branch>/<path-to-task>)"
        )
    owner, repo, branch, path = match.groups()
    name = path.rstrip("/").rsplit("/", 1)[-1]
    raw_base = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"

    base_prompt = _fetch_text(f"{raw_base}/base_prompt.txt")
    if base_prompt is None:
        raise TaskError(f"{url}: base_prompt.txt not found — not a LegalBench task folder?")
    if "{{text}}" not in base_prompt:
        raise TaskError(f"{name}: base_prompt.txt has no {{{{text}}}} placeholder")

    readme_meta = parse_readme(_fetch_text(f"{raw_base}/README.md") or "")

    warnings: list[str] = []
    train_tsv = _fetch_text(f"{raw_base}/train.tsv")
    train = parse_legalbench_tsv(train_tsv) if train_tsv else []

    test_tsv = _fetch_text(f"{raw_base}/test.tsv")
    test = parse_legalbench_tsv(test_tsv) if test_tsv else []
    test_from_hf = False
    if not test and include_hf:
        try:
            test = fetch_hf_split(name, "test")
            test_from_hf = bool(test)
        except Exception as e:
            warnings.append(f"Hugging Face test split unavailable: {e}")
    if not test:
        raise TaskError(
            f"{name}: no evaluation data (no test.tsv in the repo and the "
            "Hugging Face split could not be fetched)"
        )
    if not train:
        # our format requires a non-empty train split: borrow a few eval items
        train, test = test[:4], test[4:]
        warnings.append(
            "no train.tsv found — moved the first 4 evaluation items to the "
            "train split (review them after import)"
        )
        if not test:
            raise TaskError(f"{name}: not enough data to form train and test splits")

    labels = sorted({ex.answer for ex in train} | {ex.answer for ex in test})
    return ImportDraft(
        name=name,
        url=url.strip(),
        base_prompt=base_prompt,
        description=readme_meta["description"] or name,
        source=readme_meta["source"],
        license=readme_meta["license"],
        suggested_reasoning_type=readme_meta["reasoning_type"],
        labels=labels,
        train=train,
        test=test,
        test_from_hf=test_from_hf,
        task_type=readme_meta["task_type"],
        warnings=warnings,
    )


def classification_blocker(draft: ImportDraft) -> str | None:
    """Reason this draft can't be imported as a v1 classification task, or None."""
    task_type = draft.task_type.lower()
    if task_type and "classification" not in task_type:
        return f"not a classification task ({draft.task_type})"
    if len(draft.labels) > 25:
        return f"{len(draft.labels)} distinct answers — looks open-ended, not classification"
    if draft.suggested_reasoning_type is None:
        return "reasoning type not detected (import individually with --reasoning-type)"
    return None


def imported_readme(
    draft: ImportDraft, *, reasoning_type: str, legal_domain: str, language: str
) -> str:
    return README_TEMPLATE.format(
        name=draft.name,
        reasoning_type=reasoning_type,
        legal_domain=legal_domain,
        language=language,
        description=draft.description,
        labels=" / ".join(draft.labels),
        url=draft.url,
        source=draft.source,
        license=draft.license,
    )
