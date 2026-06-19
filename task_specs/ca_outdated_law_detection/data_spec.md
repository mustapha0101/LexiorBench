## Purpose
Détecter si une question ou un énoncé juridique fait référence à une loi obsolète ou abrogée, et citer la version actuelle applicable.

## Question format
Input: question ou énoncé contenant une référence légale (potentiellement périmée).
Output: `Oui` (référence périmée) | `Non` (référence à jour) + correction si Oui.

**Exemple:**
> "Selon l'art. 1056 C.c.B.-C., quels sont les délais de prescription en responsabilité civile?"
> → Oui — le Code civil du Bas-Canada a été remplacé par le CCQ le 1er janvier 1994. L'article pertinent est maintenant art. 2925 CCQ (prescription de 3 ans).

## Positif — `Oui` (référence périmée)
- Référence au C.c.B.-C. (remplacé par CCQ en 1994)
- Référence à la Loi sur la protection du consommateur avant les amendements de 2017 ou 2023
- Référence à Dunsmuir (remplacé par Vavilov 2019) comme critère de contrôle judiciaire
- Référence à la Loi sur les jeunes contrevenants (remplacée par LSJPA en 2003)
- Référence à une version d'une loi modifiée depuis

## Positif — `Non` (référence à jour)
- Référence correcte au CCQ, LPC, LNT, Code criminel dans leur version actuelle
- Référence à un arrêt toujours bon droit (Clements, Vavilov, Jordan)

## Sources
- Historique législatif québécois et fédéral (légisQuébec.gouv.qc.ca, justice.gc.ca)
- Table des lois abrogées ou remplacées
- Répertoire de jurisprudence CanLII pour identifier les arrêts overrulés
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier les époques: pré-1994 (C.c.B.-C.), 1994-2015, 2015-aujourd'hui
- Inclure des amendements récents de la Loi 25 (2022-2023)
- Inclure des arrêts overrulés vs arrêts toujours bon droit
- ~40% Non (références à jour) pour équilibrer

## Do not use
- Références à des lois américaines (toujours hors périmètre)
- Lois hypothétiques ou inventées