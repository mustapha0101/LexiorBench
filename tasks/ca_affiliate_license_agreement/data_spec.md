## Purpose
Identifier si une clause d'un contrat commercial québécois ou canadien accorde une licence
aux sociétés affiliées du preneur de licence (Oui/Non).

## Question format
**Input:** Une clause extraite d'un contrat commercial en français (bail, franchise,
licence logicielle, contrat de service, distribution, PI) — 2 à 15 lignes.
**Output:** `Oui` | `Non`

**Définition opérationnelle :**
`Oui` — la clause étend expressément ou nécessairement les droits du preneur de licence
à ses sociétés affiliées (filiales, sociétés mères, sociétés sœurs, entités sous contrôle commun).
`Non` — la clause ne porte pas sur l'extension de droits à des affiliées, même si elle
les mentionne dans un autre contexte (confidentialité, non-concurrence, cession, etc.).

## Label criteria

### Oui
- La clause octroie explicitement au preneur le droit de faire bénéficier ses affiliées de la licence
- La clause autorise le preneur à sous-licencier à des entités sous contrôle commun
- La clause définit le « preneur » de façon à inclure les sociétés affiliées du preneur
- La clause permet l'utilisation des droits licenciés par les filiales ou sociétés sœurs du preneur

### Non
- La clause porte sur les affiliées dans le contexte de la confidentialité ou du secret d'affaires
- La clause mentionne les affiliées pour restreindre leurs activités (non-concurrence, non-débauchage)
- La clause traite de la cession ou du transfert de contrat en cas de changement de contrôle
- La clause concerne la propriété intellectuelle sans octroyer de droits aux affiliées du preneur
- La clause est une garantie, une déclaration ou une représentation générale

## Legal sources
- **CCQ art. 1375–1432** — règles générales des contrats, interprétation, bonne foi
- **CCQ art. 1717–1722** — cession de créance et de contrat
- **Loi sur les marques de commerce, LRC 1985 c T-13** — licences de marque, art. 50 (licence d'emploi et affiliées)
- **Loi sur le droit d'auteur, LRC 1985 c C-42** — licences d'auteur, exclusivité
- **Pratique contractuelle des barreaux du Québec et du Barreau du Haut-Canada** — clauses standard NDA, licences logicielles, franchises

## Diversity requirements
- **Vary contract type** (minimum 3 types per 10 examples):
  bail commercial, contrat de franchise, accord de licence logicielle, contrat de service
  professionnel, contrat de distribution, accord de propriété intellectuelle, entente de
  confidentialité (NDA)
- **Vary clause complexity**: 2–3 lignes (simples) vs. 8–15 lignes (complexes avec définitions enchâssées)
- **Vary language register**: français québécois courant vs. français juridique formel
- **Non trompeurs** (≥40% des Non): clauses qui mentionnent des affiliées dans un autre
  contexte (confidentialité, non-concurrence, changement de contrôle) — l'affiliée est
  présente dans le texte mais la clause n'étend pas de droits de licence
- **Label balance**: strictement 50% Oui / 50% Non — jamais d'écart de plus de 1

## Do not use
- Clauses issues de contrats américains (choix de loi: Delaware, New York, California)
- Clauses en common law anglaise sans adaptation au droit québécois
- Données de a2aj/canadian-laws (risque de fuite de données)
- Clauses dont la qualification Oui/Non est ambiguë sans lecture du contrat complet
