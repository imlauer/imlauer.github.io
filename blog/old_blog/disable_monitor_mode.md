---
title: "Como deshabilitar el modo monitor"
date: 2025-01-31T21:47:05-03:00
tags: ['monitor']
---
Luego de hacer una prueba de auditoría necesitamos deshabilitar el modo monitor para lograr conectarse a las redes otra vez.

```bash
ifconfig wlp1s0 down
iwconfig wlp1s0 mode managed
ifconfig wlp1s0 up
```
