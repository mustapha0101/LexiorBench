## Purpose
Identifier si une section d'une politique de confidentialité québécoise ou canadienne traite de accès, rectification et suppression par l'utilisateur (Oui/Non).

## Question format
**Input:** Un extrait d'une politique de confidentialité en français.
**Output:** `Oui` | `Non`

**Définition opérationnelle :**
`Oui` — l'extrait traite explicitement ou de manière substantielle de droits d'accès, demande de correction ou de suppression des données.
`Non` — l'extrait ne traite pas du sujet ou n'en fait qu'une mention incidente.

## Legal sources
- **Loi 25, RLRQ c P-39.1** — modernisation de la protection des renseignements personnels au Québec
- **LPRPDE, LC 2000 c 5** — protection des renseignements personnels dans le secteur privé (fédéral)
- **Lignes directrices du CAI (Commission d'accès à l'information du Québec)**

## Diversity requirements
- Varier les types d'organisations (PME, grande entreprise, OBNL, commerce en ligne)
- Varier la longueur des extraits (2–3 phrases vs paragraphe complet)
- Inclure des `Non` trompeurs : sections adjacentes sans traiter le sujet
- Équilibre strict 50 % Oui / 50 % Non (± 1)

## Do not use
- Politiques soumises au RGPD européen ou au CCPA californien uniquement
- Données de a2aj/canadian-laws
