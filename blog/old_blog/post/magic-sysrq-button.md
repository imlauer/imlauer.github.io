---
title: "Magic Sysrq Button"
date: 2023-07-02T10:10:44-03:00
tags: ['comandos','linux']
---
Para activarlo si es que ya no está activado:
```bash
echo 'kernel.sysrq=1' | sudo tee /etc/sysctl.d/99-reisub.conf 
```

[https://en.wikipedia.org/wiki/Magic_SysRq_key](https://en.wikipedia.org/wiki/Magic_SysRq_key)  

Si tu sistema GNU/Linux se "congela" por alguna falla de hardware o software no es recomendable apagar la computadora manteniendo apretado la tecla apagar porque tenes altas probabilidades de dañar tu sistema de archivos. En lugar de hacer eso, se puede habilitar la Magic Sysrq para ejecutar un reseteo.  

[https://www.debian.org/doc/manuals/securing-debian-manual/restrict-sysrq.it.html](https://www.debian.org/doc/manuals/securing-debian-manual/restrict-sysrq.it.html)  

[https://forum.endeavouros.com/t/tip-enable-magic-sysrq-key-reisub/7576](https://forum.endeavouros.com/t/tip-enable-magic-sysrq-key-reisub/7576)

This sequence issues the following low-level commands to the kernel:

* R = Switch the keyboard from raw mode to XLATE mode
* E = Send the signal SIGTERM to gracefully terminate all processes (except PID 1)
* I = Send the signal SIGKILL to kill all processes that didn’t terminate gracefully
* S = Sync data to disk (flush)
* U = Unmount the filesystem (and remount as read-only)
* B = Reboot


Just remember that the letters spell REISUB (a good mnemonic is “Reboot Even If System Utterly Broken”).


https://forum.endeavouros.com/t/tip-enable-magic-sysrq-key-reisub/7576
