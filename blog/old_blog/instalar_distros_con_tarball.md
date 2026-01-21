---
title: "Instalar GNU/Linux distros con Tarball"
date: 2026-01-06T11:38:56-03:00
---
Anteriormente demostre como instalar Kiss Linux usando kiss-chroot.tar.xz , ahora intentare instalar debian.


¡Sí! Varias distros tienen algo equivalente a ese tarball "chroot-ready". Déjame mostrarte:

## Distros con tarballs chroot oficiales:

### 1. **Alpine Linux** (el más similar a KISS)
```bash
# Minirootfs - equivalente exacto
wget https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-minirootfs-3.19.0-x86_64.tar.gz

# Extraer y usar
tar xzf alpine-minirootfs-*.tar.gz -C /mnt
```

### 2. **Void Linux**
```bash
# ROOTFS oficial
wget https://repo-default.voidlinux.org/live/current/void-x86_64-ROOTFS-20240314.tar.xz

# Musl version (como KISS)
wget https://repo-default.voidlinux.org/live/current/void-x86_64-musl-ROOTFS-20240314.tar.xz
```

### 3. **Gentoo**
```bash
# Stage3 - el clásico
wget https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64-20240101T170204Z.tar.xz
```

### 4. **Arch Linux** (no oficial pero existe)
```bash
# archlinux-bootstrap (oficial)
wget https://geo.mirror.pkgbuild.com/iso/latest/archlinux-bootstrap-x86_64.tar.zst

# Extraer
tar xf archlinux-bootstrap-x86_64.tar.zst
# Crea un directorio root.x86_64/ con sistema base
```

### 5. **Fedora/CentOS**
```bash
# Usando docker images
docker export $(docker create fedora:39) > fedora-rootfs.tar
```

### 6. **Debian** (no oficial)
```bash
# Docker base images
wget https://github.com/debuerreotype/docker-debian-artifacts/raw/dist-amd64/bookworm/rootfs.tar.xz
```

### 7. **Artix Linux** (Arch sin systemd)
```bash
# Tiene tarballs como Arch
wget https://iso.artixlinux.org/iso/artix-base-runit-20231119-x86_64.tar.gz
```

## Comparación de formato:

| Distro | Nombre del tarball | Tamaño aprox |
|--------|-------------------|--------------|
| KISS | kiss-chroot-*.tar.xz | ~5-10MB |
| Alpine | alpine-minirootfs-*.tar.gz | ~3-5MB |
| Void | void-*-ROOTFS-*.tar.xz | ~50-100MB |
| Gentoo | stage3-*.tar.xz | ~200-300MB |
| Arch | archlinux-bootstrap-*.tar.zst | ~150-200MB |

## El más parecido a KISS:

**Alpine Linux** es prácticamente idéntico en filosofía:
- Musl libc (como KISS)
- Minimalista extremo
- Tarball de ~3-5MB
- Sistema completo funcional

```bash
# Instalación Alpine (idéntico a KISS)
mount /dev/sda3 /mnt
mount /dev/sda1 /mnt/boot

cd /mnt
wget https://dl-cdn.alpinelinux.org/alpine/v3.19/releases/x86_64/alpine-minirootfs-3.19.0-x86_64.tar.gz
tar xzf alpine-minirootfs-*.tar.gz
rm alpine-minirootfs-*.tar.gz

# Chroot y configurar
mount --bind /dev /mnt/dev
mount --bind /proc /mnt/proc
mount --bind /sys /mnt/sys
chroot /mnt /bin/sh

# Setup básico
setup-timezone
setup-keymap
apk add openrc util-linux
rc-update add devfs boot
# etc...
```

## ¿Por qué KISS/Alpine son tan pequeños?

- **Musl libc** en vez de glibc (más ligero)
- **Busybox** en vez de GNU coreutils
- Sin extras innecesarios
- Compilados con optimizaciones de tamaño

## Mi recomendación:

Si te gusta el enfoque de KISS:
1. **Alpine** - Producción, muy estable, similar filosofía
2. **Void** - Rolling release, runit, muy limpio
3. **Gentoo** - Source-based, máxima personalización
4. **KISS** - Ultra minimal, experimental

¿Quieres que te muestre cómo instalar Alpine con su minirootfs? Es prácticamente idéntico al workflow de KISS.
