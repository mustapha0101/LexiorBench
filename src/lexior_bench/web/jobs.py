"""In-process benchmark run job: one run at a time, polled for progress."""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path

from ..evaluation import evaluate_run
from ..report import write_report, write_transcript
from ..runner import count_items, run_benchmark
from ..tasks import Task


@dataclass
class RunJob:
    id: str
    status: str  # "running" | "done" | "error"
    models: list[str]
    total: int
    done: int = 0
    errors: int = 0
    current: str = ""
    run_id: str | None = None
    error: str | None = None
    started_at: str = field(default_factory=lambda: time.strftime("%Y-%m-%dT%H:%M:%S"))

    def as_dict(self) -> dict:
        return asdict(self)


_lock = threading.Lock()
_job: RunJob | None = None


def status() -> RunJob | None:
    return _job


def start(
    models: list[str],
    tasks: list[Task],
    *,
    limit: int | None,
    max_tokens: int,
    results_dir: Path = Path("results"),
) -> RunJob | None:
    """Start a run in a background thread; None if one is already running."""
    global _job
    with _lock:
        if _job is not None and _job.status == "running":
            return None
        job = RunJob(
            id=time.strftime("%Y%m%d-%H%M%S"),
            status="running",
            models=list(models),
            total=count_items(models, tasks, limit),
        )
        _job = job

    def on_progress(event: dict) -> None:
        job.done = event["done"]
        job.errors += 1 if event["error"] else 0
        job.current = f"{event['model']} · {event['task']} · {event['index']}"

    def target() -> None:
        try:
            run_dir = run_benchmark(
                models,
                tasks,
                limit=limit,
                max_tokens=max_tokens,
                results_dir=results_dir,
                on_progress=on_progress,
            )
            evaluate_run(run_dir)
            write_report(run_dir)
            write_transcript(run_dir)
            job.run_id = run_dir.name
            job.status = "done"
        except Exception as e:
            job.error = f"{type(e).__name__}: {e}"
            job.status = "error"

    threading.Thread(target=target, daemon=True).start()
    return job
