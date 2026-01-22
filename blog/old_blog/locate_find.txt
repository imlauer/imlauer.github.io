---
title: "Buscar archivos rapidamente en GNU/Linux: comando locate"
date: 2025-01-31T05:55:16-03:00
tags: ['findutils','linux']
---
El comando `find` tomará mucho tiempo, la forma más rápida de buscar archivo es usar el comando `locate`, que busca los nombres de archivos (y la ruta) en una base de datos indexada (actualizado por el comando `updatedb`).

El resultado aparecerá inmediatamente con un comando simple:

```bash
locate {file-name-or-path}
```

Si no se encuentra el comando, debe instalar el paquete `mlocate` y ejecutar `sudo updatedb` para preparar la base de datos por primera vez. 

Más detalles acá: https://medium.com/@thucnc/the-fastest-way-to-find-files-by-filename-mlocate-locate-commands-55bf40b297ab


