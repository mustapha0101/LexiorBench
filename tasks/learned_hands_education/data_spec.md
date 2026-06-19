## Purpose
Identifier si ce scénario soulève une question juridique liée au droit à l'éducation (accommodements, suspension, langue d'enseignement, droits de l'élève).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon enfant autiste a été suspendu de l'école parce qu'il a eu une crise liée à son handicap. La commission scolaire dit que son comportement était 'incompatible avec le milieu scolaire'."
> → Oui

## Positif — `Oui`
- Obligation d'accommodement raisonnable pour un élève handicapé (Charte québécoise, art. 10)
- Refus d'accès à l'école ou suspension contestable
- Droits linguistiques scolaires (Charte de la langue française — loi 101, art. 73+)
- Droit à des services éducatifs pour enfants en situation de handicap (Loi sur l'instruction publique)

## Négatif — `Non`
- Litige entre parents sur les décisions scolaires (droit de la famille)
- Faute professionnelle d'un enseignant sans dimension de droit à l'éducation
- Problème d'emploi d'un enseignant (droit du travail)

## Sources légales
- Loi sur l'instruction publique (RLRQ c I-13.3)
- Charte des droits et libertés de la personne du Québec (art. 10, 40)
- Charte de la langue française (RLRQ c C-11) — langue d'enseignement
- Loi sur l'enseignement privé (RLRQ c E-9.1)

## Diversité
- Varier: TDAH, TSA, trouble d'apprentissage, handicap physique, trouble de comportement
- Inclure: droits linguistiques (anglophone en école française, allophone)
- Inclure: suspension vs expulsion, programmes adaptés (EHDAA)
- Inclure des Non plausibles: litige de pension alimentaire mentionnant une école

## Ne pas utiliser
- IDEA, Section 504 (US)
- Données de a2aj/canadian-laws