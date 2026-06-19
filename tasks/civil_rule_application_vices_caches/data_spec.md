## Purpose
Appliquer les règles des vices cachés (art. 1726-1731 CCQ) à un scénario d'achat immobilier ou mobilier au Québec.

## Question format
Input: scénario d'achat avec description d'un défaut découvert après la vente.
Output: `Oui` (vice caché probable) | `Non` (pas un vice caché ou recours exclu)

**Exemple:**
> "Des fissures importantes aux fondations, dissimulées par le vendeur derrière un revêtement neuf, sont découvertes trois mois après l'achat."
> → Oui

## Positif — `Oui`
- Défaut existait au moment de la vente (pas causé par l'acheteur)
- Défaut n'était pas apparent lors d'un examen ordinaire
- Défaut rend le bien impropre à l'usage ou diminue l'usage de façon importante
- Acheteur n'avait pas connaissance du défaut

## Négatif — `Non`
- Défaut était apparent (visible lors d'une inspection ordinaire)
- Acheteur a acheté "tel quel" avec clause d'exclusion valide (sans dol du vendeur)
- Défaut causé par l'acheteur après la vente
- Bien vendu entre professionnels avec exclusion contractuelle valide
- Délai de dénonciation dépassé sans excuse valable

## Sources légales
- Art. 1726, 1727, 1728, 1729, 1730, 1731 CCQ
- Décisions CanLII: Cour du Québec (petites créances + chambre civile), Cour supérieure QC
- Loi sur le bâtiment (art. 2118 CCQ pour immeubles neufs)

## Diversité
- Inclure: immeubles résidentiels, copropriétés, véhicules, équipements
- Varier: nature du défaut (fondations, toiture, plomberie, électricité, contamination)
- Inclure: clause "tel quel" valide vs invalide (dol du vendeur)
- Inclure: délai de dénonciation (raisonnable vs tardif)

## Ne pas utiliser
- Droit américain (implied warranty of habitability)
- Common law provinces (Sale of Goods Act)
- Données de a2aj/canadian-laws