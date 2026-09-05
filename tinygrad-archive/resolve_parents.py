import asyncio
import json
import os
import sys

import twscrape

BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(BASE, "archive.json")


def tweet_to_dict(t):
    try:
        return json.loads(t.json())
    except Exception:
        return dict(t) if hasattr(t, '__iter__') else {"id": getattr(t, 'id', None), "rawContent": str(t)}


def load_existing():
    if os.path.exists(ARCHIVE):
        with open(ARCHIVE) as f:
            data = json.load(f)
        return data.get("tweets", []), {int(k): v for k, v in data.get("parents", {}).items()}
    return [], {}


def save_archive(tweets, parents):
    with open(ARCHIVE, "w") as f:
        json.dump({"tweets": tweets, "parents": {str(k): v for k, v in parents.items()}}, f, ensure_ascii=False, indent=2)


async def main():
    db_path = os.path.join(BASE, "accounts.db")
    api = twscrape.API(pool=db_path, raise_when_no_account=False)

    tweets_path = os.path.join(BASE, "tweets.jsonl")
    if not os.path.exists(tweets_path):
        raise SystemExit(f"missing {tweets_path}")

    with open(tweets_path) as f:
        tweets = [json.loads(line) for line in f]

    _, existing_parents = load_existing()

    missing = set()
    for t in tweets:
        pid = t.get("inReplyToTweetId") or t.get("inReplyToTweetIdStr")
        if pid is not None:
            pid = int(pid)
            if pid not in existing_parents:
                missing.add(pid)

    missing = sorted(missing)
    print(f"loaded {len(tweets)} tweets, {len(missing)} missing parents to fetch", file=sys.stderr, flush=True)

    fetched = {}
    not_found = set()
    total = len(missing)
    batch_size = 45

    for batch_start in range(0, total, batch_size):
        batch = missing[batch_start:batch_start + batch_size]
        for i, pid in enumerate(batch):
            idx = batch_start + i + 1
            if pid in not_found:
                continue
            retries = 3
            for attempt in range(retries):
                try:
                    parent = await api.tweet_details(pid)
                    if parent is not None:
                        fetched[pid] = tweet_to_dict(parent)
                        print(f"[{idx}/{total}] ok {pid}", file=sys.stderr, flush=True)
                    else:
                        not_found.add(pid)
                        print(f"[{idx}/{total}] none {pid}", file=sys.stderr, flush=True)
                    break
                except Exception as e:
                    err_str = str(e)
                    if "rate" in err_str.lower() or "429" in err_str or "Too Many" in err_str or "No account" in err_str:
                        wait = 90 * (attempt + 1)
                        print(f"[{idx}/{total}] rate limited on {pid}, waiting {wait}s...", file=sys.stderr, flush=True)
                        await asyncio.sleep(wait)
                    else:
                        print(f"[{idx}/{total}] FAIL {pid}: {e!r}", file=sys.stderr, flush=True)
                        break

        if fetched:
            merged = {**existing_parents, **fetched}
            save_archive(tweets, merged)
            print(f"--- saved checkpoint: {len(merged)} parents total ---", file=sys.stderr, flush=True)

    merged = {**existing_parents, **fetched}
    save_archive(tweets, merged)
    print(f"DONE: {len(fetched)} new parents fetched, {len(not_found)} not found, {len(merged)} total parents", file=sys.stderr, flush=True)


if __name__ == "__main__":
    asyncio.run(main())