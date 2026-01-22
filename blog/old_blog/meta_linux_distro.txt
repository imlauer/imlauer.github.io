---
title: "Meta linux distro"
date: 2025-10-15T20:52:02-03:00
---

### 🧩 What is a *meta* Linux distribution?

A **meta distribution** is a Linux distro that doesn’t just give you a fixed, prebuilt system like Ubuntu or Fedora — instead, it gives you **the tools and philosophy to *build your own*** system from the ground up, often with minimal automation.

They’re typically:

* **Source-based** (you compile most or all packages yourself).
* **Highly modular** — you choose every component (init, package manager, etc).
* **Educational** — you learn how Linux actually fits together.
* **Non-prescriptive** — they don’t impose defaults beyond what’s necessary to bootstrap the system.

You could think of them as “**distributions for building distributions**.”

---

### 🧱 Examples of meta distributions

| Distro                       | Description                                                                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KISS Linux**               | “Keep It Simple, Stupid” — an ultra-minimal, POSIX-compliant distro that uses shell scripts for package management. Everything is simple, transparent, and manually configured. |
| **Gentoo Linux**             | The classic meta distro. Source-based, built via Portage and `emerge`, giving full control over compiler flags, USE flags, and dependency choices.                              |
| **Exherbo**                  | A Gentoo-inspired meta distro for developers; more experimental, designed for people who want to *shape* their Linux system, not just use it.                                   |
| **Linux From Scratch (LFS)** | Not really a “distro” but a book and build process for compiling your own Linux system entirely from source — pure meta foundation.                                             |
| **CRUX**                     | Lightweight, BSD-style ports system. Meant for experienced users who like to keep things simple and manage their systems manually.                                              |
| **Bedrock Linux**            | A bit different: it lets you **mix and match components from multiple distros** (e.g., use Arch’s pacman, Debian’s apt, and Void’s runit together). Meta in a hybrid sense.     |
| **GNU Guix System**          | Functional-package-based meta distro; everything is declaratively built via the Guix system configuration. More reproducible and “meta” in philosophy.                          |
| **NixOS**                    | Similar to Guix — declarative and reproducible builds. The entire OS is described as code. More “meta” in the *infrastructure-as-code* sense.                                   |

---

### 💡 Summary

A **meta distribution**:

* Emphasizes *control over convenience*.
* Lets you define *how* Linux behaves instead of using defaults.
* Is often used to *learn, experiment, or build* derivative systems.

So yes — **KISS Linux absolutely qualifies** as a meta Linux distribution, much like **Gentoo, CRUX, Exherbo, LFS, Guix, or NixOS**, depending on your interpretation of “meta.”

