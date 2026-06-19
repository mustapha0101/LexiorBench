## Purpose
Déterminer si une divulgation de chaîne d'approvisionnement décrit des pratiques ou politiques d'AUDIT des fournisseurs, conformément à la Loi sur la lutte contre le travail forcé et le travail des enfants (Canada, Loi S-211, 2023).

## Question format
Input: extrait d'une divulgation annuelle d'entreprise.
Output: `Oui` | `Non`

**Exemple:**
> "Notre politique de chaîne d'approvisionnement prévoit des audits annuels de nos fournisseurs de niveau 1 afin de détecter toute situation de travail forcé."
> → Oui

## Positif — `Oui`
- L'extrait mentionne explicitement des audits, vérifications, inspections de fournisseurs
- L'extrait décrit une politique d'audit (calendrier, portée, méthode)
- L'extrait signale qu'un tiers effectue des audits pour le compte de l'entreprise

## Positif — `Non`
- L'extrait discute de formation ou de certification mais pas d'audit
- L'extrait mentionne des audits financiers (hors périmètre S-211)
- L'extrait décrit des mesures de diligence raisonnable sans audit formel

## Sources légales
- Loi sur la lutte contre le travail forcé et le travail des enfants dans les chaînes d'approvisionnement (Canada, LC 2023 c 9) — Loi S-211
- Rapports de divulgation déposés auprès du gouvernement du Canada (registre public obligatoire)
- Lignes directrices du gouvernement canadien sur la Loi S-211

## Diversité
- Varier les secteurs: manufacturier, ressources naturelles, vêtements, électronique, alimentation
- Inclure: audits annoncés vs inopinés, audits de premier vs deuxième vs troisième niveau
- Inclure des Non trompeurs: divulgations qui mentionnent la S-211 mais décrivent autre chose

## Ne pas utiliser
- California Transparency in Supply Chains Act (US)
- UK Modern Slavery Act
- Données de a2aj/canadian-laws