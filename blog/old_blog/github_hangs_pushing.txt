---
title: "Github hangs pushing"
date: 2024-11-04T22:21:56-03:00
tags: ['github']
---
Solución:
```bash
git config --global http.postBuffer 1048576000
```
