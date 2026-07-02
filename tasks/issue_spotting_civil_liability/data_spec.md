## Purpose
Identifier si une description de problème légal relève de la responsabilité civile extracontractuelle québécoise (Oui/Non).

## Question format
**Input:** Un court paragraphe (50–200 mots) décrivant un problème légal vécu par une personne.
**Output:** `Oui` | `Non`

**Définition opérationnelle :**
`Oui` — le problème principal décrit relève de la responsabilité civile extracontractuelle selon le droit québécois.
`Non` — le problème relève d'un autre domaine juridique, ou il n'y a pas de question légale identifiable.

## Typical issues covered
négligence, faute, préjudice, recours en dommages-intérêts

## Label criteria

### Oui
- Le problème principal appartient au domaine cible
- Le problème comporte un élément accessoire d'un autre domaine mais son nœud est dans le domaine cible

### Non
- Le domaine principal est différent (même si le domaine cible est mentionné accessoirement)
- La situation décrite n'est pas un problème juridique

## Legal sources
- Droit québécois applicable à la responsabilité civile extracontractuelle
- Jurisprudence Cour du Québec, Cour supérieure, CSC

## Diversity requirements
- Varier la complexité des scénarios (simple vs multi-enjeux)
- Inclure des `Non` trompeurs : problèmes d'un domaine adjacent
- Équilibre strict 50 % Oui / 50 % Non (± 1)

## Do not use
- Scénarios basés sur le droit américain
- Données de a2aj/canadian-laws
