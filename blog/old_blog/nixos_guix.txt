---
title: "NixOS Guix"
date: 2025-12-18T05:34:34-03:00
---
Yes — **NixOS does use systemd** by default.

### Key points

* **Init system:** systemd
* **Service manager:** systemd
* **Targets / units:** standard systemd units (services, timers, sockets, etc.)

NixOS integrates systemd deeply, but configures it **declaratively** via Nix instead of imperative commands.

---

### How NixOS uses systemd (what’s different)

You **don’t usually write unit files by hand**. Instead, you define services in `configuration.nix`, and NixOS generates the systemd units for you.

Example:

```nix
services.nginx.enable = true;
```

This automatically creates and manages:

* `nginx.service`
* dependencies
* users/groups
* config files

You can still interact with systemd normally:

```bash
systemctl status nginx
systemctl restart nginx
journalctl -u nginx
```

---

### Custom systemd services in NixOS

You *can* define your own units declaratively:

```nix
systemd.services.my-service = {
  description = "My custom service";
  wantedBy = [ "multi-user.target" ];
  serviceConfig = {
    ExecStart = "/path/to/binary";
    Restart = "always";
  };
};
```

---

### Can NixOS run without systemd?

* Officially: **no**
* Practically: systemd is **required** for standard NixOS
* Experimental alternatives exist (e.g. OpenRC), but they are **unsupported and incomplete**

If you want:

* ❌ no systemd → use **Void Linux**, **Artix**, or **Gentoo**
* ✔ declarative + systemd → **NixOS**

---

### Summary

| Question                        | Answer              |
| ------------------------------- | ------------------- |
| Does NixOS use systemd?         | ✅ Yes               |
| Can you avoid systemd in NixOS? | ❌ Not realistically |
| Is systemd optional?            | ❌                   |
| Is it configured declaratively? | ✅                   |

If you want, I can compare **NixOS vs Arch vs Gentoo vs Void** from a system-design perspective.

---

Yes — **Guix is very similar to NixOS in philosophy**, **but different in important technical choices**.

Short answer first:

> **GNU Guix System does NOT use systemd.**

---

## Guix vs NixOS — the big picture

| Aspect          | NixOS                   | Guix System        |
| --------------- | ----------------------- | ------------------ |
| Package manager | Nix                     | Guix               |
| Language        | Nix expression language | GNU Guile (Scheme) |
| System config   | Declarative             | Declarative        |
| Reproducibility | Yes                     | Yes                |
| Rollbacks       | Yes                     | Yes                |
| Default init    | **systemd**             | **GNU Shepherd**   |
| GNU ideology    | Neutral                 | Strongly GNU / FSF |

---

## What Guix uses instead of systemd

### 🐑 **GNU Shepherd**

* Init system written in **Guile (Scheme)**
* Older name: `dmd`
* Much simpler than systemd
* Focused only on service management

Key characteristics:

* No PID 1 feature creep
* No journal replacement
* No device manager
* No login manager
* No tight coupling with everything

Shepherd is closer to:

* runit
* s6
* OpenRC
  than to systemd.

---

## Example: defining a service in Guix

```scheme
(service nginx-service-type
         (nginx-configuration
           (server-blocks
             (list
               (nginx-server-configuration
                 (server-name '("example.com"))
                 (listen '("80"))))))
```

This generates:

* service definition
* dependency graph
* start/stop logic

No unit files.

---

## Can Guix use systemd?

* ❌ **No**
* systemd is intentionally avoided
* Guix aligns with FSF principles (systemd is considered non-GNU)

---

## Similarities with NixOS

They share the **same core ideas**:

* Declarative OS configuration
* Functional package management
* Immutable store (`/gnu/store` vs `/nix/store`)
* Atomic upgrades
* Rollbacks
* Profiles and generations

They solve the **same problems**, but with different ideology.

---

## Major differences (practical)

### Language

* NixOS: custom DSL (quirky)
* Guix: full **Scheme** (powerful, consistent)

### Boot speed

* Guix + Shepherd is usually **faster** than systemd

### Hardware support

* NixOS: broader, more practical
* Guix: more limited (especially firmware)

### Ecosystem

* NixOS: much larger
* Guix: smaller, cleaner

---

## Who should choose Guix?

Choose **Guix** if you want:

* No systemd
* 100% free software (or close)
* Scheme-based config
* Minimalism
* FSF-aligned system

Choose **NixOS** if you want:

* Best hardware support
* systemd integration
* Huge package ecosystem
* More “plug-and-play”

---

## TL;DR

* ✅ Guix ≈ NixOS philosophically
* ❌ Guix ≠ systemd
* 🐑 Guix uses **GNU Shepherd**
* 🧠 Same idea, different ideology

If you want, I can help you decide **Guix vs NixOS vs Artix vs Void** based on how you actually use your machine.

---

Yes — but with **important caveats**. GNU Guix is **FSF-pure by default**, so it avoids non-free firmware, yet you **can install non-free blobs manually** if you really need them (like for Wi-Fi).

Here’s a breakdown.

---

## 1️⃣ What Guix provides out of the box

* Only **free firmware** is included (mostly for some Intel or open Broadcom chips).
* Most Wi-Fi requiring **proprietary firmware** (Broadcom, Realtek) is **not included**.
* System won’t load non-free blobs automatically — FSF policy.

---

## 2️⃣ Ways to get non-free firmware on Guix

### Option A — Use Guix `operating-system` config hooks

You can copy firmware to `/etc/firmware` or `/lib/firmware` and load it via kernel modules.

Example:

```scheme
(operating-system
  ;; ...
  (file-systems
    (cons* (file-system
             (mount-point "/lib/firmware")
             (device #f)
             (type "tmpfs")
             (options '("mode=755")))
           %base-file-systems))
  ;; Hook to copy firmware
  (packages (append
             (list (local-file "path/to/your/firmware/driver.bin"))
             %base-packages)))
```

Then the kernel module can pick it up.

---

### Option B — Use Guix’s `--substitute-binary` feature

Guix allows **binary substitution** for packages that are not in FSF repo.
This is advanced; usually involves:

1. Downloading precompiled firmware blobs
2. Importing them as `local-package` definitions
3. Adding them to your system profile

---

### Option C — Dual-boot / hybrid approach

Some users:

* Boot Guix on **free firmware hardware**
* Or use a **USB stick with non-free firmware preloaded**
* Then Guix sees the device as working

---

## 3️⃣ Wi-Fi specifics

* Broadcom chips: almost always need **non-free `b43` or `wl` firmware**
* Realtek: often need `rtlwifi` blobs
* Intel: mostly free, works out of the box

Check with:

```bash
lspci -nnk | grep -iA3 net
```

---

## 4️⃣ Caveats

* Installing non-free firmware **breaks FSF purity**
* Updates may not be smooth, you may need to manually re-copy blobs on kernel updates
* Guix community generally recommends **Intel or Atheros cards** for 100% free experience

---

## ✅ TL;DR

* Guix doesn’t include non-free Wi-Fi firmware by default.
* You **can install it manually** (copy blobs + kernel modules).
* If you want FSF-pure, use **Intel/Atheros** Wi-Fi.
* If you need Broadcom/Realtek, you need **manual intervention**.

---

If you want, I can give you a **step-by-step example** to make a Broadcom Wi-Fi chip fully work on Guix, including config snippets. Do you want me to do that?

---

Perfect! Let’s go **step by step** for getting a **non-free Wi-Fi driver working on Guix System**. I’ll make it clear, **declarative where possible**, while keeping it practical.

We’ll assume your Wi-Fi card requires a proprietary firmware blob (like Broadcom or some Realtek chips).

---

## 1️⃣ Identify your Wi-Fi card

Open a terminal:

```bash
lspci -nnk | grep -iA3 net
```

Output example:

```
03:00.0 Network controller [0280]: Broadcom Inc. and subsidiaries BCM43142 802.11b/g/n [14e4:4365]
        Subsystem: Hewlett-Packard Company BCM43142 802.11b/g/n
        Kernel driver in use: wl
```

✅ Note:

* `14e4:4365` → PCI ID
* `Kernel driver in use` may show `b43` or `wl`
* You need a firmware blob that matches your card

---

## 2️⃣ Get the proprietary firmware

* Go to the manufacturer site or trusted repository (Broadcom, Realtek, etc.)
* For Broadcom BCM43142: get `wl_apsta.o` (or `.bin`) firmware
* Save it to a folder, e.g.:

```bash
mkdir -p ~/firmware
cp wl_apsta.o ~/firmware/
```

---

## 3️⃣ Copy firmware to `/lib/firmware`

Guix expects firmware in `/lib/firmware` (or a subdirectory used by the kernel module):

```bash
sudo cp ~/firmware/* /lib/firmware/
```

---

## 4️⃣ Load the kernel module

For Broadcom, for example:

```bash
sudo modprobe wl
```

Check your Wi-Fi interface:

```bash
ip link
```

You should see `wlan0` or similar.

---

## 5️⃣ Make it persistent (declarative approach)

Guix lets you **include local packages** in your system configuration. Create a **local package for the firmware**:

### a) Create a folder for local packages:

```bash
mkdir -p ~/guix-packages
```

### b) Define a local package `firmware-broadcom.scm`:

```scheme
(use-modules (guix packages)
             (guix download)
             (guix build-system trivial)
             (guix licenses))

(define-public firmware-broadcom
  (package
    (name "firmware-broadcom")
    (version "1.0")
    (source (local-file "/home/username/firmware/wl_apsta.o"))
    (build-system trivial-build-system)
    (arguments `(#:install-file (("wl_apsta.o" "share/firmware/wl_apsta.o"))))
    (home-page "https://www.broadcom.com")
    (synopsis "Proprietary Broadcom Wi-Fi firmware")
    (description "Firmware blob for Broadcom Wi-Fi chips")
    (license non-free)))
```

---

### c) Add to your system configuration

Edit `/etc/config.scm` (or wherever your `operating-system` block is):

```scheme
(operating-system
  ;; ...
  (packages
   (append
    (list (local-package "firmware-broadcom" "~/guix-packages/firmware-broadcom.scm"))
    %base-packages))
)
```

---

### d) Rebuild system

```bash
sudo guix system reconfigure /etc/config.scm
```

✅ This will:

* Copy the firmware to `/gnu/store/.../share/firmware/...`
* Make it part of your system declaratively
* Rollback possible if anything breaks

---

## 6️⃣ Load module on boot

Add the kernel module to `operating-system`:

```scheme
(operating-system
  ;; ...
  (linux-modules (cons "wl" %base-linux-modules))
)
```

Reconfigure again:

```bash
sudo guix system reconfigure /etc/config.scm
```

Now your non-free Wi-Fi driver is **persistent and declarative**.

---

## 7️⃣ Connect to Wi-Fi

You can use **NetworkManager**:

```bash
sudo systemctl start NetworkManager
nmcli device wifi list
nmcli device wifi connect "SSID_NAME" password "YOUR_PASSWORD"
```

---

## ✅ Summary

1. Identify Wi-Fi chip with `lspci`.
2. Download the proprietary firmware blob.
3. Copy it to `/lib/firmware` for immediate testing.
4. Load the kernel module manually (`modprobe wl`).
5. Wrap firmware as a **local package** in Guix.
6. Add package and kernel module to `operating-system` declaratively.
7. Reconfigure with `guix system reconfigure`.
8. Connect via NetworkManager.

---

If you want, I can make a **ready-to-paste Guix snippet for Broadcom and Realtek chips** so you can just drop it in your config and rebuild — fully declarative.

Do you want me to do that?

