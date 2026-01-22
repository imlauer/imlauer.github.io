---
title: "Gentoo VM desde la TTY."
date: 2025-12-30T12:00:30-03:00
tags: ['vm']
---

Esto fue un fail porque mi netbook g5 es muy vieja y me tiraba un kernel panic. Lo que hice fue reinstalar archlinux y dejar una partición libre para instalar gentoo o kiss linux o cualquier otra distro que quiera instalar usando un entorno chroot :) es una mejor solución porque al no ser una máquina virtual puedo usar todo el CPU.

```bash
Decime como bootearlo dame los comandos no me tires un texto tan largo. [I] esotericwarfare@arch ~> wget https://mimas.co.ext.planetunix.net/pub/gentoo/releases/amd64/autobuilds/current-di-amd64-cloudinit/di-amd64-cloudinit-20251228T163057Z.qcow2
--2025-12-30 11:54:22--  https://mimas.co.ext.planetunix.net/pub/gentoo/releases/amd64/autobuilds/current-di-amd64-cloudinit/di-amd64-cloudinit-20251228T163057Z.qcow2
Loaded CA certificate '/etc/ssl/certs/ca-certificates.crt'
Resolving mimas.co.ext.planetunix.net (mimas.co.ext.planetunix.net)... 38.180.182.84, 2a02:c6c1:151:202:0:1:0:10
Connecting to mimas.co.ext.planetunix.net (mimas.co.ext.planetunix.net)|38.180.182.84|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1398931456 (1.3G) [text/plain]
Saving to: ‘di-amd64-cloudinit-20251228T163057Z.qcow2’
di-amd64-cloudinit-20251228T163057Z.qcow2       100%[======================================================================================================>]   1.30G  4.88MB/s    in 3m 1s   
Last-modified header invalid -- time-stamp ignored.
2025-12-30 11:57:24 (7.37 MB/s) - ‘di-amd64-cloudinit-20251228T163057Z.qcow2’ saved [1398931456/1398931456]
```




---



```bash
# Crear cloud-init ISO
cat > user-data << EOF
#cloud-config
users:
  - name: gentoo
    sudo: ALL=(ALL) NOPASSWD:ALL
    ssh_authorized_keys:
      - $(cat ~/.ssh/id_rsa.pub)
chpasswd:
  list: |
    gentoo:gentoo
  expire: false
ssh_pwauth: true
EOF

echo "instance-id: vm1" > meta-data

genisoimage -output cloud-init.iso -volid cidata -joliet -rock user-data meta-data

# Bootear la VM
qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -cpu host \
  -smp 2 \
  -drive file=di-amd64-cloudinit-20251228T163057Z.qcow2,format=qcow2,if=virtio \
  -cdrom cloud-init.iso \
  -net nic,model=virtio \
  -net user,hostfwd=tcp::2222-:22 \
  -nographic

# Conectar por SSH (desde otra terminal)
ssh -p 2222 gentoo@localhost
```

Si no tenés `genisoimage`: `pacman -S cdrtools`



Agregá `-serial mon:stdio` para ver la consola:

```bash
qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -cpu host \
  -smp 2 \
  -drive file=di-amd64-cloudinit-20251228T163057Z.qcow2,format=qcow2,if=virtio \
  -cdrom cloud-init.iso \
  -net nic,model=virtio \
  -net user,hostfwd=tcp::2222-:22 \
  -nographic \
  -serial mon:stdio
```

O usá virsh que funciona mejor con consola:

```bash
# Instalá libvirt si no lo tenés
sudo pacman -S libvirt qemu-base
sudo systemctl start libvirtd

# Copiá archivos al directorio de libvirt
sudo cp di-amd64-cloudinit-20251228T163057Z.qcow2 /var/lib/libvirt/images/gentoo.qcow2
sudo cp cloud-init.iso /var/lib/libvirt/images/

# Creá la VM
virt-install \
  --name gentoo \
  --memory 2048 \
  --vcpus 2 \
  --disk /var/lib/libvirt/images/gentoo.qcow2,format=qcow2 \
  --disk /var/lib/libvirt/images/cloud-init.iso,device=cdrom \
  --import \
  --os-variant gentoo \
  --network network=default \
  --console pty,target_type=serial

# Después conectate
virsh console gentoo
```


---


Activá la red default:

```bash
sudo virsh net-start default
sudo virsh net-autostart default
```

Después volvé a ejecutar el virt-install:

```bash
sudo virt-install \
  --name gentoo \
  --memory 2048 \
  --vcpus 2 \
  --disk /var/lib/libvirt/images/gentoo.qcow2,format=qcow2 \
  --disk /var/lib/libvirt/images/cloud-init.iso,device=cdrom \
  --import \
  --os-variant gentoo \
  --network network=default \
  --console pty,target_type=serial
```


La VM no está obteniendo IP. Reiniciala y esperá un poco más:

```bash
sudo virsh destroy gentoo
sudo virsh start gentoo

# Esperá 2-3 minutos
sleep 120

sudo virsh domifaddr gentoo
```

O conectate directo sin red usando consola serial. Primero verificá que el disco tenga el kernel correcto:

```bash
sudo virsh destroy gentoo

# Recreá la VM con consola serial configurada correctamente
sudo virt-install \
  --name gentoo2 \
  --memory 2048 \
  --vcpus 2 \
  --disk /var/lib/libvirt/images/gentoo.qcow2,format=qcow2 \
  --disk /var/lib/libvirt/images/cloud-init.iso,device=cdrom \
  --import \
  --os-variant gentoo \
  --network network=default \
  --graphics none \
  --console pty,target.type=serial

# Deberías ver el boot ahora
```

O usá QEMU directo que es más confiable:

```bash
sudo qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -cpu host \
  -smp 2 \
  -drive file=/var/lib/libvirt/images/gentoo.qcow2,format=qcow2 \
  -cdrom /var/lib/libvirt/images/cloud-init.iso \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -device e1000,netdev=net0 \
  -nographic
```


Perdon. Probá esto:

```bash
sudo qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -cpu host \
  -smp 2 \
  -drive file=/var/lib/libvirt/images/gentoo.qcow2,format=qcow2 \
  -cdrom /var/lib/libvirt/images/cloud-init.iso \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -device e1000,netdev=net0 \
  -nographic
```

Esperá 2-3 minutos y en otra terminal:

```bash
ssh -p 2222 gentoo@localhost
```

Password: `gentoo`

Si no funciona, la imagen de Gentoo puede tener problemas. Probá con Ubuntu que sé que funciona:

```bash
cd /var/lib/libvirt/images
sudo wget https://cloud-images.ubuntu.com/minimal/releases/jammy/release/ubuntu-22.04-minimal-cloudimg-amd64.img

sudo qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -cpu host \
  -smp 2 \
  -drive file=ubuntu-22.04-minimal-cloudimg-amd64.img,format=qcow2 \
  -cdrom cloud-init.iso \
  -netdev user,id=net0,hostfwd=tcp::2222-:22 \
  -device e1000,netdev=net0 \
  -nographic
```

Esperá y probá SSH.
