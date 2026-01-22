---
title: "Transformar imagenes a video con ffmpeg"
date: 2024-11-14T15:13:53-03:00
tags: ['ffmpeg']
---
Precaución: Todas las imágenes o tienen que ser horizontales o tienen que ser verticales, de lo contrario las imágenes quedarán estiradas
```bash
cat *.jpg | ffmpeg -f image2pipe -r 1 -vcodec mjpeg -i - -vcodec libx264 out.mp4
```
