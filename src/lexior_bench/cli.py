"""Lexior Bench command-line interface."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

import typer

from .tasks import default_tasks_dir, discover_tasks, resolve_task_names

app = typer.Typer(
    help="Lexior Bench - LLM evaluation benchmark for Quebec law.",
    no_args_is_help=True,
)
annotate_app = typer.Typer(help="Push tasks to / pull validated answers from an annotation tool.")
app.add_typer(annotate_app, name="annotate")


@app.callback()
def main():
    """Lexior Bench - LLM evaluation benchmark for Quebec law."""


@app.command("list-tasks")
def list_tasks():
    """List available benchmark tasks."""
    tasks = discover_tasks()
    for task in tasks:
        typer.echo(
            f"{task.name:42s} {task.reasoning_type:26s} {task.legal_domain:7s} "
            f"labels={len(task.labels)} train={len(task.train)} test={len(task.test)}"
        )
    typer.echo(f"\n{len(tasks)} tasks.")


@app.command()
def run(
    model: List[str] = typer.Option(
        ..., "--model", "-m", help='Model spec "provider:name" (ollama, openai, anthropic, hf); repeatable.'
    ),
    tasks: str = typer.Option("all", help='Task selection: all | name1,name2 | type:<reasoning_type>.'),
    limit: Optional[int] = typer.Option(None, help="Only the first N test items per task (smoke tests)."),
    max_tokens: int = typer.Option(512, help="Max completion tokens per item."),
    temperature: float = typer.Option(0.0, help="Sampling temperature (ignored by the Anthropic backend)."),
    no_eval: bool = typer.Option(False, "--no-eval", help="Skip automatic evaluation + report."),
    results_dir: Path = typer.Option(Path("results"), help="Output directory for runs."),
):
    """Run models on benchmark tasks and (by default) evaluate + report."""
    from .runner import run_benchmark

    selected = resolve_task_names(tasks, discover_tasks())
    typer.echo(f"Models: {', '.join(model)} — tasks: {', '.join(t.name for t in selected)}")
    run_dir = run_benchmark(
        model,
        selected,
        limit=limit,
        temperature=temperature,
        max_tokens=max_tokens,
        results_dir=results_dir,
    )
    if not no_eval:
        _evaluate_and_report(run_dir)


def _evaluate_and_report(run_dir: Path) -> None:
    from .evaluation import evaluate_run
    from .report import write_report, write_transcript

    scores = evaluate_run(run_dir)
    report_path = write_report(run_dir)
    transcript_path = write_transcript(run_dir)
    typer.echo(f"Wrote {run_dir / 'scores.json'}, {report_path}, {transcript_path}")
    for model, model_scores in scores["models"].items():
        typer.echo(f"  {model}: mean={model_scores['mean']}")


@app.command()
def evaluate(
    run: Path = typer.Option(..., "--run", help="Run directory (results/<run_id>)."),
):
    """Score an existing run directory → scores.json."""
    from .evaluation import evaluate_run

    scores = evaluate_run(run)
    typer.echo(json.dumps(scores, indent=2, ensure_ascii=False))


@app.command()
def report(
    run: Path = typer.Option(..., "--run", help="Run directory (results/<run_id>)."),
):
    """Write report.md + transcript.md for an evaluated run."""
    from .evaluation import evaluate_run
    from .report import write_report, write_transcript

    if not (Path(run) / "scores.json").exists():
        evaluate_run(run)
    typer.echo(f"Wrote {write_report(run)} and {write_transcript(run)}")


@app.command("import-task")
def import_task(
    url: str = typer.Argument(..., help="GitHub URL of a LegalBench-style task folder."),
    name: Optional[str] = typer.Option(None, help="Local task name (default: folder name)."),
    reasoning_type: Optional[str] = typer.Option(
        None, help="One of the 6 types (default: detected from the README)."
    ),
    legal_domain: str = typer.Option("public", help="civil | public."),
    metric: str = typer.Option("balanced_accuracy", help="exact_match | balanced_accuracy."),
    language: str = typer.Option("en", help="Content language tag (informational)."),
    no_hf: bool = typer.Option(False, "--no-hf", help="Don't fetch the test split from Hugging Face."),
):
    """Import a task from a LegalBench-style GitHub repository."""
    from .legalbench_import import build_draft, imported_readme
    from .tasks import TaskError
    from .web.taskforms import create_task

    try:
        draft = build_draft(url, include_hf=not no_hf)
        chosen_type = reasoning_type or draft.suggested_reasoning_type
        if not chosen_type:
            raise TaskError(
                "could not detect the reasoning type from the README — "
                "pass it explicitly with --reasoning-type"
            )
        task_name = name or draft.name
        typer.echo(f"Importing {draft.name!r} as {task_name!r}")
        typer.echo(f"  labels: {', '.join(draft.labels)}")
        typer.echo(
            f"  train: {len(draft.train)} items — test: {len(draft.test)} items"
            + (" (from Hugging Face)" if draft.test_from_hf else "")
        )
        typer.echo(f"  source: {draft.source} — license: {draft.license}")
        for warning in draft.warnings:
            typer.secho(f"  warning: {warning}", fg="yellow")
        task = create_task(
            default_tasks_dir(),
            name=task_name,
            reasoning_type=chosen_type,
            legal_domain=legal_domain,
            metric=metric,
            description=draft.description,
            labels=draft.labels,
            base_prompt=draft.base_prompt,
            train=draft.train,
            test=draft.test,
            language=language,
            extra_meta={"source": draft.source, "license": draft.license, "imported_from": draft.url},
            readme=imported_readme(
                draft, reasoning_type=chosen_type, legal_domain=legal_domain, language=language
            ),
        )
    except TaskError as e:
        typer.secho(f"Import failed: {e}", fg="red")
        raise typer.Exit(1)
    typer.echo(f"Created {task.path} — try: lexior-bench run --model ollama:lexiorgpt --tasks {task.name} --limit 2")


@app.command()
def web(
    host: str = typer.Option("127.0.0.1", help="Bind address (local tool — keep it loopback)."),
    port: int = typer.Option(8000, help="HTTP port."),
    no_browser: bool = typer.Option(False, "--no-browser", help="Don't open the browser."),
):
    """Launch the local web interface (tasks, runs, results, annotation)."""
    import os
    import threading
    import webbrowser

    env_file = Path(".env")
    if env_file.is_file():
        # Convenience for the web UI only: annotation providers read env vars.
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

    import uvicorn

    from .web.app import app as web_app

    url = f"http://{host}:{port}"
    typer.echo(f"Lexior Bench web UI: {url}")
    if not no_browser:
        threading.Timer(1.0, webbrowser.open, [url]).start()
    uvicorn.run(web_app, host=host, port=port, log_level="warning")


def _annotation_provider(provider: Optional[str]):
    import os

    from .annotation import get_provider

    name = provider or os.environ.get("LEXIOR_ANNOTATION_PROVIDER", "argilla")
    return get_provider(name)


@annotate_app.command("push")
def annotate_push(
    provider: Optional[str] = typer.Option(None, help="argilla | labelstudio (default: $LEXIOR_ANNOTATION_PROVIDER, then argilla)."),
    tasks: str = typer.Option("all", help='Task selection: all | name1,name2 | type:<reasoning_type>.'),
    train_only: bool = typer.Option(False, "--train-only", help="Push only the train split."),
):
    """Push task items to the annotation tool for jurist validation."""
    backend = _annotation_provider(provider)
    for task in resolve_task_names(tasks, discover_tasks()):
        backend.push_task(task, include_test=not train_only)


@annotate_app.command("pull")
def annotate_pull(
    provider: Optional[str] = typer.Option(None, help="argilla | labelstudio (default: $LEXIOR_ANNOTATION_PROVIDER, then argilla)."),
    tasks: str = typer.Option("all", help='Task selection: all | name1,name2 | type:<reasoning_type>.'),
    dry_run: bool = typer.Option(False, "--dry-run", help="Print the change summary without rewriting TSVs."),
):
    """Pull validated annotations back into the task TSVs."""
    backend = _annotation_provider(provider)
    for task in resolve_task_names(tasks, discover_tasks()):
        backend.pull_task(task, dry_run=dry_run)


if __name__ == "__main__":
    app()
