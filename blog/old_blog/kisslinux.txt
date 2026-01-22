---
title: "Kiss Linux (compilar kernel manualmente)"
date: 2025-06-25T02:43:44-03:00
tags: ['linux']
---
![](data:image/png;base64,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)

Primero boteá ArchLinux descargá la ISO de acá: https://archlinux.org/download/

Quemá la ISO en un pendrive usando
```bash
dd if=archlinux.iso of=/dev/sdb status=progress bs=4098
```

https://kisslinux.github.io Está obsoleto, el creador desapareció pero la comunidad de KISS decidió forkearlo acá: https://kisscommunity.org/kiss/install/

Al bootear ArchLinux particionemos el disco.
###### legacy boot sin swap
Si estás en una VM podes directamente crear una única partición
```bash
o
n
p
1
Enter
Enter
w
```

###### uefi (gpt) con Swap
```bash
g (gpt disk label)
n
1 (partition number [1/128])
2048 first sector
+300M last sector (boot sector size)
t
1 (EFI System)
n
2
default
+4G
t
2
swap
n
3
default (fill up partition)
default (fill up partition)
w (write)
```

Descargá el último release **kiss-chroot** de acá: https://codeberg.org/kiss-community/repo/releases
Extraélo como `root`. 

###### Instalación en Legacy Boot en UEFI tendrás que crear una partición EFI con `mkfs.fat -F 32` (explicado en el artículo de ArchLinux)
```bash
mkfs.ext4 /dev/sda1 
mount /dev/sda1 /mnt
cd /mnt
lynx https://kisscommunity.org/kiss/install/
De ahí dale a `latest-release` bajá hasta donde dice `Downloads` y descargá `kiss-chroot-24.12.18.tar.xz`, **Download and Save to Disk**.
tar xvf kiss-chroot-24.12.18.tar.xz # Descomprimí como root
genfstab -U /mnt >> /mnt/etc/fstab
bin/kiss-chroot .
```
En el archivo `/etc/profile.d/kiss_path.sh` 

vi `/etc/profile.d/kiss_path.sh`: 
```bash
export REPOS_DIR='/var/db/kiss'
export KISS_PATH=''
KISS_PATH=$KISS_PATH:$REPOS_DIR/repo/core
KISS_PATH=$KISS_PATH:$REPOS_DIR/repo/extra
KISS_PATH=$KISS_PATH:$REPOS_DIR/repo/wayland
KISS_PATH=$KISS_PATH:$REPOS_DIR/community/community

export CFLAGS="-O2 -march=native"
export CXXFLAGS="$CFLAGS"
export MAKEFLAGS="-j2"

export KISS_SU=su
```

Cargamos las variables:
```bash
cp /etc/profile.d/kiss_path.sh .profile
source ~/.profile
echo $KISS_PATH
cd /var/db/kiss
git clone https://codeberg.org/kiss-community/repo
git clone https://codeberg.org/kiss-community/community
cd repo
git config gpg.ssh.allowedSignersFile .allowed_signers
git config merge.verifySignatures true
kiss update
cd /var/db/kiss/installed && kiss build *  
kiss b e2fsprogs dosfsprogs xfsprogs util-linux dhcpcd libelf ncurses perl baseinit
# Quedó obsoleto eudev
mkdir -p /etc/rc.d
echo "dhcpcd 2> /dev/null" > /etc/rc.d/dhcpcd.boot
echo kiss > /etc/hostname
vi /etc/hosts
127.0.0.1   kiss
ping kiss
cd /var/db/kiss
```
Descargá el linux kernel: 
```bash
lynx kernel.org
Latest Release - Download
tar xvf linux-*
cd linux-*
```

Es recomendable bootear con ArchLinux porque carga todo lo que necesitás para que tu sessión sea exitosa, ahora todos los módulos están cargados en la memoria si ejecutás: 
```bash
lspci -k
```
Verás que el ethernet está cargado, etc. Es un buen comienzo pero no es todo.
Ahora podes descargar `linux-firmware` pero en este caso lo omnitiremos.
Primero tenemos que crear la configuración por defecto del kernel
```bash
make defconfig
```
Si ejecutamos:
```bash
make help
```
Encontrarás un argumento llamado `localyesconfig (update current config converting local mods to core)`
```bash
make localyesconfig
```

Hay que habilitar `CONFIG_FRAMEBUFFER_CONSOLE`

Sacale una foto o una screenshot a la salida de ese comando para buscar uno por uno más rápido.

Ese comando convierte lo que está en memoria cargado con ArchLinux pero se da cuenta de que no está configurado todavía, así que no puedo convertirlo lo que significa que lo necesito.
Parece mucho pero hay varios `sub-modulos`.
Ejemplo: `pata_acpi` si copiás `CONFIG_PATA_ACPI` (podes copiar si habilitas el mouse systemctl start gpm en otra consola lo pegas con botón derecho).
```bash
make menuconfig
/ (slash)
CONFIG_PATA_ACPI
```
Te dice `[=n]` y abajo en `Depends: ` y en `Selects: [=n]` (esa tenes que seleccionarlo y habilitarlo con `*` para que quede todo en `[=y]`)

Si apretás el número lo podes convertir como `core` si lo pones con `*`(asterisco) - Save - Exit - Exit

Ahora ejecutá:
```bash
make localyesconfig
```
Si lo hiciste bien debería haber desaparecido el mensaje.
###### Lo mismo con todos los demás siempre guardá, salí y mirá si el mensaje desapareció ejecutando `make localyesconfig`...
Con bluetooth hay un problema BT es una subsección no es algo... `BT [=n]` dice no para habilitar esas cosas, cuando ves eso posponelo.
Dice `[=n]` pero si mirás abajo en `Selects:` dice: `CRC16[=y] && CRYPTO[=y]...` tiene varias habilitadas pero para que quede habilitado `BT [=n]` todo debería estar en `[=y]`.
Pero si copias el que dice `[=n] (CRYPTO_ECB)` haces una búsqueda no lo encontrarás porque no es un módulo, es una opción.
###### Por eso es mejor omnitirlo el `bluetooth`
Si es una sección es mejor no tocarla y mientras hacés las demás esa sección desaparecerá.
Si no ves un número al buscar, no podes hacer nada ignoralo y habilitando los demás desaparecerá el mensaje.

VMware usa `CONFIG_SND_EN5171` 

Hacé lo mismo para cada `CONFIG_`

#### A veces si haces una búsqueda y ponés el nombre completo: `CONFIG_...` no lo encuentra pero si pones la mitad del nombre si lo encuentra.

Al final cuando ejecutás `make localyesconfig` no te debería salir ningun mensaje solo:
```bash
using config: .config
```

Ahora que hicimos todo los modulos:
```bash
make menuconfig
``` 
Si vez `Kernel .config support` con un `<M>` 

Deshabilitá en `General Setup - Initial RAM filesystem and RAM disk (initramfs/initrd) support`  
En `Processor type and features - Processor family` seleccioná `Core 2/newer Xeon`.
En `General setup - Default hostname - kiss` 
En `device drives - USB support`
En `filesystem` debería estar habilitado `ext4`.

```bash
make -j $(nproc)
# Ignorá el mensaje Cannot find LILO 
make install  
mv /boot/vmlinuz    /boot/vmlinuz-VERSION  
mv /boot/System.map /boot/System.map-VERSION 
# Fijate que esté bien el fstab
cat /etc/fstab
kiss b grub
Legacy BOOT
Desde KISS Linux
sudo grub-install /dev/sda --recheck
grub-mkconfig -o /boot/grub/grub.cfg
Desde ArchLinux
grub-install --boot-directory=/mnt/boot /dev/sda --recheck
```

Descargá el `linux-firwamre`:
```bash
cd /usr/lib
git clone https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
```

Si estás en VirtualBox abrí la configuración en Experto y en Display poné `Graphics Controller` en `VBoxsSVGA`
.
Ahora en el archivo `/etc/default/grub` agregamos en la línea `GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet nomodeset"`

```bash
vi /etc/default/grub
+GRUB_CMDLINE_LINUX_DEFAULT="loglevel=3 quiet nomodeset # (no carga los drivers de video)
grub-mkconfig -o /boot/grub/grub.cfg
passwd
adduser esotericwarfare
addgroup esotericwarfare audio
addgroup esotericwarfare video
addgroup esotericwarfare input
exit
exit
reboot
```

Con `lspci -k` podes ver que módulos cargó.

```bash
dhcpcd # Levantar network
cd /var/db/kiss/community/community - Paquetes disponibles en el repositorio
ls 
```

Probamos si podemos instalar un paquete.
```bash
kiss b neofetch
neofetch
```

---

Agregado.


El built me tardo 10 horas
Desde ArchLinux
```bash
root@archiso ~ # grub-install --efi-directory=/mnt/boot --boot-directory=/mnt/boot --target=x86_64-efi --bootloader-id=grub_uefi  --removable
```
Agrega `kiss b grub lm-sensors links` al comienzo

2:42 AM

La compilacion del kernel me tardo 2 horas y 40 minutos

El `linux-firmware` pesa 2.4g

Habilita todos estos y nodemodeset en el `GRUB_CMDLINE`
```bash
CONFIG_FB 
CONFIG_FRAMEBUFFER_CONSOLE
CONFIG_FB_EFI
CONFIG_FB_VESA
```

#### Cuando bootee no tenia imagen pero igual podia escribir usuario: root y la clave y apagar mi computadora o pude ver videos con mpv e iniciar el entorno gráfico con `seatd-launch sway` esto lo hice despues de bootear la máquina usando `nomodeset` e instalar los siguientes paquetes:


Los primeros paquetes que instale despues de iniciar Linux.
##### Es mejor compilar los paquetes uno por uno porque recien los instala luego de compilarlo, si compilas varios paquetes recien los instalara cuando termine de compilar el ultimo paquete.
```
kiss b openssh imagemagick qpdf lm-sensors links vis vim mpv swayfx swagbg firefox-privacy links
(root) pip install yt-dlp
```

Tuve que compilar `irssi` desde la págian porque no estaa en el repo de kiss ni el de community.

###### Estuvo 3 dias 12 horas horas compilando LLVM y Clang SPIRV tools para instalar 2 paquetes: mpv y sway!! En una Intel Celeron N2806 Dual Core 1.6GHz
```bash
addgroup esotericwarfare audio
addgroup esotericwarfare video
addgroup esotericwarfare input
```


Clang 04:09 AM - 38%




Para instalar el driver `i915`: 
```bash
su
git clone ...linux-firware /usr/bin/firmware
cd /var/db/kiss/linux-VERSION
make menuconfig
Device Driver
Generic Driver Options
Firmware loader
```
Ahi en `Firmware blobs root directory` agregue: `/lib/firmware` y en `Build named firmware blobs into the kernel binary` puse `*` (Aunque no deberia hacer eso sino elegir una por una la que tengo que usar.)


### Como solucionar los problemas
Si no funciona nada fijate si podes escribir el usuario y contraseña en ciego y ejecutar y luego bootealo con `nomodeset`.
```bash
dmesg > dmesg.txt
```

Para instalar las fonts de sway: `kiss b terminus-font`.


Estos son los paquetes que estan en el repositorio de `community`:

```bash
9base abduco aerc age amfora aml android-tools appstream apulse aria2 asciinema autoconf autoconf-archive automake axel bandwhich bash bat bc bemenu birch
bit-bin boost bottom brlaser brotli btop btrfs-progs bubblewrap cantarell-fonts catgirl cava ccrypt cfm chicken cloc cmark-gfm cmus containerd coreutils
cproc crosstool-ng cryptsetup ctags cups cups-filters curlpp darkhttpd dash dejavu-ttf delta dialog discount diskonaut djvulibre dmidecode docker docker-buildx
docker-compose-bin dogefetch dvtm ecl elinks emacs emacs-compat emacs-kiss-git emacs-tsort entr erlang evremap evtest exa execline exfatprogs exiftool
extra-cmake-modules falkon fdk-aac fdm fff fftw file flac flatpak fmt fnf fortune fossil freeglut fuse fuse2 fzy gawk gc gcompat gdb ghostscript girara github-cli
globe-cli glorytun glow-bin gnu-netcat gnupg1 gnupg2 gnutls go go-bootstrap go-ipfs goimports gopls gperf gpgme gphoto2 groff gron-git gsl gspt gt5 gtar gtest
guile3 guile3-fibers-git gumbo-parser hack hexyl hostapd htop hugo hummingbird-git icu idmap imagemagick imath inih iniparser init-hooks iosevka-nerd-fonts
iperf iproute2 iptables isync iw jbig2dec jo jq json-glib kak-lsp-bin kakoune kexec-tools keyutils kfc kiss-find kmod lcms ldns less libaio libarchive
libassuan libatomic_ops libbpf libburn libcap libconfig libcupsfilters libdvdcss libedit libev libevent libexif libgcrypt libgpg-error libgphoto2 libisoburn
libisofs libjpeg libksba libmupdf libnl libpcap libportaudio2 libppd libpsl libseccomp libsixel libslirp libsndfile libsodium libssh libtermkey libtool libtorrent
libunistring liburing libusb libutemper libuv libvncserver libwebsockets libxdp libxml2 libxmlb libxslt libyaml limine links lm-sensors lpeg lsof lua luajit lux lvm2
lz4 lzo mblaze mdev-usb mediainfo mg minikube mksh mosh msgpack-c msmtp mtools mtpaint mtr nano nawk-git ncdu1 neatvnc neofetch neomutt neovim nettle nmap npth
nq nsd ntfs-3g numactl oksh openjpeg2 openntpd optipng ostree ox pandoc-bin pash patch patchelf pciutils perl pfetch pick pinentry pipewire pkcs11-helper pmount
poppler poppler-data popt pounce powertop pqiv procps-ng protobuf protobuf-c pv pybind11 pystring qbe qemu qpdf qrencode qt5 qt5-declarative qt5-svg qt5-wayland
qt5-webchannel qt5-webengine ranger readline reptyr retrogram-rtlsdr ripgrep rsync rtorrent ruby runc runit rustup-bin s6 s6-linux-init s6-rc sane sbase sbcl sc
sc-im sccache scenefx scrcpy scroll scryer-prolog sdl2 secret sed sed-i senpai sfeed sgt-puzzles shellcheck-bin shepherd shfm shfmt-bin shinit sinit slang slides
slirp4netns smu-karlb spotify-player spotifyd squashfs-tools sudo swappy swaybg swayfx swayidle swaylock swww syncthing sysmgr tcc tdb tea terminus-font tiff tig
tinygo-bin tinyramfs-git tiv tmate tmux tokei totp transmission tre tree ttf-font-awesome ttf-jetbrains-mono ttyd tuitube twemoji-color-font typescript-language-server
uacme ubase ugrep umurmur unbound unzip uthash virglrenderer vis viu vmwh vundle wayvnc wireguard-tools wireless_tools wl-clipboard wl-screenrec wlr-randr
wmenu xxd yajl yarn yash yasm yt-dlp ytfzf zathura zathura-cb zathura-djvu zathura-pdf-mupdf zathura-pdf-poppler zig-bin zip zls-bin zsh zzz
```

Paquetes que esta en el repo de `repo/extra` (tiene 2 mas: core y wayland)
```bash
adwaita-icon-theme alsa-lib alsa-utils bkeymaps cairo cbindgen ccache clang cmake cyrus-sasl dhcpcd dosfstools e2fsprogs efibootmgr efivar eiwd expat
ffmpeg firefox firefox-privacy fontconfig freetype-harfbuzz gdk-pixbuf glib gnugrep gtk+3 hicolor-icon-theme hwdata intel-vaapi-driver json-c kirc lame
libass libclc libdisplay-info libelf libepoxy libffi libjpeg-turbo libnl-tiny libogg libplacebo libpng libretls libtheora libudev-zero libva
libva-utils libvorbis libvpx libwebp llvm man-pages mandoc mdevd mesa meson mold mpv mutt nasm ncurses nodejs nspr nss opendoas openresolv openssh opus
pango pcre2 pkgconf python python-docutils python-flit-core python-glad python-gpep517 python-installer python-jinja2 python-mako python-markupsafe
python-packaging python-setuptools python-wheel python-yaml rust samurai scdoc skalibs spirv-headers spirv-llvm-translator spirv-tools sqlite ssu
strace ttf-croscore tzdata util-linux vim wpa_supplicant x264 x265 xvidcore zstd
```

---

Acá fue cuando ejecuté `make localyesconfig` en la carpeta del kernel descargado y fui habilitando uno por uno los `CONFIG_` saqué una foto porque eran demasiados.


[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMuPo4ZkXF4xlEXDwZW1ewbB8tntT23bPEXg66nyI2CQ-2GrC_KAL0zJh17k_dTqPjSNt6WxJ2CwIL485VBx5frF8aWegT8gDOwmRXQHVHu4tHh4ZX-LHtia1j03gZRPWtbIOidIBmKD1svsz3qZa5w_cmjESmAvQgJwZ0Dw3edLU9EhBESK0coGKdJBv_/s320/IMG_20250626_194303066.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhMuPo4ZkXF4xlEXDwZW1ewbB8tntT23bPEXg66nyI2CQ-2GrC_KAL0zJh17k_dTqPjSNt6WxJ2CwIL485VBx5frF8aWegT8gDOwmRXQHVHu4tHh4ZX-LHtia1j03gZRPWtbIOidIBmKD1svsz3qZa5w_cmjESmAvQgJwZ0Dw3edLU9EhBESK0coGKdJBv_/s4160/IMG_20250626_194303066.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLIUWBg6lqcZxg7CGijLeeqjvpW3qc5aDYwPO7FFy4mJewquiZ2N75FkkwN6TOkIHgha4_NUkigVX3wNsFqgoEeloUHknLG9fRUKEDvWNImfAKLwxYnd0UqbezI-V-pW8yCxlFL8Xd4mBLO9hVMQtPVbJPgHrKgfGTQjhlukVD7WM__qrkNUoo4wdbWQzR/s320/IMG_20250626_195009956.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLIUWBg6lqcZxg7CGijLeeqjvpW3qc5aDYwPO7FFy4mJewquiZ2N75FkkwN6TOkIHgha4_NUkigVX3wNsFqgoEeloUHknLG9fRUKEDvWNImfAKLwxYnd0UqbezI-V-pW8yCxlFL8Xd4mBLO9hVMQtPVbJPgHrKgfGTQjhlukVD7WM__qrkNUoo4wdbWQzR/s4160/IMG_20250626_195009956.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBSl-f_sWvW3On9Td1IITlsqwmOZeSZMFfLxz9hsGFjkmUCiraWtH7hDnefIHXPBZLnSrP-9wBjLEs6LKmpgKR9C2DwNmVCHo8nfpOfUOH2zSQ-7dmGMKqrUwgG4HXvUCs30A0nzofIgyOeFNmvbq0mIPniYWkQsnQYjPBB9Kv9DKlVlsJ_TfkxTIpzY69/s320/IMG_20250626_195746460.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBSl-f_sWvW3On9Td1IITlsqwmOZeSZMFfLxz9hsGFjkmUCiraWtH7hDnefIHXPBZLnSrP-9wBjLEs6LKmpgKR9C2DwNmVCHo8nfpOfUOH2zSQ-7dmGMKqrUwgG4HXvUCs30A0nzofIgyOeFNmvbq0mIPniYWkQsnQYjPBB9Kv9DKlVlsJ_TfkxTIpzY69/s4160/IMG_20250626_195746460.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbu7312OwsMgIGt33z9K6na9Kjeznh_gl7vL0pU-Wte-XxygnbnVx_jN69hn8IJ0c7ps7OgliZM1GRulE8tIAz7W0BmN50T1uTd4CYrTjQkarvYMTTX7vJeKeWHTxrj_eSi7nmmbWyIDTGyaowDtKZ-UMz5Xhn8S6YPMEwbs6Z2XI5G47mbn6O4rAInwQr/s320/IMG_20250627_212721959.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjbu7312OwsMgIGt33z9K6na9Kjeznh_gl7vL0pU-Wte-XxygnbnVx_jN69hn8IJ0c7ps7OgliZM1GRulE8tIAz7W0BmN50T1uTd4CYrTjQkarvYMTTX7vJeKeWHTxrj_eSi7nmmbWyIDTGyaowDtKZ-UMz5Xhn8S6YPMEwbs6Z2XI5G47mbn6O4rAInwQr/s4160/IMG_20250627_212721959.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg6JVSu-1Cd8p6m66FLqLqzsDAGwNidIl8xpFKNvXBDqGE2uhwq3WWSdNI9ZXX0Ey5t7Zy8WOUVgFZ0ZZX-hwDXWVgukhFgUmQAFoTIhewde0TheabT6ryMhWVtlJ6QVR9nBMa4X9sV_5PmwSa0ap-HXcdGKKFXzC4-ZaMAcLmSZVUXw2Zb0LfOj9QQnUH/s320/IMG_20250628_121352880.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjg6JVSu-1Cd8p6m66FLqLqzsDAGwNidIl8xpFKNvXBDqGE2uhwq3WWSdNI9ZXX0Ey5t7Zy8WOUVgFZ0ZZX-hwDXWVgukhFgUmQAFoTIhewde0TheabT6ryMhWVtlJ6QVR9nBMa4X9sV_5PmwSa0ap-HXcdGKKFXzC4-ZaMAcLmSZVUXw2Zb0LfOj9QQnUH/s4160/IMG_20250628_121352880.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfbh4fPIuuQ17Dyk5sC2Xh1iryfHz28ukyiF9xoPxvWngADCAtRsX7IxMuTtTqhcCSWMWDhCrFX_kJ01tN855GjdF0VScuXOALDZrIGXA9fSCmOqLCZdTMd61oNd58lmXBmLCnpWNBF4tyytvF1iCj6gOd1uswBBoxx60X2lNzC6iyqup0StEbXPuNT9Wu/s320/IMG_20250628_172336385.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfbh4fPIuuQ17Dyk5sC2Xh1iryfHz28ukyiF9xoPxvWngADCAtRsX7IxMuTtTqhcCSWMWDhCrFX_kJ01tN855GjdF0VScuXOALDZrIGXA9fSCmOqLCZdTMd61oNd58lmXBmLCnpWNBF4tyytvF1iCj6gOd1uswBBoxx60X2lNzC6iyqup0StEbXPuNT9Wu/s4160/IMG_20250628_172336385.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPtex-tkwrxVl1FAEKwkiZKK_GsYSjvG2ZoyTT3K3_9Rmzc0ZjxAjgfCmMcl7eAsyw2Wfa285VUCi4FVQOBBSFZscJlH0mVgnxzyusPK8a-kLWLgb0acAK48yS8TOE5GVmZvdMicza8CZ-zVRYy9QmxAGw-f67q_xInzDULCnaqb5mNrm6tMyvixS_eyAs/s320/IMG_20250629_015151598.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiPtex-tkwrxVl1FAEKwkiZKK_GsYSjvG2ZoyTT3K3_9Rmzc0ZjxAjgfCmMcl7eAsyw2Wfa285VUCi4FVQOBBSFZscJlH0mVgnxzyusPK8a-kLWLgb0acAK48yS8TOE5GVmZvdMicza8CZ-zVRYy9QmxAGw-f67q_xInzDULCnaqb5mNrm6tMyvixS_eyAs/s4160/IMG_20250629_015151598.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizgFx1FxNSs4Q2gPVw25oGUEV-livnmYxNhLQnixnI0fOEfPlbYuJmYVcGi4Pyob-2DFCmc_wCPkqNDdpJSiyFs1dsV_WWkzJK19cj9OYRvFrFWO_z7hAvvsRz8cs_kdcDJfwBcMGknPI7kq9vjV1B9aWcfg-J3qBqUy4fDmxnWNvVKenw4xg-RATro6ch/s320/IMG_20250629_020616031.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEizgFx1FxNSs4Q2gPVw25oGUEV-livnmYxNhLQnixnI0fOEfPlbYuJmYVcGi4Pyob-2DFCmc_wCPkqNDdpJSiyFs1dsV_WWkzJK19cj9OYRvFrFWO_z7hAvvsRz8cs_kdcDJfwBcMGknPI7kq9vjV1B9aWcfg-J3qBqUy4fDmxnWNvVKenw4xg-RATro6ch/s4160/IMG_20250629_020616031.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUaSV2QtsOhCLYhJNVXfaNjonLRJvANV_knJQRiptVKGnleWLD3dpRNKe2097jxBQ5SwdzYSQU6fyT7C_LBDatnRfwt-B1GGW5YbUkY8NzZG8HqW_8OKf_eywXbRei-wCAN_77eBvcZVAYLV7bn6X3YWGuc8OkYMzkXwIGvViJonw9f7kbK7GytOX1EV54/s320/IMG_20250629_021438204.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgUaSV2QtsOhCLYhJNVXfaNjonLRJvANV_knJQRiptVKGnleWLD3dpRNKe2097jxBQ5SwdzYSQU6fyT7C_LBDatnRfwt-B1GGW5YbUkY8NzZG8HqW_8OKf_eywXbRei-wCAN_77eBvcZVAYLV7bn6X3YWGuc8OkYMzkXwIGvViJonw9f7kbK7GytOX1EV54/s4160/IMG_20250629_021438204.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2zAIDejn_TvWWLIOEt3QsPisEFybE5is0pmy7c5FKabqHe_m4LRbSc1FOXP6JjOHlKV7i87YyIfDbDHont0_qvoVT2QmRzy88G_29dbdQowPGahrcwr4zKfL5GVY9_w3bJ7XTzi5cLbP9hcBDWBiKxEchoCYU2mRrLhfvg0S2ouJwiNSWTaJLOs4rdLDe/s320/IMG_20250629_022136547.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2zAIDejn_TvWWLIOEt3QsPisEFybE5is0pmy7c5FKabqHe_m4LRbSc1FOXP6JjOHlKV7i87YyIfDbDHont0_qvoVT2QmRzy88G_29dbdQowPGahrcwr4zKfL5GVY9_w3bJ7XTzi5cLbP9hcBDWBiKxEchoCYU2mRrLhfvg0S2ouJwiNSWTaJLOs4rdLDe/s4160/IMG_20250629_022136547.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcUnnbi75P5poTIoM8EDE6nGMQHDJPHW0wRDGBruOtxfvx8G0022tOVDqV0qJdkk54sGKylW1m8jaNiWcuQL4-2IUBjSmo3VMtlPwycX7HqkD0jLBVCZiVUBnRz9T5fhTfYkJmo3r5bdaH6m8zJdajlMMc4nsQZIRHvmc1XVRq1V4dFy5W0kDB22CVdFCE/s320/IMG_20250629_022829638.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcUnnbi75P5poTIoM8EDE6nGMQHDJPHW0wRDGBruOtxfvx8G0022tOVDqV0qJdkk54sGKylW1m8jaNiWcuQL4-2IUBjSmo3VMtlPwycX7HqkD0jLBVCZiVUBnRz9T5fhTfYkJmo3r5bdaH6m8zJdajlMMc4nsQZIRHvmc1XVRq1V4dFy5W0kDB22CVdFCE/s4160/IMG_20250629_022829638.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDTTzN-AsvJi4P0s2f4vjkk55Sokkc_uHu13gvN3Yu3LACSQTh2zIeL-47ABm4Q6EABMlY1OY3QduKavRMvZUbGjr0c-KyyPPKbEiK-1Suq2pTxbWqh6w8C1IPe6UMeJtJuH8Pl4JCZ-a2rnpGiCc7SQdY_coJPtwfL6N7m4fciNkMUPlOYw2e25NR362n/s320/IMG_20250629_023316239.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDTTzN-AsvJi4P0s2f4vjkk55Sokkc_uHu13gvN3Yu3LACSQTh2zIeL-47ABm4Q6EABMlY1OY3QduKavRMvZUbGjr0c-KyyPPKbEiK-1Suq2pTxbWqh6w8C1IPe6UMeJtJuH8Pl4JCZ-a2rnpGiCc7SQdY_coJPtwfL6N7m4fciNkMUPlOYw2e25NR362n/s4160/IMG_20250629_023316239.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHB31nAFZt8IGorHfOfmnKvmNLzj2jkJYgMQFcbsqiu0T9EQoZdcBf66RRLCzpztuI21bUcYQEFg77XwPP0wi0YTzgMYbkef5Mwmz7T5XEwC1QmKSVbMsuNyF7Wu1K36BbIUG_EalkzLKAW3EHPT7fI0xLjr8JscEGb5rqPvXmKqCIJ0Prn9mYisEY2Kt1/s320/IMG_20250629_023601922.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHB31nAFZt8IGorHfOfmnKvmNLzj2jkJYgMQFcbsqiu0T9EQoZdcBf66RRLCzpztuI21bUcYQEFg77XwPP0wi0YTzgMYbkef5Mwmz7T5XEwC1QmKSVbMsuNyF7Wu1K36BbIUG_EalkzLKAW3EHPT7fI0xLjr8JscEGb5rqPvXmKqCIJ0Prn9mYisEY2Kt1/s4160/IMG_20250629_023601922.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnGj1OncWbkdHVebxETu_GtpFXwn563134U1krbn1l78j2gErNmOF2nEHvULxdH0ECWezPCloc3_clyycr0C20EVlwRw97d3rLQPbYaxgvSgLlpnV5LNORD-OMPwHTJVNjYXxvW3DQq-HEC2uUd-HnYjTEumwLhn-hCiHZ9uQ-g-onlVeGO-OXvzr6B7bP/s320/IMG_20250629_082054265.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnGj1OncWbkdHVebxETu_GtpFXwn563134U1krbn1l78j2gErNmOF2nEHvULxdH0ECWezPCloc3_clyycr0C20EVlwRw97d3rLQPbYaxgvSgLlpnV5LNORD-OMPwHTJVNjYXxvW3DQq-HEC2uUd-HnYjTEumwLhn-hCiHZ9uQ-g-onlVeGO-OXvzr6B7bP/s4160/IMG_20250629_082054265.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggPR8Pp9s54UwegDtsIPL7NMNFqhy-BgL9uhbK5cCza4zDOuQRRbht3_uAFqOvKUeT2-X576DOKlVMwyUrBlaqA0pWf4GUTB3qO6GOcbXMag1q_4WKDAf3GSkBB09vA5g1q8ADN8vNzBfgh-dUs6VwC31BFU9teYoBY2C0RtTdu8BQgIam7tepUzE6lT5R/s320/IMG_20250629_104323619.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggPR8Pp9s54UwegDtsIPL7NMNFqhy-BgL9uhbK5cCza4zDOuQRRbht3_uAFqOvKUeT2-X576DOKlVMwyUrBlaqA0pWf4GUTB3qO6GOcbXMag1q_4WKDAf3GSkBB09vA5g1q8ADN8vNzBfgh-dUs6VwC31BFU9teYoBY2C0RtTdu8BQgIam7tepUzE6lT5R/s4160/IMG_20250629_104323619.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzXAkxAzm7i4KPBol7quT9cRrYTbeH7PNBxLXbo4V3pBOppDxAHpm7A2Y4ZiBfSrhlwP7kUvrG_YkI0HFMv-jIILhh7JgSaWFWZbq61NvsVgh-Ohn3ioZkjSqtMGvTB-JZkAStBoST4Z8jqMfAIy9VhFQTWWL9VaJsSXEjREBg4qyyvlxY7zpGOoMdRp9L/s320/IMG_20250629_104327052_BURST000_COVER_TOP.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzXAkxAzm7i4KPBol7quT9cRrYTbeH7PNBxLXbo4V3pBOppDxAHpm7A2Y4ZiBfSrhlwP7kUvrG_YkI0HFMv-jIILhh7JgSaWFWZbq61NvsVgh-Ohn3ioZkjSqtMGvTB-JZkAStBoST4Z8jqMfAIy9VhFQTWWL9VaJsSXEjREBg4qyyvlxY7zpGOoMdRp9L/s4160/IMG_20250629_104327052_BURST000_COVER_TOP.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwiu4ObJmctuALHEPbkArr9WTni-dOYbHmf323GY_83yeK2HxXTEyP7hhcEr4uNbsM-Ah_6pDj9bWQ4VP_uCz7iIaKvSgraIntknsESAf_vbW_HY3YD1XJZWeYH-pFVfeBpXjQEc9HK7yfHmgGj6y5iORavK21RJ9v81ccCExUJuNB2ROdzK7URxD4Lw7O/s320/IMG_20250629_104327052_BURST001.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgwiu4ObJmctuALHEPbkArr9WTni-dOYbHmf323GY_83yeK2HxXTEyP7hhcEr4uNbsM-Ah_6pDj9bWQ4VP_uCz7iIaKvSgraIntknsESAf_vbW_HY3YD1XJZWeYH-pFVfeBpXjQEc9HK7yfHmgGj6y5iORavK21RJ9v81ccCExUJuNB2ROdzK7URxD4Lw7O/s4160/IMG_20250629_104327052_BURST001.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEig9yt2bEKb1NSsqnNjO6gYWPQm9L-KZGLKsUkeVR5OTbIFcVHPy_SZr3MEvNZVpF6tq-tmWt4KIyOnvzTPRwegviVsZMFP9qkH9kRVaHpT3AXRZIkdU7DP6xikFYXit5RnY5JigTH6JaQHM0Od5ljaOru-303jE4OT-B1ahqtZh3rHPlLRe1RIdyQdkHpV/s320/IMG_20250629_104329091.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEig9yt2bEKb1NSsqnNjO6gYWPQm9L-KZGLKsUkeVR5OTbIFcVHPy_SZr3MEvNZVpF6tq-tmWt4KIyOnvzTPRwegviVsZMFP9qkH9kRVaHpT3AXRZIkdU7DP6xikFYXit5RnY5JigTH6JaQHM0Od5ljaOru-303jE4OT-B1ahqtZh3rHPlLRe1RIdyQdkHpV/s4160/IMG_20250629_104329091.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs9cJqEI5eMDHIfZftLAe_jGKupVqcgpoHK35SgS7hbo0warDToIXB3swijjA6QwucupZU23N0UBhJrDr7cr57hB4U3QPJO0Q6jvevIruh-vPBWWYeLnePe_1tMJjan19Xd_Rxu8Q0X0VoHaIG_zlf_8CIMMzFKpnX-DX2IaPgSjmQxOsyFxis3wSrX38e/s320/IMG_20250630_100308742.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhs9cJqEI5eMDHIfZftLAe_jGKupVqcgpoHK35SgS7hbo0warDToIXB3swijjA6QwucupZU23N0UBhJrDr7cr57hB4U3QPJO0Q6jvevIruh-vPBWWYeLnePe_1tMJjan19Xd_Rxu8Q0X0VoHaIG_zlf_8CIMMzFKpnX-DX2IaPgSjmQxOsyFxis3wSrX38e/s4160/IMG_20250630_100308742.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2eealxOVfEq6BA8iKHoN41IFKMH9B_Q-XyqeqeWiJQkZEbzfpBEKIH-qJHHVwooPs3Hu-Abz2tF9gvokALSi3C30t9kB0yDAfI5kRh6Trfx4xomo9TLXGkssJGv0ZfrWhyf_1BM55fEqn8GTFhrhCmJifdY5YQvjrtRxMNzwSYeZc2fYyIlQsscfKMiPX/s320/IMG_20250630_233903549.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2eealxOVfEq6BA8iKHoN41IFKMH9B_Q-XyqeqeWiJQkZEbzfpBEKIH-qJHHVwooPs3Hu-Abz2tF9gvokALSi3C30t9kB0yDAfI5kRh6Trfx4xomo9TLXGkssJGv0ZfrWhyf_1BM55fEqn8GTFhrhCmJifdY5YQvjrtRxMNzwSYeZc2fYyIlQsscfKMiPX/s4160/IMG_20250630_233903549.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjhvQoK-Cuv3pqmBWHOm6bhVKGXG2VZD3rCl8C9VRvsCyGlQ_S0LlR6e2_kKP2gBuslw3ZfZdZmfFwg6M_OFkTubTG46SypKK4fgvPWkOxXB6lpB4h81dO2CT_m1HzKyiQunHPo0N0kLgMRP_E16tWeWPSALem1_eAXkMwTQZohgIdoyifBKuAtJ_6_gcu/s320/IMG_20250701_012750522.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjhvQoK-Cuv3pqmBWHOm6bhVKGXG2VZD3rCl8C9VRvsCyGlQ_S0LlR6e2_kKP2gBuslw3ZfZdZmfFwg6M_OFkTubTG46SypKK4fgvPWkOxXB6lpB4h81dO2CT_m1HzKyiQunHPo0N0kLgMRP_E16tWeWPSALem1_eAXkMwTQZohgIdoyifBKuAtJ_6_gcu/s4160/IMG_20250701_012750522.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeLWrZ64rThBtdWSjNo0ANlI6AA2H77hLCOJanBsOBzp8BD0hyphenhyphen6OLaVYz9pRg9voPherc0N8iHEn3tXDf49MUZtJ275_zR2hFU7QJnSq9KWV7PQSDfX9F8t4UmEqDNPHYF9ljtA82StHuVo9b-huDRC-TE1Io7Kbc0jFwm_z1yzB1IgIhVmo5z7VdR-2xZ/s320/IMG_20250702_204439728_BURST000_COVER.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjeLWrZ64rThBtdWSjNo0ANlI6AA2H77hLCOJanBsOBzp8BD0hyphenhyphen6OLaVYz9pRg9voPherc0N8iHEn3tXDf49MUZtJ275_zR2hFU7QJnSq9KWV7PQSDfX9F8t4UmEqDNPHYF9ljtA82StHuVo9b-huDRC-TE1Io7Kbc0jFwm_z1yzB1IgIhVmo5z7VdR-2xZ/s4160/IMG_20250702_204439728_BURST000_COVER.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsdu33t3wZF8EFXfQDYsrAc52DEtyaN2iYjuF0zAjJD-bqTmdgLEu6dEzcl886sJ21xNKrOWhlWn4lqyY9qLP9C5RXtHOxB1R7TvcikVAfrRiCLyuILrqDhd5pBnfcG3uAj5nhyphenhyphenJ_6t1tvwkmRUtTQHhj_wFqiwIEn4Xn6IXSAYXCvnAfLZF_ZynzjyWKH/s320/IMG_20250702_204444197.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsdu33t3wZF8EFXfQDYsrAc52DEtyaN2iYjuF0zAjJD-bqTmdgLEu6dEzcl886sJ21xNKrOWhlWn4lqyY9qLP9C5RXtHOxB1R7TvcikVAfrRiCLyuILrqDhd5pBnfcG3uAj5nhyphenhyphenJ_6t1tvwkmRUtTQHhj_wFqiwIEn4Xn6IXSAYXCvnAfLZF_ZynzjyWKH/s4160/IMG_20250702_204444197.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRXsVwxNL5Cvdb0y4PxDTlqi6jYBlIJlJnvg7U6A0DjgdnE4qd6HM0eUi2S8KyW3EPOMRz5PLBpRi0qX8kUAWFEl4EZGcmzr7tm_o0qwvGD9xZvJODkjnQ40jdhh_djJ92LURw71JKlbYSpxRqLtibL9kPi9R0kvXDWq6XKGFu96OfHDHwzPvyTgC_gUBD/s320/IMG_20250703_103537378.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgRXsVwxNL5Cvdb0y4PxDTlqi6jYBlIJlJnvg7U6A0DjgdnE4qd6HM0eUi2S8KyW3EPOMRz5PLBpRi0qX8kUAWFEl4EZGcmzr7tm_o0qwvGD9xZvJODkjnQ40jdhh_djJ92LURw71JKlbYSpxRqLtibL9kPi9R0kvXDWq6XKGFu96OfHDHwzPvyTgC_gUBD/s4160/IMG_20250703_103537378.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdUWBosyXS3sobrSxI1iw7pNsDynj6OjHtLNdgxbN1NG-R-uQo7wpLGfkwgXtNJvKWYw8WxLtyS9UMOIy-7sZARSbteESfzP8KfDHRQUKz84gzokWy9UY0ScU1wUpW864VnPuVdbaxduwecT-KyxtjWnMMaon6CUvxKU0HTPb00e2gUZ3_NpGBI2gK1Rzh/s320/IMG_20250703_120405988.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdUWBosyXS3sobrSxI1iw7pNsDynj6OjHtLNdgxbN1NG-R-uQo7wpLGfkwgXtNJvKWYw8WxLtyS9UMOIy-7sZARSbteESfzP8KfDHRQUKz84gzokWy9UY0ScU1wUpW864VnPuVdbaxduwecT-KyxtjWnMMaon6CUvxKU0HTPb00e2gUZ3_NpGBI2gK1Rzh/s4160/IMG_20250703_120405988.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKDqLKaYtAx7svZW_7xGj7vhE80_wZ1_upGj6ug_TlfXDL8-MNw3_7i9ElQCW7lHXpfSqu_8OwKIfsemOPV0shfNVZPckI_EWNsTzEl1k2BSPCt36zXi0sUeIfTMb-90ymGDgmCawZAwPW3yF46Z_jRqaDryCUPjldbyuWhMQFTOKkoMM5crUN7lF8ggg1/s320/IMG_20250704_063857979.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhKDqLKaYtAx7svZW_7xGj7vhE80_wZ1_upGj6ug_TlfXDL8-MNw3_7i9ElQCW7lHXpfSqu_8OwKIfsemOPV0shfNVZPckI_EWNsTzEl1k2BSPCt36zXi0sUeIfTMb-90ymGDgmCawZAwPW3yF46Z_jRqaDryCUPjldbyuWhMQFTOKkoMM5crUN7lF8ggg1/s4160/IMG_20250704_063857979.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhM9U_3UmBBaRS58L5Kuf_-FF8p-H9uhGBFXo8d73Y-BtMGbiousNPa0kGVa6bvc1asbnoo2NYa_1KMP9puy7WUZm9tbcTXbq7cch0WJz5s8uyfdH7wDLcLasHaJKQU6ipuq2yOfpVkRqv-gihwmWt2un-V7X8xZDT5iLOBurdgE3ENtLRdy-RwpSJywnls/s320/IMG_20250704_064716543.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhM9U_3UmBBaRS58L5Kuf_-FF8p-H9uhGBFXo8d73Y-BtMGbiousNPa0kGVa6bvc1asbnoo2NYa_1KMP9puy7WUZm9tbcTXbq7cch0WJz5s8uyfdH7wDLcLasHaJKQU6ipuq2yOfpVkRqv-gihwmWt2un-V7X8xZDT5iLOBurdgE3ENtLRdy-RwpSJywnls/s4160/IMG_20250704_064716543.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5zjgcJ_D9dGGpFGKGO9wMigI-hh0Vl6YFVOUuDPXmLxk4oMHSr0fw9_t9ZnqHpTTp8HnQbgEnDvJ37-Z-JXjHZ_5tGPKjejsT3LT8S1UEVmhx73N4AMAOJdJZEFJZ49BRAEtKEVEyRuf-VqTVCbo9yc9ACswDMvfRlOpjIzqXtg2bEc6jvSzzYvo1fFQx/s320/IMG_20250704_065401822.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5zjgcJ_D9dGGpFGKGO9wMigI-hh0Vl6YFVOUuDPXmLxk4oMHSr0fw9_t9ZnqHpTTp8HnQbgEnDvJ37-Z-JXjHZ_5tGPKjejsT3LT8S1UEVmhx73N4AMAOJdJZEFJZ49BRAEtKEVEyRuf-VqTVCbo9yc9ACswDMvfRlOpjIzqXtg2bEc6jvSzzYvo1fFQx/s4160/IMG_20250704_065401822.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiULVlAs6PFFhztAzoo0w3_Mh8OnSzyxrrzYHJu5KEwxwNM8zVolDHm-Dgw6iRmRWauq7Ej57cS8JmmFNgU7T1Z_W9idYBCPbVI-VrrH8bwmyWuD89QeV2W8grAb3l5ZjQ3wIVvQDbKX1Rm6AoAvS_NBja11cejMi4BHKSuXqr4CXrs95qtqpq9STxva4ft/s320/IMG_20250704_070059874_BURST000_COVER_TOP.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiULVlAs6PFFhztAzoo0w3_Mh8OnSzyxrrzYHJu5KEwxwNM8zVolDHm-Dgw6iRmRWauq7Ej57cS8JmmFNgU7T1Z_W9idYBCPbVI-VrrH8bwmyWuD89QeV2W8grAb3l5ZjQ3wIVvQDbKX1Rm6AoAvS_NBja11cejMi4BHKSuXqr4CXrs95qtqpq9STxva4ft/s4160/IMG_20250704_070059874_BURST000_COVER_TOP.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh71yevc-r9iJzpNcV3yLhMm-FVCbfMFGIIZ4HpkDpzJRhyphenhyphenZgs4R6HuSws0AxZHaCanNI_iy4VxpMBwhPM6SY_7_M3N2r69TSTqZ00FqvmyTExBSLe1ZJRQCN6vdbYIqUIRBSdhapWya4Mmc82WLX0z3HkeJs9nEWToHMFQDTURjsPOprZ2tqh3mOBhJnGN/s320/IMG_20250704_070059874_BURST001.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh71yevc-r9iJzpNcV3yLhMm-FVCbfMFGIIZ4HpkDpzJRhyphenhyphenZgs4R6HuSws0AxZHaCanNI_iy4VxpMBwhPM6SY_7_M3N2r69TSTqZ00FqvmyTExBSLe1ZJRQCN6vdbYIqUIRBSdhapWya4Mmc82WLX0z3HkeJs9nEWToHMFQDTURjsPOprZ2tqh3mOBhJnGN/s4160/IMG_20250704_070059874_BURST001.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirtu36pU4eJjaMyfdxu2tNEJ1bkdlBWI26UD4WWR8TDB2rslVVZxFbqGlTQilJZieRBqAhDlbw_nVOZw4QKtEClhVPaUazZVBnlgGwHdwcJxWZiVTEcM8TU9hj0sb-qZY1gN11JXeX9B2RCPl5Db92SppO_5uaguikojkYj0C_WcVm58FSKGlEs_hckmu4/s320/IMG_20250704_070915172.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEirtu36pU4eJjaMyfdxu2tNEJ1bkdlBWI26UD4WWR8TDB2rslVVZxFbqGlTQilJZieRBqAhDlbw_nVOZw4QKtEClhVPaUazZVBnlgGwHdwcJxWZiVTEcM8TU9hj0sb-qZY1gN11JXeX9B2RCPl5Db92SppO_5uaguikojkYj0C_WcVm58FSKGlEs_hckmu4/s4160/IMG_20250704_070915172.jpg)
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgifd4d73woInGbEVhw_hMzMMK3qJZdiDGpbx_ticbJ_PxIBQxviI8JN7fHmygH_nAo_cfpau16SbTtdtqPR07UrKxY-asAm-0zFFmvUV5QS-C8yI2MiMNWC0eMWjai3K6hpE6St0W82ylaZxlJ3S__mIlEM4ETlW74Xdictcm7lkqgrjQpzDafjXf_7Jho/s320/IMG_20250704_071709677.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgifd4d73woInGbEVhw_hMzMMK3qJZdiDGpbx_ticbJ_PxIBQxviI8JN7fHmygH_nAo_cfpau16SbTtdtqPR07UrKxY-asAm-0zFFmvUV5QS-C8yI2MiMNWC0eMWjai3K6hpE6St0W82ylaZxlJ3S__mIlEM4ETlW74Xdictcm7lkqgrjQpzDafjXf_7Jho/s4160/IMG_20250704_071709677.jpg)
