#!/bin/sh
if [ $# -eq 0 ]
  then
    echo "Poné el nombre de archivo sin extension en el primer argumento"
    exit;
fi

ffmpeg -f alsa -i pipewire $1.m4a

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

