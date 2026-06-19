"""
Generate QC/CA TSV data for the remaining 11 learned_hands tasks
that still contain US Reddit posts.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TASKS_DIR = ROOT / "tasks"


def write_tsv(path: Path, rows: list[tuple]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["index", "text", "answer"])
        for i, (_, text, answer) in enumerate(rows):
            writer.writerow([i, text, answer])


# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_benefits  (aide sociale, RRQ, assurance-emploi, aide juridictionnelle)
# ─────────────────────────────────────────────────────────────────────────────

BENEFITS_TRAIN = [
    (0, "J'ai fait une demande d'aide sociale au mois de mars et on m'a refusé en disant que j'avais trop d'actifs. Mon seul actif est une vieille voiture valant moins de 2 000$. Est-ce que ce refus est justifié?", "Oui"),
    (1, "Mon dossier d'assurance-emploi a été rejeté parce que Service Canada dit que j'ai quitté mon emploi volontairement. En réalité, mon employeur m'a donné le choix entre démissionner ou être congédié.", "Oui"),
    (2, "Je reçois des prestations d'invalidité de la RRQ depuis deux ans. On me demande de subir une nouvelle évaluation médicale. Puis-je refuser et que se passe-t-il si je le fais?", "Oui"),
    (3, "Ma demande d'aide juridictionnelle a été refusée parce qu'on dit que mes revenus dépassent le seuil. Mais ce calcul inclut la pension alimentaire que je reçois pour mes enfants. Est-ce correct?", "Oui"),
    (4, "Mon propriétaire a installé une caméra de surveillance pointant directement vers la fenêtre de ma chambre à coucher. Je lui ai demandé de l'enlever mais il refuse.", "Non"),
    (5, "Mon ex-employeur refuse de me remettre mon relevé d'emploi depuis trois semaines. Sans ce document, je ne peux pas faire ma demande d'AE.", "Non"),
]

BENEFITS_TEST = [
    (0, "J'ai reçu un avis de trop-perçu de prestations d'aide sociale pour 1 800$ que le gouvernement veut récupérer. L'erreur vient de leur côté — je les avais informés de ma situation. Comment contester?", "Oui"),
    (1, "J'ai 65 ans et je viens de prendre ma retraite. On m'a dit que je pourrais recevoir à la fois la RRQ, la PSV et le SRG. Comment savoir si j'ai droit aux trois et comment en faire la demande?", "Oui"),
    (2, "Je suis travailleur autonome et j'ai contribué à l'assurance-emploi pendant 5 ans. Suite à une maladie, je veux faire une demande de prestations de maladie. Ai-je droit à cet AE?", "Oui"),
    (3, "Mon dossier d'aide sociale a été fermé sans préavis parce que j'aurais omis de déclarer un revenu d'occupation. Je n'avais pas de revenu — c'était un don de ma famille.", "Oui"),
    (4, "Mon voisin a planté des arbres le long de la clôture qui bloquent maintenant complètement la lumière naturelle dans mon salon. Ai-je un recours?", "Non"),
    (5, "J'ai loué une voiture et eu un accident. La compagnie me réclame 5 000$ pour les dommages. Mon assurance personnelle couvre-t-elle les véhicules de location?", "Non"),
    (6, "Mon employeur a payé ma formation professionnelle et veut maintenant me faire rembourser 15 000$ parce que je quitte l'entreprise après 18 mois. Y a-t-il une clause de remboursement acceptable?", "Non"),
    (7, "Mon beau-père est décédé sans testament. Sa conjointe de fait (ma mère biologique n'est pas impliquée) réclame tout l'héritage. Mes demi-frères et moi, avons-nous des droits?", "Non"),
    (8, "J'ai une audience à la Division d'appel de la Sécurité sociale pour contester un refus de prestations d'invalidité du RPC. Comment me préparer?", "Oui"),
    (9, "J'ai reçu un Supplément de revenu garanti (SRG) mais la somme est inférieure à ce que j'attendais. Après vérification, Service Canada a utilisé mes revenus de l'année passée qui étaient anormalement élevés. Puis-je demander une révision?", "Oui"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_business  (droit des affaires, sociétés, commerce)
# ─────────────────────────────────────────────────────────────────────────────

BUSINESS_TRAIN = [
    (0, "J'ai fondé une start-up avec deux associés il y a deux ans. Un associé veut partir et il réclame 50% des actifs alors qu'il n'a contribué qu'à 20%. Notre convention d'actionnaires n'est pas très claire sur ce point.", "Oui"),
    (1, "Ma société par actions a reçu un avis de cotisation pour des taxes de vente non perçues sur des services vendus en ligne à des clients québécois. Suis-je vraiment obligé de percevoir la TVQ?", "Oui"),
    (2, "Un concurrent utilise un nom commercial très similaire au mien dans la même région. Cela crée de la confusion chez mes clients. Quels sont mes recours?", "Oui"),
    (3, "J'ai vendu ma PME il y a 6 mois. L'acheteur me reproche maintenant que certains postes financiers dans ses états étaient incorrects. Il menace de poursuites pour fausse déclaration.", "Oui"),
    (4, "Mon locataire commercial n'a pas payé le loyer depuis 4 mois. Le bail prévoit-il un recours immédiat pour résiliation ou dois-je d'abord lui envoyer une mise en demeure?", "Non"),
    (5, "J'ai subi un accident de travail et la CNESST a refusé ma réclamation en disant que ma blessure n'est pas liée à mon emploi. Comment contester cette décision?", "Non"),
]

BUSINESS_TEST = [
    (0, "Mon associé a utilisé des fonds de notre société pour régler ses dettes personnelles sans mon consentement. La société est maintenant en difficulté financière. Quels sont mes recours contre lui personnellement?", "Oui"),
    (1, "Je veux dissoudre ma société par actions et distribuer les actifs restants. Quelles sont les étapes obligatoires au Québec et dois-je d'abord payer toutes mes dettes?", "Oui"),
    (2, "Un client me doit 45 000$ et il est maintenant insolvable. Puis-je me déclarer créancier prioritaire si j'ai une garantie sur ses équipements?", "Oui"),
    (3, "Je suis directeur d'une PME et on m'accuse personnellement d'avoir signé des chèques en sachant que la société était insolvable. Quelle est ma responsabilité personnelle?", "Oui"),
    (4, "Mon conjoint de fait et moi nous séparons après 12 ans. Nous n'avions pas de contrat de vie commune. Il réclame la moitié de ma maison que j'avais achetée avant notre relation.", "Non"),
    (5, "Mon fils de 17 ans a été arrêté pour vol à l'étalage. C'est sa première infraction. Va-t-il avoir un casier judiciaire?", "Non"),
    (6, "Ma compagnie a fait l'objet d'une inspection de la CNESST qui a relevé plusieurs violations. On m'impose des amendes de 10 000$. Puis-je les contester?", "Oui"),
    (7, "Je veux me convertir en travailleur autonome après 10 ans comme salarié. Mon employeur dit que le contrat de services que je signerais contient une clause de non-concurrence. Est-elle valide?", "Non"),
    (8, "Un franchiseur me demande de payer des redevances supplémentaires non prévues dans le contrat de franchise. Puis-je refuser?", "Oui"),
    (9, "J'ai découvert que mon comptable a fait des erreurs dans mes déclarations de revenus des 5 dernières années. Puis-je le poursuivre pour les pénalités fiscales que je dois payer?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_courts  (procédure judiciaire, délais, accès à la justice)
# ─────────────────────────────────────────────────────────────────────────────

COURTS_TRAIN = [
    (0, "J'ai reçu une mise en demeure d'un avocat me réclamant 8 000$. Je conteste totalement la dette. Dois-je répondre par écrit à la mise en demeure ou puis-je attendre qu'ils déposent une action en justice?", "Oui"),
    (1, "J'ai été condamné par défaut au tribunal parce que je n'avais pas reçu l'avis d'audience à temps — le courrier avait été envoyé à mon ancienne adresse. Puis-je faire annuler ce jugement?", "Oui"),
    (2, "Je veux poursuivre mon ex-employeur pour 3 500$ en salaires impayés. Est-ce que la Division des petites créances de la Cour du Québec est le bon endroit et est-ce que je peux y aller seul sans avocat?", "Oui"),
    (3, "Mon jugement est exécutoire depuis 6 mois mais l'autre partie ne paie pas. Comment faire saisir son salaire ou ses biens au Québec?", "Oui"),
    (4, "Mon propriétaire veut augmenter mon loyer de 12%. Je veux contester au TAL. Y a-t-il un délai pour le faire après réception de l'avis d'augmentation?", "Non"),
    (5, "J'ai un accident de voiture avec un conducteur non assuré. Comment être indemnisé via la SAAQ?", "Non"),
]

COURTS_TEST = [
    (0, "Mon employeur me réclame 20 000$ pour avoir prétendument divulgué des secrets commerciaux. Je n'ai rien fait de tel. L'assignation à comparaître m'a été remise. Combien de temps ai-je pour répondre?", "Oui"),
    (1, "J'ai une décision favorable du Tribunal administratif du logement mais l'autre partie fait appel à la Cour du Québec. Le recours en appel est-il suspensif — dois-je quand même quitter mon logement?", "Oui"),
    (2, "Je veux intenter un recours collectif contre une compagnie d'assurance qui a refusé de payer des milliers de sinistres similaires au mien. Par où commencer?", "Oui"),
    (3, "Mon ex-femme veut faire exécuter une ordonnance alimentaire au Québec alors qu'elle a été prononcée en Ontario. Le jugement ontarien est-il reconnu directement au Québec?", "Oui"),
    (4, "Mon voisin m'accuse de diffamation pour des commentaires que j'aurais faits sur Facebook. Quels sont les critères de la diffamation en droit québécois?", "Non"),
    (5, "Mon contrat de bail prévoit une clause que mon propriétaire qualifie d'interdiction totale d'avoir des animaux. Mais la loi québécoise permet-elle vraiment d'interdire complètement les animaux de compagnie?", "Non"),
    (6, "Je me représente seul devant la Cour supérieure. L'autre partie est représentée par un avocat et je ne comprends pas toutes les procédures. Où puis-je trouver de l'aide juridique?", "Oui"),
    (7, "Un créancier a obtenu un jugement contre moi il y a 9 ans. Peut-il encore me poursuivre ou la prescription est-elle acquise?", "Oui"),
    (8, "J'ai acheté une maison et après l'acte de vente, j'ai découvert des problèmes de fondation que le vendeur ne m'avait pas révélés. J'ai 3 ans pour poursuivre?", "Non"),
    (9, "L'arbitrage prévu dans mon contrat de travail m'empêche-t-il d'aller devant les tribunaux pour harcèlement psychologique?", "Oui"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_crime  (Code criminel, procédure pénale)
# ─────────────────────────────────────────────────────────────────────────────

CRIME_TRAIN = [
    (0, "J'ai été arrêté hier soir pour voie de fait simple. C'est la première fois que j'ai des démêlés avec la justice. On m'a remis en liberté sous conditions. Qu'est-ce qui m'attend maintenant?", "Oui"),
    (1, "Mon fils a été arrêté pour possession de drogue à des fins de trafic. Il a 19 ans et c'est sa première infraction. L'avocat commis d'office est-il compétent ou vaut-il mieux en prendre un privé?", "Oui"),
    (2, "Je suis convoqué comme témoin devant le tribunal pour une affaire criminelle impliquant mon ancien voisin. Suis-je obligé de témoigner si je ne veux pas?", "Oui"),
    (3, "Mon casier judiciaire date de 15 ans pour un délit mineur et j'ai fini ma peine. Puis-je faire une demande de suspension du casier (réhabilitation) et quels sont les effets?", "Oui"),
    (4, "J'ai signé une convention de règlement avec mon ex-employeur qui contient une clause de non-divulgation. Est-ce que cette clause est valide pour m'empêcher de parler à d'autres victimes de harcèlement?", "Non"),
    (5, "Mon propriétaire m'a envoyé un avis d'éviction pour motif sérieux — il dit que je fais du bruit la nuit. Je conteste ces accusations qui sont selon moi fausses.", "Non"),
]

CRIME_TEST = [
    (0, "J'ai reçu une citation à comparaître pour un délit de fuite après un accident mineur. Je ne savais pas que j'avais touché l'autre véhicule. Que risqué-je?", "Oui"),
    (1, "La police m'a interpellé et fouillé dans la rue sans raison apparente. Elle a trouvé du cannabis que je possédais légalement en quantité permise. L'arrestation qui a suivi est-elle légale?", "Oui"),
    (2, "Mon voisin m'a menacé de mort par message texte après une dispute. J'ai les messages. Est-ce une infraction criminelle et que dois-je faire?", "Oui"),
    (3, "J'ai été victime de fraude par carte de crédit. Quelqu'un a fait 3 000$ de transactions non autorisées. Dois-je porter plainte à la police ou suffit-il de contacter ma banque?", "Oui"),
    (4, "Mon employeur refuse de payer mes vacances accumulées depuis 2 ans lors de mon départ. Il dit que j'aurais dû les prendre pendant mon emploi.", "Non"),
    (5, "J'ai fait une demande de résidence permanente et l'agent d'IRCC m'a demandé des documents supplémentaires. Comment les soumettre et dans quel délai?", "Non"),
    (6, "J'ai été accusé d'avoir envoyé des courriels harcelants à mon ex. Les courriels m'appartiennent mais je nie les avoir envoyés. Comment la preuve numérique fonctionne-t-elle en droit pénal?", "Oui"),
    (7, "Je veux retirer ma plainte pour voies de fait contre mon ex-partenaire. Est-ce que je peux le faire et le procureur doit-il suivre ma décision?", "Oui"),
    (8, "Mon adolescent de 15 ans a été accusé de cyberharcèlement. Va-t-il être jugé comme adulte? Quelles sont les conséquences possibles?", "Oui"),
    (9, "Une société m'a facturé pour des services que je n'ai jamais commandés. Après ma plainte, elle a inscrit une fausse créance chez Equifax. C'est de la fraude?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_divorce  (divorce, séparation légale, pension alimentaire)
# ─────────────────────────────────────────────────────────────────────────────

DIVORCE_TRAIN = [
    (0, "Je suis marié depuis 8 ans et je veux divorcer. Mon conjoint refuse de signer les papiers et dit qu'il ne divorcera jamais. Peut-on forcer un divorce au Canada?", "Oui"),
    (1, "Mon époux et moi avons un contrat de mariage établissant la séparation de biens. Lors du divorce, peut-il réclamer la maison que j'ai achetée avant notre mariage?", "Oui"),
    (2, "Nous avons convenu d'un divorce par consentement mutuel. Mon ex-épouse dit que notre entente sur la garde des enfants n'est pas obligatoire si elle change d'idée. Est-ce vrai?", "Oui"),
    (3, "J'ai arrêté de payer la pension alimentaire parce que mon ex-femme ne me laisse pas voir les enfants conformément à l'ordonnance. Ai-je le droit de faire ça?", "Oui"),
    (4, "Mon employeur exige que je travaille les fins de semaine mais mon contrat de travail ne le prévoyait pas. Puis-je refuser sans risquer mon emploi?", "Non"),
    (5, "Mon propriétaire veut vendre l'immeuble et il m'offre 3 000$ pour quitter volontairement mon appartement. Suis-je obligé d'accepter?", "Non"),
]

DIVORCE_TEST = [
    (0, "Mon ex-mari est en défaut de paiement de pension alimentaire depuis 8 mois. Malgré mes rappels, il ne paie pas. Comment faire exécuter l'ordonnance alimentaire au Québec?", "Oui"),
    (1, "Mon conjoint et moi nous séparons après 15 ans de mariage. Je n'ai pas travaillé pendant 10 ans pour élever les enfants. Ai-je droit à une prestation compensatoire?", "Oui"),
    (2, "Nous vivons en union de fait depuis 12 ans et nous nous séparons. Mon partenaire réclame la moitié de la maison qui est à mon nom. Quels sont ses droits au Québec?", "Oui"),
    (3, "Mon ex-conjoint a déménagé à Toronto avec les enfants sans mon consentement alors que nous avions une garde partagée ordonnée. Que puis-je faire en urgence?", "Oui"),
    (4, "Mon bailleur commercial a vendu l'édifice. Le nouvel acquéreur dit qu'il n'est pas lié par mon bail. Est-ce vrai au Québec?", "Non"),
    (5, "J'ai perdu mon emploi il y a 3 mois et je cherche à faire une demande d'assurance-emploi. Mais mon employeur dit que j'ai démissionné alors que c'est lui qui a mis fin à l'emploi.", "Non"),
    (6, "Mon conjoint et moi nous séparons et nous avons contracté des dettes de carte de crédit ensemble. Comment sont-elles partagées lors de la séparation?", "Oui"),
    (7, "Mon divorce a été prononcé en France il y a 5 ans. Je vis maintenant au Québec. Mon ex-époux veut modifier la pension alimentaire. Le tribunal québécois a-t-il compétence?", "Oui"),
    (8, "Mon père est décédé et a laissé plus de dettes que d'actifs. Ma mère et moi devons-nous payer ses dettes?", "Non"),
    (9, "J'ai signé une procuration générale en faveur de ma sœur pour gérer mes affaires pendant mon hospitalisation. Maintenant je vais mieux mais elle continue à prendre des décisions sans me consulter.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_domestic_violence
# ─────────────────────────────────────────────────────────────────────────────

DV_TRAIN = [
    (0, "Mon conjoint me bat régulièrement. J'ai peur de lui. Je veux partir mais j'ai peur qu'il me retrouve et qu'il me tue. Je n'ai nulle part où aller et nous avons deux jeunes enfants.", "Oui"),
    (1, "Mon ex-partenaire continue de m'envoyer des messages menaçants malgré l'ordonnance de protection. Il stationne aussi devant ma maison. Que dois-je faire?", "Oui"),
    (2, "J'ai subi des violences psychologiques et économiques de mon conjoint pendant 6 ans. Il contrôle tout l'argent et me prive d'autonomie financière. Où puis-je obtenir de l'aide?", "Oui"),
    (3, "Mon ex-conjoint violent a la garde partagée de nos enfants. Ils reviennent de chez lui avec des bleus. Je pense qu'il les maltraite. Comment protéger mes enfants?", "Oui"),
    (4, "J'ai acheté un appartement neuf et le promoteur refuse d'effectuer les corrections des défauts de construction constatés lors de la réception. Quels sont mes recours?", "Non"),
    (5, "Mon père de 80 ans vivant dans une résidence pour personnes âgées me dit que les infirmiers lui volent son argent de poche. Que puis-je faire?", "Non"),
]

DV_TEST = [
    (0, "Mon mari m'a agressée la nuit dernière. J'ai porté plainte à la police mais ils n'ont fait qu'un rapport et sont repartis. Il est encore dans la maison. Que puis-je faire pour le faire partir ce soir?", "Oui"),
    (1, "Je veux quitter mon conjoint violent mais le bail est à son nom. Puis-je partir sans payer le loyer et sans conséquences légales pour moi?", "Oui"),
    (2, "Mon conjoint m'a forcée à signer des procurations et des cessions de parts de notre entreprise pendant une période où il me maltraitait. Ces documents sont-ils valides?", "Oui"),
    (3, "Je vis au Québec et j'ai une ordonnance de protection émise en Ontario contre mon ex. L'ordonnance ontarienne est-elle reconnue et applicable au Québec?", "Oui"),
    (4, "Mon propriétaire a refusé de me louer un appartement parce que j'ai deux jeunes enfants. Est-ce de la discrimination?", "Non"),
    (5, "Mon employeur m'a congédié en invoquant une faute grave pour avoir refusé de faire des heures supplémentaires non prévues à mon contrat.", "Non"),
    (6, "Je veux déposer une demande d'ordonnance de protection (anciennement injonction de ne pas harceler) contre mon ex-partenaire violents. Quelle est la procédure au Québec?", "Oui"),
    (7, "Mon conjoint violent a accès au compte bancaire joint et vide nos économies. Puis-je bloquer l'accès au compte sans son consentement?", "Oui"),
    (8, "J'ai décidé de rester avec mon conjoint violent mais j'ai retiré ma plainte. La Couronne peut-elle quand même le poursuivre?", "Oui"),
    (9, "Un entrepreneur m'a fait payer d'avance pour des travaux qu'il n'a jamais commencés. Il est maintenant introuvable. Que faire?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_education  (droit scolaire, éducation, EHDAA)
# ─────────────────────────────────────────────────────────────────────────────

EDUCATION_TRAIN = [
    (0, "Mon enfant autiste a été suspendu de l'école parce qu'il a eu une crise liée à son handicap. La commission scolaire dit que son comportement était 'inacceptable'. Mes droits?", "Oui"),
    (1, "Mon fils en secondaire 3 ne reçoit pas les services d'orthophonie prévus dans son plan d'intervention depuis 6 mois. L'école dit qu'il n'y a pas d'orthophoniste disponible. Que faire?", "Oui"),
    (2, "Mon enfant a été exclu de la classe régulière et mis dans une classe 'spéciale' sans qu'on nous ait consultés comme parents. Est-ce légal sans notre consentement?", "Oui"),
    (3, "Mon université a annulé mon résultat d'examen en m'accusant de plagiat. J'ai respecté toutes les règles de citation. Comment contester cette décision?", "Oui"),
    (4, "Mon ex-conjoint et moi avons une dispute sur la vente de notre maison familiale que nous partageons depuis notre séparation. Il refuse de la vendre mais le marché est bon.", "Non"),
    (5, "Je suis en invalidité de longue durée depuis 18 mois. Mon assureur veut mettre fin aux prestations en disant que je suis capable de faire un autre type d'emploi. Comment contester?", "Non"),
]

EDUCATION_TEST = [
    (0, "Mon fils de 8 ans a été victime de harcèlement scolaire répété pendant toute l'année. L'école dit avoir 'suivi ses protocoles' mais rien n'a changé. Puis-je poursuivre la commission scolaire?", "Oui"),
    (1, "Ma fille a été expulsée définitivement de l'école secondaire après une seule infraction. Existe-t-il une procédure d'appel et avons-nous droit à une audience?", "Oui"),
    (2, "L'école de mon enfant refuse de lui fournir les adaptations prescrites par un neuropsy (temps supplémentaire aux examens, etc.) en disant que ce n'est 'pas leur politique'.", "Oui"),
    (3, "Mon enfant immigrant allophone a été placé dans une classe d'accueil depuis 3 ans, bien au-delà de la période normale. L'école refuse de l'intégrer en classe régulière.", "Oui"),
    (4, "Mon employeur veut que je travaille pendant mes congés fériés. Je suis payé à l'heure. Ai-je droit à une prime pour ces journées?", "Non"),
    (5, "J'ai acheté une maison dont le vendeur avait caché l'existence d'une servitude. Cette servitude réduit considérablement la valeur de ma propriété.", "Non"),
    (6, "Mon cégep refuse mon dossier d'admission en invoquant mes résultats scolaires, mais les critères d'admission publiés ne mentionnent pas ce seuil. Puis-je contester?", "Oui"),
    (7, "Mon université a augmenté les frais institutionnels obligatoires en cours d'année, ce qui n'était pas prévu à mon inscription. Est-ce légal?", "Oui"),
    (8, "Mon contrat d'emploi a été résilié par mon nouvel employeur après une semaine, en dehors de la période de probation convenue. Ai-je droit à un préavis?", "Non"),
    (9, "Ma co-locataire veut rompre le bail avant terme. Si elle part, dois-je payer sa partie du loyer?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_estates  (successions, testaments, liquidation CCQ)
# ─────────────────────────────────────────────────────────────────────────────

ESTATES_TRAIN = [
    (0, "Mon père est décédé la semaine dernière sans testament. Ma mère est encore vivante. Qui hérite quoi? Je suis fils unique. Faut-il ouvrir une succession?", "Oui"),
    (1, "Ma tante a laissé un testament olographe (écrit à la main) qui me nomme légataire de tous ses biens. Ses enfants contestent ce testament. Que dois-je faire pour le faire valider?", "Oui"),
    (2, "Je suis désigné liquidateur testamentaire de la succession de ma mère. Est-ce que je dois accepter ou puis-je refuser? Quelle est ma responsabilité si je l'accepte?", "Oui"),
    (3, "Mon grand-père a fait des dons à mon cousin juste avant de mourir et il n'a presque plus rien à laisser en héritage. Ces dons peuvent-ils être contestés par les autres héritiers?", "Oui"),
    (4, "Mon employeur m'impose de nouvelles tâches qui ne correspondent pas à mon contrat de travail initial. Puis-je refuser sans risquer de perdre mon emploi?", "Non"),
    (5, "Mon propriétaire refuse de m'accorder une prolongation de bail pendant que je cherche un nouveau logement. Il veut que je parte à la date exacte de fin du bail.", "Non"),
]

ESTATES_TEST = [
    (0, "Ma sœur est décédée en laissant des dettes importantes. Ses enfants mineurs sont ses seuls héritiers légaux. Doivent-ils hériter de ses dettes?", "Oui"),
    (1, "Mon père a fait un testament notarié laissant tout à sa nouvelle conjointe. Moi et mes frères, ses enfants d'un premier mariage, n'héritons de rien. Au Québec, existe-t-il une réserve héréditaire?", "Oui"),
    (2, "Je suis co-héritier d'une maison avec mes deux frères. L'un d'eux refuse de vendre. Puis-je forcer la vente de la maison malgré son refus?", "Oui"),
    (3, "Le liquidateur de la succession de ma mère refuse de me communiquer les états de la succession. Ai-je le droit de voir ces documents en tant qu'héritier?", "Oui"),
    (4, "Ma banque a refusé ma demande de prêt hypothécaire en invoquant mon historique de crédit. Puis-je contester ce refus?", "Non"),
    (5, "J'ai commandé des meubles sur Internet. Le colis est arrivé endommagé. Le vendeur refuse tout remboursement en disant que les dommages sont survenus durant la livraison.", "Non"),
    (6, "Mon père voulait me laisser sa maison mais il a oublié de mettre à jour son testament après avoir eu un deuxième enfant. Comment la maison sera-t-elle distribuée?", "Oui"),
    (7, "Je suis légataire d'un bien immobilier au Québec selon le testament de mon oncle décédé en France. Quel droit s'applique et comment procéder?", "Oui"),
    (8, "J'ai été victime d'hameçonnage et quelqu'un a effectué 5 000$ de virements depuis mon compte. La banque refuse de me rembourser. Mes droits?", "Non"),
    (9, "Mon copropriétaire veut transformer notre condo en Airbnb à temps plein. Le règlement de copropriété l'interdit expressément. Que puis-je faire?", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_health  (droit de la santé, soins médicaux, droits des patients)
# ─────────────────────────────────────────────────────────────────────────────

HEALTH_TRAIN = [
    (0, "Mon médecin a fait une erreur de diagnostic qui a retardé mon traitement de cancer de 8 mois. Pendant ce temps, mon cancer a progressé au stade 3. Ai-je un recours contre lui?", "Oui"),
    (1, "L'hôpital refuse de me remettre une copie de mon dossier médical. Ils disent que c'est 'leur propriété'. J'ai besoin de ce dossier pour une consultation dans un autre hôpital.", "Oui"),
    (2, "Ma psychiatre veut m'hospitaliser de force en psychiatrie. Je ne suis pas d'accord. Quels sont mes droits face à une hospitalisation involontaire au Québec?", "Oui"),
    (3, "Mon chirurgien ne m'a pas informé des risques d'une complication rare qui s'est finalement produite et qui m'a laissé avec des séquelles permanentes. Est-ce de la faute médicale?", "Oui"),
    (4, "Mon voisin a construit une annexe qui dépasse la limite de propriété de 50 cm. Il refuse de la démolir. Quels sont mes recours?", "Non"),
    (5, "Mon ancienne compagnie de téléphonie mobile m'a transmis une fausse créance de 800$ à une agence de recouvrement. Je n'ai jamais eu ce compte.", "Non"),
]

HEALTH_TEST = [
    (0, "L'IVAC m'a refusé une compensation pour les préjudices subis lors d'une agression. Elle dit que je n'ai pas prouvé l'infraction criminelle. Comment contester ce refus?", "Oui"),
    (1, "Mon fils a été blessé lors d'une intervention chirurgicale pédiatrique. L'hôpital offre une compensation 'confidentielle' de 30 000$. Dois-je accepter ou risquer un procès?", "Oui"),
    (2, "Mon assureur-maladie refuse de couvrir un médicament prescrit par mon médecin en disant qu'il n'est pas dans leur formulaire. Puis-je contester ce refus?", "Oui"),
    (3, "J'ai subi une opération au Québec qui s'est mal passée. Je vis maintenant en France et je veux poursuivre le chirurgien québécois. Est-ce possible?", "Oui"),
    (4, "Mon employeur a licencié 15 personnes dont moi sans respecter les délais de préavis collectif prévus par la LNT. Que puis-je réclamer?", "Non"),
    (5, "J'ai signé un bail commercial de 5 ans avec option de renouvellement. Mon propriétaire dit que l'option est nulle parce qu'elle n'était pas suffisamment précise.", "Non"),
    (6, "Mon dentiste m'a posé une couronne défectueuse qui est tombée 3 mois après l'installation. Il refuse de la remplacer gratuitement en disant que c'est 'l'usure normale'.", "Oui"),
    (7, "Un ambulancier n'a pas suivi les protocoles lors de mon transport à l'hôpital, ce qui a aggravé ma blessure. Puis-je poursuivre le service ambulancier?", "Oui"),
    (8, "J'ai immigré récemment et j'ai besoin de soins médicaux urgents. Ai-je le droit aux soins de santé au Québec avant d'obtenir ma carte d'assurance-maladie?", "Non"),
    (9, "Mon logement est envahi par la moisissure. Mon propriétaire refuse de faire les travaux d'assainissement. J'ai des problèmes respiratoires depuis.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_torts  (responsabilité civile extracontractuelle — art. 1457 CCQ)
# ─────────────────────────────────────────────────────────────────────────────

TORTS_TRAIN = [
    (0, "Un chien de mon voisin m'a mordu profondément à la jambe alors que je marchais sur le trottoir. J'ai dû subir plusieurs points de suture et je ne peux plus travailler depuis 3 semaines.", "Oui"),
    (1, "La municipalité n'avait pas salé un trottoir glacé. Je suis tombé et je me suis cassé le poignet. J'ai dû avoir une chirurgie. Puis-je poursuivre la ville?", "Oui"),
    (2, "Un camion de livraison a reculé sur ma voiture stationnée dans un stationnement privé. Le chauffeur a prétendu ne pas avoir vu ma voiture. L'entreprise nie toute responsabilité.", "Oui"),
    (3, "Mon voisin laisse couler l'eau de sa gouttière directement sur ma fondation. Malgré mes demandes répétées, il refuse d'y remédier. Des dommages apparaissent dans mon sous-sol.", "Oui"),
    (4, "Mon employeur me force à travailler pendant mes deux semaines de vacances payées. Il dit qu'il y a une urgence mais cela se répète chaque année. Mes droits?", "Non"),
    (5, "Je veux résilier mon contrat de cellulaire avant la fin du terme. La compagnie exige des frais de résiliation de 400$. Cette pratique est-elle légale au Canada?", "Non"),
]

TORTS_TEST = [
    (0, "Une piscine sans clôture suffisante chez mon voisin a failli noyer mon fils de 4 ans qui s'était aventuré dans sa cour. Mon fils a des séquelles neurologiques légères. Recours?", "Oui"),
    (1, "Un arbre de mon voisin est tombé sur ma maison lors d'une tempête. Il était manifestement pourri — les services d'arboriculture avaient signalé le danger à mon voisin il y a 6 mois.", "Oui"),
    (2, "Un entrepreneur de construction a endommagé mes canalisations en effectuant des travaux sur la propriété voisine. Il nie sa responsabilité et dit que c'était inévitable.", "Oui"),
    (3, "Un médecin dans une clinique privée a révélé mon diagnostic de dépression à mon employeur sans ma permission. Cela a mené à mon congédiement.", "Oui"),
    (4, "J'ai signé un contrat de travail avec une clause d'arbitrage obligatoire. Puis-je quand même aller au tribunal pour un congédiement injuste?", "Non"),
    (5, "Mon conjoint et moi divisons nos biens dans le cadre d'un divorce. Nous avons une REER conjointe. Comment se passe le partage?", "Non"),
    (6, "La glace qui s'est formée sur le toit de mon immeuble locatif est tombée et a blessé un passant. Le passant me poursuit. Quelle est ma responsabilité comme propriétaire?", "Oui"),
    (7, "Un hôtel a divulgué mes informations de carte de crédit lors d'une fuite de données. Des fraudeurs ont fait 2 500$ de charges. Ai-je un recours contre l'hôtel?", "Oui"),
    (8, "Mon employeur a refusé d'accommoder mes convictions religieuses en planifiant mes quarts de travail. Je suis pratiquant juif et ne peux pas travailler le samedi.", "Non"),
    (9, "Mon bailleur m'impute une dette pour des réparations qu'il prétend que j'ai causées, mais j'avais fait un constat d'état à mon entrée dans l'appartement qui montre que ces dommages préexistaient.", "Non"),
]

# ─────────────────────────────────────────────────────────────────────────────
# learned_hands_traffic  (Code de la sécurité routière QC)
# ─────────────────────────────────────────────────────────────────────────────

TRAFFIC_TRAIN = [
    (0, "J'ai reçu un constat d'infraction pour avoir grillé un feu rouge. Je suis certain que le feu était vert. Comment contester ce constat d'infraction au Québec?", "Oui"),
    (1, "J'ai eu un accident de voiture et la SAAQ dit que j'étais à 25% responsable selon leur enquête. Je ne suis pas d'accord. Puis-je contester leur évaluation de la responsabilité?", "Oui"),
    (2, "Ma voiture a été remorquée pendant que j'étais garé sur une rue commerciale. Le panneau de limitation de stationnement était très peu visible. Puis-je contester les frais de remorquage?", "Oui"),
    (3, "J'ai eu un excès de vitesse de 47 km/h au-dessus de la limite dans une zone scolaire. Ce n'est pas ma première infraction. Que risqué-je au niveau des points et du permis?", "Oui"),
    (4, "Mon propriétaire veut vendre l'immeuble où je loue un logement depuis 10 ans. L'acheteur veut l'immeuble vide. Ai-je le droit de rester?", "Non"),
    (5, "Mon ex-partenaire a vidé le compte bancaire joint juste avant notre séparation. Il s'est avéré qu'il avait des dettes de jeu importantes. Que puis-je faire?", "Non"),
]

TRAFFIC_TEST = [
    (0, "J'ai reçu une contravention pour avoir utilisé mon téléphone au volant. Je consultais le GPS qui était sur mon téléphone. Est-ce quand même une infraction au Québec?", "Oui"),
    (1, "Mon permis de conduire a été suspendu pour accumulation de points de démérite. Je dépends de ma voiture pour travailler. Comment puis-je obtenir un permis restreint?", "Oui"),
    (2, "J'ai heurté une voiture stationnée dans un stationnement privé. J'ai laissé une note mais le propriétaire du véhicule veut me poursuivre pour 4 500$ alors que la SAAQ couvre l'essentiel.", "Oui"),
    (3, "La police m'a demandé de souffler dans l'éthylomètre lors d'un contrôle routier. J'avais consommé un verre de vin il y a 3 heures. Mon taux était de 0.07. Que se passe-t-il?", "Oui"),
    (4, "Mon propriétaire exige un chèque de dépôt pour les 'dommages éventuels' avant de me remettre les clés. Est-ce légal au Québec?", "Non"),
    (5, "Mon ex-conjoint me harcèle par SMS depuis notre séparation. J'ai bloqué son numéro mais il utilise des numéros différents. Que puis-je faire?", "Non"),
    (6, "J'ai été impliqué dans un accident de la route. L'autre conducteur prétend avoir le feu vert. Il n'y a pas de caméra sur place. Comment la SAAQ détermine-t-elle la responsabilité?", "Oui"),
    (7, "Mon camion commercial a été immobilisé lors d'une inspection de la CTQ pour des raisons mécaniques. L'immobilisation me coûte cher. La CTQ a-t-elle vraiment ce pouvoir?", "Oui"),
    (8, "Mon contrat d'emploi stipule que mon salaire est 'confidentiel'. Mon collègue m'a dit qu'il gagne 20% de plus que moi pour le même poste. Puis-je en discuter avec lui?", "Non"),
    (9, "Mon propriétaire a tenté d'entrer dans mon appartement sans préavis alors que j'y étais. Puis-je changer la serrure pour l'en empêcher?", "Non"),
]


# ─────────────────────────────────────────────────────────────────────────────
# WRITE ALL
# ─────────────────────────────────────────────────────────────────────────────

TASK_DATA = {
    "learned_hands_benefits":          (BENEFITS_TRAIN,   BENEFITS_TEST),
    "learned_hands_business":          (BUSINESS_TRAIN,   BUSINESS_TEST),
    "learned_hands_courts":            (COURTS_TRAIN,     COURTS_TEST),
    "learned_hands_crime":             (CRIME_TRAIN,      CRIME_TEST),
    "learned_hands_divorce":           (DIVORCE_TRAIN,    DIVORCE_TEST),
    "learned_hands_domestic_violence": (DV_TRAIN,         DV_TEST),
    "learned_hands_education":         (EDUCATION_TRAIN,  EDUCATION_TEST),
    "learned_hands_estates":           (ESTATES_TRAIN,    ESTATES_TEST),
    "learned_hands_health":            (HEALTH_TRAIN,     HEALTH_TEST),
    "learned_hands_torts":             (TORTS_TRAIN,      TORTS_TEST),
    "learned_hands_traffic":           (TRAFFIC_TRAIN,    TRAFFIC_TEST),
}

if __name__ == "__main__":
    written = 0
    for task_name, (train_rows, test_rows) in TASK_DATA.items():
        task_dir = TASKS_DIR / task_name
        if not task_dir.exists():
            print(f"  MISSING: {task_name}")
            continue
        write_tsv(task_dir / "train.tsv", train_rows)
        write_tsv(task_dir / "test.tsv",  test_rows)
        written += 1
        print(f"  {task_name}: {len(train_rows)} train, {len(test_rows)} test")

    print(f"\nDone. Wrote data for {written} tasks.")