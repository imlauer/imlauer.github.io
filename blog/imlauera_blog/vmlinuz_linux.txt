---
title: "Error: file Vmlinuz-linux not found"
date: 2025-02-19T05:20:30-03:00
tags: ['linux']
---
Desde un usb live o desde otra distro instalada en tu HDD.
```bash
sudo mount /dev/sda1 /mnt
sudo mount /dev/sda7 /mnt/boot
arch-chroot /mnt
sudo pacman -Syu
sudo pacman -S linux
grub-install --target=x86_64-efi --bootloader-id=grub_uefi --efi-directory=/boot --recheck
grub-mkconfig -o /boot/grub/grub.cfg
```
