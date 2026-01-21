---
title: "Freenet, ZeroNet"
date: 2025-11-17T05:05:18-03:00
---
```bash
cd Downloads
mkdir freenet
w3m https://www.hyphanet.org/index.html Download for Linux
java -jar new_installer_offline_1503.jar

Select folder> Downloads/freenet

sh run.sh start
``` 

Si todo funcionó bien, 

```bash
ss -tanp
```

Deberías ver el puerto :8888 abierto. En mi caso tuve que cambiar cerrar SearXNG que usaba el mismo puerto.

Ahora prueba ingresar a este sitio:

* [FreeNet: A la mierda copyright](http://127.0.0.1:8888/USK@NiPBeAA-PpA715zb8Jc~Q-ohFbKPt8Mo-YiH~w1D56A,--ZTBvgu7XMdX0QUJGBHp-Hogoh0AQK1p8WoY6IR80Q,AQACAAE/lawiki/5/)

