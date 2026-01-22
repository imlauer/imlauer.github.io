---
title: "Crear Stream de audio, radio digital usando icecast darkice"
date: 2023-04-30T17:12:55-03:00
tags: [radio,digital,stream,audio]
categories: [command line tool,radio,audio,stream]
---

No necesitan usar SoundWire ni pagar la version premium 
### Instalar icecast y darkice
Resumidamente IceCast crea el servidor y darkice transmite el audio a ese servidor.
En este caso veremos como podemos transmitir el audio interno de tu computadora a la red LAN (se puede hacer a traves de internet tambien)

Primero, se instalará un servidor de streaming.

Instalar icecast2 (`sudo apt install icecast2`).
Editar el fichero `/etc/icecast2/icecast.xml` para escuchar en todas las IP del PC, descomentando y poniendo:
#### Configurar icecast
```bash
<bind-adress>0.0.0.0</bind-adress>
```
Asi me quedo esa parte a mi:
```bash
<hostname>192.168.0.201</hostname>
<!-- You may have multiple <listen-socket> elements -->
<listen-socket>
<port>5553</port>
<bind-address>0.0.0.0</bind-address>
<shoutcast-mount>/stream</shoutcast-mount>
</listen-socket>
```

Yo cambie el puerto a 5553 y en el hostname puse mi IP local

Arrancar icecast2 con:
`sudo /etc/init.d/icecast2 restart`
O si usan systemd:
`sudo systemctl restart icecast2.service`

A continuación, instalamos un módulo para servir el audio local (pulse) como si fuese un mp3.

#### Instalar darkice
`sudo apt install darkice`
Crear el fichero ~/darkice.cfg con el siguiente contenido:
```bash
[general]
duration = 0 # duration in s, 0 forever
bufferSecs = 1 # buffer, in seconds
reconnect = yes # reconnect if disconnected
[input]
device = pulse # for Pulseaudio
sampleRate = 44100 # sample rate 11025, 22050 or 44100
bitsPerSample = 16 # bits
channel = 2 # 2 = stereo
[icecast2-0]
bitrateMode = vbr # variable bit rate (cbr for constant)
quality = 1.0 # 1.0 is best quality
format = mp3 # format
bitrate = 256 # bitrate
server = localhost # or IP
port = 5553 # port for IceCast2 access
password = hackme # source password to the IceCast2 server
mountPoint = mystream.mp3 # mount point on the IceCast2 server or any name
name = mystream
```

Arrancar el módulo darkice con:
`darkice -c ~/darkice.cfg` (sin root)

Podemos comprobar que el servidor icecast2 y el módulo funcionan, dirigiendo el navegador a http://192.168.0.201:5553 y ver que hay montado un stream llamado mystream.mp3 (a través de darkice) si no aparece es porque fallo darkice.

**OJO**: Yo tuve un problema con pulseaudio lo solucione moviendo la carpeta $HOME/.config/pulse a $HOME/.config/pulse.old con el comando mv.
Luego ejecute
```bash
systemctl --user status pulseaudio.service
pulseaudio --start
pulseaudio --check
```
#### Reproducimos musica 

Ponemos podes escuchar musica desde el navegador o desde mpv. Por último, configuramos el audio en pulse audio. Ejecutamos en una consola `pavucontrol`. Nos aseguramos de que:

Recording (Grabación): Deberíamos ver la aplicación "darkice" si no se ve nada hubo un problema con darkice no esta ejecutando porque hubo un problema de configuracion.
Input Devices (Dispositivos de entrada): Miramos que aparezca el que seleccionamos para darkice pidiendo que muestre todos los dispositivos y nos aseguramos que no esté en mute.
Por último, desde tu Android baja mpv o VLC accede al ip del servidor de stream de audio en mi caso http://192.168.0.201:5553 y apreta en donde dice M3U y lo abris con MPV luego pones Play in background que esta en el menu de engranaje.


Basado en  : [https://www.sing-group.org/~lipido/blog/2012/01/10/hacer-streaming-de-spotify-en-ubuntu-1104-con-icecast2-darkice-y-pulseaudio/](https://www.sing-group.org/~lipido/blog/2012/01/10/hacer-streaming-de-spotify-en-ubuntu-1104-con-icecast2-darkice-y-pulseaudio/)
