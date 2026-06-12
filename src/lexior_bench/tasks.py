"""Task registry: load and validate Lexior Bench task folders.

A task is a directory under tasks/ containing task.yaml, base_prompt.txt,
train.tsv and test.tsv (LegalBench-compatible columns: index, text, answer).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

REASONING_TYPES = (
    "issue-spotting",
    "rule-recall",
    "rule-application",
    "rule-conclusion",
    "interpretation",
    "rhetorical-understanding",
)
LEGAL_DOMAINS = ("civil", "public")
ANSWER_TYPES = ("classification",)  # v1: classification only
METRICS = ("exact_match", "balanced_accuracy", "manual")
TSV_COLUMNS = ["index", "text", "answer"]


class TaskError(ValueError):
    """Raised when a task folder fails validation."""


@dataclass
class Example:
    index: str
    text: str
    answer: str


@dataclass
class Task:
    name: str
    reasoning_type: str
    legal_domain: str
    language: str
    answer_type: str
    labels: list[str]
    metric: str
    description: str
    version: int
    path: Path
    base_prompt: str
    train: list[Example]
    test: list[Example]

    def split(self, name: str) -> list[Example]:
        if name == "train":
            return self.train
        if name == "test":
            return self.test
        raise ValueError(f"unknown split {name!r}")


def read_tsv(path: Path) -> list[Example]:
    """Read a LegalBench-style TSV (unquoted, tab-separated, header row)."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise TaskError(f"{path}: file is empty")
    header = lines[0].split("\t")
    if header != TSV_COLUMNS:
        raise TaskError(f"{path}: header must be {TSV_COLUMNS}, got {header}")
    examples: list[Example] = []
    for lineno, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != 3:
            raise TaskError(
                f"{path}:{lineno}: expected 3 tab-separated cells, got {len(cells)} "
                "(stray tab or missing column?)"
            )
        index, text, answer = (cell.strip() for cell in cells)
        if not index or not text or not answer:
            raise TaskError(f"{path}:{lineno}: empty cell")
        examples.append(Example(index=index, text=text, answer=answer))
    if not examples:
        raise TaskError(f"{path}: no data rows")
    return examples


def write_tsv(path: Path, examples: list[Example]) -> None:
    """Write examples back to TSV (UTF-8, LF line endings)."""
    lines = ["\t".join(TSV_COLUMNS)]
    for ex in examples:
        for cell in (ex.index, ex.text, ex.answer):
            if "\t" in cell or "\n" in cell or "\r" in cell:
                raise TaskError(f"{path}: cell contains tab/newline: {cell!r}")
        lines.append(f"{ex.index}\t{ex.text}\t{ex.answer}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def load_task(path: Path) -> Task:
    """Load and validate one task folder."""
    path = Path(path)
    yaml_path = path / "task.yaml"
    meta = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

    name = meta.get("name", "")
    if name != path.name:
        raise TaskError(f"{yaml_path}: name {name!r} does not match folder {path.name!r}")
    if meta.get("reasoning_type") not in REASONING_TYPES:
        raise TaskError(f"{name}: reasoning_type must be one of {REASONING_TYPES}")
    if meta.get("legal_domain") not in LEGAL_DOMAINS:
        raise TaskError(f"{name}: legal_domain must be one of {LEGAL_DOMAINS}")
    if meta.get("answer_type") not in ANSWER_TYPES:
        raise TaskError(f"{name}: answer_type must be one of {ANSWER_TYPES} (v1)")
    if meta.get("metric") not in METRICS:
        raise TaskError(f"{name}: metric must be one of {METRICS}")
    labels = meta.get("labels") or []
    if not labels or len(labels) != len(set(labels)):
        raise TaskError(f"{name}: labels must be a non-empty list of unique strings")

    base_prompt = (path / "base_prompt.txt").read_text(encoding="utf-8")
    if "{{text}}" not in base_prompt:
        raise TaskError(f"{name}: base_prompt.txt must contain {{{{text}}}}")

    train = read_tsv(path / "train.tsv")
    test = read_tsv(path / "test.tsv")
    for split_name, examples in (("train", train), ("test", test)):
        indices = [ex.index for ex in examples]
        if len(indices) != len(set(indices)):
            raise TaskError(f"{name}/{split_name}.tsv: duplicate indices")
        for ex in examples:
            if ex.answer not in labels:
                raise TaskError(
                    f"{name}/{split_name}.tsv index {ex.index}: "
                    f"answer {ex.answer!r} not in labels {labels}"
                )

    return Task(
        name=name,
        reasoning_type=meta["reasoning_type"],
        legal_domain=meta["legal_domain"],
        language=meta.get("language", "fr"),
        answer_type=meta["answer_type"],
        labels=list(labels),
        metric=meta["metric"],
        description=str(meta.get("description", "")).strip(),
        version=int(meta.get("version", 1)),
        path=path,
        base_prompt=base_prompt,
        train=train,
        test=test,
    )


def default_tasks_dir() -> Path:
    """Locate the tasks/ directory: cwd first, then the repo root (src layout)."""
    candidates = [Path.cwd() / "tasks", Path(__file__).resolve().parents[2] / "tasks"]
    for candidate in candidates:
        if candidate.is_dir():
            return candidate
    raise TaskError(f"No tasks/ directory found (looked in: {[str(c) for c in candidates]})")


def discover_tasks(tasks_dir: Path | None = None) -> list[Task]:
    """Load every directory under tasks_dir that contains a task.yaml."""
    tasks_dir = Path(tasks_dir) if tasks_dir else default_tasks_dir()
    tasks = [
        load_task(entry)
        for entry in sorted(tasks_dir.iterdir())
        if entry.is_dir() and (entry / "task.yaml").is_file()
    ]
    if not tasks:
        raise TaskError(f"{tasks_dir}: no task folders found")
    return tasks


def resolve_task_names(spec: str, tasks: list[Task]) -> list[Task]:
    """Resolve a --tasks spec: 'all' | 'name1,name2' | 'type:<reasoning_type>'."""
    spec = spec.strip()
    if spec == "all":
        return list(tasks)
    if spec.startswith("type:"):
        reasoning_type = spec.removeprefix("type:")
        if reasoning_type not in REASONING_TYPES:
            raise TaskError(f"unknown reasoning type {reasoning_type!r}")
        selected = [t for t in tasks if t.reasoning_type == reasoning_type]
        if not selected:
            raise TaskError(f"no tasks of type {reasoning_type!r}")
        return selected
    by_name = {t.name: t for t in tasks}
    selected = []
    for name in (n.strip() for n in spec.split(",")):
        if name not in by_name:
            raise TaskError(f"unknown task {name!r} (available: {', '.join(by_name)})")
        selected.append(by_name[name])
    return selected
