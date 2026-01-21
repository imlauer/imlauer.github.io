---
title: "Openbsd kvm/virtmanager"
date: 2024-09-10T06:23:41-03:00
tags: ['openbsd','virtmanager']
---
Para instalar OpenBSD usando [Qemu-kvm-virtmanager](/post/como-instalar-qemu-kvm-virt-manager/) tenés que deshabilitar la opción `Enable I/O APIC` que se encuentra en `opciones > sistema`.

#### Otra posible solución
`You need to change the VM from dynamically allocated to fixed size on the physical HDD.`

#### Otra posible solución
Utilizo virt-manager para administrar máquinas virtuales. Estos son los pasos para hacerlo al crear la VM:

1. Creá la VM y en el último paso elegí "Personalizar la configuración antes de la instalación" (Customize configuration before install)
2. Hacé clic en la pestaña "IDE CDROM 1" y cambie "Bus de disco"(Disk bus) a SATA
3. Luego hacé clic en Aplicar y luego en Iniciar instalación en la parte superior izquierda.

Después de eso, OpenBSD se instaló correctamente.


#### Otras posibles soluciones.

https://unix.stackexchange.com/questions/674372/kernel-panic-while-install-openbsd

https://www.wezm.net/v2/posts/2023/openbsd-db-atapi-start-not-ready/
