---
title: "Recuperar grub debian desde USB live"
date: 2023-11-08T14:29:18-03:00
tags: ['grub','usb','linux']
---
¿UEFI o BIOS? La forma más sencilla de saber si el sistema se ha iniciado en modo UEFI o BIOS es buscar una carpeta /sys/firmware/efi. La carpeta estará presente si su sistema utiliza UEFI.


```console
sudo grub-install /dev/sdX
```
```console
fdisk -l ó lsblk
```
```console
for i in /dev /dev/pts /proc /sys /run; do mount -B $i /mnt$i; done
```
```console
sudo chroot /mnt
```
```console
sudo grub-install /dev/sda
```
```console
sudo update-grub
```
```console
$ mount /dev/sdaY /mnt
$ mount --bind /dev /mnt/dev
$ mount --bind /dev/pts /mnt/dev/pts
$ mount --bind /proc /mnt/proc
$ mount --bind /sys /mnt/sys
$ chroot /mnt
$ grub-install /dev/sdX
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
$ sudo mount /dev/sda1/mnt/boot/efi          #use only if /boot is on a different partition
$ for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done
$ sudo chroot /mnt
$ grub-install /dev/sda
$ update-grub
```

### Otra forma
```console
sudo mount /dev/sda1 /mnt
```

```console
sudo grub-install --boot-directory=/mnt/boot /dev/sda
```
```console
sudo mount /dev/sda1 /mnt
```

### Otra forma
Precaución cambiá el nombre de las particiones.
```console
mount /dev/sda5 /mnt/
mount /dev/sda1 /mnt/boot
mount --bind /dev /mnt/dev/
mount --bind /proc /mnt/proc/
chroot /mnt
# grub-install --recheck /dev/sda
# exit
```
Luego de reiniciar el sistema ejecutá:
```console
sudo update-grub
```

### Otra forma
```console
mount /dev/sda1 /mnt
mount --bind /sys /mnt/sys
mount --bind /proc /mnt/proc
mount --bind /run /mnt/run
mount --bind /dev /mnt/dev
chroot /mnt /bin/sh -i
/sbin/grub-install --target=i386-pc /dev/sda
/sbin/grub-mkconfig > /boot/grub/grub.cfg
Control D para salir del chroot o exit
Luego ejecutá reboot
```
### Fedora
```console
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
