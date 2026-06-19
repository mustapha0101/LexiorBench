## Purpose
Determiner si une divulgation de chaine d'approvisionnement decrit des processus de vérification ou de diligence raisonnable sur les pratiques de travail des fournisseurs (POLITIQUE / PRATIQUE PREVUE), conformement a la Loi S-211 (Canada, 2023) (Oui/Non).

## Question format
Input: extrait d'une divulgation annuelle d'entreprise.
Output: `Oui` | `Non`

**Exemple:** ex: 'Nous effectuons une vérification des antécédents en matière de droits de la personne de tous les nouveaux fournisseurs avant leur homologation.'
-> Oui

## Distinction cle: best_practice vs disclosed
- **best_practice**: politique, engagement, ou pratique *prevue* (present ou futur)
- **disclosed**: activite *effectivement realisee* au cours de l'annee de rapport (passe avec chiffres)

Cette tache porte sur: **POLITIQUE / PRATIQUE PREVUE**

## Positif — `Oui`
- L'extrait decrit une politique ou un engagement relatif a des processus de vérification ou de diligence raisonnable sur les pratiques de travail des fournisseurs
- Formulations typiques: "nous nous engageons a", "notre politique prevoit", "nous exigeons de nos fournisseurs"

## Positif — `Non`
- L'extrait porte sur un autre aspect de la divulgation S-211 (audits, accountability, certification, training)
- L'extrait est une realisation passee (relevant plutot de disclosed)

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