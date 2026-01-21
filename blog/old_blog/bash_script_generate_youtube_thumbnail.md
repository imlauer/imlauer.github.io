---
title: "Bash script generate YouTube thumbnail"
date: 2024-11-03T04:09:33-03:00
tags: ['thumbnail']
---
#### Abajo hay una nueva versión esta es la vieja.
```bash
if [[ -z "$1" || -z "$2" ]]; then
  echo "Uso: thumbnailg "Esto es una prueba Esto es otra prueba Siguiente prueba" mi_portada.png"
  exit;
fi
convert -size 1920x1080 plasma:red-blue out.png
convert -font Source-Code-Pro-Medium -fill white -pointsize 100 -gravity center -draw "text 0,0 '$1'" out.png $2
rm out.png

```

##### Copiá este script a `/usr/bin/thumbnailg`

#### Uso:
```bash
thumbnailg "Esto es una prueba
Esto es otra prueba
Siguiente prueba" mi_portada.png
```
Generará un archivo llamado `out1.png`.


#### Posibles errores
`unable to read font Source-Code-Pro-Medium`

Solución: Seleccioná alguna letra disponible: 

```bash
convert -list font
```

#### Nueva version de thumbnailg
```bash
#!/bin/bash
# imagemagick
if [[ -z "$1" || -z "$2" ]]; then
  echo "Uso: thumbnailg "Esto es una prueba Esto es otra prueba Siguiente prueba" mi_portada.png"
  exit;
fi
magick -size 1920x1080 plasma:red-blue out.png
#convert -font Source-Code-Pro-Medium -fill white -pointsize 100 -gravity center -draw "text 0,0 '$1'" out.png $2
magick out.png -font "/usr/share/fonts/noto/NotoSansMono-Regular.ttf" -fill white -pointsize 100 -gravity center -draw "text 0,0 '$1'"  $2
rm out.png
```
