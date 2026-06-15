"""Label Studio annotation adapter: one Label Studio project per task."""

from __future__ import annotations

import os
from xml.sax.saxutils import escape, quoteattr

from ..tasks import Task
from .base import (
    ANSWER_OK_OPTIONS,
    ITEM_STATUS_OPTIONS,
    AnnotatedItem,
    AnnotationProvider,
    guidelines_for,
    make_external_id,
    task_to_items,
)

DEFAULT_URL = "http://localhost:8080"


def label_config_for(task: Task) -> str:
    """Generate the Label Studio labeling-interface XML for a task."""
    answer_ok_choices = "\n    ".join(
        f"<Choice value={quoteattr(option)}/>" for option in ANSWER_OK_OPTIONS
    )
    status_choices = "\n    ".join(
        f"<Choice value={quoteattr(option)}/>" for option in ITEM_STATUS_OPTIONS
    )
    labels = escape(", ".join(task.labels))
    return f"""<View>
  <Header value="Texte"/>
  <Text name="text" value="$text"/>
  <Header value="Réponse proposée"/>
  <Text name="proposed_answer" value="$proposed_answer"/>
  <Header value="La réponse proposée est-elle correcte?"/>
  <Choices name="answer_ok" toName="text" choice="single" required="true">
    {answer_ok_choices}
  </Choices>
  <Header value="Réponse corrigée (si incorrecte) — étiquettes admissibles : {labels}"/>
  <TextArea name="corrected_answer" toName="text" rows="1" maxSubmissions="1"/>
  <Header value="Statut de l'élément"/>
  <Choices name="item_status" toName="text" choice="single" required="true">
    {status_choices}
  </Choices>
</View>"""


def _get(obj, key, default=None):
    """Field access tolerant to both dicts and pydantic models."""
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


class LabelStudioProvider(AnnotationProvider):
    name = "labelstudio"

    def __init__(self, url: str | None = None, api_key: str | None = None):
        from label_studio_sdk.client import LabelStudio

        api_key = api_key or os.environ.get("LABEL_STUDIO_API_KEY")
        if not api_key:
            raise ValueError(
                "LABEL_STUDIO_API_KEY is not set. Get a personal access token from "
                "the Label Studio UI (Account & Settings page) and export it."
            )
        self.client = LabelStudio(
            base_url=url or os.environ.get("LABEL_STUDIO_URL", DEFAULT_URL),
            api_key=api_key,
        )

    @staticmethod
    def project_title(task: Task) -> str:
        import hashlib
        full = f"lexior-bench-{task.name}"
        if len(full) <= 50:
            return full
        # Label Studio enforces a 50-char title limit; keep a 4-char hash to stay unique.
        suffix = hashlib.md5(task.name.encode()).hexdigest()[:4]
        return f"{full[:45]}-{suffix}"

    def _find_project(self, task: Task):
        title = self.project_title(task)
        for project in self.client.projects.list(title=title):
            if project.title == title:
                return project
        return None

    def _existing_tasks_by_external_id(self, project_id: int) -> dict:
        existing = {}
        for ls_task in self.client.tasks.list(project=project_id, fields="all"):
            external_id = _get(_get(ls_task, "data", {}) or {}, "external_id")
            if external_id:
                existing[external_id] = ls_task
        return existing

    def push_task(self, task: Task, include_test: bool = True) -> None:
        project = self._find_project(task)
        if project is None:
            project = self.client.projects.create(
                title=self.project_title(task),
                description=task.description,
                label_config=label_config_for(task),
                expert_instruction=guidelines_for(task),
                show_instruction=True,
            )
        existing = self._existing_tasks_by_external_id(project.id)

        imported = updated = skipped = 0
        to_import = []
        for item in task_to_items(task, include_test=include_test):
            data = {
                "external_id": item.external_id,
                "text": item.text,
                "proposed_answer": item.proposed_answer,
                **item.metadata,
            }
            current = existing.get(item.external_id)
            if current is None:
                to_import.append({"data": data})
                imported += 1
            elif dict(_get(current, "data", {}) or {}) != data:
                self.client.tasks.update(id=str(_get(current, "id")), data=data)
                updated += 1
            else:
                skipped += 1
        if to_import:
            self.client.projects.import_tasks(id=project.id, request=to_import)
        print(
            f"[labelstudio] {task.name}: project {project.id} — "
            f"{imported} imported, {updated} updated, {skipped} unchanged"
        )

    def fetch_annotations(self, task: Task) -> list[AnnotatedItem]:
        project = self._find_project(task)
        if project is None:
            print(f"[labelstudio] {task.name}: project not found — nothing to pull")
            return []
        annotated: list[AnnotatedItem] = []
        for ls_task in self.client.tasks.list(project=project.id, fields="all"):
            data = _get(ls_task, "data", {}) or {}
            split = _get(data, "split")
            index = _get(data, "item_index")
            if split is None or index is None:
                continue
            annotations = _get(ls_task, "annotations") or []
            # first-response-wins; skip cancelled/empty annotations
            results = next(
                (
                    _get(a, "result") or []
                    for a in annotations
                    if not _get(a, "was_cancelled") and (_get(a, "result") or [])
                ),
                [],
            )
            values: dict[str, str] = {}
            for result in results:
                from_name = _get(result, "from_name")
                value = _get(result, "value") or {}
                if _get(value, "choices"):
                    values[from_name] = _get(value, "choices")[0]
                elif _get(value, "text"):
                    values[from_name] = _get(value, "text")[0]
            annotated.append(
                AnnotatedItem(
                    split=str(split),
                    index=str(index),
                    answer_ok=values.get("answer_ok"),
                    corrected_answer=values.get("corrected_answer"),
                    item_status=values.get("item_status"),
                )
            )
        return annotated
