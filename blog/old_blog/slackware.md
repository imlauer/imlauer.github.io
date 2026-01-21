---
title: "Instalar Slackware como ArchLinux."
date: 2025-12-27T22:55:24-03:00
---


Le pedi a Claude AI que me haga una simulacion de una instalacion de Slackware usando mi guia real de ArchLinux.

# Slackware Installation Guide (Based on Your Arch Workflow)

Here's how to achieve a similar setup on Slackware, adapted from your Arch installation process:

## Pre-Installation

```bash
# Load keyboard layout
loadkeys es

# Slackware installer handles most setup, but for manual WiFi:
# List wireless interfaces
iwconfig

# Connect to WiFi
wpa_passphrase "your-ssid" "your-password" > /etc/wpa_supplicant.conf
wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant.conf
dhcpcd wlan0

# Test connection
ping -c 3 slackware.com
```

## Partitioning (GPT for UEFI)

Slackware can use `gdisk` or `cfdisk`:

```bash
# List disks
fdisk -l

# Partition with gdisk (GPT)
gdisk /dev/sda

Commands in gdisk:
o   # Create new GPT partition table
n   # New partition
    # Partition 1: EFI
    # First sector: default (2048)
    # Last sector: +300M
    # Type: ef00 (EFI System)

n   # Partition 2: Swap
    # First sector: default
    # Last sector: +4G
    # Type: 8200 (Linux swap)

n   # Partition 3: Root
    # First sector: default
    # Last sector: default (use remaining space)
    # Type: 8300 (Linux filesystem)

w   # Write changes
```

## Format and Mount Partitions

```bash
# Format partitions
mkfs.vfat -F 32 /dev/sda1   # EFI partition
mkswap /dev/sda2             # Swap
mkfs.ext4 /dev/sda3          # Root partition

# Mount root
mount /dev/sda3 /mnt

# Create and mount boot
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot

# Enable swap
swapon /dev/sda2
```

## Install Base System

Slackware uses package sets. You can install from installer or manually:

### Method 1: Using Slackware Installer (Recommended)

```bash
# Run the installer
setup

# Follow prompts:
# 1. Select SOURCE (USB/CD/Network)
# 2. Select TARGET partition (/dev/sda3)
# 3. Select package series to install:
#    - A (Base system) - REQUIRED
#    - AP (Applications)
#    - D (Development)
#    - E (Emacs)
#    - F (FAQ/Documentation)
#    - K (Kernel source)
#    - L (Libraries)
#    - N (Network)
#    - T (TeX)
#    - X (X Window System)
#    - XAP (X Applications)
#    - XFCE (XFCE Desktop)
#    - Y (Games)
```

### Method 2: Manual Installation

```bash
# Mount Slackware ISO or USB
mount /dev/sr0 /mnt-source

# Install package series
cd /mnt-source/slackware64
installpkg -root /mnt a/*.txz    # Base system (REQUIRED)
installpkg -root /mnt ap/*.txz   # Applications
installpkg -root /mnt d/*.txz    # Development
installpkg -root /mnt l/*.txz    # Libraries
installpkg -root /mnt n/*.txz    # Networking
```

## System Configuration (chroot)

```bash
# Chroot into new system
chroot /mnt /bin/bash

# Set timezone
ln -sf /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime

# Set hardware clock
hwclock --systohc

# Configure locale (Slackware uses /etc/profile.d/)
cat > /etc/profile.d/lang.sh << EOF
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
EOF
chmod +x /etc/profile.d/lang.sh

# Set console keymap
cat > /etc/rc.d/rc.keymap << EOF
#!/bin/sh
[ -x /usr/bin/loadkeys ] && /usr/bin/loadkeys es
EOF
chmod +x /etc/rc.d/rc.keymap

# Set hostname
echo "slackware.localdomain" > /etc/HOSTNAME
echo "slackware" > /etc/hostname

# Configure hosts
cat > /etc/hosts << EOF
127.0.0.1       localhost
::1             localhost
127.0.1.1       slackware.localdomain   slackware
EOF

# Set root password
passwd
```

## Network Configuration

```bash
# Configure DNS
cat > /etc/resolv.conf << EOF
nameserver 8.8.8.8
nameserver 8.8.4.4
EOF

# Make it immutable (optional)
chattr +i /etc/resolv.conf

# WiFi configuration - create script
cat > /etc/rc.d/rc.inet1.conf << 'EOF'
# WiFi settings
IFNAME[0]="wlan0"
IPADDR[0]=""
NETMASK[0]=""
USE_DHCP[0]="yes"
DHCP_HOSTNAME[0]=""
WLAN_ESSID[0]="your-ssid"
WLAN_MODE[0]="Managed"
WLAN_KEY[0]="your-password"
WLAN_IWPRIV[0]=""
EOF

# Enable NetworkManager (alternative, easier for WiFi)
chmod +x /etc/rc.d/rc.networkmanager
```

## Install and Configure UEFI Bootloader (ELILO or GRUB)

### Option 1: ELILO (Simpler for UEFI)

```bash
# Install elilo
installpkg /path/to/elilo-*.txz

# Configure elilo
mkdir -p /boot/efi/EFI/Slackware
cp /boot/vmlinuz /boot/efi/EFI/Slackware/
cp /boot/initrd.gz /boot/efi/EFI/Slackware/

# Create elilo.conf
cat > /boot/efi/EFI/Slackware/elilo.conf << EOF
default=Slackware
prompt
timeout=10

image=vmlinuz
    label=Slackware
    initrd=initrd.gz
    append="root=/dev/sda3 ro quiet"
EOF

# Install bootloader
elilo
```

### Option 2: GRUB (More flexible)

```bash
# Install GRUB packages
slackpkg install grub

# Install GRUB to EFI
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB

# For buggy UEFI firmware, use removable option:
grub-install --target=x86_64-efi --efi-directory=/boot --removable

# Generate GRUB config
grub-mkconfig -o /boot/grub/grub.cfg
```

## Configure fstab

```bash
# Get UUIDs
blkid

# Create fstab
cat > /etc/fstab << EOF
# <file system>                         <mount point> <type> <options>         <dump> <pass>
UUID=your-root-uuid                     /             ext4   defaults          1      1
UUID=your-efi-uuid                      /boot         vfat   defaults          0      2
UUID=your-swap-uuid                     none          swap   sw                0      0
proc                                    /proc         proc   defaults          0      0
devpts                                  /dev/pts      devpts gid=5,mode=620    0      0
tmpfs                                   /dev/shm      tmpfs  defaults          0      0
EOF
```

## Exit and Reboot

```bash
# Exit chroot
exit

# Unmount partitions
umount /mnt/boot
umount /mnt
swapoff /dev/sda2

# Reboot
reboot
```

## Post-Installation Setup

### Add Regular User

```bash
# Add user to groups (wheel, audio, video, etc.)
useradd -m -G wheel,audio,video,cdrom,plugdev,users -s /bin/bash esotericwarfare
passwd esotericwarfare

# Configure sudo
visudo
# Uncomment: %wheel ALL=(ALL) ALL
```

### Package Management (slackpkg)

```bash
# Configure slackpkg mirrors
vi /etc/slackpkg/mirrors
# Uncomment a mirror close to you

# Update package list
slackpkg update

# Upgrade all packages
slackpkg upgrade-all

# Install package
slackpkg install package-name

# Search for package
slackpkg search package-name

# Remove package
slackpkg remove package-name

# List installed packages
ls /var/log/packages/
```

### Install Essential Software

```bash
# System tools
slackpkg install git vim tmux wget curl rsync

# Network tools
slackpkg install NetworkManager network-scripts

# Audio (ALSA is included by default)
# For PulseAudio:
slackpkg install pulseaudio

# Multimedia
slackpkg install mpv ffmpeg imagemagick

# Web browsers
slackpkg install firefox
# For others, use SlackBuilds (see below)
```

### Using SlackBuilds (Similar to AUR)

SlackBuilds.org is the equivalent of AUR for Slackware:

```bash
# Install sbopkg (SlackBuilds manager)
# Download from: https://sbopkg.org/downloads.php
wget https://github.com/sbopkg/sbopkg/releases/download/0.38.1/sbopkg-0.38.1-noarch-1_wsr.tgz
installpkg sbopkg-0.38.1-noarch-1_wsr.tgz

# Sync SlackBuilds repository
sbopkg -r

# Search for package
sbopkg -s package-name

# Build and install package
sbopkg -i package-name

# Or manually:
cd /tmp
wget https://slackbuilds.org/slackbuilds/15.0/package/package.tar.gz
tar xvf package.tar.gz
cd package
wget download-url  # Get from .info file
sh package.SlackBuild
installpkg /tmp/package-*.txz
```

### Services Management

Slackware uses BSD-style init scripts:

```bash
# Enable service (make executable)
chmod +x /etc/rc.d/rc.servicename

# Disable service
chmod -x /etc/rc.d/rc.servicename

# Start service
/etc/rc.d/rc.servicename start

# Stop service
/etc/rc.d/rc.servicename stop

# Restart service
/etc/rc.d/rc.servicename restart

# Common services:
chmod +x /etc/rc.d/rc.networkmanager  # NetworkManager
chmod +x /etc/rc.d/rc.sshd             # SSH
chmod +x /etc/rc.d/rc.cups             # Printing
```

### Install X Window System and DWM

```bash
# X is usually installed with the X series during setup
# If not:
slackpkg install x

# Install dependencies for dwm
slackpkg install libX11 libXinerama libXft

# Build dwm from source
cd /tmp
git clone https://git.suckless.org/dwm
cd dwm
vi config.h  # Make your customizations
make
make install

# Build st
cd /tmp
git clone https://git.suckless.org/st
cd st
make
make install

# Build dmenu
cd /tmp
git clone https://git.suckless.org/dmenu
cd dmenu
make
make install

# Create .xinitrc
cat > ~/.xinitrc << EOF
dwmstatus &
feh --bg-center ~/wallpaper.png &
st -e irssi &
chromium &
exec dwm
EOF

# Start X
startx
```

### Configure .bashrc

```bash
# Use your existing .bashrc from the document
cat > ~/.bashrc << 'EOF'
# Your complete .bashrc content here
# (Copy from the document)
EOF
```

### Audio Setup

```bash
# ALSA (default)
alsamixer  # Unmute channels and adjust volume

# For PulseAudio:
slackpkg install pulseaudio pavucontrol

# Add to ~/.xinitrc (before exec dwm)
pulseaudio --start &
```

### Additional Software

```bash
# Mail setup
slackpkg install mutt
# Use sbopkg for: isync, msmtp, neomutt

# IRC
slackpkg install irssi

# Torrent
# Use sbopkg for qbittorrent

# Video editing
# Use sbopkg for kdenlive

# Office
slackpkg install libreoffice

# LaTeX
slackpkg install texlive
```

## Key Differences from Arch

1. **Package Manager**: `slackpkg` and `installpkg` instead of `pacman`
2. **No Dependency Resolution**: Slackware doesn't auto-resolve dependencies
3. **Init System**: BSD-style init scripts instead of systemd
4. **Stability Focus**: Very conservative, rock-solid stability
5. **Manual Configuration**: More hands-on approach
6. **SlackBuilds vs AUR**: Similar concept but manual building process
7. **Full Installation**: Usually installs everything by default (can customize)

## Package Management Quick Reference

```bash
# Install local package
installpkg package.txz

# Upgrade package
upgradepkg package.txz

# Remove package
removepkg package-name

# Search installed packages
ls /var/log/packages/ | grep keyword

# List package contents
less /var/log/packages/package-name

# Find which package owns a file
grep -r "filename" /var/log/packages/
```

Slackware follows the KISS principle (Keep It Simple, Stupid) and gives you complete control over your system. It's more manual than Arch but extremely stable and straightforward.
