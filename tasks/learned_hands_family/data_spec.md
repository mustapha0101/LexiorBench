## Purpose
Identifier si ce scénario soulève une question de droit de la famille (garde, pension alimentaire pour enfants, autorité parentale).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon ex-conjoint veut déménager à Vancouver avec nos deux enfants sans mon consentement. Notre entente de garde est partagée à 50/50."
> → Oui

## Positif — `Oui`
- Garde physique ou légale des enfants (CCQ art. 394.2, Loi sur le divorce)
- Relocalisation d'un parent avec les enfants (déménagement)
- Pension alimentaire pour enfants (Lignes directrices fédérales, RLRQ c C-25.01)
- Autorité parentale contestée (art. 33 CCQ — intérêt de l'enfant)
- Adoption, tutelle, déchéance de l'autorité parentale

## Négatif — `Non`
- Divorce entre époux sans enfants (pension alimentaire pour époux — domaine distinct)
- Violence conjugale sans question de garde distincte
- Décision scolaire sans contestation de l'autorité parentale

## Sources légales
- CCQ art. 33, 394.2-413 (autorité parentale, garde, aliments)
- Loi sur le divorce (LRC 1985 c 3 (2e suppl.)) art. 16 (garde)
- Lignes directrices fédérales sur les aliments pour enfants (DORS/97-175)
- Loi sur la protection de la jeunesse (RLRQ c P-34.1)

## Diversité
- Varier: séparation de couples mariés, union civile, conjoints de fait
- Inclure: demandes d'urgence, ordonnances provisoires, médiation familiale
- Inclure: droits de visite, relocalisation internationale
- Inclure des Non plausibles: litige de divorce portant sur les biens sans enfants

## Ne pas utiliser
- Best interests standard from US state courts
- Données de a2aj/canadian-laws