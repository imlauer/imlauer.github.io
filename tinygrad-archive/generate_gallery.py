import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.join(BASE, "media")

CSS = '''body{background:#15202b;color:#e7e9ea;font:15px/1.5 system-ui,sans-serif;margin:0}
header{max-width:1400px;margin:0 auto;padding:16px 12px}
h1{font-size:18px;color:#1d9bf0;margin:0 0 8px}
h1 span{color:#8899a6;font-weight:normal;font-size:14px}
nav{max-width:1400px;margin:0 auto;padding:8px 12px;display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
nav a{color:#1d9bf0;text-decoration:none;padding:4px 10px;border:1px solid #29415a;border-radius:6px}
nav a:hover{background:#1c2938}
nav .pages a{border:none;padding:4px 7px}
nav .pages a.cur{color:#fff;background:#1d9bf0;border-radius:4px}
main{max-width:1400px;margin:0 auto;padding:0 12px 24px}
figure{margin:16px 0;text-align:center}
figure img{max-width:100%;height:auto;border-radius:8px;display:block;margin:0 auto}
figcaption{color:#667080;font-size:13px;margin-top:6px}'''


def page_file(i):
    return "gallery.html" if i == 1 else f"gallery_{i}.html"


def nav_html(cur, total):
    pages = []
    for i in range(1, total + 1):
        cls = "cur" if i == cur else ""
        pages.append(f'<a class="{cls}" href="{page_file(i)}">{i}</a>')
    parts = []
    if cur > 1:
        parts.append(f'<a href="{page_file(cur-1)}">&#8592; Prev</a>')
    parts.append('<span class="pages">' + " ".join(pages) + "</span>")
    if cur < total:
        parts.append(f'<a href="{page_file(cur+1)}">Next &#8594;</a>')
    return '<nav id="top">' + "".join(parts) + "</nav>"


def main():
    per_page = 50
    names = sorted(n for n in os.listdir(MEDIA) if os.path.isfile(os.path.join(MEDIA, n)))
    total = max(1, -(-len(names) // per_page))

    for cur in range(1, total + 1):
        chunk = names[(cur - 1) * per_page: cur * per_page]
        lines = ['<!doctype html>',
                 '<html lang="en">',
                 '<head>',
                 '<meta charset="utf-8">',
                 '<meta name="viewport" content="width=device-width,initial-scale=1">',
                 f'<title>@__tinygrad__ media gallery &mdash; page {cur} of {total}</title>',
                 '<style>',
                 CSS,
                 '</style>',
                 '</head>',
                 '<body>',
                 f'<header><h1>@__tinygrad__ media gallery <span>&mdash; page {cur} of {total} ({len(names)} images)</span></h1></header>']
        lines.append(nav_html(cur, total))
        lines.append('<main>')
        for n in chunk:
            lines.append(f'<figure><img loading="lazy" src="media/{n}" alt="{n}"><figcaption>{n}</figcaption></figure>')
        lines.append('</main>')
        lines.append(nav_html(cur, total))
        lines.append('</body>')
        lines.append('</html>')
        with open(os.path.join(BASE, page_file(cur)), "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    print(f"gallery: {len(names)} images across {total} pages", file=sys.stderr)


if __name__ == "__main__":
    main()