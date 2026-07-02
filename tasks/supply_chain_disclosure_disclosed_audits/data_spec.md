## Purpose
Identifier si une déclaration de chaîne d'approvisionnement québécoise ou canadienne mentionne des divulgation effective en matière de divulgation effective — audits (Oui/Non).

## Question format
**Input:** Un extrait de déclaration sur la chaîne d'approvisionnement publiée par une entreprise.
**Output:** `Oui` | `Non`

**Définition opérationnelle :**
`Oui` — l'extrait contient des informations sur audits effectivement réalisés et divulgués dans la déclaration.
`Non` — l'extrait ne traite pas de ce sujet ou en parle de manière trop vague pour être qualifié.

## Legal sources
- **Loi sur la lutte contre le travail forcé et le travail des enfants dans les chaînes d'approvisionnement, LC 2023 c 9** (Loi S-211)
- **Lignes directrices du gouvernement fédéral canadien sur la Loi S-211**

## Diversity requirements
- Varier les secteurs industriels (manufacturier, détail, agroalimentaire, technologie, ressources)
- Varier la longueur des extraits (1–2 phrases vs 2–3 paragraphes)
- Inclure des `Non` trompeurs : déclarations générales sans aborder le sujet spécifique
- Équilibre strict 50 % Oui / 50 % Non (± 1)

## Do not use
- Déclarations soumises à la UK Modern Slavery Act uniquement
- Déclarations soumises à la loi australienne sur la chaîne d'approvisionnement uniquement
- Données de a2aj/canadian-laws
