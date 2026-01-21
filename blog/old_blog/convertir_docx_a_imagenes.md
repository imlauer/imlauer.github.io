---
title: "Convertir docx a imágenes para leerlo desde la terminal. Convertir docx a texto."
date: 2025-01-16T06:57:22-03:00
tags: ['pandoc']
---
```bash
pandoc --extract-media . input.docx -o output.html
w3m output.html
```
##### Convertir docx a txt
```bash
pandoc -s electricidad33.docx -t plain -o output.txt
```
