# Interface web

*[English version: [web-ui.md](web-ui.md)]*

Une interface web locale couvrant toute la boucle sans commandes shell :
parcourir et créer des tâches, lancer des exécutions avec progression en
direct, consulter les résultats et piloter l'annotation (pousser/rapatrier).

```sh
uv run lexior-bench web            # ouvre http://127.0.0.1:8000
uv run lexior-bench web --port 9000 --no-browser
```

L'interface est bilingue (français par défaut — bascule dans l'en-tête). Elle
écoute sur `127.0.0.1` sans authentification : c'est un **outil local
mono-utilisateur** — ne l'exposez pas sur un réseau. Si un fichier `.env`
existe à la racine du dépôt, la commande `web` le charge dans l'environnement
(pratique pour `LABEL_STUDIO_API_KEY`); le reste du CLI ne le fait pas.

## Pages

- **Tâches** — lister, inspecter, créer (formulaire complet avec validation :
  nom, type, étiquettes, gabarit d'invite, éléments train/test), modifier les
  éléments d'une tâche existante (réécrit les TSV — git tient l'historique),
  supprimer une tâche, ou **importer une tâche LegalBench** depuis une URL
  GitHub (écran de vérification avec étiquettes détectées, décomptes,
  source/licence d'origine; jeu d'évaluation récupéré depuis Hugging Face au
  besoin).
- **Exécuter** — choisir les modèles (les modèles Ollama installés sont
  détectés en direct; autres dorsaux via des lignes `openai:…` /
  `anthropic:…` / `hf:…`, avec indicateurs de clés API), choisir les tâches,
  régler limite/max_tokens, puis suivre la barre de progression. Une
  exécution à la fois; évaluation + rapport sont produits automatiquement.
- **Résultats** — toutes les exécutions, de la plus récente à la plus
  ancienne; par run : classement (tâche / type de raisonnement / domaine),
  taux non analysés et transcription complète avec ✓/✗ et réponses brutes.
- **Annotation** — par tâche : pousser vers Argilla/Label Studio, prévisualiser
  un rapatriement (résumé des changements en mode simulation), l'appliquer.
  Mêmes règles que le CLI (voir
  [annotation-workflow.fr.md](annotation-workflow.fr.md)).

## Hors périmètre (utiliser le CLI / les fichiers)

Files d'attente d'exécutions, accès distant/authentification, modification
des étiquettes ou de l'invite d'une tâche existante (éditer `task.yaml` /
`base_prompt.txt` directement), incrément du champ `version`, gestion
multi-annotateurs.
