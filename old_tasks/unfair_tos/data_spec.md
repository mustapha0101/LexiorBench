## Purpose
Classifier une clause de conditions d'utilisation (TOS) selon sa catégorie d'iniquité en droit québécois de la consommation (LPC).

## Question format
Input: clause de conditions d'utilisation ou de contrat de consommation en français.
Output: catégorie d'iniquité (voir classes ci-dessous)

**Exemple:**
> "La compagnie peut modifier unilatéralement le prix du service sans préavis."
> → Clause abusive — modification unilatérale (art. 8 + 11.2 LPC)

## Classes (catégories d'iniquité LPC)
- **Modification unilatérale**: la commerçante se réserve le droit de modifier les conditions sans consentement du consommateur
- **Limitation de responsabilité**: exclusion ou limitation de la responsabilité du commerçant au-delà de ce que la loi permet
- **Arbitrage forcé**: clause imposant l'arbitrage et écartant les recours judiciaires
- **Résiliation abusive**: conditions de résiliation unilatéralement favorables au commerçant
- **Renonciation à des droits légaux**: le consommateur renonce à des droits que la loi lui garantit
- **Acceptable**: clause conforme à la LPC et au CCQ, pas abusive

## Sources légales
- Loi sur la protection du consommateur (RLRQ c P-40.1) art. 8, 11.2, 19, 54.8, 271
- CCQ art. 1437 (clause abusive dans un contrat de consommation)
- Décisions de la Cour du Québec et des petites créances sur les clauses abusives
- Office de la protection du consommateur (OPC) — bulletins d'interprétation

## Diversité
- Varier les secteurs: abonnements en ligne, téléphonie, logiciels SaaS, services bancaires, jeux vidéo
- Inclure des clauses clairement abusives et des clauses limites (zone grise)
- Inclure des clauses qui semblent abusives mais sont valides (nuance LPC)
- Inclure la classe "Acceptable" à ~20% pour éviter le biais

## Do not use
- Directive européenne sur les clauses abusives (CJUE)
- US unconscionability doctrine
- Données de a2aj/canadian-laws