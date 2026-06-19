## Purpose
Identifier si ce scénario soulève une question de procédure judiciaire ou de droits du justiciable devant les tribunaux québécois ou canadiens.

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai reçu une mise en demeure d'un avocat me réclamant 8 000$. Je conteste totalement la dette. Comment contester?"
> → Oui

## Positif — `Oui`
- Question sur la compétence d'un tribunal (Cour du Québec, Cour supérieure, petites créances)
- Droits en tant que partie à une instance (délais, signification, représentation)
- Question sur une ordonnance, injonction, ou mesure provisoire
- Accès à l'aide juridique
- Appel d'un jugement

## Négatif — `Non`
- Question de fond sur le droit substantif (responsabilité civile, droit du travail)
- Question de droit administratif (appel d'une décision d'organisme gouvernemental)
- Question d'arbitrage commercial

## Sources légales
- Code de procédure civile du Québec (C.p.c., RLRQ c C-25.01)
- Loi sur les tribunaux judiciaires (RLRQ c T-16)
- Règles des petites créances (C.p.c. art. 536-583)
- Loi sur l'aide juridique (RLRQ c A-14)

## Diversité
- Varier: petites créances, chambre civile, chambre commerciale
- Inclure: délais de prescription, dépôt de la demande, signification
- Inclure: représentation par avocat, auto-représentation, aide juridique

## Ne pas utiliser
- Federal Rules of Civil Procedure (US)
- Common law provincial procedure rules