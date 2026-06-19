## Purpose
Identifier si ce scénario soulève une question de droit du bail résidentiel québécois (TAL, CCQ arts. 1851-2000).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon propriétaire refuse de réparer la fournaise depuis trois semaines. Il fait -15°C dehors et mon appartement n'est plus chauffé."
> → Oui

## Positif — `Oui`
- Obligation d'entretien du logement par le locateur (CCQ art. 1854)
- Reprise de logement ou éviction (CCQ art. 1957-1970)
- Fixation ou augmentation de loyer (CCQ art. 1906-1909, TAL)
- Entrée non autorisée du locateur (CCQ art. 1930-1931)
- Résiliation de bail pour violence conjugale (CCQ art. 1974.1)
- Sous-location ou cession de bail (CCQ art. 1870-1876)

## Négatif — `Non`
- Litige entre deux locataires (pas un litige bail)
- Bail commercial (règles différentes — CCQ art. 1851 exclut les baux commerciaux)
- Litige de copropriété divise entre copropriétaires (pas un bail)
- Dispute d'emploi ou familiale se déroulant dans un logement

## Sources légales
- CCQ art. 1851-2000 (bail résidentiel)
- Règlement sur les critères de fixation de loyer (RLRQ c T-15.01, r 4)
- Tribunal administratif du logement (TAL) — jurisprudence (canlii.org — Québec — TAL)

## Diversité
- Varier: appartement, maison, chambre, coopérative d'habitation
- Inclure: reconduction tacite du bail, délais de préavis (3, 4, 6 mois)
- Inclure: dépôt de garantie illégal, animaux, fumée secondaire
- Inclure des Non plausibles: litige de bail commercial, dispute de voisinage sans lien au bail

## Ne pas utiliser
- Landlord-Tenant Act (Ontario, BC)
- Éviction moratorium rules from US states
- Données de a2aj/canadian-laws