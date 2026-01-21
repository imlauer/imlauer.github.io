---
title: "Montar android como almacenamiento usb: MTP"
date: 2025-01-07T12:40:03-03:00
tags: ['android']
---
No vas a ver la partición al ejecutar: `sudo fdisk -l o lsblk`.

Los Android modernos no utilizan el protocolo de almacenamiento USB tradicional para conceder acceso al almacenamiento del teléfono, por lo que no ves un dispositivo de bloque (/dev/sd\*) apareciendo. **Utilizan un protocolo específico llamado MTP que abstracta el sistema de archivos subyacente de la computadora (el beneficio aquí es que puedes seguir usando tu teléfono/ el sistema de archivos del teléfono**, mientras cambias los datos a través de la computadora). Para todos los efectos prácticos, piensa en él como un sistema de archivos de red como SMB o NFS donde puedes acceder a los archivos pero no tienes información sobre el almacenamiento real en el que se almacena la data.

La desventaja del problema es que MTP es un protocolo horrible, con limitaciones extrañas (sólo puedes accederlo desde una sola aplicación y realizar operaciones individuales por vez, lo que a menudo lleva a conflictos si utilizas múltiples aplicaciones que proporcionan soporte para MTP).

Implementaciones de protocolo MTP existen en varios software en el espacio de usuario, que deseas leer https://wiki.archlinux.org/index.php/Media_Transfer_Protocol que resume las diversas opciones para acceder.

```bash
yay -S android-file-transfer
mkdir $HOME/mnt
sudo aft-mtp-mount ~/mnt
sudo su
cd mnt
```
Si no funciona así hacelo con root.

En Gentoo tenés que insatlar: `simple-mtpfs` y `android-file-transfer-linux`.

```bash
emerge -va simple-mtpfs android-file-transfer-linux
mkdir ~/AndroidDevice
simple-mtpfs ~/AndroidDevice
fusermount -u ~/AndroidDevice # unmount
```

