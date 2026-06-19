"""
Fix two issues introduced by adapt_tasks.py:
1. contract_nli tasks: were set to 3-class NLI — should be binary (Oui/Non).
2. All remaining "to adapt" tasks: TSV files still have English Yes/No labels
   but task.yaml now expects Oui/Non — fix by relabelling the TSV data.
Also: fix contract_nli base_prompt.txt to be binary.
"""
import yaml
import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TASKS_DIR = ROOT / "tasks"

CONTRACT_NLI_TASKS = [
    "contract_nli_confidentiality_of_agreement",
    "contract_nli_explicit_identification",
    "contract_nli_inclusion_of_verbally_conveyed_information",
    "contract_nli_limited_use",
    "contract_nli_no_licensing",
    "contract_nli_notice_on_compelled_disclosure",
    "contract_nli_permissible_acquirement_of_similar_information",
    "contract_nli_permissible_copy",
    "contract_nli_permissible_development_of_similar_information",
    "contract_nli_permissible_post_agreement_possession",
    "contract_nli_return_of_confidential_information",
    "contract_nli_sharing_with_employees",
    "contract_nli_sharing_with_third_parties",
    "contract_nli_survival_of_obligations",
]

CONTRACT_NLI_DESCRIPTIONS = {
    "contract_nli_confidentiality_of_agreement":               "la confidentialité de l'existence même de l'accord",
    "contract_nli_explicit_identification":                     "l'identification explicite des informations confidentielles",
    "contract_nli_inclusion_of_verbally_conveyed_information":  "l'inclusion des informations transmises verbalement dans la portée de confidentialité",
    "contract_nli_limited_use":                                 "la restriction de l'utilisation des informations confidentielles",
    "contract_nli_no_licensing":                                "l'absence de licence implicite sur les informations partagées",
    "contract_nli_notice_on_compelled_disclosure":              "l'obligation de notification en cas de divulgation forcée par autorité légale",
    "contract_nli_permissible_acquirement_of_similar_information": "la permission d'acquérir des informations similaires de manière indépendante",
    "contract_nli_permissible_copy":                            "la permission de reproduire les informations confidentielles",
    "contract_nli_permissible_development_of_similar_information": "la permission de développer des informations similaires de manière indépendante",
    "contract_nli_permissible_post_agreement_possession":       "la permission de conserver des informations après la fin de l'accord",
    "contract_nli_return_of_confidential_information":          "l'obligation de restituer ou détruire les informations confidentielles",
    "contract_nli_sharing_with_employees":                      "la permission de partager des informations confidentielles avec les employés",
    "contract_nli_sharing_with_third_parties":                  "la permission de partager des informations confidentielles avec des tiers",
    "contract_nli_survival_of_obligations":                     "la survie des obligations de confidentialité après la résiliation de l'accord",
}


def fix_contract_nli():
    fixed = 0
    for task_name in CONTRACT_NLI_TASKS:
        task_dir = TASKS_DIR / task_name
        yaml_file = task_dir / "task.yaml"
        prompt_file = task_dir / "base_prompt.txt"

        if not yaml_file.exists():
            print(f"  SKIP {task_name} — not found")
            continue

        # Fix task.yaml: binary labels
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        data["labels"] = ["Non", "Oui"]
        data["description"] = (
            f"Identifier si la clause d'un accord de confidentialité québécois ou canadien "
            f"traite {CONTRACT_NLI_DESCRIPTIONS[task_name]} (Oui/Non)."
        )
        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

        # Fix base_prompt.txt: binary
        clause_desc = CONTRACT_NLI_DESCRIPTIONS[task_name]
        prompt = (
            f"Vous êtes un juriste spécialisé en droit des contrats québécois et canadien.\n"
            f"La clause ci-dessous traite-t-elle {clause_desc}?\n\n"
            f"Répondez uniquement par : Oui ou Non.\n\n"
            f"{{{{examples}}}}\n\n"
            f"Clause : {{{{text}}}}\n"
            f"Réponse :"
        )
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt)

        fixed += 1

    print(f"contract_nli: fixed {fixed} task.yaml + base_prompt.txt files")


def relabel_tsv(path: Path) -> int:
    """Replace Yes→Oui and No→Non in the answer column. Returns number of rows changed."""
    if not path.exists():
        return 0
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    rows = list(csv.reader(io.StringIO(content), delimiter="\t"))
    if not rows:
        return 0

    header = rows[0]
    try:
        answer_col = header.index("answer")
    except ValueError:
        return 0

    changed = 0
    new_rows = [header]
    for row in rows[1:]:
        if len(row) > answer_col:
            old = row[answer_col]
            if old == "Yes":
                row[answer_col] = "Oui"
                changed += 1
            elif old == "No":
                row[answer_col] = "Non"
                changed += 1
        new_rows.append(row)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerows(new_rows)

    return changed


def relabel_all_remaining():
    """
    For every task that has labels: [Non, Oui] in task.yaml,
    convert TSV answer column from Yes/No to Oui/Non.
    Skip tasks we already wrote fresh French data for.
    """
    ALREADY_DONE = {
        "learned_hands_housing", "learned_hands_employment", "learned_hands_family",
        "learned_hands_immigration", "learned_hands_consumer", "overruling",
        "definition_classification", "supply_chain_disclosure_best_practice_audits",
        "supply_chain_disclosure_disclosed_audits", "citation_prediction_classification",
        "privacy_policy_entailment", "legal_reasoning_causality",
        # Canadian tasks that were already correct
        "canada_tax_court_outcomes", "canadian_employment_insurance_recall",
        "canadian_human_rights_act_recall", "canadian_labour_code_recall",
        "canadian_privacy_act_recall", "civil_issue_spotting_responsabilite",
        "civil_rule_application_vices_caches", "civil_rule_conclusion_contrats",
        "civil_rule_recall_ccq", "proa", "public_interpretation_charte",
        "public_rhetorical_jugement",
    }

    total_tasks = 0
    total_rows = 0
    for task_dir in sorted(TASKS_DIR.iterdir()):
        if not task_dir.is_dir():
            continue
        task_name = task_dir.name
        if task_name in ALREADY_DONE:
            continue

        yaml_file = task_dir / "task.yaml"
        if not yaml_file.exists():
            continue
        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        labels = data.get("labels", [])
        if "Oui" not in labels and "Non" not in labels:
            continue  # not a task we've adapted to French labels

        changed_train = relabel_tsv(task_dir / "train.tsv")
        changed_test  = relabel_tsv(task_dir / "test.tsv")
        if changed_train + changed_test > 0:
            total_tasks += 1
            total_rows += changed_train + changed_test
            print(f"  {task_name}: {changed_train} train + {changed_test} test rows relabelled")

    print(f"\nRelabelled {total_rows} rows across {total_tasks} tasks.")


if __name__ == "__main__":
    print("=== Fixing contract_nli labels ===")
    fix_contract_nli()
    print("\n=== Relabelling remaining TSV files (Yes/No -> Oui/Non) ===")
    relabel_all_remaining()