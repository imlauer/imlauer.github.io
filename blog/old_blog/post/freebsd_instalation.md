---
title: "Instalación y configuración inicial de FreeBSD" 
date: 2023-11-10T04:52:12-03:00
tags: ['instalacion','configuracion','freebsd']
---
#### Instalar freebsd, configuración inicial, instalar xfce

[https://youtube.com/watch?v=Jg4YW-8Xr_g](https://youtube.com/watch?v=Jg4YW-8Xr_g)  
[https://youtube.com/watch?v=SQxReyTmtiE](https://youtube.com/watch?v=SQxReyTmtiE)  
[https://youtube.com/watch?v=ObQTHyvcdQ0](https://youtube.com/watch?v=ObQTHyvcdQ0)

```
su
pkg update
pkg install xorg
pkg install xfce xfce4-goodies
pkg install slim (no es necesario es la pantalla de login)
pkg install dbus
```

Editá /etc/rc.conf
```
dbus_enable="YES"
#slim_enable="YES"
```
Editá .xinitrc
```
exec xfce4-session
```
Ahora ejecutá `startx`

```
service dbus start
service slim start
```

```
pkg install openbox obconf kickshaw
```

Editá .xinitrc

```
exec openbox
```

```
kickshaw-gtk2
```


### Agregar wifi
`ifconfig` para ver cual es tu interfaz

```
dmesg | more (para buscar tu interfaz wifi)
ifconfig wlan0 create wlandev bwn0
ifconfig (para comprobar)
```

Ahora editamos `/etc/rc.conf`
```
ifconfig_bge0="inet 10.148.86.14 netmask 255.255.248.0"
defaultrouter="10.148.86.1"
wlans_bwn0="wlan0"
ifconfig_wlan="WPA DHCP"
```

Ejecutamos `wpa_passphrase tucontraseña_de_wifi >> /etc/wpa_supplicant.conf`

```
service netif restart (me acuerdo cuando ejecutaba este comando y me daba un panic)
ifconfig
```


### instalar wifi, powerd
El driver nativo de rtw88 de freebsd no me funcionó bien, el wifi se desconectaba después de unos minutos. La solución fue instalar WiFiBox [https://forums.ghostbsd.org/viewtopic.php?f=64&t=2578&sid=8d568e99cbd80762de39a23c6436ce62](https://forums.ghostbsd.org/viewtopic.php?f=64&t=2578&sid=8d568e99cbd80762de39a23c6436ce62) 

Y deshabilité la opción de background_dhclient en el /etc/rc.conf

#### Administración de la energía en FreeBSD
[https://forums.freebsd.org/threads/freebsd-13-0-and-cpu-power-management.82096/](https://forums.freebsd.org/threads/freebsd-13-0-and-cpu-power-management.82096/)

```bash
powerd_enable="YES"
```

Después de agregar esto a mi `/etc/rc.conf` aumentó muchísimo el rendimiento de mi laptop pero levantaba mucha temperatura cuando compilaba algo llegaba hasta 75º que lo solucioné con el siguiente parámentro en rc.conf:

```bash
powerd_flags="-a adp -n adp -i 75 -r 96 -m 500 -p 125 -N"
```
Luego de agregar eso y reiniciar al compilar no pasaba los 60º

Activa la webcam y ajustá el brillo:
```bash
kld_list="cuse acpi_video"
```
Luego en `/etc/rc.local` agregan: `sysctl hw.acpi.video.lcd0.brightness=10`

### compilar dwm st dvtm
[https://forums.freebsd.org/threads/solved-setting-up-dwm-in-freebsd.81729/](https://forums.freebsd.org/threads/solved-setting-up-dwm-in-freebsd.81729/)

Tenes que reemplazar las siguientes ubicaciones en el archivo config.mk

```bash
X11INC = /usr/X11R6/include                      ->          X11INC = /usr/local/include
X11LIB = /usr/X11R6/lib                          ->          X11LIB = /usr/local/lib
FREETYPEINC = /usr/include/freetype2             ->          FREETYPEINC = /usr/local/include/freetype2
```
Luego lo típico `sudo make clean install`

#### instalar docker en una maquina virtual con alpine en freebsd
[https://youtube.com/watch?v=ZVkJZJEdZNY](https://youtube.com/watch?v=ZVkJZJEdZNY)

#### autotools en freebsd
[https://people.freebsd.org/~rafan/ph/using-autotools.html](https://people.freebsd.org/~rafan/ph/using-autotools.html)
#### Habilitar cámara en freebsd
[https://www.davidschlachter.com/misc/freebsd-webcam-browser#:~:text=Load%20it%20at%20boot%20by,webcamd_0_flags%3D%22%2Dd%20ugen0.](https://www.davidschlachter.com/misc/freebsd-webcam-browser#:~:text=Load%20it%20at%20boot%20by,webcamd_0_flags%3D%22%2Dd%20ugen0.)

