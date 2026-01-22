---
title: "League of legends linux"
tags: ['league']
---
Tenés que instalar Wild Rift para poder porque llegó un anticheat que se ejecuta a nivel kernel es decir, no te deja jugar el juego si no tiene el control total de tu computadora, está probado que este tipo de anticheat no es eficiente.

Instalá waydroid En kali:

```bash
sudo apt install curl ca-certificates -y
curl -sSL https://repo.waydro.id -o wd.sh
sudo bash wd.sh trixie
sudo apt install waydroid
sudo waydroid init
reboot
```

---

Ahora iniciá el contenedor de waydroid:
```bash
sudo apt install -y weston
systemctl start waydroid-container
```

--- 

`vim /usr/bin/startweston` pegamos: 

```bash
weston &
```
Luego abrí una terminal y ejecutá: 

```bash
export WAYLAND_DISPLAY=wayland-1              
sleep 2
waydroid show-full-ui &
```

Si tenés lightdm o sino pone en el .xinitrc `startdwm &` y listo.
`sudo vim /usr/share/xsessions/weston.desktop`

```bash
[Desktop Entry]
Version=1.0
Name=WESTON
Comment=Use this session to run DWM as your desktop environment
Exec=startweston
Icon=
Type=Application
```

Ahora iniciá weston desde lightdm.


No pude instalar el juego me decía "Aplicación no instalada", acá está como borrar esta basofia:

```bash
Stop the Waydroid session: sudo waydroid session stop
Stop the Waydroid container: sudo waydroid container stop
Remove the Waydroid package: sudo apt remove waydroid
Delete the Waydroid directories: sudo rm -rf /var/lib/waydroid /home/.waydroid ~/waydroid ~/.share/waydroid ~/.local/share/applications/*aydroid* ~/.local/share/waydroid

problem solve
```
