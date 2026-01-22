---
layout: post
title: Intercambiando canales de audio en PulseAudio
tags: ['canales de audio', 'pulseaudio']
categories: ['linux']
date: 2021-02-27T17:57:57-03:00
---

Editar el archivo: `/usr/share/pulseaudio/alsa-mixer/profile-sets/default.conf`

y en la línea:

```bash
[Mapping analog-stereo]
device-strings = front:%f hw:%f
channel-map = left,right
```

Cambiar channel-map a right,left.

Luego basta con reiniciar pulseaudio, con `pulseaudio -k`
