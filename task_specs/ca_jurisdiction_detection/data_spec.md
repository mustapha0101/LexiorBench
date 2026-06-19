## Purpose
Identifier si une règle juridique décrite appartient au droit canadien/québécois ou à une juridiction étrangère (UE, USA, autre) — classification 4 classes.

## Question format
Input: description d'une règle juridique (sans nommer la juridiction).
Output: `CA/QC` | `UE` | `USA` | `Autre`

**Exemple:**
> "Toute organisation traitant des données personnelles doit nommer un délégué à la protection des données et notifier les violations dans les 72 heures."
> → UE (RGPD — la Loi 25 n'exige pas de DPO ni le délai de 72h)

## Classes
- **CA/QC**: règle de la Loi 25, LPRPDE, CCQ, LPC, LNT, Code criminel, Loi sur le divorce, etc.
- **UE**: règle du RGPD, directive européenne, droit civil français, etc.
- **USA**: règle de la FTC, CCPA, HIPAA, Miranda, 4e amendement, etc.
- **Autre**: autre pays (UK, Australie, international)

## Sources légales pour CA/QC (positifs)
- Loi 25 (QC), LPRPDE (CA), CCQ, LPC, LNT, Code canadien du travail, Loi sur la citoyenneté, Charte québécoise

## Diversité
- Varier les domaines: vie privée, contrats, travail, procédure, droit pénal, immigration
- Inclure des règles qui existent dans plusieurs juridictions mais avec des différences (droit à l'oubli: QC oui (désindexation L25), UE oui (RGPD), USA non)
- Inclure des règles exclusivement canadiennes sans équivalent américain ou européen
- Équilibrer les 4 classes (~25% chacune)

## Do not use
- Questions trop faciles (mentionnant explicitement la juridiction dans la règle)
- Données de a2aj/canadian-laws