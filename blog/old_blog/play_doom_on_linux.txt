---
title: "Play doom on Debian Linux"
date: 2023-09-19T11:46:03-03:00
tags: ['doom','linux']
---

Necesitás GZDoom, en Debian usa una librería llamada libflac8 que ya no se puede instalar desde los repositorios y se lo pueden bajar desde acá:
[https://debian.pkgs.org/10/debian-main-amd64/libflac8_1.3.2-3+deb10u2_amd64.deb.html](https://debian.pkgs.org/10/debian-main-amd64/libflac8_1.3.2-3+deb10u2_amd64.deb.html)

Luego bajan el deb del gzdoom para ubuntu desde acá: 
[https://zdoom.org/downloads](https://zdoom.org/downloads)  
Lo instalan usando sudo `dpkg -i nombre_del_paquete.deb`, probablemente si no instalaron la librería que mencioné anteriormente los va a putear porque falta esa librería.

Ahora que ya tienen **gzdoom** instalado procedemos a bajar los iwads y los pwads para correr el juego.

1. Creen una carpeta llamada doom
2. Dentro de la carpeta doom creen una carpeta llamada IWADs
3. Dentro de esa carpeta bajen los siguientes archivos: Tienen que bajar un IWAD desde acá (por ejemplo yo usé PLUTONIA.WAD y el WAD del ULTIMATE DOOM DOOM.WAD, hay otros como TNT, DOOM2, etc). Lo bajan desde aca a esos archivos: [https://archive.org/details/2020_03_22_DOOM](https://archive.org/details/2020_03_22_DOOM)
4. Ahora vuelvan a la carpeta doom y creen una carpeta llamada PWADs, el nombre hace referencia a patch wad 
5. Bajen este patch en esa carpeta desde acá:
[https://github.com/EmeraldCoasttt/BrutalDoomPlatinum/releases/tag/v3.1](https://github.com/EmeraldCoasttt/BrutalDoomPlatinum/releases/tag/v3.1)
6. Bajen otro PWAD llamado Mood4Doom, que lo bajan desde acá, lo ponen en la misma carpeta PWADs [https://www.moddb.com/mods/brutal-doom/addons/mood4doom-v1](https://www.moddb.com/mods/brutal-doom/addons/mood4doom-v1)


Ahora corren el juego ejecutando si bajaron DOOM.WAD:
```bash
gzdoom -iwad IWADs/DOOM.WAD -file "PWADs/BrutalDoomPlatinumv3.1.1.pk3" "PWADs/Mood4Doom/Mood4Doom_Doom_V1.wad"
```

Si no quieren usar BrutalDoomPlatinum pueden bajar Project Brutality desde: [https://www.moddb.com/mods/brutal-doom/addons](https://www.moddb.com/mods/brutal-doom/addons)
Y lo usan con el siguiente comando:
```bash
gzdoom -iwad IWADs/PLUTONIA.WAD -file "PWADs/Project Brutality 2.03.pk3" "PWADs/Mood4Doom/Mood4Doom_Plutonia_V1.wad"
```

Saludos!
