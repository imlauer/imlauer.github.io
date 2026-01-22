---
title: "Grabar y streamear desde TTY (con la cámara)"
date: 2025-07-18T21:32:33-03:00
tags: ['linux']
---
Grabar archivo de video (al grabar de esta forma solo estás usando el procesador sin la tarjeta gráfica):


amixer set 'Internal Mic Boost' 50%-


```bash
ffmpeg -f fbdev -framerate 60 -i /dev/fb0 -f v4l2 -i /dev/video0 -f alsa -i pipewire -filter_complex "[1:v]scale=320:-1[cam];[0:v][cam]overlay=main_w-overlay_w-20:20" -c:v libx264 -preset ultrafast -pix_fmt yuv420p -c:a aac -b:a 128k -async 1 -ar 48000 -latency 100 prueba.mp4

```

---


```bash
ffmpeg -f alsa -i pipewire -f fbdev -r 60 -i /dev/fb0 mamita.mkv

ffmpeg -f alsa -i pipewire -f fbdev -r 60 -i /dev/fb0 mamita.mp4
```


```bash
ffmpeg -f fbdev -framerate 30 -i /dev/fb0 \
       -f v4l2 -i /dev/video0 \
       -f alsa -i pipewire \
       -filter_complex "[1:v]scale=320:-1[cam];[0:v][cam]overlay=main_w-overlay_w-20:20" \
       -c:v libx264 -c:a aac output.mkv
```


### Claude Code

```bash
ffmpeg -f alsa -i pipewire \
       -f fbdev -framerate 30 -i /dev/fb0 \
       -c:v libx264 -preset ultrafast -tune zerolatency -crf 23 \
       -threads 2 \
       -c:a aac -b:a 128k \
       -pix_fmt yuv420p \
       output.mkv
```

#### Con Webcam
```bash
ffmpeg -f fbdev -framerate 30 -i /dev/fb0 \
       -f v4l2 -framerate 15 -video_size 640x480 -i /dev/video0 \
       -f alsa -i pipewire \
       -filter_complex "[1:v]scale=240:-1[cam];[0:v][cam]overlay=main_w-overlay_w-10:10" \
       -c:v libx264 -preset ultrafast -tune zerolatency -crf 25 \
       -threads 2 \
       -c:a aac -b:a 128k \
       -pix_fmt yuv420p \
       output.mkv
```

### Este es el que uso funciona de maravilla. (Claude AI).

```bash
ffmpeg -f alsa -i pipewire \
       -f fbdev -framerate 15 -i /dev/fb0 \
       -c:v libx264 -preset ultrafast -crf 28 \
       -threads 2 \
       -c:a aac -b:a 96k \
       -s 1024x576 \
       output.mkv
```

#### `-s` no sirve
```bash
ffmpeg -f alsa -i pipewire \
       -f fbdev -framerate 15 -i /dev/fb0 \
       -filter_complex "[1:v]scale=1024:576[scaled]" \
       -map 0:a -map "[scaled]" \
       -c:v libx264 -preset ultrafast -crf 28 \
       -threads 2 \
       -c:a aac -b:a 96k \
       output.mkv
```


##### Para accelerar el video eliminar el audio 

```bash
ffmpeg -i output.mkv -vf "setpts=0.04*PTS" -an -c:v libx264 -preset slow -crf 28 output_acelerado.mkv

ffmpeg -i gentoo.mkv -vf "setpts=0.04*PTS" -an -c:v libx264 -preset ultrafast -crf 28 -threads 0 output_acelerado.mkv
ffmpeg -i output.mkv -vf "setpts=0.04*PTS,scale=854x480" -an -c:v libx264 -preset veryfast -crf 30 -threads 0 output_acelerado.mkv
ffmpeg -i output.mkv -vf "setpts=0.04*PTS" -an -c:v copy output_acelerado.mkv
```

-vf "setpts=0.04*PTS" - Acelera el video 25x (0.04 = 1/25). Tu video de 24 horas quedará en aproximadamente 58 minutos


#### ffprobe

```bash
ffprobe output.mkv 2>&1 | grep -E "Stream|Video:"
```


If CPU hits 100% constantly, the recording will stutter. Drop framerate to 20 or 15 if needed.
Your hardware is pretty limited - expect some trade-offs between quality and smoothness. Start with 30fps, and if it lags, drop to 20 or 15fps.

---


### Este es el comando que uso para grabar y tiene menos lag.

```bash
ffmpeg \
 -f fbdev -framerate 60 -i /dev/fb0 \
 -f v4l2 -i /dev/video0 \
 -f alsa -i pipewire \
 -filter_complex "[1:v]scale=320:-1[cam];[0:v][cam]overlay=main_w-overlay_w-20:20" \
 -c:v libx264 -preset ultrafast -pix_fmt yuv420p \
 -c:a aac -b:a 128k \
 -async 1 -ar 48000 -latency 100 \
 prueba.mp4
```

**peg-this (ffmpeg TUI)**:

```bash
python -m venv peg_this
source peg_this/bin/activate or source peg_this/bin/activate.fish (si usas fish)
pip install peg-this
peg_this
```


#### Amplify sound with ffmpeg.
```bash
# Lento
ffmpeg -i input.mp4 -af "volume=4.0" output.mp4
# Rapido pero no anda (es rapido porque copia)
ffmpeg -i input.m4a -c:a copy -af "volume=4.0" output.m4a
```


```bash
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -f v4l2 -framerate 60 -video_size 320x240 -i /dev/video0 -filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" -map "[outv]" -map 0:a -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/stream
```

### Para transmitir a YouTube:
#### Este funcionó bastante bien (sin cámara y con audio no se puede streamear sin audio en YouTube)
```bash
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k 
```

#### Transmitir solo la cámara a resolución HD podes ver la lista de resoluciones disponibles con el comando `v4l2-ctl --list-formats-ext`.
```bash
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/stream_key
```


##### Leer el chat en vivo: 
```bash
python -m venv chat-downloader
source chat-downloader/bin/active
pip install chat-downloader
chat_downloader "https://www.youtube.com/watch?v=TU_ID_DEL_VIDEO"
```

---

#### Camara y tty:
```bash
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -f v4l2 -framerate 60 -video_size 320x240 -i /dev/video0 -filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" -map "[outv]" -map 0:a -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/stream_key
```


##### Grabar video usando DRM (con kmscon), lo uso para capturar un navegador o un juego.
Para poder grabar kmscon sin sudo y grabar el audio:
```bash
sudo setcap cap_sys_admin+ep /usr/bin/ffmpeg
[esotericwarfare@arch ~]$ getcap /usr/bin/ffmpeg
/usr/bin/ffmpeg cap_sys_admin=ep
```

Y agrega sudo systemctl edit kmscon para arreglar colores de tmux 

Para iniciar kmscon : `sudo systemctl start kmscon`

```bash
# no deberias usar sudo porque no vas a poder grabar el audio si te putea ejecuta lo que está mas arriba.

ffmpeg \
    -f kmsgrab -device /dev/dri/card1 -i - \
    -filter_complex "[0:v]hwdownload,format=bgr0[screen]" \
    -f v4l2 -i /dev/video0 \
    -f alsa -i pipewire \
    -filter_complex "\
        [1:v]scale=320:-1[cam]; \
        [screen][cam]overlay=main_w-overlay_w-20:20,format=yuv420p[outv]" \
    -map "[outv]" -map 2:a \
    -c:v libx264 -preset ultrafast \
    -c:a aac \
    out.mkv


ffmpeg -f alsa -i pipewire -f kmsgrab -device /dev/dri/card1 -i - -vf 'hwdownload,format=bgr0' -c:v libx264 -preset ultrafast out.mkv

ffmpeg -f v4l2 -i /dev/video0 \
       -f alsa -i pipewire \
       -filter_complex "[1:v]scale=320:-1[cam];[0:v][cam]overlay=main_w-overlay_w-20:20" \
       -f kmsgrab -device /dev/dri/card1 -i - -vf 'hwdownload,format=bgr0' -c:v libx264 -preset ultrafast out.mkv 





# Si queres usar sudo acá tenés.

sudo ffmpeg -f kmsgrab -device /dev/dri/card1 -i - -vf 'hwdownload,format=bgr0' -c:v libx264 -preset ultrafast out.mkv

ffmpeg -device /dev/dri/card1 -f kmsgrab -framerate 30 -i - -vf 'hwdownload,format=bgr0' -c:v libx264 output.mkv

ffmpeg -device /dev/dri/card1 -f kmsgrab -framerate 30 -i - -vf 'hwmap=derive_device=vaapi,format=nv12,hwdownload,format=bgr0' -c:v libx264 output.mkv
ffmpeg -device /dev/dri/card1 -f kmsgrab -framerate 30 -i - -vf 'hwmap=derive_device=vaapi,format=nv12,hwdownload,format=bgr0' -c:v libx264 output.mkv

Si tu hardware soporta VAAPI, podés ganar rendimiento cambiando -c:v libx264 por -c:v h264_vaapi.

sudo setcap cap_sys_admin+ep $(which ffmpeg)

```

Para bajar el volumen del micrófono: bajá el volumen `Internal Mic B` en `alsamixer` y `Mic Boost` y `Mic`.

##### Capturar pantalla desde Wayland y streamerlo a YouTube

```bash
ffmpeg -f pipewire -framerate 30 -video_size 1920x1080 -i @DEFAULT_VIDEOSOURCE@ \
-f pulse -i default \
-c:v libx264 -preset veryfast -b:v 4500k -c:a aac -b:a 128k -f flv \
"rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY"

```

#### Capturar pantalla con cámara.

```bash
ffmpeg -f pipewire -framerate 30 -video_size 1920x1080 -i @DEFAULT_VIDEOSOURCE@ \
-f pulse -i default \
-f v4l2 -framerate 60 -video_size 640x480 -i /dev/video0 
-filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" -map "[outv]" -map 0:a 
-c:v libx264 -preset veryfast -b:v 4500k -c:a aac -b:a 128k -f flv \
"rtmp://a.rtmp.youtube.com/live2/YOUR_STREAM_KEY"
``` 

###### Cuando arranco stream siempre tengo que bajar el Internal Mic desde alsamixer porque sino el micrófono se satura.


#### Este es el script que uso para streamear desde la TTY stream.sh

```bash
#!/bin/bash
sudo chmod 666 /dev/input/event*
amixer set 'Internal Mic Boost' 50%-


falkon "https://www.youtube.com/live_dashboard"
### Solo tty
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/STREAM_KEY 2> /dev/null
```


#### Este es el script que uso stream.sh

```bash
#!/bin/bash
sudo chmod 666 /dev/input/event*
amixer set 'Internal Mic Boost' 50%-


#falkon "https://www.youtube.com/live_dashboard"
### Solo tty
#ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -async 1 -ar 48000 -latency 100 -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null


#### Camara con tty
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -f v4l2 -framerate 60 -video_size 320x240 -i /dev/video0 -filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" -map "[outv]" -map 0:a -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null

### Solo camara
#ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null
```


Para poder streamear falkon, angelfish o qutebrowser desde la TTY usa:

```bash
export QT_QPA_PLATFORM=linuxfb
export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist --disable-gpu"
```

Para verificar si está transmitiendo: 

```bash
mpv "https://www.youtube.com/channel/CHANNEL\_ID/live"
```



#### Wayland (stream)

``` 
ffmpeg \
    -f alsa -i pipewire \
    -thread_queue_size 1024 \
    -f pipewire -i pipewire \
    -f v4l2 -framerate 60 -video_size 320x240 -i /dev/video0 \
    -filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" \
    -map "[outv]" -map 0:a \
    -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p \
    -c:a aac -b:a 128k \
    -f flv -bufsize 1000k <TU_URL_RTMP>

``` 

#### Wayland (record)

```bash
ffmpeg \
    -f pipewire -i pipewire \        # captura de pantalla
    -f v4l2 -framerate 30 -video_size 1280x720 -i /dev/video0 \  # cámara
    -f alsa -i pipewire \            # audio del sistema (opcional)
    -filter_complex "[1:v]scale=320:240[cam];[0:v][cam]overlay=W-w-20:H-h-20[out]" \
    -map "[out]" -map 2:a \
    -c:v libx264 -preset veryfast -pix_fmt yuv420p \
    -c:a aac -b:a 128k \
    output.mp4

```

#### Grabar audios y subirlo a YouTube

```bash

#!/bin/sh
if [ $# -eq 0 ]
  then
    echo "Poné el nombre de archivo sin extension en el primer argumento"
    exit;
fi

sudo chmod 666 /dev/input/event*
amixer set 'Internal Mic Boost' 50%-


ffmpeg -f alsa -i pipewire $1.m4a
#ffmpeg -f alsa -i pulse $1.m4a



echo "Nombre de archivo $1.m4a"

echo "Generamos thumbnail para youtube"
echo "Uso el titulo del video como el nombre del audio lo mismo para el thumbnail porque no se pueden subir audios a YouTube"
echo "Gerando thumbnail..."
thumbnailg $1 "/tmp/$1.png"
echo "Creando un video a partir del audio..."
ffmpeg -i "/tmp/$1.png" -i "$1.m4a" -c:v libx264 -tune stillimage -c:a copy "/tmp/$1.mp4"

fail=1

while ((fail==1)); do
  source $HOME/youtube-upload/bin/activate
  $HOME/youtube-upload/youtube-upload/bin/youtube-upload \
    --title="$1" \
    --description="$1" \
    --recording-date="2011-03-10T15:32:17.0Z" \
    --default-language="es" \
    --default-audio-language="es" \
    --privacy="unlisted" \
    --embeddable=True "/tmp/$1.mp4" | tee -a urls
  
  fail=0;
  (($? != 0)) && echo "Falló la carga" && echo "Lo intentamos de nuevo?[y/n]" && read respuesta && ((respuesta=="y")) && fail=1
done
```



```bash
#!/bin/sh
if [ $# -eq 0 ]
  then
    echo "Poné el nombre de archivo sin extension en el primer argumento"
    exit;
fi

ffmpeg -f alsa -i pipewire $1.m4a
#ffmpeg -f alsa -i pulse $1.m4a

echo "Nombre de archivo $1.m4a"

echo "Generamos thumbnail para youtube"
echo "Uso el titulo del video como el nombre del audio lo mismo para el thumbnail porque no se pueden subir audios a YouTube"
echo "Gerando thumbnail..."
thumbnailg $1 "/tmp/$1.png"
echo "Creando un video a partir del audio..."
ffmpeg -i "/tmp/$1.png" -i "$1.m4a" -c:v libx264 -tune stillimage -c:a copy "/tmp/$1.mp4"

source $HOME/youtube-upload/bin/activate
$HOME/youtube-upload/youtube-upload/bin/youtube-upload \
  --title="$1" \
  --description="$1" \
  --recording-date="2011-03-10T15:32:17.0Z" \
  --default-language="es" \
  --default-audio-language="es" \
  --privacy="unlisted" \
  --embeddable=True "/tmp/$1.mp4"
```
