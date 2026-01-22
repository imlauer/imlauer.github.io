---
title: "Openbsd: Instalación y configuración"
date: 2024-09-14T18:41:20-03:00
---
Mejores computadoras para correr openbsd: lenovo thinkpad t420 agregale un ssd, 8 gbde ram. nvidia no funciona bien con openbsd.

Computadoras que corren bien con openbsd:     
https://jcs.org/tagged/openbsd   
https://jcs.org/2021/07/19/desktop

Zaney: https://redirect.invidious.io/channel/UCmw-QGOHbHA5cDAvwwqUTKQ
Dejó de usar openbsd por un problema de temperatura, pero hay una solución que se explicará acá: obsdfreqd

https://redirect.invidious.io/playlist?list=PLbET-7keUM8qiNs0D7ya2cnu-n2y1JRwC  
  
https://redirect.invidious.io/watch?v=DQrXvjV9lyQ  
  
https://redirect.invidious.io/watch?v=c5WnhxFx6P8  
  
  

Primero descargamos install-number.iso de la arquitectura de pc que estemos usando y también descargá el SHA256 y SHA256.sig
  
De esta primer parte me faltó lo que hace en archlinux en el 1er video.  
  
https://www.openbsd.org/faq/faq4.html#Download > mirror sites > seleccioná el mirror > última versión de openbsd > amd64 > install-number.iso y SHA256 y el SHA256.sig.
Ahora tenés que comprobar si la iso que bajaste se bajó correctamente usando `sha256` está descripto como hacerlo en Downloads.

También hay otra forma de comprobarlo con signify.

Después tenés que instalar `apt install -y signify-openbsd`:         
Y tenés que descargar la llave pública que está en esa misma página de Downloads:

`signify -Cp openbsd-number-base.pub -x SHA256.sig install-number.iso`

Ahora hay que limpiar el discoduro, no es necesario salvo que compraste una pc usada y querés borrar todo por si las duda tenía algo ilegal.

Para limpiar el hdd: disk setup > RAID and disk encryption > y desde el usb live o el medio de instalación ejecutá `dd if=/dev/urandom of=/dev/rsd3c bs=1m` 

https://www.openbsd.org/faq/faq14.html#softraid

Ahora mostramos como hacerlo desde un archlinux live usando openssl, porque openssl no está en openbsd, openssl lo podés usar para escribir información criptográfica y es mucho más rápido.

El comando en cuestión:
**Peligro, si tenés muchos discos duros fijate bien cual querés limpiar.**

```bash
# DEVICE="/dev/sdX"
# PASS=$(tr -cd '[:alnum:]' < /dev/urandom | head -c128)
# openssl enc -aes-256-ctr -pass pass:"$PASS" -nosalt </dev/zero | dd obs=64K ibs=4K of=$DEVICE oflag=direct status=progress
```
Si no querés ver el error tenés que usar la flag: `-pbkdf2` antes del `/dev/zero`
### Tarda alrededor de 1 hora y 20 minutos.

https://wiki.archlinux.org/title/Securely_wipe_disk/Tips_and_tricks#dd_-_advanced_example

  
#### Luego de bootear OpenBSD:  
```  
Welcome to the OpenBSD/amd64 7.1 installation program.  
(I)nstall, (U)pgrade, (A)utoinstall, (S)hell? S  
```  
  
Para saber como se llama tu disco duro:  
```  
# dmesg | grep "sd"  
# cd /dev && sh MAKEDEV sd0  
# fdisk -gy -b 960 sd0 (gpt)  
# disklabel -E sd0  
sd0 > p g  
sd0 > d a  
sd0 > ?  
sd0 > a a  
offset: [1024]  
size: [...] *  
FS Type: [4.2BSD] RAID  
sd0 > w  
sd0 > q  
# bioctl -c C -l sd0a softraid0  
Creará un "crypto volume" como sd3  
# dmesg | grep "sd"  
# cd /dev && sh MAKEDEV sd3  
# dd if=/dev/zero of=/dev/rsd3c bs=1m count=1  
# exit  
```  
  
  
```  
Welcome to the OpenBSD/amd64 7.1 installation program.  
1. (I)nstall, (U)pgrade, (A)utoinstall, (S)hell? I  
2. Keyboard layout: es  
3. System hostname: obsdlaptop  
4. Which network interface do you wish to configure? done  
Es facil de crear una interfaz de red luego de la instalación así que no te preocupes.  
5. DNS domain name? Enter  
6. DNS nameservers? Usá por defecto luego lo cambiamos. (Enter)  
7. Password for root?  
8. Do you want the X window system to be started by xenodm(1)?   
* no (si querés usar startx)  
* yes (si querés una pantalla de login)  
9. Setup a user? esotericwarfare  
10. Allow root ssh login? no  
11. Which disk is the root disk? sd3 (el volumen crypto que creamos)  
12. gpt (ya expliqué en la publicación de instalacion de gentoo la diferencia entre gpt y msdos)  
13. E(edit)   
14. ?  
15. p g (print gigabytes)  
16. R l (resize)  
-2G  
17. p g  
18. R h  
+2G  
19. p g  
20. w  
21. q  
22. done  
23. disk (si usaste install-number.img, miniroot-number.img requiere internet)  
24. Is the disk partition already mounted? no  
25. Which disk contains the install media? Acá seleccioná tu pendrive (sd1 o sd2 tenés que haberlo mirado con dmesg)  
26. Which partition has the install sets? [a] a  
27. Pathname to the sets? [7.1/amd64] (Enter)  
28. -x* (eliminará todo lo relacionado con el servidor Xorg) NO lo hagas si estás instalando openbsd para desktop otro ejemplo: -game*  
29. Directory does not contain SHA256 sig. Continue without verification? YES.  
30. Location of the sets? [done]  
31. What timezone are you in ? America/Boise  
Acá falla al descargar el firmware XD vas a tener que conectarte a través de ethernet y bajarlo o usar un pendrive.  
32. Exit to (S) ,... [reboot] (Enter) Primero sacá el pendrive o el medio de instalación.  
```  
  
corebooting las thinkpad es un dolor de huevos hay muchos problemas y podés brikear la laptop.  
  
k openbsd está roto, hay que usar el archivo de openbsd efi (método que se mostró en el video de dual openbsd linux) "chain load" ese archivo hay que usar c-bios o tiana core como payload, coreboot rompe la maquina, se pierde funcionalidad de la máquina.  
Solía tener una maquina con coreboot y usaba c-bios como payload y la vendí   
  
  
```  
33. Nos logueamos como root en la tty.  
34. # mail.  
& 1  
& ?  
& more  
Podés mandar a openbsd.org tu dmesg para asegurarte que corre bien en tu PC.  
exit (ctrl+c)  
  
35. vi /etc/doas.conf  
permit persist :wheel  
exit  
exit  
```  
  
Y reingresá a tu usuario.  
  
```  
36. Ahora hay que conectarse a internet.  
37. doas pkg_add sakura  
38. reboot  
```  
  
Ahora tendremos que instalar el firmware y ver si podemos tener internet.  
  
  
39. ping google.com  
40. fw_update (con ethernet conectado o vas a tener que hacerlo usando USB)  
41. vi /etc/hostname.em0 (tenés que saber cual es tu interfaz ejecutando ifconfig esto es para el ethernet) y escribí "dhcp" y guardá  
42. Ahora mirá la interfaz que es wifi con el comando ifconfig (iwn0 probablemente)  
43. Escribí en: `vi /etc/hostname.iwn0` (tu interfaz wifi)  
```bash  
# lladdr random es para obtener una mac address random   
# lladdr = link layer address (otra forma de decir mac)  
  
lladdr random nwid network wpakey "passphase"  
dhcp  
```  
44. sh /etc/netstart (ya deberíamos tener internet a no ser que tengamos un problema con los dns)  
45. Ahora configuramos local inbound.  
46. ping google.com  
47. Ven lo simple que es? Mucho mejor que usar `iw` o `wpa_supplicant`, `netplan`, `networdmanager`.  
48. syspatch es una herramienta que se usa cuando parcheas el sistema, si yo continuo con esto que es una "release branch" (rama de lanzamiento) y la convertiría en una stable branch (rama estable) ejecutando syspatch y eso aplicará parches de seguridad y correcciones de confiabilidad.  
49. Ahora actualizaremos a la rama actual:  
`sysupgrade -s` (-s para snapshots)  
`reboot`  
Se reiniciará 2 veces.  
  
50. ping google.com  
51. doas pkg_add sakura  
52. Para instalar dwm tenés que usar opensuck: https://github.com/swindlesmccoop/opensuck (o aprendelo a compilarlo manualmente vos)  
  
https://old.reddit.com/r/openbsd/comments/rfzjge/how_to_install_dwm_on_openbsd/  
Para compilar dwm en openbsd tenés que descomentar esta línea:  
```  
# OpenBSD (uncomment)  
#FREETYPEINC = ${X11INC}/freetype2  
```  
53. `doas fw_update`  
54. `doas sysmerge`  
55. Ahora vamos a configurar x11 y usar openbsd frequency utils para regular la temperatura y el uso del ventilador, hay un script o un demonio para ponerle un tope a la temperatura, sin importar lo que haga no quiero que pase los 55 grados.  
56. Podemos ver el uso con el comando `systat`  
57. `doas usermod -L staff esotericwarfare`. Hacemos esto porque si mirás dentro del archivo `/etc/login.conf` hay una diferencia entre los recursos que un usuario `default` puede usar y un usuario staff.  
58. En /etc/login.conf te encontrarás con el ulimit umask, todos los límites para el tamaño máximo del proceso y de los datos, todos los límites para la memoria del stack (pila), son conservadores con el usuario por defecto, por eso es recomendable agregarlo al `staff` y te dará valores más altos.  
59. `doas pkg_add git`  
60. mkdir .opt (optional)  
61. cd .opt  
62. `git clone https://tildegit.org/solene/obsdfreqd.git`  
63. cd obsdfreqd  
64. `make && doas make install`  
65. Esto ayuda a regular el calor a través de regular la frecuencia del CPU: `rcctl ls on | grep ^apmd && doas rcctl set apmd flags -L && doas rcctl restart apmd`  
Para algunas computadora funciona mal y en modo inactivo la computadora estará mucho más caliente que en linux y incrementará el ruido de los ventiladores. No me gusta que la temperatura pase los 60.  
66. `doas rcctl enable obsdfreqd`  
67. `doas rcctl start obsdfreqd`  
68. Habilitemos dependencias blandas para para velocidades de disco más rápidas de lectura y escritura: `doas vi /etc/fstab` (tené mucho cuidado con este archivo si te mandas una cagada podés arreglarlo desde el usb live)  
69. Agregá `softdep` a todo menos a swap: `/ /home /tmp /usr /usr/X11R6 /usr/local /usr/obj /usr/src /var`, después del readwrite (rw) y antes del nodev dentro de `/etc/fstab`       
Tené cuidado, escribís algo mal y vas a tener que bootear desde el usb para arreglarlo y usar `chroot` en el directorio boot que es sd1a o sd0a o sd2a, c es la particion general, a es la partición root, luego tendrás que ejecutar `export TERM=vt200` y luego podés editar el fstab usando `doas vim /etc/fstab`.      
70. Luego configuramos un RAMDISK usando el sistema de archivos de memoria integrado en openbsd. Lo configuraremos con 500 megabytes porque tengo 8 gb y usaremos eso para que chromium haga almacenamiento local de caché en la ram y eso ayuda a que el ssd no se desgaste.  
71. Siempre editaremos `/etc/rc.conf.local` NO `/etc/rc.conf`  
72. `rcctl check apmd`   
73. `doas rcctl set apmd flags -L`  
74. `doas rcctl get apmd`  
75. Ahora abrí `/etc/rc.conf.local` y debería aparecer apmd  
76. `doas rcctl set obsdfreqd flags -T 65,60` (65 cuando está enchufado, 60 cuando está con la batería sola)  
77. `doas rcctl restart obsdfreqd`  
78. `less /etc/rc.conf.local`  
79. Por defecto openbsd usa los drivers mode settings en vez de intel.  
80. Instalamos picom: `doas pkg_add picom`  
81. `picom --backend glx --vsync -f -b` (no hace falta -f: fade in fade out, -b background)  
82. `doas pkg_add chromium`  
83. `chrome`  
84. Ahora instalá dwm y otras herramientas: `doas pkg_add feh dmenu mpv ffmpeg pcmanfm `  
Para saber que discos duros tenemos disponibles  
85. `dmesg | grep "sd"`  
86. `doas chown esotericwarfare /mnt` (así el usuario tiene permisos de escritura.  
87. MAL `doas mount /dev/rsd3c /mnt` a representa la partición root, c es el discoduro en total, r es raw  
88. BIEN `doas mount /dev/sd3c /mnt` a representa partición root, r es raw  
mnt = mount  
  
89. `cd .opt/openbsd-configs/etc`  
90. En `doas vi /etc/boot.conf` escribí `set timeout 1`  
91. doas rcctl set sndiod flags=-r 48000 -z 400 -e s24le4lsb -s default -m play,mon -s mon (mon monitoreará el audio cuando usas ffmpeg) si usas streamcast si tenés musica de fondo. (sndiod = sound io demon)  
92. `doas rcctl restart sndiod `  
93. `doas sysctl kern.audio.record=1`  
94. `doas su  
echo kern.audio.record=1 >> /etc/sysctl.conf`  
95. exit exit  
96. Ahora copiamos los archivos necesarios `/mnt/newinstall`  
97. Ahora podés configurar vim, dvtm, .profile, dwm, bash, fish, zsh o la shell que quieras   
98. En `.xsession:` (si usas el xenodm login manager sino en `.xinitrc`) escribí:  
```bash  
# rm -R /home/esotericwarfare/.cache/chromium  
# mkdir /ramdisk/chromium  
# ln -s /ramdisk/chromium /home/esotericwarfare/.cache/chromium  
ulimit -Sc 0 # desactiva quartums  
xrandr --dpi 96  # para las letras  
feh --bg-fil -z ~/.wall2/  
dwm  
```  
Luego explicaremos como configurar ramdisk, por eso comentamos las primeras 3 líneas.  
99. El usa el comando `cp -Rfv chromium /home/esotericwarfare/.config`  
Si copiás todos los archivos que tenés en `/home/esotericwarfare/.config/chromium` tenés toda la configuración y la podés usar facilmente en otra computadora.  
100. El usa el comando `cp -Rfv Clementine /home/esotericwarfare/.config`  
101. El usa el comando `cp -Rfv sakura /home/esotericwarfare/.config`  
102. `chrome &`  
103. `cp -Rfv .wall2/ ~`  
104. `doas pkg_add lxappearance`  
105. En tu `/etc/rc.conf.local` debería aparecer `obsdfreqd_flags=-T 65,60`  
106. En el `/etc/fstab` agregá: `swap /ramdisk mfs rw,nodev,nosuid,-s=300m 0 0`  
107. `mfs = memory file system`  
108. No planeo usar fnafi que usa mono para jugar juegos steam que usan mono y no planeo usar el emulador gamecube eso son los únicos programas que están afectados por usar wxallowed en el fstab así que eliminamos `wxallowed` en `/etc/fstab` del `/usr/local`  
109. Ahora en el `.xsession` descomentá las 3 primeras líneas.     
Cada vez que reinicias la computadora el ramdisk se pierde.   
110. `doas reboot`  
111. Ahora podrás ver el `ls /ramdisk/chromium/` `df -h /ramdisk` se ve que está siendo escrito en mfs.  
112. Es recomendable desmotar `mfs` y hacer un `chmod 1777` para configurar los permisos correctos a esa carpeta (`/ramdisk`)  
https://dataswamp.org/~solene/2022-04-21-openbsd-71-fan-noise-temperature.html  
https://dataswamp.org/~solene/2018-05-08-mfs-tmp.html  
113. Podés comprobar si todo funciona bien mirando un video de youtube, `systat` para mirar la temperatura.
114. Una vez a la semana: `sysupgrade -s` (descargará el último snapshot y actualizará)

A OpenBSD no le importa romper toda la compatibilidad con los "vendors" porque no los tiene como Linux para tener el sistema operativo más seguro posible y altamente customizable código. Es muy similar a linux pero por debajo tiene diferentes valores, principios.
OpenBSD developers: theodore rat, todd miller

En el próximo video veremos como configurar local unbound dns resolver: `man unbound`
armbian vamos a configurarlo, armboards, pine phone y freebsd.
