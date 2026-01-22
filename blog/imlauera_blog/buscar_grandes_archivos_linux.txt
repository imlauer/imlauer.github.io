---
title: "Buscar grandes archivos en la CLI en Linux y borrar caché en ArchLinux."
date: 2024-11-24T11:09:18-03:00
tags: ['linux']
---
1. To find large files on Linux, use this command: `sudo du -aBm / 2>/dev/null | sort -nr | head -n 10`.
2. To find the largest files in a directory, use: `du -ah /directory/name | sort -rn | head -n 10`.
3. To find all files over 500 MB, use: `sudo find / -type f -size +500M -ls`.

#### Para limpiar caché en ArchLinux. 

```bash
sudo pacman -Scc &&  yay  -Scc
```

#### Buscar archivos más grandes que 500 megas.

```bash
find . -type f -size +500M -printf "%s %p\n" | sort -nr | head -n 10
```
