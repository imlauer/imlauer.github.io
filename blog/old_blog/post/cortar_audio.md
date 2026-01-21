---
title: "Cortar audio"
date: 2024-09-08T03:01:20-03:00
tags: ['ffmpeg']
---
This works for me

`ffmpeg -ss 60 -i input-audio.m4a -t 15 -c copy output.m4a`

* `-ss` 60 means, "start from second 60"
* `-t` 15 audio output length in seconds.. in this case, 15 seconds..

o

`ffmpeg -ss 17:00 -i input.m4a output.m4a`

Donde 17 son minutos.
