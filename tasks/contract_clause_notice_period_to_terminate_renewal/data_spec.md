## Purpose
Identifier si une clause d'un contrat commercial québécois ou canadien constitue une clause de préavis de résiliation ou non-renouvellement (Oui/Non).

## Question format
**Input:** Une clause extraite d'un contrat commercial en français (bail, franchise, licence, service, distribution, PI) — 2 à 15 lignes.
**Output:** `Oui` | `Non`

**Définition opérationnelle :**
La clause est classifiée `Oui` si elle contient ou constitue une clause fixant le délai de préavis requis pour résilier le contrat ou s'opposer à son renouvellement automatique.
La clause est classifiée `Non` si elle porte sur un autre sujet contractuel ou ne contient aucune disposition préavis de résiliation ou non-renouvellement.

## Label criteria

### Oui
- La clause traite explicitement du sujet visé
- La clause implique nécessairement le sujet même sans le nommer directement
- La clause définit des droits ou obligations spécifiques liés à ce type de disposition

### Non
- La clause porte sur un autre sujet contractuel
- La clause effleure le sujet de manière incidente sans en faire l'objet principal
- Clause générale de représentations et garanties sans spécificité

## Legal sources
- **CCQ art. 1375–1432** — règles générales des contrats, interprétation, bonne foi
- **CCQ art. 1717–1722** — cession de créance et de contrat
- **Loi sur les marques de commerce, LRC 1985 c T-13**
- **Loi sur le droit d'auteur, LRC 1985 c C-42**
- **Pratique contractuelle des barreaux du Québec et du Barreau du Haut-Canada**

## Diversity requirements
- Varier les types de contrats (bail, franchise, licence logicielle, service, distribution, PI)
- Varier la complexité des clauses (2–3 lignes vs 10–15 lignes)
- Inclure des `Non` trompeurs : clauses adjacentes au sujet sans le couvrir directement
- Équilibre strict 50 % Oui / 50 % Non (± 1)

## Do not use
- Clauses issues de contrats américains (choix de loi: Delaware, New York)
- Données de a2aj/canadian-laws (risque de fuite de données)
- Clauses ambiguës sans qualification claire
