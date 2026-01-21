---
title: "Como descargar una playlist entera de YouTube y unirla en un solo archivo"
tags: ['descargar','youtube']
categories: ['linux','command line tool']
date: 2023-03-19T03:20:11-03:00
---

### Descargar toda la playlist y guardarlos en archivos sin espacio para facilitar el trabajo usando ffmpeg
En este caso vamos a bajar el audio solamente (esto se hace con -f 140), si queremos el video podemos usar la opcion -f 18 o -f 22 entre otras opciones. Si ponen -F en vez de -f les tira una lista de calidades disponibles.

```bash
yt-dlp -f 140 'https://youtu.be/playlist?list=PLff7Jl9WJY9tkiCxOEwAS67pFUBGQMtkE'  -o '%(autonumber)s%(id)s.%(ext)s'
```

### Guardar todo en un archivo mylist.txt para que ffmpeg pueda juntar los archivos
pueden usar este comando:
```bash
touch mylist.txt && for file in *.m4a ; do echo "file '$file'" >> mylist.txt ; done
```
OJO! Va m4a si descargaron archivos de audios pero si descargaron videos tienen que poner la extensión del video que bajaron, por ejemplo usando mp4 seria:
```bash
touch mylist.txt && for file in *.mp4 ; do echo "file '$file'" >> mylist.txt ; done
```

asi te tiene que quedar mylist.txt despues de agregar file ' al principio del nombre del archivo y la comilla al final del nombre del archivo
```bash
file 'file1.m4a'
file 'file2.m4a'
file 'file3.m4a'
```

Lo juntamos con:
```bash
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.m4a
```
OJO: Aca deberian poner m4a si bajaron archivos de audios como mencione anteriormente, sino ponen la extension del archivo de video que bajaron como por ejemplo mp4.
