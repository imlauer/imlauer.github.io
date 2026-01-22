---
title: "HUGO problema: tarda demasiado para generar la página"
date: 2024-11-05T02:17:55-03:00
tags: ['hugo']
---
Solución: `mv static the-files && mkdir static`

Igual vas a copiar dos veces la carpeta static y si tenés por ejemplo 10 gigas de imágenes vas a pasar a tener 20 gigas de imágenes porque copia la carpeta static a public cuando ejecutás `hugo`. 

Pero cambiandolo de nombre hace que sea más rápido, no sé el por qué.

```bash
[I] esotericwarfare@arch ~/p/b/imlauera (master)> cat add_commit_push.sh
#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "Poné el mensaje del commit como primer argumento"
    exit;
fi

hugo &&
cp -R the-files/* public/ &&
git add . &&
git commit -m "$1" &&
git push &&
cd public &&
git add . &&
git commit -m "$1" &&
git push
```
