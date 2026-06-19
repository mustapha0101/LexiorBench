## Purpose
Déterminer si un extrait de politique de confidentialité implique que l'entreprise effectue l'action X, selon les exigences de la Loi 25 (QC) et LPRPDE (CA).

## Question format
Input: extrait de politique de confidentialité + description d'une action.
Output: `Oui` (l'extrait implique l'action) | `Non` (l'extrait ne l'implique pas ou la nie)

**Exemple:**
> "Nous partageons vos renseignements personnels avec nos partenaires commerciaux à des fins de marketing ciblé."
> Action: "L'entreprise communique des RP à des tiers."
> → Oui

## Positif — `Oui`
- L'extrait décrit explicitement l'action (partage, conservation, collecte, traitement)
- L'action peut être déduite par implication nécessaire du texte

## Positif — `Non`
- L'extrait nie explicitement l'action
- L'extrait est ambigu et ne permet pas de conclure à l'action
- L'extrait traite d'un sujet adjacent mais pas de l'action spécifiée

## Sources légales
- Loi 25 (Loi modernisant des dispositions législatives en matière de protection des renseignements personnels, LQ 2021 c 25)
- LPRPDE (LC 2000 c 5) — organisations fédérales
- Lignes directrices du CAI (Commission d'accès à l'information)
- Politiques de confidentialité d'entreprises québécoises réelles (Desjardins, Bell, Hydro-Québec)

## Diversité
- Varier les actions: collecte, utilisation, communication, conservation, accès, rectification, désindexation
- Inclure des politiques d'entreprises de différents secteurs: finance, santé, commerce en ligne
- Inclure des formulations vagues (ambiguité intentionnelle dans la politique)
- Inclure des Non trompeurs: extrait qui mentionne les données mais pas l'action spécifiée

## Ne pas utiliser
- Politiques de confidentialité d'entreprises américaines (CCPA, GDPR)
- Données de a2aj/canadian-laws