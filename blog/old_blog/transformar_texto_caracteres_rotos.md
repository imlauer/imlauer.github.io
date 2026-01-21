---
title: "Transformar texto caracteres rotos"
date: 2025-11-20T21:51:42-03:00
tags: ['linux']
---
Ejemplo: son mÃ¡s ¡s rÃ¡pidos tecnolÃ³gicas podÃ©s

```bash
iconv -t UTF-8 la_vio.txt | tee la_vio.txt
``` 

O

```bash
iconv -t UTF-8 la_vio.txt > la_vio.txt
```
