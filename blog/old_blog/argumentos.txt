---
title: "Argumentos en bash"
date: 2025-12-13T21:19:02-03:00
---
```bash
#!/bin/sh
if [ $# -lt 2 ]
  then
          echo "Uso: $0 <nombre-archivo> \"<titulo con espacios>\" <ruta del directorio de imagenes(opcional)> <tag_name_archive(opcional)> audio \"texto_entero para generar audio\""
    exit;
fi

```
