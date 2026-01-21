---
title: "Instalar Linux en el usb para la playstation2"
date: 2023-10-13T00:52:03-03:00
tags: ['linux','ps2']
---
Primero tenés que instalar Funtuna en un pendrive y Free MCBoot en un DVD y necesitás una memory card.

[![Watch the video](https://img.youtube.com/vi/iThCnICopDk/hqdefault.jpg)](https://www.youtube.com/embed/iThCnICopDk)


[https://kernelloader.sourceforge.net/linux.html](https://kernelloader.sourceforge.net/linux.html)

Part1: Baja Black Rhino USB 
[![Watch the video](https://img.youtube.com/vi/mPU-b4lBvx0/hqdefault.jpg)](https://www.youtube.com/embed/mPU-b4lBvx0)
Parte2
[![Watch the video](https://img.youtube.com/vi/XSODLmtuJmM/hqdefault.jpg)](https://www.youtube.com/embed/XSODLmtuJmM)

Black Rhino Linux:
[https://sourceforge.net/projects/kernelloader/files/BlackRhino%20Linux%20Distribution/Live%20Linux%20USB/PS2%20Live%20Linux%20USB%20v5/](https://sourceforge.net/projects/kernelloader/files/BlackRhino%20Linux%20Distribution/Live%20Linux%20USB/PS2%20Live%20Linux%20USB%20v5/)
Este es un Linux Live System para PS2 con NetSurf 3.1 (navegador web)

El archivo ps2linux_live_v5_pal_netsurf_usb.7z debe extraerse al directorio raíz de un dispositivo de almacenamiento USB (por ejemplo, FAT).
El archivo PS2NS/kloader.elf debe iniciarse desde la memoria USB.  Puede utilizar uLaunchELF para esta tarea.
Si no usó kloader antes, iniciará Linux automáticamente y ejecuta NetSurf desde el dispositivo de almacenamiento USB. Si usó kloader antes, necesita
Cargue la configuración de NetSurf desde la memoria USB.

Se recomienda utilizar un teclado USB y un mouse USB.  Si solo tienes un ratón, puedes activar el OSK (teclado en pantalla).

Para apagar, presione brevemente el botón de encendido. La PS2 necesitará algo de tiempo
para apagar.

F12 finalizará NetSurf y estará en la línea de comando. Presione CTRL + D
para reiniciar NetSurf.

Lo nuevo en esta versión es:
-NetSurf 3.1
- bison 3.0.2
- flex 2.5.39
- gperf 3.0.4
- kernelloader 3.0

El lanzamiento tiene algunos problemas:
- Todavía se utiliza el antiguo Linux, lo que causa algunos problemas.
- https no funciona.
- El OSK (teclado en pantalla) a veces no es visible, pero sigue ahí.
Debe desactivarlo al desplazarse o hacer clic en hipervínculos.
- Algunas páginas web son demasiado grandes para caber en la memoria, es necesario activar el intercambio
memoria (debe agregar manualmente una partición de intercambio en el dispositivo de almacenamiento USB).
- La carga de páginas web puede ser lenta y la GUI no acepta más comandos
mientras se carga (no responde).
- Las cosas avanzadas como videos y sonido no funcionan (por ejemplo, youtube).
- Cuando usas una resolución de pantalla grande con muchos colores, tendrás menos
Memoria para navegación web.

En el video 13 de instalacion de gentoo en la ps2 repite todo el proceso de nuevo.
instalar gentoo ps2: [https://wiki.gentoo.org/wiki/User:Immolo/GentooPS2](https://wiki.gentoo.org/wiki/User:Immolo/GentooPS2)
