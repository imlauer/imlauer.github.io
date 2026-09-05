import asyncio
import json
import os
import re
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(BASE, "archive.json")
MEDIA = os.path.join(BASE, "media")


def safe_name(url):
    base = os.path.basename(url.split("?")[0])
    base = re.sub(r"[^A-Za-z0-9._-]", "_", base)
    return base


async def download(urls, murl2file):
    os.makedirs(MEDIA, exist_ok=True)
    todo = [u for u in urls if u not in murl2file]
    print(f"{len(todo)} media files to download", flush=True)

    import concurrent.futures
    def fetch(u):
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0", "Referer": "https://x.com/"})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            fname = safe_name(u)
            path = os.path.join(MEDIA, fname)
            with open(path, "wb") as f:
                f.write(data)
            return u, fname
        except Exception as e:
            return u, f"ERR={e!r}"

    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        for u, res in ex.map(fetch, todo):
            if isinstance(res, str) and res.startswith("ERR="):
                print(f"FAIL {u}: {res}", flush=True)
            else:
                murl2file[u] = res
                done += 1
                if done % 100 == 0:
                    print(f"{done}/{len(todo)} done", flush=True)
    print(f"downloads complete: {done}", flush=True)


async def main():
    if not os.path.exists(ARCHIVE):
        raise SystemExit(f"missing {ARCHIVE}")
    with open(ARCHIVE) as f:
        data = json.load(f)

    # persist mapping across runs
    mapping_file = os.path.join(BASE, "media_url_map.json")
    murl2file = {}
    if os.path.exists(mapping_file):
        murl2file = json.load(open(mapping_file))

    urls = set()
    for t in data["tweets"] + list(data["parents"].values()):
        m = t.get("media")
        # avatar also if scheme only
        if m:
            for p in m.get("photos", []) or []:
                urls.add(p.get("url", ""))
            for v in m.get("videos", []) or []:
                if v.get("thumbnailUrl"):
                    urls.add(v["thumbnailUrl"])

    await download(urls, murl2file)

    json.dump(murl2file, open(mapping_file, "w"), indent=2)
    print(f"mapping has {len(murl2file)} entries", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
