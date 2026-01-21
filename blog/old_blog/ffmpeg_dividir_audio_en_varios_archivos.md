---
title: "Ffmpeg: dividir audio en varios archivos"
date: 2025-03-30T01:17:20-03:00
tags: ['cli']
---
Dividir audio de 2 horas en audios de 1 minuto, esto te puede servir para repetir archivos.

```bash
ffmpeg -i Record-61.m4a -f segment -segment_time 60 -c copy out%03d.m4a
```

