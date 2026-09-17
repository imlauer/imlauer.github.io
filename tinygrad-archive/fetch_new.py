import asyncio
import json
import os
import sys

import twscrape

BASE = os.path.dirname(os.path.abspath(__file__))
TWEETS = os.path.join(BASE, "tweets.jsonl")
PENDING = os.path.join(BASE, "fetch_pending.jsonl")


def load_existing_ids():
    ids = set()
    if os.path.exists(TWEETS):
        with open(TWEETS) as f:
            for line in f:
                try:
                    t = json.loads(line)
                except Exception:
                    continue
                ids.add(str(t.get("id") or t.get("id_str")))
    return ids


def load_pending():
    out = []
    if os.path.exists(PENDING):
        with open(PENDING) as f:
            for line in f:
                line = line.strip()
                if line:
                    out.append(json.loads(line))
    return out


async def main():
    api = twscrape.API(pool=os.path.join(BASE, "accounts.db"), raise_when_no_account=False)
    existing = load_existing_ids()
    print(f"existing ids: {len(existing)}", file=sys.stderr, flush=True)

    user = await api.user_by_login("__tinygrad__")
    if user is None:
        raise SystemExit("could not resolve user")
    print(f"user id: {user.id}", file=sys.stderr, flush=True)

    pending = load_pending()
    pending_ids = {str(t.get("id")) for t in pending}
    seen = set()
    new_count = 0
    checked = 0

    # Pull as far back as needed; stop once we are well past the oldest
    # known tweet and beyond any new ones.
    async for t in api.user_tweets(user.id, limit=-1):
        d = t.json()
        tdict = json.loads(d)
        tid = str(tdict.get("id") or tdict.get("id_str"))
        checked += 1
        if tid in seen or tid in pending_ids or tid in existing:
            continue
        seen.add(tid)
        pending.append(tdict)
        pending_ids.add(tid)
        new_count += 1
        if new_count % 25 == 0:
            with open(PENDING, "w") as f:
                for td in pending:
                    f.write(json.dumps(td, ensure_ascii=False) + "\n")
            print(f"checked {checked}, new so far {new_count}", file=sys.stderr, flush=True)

    with open(PENDING, "w") as f:
        for td in pending:
            f.write(json.dumps(td, ensure_ascii=False) + "\n")
    print(f"DONE: checked {checked}, new tweets {new_count}", file=sys.stderr, flush=True)


if __name__ == "__main__":
    asyncio.run(main())