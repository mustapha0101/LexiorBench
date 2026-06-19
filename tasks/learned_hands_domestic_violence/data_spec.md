## Purpose
Identifier si ce scénario soulève une question juridique liée à la violence conjugale ou familiale (protection, ordonnances, ressources légales).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon conjoint me bat régulièrement. J'ai peur de lui. Je veux partir mais j'ai peur qu'il me retrouve."
> → Oui

## Positif — `Oui`
- Demande d'ordonnance de protection ou de sauvegarde (CCQ art. 509-512, C.p.c.)
- Violence conjugale signalée à la police (Code criminel — voie de fait, harcèlement criminel)
- Droit de quitter le logement sans perdre ses droits au bail (CCQ art. 1974.1)
- Garde d'urgence des enfants dans un contexte de violence

## Négatif — `Non`
- Conflit familial sans violence (désaccord sur la garde uniquement)
- Violence entre voisins ou étrangers (responsabilité civile ou pénale ordinaire)
- Harcèlement psychologique au travail (LNT)

## Sources légales
- Code criminel (LRC 1985 c C-46): art. 264 (harcèlement), 267 (voie de fait avec lésions)
- CCQ art. 509-512 (ordonnance de protection)
- CCQ art. 1974.1 (résiliation de bail — violence conjugale)
- Loi visant à aider les personnes victimes d'infractions criminelles (RLRQ c A-13.2.1)

## Diversité
- Varier: violence physique, psychologique, économique, sexuelle
- Inclure: démarches d'urgence, ordonnances provisoires, maisons d'hébergement
- Inclure: situation des enfants témoins de violence
- Inclure des Non plausibles: conflits de garde sans violence, disputes de voisinage

## Ne pas utiliser
- US restraining order terminology (TRO, DVPO)
- Données de a2aj/canadian-laws