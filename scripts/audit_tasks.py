import yaml, csv, io, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
TASKS = ROOT / "tasks"
results = []

for d in sorted(TASKS.iterdir()):
    if not d.is_dir(): continue
    yf = d / 'task.yaml'
    if not yf.exists(): continue
    data = yaml.safe_load(yf.read_text(encoding='utf-8'))

    lang = data.get('language', '?')
    labels = data.get('labels', [])
    version = data.get('version', 1)

    train_rows = test_rows = 0
    first_train_text = ''
    for fn, attr in [('train.tsv', 'train'), ('test.tsv', 'test')]:
        f = d / fn
        if f.exists():
            rows = list(csv.reader(io.StringIO(f.read_text(encoding='utf-8')), delimiter='\t'))
            if attr == 'train':
                train_rows = max(0, len(rows) - 1)
                if len(rows) > 1 and len(rows[1]) > 1:
                    first_train_text = rows[1][1][:80]
            else:
                test_rows = max(0, len(rows) - 1)

    english_words = {'the','of','and','or','this','is','in','to','for','a','an','that','with','by','not','from','any'}
    words = set(first_train_text.lower().split())
    is_english = len(words & english_words) >= 3

    labels_str = str(labels)
    labels_ok = any(x in labels_str for x in ['Oui', 'Non', 'Vrai', 'Faux', 'Pertinent', 'allowed', 'Arbitrage', 'Pertinent', 'Modification'])

    results.append({
        'task': d.name,
        'v': version,
        'lang': lang,
        'train': train_rows,
        'test': test_rows,
        'text_lang': 'EN' if is_english else 'FR',
        'labels_ok': labels_ok,
    })

print(f"Total tasks: {len(results)}\n")
print(f"{'Task':<55} {'V':<3} {'Txt':<4} {'Train':<6} {'Test':<7} {'LabelsOK'}")
print('-' * 95)
en_text_tasks = []
for r in results:
    flag = ' <-- EN text' if r['text_lang'] == 'EN' else ''
    print(f"{r['task']:<55} {r['v']:<3} {r['text_lang']:<4} {r['train']:<6} {r['test']:<7} {str(r['labels_ok']):<10}{flag}")
    if r['text_lang'] == 'EN':
        en_text_tasks.append(r['task'])

print(f"\n=== Tasks still with English text ({len(en_text_tasks)}) ===")
for t in en_text_tasks:
    print(f"  {t}")