---
title: "Jugar Counter Strike 1.6 en GNU/Linux"
date: 2022-06-11T05:44:03-03:00
tags: ['counter','cs']
categories: ['games']
---
Esta publicación quedó vieja si querés saber como jugar tenés que bajar el appimage desde acá: [https://de.linuxgame.cn/%E5%8F%8D%E6%81%90%E7%B2%BE%E8%8B%B1/cstrike_1.6_i386.appimage](https://de.linuxgame.cn/%E5%8F%8D%E6%81%90%E7%B2%BE%E8%8B%B1/cstrike_1.6_i386.appimage) o [https://t.me/appimage_hub/37](https://t.me/appimage_hub/37)
Si te tira el siguiente error:
```bash
└─$ ./cstrike_1.6_i386.appimage
Error:libGL.so.1: wrong ELF class: ELFCLASS64
Could not load hw.so.
Please try again at a later time.done
```
Tenés que agregar la arquitectura i386 para poder bajar la librería faltante que es libgl pero de 32 bits así:
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install libgl1:i386
```


Bajen cualquier instalador , ejecutenlo con wine y luego abran una terminal muevanse a la ubicacion `~/.wine/drive_c/Program Files (x86)/CounterStrike.16/` que es la ubicacion por defecto en donde instala el programa
### Solucionar el problema de pantalla negra en Counter Strike 1.6 Linux
En lugar de abrirlo con OpenGL intenta usar Software como renderizado y abrilo en modo ventana con el siguiente comando  

#### Opcion mas RECOMENDABLE (Rendenrizado usando Software):
```
wine hl.exe -game cstrike -windowed -soft -32bpp -nofbo -nomsaa -gl_vsync 0
```

##### FUNCIONA PERO NO ES RECOMENDABLE (Renderizado usando D3D):
Tambien podes intentar ejecutarlo con la opcion de d3d (direct3d) pero funciona demasiado lento.
```bash
wine hl.exe -game cstrike -d3d -32bpp -nofbo -nomsaa -gl_vsync 0
```

Para recuperar la resolucion que tenian antes de iniciar el juego pueden ejecutar (solo si iniciaron el juego en pantalla completa, si la iniciaron en ventana no necesitan ejecutar esto) 
```bash
xrandr -q | grep current (para obtener su resolucion actual)
xrandr -s 1366x768 (para cambiar la resolucion)
```

Parámetros que podes probar para correr el juego:  
```bash
-w <width> - Forces the engine to start with resolution set to <width>.  
-h <height> - Forces the engine to start with resolution set to <height>. This launch option does not need to be set in the presence of -w. The width value will determine the height automatically.  

standard height size is determined by the screen mode -norm or -widescreem  

Here are more "set launch options" commands that can be used for video.  
-fullscreen : no framed window  
-windowed or -sw or -startwindowed : game will be in a framed window  
-noboarder : in windowed mode this removes the frame around it.  
-gl : open_gl graphics rendering  
-software : CPU graphic rendering  
-normal : monitor size 4:3 ratio  
-wide : monitor size 16:9or10 ratio  
+gl_vsync 0 : turns off verical Synch in open_gl rendering (can improve FPS)  
-nofbo : this turns off some advance rendering in open_gl (can improve FPS)  
-nomsaa : turns off AA ;Anti-Aliasing (can improve FPS)  
+gl_aniso 0 : Removes anisotrophic filtering (can improve FPS)  
-w 800 : width screen resolution size (other sizes can be used)  
-h 600 : height screen resolution size (other sizes can be used)  
```
--------------------------------------  
  
#### Otras opciones
When running open_gl rendering mode  
These commands can be left in the command-line "set launch options" if they help increase your in game FPS.  
+gl_vsync 0  
-nofbo  
-nomsaa  
-gl_aniso 0  
or use all at once " +gl_vsync 0 -nofbo -gl_aniso 0" no quote marks  
  
Mouse  
  
-noforcemaccel > reverts to desktop mouse acceleration settings (more)  
-noforcemparms > reverts to desktop mouse button settings (more)  
-noforcemspd > uses desktop mouse speed settings (more)  
  
Monitor  
  
-w 640 -h 480 > forces the resolution to 640x480  
-w 800 -h 600 > forces the resolution to 800x600  
-w 1024 -h 768 > forces the resolution to 1024x768  
-full > forces fullscreen mode  
-windowed > forces window mode  
-freq x > forces the monitor to use x hertz  
  
Video  
  
-gl > run in OpenGL  
-d3d > run in Direct3d  
-soft > run in software mode  
  
DirectX  
  
-dxlevel 90 > DirectX 9  
-dxlevel 81 > DirectX 8.1  
-dxlevel 80 > DirectX 8  
-dxlevel 70 > DirectX 7  
-dxlevel 60 > DirectX 6  
  
Other  
  
-16bpp > forces the colors to 16bit  
-32bpp > forces the colors to 32bit  
-heapsize x > specify the number (x) of memory to use  
-zone x > allocates x amount of KiloBytes of memory for use with the console system  
-noip > disables the use of UDP, which is part of the TCP/IP protocol  
-noipx > disables the use of the IPX/SPX protocol  
-nojoy > disables joystick support (shaves a little bit off the memory footprint)  
-wavonly > disables the use of direct sound (only use if you are having sound problems)  
-noaafonts > disables Anti-Aliasing of screen fonts  
-autoconfig > restores video and performance settings to default  
-condebug > logs all console output into the console.log text file  
-novid > disables intro video  
  
```  
try adding -nofbo -nomsaa -gl\_vsync 0 to launch option settings, worked for me  
```  

https://steamcommunity.com/app/70/discussions/0/371918937276006731/
https://steamcommunity.com/discussions/forum/1/864959809848706037/?l=spanish
