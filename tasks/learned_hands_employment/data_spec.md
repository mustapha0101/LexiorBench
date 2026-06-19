## Purpose
Identifier si ce scénario soulève une question de droit du travail québécois ou canadien (LNT, CCT, harcèlement, congédiement).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon employeur me demande de travailler 55 heures par semaine depuis deux mois. Il refuse de payer les heures supplémentaires, disant que je suis 'cadre'. Je supervise deux personnes."
> → Oui

## Positif — `Oui`
- Violation des normes du travail (LNT ou Code canadien du travail)
- Congédiement sans cause juste et suffisante (LNT art. 124)
- Harcèlement psychologique au travail (LNT art. 81.18+)
- Discrimination à l'embauche ou au travail (Charte québécoise)
- Non-paiement de salaire, heures supplémentaires, vacances

## Négatif — `Non`
- Litige entre associés ou actionnaires (pas un lien d'emploi)
- Litige de prestations gouvernementales lié indirectement au travail
- Accident du travail (CNESST — domaine distinct en QC)

## Sources légales
- Loi sur les normes du travail (RLRQ c N-1.1)
- Code canadien du travail (LRC 1985 c L-2) — employeurs fédéraux
- Charte des droits et libertés de la personne (art. 10, 16, 18)
- Décisions CanLII: TAT (Tribunal administratif du travail), CNESST

## Diversité
- Varier: heures supp, congés, protection contre représailles, droit de retour
- Inclure: travailleurs autonomes vs salariés (qualification du statut)
- Inclure: secteur fédéral vs provincial (banques, transport, télécoms = fédéral)
- Inclure des Non plausibles: accident à l'extérieur du travail qui impacte l'emploi

## Ne pas utiliser
- FLSA, NLRA, EEOC (US)
- Données de a2aj/canadian-laws