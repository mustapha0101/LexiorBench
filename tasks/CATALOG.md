# LexiorBench Task Catalog

Generated from the current `tasks/` folders.

Total tasks: 128

## Summary

### Reasoning types

- `cross_task_metric`: 1
- `interpretation`: 79
- `issue_spotting`: 18
- `rhetorical`: 8
- `rule_application`: 7
- `rule_application_conclusion`: 3
- `rule_conclusion`: 4
- `rule_recall`: 8

### Answer types

- `classification`: 110
- `classification_and_generation`: 11
- `cross_task_metric`: 1
- `generation`: 6

### Jurisdictions

- `both`: 99
- `federal_ca`: 13
- `quebec`: 16

### Metrics

- `balanced_accuracy`: 111
- `llm_judge`: 16
- `parity_analysis`: 1

## Tasks

### ca_actor_role_identification

- **Jurisdiction:** `both`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Extraction
- **Metric:** `llm_judge`
- **Purpose:** Given a court decision excerpt, correctly identify all legal actors and their roles (plaintiff, defendant, judge, expert witness, intervener, appellant, respondent)
- **Sample rows:** 8

**Sample Q&A:**

> **Q:** Dans l'affaire Bélanger c. Constructions Méridien inc., Éric Bélanger soutient avoir subi des dommages à la suite de vices de construction dans son immeuble. Constructions Méridien inc. conteste toute responsabilité. Rôle d'Éric Bélanger ?
> **A:** Demandeur
>
> **Q:** Sylvie Tremblay a été blessée dans un accident impliquant un autobus de la Société de transport de Montréal. Elle a intenté une action en responsabilité civile. Rôle de la Société de transport de Montréal ?
> **A:** Défendeur
>

### ca_affiliate_license_agreement

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause d'un contrat commercial accorde une licence aux sociétés affiliées du preneur de licence (Oui/Non).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Concédant accorde au Preneur une licence non exclusive d'utilisation du Logiciel, y compris pour toutes les filiales et sociétés affiliées du Preneur, soit toute entité dans laquelle le Preneur détient directement ou indirectement plus de cinquante pour cent (50 %) des droits de vote ou du capita?
> **A:** Oui
>
> **Q:** Le Franchiseur accorde au Franchisé le droit d'exploiter le réseau de franchise sous l'enseigne protégée dans le territoire délimité à l'Annexe A. Ce droit d'exploitation s'étend aux entités corporatives que le Franchisé contrôle à plus de cinquante pour cent (50 %) et qui exercent leurs activités e?
> **A:** Oui
>

### ca_bilingual_parity

- **Jurisdiction:** `both`
- **Reasoning type:** `cross_task_metric`
- **Answer type:** `cross_task_metric`
- **Answer detail:** Parity score
- **Metric:** `parity_analysis`
- **Purpose:** Measure if the model answers equally well in French and English — same questions posed in both languages, scores compared for parity
- **Sample rows:** 0

### ca_clause_comparison

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `generation`
- **Answer detail:** Free text
- **Metric:** `llm_judge`
- **Purpose:** Given two clauses on the same topic, which is more favorable for party X? Explain.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Version A : « Le présent accord est régi par les lois du Québec. » — Version B : « Le présent accord est régi par les lois du Québec, et les parties se soumettent à la compétence exclusive des tribunaux du district judiciaire de Montréal. »
> **A:** Différence 1 : La version B ajoute une clause d'élection de for désignant les tribunaux de Montréal. Portée juridique : sans cette clause, la compétence territoriale doit être déterminée selon les règles générales du C.p.c. (art. 41-47) ; avec la clause, les parties limitent contractuellement les fo?
>
> **Q:** Version A : « En cas de retard dans la livraison, le vendeur paie une pénalité de 1 % du prix par jour ouvrable de retard. » — Version B : « En cas de retard dans la livraison, le vendeur paie une pénalité de 1 % du prix par jour ouvrable de retard, jusqu'à concurrence de 10 % du prix total. »
> **A:** Différence 1 : La version B plafonne la pénalité à 10 % du prix total. Portée juridique : en droit québécois, une clause pénale (art. 1622-1625 CCQ) peut être réduite par le tribunal si excessive, mais un plafonnement contractuel prévu à l'avance est valide et prévisible. La version B limite le risq?
>

### ca_false_premise

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_recall`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Refusal + explain
- **Metric:** `llm_judge`
- **Purpose:** This question contains a false legal premise — identify it and explain why it is wrong
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Question : « Depuis quand la prescription extinctive de droit commun est-elle de trois ans en droit québécois ? » — Affirmation implicite : La prescription de droit commun est de trois ans.
> **A:** Prémisse correcte
>
> **Q:** Question : « Quelles sont les sanctions prévues par la Loi S-211 pour les entreprises qui ne déposent pas leur rapport annuel sur la chaîne d'approvisionnement ? » — Affirmation implicite : La Loi S-211 prévoit des sanctions pour le non-dépôt du rapport annuel.
> **A:** Prémisse correcte
>

### ca_irac_generation

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_application`
- **Answer type:** `generation`
- **Answer detail:** IRAC
- **Metric:** `llm_judge`
- **Purpose:** Générer une analyse IRAC (Problème-Règle-Application-Conclusion) à partir d'un extrait de décision judiciaire québécoise ou canadienne.
- **Sample rows:** 4

**Sample Q&A:**

> **Q:** Marie Tremblay circule à vélo sur la piste cyclable du parc municipal lorsque, sans avertissement, Pierre Lachance ouvre brusquement la portière de sa voiture stationnée le long de la piste. Marie est projetée au sol et subit une fracture du poignet ainsi qu'une déchirure à l'épaule. Les dommages mé?
> **A:** Problème: Pierre Lachance est-il responsable des dommages subis par Marie Tremblay à la suite de l'ouverture brusque de sa portière sur une piste cyclable?\nRègle: Selon l'art. 1457 CCQ, toute personne qui, par sa faute, cause un préjudice à autrui est tenue de le réparer. La faute s'apprécie par ra?
>
> **Q:** En mars 2021, Josée Bouchard achète un condo auprès de Constructions DuPont inc., entrepreneur qui a rénové et revendu l'unité. En octobre 2023, Josée découvre une importante infiltration d'eau dans les murs de la salle de bain causée par un défaut de calfeutrage des joints de la douche. Un expert c?
> **A:** Problème: Josée Bouchard peut-elle exercer un recours en garantie contre les vices cachés contre Constructions DuPont inc., et son action est-elle prescrite?\nRègle: L'art. 1726 CCQ oblige le vendeur à garantir que le bien est exempt de vices cachés qui le rendent impropre à l'usage auquel il est de?
>

### ca_jurisdiction_detection

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_recall`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (juridiction compétente + base légale)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier la juridiction compétente (Cour du Québec, Cour supérieure, Cour fédérale, etc.) pour une affaire décrite
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un locataire conteste une décision de résilier son bail pour non-paiement de loyer. Le loyer mensuel est de 1 200 $. Le propriétaire a suivi la procédure de mise en demeure prévue par la loi.
> **A:** Tribunal administratif du logement\nBase légale : art. 28 de la Loi sur le Tribunal administratif du logement, RLRQ c T-15.01
>
> **Q:** Une personne réclame 18 000 $ en dommages-intérêts à un entrepreneur en construction pour des malfaçons dans la rénovation de sa maison. Il n'y a pas de contrat de consommation impliqué.
> **A:** Cour du Québec (Division des petites créances si ≤15 000 $) ou Chambre civile\nBase légale : art. 34 et 953 CPC — la Division des petites créances est compétente jusqu'à 15 000 $ ; au-delà, la Chambre civile de la Cour du Québec s'il s'agit d'un montant de 15 001 $ à 85 000 $.
>

### ca_numerical_value_extraction

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_application`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Extraction
- **Metric:** `llm_judge`
- **Purpose:** Extract and correctly identify all numerical values in a legal text — dates, deadlines, amounts, years, percentages — and their legal significance
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Art. 82 LNT : « L'employeur qui met fin à un contrat à durée indéterminée doit donner à son salarié un avis d'une semaine si ce dernier lui a rendu moins d'un an de service ; deux semaines si ce dernier lui a rendu entre un an et cinq ans de service ; quatre semaines si ce dernier lui a rendu entre ?
> **A:** 1 semaine : délai de préavis pour moins d'un an de service\n2 semaines : délai de préavis pour 1 à 5 ans de service\n4 semaines : délai de préavis pour 5 à 10 ans de service\n8 semaines : délai de préavis pour 10 ans et plus de service\nSignification juridique : le non-respect de ces délais expose l?
>
> **Q:** Art. 2925 et 2926 CCQ : « Le droit d'action qui n'est pas soumis à une autre prescription se prescrit par trois ans. Le droit d'action en réparation du préjudice corporel se prescrit par trois ans à compter du jour où la victime a eu connaissance de son préjudice, sans jamais pouvoir être intentée p?
> **A:** 3 ans : prescription extinctive de droit commun (art. 2925 CCQ)\n3 ans : prescription spécifique pour le préjudice corporel, calculée à partir de la connaissance du préjudice\n10 ans : délai de prescription absolu (butoir) pour le préjudice corporel\nSignification juridique : le délai de 10 ans est ?
>

### ca_outdated_law_detection

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_recall`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (À jour / Partiellement désuet / Désuet)
- **Metric:** `llm_judge`
- **Purpose:** Detect if a legal question references an outdated or amended law — model must flag the outdated premise and cite the current version
- **Sample rows:** 9

**Sample Q&A:**

> **Q:** Extrait : « Le contrat de travail est régi par la Loi sur les normes du travail, RLRQ c N-1.1. Le salarié a droit à un préavis de congédiement calculé selon l'art. 82 LNT, à raison d'une semaine par année de service jusqu'à un maximum de huit semaines. »
> **A:** À jour
>
> **Q:** Extrait : « La protection des renseignements personnels dans le secteur privé au Québec est encadrée par la Loi sur la protection des renseignements personnels dans le secteur privé, RLRQ c P-39.1, telle que modifiée par la Loi 25 entrée en vigueur progressivement entre 2022 et 2023. »
> **A:** À jour
>

### ca_summary_precision

- **Jurisdiction:** `both`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (Précis / Incomplet / Inexact)
- **Metric:** `llm_judge`
- **Purpose:** Évaluer la précision juridique d'un résumé de décision judiciaire québécoise ou canadienne (Précis / Incomplet / Inexact)
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Source : « La Cour conclut que le défendeur a commis une faute en ne respectant pas les normes de sécurité applicables, que cette faute a directement causé les blessures du demandeur, et condamne le défendeur à payer 45 000 $ à titre de dommages-intérêts compensatoires. » — Résumé : « La Cour a cond?
> **A:** Précis
>
> **Q:** Source : « Le contrat est formé par le seul échange des consentements. Il peut être verbal, écrit ou résulter de tout comportement non équivoque des parties. » — Résumé : « Un contrat nécessite l'échange de consentements et peut être conclu verbalement, par écrit ou par comportement implicite. »
> **A:** Précis
>

### ca_tax_credit_entailment

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_conclusion`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Vérifier si un contribuable remplit les conditions d'admissibilité à un crédit d'impôt selon une règle fiscale donnée (LIR / Loi sur les impôts).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Scénario : Marie, 67 ans, résidant en Ontario, a reçu un certificat pour le crédit d'impôt pour personnes handicapées (formulaire T2201) approuvé par l'ARC, attestant qu'elle souffre d'une déficience grave et prolongée de ses fonctions mentales. Elle n'a aucun revenu suffisant pour utiliser pleineme?
> **A:** Vrai
>
> **Q:** Scénario : Patrick, travailleur autonome à Montréal, a versé 2 500 $ en dons à des organismes de bienfaisance enregistrés auprès de l'ARC au cours de l'année d'imposition 2023. Il dispose des reçus officiels de dons correspondants. Son revenu net s'élève à 85 000 $. — Affirmation : Patrick peut dema?
> **A:** Vrai
>

### ca_tax_deduction_entailment

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_conclusion`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Vérifier si un contribuable remplit les conditions pour bénéficier d'une déduction fiscale selon une règle fiscale donnée (LIR / Loi sur les impôts).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Scénario : Hind est consultante autonome en technologie de l'information. Elle consacre une pièce de son appartement exclusivement à son bureau à domicile, représentant 15 % de la superficie totale de son logement. Ses dépenses de loyer annuelles s'élèvent à 18 000 $. Elle travaille principalement d?
> **A:** Vrai
>
> **Q:** Scénario : Antoine est employé d'une société de construction et est contractuellement tenu d'utiliser son propre camion pour se rendre sur différents chantiers. Son employeur a signé un formulaire T2200 attestant que ces conditions s'appliquent. Antoine a engagé 8 400 $ en frais de véhicule non remb?
> **A:** Vrai
>

### canada_tax_court_outcomes

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Succès total / Succès partiel / Rejet)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identify outcome of a Tax Court of Canada decision
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un contribuable conteste la cotisation de l'ARC qui a refusé la totalité de ses dépenses d'entreprise, alléguant qu'elles étaient personnelles. La CCI conclut que toutes les dépenses étaient effectivement liées à l'exploitation de l'entreprise et ordonne l'annulation complète de la cotisation.
> **A:** Succès total
>
> **Q:** Un actionnaire conteste la qualification d'une distribution comme dividende imposable. La Cour accueille le pourvoi dans sa totalité, conclut à l'absence de dividende réputé et annule la cotisation en entier.
> **A:** Succès total
>

### canadian_legal_ethics

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_recall`
- **Answer type:** `classification`
- **Answer detail:** Binary (Manquement / Pas de manquement)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si un scénario soulève un manquement déontologique d'un juge ou d'un avocat dans un contexte canadien ou québécois.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un juge de la Cour supérieure du Québec siège dans un litige commercial opposant deux entreprises. Il ne divulgue pas aux parties qu'il détient des actions dans l'une des sociétés défenderesses via un compte de fiducie dont il est bénéficiaire. Le jugement est favorable à cette société.
> **A:** Manquement
>
> **Q:** Un avocat représente deux coaccusés dans la même affaire criminelle. À mi-procès, il apprend que les intérêts de ses clients deviennent divergents : l'un veut témoigner contre l'autre en échange d'une clémence. L'avocat continue à représenter les deux sans en informer le tribunal ni obtenir le conse?
> **A:** Manquement
>

### ccq_v_common_law

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_conclusion`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Droit civil québécois / Common law canadienne / Les deux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Is this contract governed by the CCQ (Quebec civil law) or common law?
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Une entreprise québécoise vend des équipements industriels à une autre entreprise québécoise. Le contrat est rédigé en français, signé à Montréal, et les livraisons se font à l'usine de l'acheteur à Laval. Aucun choix de loi explicite n'est prévu.
> **A:** Droit civil québécois (CCQ)
>
> **Q:** Une PME montréalaise conclut un contrat de distribution avec un distributeur torontois pour la revente de produits au Québec uniquement. Le contrat prévoit que la propriété des biens est transférée à la livraison à Montréal. Le contrat ne comporte aucune clause de choix de loi.
> **A:** Droit civil québécois (CCQ)
>

### citation_prediction_classification

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Favorable / Défavorable / Non cité)
- **Metric:** `balanced_accuracy`
- **Purpose:** Prédire si une décision judiciaire sera citée favorablement, défavorablement ou non citée dans les décisions subséquentes
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Extrait de décision : la Cour suprême dans Donoghue c. Stevenson [1932] AC 562 a posé le principe fondateur du droit de la responsabilité fondé sur la négligence en common law : l'existence d'un devoir de diligence envers son prochain. Ce principe est constamment cité avec approbation dans les décis?
> **A:** Favorable
>
> **Q:** Extrait de décision : la règle formulée dans Anns c Merton London Borough Council [1978] AC 728 concernant le test en deux étapes pour le devoir de diligence en droit public a été suivie par les tribunaux canadiens dans de nombreuses affaires avant d'être reformulée dans Cooper c Hobart 2001 CSC 79.?
> **A:** Favorable
>

### citation_prediction_open

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_recall`
- **Answer type:** `generation`
- **Answer detail:** Free text
- **Metric:** `llm_judge`
- **Purpose:** Generate the correct citation for this legal quote
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Extrait (tronqué avant les références) : « La Cour conclut que la demanderesse a démontré les trois éléments constitutifs de la responsabilité civile extracontractuelle : une faute du défendeur consistant en son omission d'entretenir son trottoir, un préjudice corporel subi par la demanderesse (frac?
> **A:** Art. 1457 CCQ (responsabilité civile extracontractuelle, faute, préjudice, lien de causalité)\nArt. 1458 CCQ (responsabilité contractuelle vs extracontractuelle)\nClements c Clements 2012 CSC 32 (test de causalité)\nArt. 976 CCQ (troubles de voisinage si applicable)\nDominique Goubau (dir), Droit de?
>
> **Q:** Extrait (tronqué avant les références) : « Le tribunal analyse la validité d'une clause d'exclusion de responsabilité dans un contrat d'adhésion conclu entre un commerçant et un consommateur. Bien que la clause soit rédigée clairement, son effet est de priver le consommateur de tout recours pour les?
> **A:** Art. 1437 CCQ (clause abusive dans un contrat d'adhésion)\nArt. 8 Loi sur la protection du consommateur, RLRQ c P-40.1 (clauses abusives)\nArt. 1432 CCQ (règle contra proferentem — interprétation en faveur du débiteur)\nHydro-Québec c Matta, 2020 QCCA (clause d'exclusion)\nMassol c Apple Inc, 2016 Q?
>

### civil_issue_spotting_responsabilite

- **Jurisdiction:** `quebec`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario soulève une question de responsabilité civile extracontractuelle (art. 1457 CCQ).
- **Sample rows:** 9

**Sample Q&A:**

> **Q:** Un chauffeur de livraison distraite par son téléphone cellulaire grille un feu rouge et percute un véhicule dont le conducteur subit de graves blessures à la colonne vertébrale, l'immobilisant pendant six mois.
> **A:** Oui
>
> **Q:** Une pharmacienne remet à un client un médicament qui n'est pas celui prescrit par le médecin en raison d'une confusion entre deux noms similaires. Le client, qui souffre d'une allergie au médicament remis, est hospitalisé d'urgence.
> **A:** Oui
>

### civil_rule_application_vices_caches

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rule_application`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Appliquer les conditions du recours en vices cachés (art. 1726 CCQ) à un scénario factuel.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Marc achète un immeuble résidentiel en octobre. En mars suivant, il découvre que la fondation souffre de fissures causées par des infiltrations d'eau souterraines, un problème qui existait avant la vente et qui n'était pas décelable lors d'une inspection visuelle normale. Le vendeur n'en avait pas a?
> **A:** Oui
>
> **Q:** Sophie achète une voiture d'occasion auprès d'un concessionnaire professionnel. Trois mois après l'achat, le moteur tombe en panne en raison d'un défaut de fabrication interne qui n'était pas apparent à l'achat et que le concessionnaire ignorait. La réparation coûte 8 000 $.
> **A:** Oui
>

### civil_rule_conclusion_contrats

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rule_conclusion`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si les conditions de formation du contrat (art. 1385–1397 CCQ) sont réunies.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le 5 mars, une entreprise envoie un courriel proposant la vente de 500 chaises de bureau à 80 $ l'unité, offre valable jusqu'au 12 mars. Le 10 mars, l'acheteur répond par courriel en acceptant les termes sans modification. Les deux parties sont des personnes morales ayant la capacité de contracter.
> **A:** Oui
>
> **Q:** Un entrepreneur soumet une soumission écrite pour la rénovation d'une cuisine à 45 000 $, valide pour trente jours. Le propriétaire signe la soumission dans le délai imparti et la retourne par courriel. L'entrepreneur confirme la réception de l'acceptation. Tous deux sont majeurs et capables.
> **A:** Oui
>

### civil_rule_recall_ccq

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rule_recall`
- **Answer type:** `classification`
- **Answer detail:** Binary (True/False)
- **Metric:** `balanced_accuracy`
- **Purpose:** Vérifier si un énoncé portant sur le Code civil du Québec est vrai ou faux.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le contrat se forme par le seul échange de consentement entre des personnes capables de contracter, à moins que la loi n'exige une forme particulière.
> **A:** Vrai
>
> **Q:** La prescription extinctive de droit commun pour les droits personnels et les droits réels mobiliers est de trois ans, à défaut d'une disposition contraire.
> **A:** Vrai
>

### competence_territoriale_ccq

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rule_application_conclusion`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (district judiciaire — 6 valeurs + absence de compétence)
- **Metric:** `llm_judge`
- **Purpose:** Déterminer le district judiciaire québécois compétent pour un litige selon les règles de compétence territoriale du C.p.c. (art. 41-69)
- **Sample rows:** 8

**Sample Q&A:**

> **Q:** Un litige porte sur un contrat signé à Montréal entre deux entreprises québécoises pour la prestation de services informatiques devant être fournis à Montréal. Le défendeur a son siège à Montréal.
> **A:** District judiciaire de Montréal
>
> **Q:** Un accident de la route survenu à Québec implique deux résidents de la ville de Québec. Le demandeur y réside et y a subi son préjudice. Le défendeur y est domicilié.
> **A:** District judiciaire de Québec
>

### consumer_contracts_qa

- **Jurisdiction:** `quebec`
- **Reasoning type:** `interpretation`
- **Answer type:** `generation`
- **Answer detail:** Rights/obligations QA
- **Metric:** `llm_judge`
- **Purpose:** What rights or obligations does this consumer contract clause impose on the user?
- **Sample rows:** 9

**Sample Q&A:**

> **Q:** Clause de contrat : « Le commerçant se réserve le droit de modifier unilatéralement le prix de l'abonnement mensuel en avisant le consommateur par courriel trente (30) jours à l'avance. » — Question : Cette clause est-elle valide selon la Loi sur la protection du consommateur du Québec ?
> **A:** Non, cette clause est problématique. En vertu de l'art. 11.2 LPC, un contrat à exécution successive (comme un abonnement mensuel) ne peut être modifié unilatéralement que si le contrat le prévoit expressément et que le consommateur dispose d'un droit de résiliation sans frais. Un simple avis de 30 j?
>
> **Q:** Clause de contrat : « Le consommateur dispose de cinq (5) jours à compter de la signature du contrat pour résoudre le présent contrat de service conclu à distance. » — Question : Ce délai de résiliation est-il conforme à la LPC ?
> **A:** Non, ce délai est insuffisant. La Loi sur la protection du consommateur (art. 54.12 et suivants) prévoit un délai de résolution de dix (10) jours pour les contrats conclus à distance, à compter de la réception d'un exemplaire du contrat. Un délai contractuel de cinq jours est contraire à l'ordre pub?
>

### contract_clause_anti_assignment

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause contractuelle restreint ou interdit la cession du contrat à un tiers sans consentement préalable.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Licencié ne peut céder le présent accord, en tout ou en partie, ni transférer ses droits ou obligations qui en découlent à quelque tiers que ce soit, sans le consentement écrit préalable du Concédant, lequel peut être refusé à son entière discrétion. Toute tentative de cession en violation de la ?
> **A:** Oui
>
> **Q:** Les droits et obligations des parties aux termes du présent contrat ne peuvent être cédés ou transférés par l'une ou l'autre des parties sans l'accord écrit préalable de l'autre partie. Une fusion ou une acquisition d'une partie sera réputée constituer une cession aux fins de la présente clause.
> **A:** Oui
>

### contract_clause_audit_rights

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause accorde à une partie le droit d'auditer les livres comptables ou les locaux de l'autre partie.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Client se réserve le droit d'effectuer, à ses frais, un audit annuel des livres et registres du Fournisseur relatifs aux redevances payables en vertu du présent accord, sur préavis écrit de quinze (15) jours ouvrables. Le Fournisseur s'engage à coopérer pleinement et à fournir l'accès aux documen?
> **A:** Oui
>
> **Q:** Le Donneur de licence a le droit de faire vérifier par un auditeur indépendant, à ses frais, les rapports d'utilisation et les registres comptables du Licencié aux fins de confirmer l'exactitude des redevances déclarées, sur préavis de trente (30) jours. Si un écart supérieur à 5 % est constaté, le ?
> **A:** Oui
>

### contract_clause_cap_on_liability

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause plafonne la responsabilité d'une partie à un montant maximal déterminé.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** La responsabilité totale cumulée de chaque partie envers l'autre au titre du présent accord, que ce soit en vertu du droit contractuel, délictuel ou autre, ne saurait en aucun cas excéder le montant total des redevances effectivement payées par le Licencié au cours des douze (12) mois précédant l'év?
> **A:** Oui
>
> **Q:** En aucun cas la responsabilité du Prestataire ne dépassera le montant de cent mille dollars canadiens (100 000 $ CAD) par incident ou par année contractuelle, peu importe la nature de la réclamation, le fondement juridique invoqué ou le fait que le Prestataire ait été informé de la possibilité de te?
> **A:** Oui
>

### contract_clause_change_of_control

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit des droits ou obligations déclenchés par un changement de contrôle d'une des parties (fusion, acquisition).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Dans l'éventualité où une partie subirait un changement de contrôle, notamment par voie de fusion, d'acquisition, de vente de la majorité des actions avec droit de vote ou d'actifs, ou de toute autre restructuration ayant pour effet de transférer le contrôle effectif de cette partie, l'autre partie ?
> **A:** Oui
>
> **Q:** Si le Licencié fait l'objet d'une acquisition par un concurrent direct du Concédant ou si le contrôle du Licencié est transféré à une telle entité concurrente, le Concédant peut résilier le présent accord immédiatement sur avis écrit, sans indemnité.
> **A:** Oui
>

### contract_clause_competitive_restriction_exception

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit des exceptions aux restrictions de concurrence, autorisant certaines activités concurrentielles déterminées.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nonobstant la clause de non-concurrence prévue à l'article 8, le Partenaire conserve le droit d'exploiter ses activités existantes dans le secteur de la distribution alimentaire, lesquelles sont expressément exclues du champ d'application de la restriction concurrentielle.
> **A:** Oui
>
> **Q:** La restriction concurrentielle prévue à l'article 12 ne s'applique pas aux investissements passifs dans des sociétés cotées en bourse dont le Consultant détient moins de deux pour cent (2 %) des actions, ni aux activités d'enseignement et de conférence non rémunérées.
> **A:** Oui
>

### contract_clause_covenant_not_to_sue

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause contient un engagement de ne pas poursuivre une partie pour certaines réclamations.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** En contrepartie des considérations prévues aux présentes, chaque partie accorde à l'autre un engagement irrévocable de ne pas intenter de poursuites judiciaires, d'arbitrage ou d'autres procédures légales concernant toute réclamation existante ou future liée à la propriété intellectuelle visée par l?
> **A:** Oui
>
> **Q:** Le Concédant s'engage irrévocablement à ne pas intenter de poursuites contre le Licencié pour toute violation alléguée des droits de brevet listés à l'Annexe A, à condition que le Licencié respecte les conditions du présent accord et continue de payer les redevances dues.
> **A:** Oui
>

### contract_clause_effective_date

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause précise la date d'entrée en vigueur du contrat.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le présent accord entre en vigueur à compter du 1er mars 2024 (la « Date d'entrée en vigueur »), indépendamment de la date à laquelle il est signé par les parties. Toutes les obligations des parties prennent naissance à cette date.
> **A:** Oui
>
> **Q:** Le présent contrat devient effectif à la date à laquelle il est signé par la dernière des deux parties à le signer (ci-après la « Date effective »). Les parties conviennent qu'il peut être signé en contreparties séparées, chacune ayant force obligatoire.
> **A:** Oui
>

### contract_clause_exclusivity

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause impose une obligation d'exclusivité, empêchant une partie de travailler avec des concurrents.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Fournisseur accorde au Distributeur le droit exclusif de distribuer et de commercialiser les Produits sur le territoire de la province de Québec. Pendant la durée du présent accord, le Fournisseur s'engage à ne pas distribuer les Produits directement ni par l'entremise d'un autre distributeur dan?
> **A:** Oui
>
> **Q:** Le Concédant accorde au Licencié une licence exclusive pour utiliser, reproduire et distribuer le Logiciel dans le secteur de l'éducation postsecondaire au Canada. Cette exclusivité interdit au Concédant d'accorder à tout autre licencié des droits similaires dans ledit secteur.
> **A:** Oui
>

### contract_clause_expiration_date

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause fixe la date d'expiration ou le terme du contrat.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le présent accord expire automatiquement le 30 juin 2026 (la « Date d'expiration ») à moins qu'il ne soit renouvelé par accord écrit préalable des parties, ou résilié avant cette date conformément aux dispositions prévues aux présentes.
> **A:** Oui
>
> **Q:** La durée initiale du présent contrat est de vingt-quatre (24) mois à compter de la Date d'entrée en vigueur. À l'expiration de cette période, le contrat prendra fin sans qu'un préavis supplémentaire soit requis, sauf renouvellement explicite par les parties.
> **A:** Oui
>

### contract_clause_governing_law

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause précise la loi applicable au contrat et la juridiction compétente en cas de litige.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le présent accord est régi et interprété conformément aux lois de la province de Québec et aux lois fédérales du Canada applicables en Québec, à l'exclusion de ses règles de conflit de lois. Les parties conviennent de la compétence exclusive des tribunaux de Montréal.
> **A:** Oui
>
> **Q:** Ce contrat sera interprété exclusivement selon les lois de l'Ontario, sans égard à ses dispositions sur les conflits de lois. Tout différend sera soumis à la compétence des tribunaux de la province d'Ontario siégeant dans la ville de Toronto.
> **A:** Oui
>

### contract_clause_insurance

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause impose à l'une des parties l'obligation de maintenir une couverture d'assurance.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Prestataire doit, à ses frais, souscrire et maintenir en vigueur pendant toute la durée du présent accord les polices d'assurance suivantes : (i) responsabilité civile générale, avec une limite de deux millions de dollars (2 000 000 $) par sinistre; (ii) assurance fautes et omissions professionne?
> **A:** Oui
>
> **Q:** Le Fournisseur s'engage à maintenir une assurance responsabilité civile des entreprises d'un montant minimal de cinq millions de dollars (5 000 000 $) et à fournir au Client, sur demande, une copie du certificat d'assurance attestant de cette couverture. Le Client doit être désigné à titre d'assuré ?
> **A:** Oui
>

### contract_clause_ip_ownership_assignment

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit la cession de la propriété intellectuelle créée dans le cadre du contrat.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Par les présentes, le Prestataire cède et transfère irrévocablement au Client l'ensemble des droits de propriété intellectuelle sur les livrables développés dans le cadre du présent accord, y compris les droits d'auteur, les brevets, les secrets commerciaux et les marques de commerce, dès leur créat?
> **A:** Oui
>
> **Q:** Toutes les inventions, créations, œuvres, logiciels et autres éléments de propriété intellectuelle créés, développés ou mis au point par l'Employé dans le cadre de ses fonctions ou en utilisant les ressources de l'Employeur appartiendront exclusivement à l'Employeur, qui en acquiert tous les droits ?
> **A:** Oui
>

### contract_clause_irrevocable_or_perpetual_license

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause accorde une licence irrévocable ou perpétuelle sur une propriété intellectuelle.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Concédant accorde au Licencié une licence irrévocable et perpétuelle pour utiliser, modifier et distribuer le Logiciel open source conformément aux termes de la Licence Apache 2.0. Cette licence ne peut être révoquée même en cas de manquement du Licencié, sous réserve des recours en dommages.
> **A:** Oui
>
> **Q:** En contrepartie du paiement unique de la redevance forfaitaire prévue à l'Annexe B, le Titulaire accorde au Bénéficiaire une licence perpétuelle et irrévocable pour utiliser la Technologie aux fins définies dans le présent accord, sans que la résiliation du présent accord puisse affecter cette licen?
> **A:** Oui
>

### contract_clause_joint_ip_ownership

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit une copropriété de la propriété intellectuelle entre les parties.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Toute propriété intellectuelle créée conjointement par les deux parties dans le cadre du présent accord de recherche et développement sera détenue en copropriété selon une quote-part de cinquante pour cent (50 %) chacun, et chaque partie pourra exploiter librement cette PI conjointe sans obligation ?
> **A:** Oui
>
> **Q:** Les inventions, œuvres et créations développées conjointement dans le cadre du partenariat seront la propriété commune des deux parties à parts égales. Pour exercer ses droits sur la PI conjointe, chaque partie doit obtenir le consentement de l'autre pour toute sous-licence ou cession à des tiers.
> **A:** Oui
>

### contract_clause_license_grant

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause accorde une licence sur une propriété intellectuelle, un logiciel ou une marque de commerce.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Concédant accorde par les présentes au Licencié une licence non exclusive, non transférable et mondiale pour utiliser, reproduire et distribuer le Logiciel uniquement pour les besoins internes de l'entreprise du Licencié, pour la durée du présent accord.
> **A:** Oui
>
> **Q:** Sous réserve des conditions du présent accord, le Titulaire accorde au Bénéficiaire une licence limitée, révocable, non sous-licenciable et non transférable pour accéder à la plateforme et l'utiliser conformément à la documentation technique, uniquement pendant la durée de l'abonnement.
> **A:** Oui
>

### contract_clause_liquidated_damages

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit des dommages-intérêts liquidés ou une clause pénale en cas d'inexécution contractuelle.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** En cas de retard dans la livraison des livrables au-delà de la date convenue, le Prestataire paiera au Client une indemnité forfaitaire de deux mille dollars (2 000 $) par jour ouvrable de retard, jusqu'à concurrence de dix pour cent (10 %) du contrat total, ce montant étant convenu comme étant une ?
> **A:** Oui
>
> **Q:** Si le Distributeur ne respecte pas ses engagements minimaux d'achat annuel, une pénalité forfaitaire de vingt pour cent (20 %) de l'écart entre l'engagement et les achats réels sera exigible à titre de dommages-intérêts préétablis. Les parties reconnaissent que le préjudice réel serait difficile à q?
> **A:** Oui
>

### contract_clause_minimum_commitment

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause impose à une partie un engagement minimal d'achat, de volume ou de chiffre d'affaires.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Distributeur s'engage à acheter auprès du Fournisseur une quantité minimale de cinq cent mille (500 000) unités de Produits par année fiscale. Si le Distributeur n'atteint pas cet engagement minimal, le Fournisseur pourra convertir l'exclusivité en licence non exclusive pour la période suivante.
> **A:** Oui
>
> **Q:** En contrepartie de l'exclusivité territoriale accordée, l'Acheteur s'engage à passer des commandes pour un montant minimal de deux cent cinquante mille dollars (250 000 $) par trimestre pendant toute la durée de l'accord. Les commandes inférieures à ce seuil seront compensées par un paiement de la d?
> **A:** Oui
>

### contract_clause_most_favored_nation

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause garantit à une partie des conditions au moins aussi favorables que celles accordées à tout autre client ou partenaire.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Fournisseur garantit au Client qu'il ne vendra pas les Produits à des conditions plus favorables (prix, délais de paiement, remises) à d'autres acheteurs comparables sans offrir les mêmes conditions au Client dans les trente (30) jours suivant la signature de tout accord plus favorable.
> **A:** Oui
>
> **Q:** Dans l'éventualité où le Concédant accorderait à un tiers une licence à des conditions tarifaires plus avantageuses que celles prévues au présent accord, le Licencié bénéficiera automatiquement de ces mêmes conditions améliorées dès la prise d'effet de l'accord tiers.
> **A:** Oui
>

### contract_clause_no_solicit_of_customers

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause interdit à une partie de solliciter les clients de l'autre partie pendant ou après la durée du contrat.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Pendant la durée du présent accord et pour une période de vingt-quatre (24) mois suivant sa résiliation, le Distributeur s'interdit de solliciter directement ou indirectement, pour son propre compte ou pour le compte de tiers, les clients de la liste de comptes protégés fournie par le Fournisseur à ?
> **A:** Oui
>
> **Q:** Le Consultant s'engage à ne pas approcher, contacter ou solliciter les clients du Client existants à la date de fin du mandat, à des fins commerciales concurrentielles, pendant une période de douze (12) mois suivant la fin de la relation contractuelle.
> **A:** Oui
>

### contract_clause_no_solicit_of_employees

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause interdit à une partie de solliciter ou d'embaucher les employés de l'autre partie.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Pendant la durée du présent accord et pour une période de vingt-quatre (24) mois à compter de sa résiliation, chacune des parties s'interdit de recruter, d'embaucher ou de solliciter directement ou indirectement les employés de l'autre partie qui ont participé à l'exécution du présent accord.
> **A:** Oui
>
> **Q:** Le Client s'engage à ne pas approcher, recruter ou engager, directement ou indirectement, les ressources humaines du Prestataire qui lui ont été assignées dans le cadre du présent mandat, pendant la durée du contrat et pour une période de dix-huit (18) mois après son expiration.
> **A:** Oui
>

### contract_clause_non_compete

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause impose une obligation de non-concurrence à une partie après la fin du contrat (art. 2089 CCQ).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Pendant la durée du présent accord et pour une période de vingt-quatre (24) mois suivant sa résiliation pour quelque motif que ce soit, le Distributeur s'engage à ne pas distribuer, commercialiser ou promouvoir, directement ou indirectement, des produits ou services concurrençant directement les Pro?
> **A:** Oui
>
> **Q:** Le Consultant s'engage à n'exercer aucune activité professionnelle concurrente dans le secteur de la cybersécurité pour le compte de toute entreprise concurrençant directement le Client, que ce soit à titre d'employé, de consultant, d'associé ou d'actionnaire (au-delà de 5 %) pendant une période de ?
> **A:** Oui
>

### contract_clause_non_disparagement

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause interdit à une partie de tenir des propos négatifs ou dénigrants envers l'autre partie.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Les parties s'engagent mutuellement à s'abstenir de faire, publier ou relayer, directement ou indirectement, toute déclaration négative, critique, dépréciative ou autrement préjudiciable concernant l'autre partie, ses produits, services, dirigeants ou employés, sur quelque support que ce soit, inclu?
> **A:** Oui
>
> **Q:** Le Franchisé s'engage à ne pas ternir l'image ou la réputation du Franchiseur, de son réseau ou de ses partenaires par des déclarations publiques, des commentaires en ligne, ou des actions délibérément nuisibles pendant la durée du présent accord et pour une période de trente-six (36) mois suivant s?
> **A:** Oui
>

### contract_clause_non_transferable_license

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause stipule que la licence accordée est non cessible et ne peut être transférée à des tiers.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** La licence accordée aux termes du présent accord est strictement personnelle et non transférable. Le Licencié ne peut en aucun cas la céder, la sous-licencier, la nantir ou la transférer à quelque tiers que ce soit, directement ou indirectement, sans le consentement écrit préalable du Concédant.
> **A:** Oui
>
> **Q:** La présente licence d'utilisation est accordée au Licencié nominativement et pour son usage exclusif. Elle ne peut faire l'objet d'aucune cession, ni d'aucune sous-licence. Toute tentative de transfert rend la licence caduque de plein droit.
> **A:** Oui
>

### contract_clause_notice_period_to_terminate_renewal

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause précise le délai de préavis requis pour résilier le contrat ou empêcher son renouvellement automatique.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Chaque partie peut résilier le présent accord en donnant un préavis écrit de quatre-vingt-dix (90) jours à l'autre partie. En cas de non-renouvellement, ce même préavis de quatre-vingt-dix (90) jours doit être donné avant la date d'expiration du terme en cours.
> **A:** Oui
>
> **Q:** Pour s'opposer au renouvellement automatique du présent accord, l'une ou l'autre des parties doit transmettre un avis de non-renouvellement par écrit au moins cent vingt (120) jours avant la date anniversaire. À défaut d'un tel avis, l'accord sera reconduit pour une nouvelle période de douze (12) mo?
> **A:** Oui
>

### contract_clause_post_termination_services

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit des obligations de service ou de transition à la charge d'une partie après la résiliation du contrat.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** À la résiliation du présent accord pour quelque motif que ce soit, le Prestataire s'engage à fournir des services de transition pendant une période de six (6) mois, incluant le transfert de connaissances, la documentation des systèmes et l'assistance à la migration des données vers le système de rem?
> **A:** Oui
>
> **Q:** En cas de résiliation, qu'elle soit imputable à l'une ou l'autre des parties, le Fournisseur continuera à assurer les services de maintenance et de support essentiels pendant une période de transition de quatre-vingt-dix (90) jours aux tarifs contractuels en vigueur, afin d'éviter toute interruption?
> **A:** Oui
>

### contract_clause_price_restrictions

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause impose des restrictions sur les prix qu'une partie peut pratiquer (maintien des prix, prix plancher ou plafond).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Distributeur s'engage à ne pas vendre les Produits en dessous du prix de revente minimal (PRM) fixé par le Fournisseur à l'Annexe de tarification, lequel sera mis à jour trimestriellement. Toute vente en dessous du PRM constitue un manquement contractuel donnant lieu à une mise en demeure.
> **A:** Oui
>
> **Q:** Le Licencié s'interdit de consentir à ses clients finaux des remises dépassant vingt pour cent (20 %) sur le prix de liste officiel, sauf autorisation écrite préalable du Concédant. Cette restriction vise à protéger la valeur perçue de la marque sur le marché.
> **A:** Oui
>

### contract_clause_renewal_term

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit le renouvellement automatique ou optionnel du contrat à son expiration.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** À l'expiration de la période initiale de trois (3) ans, le présent accord se renouvellera automatiquement pour des périodes successives d'un (1) an, à moins que l'une ou l'autre des parties ne signifie à l'autre, par écrit, son intention de ne pas renouveler, au moins quatre-vingt-dix (90) jours ava?
> **A:** Oui
>
> **Q:** Le contrat est renouvelable tacitement d'année en année à moins que l'une des parties ne donne un préavis de résiliation d'au moins soixante (60) jours avant la date anniversaire. Chaque renouvellement est aux mêmes conditions, sauf ajustement tarifaire selon l'IPC annuel.
> **A:** Oui
>

### contract_clause_revenue_profit_sharing

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit un partage des revenus ou des bénéfices entre les parties.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** En contrepartie de la mise à disposition de la Plateforme, le Fournisseur recevra une redevance égale à vingt-cinq pour cent (25 %) des revenus nets générés par le Client à partir des transactions effectuées via la Plateforme, payable trimestriellement dans les quarante-cinq (45) jours suivant la cl?
> **A:** Oui
>
> **Q:** Les bénéfices nets issus des activités de la coentreprise seront partagés entre les parties dans les proportions suivantes : soixante pour cent (60 %) au Partenaire A et quarante pour cent (40 %) au Partenaire B, reflétant leurs apports respectifs en capital et en ressources humaines.
> **A:** Oui
>

### contract_clause_rofr_rofo_rofn

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause accorde un droit de premier refus, de première offre ou de première négociation sur une transaction.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Partenaire A dispose d'un droit de premier refus (ROFR) sur les actions du Partenaire B. Si le Partenaire B reçoit une offre d'achat d'un tiers, il doit en aviser le Partenaire A, qui dispose de trente (30) jours pour acquérir ces actions aux mêmes conditions.
> **A:** Oui
>
> **Q:** Avant de conclure tout accord de licence avec un tiers dans le secteur de la santé numérique, le Titulaire doit d'abord soumettre au Bénéficiaire une offre de première négociation (ROFN). Le Bénéficiaire dispose de vingt-un (21) jours pour entamer des négociations exclusives.
> **A:** Oui
>

### contract_clause_source_code_escrow

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit le dépôt du code source en séquestre au bénéfice d'une partie en cas de défaillance du concédant.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Concédant déposera le code source complet du Logiciel, incluant les fichiers de compilation, la documentation technique et les procédures d'installation, auprès du séquestre désigné (Iron Mountain Canada), dans les trente (30) jours suivant la date d'entrée en vigueur du présent accord.
> **A:** Oui
>
> **Q:** Afin de protéger les intérêts du Licencié en cas de cessation d'activité du Concédant, les parties conviennent de conclure un accord de séquestre de code source avec un tiers indépendant. Le code déposé sera mis à jour trimestriellement et sera libéré au Licencié si les conditions de libération défi?
> **A:** Oui
>

### contract_clause_termination_for_convenience

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause permet à l'une des parties de résilier le contrat sans motif, à sa seule discrétion.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Client peut résilier le présent accord à tout moment, pour quelque motif que ce soit ou sans motif, en donnant au Prestataire un préavis écrit de quatre-vingt-dix (90) jours. En cas de résiliation pour convenance, le Client paiera les services rendus jusqu'à la date effective de résiliation.
> **A:** Oui
>
> **Q:** Chacune des parties peut mettre fin au présent accord sans cause, sur préavis de soixante (60) jours donné à l'autre partie par écrit. La résiliation pour convenance ne donne pas lieu à des indemnités supplémentaires au-delà des montants dus pour les prestations déjà effectuées.
> **A:** Oui
>

### contract_clause_third_party_beneficiary

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause désigne un tiers bénéficiaire des droits ou obligations du contrat (stipulation pour autrui — CCQ art. 1444).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Les employés du Client sont expressément désignés comme tiers bénéficiaires des garanties de niveau de service stipulées à l'Annexe SLA du présent accord. Ces employés peuvent invoquer directement ces garanties si le Prestataire ne les respecte pas.
> **A:** Oui
>
> **Q:** Les clients finaux du Licencié sont reconnus comme tiers bénéficiaires des garanties de qualité et de conformité accordées par le Concédant aux termes du présent accord. Ces clients peuvent se prévaloir directement de ces garanties contre le Concédant dans la mesure permise par la loi.
> **A:** Oui
>

### contract_clause_uncapped_liability

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause prévoit une responsabilité illimitée, sans plafond maximal de dommages-intérêts.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nonobstant tout plafond de responsabilité prévu aux présentes, la responsabilité du Prestataire sera illimitée en cas de fraude, de faute intentionnelle, de négligence grave ou de violation des obligations de confidentialité. Dans ces cas, la partie lésée pourra réclamer la totalité de ses dommages ?
> **A:** Oui
>
> **Q:** Les limites de responsabilité prévues à l'article 12 ne s'appliquent pas aux réclamations découlant de la violation des droits de propriété intellectuelle du Client. Dans ce cas, la responsabilité du Prestataire est illimitée et la partie lésée peut réclamer l'intégralité de ses pertes.
> **A:** Oui
>

### contract_clause_unlimited_all_you_can_eat_license

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause accorde une licence illimitée sans restriction de volume, d'utilisateurs ou d'usage.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** En contrepartie du forfait annuel global prévu aux présentes, le Licencié bénéficie d'une licence d'utilisation illimitée du Logiciel, sans restriction quant au nombre d'utilisateurs, d'installations, de transactions ou de volumes de données traitées pendant la durée de l'accord.
> **A:** Oui
>
> **Q:** Le présent abonnement confère au Client un droit d'accès et d'utilisation illimité à l'ensemble des fonctionnalités de la Plateforme, pour un nombre d'utilisateurs illimité au sein de l'organisation du Client, sans frais supplémentaires liés à l'usage.
> **A:** Oui
>

### contract_clause_volume_restriction

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause impose des restrictions de volume sur la production, la vente ou la distribution.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** L'utilisation du présent abonnement est plafonnée à dix millions (10 000 000) de requêtes API par mois. Tout dépassement de ce seuil sera facturé au tarif excédentaire de zéro virgule cinq cent centimes (0,0005 $) par requête additionnelle, sans préavis.
> **A:** Oui
>
> **Q:** La présente licence d'utilisation est limitée à cinq cents (500) utilisateurs actifs par mois. L'ajout d'utilisateurs au-delà de ce plafond nécessite la mise à niveau vers un palier supérieur. Le nombre d'utilisateurs actifs sera mesuré mensuellement et rapporté automatiquement au Concédant.
> **A:** Oui
>

### contract_clause_warranty_duration

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une clause précise la durée d'une garantie contractuelle ou légale sur un bien ou service.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le Fabricant garantit que les équipements livrés seront exempts de défauts de matériaux et de fabrication pendant une période de vingt-quatre (24) mois à compter de la date de livraison au Client final. Les pièces réparées ou remplacées bénéficient d'une garantie résiduelle jusqu'à la fin de la péri?
> **A:** Oui
>
> **Q:** Le Prestataire garantit que les services de développement logiciel seront exempts de défauts de conception pendant quatre-vingt-dix (90) jours suivant l'acceptation finale. Passé ce délai, les défauts découverts seront traités dans le cadre du contrat de maintenance.
> **A:** Oui
>

### contract_nli_confidentiality_of_agreement

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause d'accord de confidentialité soutient, contredit ou ne traite pas l'hypothèse que l'accord lui-même est confidentiel.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Les parties s'engagent à maintenir confidentiels l'existence du présent accord, ses termes et conditions ainsi que toute information échangée dans ce cadre. » — Affirmation : Les parties ne peuvent pas révéler qu'elles ont conclu un accord de confidentialité.
> **A:** Vrai
>
> **Q:** Clause : « La conclusion du présent accord, son contenu et l'identité des parties sont considérés comme des informations confidentielles protégées par les présentes et ne peuvent être divulgués à des tiers sans consentement mutuel. » — Affirmation : L'accord lui-même doit rester secret entre les par?
> **A:** Vrai
>

### contract_nli_explicit_identification

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause d'accord de confidentialité soutient, contredit ou ne traite pas l'hypothèse que les informations confidentielles doivent être explicitement identifiées.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Aux fins du présent accord, les "informations confidentielles" désignent : (i) les données financières, projections et états financiers non publiés ; (ii) les listes de clients et informations sur les fournisseurs ; (iii) les spécifications techniques, codes source et algorithmes ; (iv) l?
> **A:** Vrai
>
> **Q:** Clause : « Seules les informations portant la mention écrite "CONFIDENTIEL" ou "PROPRIÉTAIRE" au moment de leur divulgation seront considérées comme des informations confidentielles aux termes du présent accord. Les informations divulguées oralement doivent être confirmées par écrit avec la mention ?
> **A:** Vrai
>

### contract_nli_inclusion_of_verbally_conveyed_information

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que les informations transmises verbalement sont couvertes par l'accord de confidentialité.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Les "informations confidentielles" comprennent toutes les informations divulguées par le Divulgateur, qu'elles soient communiquées par écrit, oralement, visuellement ou sous toute autre forme, et quel que soit le support utilisé. » — Affirmation : Les informations transmises lors de discu?
> **A:** Vrai
>
> **Q:** Clause : « Toute information divulguée de vive voix lors de réunions, présentations ou conversations téléphoniques entre les parties est réputée confidentielle, à condition que le Divulgateur en signale le caractère confidentiel au moment de la divulgation. » — Affirmation : Les informations communi?
> **A:** Vrai
>

### contract_nli_limited_use

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que l'usage des informations confidentielles est limité à un but précis.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le Bénéficiaire ne peut utiliser les informations confidentielles qu'aux seules fins de l'évaluation de la transaction envisagée entre les parties et à nulle autre fin. » — Affirmation : Le Bénéficiaire ne peut pas utiliser les informations pour améliorer ses propres produits.
> **A:** Vrai
>
> **Q:** Clause : « Les informations reçues ne peuvent être utilisées que pour les activités prévues à l'Annexe A et à nulle autre fin, commerciale ou non. » — Affirmation : L'utilisation des informations à des fins de marketing serait une violation de la clause.
> **A:** Vrai
>

### contract_nli_no_licensing

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse qu'aucune licence n'est accordée sur les informations confidentielles échangées.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le présent accord ne confère au Bénéficiaire aucun droit de licence, de propriété ou autre droit sur les informations confidentielles, les brevets, marques ou autres droits de propriété intellectuelle du Divulgateur. » — Affirmation : Le Bénéficiaire ne peut pas utiliser les brevets du Di?
> **A:** Vrai
>
> **Q:** Clause : « Aucune disposition du présent accord ne doit être interprétée comme octroyant au Bénéficiaire un droit de licence exprès ou implicite sur les informations confidentielles ou sur tout droit de propriété intellectuelle connexe. » — Affirmation : La divulgation d'informations confidentielles?
> **A:** Vrai
>

### contract_nli_notice_on_compelled_disclosure

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse qu'une partie doit aviser l'autre avant de divulguer des informations confidentielles en vertu d'une obligation légale.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Si le Bénéficiaire est contraint par une ordonnance judiciaire, une injonction réglementaire ou toute autre obligation légale de divulguer des informations confidentielles, il devra en informer le Divulgateur par écrit dans les meilleurs délais, et en tout état de cause avant toute divulg?
> **A:** Vrai
>
> **Q:** Clause : « En cas de divulgation requise par la loi ou ordonnée par un tribunal compétent, le Bénéficiaire s'engage à : (i) aviser promptement le Divulgateur dès la réception de la demande ; (ii) coopérer raisonnablement avec le Divulgateur dans ses démarches pour limiter la divulgation ; (iii) ne d?
> **A:** Vrai
>

### contract_nli_permissible_acquirement_of_similar_information

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que l'acquisition d'informations similaires de manière indépendante est permise.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Les obligations du présent accord ne s'appliquent pas aux informations que le Bénéficiaire développe ou acquiert de manière indépendante, sans recourir aux informations confidentielles du Divulgateur et sans violer les présentes obligations. » — Affirmation : Le Bénéficiaire peut légitime?
> **A:** Vrai
>
> **Q:** Clause : « Les restrictions du présent accord ne s'appliquent pas aux informations que le Bénéficiaire peut démontrer : (i) avoir développées de manière indépendante avant toute divulgation par le Divulgateur ; ou (ii) avoir obtenues légitimement auprès de tiers non tenus à des obligations de confid?
> **A:** Vrai
>

### contract_nli_permissible_copy

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que la reproduction des informations confidentielles est autorisée dans certaines circonstances.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le Bénéficiaire est autorisé à reproduire les informations confidentielles dans la stricte mesure nécessaire à l'évaluation de la transaction visée, à condition que chaque copie porte la mention "Confidentiel" et soit conservée dans un environnement sécurisé. » — Affirmation : Le Bénéfici?
> **A:** Vrai
>
> **Q:** Clause : « Le Bénéficiaire peut reproduire les informations confidentielles en nombre limité, uniquement aux fins décrites à l'article 2 du présent accord, et à condition que l'ensemble des copies soit soumis aux mêmes obligations de confidentialité que les originaux. » — Affirmation : La reproducti?
> **A:** Vrai
>

### contract_nli_permissible_development_of_similar_information

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que le développement indépendant d'informations similaires est permis.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le présent accord ne restreint pas la capacité du Bénéficiaire à développer, de manière indépendante et sans utiliser les informations confidentielles du Divulgateur, des produits, services ou technologies similaires à ceux du Divulgateur. » — Affirmation : Le Bénéficiaire peut développer?
> **A:** Vrai
>
> **Q:** Clause : « Les obligations du présent accord ne s'appliquent pas aux informations ou technologies développées de manière autonome par le Bénéficiaire sans recours aux informations confidentielles, même si ces développements aboutissent à des résultats similaires ou identiques à ceux du Divulgateur. ?
> **A:** Vrai
>

### contract_nli_permissible_post_agreement_possession

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que la détention des informations confidentielles après la fin de l'accord est permise.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le Bénéficiaire est autorisé à conserver les copies des informations confidentielles strictement nécessaires au respect de ses obligations légales ou réglementaires, à condition que ces copies demeurent soumises aux obligations de confidentialité du présent accord tant qu'elles sont en sa?
> **A:** Vrai
>
> **Q:** Clause : « Nonobstant l'obligation générale de restitution ou de destruction, le Bénéficiaire peut conserver dans les archives confidentielles de ses avocats externes les informations confidentielles dans la seule mesure requise pour documenter ses obligations juridiques passées, sans pouvoir les ut?
> **A:** Vrai
>

### contract_nli_return_of_confidential_information

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que les informations confidentielles doivent être retournées ou détruites à la fin de l'accord.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « À la demande du Divulgateur ou à la fin du présent accord, le Bénéficiaire devra promptement retourner ou détruire toutes les copies des informations confidentielles en sa possession, et confirmer cette destruction par écrit. » — Affirmation : Le Bénéficiaire doit certifier qu'il a détrui?
> **A:** Vrai
>
> **Q:** Clause : « À la résiliation du présent accord pour quelque motif que ce soit, le Bénéficiaire s'engage à restituer sans délai au Divulgateur l'ensemble des supports contenant les informations confidentielles ou à en certifier la destruction irrémédiable. » — Affirmation : Le Bénéficiaire ne peut pas?
> **A:** Vrai
>

### contract_nli_sharing_with_employees

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que les informations confidentielles peuvent être partagées avec les employés de la partie réceptrice.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le Bénéficiaire peut communiquer les informations confidentielles à ses employés, agents et consultants qui ont besoin d'en connaître pour les fins du présent accord, à condition que ces personnes soient liées par des obligations de confidentialité équivalentes. » — Affirmation : Les empl?
> **A:** Vrai
>
> **Q:** Clause : « La divulgation aux membres du personnel du Bénéficiaire est permise dans la stricte mesure nécessaire à l'évaluation de la transaction, sous réserve que chaque employé concerné soit informé du caractère confidentiel des informations et soit tenu aux mêmes obligations. » — Affirmation : Le?
> **A:** Vrai
>

### contract_nli_sharing_with_third_parties

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que les informations confidentielles peuvent être communiquées à des tiers.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Le Bénéficiaire peut communiquer les informations confidentielles à ses avocats, comptables et conseillers financiers externes, sous réserve que ces professionnels soient soumis à des obligations légales de confidentialité équivalentes ou aient signé des accords de confidentialité appropr?
> **A:** Vrai
>
> **Q:** Clause : « Le partage des informations confidentielles avec des tiers prestataires de services impliqués dans la réalisation du projet est autorisé, à condition que ces tiers soient liés par des obligations de confidentialité au moins aussi contraignantes que celles prévues aux présentes. » — Affirm?
> **A:** Vrai
>

### contract_nli_survival_of_obligations

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Vrai/Faux)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une clause soutient, contredit ou ne traite pas l'hypothèse que les obligations de confidentialité survivent à la résiliation de l'accord.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « Les obligations de confidentialité prévues par le présent accord survivront à sa résiliation ou expiration pour une période de cinq (5) ans. » — Affirmation : Même si le contrat prend fin, le Bénéficiaire reste tenu au secret pendant cinq ans.
> **A:** Vrai
>
> **Q:** Clause : « Nonobstant la résiliation ou l'expiration du présent accord, les parties demeurent liées par les obligations de confidentialité établies aux présentes pour une durée indéterminée ou jusqu'à ce que les informations entrent dans le domaine public. » — Affirmation : La fin du contrat ne met ?
> **A:** Vrai
>

### contract_qa

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `generation`
- **Answer detail:** Provision ID
- **Metric:** `llm_judge`
- **Purpose:** What type of contractual provision is present in this excerpt?
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « La partie défaillante devra payer à l'autre partie une pénalité de 15 000 $ pour chaque semaine de retard dans la livraison du logiciel, à titre de dommages-intérêts liquidés. » — Question : Cette clause pénale est-elle automatiquement exécutoire au Québec ?
> **A:** En droit québécois, une clause pénale est valide (art. 1622 CCQ) mais peut être réduite par le tribunal si elle est abusive et si le créancier n'a subi qu'un préjudice moindre (art. 1623 CCQ). Elle n'est donc pas automatiquement exécutoire à hauteur du montant stipulé : le tribunal peut la réduire a?
>
> **Q:** Clause : « Toute modification au présent contrat doit être constatée par écrit et signée par les représentants autorisés des deux parties. » — Question : Un échange de courriels entre les directeurs des deux entreprises suffit-il pour modifier le contrat ?
> **A:** Cela dépend. Un échange de courriels peut constituer un accord écrit si les courriels émanent des représentants autorisés (art. 1386 et 2839 CCQ) et que leur contenu manifeste clairement une volonté de modifier le contrat. Cependant, si la clause exige une signature formelle, un simple courriel non ?
>

### corporate_lobbying

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Lobbying / Pas de lobbying)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une entreprise est susceptible d'exercer des activités de lobbying au sens de la Loi sur la transparence et l'éthique en matière de lobbyisme (Québec) ou de la Loi sur le lobbying (Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le vice-président aux affaires gouvernementales d'une société pharmaceutique rencontre le sous-ministre de la Santé du Québec pour lui présenter des données scientifiques et demander l'inscription d'un nouveau médicament oncologique sur la liste des médicaments remboursés par la RAMQ. La rencontre e?
> **A:** Lobbying
>
> **Q:** Un consultant en relations gouvernementales, inscrit au registre des lobbyistes du Québec, envoie une série de courriels au cabinet du ministre de l'Environnement pour demander un assouplissement des normes d'émissions industrielles au profit de son client, une aluminerie.
> **A:** Lobbying
>

### corporate_successor_obligations

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_application_conclusion`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class
- **Metric:** `llm_judge`
- **Purpose:** Déterminer si une société acquéreuse ou issue d'une opération corporative reprend certaines obligations de l'entreprise cédée selon le droit québécois et canadien des sociétés.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Société Alpha inc. fusionne avec Société Bêta inc., laquelle devient la société absorbante. Au moment de la fusion, Bêta avait des créances impayées auprès de fournisseurs. Conformément à l'art. 295 de la Loi sur les sociétés par actions du Québec (LSAQ), la société résultante hérite de l'ensemble d?
> **A:** Reprise d'obligations
>
> **Q:** Une société acquiert tous les actifs et le fonds de commerce d'une autre entreprise, y compris ses listes de clients, ses contrats en cours et sa marque de commerce, dans le cadre d'une opération qualifiée comme transfert d'entreprise au sens de l'art. 1525 CCQ. Les anciens employés et les parties c?
> **A:** Reprise d'obligations
>

### cpc_drafting_evaluation

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rule_application`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (Conforme / Partiellement conforme / Non conforme)
- **Metric:** `llm_judge`
- **Purpose:** Evaluate if this legal document respects the required form under C.p.c.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** DEMANDE INTRODUCTIVE D'INSTANCE — Cour supérieure du Québec — District de Montréal — No : 500-17-000001-230 — La demanderesse, TECH SOLUTIONS INC., société par actions dûment constituée selon les lois du Québec, dont le siège social est au 1200, rue Sherbrooke Ouest, Montréal (Québec) H3A 1G2, deman?
> **A:** Conforme
>
> **Q:** REQUÊTE EN INJONCTION PROVISOIRE — Présentée devant la soussignée, juge de la Cour supérieure — Le demandeur allègue : [faits numérotés, droit, conclusion] — Appuyée sur les affidavits de [nom] ci-joints — Signée par l'avocat, avec coordonnées complètes, date et district judiciaire — Preuve d'urgenc?
> **A:** Conforme
>

### definition_classification

- **Jurisdiction:** `both`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Statutaire / Jurisprudentielle / Contractuelle / Doctrinale)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une phrase extraite d'un jugement ou d'un texte juridique contient une définition d'un terme de droit québécois ou canadien.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Terme : "tutelle" — Contexte : utilisé à l'art. 177 CCQ pour désigner la charge confiée à une personne d'assurer la protection d'un mineur ou d'un majeur inapte et d'administrer ses biens.
> **A:** Statutaire
>
> **Q:** Terme : "bonne foi" — Contexte : art. 1375 CCQ, qui dispose que les parties à un contrat doivent se conduire de bonne foi tant lors de sa conclusion que lors de son exécution.
> **A:** Statutaire
>

### function_of_decision_section

- **Jurisdiction:** `both`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification`
- **Answer detail:** Multi-class
- **Metric:** `balanced_accuracy`
- **Purpose:** What function does this excerpt perform? (statement of facts / rule / application / conclusion)
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le 15 mars 2021, la demanderesse a glissé sur le trottoir enneigé devant l'immeuble du défendeur et s'est fracturé le poignet droit. Elle a été transportée à l'Hôpital du Sacré-Cœur, où elle a subi une chirurgie le lendemain. Elle occupe un emploi de pianiste concertiste et n'a pu reprendre ses acti?
> **A:** Faits
>
> **Q:** La défenderesse est propriétaire d'un immeuble commercial situé au 1245, rue Sainte-Catherine Ouest à Montréal depuis 2018. Le demandeur est locataire commercial de ladite propriété aux termes d'un bail commercial signé le 1er janvier 2019 pour une durée de cinq ans.
> **A:** Faits
>

### hearsay_evidence

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_application`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (Pas de ouï-dire / Ouï-dire avec exception / Ouï-dire sans exception)
- **Metric:** `llm_judge`
- **Purpose:** Is this evidence hearsay under Canadian evidence law? Explain your reasoning.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un témoin dépose que son collègue lui a dit, la veille du sinistre : "J'ai vu le défendeur sortir de l'édifice en courant et l'édifice a pris feu quelques minutes après." Le collègue est décédé avant le procès. La poursuite invoque la nécessité d'utiliser cette déclaration et sa fiabilité inhérente ?
> **A:** Ouï-dire avec exception applicable
>
> **Q:** Une travailleuse sociale témoigne qu'un enfant lui a rapporté, lors d'une entrevue filmée suivant le protocole d'investigation, avoir été victime de violence physique de la part de son père. L'enfant n'est pas convoqué à témoigner en raison de son jeune âge et de l'impact psychologique d'un tel témo?
> **A:** Ouï-dire avec exception applicable
>

### insurance_policy_interpretation

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Couvert / Couverture partielle / Non couvert)
- **Metric:** `balanced_accuracy`
- **Purpose:** Is this insurance claim covered under the policy terms?
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Police : « La police couvre tous les dommages matériels causés à l'immeuble assuré par l'eau, y compris les refoulements d'égout et les infiltrations latérales. » Sinistre : Un refoulement d'égout municipal a causé 35 000 $ de dommages aux sous-sol de l'immeuble assuré.
> **A:** Couvert
>
> **Q:** Police : « La garantie responsabilité civile couvre les dommages corporels ou matériels causés à des tiers résultant des activités professionnelles de l'assuré dans le cadre de son commerce de détail. » Sinistre : Un client a trébuché sur un présentoir mal positionné et s'est blessé au genou. Il réc?
> **A:** Couvert
>

### international_citizenship_questions

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `rule_recall`
- **Answer type:** `classification`
- **Answer detail:** Extractive open-ended (réponse libre en français)
- **Metric:** `balanced_accuracy`
- **Purpose:** Yes/No questions on Canadian citizenship and immigration rules
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Question : Combien d'années de résidence permanente un adulte doit-il avoir au Canada pour être admissible à la citoyenneté canadienne ?
> **A:** En vertu de l'art. 5(1) de la Loi sur la citoyenneté (LRC 1985 c C-29, telle que modifiée), un adulte doit avoir résidé au Canada pendant au moins 1 095 jours (trois ans) au cours des cinq ans précédant sa demande de citoyenneté. Les jours passés au Canada avant l'obtention de la résidence permanent?
>
> **Q:** Question : Un enfant né à l'étranger d'un parent canadien peut-il automatiquement devenir citoyen canadien ?
> **A:** Selon l'art. 3(1)b) de la Loi sur la citoyenneté, un enfant né à l'étranger est citoyen canadien par filiation s'il est né après le 17 avril 1981 d'un parent qui était citoyen canadien au moment de la naissance. Toutefois, depuis 2009, la règle de « citoyenneté de deuxième génération » s'applique : ?
>

### issue_spotting_benefits

- **Jurisdiction:** `quebec`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question juridique relative aux prestations sociales ou à l'aide au revenu (Québec/Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Je suis sans emploi depuis 3 mois et j'ai fait une demande d'assurance-emploi au fédéral, mais ma demande a été refusée parce que l'agent dit que j'ai quitté mon emploi volontairement. Pourtant, j'ai dû partir parce que mon employeur refusait de m'accommoder pour un problème de santé. Est-ce que je ?
> **A:** Oui
>
> **Q:** Mon dossier d'aide sociale a été fermé sans préavis parce que le ministère prétend que je reçois des revenus non déclarés. Ce n'est pas vrai. Je suis locataire et je ne travaille pas. Qu'est-ce que je peux faire pour rétablir mes prestations ?
> **A:** Oui
>

### issue_spotting_business

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question juridique de droit des affaires ou des sociétés (LSAQ/LCSA/CCQ, Québec/Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon partenaire d'affaires et moi avons fondé une société par actions ensemble il y a trois ans. Il veut maintenant se retirer mais refuse de vendre ses actions à la valeur marchande et bloque toutes les décisions au conseil d'administration. Quels sont mes recours légaux pour sortir de cette impasse?
> **A:** Oui
>
> **Q:** J'ai signé un contrat de franchise avec une enseigne nationale. La franchiseur a modifié unilatéralement les conditions d'approvisionnement, ce qui a fait doubler mes coûts. Le contrat interdit les modifications unilatérales. Puis-je réclamer des dommages-intérêts ou résilier ?
> **A:** Oui
>

### issue_spotting_civil_liability

- **Jurisdiction:** `quebec`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de responsabilité civile extracontractuelle au Québec (CCQ art. 1457).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** J'ai glissé sur une plaque de glace devant un commerce en hiver et je me suis cassé la cheville. Le commerce n'avait pas salé ni déneigé le trottoir devant son établissement depuis plusieurs jours. Puis-je poursuivre le propriétaire du commerce ?
> **A:** Oui
>
> **Q:** Un chien de mon voisin m'a mordu gravement au bras lors d'une sortie dans la rue. Le propriétaire dit que c'était un accident et que le chien n'avait jamais mordu auparavant. Suis-je en droit de réclamer des dommages-intérêts ?
> **A:** Oui
>

### issue_spotting_consumer

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question juridique de droit de la consommation (LPC/CCQ, Québec/Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** J'ai acheté un cellulaire à 800 $ dans un magasin et il est tombé en panne après trois mois d'utilisation normale. Le vendeur refuse de le réparer ou de me rembourser, disant que la garantie du fabricant est expirée. Ai-je des droits en vertu de la garantie légale de qualité ?
> **A:** Oui
>
> **Q:** Un vendeur de voitures usagées m'a dit que l'auto n'avait jamais été accidentée. J'ai découvert après l'achat qu'elle avait été déclarée perte totale. Il m'a induit en erreur. La Loi sur la protection du consommateur protège-t-elle dans ce cas ?
> **A:** Oui
>

### issue_spotting_courts

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de procédure civile ou de compétence des tribunaux (C.p.c., Québec/Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Je veux poursuivre mon ancien employeur pour congédiement injustifié mais je ne sais pas si je dois aller à la Commission des normes du travail, au Tribunal des droits de la personne ou à la Cour du Québec. Le montant réclamé est de 25 000 $. Vers quel tribunal dois-je me tourner ?
> **A:** Oui
>
> **Q:** J'ai reçu un jugement de la Cour du Québec contre un débiteur il y a 8 mois mais il refuse de payer. Je veux faire saisir son compte bancaire. Comment procède-t-on à l'exécution forcée d'un jugement au Québec ?
> **A:** Oui
>

### issue_spotting_crime

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de droit pénal ou criminel (Code criminel / Code de procédure pénale).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** La police m'a arrêté hier soir et accusé de possession de cocaïne. On m'a trouvé avec 1,5 gramme sur moi. C'est ma première offense. J'ai été libéré sous conditions. Quelles sont les conséquences possibles et est-ce que je peux éviter un casier judiciaire ?
> **A:** Oui
>
> **Q:** J'ai reçu une mise en accusation pour fraude de moins de 5 000 $. On prétend que j'aurais utilisé la carte de crédit d'un collègue sans sa permission. Je nie les faits. Quels sont mes droits lors des procédures criminelles qui vont suivre ?
> **A:** Oui
>

### issue_spotting_divorce

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question relative au divorce, à la séparation ou à l'union civile (Loi sur le divorce / CCQ).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon mari et moi sommes mariés depuis 12 ans et nous voulons divorcer à l'amiable. Nous avons deux enfants et une maison. Comment se déroule un divorce non contesté au Québec et combien de temps cela prend-il ?
> **A:** Oui
>
> **Q:** Mon conjoint a quitté le domicile familial il y a un an sans explication. Je veux demander le divorce mais il est introuvable. Est-ce que je peux divorcer en son absence et comment le signifier si je ne connais pas son adresse ?
> **A:** Oui
>

### issue_spotting_domestic_violence

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question juridique relative à la violence conjugale ou familiale (Code criminel / CCQ).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon conjoint me frappe lors de conflits. Hier, il m'a blessé au visage. J'ai deux enfants. J'ai peur de rester à la maison. Qu'est-ce que je peux faire immédiatement pour être en sécurité, moi et mes enfants ?
> **A:** Oui
>
> **Q:** Mon ex-partenaire m'envoie des dizaines de messages menaçants par jour depuis notre séparation il y a trois mois. Il m'a dit qu'il allait « me faire regretter » si je le quittais. La police m'a dit qu'elle ne peut rien faire tant qu'il ne passe pas à l'acte. Ai-je des recours légaux dès maintenant ?
> **A:** Oui
>

### issue_spotting_education

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de droit de l'éducation (Loi sur l'instruction publique, Québec).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon fils de 10 ans a un TDAH diagnostiqué. L'école refuse de lui fournir un plan d'intervention personnalisé et un accompagnement adapté. Il échoue ses cours. Quels sont nos droits en matière d'accommodement scolaire au Québec ?
> **A:** Oui
>
> **Q:** La commission scolaire veut placer mon enfant de 8 ans dans une classe spécialisée pour troubles de comportement. Nous refusons ce placement et pensons qu'il peut réussir en classe régulière avec du soutien. Pouvons-nous contester cette décision ?
> **A:** Oui
>

### issue_spotting_employment

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de droit du travail ou de l'emploi (LNT / Code du travail / CCQ, Québec/Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon employeur m'a congédié après 9 ans de service en prétextant une réorganisation. Je n'ai reçu qu'un préavis de 2 semaines et aucune indemnité de départ. Mon dossier était excellent. Est-ce que ce congédiement est justifié et quels sont mes recours ?
> **A:** Oui
>
> **Q:** Je suis employée de bureau depuis 5 ans. Mon supérieur me fait des commentaires à connotation sexuelle et m'a proposé une promotion en échange de faveurs. J'ai refusé et il a modifié mes horaires en punition. Comment porter plainte pour harcèlement sexuel au travail ?
> **A:** Oui
>

### issue_spotting_estates

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de droit successoral ou testamentaire (CCQ — successions).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Ma mère est décédée il y a deux mois sans laisser de testament. Elle avait une maison (valeur 380 000 $), un compte bancaire et un REER. Mon père était décédé avant elle. Il y a trois enfants adultes. Comment se fait la dévolution légale de ses biens au Québec ?
> **A:** Oui
>
> **Q:** Mon père a signé un testament il y a 10 ans dans lequel il me déshérite complètement en faveur de ma sœur. Je pense qu'il n'était pas en pleine possession de ses facultés à ce moment-là. Puis-je contester la validité de ce testament ?
> **A:** Oui
>

### issue_spotting_family

- **Jurisdiction:** `quebec`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de droit de la famille (filiation, garde, aliments, autorité parentale — CCQ/Loi sur le divorce).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon ex-conjoint (nous n'étions pas mariés) et moi avons deux enfants de 5 et 8 ans. Il veut que les enfants déménagent avec lui à Vancouver. Je refuse de les laisser partir. Comment protéger mon droit de garde et m'opposer au déménagement ?
> **A:** Oui
>
> **Q:** Mon père est âgé et a des problèmes cognitifs. Il prend des décisions financières risquées sous l'influence de sa nouvelle petite amie. Puis-je demander l'ouverture d'un régime de protection (tutelle ou curatelle) pour le protéger ?
> **A:** Oui
>

### issue_spotting_health

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question de droit de la santé ou des services sociaux (Québec/Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon médecin a effectué une chirurgie sans m'informer adéquatement des risques. J'ai subi une complication grave qui m'a partiellement paralysé. Quels sont mes recours pour une faute médicale par manquement au devoir d'information ?
> **A:** Oui
>
> **Q:** Je suis hospitalisé et les médecins veulent me faire une transfusion sanguine que je refuse pour des raisons religieuses. L'hôpital veut obtenir une ordonnance judiciaire pour passer outre mon refus. Ai-je le droit de refuser ce traitement ?
> **A:** Oui
>

### issue_spotting_housing

- **Jurisdiction:** `quebec`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question juridique relative au bail résidentiel ou au logement (CCQ art. 1851-2000 / TAL).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Mon propriétaire veut me mettre dehors dans 15 jours parce qu'il dit vouloir reprendre le logement pour y habiter lui-même, mais il loue depuis 8 ans à un autre locataire dans l'immeuble voisin. Est-ce qu'il peut me forcer à partir si c'est une fausse reprise ?
> **A:** Oui
>
> **Q:** Je suis locataire d'un appartement où les coquerelles infestent toutes les pièces depuis 6 mois. Le propriétaire refuse de faire la dératisation. Le loyer est payé. Quels sont mes recours pour forcer les réparations ou obtenir une réduction de loyer ?
> **A:** Oui
>

### issue_spotting_immigration

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question d'immigration, de statut ou de protection des réfugiés (LIPR, Canada).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Je suis résident permanent au Canada depuis 4 ans. J'ai passé beaucoup de temps à l'étranger pour soigner ma mère malade. J'ai peur que mon statut de résident permanent soit compromis. Quels sont les critères de présence obligatoire et comment savoir si je les respecte ?
> **A:** Oui
>
> **Q:** J'ai déposé une demande d'asile au Canada il y a 6 mois parce que je fuis la persécution dans mon pays d'origine. Ma demande a été refusée et je dois quitter le pays dans 30 jours. Quels sont mes recours (appel, demande humanitaire, etc.) ?
> **A:** Oui
>

### issue_spotting_traffic

- **Jurisdiction:** `both`
- **Reasoning type:** `issue_spotting`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario factuel soulève une question relative à la sécurité routière ou à la circulation (Code de la sécurité routière, Québec).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** J'ai reçu un constat d'infraction pour excès de vitesse (120 km/h dans une zone de 90 km/h) sur une route nationale. L'amende est de 250 $ et je risque 4 points de démérite. Est-ce que ça vaut la peine de contester et sur quels motifs ?
> **A:** Oui
>
> **Q:** Mon permis de conduire a été suspendu automatiquement par la SAAQ parce que j'ai accumulé 15 points de démérite. Je dépends de ma voiture pour mon travail. Y a-t-il une façon de contester la suspension ou d'obtenir un permis restreint ?
> **A:** Oui
>

### legal_reasoning_causality

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Causalité directe / Causalité contributive / Absence de lien causal)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de jugement repose sur un raisonnement causal de type probabiliste ou épidémiologique pour établir le lien de causalité en responsabilité civile (CCQ art. 1607).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un conducteur ivre grille un feu rouge et percute un piéton qui traversait légalement. Le piéton décède des suites de ses blessures. Sans la faute du conducteur, le piéton n'aurait pas été frappé. Aucun autre facteur intermédiaire n'a contribué à l'accident.
> **A:** Causalité directe
>
> **Q:** Un chirurgien omet de vérifier l'allergie aux antibiotiques d'un patient avant l'opération et lui administre une pénicilline. Le patient fait une réaction anaphylactique et décède. Sans cette omission, le patient aurait survécu à l'intervention sans complication.
> **A:** Causalité directe
>

### overruling

- **Jurisdiction:** `both`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Renversé explicitement / Renversé implicitement / Non renversé)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une phrase extraite d'un jugement renverse explicitement ou implicitement un précédent judiciaire (Cour suprême du Canada / Cour d'appel du Québec).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Extrait de décision : « La Cour confirme que l'arrêt Procureur général du Canada c Mossip [1988] RJQ 1971 (CA) ne peut plus être considéré comme faisant autorité sur la question du droit à l'égalité devant la loi en matière d'emploi. La présente Cour renverse explicitement cet arrêt en ce qu'il rest?
> **A:** Renversé explicitement
>
> **Q:** Extrait de décision : « Par les présents motifs, la Cour déclare que le test à deux étapes formulé dans notre propre décision Société canadienne des droits d'auteur c Télévision Éducative [2007] QCCA 1424 n'est plus conforme à l'état du droit tel qu'établi par la Cour suprême. Ledit test est par les?
> **A:** Renversé explicitement
>

### privacy_browser_tracking_signals

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité aborde le signal Do Not Track ou les mécanismes d'opt-out du suivi en ligne.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Notre site Web reconnaît et respecte les signaux "Do Not Track" (Ne pas suivre) envoyés par les navigateurs qui prennent en charge cette fonctionnalité. Lorsque nous détectons un tel signal, nous cessons de collecter des données de navigation à des fins de suivi comportemental ou publicitaire pour l?
> **A:** Oui
>
> **Q:** Notre plateforme ne prend pas actuellement en charge les signaux "Ne pas me suivre" (Do Not Track) émis par les navigateurs. Si vous souhaitez limiter le suivi de votre navigation, nous vous invitons à utiliser les paramètres de votre navigateur pour bloquer les témoins de connexion tiers ou à vous ?
> **A:** Oui
>

### privacy_data_retention

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité traite de la durée de conservation des renseignements personnels (Loi 25 / LPRPDE).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous conservons vos renseignements personnels pendant la durée nécessaire à l'accomplissement des finalités pour lesquelles ils ont été collectés, soit généralement une période de cinq (5) ans à compter de la fin de votre relation avec nous. À l'expiration de ce délai, vos données sont supprimées de?
> **A:** Oui
>
> **Q:** Vos renseignements personnels sont conservés aussi longtemps que votre compte est actif ou que nécessaire pour vous fournir nos services. Une fois votre compte fermé, nous procédons à la suppression automatique de vos données personnelles dans un délai de quatre-vingt-dix (90) jours, sauf si leur co?
> **A:** Oui
>

### privacy_data_security

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité décrit les mesures de sécurité appliquées aux renseignements personnels.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous mettons en place des mesures de sécurité techniques et organisationnelles rigoureuses pour protéger vos renseignements personnels contre tout accès non autorisé, toute divulgation accidentelle, toute perte ou toute destruction. Ces mesures incluent le chiffrement AES-256 de toutes les données s?
> **A:** Oui
>
> **Q:** La sécurité de vos renseignements personnels est une priorité absolue. Nous avons recours à des protocoles de transmission sécurisée (TLS 1.3), des pare-feux, des systèmes de détection d'intrusion et des contrôles d'accès basés sur le principe du moindre privilège. En cas de violation de données sus?
> **A:** Oui
>

### privacy_first_party_collection_use

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité décrit la collecte et l'utilisation directe des renseignements personnels par l'organisation.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous collectons directement auprès de vous les renseignements personnels suivants : votre nom complet, votre adresse courriel, votre numéro de téléphone et votre adresse postale lors de votre inscription. Ces renseignements sont utilisés uniquement pour traiter vos commandes, vous informer du statut?
> **A:** Oui
>
> **Q:** Les renseignements que vous nous fournissez directement — comme lors de la création de votre compte, du remplissage d'un formulaire ou d'une prise de contact avec notre équipe — sont utilisés pour vous offrir nos services, personnaliser votre expérience et vous envoyer des communications pertinentes?
> **A:** Oui
>

### privacy_international_transfers_and_audiences

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité traite des transferts internationaux de données ou de pratiques visant des publics spécifiques (mineurs, pays ciblés).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Notre service est destiné aux utilisateurs résidant au Canada et n'est pas spécifiquement conçu pour les utilisateurs d'autres pays. Toutefois, si vous accédez à notre service depuis l'extérieur du Canada, sachez que vos renseignements personnels peuvent être transférés, stockés et traités dans un p?
> **A:** Oui
>
> **Q:** Nos serveurs sont situés au Canada. Cependant, certains de nos prestataires de services peuvent stocker ou traiter vos données dans d'autres pays, notamment aux États-Unis. Dans ce cas, vos données sont soumises aux lois de ces pays, lesquelles peuvent prévoir des droits et protections différents de?
> **A:** Oui
>

### privacy_policy_change

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité décrit les modalités de notification en cas de modification de la politique.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous nous réservons le droit de modifier la présente politique de confidentialité à tout moment. En cas de modification substantielle, nous vous en informerons par courriel à l'adresse enregistrée dans votre profil ou par un avis bien visible sur notre site Web, au moins trente (30) jours avant l'en?
> **A:** Oui
>
> **Q:** La présente politique de confidentialité peut être mise à jour périodiquement afin de refléter les changements apportés à nos pratiques de traitement des données ou les modifications législatives. La date de la dernière révision est indiquée en haut de ce document. Nous vous encourageons à consulter?
> **A:** Oui
>

### privacy_policy_entailment

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Impliquée / Contradictoire / Non impliquée)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si un extrait de politique de confidentialité implique, contredit ou ne traite pas une pratique de collecte ou de traitement des données (Loi 25 / LPRPDE).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Politique : « Nous partageons vos renseignements personnels avec nos filiales et sociétés affiliées qui fournissent des services en notre nom. Ces entités sont contractuellement tenues de protéger vos données. » — Déclaration : La politique autorise le partage de données avec des sociétés du même gr?
> **A:** Impliquée
>
> **Q:** Politique : « Nous conservons vos renseignements personnels pendant cinq (5) ans suivant la fin de votre relation avec nous, après quoi vos données sont supprimées ou anonymisées. » — Déclaration : Les données d'un utilisateur dont le compte est fermé depuis six ans ont été supprimées ou rendues ano?
> **A:** Impliquée
>

### privacy_policy_qa

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Extractive open-ended (réponse libre en français)
- **Metric:** `balanced_accuracy`
- **Purpose:** Répondre à une question en langage naturel sur le contenu d'une politique de confidentialité rédigée conformément à la Loi 25 (RLRQ c P-39.1) ou à la LPRPDE.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Politique : « Nous conservons vos renseignements personnels pendant cinq (5) ans suivant la fin de notre relation commerciale. À l'expiration de ce délai, vos données sont supprimées ou anonymisées de manière sécuritaire. » — Question : Combien de temps après la clôture de son compte un utilisateur ?
> **A:** Selon cette politique, les données de l'utilisateur seront conservées pendant cinq ans suivant la fin de la relation commerciale (c'est-à-dire la clôture du compte). Après ce délai, elles seront supprimées ou anonymisées.
>
> **Q:** Politique : « Nous partageons vos données avec les catégories de tiers suivantes : (a) prestataires de services d'hébergement infonuagique ; (b) agences d'analyse de données ; (c) partenaires publicitaires avec lesquels vous avez consenti au partage. » — Question : L'organisation partage-t-elle des ?
> **A:** Non. Selon la politique, le partage avec des partenaires publicitaires est conditionnel à votre consentement préalable. Seul le partage avec les prestataires d'hébergement et les agences d'analyse s'effectue sans exiger un consentement distinct, car ces prestataires agissent à titre de sous-traitant?
>

### privacy_third_party_sharing_collection

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité traite du partage ou de la collecte de renseignements personnels par des tiers.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous partageons vos renseignements personnels avec des tiers dans les situations suivantes : (i) avec nos prestataires de services qui nous aident à exploiter notre plateforme ; (ii) avec nos partenaires commerciaux si vous y avez consenti ; (iii) en cas d'obligation légale. Tous nos prestataires ti?
> **A:** Oui
>
> **Q:** Nous pouvons partager certaines de vos données avec des partenaires publicitaires afin de vous proposer des publicités ciblées correspondant à vos intérêts. Ces partenaires peuvent collecter des informations sur votre navigation en ligne au moyen de témoins de connexion. Vous pouvez vous opposer à c?
> **A:** Oui
>

### privacy_user_access_edit_and_deletion

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité traite des droits des utilisateurs d'accéder, de rectifier ou de supprimer leurs renseignements personnels.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Conformément à la Loi 25 (RLRQ, c. P-39.1), vous disposez du droit d'accéder aux renseignements personnels que nous détenons à votre sujet, d'en demander la rectification si ceux-ci sont inexacts, incomplets ou équivoques, et d'en demander la suppression dans les cas prévus par la loi. Pour exercer ?
> **A:** Oui
>
> **Q:** Vous pouvez, à tout moment, consulter et modifier les renseignements personnels que vous nous avez fournis en vous connectant à votre espace personnel. Vous pouvez également demander la fermeture définitive de votre compte et la suppression des renseignements vous concernant en nous contactant par c?
> **A:** Oui
>

### privacy_user_choice_control

- **Jurisdiction:** `both`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un extrait de politique de confidentialité traite des mécanismes de contrôle et des choix offerts aux utilisateurs sur l'utilisation de leurs données.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Vous disposez d'un droit d'opposition à l'utilisation de vos renseignements personnels à des fins commerciales. Vous pouvez également retirer à tout moment votre consentement à la réception de communications marketing en cliquant sur le lien de désabonnement figurant dans nos courriels ou en ajustan?
> **A:** Oui
>
> **Q:** Nous vous offrons plusieurs mécanismes pour contrôler l'utilisation de vos renseignements personnels : (i) un tableau de bord de gestion des préférences pour vos choix en matière de communications ; (ii) un outil de gestion des témoins de connexion ; (iii) un formulaire de demande de suppression de ?
> **A:** Oui
>

### private_right_of_action

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_application`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Déterminer si une personne dispose d'un droit d'action privé en vertu de la loi fédérale ou québécoise applicable.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un consommateur québécois achète un produit défectueux d'un commerçant en ligne canadien. La défectuosité cause des dommages à sa propriété. La Loi sur la protection du consommateur, RLRQ c P-40.1, art. 271-272, prévoit explicitement que le consommateur peut exercer directement un recours contre le ?
> **A:** Oui
>
> **Q:** Une personne physique se prétend victime de pratiques commerciales déloyales de la part d'une entreprise qui a coordonné des prix avec ses concurrents. L'art. 36 de la Loi sur la concurrence, LRC 1985 c C-34, prévoit un droit d'action privé au profit des personnes ayant subi un préjudice résultant d?
> **A:** Oui
>

### public_interpretation_charte

- **Jurisdiction:** `quebec`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si un scénario met en jeu un droit protégé par la Charte des droits et libertés de la personne du Québec.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un propriétaire d'immeuble refuse de louer un appartement à un couple en raison de leur origine ethnique. L'un des membres du couple est d'origine haïtienne. Le propriétaire leur dit explicitement qu'il ne loue pas aux "gens comme eux".
> **A:** Oui
>
> **Q:** Une entreprise congédie une employée enceinte trois jours après avoir appris sa grossesse. L'employeur invoque des "raisons économiques" mais n'a congédié aucun autre employé et a affiché un nouveau poste similaire une semaine plus tard.
> **A:** Oui
>

### public_rhetorical_jugement

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rhetorical`
- **Answer type:** `classification`
- **Answer detail:** Multi-class (Faits / Règle / Application / Conclusion / Obiter)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier la fonction rhétorique d'un extrait de jugement québécois (exposé des faits, règle, application, conclusion).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Le 3 novembre 2022, la demanderesse, une charpentière-menuisière, a été victime d'un accident du travail lors de l'installation de coffrages au chantier du défendeur. Elle a chuté d'un échafaudage à deux mètres de hauteur et a subi des fractures multiples au bras gauche et à l'épaule droite.
> **A:** Faits
>
> **Q:** L'entreprise défenderesse exploite une plateforme de commerce électronique depuis 2019 et vend des biens aux consommateurs québécois via internet. La demanderesse a passé une commande de 1 850 $ le 14 mars 2023 pour du matériel photographique qui n'a jamais été livré malgré des relances répétées.
> **A:** Faits
>

### rule_qa

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_recall`
- **Answer type:** `generation`
- **Answer detail:** Free text
- **Metric:** `llm_judge`
- **Purpose:** State the legal rule / list the elements / identify where this rule is codified
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Extrait législatif : Art. 1457 CCQ : « Toute personne a le devoir de respecter les règles de conduite qui, suivant les circonstances, les usages ou la loi, s'imposent à elle, de manière à ne pas causer de préjudice à autrui. Elle est, lorsqu'elle est douée de raison et qu'elle manque à ce devoir, re?
> **A:** Le demandeur doit prouver : (1) une faute du défendeur (manquement aux règles de conduite imposées par les circonstances, les usages ou la loi) ; (2) un préjudice subi (corporel, moral ou matériel) ; et (3) un lien de causalité entre la faute et le préjudice. Ces trois éléments sont cumulatifs et do?
>
> **Q:** Extrait législatif : Art. 82 LNT : « L'employeur qui met fin à un contrat à durée indéterminée doit donner à son salarié un avis d'une semaine si ce dernier lui a rendu moins d'un an de service ; deux semaines si ce dernier lui a rendu entre un an et cinq ans de service ; quatre semaines si ce derni?
> **A:** Un salarié ayant sept ans et demi de service se trouve dans la tranche "entre cinq ans et dix ans de service" ; il a donc droit à un préavis de quatre semaines en vertu de l'art. 82 LNT.
>

### supply_chain_disclosure_best_practice_accountability

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une divulgation au titre de la Loi S-211 aborde les mécanismes de reddition de comptes en matière de travail forcé.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Notre entreprise a intégré la gouvernance de la chaîne d'approvisionnement au niveau du conseil d'administration, où un comité d'audit et d'éthique supervise les risques liés au travail forcé. Chaque fournisseur de premier rang est tenu de signer notre Code de conduite des fournisseurs, lequel prévo?
> **A:** Oui
>
> **Q:** Nous avons désigné un directeur de la responsabilité de la chaîne d'approvisionnement relevant directement du chef de la direction. Ce poste est responsable de l'application de notre politique d'approvisionnement responsable, de la gestion des incidents de non-conformité et de la présentation de rap?
> **A:** Oui
>

### supply_chain_disclosure_best_practice_audits

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une divulgation au titre de la Loi S-211 aborde la réalisation d'audits des fournisseurs pour détecter le travail forcé.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous privilégions les audits non annoncés réalisés par des tierces parties indépendantes selon la méthodologie SMETA quatre piliers, qui couvre les droits du travail, la santé et la sécurité, l'environnement et les pratiques commerciales éthiques. Chaque fournisseur de premier rang est audité au min?
> **A:** Oui
>
> **Q:** Notre approche d'audit de la chaîne d'approvisionnement repose sur une évaluation préalable des risques fondée sur le secteur, la géographie et l'historique de conformité du fournisseur. Les fournisseurs présentant un profil de risque élevé font l'objet d'audits annuels non annoncés ; ceux à risque ?
> **A:** Oui
>

### supply_chain_disclosure_best_practice_certification

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une divulgation au titre de la Loi S-211 aborde la certification des fournisseurs quant au respect des normes sur le travail.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous recommandons l'adoption de certifications tierces reconnues — telles que SA8000, Fair Trade ou la certification de l'Initiative du commerce éthique (ICE) — comme pilier central de toute stratégie d'approvisionnement responsable. Ces certifications garantissent que les pratiques des fournisseurs?
> **A:** Oui
>
> **Q:** Notre approche préconise la certification par des organismes accrédités comme condition préalable à l'intégration de nouveaux fournisseurs dans les secteurs à risque élevé (textile, agriculture, électronique). Nous considérons que la certification constitue la meilleure pratique pour établir une bas?
> **A:** Oui
>

### supply_chain_disclosure_best_practice_training

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une divulgation au titre de la Loi S-211 aborde la formation offerte aux employés sur la lutte contre le travail forcé.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous considérons que la formation est un pilier fondamental de toute stratégie efficace de lutte contre le travail forcé. Notre programme de formation couvre l'identification des indicateurs de vulnérabilité, les procédures de signalement internes, et les obligations légales découlant de la Loi S-21?
> **A:** Oui
>
> **Q:** La meilleure pratique en matière de formation consiste à adapter le contenu selon le niveau de responsabilité : une sensibilisation générale pour tous les employés, et une formation approfondie spécialisée pour les acheteurs, les gestionnaires de fournisseurs et les équipes de conformité. Nous avons?
> **A:** Oui
>

### supply_chain_disclosure_best_practice_verification

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une divulgation au titre de la Loi S-211 aborde les mécanismes de vérification de la conformité des chaînes d'approvisionnement.
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Nous recommandons le recours à une vérification indépendante tierce comme meilleure pratique pour valider les informations publiées dans les rapports sur les chaînes d'approvisionnement. Cette vérification assure la crédibilité des déclarations auprès des parties prenantes et contribue à l'améliorat?
> **A:** Oui
>
> **Q:** La vérification par des pairs sectoriels est une pratique émergente que nous considérons comme prometteuse pour renforcer la transparence dans les chaînes d'approvisionnement. Dans le cadre d'un consortium industriel, nous participons à des évaluations croisées où des représentants de membres du con?
> **A:** Oui
>

### supply_chain_disclosure_disclosed_accountability

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une entreprise déclare avoir mis en place des mécanismes de reddition de comptes pour le travail forcé (Loi S-211).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Conformément à la Loi S-211, nous avons nommé M. Jean-François Tremblay, vice-président aux opérations, à titre de responsable de la lutte contre le travail forcé au sein de notre organisation. Ce poste est chargé de superviser l'application de notre Code de conduite des fournisseurs et de présenter?
> **A:** Oui
>
> **Q:** En 2023, notre conseil d'administration a adopté une politique formelle de lutte contre le travail forcé et le travail des enfants dans nos chaînes d'approvisionnement. Un comité de surveillance de la chaîne d'approvisionnement, composé de trois administrateurs indépendants, est chargé d'en assurer ?
> **A:** Oui
>

### supply_chain_disclosure_disclosed_audits

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une entreprise déclare avoir effectué des audits de ses fournisseurs pour détecter le travail forcé (Loi S-211).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Au cours de l'exercice 2023-2024, nous avons réalisé cent vingt-trois (123) audits de conformité sociale auprès de nos fournisseurs, dont quarante-quatre pour cent (44 %) étaient non annoncés. Ces audits ont été conduits par Bureau Veritas dans douze pays. Vingt-huit fournisseurs ont reçu des plans ?
> **A:** Oui
>
> **Q:** En 2023, nous avons audité la totalité de nos soixante-dix-huit (78) fournisseurs de premier rang, représentant quatre-vingt-six pour cent (86 %) de nos dépenses d'approvisionnement. Les audits ont été réalisés selon la méthodologie SMETA quatre piliers. Le taux de non-conformité majeure s'établit à?
> **A:** Oui
>

### supply_chain_disclosure_disclosed_certification

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une entreprise déclare avoir certifié ses fournisseurs quant au respect des normes sur le travail (Loi S-211).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Au 31 décembre 2023, soixante-dix-neuf (79) de nos cent vingt (120) fournisseurs stratégiques détenaient une certification SA8000, BSCI ou équivalente reconnue, soit un taux de certification de soixante-six pour cent (66 %), en hausse de quatorze points par rapport à l'exercice précédent. Nous vison?
> **A:** Oui
>
> **Q:** Nos fournisseurs de matières textiles situés en Asie du Sud-Est sont tenus de détenir une certification Oeko-Tex MADE IN GREEN ou équivalente. En 2023, cent pour cent (100 %) de nos volumes d'achat de tissus et fils provenaient de fournisseurs certifiés, ce qui représente une augmentation par rappor?
> **A:** Oui
>

### supply_chain_disclosure_disclosed_training

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une entreprise déclare avoir fourni une formation sur la lutte contre le travail forcé à ses employés (Loi S-211).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** En 2023, nous avons dispensé une formation obligatoire sur la Loi S-211 et la prévention du travail forcé à deux cent quarante-sept (247) employés dans nos fonctions d'approvisionnement, de conformité et de direction. Le taux de complétion s'établit à quatre-vingt-seize pour cent (96 %). La formatio?
> **A:** Oui
>
> **Q:** Notre programme de formation 2023 distinguait trois niveaux : une sensibilisation générale de deux heures pour l'ensemble du personnel (mille deux cents (1 200) employés formés) ; une formation intermédiaire de six heures pour les équipes d'approvisionnement (cent quatre-vingt-dix (190) employés for?
> **A:** Oui
>

### supply_chain_disclosure_disclosed_verification

- **Jurisdiction:** `federal_ca`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Binary (Oui/Non)
- **Metric:** `balanced_accuracy`
- **Purpose:** Identifier si une entreprise déclare avoir mis en place des mécanismes de vérification de la conformité de sa chaîne d'approvisionnement (Loi S-211).
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Les données présentées dans la présente déclaration ont fait l'objet d'une vérification indépendante par Deloitte s.e.n.c.r.l. selon la norme ISAE 3000 (niveau d'assurance limité). Le périmètre de vérification couvre les indicateurs relatifs au nombre de fournisseurs évalués, au nombre d'employés fo?
> **A:** Oui
>
> **Q:** En 2023, nous avons mandaté PricewaterhouseCoopers pour vérifier l'exactitude et l'exhaustivité de notre déclaration sur la chaîne d'approvisionnement conformément aux exigences de la Loi S-211. La vérification a été réalisée selon les normes d'assurance canadiennes CPA Canada et portait sur quatre-?
> **A:** Oui
>

### territorial_jurisdiction

- **Jurisdiction:** `quebec`
- **Reasoning type:** `rule_application_conclusion`
- **Answer type:** `classification_and_generation`
- **Answer detail:** Multi-class (Compétence établie / Compétence douteuse / Absence de compétence)
- **Metric:** `llm_judge`
- **Purpose:** Do Quebec authorities have personal jurisdiction over this defendant? Explain. (art. 3148 CCQ)
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Un e-commerçant ontarien vend activement des produits au Québec via un site en français, livre des biens à des acheteurs québécois, a un entrepôt à Laval et emploie deux représentants commerciaux résidant au Québec. Un client québécois le poursuit pour vice caché.
> **A:** Compétence établie
>
> **Q:** Une entreprise new-yorkaise a signé au Québec un contrat de services avec une PME québécoise, stipulant que le siège des activités contractuelles est à Montréal. Le litige porte sur l'inexécution de ce contrat dont toutes les prestations devaient être fournies au Québec.
> **A:** Compétence établie
>

### trademark_classification

- **Jurisdiction:** `both`
- **Reasoning type:** `rule_application`
- **Answer type:** `classification`
- **Answer detail:** 5 classes
- **Metric:** `balanced_accuracy`
- **Purpose:** Classify this trademark's distinctiveness under the Canadian Trademarks Act
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Marque : LAIT — Produits/services : lait de vache frais
> **A:** Générique
>
> **Q:** Marque : AVOCAT — Produits/services : services juridiques de représentation devant les tribunaux
> **A:** Générique
>

### unfair_tos

- **Jurisdiction:** `quebec`
- **Reasoning type:** `interpretation`
- **Answer type:** `classification`
- **Answer detail:** Multi-class
- **Metric:** `balanced_accuracy`
- **Purpose:** Classify this terms-of-service clause into an unfairness category
- **Sample rows:** 10

**Sample Q&A:**

> **Q:** Clause : « La présente entreprise se réserve le droit de modifier unilatéralement les présentes conditions d'utilisation à tout moment, sans préavis, et l'utilisation continue du service après toute modification constitue l'acceptation des nouvelles conditions, même si l'utilisateur n'en a pas été i?
> **A:** Abusive/illégale
>
> **Q:** Clause : « L'utilisateur renonce irrévocablement à tout recours judiciaire ou quasi judiciaire pour tout litige découlant de l'utilisation du service et accepte que tout différend soit résolu exclusivement par une médiation privée dans la juridiction du siège social de l'entreprise (Delaware, États-?
> **A:** Abusive/illégale
>

## Project Maintenance Notes

- Task names and metadata were cleaned so the active benchmark uses Canadian/Quebec terminology rather than imported dataset names.
- `sample.tsv` files are explanatory examples for review; `train.tsv` and `test.tsv` remain empty placeholders until validation.
- Structured sample generation remains provider-neutral via `scripts/generate_samples_structured.py` and `prompts/generation_system_prompt.md`.
