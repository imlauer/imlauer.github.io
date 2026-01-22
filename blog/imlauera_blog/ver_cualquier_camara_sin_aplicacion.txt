---
title: "Ver cualquier cámara sin aplicación móvil sólo con MPV"
date: 2025-01-02T17:50:43-03:00
tags: ['camera']
---
Primero tenemos que saber cual es la IP de la cámara para eso podemos bajarnos una aplicación de visor de cámaras en el celular o escanear las IPs con nmap o con un escaner de IPs en Windows como Advanced IP Scanner.

Cuando identificamos la IP de la cámara, tenemos que saber su usuario y contraseña para saber esta información si tendremos que bajar la aplicación pero solo 1 vez.

Podemos escanear la red con nmap en busca de cámaras así: `nmap -sP 192.168.0.0/24`
Luego `nmap -sS IP` para saber si esa es la cámara: generalmente tienen los puertos 554 (rtsp) abierto. 

Ahora desde la aplicación de celular en configuración avanzada al conectarse a la cámara encontraremos el usuario y contraseña.

Luego ejecutamos `mpv rtsp://usuario:clave@IP_CAMARA:PUERTO(554)`

Y así vamos a poder ver la cámara pero **no podremos enviar comandos como rotar**, en otro tutorial explicaré como hacer eso.
