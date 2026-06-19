## Purpose
Identifier si ce scénario soulève une question juridique liée à la protection du consommateur (LPC, garantie légale, pratiques commerciales déloyales).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai acheté un lave-vaisselle neuf il y a 8 mois. Il est déjà brisé. Le vendeur refuse la garantie légale et dit que j'aurais dû prendre l'assurance étendue."
> → Oui

## Positif — `Oui`
- Vendeur refuse d'honorer la garantie légale de bon fonctionnement (LPC art. 37-38)
- Représentation fausse ou trompeuse dans une publicité ou une vente (LPC art. 219+)
- Clause abusive dans un contrat de consommation (LPC art. 8)
- Contrat à distance ou à exécution successive avec droit de résiliation (LPC art. 54.4+)
- Prix affiché non respecté

## Négatif — `Non`
- Litige entre deux commerçants (pas un contrat de consommation)
- Litige de bail résidentiel (Loi sur le bail, pas LPC)
- Litige de service professionnel réglementé (médecin, avocat)

## Sources légales
- Loi sur la protection du consommateur (RLRQ c P-40.1)
- Office de la protection du consommateur (OPC) — guides d'application
- CCQ art. 1384, 1386 (contrat de consommation)
- Décisions du Tribunal de protection du consommateur / petites créances QC

## Diversité
- Varier: bien meuble, service, contrat électronique, vente itinérante, crédit
- Inclure: pratiques de vente sous pression, vente pyramidale, faux soldes
- Inclure des Non plausibles: disputes entre particuliers, services professionnels

## Ne pas utiliser
- FTC regulations (US)
- Consumer Protection Act (Ontario)
- Données de a2aj/canadian-laws