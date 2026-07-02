"""Evaluation: label extraction and per-task metrics → scores.json."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

UNPARSED = "<unparsed>"


def normalize(text: str) -> str:
    """NFKD accent-strip + casefold + strip punctuation + collapse whitespace."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^\w\s]", " ", text.casefold())
    return " ".join(text.split())


def extract_label(response: str, labels: list[str]) -> str:
    """Map a raw model response onto one of the task labels.

    Tries an exact match on the first non-empty line, then a word-boundary
    substring search over the whole response (earliest occurrence wins, longer
    label on ties). Returns UNPARSED when nothing matches.
    """
    if response.startswith("<ERROR:"):
        return UNPARSED
    normalized_labels = [(label, normalize(label)) for label in labels]

    first_line = next((line for line in response.splitlines() if line.strip()), "")
    normalized_first = normalize(first_line)
    for label, norm_label in normalized_labels:
        if normalized_first == norm_label:
            return label

    normalized_response = normalize(response)
    best: tuple[int, int, str] | None = None  # (position, -len, label)
    for label, norm_label in normalized_labels:
        match = re.search(rf"\b{re.escape(norm_label)}\b", normalized_response)
        if match:
            key = (match.start(), -len(norm_label), label)
            if best is None or key < best:
                best = key
    return best[2] if best else UNPARSED


def exact_match(references: list[str], predictions: list[str]) -> float:
    if not references:
        return 0.0
    return sum(r == p for r, p in zip(references, predictions)) / len(references)


def balanced_accuracy(references: list[str], predictions: list[str]) -> float:
    """Mean per-class recall over the classes present in the references."""
    classes = sorted(set(references))
    if not classes:
        return 0.0
    recalls = []
    for cls in classes:
        relevant = [(r, p) for r, p in zip(references, predictions) if r == cls]
        recalls.append(sum(r == p for r, p in relevant) / len(relevant))
    return sum(recalls) / len(recalls)


METRIC_FUNCS = {
    "exact_match": exact_match,
    "balanced_accuracy": balanced_accuracy,
}
MANUAL_METRICS = {"manual", "llm_judge", "parity_analysis"}


def evaluate_run(run_dir: Path) -> dict:
    """Score a run directory and write scores.json."""
    run_dir = Path(run_dir)
    run_meta = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    records = json.loads((run_dir / "results.json").read_text(encoding="utf-8"))

    scores: dict = {"run_id": run_meta["run_id"], "models": {}}
    for model in run_meta["models"]:
        model_tasks: dict = {}
        for task_name, task_meta in run_meta["tasks"].items():
            rows = [r for r in records if r["model"] == model and r["task"] == task_name]
            if not rows:
                continue
            references = [r["reference"] for r in rows]
            predictions = [extract_label(r["response"], task_meta["labels"]) for r in rows]
            metric = task_meta["metric"]
            score = (
                None
                if metric in MANUAL_METRICS
                else round(METRIC_FUNCS[metric](references, predictions), 4)
            )
            model_tasks[task_name] = {
                "metric": metric,
                "score": score,
                "exact_match": round(exact_match(references, predictions), 4),
                "unparsed_rate": round(
                    sum(p == UNPARSED for p in predictions) / len(predictions), 4
                ),
                "errors": sum(r["response"].startswith("<ERROR:") for r in rows),
                "n": len(rows),
                "reasoning_type": task_meta["reasoning_type"],
                "legal_domain": task_meta["legal_domain"],
            }

        def mean_over(key: str) -> dict:
            groups: dict[str, list[float]] = {}
            for task_scores in model_tasks.values():
                if task_scores["score"] is None:
                    continue
                groups.setdefault(task_scores[key], []).append(task_scores["score"])
            return {
                group: round(sum(values) / len(values), 4)
                for group, values in sorted(groups.items())
            }

        scored = [t["score"] for t in model_tasks.values() if t["score"] is not None]
        scores["models"][model] = {
            "tasks": model_tasks,
            "by_reasoning_type": mean_over("reasoning_type"),
            "by_legal_domain": mean_over("legal_domain"),
            "mean": round(sum(scored) / len(scored), 4) if scored else None,
        }

    (run_dir / "scores.json").write_text(
        json.dumps(scores, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return scores
