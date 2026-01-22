---
title: "Modificar el layout del teclado en GNU/linux a español"
date: 2023-11-09T19:51:46-03:00
tags: ['layout','linux']
---
Generalmente yo uso el idioma del sistema operativo en ingles, así es más fácil googlear los errores y mi distribución de teclado español de españa.
En `/etc/X11/xorg.conf.d/00-keyboard.conf`
```console
# dpkg-reconfigure keyboard-configuration
# localectl --no-convert set-x11-keymap es pc104
# service keyboard-setup restart
```

O editalo manualmente modificando el archivo /etc/X11/xorg.conf.d/00-keyboard.conf
```console
# Read and parsed by systemd-localed. It's probably wise not to edit this file
# manually too freely.
Section "InputClass"
        Identifier "system-keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "es"
        Option "XkbModel" "pc105"
EndSection
```

O podés ejecutar el siguiente comando: `localectl --no-convert set-x11-keymap es pc104`

Si eso no funcinoa podes cambiar el archivo `/etc/default/keyboard`
```console
Manual configuration of keyboard
You can edit /etc/default/keyboard manually instead of running dpkg-reconfigure keyboard-configuration.

Here's an example:

# KEYBOARD CONFIGURATION FILE
# Consult the keyboard(5) and xkeyboard-config(7) manual page.

XKBMODEL="pc105"
XKBLAYOUT="us,de,fr,ua,ru"
XKBVARIANT=""
XKBOPTIONS="grp:alt_shift_toggle"
BACKSPACE="guess"
```

```bash
sudo apt-get purge locales;sudo apt-get install locales;export LANGUAGE=es_ES.UTF-8;export LANG=es_ES.UTF-8;sudo locale-gen es_ES.UTF-8;sudo localectl set-locale es_ES.UTF-8

```

```bash
$ sudo dpkg-reconfigure keyboard-configuration
$ setupcon
$ sudo update-initramfs -u
```

```bash
dpkg-reconfigure locales
```


[https://superuser.com/questions/646425/permanently-change-default-language-and-keyboard-settings-what-am-i-missing](https://superuser.com/questions/646425/permanently-change-default-language-and-keyboard-settings-what-am-i-missing)
[https://unix.stackexchange.com/questions/621053/xkb-keyboard-configuration-on-debian-system](https://unix.stackexchange.com/questions/621053/xkb-keyboard-configuration-on-debian-system)
