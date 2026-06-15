# Deploying Lexior Bench on RunPod

This guide covers running the Lexior Bench web UI on a [RunPod](https://runpod.io) cloud instance, with either a local model (Ollama / HuggingFace) or a remote API (OpenAI, Anthropic).

---

## 1 — Choose your Pod type

| Use case | Pod type | Min VRAM |
|---|---|---|
| Ollama / HuggingFace local model (e.g. `qwen2.5:7b`) | **GPU Pod** | 8 GB |
| OpenAI or Anthropic API only | **CPU Pod** | — |

If you only use OpenAI / Anthropic, a CPU-only Pod is cheaper and sufficient — no GPU needed.

---

## 2 — Create a Pod on RunPod

1. Log in at [runpod.io](https://runpod.io) and add a payment method (or credits).
2. Click **Deploy** → **GPU Pod** (or **CPU Pod**).
3. Select a template: **RunPod PyTorch 2.x** (GPU) or **RunPod Ubuntu 22.04** (CPU).
4. Under **Expose HTTP Ports**, add **`8000`** (the FastAPI web UI port).
5. *(Optional but recommended)* Attach a **Network Volume** (e.g. 20 GB) and mount it at `/workspace/data`. This keeps `results/` and `tasks/` between Pod restarts.
6. Click **Deploy On-Demand**.
7. Wait for the Pod to reach **Running** state, then click **Connect → SSH**.

> RunPod automatically proxies HTTP port 8000 at:
> `https://<pod-id>-8000.proxy.runpod.net`

---

## 3 — Set up the environment

Connect via SSH (button in the RunPod dashboard) and run:

```bash
# 1. Update system packages
apt-get update -y && apt-get install -y git curl

# 2. Install uv (fast Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.cargo/env   # or restart your shell

# 3. Clone the repository
git clone https://github.com/mustapha0101/LexiorBench.git
cd LexiorBench
git checkout localbench
```

---

## 4 — Install Python dependencies

```bash
# Core dependencies
uv sync

# Add the optional extras you need:
uv sync --extra openai       # OpenAI API support
uv sync --extra anthropic    # Anthropic API support
uv sync --extra hf           # HuggingFace local inference
```

> Python 3.10–3.12 is required. The RunPod PyTorch template ships with 3.10+.

---

## 5 — Configure environment variables

Create a `.env` file at the root of the project (the web server loads it automatically):

```bash
cat > .env << 'EOF'
# --- API keys (leave blank if unused) ---
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
HF_TOKEN=hf_...            # only needed for private HuggingFace repos

# --- Ollama (only if running locally on the same Pod) ---
OLLAMA_BASE_URL=http://localhost:11434

# --- Annotation tools (optional) ---
# ARGILLA_API_URL=https://...
# ARGILLA_API_KEY=...
# LABEL_STUDIO_URL=https://...
# LABEL_STUDIO_API_KEY=...
EOF
```

---

## 6 — (GPU Pod only) Install Ollama and pull a model

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start the Ollama daemon in the background
ollama serve &

# Pull the model you want to benchmark
ollama pull qwen2.5:7b
# Other examples:
# ollama pull mistral:7b
# ollama pull llama3.1:8b
```

> `qwen2.5:7b` requires ~8 GB VRAM. Choose a GPU with at least that much memory (e.g. RTX 4090 24 GB, A40 48 GB).

---

## 7 — Persist results with the Network Volume (optional)

If you attached a Network Volume at `/workspace/data`:

```bash
# Symlink results/ and tasks/ to the persistent volume
mkdir -p /workspace/data/results /workspace/data/tasks
ln -s /workspace/data/results results
ln -s /workspace/data/tasks tasks
```

This way run results and custom tasks survive Pod stops and restarts.

---

## 8 — Start the web UI

```bash
uv run lexior-bench web --host 0.0.0.0 --port 8000 --no-browser
```

The `--host 0.0.0.0` flag is required so RunPod's proxy can reach the server.

The server is now accessible at:

```
https://<pod-id>-8000.proxy.runpod.net
```

Copy this URL from the RunPod dashboard (**Connect → HTTP Service [Port 8000]**).

---

## 9 — Keep the server alive (optional)

SSH sessions terminate when you disconnect. Use `tmux` or `nohup` to keep the process running:

```bash
# Using tmux (recommended)
tmux new -s bench
uv run lexior-bench web --host 0.0.0.0 --port 8000 --no-browser
# Detach with Ctrl+B then D — the server keeps running
```

---

## 10 — Run a benchmark from the CLI (alternative to the web UI)

```bash
# Ollama model
uv run lexior-bench run --model qwen2.5:7b --tasks all --limit 10

# OpenAI model
uv run lexior-bench run --model openai:gpt-4o-mini --tasks all --limit 10

# Anthropic model
uv run lexior-bench run --model anthropic:claude-haiku-4-5-20251001 --tasks all
```

---

## Environment variable reference

| Variable | Purpose | Default |
|---|---|---|
| `OPENAI_API_KEY` | OpenAI API authentication | — |
| `ANTHROPIC_API_KEY` | Anthropic API authentication | — |
| `HF_TOKEN` | HuggingFace Hub token (private repos) | — |
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `LEXIOR_ANNOTATION_PROVIDER` | Default annotation tool (`argilla` / `labelstudio`) | `argilla` |

---

## Troubleshooting

**Port 8000 not accessible** — Make sure port `8000` was added under *Expose HTTP Ports* when creating the Pod. You can verify in the Pod settings.

**`uv: command not found`** — Re-run `source $HOME/.cargo/env` or open a new shell after installing uv.

**Ollama timeout / model not responding** — Confirm `ollama serve` is still running (`ps aux | grep ollama`). Restart it if needed before starting the web server.

**Out of VRAM** — Switch to a larger GPU type in the RunPod dashboard, or use an API backend (OpenAI / Anthropic) instead.
