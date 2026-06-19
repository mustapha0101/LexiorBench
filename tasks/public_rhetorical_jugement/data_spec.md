## Purpose
Identifier la fonction rhétorique d'un extrait d'un jugement canadien (énoncé des faits, règle de droit, application, ou conclusion).

## Question format
Input: extrait d'un jugement canadien.
Output: `Faits` | `Règle` | `Application` | `Conclusion`

**Exemple:**
> "La Cour doit faire preuve de déférence à l'égard de la décision du Tribunal administratif et n'interviendra que si celle-ci est déraisonnable."
> → Règle

## Classes
- **Faits**: résume ou décrit les événements factuels, le contexte, les antécédents
- **Règle**: énonce un principe juridique, une présomption, un critère légal
- **Application**: applique la règle aux faits de l'espèce, raisonne vers un résultat
- **Conclusion**: annonce la décision finale (accueillie, rejetée, renvoyée)

## Sources légales
- Décisions CanLII: CSC, CA-QC, Cour fédérale, Cour du Québec
- Arrêts avec raisonnement IRAC explicite: Vavilov, Doré, Jordan, Clements

## Diversité
- Couvrir tous les 4 types de fonctions
- Varier les domaines: droit administratif, criminel, civil, familial
- Inclure des extraits ambigus (Application qui ressemble à une Règle)
- Équilibrer les 4 classes (25% chacune approximativement)

## Ne pas utiliser
- Décisions américaines ou de common law étrangère
- Données de a2aj/canadian-laws