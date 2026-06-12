"""FastAPI application: pages and JSON API for the local web UI."""

from __future__ import annotations

import json
import os
import shutil
from pathlib import Path

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from ..annotation import get_provider
from ..annotation.base import apply_annotations, task_to_items
from ..backends import DEFAULT_OLLAMA_BASE_URL
from ..evaluation import UNPARSED, evaluate_run, extract_label
from ..tasks import (
    LEGAL_DOMAINS,
    METRICS,
    REASONING_TYPES,
    TaskError,
    default_tasks_dir,
    discover_tasks,
    load_task,
    resolve_task_names,
)
from . import jobs, taskforms
from .i18n import resolve_lang, translator

WEB_DIR = Path(__file__).parent
RESULTS_DIR = Path("results")

app = FastAPI(title="Lexior Bench", docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory=WEB_DIR / "static"), name="static")
templates = Jinja2Templates(directory=WEB_DIR / "templates")


def render(request: Request, template: str, **context) -> HTMLResponse:
    lang = resolve_lang(request.cookies.get("lang"))
    context.update(request=request, t=translator(lang), lang=lang)
    return templates.TemplateResponse(request, template, context)


@app.get("/", include_in_schema=False)
def index():
    return RedirectResponse("/runs")


@app.get("/lang/{code}", include_in_schema=False)
def set_lang(code: str, next: str = "/"):
    response = RedirectResponse(next if next.startswith("/") else "/", status_code=303)
    response.set_cookie("lang", resolve_lang(code), max_age=365 * 24 * 3600)
    return response


# --- tasks -----------------------------------------------------------------


@app.get("/tasks", response_class=HTMLResponse)
def tasks_page(request: Request):
    return render(request, "tasks.html", tasks=discover_tasks())


@app.get("/tasks/new", response_class=HTMLResponse)
def task_new_page(request: Request):
    return render(
        request,
        "task_new.html",
        reasoning_types=REASONING_TYPES,
        legal_domains=LEGAL_DOMAINS,
        metrics=[m for m in METRICS if m != "manual"],
        default_prompt=taskforms.default_prompt([]),
        form={},
        error=None,
    )


@app.post("/tasks", response_class=HTMLResponse)
async def task_create(request: Request):
    form = await request.form()
    labels = [line.strip() for line in form.get("labels", "").splitlines() if line.strip()]
    payload = dict(
        name=form.get("name", "").strip(),
        reasoning_type=form.get("reasoning_type", ""),
        legal_domain=form.get("legal_domain", ""),
        metric=form.get("metric", ""),
        description=form.get("description", ""),
        labels=labels,
        base_prompt=form.get("base_prompt", ""),
        train=taskforms.parse_items(
            form.getlist("train_index"), form.getlist("train_text"), form.getlist("train_answer")
        ),
        test=taskforms.parse_items(
            form.getlist("test_index"), form.getlist("test_text"), form.getlist("test_answer")
        ),
    )
    try:
        task = taskforms.create_task(default_tasks_dir(), **payload)
    except TaskError as e:
        return render(
            request,
            "task_new.html",
            reasoning_types=REASONING_TYPES,
            legal_domains=LEGAL_DOMAINS,
            metrics=[m for m in METRICS if m != "manual"],
            default_prompt=payload["base_prompt"] or taskforms.default_prompt(labels),
            form=form,
            error=str(e),
        )
    return RedirectResponse(f"/tasks/{task.name}", status_code=303)


# NOTE: fixed /tasks/import routes must be registered before /tasks/{name}


@app.get("/tasks/import", response_class=HTMLResponse)
def task_import_page(request: Request):
    return render(request, "task_import.html", draft=None, form={}, error=None,
                  reasoning_types=REASONING_TYPES, legal_domains=LEGAL_DOMAINS,
                  metrics=[m for m in METRICS if m != "manual"])


@app.post("/tasks/import", response_class=HTMLResponse)
async def task_import_preview(request: Request):
    from ..legalbench_import import build_draft

    form = await request.form()
    try:
        draft = build_draft(form.get("url", ""))
        error = None
    except Exception as e:
        draft, error = None, str(e)
    return render(request, "task_import.html", draft=draft, form=form, error=error,
                  reasoning_types=REASONING_TYPES, legal_domains=LEGAL_DOMAINS,
                  metrics=[m for m in METRICS if m != "manual"])


@app.post("/tasks/import/confirm", response_class=HTMLResponse)
async def task_import_confirm(request: Request):
    from ..legalbench_import import build_draft, imported_readme

    form = await request.form()
    try:
        draft = build_draft(form.get("url", ""))
        reasoning_type = form.get("reasoning_type", "")
        legal_domain = form.get("legal_domain", "")
        language = form.get("language", "en").strip() or "en"
        task = taskforms.create_task(
            default_tasks_dir(),
            name=form.get("name", "").strip() or draft.name,
            reasoning_type=reasoning_type,
            legal_domain=legal_domain,
            metric=form.get("metric", ""),
            description=draft.description,
            labels=draft.labels,
            base_prompt=draft.base_prompt,
            train=draft.train,
            test=draft.test,
            language=language,
            extra_meta={
                "source": draft.source,
                "license": draft.license,
                "imported_from": draft.url,
            },
            readme=imported_readme(
                draft, reasoning_type=reasoning_type, legal_domain=legal_domain, language=language
            ),
        )
    except Exception as e:
        return render(request, "task_import.html", draft=None, form=form, error=str(e),
                      reasoning_types=REASONING_TYPES, legal_domains=LEGAL_DOMAINS,
                      metrics=[m for m in METRICS if m != "manual"])
    return RedirectResponse(f"/tasks/{task.name}", status_code=303)


@app.get("/tasks/{name}", response_class=HTMLResponse)
def task_detail(request: Request, name: str, saved: int = 0):
    task = load_task(default_tasks_dir() / name)
    return render(request, "task_detail.html", task=task, saved=saved, error=None)


@app.post("/tasks/{name}/items", response_class=HTMLResponse)
async def task_save_items(request: Request, name: str):
    task = load_task(default_tasks_dir() / name)
    form = await request.form()
    try:
        taskforms.save_items(
            task,
            train=taskforms.parse_items(
                form.getlist("train_index"), form.getlist("train_text"), form.getlist("train_answer")
            ),
            test=taskforms.parse_items(
                form.getlist("test_index"), form.getlist("test_text"), form.getlist("test_answer")
            ),
        )
    except TaskError as e:
        return render(request, "task_detail.html", task=task, saved=0, error=str(e))
    return RedirectResponse(f"/tasks/{name}?saved=1", status_code=303)


@app.post("/tasks/{name}/delete", include_in_schema=False)
def task_delete(name: str):
    folder = default_tasks_dir() / name
    load_task(folder)  # 500s on anything that isn't a valid task folder
    shutil.rmtree(folder)
    return RedirectResponse("/tasks", status_code=303)


# --- run -------------------------------------------------------------------


def _ollama_models() -> list[str] | None:
    base = os.environ.get("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL).rstrip("/")
    try:
        response = httpx.get(f"{base}/api/tags", timeout=2.0)
        response.raise_for_status()
        return sorted(model["name"].removesuffix(":latest") for model in response.json()["models"])
    except Exception:
        return None


@app.get("/run", response_class=HTMLResponse)
def run_page(request: Request):
    return render(
        request,
        "run.html",
        ollama_models=_ollama_models(),
        tasks=discover_tasks(),
        reasoning_types=REASONING_TYPES,
        openai_key=bool(os.environ.get("OPENAI_API_KEY")),
        anthropic_key=bool(os.environ.get("ANTHROPIC_API_KEY")),
        job=jobs.status(),
    )


@app.post("/api/run")
async def api_run_start(request: Request):
    body = await request.json()
    models = [m.strip() for m in body.get("models", []) if m.strip()]
    task_names = [t.strip() for t in body.get("tasks", []) if t.strip()]
    if not models:
        return JSONResponse({"error": "no_models"}, status_code=400)
    if not task_names:
        return JSONResponse({"error": "no_tasks"}, status_code=400)
    try:
        tasks = resolve_task_names(",".join(task_names), discover_tasks())
        limit = int(body["limit"]) if body.get("limit") else None
        max_tokens = int(body.get("max_tokens") or 512)
    except (TaskError, ValueError) as e:
        return JSONResponse({"error": str(e)}, status_code=400)
    job = jobs.start(models, tasks, limit=limit, max_tokens=max_tokens, results_dir=RESULTS_DIR)
    if job is None:
        return JSONResponse({"error": "busy"}, status_code=409)
    return job.as_dict()


@app.get("/api/run/status")
def api_run_status():
    job = jobs.status()
    return job.as_dict() if job else {"status": "idle"}


# --- results ---------------------------------------------------------------


def _load_json(path: Path) -> dict | list | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


@app.get("/runs", response_class=HTMLResponse)
def runs_page(request: Request):
    runs = []
    if RESULTS_DIR.is_dir():
        for run_dir in sorted(RESULTS_DIR.iterdir(), reverse=True):
            meta = _load_json(run_dir / "run.json")
            if not meta:
                continue
            scores = _load_json(run_dir / "scores.json") or {"models": {}}
            means = {
                model: data.get("mean") for model, data in scores["models"].items()
            }
            runs.append({"meta": meta, "means": means})
    return render(request, "runs.html", runs=runs)


@app.get("/runs/{run_id}", response_class=HTMLResponse)
def run_detail(request: Request, run_id: str):
    run_dir = RESULTS_DIR / run_id
    meta = _load_json(run_dir / "run.json")
    if not meta:
        return RedirectResponse("/runs")
    scores = _load_json(run_dir / "scores.json")
    if scores is None:
        scores = evaluate_run(run_dir)
    records = _load_json(run_dir / "results.json") or []

    transcript: dict[str, dict[str, list[dict]]] = {}
    for record in records:
        task_meta = meta["tasks"].get(record["task"], {})
        predicted = extract_label(record["response"], task_meta.get("labels", []))
        transcript.setdefault(record["model"], {}).setdefault(record["task"], []).append(
            {
                **record,
                "predicted": predicted,
                "unparsed": predicted == UNPARSED,
                "ok": predicted == record["reference"],
            }
        )
    return render(
        request,
        "run_detail.html",
        meta=meta,
        scores=scores,
        transcript=transcript,
        task_names=list(meta["tasks"]),
    )


# --- annotation ------------------------------------------------------------


@app.get("/annotate", response_class=HTMLResponse)
def annotate_page(request: Request):
    return render(
        request,
        "annotate.html",
        tasks=discover_tasks(),
        default_provider=os.environ.get("LEXIOR_ANNOTATION_PROVIDER", "argilla"),
    )


def _pull_summary(result) -> dict:
    return {
        "annotated": result.annotated,
        "validated": result.validated,
        "changes": [
            {"split": c.split, "index": c.index, "action": c.action, "old": c.old, "new": c.new}
            for c in result.changes
        ],
    }


@app.post("/api/annotate/push")
async def api_annotate_push(request: Request):
    body = await request.json()
    try:
        provider = get_provider(body["provider"])
        task = load_task(default_tasks_dir() / body["task"])
        provider.push_task(task, include_test=not body.get("train_only", False))
        return {"pushed": len(task_to_items(task, include_test=not body.get("train_only", False)))}
    except Exception as e:
        return JSONResponse({"error": f"{type(e).__name__}: {e}"}, status_code=400)


@app.post("/api/annotate/pull")
async def api_annotate_pull(request: Request):
    body = await request.json()
    try:
        provider = get_provider(body["provider"])
        task = load_task(default_tasks_dir() / body["task"])
        if body.get("dry_run", True):
            result = apply_annotations(task, provider.fetch_annotations(task))
        else:
            result = provider.pull_task(task, dry_run=False)
        return _pull_summary(result)
    except Exception as e:
        return JSONResponse({"error": f"{type(e).__name__}: {e}"}, status_code=400)
