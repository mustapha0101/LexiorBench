import pytest

from lexior_bench import legalbench_import as lb
from lexior_bench.tasks import Example, TaskError, load_task
from lexior_bench.web.taskforms import create_task

LEGALBENCH_TSV = (
    "index\ttext\tanswer\n"
    '0\t"The appeal is allowed.\nSigned at Ottawa.\n"\tallowed\n'
    '1\t"The appeal is dismissed,\twith costs."\tdismissed\n'
)

README = """# canada_tax_court_outcomes

### Classify whether an excerpt includes the outcome of the appeal.
---

**Source**: Sean Rehaag

**License**: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

**Legal reasoning type**: Rhetorical-analysis
"""


def test_parse_legalbench_tsv_quoted_multiline():
    examples = lb.parse_legalbench_tsv(LEGALBENCH_TSV)
    assert len(examples) == 2
    assert examples[0].text == "The appeal is allowed. Signed at Ottawa."
    assert examples[1].text == "The appeal is dismissed, with costs."
    assert "\n" not in examples[0].text and "\t" not in examples[1].text


def test_parse_readme_metadata():
    meta = lb.parse_readme(README)
    assert meta["description"].startswith("Classify whether")
    assert meta["source"] == "Sean Rehaag"
    assert "CC BY-NC 4.0" in meta["license"]
    assert meta["reasoning_type"] == "rhetorical-understanding"


def test_build_draft_url_validation():
    with pytest.raises(TaskError, match="unsupported URL"):
        lb.build_draft("https://example.com/not-github")


def test_sanitize_name_handles_legalbench_charset():
    assert lb.sanitize_name("cuad_affiliate_license-licensee") == "cuad_affiliate_license_licensee"
    assert lb.sanitize_name("privacy_user_access,_edit_and_deletion") == "privacy_user_access_edit_and_deletion"
    assert lb.sanitize_name("maud_initial_matching_rights_period_(cor)") == "maud_initial_matching_rights_period_cor"
    assert lb.sanitize_name("hearsay") == "hearsay"


def test_classification_blocker():
    def draft_with(**overrides):
        base = dict(
            name="x", url="u", base_prompt="{{text}}", description="d",
            source="s", license="l", suggested_reasoning_type="interpretation",
            labels=["a", "b"], train=[], test=[], task_type="2-way classification",
        )
        base.update(overrides)
        return lb.ImportDraft(**base)

    assert lb.classification_blocker(draft_with()) is None
    assert "not a classification task" in lb.classification_blocker(
        draft_with(task_type="extraction")
    )
    assert "open-ended" in lb.classification_blocker(
        draft_with(labels=[str(i) for i in range(30)])
    )
    assert "reasoning type" in lb.classification_blocker(
        draft_with(suggested_reasoning_type=None)
    )


def test_list_task_folders(monkeypatch):
    class FakeResponse:
        status_code = 200

        @staticmethod
        def raise_for_status():
            pass

        @staticmethod
        def json():
            return [
                {"name": "hearsay", "type": "dir"},
                {"name": "README.md", "type": "file"},
                {"name": "abercrombie", "type": "dir"},
            ]

    monkeypatch.setattr(lb, "_get", lambda url: FakeResponse())
    folders = lb.list_task_folders("https://github.com/o/r/tree/main/tasks")
    assert folders == [
        ("hearsay", "https://github.com/o/r/tree/main/tasks/hearsay"),
        ("abercrombie", "https://github.com/o/r/tree/main/tasks/abercrombie"),
    ]


@pytest.fixture
def fake_repo(monkeypatch):
    """Simulate the GitHub raw files and the HF datasets-server."""
    files = {
        "base_prompt.txt": "INSTRUCTIONS: classify.\nOptions: allowed, dismissed\n\nEXCERPT: {{text}}\nOUTCOME:",
        "README.md": README,
        "train.tsv": LEGALBENCH_TSV,
        "test.tsv": None,  # not in the repo — comes from HF
    }

    def fake_fetch_text(url):
        return files.get(url.rsplit("/", 1)[-1])

    hf_rows = [
        Example(index=str(i), text=f"Excerpt {i}.", answer="allowed" if i % 2 else "other")
        for i in range(6)
    ]
    monkeypatch.setattr(lb, "_fetch_text", fake_fetch_text)
    monkeypatch.setattr(lb, "fetch_hf_split", lambda name, split: list(hf_rows))
    return files


def test_build_draft_with_hf_test_split(fake_repo):
    draft = lb.build_draft("https://github.com/owner/repo/tree/main/tasks/canada_tax_court_outcomes")
    assert draft.name == "canada_tax_court_outcomes"
    assert draft.suggested_reasoning_type == "rhetorical-understanding"
    assert draft.test_from_hf
    assert len(draft.train) == 2
    assert len(draft.test) == 6
    assert draft.labels == ["allowed", "dismissed", "other"]
    assert "Sean Rehaag" in draft.source


def test_build_draft_borrows_train_when_missing(fake_repo):
    fake_repo["train.tsv"] = None
    draft = lb.build_draft("https://github.com/owner/repo/tree/main/tasks/canada_tax_court_outcomes")
    assert len(draft.train) == 4
    assert len(draft.test) == 2
    assert any("train" in w for w in draft.warnings)


def test_build_draft_requires_base_prompt(fake_repo):
    fake_repo["base_prompt.txt"] = None
    with pytest.raises(TaskError, match="base_prompt.txt not found"):
        lb.build_draft("https://github.com/owner/repo/tree/main/tasks/x")


def test_imported_task_folder_carries_provenance(fake_repo, tmp_path):
    draft = lb.build_draft("https://github.com/owner/repo/tree/main/tasks/canada_tax_court_outcomes")
    task = create_task(
        tmp_path,
        name=draft.name,
        reasoning_type=draft.suggested_reasoning_type,
        legal_domain="public",
        metric="balanced_accuracy",
        description=draft.description,
        labels=draft.labels,
        base_prompt=draft.base_prompt,
        train=draft.train,
        test=draft.test,
        language="en",
        extra_meta={"source": draft.source, "license": draft.license, "imported_from": draft.url},
        readme=lb.imported_readme(
            draft, reasoning_type=draft.suggested_reasoning_type,
            legal_domain="public", language="en",
        ),
    )
    assert task.language == "en"
    readme = (task.path / "README.md").read_text(encoding="utf-8")
    assert "CC BY-NC 4.0" in readme and "Sean Rehaag" in readme
    yaml_text = (task.path / "task.yaml").read_text(encoding="utf-8")
    assert "imported_from" in yaml_text
    load_task(task.path)  # still fully valid for the runner


def test_web_import_flow(fake_repo, tmp_path, monkeypatch):
    from fastapi.testclient import TestClient
    from lexior_bench.web.app import app

    tasks_dir = tmp_path / "tasks"
    tasks_dir.mkdir()
    monkeypatch.setattr("lexior_bench.web.app.default_tasks_dir", lambda: tasks_dir)
    client = TestClient(app)

    assert client.get("/tasks/import").status_code == 200

    url = "https://github.com/owner/repo/tree/main/tasks/canada_tax_court_outcomes"
    preview = client.post("/tasks/import", data={"url": url})
    assert preview.status_code == 200
    assert "canada_tax_court_outcomes" in preview.text
    assert "CC BY-NC 4.0" in preview.text

    confirm = client.post(
        "/tasks/import/confirm",
        data={
            "url": url,
            "name": "canada_tax_court_outcomes",
            "reasoning_type": "rhetorical-understanding",
            "legal_domain": "public",
            "metric": "balanced_accuracy",
            "language": "en",
        },
        follow_redirects=False,
    )
    assert confirm.status_code == 303
    task = load_task(tasks_dir / "canada_tax_court_outcomes")
    assert task.labels == ["allowed", "dismissed", "other"]


def test_web_import_bad_url_shows_error():
    from fastapi.testclient import TestClient
    from lexior_bench.web.app import app

    client = TestClient(app)
    response = client.post("/tasks/import", data={"url": "https://example.com/x"})
    assert response.status_code == 200
    assert "unsupported URL" in response.text
