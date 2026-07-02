"""Build and edit task folders from web-form payloads (validated via load_task)."""

from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path

import yaml

from ..tasks import Example, Task, TaskError, load_task, write_tsv

NAME_RE = re.compile(r"^[a-z][a-z0-9_]*$")

DEFAULT_PROMPT = """Vous êtes un juriste québécois. [Consigne de la tâche — nommez les étiquettes admissibles.]

Répondez uniquement par l'une des étiquettes suivantes : {labels}.

{{{{examples}}}}

Situation : {{{{text}}}}
Réponse :
"""

README_TEMPLATE = """# {name}

**Type de raisonnement :** {reasoning_type} · **Territoire :** {jurisdiction} · **Langue :** français

{description}

**Étiquettes :** {labels}

> ⚠️ Les réponses de référence sont des ébauches en attente de validation par un
> juriste (voir `docs/annotation-workflow.md`).
>
> Données du jeu de tâches publiées sous licence CC BY 4.0.
"""


def default_prompt(labels: list[str]) -> str:
    return DEFAULT_PROMPT.format(labels=", ".join(labels) if labels else "…")


def parse_items(indices: list[str], texts: list[str], answers: list[str]) -> list[Example]:
    """Zip parallel form fields into Examples, skipping fully empty rows."""
    items = []
    for index, text, answer in zip(indices, texts, answers):
        if not text.strip() and not answer.strip():
            continue
        items.append(Example(index=index.strip(), text=text.strip(), answer=answer.strip()))
    return items


def create_task(
    tasks_dir: Path,
    *,
    name: str,
    reasoning_type: str,
    legal_domain: str,
    metric: str,
    description: str,
    labels: list[str],
    base_prompt: str,
    train: list[Example],
    test: list[Example],
    language: str = "fr",
    extra_meta: dict | None = None,
    readme: str | None = None,
) -> Task:
    """Materialize a new task folder; raises TaskError on any validation failure."""
    if not NAME_RE.match(name):
        raise TaskError(
            f"invalid task name {name!r} (expected lowercase letters, digits, underscores)"
        )
    target = tasks_dir / name
    if target.exists():
        raise TaskError(f"task {name!r} already exists")

    meta = {
        "name": name,
        "reasoning_type": reasoning_type,
        "jurisdiction": legal_domain,
        "language": language,
        "answer_type": "classification",
        "labels": labels,
        "metric": metric,
        "description": description.strip(),
        "version": 1,
        **(extra_meta or {}),
    }
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp) / name
        folder.mkdir()
        (folder / "task.yaml").write_text(
            yaml.safe_dump(meta, allow_unicode=True, sort_keys=False), encoding="utf-8"
        )
        (folder / "base_prompt.txt").write_text(base_prompt, encoding="utf-8")
        write_tsv(folder / "train.tsv", train)
        write_tsv(folder / "test.tsv", test)
        (folder / "README.md").write_text(
            readme
            or README_TEMPLATE.format(
                name=name,
                reasoning_type=reasoning_type,
                jurisdiction=legal_domain,
                description=description.strip(),
                labels=" / ".join(labels),
            ),
            encoding="utf-8",
        )
        load_task(folder)  # full validation before anything lands in tasks/
        shutil.move(str(folder), str(target))
    return load_task(target)


def save_items(task: Task, train: list[Example], test: list[Example]) -> Task:
    """Full-replace both splits after validation; rewrites the TSVs in place."""
    for split_name, items in (("train", train), ("test", test)):
        if not items:
            raise TaskError(f"{split_name}: at least one item is required")
        indices = [ex.index for ex in items]
        if len(indices) != len(set(indices)):
            raise TaskError(f"{split_name}: duplicate indices")
        for ex in items:
            if not ex.index or not ex.text or not ex.answer:
                raise TaskError(f"{split_name}: empty cell")
            if ex.answer not in task.labels:
                raise TaskError(
                    f"{split_name} index {ex.index}: answer {ex.answer!r} "
                    f"not in labels {task.labels}"
                )
    write_tsv(task.path / "train.tsv", train)
    write_tsv(task.path / "test.tsv", test)
    return load_task(task.path)
