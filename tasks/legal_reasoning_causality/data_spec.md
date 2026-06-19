## Purpose
Identifier si un extrait judiciaire s'appuie sur des preuves statistiques ou épidémiologiques pour établir la causalité (Oui/Non).

## Question format
Input: extrait d'une décision judiciaire canadienne.
Output: `Oui` | `Non`

**Exemple:**
> "Les données épidémiologiques présentées par l'expert démontrent une corrélation statistiquement significative (risque relatif > 2) entre l'exposition au benzène et la leucémie."
> → Oui

## Positif — `Oui`
- Extrait mentionne une étude épidémiologique, un risque relatif, une méta-analyse
- Expert utilise des statistiques pour établir ou contester un lien de causalité
- Extrait discute de la causalité probabiliste (balance des probabilités, Snell c Farrell)
- Tribunal évalue la crédibilité d'une preuve d'expert chiffrée

## Négatif — `Non`
- Extrait établit la causalité par la logique factuelle sans données statistiques
- Extrait discute de causalité mais uniquement par témoignage de faits
- Extrait présente une statistique descriptive sans raisonnement causal

## Sources légales
- Clements c Clements, 2012 CSC 32 (causalité en responsabilité civile)
- Snell c Farrell, [1990] 2 RCS 311 (causalité médicale)
- Laferrière c Lawson, [1991] 1 RCS 541
- Décisions CanLII impliquant des preuves d'expert en responsabilité médicale, environnementale, tabac

## Diversité
- Varier: responsabilité médicale, exposition environnementale, tabac, amiante, produits pharmaceutiques
- Inclure des Non trompeurs: extraits qui discutent de statistiques sans les utiliser pour la causalité
- Inclure des extraits d'expertises rejetées (le tribunal dit que la preuve statistique est insuffisante)

## Ne pas utiliser
- Daubert standard (US)
- Données de a2aj/canadian-laws