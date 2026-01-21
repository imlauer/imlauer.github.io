---
title: "Obtener todas las URLs de las imagenes de un sitio"
date: 2025-03-13T08:08:36-03:00
tags: ['cli']
---
Esto lo uso porque no quiero pushear imágenes a GitHub sino la carpeta se hace enorme, aparte GitHub tiene un historial que por más que borres una imagen, la imagen sigue ahí. Entonces la solución que hice fue subir todas las imágenes a un `blogspot` luego obtengo todas las URL y las inserto en mi página.

Abro vim, entro en selección visual y ejecuto wget: `(Escape+Shift+V+!wget...)`

Ojo estas imágenes son de previsualización tenés que cambiar el `s320` por `s4160` para obtener la imagen a máxima calidad. Es decir cargá las imágenes de previsualización reemplazá s320 por s4160 usando `:%s/s320/s4160/g` y luego volvé a cargar las imágenes de previsualización y agregá los links a la imagen de mejor calidad.

#### Con Wget:
```bash
wget -qO- "https://imlauer.blogspot.com/2025/03/aux-electricista-primera-clase.html" | grep -oP 'img[^>]*src="\K[^"]+'
```
#### Con headless chromium:
```bash
chromium --headless=new "https://imlauer.blogspot.com/2025/03/aux-electricista-primera-clase.html"  --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | grep -oP 'img[^>]*src="\K[^"]+'
```
