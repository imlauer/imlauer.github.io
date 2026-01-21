---
title: "Como mirar videos desde la TTY (how to play videos from tty) y ver imágenes desde ranger con MPV"
date: 2024-11-02T22:16:20-03:00
tags: ['framebuffer']
---

Esto se puede hacer a través de direct rendering manager, y mpv tiene una opción gpu que te permite ver un video desde la TTY.

```bash
mpv --vo=drm filename.mp4
mpv --vo=gpu filename.mp4
```

Además de eso se puede usar el framebuffer que fue removido de mpv, tenés que compilarlo con esa funcionalidad.

Agregá eso a `/etc/mpv/mpv.conf`


Desde ranger con r se configura con que archivo querés abrir la imágen.


En el archivo `.config/mpv/rifle.conf` 

```bash
mime ^image, has mpv, X, flag f = /usr/bin/mpv -profile image -- "$@"
```


#### En `~/.config/ranger/rc.conf`
```bash
set preview_images true
set preview_images_method  w3m-img
```


```bash
mime ^video|audio, has mpv, flag f = mpv -- "$0"
```

##### Lo ideal es no usar la mierda de ranger, solo navegando a través de la consola y ejecutando mpv.


**ES POSIBLE VER IMÁGENES DIRECTAMENTE DESDE W3M EN LA TTY Y USAR RANGER PARA QUE ABRA LA IMAGEN CON W3M**

Abrí `w3m asdf.org` apretá o y buscá `Use external image viewer` y desactivalo, eso es todo. 

Apretá "=" para ver la información de la imágen.


Fuente: https://forums.freebsd.org/threads/image-viewer-for-the-console.66672/
