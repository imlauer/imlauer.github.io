---
title: "HUGO consejos: NO subir imágenes"
date: 2024-10-20T12:01:48-03:00
tags: ['hugo']
---
Lo más recomendable es subir las imágenes a otro repositorio, porque sino cuando generás la página ejecutando hugo te genera una carpeta llamada `public` y te copia todas las imágenes a public, o sea si tenés 10 gigas de imágenes vas a tener 20 gigas de imágenes.

Sería bueno crear otro repositorio de la carpeta static así:
```bash
cd static
git init . 
git add . && git commit -m "images and files" && git push
```

O creá el repositorio y clonalo como static:
```bash
mv static static_backup
git clone git@github.com:imlauera/blogimagesandfiles static
cd static_backup
mv * ../static
cd ../static
git add . && git commit -m "images and files" && git push
```


