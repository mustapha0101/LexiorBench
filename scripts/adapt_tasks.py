"""
Batch adaptation of LexiorBench v2 tasks from US LegalBench to QC/Canadian context.
Updates: task.yaml, base_prompt.txt for all "to adapt" tasks.
"""
import yaml
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TASKS_DIR = ROOT / "tasks"

# ─────────────────────────────────────────────────────────────────────────────
# 1. TASK.YAML UPDATES
# ─────────────────────────────────────────────────────────────────────────────

YAML_UPDATES: dict[str, dict] = {
    "overruling": {
        "description": "Identifier si cette phrase extraite d'un jugement canadien (CSC, Cour d'appel, Cour fédérale) constitue un revirement jurisprudentiel infirmant un précédent (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Non", "Oui"],
    },
    "definition_classification": {
        "description": "Identifier si cette phrase extraite d'une décision judiciaire canadienne définit un terme juridique (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Non", "Oui"],
    },
    "legal_reasoning_causality": {
        "description": "Identifier si cet extrait d'une décision judiciaire canadienne s'appuie sur des preuves statistiques ou épidémiologiques pour établir la causalité (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Federal CA",
        "labels": ["Non", "Oui"],
    },
    "citation_prediction_classification": {
        "description": "Vérifier si la référence bibliographique fournie correspond correctement à la citation juridique selon le Guide McGill (10e éd.) (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Non", "Oui"],
    },
    "contract_qa": {
        "description": "Identifier le type de clause contractuelle présente dans cet extrait d'un contrat commercial québécois ou canadien.",
        "language": "fr",
        "target_jurisdiction": "Both",
    },
    "privacy_policy_entailment": {
        "description": "Identifier si cet extrait de politique de confidentialité implique que l'organisation effectue l'action décrite, conformément à la Loi 25 (QC) et à la LPRPDE (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Non", "Oui"],
    },
    "privacy_policy_qa": {
        "description": "Répondre à une question sur le contenu d'une politique de confidentialité d'une organisation québécoise ou canadienne (Loi 25 / LPRPDE).",
        "language": "fr",
        "target_jurisdiction": "Both",
    },
    "unfair_tos": {
        "description": "Classifier cette clause de conditions générales d'utilisation selon les catégories d'abus prévues par la Loi sur la protection du consommateur (LPC) du Québec.",
        "language": "fr",
        "target_jurisdiction": "QC",
    },
}

# learned_hands group
LEARNED_HANDS_DOMAINS = {
    "benefits":          ("prestations sociales, aide sociale et services gouvernementaux", "QC"),
    "business":          ("droit des affaires, entreprises et sociétés", "Both"),
    "consumer":          ("protection du consommateur sous la LPC québécoise", "QC"),
    "courts":            ("procédure judiciaire et accès à la justice", "Both"),
    "crime":             ("droit criminel et pénal (Code criminel)", "Both"),
    "divorce":           ("divorce, séparation et pension alimentaire", "QC"),
    "domestic_violence": ("violence conjugale et protection des victimes", "QC"),
    "education":         ("droit scolaire et éducation", "QC"),
    "employment":        ("droit du travail et emploi (LNT / Code canadien du travail)", "Both"),
    "estates":           ("successions, testaments et liquidation de succession (CCQ)", "QC"),
    "family":            ("droit de la famille — garde, autorité parentale, adoption (CCQ)", "QC"),
    "health":            ("droit de la santé et soins médicaux", "QC"),
    "housing":           ("bail résidentiel et logement (CCQ arts. 1851–2000)", "QC"),
    "immigration":       ("immigration, visa et statut de réfugié (LIPR)", "Federal CA"),
    "torts":             ("responsabilité civile extracontractuelle (art. 1457 CCQ)", "QC"),
    "traffic":           ("infractions au Code de la sécurité routière du Québec", "QC"),
}
for domain, (domain_fr, jurisdiction) in LEARNED_HANDS_DOMAINS.items():
    YAML_UPDATES[f"learned_hands_{domain}"] = {
        "description": f"Identifier si ce scénario soulève une question légale liée à {domain_fr} (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": jurisdiction,
        "labels": ["Non", "Oui"],
    }

# contract_nli group
CONTRACT_NLI_CLAUSES = {
    "confidentiality_of_agreement":               "la confidentialité de l'existence même de l'accord",
    "explicit_identification":                     "l'identification explicite des informations confidentielles",
    "inclusion_of_verbally_conveyed_information":  "l'inclusion des informations transmises verbalement dans la portée de confidentialité",
    "limited_use":                                 "la restriction de l'utilisation des informations confidentielles",
    "no_licensing":                                "l'absence de licence implicite sur les informations partagées",
    "notice_on_compelled_disclosure":              "l'obligation de notification en cas de divulgation forcée par autorité légale",
    "permissible_acquirement_of_similar_information": "la permission d'acquérir des informations similaires de manière indépendante",
    "permissible_copy":                            "la permission de reproduire les informations confidentielles",
    "permissible_development_of_similar_information": "la permission de développer des informations similaires de manière indépendante",
    "permissible_post_agreement_possession":       "la permission de conserver des informations après la fin de l'accord",
    "return_of_confidential_information":          "l'obligation de restituer ou détruire les informations confidentielles",
    "sharing_with_employees":                      "la permission de partager des informations confidentielles avec les employés",
    "sharing_with_third_parties":                  "la permission de partager des informations confidentielles avec des tiers",
    "survival_of_obligations":                     "la survie des obligations de confidentialité après la résiliation de l'accord",
}
for clause, clause_fr in CONTRACT_NLI_CLAUSES.items():
    YAML_UPDATES[f"contract_nli_{clause}"] = {
        "description": f"Identifier si la clause d'un contrat québécois ou canadien exprime, contredit ou ne traite pas la proposition concernant {clause_fr}.",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Entailment", "Contradiction", "Neutral"],
    }

# cuad group
CUAD_CLAUSES = {
    "affiliate_license_licensee":     "une licence accordée à une filiale ou affiliée en tant que licenciée",
    "affiliate_license_licensor":     "une licence accordée par une filiale ou affiliée en tant que donneur de licence",
    "anti_assignment":                "une restriction de cession ou de transfert du contrat sans consentement",
    "audit_rights":                   "un droit d'audit ou d'inspection des livres et des locaux de la contrepartie",
    "cap_on_liability":               "un plafonnement de la responsabilité entre les parties",
    "change_of_control":              "une clause de changement de contrôle ou de propriétaire",
    "competitive_restriction_exception": "une exception à la restriction de concurrence",
    "covenant_not_to_sue":            "un engagement de ne pas intenter de poursuites judiciaires",
    "effective_date":                 "une date d'entrée en vigueur spécifique du contrat",
    "exclusivity":                    "une clause d'exclusivité interdisant de traiter avec des concurrents",
    "expiration_date":                "une date d'expiration ou de fin de contrat",
    "governing_law":                  "une clause de droit applicable désignant la loi gouvernant le contrat",
    "insurance":                      "une obligation d'assurance à la charge d'une partie",
    "ip_ownership_assignment":        "une cession ou transfert de droits de propriété intellectuelle",
    "irrevocable_or_perpetual_license": "une licence irrévocable ou perpétuelle",
    "joint_ip_ownership":             "une propriété intellectuelle conjointe entre les parties",
    "license_grant":                  "un octroi de licence de propriété intellectuelle",
    "liquidated_damages":             "des dommages-intérêts conventionnels (clause pénale) préétablis",
    "minimum_commitment":             "un engagement minimum d'achat, d'utilisation ou de commande",
    "most_favored_nation":            "une clause de la nation la plus favorisée ou de traitement préférentiel",
    "no_solicit_of_customers":        "une clause de non-sollicitation des clients de la contrepartie",
    "no_solicit_of_employees":        "une clause de non-sollicitation ou de non-débauchage des employés",
    "non_compete":                    "une clause de non-concurrence (art. 2089 CCQ ou équivalent fédéral)",
    "non_disparagement":              "une clause de non-dénigrement",
    "non_transferable_license":       "une licence non transférable à des tiers",
    "notice_period_to_terminate_renewal": "un délai de préavis requis pour empêcher le renouvellement automatique",
    "post_termination_services":      "des obligations de services à rendre après la résiliation du contrat",
    "price_restrictions":             "des restrictions sur la fixation ou la modification unilatérale des prix",
    "renewal_term":                   "une durée ou des conditions de renouvellement automatique du contrat",
    "revenue_profit_sharing":         "un mécanisme de partage de revenus ou de bénéfices entre les parties",
    "rofr_rofo_rofn":                 "un droit de premier refus, de première offre ou de première négociation",
    "source_code_escrow":             "un dépôt de code source auprès d'un tiers séquestre",
    "termination_for_convenience":    "un droit de résiliation à la convenance d'une partie",
    "third_party_beneficiary":        "la désignation d'un bénéficiaire tiers des droits contractuels",
    "uncapped_liability":             "une responsabilité illimitée ou expressément non plafonnée",
    "unlimited_all_you_can_eat_license": "une licence illimitée et sans restriction de volume d'utilisation",
    "volume_restriction":             "une restriction de volume, de quantité ou de capacité d'utilisation",
    "warranty_duration":              "une durée de garantie spécifique accordée sur les produits ou services",
}
for clause, clause_fr in CUAD_CLAUSES.items():
    YAML_UPDATES[f"cuad_{clause}"] = {
        "description": f"Identifier si cette clause d'un contrat commercial québécois ou canadien contient {clause_fr} (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Non", "Oui"],
    }

# supply_chain group
SUPPLY_CHAIN_TOPICS = {
    "best_practice_accountability": "si la divulgation décrit des pratiques de responsabilisation sur le travail forcé",
    "best_practice_audits":         "si la divulgation décrit des pratiques ou politiques d'audit des fournisseurs",
    "best_practice_certification":  "si la divulgation décrit des pratiques de certification des fournisseurs",
    "best_practice_training":       "si la divulgation décrit des programmes de formation sur la détection du travail forcé",
    "best_practice_verification":   "si la divulgation décrit des pratiques de vérification de la chaîne d'approvisionnement",
    "disclosed_accountability":     "si la divulgation indique que des mesures de responsabilisation ont été effectivement mises en place",
    "disclosed_audits":             "si la divulgation indique que des audits de fournisseurs ont réellement été effectués",
    "disclosed_certification":      "si la divulgation indique que des certifications ont été obtenues ou exigées des fournisseurs",
    "disclosed_training":           "si la divulgation indique que des formations sur le travail forcé ont été dispensées",
    "disclosed_verification":       "si la divulgation indique que des vérifications ont réellement été effectuées auprès des fournisseurs",
}
for topic, topic_fr in SUPPLY_CHAIN_TOPICS.items():
    YAML_UPDATES[f"supply_chain_disclosure_{topic}"] = {
        "description": f"Déterminer {topic_fr}, conformément à la Loi sur la lutte contre le travail forcé et le travail des enfants dans les chaînes d'approvisionnement (Canada, S-211, 2023) (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Federal CA",
        "labels": ["Non", "Oui"],
    }

# opp115 group
OPP115_TOPICS = {
    "data_retention":                  "la période et les conditions de conservation des renseignements personnels",
    "data_security":                   "les mesures de sécurité protégeant les renseignements personnels",
    "do_not_track":                    "le traitement des signaux 'Do Not Track' des navigateurs",
    "first_party_collection_use":      "la collecte et l'utilisation des renseignements par l'organisation elle-même",
    "international_and_specific_audiences": "les pratiques relatives aux résidents étrangers ou aux publics spécifiques (mineurs)",
    "policy_change":                   "les modalités de modification de la politique de confidentialité",
    "third_party_sharing_collection":  "le partage ou la collecte de renseignements par des tiers",
    "user_access_edit_and_deletion":   "les droits d'accès, de rectification et de suppression des données de l'utilisateur",
    "user_choice_control":             "les options de choix et de contrôle offertes à l'utilisateur sur ses données",
}
for topic, topic_fr in OPP115_TOPICS.items():
    YAML_UPDATES[f"opp115_{topic}"] = {
        "description": f"Identifier si cette politique de confidentialité d'une organisation québécoise ou canadienne traite {topic_fr}, conformément à la Loi 25 et à la LPRPDE (Oui/Non).",
        "language": "fr",
        "target_jurisdiction": "Both",
        "labels": ["Non", "Oui"],
    }


# ─────────────────────────────────────────────────────────────────────────────
# 2. BASE_PROMPT.TXT TEMPLATES
# ─────────────────────────────────────────────────────────────────────────────

def make_clause_prompt(question_fr: str, item_label: str = "Clause") -> str:
    return f"""{question_fr}

Répondez uniquement par : Oui ou Non.

{{{{examples}}}}

{item_label} : {{{{text}}}}
Réponse :"""


def make_nli_prompt(hypothesis_context: str) -> str:
    return f"""Vous êtes un juriste spécialisé en droit des contrats québécois et canadien.
L'hypothèse suivante est-elle exprimée (Entailment), contredite (Contradiction) ou non traitée (Neutral) par la clause contractuelle?

{hypothesis_context}

Répondez uniquement par : Entailment, Contradiction ou Neutral.

{{{{examples}}}}

Clause : {{{{text}}}}
Réponse :"""


BASE_PROMPT_TEMPLATES: dict[str, str] = {
    "overruling": """Vous êtes un juriste spécialisé en droit judiciaire canadien.
Lisez la phrase extraite d'un jugement canadien (CSC, Cour d'appel, Cour fédérale ou Cour du Québec).
Cette phrase constitue-t-elle un revirement jurisprudentiel explicite, c'est-à-dire infirme-t-elle, annule-t-elle ou écarte-t-elle un précédent?

Répondez uniquement par : Oui ou Non.

{{examples}}

Phrase : {{text}}
Réponse :""",

    "definition_classification": """Vous êtes un juriste spécialisé en droit canadien.
Lisez la phrase extraite d'une décision judiciaire canadienne.
Cette phrase fournit-elle une définition d'un terme juridique ou d'un concept de droit?

Répondez uniquement par : Oui ou Non.

{{examples}}

Phrase : {{text}}
Réponse :""",

    "legal_reasoning_causality": """Vous êtes un juriste spécialisé en droit de la responsabilité civile et en droit de la preuve au Canada.
Lisez l'extrait d'une décision judiciaire canadienne.
Cet extrait s'appuie-t-il sur des preuves statistiques ou épidémiologiques pour établir un lien de causalité?

Répondez uniquement par : Oui ou Non.

{{examples}}

Extrait : {{text}}
Réponse :""",

    "citation_prediction_classification": """Vous êtes un juriste maîtrisant le Guide McGill de référence juridique (10e éd.).
Vérifiez si la citation bibliographique fournie correspond correctement au passage juridique indiqué.

Répondez uniquement par : Oui ou Non.

{{examples}}

Vérification : {{text}}
Réponse :""",

    "contract_qa": """Vous êtes un juriste spécialisé en droit des contrats québécois et canadien.
Lisez l'extrait contractuel ci-dessous et identifiez le type de clause contractuelle qu'il représente.

{{examples}}

Extrait : {{text}}
Réponse :""",

    "privacy_policy_entailment": """Vous êtes un juriste spécialisé en protection des renseignements personnels au Québec et au Canada (Loi 25, LPRPDE).
Lisez l'extrait de politique de confidentialité. Cet extrait implique-t-il que l'organisation effectue l'action décrite?

Répondez uniquement par : Oui ou Non.

{{examples}}

Extrait : {{text}}
Réponse :""",

    "privacy_policy_qa": """Vous êtes un juriste spécialisé en protection des renseignements personnels au Québec et au Canada (Loi 25, LPRPDE).
Lisez l'extrait de politique de confidentialité et répondez à la question posée.

{{examples}}

Extrait : {{text}}
Réponse :""",

    "unfair_tos": """Vous êtes un juriste spécialisé en protection du consommateur au Québec (Loi sur la protection du consommateur, LPC).
Classifiez cette clause de conditions générales d'utilisation selon la catégorie d'abus qui lui correspond.

{{examples}}

Clause : {{text}}
Réponse :""",
}

# learned_hands templates
LH_DOMAIN_PROMPTS = {
    "benefits":          ("prestations sociales, l'aide sociale et les services gouvernementaux", "ce scénario", "Scénario"),
    "business":          ("le droit des affaires, les sociétés et les entreprises au Canada", "ce scénario", "Scénario"),
    "consumer":          ("la protection du consommateur en vertu de la Loi sur la protection du consommateur (LPC) du Québec", "ce scénario", "Scénario"),
    "courts":            ("la procédure judiciaire, les délais et l'accès à la justice au Canada", "ce scénario", "Scénario"),
    "crime":             ("le droit criminel et pénal en vertu du Code criminel canadien", "ce scénario", "Scénario"),
    "divorce":           ("le divorce, la séparation et la pension alimentaire au Québec", "ce scénario", "Scénario"),
    "domestic_violence": ("la violence conjugale et la protection des victimes au Québec", "ce scénario", "Scénario"),
    "education":         ("le droit scolaire et l'éducation au Québec", "ce scénario", "Scénario"),
    "employment":        ("le droit du travail en vertu de la Loi sur les normes du travail (LNT) du Québec ou du Code canadien du travail", "ce scénario", "Scénario"),
    "estates":           ("les successions, les testaments et la liquidation de succession en vertu du Code civil du Québec (CCQ)", "ce scénario", "Scénario"),
    "family":            ("le droit de la famille québécois — garde d'enfants, autorité parentale, adoption (CCQ)", "ce scénario", "Scénario"),
    "health":            ("le droit de la santé, les soins médicaux et les droits des patients au Québec", "ce scénario", "Scénario"),
    "housing":           ("le bail résidentiel et le logement en vertu du Code civil du Québec (arts. 1851–2000)", "ce scénario", "Scénario"),
    "immigration":       ("l'immigration, le visa, le permis de travail et le statut de réfugié en vertu de la LIPR (Canada)", "ce scénario", "Scénario"),
    "torts":             ("la responsabilité civile extracontractuelle en vertu de l'art. 1457 CCQ", "ce scénario", "Scénario"),
    "traffic":           ("les infractions au Code de la sécurité routière du Québec", "ce scénario", "Scénario"),
}

for domain, (domain_fr, article, label) in LH_DOMAIN_PROMPTS.items():
    task_name = f"learned_hands_{domain}"
    BASE_PROMPT_TEMPLATES[task_name] = f"""Vous êtes un juriste québécois ou canadien.
Lisez {article} ci-dessous et déterminez s'il soulève une question juridique liée à {domain_fr}.

Répondez uniquement par : Oui ou Non.

{{{{examples}}}}

Scénario : {{{{text}}}}
Réponse :"""

# contract_nli templates
for clause, clause_fr in CONTRACT_NLI_CLAUSES.items():
    task_name = f"contract_nli_{clause}"
    BASE_PROMPT_TEMPLATES[task_name] = make_nli_prompt(
        f"La proposition porte sur {clause_fr}."
    )

# cuad templates
CUAD_QUESTIONS = {
    "affiliate_license_licensee":     "Cette clause d'un contrat québécois ou canadien accorde-t-elle une licence à une filiale ou affiliée en tant que licenciée?",
    "affiliate_license_licensor":     "Cette clause d'un contrat québécois ou canadien accorde-t-elle à une filiale ou affiliée le droit d'agir en tant que donneur de licence?",
    "anti_assignment":                "Cette clause d'un contrat québécois ou canadien interdit-elle ou restreint-elle la cession ou le transfert du contrat sans consentement préalable?",
    "audit_rights":                   "Cette clause d'un contrat québécois ou canadien accorde-t-elle un droit d'audit ou d'inspection des livres et locaux de la contrepartie?",
    "cap_on_liability":               "Cette clause d'un contrat québécois ou canadien plafonne-t-elle la responsabilité d'une partie?",
    "change_of_control":              "Cette clause d'un contrat québécois ou canadien prévoit-elle des conséquences en cas de changement de contrôle ou de propriétaire d'une partie?",
    "competitive_restriction_exception": "Cette clause d'un contrat québécois ou canadien prévoit-elle une exception à une restriction de concurrence?",
    "covenant_not_to_sue":            "Cette clause d'un contrat québécois ou canadien constitue-t-elle un engagement de ne pas intenter de poursuites judiciaires?",
    "effective_date":                 "Cette clause d'un contrat québécois ou canadien désigne-t-elle une date d'entrée en vigueur spécifique?",
    "exclusivity":                    "Cette clause d'un contrat québécois ou canadien impose-t-elle une obligation d'exclusivité à une partie?",
    "expiration_date":                "Cette clause d'un contrat québécois ou canadien précise-t-elle une date d'expiration ou de fin du contrat?",
    "governing_law":                  "Cette clause d'un contrat québécois ou canadien désigne-t-elle le droit applicable au contrat?",
    "insurance":                      "Cette clause d'un contrat québécois ou canadien impose-t-elle une obligation de maintenir une assurance?",
    "ip_ownership_assignment":        "Cette clause d'un contrat québécois ou canadien prévoit-elle une cession de droits de propriété intellectuelle?",
    "irrevocable_or_perpetual_license": "Cette clause d'un contrat québécois ou canadien octroie-t-elle une licence irrévocable ou perpétuelle?",
    "joint_ip_ownership":             "Cette clause d'un contrat québécois ou canadien établit-elle une propriété intellectuelle conjointe entre les parties?",
    "license_grant":                  "Cette clause d'un contrat québécois ou canadien octroie-t-elle une licence de propriété intellectuelle?",
    "liquidated_damages":             "Cette clause d'un contrat québécois ou canadien prévoit-elle des dommages-intérêts conventionnels (clause pénale) préétablis?",
    "minimum_commitment":             "Cette clause d'un contrat québécois ou canadien impose-t-elle un engagement minimum d'achat, d'utilisation ou de commande?",
    "most_favored_nation":            "Cette clause d'un contrat québécois ou canadien contient-elle une clause de la nation la plus favorisée ou de traitement préférentiel?",
    "no_solicit_of_customers":        "Cette clause d'un contrat québécois ou canadien interdit-elle la sollicitation des clients de la contrepartie?",
    "no_solicit_of_employees":        "Cette clause d'un contrat québécois ou canadien interdit-elle le débauchage ou la sollicitation des employés de la contrepartie?",
    "non_compete":                    "Cette clause d'un contrat québécois ou canadien constitue-t-elle une clause de non-concurrence (art. 2089 CCQ ou équivalent)?",
    "non_disparagement":              "Cette clause d'un contrat québécois ou canadien constitue-t-elle une clause de non-dénigrement?",
    "non_transferable_license":       "Cette clause d'un contrat québécois ou canadien stipule-t-elle que la licence accordée est non transférable?",
    "notice_period_to_terminate_renewal": "Cette clause d'un contrat québécois ou canadien exige-t-elle un délai de préavis pour empêcher le renouvellement automatique?",
    "post_termination_services":      "Cette clause d'un contrat québécois ou canadien impose-t-elle des obligations de services après la résiliation?",
    "price_restrictions":             "Cette clause d'un contrat québécois ou canadien prévoit-elle des restrictions sur la fixation ou la modification des prix?",
    "renewal_term":                   "Cette clause d'un contrat québécois ou canadien précise-t-elle des conditions ou une durée de renouvellement?",
    "revenue_profit_sharing":         "Cette clause d'un contrat québécois ou canadien prévoit-elle un partage de revenus ou de bénéfices entre les parties?",
    "rofr_rofo_rofn":                 "Cette clause d'un contrat québécois ou canadien contient-elle un droit de premier refus, de première offre ou de première négociation?",
    "source_code_escrow":             "Cette clause d'un contrat québécois ou canadien prévoit-elle un dépôt de code source auprès d'un tiers séquestre?",
    "termination_for_convenience":    "Cette clause d'un contrat québécois ou canadien accorde-t-elle à une partie un droit de résiliation à sa convenance?",
    "third_party_beneficiary":        "Cette clause d'un contrat québécois ou canadien désigne-t-elle un bénéficiaire tiers des droits contractuels?",
    "uncapped_liability":             "Cette clause d'un contrat québécois ou canadien exclut-elle tout plafonnement de la responsabilité?",
    "unlimited_all_you_can_eat_license": "Cette clause d'un contrat québécois ou canadien octroie-t-elle une licence sans restriction de volume ou de quantité?",
    "volume_restriction":             "Cette clause d'un contrat québécois ou canadien impose-t-elle une restriction de volume, de quantité ou de capacité d'utilisation?",
    "warranty_duration":              "Cette clause d'un contrat québécois ou canadien précise-t-elle la durée d'une garantie?",
}
for clause, question_fr in CUAD_QUESTIONS.items():
    task_name = f"cuad_{clause}"
    BASE_PROMPT_TEMPLATES[task_name] = make_clause_prompt(
        f"Vous êtes un juriste spécialisé en droit des contrats québécois et canadien.\n{question_fr}"
    )

# supply_chain templates
SC_QUESTIONS = {
    "best_practice_accountability":  "Cette divulgation de chaîne d'approvisionnement décrit-elle des pratiques ou politiques de responsabilisation visant à prévenir le travail forcé, conformément à la Loi S-211 (Canada, 2023)?",
    "best_practice_audits":          "Cette divulgation de chaîne d'approvisionnement décrit-elle des pratiques ou politiques d'audit des fournisseurs pour détecter le travail forcé, conformément à la Loi S-211 (Canada, 2023)?",
    "best_practice_certification":   "Cette divulgation de chaîne d'approvisionnement décrit-elle des pratiques ou politiques de certification des fournisseurs, conformément à la Loi S-211 (Canada, 2023)?",
    "best_practice_training":        "Cette divulgation de chaîne d'approvisionnement décrit-elle des programmes de formation sur la détection et la prévention du travail forcé, conformément à la Loi S-211 (Canada, 2023)?",
    "best_practice_verification":    "Cette divulgation de chaîne d'approvisionnement décrit-elle des pratiques ou politiques de vérification de la chaîne d'approvisionnement, conformément à la Loi S-211 (Canada, 2023)?",
    "disclosed_accountability":      "Cette divulgation de chaîne d'approvisionnement indique-t-elle que des mesures concrètes de responsabilisation ont été effectivement mises en œuvre, conformément à la Loi S-211 (Canada, 2023)?",
    "disclosed_audits":              "Cette divulgation de chaîne d'approvisionnement indique-t-elle que des audits de fournisseurs ont réellement été effectués, conformément à la Loi S-211 (Canada, 2023)?",
    "disclosed_certification":       "Cette divulgation de chaîne d'approvisionnement indique-t-elle que des certifications ont été obtenues ou exigées des fournisseurs, conformément à la Loi S-211 (Canada, 2023)?",
    "disclosed_training":            "Cette divulgation de chaîne d'approvisionnement indique-t-elle que des formations sur le travail forcé ont été effectivement dispensées, conformément à la Loi S-211 (Canada, 2023)?",
    "disclosed_verification":        "Cette divulgation de chaîne d'approvisionnement indique-t-elle que des vérifications ont réellement été effectuées auprès des fournisseurs, conformément à la Loi S-211 (Canada, 2023)?",
}
for topic, question_fr in SC_QUESTIONS.items():
    task_name = f"supply_chain_disclosure_{topic}"
    BASE_PROMPT_TEMPLATES[task_name] = make_clause_prompt(
        f"Vous êtes un juriste spécialisé en droit des affaires et en responsabilité des entreprises au Canada.\n{question_fr}",
        item_label="Divulgation"
    )

# opp115 templates
OPP_QUESTIONS = {
    "data_retention":                  "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle la durée ou les conditions de conservation des renseignements personnels (Loi 25 / LPRPDE)?",
    "data_security":                   "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle les mesures de sécurité mises en place pour protéger les renseignements personnels (Loi 25 / LPRPDE)?",
    "do_not_track":                    "Cette clause de politique de confidentialité québécoise ou canadienne traite-t-elle des signaux 'Do Not Track' envoyés par les navigateurs (Loi 25 / LPRPDE)?",
    "first_party_collection_use":      "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle la collecte et l'utilisation des renseignements personnels par l'organisation elle-même (Loi 25 / LPRPDE)?",
    "international_and_specific_audiences": "Cette clause de politique de confidentialité québécoise ou canadienne traite-t-elle du transfert international de données ou de publics spécifiques tels que les mineurs (Loi 25 / LPRPDE)?",
    "policy_change":                   "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle les modalités de modification de la politique (Loi 25 / LPRPDE)?",
    "third_party_sharing_collection":  "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle le partage ou la collecte de renseignements par des tiers (Loi 25 / LPRPDE)?",
    "user_access_edit_and_deletion":   "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle les droits d'accès, de rectification et de suppression des renseignements par l'utilisateur (Loi 25 / LPRPDE)?",
    "user_choice_control":             "Cette clause de politique de confidentialité québécoise ou canadienne décrit-elle les options de choix et de contrôle offertes à l'utilisateur sur ses renseignements personnels (Loi 25 / LPRPDE)?",
}
for topic, question_fr in OPP_QUESTIONS.items():
    task_name = f"opp115_{topic}"
    BASE_PROMPT_TEMPLATES[task_name] = make_clause_prompt(
        f"Vous êtes un juriste spécialisé en protection des renseignements personnels au Québec et au Canada.\n{question_fr}",
        item_label="Clause"
    )


# ─────────────────────────────────────────────────────────────────────────────
# 3. APPLY ALL UPDATES
# ─────────────────────────────────────────────────────────────────────────────

def apply_updates():
    yaml_updated = 0
    yaml_missing = []
    prompt_updated = 0
    prompt_missing = []

    for task_name, updates in YAML_UPDATES.items():
        yaml_file = TASKS_DIR / task_name / "task.yaml"
        if not yaml_file.exists():
            yaml_missing.append(task_name)
            continue

        with open(yaml_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        data.update(updates)

        # Remove US-source fields
        for field in ("source", "license", "imported_from"):
            data.pop(field, None)
        data["version"] = 2

        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        yaml_updated += 1

    for task_name, template in BASE_PROMPT_TEMPLATES.items():
        prompt_file = TASKS_DIR / task_name / "base_prompt.txt"
        if not (TASKS_DIR / task_name).exists():
            prompt_missing.append(task_name)
            continue

        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(template)
        prompt_updated += 1

    print(f"task.yaml   updated : {yaml_updated}")
    print(f"task.yaml   missing : {yaml_missing}")
    print(f"base_prompt updated : {prompt_updated}")
    print(f"base_prompt missing : {prompt_missing}")


if __name__ == "__main__":
    apply_updates()