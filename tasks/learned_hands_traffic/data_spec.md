## Purpose
Identifier si ce scénario soulève une question de droit routier ou de contravention québécoise (Code de la sécurité routière, contestation d'infraction).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai reçu un constat d'infraction pour avoir grillé un feu rouge. Je suis certain que le feu était vert. Comment contester ce constat?"
> → Oui

## Positif — `Oui`
- Contestation d'un constat d'infraction (Code de la sécurité routière — RLRQ c C-24.2)
- Suspension de permis de conduire (points de démérite, alcool au volant)
- Infraction au Code criminel liée à la conduite (art. 320.11+ CCC)
- Responsabilité civile pour accident de voiture (régime SAAQ — dommages corporels)
- Saisie ou remorquage illégal d'un véhicule

## Négatif — `Non`
- Réclamation pour dommages matériels à un véhicule entre particuliers (responsabilité civile ordinaire, pas régime SAAQ)
- Litige d'assurance automobile (contrat d'assurance, pas infraction routière)
- Accident impliquant un véhicule hors route (différentes règles)

## Sources légales
- Code de la sécurité routière (RLRQ c C-24.2)
- Loi sur l'assurance automobile (RLRQ c A-25) — régime no-fault
- Code criminel art. 320.11-320.22 (infractions liées à la conduite)
- Loi sur les infractions et les peines (contestation de constats)

## Diversité
- Varier: excès de vitesse, feu rouge, alcool au volant, utilisation du cellulaire, permis suspendu
- Inclure: délai pour contester, fardeau de la preuve devant la Cour municipale
- Inclure: impacts sur l'assurance automobile suite à des infractions
- Inclure des Non plausibles: accident impliquant un cycliste (RC extracontractuelle)

## Ne pas utiliser
- Traffic laws from US states
- Ontario Highway Traffic Act
- Données de a2aj/canadian-laws