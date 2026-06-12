"""Reporting: report.md (leaderboard) + transcript.md for a run directory."""

from __future__ import annotations

import json
from pathlib import Path

from .evaluation import UNPARSED, extract_label


def _fmt(score: float | None) -> str:
    return "—" if score is None else f"{score:.1%}"


def write_report(run_dir: Path) -> Path:
    """Write report.md: leaderboard models × tasks + means per type and domain."""
    run_dir = Path(run_dir)
    run_meta = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    scores = json.loads((run_dir / "scores.json").read_text(encoding="utf-8"))

    task_names = list(run_meta["tasks"])
    models = list(scores["models"])
    lines = [
        f"# Lexior Bench — rapport du run `{run_meta['run_id']}`",
        "",
        f"Date : {run_meta['created_at']} · Paramètres : {json.dumps(run_meta['params'])}",
        "",
        "## Classement (score par tâche)",
        "",
        "| Modèle | " + " | ".join(task_names) + " | Moyenne |",
        "|---" * (len(task_names) + 2) + "|",
    ]
    for model in models:
        model_scores = scores["models"][model]
        cells = [
            _fmt(model_scores["tasks"].get(t, {}).get("score")) for t in task_names
        ]
        lines.append(
            f"| `{model}` | " + " | ".join(cells) + f" | **{_fmt(model_scores['mean'])}** |"
        )

    for title, key in (
        ("Par type de raisonnement", "by_reasoning_type"),
        ("Par domaine juridique", "by_legal_domain"),
    ):
        groups = sorted({g for m in models for g in scores["models"][m][key]})
        lines += [
            "",
            f"## {title}",
            "",
            "| Modèle | " + " | ".join(groups) + " |",
            "|---" * (len(groups) + 1) + "|",
        ]
        for model in models:
            by_group = scores["models"][model][key]
            lines.append(
                f"| `{model}` | "
                + " | ".join(_fmt(by_group.get(g)) for g in groups)
                + " |"
            )

    lines += [
        "",
        "## Taux de réponses non analysables",
        "",
        "| Modèle | " + " | ".join(task_names) + " |",
        "|---" * (len(task_names) + 1) + "|",
    ]
    for model in models:
        tasks_scores = scores["models"][model]["tasks"]
        lines.append(
            f"| `{model}` | "
            + " | ".join(
                _fmt(tasks_scores.get(t, {}).get("unparsed_rate")) for t in task_names
            )
            + " |"
        )

    report_path = run_dir / "report.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def write_transcript(run_dir: Path) -> Path:
    """Write transcript.md: every prompt/response with ✓/✗ per item."""
    run_dir = Path(run_dir)
    run_meta = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    records = json.loads((run_dir / "results.json").read_text(encoding="utf-8"))

    lines = [f"# Transcription — run `{run_meta['run_id']}`", ""]
    for model in run_meta["models"]:
        lines += [f"## Modèle : `{model}`", ""]
        for task_name, task_meta in run_meta["tasks"].items():
            rows = [r for r in records if r["model"] == model and r["task"] == task_name]
            if not rows:
                continue
            lines += [f"### {task_name}", ""]
            for row in rows:
                predicted = extract_label(row["response"], task_meta["labels"])
                ok = "✓" if predicted == row["reference"] else "✗"
                extracted = "non analysé" if predicted == UNPARSED else predicted
                lines += [
                    f"#### {ok} item {row['index']} ({row['latency_s']}s)",
                    "",
                    f"**Attendu :** {row['reference']} · **Extrait :** {extracted}",
                    "",
                    f"**Réponse brute :**",
                    "",
                    "```",
                    row["response"],
                    "```",
                    "",
                ]
    transcript_path = run_dir / "transcript.md"
    transcript_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return transcript_path
