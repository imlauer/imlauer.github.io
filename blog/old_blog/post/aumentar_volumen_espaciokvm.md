---
title: "Aumentar volumen espacio en qemu/kvm y compartir clipboard y compartir carpeta"
date: 2024-09-21T13:03:44-03:00
tags: ['kvm']
---
```bash
sudo qemu-img resize /var/lib/libvirt/images/artix.qcow2 +10G
```

```bash
sudo apt install spice-vdagent
```

### Agregar carpeta compartida.
Graficamente: https://ostechnix.com/setup-a-shared-folder-between-kvm-host-and-guest/

https://libvirt.org/kbase/virtiofs.html


* `sudo apt-get install virt-manager libguestfs-tools`
* 9p option in your libvirt XML definition.

```
cd /etc/libvirt/qemu/
sudo vim debian12.xml
```
Agregá antes de `</domain>` y dentro de `<devices>`

```bash
<filesystem type='mount' accessmode='passthrough'>
 <source dir='/tu/carpeta/host'/>
 <target dir='share'/>
</filesystem>
```

En el guest:
```bash
mount -t 9p -o trans=virtio share /mnt/shared
```
Si no te funcioná tenés que habilitar módulos.

Resolved for me (with an ubuntu 18.04 host and 14.04 guest) by adding theses modules:

* virtio_input
* 9pnet
* 9pnet_virtio

into guest file `/etc/initramfs-tools/modules`.

**Don't forget** to upadate initramfs for your kernel(s) after add:

```bash
update-initramfs -uk <kernel|all>
modprobe virtio_pci
```

https://www.guyrutenberg.com/2018/10/25/sharing-a-folder-a-windows-guest-under-virt-manager/

https://superuser.com/questions/1317119/qemu-share-folder-9pnet-virtio-no-channels-available-for-device

### Otra forma (no es necesario)
https://libvirt.org/kbase/virtiofs.html

```xml
<domain>
  ...
  <memoryBacking>
    <source type='memfd'/>
    <access mode='shared'/>
  </memoryBacking>
  ...
  <devices>
    ...
    <filesystem type='mount' accessmode='passthrough'>
      <driver type='virtiofs' queue='1024'/>
      <source dir='/path'/>
      <target dir='mount_tag'/>
    </filesystem>
    ...
  </devices>
</domain>
```

#### Montá el directorio en el guest.
```bash
# mount -t virtiofs mount_tag /mnt/mount/path
```
