---
title: "Gif to mp4"
date: 2023-11-10T22:41:22-03:00
tags: ['comandos']
---

```bash
ffmpeg -i testing.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" testing.mp4
```

