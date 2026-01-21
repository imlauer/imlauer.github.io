---
title: "Recuperar grub en debian desde usb live"
date: 2023-11-10T04:51:31-03:00
tags: ['grub','debian','usb']
---
¿UEFI o BIOS? La forma más sencilla de saber si el sistema se ha iniciado en modo UEFI o BIOS es buscar una carpeta /sys/firmware/efi. La carpeta estará presente si su sistema utiliza UEFI.


Mejor mirá como instalé el GRUB en ArchLinux bajo UEFI y agregá la opción `--removable` si cuando booteás te lleva a la EFI shell, y en caso de archlinux no hace falta hacer `mount --bind` sino que sólo con montar la particion de root y de efi y ejecutar `arch-chroot /mnt` basta.


UEFI bootea desde un usb live y ejecutá:

```bash
sudo mount /dev/sda3 (root) /mnt
sudo mount /dev/sda1 (efi) /mnt/boot

sudo pacman -Ss arch-install-scripts
arch-chroot /mnt

### Si estás desde otra distro
# for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done  
# 
# sudo chroot /mnt  

# bios legacy
pacman -S efibootmgr dosfstools mtools
grub-install /dev/sda --removable

# uefi
grub-install --target=x86_64-efi --bootloader-id=grub_uefi --efi-directory=/boot --recheck

# En el caso de otras distros
# update-grub

grub-mkconfig -o /boot/grub/grub.cfg

exit  
reboot
```

Si falla `grub-install` ejecutá: `mount -t efivarfs none /sys/firmware/efi/efivars`

```bash
sudo umount /dev/sdXX
sudo umount /dev/sdXY
```



```console
sudo grub-install /dev/sdX --removable
fdisk -l ó lsblk
for i in /dev /dev/pts /proc /sys /run; do mount -B $i /mnt$i; done
sudo chroot /mnt
sudo grub-install /dev/sda
sudo update-grub
$ mount /dev/sdaY /mnt
$ mount --bind /dev /mnt/dev
$ mount --bind /dev/pts /mnt/dev/pts
$ mount --bind /proc /mnt/proc
$ mount --bind /sys /mnt/sys
$ chroot /mnt
$ grub-install /dev/sdX
# O podés intentar con la opción removable
# BIOS
$ grub-install /dev/sdX --removable
$ update-grub
$ exit
$ umount /mnt/dev/pts
$ umount /mnt/dev
$ umount /mnt/proc
$ umount /mnt/sys
$ umount /mnt
```

### Otra forma

```console
$ sudo mount /dev/sdXY /mnt
$ sudo mount /dev/sda1 /mnt/boot/efi #use only if /boot is on a different partition
$ for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done
$ sudo chroot /mnt
# BIOS
$ sudo grub-install /dev/sda --removable
# UEFI
$ sudo grub-install --target=x86_64-efi --efi-directory=/boot --removable
$ update-grub
```
#### Otra forma
```bash
sudo mount /dev/sda1 /mnt
sudo grub-install --boot-directory=/mnt/boot /dev/sda1 (efi partition) --removable
sudo mount /dev/sda1 /mnt
```
### Otra forma
Precaución cambiá el nombre de las particiones.

```bash
mount /dev/sda5 /mnt/
mount /dev/sda1 /mnt/boot
mount --bind /dev /mnt/dev/
mount --bind /proc /mnt/proc/
chroot /mnt
# grub-install --recheck /dev/sda
# exit
```

Luego de reiniciar el sistema ejecutá:

```bash
sudo update-grub
```
### Otra forma
```bash
mount /dev/sda1 /mnt
mount --bind /sys /mnt/sys
mount --bind /proc /mnt/proc
mount --bind /run /mnt/run
mount --bind /dev /mnt/dev
chroot /mnt /bin/sh -i
/sbin/grub-install --target=i386-pc /dev/sda
/sbin/grub-mkconfig > /boot/grub/grub.cfg
```
Control D para salir del chroot o exit
Luego ejecutá reboot
##### Fedora

```bash
sudo mount /dev/sda3 /mnt
sudo mount --bind /sys /mnt/root/sys
sudo mount --bind /proc /mnt/root/proc
sudo mount --bind /run /mnt/root/run
sudo mount --bind /dev /mnt/root/dev
sudo chroot /mnt/root bash
mount /dev/sd3 /
mount /dev/sda2 /boot
rm -f /etc/grub.d/*
rm -f /etc/sysconfig/grub
grub2-mkconfig -o /boot/grub2/grub.cfg
grub2-install --target=i386-pc /dev/sda
```
[https://www.maketecheasier.com/restore-grub-2-as-the-main-bootloader/](https://www.maketecheasier.com/restore-grub-2-as-the-main-bootloader/)


```bash
sudo mount /dev/sdb8 /mnt 
sudo mount /dev/sdb6 /mnt/boot 
sudo mount /dev/sdb2 /mnt/boot/efi

sudo mount --bind /dev /mnt/dev &&
sudo mount --bind /dev/pts /mnt/dev/pts &&
sudo mount --bind /proc /mnt/proc &&
sudo mount --bind /sys /mnt/sys

sudo chroot /mnt

grub-install --target=x86_64-efi /dev/sdb

grub-install --recheck /dev/sdb

exit &&
sudo umount /mnt/sys &&
sudo umount /mnt/proc &&
sudo umount /mnt/dev/pts &&
sudo umount /mnt/dev &&
sudo umount /mnt
```

[https://askubuntu.com/questions/831216/how-can-i-reinstall-grub-to-the-efi-partition](https://askubuntu.com/questions/831216/how-can-i-reinstall-grub-to-the-efi-partition)
