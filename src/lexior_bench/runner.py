"""Benchmark runner: models × tasks → results/<run_id>/{run.json,results.json}."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Callable

from .backends import create_backend
from .prompts import render_prompt
from .tasks import Task


def count_items(model_specs: list[str], tasks: list[Task], limit: int | None = None) -> int:
    """Total generations a run will perform (for progress displays)."""
    per_model = sum(len(task.test[:limit] if limit else task.test) for task in tasks)
    return per_model * len(model_specs)


def run_benchmark(
    model_specs: list[str],
    tasks: list[Task],
    *,
    limit: int | None = None,
    temperature: float = 0.0,
    max_tokens: int = 512,
    results_dir: Path = Path("results"),
    on_progress: Callable[[dict], None] | None = None,
) -> Path:
    """Run every model on every task's test split; return the run directory."""
    run_id = time.strftime("%Y%m%d-%H%M%S")
    run_dir = results_dir / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    total = count_items(model_specs, tasks, limit)
    records: list[dict] = []
    for spec in model_specs:
        backend = create_backend(spec)
        for task in tasks:
            items = task.test[:limit] if limit else task.test
            print(f"[{backend.spec}] {task.name} ({len(items)} items)", flush=True)
            for ex in items:
                prompt = render_prompt(task, ex.text)
                try:
                    result = backend.generate(
                        prompt, temperature=temperature, max_tokens=max_tokens
                    )
                    response_text, latency_s = result.text, result.latency_s
                    print(f"  {ex.index}: {latency_s}s", flush=True)
                except Exception as e:
                    response_text, latency_s = f"<ERROR: {e}>", 0.0
                    print(f"  {ex.index}: ERROR {e}", flush=True)
                if on_progress:
                    on_progress(
                        {
                            "model": backend.spec,
                            "task": task.name,
                            "index": ex.index,
                            "done": len(records) + 1,
                            "total": total,
                            "latency_s": latency_s,
                            "error": response_text.startswith("<ERROR:"),
                        }
                    )
                records.append(
                    {
                        "model": backend.spec,
                        "task": task.name,
                        "reasoning_type": task.reasoning_type,
                        "index": ex.index,
                        "prompt": prompt,
                        "reference": ex.answer,
                        "response": response_text,
                        "latency_s": latency_s,
                    }
                )

    run_meta = {
        "run_id": run_id,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "models": list(model_specs),
        "tasks": {
            task.name: {
                "version": task.version,
                "reasoning_type": task.reasoning_type,
                "legal_domain": task.legal_domain,
                "metric": task.metric,
                "labels": task.labels,
            }
            for task in tasks
        },
        "params": {"limit": limit, "temperature": temperature, "max_tokens": max_tokens},
    }
    (run_dir / "run.json").write_text(
        json.dumps(run_meta, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (run_dir / "results.json").write_text(
        json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    errors = sum(r["response"].startswith("<ERROR:") for r in records)
    if errors:
        print(
            f"WARNING: {errors}/{len(records)} items failed with backend errors "
            "(scores treat them as wrong) — check the backend is reachable.",
            flush=True,
        )
    print(f"Saved {len(records)} responses to {run_dir}", flush=True)
    return run_dir
