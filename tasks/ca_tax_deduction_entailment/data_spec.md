## Purpose
Déterminer si un scénario factuel ouvre droit à une déduction fiscale au sens des lois fiscales fédérales canadiennes (Vrai/Faux).

## Question format
**Input:** Un scénario factuel décrivant la situation fiscale d'un contribuable canadien, suivi d'une affirmation sur son droit à une déduction fiscale.
**Output:** `Vrai` | `Faux`

## Legal sources
- **Loi de l'impôt sur le revenu, LRC 1985 c 1 (5e suppl.)** — dispositions applicables aux déductions fiscales fédérales canadiennes
- **Bulletins d'interprétation de l'ARC** pertinents
- **Jurisprudence CCI et Cour d'appel fédérale**

## Diversity requirements
- Varier les types de contribuables (particulier, travailleur autonome, PME, société)
- Varier la complexité (cas clair vs cas limite)
- Inclure des `Faux` : situations qui semblent admissibles mais ne le sont pas
- Équilibre strict 50 % Vrai / 50 % Faux (± 1)

## Do not use
- Droit fiscal américain (IRS, IRC)
- Données de a2aj/canadian-laws
