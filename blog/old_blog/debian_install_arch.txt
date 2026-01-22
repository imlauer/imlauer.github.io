---
title: "Instalar Debian como ArchLinux con debootstrap"
date: 2025-12-28T01:24:27-03:00
tags: ['linux']
---

Todavía tengo que revisar esto. Le pedí a Claude AI que me lo genere a partir de mi instalación de ArchLinux.

Tienes dos opciones:

## Opción 1: Instalar debootstrap en el LiveCD de Arch (Recomendada)

```bash
# Desde el LiveCD de Arch Linux
pacman -Sy debootstrap debian-archive-keyring

# Luego sí puedes usar el comando:
debootstrap --arch amd64 bookworm /mnt http://deb.debian.org/debian
```

## Opción 2: Usar el LiveCD oficial de Debian

Descarga la **netinst** o **live** de Debian desde:
- https://www.debian.org/download

En el instalador de Debian puedes:
1. Arrancar en modo "Advanced options" → "Rescue mode"
2. O usar la versión Live que incluye un terminal

Desde ahí `debootstrap` ya está disponible.



**Much more familiar for a Gentoo user!** Want me to update the guide using this tarball method instead of debootstrap?


# Instalación Manual de Debian (siguiendo tu configuración de Arch)

Voy a adaptarte la instalación para Debian siguiendo la estructura de tu instalación de Arch.

## Preparación Inicial

```bash
# Configurar teclado español
loadkeys es

# Configurar WiFi (Debian usa diferentes herramientas)
ip link set wlan0 up
wpa_passphrase "nombre_red" "contraseña" > /etc/wpa_supplicant.conf
wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
dhclient wlan0

# Probar conexión
ping -c 3 debian.org
```

## Particionado (igual que en Arch)

```bash
# Listar particiones
fdisk -l

# Particionar
cfdisk /dev/sda

# Seleccionar GPT y crear:
# - Partición EFI: 300MB (tipo: EFI System)
# - Partición Swap: 4GB (tipo: Linux swap)
# - Partición Root: resto (tipo: Linux filesystem)
```

## Formateo y Montaje

```bash
# Formatear particiones
mkfs.ext4 /dev/sda3        # root
mkswap /dev/sda2           # swap
mkfs.fat -F32 /dev/sda1    # EFI

# Montar
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
swapon /dev/sda2
```

## Instalación Base

```bash
# Instalar sistema base (debootstrap viene en el instalador de Debian)
debootstrap --arch amd64 bookworm /mnt http://deb.debian.org/debian

# Generar fstab
genfstab -U /mnt >> /mnt/etc/fstab
# Si no tienes genfstab, hazlo manual:
echo "UUID=$(blkid -s UUID -o value /dev/sda3) / ext4 defaults 0 1" >> /mnt/etc/fstab
echo "UUID=$(blkid -s UUID -o value /dev/sda1) /boot/efi vfat defaults 0 2" >> /mnt/etc/fstab
echo "UUID=$(blkid -s UUID -o value /dev/sda2) none swap sw 0 0" >> /mnt/etc/fstab

# Chroot
mount --bind /dev /mnt/dev
mount --bind /proc /mnt/proc
mount --bind /sys /mnt/sys
chroot /mnt /bin/bash
```

## Configuración del Sistema

```bash
# Zona horaria
ln -sf /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime
hwclock --systohc

# Locales
apt install locales
dpkg-reconfigure locales
# Seleccionar: en_US.UTF-8 UTF-8 y es_AR.UTF-8 UTF-8

# Teclado en consola
echo "KEYMAP=es" > /etc/vconsole.conf
echo "FONT=Lat2-Terminus16" >> /etc/vconsole.conf

# Hostname
echo "debian" > /etc/hostname

# Hosts
cat > /etc/hosts << EOF
127.0.0.1       localhost
::1             localhost
127.0.1.1       debian.localdomain debian
EOF

# DNS (Quad9 o Google)
cat > /etc/resolv.conf << EOF
nameserver 9.9.9.11
nameserver 149.112.112.11
EOF
chattr +i /etc/resolv.conf

# Contraseña root
passwd
```

## Instalación de Paquetes Base

```bash
# Actualizar repositorios
apt update

# Paquetes esenciales
apt install -y \
    linux-image-amd64 linux-headers-amd64 firmware-linux \
    grub-efi-amd64 efibootmgr \
    network-manager wireless-tools wpasupplicant \
    alsa-utils pulseaudio \
    vim git tmux fish \
    sudo build-essential \
    firmware-iwlwifi firmware-realtek

# Fuentes
apt install -y \
    fonts-noto fonts-noto-cjk fonts-noto-color-emoji \
    xfonts-terminus console-setup
```

## Configuración de GRUB

```bash
# Instalar GRUB (UEFI)
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=debian --recheck

# Si tienes problemas con UEFI, usa --removable:
# grub-install --target=x86_64-efi --efi-directory=/boot/efi --removable

# Detectar otros sistemas operativos
apt install os-prober
echo "GRUB_DISABLE_OS_PROBER=false" >> /etc/default/grub

# Generar configuración
update-grub
```

## Crear Usuario

```bash
# Crear usuario
useradd -m -G sudo,audio,video,netdev tu_usuario
passwd tu_usuario

# Configurar sudo (ya viene instalado)
# El grupo 'sudo' ya tiene permisos
```

## Servicios

```bash
# Habilitar NetworkManager
systemctl enable NetworkManager

# Habilitar SSH (opcional)
apt install openssh-server
systemctl enable ssh
```

## Salir y Reiniciar

```bash
exit  # salir del chroot
umount -R /mnt
reboot
```

## Post-Instalación

Después de reiniciar e iniciar sesión:

```bash
# Conectar WiFi
nmtui

# Instalar paquetes adicionales (equivalentes a tu lista de Arch)
sudo apt install -y \
    mpv firefox-esr chromium \
    w3m lynx links2 \
    irssi \
    thunderbird \
    gimp kdenlive obs-studio \
    qbittorrent transmission \
    git hugo \
    python3-pip \
    imagemagick \
    tor torbrowser-launcher \
    libreoffice \
    telegram-desktop \
    neovim \
    tmux btop htop \
    fastfetch neofetch \
    rsync rclone \
    unrar unzip p7zip-full \
    vlc \
    samba cifs-utils \
    texlive-full \
    evince okular
```

## Configuración de Teclado Español (signo > <)

```bash
# Igual que en tu Arch
sudo loadkeys es
sudo dumpkeys > mi_mapa.kmap
vim mi_mapa.kmap

# Agregar después del keycode 119:
# keycode 120 = period greater
#     altgr keycode 51 = less
# keycode 121 = comma less
#     altgr keycode 52 = greater

sudo cp mi_mapa.kmap /usr/share/keymaps/
sudo loadkeys mi_mapa
```

## Diferencias Clave: Debian vs Arch

| Aspecto | Arch | Debian |
|---------|------|--------|
| Instalación base | `pacstrap` | `debootstrap` |
| Gestor de paquetes | `pacman` | `apt` |
| AUR | `yay` | No oficial (usar repos externos con cuidado) |
| Actualización | `pacman -Syu` | `apt update && apt upgrade` |
| Paquetes | Rolling release | Versiones estables |
| Configuración | Más manual | Más automática |

## Para Instalar Software No Oficial en Debian

```bash
# Flatpak (alternativa a AUR)
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# AppImage (portables)
# Descargar .appimage, dar permisos de ejecución

# Compilar desde fuente (como en tu guía de Arch con dwm/st)
sudo apt install build-essential libx11-dev libxinerama-dev libxft-dev
# Luego: git clone, make, sudo make install
```

Good question! **Yes, Debian does have tarballs**, but they're less commonly used than Gentoo's stage3.

## Debian "stage3" equivalent

Debian calls them **"rootfs tarballs"** or **"bootstrap tarballs"**:

```bash
# Download Debian rootfs (similar to Gentoo stage3)
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.tar.xz

# Or the minimal bootstrap:
wget http://deb.debian.org/debian/dists/bookworm/main/installer-amd64/current/images/netboot/mini.iso
```

## Method 1: Using rootfs tarball (like Gentoo)

```bash
# Mount your partitions
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi

# Extract tarball
cd /mnt
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.tar.xz
tar xvf debian-12-generic-amd64.tar.xz
rm debian-12-generic-amd64.tar.xz

# Chroot and continue configuration
arch-chroot /mnt /bin/bash
```

## Method 2: Minimal bootstrap tarball

```bash
# For a truly minimal install (closest to Gentoo):
wget http://ftp.debian.org/debian/dists/bookworm/main/installer-amd64/current/images/netboot/debian-installer/amd64/linux
wget http://ftp.debian.org/debian/dists/bookworm/main/installer-amd64/current/images/netboot/debian-installer/amd64/initrd.gz
```

## Why debootstrap is more common?

- **Gentoo**: Tarball is the standard (portage needs to be there)
- **Debian**: `debootstrap` is more flexible and can install different versions/architectures
- **Arch**: `pacstrap` is integrated into the install process

## My recommendation for you:

Since you're familiar with the Gentoo tarball method:

```bash
# From Arch LiveCD:
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi

cd /mnt
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.tar.xz
tar xvpf debian-12-generic-amd64.tar.xz --xattrs-include='*.*' --numeric-owner
rm debian-12-generic-amd64.tar.xz

# Then chroot and configure
mount --bind /dev /mnt/dev
mount --bind /proc /mnt/proc
mount --bind /sys /mnt/sys
chroot /mnt /bin/bash
```

**Much more familiar for a Gentoo user!** Want me to update the guide using this tarball method instead of debootstrap?
