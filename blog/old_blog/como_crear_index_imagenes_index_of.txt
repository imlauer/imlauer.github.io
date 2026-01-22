---
title: "Como crear Índice de Imágenes e Index of / sin python sin HUGO solo con bash"
date: 2025-02-02T14:20:16-03:00
tags: ['img']
---
Crear un Index Of para publicarlo en GitHub Pages:

```bash
mkdir mi_pagina
cd mi_pagina
tree -H '' -o index.html
```

Crear gallery index con este script bash, aunque no recomiendo **subir imágenes a github**:

Guardás esto en `gallery-index.sh` y lo ejecutás sobre un directorio te generará un `index.html` 

```bash
#! /bin/sh
echo "<!DOCTYPE html>" > index.html
echo "<html>" >> index.html
echo "<head>" >> index.html
echo "<title>My file gallery</title>" >> index.html
echo "<meta charset=\"utf-8\">" >> index.html
echo "</head>" >> index.html
echo "<body>" >> index.html

echo "<h1>Subdirs</h1>" >> index.html
#link to subdirs
for D in *; do
    if [ -d "${D}" ]; then
        echo "<h3><a href=\"$D\">$D</a></h3>" >> index.html
    fi
done

echo "<h1>Images</h1>" >> index.html
echo "<div style=\"width: 100vw; display: flex; flex-direction: row;  flex-wrap: wrap; \">" >> index.html
for img in *.jpg *.JPG *.png *.PNG *.bmp *.BMP *.jpeg *.JPEG *.gif *.GIF; do
    if [ ! -f "${img}" ]; then
        continue
    fi
    convert -auto-orient -scale 640 $img thumb-$img
     echo "<div style=\"width: 33vw; height: 33vh; \">" >> index.html
         echo "<div style=\"width: 100%; height: 90%;\">" >> index.html
            echo "<img style=\"height: 100%;\" src=\"thumb-$img\"></a>" >> index.html
         echo "</div>" >> index.html
         echo "<div style=\"width: 100%; height: 10%;\">" >> index.html
            echo "<a href=\"$img\">$img</a>" >> index.html
         echo "</div>" >> index.html
     echo "</div>" >> index.html
done
echo "</div>" >> index.html

echo "<h1>Videos</h1>" >> index.html
echo "<div style=\"width: 100vw; display: flex; flex-direction: row;  flex-wrap: wrap; \">" >> index.html
for video in *.mp4 *.MP4 *.ogg *.OGG *.avi *.AVI *.mkv *.MKV *.mpeg *.MPEG; do
    if [ ! -f "${video}" ]; then
       continue
    fi
     echo "<div style=\"width: 33vw; height: 33vh;\">" >> index.html
         echo "<div style=\"width: 100%; height: 90%;\">" >> index.html
            echo "<video style=\"height:100%;\" controls>" >> index.html
                echo "<source src=\"$video\">" >> index.html
            echo "</video>" >> index.html
         echo "</div>" >> index.html
         echo "<div style=\"width: 100%; height: 10%;\">" >> index.html
            echo "<a href=\"$video\">$video</a>" >> index.html
         echo "</div>" >> index.html
     echo "</div>" >> index.html
done
echo "</div>" >> index.html



echo "</body>" >>index.html
echo "</html>" >>index.html
```

