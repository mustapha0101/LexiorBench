import time

import pytest
from fastapi.testclient import TestClient

from lexior_bench.backends import ModelResponse
from lexior_bench.tasks import load_task, read_tsv
from lexior_bench.web import jobs
from lexior_bench.web.app import app

from conftest import write_task_folder
from test_annotation import FakeProvider
from lexior_bench.annotation.base import AnnotatedItem

client = TestClient(app)


@pytest.fixture
def tmp_tasks(tmp_path, monkeypatch):
    """Point the web app at a temp tasks dir with one toy task."""
    tasks_dir = tmp_path / "tasks"
    write_task_folder(tasks_dir)
    monkeypatch.setattr("lexior_bench.web.app.default_tasks_dir", lambda: tasks_dir)
    return tasks_dir


@pytest.fixture(autouse=True)
def reset_jobs():
    jobs._job = None
    yield
    jobs._job = None


def test_pages_render_in_both_languages():
    for path in ("/tasks", "/run", "/runs", "/annotate", "/tasks/new"):
        for lang, marker in (("fr", "Tâches"), ("en", "Tasks")):
            client.cookies.set("lang", lang)
            response = client.get(path)
            assert response.status_code == 200, path
            assert marker in response.text, (path, lang)
    client.cookies.delete("lang")


def test_static_urls_are_cache_busted():
    response = client.get("/runs")
    assert "/static/app.js?v=" in response.text
    assert "/static/style.css?v=" in response.text


def test_run_page_task_selection_tools():
    """With the large imported registry, the run page must not default to All."""
    response = client.get("/run")
    assert response.status_code == 200
    assert 'id="select-random"' in response.text
    assert 'id="select-first"' in response.text
    # 140+ real tasks → many-mode: All unchecked, boxes enabled for JS preselection
    assert 'data-many="1"' in response.text
    assert '<input type="checkbox" id="all-tasks" checked' not in response.text
    # live item-count estimate: per-task counts + the estimate element
    assert 'id="run-estimate"' in response.text
    assert 'data-count="244"' in response.text  # canada_tax_court_outcomes


def test_lang_toggle_sets_cookie():
    response = client.get("/lang/en?next=/tasks", follow_redirects=False)
    assert response.status_code == 303
    assert response.cookies.get("lang") == "en"
    assert response.headers["location"] == "/tasks"


def test_create_task_via_form(tmp_tasks):
    response = client.post(
        "/tasks",
        data={
            "name": "toy_web_task",
            "reasoning_type": "rule-recall",
            "legal_domain": "civil",
            "metric": "balanced_accuracy",
            "description": "Tâche créée via le web.",
            "labels": "Vrai\nFaux",
            "base_prompt": "{{examples}}\n\nSituation : {{text}}\nRéponse :",
            "train_index": ["0", "1"],
            "train_text": ["A", "B"],
            "train_answer": ["Vrai", "Faux"],
            "test_index": ["0"],
            "test_text": ["C"],
            "test_answer": ["Vrai"],
        },
        follow_redirects=False,
    )
    assert response.status_code == 303
    task = load_task(tmp_tasks / "toy_web_task")
    assert task.labels == ["Vrai", "Faux"]
    assert (tmp_tasks / "toy_web_task" / "README.md").exists()


def test_create_task_invalid_leaves_nothing(tmp_tasks):
    response = client.post(
        "/tasks",
        data={
            "name": "bad_task",
            "reasoning_type": "rule-recall",
            "legal_domain": "civil",
            "metric": "balanced_accuracy",
            "description": "x",
            "labels": "Vrai\nFaux",
            "base_prompt": "no placeholder",
            "train_index": ["0"], "train_text": ["A"], "train_answer": ["Vrai"],
            "test_index": ["0"], "test_text": ["C"], "test_answer": ["Vrai"],
        },
    )
    assert response.status_code == 200  # form re-rendered with error
    assert "Erreur" in response.text or "Error" in response.text
    assert not (tmp_tasks / "bad_task").exists()


def test_create_task_duplicate_name_rejected(tmp_tasks):
    response = client.post(
        "/tasks",
        data={
            "name": "toy_task",  # already exists in tmp_tasks
            "reasoning_type": "rule-recall",
            "legal_domain": "civil",
            "metric": "balanced_accuracy",
            "description": "x",
            "labels": "Vrai\nFaux",
            "base_prompt": "{{text}}",
            "train_index": ["0"], "train_text": ["A"], "train_answer": ["Vrai"],
            "test_index": ["0"], "test_text": ["C"], "test_answer": ["Vrai"],
        },
    )
    assert response.status_code == 200
    assert "already exists" in response.text


def test_edit_items_rewrites_tsv(tmp_tasks):
    response = client.post(
        "/tasks/toy_task/items",
        data={
            "train_index": ["0", "1"],
            "train_text": ["A modifié", "B"],
            "train_answer": ["Faux", "Faux"],
            "test_index": ["0", "1"],
            "test_text": ["C", "D"],
            "test_answer": ["Vrai", "Faux"],
        },
        follow_redirects=False,
    )
    assert response.status_code == 303
    train = read_tsv(tmp_tasks / "toy_task" / "train.tsv")
    assert train[0].text == "A modifié"
    assert train[0].answer == "Faux"


def test_edit_items_bad_answer_rejected(tmp_tasks):
    before = (tmp_tasks / "toy_task" / "train.tsv").read_text(encoding="utf-8")
    response = client.post(
        "/tasks/toy_task/items",
        data={
            "train_index": ["0"], "train_text": ["A"], "train_answer": ["Peut-être"],
            "test_index": ["0"], "test_text": ["C"], "test_answer": ["Vrai"],
        },
    )
    assert response.status_code == 200
    assert "not in labels" in response.text
    assert (tmp_tasks / "toy_task" / "train.tsv").read_text(encoding="utf-8") == before


def test_delete_task(tmp_tasks):
    response = client.post("/tasks/toy_task/delete", follow_redirects=False)
    assert response.status_code == 303
    assert not (tmp_tasks / "toy_task").exists()


class FakeBackend:
    def __init__(self, spec):
        self.spec = spec

    def generate(self, prompt, *, temperature=0.0, max_tokens=512):
        return ModelResponse(text="Vrai", latency_s=0.01)


def test_run_flow_with_fake_backend(tmp_tasks, tmp_path, monkeypatch):
    monkeypatch.setattr("lexior_bench.runner.create_backend", lambda spec: FakeBackend(spec))
    results_dir = tmp_path / "results"
    monkeypatch.setattr("lexior_bench.web.app.RESULTS_DIR", results_dir)
    monkeypatch.setattr(
        "lexior_bench.web.app.discover_tasks",
        lambda: [load_task(tmp_tasks / "toy_task")],
    )

    response = client.post(
        "/api/run",
        json={"models": ["ollama:fake"], "tasks": ["toy_task"], "limit": None, "max_tokens": 64},
    )
    assert response.status_code == 200

    for _ in range(100):
        status = client.get("/api/run/status").json()
        if status["status"] != "running":
            break
        time.sleep(0.05)
    assert status["status"] == "done", status
    assert status["done"] == status["total"] == 2  # toy_task has 2 test items
    run_id = status["run_id"]
    assert (results_dir / run_id / "scores.json").exists()
    assert (results_dir / run_id / "report.md").exists()

    page = client.get(f"/runs/{run_id}")
    assert page.status_code == 200
    assert "ollama:fake" in page.text


def test_run_busy_returns_409(tmp_tasks, tmp_path, monkeypatch):
    import threading

    release = threading.Event()

    class SlowBackend(FakeBackend):
        def generate(self, prompt, **kwargs):
            release.wait(timeout=5)
            return ModelResponse(text="Vrai", latency_s=0.01)

    monkeypatch.setattr("lexior_bench.runner.create_backend", lambda spec: SlowBackend(spec))
    monkeypatch.setattr("lexior_bench.web.app.RESULTS_DIR", tmp_path / "results")
    monkeypatch.setattr(
        "lexior_bench.web.app.discover_tasks",
        lambda: [load_task(tmp_tasks / "toy_task")],
    )
    body = {"models": ["ollama:fake"], "tasks": ["toy_task"]}
    assert client.post("/api/run", json=body).status_code == 200
    assert client.post("/api/run", json=body).status_code == 409
    release.set()


def test_run_validation_errors():
    assert client.post("/api/run", json={"models": [], "tasks": ["x"]}).status_code == 400
    assert client.post("/api/run", json={"models": ["m"], "tasks": []}).status_code == 400
    assert client.post("/api/run", json={"models": ["m"], "tasks": ["nope"]}).status_code == 400


def test_annotate_endpoints_with_fake_provider(tmp_tasks, monkeypatch):
    fake = FakeProvider(
        [AnnotatedItem(split="train", index="0", answer_ok="Incorrecte",
                       corrected_answer="Faux", item_status="Validé")]
    )
    monkeypatch.setattr("lexior_bench.web.app.get_provider", lambda name: fake)

    push = client.post("/api/annotate/push", json={"provider": "argilla", "task": "toy_task"})
    assert push.status_code == 200
    assert push.json()["pushed"] == 4

    preview = client.post(
        "/api/annotate/pull", json={"provider": "argilla", "task": "toy_task", "dry_run": True}
    )
    assert preview.status_code == 200
    data = preview.json()
    assert data["validated"] == 1
    assert data["changes"][0]["action"] == "corrected"
    # dry run leaves the TSV alone
    assert read_tsv(tmp_tasks / "toy_task" / "train.tsv")[0].answer == "Vrai"

    apply = client.post(
        "/api/annotate/pull", json={"provider": "argilla", "task": "toy_task", "dry_run": False}
    )
    assert apply.status_code == 200
    assert read_tsv(tmp_tasks / "toy_task" / "train.tsv")[0].answer == "Faux"


def test_annotate_provider_error_is_400(tmp_tasks, monkeypatch):
    def boom(name):
        raise ValueError("LABEL_STUDIO_API_KEY is not set")

    monkeypatch.setattr("lexior_bench.web.app.get_provider", boom)
    response = client.post("/api/annotate/push", json={"provider": "labelstudio", "task": "toy_task"})
    assert response.status_code == 400
    assert "LABEL_STUDIO_API_KEY" in response.json()["error"]
