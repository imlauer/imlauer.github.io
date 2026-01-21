---
title: "Instalar impresora compartida de Windows en GNU/Linux"
date: 2024-07-08T07:01:37-03:00
tags: ['impresora','linux']
---
Para que todo esto funcione tenés que compartir la impresora con contraseña.

```bash
smbclient "//192.168.0.203/HP PSC 1400 series"
sudo apt install -y cups
sudo apt install -y hplip hplip-gui printer-driver-hpcups
chattr +i /etc/cups/printers.conf
sudo vim /etc/cups/printers.conf

smbclient "//LIVING/HPPSC1400series" -U "WORKGROUP\Usuario" -c "print hola"


sudo cups
netstat -plnt
http://127.0.0.1:631/printers/?
https://github.com/kentio/hp-ppd
```

Si no tiene contraseña tenes que cambiar en Windows en el regedit BlankPassswords un registro así que ya no recuerdo 


### LPR
https://old.reddit.com/r/learnpython/comments/124ws9d/printing_from_python_linux_to_shared_printer/

https://forums.linuxmint.com/viewtopic.php?t=378584
