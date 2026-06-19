## Purpose
Identifier si la clause d'un accord de confidentialité canadien traite l'obligation de restituer ou détruire les informations confidentielles à la fin de l'accord (Oui/Non).

## Question format
Input: clause extraite d'un accord de confidentialité québécois ou canadien (en français).
Output: `Oui` | `Non`

**Exemple:**
> Clause: "Les parties s'engagent à ne divulguer à aucun tiers l'existence du présent accord."
> → Oui (si la tâche porte sur la confidentialité de l'accord lui-même)

## Positif — `Oui`
- La clause traite explicitement ou implicitement l'obligation de restituer ou détruire les informations confidentielles à la fin de l'accord
- La clause délimite les droits et obligations relatifs à ce sujet spécifique

## Positif — `Non`
- La clause porte sur un autre aspect de la confidentialité
- La clause est une clause générale d'accord de confidentialité sans dispositions sur ce sujet
- La clause traite d'un sujet adjacent (ex: durée) sans aborder l'obligation de restituer ou détruire les informations confidentielles à la fin de l'accord

## Sources légales
- Modèles d'accords de confidentialité (NDA) en droit québécois et canadien
- CCQ art. 1373-1379 (obligation de ne pas faire), 1434 (clauses implicites)
- Pratiques notariales québécoises en droit des affaires
- Barreaux provinciaux — modèles de contrats types

## Diversité
- Varier: NDA entre employeur-employé, entre entreprises, dans un contexte de fusion-acquisition
- Varier la formulation: explicite vs implicite, interdiction vs permission conditionnelle
- Inclure des clauses longues et complexes où le sujet est secondaire
- Inclure des clauses en français québécois courant et en français juridique formel

## Do not use
- US NDA boilerplate (governed by Delaware/NY law)
- UK NDA clauses
- Données de a2aj/canadian-laws (source d'entraînement de LexiorGPT)