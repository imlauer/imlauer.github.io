---
title: "VirtualBox"
date: 2025-06-06T14:09:41-03:00
tags: ['VMs']
---
Estoy instalando Gentoo en VirtualBox en una `Intel(R) Celeron(R) N2806 (2) @ 2.00 GHz` primero intenté usar `Qemu/KVM con virt-manager` pero me tira un kernel panic al intentar bootear cualquier distro, no sé el motivo.

En VirtualBox para scrollear en la TTY se usa `Shift+{PgUp,PgDn}`
Cambiar de tamaño un hdd ya creado: `VBoxManage modifymedium disk <path-to-your-vdi> --resize <size-in-MB>`

