"""Annotation provider abstraction and shared (pure) record transforms.

The task TSVs are the single source of truth; providers are interchangeable
push/pull adapters. The annotation schema and pull semantics are identical for
every provider:

- answer_ok: Correcte / Incorrecte
- corrected_answer: free text (optional, must be one of the task labels)
- item_status: Validé / À réviser / Rejeté

Pull rules: only "Validé" items are applied (final answer = correction when
answer_ok == "Incorrecte" and a correction is given); "Rejeté" items are
dropped; everything else keeps its current TSV values. Corrections outside the
label set are warned about and skipped. First validated response wins.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from ..tasks import Example, Task, write_tsv

ANSWER_OK_OPTIONS = ["Correcte", "Incorrecte"]
ITEM_STATUS_OPTIONS = ["Validé", "À réviser", "Rejeté"]
STATUS_VALIDATED = "Validé"
STATUS_REJECTED = "Rejeté"
SPLITS = ("train", "test")


@dataclass
class AnnotationItem:
    """A neutral, provider-independent item to annotate."""

    external_id: str
    task_name: str
    split: str
    index: str
    text: str
    proposed_answer: str
    metadata: dict = field(default_factory=dict)


@dataclass
class AnnotatedItem:
    """A provider-independent annotation result for one item."""

    split: str
    index: str
    answer_ok: str | None = None
    corrected_answer: str | None = None
    item_status: str | None = None


@dataclass
class PullChange:
    split: str
    index: str
    action: str  # "corrected" | "rejected" | "invalid_correction"
    old: str
    new: str | None


@dataclass
class PullResult:
    splits: dict[str, list[Example]]
    changes: list[PullChange]
    validated: int  # items confirmed "Validé" (including unchanged answers)
    annotated: int  # items with any annotation


def make_external_id(task_name: str, split: str, index: str) -> str:
    return f"{task_name}-{split}-{index}"


def parse_external_id(external_id: str) -> tuple[str, str, str] | None:
    """Return (task_name, split, index) or None if malformed."""
    parts = external_id.rsplit("-", 2)
    if len(parts) != 3 or parts[1] not in SPLITS:
        return None
    return parts[0], parts[1], parts[2]


def task_to_items(task: Task, include_test: bool = True) -> list[AnnotationItem]:
    """Transform a Task into neutral annotation items (gold answer proposed)."""
    splits = SPLITS if include_test else ("train",)
    items = []
    for split in splits:
        for ex in task.split(split):
            items.append(
                AnnotationItem(
                    external_id=make_external_id(task.name, split, ex.index),
                    task_name=task.name,
                    split=split,
                    index=ex.index,
                    text=ex.text,
                    proposed_answer=ex.answer,
                    metadata={
                        "split": split,
                        "item_index": ex.index,
                        "reasoning_type": task.reasoning_type,
                        "legal_domain": task.legal_domain,
                    },
                )
            )
    return items


def guidelines_for(task: Task) -> str:
    """French annotation guidelines generated from task.yaml."""
    labels = ", ".join(task.labels)
    return (
        f"## Tâche : {task.name}\n\n"
        f"{task.description}\n\n"
        f"**Étiquettes admissibles :** {labels}\n\n"
        "Pour chaque élément :\n"
        "1. Lisez le texte et la réponse proposée.\n"
        "2. Indiquez si la réponse proposée est **Correcte** ou **Incorrecte**.\n"
        "3. Si elle est incorrecte, saisissez la bonne réponse dans « Réponse "
        "corrigée » (elle doit être l'une des étiquettes admissibles, à "
        "l'identique).\n"
        "4. Donnez le statut : **Validé** (réponse finale fiable), **À réviser** "
        "(douteux, à discuter) ou **Rejeté** (élément à retirer du jeu de "
        "données).\n"
    )


def apply_annotations(task: Task, annotated: list[AnnotatedItem]) -> PullResult:
    """Merge annotations into the task's splits (pure; no I/O)."""
    by_key = {(a.split, a.index): a for a in annotated}
    splits: dict[str, list[Example]] = {}
    changes: list[PullChange] = []
    validated = 0
    for split_name in SPLITS:
        new_examples: list[Example] = []
        for ex in task.split(split_name):
            ann = by_key.get((split_name, ex.index))
            if ann is None or ann.item_status not in (STATUS_VALIDATED, STATUS_REJECTED):
                # unannotated (or "À réviser") rows keep their current TSV values
                new_examples.append(ex)
                continue
            if ann.item_status == STATUS_REJECTED:
                changes.append(PullChange(split_name, ex.index, "rejected", ex.answer, None))
                continue
            validated += 1
            final = ex.answer
            correction = (ann.corrected_answer or "").strip()
            if ann.answer_ok == "Incorrecte" and correction:
                if correction not in task.labels:
                    changes.append(
                        PullChange(split_name, ex.index, "invalid_correction", ex.answer, correction)
                    )
                    new_examples.append(ex)
                    continue
                if correction != ex.answer:
                    changes.append(
                        PullChange(split_name, ex.index, "corrected", ex.answer, correction)
                    )
                final = correction
            new_examples.append(Example(index=ex.index, text=ex.text, answer=final))
        splits[split_name] = new_examples
    return PullResult(
        splits=splits, changes=changes, validated=validated, annotated=len(annotated)
    )


class AnnotationProvider(ABC):
    """Push task items to an annotation tool and pull validated answers back."""

    name: str = "base"

    @abstractmethod
    def push_task(self, task: Task, include_test: bool = True) -> None:
        """Create/update the task's dataset in the tool (idempotent re-push)."""

    @abstractmethod
    def fetch_annotations(self, task: Task) -> list[AnnotatedItem]:
        """Fetch current annotations for the task from the tool."""

    def pull_task(self, task: Task, dry_run: bool = False) -> PullResult:
        """Merge validated annotations back into the task TSVs."""
        result = apply_annotations(task, self.fetch_annotations(task))
        print(
            f"[{self.name}] {task.name}: {result.annotated} annotated items, "
            f"{result.validated} validated, {len(result.changes)} changes"
        )
        for change in result.changes:
            if change.action == "corrected":
                print(f"  {change.split}/{change.index}: {change.old!r} -> {change.new!r}")
            elif change.action == "rejected":
                print(f"  {change.split}/{change.index}: rejected (row dropped)")
            else:
                print(
                    f"  {change.split}/{change.index}: WARNING correction {change.new!r} "
                    f"not in labels {task.labels} — skipped, kept {change.old!r}"
                )
        if dry_run:
            print("  (dry-run: TSV files unchanged)")
            return result
        for split_name, examples in result.splits.items():
            write_tsv(task.path / f"{split_name}.tsv", examples)
        print(f"  TSV files rewritten in {task.path} (use git diff to review)")
        return result
