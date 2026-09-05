import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(BASE, 'archive.json')
OUTPUT = os.path.join(BASE, 'archive.html')
MAPPING = os.path.join(BASE, 'media_url_map.json')

CSS = '''body{background:#15202b;color:#e7e9ea;font:15px/1.5 system-ui,sans-serif;margin:0}
main{max-width:600px;margin:0 auto;padding:12px}
h1{font-size:16px;color:#1d9bf0}
a{color:#1d9bf0;text-decoration:none}
a:hover{text-decoration:underline}
img{max-width:100%;border-radius:8px;margin-top:4px}
blockquote{border-left:3px solid #657786;margin:4px 0 10px;padding:2px 10px;color:#8899a6}
.s{color:#8899a6;font-size:13px}
p{margin:10px 0;display:block}'''

def esc(x):
    return str(x).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def linkify(x):
    x = esc(x)
    x = re.sub(r'(https?://[^\s]+)', r'<a href="\1">\1</a>', x)
    return x

def media(t, murl2file):
    out = []
    m = t.get('media')
    if m:
        for p in (m.get('photos') or []):
            u = 'media/' + murl2file.get(p.get('url','')) if murl2file.get(p.get('url','')) else p.get('url')
            out.append('<br><img loading="lazy" src="' + esc(u) + '">')
        for v in (m.get('videos') or []):
            t = v.get('thumbnailUrl')
            if t:
                u = 'media/' + murl2file.get(t) if murl2file.get(t) else t
                out.append('<br><img loading="lazy" src="' + esc(u) + '">')
    return ''.join(out)

def say(t, murl2file):
    u = t.get('user') or {}
    name = u.get('username') or t.get('inReplyToScreenName') or ''
    dt = str(t.get('date','')).replace('T',' ')[:16]
    if u.get('profileImageUrl') and murl2file.get(u.get('profileImageUrl')):
        av = '<img src="' + esc('media/' + murl2file[u.get('profileImageUrl')]) + '" style="width:20px;height:20px;border-radius:50%;display:inline;margin:0 4px;vertical-align:-4px">'
    else:
        av = ''
    return f'<span class="s">{av}<b>@{esc(name)}</b> &middot; {dt}</span><br>{linkify(t.get("rawContent",""))}{media(t, murl2file)}'

def main():
    with open(ARCHIVE) as f:
        data = json.load(f)
    murl2file = {}
    if os.path.exists(MAPPING):
        murl2file = json.load(open(MAPPING))
    tweets = sorted(data.get('tweets', []), key=lambda t: t.get('date',''))
    parents = data.get('parents', {})
    lines = ['<h1>@__tinygrad__ &mdash; ' + str(len(tweets)) + ' tweets</h1>']
    for t in tweets:
        pid = t.get('inReplyToTweetId') or t.get('inReplyToTweetIdStr')
        if pid is not None:
            pt = parents.get(str(pid)) or parents.get(pid)
            if pt:
                lines.append('<blockquote>' + say(pt, murl2file) + '</blockquote>')
        lines.append('<p>' + say(t, murl2file) + '</p>')
    html = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>@__tinygrad__ archive</title><style>' + CSS + '</style></head><body><main>' + '\n'.join(lines) + '</main></body></html>'
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print('tweets:', len(tweets), file=sys.stderr)
    print('html:', OUTPUT, f'({os.path.getsize(OUTPUT)/1024/1024:.2f} MB)', file=sys.stderr)

if __name__ == '__main__':
    main()
