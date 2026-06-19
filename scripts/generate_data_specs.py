# generate_data_specs.py
# Generates data_spec.md for all LexiorBench tasks.
# Run from repo root: python scripts/generate_data_specs.py
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ======================================================================
# generate_data_specs_part1.py
# ======================================================================

"""
Part 1 — data_spec.md for the 35 tasks currently in tasks/
"""
from pathlib import Path

TASKS = ROOT / "tasks"

SPECS = {

"canada_tax_court_outcomes": """\
## Purpose
Classify whether a Tax Court of Canada decision excerpt reveals the outcome of the appeal (allowed / dismissed / other).

## Question format
Input: excerpt from a Tax Court of Canada judgment (English or French).
Output: `allowed` | `dismissed` | `other`

**Example:**
> "L'appel est accueilli en partie et le dossier est renvoyé au ministre pour réévaluation."
> → allowed

## Positive — `allowed`
- Excerpt explicitly states the appeal is allowed, granted, or partially allowed
- Mixed results (partly allowed, partly dismissed) → classify as `allowed`
- Costs orders alone are not the outcome; ignore them

## Positive — `dismissed`
- Excerpt states the appeal is dismissed, rejected, or denied

## Positive — `other`
- Outcome is unclear, interlocutory, procedural, or not stated in the excerpt
- Excerpt is from reasons only, no dispositif present

## Legal sources
- Tax Court of Canada Act, RSC 1985 c T-2
- Real Tax Court decisions from CanLII (taxe.ca, canlii.org — Tax Court of Canada section)
- Bilingual: include both English and French decision excerpts

## Diversity guidelines
- Mix English and French excerpts (federal bilingual court)
- Vary excerpt location: dispositif, opening paragraph, summary
- Include both income tax and GST/HST cases
- Include cases where the outcome is buried in a long paragraph (hard negatives)

## Do not use
- US Tax Court decisions
- Provincial tax tribunal decisions
- Excerpts that only discuss procedure with no outcome signal
""",

"canadian_employment_insurance_recall": """\
## Purpose
True/False recall of rules under the Employment Insurance Act (Canada).

## Question format
Input: a declarative statement about EI rules.
Output: `Vrai` | `Faux`

**Example:**
> "Sous la Loi sur l'assurance-emploi, le prestataire doit effectuer un délai de carence de deux semaines avant d'avoir droit aux prestations."
> → Vrai

## Positive — `Vrai`
- Statement accurately reflects the Act as currently in force
- Paraphrase is acceptable as long as the substance is correct

## Positive — `Faux`
- Statement contains a factual error (wrong number of weeks, wrong eligibility condition, wrong exception)
- Statement describes a rule that was amended and is no longer in force
- Statement confuses EI with provincial programs (RQAP, etc.)

## Legal sources
- Employment Insurance Act, SC 1996 c 23 (especially Parts I, IV, VIII)
- EI regulations (SOR/96-332)
- ESDC policy manuals (publicly available)
- CanLII: Federal Court EI decisions

## Diversity guidelines
- Cover: waiting period, insurable hours, benefit rate, clawback, parental/maternity benefits, self-employed provisions, disqualification, appeal rights
- Include statements about RQAP vs EI distinctions (Quebec specificity)
- Mix straightforward recalls with subtle errors (wrong number by 1, transposed conditions)

## Do not use
- Provincial EI equivalents outside Quebec
- US unemployment insurance rules
- Outdated rules pre-1996 without noting they are historical
""",

"canadian_human_rights_act_recall": """\
## Purpose
True/False recall of rules under the Canadian Human Rights Act (Canada).

## Question format
Input: declarative statement about prohibited grounds or processes under the CHRA.
Output: `Vrai` | `Faux`

**Example:**
> "L'âge est un motif de distinction illicite en vertu de la Loi canadienne sur les droits de la personne."
> → Vrai

## Positive — `Vrai`
- Accurately states a prohibited ground, a protected activity, or a remedial power under the CHRA

## Positive — `Faux`
- Names a ground that is NOT listed (e.g., political opinion — not a CHRA ground at federal level)
- Confuses CHRA with Quebec's Charte des droits et libertés de la personne
- Misstates the complaint process (e.g., wrong time limit, wrong body)

## Legal sources
- Canadian Human Rights Act, RSC 1985 c H-6
- Canadian Human Rights Commission (CHRC) policies
- Key CHRT and Federal Court decisions (CanLII)

## Diversity guidelines
- Cover all 13 prohibited grounds individually
- Include harassment, accommodation duties, bona fide occupational requirements
- Distinguish federal CHRA from provincial human rights codes
- Include procedural rules (complaint deadlines, mediation, tribunal)

## Do not use
- Quebec Charte (separate instrument — use for QC tasks)
- US civil rights legislation (Title VII, ADA)
""",

"canadian_labour_code_recall": """\
## Purpose
True/False recall of rules under the Canada Labour Code (federal).

## Question format
Input: declarative statement about federally regulated workplace rules.
Output: `Vrai` | `Faux`

**Example:**
> "Le Code canadien du travail s'applique aux employeurs sous réglementation fédérale, comme les banques et les transporteurs aériens."
> → Vrai

## Positive — `Vrai`
- Accurately states a rule from Parts I (industrial relations), II (occupational health and safety), or III (labour standards) of the Code

## Positive — `Faux`
- Confuses federal Code with provincial labour laws (LNT for Quebec)
- States a rule that applies only to provincially regulated employers
- Misstates a threshold (e.g., wrong notice period, wrong overtime rate)

## Legal sources
- Canada Labour Code, RSC 1985 c L-2 (Parts I, II, III)
- Federal labour standards regulations
- CIRB and Federal Court decisions (CanLII)

## Diversity guidelines
- Cover: scope of application (which employers), termination notice, overtime, leave entitlements, collective bargaining, OHS duties
- Include difficult cases: interprovincial transport, broadcasting, Indigenous enterprises
- Mix Part I (unions), Part II (safety), Part III (individual standards) questions

## Do not use
- Quebec LNT rules
- Provincial occupational health codes
""",

"canadian_privacy_act_recall": """\
## Purpose
True/False recall of rules under the Privacy Act (Canada, federal institutions).

## Question format
Input: declarative statement about the Privacy Act's application or requirements.
Output: `Vrai` | `Faux`

**Example:**
> "La Loi sur la protection des renseignements personnels s'applique aux renseignements personnels détenus par les institutions fédérales."
> → Vrai

## Positive — `Vrai`
- Accurately describes scope, rights (access, correction), obligations of federal institutions, or the OPC's role

## Positive — `Faux`
- Confuses the Privacy Act (federal institutions) with PIPEDA/LPRPDE (private sector)
- States the Act applies to private companies
- Misstates a time limit or access right

## Legal sources
- Privacy Act, RSC 1985 c P-21
- Office of the Privacy Commissioner of Canada (OPC) guidance
- Key Federal Court decisions (CanLII)

## Diversity guidelines
- Cover: scope (federal institutions only), individual rights (access, correction, complaint), exempt banks, OPC oversight
- Include PIPEDA vs Privacy Act distinctions
- Include Loi 25 (QC) vs LPRPDE vs Privacy Act distinctions

## Do not use
- US Privacy Act (5 USC 552a)
- GDPR
- Quebec Loi 25 (use for QC privacy tasks)
""",

"citation_prediction_classification": """\
## Purpose
Verify whether a bibliographic reference matches the legal source cited, using McGill Guide format (10th ed.).

## Question format
Input: a citation string paired with a description of the source.
Output: `Oui` (citation is correct) | `Non` (citation has an error)

**Example:**
> "Citation proposée: 'Doré c Barreau du Québec, 2012 CSC 12, [2012] 1 RCS 395.' — Cette citation correspond-elle à l'arrêt portant sur le contrôle judiciaire des décisions du Barreau?"
> → Oui

## Positive — `Oui`
- Citation format matches McGill Guide: parties, year, neutral citation, reporter citation
- Year, volume, reporter, and page are all correct

## Positive — `Non`
- Wrong year (e.g., 2011 instead of 2012)
- Wrong neutral citation number
- Wrong reporter (e.g., RCS vs CF)
- Parties listed in wrong order (respondent before applicant)
- Missing required element

## Legal sources
- McGill Guide to Legal Citation, 10th ed. (Le Manuel canadien de la référence juridique)
- CanLII neutral citations for CSC, CA-QC, Cour fédérale, Cour du Québec
- Key landmark cases: Doré, Dunsmuir, Vavilov, Clements, Jordan

## Diversity guidelines
- Include citations to: CSC, CA-QC, Cour fédérale, Cour du Québec, CRTC, TAL
- Mix errors: wrong year, transposed neutral citation number, wrong reporter
- Include both English and French case names
- Include legislation citations (LIR, CCQ, LPC) not just case law

## Do not use
- Bluebook format (US)
- OSCOLA (UK)
- Invented case names that do not exist in CanLII
""",

"civil_issue_spotting_responsabilite": """\
## Purpose
Identifier si un scénario factuel soulève une question de responsabilité civile extracontractuelle selon l'art. 1457 CCQ.

## Question format
Input: court scénario factuel en français.
Output: `Oui` | `Non`

**Exemple:**
> "Lors d'une dispute de voisinage, Marc pousse violemment son voisin, qui chute et se fracture le poignet."
> → Oui

## Positif — `Oui`
- Scénario implique une faute (action ou omission), un préjudice (corporel, matériel, moral) et un lien de causalité
- Responsabilité du fait d'autrui (employeur, parent, gardien)
- Trouble de voisinage (art. 976 CCQ)
- Responsabilité du gardien d'une chose (art. 1465 CCQ)

## Négatif — `Non`
- Scénario de responsabilité contractuelle pure (art. 1458 CCQ) sans faute extracontractuelle distincte
- Préjudice sans faute identifiable (accident pur)
- Scénario de droit criminel sans dimension civile
- Scénario hors QC ou hors droit civil

## Sources légales
- Art. 1457, 1458, 1459, 1463, 1465, 1467, 1468, 976 CCQ
- Décisions CanLII: Cour du Québec, Cour supérieure QC, CA-QC (responsabilité civile)
- Droit québécois de l'obligation (Lluelles & Moore)

## Diversité
- Varier: dommages corporels, matériels, moraux
- Inclure: accidents de la route, chutes sur trottoir, erreurs médicales, nuisances de voisinage
- Inclure des scénarios mixtes (faute contractuelle + extracontractuelle)
- Inclure des défenses plausibles (consentement, force majeure)

## Ne pas utiliser
- Jurisprudence américaine ou common law
- Scénarios en droit pénal sans dimension civile
- Données de a2aj/canadian-laws (source d'entraînement de LexiorGPT)
""",

"civil_rule_application_vices_caches": """\
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
""",

"civil_rule_conclusion_contrats": """\
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
""",

"civil_rule_recall_ccq": """\
## Purpose
Recall the content of the Code civil du Québec — determine if a stated rule is Vrai or Faux.

## Question format
Input: declarative statement about a CCQ rule (obligations, prescription, capacity, property, successions).
Output: `Vrai` | `Faux`

**Example:**
> "Au Québec, la prescription extinctive de droit commun est de dix ans."
> → Faux (correct answer is 3 years, art. 2925 CCQ)

## Positive — `Vrai`
- Statement accurately states a current CCQ rule
- Paraphrase is acceptable if substantively correct

## Positive — `Faux`
- Wrong number (prescriptions, delays, percentages)
- Describes an abrogated rule (C.c.B.-C. → CCQ 1994)
- Confuses CCQ with federal law or common law rule
- States an exception as if it were the general rule

## Legal sources
- CCQ (all 5 books): Personnes, Famille, Successions, Biens, Obligations, Priorités et hypothèques, Preuve, Prescription, DIP, Droit international privé
- Annotated CCQ (Wilson & Lafleur, or Barreau du Québec collection)
- lexior-ccq MCP for article text

## Diversity guidelines
- Cover all 5 books proportionally
- Prioritize: obligations (art. 1371-1707), prescription (art. 2875-2933), biens (art. 899-1008), successions (art. 613-898)
- Include subtle errors: off-by-one on delay periods, confused article numbers
- Include rules changed since 1994 (old C.c.B.-C. vs current CCQ)

## Do not use
- Rules from the Code de procédure civile (separate code)
- Federal legislation
- Rules that vary by regulation (use the statutory text only)
""",

"definition_classification": """\
## Purpose
Identifier si une phrase extraite d'une décision de justice définit un terme juridique (Oui/Non).

## Question format
Input: phrase extraite d'un arrêt canadien (CSC, CA-QC, Cour fédérale).
Output: `Oui` | `Non`

**Exemple:**
> "Le terme 'résidence principale' au sens de l'art. 395 CCQ désigne le lieu où une personne a son principal établissement, déterminé par l'intention de s'y établir de façon durable."
> → Oui

## Positif — `Oui`
- Phrase contient une définition explicite d'un terme: "X désigne/signifie/s'entend de Y"
- Phrase délimite la portée d'un concept juridique par des critères positifs ou négatifs
- Phrase établit un test pour identifier quand un terme s'applique

## Négatif — `Non`
- Phrase applique une règle sans définir de terme
- Phrase cite un article de loi sans en dégager une définition
- Phrase constate des faits
- Phrase exprime un raisonnement de causalité ou de conclusion

## Sources légales
- Décisions CanLII: CSC, CA-QC, Cour fédérale (section Jurisprudence)
- Arrêts de principe définissant des termes: Doré (raisonnabilité), Vavilov (caractère raisonnable), Jordan (délai raisonnable)
- Dictionnaires juridiques canadiens pour validation

## Diversité
- Varier: droit civil, droit public, droit criminel, droit fiscal
- Inclure des définitions implicites (sans le mot "désigne" mais équivalentes)
- Inclure des phrases qui ressemblent à des définitions mais n'en sont pas (trompe-l'œil)
- Équilibre Oui/Non: ~50/50

## Ne pas utiliser
- Décisions SCOTUS ou cours américaines
- Définitions législatives (lire directement dans la loi — trop facile)
- Données de a2aj/canadian-laws
""",

"learned_hands_benefits": """\
## Purpose
Identifier si ce scénario soulève une question juridique liée aux prestations sociales et services gouvernementaux (aide sociale, AE, RRQ, PFCE, invalidité).

## Question format
Input: scénario en français décrivant une situation personnelle.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai fait une demande d'aide sociale au mois de mars et on m'a refusé en disant que j'avais trop d'actifs. Mon seul actif est une vieille voiture valant 800$."
> → Oui

## Positif — `Oui`
- Admissibilité refusée ou contestée pour aide sociale, AE, RRQ, PFCE, allocation invalidité
- Coupure ou réduction de prestations sans explication valable
- Non-paiement d'une prestation due
- Recours en révision administrative d'une décision de refus

## Négatif — `Non`
- Scénario de droit du travail (congédiement, heures supplémentaires)
- Scénario de droit familial (pension alimentaire, garde)
- Scénario de droit du logement (expulsion, réparations)
- Scénario fiscal sans lien avec une prestation

## Sources légales
- Loi sur l'aide aux personnes et aux familles (RLRQ c A-13.1.1) — aide sociale QC
- Loi sur l'assurance-emploi (SC 1996 c 23)
- Loi sur le régime de rentes du Québec (RLRQ c R-9)
- Loi sur la sécurité de la vieillesse (LRC 1985 c O-9)
- Prestation canadienne pour enfants (LIR art. 122.6)

## Diversité
- Varier: aide sociale, AE, RRQ/CPP, SV/GIS, allocations familiales, invalidité
- Inclure: refus initial, révision, appel, coupure mid-prestations
- Inclure des Non plausibles: droit du travail, droit familial (semblent liés aux prestations)
- Varier le profil: parent monoparental, personne handicapée, travailleur autonome, aîné

## Ne pas utiliser
- Medicaid, SNAP, SSI (US)
- Données de a2aj/canadian-laws
""",

"learned_hands_business": """\
## Purpose
Identifier si ce scénario soulève une question juridique liée au droit des affaires (sociétés, associés, contrats commerciaux, faillite, propriété intellectuelle).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai fondé une start-up avec deux associés il y a deux ans. Un associé veut partir et réclame 50% des actifs alors qu'il n'a contribué qu'à 20%."
> → Oui

## Positif — `Oui`
- Litige entre associés ou actionnaires (CCQ art. 2186+, LSAQ, LCSA)
- Rupture de contrat commercial, clause de non-concurrence
- Insolvabilité ou faillite d'une entreprise (LFI)
- Atteinte à une marque de commerce ou à un brevet
- Responsabilité d'un administrateur

## Négatif — `Non`
- Litige de travail entre employeur et employé (pas un différend entre associés)
- Litige de consommation entre particulier et commerçant
- Droit fiscal d'une entreprise (sauf si lié à une question de gouvernance)

## Sources légales
- CCQ art. 2186-2279 (société)
- Loi sur les sociétés par actions du Québec (LSAQ, RLRQ c S-31.1)
- Loi canadienne sur les sociétés par actions (LCSA, LRC 1985 c C-44)
- Loi sur la faillite et l'insolvabilité (LFI, LRC 1985 c B-3)
- Loi sur les marques de commerce (LRC 1985 c T-13)

## Diversité
- Varier: sociétés en nom collectif, SPA, sociétés en commandite
- Inclure: convention entre actionnaires, droits des minoritaires, oppression
- Inclure des faillites personnelles d'entrepreneurs

## Ne pas utiliser
- Delaware corporate law
- SEC regulations
- Données de a2aj/canadian-laws
""",

"learned_hands_consumer": """\
## Purpose
Identifier si ce scénario soulève une question juridique liée à la protection du consommateur (LPC, garantie légale, pratiques commerciales déloyales).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai acheté un lave-vaisselle neuf il y a 8 mois. Il est déjà brisé. Le vendeur refuse la garantie légale et dit que j'aurais dû prendre l'assurance étendue."
> → Oui

## Positif — `Oui`
- Vendeur refuse d'honorer la garantie légale de bon fonctionnement (LPC art. 37-38)
- Représentation fausse ou trompeuse dans une publicité ou une vente (LPC art. 219+)
- Clause abusive dans un contrat de consommation (LPC art. 8)
- Contrat à distance ou à exécution successive avec droit de résiliation (LPC art. 54.4+)
- Prix affiché non respecté

## Négatif — `Non`
- Litige entre deux commerçants (pas un contrat de consommation)
- Litige de bail résidentiel (Loi sur le bail, pas LPC)
- Litige de service professionnel réglementé (médecin, avocat)

## Sources légales
- Loi sur la protection du consommateur (RLRQ c P-40.1)
- Office de la protection du consommateur (OPC) — guides d'application
- CCQ art. 1384, 1386 (contrat de consommation)
- Décisions du Tribunal de protection du consommateur / petites créances QC

## Diversité
- Varier: bien meuble, service, contrat électronique, vente itinérante, crédit
- Inclure: pratiques de vente sous pression, vente pyramidale, faux soldes
- Inclure des Non plausibles: disputes entre particuliers, services professionnels

## Ne pas utiliser
- FTC regulations (US)
- Consumer Protection Act (Ontario)
- Données de a2aj/canadian-laws
""",

"learned_hands_courts": """\
## Purpose
Identifier si ce scénario soulève une question de procédure judiciaire ou de droits du justiciable devant les tribunaux québécois ou canadiens.

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai reçu une mise en demeure d'un avocat me réclamant 8 000$. Je conteste totalement la dette. Comment contester?"
> → Oui

## Positif — `Oui`
- Question sur la compétence d'un tribunal (Cour du Québec, Cour supérieure, petites créances)
- Droits en tant que partie à une instance (délais, signification, représentation)
- Question sur une ordonnance, injonction, ou mesure provisoire
- Accès à l'aide juridique
- Appel d'un jugement

## Négatif — `Non`
- Question de fond sur le droit substantif (responsabilité civile, droit du travail)
- Question de droit administratif (appel d'une décision d'organisme gouvernemental)
- Question d'arbitrage commercial

## Sources légales
- Code de procédure civile du Québec (C.p.c., RLRQ c C-25.01)
- Loi sur les tribunaux judiciaires (RLRQ c T-16)
- Règles des petites créances (C.p.c. art. 536-583)
- Loi sur l'aide juridique (RLRQ c A-14)

## Diversité
- Varier: petites créances, chambre civile, chambre commerciale
- Inclure: délais de prescription, dépôt de la demande, signification
- Inclure: représentation par avocat, auto-représentation, aide juridique

## Ne pas utiliser
- Federal Rules of Civil Procedure (US)
- Common law provincial procedure rules
""",

"learned_hands_crime": """\
## Purpose
Identifier si ce scénario soulève une question de droit criminel canadien (Code criminel, droits de l'accusé, procédure pénale).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "J'ai été arrêté hier soir pour voie de fait simple. C'est la première fois. On m'a remis en liberté sous conditions."
> → Oui

## Positif — `Oui`
- Infraction au Code criminel (LRC 1985 c C-46) ou à une loi pénale fédérale
- Droits constitutionnels de l'accusé (Charte canadienne, art. 7-14)
- Procédure pénale: mise en liberté provisoire, enquête préliminaire, plaidoyer
- Condamnation, sentence, casier judiciaire, absolution

## Négatif — `Non`
- Infraction purement réglementaire provinciale ou municipale (contraventions de stationnement, points de démérite)
- Litige civil découlant d'un acte criminel (poursuite en responsabilité civile distincte)
- Question de droit de la famille non criminelle

## Sources légales
- Code criminel (LRC 1985 c C-46)
- Charte canadienne des droits et libertés (art. 7-14)
- Code de procédure pénale du Québec (RLRQ c C-25.1)
- Loi sur le système de justice pénale pour les adolescents (LSJPA)

## Diversité
- Varier: infractions contre la personne, contre les biens, infractions de drogues, conduite avec facultés affaiblies
- Inclure: droits à l'arrestation (art. 10 Charte), droit à l'avocat, droit au silence
- Inclure: adolescents (LSJPA), récidivistes, mesures de déjudiciarisation

## Ne pas utiliser
- US criminal law (4th Amendment, Miranda)
- Droit pénal d'autres pays
""",

"learned_hands_divorce": """\
## Purpose
Identifier si ce scénario soulève une question de droit du divorce ou de séparation (Loi sur le divorce, CCQ).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Je suis marié depuis 8 ans et je veux divorcer. Mon conjoint refuse de signer. Peut-on forcer un divorce au Canada?"
> → Oui

## Positif — `Oui`
- Divorce (Loi sur le divorce, LRC 1985 c 3 (2e suppl.))
- Séparation de corps (CCQ art. 493-515)
- Partage du patrimoine familial lors de la rupture (CCQ art. 414-430)
- Prestation compensatoire entre ex-époux (CCQ art. 427-430)
- Pension alimentaire entre ex-époux (Loi sur le divorce art. 15.2)

## Négatif — `Non`
- Garde d'enfants ou pension alimentaire pour enfants (domaine séparé — learned_hands_family)
- Union de fait sans régime d'union civile (pas de divorce possible)
- Litige successoral entre ex-conjoints

## Sources légales
- Loi sur le divorce (LRC 1985 c 3 (2e suppl.))
- CCQ art. 493-515 (séparation de corps)
- CCQ art. 414-430 (patrimoine familial)
- Décisions CanLII: Cour supérieure QC (chambre de la famille)

## Diversité
- Inclure: motif unique (échec du mariage ≥ 1 an), faute (adultère, cruauté)
- Inclure: divorce par consentement mutuel vs divorce contesté
- Inclure: partage de la maison familiale, du REER, du RRQ
- Inclure des unions de fait (Oui si union civile, Non si pure union de fait)

## Ne pas utiliser
- Divorce laws from US states
- Données de a2aj/canadian-laws
""",

"learned_hands_domestic_violence": """\
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
""",

"learned_hands_education": """\
## Purpose
Identifier si ce scénario soulève une question juridique liée au droit à l'éducation (accommodements, suspension, langue d'enseignement, droits de l'élève).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon enfant autiste a été suspendu de l'école parce qu'il a eu une crise liée à son handicap. La commission scolaire dit que son comportement était 'incompatible avec le milieu scolaire'."
> → Oui

## Positif — `Oui`
- Obligation d'accommodement raisonnable pour un élève handicapé (Charte québécoise, art. 10)
- Refus d'accès à l'école ou suspension contestable
- Droits linguistiques scolaires (Charte de la langue française — loi 101, art. 73+)
- Droit à des services éducatifs pour enfants en situation de handicap (Loi sur l'instruction publique)

## Négatif — `Non`
- Litige entre parents sur les décisions scolaires (droit de la famille)
- Faute professionnelle d'un enseignant sans dimension de droit à l'éducation
- Problème d'emploi d'un enseignant (droit du travail)

## Sources légales
- Loi sur l'instruction publique (RLRQ c I-13.3)
- Charte des droits et libertés de la personne du Québec (art. 10, 40)
- Charte de la langue française (RLRQ c C-11) — langue d'enseignement
- Loi sur l'enseignement privé (RLRQ c E-9.1)

## Diversité
- Varier: TDAH, TSA, trouble d'apprentissage, handicap physique, trouble de comportement
- Inclure: droits linguistiques (anglophone en école française, allophone)
- Inclure: suspension vs expulsion, programmes adaptés (EHDAA)
- Inclure des Non plausibles: litige de pension alimentaire mentionnant une école

## Ne pas utiliser
- IDEA, Section 504 (US)
- Données de a2aj/canadian-laws
""",

"learned_hands_employment": """\
## Purpose
Identifier si ce scénario soulève une question de droit du travail québécois ou canadien (LNT, CCT, harcèlement, congédiement).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon employeur me demande de travailler 55 heures par semaine depuis deux mois. Il refuse de payer les heures supplémentaires, disant que je suis 'cadre'. Je supervise deux personnes."
> → Oui

## Positif — `Oui`
- Violation des normes du travail (LNT ou Code canadien du travail)
- Congédiement sans cause juste et suffisante (LNT art. 124)
- Harcèlement psychologique au travail (LNT art. 81.18+)
- Discrimination à l'embauche ou au travail (Charte québécoise)
- Non-paiement de salaire, heures supplémentaires, vacances

## Négatif — `Non`
- Litige entre associés ou actionnaires (pas un lien d'emploi)
- Litige de prestations gouvernementales lié indirectement au travail
- Accident du travail (CNESST — domaine distinct en QC)

## Sources légales
- Loi sur les normes du travail (RLRQ c N-1.1)
- Code canadien du travail (LRC 1985 c L-2) — employeurs fédéraux
- Charte des droits et libertés de la personne (art. 10, 16, 18)
- Décisions CanLII: TAT (Tribunal administratif du travail), CNESST

## Diversité
- Varier: heures supp, congés, protection contre représailles, droit de retour
- Inclure: travailleurs autonomes vs salariés (qualification du statut)
- Inclure: secteur fédéral vs provincial (banques, transport, télécoms = fédéral)
- Inclure des Non plausibles: accident à l'extérieur du travail qui impacte l'emploi

## Ne pas utiliser
- FLSA, NLRA, EEOC (US)
- Données de a2aj/canadian-laws
""",

"learned_hands_estates": """\
## Purpose
Identifier si ce scénario soulève une question de droit successoral québécois (testament, liquidation, héritage, réserve héréditaire).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon père est décédé la semaine dernière sans testament. Ma mère est encore vivante. Qui hérite? Je suis fils unique."
> → Oui

## Positif — `Oui`
- Succession ab intestat (sans testament) — qui hérite? (CCQ art. 653+)
- Validité ou contestation d'un testament (olographe, devant témoins, notarié)
- Legs particulier ou universel, liquidateur de succession
- Renonciation à une succession / acceptation sous bénéfice d'inventaire (CCQ art. 630+)
- Partage d'une succession avec dettes

## Négatif — `Non`
- Régime matrimonial entre conjoints vivants (patrimoine familial — distinct de la succession)
- Assurance-vie (désignation de bénéficiaire — hors succession)
- Litige de garde ou de pension alimentaire pour enfants

## Sources légales
- CCQ Livre III (art. 613-898) — successions, testament, liquidation
- Loi sur les testaments (abolie — intégrée dans CCQ depuis 1994)
- Décisions CanLII: Cour supérieure QC (chambre de la famille / des successions)

## Diversité
- Varier: décès avec et sans testament, héritiers multiples, dettes de la succession
- Inclure: testaments olographes contestés, vices de forme, undue influence
- Inclure: situations avec enfants de différents lits, conjoints de fait (pas d'héritage légal)
- Inclure des Non plausibles: assurance-vie, REER avec bénéficiaire désigné

## Ne pas utiliser
- Wills and Succession Act (Alberta, BC)
- Common law intestacy rules
- Données de a2aj/canadian-laws
""",

"learned_hands_family": """\
## Purpose
Identifier si ce scénario soulève une question de droit de la famille (garde, pension alimentaire pour enfants, autorité parentale).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon ex-conjoint veut déménager à Vancouver avec nos deux enfants sans mon consentement. Notre entente de garde est partagée à 50/50."
> → Oui

## Positif — `Oui`
- Garde physique ou légale des enfants (CCQ art. 394.2, Loi sur le divorce)
- Relocalisation d'un parent avec les enfants (déménagement)
- Pension alimentaire pour enfants (Lignes directrices fédérales, RLRQ c C-25.01)
- Autorité parentale contestée (art. 33 CCQ — intérêt de l'enfant)
- Adoption, tutelle, déchéance de l'autorité parentale

## Négatif — `Non`
- Divorce entre époux sans enfants (pension alimentaire pour époux — domaine distinct)
- Violence conjugale sans question de garde distincte
- Décision scolaire sans contestation de l'autorité parentale

## Sources légales
- CCQ art. 33, 394.2-413 (autorité parentale, garde, aliments)
- Loi sur le divorce (LRC 1985 c 3 (2e suppl.)) art. 16 (garde)
- Lignes directrices fédérales sur les aliments pour enfants (DORS/97-175)
- Loi sur la protection de la jeunesse (RLRQ c P-34.1)

## Diversité
- Varier: séparation de couples mariés, union civile, conjoints de fait
- Inclure: demandes d'urgence, ordonnances provisoires, médiation familiale
- Inclure: droits de visite, relocalisation internationale
- Inclure des Non plausibles: litige de divorce portant sur les biens sans enfants

## Ne pas utiliser
- Best interests standard from US state courts
- Données de a2aj/canadian-laws
""",

"learned_hands_health": """\
## Purpose
Identifier si ce scénario soulève une question de droit de la santé (consentement aux soins, responsabilité médicale, droits du patient).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon médecin a fait une erreur de diagnostic qui a retardé mon traitement de cancer de 8 mois. Mon cancer a progressé au stade 3."
> → Oui

## Positif — `Oui`
- Responsabilité médicale ou hospitalière (CCQ art. 1457 + Loi médicale)
- Défaut de consentement éclairé aux soins (CCQ art. 10-14, Loi sur les services de santé)
- Refus de soins par un professionnel de la santé
- Divulgation non autorisée de renseignements médicaux (Loi sur les services de santé art. 19)
- Soins contre le gré d'un patient inapte (CCQ art. 11-23)

## Négatif — `Non`
- Litige avec une assurance-maladie complémentaire (droit des assurances, pas droit de la santé)
- Litige d'emploi d'un professionnel de la santé (droit du travail)
- Remboursement de médicaments par la RAMQ (droit administratif)

## Sources légales
- CCQ art. 10-25 (intégrité de la personne, consentement)
- Loi sur les services de santé et les services sociaux (RLRQ c S-4.2)
- Code de déontologie des médecins (RLRQ c M-9, r 17)
- Loi médicale (RLRQ c M-9)
- Décisions CanLII: Cour supérieure QC (responsabilité médicale)

## Diversité
- Varier: erreur chirurgicale, erreur de diagnostic, erreur médicamenteuse
- Inclure: patients hospitalisés vs ambulatoires, urgences
- Inclure: consentement d'un mineur, d'un inapte, refus de transfusion
- Inclure des Non plausibles: litige avec une mutuelle d'assurance médicale

## Ne pas utiliser
- HIPAA, ACA, Medicaid (US)
- Données de a2aj/canadian-laws
""",

"learned_hands_housing": """\
## Purpose
Identifier si ce scénario soulève une question de droit du bail résidentiel québécois (TAL, CCQ arts. 1851-2000).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon propriétaire refuse de réparer la fournaise depuis trois semaines. Il fait -15°C dehors et mon appartement n'est plus chauffé."
> → Oui

## Positif — `Oui`
- Obligation d'entretien du logement par le locateur (CCQ art. 1854)
- Reprise de logement ou éviction (CCQ art. 1957-1970)
- Fixation ou augmentation de loyer (CCQ art. 1906-1909, TAL)
- Entrée non autorisée du locateur (CCQ art. 1930-1931)
- Résiliation de bail pour violence conjugale (CCQ art. 1974.1)
- Sous-location ou cession de bail (CCQ art. 1870-1876)

## Négatif — `Non`
- Litige entre deux locataires (pas un litige bail)
- Bail commercial (règles différentes — CCQ art. 1851 exclut les baux commerciaux)
- Litige de copropriété divise entre copropriétaires (pas un bail)
- Dispute d'emploi ou familiale se déroulant dans un logement

## Sources légales
- CCQ art. 1851-2000 (bail résidentiel)
- Règlement sur les critères de fixation de loyer (RLRQ c T-15.01, r 4)
- Tribunal administratif du logement (TAL) — jurisprudence (canlii.org — Québec — TAL)

## Diversité
- Varier: appartement, maison, chambre, coopérative d'habitation
- Inclure: reconduction tacite du bail, délais de préavis (3, 4, 6 mois)
- Inclure: dépôt de garantie illégal, animaux, fumée secondaire
- Inclure des Non plausibles: litige de bail commercial, dispute de voisinage sans lien au bail

## Ne pas utiliser
- Landlord-Tenant Act (Ontario, BC)
- Éviction moratorium rules from US states
- Données de a2aj/canadian-laws
""",

"learned_hands_immigration": """\
## Purpose
Identifier si ce scénario soulève une question de droit de l'immigration canadienne (LIPR, visa, statut, réfugié).

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Mon visa étudiant expire dans 4 semaines et ma demande de renouvellement est toujours en traitement. Puis-je continuer mes études?"
> → Oui

## Positif — `Oui`
- Statut de résident permanent, visa temporaire, visa étudiant, permis de travail
- Demande d'asile / protection des réfugiés (LIPR art. 95+)
- Renvoi ou déportation (mesure d'interdiction de séjour ou d'expulsion)
- Parrainage familial (LIPR art. 12(1))
- Citoyenneté canadienne (Loi sur la citoyenneté)

## Négatif — `Non`
- Litige de travail d'un travailleur étranger (droit du travail distinct de l'immigration)
- Conflit familial entre citoyens canadiens sans question d'immigration
- Reconnaissance de diplômes étrangers (hors processus d'immigration)

## Sources légales
- Loi sur l'immigration et la protection des réfugiés (LIPR, LC 2001 c 27)
- Règlement sur l'immigration et la protection des réfugiés (RIPR, DORS/2002-227)
- Loi sur la citoyenneté (LRC 1985 c C-29)
- IRCC (Immigration, Réfugiés et Citoyenneté Canada) — guides publics

## Diversité
- Varier: résident temporaire, permanent, demandeur d'asile, travailleur étranger
- Inclure: prolongation de statut, "implied status", perte de statut
- Inclure: CISR (Commission de l'immigration et du statut de réfugié)
- Inclure des Non plausibles: litige de travail avec un immigrant (pas une question d'immigration)

## Ne pas utiliser
- US immigration law (USCIS, DACA, H-1B)
- Données de a2aj/canadian-laws
""",

"learned_hands_torts": """\
## Purpose
Identifier si ce scénario soulève une question de responsabilité civile extracontractuelle (art. 1457 CCQ) distincte du domaine contractuel.

## Question format
Input: scénario en français.
Output: `Oui` | `Non`

**Exemple:**
> "Un chien de mon voisin m'a mordu profondément à la jambe alors que je marchais sur le trottoir. J'ai dû subir plusieurs points de suture."
> → Oui

## Positif — `Oui`
- Blessure causée par un animal (CCQ art. 1466)
- Accident causé par un bien sous la garde d'autrui (CCQ art. 1465)
- Atteinte à la réputation / diffamation (CCQ art. 1457)
- Invasion de la vie privée (CCQ art. 35-41)
- Nuisance causant un préjudice réel (art. 976 CCQ)

## Négatif — `Non`
- Blessure couverte par la CNESST (accident du travail — exclusion légale de la RC)
- Accident de voiture (SAAQ couvre les dommages corporels — régime sans faute)
- Inexécution d'un contrat (responsabilité contractuelle — art. 1458 CCQ)

## Sources légales
- CCQ art. 1457-1481 (responsabilité civile)
- Loi sur l'assurance automobile (RLRQ c A-25) — régime sans faute QC
- Loi sur les accidents du travail et les maladies professionnelles (LATMP, RLRQ c A-3.001)
- Décisions CanLII: Cour du Québec, Cour supérieure QC

## Diversité
- Varier: blessures corporelles, préjudice moral, dommages matériels
- Inclure: défense de force majeure, fait de la victime, fait d'un tiers
- Inclure des exclusions importantes: SAAQ (accident de voiture), CNESST (travail)
- Inclure des Non plausibles: réclamation sous contrat d'assurance (pas RC directe)

## Ne pas utiliser
- Common law torts (negligence, battery — use for English Canada tasks)
- Workers' compensation exclusion from non-QC provinces
""",

"learned_hands_traffic": """\
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
""",

"legal_reasoning_causality": """\
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
""",

"overruling": """\
## Purpose
Identifier si une phrase extraite d'une décision judiciaire canadienne (CSC, CA) renverse un précédent jurisprudentiel (Oui/Non).

## Question format
Input: phrase extraite d'un arrêt canadien.
Output: `Oui` | `Non`

**Exemple:**
> "Dans la mesure où notre décision dans Doré c. Barreau du Québec [2012] 1 RCS 395 entre en conflit avec le présent arrêt, Doré est infirmé."
> → Oui

## Positif — `Oui`
- Phrase contient des mots de revirement: "est infirmé", "n'est plus le droit", "nous revenons sur", "est remplacé par", "notre décision antérieure dans X ne fait plus droit"
- Phrase signale explicitement que la Cour s'écarte d'un précédent antérieur

## Négatif — `Non`
- Phrase distingue un précédent sans le renverser ("dans X, les faits étaient différents")
- Phrase applique un précédent à de nouveaux faits
- Phrase critique un précédent sans officiellement le renverser
- Phrase discute de l'évolution du droit sans déclarer de revirement

## Sources légales
- Décisions CSC: Vavilov (renversant Dunsmuir), Jordan (renversant Morin), Henry (renversant Evans)
- Décisions CA-QC disponibles sur CanLII (section Cour d'appel du Québec)
- Arrêts importants avec revirement explicite

## Diversité
- Inclure des revirements en droit criminel, droit administratif, droit civil
- Inclure des formulations variées du revirement (pas toujours "est infirmé")
- Inclure des Non trompeurs: phrases contenant le nom d'un arrêt précédent mais sans revirement
- Équilibre Oui/Non: ~50/50 avec les Non soigneusement construits

## Ne pas utiliser
- Décisions SCOTUS
- Données de a2aj/canadian-laws
""",

"privacy_policy_entailment": """\
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
""",

"proa": """\
## Purpose
Déterminer si une personne dispose d'un droit d'action privé (recours civil) en vertu d'une loi canadienne ou québécoise particulière.

## Question format
Input: scénario décrivant une situation légale + loi potentiellement applicable.
Output: `Oui` | `Non`

**Exemple:**
> "Toute personne qui a subi des pertes par suite d'un comportement contraire à la présente partie peut, devant tout tribunal compétent, réclamer le recouvrement de ses pertes."
> → Oui

## Positif — `Oui`
- La loi crée explicitement un droit d'action pour les particuliers (recours civil)
- La loi prévoit une indemnisation privée (LPC art. 271, Loi sur la concurrence art. 36)
- Le demandeur fait partie de la classe visée par la disposition

## Positif — `Non`
- La loi prévoit uniquement des sanctions pénales ou administratives (pas de recours civil)
- La loi confère le droit d'action uniquement à un organisme public (pas aux particuliers)
- Le demandeur ne fait pas partie de la classe visée

## Sources légales
- Loi sur la protection du consommateur (RLRQ c P-40.1) art. 271-272
- Loi sur la concurrence (LRC 1985 c C-34) art. 36
- Loi sur les valeurs mobilières (RLRQ c V-1.1) — recours civil
- Loi sur la protection des renseignements personnels dans le secteur privé (Loi 25) — droit de recours

## Diversité
- Varier les lois: LPC, Loi sur la concurrence, lois environnementales, Loi 25, lois sur l'emploi
- Inclure: recours collectifs (art. 575 C.p.c.) vs recours individuels
- Inclure des Non: lois purement réglementaires sans volet civil
- Inclure des cas limites: lois ambiguës sur l'existence d'un recours privé

## Ne pas utiliser
- US private rights of action under Section 1983 or Bivens
- Données de a2aj/canadian-laws
""",

"public_interpretation_charte": """\
## Purpose
Identifier si un comportement ou une décision constitue une atteinte à un droit protégé par la Charte des droits et libertés de la personne du Québec.

## Question format
Input: scénario décrivant une situation de discrimination ou d'atteinte à un droit fondamental.
Output: `Oui` | `Non`

**Exemple:**
> "Un propriétaire refuse de louer un logement à une famille parce qu'elle reçoit des prestations d'aide sociale."
> → Oui (motif de discrimination: condition sociale, art. 10 Charte)

## Positif — `Oui`
- Discrimination fondée sur un motif listé à l'art. 10 (race, sexe, âge, handicap, condition sociale, etc.)
- Atteinte à la dignité, vie privée, ou inviolabilité de la personne (art. 1-9 Charte)
- Harcèlement discriminatoire
- Refus d'accommodement raisonnable sans contrainte excessive

## Positif — `Non`
- Distinction fondée sur un critère légitime et non discriminatoire
- Accommodement fourni qui répond aux besoins
- Distinction fondée sur un motif non listé et non analogue
- Restriction justifiée par une exigence professionnelle réelle (BFOQ)

## Sources légales
- Charte des droits et libertés de la personne du Québec (RLRQ c C-12)
- Décisions du Tribunal des droits de la personne du Québec (CanLII)
- Arrêts CSC interprétant la Charte québécoise: Granovsky, Meiorin, Boisbriand

## Diversité
- Couvrir tous les motifs de l'art. 10: race, couleur, sexe, grossesse, orientation sexuelle, état civil, âge, religion, convictions politiques, langue, origine ethnique, condition sociale, handicap
- Inclure: accès aux lieux publics (art. 12), emploi (art. 16), logement (art. 12)
- Inclure des Non trompeurs: traitements différenciés légitimes

## Ne pas utiliser
- Charte canadienne des droits et libertés (application différente — institutions gouvernementales)
- Human Rights Code (Ontario)
""",

"public_rhetorical_jugement": """\
## Purpose
Identifier la fonction rhétorique d'un extrait d'un jugement canadien (énoncé des faits, règle de droit, application, ou conclusion).

## Question format
Input: extrait d'un jugement canadien.
Output: `Faits` | `Règle` | `Application` | `Conclusion`

**Exemple:**
> "La Cour doit faire preuve de déférence à l'égard de la décision du Tribunal administratif et n'interviendra que si celle-ci est déraisonnable."
> → Règle

## Classes
- **Faits**: résume ou décrit les événements factuels, le contexte, les antécédents
- **Règle**: énonce un principe juridique, une présomption, un critère légal
- **Application**: applique la règle aux faits de l'espèce, raisonne vers un résultat
- **Conclusion**: annonce la décision finale (accueillie, rejetée, renvoyée)

## Sources légales
- Décisions CanLII: CSC, CA-QC, Cour fédérale, Cour du Québec
- Arrêts avec raisonnement IRAC explicite: Vavilov, Doré, Jordan, Clements

## Diversité
- Couvrir tous les 4 types de fonctions
- Varier les domaines: droit administratif, criminel, civil, familial
- Inclure des extraits ambigus (Application qui ressemble à une Règle)
- Équilibrer les 4 classes (25% chacune approximativement)

## Ne pas utiliser
- Décisions américaines ou de common law étrangère
- Données de a2aj/canadian-laws
""",

"supply_chain_disclosure_best_practice_audits": """\
## Purpose
Déterminer si une divulgation de chaîne d'approvisionnement décrit des pratiques ou politiques d'AUDIT des fournisseurs, conformément à la Loi sur la lutte contre le travail forcé et le travail des enfants (Canada, Loi S-211, 2023).

## Question format
Input: extrait d'une divulgation annuelle d'entreprise.
Output: `Oui` | `Non`

**Exemple:**
> "Notre politique de chaîne d'approvisionnement prévoit des audits annuels de nos fournisseurs de niveau 1 afin de détecter toute situation de travail forcé."
> → Oui

## Positif — `Oui`
- L'extrait mentionne explicitement des audits, vérifications, inspections de fournisseurs
- L'extrait décrit une politique d'audit (calendrier, portée, méthode)
- L'extrait signale qu'un tiers effectue des audits pour le compte de l'entreprise

## Positif — `Non`
- L'extrait discute de formation ou de certification mais pas d'audit
- L'extrait mentionne des audits financiers (hors périmètre S-211)
- L'extrait décrit des mesures de diligence raisonnable sans audit formel

## Sources légales
- Loi sur la lutte contre le travail forcé et le travail des enfants dans les chaînes d'approvisionnement (Canada, LC 2023 c 9) — Loi S-211
- Rapports de divulgation déposés auprès du gouvernement du Canada (registre public obligatoire)
- Lignes directrices du gouvernement canadien sur la Loi S-211

## Diversité
- Varier les secteurs: manufacturier, ressources naturelles, vêtements, électronique, alimentation
- Inclure: audits annoncés vs inopinés, audits de premier vs deuxième vs troisième niveau
- Inclure des Non trompeurs: divulgations qui mentionnent la S-211 mais décrivent autre chose

## Ne pas utiliser
- California Transparency in Supply Chains Act (US)
- UK Modern Slavery Act
- Données de a2aj/canadian-laws
""",

"supply_chain_disclosure_disclosed_audits": """\
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
""",

}  # end SPECS

written = 0
for name, content in SPECS.items():
    task_dir = TASKS / name
    if not task_dir.exists():
        print(f"SKIP {name} — folder not found in tasks/")
        continue
    spec_file = task_dir / "data_spec.md"
    spec_file.write_text(content.strip(), encoding="utf-8")
    written += 1

print(f"Written {written} data_spec.md files to tasks/")

# ======================================================================
# generate_data_specs_part2.py
# ======================================================================

"""
Part 2 — data_spec.md for tasks in old_tasks/ not yet in tasks/
Covers: contract_nli_* (14), cuad_* (38), opp115_* (9),
        contract_qa, privacy_policy_qa, unfair_tos,
        supply_chain remaining 8
"""
from pathlib import Path

OLD = ROOT / "old_tasks"

# ── contract_nli_* ────────────────────────────────────────────────────────────

CONTRACT_NLI_CLAUSES = {
    "contract_nli_confidentiality_of_agreement":
        "la confidentialité de l'existence même de l'accord de confidentialité",
    "contract_nli_explicit_identification":
        "l'identification explicite des informations considérées comme confidentielles",
    "contract_nli_inclusion_of_verbally_conveyed_information":
        "l'inclusion des informations transmises verbalement dans la portée de confidentialité",
    "contract_nli_limited_use":
        "la restriction de l'utilisation des informations confidentielles à des fins déterminées",
    "contract_nli_no_licensing":
        "l'absence de licence implicite sur les informations partagées",
    "contract_nli_notice_on_compelled_disclosure":
        "l'obligation de notifier la divulgation forcée par autorité légale",
    "contract_nli_permissible_acquirement_of_similar_information":
        "la permission d'acquérir des informations similaires de manière indépendante",
    "contract_nli_permissible_copy":
        "la permission de reproduire les informations confidentielles",
    "contract_nli_permissible_development_of_similar_information":
        "la permission de développer des informations similaires de manière indépendante",
    "contract_nli_permissible_post_agreement_possession":
        "la permission de conserver des informations après la résiliation de l'accord",
    "contract_nli_return_of_confidential_information":
        "l'obligation de restituer ou détruire les informations confidentielles à la fin de l'accord",
    "contract_nli_sharing_with_employees":
        "la permission de partager des informations confidentielles avec les employés",
    "contract_nli_sharing_with_third_parties":
        "la permission de partager des informations confidentielles avec des tiers",
    "contract_nli_survival_of_obligations":
        "la survie des obligations de confidentialité après la résiliation de l'accord",
}

def contract_nli_spec(task_name, clause_desc):
    return f"""\
## Purpose
Identifier si la clause d'un accord de confidentialité canadien traite {clause_desc} (Oui/Non).

## Question format
Input: clause extraite d'un accord de confidentialité québécois ou canadien (en français).
Output: `Oui` | `Non`

**Exemple:**
> Clause: "Les parties s'engagent à ne divulguer à aucun tiers l'existence du présent accord."
> → Oui (si la tâche porte sur la confidentialité de l'accord lui-même)

## Positif — `Oui`
- La clause traite explicitement ou implicitement {clause_desc}
- La clause délimite les droits et obligations relatifs à ce sujet spécifique

## Positif — `Non`
- La clause porte sur un autre aspect de la confidentialité
- La clause est une clause générale d'accord de confidentialité sans dispositions sur ce sujet
- La clause traite d'un sujet adjacent (ex: durée) sans aborder {clause_desc}

## Sources légales
- Modèles d'accords de confidentialité (NDA) en droit québécois et canadien
- CCQ art. 1373-1379 (obligation de ne pas faire), 1434 (clauses implicites)
- Pratiques notariales québécoises en droit des affaires
- Barreaux provinciaux — modèles de contrats types

## Diversité
- Varier: NDA entre employeur-employé, entre entreprises, dans un contexte de fusion-acquisition
- Varier la formulation: explicite vs implicite, interdiction vs permission conditionnelle
- Inclure des clauses longues et complexes où le sujet est secondaire
- Inclure des clauses en français québécois courant et en français juridique formel

## Do not use
- US NDA boilerplate (governed by Delaware/NY law)
- UK NDA clauses
- Données de a2aj/canadian-laws (source d'entraînement de LexiorGPT)
""".strip()

# ── cuad_* ────────────────────────────────────────────────────────────────────

CUAD_CLAUSES = {
    "cuad_affiliate_license_licensee":
        ("si la clause accorde une licence à des sociétés affiliées du preneur de licence",
         "licence accordée aux affiliées du preneur — ex: filiales, sociétés sœurs"),
    "cuad_affiliate_license_licensor":
        ("si la clause accorde une licence à des sociétés affiliées du donneur de licence",
         "licence accordée aux affiliées du donneur — ex: filiales du propriétaire de la PI"),
    "cuad_anti_assignment":
        ("si la clause restreint la cession du contrat sans consentement",
         "clause de non-cession ou d'anti-cession — ex: 'ne peut céder sans accord écrit préalable'"),
    "cuad_audit_rights":
        ("si la clause accorde un droit d'audit ou d'inspection des livres ou locaux",
         "droit d'audit — ex: 'le donneur de licence peut vérifier les registres du preneur'"),
    "cuad_cap_on_liability":
        ("si la clause plafonne la responsabilité d'une partie",
         "plafond de responsabilité — ex: 'la responsabilité totale ne dépassera pas les redevances payées'"),
    "cuad_change_of_control":
        ("si la clause traite des conséquences d'un changement de contrôle d'une partie",
         "changement de contrôle — ex: résiliation automatique si acquisition par un tiers"),
    "cuad_competitive_restriction_exception":
        ("si la clause prévoit des exceptions à une restriction de concurrence",
         "exception à la non-concurrence — ex: activités préexistantes exemptées"),
    "cuad_covenant_not_to_sue":
        ("si la clause contient un engagement de ne pas intenter de poursuites",
         "engagement de ne pas poursuivre — ex: renonciation à tout recours sur la PI concédée"),
    "cuad_effective_date":
        ("si la clause précise la date d'entrée en vigueur du contrat",
         "date d'entrée en vigueur — ex: 'le présent accord prend effet le 1er janvier 2024'"),
    "cuad_exclusivity":
        ("si la clause impose une exclusivité à l'une ou l'autre partie",
         "exclusivité — ex: 'le distributeur est le seul autorisé dans le territoire désigné'"),
    "cuad_expiration_date":
        ("si la clause précise la date d'expiration ou la durée du contrat",
         "date d'expiration ou durée — ex: 'le contrat expire 3 ans après la date de signature'"),
    "cuad_governing_law":
        ("si la clause désigne la loi applicable au contrat",
         "loi applicable — ex: 'le présent contrat est régi par les lois de la province de Québec'"),
    "cuad_insurance":
        ("si la clause impose des obligations d'assurance à une partie",
         "assurance — ex: 'le prestataire doit maintenir une assurance responsabilité civile d'au moins 2 M$'"),
    "cuad_ip_ownership_assignment":
        ("si la clause attribue la propriété de la propriété intellectuelle créée dans le cadre du contrat",
         "cession de PI — ex: 'toute création réalisée dans le cadre du présent contrat appartient au client'"),
    "cuad_irrevocable_or_perpetual_license":
        ("si la clause accorde une licence irrévocable ou perpétuelle",
         "licence irrévocable ou perpétuelle — ex: 'licence perpétuelle, non exclusive et irrévocable'"),
    "cuad_joint_ip_ownership":
        ("si la clause prévoit une copropriété de la propriété intellectuelle",
         "copropriété de PI — ex: 'les parties seront copropriétaires à parts égales des innovations conjointes'"),
    "cuad_license_grant":
        ("si la clause contient une concession de licence",
         "concession de licence — ex: 'le concédant accorde au preneur une licence non exclusive d'utilisation'"),
    "cuad_liquidated_damages":
        ("si la clause prévoit des dommages-intérêts liquidés ou une clause pénale",
         "clause pénale ou dommages liquidés — ex: 'en cas de retard, une pénalité de 500$/jour s'applique'"),
    "cuad_minimum_commitment":
        ("si la clause impose un engagement minimal d'achat ou de volume",
         "engagement minimal — ex: 'l'acheteur s'engage à commander au moins 500 unités par trimestre'"),
    "cuad_most_favored_nation":
        ("si la clause contient une clause de la nation la plus favorisée ou de meilleur prix",
         "clause MFN ou meilleur prix — ex: 'le fournisseur garantit que les prix ne seront pas inférieurs à ceux offerts à d'autres clients'"),
    "cuad_no_solicit_of_customers":
        ("si la clause interdit le démarchage des clients de l'autre partie",
         "non-sollicitation des clients — ex: 'ne pas démarcher les clients de l'autre partie pendant 2 ans'"),
    "cuad_no_solicit_of_employees":
        ("si la clause interdit le recrutement des employés de l'autre partie",
         "non-sollicitation des employés — ex: 'ne pas recruter les employés de l'autre partie pendant la durée du contrat'"),
    "cuad_non_compete":
        ("si la clause interdit à une partie d'exercer des activités concurrentes",
         "non-concurrence — ex: 'ne pas exercer d'activités similaires dans un rayon de 50 km pendant 2 ans'"),
    "cuad_non_disparagement":
        ("si la clause interdit de dénigrer l'autre partie",
         "non-dénigrement — ex: 's'abstenir de tout commentaire négatif public sur l'autre partie'"),
    "cuad_non_transferable_license":
        ("si la clause stipule que la licence est non transférable",
         "licence non transférable — ex: 'la présente licence est personnelle et ne peut être transférée'"),
    "cuad_notice_period_to_terminate_renewal":
        ("si la clause précise le délai de préavis requis pour résilier ou ne pas renouveler",
         "délai de préavis de résiliation — ex: 'un préavis de 90 jours est requis pour ne pas renouveler'"),
    "cuad_post_termination_services":
        ("si la clause prévoit des services à fournir après la résiliation du contrat",
         "services post-résiliation — ex: 'le prestataire continuera à fournir des services de transition pendant 6 mois'"),
    "cuad_price_restrictions":
        ("si la clause impose des restrictions sur les prix que l'une des parties peut pratiquer",
         "restrictions de prix — ex: 'le distributeur ne peut pas vendre en dessous du prix recommandé'"),
    "cuad_renewal_term":
        ("si la clause précise les conditions de renouvellement du contrat",
         "renouvellement — ex: 'le contrat se renouvelle automatiquement pour 1 an sauf préavis contraire'"),
    "cuad_revenue_profit_sharing":
        ("si la clause prévoit un partage de revenus ou de profits entre les parties",
         "partage de revenus ou profits — ex: 'le fournisseur recevra 15% des revenus générés par le produit'"),
    "cuad_rofr_rofo_rofn":
        ("si la clause contient un droit de premier refus, de première offre ou de première négociation",
         "droit de préemption ou de premier refus — ex: 'avant toute cession, le titulaire devra proposer les parts à l'autre partie'"),
    "cuad_source_code_escrow":
        ("si la clause prévoit un séquestre du code source",
         "séquestre du code source — ex: 'le fournisseur déposera le code source chez un séquestre agréé'"),
    "cuad_termination_for_convenience":
        ("si la clause permet la résiliation du contrat sans cause par l'une des parties",
         "résiliation pour convenance — ex: 'chaque partie peut résilier le contrat sur préavis de 30 jours sans avoir à justifier sa décision'"),
    "cuad_third_party_beneficiary":
        ("si la clause désigne un tiers bénéficiaire du contrat",
         "tiers bénéficiaire — ex: 'la présente stipulation est faite au bénéfice de la société mère du preneur'"),
    "cuad_uncapped_liability":
        ("si la clause prévoit une responsabilité illimitée pour certains types de dommages",
         "responsabilité illimitée — ex: 'la limitation de responsabilité ne s'applique pas en cas de fraude ou de faute intentionnelle'"),
    "cuad_unlimited_all_you_can_eat_license":
        ("si la clause accorde une licence illimitée (en volume ou en utilisateurs)",
         "licence illimitée — ex: 'la licence couvre un nombre illimité d'utilisateurs au sein de l'organisation'"),
    "cuad_volume_restriction":
        ("si la clause impose une restriction sur le volume de production ou de vente",
         "restriction de volume — ex: 'le distributeur ne peut pas vendre plus de 10 000 unités par année sans accord préalable'"),
    "cuad_warranty_duration":
        ("si la clause précise la durée d'une garantie",
         "durée de garantie — ex: 'le vendeur garantit le produit contre tout défaut pendant 24 mois'"),
}

def cuad_spec(task_name, question, example_desc):
    return f"""\
## Purpose
Identifier si une clause d'un contrat commercial québécois ou canadien {question} (Oui/Non).

## Question format
Input: clause extraite d'un contrat commercial en français.
Output: `Oui` | `Non`

**Exemple de clause:** {example_desc}

## Positif — `Oui`
- La clause traite explicitement du sujet visé
- La clause implique nécessairement le sujet même sans le nommer

## Positif — `Non`
- La clause porte sur un autre sujet contractuel
- La clause effleure le sujet de manière incidente sans en faire l'objet principal
- Clause générale de représentations et garanties sans spécificité

## Sources légales
- CCQ art. 1375-1432 (règles générales des contrats)
- CCQ art. 2089 CCQ (non-concurrence entre employeur-employé)
- Loi sur les marques de commerce (LRC 1985 c T-13) — pour clauses PI
- Pratique contractuelle des barreaux du Québec et du Barreau du Haut-Canada
- Modèles de contrats commerciaux (baux commerciaux, franchises, contrats de service TI)

## Diversité
- Varier les types de contrats: bail commercial, contrat de franchise, accord de licence logicielle, contrat de service professionnel, contrat de distribution
- Varier la complexité: clauses courtes (2 lignes) vs clauses longues (10 lignes)
- Inclure des clauses en français québécois courant et en français juridique formel
- Inclure des Non trompeurs: clauses qui semblent liées mais portent sur autre chose

## Do not use
- Clauses tirées de contrats américains (choix de loi: Delaware, New York)
- Clauses en common law anglaise
- Données de a2aj/canadian-laws
""".strip()

# ── opp115_* ─────────────────────────────────────────────────────────────────

OPP115_TOPICS = {
    "opp115_data_retention": (
        "conservation des données",
        "la politique décrit combien de temps les données sont conservées et les critères de suppression"
    ),
    "opp115_data_security": (
        "sécurité des données",
        "la politique décrit les mesures de sécurité techniques ou organisationnelles pour protéger les RP"
    ),
    "opp115_do_not_track": (
        "Do Not Track / désinscription du suivi",
        "la politique mentionne comment l'organisation répond aux signaux Do Not Track ou aux demandes de désinscription du suivi"
    ),
    "opp115_first_party_collection_use": (
        "collecte et utilisation par la première partie",
        "la politique décrit quels renseignements personnels l'organisation collecte directement auprès des utilisateurs et comment elle les utilise"
    ),
    "opp115_international_and_specific_audiences": (
        "audiences internationales et spécifiques",
        "la politique contient des dispositions spéciales pour les utilisateurs internationaux, les mineurs, ou d'autres audiences spécifiques"
    ),
    "opp115_policy_change": (
        "modifications de la politique",
        "la politique décrit comment les utilisateurs seront informés des modifications apportées à la politique de confidentialité"
    ),
    "opp115_third_party_sharing_collection": (
        "partage ou collecte par des tiers",
        "la politique décrit la communication de RP à des tiers ou la collecte par des tiers"
    ),
    "opp115_user_access_edit_and_deletion": (
        "accès, modification et suppression par l'utilisateur",
        "la politique décrit les droits de l'utilisateur d'accéder, corriger ou supprimer ses RP"
    ),
    "opp115_user_choice_control": (
        "choix et contrôle de l'utilisateur",
        "la politique décrit les options offertes à l'utilisateur pour contrôler l'utilisation de ses RP (opt-in, opt-out)"
    ),
}

def opp115_spec(task_name, topic_fr, description):
    return f"""\
## Purpose
Identifier si un extrait de politique de confidentialité traite du sujet: **{topic_fr}** (Oui/Non).
Spécifiquement: {description}.

## Question format
Input: extrait d'une politique de confidentialité d'une organisation québécoise ou canadienne (en français).
Output: `Oui` | `Non`

**Exemple:**
> Extrait traitant de {topic_fr}: [clause décrivant {topic_fr}]
> → Oui

## Positif — `Oui`
- L'extrait traite explicitement ou implicitement de {topic_fr}
- {description}

## Positif — `Non`
- L'extrait traite d'un autre sujet de confidentialité non lié à {topic_fr}
- L'extrait mentionne le sujet de manière incidente sans l'aborder substantiellement

## Sources légales
- Loi 25 (Loi modernisant des dispositions législatives en matière de protection des renseignements personnels, LQ 2021 c 25)
- LPRPDE (LC 2000 c 5) et ses règlements
- Loi sur la protection des renseignements personnels dans le secteur public (RLRQ c A-2.1)
- Politiques de confidentialité d'entreprises québécoises publiées: Desjardins, Hydro-Québec, Bell, Vidéotron

## Diversité
- Varier les secteurs: finance, santé, commerce électronique, SaaS, médias sociaux
- Inclure des politiques bilingues (certains extraits en anglais pour le marché canadien)
- Inclure des formulations vagues vs très précises sur le sujet
- Inclure des Non trompeurs: extraits d'une politique de confidentialité qui parlent de RP sans aborder {topic_fr}

## Do not use
- Politiques de confidentialité d'entreprises purement américaines (CCPA, COPPA)
- Politiques conformes uniquement au RGPD (UE) sans dimension canadienne
- Données de a2aj/canadian-laws
""".strip()

# ── contract_qa ──────────────────────────────────────────────────────────────

CONTRACT_QA_SPEC = """\
## Purpose
Identifier quel type de clause contractuelle est présent dans un extrait de contrat québécois ou canadien (réponse ouverte: nom de la clause).

## Question format
Input: extrait d'un contrat commercial ou de consommation en français.
Output: nom du type de clause (ex: "clause de médiation", "clause pénale", "clause de non-concurrence")

**Exemple:**
> "Les parties conviennent de soumettre tout différend découlant du présent contrat à la médiation avant tout recours judiciaire."
> → clause de médiation / clause de règlement des différends

## Classes principales à couvrir
- Clause d'arbitrage / médiation / règlement des différends
- Clause pénale (CCQ art. 1622-1625)
- Clause de non-concurrence (CCQ art. 2089)
- Clause de confidentialité
- Clause de résiliation / résolution
- Clause limitative de responsabilité
- Clause de cession / anti-cession
- Clause de loi applicable / for contractuel
- Clause de renouvellement automatique
- Clause de garantie / représentations

## Sources légales
- CCQ art. 1371-1707 (droit des obligations et des contrats)
- Loi sur la protection du consommateur (RLRQ c P-40.1) — clauses abusives
- Code de procédure civile art. 1-7 (arbitrage conventionnel)
- Pratique contractuelle québécoise — modèles de contrats types

## Diversité
- Varier les types de contrats: bail commercial, service, emploi, franchise, licence
- Inclure des clauses longues et complexes nécessitant une identification précise
- Inclure des clauses qui combinent deux types (ex: résiliation + pénalité)
- Varier la difficulté: clauses clairement nommées vs clauses implicites

## Do not use
- Clauses de contrats sous droit américain ou droit anglais
- Termes juridiques anglais sans équivalent français
- Données de a2aj/canadian-laws
""".strip()

# ── privacy_policy_qa ─────────────────────────────────────────────────────────

PRIVACY_POLICY_QA_SPEC = """\
## Purpose
Répondre à une question spécifique sur le contenu d'une politique de confidentialité québécoise ou canadienne (Oui/Non ou réponse courte).

## Question format
Input: extrait de politique de confidentialité + question précise.
Output: `Oui` | `Non` (ou réponse courte)

**Exemple:**
> "Cette politique de confidentialité mentionne-t-elle explicitement le droit de l'utilisateur d'accéder à ses renseignements personnels?"
> → Oui (requis par Loi 25 art. 27)

## Types de questions à couvrir
- L'organisation collecte-t-elle [type de donnée]?
- La politique mentionne-t-elle le droit d'accès / de rectification / de portabilité?
- Les données sont-elles partagées avec des tiers?
- Quelle est la durée de conservation des données?
- La politique respecte-t-elle [exigence spécifique de la Loi 25]?

## Sources légales
- Loi 25 (RLRQ c P-39.1) — droits: accès (art. 27), rectification (art. 28), désindexation (art. 28.1), portabilité (art. 27.1)
- LPRPDE (LC 2000 c 5) — principes PIPEDA
- Lignes directrices du CAI (Commission d'accès à l'information du Québec)
- Politiques de confidentialité réelles d'entreprises québécoises publiées

## Diversité
- Inclure des questions sur chacun des droits de la Loi 25
- Inclure des questions dont la réponse requiert de lire entre les lignes (implicite vs explicite)
- Varier les secteurs: santé, commerce, finance, technologie
- Inclure des questions avec réponse Non (politique qui ne mentionne pas le droit)

## Do not use
- Politiques GDPR sans lien canadien
- Politiques pré-Loi 25 sans signalement que les règles ont changé
- Données de a2aj/canadian-laws
""".strip()

# ── unfair_tos ────────────────────────────────────────────────────────────────

UNFAIR_TOS_SPEC = """\
## Purpose
Classifier une clause de conditions d'utilisation (TOS) selon sa catégorie d'iniquité en droit québécois de la consommation (LPC).

## Question format
Input: clause de conditions d'utilisation ou de contrat de consommation en français.
Output: catégorie d'iniquité (voir classes ci-dessous)

**Exemple:**
> "La compagnie peut modifier unilatéralement le prix du service sans préavis."
> → Clause abusive — modification unilatérale (art. 8 + 11.2 LPC)

## Classes (catégories d'iniquité LPC)
- **Modification unilatérale**: la commerçante se réserve le droit de modifier les conditions sans consentement du consommateur
- **Limitation de responsabilité**: exclusion ou limitation de la responsabilité du commerçant au-delà de ce que la loi permet
- **Arbitrage forcé**: clause imposant l'arbitrage et écartant les recours judiciaires
- **Résiliation abusive**: conditions de résiliation unilatéralement favorables au commerçant
- **Renonciation à des droits légaux**: le consommateur renonce à des droits que la loi lui garantit
- **Acceptable**: clause conforme à la LPC et au CCQ, pas abusive

## Sources légales
- Loi sur la protection du consommateur (RLRQ c P-40.1) art. 8, 11.2, 19, 54.8, 271
- CCQ art. 1437 (clause abusive dans un contrat de consommation)
- Décisions de la Cour du Québec et des petites créances sur les clauses abusives
- Office de la protection du consommateur (OPC) — bulletins d'interprétation

## Diversité
- Varier les secteurs: abonnements en ligne, téléphonie, logiciels SaaS, services bancaires, jeux vidéo
- Inclure des clauses clairement abusives et des clauses limites (zone grise)
- Inclure des clauses qui semblent abusives mais sont valides (nuance LPC)
- Inclure la classe "Acceptable" à ~20% pour éviter le biais

## Do not use
- Directive européenne sur les clauses abusives (CJUE)
- US unconscionability doctrine
- Données de a2aj/canadian-laws
""".strip()

# ── supply_chain remaining 8 ─────────────────────────────────────────────────

SUPPLY_CHAIN_TOPICS = {
    "supply_chain_disclosure_best_practice_accountability": (
        "best_practice", "accountability",
        "des mécanismes de responsabilisation (accountability) pour les pratiques de travail dans la chaîne d'approvisionnement",
        "ex: 'Notre directeur des achats est responsable de la conformité à la Loi S-211 et rend compte annuellement au conseil d'administration.'"
    ),
    "supply_chain_disclosure_best_practice_certification": (
        "best_practice", "certification",
        "des certifications ou normes requises des fournisseurs en matière de travail éthique",
        "ex: 'Nous exigeons que nos fournisseurs de niveau 1 obtiennent la certification SA8000 ou équivalente.'"
    ),
    "supply_chain_disclosure_best_practice_training": (
        "best_practice", "training",
        "des programmes de formation sur le travail forcé offerts aux employés ou aux fournisseurs",
        "ex: 'Nos acheteurs reçoivent une formation annuelle de 4 heures sur la détection du travail forcé dans la chaîne d'approvisionnement.'"
    ),
    "supply_chain_disclosure_best_practice_verification": (
        "best_practice", "verification",
        "des processus de vérification ou de diligence raisonnable sur les pratiques de travail des fournisseurs",
        "ex: 'Nous effectuons une vérification des antécédents en matière de droits de la personne de tous les nouveaux fournisseurs avant leur homologation.'"
    ),
    "supply_chain_disclosure_disclosed_accountability": (
        "disclosed", "accountability",
        "des mécanismes de responsabilisation ayant été MIS EN OEUVRE (pas seulement planifiés)",
        "ex: 'En 2023, notre comité de conformité S-211 a tenu 6 réunions et a revu les divulgations de 42 fournisseurs.'"
    ),
    "supply_chain_disclosure_disclosed_certification": (
        "disclosed", "certification",
        "des certifications de fournisseurs EFFECTIVEMENT OBTENUES (pas seulement exigées)",
        "ex: 'Au 31 décembre 2023, 78% de nos fournisseurs de niveau 1 détenaient une certification SA8000 ou équivalente.'"
    ),
    "supply_chain_disclosure_disclosed_training": (
        "disclosed", "training",
        "des formations sur le travail forcé EFFECTIVEMENT DISPENSÉES (pas seulement planifiées)",
        "ex: 'En 2023, 142 employés ont suivi notre module de formation sur la Loi S-211, pour un total de 568 heures de formation.'"
    ),
    "supply_chain_disclosure_disclosed_verification": (
        "disclosed", "verification",
        "des vérifications de fournisseurs EFFECTIVEMENT RÉALISÉES (pas seulement décrites comme politique)",
        "ex: 'En 2023, nous avons évalué 89 fournisseurs à l'aide de notre questionnaire de diligence raisonnable S-211.'"
    ),
}

def supply_chain_spec(task_name, practice_type, topic_en, description, example):
    practice_label = "POLITIQUE / PRATIQUE PREVUE" if practice_type == "best_practice" else "ACTIVITE EFFECTIVEMENT REALISEE"
    if practice_type == "best_practice":
        positif_verb = "une politique ou un engagement relatif a"
        formulations = 'Formulations typiques: "nous nous engageons a", "notre politique prevoit", "nous exigeons de nos fournisseurs"'
        negatif_type = "une realisation passee (relevant plutot de disclosed)"
    else:
        positif_verb = "une realisation concrete portant sur"
        formulations = 'Formulations typiques: "en 2023, nous avons", "au cours de l exercice", chiffres concrets (nombre, %, dates)'
        negatif_type = "une politique future (relevant plutot de best_practice)"
    other_topics = ", ".join([t for t in ["audits", "accountability", "certification", "training", "verification"] if t != topic_en])
    lines = [
        "## Purpose",
        f"Determiner si une divulgation de chaine d'approvisionnement decrit {description} ({practice_label}), conformement a la Loi S-211 (Canada, 2023) (Oui/Non).",
        "",
        "## Question format",
        "Input: extrait d'une divulgation annuelle d'entreprise.",
        "Output: `Oui` | `Non`",
        "",
        f"**Exemple:** {example}",
        "-> Oui",
        "",
        "## Distinction cle: best_practice vs disclosed",
        "- **best_practice**: politique, engagement, ou pratique *prevue* (present ou futur)",
        "- **disclosed**: activite *effectivement realisee* au cours de l'annee de rapport (passe avec chiffres)",
        "",
        f"Cette tache porte sur: **{practice_label}**",
        "",
        "## Positif — `Oui`",
        f"- L'extrait decrit {positif_verb} {description}",
        f"- {formulations}",
        "",
        "## Positif — `Non`",
        f"- L'extrait porte sur un autre aspect de la divulgation S-211 ({other_topics})",
        f"- L'extrait est {negatif_type}",
        "",
        "## Sources legales",
        "- Loi sur la lutte contre le travail force et le travail des enfants dans les chaines d'approvisionnement (Canada, LC 2023 c 9) — Loi S-211",
        "- Registre public des rapports S-211 (gouvernement du Canada)",
        "- Rapport annuel S-211 type — guide du gouvernement du Canada",
        "",
        "## Diversite",
        "- Varier les secteurs: manufacturier, ressources naturelles, textile, alimentation, electronique",
        "- Inclure des divulgations avec chiffres precis vs divulgations vagues",
        "- Inclure des Non trompeurs: divulgations mentionnant S-211 mais decrivant un autre aspect",
        "",
        "## Do not use",
        "- California TISCA ou UK Modern Slavery Act",
        "- Donnees de a2aj/canadian-laws",
    ]
    return "\n".join(lines)

# ── Write all specs ───────────────────────────────────────────────────────────

written = 0
skipped = 0

# contract_nli
for task_name, clause_desc in CONTRACT_NLI_CLAUSES.items():
    task_dir = OLD / task_name
    if not task_dir.exists():
        print(f"SKIP {task_name}")
        skipped += 1
        continue
    (task_dir / "data_spec.md").write_text(
        contract_nli_spec(task_name, clause_desc), encoding="utf-8"
    )
    written += 1

# cuad
for task_name, (question, example_desc) in CUAD_CLAUSES.items():
    task_dir = OLD / task_name
    if not task_dir.exists():
        print(f"SKIP {task_name}")
        skipped += 1
        continue
    (task_dir / "data_spec.md").write_text(
        cuad_spec(task_name, question, example_desc), encoding="utf-8"
    )
    written += 1

# opp115
for task_name, (topic_fr, description) in OPP115_TOPICS.items():
    task_dir = OLD / task_name
    if not task_dir.exists():
        print(f"SKIP {task_name}")
        skipped += 1
        continue
    (task_dir / "data_spec.md").write_text(
        opp115_spec(task_name, topic_fr, description), encoding="utf-8"
    )
    written += 1

# individual tasks
for task_name, spec in [
    ("contract_qa", CONTRACT_QA_SPEC),
    ("privacy_policy_qa", PRIVACY_POLICY_QA_SPEC),
    ("unfair_tos", UNFAIR_TOS_SPEC),
]:
    task_dir = OLD / task_name
    if not task_dir.exists():
        print(f"SKIP {task_name}")
        skipped += 1
        continue
    (task_dir / "data_spec.md").write_text(spec, encoding="utf-8")
    written += 1

# supply_chain remaining 8
for task_name, (pt, topic_en, desc, example) in SUPPLY_CHAIN_TOPICS.items():
    task_dir = OLD / task_name
    if not task_dir.exists():
        print(f"SKIP {task_name}")
        skipped += 1
        continue
    (task_dir / "data_spec.md").write_text(
        supply_chain_spec(task_name, pt, topic_en, desc, example), encoding="utf-8"
    )
    written += 1

print(f"Written {written} data_spec.md files to old_tasks/  (skipped {skipped})")

# ======================================================================
# generate_data_specs_part3.py
# ======================================================================

# Written to task_specs/<name>/data_spec.md under the LexiorBench directory.
from pathlib import Path

SPECS_DIR = ROOT / "task_specs"
SPECS_DIR.mkdir(exist_ok=True)

SPECS = {

"ca_irac_generation": """\
## Purpose
Génerer une analyse IRAC complète (Issue, Règle, Application, Conclusion) à partir d'un extrait d'une décision CanLII.

## Question format
Input: extrait de décision judiciaire canadienne (500-2000 mots).
Output: analyse IRAC structurée en 4 parties (génération libre).

**Exemple de question:**
> Décision: [extrait d'un arrêt de la Cour d'appel du Québec sur la responsabilité médicale]
> Rédigez une analyse IRAC complète couvrant: Issue (question juridique centrale), Règle (article de loi ou principe applicable avec citation), Application (raisonnement pas à pas), Conclusion (résultat et dispositif).

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- **Issue (25%)**: question juridique bien identifiée, précise, centrée sur le litige réel
- **Règle (25%)**: article de loi ou principe correctement cité (CCQ, Charte, loi fédérale), source précise
- **Application (35%)**: raisonnement étape par étape, faits liés à la règle, anticipation des arguments opposés
- **Conclusion (15%)**: résultat cohérent avec le raisonnement, dispositif correct

## Sources pour les décisions d'entrée
- Décisions CanLII: CSC, CA-QC, Cour du Québec, Cour supérieure QC
- Domaines: responsabilité civile (CCQ 1457), bail résidentiel, droit du travail, droit administratif
- NE PAS utiliser les 60 décisions de la Phase 3 de l'entraînement LexiorGPT
- NE PAS utiliser les données de a2aj/canadian-laws

## Diversité
- Varier les domaines: civil, pénal, administratif, famille, travail
- Varier la complexité: décisions de 1 page vs 15 pages
- Inclure des décisions en français et en anglais (bilingue)
- Inclure des décisions avec dissidence (le modèle doit choisir le raisonnement majoritaire)

## Format de sortie attendu
```
**Issue:** [question juridique]
**Règle:** [article/principe + citation précise]
**Application:** [raisonnement structuré, 3-5 paragraphes]
**Conclusion:** [résultat + dispositif]
```

## Do not use
- Décisions américaines
- Décisions des 60 arrêts Phase 3 LexiorGPT
""",

"ca_clause_comparison": """\
## Purpose
Comparer deux clauses portant sur le même sujet et identifier laquelle est la plus avantageuse pour une partie désignée, avec justification selon le droit québécois ou canadien.

## Question format
Input: deux clauses sur le même sujet + indication de la partie (acheteur, vendeur, locataire, employé, etc.).
Output: identification de la clause la plus avantageuse + justification (génération libre).

**Exemple:**
> Clause A: "Le vendeur garantit le bien contre tout vice caché pendant 1 an à compter de la livraison."
> Clause B: "Le vendeur exclut toute garantie légale ou conventionnelle sur le bien vendu."
> Quelle clause est la plus avantageuse pour l'acheteur selon le CCQ?
> → Clause A (garantie légale CCQ art. 1726 vs exclusion potentiellement nulle sous art. 1733 si dol)

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- Identification correcte de la clause plus avantageuse (25%)
- Justification ancrée dans le droit applicable (CCQ, LPC, loi fédérale) avec citation (40%)
- Anticipation des risques ou nuances (ex: validité conditionnelle de la clause B) (25%)
- Clarté et structure de la réponse (10%)

## Sources pour les paires de clauses
- Modèles de contrats québécois: baux résidentiels et commerciaux, contrats de vente, contrats de service, contrats d'emploi
- CCQ arts. 1375-1707 (obligations), 1726-1731 (vices cachés), 2089 (non-concurrence)
- Loi sur la protection du consommateur (RLRQ c P-40.1)
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier les paires: garantie vs exclusion, arbitrage vs tribunal, délai court vs long
- Varier la partie avantageuse: parfois la Clause A est meilleure, parfois la Clause B
- Inclure des cas ambigus où les deux clauses ont des avantages différents
- Varier les domaines: vente, bail, emploi, service, franchise

## Format de sortie attendu
```
La clause [A/B] est la plus avantageuse pour [la partie] car [justification avec citation légale].
[Nuance: La clause [B/A] présente toutefois l'avantage de... / Le risque est que...]
```

## Do not use
- Droit américain ou droit anglais
""",

"cpc_drafting_evaluation": """\
## Purpose
Évaluer si un document juridique respecte les exigences de forme du Code de procédure civile du Québec (C.p.c.) et identifier les lacunes.

## Question format
Input: document juridique rédigé (mise en demeure, demande introductive d'instance, etc.).
Output: évaluation de la conformité au C.p.c. + liste des lacunes (génération libre).

**Exemple:**
> Document: [mise en demeure rédigée]
> Cette mise en demeure respecte-t-elle les exigences des art. 110-111 C.p.c.? Identifiez les lacunes s'il y en a.

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- Identification correcte du type de document et des articles applicables (20%)
- Vérification de tous les éléments obligatoires (nom des parties, objet, délai, conséquences) (40%)
- Identification précise des lacunes avec référence à l'article violé (30%)
- Suggestion concrète de correction (10%)

## Types de documents à couvrir
- Mise en demeure (C.p.c. art. 110-111)
- Demande introductive d'instance (C.p.c. art. 141-148)
- Déclaration sous serment / affidavit (C.p.c. art. 86-88)
- Inscription pour instruction et jugement (C.p.c. art. 172-173)

## Sources
- Code de procédure civile du Québec (RLRQ c C-25.01)
- Collection Barreau du Québec — procédure civile
- Modèles de documents judiciaires (Wilson & Lafleur)
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité des documents de test
- Inclure des documents conformes (réponse: aucune lacune)
- Inclure des documents avec 1-2 lacunes mineures
- Inclure des documents avec lacunes majeures (vices de forme invalidants)
- Varier les types: mise en demeure, demande, affidavit

## Do not use
- Federal Rules of Civil Procedure (US)
- Rules of Civil Procedure (Ontario)
""",

"ca_summary_precision": """\
## Purpose
Résumer une décision CanLII en 5-7 phrases — évalué sur la fidélité factuelle et la complétude.

## Question format
Input: décision judiciaire complète (ou extrait substantiel de 1000-3000 mots).
Output: résumé de 5-7 phrases (génération libre).

**Exemple:**
> Décision: [arrêt CanLII complet]
> Rédigez un résumé de 5 à 7 phrases couvrant: parties, contexte factuel, question juridique centrale, règle applicable, raisonnement, conclusion.

## Critères d'évaluation (rubrique LLM-judge GPT-4o)
- **Parties et contexte (15%)**: identification correcte des parties et du contexte factuel
- **Question juridique (20%)**: formulation précise de la question centrale
- **Règle (20%)**: règle applicable correctement citée (article, nom du principe)
- **Raisonnement (30%)**: synthèse fidèle du raisonnement sans déformation
- **Conclusion (15%)**: résultat correct (accueillie/rejetée/renvoyée)

## Sources pour les décisions de test
- Décisions CanLII disponibles publiquement: CSC, CA-QC, Cour fédérale, Cour du Québec
- Varier les domaines: civil, pénal, administratif, familial, travail
- Résumés de référence validés par juristes (ground truth)
- NE PAS utiliser les 60 décisions Phase 3 LexiorGPT
- NE PAS utiliser a2aj/canadian-laws

## Diversité
- Varier la longueur des décisions (1 page vs 30 pages)
- Inclure des décisions avec dissidence (résumé doit indiquer le désaccord)
- Inclure des décisions en français et en anglais
- Inclure des décisions récentes (post-2020) pour éviter données d'entraînement

## Format de sortie attendu
5-7 phrases continues (pas de liste à puces) couvrant parties → faits → question → règle → raisonnement → résultat.

## Do not use
- Résumés déjà publiés sur CanLII (risque de copie)
- Décisions de la Phase 3 d'entraînement LexiorGPT
""",

"ca_false_premise": """\
## Purpose
Identifier une fausse prémisse juridique dans une question et expliquer pourquoi elle est incorrecte, en citant le droit canadien ou québécois applicable.

## Question format
Input: question contenant une fausse prémisse juridique.
Output: identification de la fausse prémisse + correction avec citation légale (classification + génération).

**Exemple:**
> "Selon l'art. 1720 CCQ, la garantie légale contre les vices cachés dure 5 ans. Mon recours est-il prescrit après 4 ans?"
> → Fausse prémisse: le délai de prescription des vices cachés n'est pas 5 ans mais 3 ans (art. 2925 CCQ). La garantie légale (art. 1726 CCQ) est distincte de la prescription (art. 2925 CCQ).

## Classes
- `Oui` (fausse prémisse présente): la question contient une erreur factuelle sur le droit
- `Non` (prémisse correcte): la question est factuellement correcte sur le droit

## Critères d'évaluation
- Identification de la prémisse erronée (25%)
- Citation correcte de l'article ou du principe qui corrige l'erreur (35%)
- Explication claire de pourquoi c'est une erreur (25%)
- Réponse à la question réelle (si elle en a une) (15%)

## Types de fausses prémisses à inclure
- Mauvais délai de prescription (art. 2925 CCQ est 3 ans, pas 5 ans)
- Référence à une loi abrogée (C.c.B.-C. → CCQ 1994)
- Confusion entre régimes juridiques (SAAQ vs responsabilité civile ordinaire)
- Mauvais tribunal compétent (Cour du Québec < 100 000$ vs Cour supérieure ≥ 100 000$)
- Droits inexistants en droit québécois (dépôt de garantie de loyer interdit CCQ 1904)

## Sources légales
- CCQ (toutes les matières)
- LPC, LNT, C.p.c., Charte québécoise
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier les domaines: bail, responsabilité civile, succession, contrat, procédure
- Inclure des erreurs subtiles (différence d'un an dans un délai)
- Inclure des erreurs grossières (loi inexistante, droit impossible)
- Inclure ~30% de `Non` (questions avec prémisse correcte)

## Do not use
- Fausses prémisses sur le droit américain ou européen
- Questions sans enjeu légal clair
""",

"canadian_judicial_ethics": """\
## Purpose
Répondre Oui/Non à des questions sur les règles d'éthique judiciaire canadiennes (Code de déontologie de la magistrature, TR/2002-76).

## Question format
Input: scénario ou énoncé sur la conduite d'un juge.
Output: `Oui` (comportement conforme) | `Non` (comportement contraire à l'éthique)

**Exemple:**
> "Un juge peut-il accepter une invitation à un voyage de golf offert par un cabinet d'avocats qui plaide régulièrement devant lui?"
> → Non (Code de déontologie de la magistrature, principe d'impartialité)

## Positif — `Oui` (comportement éthique)
- Juge se récuse volontairement pour conflit d'intérêts potentiel
- Juge refuse un cadeau d'une partie ou d'un avocat plaidant devant lui
- Juge s'abstient de commenter publiquement une affaire en cours

## Positif — `Non` (comportement non éthique)
- Juge accepte des avantages de parties ou d'avocats ayant des affaires devant lui
- Juge s'engage dans des activités politiques partisanes
- Juge ne se récuse pas malgré un conflit d'intérêts évident
- Juge fait des déclarations publiques qui compromettent son impartialité apparente

## Sources légales
- Code de déontologie de la magistrature (TR/2002-76)
- Loi sur les juges (LRC 1985 c J-1)
- Conseil canadien de la magistrature — Principes de déontologie judiciaire
- Décisions du CCM sur les plaintes (disponibles en ligne)

## Diversité
- Couvrir: indépendance, impartialité, intégrité, diligence, égalité, expression
- Inclure des situations limites (activités communautaires, dons à des organismes de charité)
- Inclure des situations impliquant la famille proche du juge
- Varier entre juges de première instance et juges d'appel

## Do not use
- ABA Model Code of Judicial Conduct (US)
- Code d'éthique des avocats (pas des juges)
- Données de a2aj/canadian-laws
""",

"competence_territoriale_ccq": """\
## Purpose
Déterminer si les autorités québécoises ont compétence territoriale sur un défendeur dans un litige donné, selon les art. 3148 CCQ et suivants (Oui/Non + explication).

## Question format
Input: scénario décrivant un litige avec un élément d'extranéité.
Output: `Oui` (compétence des tribunaux québécois) | `Non` (pas compétents) + justification.

**Exemple:**
> "Marie (Québec) poursuit une entreprise ontarienne qui lui a vendu en ligne un produit défectueux livré à son domicile au Québec. Les tribunaux québécois ont-ils compétence?"
> → Oui — art. 3148(3) CCQ: préjudice subi au Québec

## Positif — `Oui` — critères de l'art. 3148 CCQ
- Défendeur domicilié au Québec
- Défendeur a un établissement au Québec et le litige est lié à cet établissement
- Faute commise au Québec ou préjudice subi au Québec
- Obligation née ou exécutable au Québec
- Les parties ont choisi le Québec comme for contractuel

## Positif — `Non`
- Aucun des critères de l'art. 3148 CCQ n'est rempli
- Le défendeur peut invoquer l'art. 3135 CCQ (forum non conveniens)
- Clause attributive de compétence en faveur d'un autre tribunal

## Sources légales
- CCQ art. 3148-3154 (compétence internationale des autorités du Québec)
- CCQ art. 3135 (forum non conveniens)
- CCQ art. 3148(5) (choix de for contractuel)
- Décisions CanLII: Cour supérieure QC (requêtes en déclinature de compétence)

## Diversité
- Varier: défendeurs de différentes provinces canadiennes, des États-Unis, d'Europe
- Inclure: commerce électronique, contrats de service à distance, accidents extraterritoriaux
- Inclure des cas de forum non conveniens (compétence formelle mais plus appropriée ailleurs)
- Varier la difficulté: critère évident vs critère limite

## Do not use
- US diversity jurisdiction (28 USC 1332)
- Long-arm statutes américains
- Données de a2aj/canadian-laws
""",

"ca_bilingual_parity": """\
## Purpose
Métrique transversale — mesurer si le modèle répond de manière équivalente en français et en anglais sur les mêmes questions.
NOTE: ce n'est pas une tâche standalone — c'est une métrique implémentée au niveau du runner.

## Implementation
1. Sélectionner un sous-ensemble de tâches existantes (ex: learned_hands_housing, civil_rule_recall_ccq)
2. Créer des versions EN des questions déjà en FR (traduction fidèle)
3. Exécuter chaque version (FR et EN) sur le modèle
4. Calculer l'écart de balanced_accuracy entre FR et EN
5. Signaler un écart > 5 points comme "parité insuffisante"

## Format des données
Ajouter un fichier `test_en.tsv` aux tâches sélectionnées, avec les mêmes questions traduites fidèlement en anglais. Le `test.tsv` original (en FR) reste la source principale.

## Seuil
- Écart ≤ 5 points → parité acceptable
- Écart 5-10 points → avertissement
- Écart > 10 points → parité insuffisante, signaler dans le rapport benchmark

## Tâches prioritaires pour la parité
- learned_hands_* (issue-spotting bilingue)
- civil_rule_recall_ccq (règles du CCQ en FR + EN)
- supply_chain_disclosure_* (textes bilingues soumis aux entreprises)
- canadian_*_recall (lois fédérales bilingues)

## Do not use
- Traductions automatiques sans révision (risque d'introduire des biais de traduction)
- Données de a2aj/canadian-laws
""",

"ca_jurisdiction_detection": """\
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
""",

"ca_outdated_law_detection": """\
## Purpose
Détecter si une question ou un énoncé juridique fait référence à une loi obsolète ou abrogée, et citer la version actuelle applicable.

## Question format
Input: question ou énoncé contenant une référence légale (potentiellement périmée).
Output: `Oui` (référence périmée) | `Non` (référence à jour) + correction si Oui.

**Exemple:**
> "Selon l'art. 1056 C.c.B.-C., quels sont les délais de prescription en responsabilité civile?"
> → Oui — le Code civil du Bas-Canada a été remplacé par le CCQ le 1er janvier 1994. L'article pertinent est maintenant art. 2925 CCQ (prescription de 3 ans).

## Positif — `Oui` (référence périmée)
- Référence au C.c.B.-C. (remplacé par CCQ en 1994)
- Référence à la Loi sur la protection du consommateur avant les amendements de 2017 ou 2023
- Référence à Dunsmuir (remplacé par Vavilov 2019) comme critère de contrôle judiciaire
- Référence à la Loi sur les jeunes contrevenants (remplacée par LSJPA en 2003)
- Référence à une version d'une loi modifiée depuis

## Positif — `Non` (référence à jour)
- Référence correcte au CCQ, LPC, LNT, Code criminel dans leur version actuelle
- Référence à un arrêt toujours bon droit (Clements, Vavilov, Jordan)

## Sources
- Historique législatif québécois et fédéral (légisQuébec.gouv.qc.ca, justice.gc.ca)
- Table des lois abrogées ou remplacées
- Répertoire de jurisprudence CanLII pour identifier les arrêts overrulés
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier les époques: pré-1994 (C.c.B.-C.), 1994-2015, 2015-aujourd'hui
- Inclure des amendements récents de la Loi 25 (2022-2023)
- Inclure des arrêts overrulés vs arrêts toujours bon droit
- ~40% Non (références à jour) pour équilibrer

## Do not use
- Références à des lois américaines (toujours hors périmètre)
- Lois hypothétiques ou inventées
""",

"ca_actor_role_identification": """\
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
""",

"ca_numerical_value_extraction": """\
## Purpose
Extraire et identifier tous les valeurs numériques significatives (dates, délais, montants, pourcentages, années) dans un texte juridique canadien, avec leur signification légale.

## Question format
Input: extrait d'une décision judiciaire ou d'un article de loi.
Output: liste structurée des valeurs numériques et leur signification (extraction).

**Exemple:**
> "Le demandeur dispose de 3 ans à compter de la connaissance du préjudice pour intenter son recours (art. 2925 CCQ). L'indemnité accordée est de 15 000$ dont 5 000$ pour préjudice moral. La décision est rendue le 12 mars 2023."
> → Délai de prescription: 3 ans (art. 2925 CCQ) | Indemnité totale: 15 000$ | Dont préjudice moral: 5 000$ | Date du jugement: 12 mars 2023

## Types de valeurs à extraire
- **Délais**: prescription, préavis, délai de dénonciation, délai d'appel
- **Montants**: dommages-intérêts, amendes, seuils de compétence (100 000$ Cour du Québec)
- **Dates**: date du jugement, date des faits, date de la demande
- **Pourcentages**: taux d'intérêt, taux de réduction, quote-part
- **Durées**: durée d'un contrat, durée d'une garantie, durée d'une peine

## Sources
- Articles du CCQ contenant des valeurs précises: art. 1604 (réduction de 50% faute de la victime), art. 2925 (3 ans), art. 1623 (pénalité contractuelle)
- Décisions de petites créances QC (montants précis, dates importantes)
- Seuils légaux: aide juridique, compétence des tribunaux, franchise d'assurance
- NE PAS utiliser de données de a2aj/canadian-laws

## Diversité
- Varier: extraits courts (1-2 valeurs) vs extraits complexes (8+ valeurs)
- Inclure des valeurs imbriquées (ex: "3 ans moins 1 jour" = calcul requis)
- Inclure des valeurs dont la signification légale est non-évidente
- Varier les domaines: bail (délais TAL), travail (seuils LNT), succession (calculs de parts)

## Format de sortie attendu
Liste structurée: [Type de valeur]: [valeur] — [signification légale + source si applicable]

## Do not use
- Textes juridiques américains (dollars US, federal thresholds)
- Données de a2aj/canadian-laws
""",

}

written = 0
for name, content in SPECS.items():
    task_dir = SPECS_DIR / name
    task_dir.mkdir(exist_ok=True)
    (task_dir / "data_spec.md").write_text(content.strip(), encoding="utf-8")
    written += 1
    print(f"  {name}")

print(f"\nWritten {written} data_spec.md files to task_specs/")