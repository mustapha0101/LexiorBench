## Purpose
Determiner si une divulgation de chaine d'approvisionnement decrit des certifications de fournisseurs EFFECTIVEMENT OBTENUES (pas seulement exigées) (ACTIVITE EFFECTIVEMENT REALISEE), conformement a la Loi S-211 (Canada, 2023) (Oui/Non).

## Question format
Input: extrait d'une divulgation annuelle d'entreprise.
Output: `Oui` | `Non`

**Exemple:** ex: 'Au 31 décembre 2023, 78% de nos fournisseurs de niveau 1 détenaient une certification SA8000 ou équivalente.'
-> Oui

## Distinction cle: best_practice vs disclosed
- **best_practice**: politique, engagement, ou pratique *prevue* (present ou futur)
- **disclosed**: activite *effectivement realisee* au cours de l'annee de rapport (passe avec chiffres)

Cette tache porte sur: **ACTIVITE EFFECTIVEMENT REALISEE**

## Positif — `Oui`
- L'extrait decrit une realisation concrete portant sur des certifications de fournisseurs EFFECTIVEMENT OBTENUES (pas seulement exigées)
- Formulations typiques: "en 2023, nous avons", "au cours de l exercice", chiffres concrets (nombre, %, dates)

## Positif — `Non`
- L'extrait porte sur un autre aspect de la divulgation S-211 (audits, accountability, training, verification)
- L'extrait est une politique future (relevant plutot de best_practice)

## Sources legales
- Loi sur la lutte contre le travail force et le travail des enfants dans les chaines d'approvisionnement (Canada, LC 2023 c 9) — Loi S-211
- Registre public des rapports S-211 (gouvernement du Canada)
- Rapport annuel S-211 type — guide du gouvernement du Canada

## Diversite
- Varier les secteurs: manufacturier, ressources naturelles, textile, alimentation, electronique
- Inclure des divulgations avec chiffres precis vs divulgations vagues
- Inclure des Non trompeurs: divulgations mentionnant S-211 mais decrivant un autre aspect

## Do not use
- California TISCA ou UK Modern Slavery Act
- Donnees de a2aj/canadian-laws