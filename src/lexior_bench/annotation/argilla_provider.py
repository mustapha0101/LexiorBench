"""Argilla 2.x annotation adapter: one Argilla dataset per task."""

from __future__ import annotations

import os

from ..tasks import Task
from .base import (
    ANSWER_OK_OPTIONS,
    ITEM_STATUS_OPTIONS,
    AnnotatedItem,
    AnnotationProvider,
    guidelines_for,
    parse_external_id,
    task_to_items,
)

WORKSPACE = "lexior-bench"
DEFAULT_API_URL = "http://localhost:6900"
DEFAULT_API_KEY = "argilla.apikey"


class ArgillaProvider(AnnotationProvider):
    name = "argilla"

    def __init__(self, api_url: str | None = None, api_key: str | None = None):
        import argilla as rg

        self.rg = rg
        self.client = rg.Argilla(
            api_url=api_url or os.environ.get("ARGILLA_API_URL", DEFAULT_API_URL),
            api_key=api_key or os.environ.get("ARGILLA_API_KEY", DEFAULT_API_KEY),
        )

    @staticmethod
    def dataset_name(task: Task) -> str:
        return f"lexior-bench-{task.name}"

    def _ensure_workspace(self):
        workspace = self.client.workspaces(WORKSPACE)
        if workspace is None:
            workspace = self.client.workspaces.add(self.rg.Workspace(name=WORKSPACE))
        return workspace

    def _settings(self, task: Task):
        rg = self.rg
        labels = ", ".join(task.labels)
        return rg.Settings(
            guidelines=guidelines_for(task),
            fields=[
                rg.TextField(name="text", title="Texte"),
                rg.TextField(name="proposed_answer", title="Réponse proposée"),
            ],
            questions=[
                rg.LabelQuestion(
                    name="answer_ok",
                    labels=ANSWER_OK_OPTIONS,
                    title="La réponse proposée est-elle correcte?",
                    required=True,
                ),
                rg.TextQuestion(
                    name="corrected_answer",
                    title="Réponse corrigée (si incorrecte)",
                    description=f"Doit être l'une des étiquettes : {labels}",
                    required=False,
                ),
                rg.LabelQuestion(
                    name="item_status",
                    labels=ITEM_STATUS_OPTIONS,
                    title="Statut de l'élément",
                    required=True,
                ),
            ],
            metadata=[
                rg.TermsMetadataProperty(name="split"),
                rg.TermsMetadataProperty(name="item_index"),
                rg.TermsMetadataProperty(name="reasoning_type"),
                rg.TermsMetadataProperty(name="legal_domain"),
            ],
        )

    def push_task(self, task: Task, include_test: bool = True) -> None:
        rg = self.rg
        self._ensure_workspace()
        name = self.dataset_name(task)
        dataset = self.client.datasets(name, workspace=WORKSPACE)
        if dataset is None:
            dataset = rg.Dataset(
                name=name, workspace=WORKSPACE, settings=self._settings(task), client=self.client
            ).create()
        items = task_to_items(task, include_test=include_test)
        records = [
            rg.Record(
                id=item.external_id,
                fields={"text": item.text, "proposed_answer": item.proposed_answer},
                metadata=item.metadata,
                suggestions=[
                    rg.Suggestion(question_name="answer_ok", value="Correcte", agent="gold-draft")
                ],
            )
            for item in items
        ]
        dataset.records.log(records)
        print(f"[argilla] {task.name}: pushed {len(records)} records to dataset {name!r}")

    def fetch_annotations(self, task: Task) -> list[AnnotatedItem]:
        dataset = self.client.datasets(self.dataset_name(task), workspace=WORKSPACE)
        if dataset is None:
            print(f"[argilla] {task.name}: dataset not found on server — nothing to pull")
            return []
        annotated: list[AnnotatedItem] = []
        for record in dataset.records(with_responses=True):
            parsed = parse_external_id(str(record.id))
            if parsed is None or parsed[0] != task.name:
                continue
            _, split, index = parsed

            def first_response(question_name: str):
                responses = record.responses[question_name]
                return responses[0].value if responses else None

            annotated.append(
                AnnotatedItem(
                    split=split,
                    index=index,
                    answer_ok=first_response("answer_ok"),
                    corrected_answer=first_response("corrected_answer"),
                    item_status=first_response("item_status"),
                )
            )
        return annotated
