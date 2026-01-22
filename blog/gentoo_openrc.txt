---
title: "Nueva instalación binaria de Gentoo con OpenRC, XFS y Sway (Los binarios de Gentoo no son como los de ArchLinux)" 
date: 2025-06-22T22:25:52-03:00
tags: ['gentoo']
---

https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet


**Clásicos momentos usando Gentoo:**  
Instalé `OBS Studio` en Gentoo sin mirar las banderas (USE Flags) cuando ejecuté `obs` no podía agregar la cámara, y tampoco podía compartir la pantalla.  
Con el comando `emerge -pv obs-studio` pude ver las banderas y leyendo la Wiki de Gentoo de OBS me dí cuenta que tengo que habilitar las siguientes banderas para tener esas funcionalidades:  
```bash  
[ebuild   R    ] media-video/obs-studio-31.0.3-r2::gentoo  USE="alsa truetype wayland -browser -decklink -fdk -jack -lua (-mpegts) -nvenc -pipewire -pulseaudio -python -qsv -sndio -speex -test-input -v4l -vlc -websocket" LUA_SINGLE_TARGET="luajit" PYTHON_SINGLE_TARGET="python3_13 -python3_11 -python3_12 -python3_14" 0 KiB  
```  
Ahí se pueden ver las banderas DESHABILITADAS (las que comienzan con un signo `-`)  
  
Según la Wiki de OBS de Gentoo: https://wiki.gentoo.org/wiki/OBS_Studio estas son las banderas disponibles:  
```bash  
+alsa      Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)  
browser    Enable browser source support via (precompiled) CEF.  
decklink   Build the Decklink plugin.  
fdk        Build with LibFDK AAC support.  
jack       Add support for the JACK Audio Connection Kit  
lua        Enable Lua scripting support  
mpegts     Enable native SRT/RIST mpegts output.  
nvenc      Add support for NVIDIA Encoder/Decoder (NVENC/NVDEC) API for hardware accelerated encoding  
           and decoding on NVIDIA cards (requires x11-drivers/nvidia-drivers)  
pipewire   Build with PipeWire support.  
pulseaudio Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)  
python     Build with scripting support for Python 3.  
qsv        Build with Intel Quick Sync Video support.  
sndio      Build with sndio support.  
speex      Build with Speex noise suppression filter support.  
test-input Build and install input sources used for testing.  
truetype   Add support for FreeType and/or FreeType2 fonts  
v4l        Enable support for video4linux (using linux-headers or userspace libv4l libraries)  
vlc        Build with VLC media source support.  
wayland    Enable dev-libs/wayland backend  
websocket  Build with WebSocket API support.  
```  
  
Entonces para que nos funcione la **cámara y podamos compartir pantalla** necesitamos:   
* `v4l`  
* `browser` para poder cargar elementos programados con Javascript, HTML y CSS.  
* `pipewire` para captura de audio  
* `truetype` letras  
* `websocket`   
  
Para saber donde escribimos estas banderas tenemos que leer lo básico de como usar Portage: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Portage  
  
Within `/etc/portage/` users can create the following files:  
* `package.mask` which lists the packages that Portage should never try to install  
* `package.unmask` which lists the packages Portage should be able to install even though the Gentoo developers highly discourage users from emerging them  
* `package.accept_keywords` which lists the packages Portage should be able to install even though the package hasn't been found suitable for the system or architecture (yet)  
* **`package.use` which lists the USE flags to use for certain packages without having the entire system use those USE flags**  
  
Entonces todas esas banderas las escribiremos en el archivo `/etc/portage/package.use/obs` de la siguiente manera:  
```bash  
media-video/obs-studio v4l browser pipewire truetype websocket  
```  
Y ahora recompilemos  
```bash  
emerge -av --quiet obs-studio  
```  
Debería aparecer en **verde las nuevas banderas con un asterisco**.  
```bash
[ebuild   R   ] media-video/obs-studio-31.0.3-r2  USE="alsa browser* pipewire* truetype v4l* wayland websocket* -decklink -fdk -jack -lua (-mpegts) -nvenc -pulseaudio -python -qsv -sndio -speex -test-input -vlc" LUA_SINGLE_TARGET="luajit" PYTHON_SINGLE_TARGET="python3_13 -python3_11 -python3_12 -python3_14"
```
  
Como estoy en Wayland (Sway) para compartir la pantalla debo seguir los siguientes pasos: https://imlauera.github.io/sway/  

---

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgHABzk8ar7MZ6s1NvBGSu_y54LtiYr0Igp7Fl9Q21Xniedh6_OT9l7EjHF5E6CCvWOBb-e8f5C4WnfbwhnDDtSmKsBi_vT1YnubrS8zB00axT48yUHrUv09CTyL_LeAQ2RBbSB5juTTqCHydiP-bpJoQmWD5dNnUEoVEVSrNVWWJsFGgmkGm2ef0S4F96w/s1366/reddit.png)


Ya había hecho una guía anteriromente sobre instalar Gentoo: https://imlauera.github.io/post/gentoo_installation/


###### Binarios
Si instalas el binario del grub en Gentoo no es lo mismo que el binario en ArchLinux.   
El binario de GRUB no viene con la bandera `mount (USE Flag)` habilitada por lo tanto si quiero usar `OS-PROBER` estoy obligado a compilar el GRUB porque **el binario de GRUB en Gentoo no tiene la bandera mount activada** entonces tengo que compilarlo para poder usar `OS-PROBER`.   
Es decir los binarios vienen con la mínima cantidad de banderas posibles, a diferencia de ArchLinux que vienen con la máxima cantidad de banderas posibles activadas.   
   
---   
   
###### Handbook AMD64 FULL: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full
1. Instalación: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation
2. Como usar emerge: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Working
3. Portage: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Portage
4. Configurando la red en OpenRC: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Networking


https://wiki.gentoo.org/wiki/Handbook:AMD64/Full   

**AVISO: Esta guía no incluye la creación del pendrive con Gentoo ni el particionado**. Esta guía comienza después el particionado para adelante.   
**Como hacer crear el pendrive y el particionado están bien descriptos en el handbook**.
   
Instalé gentoo guíandome con el handbook: Usé XFS, OpenRC, Grub y agregué el binary host.   
   
NO instalé pipewire y funcionó el audio sin configurarlo.   
   
##### En el handbook usaba `/efi` como partición yo usé `/boot`(que supuestamente es para Legacy BIOS), funcionó pero no tengo Legacy BIOS tengo UEFI.   
```bash   
mkfs.fat -F 32 /dev/sda2   
mkfs.xfs /dev/sda1   
mkswap /dev/sda6   
mount /dev/sda1 /mnt/gentoo   
mount /dev/sda2 /mnt/gentoo/boot (En la guía sugiere /efi pero no lo usé así)   
swapon /dev/sda6   
cd /mnt/gentoo   
chronyd -q   
links https://gentoo.org/downloads/mirrors/   
releases/amd64/autobuilds/   
Descargué OpenRC: current-stage3-amd64-desktop-openrc/   
tar xpvf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /mnt/gentoo   
```   
   
   
nano `/mnt/gentoo/etc/portage/make.conf`   
   
```bash   
COMMON_FLAGS="-march=native -O2"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
RUSTFLAGS="${RUSTFLAGS} -C target-cpu=native"
FCFLAGS="${COMMON_FLAGS}"
FFLAGS="${COMMON_FLAGS}"

# NOTE: This stage was built with the bindist USE flag enabled

# This sets the language of build output to English.
# Please keep this setting intact when reporting bugs.
LC_MESSAGES=C.utf8
MAKEOPTS="-j2 -l3"

GENTOO_MIRRORS="https://gentoo.zero.com.ar/gentoo/ \
    rsync://gentoo.zero.com.ar/gentoo"

FEATURES="${FEATURES} getbinpkg"
FEATURES="${FEATURES} binpkg-request-signature"
ACCEPT_LICENSE="*"
USE="dist-kernel -X -gtk -qt5 -gnome -kde minimal " # Importantisimo porque sino no te carga los módulos no te funcionará nada ni carga las interfaces de red.
ACCEPT_KEYWORDS="~amd64"



ln -sf /usr/share/zoneinfo/America/Buenos_Aires /etc/localtime
hwclock --systohc
nano /etc/locale.gen # en_US.UTF-8
locale-gen

```   

   
nano /etc/resolv.conf   

**Borrá todo y poné las DNS de Cloudflare o Quad9**. Las DNS de Personal, Claro, Movistar bloquean sitios como: https://librefutbol.su, https://thepiratebay.org, https://example.com, etc
```   
# Cloudflare (no uso porque reporta como Malware sitios para aprender reversing)  
nameserver 1.1.1.1   
nameserver 1.0.0.1   
# Quad9   
9.9.9.9
149.112.112.112
# Quad9 - Otra DNS (Esta uso) (no uso más porque bloquea digdeeper.love)
nameserver 9.9.9.11
nameserver 149.112.112.11
```   
   
```bash   
cp --dereference /etc/resolv.conf /mnt/gentoo/etc` # se usa --dereference para que copie el archivo y no el link simbólico   
arch-chroot /mnt/gentoo` o podes montar uno por uno como está en el Handbook   
source /etc/profile   
export PS1="(chroot) ${PS1}"   
emerge-webrsync # Baja una snapshot de los títulos de los paquetes disponibles, sirve si estás detrás de un firewall (se actualiza cada 24 horas)
rm -rf /etc/portage/gnupg/
emerge --verbose --oneshot app-portage/mirrorselect   
mirrorselect -i -o >> /etc/portage/make.conf   
emerge --sync # Lo mismo que emerge-webrsync pero más actualizado. No hace falta porque emerge-webrsync está bastante actualizado.   
eselect news list   
eselect news read   
eselect profile list   
eselect profile set número (Probablemente ya está seleccionado con asterisco sino: default/linux/amd64/23.0/desktop no usé no-multilib)   
```   
   
###### Agregando el host de paquetes binarios.   
Esta parte la hice igual que como está en el Handbook   
   
   
Este archivo `/etc/portage/binrepos.conf/gentoobinhost.conf` ya está creado pero le cambié la prioridad:   
```console   
[binhost]   
priority = 9999   
sync-uri = https://distfiles.gentoo.org/releases/<arch>/binpackages/<profile>/x86-64/   
```   
   
En el archivo `/etc/portage/make.conf`:    
```bash   
# Appending getbinpkg to the list of values within the FEATURES variable   
FEATURES="${FEATURES} getbinpkg"   
# Require signatures   
FEATURES="${FEATURES} binpkg-request-signature"   
```   
Luego:   
```bash   
getuto   
```   
Para ver las banderas activas: `emerge --info | grep ^USE`   
Luego agregué `USE=""` en /etc/portage/make.conf    
```bash   
emerge --ask --oneshot app-portage/cpuid2cpuflags   
cpuid2cpuflags   
echo "*/* $(cpuid2cpuflags)" > /etc/portage/package.use/00cpu-flags   
```   
   
En el archivo: `/etc/portage/package.use/00video_cards`   
```bash   
*/* VIDEO_CARDS: intel   
```   
   
##### Aceptá la licencia (ya lo hice antes en el `make.conf`)   
Para ver la licencia actual: `portageq envvar ACCEPT_LICENSE`   
Yo usé `ACCEPT_LICENCE="*"` se puede aceptar licencia por cada paquete usando el archivo `/etc/portage/package.license/kernel`.   
Para actualizar: `emerge --ask --verbose --update --deep --newuse --getbinpkg @world --quiet`   
   
Eliminar paquetes obsoletos te muestra una lista: `emerge --ask --pretend --depclean` # Si le sacas `--pretend` los borra.   
   
Configurar fecha y hora:    
```bash   
echo "America/Buenos_Aires" > /etc/timezone   
emerge --config sys-libs/timezone-data   
```   
   
En el archivo `nano /etc/locale.gen` habilitá US locales (es el idioma del sitema operativo).   
```bash   
en_US ISO-8859-1   
en_US.UTF-8 UTF-8   
```   
   
Ejecutá:   
```bash   
locale-gen   
eselect locale list   
eselect locale set 5 (en_US.utf8)   
```   
   
Ahora: `env-update && source /etc/profile && export PS1="(chroot) ${PS1}"`   
   
Ahora instalamos `linux-firmware` (sin esto probablemente no funcionará tu WiFi son los drivers).   
```bash   
emerge -G sys-kernel/linux-firmware   
emerge -G sys-firmware/sof-firmware   
emerge -G sys-firmware/intel-microcode   
```   
   
##### Instalando el GRUB:   
**Para mi esto no lo necesito pero igual lo hice así**:   
En el archivo `/etc/portage/package.use/installkernel` agregá:   
`sys-kernel/installkernel grub dracut`   
   
En el archivo `/etc/portage/package.use/uki` **(Creo que no necesito hacer esto si vas a usar gentoo-kernel-bin)**:   
```bash   
sys-kernel/installkernel dracut uki   
sys-apps/systemd-utils boot kernel-install   
```   
`emerge --ask sys-kernel/installkernel`   
   
Ahora instalamos un "distribution kernel": `emerge -G sys-kernel/gentoo-kernel` o `emerge sys-kernel/gentoo-kernel-bin`   
   
Actualizando y limpiando: `emerge --depclean`   
   
Agregá `USE="dist-kernel"` para reconstruir automáticamente módulos externos instalados por otros paquetes.   
   
```bash   
emerge --config sys-kernel/gentoo-kernel-bin   
```   
   
Podes usar `sys-kernel/modprobed-db` para recolectar información acerca de lo que el sistema requiere: si un control de Xbox es agregado a la instalación `modprobed-db` va a agregar módulos para ser compilados la próxima vez que el kernel es compilado.   
   
Usá `sys-apps/pciutils` que contiene el comando `lspci` para obtener más información del sistema y `lsmod`.   
   
En el handbook explica como compilar el kernel cosa que no lo vamos a hacer.   
   
**Información sobre sistema de archivos**:   
Ejecutá `blkid` para obtener el UUID para construir el `/etc/fstab` o simplemente ejecutá en otra TTY:
```bash
genfstab /mnt/gentoo >> /mnt/gentoo/etc/fstab
```   
En el handbook explica que es cada propiedad del archivo `/etc/fstab`.   
   
Podes agregar `noatime` para mejorar el rendimiento en la partición de raiz (XFS): `defaults,noatime` en `/etc/fstab`.   
   
Agregá el **hostname**: `echo tux > /etc/hostname`   
   
Instalá NetworkManager:    
```bash   
emerge -G NetworkManager   
rc-update add NetworkManager default   
```   
Ahora podes conectarte a una WiFi usando el comando: `nmtui`.   
   
Si no queres usar `NetworkManager` podes usar `netifrc` con `wpa_supplicant`.   
Explicado en el handbook: https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#netifrc_.28OpenRC.29   
   
###### En el archivo `/etc/hosts`:   
```bash   
127.0.0.1	tux.homenetwork	tux	localhost   
::1		tux.homenetwork	tux	localhost   
```   
   
###### Cambiá la contraseña de `root`:    
```bash   
passwd   
```   
   
Cuando usas OpenRC con Gentoo el archivo `/etc/rc.conf` configura los servicios, inicio y apagado de un sistema. Abrí el archivo `/etc/rc.conf` y disfrutá de todos los comentarios en el archivo. Observá las configuraciones y cambia lo que necesitás.   
   
###### Configurá el teclado en el archivo `/etc/conf.d/keymaps`   
Ahí usé `"es"` (teclado Español)   
   
###### En el archivo `/etc/conf.d/hwclock` configurá el reloj:   
Si el reloj de hardware no está usando UTC, entonces es necesario usar `clock="local"` en el archivo. De lo contrario el sistema mostrará un mal comportamiento de reloj.   
   
###### System logger.   
Sysklogd es recomendado para principiantes.   
```bash   
emerge -G app-admin/sysklogd   
rc-update add sysklogd default   
```   
###### Cron daemon.   
```bash   
emerge sys-process/cronie   
rc-update add cronie default   
```   
   
###### File indexing (para búsqueda rápida)   
```bash   
emerge -G --ask sys-apps/mlocate   
```   
   
###### Opcional: Shell para acceso remoto.   
La configuración por defecto de `openssh` no permite ingresar como `root`. Por favor cree un usuario `no-root` y configuralo apropiadamente para permitir el acceso luego de la instalación si es requerido, o ajustá `/etc/ssh/sshd_config` para permitir acceso `root`.   
   
```bash   
rc-update add sshd default   
```   
   
##### Shell completion   
```bash   
emerge app-shells/bash-completion   
```   
   
##### Sincronicación horaria   
```bash   
emerge -G net-misc/chrony # Con -G fijate si está el binario   
rc-update add chronyq default   
```   
   
Es recomendable que `sys-block/io-scheduler-udev-rules` esté instalado para el correcto comportamiento horario (correct scheduler behavior) por ejemplo con dispositivos `nvme`.   
   
```bash   
emerge sys-block/io-scheduler-udev-rules   
```   
   
##### Herramientas de red   
   
No usé Netirfc (https://wiki.gentoo.org/wiki/Netifrc) ni el cliente dhcp, directamente instalé NetworkManager que tiene soporte WiFi (instalación realizada anteriormente).   
El handbook sugiere para WiFi: `emerge net-wireless/iw net-wireless/wpa_supplicant` **pero yo no lo usé**.   
   
##### Eligiendo el `boot loader`   
Podes elegir: GRUB, systemd-boot(usando OpenRC también sirve), EFI Stub.   
   
#### Importante: Si tenes UEFI directamente podes usar EFI STUB porque UEFI no necesita Grub para bootear. Grub es un bootloader secundario. Grub es cómodo ya que con `os-prober` te permite agregar otros sistemas operativos.   
   
```bash   
emerge -G sys-boot/grub   
```   
   
##### Usando `GRUB` como boot loader   
Uso la opción `--removable` porque en algunas placas madres con pobres implementaciones UEFI parece que solo funcionan con el directorio `/BOOT/BOOT` para el archivo `.EFI`. El instalador GRUB crea el `.EFI` archivo en esa ubicación automáticamente agregando la opción `--removable`.   
```bash   
grub-install --target=x86_64-efi --efi-directory=/boot --removable   
```   
###### Si instalaste el binario de `GRUB` ahora lo tendrás que compilar porque el **binario de GRUB no posee la bandera(USE flag) `mount` habilitada**.   
   
En el archivo `/etc/portage/package.use/os-prober` agregá:    
```bash   
>=sys-boot/grub-2.12-r7 mount   
```   
Instalamos OS-PROBER para detectar otras distros.   
```bash   
sudo emerge os-prober    
```   
En el archivo `/etc/default/grub` agregá:   
```bash   
GRUB_DISABLE_OS_PROBER=false   
```   
   
Y ahora:    
```bash   
grub-mkconfig -o /boot/grub/grub.cfg   
```   
En el handbook sugería usar: `grub-mkconfig -o /efi/EFI/Gentoo/grub.cfg` pero yo usé la partición `/boot` (explicado anteriormente).   

Hay una discusión sobre esto:
> Edit: 2024-04-19 20:09 (UTC) Handbook > GRUB > UEFI systems grub-install --efi-directory=/efi installs all files except grubx64.efi in /boot rather than /efi. Is that not a dangerous configuration, that will break for most? I propose recommending `grub-install --efi-directory=/efi --boot-directory=/efi` instead. `grub-mkconfig -o /efi/grub/grub.cfg` doesn't run without symlinking /boot into /efi. I also had to update that command from the wiki provided version using -o /boot/grub/grub.cfg

#### Agregando un usuario.   
El handbook fue muy puto acá: me recomendó un comando para crear el usuario pero sin el grupo `video` y estuve peleando un poco para iniciar `sway`.   
   
**Acá está el comando con el grupo video agregado.**   
```bash   
useradd -m -G users,video,wheel,audio -s /bin/bash esotericwarfare   
passwd esotericwarfare   
```   
   
##### Reiniciando el sistema:   
```bash   
(chroot) livecd # exit   
livecd~# cd   
livecd~# umount -l /mnt/gentoo/dev{/shm,/pts,}   
livecd~# umount -R /mnt/gentoo   
livecd~# reboot   
```   
   
Cuando botea Gentoo, instalé `sudo` y cambié la configuración de `/etc/sudoers`.   
Agregá al final:   
```bash   
esotericwarfare ALL=(ALL:ALL) NOPASSWD:ALL   
```     
Y ahora eliminamos la contraseña del usuario `root` por seguridad:   
```bash   
passwd -l root   
passwd -dl root   
```     
##### Eliminamos los artifactos de instalación.   
```bash   
cd /   
rm stage3-*   
```   
   
Podes consultar cualquier duda en el canal de IRC en LiberaChat: `#gentoo` o en los foros: https://forums.gentoo.org   
   
Cualquier bug: https://bugs.gentoo.org   

##### Para buscar paquetes
```bash
emerge -s hola
```
O con `eix`:
```bash
sudo emerge eix
sudo eix-update
eix wifite
```

### Lista de programas que instalé luego 
```bash
### Binarios
sudo emerge -G sys-devel/bc btop evince falkon gimp imagemagick jq neomutt pcmanfm-qt samba translate-shell wget wl-clipboard xhost xwayland libreoffice mpv git nim thunderbird grim

sudo emerge yt-dlp xdg-desktop-portal-wlr xdg-desktop-portal-wlr vim firefox-bin wmenu telegram-desktop-bin qbittorent tor rclone proxychains unrar unzip tor torsocks os-prober
```

# Actualización 2026

### Intenté instalar Gentoo GNU/Linux con ArchLinux (dual boot)

Si después de toda la instalación al bootear ArchLinux te dice: `Failed to mount /boot` es porque estás usando el kernel de Gentoo para bootear ArchLinux. Tenes que bootear desde le USB Live y montar la particion de ArchLinux y EFI en /mnt/arch y /mnt/arch/boot y arch-chroot /mnt/arch y reinstalar linux `pacman -S linux`  luego ejecutá `grub-mkconfig -o...` pero te va a detectar mal Gentoo tenes que crear un archivo en `/etc/grub.d/40_custom` y agregar manualmente la entrada porque si compartís `/boot` os-prober no lo detecta bien.

Pero cuando intenté botear ArchLinux me decía que el kernel de Gentoo no tiene soporte VFAT, FAT32.
Me olvidé de agregar `"dist-kernel"`.


`emerge gentoo-kernel-bin` no funcionó porque no trae soporte para montar vfat en boot así que no podía bootear mi ArchLinux XD

Tuve que ejecutar:

```bash
emerge sys-kernel/gentoo-sources
eselect kernel list
zcat /proc/config.gz | tee /usr/src/linux/.config
cd /usr/src/linux
make menuconfig
```

Acá mirá como compilé el kernel en Kiss Linux.

```bash
CONFIG_FAT_FS=y
CONFIG_VFAT_FS=y
make -j$(nproc)
make modules_install
make install
grub-mkconfig -o /boot...
``` 

Intenté separar las particiones en `/boot` y `/boot/efi` pero no funcionó. Hice el formateo de `/boot` en ext4 y `/boot/efi` en vfat pero no funcionó igual no pude bootear archlinux.

Encima después de hacer todo eso tuve que reinstalar `gentoo-kernel-bin` pero igual no funcionó tuve que recompilar el kernel. Mientras compilaba el kernel usé los binarios de archlinux (hice un chroot).


Luego me dí cuenta(me lo dijo Claude AI) que no era necesario bootear montando la partición `/boot`, así que la saqué del `/etc/fstab` y boteo archlinux.

#### Esto hice para repararlo:

Desde Gentoo monté `/boot` corrí grub-install (creo que no era necesario) e instalé gentoo-kernel-bin con `/boot` montado al terminar de instalar `gentoo-kernel-bin` me instaló estos archivos: `vmlinuz-6.18.2-p1-gentoo-dist, System.map-6.18.2-p1-gentoo-dist, initramfs-6.18.2-p1-gentoo-dist.img`.

Luego desde ArchLinux USB Live monté la partición de ArchLinux con `arch-chroot` y monté el `/boot` en `/mnt/arch/boot` y ejecuté `sudo pacman -S linux` luego me copió estos archivos al `/boot`: `vmlinuz-linux initramfs-linux.img`.

```bash
grub-install --target=x86_64-efi --efi-directory=/boot --removable   
mkdir /dev/sda4 /mnt/gentoo # Para que lo detecte.
grub-mkconfig -o /boot/grub/grub.cfg   
```


---

En el proceso me quedo una particion como `swap` cambie la etiqueta de esta forma (estaba formateado como ext4 no me equivoque).

Para cambiar el tipo de partición de swap a Linux filesystem en la tabla de particiones GPT, puedes usar `fdisk` o `gdisk`. Te muestro ambas opciones:

## Usando fdisk

```bash
sudo fdisk /dev/sda
```

Luego dentro de fdisk:
1. Presiona `t` (para cambiar el tipo)
2. Escribe `3` (número de partición)
3. Escribe `20` o busca el código con `L` (Linux filesystem)
4. Presiona `w` para escribir los cambios y salir


---


`grub-mkconfig` detecta mi particion pero me pone mal el parametro en el `/boot/grub/grub.cfg` archlinux esta bien pero gentoo no

```bash
### BEGIN /etc/grub.d/30_os-prober ###
menuentry 'Gentoo Linux (on /dev/sda3)' --class gentoo --class gnu-linux --class gnu --class os $menuentry_id_option 'osprober-gnulinux-simple-78b556fb-5a81-40ab-b8f2-29d5527e3120' {
        insmod part_gpt
        insmod fat
        set root='hd0,gpt1'
        if [ x$feature_platform_search_hint = xy ]; then
          search --no-floppy --fs-uuid --set=root --hint-bios=hd0,gpt1 --hint-efi=hd0,gpt1 --hint-baremetal=ahci0,gpt1  BE8B-209C
        else
          search --no-floppy --fs-uuid --set=root BE8B-209C
        fi
        linux /vmlinuz-linux root=UUID=9f4c187a-f57d-4686-805d-89d82f99e536 rw loglevel=3 quiet
        initrd /initramfs-linux.img
}
```
pero no deberia usar vmlinuz ni initramfs ese es el de archlinux deberia usar estos:

```bash
[I] esotericwarfare@arch ~> ls /boot
config-6.18.2-p1-gentoo-dist  grub                                 initramfs-linux.img               vmlinuz-6.18.2-p1-gentoo-dist
EFI                           initramfs-6.18.2-p1-gentoo-dist.img  System.map-6.18.2-p1-gentoo-dist  vmlinuz-linux
[I] esotericwarfare@arch ~>
```

### Solucion

Los archivos de Gentoo están en `/boot` de la partición EFI (que es compartida), no en `/dev/sda3/boot`. 

Aquí está la entrada correcta para Gentoo:

```bash
sudo vim /etc/grub.d/40_custom
```

#### Agrega esto (si cambiás la particion tenes que cambiar el UUID).

```bash
menuentry 'Gentoo Linux' --class gentoo --class gnu-linux --class gnu --class os {
    insmod part_gpt
    insmod ext2
    set root='hd0,gpt3'
    if [ x$feature_platform_search_hint = xy ]; then
      search --no-floppy --fs-uuid --set=root --hint-bios=hd0,gpt3 --hint-efi=hd0,gpt3 --hint-baremetal=ahci0,gpt3  78b556fb-5a81-40ab-b8f2-29d5527e3120
    else
      search --no-floppy --fs-uuid --set=root 78b556fb-5a81-40ab-b8f2-29d5527e3120
    fi
    linux (hd0,gpt1)/vmlinuz-6.18.2-p1-gentoo-dist root=UUID=78b556fb-5a81-40ab-b8f2-29d5527e3120 rw
    initrd (hd0,gpt1)/initramfs-6.18.2-p1-gentoo-dist.img
}
```

La clave es que el kernel y el initramfs están en **(hd0,gpt1)** que es tu partición EFI `/dev/sda1`, pero el root filesystem es **/dev/sda3**.

Luego regenera grub:

```bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

Esto debería crear la entrada correcta apuntando a los archivos de Gentoo que están en la partición EFI compartida.


### Os prober falla cuando tenes compartido el /boot segun Claude AI

Sí, **debería ser automático**, pero `os-prober` tiene limitaciones y a veces falla en detectar correctamente las configuraciones. En tu caso específico:

## Por qué falló os-prober:

1. **Kernel en partición EFI compartida**: `os-prober` detectó que Gentoo está en `/dev/sda3`, pero no se dio cuenta de que el kernel de Gentoo está en `/dev/sda1` (la partición EFI compartida). Asumió que el kernel estaría en `/boot` dentro de `/dev/sda3`.

2. **Encontró kernels de Arch en /boot**: Cuando montó la partición EFI (que está en `/boot` de Arch), encontró `vmlinuz-linux` e `initramfs-linux.img` y los usó por defecto para la entrada de Gentoo.

3. **Configuración de dual-boot compleja**: Tener ambos sistemas compartiendo la misma partición EFI con diferentes kernels confunde a `os-prober`, que está diseñado para casos más simples donde cada distro tiene su `/boot` separado.

## Esto es común cuando:
- Compartes `/boot` (EFI) entre múltiples distros
- Los nombres de kernel no siguen convenciones estándar
- Gentoo usa kernels compilados manualmente con nombres personalizados

## Alternativas para hacerlo más automático:

Si quieres que sea más automático en el futuro, podrías:
- Usar `grub-customizer` (interfaz gráfica)
- Mantener las entradas manuales en `/etc/grub.d/40_custom` (lo más confiable)
- Configurar Gentoo con su propio `/boot` en `/dev/sda3/boot` en lugar de usar la EFI compartida

En resumen: **sí debería ser automático, pero tu configuración es más compleja de lo que os-prober maneja bien**.



# Recomendaciones de Claude AI de software alternativo.


Aquí están las alternativas **ligeras** para reducir tiempos de compilación en Gentoo:

## Alternativas Ligeras

### Navegadores con JavaScript
- **netsurf** - Muy ligero, tiene JavaScript básico
- **dillo** (ya lo tienes) - Sin JS pero ultra rápido
- **links2** con `-g` - Modo gráfico, sin JS pero mejor que w3m
- **surf** - Basado en webkit, minimalista
- **qutebrowser** - Usa QtWebEngine (compila, pero menos que Firefox/Chromium)

### Alternativas a MPV (más ligeras)
- **mplayer** - Clásico, menos dependencias
- **vlc** - Opcional, pero compila menos que mpv con todas las features
- **ffplay** (viene con ffmpeg) - Minimalista extremo

### Alternativas a Samba
- **NFS** (nfs-utils) - Protocolo nativo Unix/Linux, mucho más simple
- **SSHFS** (fuse-sshfs) - Compartir carpetas vía SSH
- **syncthing** - P2P, sin servidor central
- **rsync** vía SSH - Para transferencias puntuales (ya lo tienes)

### Otras Optimizaciones

**Puedes eliminar/simplificar:**
- ~~chromium~~ (tarda HORAS) → netsurf o mantén firefox si es crítico
- ~~obs-studio~~ → ffmpeg (ya lo mencionaste) + wf-recorder para Wayland
- ~~kdenlive~~ → **openshot** o **shotcut** (más ligeros)
- ~~libreoffice~~ → **abiword** + **gnumeric** (mucho más ligeros)
- ~~gimp~~ → **mtpaint** o **feh** + imagemagick para edición básica
- ~~thunderbird~~ → Ya tienes neomutt (perfecto)
- ~~qemu-full~~ → qemu con menos targets específicos

### Para Gentoo específicamente

En `/etc/portage/make.conf`:
```bash
# Usa binarios precompilados para los paquetes más pesados
EMERGE_DEFAULT_OPTS="--binpkg-respect-use=y --getbinpkg=y"

# Reduce paralelismo si te quedas sin RAM
MAKEOPTS="-j4"  # ajusta según tu CPU

# USE flags minimalistas
USE="-X -gtk -qt5 -gnome -kde minimal"
```

**Paquetes que puedes usar binarios en Gentoo:**
- Firefox/Chromium (disponibles como `firefox-bin`, `chromium-bin`)
- Rust toolchain
- LLVM/Clang

### Respuesta a tu setup específico

**Para JavaScript ligero:** `netsurf` o `surf` son tus mejores opciones

**Para Samba:** Si es para compartir archivos con Windows → mantén samba. Si es solo Linux-Linux → usa **NFS** o **SSHFS**

**Para MPV:** `mplayer` o simplemente usa `ffplay` para casos básicos

¿Qué tipo de uso le das a samba y mpv? Te puedo dar una recomendación más específica.


---


El problema es que Gentoo compila optimizado para tu CPU específica, pero necesitas configurarlo correctamente. Con un **Intel Celeron N2806** (Bay Trail, arquitectura Silvermont), aquí está la configuración óptima:

## Configuración para `/etc/portage/make.conf`

```bash
# CPU específica para Intel Celeron N2806 (Bay Trail)
COMMON_FLAGS="-march=silvermont -O2 -pipe"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
FCFLAGS="${COMMON_FLAGS}"
FFLAGS="${COMMON_FLAGS}"

# Tu CPU tiene 2 cores, usa -j3 (cores + 1)
MAKEOPTS="-j3 -l2"

# Video Drivers para Intel Bay Trail
VIDEO_CARDS="intel i965"

# Input devices
INPUT_DEVICES="libinput"

# USE flags mínimos (ajusta según necesites)
USE="X alsa pulseaudio -gnome -kde -systemd minimal"

# Licencias aceptadas
ACCEPT_LICENSE="*"

# Para ahorrar espacio
FEATURES="parallel-fetch candy"

# Locale
L10N="en es"
```

## Por qué compila para AMD

Probablemente tu `make.conf` tiene:
- `-march=native` → Esto **debería** funcionar, pero a veces detecta mal
- `-march=x86-64` → Genérico, no optimizado
- Algún USE flag con `video_cards_amdgpu` o `video_cards_radeon`

## Verificación

```bash
# Ver qué arquitectura está usando
gcc -march=native -Q --help=target | grep march

# Debería mostrar: -march= silvermont

# Ver USE flags de video
emerge --info | grep VIDEO_CARDS
```

## Advertencia: Tu Hardware es MUY limitado

**Celeron N2806 + 3.7GB RAM** es muy débil para compilar en Gentoo. Recomendaciones:

### 1. Usa Stage3 Precompilado
```bash
# Al instalar, usa stage3 con binarios
# https://www.gentoo.org/downloads/

# En make.conf agrega:
EMERGE_DEFAULT_OPTS="--binpkg-respect-use=y --getbinpkg=y"
FEATURES="${FEATURES} getbinpkg"
```

### 2. Cross-Compile desde otra máquina
Si tienes otra PC más potente, compila ahí y copia los binarios.

### 3. Usa distcc (compilación distribuida)
Si tienes otra máquina en la red.

### 4. Alternativa más realista: **Void Linux**
Con tu hardware, considera:
- **Void Linux** → Binarios precompilados, musl/glibc, muy minimalista
- **Alpine Linux** → Ultra ligero, musl libc
- **Artix Linux** → Arch sin systemd, binarios precompilados

### Paquetes que NO compiles en tu Celeron
Estos te matarán (horas/días):
- ❌ chromium (8-12 horas)
- ❌ firefox (4-8 horas) → usa `firefox-bin`
- ❌ libreoffice (6-10 horas)
- ❌ qtwebengine (8-15 horas)
- ❌ rust (2-4 horas)
- ❌ llvm/clang (4-8 horas)

```bash
# Instala versiones binarias
emerge firefox-bin chromium-bin
```

## Mi recomendación honesta

Con un Celeron N2806 y 3.7GB RAM:

1. **Gentoo NO es la mejor opción** para uso diario
2. Si quieres aprender Gentoo → VM en otra máquina
3. Para este hardware → **Void Linux** o **Artix** son perfectos
4. Si insistes en Gentoo → Usa **máximo binarios** y crossdev

¿Quieres que te ayude a configurar Void Linux en su lugar? Es igual de minimalista pero con binarios---


El problema es que Gentoo compila optimizado para tu CPU específica, pero necesitas configurarlo correctamente. Con un **Intel Celeron N2806** (Bay Trail, arquitectura Silvermont), aquí está la configuración óptima:

## Configuración para `/etc/portage/make.conf`

```bash
# CPU específica para Intel Celeron N2806 (Bay Trail)
COMMON_FLAGS="-march=silvermont -O2 -pipe"
CFLAGS="${COMMON_FLAGS}"
CXXFLAGS="${COMMON_FLAGS}"
FCFLAGS="${COMMON_FLAGS}"
FFLAGS="${COMMON_FLAGS}"

# Tu CPU tiene 2 cores, usa -j3 (cores + 1)
MAKEOPTS="-j3 -l2"

# Video Drivers para Intel Bay Trail
VIDEO_CARDS="intel i965"

# Input devices
INPUT_DEVICES="libinput"

# USE flags mínimos (ajusta según necesites)
USE="X alsa pulseaudio -gnome -kde -systemd minimal"

# Licencias aceptadas
ACCEPT_LICENSE="*"

# Para ahorrar espacio
FEATURES="parallel-fetch candy"

# Locale
L10N="en es"
```

## Por qué compila para AMD

Probablemente tu `make.conf` tiene:
- `-march=native` → Esto **debería** funcionar, pero a veces detecta mal
- `-march=x86-64` → Genérico, no optimizado
- Algún USE flag con `video_cards_amdgpu` o `video_cards_radeon`

## Verificación

```bash
# Ver qué arquitectura está usando
gcc -march=native -Q --help=target | grep march

# Debería mostrar: -march= silvermont

# Ver USE flags de video
emerge --info | grep VIDEO_CARDS
```

## Advertencia: Tu Hardware es MUY limitado

**Celeron N2806 + 3.7GB RAM** es muy débil para compilar en Gentoo. Recomendaciones:

### 1. Usa Stage3 Precompilado
```bash
# Al instalar, usa stage3 con binarios
# https://www.gentoo.org/downloads/

# En make.conf agrega:
EMERGE_DEFAULT_OPTS="--binpkg-respect-use=y --getbinpkg=y"
FEATURES="${FEATURES} getbinpkg"
```

### 2. Cross-Compile desde otra máquina
Si tienes otra PC más potente, compila ahí y copia los binarios.

### 3. Usa distcc (compilación distribuida)
Si tienes otra máquina en la red.

### 4. Alternativa más realista: **Void Linux**
Con tu hardware, considera:
- **Void Linux** → Binarios precompilados, musl/glibc, muy minimalista
- **Alpine Linux** → Ultra ligero, musl libc
- **Artix Linux** → Arch sin systemd, binarios precompilados

### Paquetes que NO compiles en tu Celeron
Estos te matarán (horas/días):
- ❌ chromium (8-12 horas)
- ❌ firefox (4-8 horas) → usa `firefox-bin`
- ❌ libreoffice (6-10 horas)
- ❌ qtwebengine (8-15 horas)
- ❌ rust (2-4 horas)
- ❌ llvm/clang (4-8 horas)

```bash
# Instala versiones binarias
emerge firefox-bin chromium-bin
```

## Mi recomendación honesta

Con un Celeron N2806 y 3.7GB RAM:

1. **Gentoo NO es la mejor opción** para uso diario
2. Si quieres aprender Gentoo → VM en otra máquina
3. Para este hardware → **Void Linux** o **Artix** son perfectos
4. Si insistes en Gentoo → Usa **máximo binarios** y crossdev

¿Quieres que te ayude a configurar Void Linux en su lugar? Es igual de minimalista pero con binarios..


---


---

# Guía de Optimización Gentoo - Celeron N2806

## 🚨 PROBLEMAS CRÍTICOS DETECTADOS

### 1. **VIDEO_CARDS incorrectos**
Tu `make.conf` tiene:
```
VIDEO_CARDS="amdgpu fbdev intel nouveau radeon radeonsi vesa dummy"
```

**INCORRECTO** - Estás compilando drivers AMD/Nouveau que NO USAS.

**Tu CPU tiene Intel HD Graphics (Bay Trail/Gen7)**
```bash
VIDEO_CARDS="intel i965"
```

### 2. **Profile Desktop cuando usás TTY puro**
```
[3] default/linux/amd64/23.0/desktop (stable) *
```

**CAMBIAR A:**
```bash
eselect profile set 1  # default/linux/amd64/23.0
```

El profile desktop instala X11, GTK, Qt - 100% innecesario para TTY.

### 3. **Muchos paquetes GUI instalados**
Detectados en tu sistema:
- `x11-libs/*` (todo X11)
- `kde-frameworks/*`
- `gnome-base/*`
- `dev-qt/*` (Qt5/Qt6)
- `x11-apps/*`

**Estos NO deberían estar en TTY puro.**

### 4. **LLVM compilado localmente (CRÍTICO)**
Tienes `llvm-core/llvm` y `llvm-core/clang` - esto tarda 8-12 horas en compilar.

**NUNCA compiles LLVM en este CPU.**

---

## ✅ PASOS INMEDIATOS

### 1. Cambiar Profile
```bash
eselect profile set 1
```

### 2. Limpiar USE flags globales
Editar `/etc/portage/make.conf`:
```bash
USE="dist-kernel minimal -X -gtk -qt5 -qt6 -kde -gnome -wayland -dbus"
```

### 3. Forzar binarios para paquetes pesados
Crear `/etc/portage/package.env`:
```bash
# Forzar binarios
llvm-core/llvm nobuild.conf
llvm-core/clang nobuild.conf
dev-lang/rust nobuild.conf
sys-devel/gcc nobuild.conf
dev-qt/qtwebengine nobuild.conf
```

Crear `/etc/portage/env/nobuild.conf`:
```bash
# Rechazar compilación local
FEATURES="${FEATURES} -test"
ACCEPT_KEYWORDS="~amd64"
```

### 4. Instalar binarios críticos
```bash
# LLVM/Clang precompilado
emerge --oneshot --getbinpkg llvm-core/llvm llvm-core/clang

# Rust precompilado
emerge dev-lang/rust-bin

# Eliminar rust source si existe
emerge -C dev-lang/rust
```

---

## 🔥 PAQUETES QUE **NUNCA** COMPILAR

### Tiempo de compilación estimado en tu CPU:

| Paquete | Tiempo | Acción |
|---------|--------|--------|
| `chromium` | 10-15h | ❌ Imposible |
| `firefox` | 6-10h | ❌ Usa `firefox-bin` |
| `llvm` | 8-12h | ❌ Usa binarios |
| `rust` | 4-6h | ❌ Usa `rust-bin` |
| `qtwebengine` | 8-12h | ❌ Usa binarios |
| `libreoffice` | 8-10h | ❌ Evitar o binario |
| `gcc` | 3-5h | ⚠️ Binario si es posible |
| `webkit-gtk` | 6-8h | ❌ Evitar |

---

## 🎯 ALTERNATIVAS LIGERAS

### Navegadores
```bash
# TTY puro
emerge www-client/lynx     # ~2 min
emerge www-client/w3m      # ~3 min

# Si necesitas JS básico
emerge www-client/netsurf  # ~15 min
```

### Editor
```bash
# Ya tienes vim (bien)
emerge app-editors/nano    # ~1 min
```

### Herramientas de desarrollo
```bash
# Git sin GUI
echo "dev-vcs/git -gtk -perl" >> /etc/portage/package.use/dev

# Python sin Tkinter
echo "dev-lang/python -tk" >> /etc/portage/package.use/dev
```

---

## 🚀 OPTIMIZACIONES ADICIONALES

### 1. CCACHE (recomendado)
```bash
emerge dev-util/ccache

# En make.conf
FEATURES="${FEATURES} ccache"
CCACHE_DIR="/var/cache/ccache"
CCACHE_SIZE="2G"
```

### 2. Tmpfs para compilación (si tienes RAM)
**NO RECOMENDADO con 3.7GB RAM** - usarías swap constantemente.

### 3. Binhost custom (avanzado)
Si tienes otra máquina más potente:
```bash
# En la máquina potente
FEATURES="${FEATURES} buildpkg"

# En tu Celeron
PORTAGE_BINHOST="http://192.168.x.x:8080"
```

### 4. eix para búsquedas rápidas
```bash
emerge app-portage/eix
eix-update
```

---

## 📊 ESTIMACIÓN DE TIEMPOS

### Actualización del sistema completo:
- **Con optimizaciones**: 4-8 horas
- **Sin optimizaciones**: 24-48 horas
- **Mundo ideal (100% binarios)**: 1-2 horas

### Primera instalación (desde stage3):
- **Con profile desktop**: 3-5 días
- **Con profile minimal + binarios**: 12-24 horas

---

## ⚠️ ADVERTENCIA FINAL

Tu Celeron N2806 es 10 años viejo y muy débil. Gentoo en este hardware es **extremadamente lento** para compilar.

### Recomendación sincera:

1. **Si querés aprender Gentoo**: Usa una VM en otra PC
2. **Si querés velocidad**: Usa Void Linux o Alpine
3. **Si insistís en Gentoo**: Usa 90% binarios precompilados

### Void Linux (alternativa recomendada):
- Binarios precompilados
- xbps (gestor rápido)
- Runit init (más simple que OpenRC)
- Musl libc (más ligero)
- Instalación: 30 minutos

```bash
# Void Linux instalación típica
xbps-install vim git lynx alsa-utils
# Total: ~5 minutos
```

vs Gentoo:
```bash
emerge vim git lynx alsa-utils
# Total: 2-3 horas (con dependencias)
```

---

## 🔧 COMANDOS ÚTILES

### Ver qué se está compilando
```bash
genlop -c
```

### Estimar tiempo de compilación
```bash
genlop -pt llvm
```

### Ver paquetes que tardan más
```bash
genlop -t | sort -k5 -n | tail -20
```

### Limpiar sistema
```bash
emerge --depclean
eclean-dist --deep
eclean-pkg --deep
```

### Actualizar con binarios
```bash
emerge --update --deep --newuse --getbinpkg @world
```

---

## 📝 CHECKLIST FINAL

- [ ] Cambiar profile a minimal (no desktop)
- [ ] Corregir VIDEO_CARDS (solo intel i965)
- [ ] Limpiar USE flags globales
- [ ] Forzar binarios para LLVM/Clang/Rust
- [ ] Instalar ccache
- [ ] Eliminar paquetes X11 innecesarios
- [ ] Configurar MAKEOPTS="-j2 -l2"
- [ ] Usar --getbinpkg en emerge
- [ ] Considerar seriamente Void Linux

¿Querés que te ayude con algún paso específico?


---


### Mirar de OpenRC a Systemd (por los binarios)

Tienes razón, déjame darte una guía más precisa y segura para migrar de OpenRC a systemd en Gentoo.

## Migración de OpenRC a systemd - Guía Completa

### Paso 1: Verifica tu perfil actual y elige uno con systemd

```bash
# Ver perfil actual y opciones disponibles
eselect profile list
```

Busca un perfil que incluya "systemd" (ejemplo: `default/linux/amd64/23.0/desktop/systemd` o similar según tu arquitectura).

```bash
# Cambia al perfil systemd apropiado
eselect profile set <número_del_perfil_systemd>
```

### Paso 2: Configura USE flags en make.conf

Edita `/etc/portage/make.conf`:

```bash
# Asegúrate de tener estos USE flags
USE="systemd -elogind -sysv-utils"
```

**Importante**: No añadas `-consolekit` a menos que lo tengas activo (está obsoleto).

### Paso 3: Actualiza @world con los nuevos USE flags

```bash
# Esto reconstruirá paquetes con las nuevas dependencias
emerge --ask --verbose --update --deep --newuse @world
```

Este paso instalará systemd y reconstruirá paquetes que necesitan cambiar de elogind a systemd.

### Paso 4: Elimina los paquetes de OpenRC que conflictúan

**IMPORTANTE**: No hagas esto hasta después de que el paso 3 haya instalado systemd exitosamente.

```bash
# Verifica que systemd esté instalado primero
emerge --search sys-apps/systemd

# Luego desinstala los paquetes conflictivos
emerge --deselect sys-apps/sysvinit
emerge --ask --depclean
```

### Paso 5: Configura el bootloader para usar systemd

**Para GRUB:**

Edita `/etc/default/grub` y modifica o añade:

```bash
GRUB_CMDLINE_LINUX="init=/lib/systemd/systemd"
```

Luego regenera la configuración:

```bash
grub-mkconfig -o /boot/grub/grub.cfg
```

**Para systemd-boot u otros**: Consulta la documentación específica.

### Paso 6: Configuración básica de systemd

```bash
# Establece el hostname
hostnamectl set-hostname tu-hostname

# Configura la zona horaria
timedatectl set-timezone America/Mexico_City  # o tu zona

# Habilita servicios básicos que probablemente necesitas
systemctl enable systemd-networkd    # O NetworkManager si lo usas
systemctl enable systemd-resolved    # DNS
systemctl enable systemd-timesyncd   # NTP
```

### Paso 7: Migra servicios de OpenRC a systemd

Revisa qué servicios tenías habilitados en OpenRC:

```bash
# Antes de reiniciar, lista servicios de OpenRC
rc-update show
```

Habilita los equivalentes en systemd. Ejemplos comunes:

```bash
# Si usabas NetworkManager
systemctl enable NetworkManager

# Si usabas dhcpcd
systemctl enable dhcpcd

# Si usabas sshd
systemctl enable sshd

# Para interfaz gráfica
systemctl enable display-manager  # o gdm, sddm, lightdm, etc.
```

### Paso 8: Limpieza final (ANTES de reiniciar)

```bash
# Limpia paquetes huérfanos
emerge --ask --depclean

# Verifica que no haya problemas
revdep-rebuild
```

### Paso 9: Reinicia

```bash
reboot
```

### Paso 10: Verificación post-reinicio

Después de reiniciar, verifica:

```bash
# Confirma que systemd está corriendo
ps --no-headers -o comm 1
# Debería mostrar "systemd"

# Verifica servicios activos
systemctl status

# Verifica logs
journalctl -b
```

## Notas importantes:

1. **No desinstales OpenRC/sysvinit ANTES de tener systemd funcionando** - podrías dejar tu sistema sin init
2. **Haz un backup o snapshot** antes de empezar
3. **No reinicies hasta completar todos los pasos** - especialmente la configuración del bootloader
4. Si usas NetworkManager, asegúrate de habilitarlo en systemd antes de reiniciar o podrías perder conectividad de red
5. El archivo `/etc/portage/package.use/` que creaste antes para elogind ya no será necesario, puedes eliminarlo después

## Si algo sale mal:

En el bootloader (GRUB), puedes agregar `init=/bin/bash` temporalmente para arrancar en modo emergencia y corregir problemas.


emerge --ask --verbose --update --deep --newuse @world --binpkg-respect-use=n


Perfecto, el sistema está listo para la actualización. Aquí está lo que va a pasar:

## Análisis de la salida

**Buenas noticias:**
- ✅ Se van a **instalar 2 paquetes que resuelven conflictos** (los "uninstalls")
- ✅ 45 paquetes binarios disponibles (instalación rápida)
- ✅ Los conflictos están satisfechos
- ✅ No hay errores de bloqueo críticos

**Sobre los binarios ignorados:**
Los binarios ignorados son porque tienen USE flags diferentes a tu configuración actual. Esos paquetes se compilarán desde source en lugar de usar binarios - es normal.

## Qué hacer:

### Opción 1: Proceder normalmente (Recomendado)

```bash
Yes
```

Esto instalará los paquetes. Los binarios con USE flags incompatibles se compilarán desde source.

### Opción 2: Forzar uso de binarios (más rápido pero menos preciso)

Si quieres usar los binarios aunque tengan USE flags diferentes:

```bash
No  # Cancela primero
```

Luego ejecuta:

```bash
emerge --ask --verbose --update --deep --newuse --binpkg-respect-use=n @world
```
## Después de que termine:

Una vez completado exitosamente, continúa con el **Paso 4** de la guía anterior:

```bash
# Verifica que systemd esté instalado
emerge --search sys-apps/systemd

# Limpia paquetes obsoletos
emerge --ask --depclean

# Configura GRUB

Acá hay un problema. Yo ejecuto grub-mkconfig desde archlinux así que no me va a tomar `GRUB_CMDLINE_LINUX="init=/usr/lib/systemd/systemd"` porque os-prober no detecta, vas a tener que escribirlo manualmente desde `/etc/grub.d/40_custom`

En vez de hacer esto:

```bash
vim /etc/default/grub  # Añade init=/lib/systemd/systemd
```

Hace esto:

```bash
vim /etc/grub.d/40_custom
menuentry 'Gentoo Linux' --class gentoo --class gnu-linux --class gnu --class os {
        insmod part_gpt
        insmod ext2
        set root='hd0,gpt3'
        if [ x$feature_platform_search_hint = xy ]; then
          search --no-floppy --fs-uuid --set=root --hint-bios=hd0,gpt3 --hint-efi=hd0,gpt3 --hint-baremetal=ahci0,gpt3  3fe2e015-ef10-4d2f-81b2-ba299be39370
        else
          search --no-floppy --fs-uuid --set=root 3fe2e015-ef10-4d2f-81b2-ba299be39370
        fi
        linux (hd0,gpt1)/vmlinuz-6.18.2-p1-gentoo-dist root=UUID=3fe2e015-ef10-4d2f-81b2-ba299be39370 rw init=/usr/lib/systemd/systemd
        initrd (hd0,gpt1)/initramfs-6.18.2-p1-gentoo-dist.img
}

Agregá al final de linux init=/usr/lib/systemd/systemd


grub-mkconfig -o /boot/grub/grub.cfg
```

Despues de pasar a systemd intente instalar Falkon y me puteaba por "Paquete bloqueado".

I can see you're encountering a package conflict in Gentoo between `systemd` and `elogind`. This is a common issue when trying to install packages that depend on elogind while your system is configured to use systemd.

The problem is:
- Your system currently has **systemd** installed (which provides init system and session management)
- You're trying to install **falkon** (a web browser), which pulls in dependencies that want **elogind** instead

**Solution: Reconfigure pipewire and wireplumber to use systemd**

Since your system uses systemd, you need to adjust the USE flags for the conflicting packages:

```bash
# Add these lines to /etc/portage/package.use/pipewire
media-video/pipewire -elogind systemd
media-video/wireplumber -elogind systemd
sys-auth/polkit -elogind systemd
```

Then try the installation again:

```bash
emerge --ask --verbose www-client/falkon
```

**Alternative: If you prefer a simpler approach**

You can also add this to your global USE flags in `/etc/portage/make.conf`:

```bash
USE="systemd -elogind"
```

This tells Portage to prefer systemd over elogind system-wide.

**Why this happens:**
- Gentoo allows you to choose between systemd and elogind for session management
- Some packages can work with either one, but both cannot be installed simultaneously
- The binary packages you're trying to install were compiled with elogind support, but your system expects systemd

After making these changes, the dependency resolver should be able to find a compatible solution without the blocking conflict.

Option 2: Request different binaries
If you're using Gentoo's official binpkgs or a custom binary host, you need binaries compiled with systemd -elogind instead. Check:

What binary package repository are you using? (/etc/portage/binrepos.conf)
Can you switch to a systemd-based binary repository?

arch / # cat /etc/portage/binrepos.conf/gentoobinhost.conf 
# These settings were set by the catalyst build script that automatically
# built this stage.
# Please consider using a local mirror.
[gentoobinhost]
priority = 1
sync-uri = https://distfiles.gentoo.org/releases/amd64/binpackages/23.0/x86-64
arch / #


Ah, now I see the issue! You're using Gentoo's official binary package repository for the **23.0/x86-64 profile**, which is OpenRC-based (uses elogind), but your system is configured for systemd.

**Solution: Switch to the systemd binary package repository**

Edit `/etc/portage/binrepos.conf/gentoobinhost.conf`:

```bash
[gentoobinhost]
priority = 1
sync-uri = https://distfiles.gentoo.org/releases/amd64/binpackages/23.0/x86-64-systemd
```

Notice the change: `x86-64` → `x86-64-systemd`

Then update your binary package index:

```bash
emaint binhost --fix
emerge --sync
# Or if using getuto:
getuto
```

Now try installing falkon again:

```bash
emerge --ask --verbose www-client/falkon
```

The systemd binary repository should have packages compiled with `systemd -elogind` USE flags that match your system configuration.

**Note:** Make sure your profile is also set to a systemd profile. Check with:
```bash
eselect profile list
```

You should be using something like `default/linux/amd64/23.0/systemd` rather than just `default/linux/amd64/23.0`.



---

 * IMPORTANT: 27 news items need reading for repository 'gentoo'.
 * Use eselect news read to view new items.

Calculating dependencies  .... ... done!
Dependency resolution took 33.86 s (backtrack: 0/20).

[binary  N     ] x11-misc/compose-tables-1.8.12-1 
[binary  N     ] llvm-core/llvm-common-21.1.8-1  USE="-emacs -verify-sig" 
[binary  N     ] x11-themes/hicolor-icon-theme-0.17-1 
[binary  N     ] acct-group/colord-0-r2-1 
[binary  N     ] acct-group/pipewire-0-r2-1 
[binary  N     ] acct-group/polkitd-0-r3-1 
[binary  N     ] x11-themes/sound-theme-freedesktop-0.8-r1-1 
[binary  N     ] app-text/iso-codes-4.18.0-1 
[binary  N     ] media-libs/alsa-topology-conf-1.2.5.1-1 
[binary  N     ] media-libs/alsa-ucm-conf-1.2.14-1 
[binary  N     ] x11-misc/xkeyboard-config-2.46-1  USE="-test" 
[binary  N     ] x11-base/xorg-proto-2024.1-1  USE="-test" 
[binary  N     ] dev-qt/qttranslations-6.10.1-1  USE="-custom-cflags" 
[binary  N     ] dev-libs/wayland-protocols-1.45-1  USE="-test" 
[binary  N     ] acct-group/lpadmin-0-r3-1 
[binary  N     ] acct-user/polkitd-0-r3-1 
[binary  N     ] acct-user/colord-0-r2-1 
[binary   R    ] sys-libs/zlib-1.3.1-r1-17  USE="minizip*" ABI_X86="32*" 
[binary   R    ] virtual/zlib-1.3.1-r1-2  ABI_X86="32*" 
[binary  N     ] media-libs/alsa-lib-1.2.14-3  USE="-debug -doc -python" ABI_X86="(64) -32 (-x32)" PYTHON_SINGLE_TARGET="-python3_11 -python3_12 -python3_13" 
[binary  N     ] dev-libs/icu-77.1-2  USE="-debug -doc -examples -static-libs -test -verify-sig" ABI_X86="32 (64) (-x32)" 
[binary  N     ] media-libs/libogg-1.3.6-1  USE="-static-libs" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/lcms-2.17-2  USE="-doc -jpeg -static-libs -test -tiff" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/libltdl-2.5.4-1  USE="-static-libs" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/wayland-1.24.0-1  USE="-doc -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libICE-1.1.2-3  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/nspr-4.37-1  USE="-debug" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/opus-1.5.2-4  USE="-custom-modes -debug -deep-plc -doc -dred -hardened -osce -static-libs -test" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="sse" 
[binary  N     ] dev-lang/orc-0.4.41-1  USE="-gtk-doc -static-libs -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/libatomic_ops-7.8.4-2  ABI_X86="(64) (-32) (-x32)" 
[binary  N     ] net-libs/libasyncns-0.8-r4-7  USE="-debug -doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXau-1.0.12-3  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXdmcp-1.1.5-5  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] app-arch/snappy-1.2.2-r1-2  USE="-test" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="-avx -avx2" 
[binary  N     ] dev-lang/duktape-2.7.0-r3-1 
[binary  N     ] media-libs/flac-1.5.0-4  USE="cxx -debug -ogg -static-libs" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="-avx -avx2" 
[binary  N     ] media-sound/lame-3.100-r3-7  USE="frontend -debug -mp3rtp -sndfile -static-libs" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="(-mmx)" 
[binary  N     ] dev-util/spirv-tools-1.4.328.0-1  USE="-test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libxshmfence-1.3.3-3  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/double-conversion-3.4.0-1  USE="-test" 
[binary  N     ] dev-libs/md4c-0.5.2-2  USE="md2html -test" 
[binary  N     ] app-text/libpaper-2.1.3-1 
[binary  N     ] dev-libs/libevdev-1.13.5-1  USE="-doc -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] sys-libs/mtdev-1.1.7-1 
[binary  N     ] media-libs/speexdsp-1.2.1-7  ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="sse sse2" 
[binary  N     ] dev-cpp/abseil-cpp-20250512.1-2  USE="-test -test-helpers" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] virtual/minizip-1.3.1-1  USE="-static-libs" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libxcb-1.17.0-6  USE="xkb -doc (-selinux) -test" ABI_X86="(64) -32 (-x32)" 
[binary   R    ] dev-libs/libxml2-2.15.1-8  USE="icu*" ABI_X86="32*" PYTHON_TARGETS="-python3_13*" 
[binary  N     ] media-libs/libvorbis-1.3.7-r2-2  USE="-static-libs -test" ABI_X86="(64) -32 (-x32)" 
[binary     UD ] x11-libs/libdrm-2.4.127-2 [2.4.131] USE="-udev*" VIDEO_CARDS="amdgpu* nouveau* radeon*" 
[binary  N     ] media-libs/libwebp-1.6.0-2  USE="jpeg png -gif -opengl -static-libs -swap-16bit-csp -tiff" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="sse2 -avx2 -sse4_1" 
[binary  N     ] dev-libs/nss-3.112.2-3  USE="utils -cacert -test -test-full" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="-avx2 -sse3" 
[binary  N     ] dev-db/mysql-connector-c-8.0.36-3  USE="-ldap -static-libs" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/webrtc-audio-processing-1.3-r3-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libX11-1.8.12-1  USE="-doc -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libxkbcommon-1.12.3-2  USE="X -doc -static-libs -test -tools -wayland" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/xcb-util-0.4.1-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/xcb-util-keysyms-0.4.1-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/xcb-util-renderutil-0.3.10-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/libcanberra-0.30-r8-6  USE="-alsa -gstreamer -oss -pulseaudio -tdb -udev" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] app-eselect/eselect-lua-4-r1-1 
[binary  N     ] media-libs/libtheora-1.2.0-r1-1  USE="encode -doc -examples -static-libs" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/xcb-util-wm-0.4.2-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXext-1.3.6-6  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXfixes-6.0.2-1  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXrender-0.9.12-3  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXcomposite-0.4.6-6  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXdamage-1.1.6-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/xcb-util-image-0.4.1-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libxkbfile-1.1.3-6  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-lang/lua-5.4.8-1  USE="deprecated readline" 
[binary  N     ] app-eselect/eselect-mpg123-0.1-r1-1 
[binary  N     ] media-libs/libglvnd-1.7.0-6  USE="X -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXrandr-1.5.4-6  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXi-1.8.2-3  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXxf86vm-1.1.6-3  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXv-1.0.13-3  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-sound/mpg123-base-1.33.3-3  USE="ipv6 -alsa (-coreaudio) -int-quality -jack -nas -oss -portaudio -pulseaudio -sdl" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="sse (-3dnow) (-3dnowext) (-mmx)" 
[binary  N     ] x11-libs/xcb-util-cursor-0.1.6-1  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXcursor-1.2.3-3  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXtst-1.2.5-3  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/libsndfile-1.2.2-r2-16  USE="-alsa -minimal -sqlite -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/libepoxy-1.5.10-r3-4  USE="X -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] virtual/opengl-8-1  USE="(X)" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/glu-9.0.3-1  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] virtual/glu-9.0-r2-1  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/freeglut-3.6.0-r1-2  ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/tiff-4.7.0-r1-11  USE="cxx jpeg lzma opengl webp zlib zstd -jbig -lerc -libdeflate -static-libs -test -verify-sig" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/openjpeg-2.5.3-r1-3  USE="-doc -test" ABI_X86="(64) -32 (-x32)" 
[binary   R    ] media-libs/freetype-2.14.1-r1-10  USE="harfbuzz*" 
[binary  N     ] llvm-core/llvm-20.1.8-28  USE="binutils-plugin debug libffi zstd (-debuginfod) -doc -exegesis -libedit -test -verify-sig -xml -z3" ABI_X86="(64) -32 (-x32)" LLVM_TARGETS="(AArch64) (AMDGPU) (ARM) (AVR) (BPF) (Hexagon) (Lanai) (LoongArch) (MSP430) (Mips) (NVPTX) (PowerPC) (RISCV) (SPIRV) (Sparc) (SystemZ) (VE) (WebAssembly) (X86) (XCore) -ARC -CSKY -DirectX -M68k -Xtensa" 
[binary  N     ] llvm-core/llvm-toolchain-symlinks-20-r1-2  USE="-multilib-symlinks -native-symlinks" 
[binary  N     ] llvm-core/llvm-21.1.8-6  USE="binutils-plugin debug libffi xml zstd (-debuginfod) -doc -exegesis -libedit -test -verify-sig -z3" ABI_X86="(64) -32 (-x32)" LLVM_TARGETS="(AArch64) (AMDGPU) (ARM) (AVR) (BPF) (Hexagon) (Lanai) (LoongArch) (MSP430) (Mips) (NVPTX) (PowerPC) (RISCV) (SPIRV) (Sparc) (SystemZ) (VE) (WebAssembly) (X86) (XCore) -ARC -CSKY -DirectX -M68k -Xtensa" 
[binary  N     ] llvm-core/llvmgold-21-1 
[binary  N     ] llvm-core/llvm-toolchain-symlinks-21-1  USE="-multilib-symlinks -native-symlinks" 
[binary  N     ] media-libs/mesa-25.2.7-2  USE="X llvm (opengl) proprietary-codecs sysprof vulkan wayland zstd -debug -lm-sensors -opencl -test -unwind -vaapi -valgrind -vdpau" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="sse2" LLVM_SLOT="20 -18 -19" VIDEO_CARDS="intel nouveau radeon radeonsi -asahi -d3d12 (-freedreno) -lavapipe (-lima) -nvk (-panfrost) -r300 -r600 (-v3d) (-vc4) -virgl (-vivante) -vmware -zink" 
[binary  N     ] x11-libs/libSM-1.2.6-1  USE="uuid -doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/libusb-1.0.29-1  USE="udev -debug -doc -examples -static-libs -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/libXft-2.3.9-1  USE="-doc" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/libinput-1.29.1-1  USE="-doc -test" INPUT_DEVICES="-wacom" 
[binary  N     ] virtual/libusb-1-r2-1  USE="udev" ABI_X86="(64) -32 (-x32)" 
[binary   R    ] x11-libs/cairo-1.18.4-r1-24  USE="X*" 
[binary  N     ] net-print/cups-2.4.14-8  USE="acl pam -X -dbus -debug -kerberos -openssl (-selinux) -static-libs -systemd -test -usb -xinetd -zeroconf" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-misc/xdg-utils-1.2.1-r9-6  USE="-X -dbus -doc -gnome -perl -plasma" 
[binary  N     ] gnome-base/gsettings-desktop-schemas-48.0-2  USE="introspection" 
[binary  N     ] kde-frameworks/breeze-icons-6.20.0-1  USE="-test" 
[binary  N     ] kde-frameworks/kf-env-6-1 
[binary  N     ] media-libs/libpulse-17.0-3  USE="X asyncns glib -dbus -doc -gtk (-selinux) -systemd -test -valgrind" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-sound/pulseaudio-daemon-17.0-r1-4  USE="X alsa alsa-plugin asyncns gdbm glib orc ssl udev webrtc-aec -aptx -bluetooth -dbus (-elogind) -equalizer -fftw -gstreamer -jack -ldac -lirc -ofono-headset (-oss) (-selinux) -sox (-system-wide) -systemd -tcpd -test -valgrind -zeroconf" 
[binary  N     ] media-plugins/alsa-plugins-1.2.12-4  USE="mix pulseaudio usb_stream -arcam_av -debug -ffmpeg -jack -libsamplerate -oss -speex" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] sys-auth/elogind-255.17-r1-1  USE="acl pam policykit -audit -cgroup-hybrid -debug -doc (-selinux) -test" 
[binary  N     ] sys-auth/polkit-126-r2-8  USE="introspection nls pam -examples -gtk -kde (-selinux) -systemd -test" 
[binary  N     ] x11-libs/gdk-pixbuf-2.42.12-4  USE="introspection -gif -gtk-doc -jpeg -test -tiff" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/gstreamer-1.24.11-5  USE="caps introspection nls -ptp -test -unwind" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/graphene-1.10.8-r1-5  USE="introspection -doc -test" ABI_X86="(64) -32 (-x32)" CPU_FLAGS_X86="sse2" 
[binary  N     ] net-libs/libproxy-0.5.11-2  USE="gnome introspection -duktape -gtk-doc -test -vala" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] app-accessibility/at-spi2-core-2.56.5-6  USE="introspection -X -dbus-broker -gtk-doc -systemd -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/libgudev-238-r2-3  USE="introspection -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-libs/json-glib-1.10.8-2  USE="introspection nls -gtk-doc -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-libs/pango-1.57.0-3  USE="X introspection sysprof -debug -examples -gtk-doc -test" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-util/gtk-update-icon-cache-3.24.42-1 
[binary  N     ] dev-libs/libgusb-0.4.9-6  USE="introspection -gtk-doc -test -vala" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] gnome-base/librsvg-2.60.0-6  USE="introspection -debug -gtk-doc -test -vala" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-libs/gst-plugins-base-1.24.11-r1-16  USE="X alsa egl gles2 introspection nls ogg opengl orc pango theora vorbis -gbm -ivorbis -test -wayland" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-misc/colord-1.4.8-4  USE="introspection -argyllcms -examples -extra-print-profiles -gtk-doc -scanner (-selinux) -systemd -test -vala" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] x11-themes/adwaita-icon-theme-legacy-46.2-1 
[binary  N     ] x11-themes/adwaita-icon-theme-48.1-2  USE="-branding" 
[binary  N     ] x11-libs/gtk+-3.24.51-5  USE="X colord cups introspection sysprof wayland (-aqua) -broadway -cloudproviders -examples -gtk-doc -test -vim-syntax -xinerama" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] dev-qt/qtbase-6.10.1-3  USE="X concurrent cups dbus gtk gui icu libinput libproxy mysql network nls opengl sql sqlite ssl udev vulkan wayland widgets xml (zstd) -accessibility -brotli -custom-cflags -eglfs -evdev -gles2-only -gssapi -journald -oci8 -odbc -postgres -renderdoc -sctp -syslog -test -tslib" 
[binary  N     ] dev-qt/qtsvg-6.10.1-1  USE="-custom-cflags -test" 
[binary  N     ] kde-frameworks/karchive-6.20.0-1  USE="crypt zstd -debug -test" 
[binary  N     ] dev-qt/qtshadertools-6.10.1-1  USE="-custom-cflags -test" 
[binary  N     ] dev-qt/qtdeclarative-6.10.1-r1-2  USE="jit network opengl sql ssl svg vulkan widgets -accessibility -custom-cflags -qmlls" 
[binary  N     ] dev-qt/qtwebchannel-6.10.1-1  USE="qml -custom-cflags -test" 
[binary  N     ] dev-qt/qt5compat-6.10.1-1  USE="gui icu qml -custom-cflags -test" 
[binary  N     ] media-video/pipewire-1.4.9-r1-4  USE="X dbus gstreamer readline ssl systemd -bluetooth -doc -echo-cancel (-elogind) -extra -ffmpeg -fftw -flatpak -gsettings -ieee1394 -jack-client -jack-sdk -liblc3 -loudness -lv2 -man -modemmanager -pipewire-alsa -roc (-selinux) -sound-server (-system-service) -test -v4l -zeroconf" ABI_X86="(64) -32 (-x32)" 
[binary  N     ] media-video/wireplumber-0.5.12-2  USE="(elogind) -doc (-system-service) -systemd -test" LUA_SINGLE_TARGET="lua5-4 -lua5-3" 
[binary  N     ] dev-qt/qtwebengine-6.10.1-3  USE="alsa bindist jumbo-build opengl pdfium pulseaudio qml screencast system-icu vulkan widgets -accessibility -custom-cflags -designer -geolocation -kerberos -test -vaapi -webdriver" 
[binary  N     ] www-client/falkon-25.08.3-2  USE="X dbus -debug -kde -python -test" PYTHON_SINGLE_TARGET="python3_13 -python3_11 -python3_12" 
[blocks B      ] sys-apps/systemd ("sys-apps/systemd" is soft blocking sys-auth/elogind-255.17-r1)

[31;01m * [39;49;00mError: The above package list contains packages which cannot be
[31;01m * [39;49;00minstalled at the same time on the same system.

