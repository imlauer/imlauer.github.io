---
title: "Incrementar velocidad subir volumen con ffmpeg"
date: 2025-10-03T16:20:25-03:00
tags: ['ffmpeg']
---

```bash
ffmpeg -i input.m4a -filter:a "volume=4.0,atempo=1.5" output.m4a
```

* `volume=2.0` → doubles the volume (you can use e.g. `1.5` = +50%, `3.0` = triple).
* `atempo=1.5` → speeds up the audio to 1.5×.
* You can chain filters with a comma: `"volume=...,atempo=..."`.

⚠️ Note:

* `atempo` only accepts values from **0.5 to 2.0**.
* If you need faster than 2×, you must chain multiple `atempo` filters, e.g.:

```bash
ffmpeg -i input.mp3 -filter:a "atempo=2.0,atempo=1.5" output.mp3
```

(this would give 3× speed).
