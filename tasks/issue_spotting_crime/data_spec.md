## Purpose
Identifier si une description de problème légal relève du domaine du droit criminel et pénal au Québec ou au Canada (Oui/Non).

## Question format
**Input:** Un court paragraphe (50–200 mots) décrivant un problème légal vécu par une personne.
**Output:** `Oui` | `Non`

**Définition opérationnelle :**
`Oui` — le problème principal décrit relève du domaine du droit criminel et pénal selon le droit québécois ou canadien.
`Non` — le problème relève d'un autre domaine juridique, ou il n'y a pas de question légale identifiable.

## Typical issues covered
accusations criminelles, droits de l'accusé, détention, procédure pénale

## Label criteria

### Oui
- Le problème principal appartient au domaine cible
- Le problème comporte un élément accessoire d'un autre domaine mais son nœud est dans le domaine cible

### Non
- Le domaine principal est différent (même si le domaine cible est mentionné accessoirement)
- La situation décrite n'est pas un problème juridique

## Legal sources
- Droit québécois et fédéral canadien applicable au domaine
- Jurisprudence Cour du Québec, Cour supérieure, CSC

## Diversity requirements
- Varier la complexité des scénarios (simple vs multi-enjeux)
- Inclure des `Non` trompeurs : problèmes d'un domaine adjacent
- Équilibre strict 50 % Oui / 50 % Non (± 1)

## Do not use
- Scénarios basés sur le droit américain
- Données de a2aj/canadian-laws
