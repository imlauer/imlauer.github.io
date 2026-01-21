---
title: "Mirar peliculas en la PS2"
date: 2025-01-22T05:45:10-03:00
tags: ['PS2']
---
La playstation reproduce mp4 como un audio, no tiene los codecs, así que hay que convertirlo a avi y no admite videos en 720p hay que bajar la resolución. Admite 360p,
creo que 480p también y 880x495. Más alto que eso no, salvo que tengas un gadget que hace que la salida sea HD.

Podés bajarte un canal de YouTube entero, luego juntarlos todos en un archivo y pasarlos a avi. Probé con un video de 900 megas y de 2 horas y funcionó.

Algo así:
```bash
yt-dlp -f134+140 "https://youtube.com/channel/UCT..." -o '%(autonumber)s%(id)s.%(ext)s'
```
Tengo una [publicación](https://imlauera.github.io/post/download_and_concat/
) en donde explico como juntar varios archivos en uno.
```bash
ffmpeg -i input.mp4 -vf scale="880:495" output.avi
```

Si tenés NVIDIA que soporta acceleración CUDA podés usar el siguiente comando:

```bash
ffmpeg -hwaccel cuda -hwaccel_output_format cuda -i "input_file.mp4" -c:a copy -vf "scale_cuda=880:495" -c:v h264_nvenc "output_file.mp4"
```
