"""
generate_samples_structured.py — Generate structured sample data with a configured LLM.

Reads prompts/generation_system_prompt.md, fills in task fields from task.yaml,
calls the configured generation model, and writes the resulting JSON to
data/generated_samples/<task_name>.json. Optionally converts the JSON to
sample.tsv format.

Usage:
    python scripts/generate_samples_structured.py --task <name> --generation-model <provider:model> [--n 20] [--dry-run] [--to-tsv]
    python scripts/generate_samples_structured.py --all --generation-model <provider:model> [--n 20] [--skip-existing] [--to-tsv]

Options:
    --task <name>       Process one task only
    --all               Process all tasks missing a sample.tsv
    --generation-model  Model spec understood by lexior_bench.backends
    --n <int>           Number of examples to generate (default: 20)
    --dry-run           Print filled prompt without calling the model
    --skip-existing     Skip tasks that already have sample.tsv
    --to-tsv            After generation, convert JSON output to sample.tsv
    --law-as-of         Date for legal versioning (default: 2026-01-01)
"""
import sys, io, os, argparse, json, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import yaml
from pathlib import Path

ROOT       = Path(__file__).resolve().parent.parent
TASKS_DIR  = ROOT / 'tasks'
PROMPT_PATH = ROOT / 'prompts' / 'generation_system_prompt.md'
DATA_DIR   = ROOT / 'data' / 'generated_samples'
SRC_DIR    = ROOT / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from lexior_bench.backends import ModelBackend, create_backend

# Load .env
_env_file = ROOT / '.env'
if _env_file.exists():
    for _line in _env_file.read_text(encoding='utf-8').splitlines():
        _line = _line.strip()
        if _line and not _line.startswith('#') and '=' in _line:
            _k, _v = _line.split('=', 1)
            os.environ.setdefault(_k.strip(), _v.strip())

LAW_AS_OF_DEFAULT = '2026-01-01'


def load_task(task_dir: Path) -> dict | None:
    y = task_dir / 'task.yaml'
    return yaml.safe_load(y.read_text(encoding='utf-8')) if y.exists() else None


def load_data_spec(task_dir: Path) -> str:
    p = task_dir / 'data_spec.md'
    return p.read_text(encoding='utf-8') if p.exists() else '(aucune spec disponible)'


def build_classes(meta: dict) -> str:
    detail = meta.get('answer_detail', '')
    # Extract class labels from answer_detail string, e.g. "Binary (Oui/Non)" → "Oui | Non"
    import re
    m = re.search(r'\((.+?)\)', detail)
    if m:
        raw = m.group(1)
        classes = [c.strip() for c in re.split(r'[/|,]', raw)]
        return ' | '.join(classes)
    if meta.get('answer_type') in ('generation', 'classification_and_generation'):
        return 'génération (texte libre)'
    return detail or '—'


def fill_prompt(template: str, meta: dict, n: int, law_as_of: str) -> str:
    legal_sources = meta.get('legal_sources') or []
    sources_str = '\n'.join(f'  - {s}' for s in legal_sources) if legal_sources else '  (non spécifiées)'

    return template.replace('{task_name}',     meta.get('name', ''))            \
                   .replace('{description}',   meta.get('purpose', ''))          \
                   .replace('{answer_type}',   meta.get('answer_type', ''))      \
                   .replace('{answer_detail}', meta.get('answer_detail', ''))    \
                   .replace('{reasoning_type}',meta.get('reasoning_type', ''))   \
                   .replace('{jurisdiction}',  meta.get('jurisdiction', 'both')) \
                   .replace('{language}',      meta.get('language', 'fr'))       \
                   .replace('{metric}',        meta.get('metric', ''))           \
                   .replace('{legal_sources}', sources_str)                      \
                   .replace('{classes}',       build_classes(meta))              \
                   .replace('{n}',             str(n))                           \
                   .replace('{law_as_of}',     law_as_of)


def call_generation_model(model_client: ModelBackend, prompt: str, max_tokens: int) -> str:
    response = model_client.generate(prompt, max_tokens=max_tokens)
    return response.text


def parse_json_response(text: str) -> list[dict]:
    text = text.strip()
    # Strip markdown code fences if present
    if text.startswith('```'):
        text = text.split('\n', 1)[1] if '\n' in text else text[3:]
        if text.endswith('```'):
            text = text[:-3]
    return json.loads(text)


def json_to_tsv_rows(records: list[dict]) -> list[tuple[str, str]]:
    """Convert structured JSON records to (input_text, label) pairs for sample.tsv."""
    rows = []
    for r in records:
        text  = r.get('input', '').replace('\n', '\\n').strip()
        label = r.get('label', '').replace('\n', '\\n').strip()
        if text and label:
            rows.append((text, label))
    return rows


def write_tsv(task_dir: Path, rows: list[tuple[str, str]], generation_model: str):
    tsv_path = task_dir / 'sample.tsv'
    with open(tsv_path, 'w', encoding='utf-8', newline='') as f:
        f.write('index\ttext\tanswer\tsource_model\n')
        for i, (text, answer) in enumerate(rows, 1):
            f.write(f'{i}\t{text}\t{answer}\t{generation_model}\n')
    print(f'  → sample.tsv written ({len(rows)} rows)')


def process_task(
    task_dir: Path,
    template: str,
    n: int,
    law_as_of: str,
    dry_run: bool,
    to_tsv: bool,
    skip_existing: bool,
    model_client: ModelBackend | None,
    generation_model: str,
    max_tokens: int,
):
    name = task_dir.name
    meta = load_task(task_dir)
    if not meta:
        print(f'[SKIP] {name}: no task.yaml')
        return

    if skip_existing and (task_dir / 'sample.tsv').exists():
        print(f'[SKIP] {name}: sample.tsv already exists')
        return

    data_spec = load_data_spec(task_dir)
    system_prompt = fill_prompt(template, meta, n, law_as_of)

    user_message = (
        f"Génère {n} exemples pour la tâche `{name}` en respectant strictement "
        f"le prompt système ci-dessus.\n\n"
        f"=== data_spec.md ===\n{data_spec}"
    )
    generation_prompt = f"{system_prompt}\n\n{user_message}"

    if dry_run:
        print(f'\n{"="*60}')
        print(f'TASK: {name}')
        print(f'{"="*60}')
        print('--- SYSTEM PROMPT (first 600 chars) ---')
        print(system_prompt[:600])
        print('--- GENERATION PROMPT (first 1000 chars) ---')
        print(generation_prompt[:1000])
        return

    print(f'[GEN] {name} (n={n})...')
    try:
        if model_client is None:
            raise RuntimeError('generation model is required outside --dry-run')
        raw = call_generation_model(model_client, generation_prompt, max_tokens)
    except Exception as e:
        print(f'  ERROR calling API: {e}')
        return

    # Save raw JSON
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    json_path = DATA_DIR / f'{name}.json'
    json_path.write_text(raw, encoding='utf-8')
    print(f'  → {json_path.name} saved')

    if to_tsv:
        try:
            records = parse_json_response(raw)
            rows = json_to_tsv_rows(records)
            write_tsv(task_dir, rows, generation_model)
        except Exception as e:
            print(f'  WARNING: could not convert to TSV: {e}')

    time.sleep(1)  # avoid rate limits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--task',          help='Process one task by name')
    parser.add_argument('--all',           action='store_true')
    parser.add_argument('--n',             type=int, default=20)
    parser.add_argument('--dry-run',       action='store_true')
    parser.add_argument('--skip-existing', action='store_true')
    parser.add_argument('--to-tsv',        action='store_true')
    parser.add_argument('--law-as-of',     default=LAW_AS_OF_DEFAULT)
    parser.add_argument(
        '--generation-model',
        '--model',
        dest='generation_model',
        default=os.environ.get('LEXIOR_GENERATION_MODEL'),
        help='Generation model spec, e.g. ollama:qwen2.5:7b, openai:gpt-4o-mini, anthropic:claude-sonnet-4-6.',
    )
    parser.add_argument('--max-tokens', type=int, default=8192)
    args = parser.parse_args()

    if not PROMPT_PATH.exists():
        print(f'ERROR: prompt file not found at {PROMPT_PATH}')
        sys.exit(1)

    template = PROMPT_PATH.read_text(encoding='utf-8')
    model_client = None
    generation_model = args.generation_model or ''
    if not args.dry_run:
        if not generation_model:
            print('ERROR: pass --generation-model or set LEXIOR_GENERATION_MODEL.')
            sys.exit(1)
        try:
            model_client = create_backend(generation_model)
        except Exception as e:
            print(f'ERROR: could not initialize generation model {generation_model!r}: {e}')
            sys.exit(1)

    if args.task:
        task_dir = TASKS_DIR / args.task
        if not task_dir.exists():
            print(f'ERROR: task directory not found: {task_dir}')
            sys.exit(1)
        process_task(
            task_dir,
            template,
            args.n,
            args.law_as_of,
            args.dry_run,
            args.to_tsv,
            args.skip_existing,
            model_client,
            generation_model,
            args.max_tokens,
        )

    elif args.all:
        dirs = sorted(d for d in TASKS_DIR.iterdir() if d.is_dir() and (d / 'task.yaml').exists())
        print(f'Processing {len(dirs)} tasks...')
        for d in dirs:
            process_task(
                d,
                template,
                args.n,
                args.law_as_of,
                args.dry_run,
                args.to_tsv,
                args.skip_existing,
                model_client,
                generation_model,
                args.max_tokens,
            )
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
