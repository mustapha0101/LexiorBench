from pathlib import Path

import pytest

from lexior_bench.tasks import Task, Example

REPO_ROOT = Path(__file__).resolve().parents[1]
TASKS_DIR = REPO_ROOT / "tasks"


@pytest.fixture
def toy_task(tmp_path) -> Task:
    """A minimal valid in-memory task for prompt/eval/annotation tests."""
    return Task(
        name="toy_task",
        reasoning_type="rule-recall",
        legal_domain="civil",
        language="fr",
        answer_type="classification",
        labels=["Vrai", "Faux"],
        metric="balanced_accuracy",
        description="Tâche jouet.",
        version=1,
        path=tmp_path,
        base_prompt=(
            "Répondez par Vrai ou Faux.\n\n{{examples}}\n\nSituation : {{text}}\nRéponse :\n"
        ),
        train=[
            Example(index="0", text="Le ciel est bleu.", answer="Vrai"),
            Example(index="1", text="La mer est rose.", answer="Faux"),
        ],
        test=[
            Example(index="0", text="L'eau bout à 100 degrés.", answer="Vrai"),
            Example(index="1", text="Deux et deux font cinq.", answer="Faux"),
        ],
    )


def write_task_folder(root: Path, name: str = "toy_task", **overrides) -> Path:
    """Materialize a small valid task folder on disk; overrides patch task.yaml."""
    folder = root / name
    folder.mkdir(parents=True)
    meta = {
        "name": name,
        "reasoning_type": "rule-recall",
        "legal_domain": "civil",
        "language": "fr",
        "answer_type": "classification",
        "labels": ["Vrai", "Faux"],
        "metric": "balanced_accuracy",
        "description": "Tâche jouet.",
        "version": 1,
    }
    meta.update(overrides)
    import yaml

    (folder / "task.yaml").write_text(
        yaml.safe_dump(meta, allow_unicode=True), encoding="utf-8"
    )
    (folder / "base_prompt.txt").write_text(
        "{{examples}}\n\nSituation : {{text}}\nRéponse :\n", encoding="utf-8"
    )
    (folder / "train.tsv").write_text(
        "index\ttext\tanswer\n0\tA\tVrai\n1\tB\tFaux\n", encoding="utf-8"
    )
    (folder / "test.tsv").write_text(
        "index\ttext\tanswer\n0\tC\tVrai\n1\tD\tFaux\n", encoding="utf-8"
    )
    return folder
