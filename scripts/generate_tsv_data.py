"""
Generate initial QC/CA TSV data for adapted LexiorBench v2 tasks.
Creates train.tsv (6 examples) and test.tsv (10 examples) per task.
All examples are in French and grounded in QC/Canadian law.

These are starter datasets — each task needs 50+ examples for full statistical validity.
Lawyers must validate before any task is considered final.
"""
import csv
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TASKS_DIR = ROOT / "tasks"


def write_tsv(path: Path, rows: list[tuple[int, str, str]]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["index", "text", "answer"])
        for i, (_, text, answer) in enumerate(rows):
            writer.writerow([i, text, answer])


# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_housing  (CCQ arts. 1851–2000, Tribunal administratif du logement)
# ─────────────────────────────────────────────────────────────────────────────

HOUSING_TRAIN = [
    (0, "Mon propriétaire refuse de réparer la fournaise depuis trois semaines. Il fait -15°C dehors et mon appartement n'est plus chauffé. Qu'est-ce que je peux faire?", "Oui"),
    (1, "Je viens de recevoir un avis de reprise de logement de mon propriétaire. Il dit qu'il veut reprendre l'appartement pour y loger son fils. J'ai 20 ans de location. Ai-je des droits?", "Oui"),
    (2, "Mon propriétaire veut augmenter mon loyer de 15% à la prochaine reconduction. La fixation de loyer par le TAL est-elle possible dans mon cas?", "Oui"),
    (3, "La colocation avec qui je partageais mon appartement est partie sans payer sa part du loyer des deux derniers mois. Le propriétaire me réclame l'intégralité. Est-ce légal?", "Oui"),
    (4, "Mon employeur m'a dit que je devais obligatoirement reprendre le travail en présentiel dès lundi, sans quoi je serai congédié. J'ai une condition médicale qui justifie le télétravail selon mon médecin.", "Non"),
    (5, "Ma mère est décédée il y a deux mois sans laisser de testament. Mon père veut tout garder pour lui mais j'ai l'impression que j'ai droit à une part. Comment savoir?", "Non"),
]

HOUSING_TEST = [
    (0, "Mon propriétaire a entré dans mon appartement sans me prévenir pendant que j'étais au travail. Il dit qu'il était là pour 'vérifier quelque chose'. C'est la troisième fois ce mois-ci.", "Oui"),
    (1, "Je veux sous-louer mon appartement pour trois mois pendant que je voyage. Mon bail contient une clause interdisant la sous-location. Est-ce que cette clause est valide au Québec?", "Oui"),
    (2, "Mon propriétaire m'a envoyé un avis d'éviction pour cause de travaux majeurs. Il me donne 3 mois pour partir. Est-ce qu'il doit me reloger ou m'indemniser?", "Oui"),
    (3, "Mon voisin de palier fume dans les parties communes et la fumée entre sous ma porte. Mes enfants ont de l'asthme. J'ai des recours contre qui — le voisin ou le propriétaire?", "Oui"),
    (4, "J'ai signé un bail avec une clause pénale de deux mois de loyer si je résilie avant la fin du terme. Cette clause est-elle exécutoire en droit québécois?", "Oui"),
    (5, "Le propriétaire me demande un dépôt de sécurité de 500$ avant la remise des clés. Est-ce permis au Québec?", "Oui"),
    (6, "Mon comptable m'a fait une erreur dans ma déclaration de revenus. Je dois maintenant 3 000$ supplémentaires à Revenu Québec. Est-ce sa responsabilité?", "Non"),
    (7, "Mon ex-conjoint veut que nos enfants passent Noël chez lui cette année. Notre entente de garde prévoit qu'on alterne, mais il dit que c'était à moi l'année passée alors que c'est faux.", "Non"),
    (8, "J'ai acheté un téléphone qui a cessé de fonctionner après 15 jours. Le vendeur refuse le remboursement et m'offre seulement une réparation. Quels sont mes droits?", "Non"),
    (9, "Mon employeur m'a mis à pied temporairement depuis six semaines. Il ne répond plus à mes messages. À partir de quand peut-on parler de congédiement déguisé?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_employment  (LNT, Code canadien du travail)
# ─────────────────────────────────────────────────────────────────────────────

EMPLOYMENT_TRAIN = [
    (0, "Mon employeur me demande de travailler 55 heures par semaine depuis deux mois. Il refuse de payer les heures supplémentaires, disant que je suis 'cadre'. Je supervise deux personnes. Est-ce légal?", "Oui"),
    (1, "J'ai été congédié sans avis ni indemnité après 8 ans de service. Mon employeur dit que c'est une 'fin d'emploi pour cause'. Je n'ai reçu aucun avertissement écrit auparavant.", "Oui"),
    (2, "Mon patron me harcèle psychologiquement depuis plusieurs mois — commentaires dégradants devant les collègues, tâches humiliantes, exclusion des réunions. Que puis-je faire?", "Oui"),
    (3, "J'ai pris un congé de maternité et à mon retour on m'a offert un poste différent, moins bien rémunéré. Mon ancien poste a été donné à quelqu'un d'autre.", "Oui"),
    (4, "Mon propriétaire refuse de me restituer mon dépôt de garantie d'un mois après mon départ. Il prétend que j'ai causé des dommages au logement alors que l'état des lieux était propre.", "Non"),
    (5, "Ma belle-mère a rédigé un testament laissant tout à mon conjoint, mais elle voulait qu'une partie revienne à ses petits-enfants. Peut-on contester le testament?", "Non"),
]

EMPLOYMENT_TEST = [
    (0, "Mon contrat de travail prévoit une clause de non-concurrence de deux ans dans toute la province de Québec. Je veux partir chez un concurrent. Cette clause est-elle valide?", "Oui"),
    (1, "Mon employeur ne m'a pas payé depuis trois semaines. Il dit qu'il a des problèmes de trésorerie. Que puis-je faire pour récupérer mon salaire?", "Oui"),
    (2, "Je travaille pour une agence de placement. L'entreprise cliente m'a demandé de partir sans explication. L'agence dit qu'elle n'a pas d'autre contrat pour moi pour le moment. Suis-je mis à pied?", "Oui"),
    (3, "Mon employeur m'oblige à signer une renonciation à mes droits aux heures supplémentaires comme condition de mon embauche. Cette clause est-elle légale sous la LNT?", "Oui"),
    (4, "J'ai subi un accident de travail et je suis en arrêt depuis 4 mois. Mon employeur veut me remplacer de façon permanente. A-t-il le droit?", "Oui"),
    (5, "Mon voisin a construit une clôture qui empiète de 30 cm sur mon terrain. J'ai un certificat de localisation qui le prouve. Comment forcer la correction?", "Non"),
    (6, "J'ai reçu une mise en demeure d'un créancier pour une dette que j'avais oubliée. La dette date de 4 ans et demi. Est-elle encore exigible?", "Non"),
    (7, "Mon médecin m'a prescrit un médicament qui m'a causé des effets secondaires graves non mentionnés dans la notice. Ai-je un recours contre le fabricant?", "Non"),
    (8, "La société dont je suis actionnaire minoritaire prend des décisions qui me lèsent. Les dirigeants refusent de me convoquer aux assemblées. Que faire?", "Non"),
    (9, "J'ai fait une demande de permis de rénovation il y a 8 mois et la ville ne répond pas. Mon entrepreneur ne peut pas commencer les travaux.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_family  (CCQ, Loi sur le divorce)
# ─────────────────────────────────────────────────────────────────────────────

FAMILY_TRAIN = [
    (0, "Mon ex-conjoint veut déménager à Vancouver avec nos deux enfants sans mon consentement. Notre entente de garde est partagée à 50/50. Peut-il faire ça?", "Oui"),
    (1, "Je suis en instance de divorce et mon conjoint cache des revenus pour réduire la pension alimentaire. Comment puis-je prouver ses véritables revenus?", "Oui"),
    (2, "Mon ex-conjoint de fait (union civile) refuse de me payer la pension alimentaire ordonnée par le tribunal depuis 6 mois. Que faire pour faire exécuter l'ordonnance?", "Oui"),
    (3, "Mon enfant de 16 ans veut vivre chez son autre parent. L'ordonnance de garde actuelle ne le permet pas. Les tribunaux peuvent-ils tenir compte de son souhait?", "Oui"),
    (4, "Mon employeur a modifié mon horaire de travail de nuit sans préavis. Je dois maintenant travailler de 23h à 7h du matin, ce qui est incompatible avec ma vie familiale.", "Non"),
    (5, "Ma voiture a été gravement endommagée lors d'un accident causé par un conducteur sans assurance. Comment être indemnisé au Québec?", "Non"),
]

FAMILY_TEST = [
    (0, "Je veux adopter l'enfant de mon conjoint (belle-fille de 7 ans). Le père biologique a disparu depuis 5 ans et ne verse plus de pension. Quelle est la procédure d'adoption?", "Oui"),
    (1, "Mon conjoint et moi n'étions pas mariés et vivions ensemble depuis 10 ans. On se sépare. Est-ce que j'ai droit à une compensation pour les biens acquis ensemble?", "Oui"),
    (2, "Mon ex-mari ne respecte pas le droit de visite — il refuse systématiquement de me remettre les enfants à la fin de ses périodes de garde.", "Oui"),
    (3, "Lors de notre séparation, mon conjoint a contracté des dettes à mon insu en mon nom. Suis-je responsable de ces dettes?", "Oui"),
    (4, "Mes parents veulent modifier leur testament pour exclure mon frère. Quelles sont les règles concernant la réserve héréditaire au Québec?", "Non"),
    (5, "Mon propriétaire a refusé de renouveler mon bail parce qu'il veut reprendre l'appartement. Je suis locataire depuis 15 ans.", "Non"),
    (6, "Un livreur a glissé sur le trottoir glacé devant mon commerce et me poursuit pour 50 000$. J'avais salé le trottoir ce matin.", "Non"),
    (7, "Mon patron m'a congédié le lendemain de mon retour de congé de maladie. Il dit que c'est pour 'restructuration'.", "Non"),
    (8, "J'ai commandé une cuisine sur mesure, j'ai versé 40% d'acompte et l'entreprise a fermé sans livrer. Comment récupérer mon argent?", "Non"),
    (9, "Mon cousin m'a signé un billet promissoire il y a 4 ans pour un prêt de 15 000$. Il refuse maintenant de payer. Le billet est-il encore valide?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_immigration  (LIPR, Règlement sur l'immigration)
# ─────────────────────────────────────────────────────────────────────────────

IMMIGRATION_TRAIN = [
    (0, "Mon visa étudiant expire dans 4 semaines et ma demande de renouvellement est toujours en traitement. Est-ce que je peux continuer mes études pendant ce temps?", "Oui"),
    (1, "J'ai reçu une décision négative de la Section de protection des réfugiés. On me demande de quitter le Canada dans 30 jours. Quels sont mes recours?", "Oui"),
    (2, "Mon permis de travail est lié à un employeur spécifique qui m'a congédié. Ai-je le droit de travailler pour un autre employeur pendant que je change mon permis?", "Oui"),
    (3, "Je suis résidente permanente depuis 4 ans. Mon conjoint canadien et moi nous séparons. Est-ce que mon statut de résidence est en danger?", "Oui"),
    (4, "Mon locataire a six semaines de retard dans le paiement du loyer. J'ai déjà envoyé un avis. Quand puis-je déposer une demande de résiliation de bail au TAL?", "Non"),
    (5, "J'ai été victime d'une fraude par virement bancaire pour 8 000$. La banque refuse de me rembourser. Ai-je des recours?", "Non"),
]

IMMIGRATION_TEST = [
    (0, "Je suis titulaire d'un permis de travail fermé. Mon employeur veut que je travaille dans une ville différente de celle indiquée sur mon permis. Est-ce autorisé?", "Oui"),
    (1, "J'ai une demande de résidence permanente en attente depuis 3 ans. IRCC n'a pas traité mon dossier dans les délais normaux. Que puis-je faire?", "Oui"),
    (2, "Mon père, résident permanent, veut faire venir ma mère du Maroc pour la rejoindre au Canada. Quelle est la procédure de parrainage?", "Oui"),
    (3, "J'ai été arrêté pour conduite avec facultés affaiblies. Je suis résident permanent depuis 2 ans. Cela peut-il affecter mon statut ou mes chances d'obtenir la citoyenneté?", "Oui"),
    (4, "J'ai réussi tous mes examens mais l'université refuse de me remettre mon diplôme parce que j'ai une balance administrative impayée. Est-ce légal?", "Non"),
    (5, "Mon employeur refuse de me verser mes commissions depuis deux mois. J'ai des courriels prouvant les montants convenus.", "Non"),
    (6, "Je veux contester une contravention de stationnement. La ville refuse de l'annuler malgré une photo prouvant que le panneau était obscurci.", "Non"),
    (7, "Mon copropriétaire refuse de faire les réparations urgentes sur les parties communes de notre immeuble. Je dois payer ma quote-part pour les travaux.", "Non"),
    (8, "J'ai acheté une voiture d'occasion chez un concessionnaire. Elle avait un vice caché que le vendeur connaissait. Je veux la retourner.", "Non"),
    (9, "Ma compagnie d'assurance refuse de me rembourser des dommages causés par un dégât des eaux, invoquant une exclusion que je n'avais pas vue dans le contrat.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_consumer  (LPC québécoise)
# ─────────────────────────────────────────────────────────────────────────────

CONSUMER_TRAIN = [
    (0, "J'ai acheté un lave-vaisselle neuf il y a 8 mois. Il est déjà brisé. Le vendeur refuse la garantie légale et dit que j'aurais dû prendre l'assurance étendue. Ai-je des recours?", "Oui"),
    (1, "Un gym m'a fait signer un contrat de 24 mois sans me l'expliquer. Je veux annuler après 3 semaines. Peuvent-ils me retenir plus de 50$?", "Oui"),
    (2, "J'ai commandé un canapé sur Internet livrable en 6 semaines. Il n'est toujours pas arrivé après 4 mois et le marchand ne répond plus. Que faire?", "Oui"),
    (3, "Une entreprise de rénovation m'a présenté un contrat d'urgence pour réparer une fuite. Elle a fait des travaux non demandés et exige maintenant le double du devis. Est-ce légal?", "Oui"),
    (4, "Mon ex-employeur a tenté de me forcer à signer un quittance complète en échange de mon certificat de travail. J'ai refusé. Peut-il légalement retenir mon certificat?", "Non"),
    (5, "Mon propriétaire a installé des caméras à l'intérieur du couloir commun de l'immeuble. Est-ce qu'il doit m'en informer?", "Non"),
]

CONSUMER_TEST = [
    (0, "J'ai payé 5 000$ pour un cours de formation professionnelle en ligne qui ne correspond pas à ce qui était annoncé. La formation est de mauvaise qualité. Puis-je annuler et être remboursé?", "Oui"),
    (1, "Une compagnie de télécoms a modifié unilatéralement mon forfait en augmentant le prix de 8$ par mois sans me laisser possibilité de résiliation sans pénalité. Est-ce permis?", "Oui"),
    (2, "Je me suis fait vendre un contrat de service de déneigement lors d'un démarchage à domicile. Je veux me rétracter dans les 10 jours. Comment procéder?", "Oui"),
    (3, "Un garagiste a réparé ma voiture pour 1 200$ sans mon autorisation. Je lui avais demandé un devis et il a tout de suite commencé les réparations. Dois-je payer?", "Oui"),
    (4, "Mon bailleur commercial veut augmenter mon loyer de 40% lors du renouvellement du bail. Le bail commercial n'est pas régi par le TAL, mais quels sont mes recours?", "Non"),
    (5, "Un cycliste a brisé la vitre de ma voiture en tombant dessus. Il nie toute responsabilité. Comment établir sa faute?", "Non"),
    (6, "Ma voisine a planté une haie qui coupe la lumière naturelle de ma fenêtre principale. Y a-t-il un recours légal pour les servitudes de vue ou d'ensoleillement?", "Non"),
    (7, "J'ai reçu une convocation pour un jury. Je travaille à contrat et je ne suis pas payé pendant mon absence. Mon client peut-il annuler mon contrat pour ça?", "Non"),
    (8, "Le bureau des coroners a classé le décès de mon père comme accidentel. Je pense qu'il y a eu négligence médicale. Comment demander une révision?", "Non"),
    (9, "Mon fils mineur de 16 ans a signé un contrat d'abonnement à un service de jeux vidéo. Puis-je faire annuler ce contrat?", "Oui"),
]

# ─────────────────────────────────────────────────────────────────────────────
# overruling  (CSC / Cour d'appel / tribunaux fédéraux)
# ─────────────────────────────────────────────────────────────────────────────

OVERRULING_TRAIN = [
    (0, "Dans la mesure où notre décision dans Doré c. Barreau du Québec [2012] 1 RCS 395 entre en conflit avec le présent arrêt, Doré est infirmé.", "Oui"),
    (1, "Le présent arrêt écarte l'approche retenue dans R c. Askov [1990] 2 RCS 1199 concernant les délais déraisonnables et lui substitue le cadre d'analyse établi dans Jordan.", "Oui"),
    (2, "La Cour est d'avis que l'analyse formulée dans Anns c. Merton London Borough Council [1978] AC 728, telle qu'adoptée en droit canadien dans Cooper c. Hobart [2001] 3 RCS 537, doit être abandonnée.", "Oui"),
    (3, "Pour toutes ces raisons, l'appel est accueilli et la décision de la Cour d'appel est infirmée. Le jugement de première instance est rétabli.", "Non"),
    (4, "La Cour confirme l'analyse du juge de première instance et conclut que la défenderesse a manqué à son obligation de bonne foi dans l'exécution du contrat.", "Non"),
    (5, "Nous n'avons pas à trancher dans le présent pourvoi si l'arrêt Kirkness c. John Hudson and Co. [1955] AC 696 s'applique en droit canadien, cette question pouvant être laissée à une occasion future.", "Non"),
]

OVERRULING_TEST = [
    (0, "Dans la mesure où notre décision dans Peart c. Procureur général du Canada entre en conflit avec la position adoptée ici, elle doit être considérée comme modifiée.", "Oui"),
    (1, "Le présent arrêt abandonne le cadre d'analyse Oakes traditionnel pour ce type de restriction aux droits fondamentaux, au profit d'une approche contextuelle plus souple.", "Oui"),
    (2, "L'arrêt KVP Co. c. Syndicat des travailleurs du papier, dans la mesure où il suggère que les politiques de l'employeur priment automatiquement sur les dispositions d'une convention collective, est expressément écarté.", "Oui"),
    (3, "La Cour d'appel du Québec a eu tort de substituer son appréciation de la preuve à celle du juge de première instance, qui avait l'avantage d'avoir vu et entendu les témoins.", "Non"),
    (4, "Pour les motifs exposés par le juge Lebel, au nom de la Cour, l'appel est rejeté avec dépens.", "Non"),
    (5, "Même si nous reconnaissons certaines difficultés dans le raisonnement de l'arrêt Syndicat Northcrest c. Amselem [2004] 2 RCS 551, il n'est pas nécessaire de le réexaminer ici.", "Non"),
    (6, "La présente décision doit être lue comme mettant fin à l'approche adoptée dans Seneca College of Applied Arts and Technology c. Bhadauria [1981] 2 RCS 181, dans laquelle la Cour avait refusé de reconnaître un délit civil d'atteinte aux droits de la personne.", "Oui"),
    (7, "Le jugement de la Cour d'appel est infirmé et la décision du Tribunal des droits de la personne est rétablie pour les motifs suivants.", "Non"),
    (8, "En adoptant ce cadre d'analyse, la Cour s'écarte résolument de la démarche fondée sur la distinction entre droits réels et droits personnels, telle qu'exposée dans les arrêts antérieurs sur les sûretés.", "Oui"),
    (9, "La Cour souscrit à la conclusion du juge Sopinka dans Snell c. Farrell [1990] 2 RCS 311 selon laquelle la preuve de causalité ne requiert pas une certitude absolue.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# definition_classification  (CSC / CA-QC sentences defining legal terms)
# ─────────────────────────────────────────────────────────────────────────────

DEFINITION_TRAIN = [
    (0, "Le terme 'résidence principale' au sens de l'art. 395 CCQ désigne le lieu où une personne a son principal établissement, déterminé par l'intention de la partie et les circonstances de fait.", "Oui"),
    (1, "Par 'préjudice moral', la Cour entend toute atteinte à l'intégrité psychologique de la victime, y compris la douleur physique, la peine morale et les inconvénients de la vie quotidienne.", "Oui"),
    (2, "La notion de 'faute grave' au sens de l'article 1474 CCQ équivaut à la faute intentionnelle ou à la faute lourde, c'est-à-dire la faute qui dénote une insouciance, une imprudence ou une négligence grossières.", "Oui"),
    (3, "Après avoir analysé l'ensemble de la preuve, le Tribunal conclut que la défenderesse a manqué à son obligation de renseignement envers le demandeur.", "Non"),
    (4, "L'appel est accueilli et les dommages-intérêts accordés en première instance sont réduits de 75 000$ à 40 000$, les dommages moraux n'ayant pas été établis avec la précision requise.", "Non"),
    (5, "La Cour note que le témoignage de M. Tremblay sur ce point n'était pas crédible et qu'il y avait lieu de préférer la version des faits donnée par la plaignante.", "Non"),
]

DEFINITION_TEST = [
    (0, "L'expression 'acte à titre gratuit' vise tout acte par lequel une personne procure à une autre un avantage sans contrepartie, ce qui inclut notamment la donation, le legs et le prêt à usage.", "Oui"),
    (1, "Au sens de l'art. 1803 CCQ, le mandataire est celui qui, en vertu d'un acte juridique appelé mandat, reçoit le pouvoir d'accomplir des actes juridiques pour le compte du mandant et en son nom.", "Oui"),
    (2, "Par 'vice caché' au sens de l'art. 1726 CCQ, on entend un défaut qui rend le bien impropre à l'usage auquel on le destine ou qui diminue tellement son utilité que l'acheteur ne l'aurait pas acheté, ou n'aurait pas payé si haut prix, s'il l'avait connu.", "Oui"),
    (3, "La Cour d'appel a donc eu raison de conclure que les conditions d'application de l'art. 49 de la Charte québécoise étaient réunies en l'espèce.", "Non"),
    (4, "En application des principes retenus dans Clements c. Clements 2012 CSC 32, la preuve de causalité a été établie selon la norme civile applicable.", "Non"),
    (5, "La clause litigieuse est ambiguë et doit être interprétée contre la partie qui l'a rédigée, conformément à la règle contra proferentem.", "Non"),
    (6, "La 'diligence raisonnable', dans le contexte du droit pénal réglementaire canadien, désigne l'ensemble des mesures qu'une personne raisonnablement prudente aurait prises pour éviter l'infraction.", "Oui"),
    (7, "Pour les besoins du présent recours, la 'date de connaissance' s'entend du jour où la victime a su ou aurait dû savoir, en faisant preuve de diligence raisonnable, que le préjudice était imputable à la conduite du défendeur.", "Oui"),
    (8, "Le tribunal a appliqué le critère de la personne raisonnable pour évaluer le comportement de l'accusé dans les circonstances.", "Non"),
    (9, "La demande reconventionnelle est rejetée au motif que la prescription triennale était acquise au moment de l'introduction de l'instance.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# supply_chain_disclosure_best_practice_audits
# ─────────────────────────────────────────────────────────────────────────────

SC_AUDITS_TRAIN = [
    (0, "Notre politique de chaîne d'approvisionnement prévoit des audits annuels de nos fournisseurs de niveau 1 afin de détecter toute situation de travail forcé ou de travail des enfants conformément à nos engagements en vertu de la Loi S-211.", "Oui"),
    (1, "Nous nous réservons le droit d'effectuer des audits inopinés chez nos fournisseurs stratégiques pour vérifier le respect de notre Code de conduite en matière de droits du travail.", "Oui"),
    (2, "Notre programme de conformité inclut des évaluations sur site effectuées par des tiers indépendants chez les fournisseurs dont le profil de risque est élevé.", "Oui"),
    (3, "La société s'engage à collaborer avec les autorités compétentes et à divulguer annuellement ses pratiques relatives à la lutte contre le travail forcé dans sa chaîne d'approvisionnement.", "Non"),
    (4, "Nous offrons à tous nos employés et fournisseurs une formation annuelle sur la reconnaissance et la prévention du travail forcé et du travail des enfants.", "Non"),
    (5, "Notre politique exige que tous les fournisseurs signent notre Code de conduite et certifient qu'ils respectent les normes internationales du travail, notamment les conventions de l'OIT.", "Non"),
]

SC_AUDITS_TEST = [
    (0, "Conformément à la Loi sur la lutte contre le travail forcé et le travail des enfants dans les chaînes d'approvisionnement, nous effectuons des vérifications documentaires et des visites sur site chez nos 50 principaux fournisseurs chaque année.", "Oui"),
    (1, "Notre équipe de conformité réalise des audits trimestriels dans les pays à risque élevé, y compris des entretiens confidentiels avec les travailleurs.", "Oui"),
    (2, "Nous avons mandaté un cabinet spécialisé pour réaliser des audits sociaux chez l'ensemble de nos fournisseurs de rang 1 en Asie du Sud-Est et en Amérique centrale.", "Oui"),
    (3, "Notre programme d'audit prévoit une inspection préalable des installations avant toute signature de contrat avec un nouveau fournisseur, quel que soit son pays d'origine.", "Oui"),
    (4, "En 2023, nous avons revu notre politique d'approvisionnement pour intégrer les exigences de la Loi S-211 et avons informé l'ensemble de nos fournisseurs de ces nouvelles obligations.", "Non"),
    (5, "Nous collaborons avec des organisations de la société civile pour identifier les risques de travail forcé dans nos chaînes d'approvisionnement, notamment dans le secteur textile.", "Non"),
    (6, "La société a adopté un Comité de conformité chargé de superviser la mise en œuvre de sa politique en matière de droits du travail et d'en rendre compte au Conseil d'administration.", "Non"),
    (7, "En cas de manquement détecté, notre politique prévoit un plan d'action correctif assorti d'un délai de 90 jours et, si le fournisseur ne se conforme pas, la résiliation du contrat.", "Non"),
    (8, "Nous certifions que nos fournisseurs ont signé notre Code de conduite et attestent ne pas recourir au travail forcé, conformément aux Principes directeurs de l'ONU relatifs aux entreprises et aux droits de l'homme.", "Non"),
    (9, "Nous avons formé 100% de nos acheteurs à l'identification des indicateurs de risque de travail forcé lors de leurs visites chez les fournisseurs.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# supply_chain_disclosure_disclosed_audits
# ─────────────────────────────────────────────────────────────────────────────

SC_DISCLOSED_AUDITS_TRAIN = [
    (0, "En 2023, nous avons réalisé 47 audits chez nos fournisseurs de niveau 1 répartis dans 12 pays. Ces audits ont permis d'identifier 8 cas de non-conformité ayant nécessité des plans d'action correctifs.", "Oui"),
    (1, "Durant l'exercice 2022-2023, notre équipe de conformité a effectué des vérifications sur site dans 23 installations de fournisseurs au Vietnam, au Bangladesh et en Inde.", "Oui"),
    (2, "Nous avons mandaté Bureau Veritas pour réaliser 15 audits indépendants chez nos fournisseurs de matières premières en Amérique du Sud au cours de l'exercice écoulé.", "Oui"),
    (3, "Notre politique prévoit la réalisation d'audits annuels dans nos usines partenaires. Ces audits seront effectués par des tiers indépendants accrédités.", "Non"),
    (4, "Nous nous engageons à mettre en place, d'ici 2025, un programme d'audit couvrant 80% de nos fournisseurs directs dans les zones à risque.", "Non"),
    (5, "La direction est consciente de la nécessité d'améliorer sa capacité d'audit et a alloué un budget supplémentaire à cette fin pour l'exercice 2024.", "Non"),
]

SC_DISCLOSED_AUDITS_TEST = [
    (0, "Au cours du dernier exercice financier, nous avons procédé à 32 audits documentaires et 11 inspections physiques dans les installations de nos fournisseurs clés.", "Oui"),
    (1, "En 2023, nous avons conduit 5 audits inopinés dans des usines de confection au Cambodge, dont 2 ont révélé des heures supplémentaires excessives ayant fait l'objet d'une mise en demeure.", "Oui"),
    (2, "Notre rapport de durabilité 2023 fait état de 20 audits réalisés chez des fournisseurs de rang 2, avec un taux de conformité de 87% aux exigences de notre Code de conduite.", "Oui"),
    (3, "Afin de renforcer notre programme, nous prévoyons d'étendre nos activités d'audit à nos fournisseurs de rang 2 d'ici la fin de 2025.", "Non"),
    (4, "La politique d'audit adoptée par le Conseil d'administration en 2023 décrit les modalités d'inspection prévues pour l'exercice à venir.", "Non"),
    (5, "Notre Code de conduite fournisseur exige que tout partenaire commercial autorise nos représentants ou des auditeurs mandatés à accéder à ses installations sur demande.", "Non"),
    (6, "Nous travaillons actuellement à l'élaboration d'un cadre d'audit adapté aux spécificités de notre secteur d'activité et aux exigences de la Loi S-211.", "Non"),
    (7, "Des ressources supplémentaires ont été allouées à notre fonction de conformité afin de soutenir le déploiement de notre nouveau programme d'audit fournisseurs.", "Non"),
    (8, "Dans le cadre de notre démarche ESG, nous avons rejoint l'initiative SEDEX qui facilite le partage d'informations d'audit entre donneurs d'ordres et fournisseurs.", "Non"),
    (9, "Tous nos nouveaux fournisseurs font l'objet d'une évaluation préalable fondée sur des questionnaires d'auto-déclaration couvrant les risques de travail forcé.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# citation_prediction_classification  (McGill Guide 10th ed.)
# ─────────────────────────────────────────────────────────────────────────────

CITATION_TRAIN = [
    (0, "Citation proposée: 'Doré c Barreau du Québec, 2012 CSC 12, [2012] 1 RCS 395.' — Cette citation correspond-elle à l'arrêt portant sur le contrôle judiciaire des décisions administratives affectant les droits garantis par la Charte?", "Oui"),
    (1, "Citation proposée: 'R c Jordan, 2016 CSC 28' — Cette citation correspond-elle à l'arrêt dans lequel la Cour suprême a établi le nouveau cadre d'analyse pour les délais déraisonnables en vertu de l'art. 11b) de la Charte?", "Oui"),
    (2, "Citation proposée: 'Clements c Clements, 2010 CSC 32' — Cette citation est-elle correcte pour l'arrêt sur la preuve de la causalité en responsabilité civile délictuelle?", "Non"),
    (3, "Citation proposée: 'Bhasin c Hrynew, 2014 CSC 71, [2014] 3 RCS 494' — Cette citation correspond-elle à l'arrêt ayant reconnu une obligation générale d'exécution honnête des contrats en droit canadien?", "Oui"),
    (4, "Citation proposée: 'Banque de Montréal c Bail Ltée, [1992] 2 RCS 544' — Cette citation est-elle exacte pour l'arrêt sur l'obligation de renseignement précontractuelle?", "Oui"),
    (5, "Citation proposée: 'Cinar Corporation c Robinson, 2013 CSC 73' — Cette citation correspond-elle à l'arrêt sur la violation du droit d'auteur et la détermination du quantum des dommages en propriété intellectuelle?", "Oui"),
]

CITATION_TEST = [
    (0, "Citation proposée: 'Housen c Nikolaisen, 2002 CSC 33, [2002] 2 RCS 235' — Cette citation est-elle exacte pour l'arrêt établissant les normes d'appel en matière de conclusions de fait et de droit?", "Oui"),
    (1, "Citation proposée: 'Dunsmuir c Nouveau-Brunswick, 2009 CSC 9' — Cette citation est-elle correcte pour l'arrêt ayant rationalisé les normes de contrôle judiciaire en droit administratif canadien?", "Non"),
    (2, "Citation proposée: 'Syndicat Northcrest c Amselem, 2004 CSC 47, [2004] 2 RCS 551' — Cette citation est-elle exacte pour l'arrêt sur la liberté de religion et les pratiques religieuses dans les immeubles en copropriété?", "Oui"),
    (3, "Citation proposée: 'R c Oakes, [1986] 1 RCS 103' — Cette citation est-elle exacte pour l'arrêt établissant le test d'application de l'article premier de la Charte?", "Oui"),
    (4, "Citation proposée: 'Ciment du Saint-Laurent inc c Barrette, 2008 CSC 64' — Cette citation est-elle exacte pour l'arrêt sur la responsabilité civile pour trouble de voisinage et pollution?", "Oui"),
    (5, "Citation proposée: 'Colombie-Britannique c Imperial Tobacco Canada Ltée, 2006 CSC 49' — Cette citation correspond-elle à l'arrêt sur la constitutionnalité de la Loi sur l'indemnisation des droits à l'égard du tabac?", "Oui"),
    (6, "Citation proposée: 'R c Big M Drug Mart Ltd, [1985] 1 RCS 295' — Cette citation est-elle exacte pour l'arrêt établissant que la Loi sur le dimanche violait la liberté de religion?", "Oui"),
    (7, "Citation proposée: 'Anns c Merton London Borough Council, [1977] 2 All ER 492' — Cette citation est-elle correcte pour la référence utilisée dans les décisions de la CSC sur la négligence des inspecteurs municipaux?", "Non"),
    (8, "Citation proposée: 'Goodwin c Registrar des sociétés par actions, 2013 CSC 39' — Cette citation est-elle exacte pour l'arrêt sur l'usage du nom choisi par une personne transgenre?", "Non"),
    (9, "Citation proposée: 'Mustapha c Culligan du Canada Ltée, 2008 CSC 27, [2008] 2 RCS 114' — Cette citation est-elle exacte pour l'arrêt sur les dommages psychologiques et le critère de la prévisibilité du préjudice?", "Oui"),
]

# ─────────────────────────────────────────────────────────────────────────────
# privacy_policy_entailment  (Loi 25 / LPRPDE)
# ─────────────────────────────────────────────────────────────────────────────

PRIVACY_ENTAILMENT_TRAIN = [
    (0, "Nous partageons vos renseignements personnels avec nos partenaires commerciaux à des fins de marketing ciblé et d'analyse comportementale.", "Oui"),
    (1, "Vos données peuvent être transférées à des tiers prestataires de services situés hors du Québec, notamment aux États-Unis, aux fins d'hébergement et de traitement informatique.", "Oui"),
    (2, "En cas de fusion, d'acquisition ou de vente de tout ou partie de nos actifs, vos renseignements personnels pourraient être transférés à l'entité acquérante.", "Oui"),
    (3, "Nous utilisons des témoins de connexion (cookies) pour améliorer votre expérience de navigation et vous proposer des contenus personnalisés.", "Non"),
    (4, "Vous avez le droit de retirer votre consentement à la collecte de vos renseignements personnels à tout moment, sans préjudice de la licéité du traitement fondé sur le consentement effectué avant ce retrait.", "Non"),
    (5, "Nous conservons vos renseignements personnels pendant la durée nécessaire aux fins pour lesquelles ils ont été collectés, soit généralement 5 ans après la fin de notre relation contractuelle.", "Non"),
]

PRIVACY_ENTAILMENT_TEST = [
    (0, "Nous divulguons vos données à des plateformes publicitaires tierces, notamment Google et Meta, afin de vous montrer des annonces pertinentes sur d'autres sites Web.", "Oui"),
    (1, "En souscrivant à notre service, vous acceptez que vos renseignements personnels soient partagés avec nos filiales et sociétés affiliées pour des offres promotionnelles.", "Oui"),
    (2, "Nos sous-traitants ont accès à certaines de vos données personnelles dans la mesure nécessaire à l'exécution des services qu'ils nous fournissent.", "Oui"),
    (3, "Nous conservons vos données de navigation pour une durée maximale de 13 mois à compter de leur collecte.", "Non"),
    (4, "Vous pouvez à tout moment demander l'accès à vos renseignements personnels en soumettant une demande écrite à notre responsable de la protection des renseignements personnels.", "Non"),
    (5, "Nous mettons en œuvre des mesures de sécurité organisationnelles et techniques proportionnées aux risques afin de protéger vos renseignements personnels contre l'accès non autorisé.", "Non"),
    (6, "Nos serveurs sont localisés au Québec et vos données ne sont pas transférées à l'extérieur du Canada.", "Non"),
    (7, "Nous pouvons communiquer vos renseignements personnels à des autorités gouvernementales ou judiciaires lorsque la loi l'exige.", "Oui"),
    (8, "Vos données sont vendues à des tiers non affiliés à des fins statistiques et de recherche commerciale.", "Oui"),
    (9, "Nous utilisons un système de recommandation automatisé qui analyse vos habitudes d'achat pour personnaliser les offres affichées dans votre espace client.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# legal_reasoning_causality  (Canadian causation cases)
# ─────────────────────────────────────────────────────────────────────────────

CAUSALITY_TRAIN = [
    (0, "Les données épidémiologiques présentées par l'expert démontrent une corrélation statistiquement significative (risque relatif > 2) entre l'exposition professionnelle à l'amiante et le développement du mésothéliome.", "Oui"),
    (1, "L'étude de cohorte rétrospective portant sur 12 000 participants a révélé que le risque de développer la maladie était 3,4 fois plus élevé chez les personnes exposées au composé chimique en cause.", "Oui"),
    (2, "Selon les calculs actuariels présentés en preuve, la probabilité que l'accident de travail soit la cause déterminante de l'invalidité permanente de la victime dépasse 65%.", "Oui"),
    (3, "Le juge de première instance a conclu que le défendeur avait manqué à son obligation de prudence en ne signalant pas le danger imminent que présentait l'état du trottoir.", "Non"),
    (4, "La Cour accepte que le préjudice subi par le demandeur découle directement de la déclaration inexacte faite par la défenderesse lors des négociations précontractuelles.", "Non"),
    (5, "Après examen de l'ensemble des témoignages d'experts, le tribunal retient que la faute du médecin-défendeur a contribué de manière substantielle à l'aggravation de l'état du patient.", "Non"),
]

CAUSALITY_TEST = [
    (0, "La méta-analyse de 23 études épidémiologiques a permis d'établir qu'une exposition de plus de 10 ans aux particules fines ultrafines multiplie par 2,7 le risque d'accident vasculaire cérébral.", "Oui"),
    (1, "L'analyse statistique du dossier épidémiologique démontre que la probabilité d'une corrélation causale entre la contamination au plomb et le déficit cognitif des enfants exposés est supérieure à 95%.", "Oui"),
    (2, "L'expert en biomécanique a calculé, sur la base des données accélérométriques disponibles, que les forces exercées lors de l'impact auraient causé, dans 80% des cas simulés, une fracture vertébrale.", "Oui"),
    (3, "Le Tribunal est convaincu, selon la prépondérance des probabilités, que l'infection postopératoire est imputable à une stérilisation insuffisante des instruments chirurgicaux.", "Non"),
    (4, "La jurisprudence de la Cour suprême du Canada dans Snell c. Farrell [1990] 2 RCS 311 a assoupli le critère de preuve de la causalité dans les affaires médicales.", "Non"),
    (5, "L'expert pharmacologue a attesté que le médicament prescrit était contre-indiqué en présence d'une insuffisance rénale, condition dont le médecin aurait dû être au courant.", "Non"),
    (6, "Les données recueillies sur une période de 20 ans montrent que le taux d'incidence du cancer de la thyroïde est statistiquement 4,1 fois supérieur dans les régions proches des sites d'enfouissement contaminés.", "Oui"),
    (7, "Les résultats de l'étude longitudinale indiquent que 72% des travailleurs exposés au chrome hexavalent pendant plus de 15 ans ont développé des pathologies pulmonaires obstructives.", "Oui"),
    (8, "Les dommages subis par le demandeur comprennent des pertes de revenus passées et futures, ainsi que des douleurs et souffrances évaluées à 85 000$.", "Non"),
    (9, "La Cour retient la responsabilité solidaire des deux défendeurs et condamne chacun à indemniser le demandeur à hauteur de 50% des dommages prouvés.", "Non"),
]


# ─────────────────────────────────────────────────────────────────────────────
# WRITE ALL TSV FILES
# ─────────────────────────────────────────────────────────────────────────────

TASK_DATA = {
    "learned_hands_housing":                              (HOUSING_TRAIN,              HOUSING_TEST),
    "learned_hands_employment":                           (EMPLOYMENT_TRAIN,           EMPLOYMENT_TEST),
    "learned_hands_family":                               (FAMILY_TRAIN,               FAMILY_TEST),
    "learned_hands_immigration":                          (IMMIGRATION_TRAIN,          IMMIGRATION_TEST),
    "learned_hands_consumer":                             (CONSUMER_TRAIN,             CONSUMER_TEST),
    "overruling":                                         (OVERRULING_TRAIN,           OVERRULING_TEST),
    "definition_classification":                          (DEFINITION_TRAIN,           DEFINITION_TEST),
    "supply_chain_disclosure_best_practice_audits":       (SC_AUDITS_TRAIN,            SC_AUDITS_TEST),
    "supply_chain_disclosure_disclosed_audits":           (SC_DISCLOSED_AUDITS_TRAIN,  SC_DISCLOSED_AUDITS_TEST),
    "citation_prediction_classification":                 (CITATION_TRAIN,             CITATION_TEST),
    "privacy_policy_entailment":                          (PRIVACY_ENTAILMENT_TRAIN,   PRIVACY_ENTAILMENT_TEST),
    "legal_reasoning_causality":                          (CAUSALITY_TRAIN,            CAUSALITY_TEST),
}


def write_all() -> None:
    written = 0
    missing = []
    for task_name, (train_rows, test_rows) in TASK_DATA.items():
        task_dir = TASKS_DIR / task_name
        if not task_dir.exists():
            missing.append(task_name)
            continue
        write_tsv(task_dir / "train.tsv", train_rows)
        write_tsv(task_dir / "test.tsv",  test_rows)
        written += 1
        print(f"  {task_name}: {len(train_rows)} train, {len(test_rows)} test")

    print(f"\nWrote TSV data for {written} tasks.")
    if missing:
        print(f"Missing task dirs: {missing}")


if __name__ == "__main__":
    write_all()