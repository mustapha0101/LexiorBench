# Lexior Bench smoke test (Windows / PowerShell)
# Requires: uv, and Ollama running with the lexiorgpt model pulled.
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "== unit tests ==" -ForegroundColor Cyan
uv run pytest -q
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "== task registry ==" -ForegroundColor Cyan
uv run lexior-bench list-tasks
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "== live run (2 items per task) ==" -ForegroundColor Cyan
uv run lexior-bench run --model ollama:lexiorgpt --tasks all --limit 2
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Host "Smoke test passed. See the latest folder under results\ for report.md." -ForegroundColor Green
