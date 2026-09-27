import asyncio, json, sys
import twscrape

async def fetch_range(api, user, until_iso, since_iso=None, limit=-1):
    q = f'from:__tinygrad__ until:{until_iso}'
    if since_iso:
        q += f' since:{since_iso}'
    out = []
    async for t in api.search(q, limit=limit):
        d = json.loads(t.json())
        out.append(d)
    return out

async def main():
    api = twscrape.API(pool='accounts.db', raise_when_no_account=False)
    user = await api.user_by_login('__tinygrad__')
    data = [json.loads(l) for l in open('tweets.jsonl')]
    existing = {str(t.get('id') or t.get('id_str')): True for t in data}
    with open('backfill.jsonl', 'w') as out:
        pass
    added = {}
    for month in range(6, 13):
        since = f'2023-{month:02d}-01'
        until = f'2023-{month+1:02d}-01' if month < 12 else f'2024-01-01'
        q = f'from:__tinygrad__ since:{since} until:{until}'
        print(f'--- {q}', flush=True)
        async for t in api.search(q, limit=-1):
            d = json.loads(t.json())
            tid = str(d.get('id'))
            if tid not in existing and tid not in added:
                added[tid] = d
                with open('backfill.jsonl', 'a') as out:
                    out.write(json.dumps(d, ensure_ascii=False) + '\n')
        print(f'cumulative backfill: {len(added)}', flush=True)
    for month in range(1, 4):
        since = f'2024-{month:02d}-01'
        until = f'2024-{month+1:02d}-01' if month < 3 else f'2024-03-16'
        q = f'from:__tinygrad__ since:{since} until:{until}'
        print(f'--- {q}', flush=True)
        async for t in api.search(q, limit=-1):
            d = json.loads(t.json())
            tid = str(d.get('id'))
            if tid not in existing and tid not in added:
                added[tid] = d
                with open('backfill.jsonl', 'a') as out:
                    out.write(json.dumps(d, ensure_ascii=False) + '\n')
        print(f'cumulative backfill: {len(added)}', flush=True)
    print('BACKFILL DONE:', len(added))

asyncio.run(main())