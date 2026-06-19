## Purpose
Déterminer si une divulgation de chaîne d'approvisionnement mentionne des AUDITS EFFECTIVEMENT RÉALISÉS (par opposition à une politique d'audit), conformément à la Loi S-211 (Canada, 2023).

## Question format
Input: extrait d'une divulgation annuelle d'entreprise.
Output: `Oui` | `Non`

**Exemple:**
> "En 2023, nous avons réalisé 47 audits chez nos fournisseurs de niveau 1 répartis dans 12 pays. Ces audits ont permis d'identifier 8 cas de non-conformité."
> → Oui

## Positif — `Oui`
- L'extrait rapporte des audits réellement menés (avec chiffres, dates, résultats)
- L'extrait donne des statistiques sur les audits effectués (nombre, couverture, findings)

## Positif — `Non`
- L'extrait décrit une politique ou un engagement futur (pas des audits déjà effectués)
- L'extrait mentionne des audits sans confirmer qu'ils ont eu lieu
- L'extrait rapporte des indicateurs autres que des audits (formations, certifications)

## Sources légales (idem best_practice_audits)
- Loi S-211 (LC 2023 c 9)
- Rapports de divulgation publics déposés sous S-211

## Diversité
- Contraster avec best_practice_audits: ici on veut des audits passés, pas de politiques futures
- Inclure: audits avec et sans résultats publiés, audits internes vs externes
- Inclure des Non trompeurs: "nous prévoyons d'effectuer des audits l'an prochain"

## Ne pas utiliser
- California TISCA disclosures
- Données de a2aj/canadian-laws