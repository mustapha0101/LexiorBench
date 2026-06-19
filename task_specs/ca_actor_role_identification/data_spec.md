## Purpose
Identifier tous les acteurs juridiques mentionnés dans un extrait de décision canadienne et préciser leur rôle (demandeur, défendeur, juge, expert, intervenant, appelant, intimé).

## Question format
Input: extrait d'une décision judiciaire canadienne.
Output: liste des acteurs + leur rôle (extraction structurée).

**Exemple:**
> "La Cour d'appel accueille le pourvoi de M. Tremblay et infirme le jugement de première instance rendu en faveur de la compagnie Assurances XYZ Inc. Le juge Leblanc, dissident, aurait maintenu la décision."
> → Appelant: M. Tremblay | Intimée: Assurances XYZ Inc. | Juge dissident: Leblanc

## Rôles à identifier
- **Appelant / Demandeur en cassation**: partie qui interjette appel
- **Intimé / Défendeur en appel**: partie qui défend le jugement attaqué
- **Demandeur / Requérant** (première instance)
- **Défendeur** (première instance)
- **Juge**: juge(s) avec nom, mention dissidence si applicable
- **Expert**: témoin expert et sa spécialité
- **Intervenant**: tiers autorisé à présenter des arguments
- **Procureur général**: intervenant gouvernemental fréquent devant CSC

## Sources
- Décisions CanLII avec structure multipartite complexe: CSC (intervenants fréquents), CA-QC (parties multiples)
- Arrêts avec dissidences, jugements unanimes, parties multiples
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier: décisions avec 2 parties vs décisions multipartites (4+ parties)
- Inclure: intervenants (Procureur général du Canada, organismes tiers)
- Inclure: recours collectifs (représentants d'un groupe)
- Inclure des extraits où le rôle d'une partie est ambigu

## Format de sortie attendu
Tableau ou liste structurée: Rôle: Nom (indicateur de partie si personne morale ou physique)

## Do not use
- Rôles propres au système américain (District Attorney, Public Defender)
- Données de a2aj/canadian-laws