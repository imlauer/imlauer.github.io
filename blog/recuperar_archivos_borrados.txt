---
title: "Recuperar archivos borrados"
date: 2025-01-22T07:16:37-03:00
tags: ['linux']
---
Podes usar testdisk, photorec y scalpel.

Si tenés una distro de Linux adicional instalada, o un USB live bootealo e instalá las herramientas mencionadas anteriormente.

```bash
sudo apt install -y testdisk
pacman -S testdisk
```

Ahora ejecutamos `photorec`

Ojo tenés que tener espacio en la partición para recuperar los archivos o vas a tener que ir eliminando a medida que los recupera.

https://recoverit.wondershare.es/file-recovery/photorec-linux.html

https://archive.is/wip/lHLFe


##### **extundelete** quedó **obsoleto** me tira segmentation fault al ejecutar
```bash
extundelete /dev/sda1 --restore-directory /home/usuario/carpeta_a_recuperar
```

