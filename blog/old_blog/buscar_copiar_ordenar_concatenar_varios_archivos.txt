---
title: "Buscar copiar ordenar concatenar varios archivos"
date: 2024-06-11T14:07:54-03:00
tags: ['copiar','ordenar','concatenar']
---
#### Copiar todos los archivos a un directorio
```bash
find . -name *.vtt -print0 -exec cp {} ./subs/ \;
```
#### Ordenarlos, concatenarlos y guardarlos con el titulo de cada archivo.
```bash
ls | sort -V | tail -n +1 * > wow.txt
```

#### Ejemplo

```bash
tail -n +1 file1.txt file2.txt file3.txt
==> file1.txt <==
```
