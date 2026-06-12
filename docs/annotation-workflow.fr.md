# Flux d'annotation (juriste dans la boucle)

*[English version: [annotation-workflow.md](annotation-workflow.md)]*

Les réponses de référence des tâches initiales sont des **ébauches** tant
qu'un juriste ne les a pas validées. La boucle : pousser les éléments vers un
outil d'annotation → les juristes valident/corrigent dans l'interface web →
rapatrier les réponses validées dans les TSV → revue avec `git diff` →
commit.

Les TSV demeurent la **source de vérité unique**; les outils d'annotation sont
des adaptateurs interchangeables. Deux fournisseurs sont livrés en v1 —
**Argilla** et **Label Studio** — avec le même schéma d'annotation, ce qui
permet de les évaluer sur les mêmes données et de garder celui que vos
juristes préfèrent. Sélection par `--provider` ou la variable
`LEXIOR_ANNOTATION_PROVIDER` (défaut : `argilla`).

## Schéma d'annotation (identique dans les deux outils)

Pour chaque élément, l'annotateur voit le texte et la réponse proposée
(ébauche), puis remplit :

| Question | Valeurs | Sens |
|---|---|---|
| `answer_ok` | Correcte / Incorrecte | La réponse proposée est-elle bonne? |
| `corrected_answer` | texte libre | La bonne réponse si Incorrecte — doit être l'une des étiquettes de la tâche, à l'identique |
| `item_status` | Validé / À réviser / Rejeté | Validé = final; À réviser = douteux, à discuter; Rejeté = retirer l'élément |

## Règles de rapatriement (pull)

- Seuls les éléments **Validé** sont appliqués. Réponse finale =
  `corrected_answer` si `answer_ok == Incorrecte` et qu'une correction est
  fournie, sinon la réponse originale.
- Les éléments **Rejeté** sont retirés du TSV.
- Les lignes non annotées et **À réviser** conservent leurs valeurs actuelles
  — une annotation partielle ne perd jamais d'éléments.
- Les corrections hors du jeu d'étiquettes déclenchent un avertissement et
  sont ignorées.
- La première réponse validée l'emporte; l'agrégation multi-annotateurs est
  hors périmètre pour la v1.
- Les TSV sont réécrits sur place; **git tient l'historique**. Toujours
  exécuter `--dry-run` d'abord, puis réviser avec `git diff tasks/`.

Chaque élément porte l'identifiant externe `{tâche}-{partition}-{index}` :
re-pousser met à jour les enregistrements au lieu de les dupliquer (sûr après
modification des TSV).

## Argilla (défaut)

```sh
docker compose -f docker/argilla/docker-compose.yml up -d
# Interface : http://localhost:6900 — connexion argilla / 12345678
uv run lexior-bench annotate push --provider argilla --tasks all
# ... annotation dans l'interface (jeux lexior-bench-<tâche>, espace lexior-bench) ...
uv run lexior-bench annotate pull --provider argilla --tasks all --dry-run
uv run lexior-bench annotate pull --provider argilla --tasks all
git diff tasks/
```

Variables : `ARGILLA_API_URL` (défaut `http://localhost:6900`),
`ARGILLA_API_KEY` (défaut `argilla.apikey`).

### Argilla sur Hugging Face Spaces (voie de production)

Pour un hébergement accessible aux juristes sans votre machine : déployer le
[gabarit officiel d'espace Argilla](https://huggingface.co/new-space?template=argilla/argilla-template-space),
puis pointer l'outil vers l'espace — aucun changement de code :

```powershell
$env:ARGILLA_API_URL = "https://<proprietaire>-<espace>.hf.space"
$env:ARGILLA_API_KEY = "<la clé API configurée dans l'espace>"
uv run lexior-bench annotate push --tasks all
```

## Label Studio

```sh
docker compose -f docker/labelstudio/docker-compose.yml up -d
# Interface : http://localhost:8080 — créer un compte à la première visite,
# puis copier votre jeton d'accès depuis « Account & Settings ».
$env:LABEL_STUDIO_API_KEY = "<votre jeton>"      # PowerShell
uv run lexior-bench annotate push --provider labelstudio --tasks all
# ... annotation dans l'interface (projets lexior-bench-<tâche>) ...
uv run lexior-bench annotate pull --provider labelstudio --tasks all --dry-run
uv run lexior-bench annotate pull --provider labelstudio --tasks all
git diff tasks/
```

Variables : `LABEL_STUDIO_URL` (défaut `http://localhost:8080`),
`LABEL_STUDIO_API_KEY` (requise).

## Comparer les deux

Poussez les mêmes tâches vers les deux outils et faites essayer chaque
interface aux juristes. Points à peser, tirés de la mise en place sur ce
projet :

- **Installation** : Label Studio tient dans un seul conteneur; Argilla en
  demande quatre (serveur, worker, Elasticsearch ~1 Go de tas, Redis).
- **Authentification** : Argilla fournit un utilisateur/clé API par défaut
  prévisibles (pratique en local); Label Studio exige la création d'un compte
  et la copie d'un jeton.
- **Ergonomie de revue** : Argilla offre des suggestions de première classe
  (la réponse-ébauche est présélectionnée), des filtres par statut et un suivi
  de progression par jeu; Label Studio offre une interface d'étiquetage plus
  généraliste, un contrôle fin de la mise en page (XML) et de larges options
  d'export.
- **Hébergement** : Argilla a un gabarit officiel gratuit sur HF Spaces (voir
  ci-dessus); Label Studio est généralement auto-hébergé.
