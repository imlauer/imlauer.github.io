---
title: "Bisq2 en Arch"
date: 2025-06-01T19:20:38-03:00
tags: ['bitcoin']
---
`yay -S bisq2` me da este eroror: **Falla porque necesitas la versión 22 de jdk** podes mirar la versión en uso con `archlinux-java status`
```console
Configuring project user

> Configure project :daemon
daemon does not have a Java component, skipping

FAILURE: Build failed with an exception.

* What went wrong:
BUG! exception in phase 'semantic analysis' in source unit '_BuildScript_' Unsupported class file major version 68
> Unsupported class file major version 68

* Try:
> Run with --stacktrace option to get the stack trace.
> Run with --info or --debug option to get more log output.
> Run with --scan to get full insights.
> Get more help at https://help.gradle.org.

BUILD FAILED in 10m 23s
64 actionable tasks: 64 executed
==> ERROR: A failure occurred in build().
    Aborting...
 -> error making: bisq2-exit status 4
 -> Failed to install the following packages. Manual intervention is required:
bisq2 - exit status 4
```

###### Así que tuve que instalar `yay -S jdk22-openjdk` y ejecutar `sudo archlinux-java set java-22-openjdk`. Logré instalar el paquete `bisq2`.
```bash
yay -S jdk22-openjdk
sudo archlinux-java set java-22-openjdk
yay -S bisq2
```
