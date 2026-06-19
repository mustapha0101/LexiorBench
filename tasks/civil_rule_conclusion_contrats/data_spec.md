## Purpose
Déterminer si un contrat a été valablement formé selon les règles du CCQ (art. 1385-1415).

## Question format
Input: scénario décrivant un échange entre deux parties.
Output: `Oui` (contrat formé) | `Non` (pas de contrat valide)

**Exemple:**
> "Marie, âgée de 16 ans, signe seule un contrat d'abonnement de 12 000 $ pour des cours de conditionnement physique sur trois ans."
> → Non (incapacité du mineur, art. 153 CCQ)

## Positif — `Oui`
- Offre ferme + acceptation conforme + consentement libre et éclairé + objet licite + cause existante
- Contrat verbal valide (sauf exceptions de forme)
- Ratification d'un acte fait par un mineur

## Négatif — `Non`
- Absence d'offre (invitation à contracter seulement)
- Contre-offre (l'acceptation modifie l'offre — art. 1393 CCQ)
- Vice de consentement: erreur sur la nature, dol, crainte (art. 1399-1408 CCQ)
- Incapacité: mineur (art. 153), personne sous tutelle
- Objet illicite ou contraire à l'ordre public
- Formalité requise non respectée (donation par acte notarié, art. 1824 CCQ)

## Sources légales
- Art. 1385-1415 CCQ (formation du contrat)
- Art. 1398-1408 CCQ (vices du consentement)
- Art. 153-176 CCQ (capacité des mineurs)
- Art. 1410-1413 CCQ (objet et cause)

## Diversité
- Varier: contrats verbaux, écrits, électroniques
- Inclure: erreurs sur l'identité, sur la nature, dol par réticence
- Inclure: clauses abusives dans contrats de consommation (LPC)
- Inclure: contrats entre professionnels vs consommateurs

## Ne pas utiliser
- UCC (US)
- Common law offer and acceptance (use for English Canada tasks)
- Données de a2aj/canadian-laws