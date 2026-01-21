---
title: "Comandos para obtener informacion acerca de tu hardware"
date: 2024-07-17T23:46:43-03:00
tags: ['hardware','obtener','informacion']
---
```console
wmic
cpu get name
os get Caption, OSArchitecture
diskdrive get model, size
logicaldisk get name, Size
sounddev get Caption
product get name

Guardalos en un archivo:
####
wmic cpu get name >> cpuinfo.txt
```
