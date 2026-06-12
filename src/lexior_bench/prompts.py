"""Prompt rendering: {{examples}} / {{text}} substitution in base_prompt.txt."""

from __future__ import annotations

from .tasks import Task

EXAMPLE_TEMPLATE = "Situation : {text}\nRéponse : {answer}"


def render_examples(task: Task) -> str:
    """Render the few-shot block from the task's train split."""
    return "\n\n".join(
        EXAMPLE_TEMPLATE.format(text=ex.text, answer=ex.answer) for ex in task.train
    )


def render_prompt(task: Task, text: str) -> str:
    """Render the full prompt for one test item.

    If the base prompt contains {{examples}}, few-shot blocks are rendered from
    train.tsv; pure-LegalBench prompts (no {{examples}}) pass through as-is.
    """
    prompt = task.base_prompt
    if "{{examples}}" in prompt:
        prompt = prompt.replace("{{examples}}", render_examples(task))
    return prompt.replace("{{text}}", text)
