---
title: "Como descargar hilo entero de un Foro vBulletin"
date: 2024-09-15T13:27:47-03:00
tags: ['vbulletin']
---

```bash
for id in {1..772}; do
    wget -E --follow-tags=a --reject '*.js,*.css,*.ico,*.txt,*.gif,*.jpg,*.jpeg,*.png,*.mp3,*.pdf,*.tgz,*.flv,*.avi,*.mpeg,*.iso' --header="Accept: text/html" "https://mipagina.com.ar/threads/3934819-mi-hilo/page$id" 
done
```
