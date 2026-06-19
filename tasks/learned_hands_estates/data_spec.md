## Purpose
Identifier si ce scénario soulève une question de droit successoral québécois (testament, liquidation, héritage, réserve héréditaire).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon père est décédé la semaine dernière sans testament. Ma mère est encore vivante. Qui hérite? Je suis fils unique."
> → Oui

## Positif — `Oui`
- Succession ab intestat (sans testament) — qui hérite? (CCQ art. 653+)
- Validité ou contestation d'un testament (olographe, devant témoins, notarié)
- Legs particulier ou universel, liquidateur de succession
- Renonciation à une succession / acceptation sous bénéfice d'inventaire (CCQ art. 630+)
- Partage d'une succession avec dettes

## Négatif — `Non`
- Régime matrimonial entre conjoints vivants (patrimoine familial — distinct de la succession)
- Assurance-vie (désignation de bénéficiaire — hors succession)
- Litige de garde ou de pension alimentaire pour enfants

## Sources légales
- CCQ Livre III (art. 613-898) — successions, testament, liquidation
- Loi sur les testaments (abolie — intégrée dans CCQ depuis 1994)
- Décisions CanLII: Cour supérieure QC (chambre de la famille / des successions)

## Diversité
- Varier: décès avec et sans testament, héritiers multiples, dettes de la succession
- Inclure: testaments olographes contestés, vices de forme, undue influence
- Inclure: situations avec enfants de différents lits, conjoints de fait (pas d'héritage légal)
- Inclure des Non plausibles: assurance-vie, REER avec bénéficiaire désigné

## Ne pas utiliser
- Wills and Succession Act (Alberta, BC)
- Common law intestacy rules
- Données de a2aj/canadian-laws