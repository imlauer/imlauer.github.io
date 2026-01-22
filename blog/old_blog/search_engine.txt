---
title: "Search engine"
date: 2025-10-20T01:23:15-03:00
---

YaCy buscador P2P 

* **Using link directories** (human-curated lists like [https://neocities.org/browse](https://neocities.org/browse), [https://dmoztools.net](https://dmoztools.net), [https://tildeverse.org](https://tildeverse.org)).
* **Following hyperlinks** from one site to another — like surfing in the 1990s.
* **Using public web indexes** or “link crawls” such as:
  * [https://curlie.org](https://curlie.org) (the modern DMOZ)
  * [https://wiby.me](https://wiby.me) (focuses on classic-style personal websites)
  * [https://smallweb.directory](https://smallweb.directory)
  * [https://marginalia.nu/explore/](https://marginalia.nu/explore/) — a small-web exploration view

## 💾 2. Using **Marginalia’s downloadable domain lists**

Marginalia provides downloadable **domain databases** so you can browse the “small web” offline or create your own local index.

You can find them at:
👉 **[https://downloads.marginalia.nu/](https://downloads.marginalia.nu/)**

There you’ll see:

* `domainlist.txt` – all known small-web domains that Marginalia indexed.
* `domains-YYYY-MM-DD.txt.gz` – dated versions for archival use.
* `linkgraph.tsv.gz` – optional graph of hyperlinks between sites.

Once downloaded, you can:

```bash
wget https://downloads.marginalia.nu/domainlist.txt.gz
gunzip domainlist.txt.gz
less domainlist.txt
```

Then you can browse like this:

```bash
cat domainlist.txt | shuf | head -n 10
```

That shows random domains to open in your browser.

You could even script it:

```bash
for url in $(shuf domainlist.txt | head -n 5); do
  xdg-open "https://$url"
done
```

That opens random “small web” sites in your default browser — **no search engine needed**.

---

## 🛠️ 3. Bonus: build your own offline “explorer”

You can make a lightweight **offline search** or **random site viewer** with:

* `fzf` or `rofi` for interactive selection
* `w3m`, `lynx`, or `falkon` to open pages
* Optionally, use `grep` or `ripgrep` on downloaded domain metadata

Example:

```bash
cat domainlist.txt | fzf | xargs -I{} xdg-open "https://{}"
```

---

Would you like me to show you how to **turn Marginalia’s domain list into a local “surf” command** that randomly opens small-web pages in `w3m` or your preferred browser?


