## Purpose
Déterminer si une clause d'accord de confidentialité (NDA) implique ou garantit les conditions sous lesquelles les employés de la partie réceptrice peuvent accéder aux informations (Vrai/Faux).

## Question format
**Input:** Une clause d'accord de confidentialité en français, suivie d'une affirmation portant sur partage autorisé avec les employés.
**Output:** `Vrai` | `Faux`

**Définition opérationnelle :**
`Vrai` — la clause implique logiquement l'affirmation sur partage autorisé avec les employés.
`Faux` — la clause n'implique pas ou contredit l'affirmation.

## Label criteria

### Vrai
- L'affirmation découle directement du texte de la clause
- La clause impose explicitement l'obligation décrite

### Faux
- L'affirmation va au-delà de ce que prévoit la clause
- La clause impose une obligation contraire ou différente
- La clause est muette sur le sujet de l'affirmation

## Legal sources
- **CCQ art. 1375–1432** — interprétation des contrats, bonne foi
- **Loi 25, RLRQ c P-39.1** — protection des renseignements personnels (si applicable)
- **Pratique contractuelle des NDA au Québec et au Canada**

## Diversity requirements
- Varier la formulation des clauses (restrictive vs permissive vs conditionnelle)
- Varier la longueur des clauses (courte 2–3 lignes vs détaillée 8–12 lignes)
- Inclure des `Faux` nuancés : clauses qui semblent couvrir le sujet mais comportent une exception
- Équilibre strict 50 % Vrai / 50 % Faux (± 1)

## Do not use
- NDA régis par le droit américain ou le droit anglais
- Données de a2aj/canadian-laws
- Clauses dont la qualification est impossible sans le reste du contrat
