---
title: "Buscando links rotos en Archive.org"
date: 2025-07-26T02:45:18-03:00
tags: ['hacking']
---
Quise instalar cstrike desde el AUR pero me encontré con el que el link estaba roto: 

Este era el link del juego `cstrike1.6`:
https://de.linuxgame.cn/%E5%8F%8D%E6%81%90%E7%B2%BE%E8%8B%B1/cstrike_1.6_i386.appimage

Con este comando verificamos si el ese link está archivado en https://archive.org:
```bash
curl -s -I https://web.archive.org/web/*/de.linuxgame.cn/%E5%8F%8D%E6%81%90%E7%B2%BE%E8%8B%B1/cstrike_1.6_i386.appimage
```

Si nos retorna `200 o 301` lo tenemos. Ahora necesitamos el link para descargarlo, lo obtenemos de la siguiente manera:

```bash
$ curl -s "http://archive.org/wayback/available?url=URL" | jq '.archived_snapshots.closest.url'

$ curl -s "http://archive.org/wayback/available?url=de.linuxgame.cn/%E5%8F%8D%E6%81%90%E7%B2%BE%E8%8B%B1/cstrike_1.6_i386.appimage" | jq '.archived_snapshots.closest.url'
```

Ahora descargamos el appimage con el resultado obtenido:
```bash
wget "http://web.archive.org/web/20241205202654/https://de.linuxgame.cn/%E5%8F%8D%E6%81%90%E7%B2%BE%E8%8B%B1/cstrike_1.6_i386.appimage"
```
