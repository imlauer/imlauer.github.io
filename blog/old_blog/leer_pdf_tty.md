---
title: "Leer pdf desde la TTY, configuración MPV y como hacer todo desde la TTY en el 2024 XD"
date: 2024-11-17T16:41:01-03:00
tags: ['framebuffer']
---
Ya expliqué [como mirar imágenes desde la TTY usando el navegador w3m](https://imlauera.github.io/how_to_play_videos_from_tty/) y descargá el PDF. Expliqué [como mirar videos de YouTube usando mpv y ytfzf (cuando usas MPV tenés que ejecutarlo sin tmux sino no podras moverte entre las demas TTY)](https://imlauera.github.io/post/2022-07-12-usando-mpv-para-mirar-videos-en-pc-s-de-bajos-recursos). También expliqué [como buscar torrents desde la consola con jackett y btstrm](https://imlauera.github.io/search_and_stream_torrents_cli/). Se puede usar MPV para mirar videos y para mirar imágenes. También ya expliqué [como abrir tmux al iniciar session en la TTY](https://imlauera.github.io/start_tmux_on_login/).

Esta es mi actual configuración de `/etc/mpv/mpv.conf`:

```bash
[I] esotericwarfare@arch ~> cat /etc/mpv/mpv.conf
--ytdl-raw-options="format=bestvideo[height<=?360]+bestaudio/best[height<=?360]/bestvideo[height<=?480]+bestaudio/best[height<=?480],write-auto-sub=,sub-lang=[en,ru],write-sub="
#--vo=drm
--profile=fast
--sub-auto=all
--ytdl-raw-options="format=233+230,write-auto-sub=,write-sub=,sub-lang=[en,ru]"
--volume-max=600
--save-position-on-quit
--mute=yes
--untimed
--profile=low-latency
```
Y este es mi `/etc/yt-dlp.conf`:

```bash
[I] esotericwarfare@arch ~> cat /etc/yt-dlp.conf
#--format=18
--write-auto-sub
--write-sub
--sub-lang=en,ru,es
--cookies-from-browser=chromium
[I] esotericwarfare@arch ~>
```


Leer pdf's desde la terminal: [https://bbs.archlinux.org/viewtopic.php?id=72913](https://bbs.archlinux.org/viewtopic.php?id=72913)


```bash
sudo pacman -S fbida # Instala fbi, fbgs, ida y exiftran
fbpdf /tmp/mipdf.pdf
```
---

### Como buscar en MercadoLibre desde la TTY.

```bash
curl "https://api.mercadolibre.com/sites/MLC/search?q=tu_busqueda" | jq . -C | less -R
```

## Con w3m podés mirar youtube desde Invidious poniendo mpv como el navegador por defecto en vez de usar firefox y apretando Shift+M al acceder a la URL del video.

O con w3m más o menos funciona XD. elinks y lynx tienen soporte de javascript y podés usar fbi y mpv para ver imágenes y videos. Elinks soporta un javascript básico, olvidate de una aplicación de ReactJS.

### Como mirar horarios F1 desde la Terminal.

Guardá este script en `~/scripts/f1exposure.sh`:

```bash
curl 'https://f1exposure.com/f1exposure/countdown?mode=0' \
                                  -H 'Accept: application/json, text/plain, */*' \
                                  -H 'Accept-Language: en-US,en;q=0.9,es;q=0.8' \
                                  -H 'Client: 36aed15c-f2ca-40a0-ae6d-96d82091df99' \
                                  -H 'Connection: keep-alive' \
                                  -H 'Content-Type: application/json' \
                                  -H 'Sec-Fetch-Dest: empty' \
                                  -H 'Sec-Fetch-Mode: cors' \
                                  -H 'Sec-Fetch-Site: same-origin' \
                                  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
                                  -H 'sec-ch-ua: "Chromium";v="131", "Not_A Brand";v="24"' \
                                  -H 'sec-ch-ua-mobile: ?0' \
                                  -H 'sec-ch-ua-platform: "Linux"'
```

Y agregá este alias a tu `.bashrc`:

```bash
alias f1="echo 'Los tiempos están en UTC. Coordinated Universal Time está 3 horas adelantado a Buenos Aires'; bash scripts/f1exposure.sh | jq ."
```

Luego ejecutá: `f1`
