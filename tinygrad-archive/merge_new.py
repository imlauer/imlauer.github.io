import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
TWEETS = os.path.join(BASE, "tweets.jsonl")
PENDING = os.path.join(BASE, "fetch_pending.jsonl")


def main():
    order = []
    seen = {}
    if os.path.exists(TWEETS):
        with open(TWEETS) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                t = json.loads(line)
                tid = str(t.get("id") or t.get("id_str"))
                if tid in seen:
                    continue
                seen[tid] = t
                order.append(tid)

    added = 0
    if os.path.exists(PENDING):
        with open(PENDING) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                t = json.loads(line)
                tid = str(t.get("id") or t.get("id_str"))
                if tid in seen:
                    continue
                seen[tid] = t
                order.append(tid)
                added += 1

    tmp = TWEETS + ".tmp"
    with open(tmp, "w") as f:
        for tid in order:
            f.write(json.dumps(seen[tid], ensure_ascii=False) + "\n")
    os.replace(tmp, TWEETS)
    print(f"tweets.jsonl: {len(order)} unique, {added} added", file=sys.stderr, flush=True)


if __name__ == "__main__":
    main()
