---
title: "Conectar a dispositivo bluetooth en ArchLinux y transferir archivos."
date: 2025-03-22T14:27:39-03:00
tags: ['linux']
---
Actualmente levanto un Hotspot en Android me conecto desde la computadora y paso los archivos así (cuando no tengo Internet hago esto).

**Si queres transferir archivos tendras que instalar obex primero (explicado más abajo) y después levantar el servicio de bluetooth.** Si solo queres compartir audio podes hacer lo siguiente.

```bash
sudo pacman -S bluez bluez-utils bluez-obex bluez-tools
sudo systemctl start bluetooth
```

#### Levantamos el servicio obex

```bash
sudo systemctl start obex  # Si falla correlo como usuario 
systemctl status obex.service
systemctl status bluetooth.service

### Levantar obex como usuario

systemctl --user start --now obex.service
systemctl --user enable --now obex
systemctl --user status obex
```

### No es necesario: Para que bootee con bluetooth activado

```bash
sudo systemctl enable --now bluetooth.service # Si queres que bluetooth inicie en el boot.
sudo systemctl enable --now obex.service # Si queres que obex inicie en el boot. 
```

#### Nos conectamos a nuestro Android.

```bash
bluetoothctl
> power on
> agent on
> scan on
> devices
> pair MAC_ADDRESS
> connect MAC_ADDRESS
```

En caso de una mala conexión usar `disconnect MAC_ADDRESS`

#### Enviar archivos con `obexctl` (de ArchLinux a Android).

Start obexctl: `systemctl start --user obex` conectate con bluetoothctl (explicado más arriba). Y luego ejecutá:

```bash
obexctl
connect XX:XX:XX:XX:XX:XX
send /home/user/documents/my_file.txt
journalctl --user -u obex.service -f
```

#### Recibir archivo desde Android a la PC (antes tenes que estar conectado con bluetoothctl y tenes que tener el servicio de bluez-obex instalado e iniciado).

```bash
sudo pacman -S bluez-tools
bt-obex --auto-accept -s ~/Downloads
```
