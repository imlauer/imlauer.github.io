---
title: "Controlar android desde terminal usando ADB"
date: 2023-04-20T23:01:04-03:00
tags: ['controlar','android','adb']
---

Primero tienen que conectar Android a la computadora a traves de un USB y activar el modo debugger en Android. Para hacer esto deben apretar 7 veces en Numero de compilacion que esta a lo ultimo en `Ajustes->Acerca del Telefono`, despues regresan al menu anterior y les aparecera un menu de opciones de programador entran ahi y activan el USB Debugging. Luego desconectan el USB.
Ahora instalan adb en Linux es simple 

#### Instalacion adb 
```bash
sudo apt install adb
```
Y ejecutan `adb devices`
Ahi les tiene que aparecer una codigo de su android para establecer una conexion a traves de LAN ejecutamos 
### Abrimos un puerto en Android para poder establecer la conexion
```bash
adb -s <CODIGO> tcpip 5555
```
Ahora si vuelven a ejecutar adb devices les aparecera la IP de su celular android con el puerto, ahora procedemos a conectarnos para luego poder enviar comandos.
#### Nos conectamos
```bash
adb connect 192.168.0.129:5555
```
### Reproducimos el audio en Android remotamente desde la PC
Si todo anduvo bien hasta aca, estamos conectados y podemos por ejemplo reproducir una cancion
```bash
adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Download/cancerslug_playlist.m4a -t audio/mp3
```
O abrir una imagen
```bash
adb shell am start -a android.intent.action.VIEW -d file:///storage/emulated/0/Pictures/Screenshots/2.png -t image/png
```

Tambien podemos controlar con que programa abrir el archivo con el parametro -n:
```bash
adb shell am start -a android.intent.action.VIEW -d file:///sdcard/<nombre del archivo de audio> -t audio/mp3 -n com.example.app/.ActivityName
```
Tienen que saber el ActivityName para saber eso pueden bajar la aplicacion "Activity Launcher" desde F-droid o la Play Store.

Necesitamos saber la ruta completa del archivo de audio, para saberla pueden bajar Files desde la F-droid en donde te la muestra.

#### Para subir bajar el volumen y darle play/pause
`adb shell input keyevent KEYCODE_VOLUME_DOWN`
`adb shell input keyevent KEYCODE_VOLUME_UP`
`adb shell input keyevent KEYCODE_VOLUME_PLAY`
`adb shell input keyevent KEYCODE_VOLUME_PAUSE`

```bash
KEYCODE_DPAD_UP: Pulsar la tecla de flecha hacia arriba en el D-pad.
KEYCODE_DPAD_DOWN: Pulsar la tecla de flecha hacia abajo en el D-pad.
KEYCODE_DPAD_LEFT: Pulsar la tecla de flecha hacia la izquierda en el D-pad.
KEYCODE_DPAD_RIGHT: Pulsar la tecla de flecha hacia la derecha en el D-pad.
KEYCODE_ENTER: Pulsar la tecla Enter.
KEYCODE_BACK: Pulsar la tecla de retroceso.
KEYCODE_HOME: Pulsar la tecla Inicio.
KEYCODE_MENU: Pulsar la tecla Menú.
KEYCODE_VOLUME_UP: Pulsar la tecla de subir volumen.
KEYCODE_VOLUME_DOWN: Pulsar la tecla de bajar volumen.
KEYCODE_MEDIA_PLAY: Pulsar la tecla de reproducción de medios.
KEYCODE_MEDIA_PAUSE: Pulsar la tecla de pausa de medios.
KEYCODE_MEDIA_PLAY_PAUSE: Pulsar la tecla de reproducción/pausa de medios.
KEYCODE_MEDIA_STOP: Pulsar la tecla de detener reproducción de medios.
KEYCODE_MEDIA_NEXT: Pulsar la tecla de siguiente de medios.
KEYCODE_MEDIA_PREVIOUS: Pulsar la tecla de anterior de medios.
```

[https://youtube.com/watch?v=qP3lMMaGp-A](https://youtube.com/watch?v=qP3lMMaGp-A)

