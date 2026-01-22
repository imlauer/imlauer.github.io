---
title: "Msys2 windows"
date: 2025-11-03T17:27:43-03:00
tags: ['windows']
---
Yo nunca usaría Windows pero cuando tengo que usarlo uso msys2

Instale esto en Windows 10 me pareció interesante: https://www.msys2.org/

Tiene `pacman` instale `w3m` y `vim` y puse `mpv` como mi navegador por defecto (no instalé `mpv` desde `msys2` con `pacman`), `mpv` ya lo tenia de antes con `yt-dlp` y con esta configuración:

Establecí `/c/Mpv/mpv.exe` como navegador externo en `w3m`.

```bash
$ cd /c/Users/ttt/AppData/Roaming/mpv/

ttt@LIVING UCRT64 /c/Users/ttt/AppData/Roaming/mpv
$ dir
mpv.conf

ttt@LIVING UCRT64 /c/Users/ttt/AppData/Roaming/mpv
$ cat mpv.conf
--ytdl-raw-options="format=bestvideo[height<=?720]+bestaudio/best[height<=?720]/bestvideo[height<=?720]+bestaudio/best[height<=?720],write-auto-sub=,sub-lang=[en,ru],write-sub="
```

Lo anclé a la barra de tareas. (No uso Windows ni lo tengo instalado en mi computadora).
