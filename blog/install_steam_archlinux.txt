---
title: "Install steam ArchLinux"
date: 2024-11-12T06:29:11-03:00
tags: ['games']
---
`sudo vim /etc/pacman.conf` y descomentá las líneas

```bash
[multilib]
Include = /etc/pacman.d/mirrorlist
```

Luego ejecutá: 

```bash
sudo pacman -Syu
sudo pamcan -S steam
```
