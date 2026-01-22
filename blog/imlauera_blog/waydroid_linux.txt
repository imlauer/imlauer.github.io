---
title: "Waydroid: Ejecutar aplicaciones Android en ArchLinux"
date: 2025-05-04T03:23:15-03:00
tags: ['linux']
---

Waydroid no es un emulador: 
> No, Waydroid is not a traditional Android emulator. It's a container-based approach that allows you to run a full Android system within a Linux container, rather than emulating it. Think of it as running a dedicated, isolated Android environment on top of your Linux host.

Hay que aprender a instalar los paquetes AUR manualmente porque a veces falla con `yay` en este caso me falló la compilación de `libgbinder` porque faltaba la CFLAG `-Wno-incompatible-pointer-types`

Si tenés suerte podés instalarlo con `yay` a mi no me sirvió y lo tuve que hacer manualmente:
```bash
sudo pacman -Syu
yay -S waydroid
```

###### Compilación manual de waydroid porque me falló `yay -S waydroid`
```bash
$ mkdir tools && cd tools
$ git clone https://aur.archlinux.org/libgbinder.git
$ git clone https://aur.archlinux.org/python-gbinder.git
$ git clone https://aur.archlinux.org/waydroid.git
$ ls
libgbinder/  python-gbinder/  waydroid/
$ cd libgbinder
$ vim PKGBUILD
```

En el `PKGBUILD` de `libgbinder` agregá:

```bash
build() {
  cd $pkgname-$pkgver
  export CFLAGS="-Wno-incompatible-pointer-types ${CFLAGS}" #added line
  make KEEP_SYMBOLS=1 release pkgconfig
}
```

```bash
$ makepkg -si
$ cd ../python-gbinder/
$ makepkg -si
$ cd ../waydroid
$ makepkg -si
```

##### Ahora que tenemos waydroid instalado:
Tenemos que tener instalado `linux-zen`:
```bash
pacman -Q | grep '^linux'
``` 

Si no lo tenemos lo instalamos de la siguiente forma:
```bash
sudo pacman -Syu linux-zen linux-zen-headers
sudo grub-mkconfig -o /boot/grub/grub.cfg
sudo waydroid init -f
sudo waydroid init -s GAPPS # Si querés GAPPS (es más lento) (Si ya ejecutaste el comando anterior agregá -f para forzar)
```

Si descargás GAPPS tenés que registrar tu Android acá: https://www.google.com/android/uncertified

```bash
sudo systemctl enable waydroid-container.service
sudo systemctl start waydroid-container.service
```

Editá el archivo `vim /var/lib/waydroid/waydroid.cfg` y agregá lo siguiente al final:
```
ro.hardware.gralloc=default
ro.hardware.egl=swiftshader
```
Luego ejecutá: `waydroid upgrade --offline`

###### Cambiá el ancho para que funcione más rápido XD.
```bash
$ waydroid prop set persist.waydroid.width 576
$ waydroid prop set persist.waydroid.height 1024
$ systemctl restart waydroid-container.service
```

#### Para actualizarlo
```bash
sudo waydroid upgrade
```

#### Iniciar la sección, mostrar la ventana, ingresar a la shell, listar aplicaciones, y abrir una.
```bash
waydroid session start
waydroid show-full-ui
waydroid shell
waydroid app list
waydroid app launch $package_name
```

---

#### Fuentes:
https://wiki.archlinux.org/title/Waydroid https://inv.nadeko.net/watch?v=4yCnutLzWyU

