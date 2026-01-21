---
title: "Cambiar resolucion camara: MPV"
date: 2024-10-16T21:30:38-03:00
tags: ['mpv']
---

```bash
sudo apt-get install v4l-utils

### Listar los formatos disponibles
v4l2-ctl --list-formats

ffmpeg -f v4l2 -list_formats all -i /dev/video0


v4l2-ctl --device=/dev/video0 --set-fmt-video=width=1280,height=720,pixelformat=YUYV

v4l2-ctl --device=/dev/video0 --set-fmt-video=width=1280,height=720,pixelformat=MJPG

v4l2-ctl --device=/dev/video0 --get-fmt-video

mpv /dev/video0
```
