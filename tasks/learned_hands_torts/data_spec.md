## Purpose
Identifier si ce scénario soulève une question de responsabilité civile extracontractuelle (art. 1457 CCQ) distincte du domaine contractuel.

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Un chien de mon voisin m'a mordu profondément à la jambe alors que je marchais sur le trottoir. J'ai dû subir plusieurs points de suture."
> → Oui

## Positif — `Oui`
- Blessure causée par un animal (CCQ art. 1466)
- Accident causé par un bien sous la garde d'autrui (CCQ art. 1465)
- Atteinte à la réputation / diffamation (CCQ art. 1457)
- Invasion de la vie privée (CCQ art. 35-41)
- Nuisance causant un préjudice réel (art. 976 CCQ)

## Négatif — `Non`
- Blessure couverte par la CNESST (accident du travail — exclusion légale de la RC)
- Accident de voiture (SAAQ couvre les dommages corporels — régime sans faute)
- Inexécution d'un contrat (responsabilité contractuelle — art. 1458 CCQ)

## Sources légales
- CCQ art. 1457-1481 (responsabilité civile)
- Loi sur l'assurance automobile (RLRQ c A-25) — régime sans faute QC
- Loi sur les accidents du travail et les maladies professionnelles (LATMP, RLRQ c A-3.001)
- Décisions CanLII: Cour du Québec, Cour supérieure QC

## Diversité
- Varier: blessures corporelles, préjudice moral, dommages matériels
- Inclure: défense de force majeure, fait de la victime, fait d'un tiers
- Inclure des exclusions importantes: SAAQ (accident de voiture), CNESST (travail)
- Inclure des Non plausibles: réclamation sous contrat d'assurance (pas RC directe)

## Ne pas utiliser
- Common law torts (negligence, battery — use for English Canada tasks)
- Workers' compensation exclusion from non-QC provinces