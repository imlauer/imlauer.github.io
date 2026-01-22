---
title: "Cambiar letra TTY y resolucion."
date: 2024-11-03T22:55:16-03:00
tags: ['tty']
---

https://adeverteuil.github.io/linux-console-fonts-screenshots/

```bash
cd /usr/share/kbd/consolefonts
setfont latarcyrheb-sun32
sudo setfont LatGrkCyr-12x22



o

sudo setfont ter-p20b.psf.gz

sudo setfont iso02-12x22.psfu.gz

```

En `/etc/vconsole.conf` tenés que agregar:

```bash
FONT=latarcyrheb-sun32
```

Antes usaba latarcyrheb-sun16 pero era muy chica y sun32 es muy grande asi que tuve que cambiar la resolucion de mi GRUB y usar la letra mas chica.


Si estás usando framebuffer (ves colores o logos al arrancar), podés cambiar la resolución del framebuffer, lo que escala la fuente sin cambiarla: explicado acá:  https://imlauera.github.io/post/2021-01-08-cambiando-la-resolución-de-tty

