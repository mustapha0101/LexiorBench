# Déployer Lexior Bench sur RunPod

Ce guide explique comment faire tourner l'interface web de Lexior Bench sur une instance [RunPod](https://runpod.io), en utilisant un modèle local (Ollama / HuggingFace) ou une API distante (OpenAI, Anthropic).

---

## 1 — Choisir le type de Pod

| Cas d'usage | Type de Pod | VRAM minimum |
|---|---|---|
| Modèle local Ollama / HuggingFace (ex. `qwen2.5:7b`) | **GPU Pod** | 8 Go |
| API OpenAI ou Anthropic uniquement | **CPU Pod** | — |

Si vous n'utilisez que les APIs OpenAI ou Anthropic, un Pod CPU suffit et coûte moins cher — aucun GPU requis.

---

## 2 — Créer un Pod sur RunPod

1. Connectez-vous sur [runpod.io](https://runpod.io) et ajoutez un mode de paiement (ou des crédits).
2. Cliquez sur **Deploy** → **GPU Pod** (ou **CPU Pod**).
3. Choisissez un template : **RunPod PyTorch 2.x** (GPU) ou **RunPod Ubuntu 22.04** (CPU).
4. Dans la section **Expose HTTP Ports**, ajoutez le port **`8000`** (port de l'interface FastAPI).
5. *(Optionnel mais recommandé)* Attachez un **Network Volume** (ex. 20 Go) monté sur `/workspace/data`. Cela permet de conserver `results/` et `tasks/` entre les redémarrages.
6. Cliquez sur **Deploy On-Demand**.
7. Attendez que le Pod passe en état **Running**, puis cliquez sur **Connect → SSH**.

> RunPod expose automatiquement le port 8000 via un proxy à l'adresse :
> `https://<pod-id>-8000.proxy.runpod.net`

---

## 3 — Préparer l'environnement

Connectez-vous en SSH (bouton dans le tableau de bord RunPod) et exécutez :

```bash
# 1. Mettre à jour les paquets système
apt-get update -y && apt-get install -y git curl

# 2. Installer uv (gestionnaire de paquets Python rapide)
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env   # ou rouvrez votre shell

# 3. Cloner le dépôt
git clone https://github.com/mustapha0101/LexiorBench.git
cd LexiorBench
git checkout localbench
```

---

## 4 — Installer les dépendances Python

```bash
# Dépendances de base
uv sync

# Ajoutez les extras dont vous avez besoin :
uv sync --extra openai       # Support de l'API OpenAI
uv sync --extra anthropic    # Support de l'API Anthropic
uv sync --extra hf           # Inférence locale HuggingFace
```

> Python 3.10 à 3.12 est requis. Le template PyTorch de RunPod inclut Python 3.10+.

---

## 5 — Configurer les variables d'environnement

Créez un fichier `.env` à la racine du projet (le serveur web le charge automatiquement) :

```bash
cat > .env << 'EOF'
# --- Clés API (laisser vide si non utilisées) ---
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
HF_TOKEN=hf_...            # uniquement pour les dépôts privés HuggingFace

# --- Ollama (uniquement si Ollama tourne sur le même Pod) ---
OLLAMA_BASE_URL=http://localhost:11434

# --- Outils d'annotation (optionnel) ---
# ARGILLA_API_URL=https://...
# ARGILLA_API_KEY=...
# LABEL_STUDIO_URL=https://...
# LABEL_STUDIO_API_KEY=...
EOF
```

---

## 6 — (GPU Pod uniquement) Installer Ollama et télécharger un modèle

```bash
# Installer Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Démarrer le daemon Ollama en arrière-plan
ollama serve &

# Télécharger le modèle à évaluer
ollama pull qwen2.5:7b
# Autres exemples :
# ollama pull mistral:7b
# ollama pull llama3.1:8b
```

> `qwen2.5:7b` nécessite environ 8 Go de VRAM. Choisissez un GPU avec au moins cette capacité (ex. RTX 4090 24 Go, A40 48 Go).

---

## 7 — Persister les résultats avec le Network Volume (optionnel)

Si vous avez attaché un Network Volume monté sur `/workspace/data` :

```bash
# Créer des liens symboliques vers le volume persistant
mkdir -p /workspace/data/results /workspace/data/tasks
ln -s /workspace/data/results results
ln -s /workspace/data/tasks tasks
```

Ainsi, les résultats de benchmarks et les tâches personnalisées survivent aux arrêts et redémarrages du Pod.

---

## 8 — Lancer l'interface web

```bash
uv run lexior-bench web --host 0.0.0.0 --port 8000 --no-browser
```

L'option `--host 0.0.0.0` est obligatoire pour que le proxy RunPod puisse atteindre le serveur.

L'interface est maintenant accessible à :

```
https://<pod-id>-8000.proxy.runpod.net
```

Copiez cette URL depuis le tableau de bord RunPod (**Connect → HTTP Service [Port 8000]**).

---

## 9 — Maintenir le serveur actif (optionnel)

Les sessions SSH se ferment à la déconnexion. Utilisez `tmux` ou `nohup` pour garder le processus en vie :

```bash
# Avec tmux (recommandé)
tmux new -s bench
uv run lexior-bench web --host 0.0.0.0 --port 8000 --no-browser
# Détachez-vous avec Ctrl+B puis D — le serveur continue de tourner
```

---

## 10 — Lancer un benchmark en ligne de commande (alternative à l'interface web)

```bash
# Modèle Ollama
uv run lexior-bench run --model qwen2.5:7b --tasks all --limit 10

# Modèle OpenAI
uv run lexior-bench run --model openai:gpt-4o-mini --tasks all --limit 10

# Modèle Anthropic
uv run lexior-bench run --model anthropic:claude-haiku-4-5-20251001 --tasks all
```

---

## Référence des variables d'environnement

| Variable | Rôle | Valeur par défaut |
|---|---|---|
| `OPENAI_API_KEY` | Authentification API OpenAI | — |
| `ANTHROPIC_API_KEY` | Authentification API Anthropic | — |
| `HF_TOKEN` | Token HuggingFace Hub (dépôts privés) | — |
| `OLLAMA_BASE_URL` | URL du serveur Ollama | `http://localhost:11434` |
| `LEXIOR_ANNOTATION_PROVIDER` | Outil d'annotation par défaut (`argilla` / `labelstudio`) | `argilla` |

---

## Résolution des problèmes courants

**Le port 8000 n'est pas accessible** — Vérifiez que le port `8000` a bien été ajouté dans *Expose HTTP Ports* lors de la création du Pod. Vous pouvez le vérifier dans les paramètres du Pod.

**`uv: command not found`** — Relancez `source $HOME/.cargo/env` ou ouvrez un nouveau shell après l'installation de uv.

**Timeout Ollama / modèle qui ne répond pas** — Vérifiez que `ollama serve` tourne toujours (`ps aux | grep ollama`). Redémarrez-le si nécessaire avant de lancer le serveur web.

**Manque de VRAM** — Choisissez un GPU plus puissant dans le tableau de bord RunPod, ou utilisez un backend API (OpenAI / Anthropic) à la place.
