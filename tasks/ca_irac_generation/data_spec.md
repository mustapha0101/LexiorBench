## Purpose
Générer une analyse IRAC complète (Problème — Règle — Application — Conclusion) à partir
d'un extrait de décision judiciaire québécoise ou canadienne.

## Question format
**Input:** Un extrait de décision judiciaire de 150 à 400 mots, en français, décrivant
les faits et la question juridique centrale.
**Output:** Une analyse IRAC structurée en 4 sections étiquetées, 150–300 mots,
citant les articles pertinents du CCQ ou les lois fédérales applicables.

*Évaluation: juge LLM (GPT-4o) sur rubrique 4 critères — fidélité aux faits, exactitude
de la règle citée, rigueur de l'application, clarté de la conclusion.*

## Required IRAC structure
```
Problème: [question juridique centrale, une phrase]
Règle: [règle(s) applicable(s) avec citation d'article(s) ou d'arrêt(s) — 2 à 4 phrases]
Application: [raisonnement appliquant la règle aux faits — 3 à 5 phrases]
Conclusion: [issue probable et réparation/sanction si applicable — 1 à 2 phrases]
```

## Legal sources (verified via lexior-ccq MCP — 2026-06-19)
- **Art. 1457–1458 CCQ** — responsabilité civile extra- et contractuelle
- **Art. 1470 CCQ** — exonération par force majeure (imprévisible, irrésistible, extérieure)
- **Art. 1478 CCQ** — partage de responsabilité / faute contributive
- **Art. 1590 CCQ** — droits du créancier en cas d'inexécution contractuelle
- **Art. 1607–1625 CCQ** — évaluation des dommages-intérêts
- **Art. 1726–1730 CCQ** — garantie contre les vices cachés; présomption (vendeur professionnel)
- **Art. 2925–2926 CCQ** — prescription 3 ans; préjudice graduel
- **Art. 976 CCQ** — troubles de voisinage (inconvénients anormaux)
- **Clements c. Clements, 2012 CSC 32** — causalité en responsabilité civile
- **Loi sur les normes du travail, RLRQ c N-1.1** — art. 82–83 (avis de licenciement), art. 124 (congédiement sans cause juste)
- **Loi sur la protection du consommateur, RLRQ c P-40.1** — art. 8 (clause abusive)
- **Loi sur le notariat, RLRQ c N-3** — obligation de conseil et de vérification des titres

## Diversity requirements
- **Vary legal domain** (minimum 4 distinct domains per 10 examples):
  responsabilité civile extracontractuelle, vices cachés, prescription extinctive,
  inexécution contractuelle / force majeure, responsabilité professionnelle,
  droit du travail, troubles de voisinage, consommation
- **Vary court level**: Cour du Québec, Cour supérieure, Cour d'appel du Québec, CSC
- **Vary complexity**:
  40% straightforward (single article, clear fault, obvious outcome),
  40% nuanced (force majeure plea, partial fault, competing regimes),
  20% edge cases (prescription that nearly runs, ambiguous causation)
- **Vary outcome**: ≥40% cases where defendant succeeds or there is partial success only
- **Vary input length**: 150 words (simple) to 400 words (multi-issue complex)

## Do not use
- Verbatim text from actual CanLII decisions (data leakage risk — paraphrase/reconstruct)
- US law, common law concepts without CCQ equivalent, SCOTUS references
- Fact patterns with no identifiable legal dispute
- Data from a2aj/canadian-laws training set
- Federal bilingual statutes applied to purely Quebec scenarios without acknowledgment
