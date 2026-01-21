---
title: "Srt to txt"
date: 2025-08-02T09:39:33-03:00
tags: ['subtitles']
---
Si queres hacer un resumen de un video podes descargar los subtítulos y copiar y pegar por partes en Grok, ChatGPT o NotebookLM.

```bash
yt-dlp --ignore-config --write-subs --write-auto-sub --sub-lang es --sub-format "srt" --skip-download https://www.youtube.com/watch?v=VIDEO_ID
sed -E '/^[0-9]+$|^$/d; /^[0-9]{2}:/d' video.en.srt > subtitles.txt
```
