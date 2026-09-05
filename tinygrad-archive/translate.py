import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(BASE, "archive.json")
TRANS = os.path.join(BASE, "translations.json")
OLLAMA = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:1.5b"
WORKERS = 3
KEEP_ALIVE = "120m"

SYS = (
    "Translator EN->ES Rioplatense. Preserve URLs, @mentions, #tags, code, "
    "proper nouns (tinygrad, tinybox, GPU, CUDA, etc). "
    "Output ONLY the translation, nothing else."
)


def has_text(x):
    for c in x:
        if c.isalpha():
            return True
    return False


def translate(text):
    if not text or not text.strip() or not has_text(text):
        return text
    prompt = f"{SYS}\n\nTweet:\n{text}\n\nTranslation:"
    body = json.dumps({"model": MODEL, "prompt": prompt, "stream": False, "temperature": 0.1, "keep_alive": KEEP_ALIVE}).encode()
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(OLLAMA, data=body, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                res = json.loads(r.read().decode()).get("response", "").strip()
            if res:
                if "Translation:" in res[:60]:
                    res = res.split("Translation:", 1)[-1].strip()
                if res:
                    return res
            last = "empty response"
        except Exception as e:
            last = repr(e)
        time.sleep(6)
    sys.stderr.write(f"PERMA-FAIL: {last} for {text[:60]!r}\n")
    return text


def main():
    with open(ARCHIVE) as f:
        data = json.load(f)

    jobs = []
    seen = set()
    for group, entries in (("tweets", data.get("tweets", [])), ("parents", list(data.get("parents", {}).values()))):
        for t in entries:
            tid = t.get("id") or t.get("id_str")
            content = t.get("rawContent")
            key = f"{group}:{tid}"
            if key not in seen:
                seen.add(key)
                if content and content.strip():
                    jobs.append((key, content))

    print(f"total jobs: {len(jobs)}", flush=True)

    translations = {}
    if os.path.exists(TRANS):
        with open(TRANS) as f:
            translations = json.load(f)

    todo = [(k, c) for k, c in jobs if k not in translations]
    print(f"remaining: {len(todo)}", flush=True)

    new_t = {}
    done = 0
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(translate, c): k for k, c in todo}
        for fut in as_completed(futs):
            k = futs[fut]
            try:
                new_t[k] = fut.result()
            except Exception as e:
                new_t[k] = ""
                sys.stderr.write(f"EXC {k}: {e!r}\n")
            done += 1
            if done % 50 == 0:
                elapsed = time.time() - t0
                rate = done / elapsed * 60
                eta = (len(todo) - done) / rate if rate else 0
                print(f"{done}/{len(todo)} | {rate:.0f}/min | ETA {eta:.1f}h", flush=True)
                with open(TRANS, "w") as f:
                    json.dump({**translations, **new_t}, f, ensure_ascii=False)

    with open(TRANS, "w") as f:
        json.dump({**translations, **new_t}, f, ensure_ascii=False)
    total = len({**translations, **new_t})
    print(f"DONE: {total} translations", flush=True)


if __name__ == "__main__":
    main()