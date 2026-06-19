## Purpose
Évaluer si un document juridique respecte les exigences de forme du Code de procédure civile du Québec (C.p.c.) et identifier les lacunes.

## Question format
Input: document juridique rédigé (mise en demeure, demande introductive d'instance, etc.).
Output: évaluation de la conformité au C.p.c. + liste des lacunes (génération libre).

**Exemple:**
> Document: [mise en demeure rédigée]
> Cette mise en demeure respecte-t-elle les exigences des art. 110-111 C.p.c.? Identifiez les lacunes s'il y en a.

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- Identification correcte du type de document et des articles applicables (20%)
- Vérification de tous les éléments obligatoires (nom des parties, objet, délai, conséquences) (40%)
- Identification précise des lacunes avec référence à l'article violé (30%)
- Suggestion concrète de correction (10%)

## Types de documents à couvrir
- Mise en demeure (C.p.c. art. 110-111)
- Demande introductive d'instance (C.p.c. art. 141-148)
- Déclaration sous serment / affidavit (C.p.c. art. 86-88)
- Inscription pour instruction et jugement (C.p.c. art. 172-173)

## Sources
- Code de procédure civile du Québec (RLRQ c C-25.01)
- Collection Barreau du Québec — procédure civile
- Modèles de documents judiciaires (Wilson & Lafleur)
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité des documents de test
- Inclure des documents conformes (réponse: aucune lacune)
- Inclure des documents avec 1-2 lacunes mineures
- Inclure des documents avec lacunes majeures (vices de forme invalidants)
- Varier les types: mise en demeure, demande, affidavit

## Do not use
- Federal Rules of Civil Procedure (US)
- Rules of Civil Procedure (Ontario)