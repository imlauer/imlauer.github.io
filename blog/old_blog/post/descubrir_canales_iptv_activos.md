---
title: "Descubrir canales iptv activos"
date: 2023-11-10T04:51:41-03:00
tags: ['iptv']
---
Si googlean iptv list m3u se encontrarán con listas de url de canales enormes, en vez de probar 1 por 1 pueden guardar la lista en un archivo y recorrerla con el siguiente comando:

```
for url in $(cat iptv_list.txt); do mpv --script-opts=iptv=1 $url; done
```
Ojo: Necesitan instalar iptv mpv que lo bajan acá: [https://github.com/gthreepw00d/mpv-iptv](https://github.com/gthreepw00d/mpv-iptv)

Probablemente se puede utilizar ese script para buscar canales de una forma mas eficiente.
