---
title: "Arch: Unable to lock database"
date: 2025-03-13T21:08:42-03:00
tags: ['archlinux']
---
```bash
Last login: Thu Mar 13 21:06:24 on tty2
[I] esotericwarfare@arch ~> sudo pacman -Syy
:: Synchronizing package databases...
error: failed to synchronize all databases (unable to lock database)
```
#### Solución:
```
[I] esotericwarfare@arch ~ [1]> sudo rm -rf /var/lib/pacman/db.lck
```
