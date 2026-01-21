---
layout: post
title: Usando MPV para mirar videos en PC's de bajos recursos, subir volumen a mas del maximo
tags: ['mpv','youtube']
categories: ['linux']
date: 2022-07-12T09:39:57-03:00
---
### Subir el volumen 
Yes, either by supplying --volume-max=300 as a command line argument, or by adding volume-max=300 as a line in your mpv.conf to make the change permanent. Ctrl+f volume-max in the mpv manual for the description of this option.

Baja resolución no implica menor consumo de ancho de banda pero si menor consumo de recursos. En vez de mirar el video en 360p si tenés una computadora lenta podés usar 480p AV1 o 480p VP9, el consumo de ancho de banda depende del codec usado.

No uses YouTube.com es muy pesado para computadoras viejas.
Lo mejor hoy en dia es usar yt-dlp (fork de youtube-dl).
YouTube-dl quedo obsoleto porque Google intenta hacer lo imposible para arruinarlo. Y la gente de yt-dlp hace lo imposible para que siga funcionando.
Luego tienen que combinar mpv con yt-dlp para poder mirar videos.
Ejemplo
```bash
mpv --ytdl-format=18 https://youtube...
```

La opcion 18 significa 480p pueden obtener una lista de formatos usando la opcion -F en yt-dlp
por ejemplo
```bash
yt-dlp -F URL_DEL_VIDEO
yt-dlp -f134+140 --write-thumbnail URL
```

Ojo: mpv usa el binario /usr/bin/youtube-dl pero ya esta obsoleto entonces lo que tienen
que hacer es instalar yt-dlp desde el [GitHub](https://github.com/yt-dlp/yt-dlp) y 
borrar el /usr/bin/youtube-dlp y crear un link de youtube-dl a yt-dlp algo como

Instalacion:
```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```
Linkeo de Youtube-al a yt-dlp para MPV:
```bash
cd /usr/bin
sudo ln -s /usr/local/bin/yt-dlp youtube-dl
```

Entonces cuando ejecuten mpv con la url de un video va a usar yt-dlp en vez de youtube-dl.

Otras alternativas son usar [yewtu.be](yewtu.be) que es una instancia de invidious o 
el cliente smtube en Linux que tambien usa mpv con yt-dlp pero tiene una interfaz grafica
mas rapida para buscar los videos que yewtu.be

Atajos para descargar el audio, el video desde ytfzf:
```console
download
       alt-d (download_shortcut)

watch video
       alt-v (video_shortcut)

audio only
       alt-m (audio_shortcut)

detatch
       alt-e (detach_shortcut)

print link
       alt-l (print_link_shortcut)

show formats
       alt-f (show_formats_shortcut)

show all info
       alt-i (info_shortcut)

new search
       alt-s (search_again_shortcut)
```
### Para ver más atajos `man ytfzf`

Espero que les haya servido.





##### Para abrir videos pegando la url en vez de escribir cada vez mpv
```bash
[I] esotericwarfare@arch ~> cat launch_mpv.sh
while true; do
	echo -n "mpv > "
	read url
	mpv $url > /dev/null &
done

[I] esotericwarfare@arch ~>
```
