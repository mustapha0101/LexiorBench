import pytest

from lexior_bench.tasks import (
    REASONING_TYPES,
    Example,
    TaskError,
    discover_tasks,
    load_task,
    read_tsv,
    resolve_task_names,
    write_tsv,
)

from conftest import TASKS_DIR, write_task_folder


def test_discover_real_seed_tasks():
    """Loading every real seed task doubles as data validation."""
    tasks = discover_tasks(TASKS_DIR)
    assert len(tasks) == 6
    assert {t.reasoning_type for t in tasks} == set(REASONING_TYPES)
    assert {t.legal_domain for t in tasks} == {"civil", "public"}
    for task in tasks:
        assert task.language == "fr"
        assert len(task.train) >= 4
        assert len(task.test) >= 8
        assert "{{text}}" in task.base_prompt


def test_load_valid_toy_task(tmp_path):
    folder = write_task_folder(tmp_path)
    task = load_task(folder)
    assert task.name == "toy_task"
    assert [ex.index for ex in task.train] == ["0", "1"]


def test_name_must_match_folder(tmp_path):
    folder = write_task_folder(tmp_path, name="toy_task")
    (folder / "task.yaml").write_text(
        (folder / "task.yaml").read_text(encoding="utf-8").replace("toy_task", "other"),
        encoding="utf-8",
    )
    with pytest.raises(TaskError, match="does not match folder"):
        load_task(folder)


def test_bad_reasoning_type(tmp_path):
    folder = write_task_folder(tmp_path, reasoning_type="vibes")
    with pytest.raises(TaskError, match="reasoning_type"):
        load_task(folder)


def test_answer_not_in_labels(tmp_path):
    folder = write_task_folder(tmp_path)
    (folder / "test.tsv").write_text(
        "index\ttext\tanswer\n0\tC\tPeut-être\n", encoding="utf-8"
    )
    with pytest.raises(TaskError, match="not in labels"):
        load_task(folder)


def test_duplicate_indices(tmp_path):
    folder = write_task_folder(tmp_path)
    (folder / "train.tsv").write_text(
        "index\ttext\tanswer\n0\tA\tVrai\n0\tB\tFaux\n", encoding="utf-8"
    )
    with pytest.raises(TaskError, match="duplicate indices"):
        load_task(folder)


def test_stray_tab_in_cell(tmp_path):
    folder = write_task_folder(tmp_path)
    (folder / "train.tsv").write_text(
        "index\ttext\tanswer\n0\tA\tavec\ttab\tVrai\n", encoding="utf-8"
    )
    with pytest.raises(TaskError, match="3 tab-separated cells"):
        load_task(folder)


def test_missing_text_placeholder(tmp_path):
    folder = write_task_folder(tmp_path)
    (folder / "base_prompt.txt").write_text("pas de placeholder", encoding="utf-8")
    with pytest.raises(TaskError, match="must contain"):
        load_task(folder)


def test_write_tsv_roundtrip(tmp_path):
    examples = [Example(index="0", text="Été à l'île d'Orléans", answer="Vrai")]
    path = tmp_path / "out.tsv"
    write_tsv(path, examples)
    assert read_tsv(path) == examples
    raw = path.read_bytes()
    assert b"\r" not in raw  # LF endings even on Windows
    assert "Été".encode("utf-8") in raw


def test_write_tsv_rejects_embedded_tab(tmp_path):
    with pytest.raises(TaskError, match="tab/newline"):
        write_tsv(tmp_path / "out.tsv", [Example(index="0", text="a\tb", answer="X")])


def test_resolve_task_names_all_and_type_and_list():
    tasks = discover_tasks(TASKS_DIR)
    assert resolve_task_names("all", tasks) == tasks
    by_type = resolve_task_names("type:rule-recall", tasks)
    assert [t.name for t in by_type] == ["civil_rule_recall_ccq"]
    pair = resolve_task_names("civil_rule_recall_ccq, public_interpretation_charte", tasks)
    assert [t.name for t in pair] == ["civil_rule_recall_ccq", "public_interpretation_charte"]
    with pytest.raises(TaskError, match="unknown task"):
        resolve_task_names("nope", tasks)
    with pytest.raises(TaskError, match="unknown reasoning type"):
        resolve_task_names("type:nope", tasks)
