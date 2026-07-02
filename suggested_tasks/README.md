# Suggested Tasks — LexiorBench v2 Gap Analysis

Generated: 2026-06-19

These tasks address coverage gaps identified after completing the 128-task v2 benchmark.
Each file contains a draft `task.yaml` spec. To activate a task, create a folder under `tasks/`,
add the YAML, then run the generation pipeline for `base_prompt.txt`, `data_spec.md`, and `sample.tsv`.

---

## Coverage Gaps Identified

### Reasoning type gaps
- `interpretation` dominates (78/128 = 61%). Under-represented: `rule_application` (7), `rule_conclusion` (4).
- No `analogical_reasoning` tasks (case-to-case analogy).

### Legal domain gaps
| Domain | Current Coverage | Gap |
|---|---|---|
| Criminal / penal law | `learned_hands_crime` (issue spotting only) | No element identification, no defences |
| Family law | `learned_hands_family/divorce` (issue spotting) | No CCQ Book II tasks (custody, support) |
| Administrative law | None | No judicial review standard tasks |
| Constitutional law | `public_interpretation_charte` (partial) | No division of powers tasks |
| Labour / employment | `learned_hands_employment` (issue spotting) | No LNT specific tasks, no C.c.t. tasks |
| Intellectual property | CUAD IP clause tasks only | No Canadian copyright/trademark analysis |
| Succession / notarial | `learned_hands_estates` (issue spotting) | No CCQ Book III tasks |
| Real estate / property | `civil_rule_application_vices_caches` | No lease, ownership, hypothec tasks |

### Jurisdiction gaps
- `quebec`-only tasks: 14/128 (11%). Could add more CCQ-specific tasks.
- `federal_ca`-only tasks: 19/128 (15%). Could add more CBCA / Criminal Code tasks.

---

## Suggested Task Files

1. `ca_criminal_elements.yaml` — Identify actus reus / mens rea / defences (Criminal Code)
2. `ca_administrative_review_standard.yaml` — Judicial review standard (Vavilov framework)
3. `ca_lnt_termination.yaml` — LNT art. 82-83-124 wrongful dismissal analysis
4. `ca_succession_testamentary_capacity.yaml` — CCQ art. 710-730 testamentary capacity
5. `ca_constitutional_division_powers.yaml` — s.91/92 Constitution Act division of powers
6. `ca_copyright_authorship.yaml` — Who owns the copyright? (Loi sur le droit d'auteur)
7. `ca_ccq_lease_rights.yaml` — Residential lease rights CCQ art. 1851-2000
8. `ca_human_rights_grounds_identification.yaml` — Identify CDLP / CHRA protected ground
9. `ca_analogical_reasoning.yaml` — Apply ratio from precedent to new facts (analogical)
10. `ca_cbca_director_duty.yaml` — CBCA s.122 director duty of care / loyalty

---

## Project Update Notes

Suggested tasks should now follow the same provider-neutral generation path as active tasks:

- Draft or revise the suggested task YAML under `suggested_tasks/`.
- When promoting a suggested task, create its folder under `tasks/` and add `task.yaml`, `base_prompt.txt`, `data_spec.md`, and `sample.tsv`.
- Use `scripts/generate_samples_structured.py` with `--generation-model <provider:model>` or `LEXIOR_GENERATION_MODEL` for structured sample generation.
- Use `prompts/generation_system_prompt.md` as the shared generation prompt.
- Keep one-off migration and metadata repair helpers in `changes/`; do not treat them as part of the normal task-generation interface.
- New suggested tasks should preserve the current benchmark requirements: balanced labels, hard negatives, exact labels, legal-source restrictions, `law_as_of`, structured JSON, validation errors for inconsistent specs, and `needs_human_review` for borderline examples.
