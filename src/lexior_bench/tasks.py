"""Task registry: load and validate LexiorBench task folders.

V2 tasks use task.yaml, base_prompt.txt, data_spec.md, and sample.tsv for
task explanation/examples. train.tsv and test.tsv may exist as empty
placeholders until the task is validated and promoted for evaluation.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

REASONING_TYPES = (
    "issue_spotting",
    "rule_recall",
    "rule_application",
    "rule_conclusion",
    "rule_application_conclusion",
    "interpretation",
    "rhetorical",
    "cross_task_metric",
)
REASONING_TYPE_ALIASES = {
    "issue-spotting": "issue_spotting",
    "rule-recall": "rule_recall",
    "rule-application": "rule_application",
    "rule-conclusion": "rule_conclusion",
    "rhetorical-understanding": "rhetorical",
}
JURISDICTIONS = ("quebec", "federal_ca", "both")
LEGAL_DOMAINS = JURISDICTIONS
JURISDICTION_ALIASES = {"civil": "quebec", "public": "both"}
ANSWER_TYPES = ("classification", "generation", "classification_and_generation", "cross_task_metric")
METRICS = ("exact_match", "balanced_accuracy", "manual", "llm_judge", "parity_analysis")
TSV_COLUMNS = ["index", "text", "answer"]
SAMPLE_TSV_COLUMNS = ["index", "text", "answer", "source_model"]


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
    sample: list[Example]
    train: list[Example]
    test: list[Example]

    def split(self, name: str) -> list[Example]:
        if name == "train":
            return self.train
        if name == "test":
            return self.test
        if name == "sample":
            return self.sample
        raise ValueError(f"unknown split {name!r}")


def read_tsv(path: Path, *, allow_empty: bool = False, allow_source_model: bool = False) -> list[Example]:
    """Read a TSV with index, text and answer columns.

    sample.tsv may include an additional source_model column. Empty train/test
    files are allowed while tasks are still awaiting validated splits.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        if allow_empty:
            return []
        raise TaskError(f"{path}: file is empty")
    header = lines[0].split("\t")
    expected_headers = [TSV_COLUMNS]
    if allow_source_model:
        expected_headers.append(SAMPLE_TSV_COLUMNS)
    if header not in expected_headers:
        raise TaskError(f"{path}: header must be one of {expected_headers}, got {header}")
    examples: list[Example] = []
    for lineno, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != len(header):
            raise TaskError(
                f"{path}:{lineno}: expected {len(header)} tab-separated cells, got {len(cells)} "
                "(stray tab or missing column?)"
            )
        row = dict(zip(header, (cell.strip() for cell in cells)))
        index, text, answer = row["index"], row["text"], row["answer"]
        if not index or not text or not answer:
            raise TaskError(f"{path}:{lineno}: empty cell")
        examples.append(Example(index=index, text=text, answer=answer))
    if not examples and not allow_empty:
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


def normalize_reasoning_type(value: str) -> str:
    return REASONING_TYPE_ALIASES.get(value, value)


def normalize_jurisdiction(meta: dict) -> str:
    value = meta.get("jurisdiction", meta.get("legal_domain", ""))
    return JURISDICTION_ALIASES.get(value, value)


def infer_labels(meta: dict, examples: list[Example]) -> list[str]:
    labels = meta.get("labels") or []
    if labels:
        return list(labels)
    answer_type = meta.get("answer_type")
    if answer_type in ("generation", "cross_task_metric"):
        return []
    answers = []
    seen = set()
    for ex in examples:
        if ex.answer not in seen:
            answers.append(ex.answer)
            seen.add(ex.answer)
    return answers


def load_task(path: Path) -> Task:
    """Load and validate one task folder."""
    path = Path(path)
    yaml_path = path / "task.yaml"
    meta = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))

    name = meta.get("name", "")
    if name != path.name:
        raise TaskError(f"{yaml_path}: name {name!r} does not match folder {path.name!r}")
    reasoning_type = normalize_reasoning_type(meta.get("reasoning_type", ""))
    jurisdiction = normalize_jurisdiction(meta)
    if reasoning_type not in REASONING_TYPES:
        raise TaskError(f"{name}: reasoning_type must be one of {REASONING_TYPES}")
    if jurisdiction not in JURISDICTIONS:
        raise TaskError(f"{name}: jurisdiction must be one of {JURISDICTIONS}")
    if meta.get("answer_type") not in ANSWER_TYPES:
        raise TaskError(f"{name}: answer_type must be one of {ANSWER_TYPES}")
    if meta.get("metric") not in METRICS:
        raise TaskError(f"{name}: metric must be one of {METRICS}")

    sample_path = path / "sample.tsv"
    sample = read_tsv(sample_path, allow_empty=True, allow_source_model=True) if sample_path.exists() else []
    labels = infer_labels(meta, sample)
    if labels and len(labels) != len(set(labels)):
        raise TaskError(f"{name}: labels must be unique strings")
    if meta.get("answer_type") == "classification" and not labels:
        raise TaskError(f"{name}: classification tasks need labels or sample answers")

    base_prompt_path = path / "base_prompt.txt"
    base_prompt = base_prompt_path.read_text(encoding="utf-8") if base_prompt_path.exists() else ""
    if meta.get("answer_type") != "cross_task_metric" and "{{text}}" not in base_prompt:
        raise TaskError(f"{name}: base_prompt.txt must contain {{{{text}}}}")

    train_path = path / "train.tsv"
    test_path = path / "test.tsv"
    train = read_tsv(train_path, allow_empty=True) if train_path.exists() else []
    test = read_tsv(test_path, allow_empty=True) if test_path.exists() else []
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
        reasoning_type=reasoning_type,
        legal_domain=jurisdiction,
        language=meta.get("language", "fr"),
        answer_type=meta["answer_type"],
        labels=list(labels),
        metric=meta["metric"],
        description=str(meta.get("purpose", meta.get("description", ""))).strip(),
        version=int(meta.get("version", 1)),
        path=path,
        base_prompt=base_prompt,
        sample=sample,
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
        reasoning_type = normalize_reasoning_type(spec.removeprefix("type:"))
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
