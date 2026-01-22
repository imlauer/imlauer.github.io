---
title: "Bash: How to remove file extension"
date: 2025-12-13T19:25:40-03:00
tags: ['cli']
---
```bash
filename="example.txt"
filename_without_extension="${filename%.*}"
echo "$filename_without_extension"
```


Ejemplo de uso para formar urls de imagenes de Archive:
```bash
for i in $(ls *.jpg); do echo "<a href=\"https://archive.org/download/tag_name/$i\"><img src=\"https://archive.org/download/tag_name/${i%.*}_thumb.jpg\"></a>"; done
```
