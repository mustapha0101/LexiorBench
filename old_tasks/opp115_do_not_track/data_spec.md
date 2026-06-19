## Purpose
Identifier si un extrait de politique de confidentialité traite du sujet: **Do Not Track / désinscription du suivi** (Oui/Non).
Spécifiquement: la politique mentionne comment l'organisation répond aux signaux Do Not Track ou aux demandes de désinscription du suivi.

## Question format
Input: extrait d'une politique de confidentialité d'une organisation québécoise ou canadienne (en français).
Output: `Oui` | `Non`

**Exemple:**
> Extrait traitant de Do Not Track / désinscription du suivi: [clause décrivant Do Not Track / désinscription du suivi]
> → Oui

## Positif — `Oui`
- L'extrait traite explicitement ou implicitement de Do Not Track / désinscription du suivi
- la politique mentionne comment l'organisation répond aux signaux Do Not Track ou aux demandes de désinscription du suivi

## Positif — `Non`
- L'extrait traite d'un autre sujet de confidentialité non lié à Do Not Track / désinscription du suivi
- L'extrait mentionne le sujet de manière incidente sans l'aborder substantiellement

## Sources légales
- Loi 25 (Loi modernisant des dispositions législatives en matière de protection des renseignements personnels, LQ 2021 c 25)
- LPRPDE (LC 2000 c 5) et ses règlements
- Loi sur la protection des renseignements personnels dans le secteur public (RLRQ c A-2.1)
- Politiques de confidentialité d'entreprises québécoises publiées: Desjardins, Hydro-Québec, Bell, Vidéotron

## Diversité
- Varier les secteurs: finance, santé, commerce électronique, SaaS, médias sociaux
- Inclure des politiques bilingues (certains extraits en anglais pour le marché canadien)
- Inclure des formulations vagues vs très précises sur le sujet
- Inclure des Non trompeurs: extraits d'une politique de confidentialité qui parlent de RP sans aborder Do Not Track / désinscription du suivi

## Do not use
- Politiques de confidentialité d'entreprises purement américaines (CCPA, COPPA)
- Politiques conformes uniquement au RGPD (UE) sans dimension canadienne
- Données de a2aj/canadian-laws