import json

from lexior_bench.evaluation import (
    UNPARSED,
    balanced_accuracy,
    evaluate_run,
    exact_match,
    extract_label,
    normalize,
)

LABELS_RESP = [
    "Fait personnel",
    "Fait d'autrui",
    "Fait des biens",
    "Aucune responsabilité extracontractuelle",
]


def test_normalize_accents_case_punctuation():
    assert normalize("  Réponse : VRAI!  ") == "reponse vrai"
    assert normalize("Fait d'autrui") == "fait d autrui"


def test_extract_label_first_line():
    assert extract_label("Vrai", ["Vrai", "Faux"]) == "Vrai"
    assert extract_label("vrai.", ["Vrai", "Faux"]) == "Vrai"
    assert extract_label("FAUX\nParce que l'article 2925...", ["Vrai", "Faux"]) == "Faux"


def test_extract_label_substring_word_boundary():
    text = "Selon moi, la réponse est : Fait des biens (art. 1466 C.c.Q.)."
    assert extract_label(text, LABELS_RESP) == "Fait des biens"
    # "Âge" must not match inside "dommage"
    assert extract_label("Il y a un dommage.", ["Âge", "Religion"]) == UNPARSED


def test_extract_label_earliest_occurrence_wins():
    text = "Réponse : Oui. (et non pas Non.)"
    assert extract_label(text, ["Oui", "Non"]) == "Oui"


def test_extract_label_unparsed_and_errors():
    assert extract_label("Je ne sais pas.", ["Vrai", "Faux"]) == UNPARSED
    assert extract_label("<ERROR: timeout>", ["Vrai", "Faux"]) == UNPARSED


def test_exact_match():
    assert exact_match(["A", "B"], ["A", "C"]) == 0.5
    assert exact_match([], []) == 0.0


def test_balanced_accuracy_weighs_classes_equally():
    refs = ["Oui"] * 8 + ["Non"] * 2
    preds = ["Oui"] * 8 + ["Oui"] * 2  # all-Oui predictor
    assert exact_match(refs, preds) == 0.8
    assert balanced_accuracy(refs, preds) == 0.5  # (1.0 + 0.0) / 2


def test_evaluate_run_writes_scores(tmp_path):
    run_dir = tmp_path / "20260611-000000"
    run_dir.mkdir()
    run_meta = {
        "run_id": "20260611-000000",
        "created_at": "2026-06-11T00:00:00",
        "models": ["ollama:toy"],
        "tasks": {
            "toy_task": {
                "version": 1,
                "reasoning_type": "rule-recall",
                "legal_domain": "civil",
                "metric": "balanced_accuracy",
                "labels": ["Vrai", "Faux"],
            }
        },
        "params": {"limit": None, "temperature": 0.0, "max_tokens": 512},
    }
    records = [
        {"model": "ollama:toy", "task": "toy_task", "reasoning_type": "rule-recall",
         "index": "0", "prompt": "p", "reference": "Vrai", "response": "Vrai", "latency_s": 0.1},
        {"model": "ollama:toy", "task": "toy_task", "reasoning_type": "rule-recall",
         "index": "1", "prompt": "p", "reference": "Faux", "response": "réponse : vrai", "latency_s": 0.1},
        {"model": "ollama:toy", "task": "toy_task", "reasoning_type": "rule-recall",
         "index": "2", "prompt": "p", "reference": "Faux", "response": "<ERROR: boom>", "latency_s": 0.0},
    ]
    (run_dir / "run.json").write_text(json.dumps(run_meta), encoding="utf-8")
    (run_dir / "results.json").write_text(json.dumps(records), encoding="utf-8")

    scores = evaluate_run(run_dir)
    task_scores = scores["models"]["ollama:toy"]["tasks"]["toy_task"]
    assert task_scores["n"] == 3
    assert task_scores["errors"] == 1
    assert task_scores["unparsed_rate"] == round(1 / 3, 4)
    # recalls: Vrai 1/1, Faux 0/2 → balanced accuracy 0.5
    assert task_scores["score"] == 0.5
    assert scores["models"]["ollama:toy"]["by_legal_domain"] == {"civil": 0.5}
    assert (run_dir / "scores.json").exists()
