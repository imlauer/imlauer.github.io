import asyncio, json, os
import twscrape

RANGES = [
    ('2023-01-01', '2024-01-01'),
    ('2024-01-01', '2025-01-01'),
    ('2025-01-01', '2026-01-01'),
    ('2026-01-01', '2026-10-01'),
]

async def main():
    api = twscrape.API(pool='accounts.db', raise_when_no_account=False)
    data = [json.loads(l) for l in open('tweets.jsonl')]
    arch = {str(t.get('id')): t for t in data}
    saved = set()
    if os.path.exists('backfill3.jsonl'):
        for l in open('backfill3.jsonl'):
            saved.add(str(json.loads(l)['id']))
    out = open('backfill3.jsonl', 'a')
    for since, until in RANGES:
        q = f'from:__tinygrad__ since:{since} until:{until}'
        n = 0
        got = 0
        print('---', q, flush=True)
        async for t in api.search(q, limit=-1):
            d = json.loads(t.json())
            n += 1
            if d['user']['username'] == '__tinygrad__':
                tid = str(d['id'])
                if tid not in arch and tid not in saved:
                    saved.add(tid)
                    out.write(json.dumps(d, ensure_ascii=False) + '\n')
                    got += 1
            if n % 500 == 0:
                print(f'  entries {n}, missing saved {got}', flush=True)
        print(f'DONE {q}: {got} missing this range', flush=True)
    out.close()
    print('TOTAL MISSING SAVED:', len(saved))

asyncio.run(main())