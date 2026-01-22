---
title: "Intenté usar Guix GNU/Linux el día de navidad."
date: 2025-12-24T20:53:39-03:00
---
Toda la configuración está escrita en Lisp (Scheme).

Lisp constituye una familia de lenguajes de programación minimalistas como Common Lisp, Scheme o Clojure, todos descienden de un viejo lenguaje de LISP (1960 creado por John McCarthy).

## 1. Preparación inicial (desde el USB de Guix)

```bash
# Cargar teclado español
loadkeys es

# Conectar WiFi
rfkill unblock all
nmcli device wifi list
nmcli device wifi connect "tu-ssid" password "tu-password"
```

## 2. Particionado (igual que en Arch con GPT/UEFI)

```bash
cfdisk /dev/sda
# Crear:
# - /dev/sda1: 512M (EFI System)
# - /dev/sda2: 4G (Linux swap)
# - /dev/sda3: resto (Linux filesystem)

# Formatear
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
mkfs.ext4 /dev/sda3

# Montar
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
swapon /dev/sda2
```

## 3. Crear configuración base de Guix

```bash
# Generar configuración inicial
herd start cow-store /mnt
guix system init /mnt/etc/config.scm /mnt
```

Pero antes necesitás crear el archivo `/mnt/etc/config.scm`. Acá va el equivalente a tu setup de Arch:

```scheme
(use-modules (gnu)
             (gnu packages bash)
             (gnu packages linux)
             (gnu packages admin)
             (gnu packages vim)
             (gnu packages wm)
             (gnu packages terminals)
             (gnu packages web-browsers)
             (gnu packages video)
             (gnu packages image)
             (gnu packages irc)
             (gnu packages mail)
             (gnu packages tmux)
             (gnu packages version-control)
             (gnu services networking)
             (gnu services desktop)
             (gnu services ssh)
             (gnu services base))

(use-service-modules desktop networking ssh)
(use-package-modules bootloaders certs suckless wm xorg)

(operating-system
  (locale "en_US.utf8")
  (timezone "America/Argentina/Buenos_Aires")
  (keyboard-layout (keyboard-layout "es"))
  (host-name "guix")

  (bootloader (bootloader-configuration
                (bootloader grub-efi-bootloader)
                (targets '("/boot/efi"))
                (keyboard-layout keyboard-layout)))

  (file-systems (cons* (file-system
                         (mount-point "/boot/efi")
                         (device (uuid "TU-UUID-EFI" 'fat32))
                         (type "vfat"))
                       (file-system
                         (mount-point "/")
                         (device (uuid "TU-UUID-ROOT"))
                         (type "ext4"))
                       %base-file-systems))

  (swap-devices (list (swap-space
                        (target (uuid "TU-UUID-SWAP")))))

  ;; Usuario
  (users (cons* (user-account
                  (name "esotericwarfare")
                  (comment "Usuario")
                  (group "users")
                  (home-directory "/home/esotericwarfare")
                  (supplementary-groups '("wheel" "netdev" "audio" "video")))
                %base-user-accounts))

  ;; Paquetes del sistema
  (packages (append (list 
                     vim
                     git
                     tmux
                     fish
                     w3m
                     lynx
                     mpv
                     imagemagick
                     irssi
                     neomutt
                     wget
                     rsync
                     tree
                     htop
                     unzip
                     nss-certs) ; Certificados SSL importantes
                    %base-packages))

  ;; Servicios
  (services (append (list
                     (service network-manager-service-type)
                     (service wpa-supplicant-service-type)
                     (service openssh-service-type))
                    %base-services)))
```

## 4. Obtener los UUIDs

```bash
# Antes de crear el config.scm, obtené los UUIDs:
blkid /dev/sda1  # EFI
blkid /dev/sda2  # SWAP
blkid /dev/sda3  # ROOT
```

## 5. Instalación

```bash
# Copiar el config.scm a /mnt/etc/
mkdir -p /mnt/etc
vim /mnt/etc/config.scm
# Pegá la configuración de arriba con tus UUIDs

# Instalar
guix system init /mnt/etc/config.scm /mnt

# Esto va a tardar bastante, compilando todo desde fuentes
```

## 6. Configuración post-instalación

```bash
# Después del primer boot
# Cambiar contraseña de root
sudo passwd

# Agregar contraseña a tu usuario
sudo passwd esotericwarfare

# Cambiar shell
chsh -s /run/current-system/profile/bin/fish
```

## 7. Para software no libre (Nonguix)

Si necesitás drivers propietarios o software no libre:

```bash
# Agregar el canal Nonguix
mkdir -p ~/.config/guix
vim ~/.config/guix/channels.scm
```

Contenido:

```scheme
(cons* (channel
        (name 'nonguix)
        (url "https://gitlab.com/nonguix/nonguix")
        (branch "master")
        (introduction
          (make-channel-introduction
            "897c1a470da759236cc11798f4e0a5f7d4d59fbc"
            (openpgp-fingerprint
              "2A39 3FFF 68F4 EF7A 3D29  12AF 6F51 20A0 22FB B2D0"))))
       %default-channels)
```

Luego:

```bash
guix pull
sudo guix system reconfigure /etc/config.scm
```

## 8. Instalar paquetes adicionales

```bash
# Paquetes de usuario (no del sistema)
guix install firefox chromium qbittorrent gimp obs tor yt-dlp
```

## Diferencias clave con Arch:

1. **Todo es declarativo**: Tu `/etc/config.scm` define TODO el sistema
2. **Sin pacman/yay**: Usás `guix install`, `guix remove`, `guix search`
3. **Rollbacks**: `sudo guix system roll-back` para volver atrás
4. **Generaciones**: El sistema guarda cada versión de tu config
5. **Más lento**: Guix compila mucho desde source
6. **Software no libre**: Requiere Nonguix y más configuración manual

En Guix **tenés binarios precompilados** para la mayoría de paquetes populares (llamados "substitutes"). Solo compilás desde source si:
- No hay substitute disponible en los servidores
- Modificás algo en la configuración del paquete
- Usás hardware muy específico

Para Firefox y otros programas grandes, casi siempre hay binarios.

## Configuración 100% reproducible

Tenés razón, **TODO debe ir en el `config.scm`** para que sea reproducible. Acá te dejo una configuración completa basada en tus paquetes de Arch:

```scheme
;; /etc/config.scm - Configuración completa del sistema

(use-modules (gnu)
             (gnu system)
             (gnu system nss)
             (gnu packages)
             (gnu packages admin)
             (gnu packages audio)
             (gnu packages base)
             (gnu packages bash)
             (gnu packages bittorrent)
             (gnu packages compression)
             (gnu packages curl)
             (gnu packages disk)
             (gnu packages emacs)
             (gnu packages file-systems)
             (gnu packages fonts)
             (gnu packages freedesktop)
             (gnu packages games)
             (gnu packages gcc)
             (gnu packages gdb)
             (gnu packages gnome)
             (gnu packages gnuzilla)
             (gnu packages image)
             (gnu packages image-viewers)
             (gnu packages irc)
             (gnu packages kde-frameworks)
             (gnu packages less)
             (gnu packages libusb)
             (gnu packages linux)
             (gnu packages mail)
             (gnu packages man)
             (gnu packages music)
             (gnu packages ncurses)
             (gnu packages networking)
             (gnu packages package-management)
             (gnu packages pdf)
             (gnu packages pulseaudio)
             (gnu packages python)
             (gnu packages rsync)
             (gnu packages samba)
             (gnu packages screen)
             (gnu packages ssh)
             (gnu packages terminals)
             (gnu packages tex)
             (gnu packages text-editors)
             (gnu packages tor)
             (gnu packages version-control)
             (gnu packages video)
             (gnu packages vim)
             (gnu packages virtualization)
             (gnu packages web)
             (gnu packages web-browsers)
             (gnu packages wm)
             (gnu packages xdisorg)
             (gnu packages xorg)
             (nongnu packages linux)      ; Para kernel no libre si lo necesitás
             (nongnu system linux-initrd)) ; Para firmware propietario

(use-service-modules desktop networking ssh xorg)

(operating-system
  (locale "en_US.utf8")
  (timezone "America/Argentina/Buenos_Aires")
  (keyboard-layout (keyboard-layout "es" #:options '("ctrl:nocaps")))
  
  (host-name "guix")

  ;; Kernel (comentá estas 2 líneas si querés solo software libre)
  (kernel linux)
  (initrd microcode-initrd)
  (firmware (list linux-firmware))

  (bootloader (bootloader-configuration
                (bootloader grub-efi-bootloader)
                (targets '("/boot/efi"))
                (keyboard-layout keyboard-layout)))

  (file-systems (cons* (file-system
                         (mount-point "/boot/efi")
                         (device (uuid "XXXX-XXXX" 'fat32)) ; Reemplazá con tu UUID
                         (type "vfat"))
                       (file-system
                         (mount-point "/")
                         (device (uuid "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")) ; Tu UUID
                         (type "ext4"))
                       %base-file-systems))

  (swap-devices (list (swap-space
                        (target (uuid "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"))))) ; Tu UUID

  ;; Usuarios
  (users (cons* (user-account
                  (name "esotericwarfare")
                  (comment "")
                  (group "users")
                  (home-directory "/home/esotericwarfare")
                  (supplementary-groups '("wheel" "netdev" "audio" "video" 
                                         "lp" "kvm" "libvirt")))
                %base-user-accounts))

  ;; Sudoers
  (sudoers-file (plain-file "sudoers" "\
root ALL=(ALL) ALL
%wheel ALL=(ALL) ALL
"))

  ;; PAQUETES DEL SISTEMA - TODO acá para que sea reproducible
  (packages (append (list
                     ;; Base
                     vim
                     git
                     tmux
                     fish-shell
                     wget
                     curl
                     rsync
                     tree
                     htop
                     btop
                     unzip
                     unrar
                     bash-completion
                     man-db
                     man-pages
                     plocate
                     fzf
                     bc
                     jq
                     
                     ;; Network
                     whois
                     inetutils
                     openssh
                     tor
                     torsocks
                     
                     ;; Browsers y web
                     icecat              ; Firefox de GNU
                     ungoogled-chromium  ; Chromium sin Google
                     w3m
                     lynx
                     falkon
                     
                     ;; Terminal apps
                     irssi
                     neomutt
                     isync
                     msmtp
                     notmuch
                     newsboat
                     
                     ;; Multimedia
                     mpv
                     yt-dlp
                     imagemagick
                     gimp
                     obs
                     ffmpeg
                     
                     ;; Audio
                     pipewire
                     pulseaudio  ; o pipewire según prefieras
                     alsa-utils
                     
                     ;; Documents
                     libreoffice
                     evince
                     texlive
                     
                     ;; Desarrollo
                     python
                     python-pip
                     
                     ;; Sway/Wayland
                     sway
                     waybar
                     wofi        ; equivalente a dmenu para wayland
                     foot        ; terminal
                     grim        ; screenshots
                     wl-clipboard
                     xdg-desktop-portal
                     xdg-desktop-portal-wlr
                     
                     ;; Fonts
                     font-terminus
                     font-google-noto
                     font-google-noto-emoji
                     font-google-noto-sans-cjk
                     
                     ;; Virtualización
                     qemu
                     virt-manager
                     
                     ;; Torrents
                     qbittorrent
                     
                     ;; Otros
                     translate-shell
                     hugo
                     telegram-desktop
                     
                     ;; Certificados SSL (IMPORTANTE)
                     nss-certs
                     le-certs)
                    %base-packages))

  ;; SERVICIOS
  (services
   (append (list
            ;; Network
            (service network-manager-service-type)
            (service wpa-supplicant-service-type)
            
            ;; SSH
            (service openssh-service-type
                     (openssh-configuration
                      (permit-root-login #f)
                      (password-authentication? #t)))
            
            ;; Tor
            (service tor-service-type)
            
            ;; Desktop/Wayland
            (service seatd-service-type)
            (service greetd-service-type
                     (greetd-configuration
                      (terminals
                       (list
                        (greetd-terminal-configuration
                         (terminal-vt "1")
                         (terminal-switch #t))))))
            
            ;; Audio
            (service pipewire-service-type)
            
            ;; Samba
            (service samba-service-type
                     (samba-configuration
                      (config-file (plain-file "smb.conf" "\
[global]
workgroup = WORKGROUP
security = user
"))))
            
            ;; Virtualization
            (service libvirt-service-type
                     (libvirt-configuration
                      (unix-sock-group "libvirt")))
            (service virtlog-service-type)
            
            ;; Cron
            (service mcron-service-type))
           
           ;; Servicios base
           %base-services))

  ;; Name service switch (para resolver nombres)
  (name-service-switch %mdns-host-lookup-nss))
```

## Archivo de canales (`~/.config/guix/channels.scm`)

Para tener Nonguix (software no libre):

```scheme
(list (channel
        (name 'nonguix)
        (url "https://gitlab.com/nonguix/nonguix")
        (branch "master")
        (introduction
          (make-channel-introduction
            "897c1a470da759236cc11798f4e0a5f7d4d59fbc"
            (openpgp-fingerprint
              "2A39 3FFF 68F4 EF7A 3D29  12AF 6F51 20A0 22FB B2D0"))))
      (channel
        (name 'guix)
        (url "https://git.savannah.gnu.org/git/guix.git")
        (branch "master")
        (introduction
          (make-channel-introduction
            "9edb3f66fd807b096b48283debdcddccfea34bad"
            (openpgp-fingerprint
              "BBB0 2DDF 2CEA F6A8 0D1D  E643 A2A0 6DF2 A33A 54FA")))))
```

## Workflow de uso:

```bash
# 1. Editar config.scm
sudo vim /etc/config.scm

# 2. Actualizar canales (equivalente a pacman -Sy)
guix pull

# 3. Reconstruir sistema (aplica cambios)
sudo guix system reconfigure /etc/config.scm

# 4. Ver generaciones disponibles
guix system list-generations

# 5. Rollback si algo falla
sudo guix system roll-back

# 6. Buscar paquetes
guix search firefox

# 7. Ver qué hay instalado
guix package --list-installed
```

## Para hacer backup de tu configuración:

```bash
# Todo lo que necesitás es:
/etc/config.scm
~/.config/guix/channels.scm
```

Con esos 2 archivos podés reproducir tu sistema **exactamente** en otra máquina.

**Nota importante sobre binarios**: Cuando hagas `guix pull` la primera vez, va a descargar MUCHOS substitutes (binarios). Para Firefox, Chromium, LibreOffice, etc., siempre hay binarios disponibles. Solo compilás si instalás algo muy obscuro o modificás las opciones de compilación.


---


# ChatGPT

Below is a **clean, Arch-mindset, step-by-step guide to install GNU Guix System**, explicitly mapped from how *you* already install Arch.

I’ll **reuse your mental model** (UEFI+GPT, manual partitioning, Wi-Fi, keymap ES, nonfree firmware) but **translate it to Guix terms**.

This is **not Guix “easy mode”** — it’s the *right* way for someone coming from Arch.

---

# 0. Important conceptual differences (Arch → Guix)

Before commands, this matters:

| Arch                  | Guix                               |
| --------------------- | ---------------------------------- |
| pacman                | guix package / guix system         |
| mutable system        | **immutable system** (declarative) |
| edit files directly   | edit **/etc/config.scm**           |
| reinstall to rollback | **guix roll-back**                 |
| AUR                   | **Guix channels**                  |
| systemd               | **shepherd**                       |

You **do not chroot** in Guix.
You **declare the system**, then Guix builds it.

---

# 1. Boot the Guix installer ISO

Download **nonfree ISO** (you explicitly asked for nonfree drivers):

👉 **Use this one**
[https://guix.gnu.org/download/](https://guix.gnu.org/download/)

Choose:

```
guix-system-install-1.4.x.x86_64-linux.iso (with firmware)
```

Write it with `dd` (from Arch):

```bash
sudo dd if=guix-system-install-*.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

Boot **UEFI mode**.

---

# 2. Keyboard, locale, time (Arch equivalent)

Same mindset as your Arch install:

```bash
loadkeys es
```

Time sync:

```bash
herd start ntpd
```

(Check time)

```bash
date
```

---

# 3. Wi-Fi (equivalent to iwctl)

Guix uses **wpa_supplicant**, not iwd.

### List interfaces

```bash
ip link
```

Assume `wlan0`.

### Scan & connect

```bash
wpa_cli
```

Inside prompt:

```text
scan
scan_results
add_network
set_network 0 ssid "TU_WIFI"
set_network 0 psk "TU_PASSWORD"
enable_network 0
quit
```

Test:

```bash
ping -c 3 dgg.gg
```

---

# 4. Disk partitioning (same logic as your Arch guide)

You already understand **UEFI + GPT**, so we reuse it.

### Example disk: `/dev/sda`

```bash
cfdisk /dev/sda
```

Choose **GPT**.

Create:

| Partition | Size     | Type             |
| --------- | -------- | ---------------- |
| EFI       | 300–512M | EFI System       |
| Swap      | 4G       | Linux swap       |
| Root      | rest     | Linux filesystem |

---

# 5. Format partitions

Assume:

* EFI → `/dev/sda1`
* swap → `/dev/sda2`
* root → `/dev/sda3`

```bash
mkfs.fat -F32 /dev/sda1
mkswap /dev/sda2
mkfs.ext4 /dev/sda3
```

Mount:

```bash
mount /dev/sda3 /mnt
mkdir -p /mnt/boot/efi
mount /dev/sda1 /mnt/boot/efi
swapon /dev/sda2
```

---

# 6. Generate initial Guix system config

This replaces **pacstrap + genfstab + arch-chroot**.

```bash
guix system init /mnt
```

This creates:

```
/mnt/etc/config.scm
```

THIS FILE IS YOUR SYSTEM.

---

# 7. Edit the system configuration (VERY IMPORTANT)

Open it:

```bash
nano /mnt/etc/config.scm
```

### 7.1 Keyboard, locale, timezone

Find and edit:

```scheme
(locale "en_US.utf8")
(timezone "America/Argentina/Buenos_Aires")
(keyboard-layout (keyboard-layout "es"))
```

---

### 7.2 Enable nonfree firmware (critical)

Add **near the top**:

```scheme
(use-modules (gnu) (nongnu packages linux))
```

Then replace kernel section with:

```scheme
(kernel linux)
(firmware (list linux-firmware))
```

This is the **equivalent of `linux-firmware` in Arch**.

---

### 7.3 Bootloader (UEFI, GRUB)

Replace bootloader section with:

```scheme
(bootloader
 (bootloader-configuration
  (bootloader grub-efi-bootloader)
  (targets '("/boot/efi"))
  (keyboard-layout keyboard-layout)))
```

---

### 7.4 Filesystems (fstab equivalent)

Replace file-systems section with:

```scheme
(file-systems
 (cons*
  (file-system
   (mount-point "/boot/efi")
   (device "/dev/sda1")
   (type "vfat"))
  (file-system
   (mount-point "/")
   (device "/dev/sda3")
   (type "ext4"))
  %base-file-systems))
```

Swap:

```scheme
(swap-devices
 (list (swap-space (target "/dev/sda2"))))
```

---

### 7.5 Networking (NetworkManager equivalent)

Add:

```scheme
(service network-manager-service-type)
```

Guix does NOT enable it by default.

---

### 7.6 Users (equivalent to useradd + sudo)

```scheme
(users
 (cons
  (user-account
   (name "esotericwarfare")
   (comment "Main user")
   (group "users")
   (supplementary-groups '("wheel" "audio" "video" "netdev")))
  %base-user-accounts))
```

Enable sudo:

```scheme
(service sudo-service-type)
```

---

# 8. Install the system (this is the “makepkg + pacstrap” moment)

```bash
guix system init /mnt/etc/config.scm /mnt
```

⚠️ This takes time.
Guix builds everything **from source or substitutes**.

---

# 9. Set root password

```bash
passwd
```

---

# 10. Reboot

```bash
reboot
```

Remove USB.

---

# 11. First boot tasks

Login as **root**.

### Enable NetworkManager

```bash
herd start network-manager
```

### Set user password

```bash
passwd esotericwarfare
```

---

# 12. Package management (Arch → Guix translation)

| Arch            | Guix            |
| --------------- | --------------- |
| pacman -S       | guix install    |
| pacman -R       | guix remove     |
| pacman -Q       | guix package -I |
| system packages | **config.scm**  |
| user packages   | `guix install`  |

Example:

```bash
guix install vim tmux git mpv neomutt w3m
```

---

# 13. System updates (NO partial upgrades)

Equivalent to `pacman -Syu`:

```bash
guix pull
sudo guix system reconfigure /etc/config.scm
```

Rollback if broken:

```bash
sudo guix system roll-back
```

---

# 14. Desktop / Wayland / Xorg

Guix supports **sway, dwm, xfce, etc**, but installed declaratively.

Example sway:

```scheme
(service sway-service-type)
```

Or Xorg + dwm (manual like you prefer).

---

# 15. Mental model shift (important)

Think of Guix as:

> **Git + Nix + Arch philosophy without bullshit**

* Your OS is a **single Scheme file**
* You can diff it
* You can roll back kernels
* You can reproduce it on another machine exactly

---

## If you want next:

* 🧱 **Full disk encryption (LUKS) in Guix**
* 🪟 **dwm setup declaratively**
* 📦 **Arch package → Guix equivalent list**
* 🔧 **Nonfree Wi-Fi edge cases (Intel / Realtek)**

Tell me what you want next and I’ll go deep, no hand-holding.

