---
title: "Como recuperar archivos de audio corruptos"
date: 2024-07-25T20:24:37-03:00
tags: ['audio','recuperar','corruptos','archivos']
---
### Si tenés algún archivo de audio corrupto ¡NO LO BORRÉS!

Descargá faad, faac, un editor de hexadecimal o podés usar VIM.
### GNU/Linux:

`sudo apt install -y faad faac hexedit`
`sudo pacman -S faad faac`

### Windows:
En Windows tendrás que bajar manualmente cada programa y ponerlos todo en la misma carpeta junto con los archivos de audio a recuperar.
Descargá faad y faac acá:
https://rarewares.org/aac-decoders.php
Descargá un editor hexadecimal para Windows:
[http://download.cnet.com/HxD-Hex-Editor/3000-2352_4-10891068.html](http://download.cnet.com/HxD-Hex-Editor/3000-2352_4-10891068.html) o [http://mh-nexus.de/en/downloads.php?product=HxD](http://mh-nexus.de/en/downloads.php?product=HxD)
Extraelo y ejecutá setup.exe y para instalarlo.


Abrí el audio con VIM o con tu editor hexadecimal (yo lo hice con VIM) buscá la palabra mdat y borrá todo lo que está detrás de esa palabra incluyendo la palabra. En VIM lo podemos hacer con `/mdat` seleccioná todo con situá el cursor en la t de mdat apretá v-gg-x guardá el archivo con Escape:wq
![/img/find_mdat.png](/img/find_mdat.png)

#### Decodificamos usando faad
Ahora ejecutá `faad nombre_del_audio_corrupto.m4a` te generará un archivo wav fijate si ya podés escucharlo.

#### Codificamos usando faac, y recuperamos el archivo m4a.
`faac -b 160 -o repaired.m4a "nombre_del_audio_corrupto.wav"`

##### Para unir dos archivos de audio:
Lee el final de esta publicación: https://imlauera.github.io/post/download_and_concat/

Listo :)

