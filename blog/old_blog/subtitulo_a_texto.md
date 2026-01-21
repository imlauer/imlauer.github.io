---
title: "Bajar playlist youtube con subtitulo y pasarlo a texto"
date: 2025-01-11T05:27:44-03:00
tags: ['subs']
---
```bash
yt-dlp --ignore-config --write-auto-sub --write-sub --sub-lang es -i "ID_PLAYLIST" -o "%(autonumber)s%(id)s.%(ext)s"
```
Pasar subtítulos de YouTube a texto plano.

```bash
awk 'FNR<=4 || ($0 ~ /^$|-->|\[|\]|</){next} !a[$0]++'  Input_file
```
