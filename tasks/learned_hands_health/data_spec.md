## Purpose
Identifier si ce scénario soulève une question de droit de la santé (consentement aux soins, responsabilité médicale, droits du patient).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon médecin a fait une erreur de diagnostic qui a retardé mon traitement de cancer de 8 mois. Mon cancer a progressé au stade 3."
> → Oui

## Positif — `Oui`
- Responsabilité médicale ou hospitalière (CCQ art. 1457 + Loi médicale)
- Défaut de consentement éclairé aux soins (CCQ art. 10-14, Loi sur les services de santé)
- Refus de soins par un professionnel de la santé
- Divulgation non autorisée de renseignements médicaux (Loi sur les services de santé art. 19)
- Soins contre le gré d'un patient inapte (CCQ art. 11-23)

## Négatif — `Non`
- Litige avec une assurance-maladie complémentaire (droit des assurances, pas droit de la santé)
- Litige d'emploi d'un professionnel de la santé (droit du travail)
- Remboursement de médicaments par la RAMQ (droit administratif)

## Sources légales
- CCQ art. 10-25 (intégrité de la personne, consentement)
- Loi sur les services de santé et les services sociaux (RLRQ c S-4.2)
- Code de déontologie des médecins (RLRQ c M-9, r 17)
- Loi médicale (RLRQ c M-9)
- Décisions CanLII: Cour supérieure QC (responsabilité médicale)

## Diversité
- Varier: erreur chirurgicale, erreur de diagnostic, erreur médicamenteuse
- Inclure: patients hospitalisés vs ambulatoires, urgences
- Inclure: consentement d'un mineur, d'un inapte, refus de transfusion
- Inclure des Non plausibles: litige avec une mutuelle d'assurance médicale

## Ne pas utiliser
- HIPAA, ACA, Medicaid (US)
- Données de a2aj/canadian-laws