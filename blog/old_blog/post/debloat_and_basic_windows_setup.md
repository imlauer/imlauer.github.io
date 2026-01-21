---
title: "Debloat and basic windows setup (activate windows)"
date: 2023-11-26T21:57:39-03:00
tags: ['debloat','windows','basic','setup']
---

[OpenShell](https://open-shell.github.io/Open-Shell-Menu/)

[Ninite](https://ninite.com/) - Instalá o actualizá varias aplicaciones de una sóla vez.  

Instalá LibreOffice, Firefox, SumatraPDF, VLC, K-lite codecs, OpenSHELL (si no lo instalaste anteriormente), 7-zip

Bajá uBlock, SponsorBlock, Bypass Paywals y, Return of YouTube Dislikes.

Para bloquear las advertencias de cookies en la configuración de ublock (el engranage al apretar el icono de la extensión) te vas a la pestaña de filter lists, o litra de filtros y buscá annoyances, ahi activá adguard, y  uBlock filters luego dale update now.


Bajá esto 
[/Sycnex/Windows10Debloater](https://github.com/Sycnex/Windows10Debloater)
Ejecuta powershell como administrador y ejecutá el script GUI o `.\Windows10SysPrepDebloater.ps1 -Sysprep -Debloat -Privacy`


Borrá tips, feedback hub, maps, people del menú de inicio
Dato adiccional: no uses google drive web ni whatsapp web siempre que tengas la posibilidad de usar la aplicación de escritorio usála son más rápidas.

#### Activar Windows
[https://github.com/massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)

### Método 1
En Windows botón derecho en el menú de Inicio y ejecutá Powershell o terminal (no CMD) si no funciona probá ejecutando powershell como administrador y copiá y pegá el siguiente código `irm https://massgrave.dev/get | iex`. Verá las opciones de activación y seguirá las instrucciones en pantalla. Eso es todo.

### Método 2
Descarga el archivo desde [GitHub](https://github.com/massgravel/Microsoft-Activation-Scripts/archive/refs/heads/master.zip) o [Bitbucket](https://bitbucket.org/WindowsAddict/microsoft-activation-scripts/get/master.zip)  

Hacé clic derecho en el archivo zip descargado y extraelo   
En la carpeta extraída, buscá la carpeta llamada `All-In-One-Version`  
Ejecutá el archivo llamado `MAS_AIO.cmd`  
Vas a ver las opciones de activación y seguirá las instrucciones en pantalla.  
Eso es todo.  


