## Purpose
Identifier si ce scénario soulève une question juridique liée aux prestations sociales et services gouvernementaux (aide sociale, AE, RRQ, PFCE, invalidité).

## Question format
Input: scénario en français décrivant une situation personnelle.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai fait une demande d'aide sociale au mois de mars et on m'a refusé en disant que j'avais trop d'actifs. Mon seul actif est une vieille voiture valant 800$."
> → Oui

## Positif — `Oui`
- Admissibilité refusée ou contestée pour aide sociale, AE, RRQ, PFCE, allocation invalidité
- Coupure ou réduction de prestations sans explication valable
- Non-paiement d'une prestation due
- Recours en révision administrative d'une décision de refus

## Négatif — `Non`
- Scénario de droit du travail (congédiement, heures supplémentaires)
- Scénario de droit familial (pension alimentaire, garde)
- Scénario de droit du logement (expulsion, réparations)
- Scénario fiscal sans lien avec une prestation

## Sources légales
- Loi sur l'aide aux personnes et aux familles (RLRQ c A-13.1.1) — aide sociale QC
- Loi sur l'assurance-emploi (SC 1996 c 23)
- Loi sur le régime de rentes du Québec (RLRQ c R-9)
- Loi sur la sécurité de la vieillesse (LRC 1985 c O-9)
- Prestation canadienne pour enfants (LIR art. 122.6)

## Diversité
- Varier: aide sociale, AE, RRQ/CPP, SV/GIS, allocations familiales, invalidité
- Inclure: refus initial, révision, appel, coupure mid-prestations
- Inclure des Non plausibles: droit du travail, droit familial (semblent liés aux prestations)
- Varier le profil: parent monoparental, personne handicapée, travailleur autonome, aîné

## Ne pas utiliser
- Medicaid, SNAP, SSI (US)
- Données de a2aj/canadian-laws