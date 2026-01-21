---
title: "Record framebuffer"
date: 2024-12-13T19:23:48-03:00
tags: ['framebuffer']
---
```bash
ffmpeg -f fbdev -framerate 10 -i /dev/fb0 output.mkv
```
