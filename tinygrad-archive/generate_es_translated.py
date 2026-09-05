import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(BASE, 'archive.json')
TRANS = os.path.join(BASE, 'translations.json')
OUTPUT = os.path.join(BASE, 'archive_es.html')
MAPPING = os.path.join(BASE, 'media_url_map.json')

CSS = '''body{background:#15202b;color:#e7e9ea;font:15px/1.5 system-ui,sans-serif;margin:0}
main{max-width:600px;margin:0 auto;padding:12px}
h1{font-size:18px;color:#1d9bf0}
a{color:#1d9bf0;text-decoration:none}
a:hover{text-decoration:underline}
img{max-width:100%;border-radius:8px;margin-top:4px}
blockquote{border-left:3px solid #657786;margin:4px 0 10px;padding:2px 10px;color:#8899a6;background:#1e2732}
.s{color:#8899a6;font-size:13px}
.r{margin:6px 0 0;font-size:12px;color:#5b6d7a}
p{margin:10px 0;display:block}
.trans{color:#e7e9ea}
.orig{color:#8899a6;font-size:13px;margin-top:4px}
.otag{color:#5b6d7a;font-size:11px;letter-spacing:.05em;text-transform:uppercase}'''

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
            vt = v.get('thumbnailUrl')
            if vt:
                u = 'media/' + murl2file.get(vt) if murl2file.get(vt) else vt
                out.append('<br><img loading="lazy" src="' + esc(u) + '">')
    return ''.join(out)

def render(t, murl2file, trans, key, show_trans=True):
    u = t.get('user') or {}
    name = u.get('username') or t.get('inReplyToScreenName') or ''
    dt = str(t.get('date','')).replace('T',' ')[:16]
    head = f'<span class="s"><b>@{esc(name)}</b> &middot; {dt}</span><br>'
    if show_trans and key in trans:
        body = '<span class="trans">' + linkify(trans[key]) + '</span>'
        if (t.get('rawContent') or '').strip() != (trans[key] or '').strip():
            body += '<div class="orig"><span class="otag">Original:</span> ' + linkify(t.get('rawContent','')) + '</div>'
    else:
        body = linkify(t.get('rawContent',''))
    return head + body + media(t, murl2file)

def main():
    with open(ARCHIVE) as f:
        data = json.load(f)
    trans = {}
    if os.path.exists(TRANS):
        trans = json.load(open(TRANS))
    murl2file = {}
    if os.path.exists(MAPPING):
        murl2file = json.load(open(MAPPING))
    tweets = sorted(data.get('tweets', []), key=lambda t: t.get('date',''))
    parents = data.get('parents', {})
    lines = ['<div class="r">Archivo de</div><h1>@__tinygrad__ — ' + str(len(tweets)) + ' tweets</h1><div class="r">Traducido al español (rioplatense). En orden cronológico, con los tweets a los que respondió.</div>']
    missing = 0
    for t in tweets:
        pid = t.get('inReplyToTweetId') or t.get('inReplyToTweetIdStr')
        if pid is not None:
            pt = parents.get(str(pid)) or parents.get(pid)
            if pt:
                pkey = f'parents:{str(pid)}'
                if pkey not in trans:
                    missing += 1
                lines.append('<div class="r">Respondió a:</div><blockquote>' + render(pt, murl2file, trans, pkey) + '</blockquote>')
        tkey = f"tweets:{str(t.get('id') or t.get('id_str'))}"
        if tkey not in trans:
            missing += 1
        lines.append('<p>' + render(t, murl2file, trans, tkey) + '</p>')
    html = '<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>@__tinygrad__ — archivo (ES)</title><style>' + CSS + '</style></head><body><main>' + '\n'.join(lines) + '</main></body></html>'
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print('tweets:', len(tweets), file=sys.stderr)
    print('html:', OUTPUT, f'({os.path.getsize(OUTPUT)/1024/1024:.2f} MB)', file=sys.stderr)
    print('sin traduccion (se muestra original):', missing, file=sys.stderr)

if __name__ == '__main__':
    main()
