---
title: "2 routers 1 red doméstica: Deshabiliten el DHCP en el 2do router"
date: 2023-10-13T00:23:16-03:00
tags: ['networking','dhcp']
---
https://youtube.com/watch?v=nOitxBangvk

[![Watch the video](https://img.youtube.com/vi/nOitxBangvk/hqdefault.jpg)](https://www.youtube.com/embed/nOitxBangvk)


En el router Thomson tenés que ir a Red Hogareña - Interfaces - Local Network - Configuración y deshabilitar el DHCP, pero ojo esto solo deshabilita el DHCP a nivel WiFi si conectás un dispositivo a través de Ethernet seguirás teniendo una IP en esa interfaz por ejemplo: 192.168.1.123 en vez de 192.168.0.123.

Así que para encontrar tu dispositivo conectado a través de Ethernet al segundo router, tendrás que conectarte a la WiFi pero configurar IP estática y usar el la puerta de enlace (gateway) de tu segundo router en mi caso es: 192.168.1.254 y configurar una IP en esa interfaz es decir : 192.168.1.123 no tendrás acceso a internet, pero podrás ver el dispositivo.
