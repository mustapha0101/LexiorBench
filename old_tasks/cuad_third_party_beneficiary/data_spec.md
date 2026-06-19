## Purpose
Identifier si une clause d'un contrat commercial québécois ou canadien si la clause désigne un tiers bénéficiaire du contrat (Oui/Non).

## Question format
Input: clause extraite d'un contrat commercial en français.
Output: `Oui` | `Non`

**Exemple de clause:** tiers bénéficiaire — ex: 'la présente stipulation est faite au bénéfice de la société mère du preneur'

## Positif — `Oui`
- La clause traite explicitement du sujet visé
- La clause implique nécessairement le sujet même sans le nommer

## Positif — `Non`
- La clause porte sur un autre sujet contractuel
- La clause effleure le sujet de manière incidente sans en faire l'objet principal
- Clause générale de représentations et garanties sans spécificité

## Sources légales
- CCQ art. 1375-1432 (règles générales des contrats)
- CCQ art. 2089 CCQ (non-concurrence entre employeur-employé)
- Loi sur les marques de commerce (LRC 1985 c T-13) — pour clauses PI
- Pratique contractuelle des barreaux du Québec et du Barreau du Haut-Canada
- Modèles de contrats commerciaux (baux commerciaux, franchises, contrats de service TI)

## Diversité
- Varier les types de contrats: bail commercial, contrat de franchise, accord de licence logicielle, contrat de service professionnel, contrat de distribution
- Varier la complexité: clauses courtes (2 lignes) vs clauses longues (10 lignes)
- Inclure des clauses en français québécois courant et en français juridique formel
- Inclure des Non trompeurs: clauses qui semblent liées mais portent sur autre chose

## Do not use
- Clauses tirées de contrats américains (choix de loi: Delaware, New York)
- Clauses en common law anglaise
- Données de a2aj/canadian-laws