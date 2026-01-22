---
title: "Gentoo handbook: Definiciones"
date: 2025-06-19T04:23:59-03:00
tags: ['linux']
---
https://wiki.gentoo.org/index.php?title=Handbook:AMD64/Full/Installation&printable=yes    
https://wiki.gentoo.org/index.php?title=Handbook:AMD64/Full/Installation

**inode:**

```bash
mkfs.ext4 -T small /dev/device
```
Hacer esto cuadruplica el número de inodes de un dado sistema de archivos, como es "bytes-per-inode" reduce de uno cada `16kB` a uno cada `4kB`.

Un inode (o inodo) es una estructura de datos que usan los sistemas de archivos como Linux o Unix para guardar toda la información sobre un archivo o directorio, excepto el nombre y el contenido real del archivo. El inodo almacena metadatos como: tamaño, permisos, propietario, fechas de creación/modificación, y la ubicación de los bloques de datos en el disco.

Cada archivo o carpeta tiene su propio inodo, y si se alcanza el límite de inodos en un sistema, no podrás crear más archivos aunque tengas espacio libre. Es como el "carnet de identidad" de cada archivo en el sistema.

**XFS soporta reflinks**:

El "reflink" y el "copy-on-write" (CoW) en XFS permiten hacer copias rápidas de archivos sin duplicar los datos en disco al momento de la copia. Cuando usas un reflink (por ejemplo, con cp --reflink), ambos archivos apuntan a los mismos bloques de datos; solo si modificas uno de ellos, el sistema crea una copia real de los bloques afectados, manteniendo la integridad y ahorrando espacio.
Esto es súper útil para snapshots, deduplicación y clonar archivos grandes, porque solo ocupan espacio extra cuando realmente cambias algo. 

###### Ejemplo práctico de cómo usar reflink y Copy-on-Write (CoW) en XFS:
* Para hacer una copia rápida de un archivo grande usando reflink (sin duplicar espacio al principio), solo usa:
```bash
cp --reflink=always archivo_original copia_reflink
```
* Ambos archivos compartirán los mismos bloques de datos hasta que modifiques alguno; solo entonces XFS hace una copia real de los bloques cambiados (esto es el CoW).
* Esto ahorra muchísimo espacio y tiempo, especialmente útil para backups, snapshots, o clonar imágenes de máquinas virtuales.



```bash
nameserver 9.9.9.9
nameserver 149.112.112.112
```

###### how to connect to a WPA2 WiFi network using either iwd 

With `iwd`:
1. Make sure wpa_supplicant is not running: `rc-service wpa_supplicant stop`
2. Start iwd: `rc-service iwd start`
3. Enter the interactive shell: `iwctl`
4. List devices: `device list`
5. Scan and connect:
```bash
station <device> scan
station <device> get-networks
station <device> connect <SSID>
```
(It’ll ask for your password if needed.)
