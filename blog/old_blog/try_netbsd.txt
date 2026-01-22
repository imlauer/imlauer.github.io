---
title: "I tried NetBSD. Intenté usar NetBSD por día."
date: 2025-12-27T14:58:04-03:00
tags: ['bsd']
---

Funcionaba todo lento. Y chromium tenía un flickering tremendo, aparte como es BSD los algunos scripts de bash que tenía tiraba error el comando `date` aparentemente la sintaxis es diferente aunque sea bash.

En NetBSD no existe el "framebuffer" así que no tenes fbida (fbpdf para leer pdfs y fbi para ver imágenes).

* `/dev/fb0` no existe.

```bash
export PKG_PATH=https://cdn.NetBSD.org/pub/pkgsrc/packages/NetBSD/10.1/x86_64/
pkg_add pkgin not found
PKG_PATH=https://cdn.NetBSD.org/pub/pkgsrc/packages/NetBSD/amd64/10.1/All
PKG_PATH="https://cdn.NetBSD.org/pub/pkgsrc/packages/$(uname -s)/$(uname -m)/$(uname -r | cut -f '1 2' -d.)/All"
pkg_add pkgin not found # pkgin es frontend para las herramientas pkg_*
su
pkg_add w3m tmux newsraft pkgin
pkg install dwm dmenu mpv yt-dlp

Segui mi instalacion de archlinux o de gentoo (los nombre de los programas).

Otter-browser esta disponible en pkgsrc pero no esta en pkgin porque pkgin solo tiene binarios, pkgsrc tenes que compilarlo.

# No hace falta, si usas PKG_PATH.
ls /usr/pkgsrc: No such file or directory
su
cd /usr; ftp https://cdn.NetBSD.org/pub/pkgsrc/current/pkgsrc.tar.gz
tar xvf pkgsrc.tar.gz
cd /usr/pkgsrc/net/netbssd
make install clean
/usr/pkg/sbin/netbssd -h
pkg_info | grep netbssd
ls /usr/pkgsrc/net | grep bsd


Para solucionar flickering en mi intel celeron con igpu integrada.

Section "Device"
	Identifier "Intel Graphics"
	Driver "modesetting"
	Option "AccelMethod" "none"
EndSection

doas sin contraseña tenes que agregar alias sudo="doas" en el .shrc

/usr/pkg/etc/doas.conf

permit persist :wheel
permit nopass esotericwarfare

XTerm*locale: true
XTerm*utf8: 1
xterm*background:black
xterm*foreground:white
xterm*faceName:Monospace
xterm*faceSize:15


# al pedo
groupadd video
sudo usermod -G video,wheel <your_username>

su 
X -configure
mv /root/xorg.conf.new /etc/X11/xorg.conf

Tenia xterm asi que hice esto primero cree un system link pero no funciono, asi que cree archivo bash

sudo /usr/bin/pkg/vim /usr/pkg/bin/st

#!/bin/sh
xterm

xD sino no me tomaba la configuracion del .Xdefaults .Xresources
```


![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_000530662_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_000530662.jpg)
![https://archive.org/download/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_001830932_thumb.jpg](https://archive.org/download/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_001830932.jpg)
![https://archive.org/download/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_041802529_thumb.jpg](https://archive.org/download/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_041802529.jpg)
![https://archive.org/download/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055816886_thumb.jpg](https://archive.org/download/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055816886.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055816886_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055816886.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055826300_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055826300.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055832445_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055832445.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055836260_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055836260.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055840909_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055840909.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055845685_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055845685.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055923430_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055923430.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055928943_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_055928943.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060048076_BURST001_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060048076_BURST001.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060103022_BURST000_COVER_TOP_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060103022_BURST000_COVER_TOP.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060108397_BURST001_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060108397_BURST001.jpg)
![https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060118438_thumb.jpg](https://ia600709.us.archive.org/17/items/2025-12-27-netbsd_archlinux_pasto-images/IMG_20251227_060118438.jpg)


# Claude AI
Le pedi que me haga una instalacion como archlinux.

```bash
# NetBSD Installation Guide (Based on Your Arch Workflow)

Here's how to achieve a similar setup on NetBSD, adapted from your Arch installation process:

## Pre-Installation

```bash
# Set keyboard layout (NetBSD uses wscons)
wsconsctl -w encoding=es

# NetBSD installer handles network during installation
# For manual WiFi after boot:
ifconfig -a  # list interfaces
ifconfig iwn0 up  # replace iwn0 with your interface
ifconfig iwn0 nwid "your-ssid" wpakey "your-password"
dhcpcd iwn0
```

## Partitioning (GPT for UEFI)

NetBSD uses different partition tools:

```bash
# List disks
dkctl wd0 listwedges
# or
gpt show wd0

# Partition with gpt tool
gpt destroy wd0  # if needed
gpt create wd0

# Create EFI partition (300MB)
gpt add -b 2048 -s 614400 -t efi -l "EFI System" wd0

# Create swap (4GB)
gpt add -s 8388608 -t swap -l "swap" wd0

# Create root partition (rest of disk)
gpt add -t ffs -l "NetBSD Root" wd0

# Show partitions
gpt show wd0
```

## Format and Mount

```bash
# Format partitions
newfs_msdos -F 32 /dev/rdk0  # EFI partition (use actual device name)
newfs -O2 /dev/rdk2  # root partition with FFSv2

# Mount
mount /dev/dk2 /mnt
mkdir /mnt/boot
mount_msdos /dev/dk0 /mnt/boot

# Enable swap
swapon /dev/dk1
```

## Base System Installation

NetBSD installation is typically done via the installer, but for manual installation:

```bash
# Download sets from NetBSD mirror
cd /mnt
ftp ftp://ftp.netbsd.org/pub/NetBSD/NetBSD-10.0/amd64/binary/sets/

# Extract base sets (minimum required)
for set in base comp etc kern-GENERIC man misc modules text; do
    tar -xzpf ${set}.tar.xz -C /mnt
done

# Optional sets
tar -xzpf xbase.tar.xz -C /mnt  # X11 base
tar -xzpf xetc.tar.xz -C /mnt   # X11 config
```

## Configure System (chroot)

```bash
chroot /mnt /bin/sh

# Set timezone
ln -sf /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime

# Set hostname
echo "netbsd" > /etc/myname

# Configure rc.conf
cat >> /etc/rc.conf << EOF
hostname="netbsd"
dhcpcd=YES
sshd=YES
wscons=YES
EOF

# Set root password
passwd

# Configure keyboard
cat > /etc/wscons.conf << EOF
encoding es
font terminus-32
EOF
```

## Network Configuration

```bash
# /etc/ifconfig.iwn0 (replace iwn0 with your interface)
cat > /etc/ifconfig.iwn0 << EOF
nwid your-ssid wpakey your-password
dhcp
EOF

# DNS configuration
cat > /etc/resolv.conf << EOF
nameserver 8.8.8.8
nameserver 8.8.4.4
EOF
```

## Bootloader (UEFI)

```bash
# Install bootloader
mkdir -p /boot/EFI/boot
cp /usr/mdec/bootx64.efi /boot/EFI/boot/bootx64.efi

# Create boot.cfg
cat > /boot/boot.cfg << EOF
menu=Boot NetBSD:rndseed /var/db/entropy-file;boot
menu=Boot single user:rndseed /var/db/entropy-file;boot -s
timeout=5
EOF

# Exit chroot
exit

# Unmount and reboot
umount /mnt/boot
umount /mnt
reboot
```

## Post-Installation

After first boot:

```bash
# Update package database
pkgin update

# Install pkgin if not available
cd /usr && cvs checkout -P pkgsrc
cd /usr/pkgsrc/pkgtools/pkgin
bmake install clean

# Install essential packages
pkgin install vim tmux git bash fish wget curl rsync

# Audio (NetBSD uses audio(4) and mixer(4))
# Audio works out of the box, configure with mixerctl

# For PipeWire-like functionality, use oss or sndiod
```

## Key Differences from Arch

1. **Package Manager**: `pkgin` instead of `pacman`
   ```bash
   pkgin search package
   pkgin install package
   pkgin remove package
   pkgin list
   ```

2. **Service Management**: `/etc/rc.d/` instead of systemd
   ```bash
   /etc/rc.d/sshd start
   echo 'sshd=YES' >> /etc/rc.conf
   ```

3. **File Systems**: FFS/FFSv2 instead of ext4
4. **Device Names**: `wd0`, `dk0` instead of `sda`, `sda1`
5. **Network Config**: `/etc/ifconfig.interface` files
6. **Building from Source**: Use pkgsrc instead of AUR
   ```bash
   cd /usr/pkgsrc/category/package
   bmake install clean
   ```

## User Management

```bash
# Add user
useradd -m -G wheel -s /usr/pkg/bin/bash username
passwd username

# Enable sudo
pkgin install sudo
visudo  # uncomment %wheel line
```

## Additional Software

```bash
# Web browsers
pkgin install firefox links lynx w3m

# Multimedia
pkgin install mpv ffmpeg imagemagick

# Development
pkgin install gcc git python39 nodejs

# Terminal multiplexer
pkgin install tmux dvtm

# Mail
pkgin install mutt isync msmtp
```

NetBSD's philosophy emphasizes clean, well-documented code over bleeding-edge features. The system is more conservative than Arch but extremely stable and portable.
```
