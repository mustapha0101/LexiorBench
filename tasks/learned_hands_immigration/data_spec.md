## Purpose
Identifier si ce scénario soulève une question de droit de l'immigration canadienne (LIPR, visa, statut, réfugié).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon visa étudiant expire dans 4 semaines et ma demande de renouvellement est toujours en traitement. Puis-je continuer mes études?"
> → Oui

## Positif — `Oui`
- Statut de résident permanent, visa temporaire, visa étudiant, permis de travail
- Demande d'asile / protection des réfugiés (LIPR art. 95+)
- Renvoi ou déportation (mesure d'interdiction de séjour ou d'expulsion)
- Parrainage familial (LIPR art. 12(1))
- Citoyenneté canadienne (Loi sur la citoyenneté)

## Négatif — `Non`
- Litige de travail d'un travailleur étranger (droit du travail distinct de l'immigration)
- Conflit familial entre citoyens canadiens sans question d'immigration
- Reconnaissance de diplômes étrangers (hors processus d'immigration)

## Sources légales
- Loi sur l'immigration et la protection des réfugiés (LIPR, LC 2001 c 27)
- Règlement sur l'immigration et la protection des réfugiés (RIPR, DORS/2002-227)
- Loi sur la citoyenneté (LRC 1985 c C-29)
- IRCC (Immigration, Réfugiés et Citoyenneté Canada) — guides publics

## Diversité
- Varier: résident temporaire, permanent, demandeur d'asile, travailleur étranger
- Inclure: prolongation de statut, "implied status", perte de statut
- Inclure: CISR (Commission de l'immigration et du statut de réfugié)
- Inclure des Non plausibles: litige de travail avec un immigrant (pas une question d'immigration)

## Ne pas utiliser
- US immigration law (USCIS, DACA, H-1B)
- Données de a2aj/canadian-laws