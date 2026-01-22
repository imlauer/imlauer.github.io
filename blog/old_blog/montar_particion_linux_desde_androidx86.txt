---
title: "Montar particion Linux desde Androidx86 (o BlissOS, PrimaOS, Phoenix OS)"
date: 2025-05-10T03:53:05-03:00
tags: ['linux']
---
En Androidx86 para montar una partición de Linux tenes que usar `/dev/block` no `/dev` de la siguiente manera:
```bash
/system/bin/su
busybox mkdir /mnt/archlinux
busybox mount /dev/block/sda1 /mnt/archlinux
export PATH="/usr/bin:/bin:$PATH"
busybox chroot /dev/block/sda1 /bin/bash
```

Podés leer en `como recuperar el grub de debian` una entrada que se encuentra en mi blog para saber más.
