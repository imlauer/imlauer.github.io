---
title: "Crear backup Windows10"
date: 2024-09-27T14:24:36-03:00
tags: ['windows','backup']
---
Universal backup: https://www.youtube.com/watch?v=tXGVzMUsuE4

https://www.youtube.com/watch?v=dwMr3ODbFIQ

https://rescuezilla.com/


#### Como crear backup de Windows desde Linux.
https://unix.stackexchange.com/questions/444019/how-can-i-clone-backup-restore-windows-10-from-linux
```bash
sudo sh -c 'pv < /dev/sda > /destination'
sudo -i
pv < /dev/sda > /BackupDestination
pv < /BackupDestination > /dev/sda

```

---

```bash
sdelete -z c:
Desde un USB live con linux:
dd if=/dev/sda of=/somewhere/file.mbr bs=512 count=63
dd if=/dev/sda1 bs=1M status=progress | lz4 > /somewhere/sda1.lz4
dd if=/dev/sda2 bs=1M status=progress | lz4 > /somewhere/sda2.lz4
dd of=/dev/sda if=/somewhere/file.mbr

Ahora restaure las dos particiones de Windows.
dd of=/dev/sda1 bs=1M status=progress < lz4cat /somewhere/sda1.lz4
dd of=/dev/sda2 bs=1M status=progress < lz4cat /somewhere/sda2.lz4 

bootrec /fixmbr

```


La solución más fácil es: `dd if=/dev/sda of="/media/usb/$(date).img"` pero es muy lento.
