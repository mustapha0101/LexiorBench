from lexior_bench.annotation.base import (
    AnnotatedItem,
    AnnotationProvider,
    apply_annotations,
    make_external_id,
    parse_external_id,
    task_to_items,
)
from lexior_bench.tasks import read_tsv

from conftest import write_task_folder
from lexior_bench.tasks import load_task


def test_external_id_roundtrip():
    eid = make_external_id("civil_rule_recall_ccq", "test", "7")
    assert eid == "civil_rule_recall_ccq-test-7"
    assert parse_external_id(eid) == ("civil_rule_recall_ccq", "test", "7")
    assert parse_external_id("garbage") is None
    assert parse_external_id("task-nosplit-3") is None


def test_task_to_items(toy_task):
    items = task_to_items(toy_task)
    assert len(items) == 4  # 2 train + 2 test
    first = items[0]
    assert first.external_id == "toy_task-train-0"
    assert first.proposed_answer == "Vrai"
    assert first.metadata["split"] == "train"
    train_only = task_to_items(toy_task, include_test=False)
    assert all(item.split == "train" for item in train_only)


def test_apply_annotations_rules(toy_task):
    annotated = [
        # validated and correct: unchanged
        AnnotatedItem(split="train", index="0", answer_ok="Correcte", item_status="Validé"),
        # validated with correction: answer replaced
        AnnotatedItem(
            split="train", index="1", answer_ok="Incorrecte",
            corrected_answer="Vrai", item_status="Validé",
        ),
        # rejected: row dropped
        AnnotatedItem(split="test", index="0", answer_ok="Correcte", item_status="Rejeté"),
        # test/1 left unannotated: kept as-is
    ]
    result = apply_annotations(toy_task, annotated)
    assert result.validated == 2
    train = {ex.index: ex.answer for ex in result.splits["train"]}
    assert train == {"0": "Vrai", "1": "Vrai"}  # index 1 corrected Faux -> Vrai
    test_indices = [ex.index for ex in result.splits["test"]]
    assert test_indices == ["1"]  # index 0 rejected
    actions = {(c.split, c.index): c.action for c in result.changes}
    assert actions == {("train", "1"): "corrected", ("test", "0"): "rejected"}


def test_apply_annotations_invalid_correction_kept(toy_task):
    annotated = [
        AnnotatedItem(
            split="train", index="0", answer_ok="Incorrecte",
            corrected_answer="Peut-être", item_status="Validé",
        ),
    ]
    result = apply_annotations(toy_task, annotated)
    assert result.splits["train"][0].answer == "Vrai"  # original kept
    assert result.changes[0].action == "invalid_correction"


def test_apply_annotations_a_reviser_keeps_row(toy_task):
    annotated = [
        AnnotatedItem(
            split="train", index="1", answer_ok="Incorrecte",
            corrected_answer="Vrai", item_status="À réviser",
        ),
    ]
    result = apply_annotations(toy_task, annotated)
    # not validated → correction NOT applied, row kept
    assert result.splits["train"][1].answer == "Faux"
    assert result.validated == 0
    assert result.changes == []


class FakeProvider(AnnotationProvider):
    """In-memory provider exercising the shared pull_task flow."""

    name = "fake"

    def __init__(self, annotated):
        self._annotated = annotated
        self.pushed = []

    def push_task(self, task, include_test=True):
        self.pushed.extend(task_to_items(task, include_test=include_test))

    def fetch_annotations(self, task):
        return self._annotated


def test_pull_task_dry_run_leaves_tsv_untouched(tmp_path):
    task = load_task(write_task_folder(tmp_path))
    before = (task.path / "train.tsv").read_text(encoding="utf-8")
    provider = FakeProvider(
        [AnnotatedItem(split="train", index="0", answer_ok="Incorrecte",
                       corrected_answer="Faux", item_status="Validé")]
    )
    result = provider.pull_task(task, dry_run=True)
    assert result.changes[0].action == "corrected"
    assert (task.path / "train.tsv").read_text(encoding="utf-8") == before


def test_pull_task_rewrites_tsv(tmp_path):
    task = load_task(write_task_folder(tmp_path))
    provider = FakeProvider(
        [
            AnnotatedItem(split="train", index="0", answer_ok="Incorrecte",
                          corrected_answer="Faux", item_status="Validé"),
            AnnotatedItem(split="test", index="1", item_status="Rejeté"),
        ]
    )
    provider.pull_task(task, dry_run=False)
    train = read_tsv(task.path / "train.tsv")
    assert train[0].answer == "Faux"
    test = read_tsv(task.path / "test.tsv")
    assert [ex.index for ex in test] == ["0"]
