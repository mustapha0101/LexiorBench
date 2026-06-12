#!/usr/bin/env bash
# Lexior Bench smoke test (Linux / macOS)
# Requires: uv, and Ollama running with the lexiorgpt model pulled.
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== unit tests =="
uv run pytest -q

echo "== task registry =="
uv run lexior-bench list-tasks

echo "== live run (2 items per task) =="
uv run lexior-bench run --model ollama:lexiorgpt --tasks all --limit 2

echo "Smoke test passed. See the latest folder under results/ for report.md."
