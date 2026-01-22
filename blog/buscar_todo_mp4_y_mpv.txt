---
title: "Buscar todos los mp4 y reproducirlos con mp4"
date: 2025-11-02T15:36:49-03:00
---

```bash
find . -type f -name "*.mp4" -exec mpv {} \;
```


Si estas mirando un video con MPV podes cerrar el video y solo reproducir el audio cambiando el track a audio apretando: `g t` o simplemente `_` (guion bajo).
