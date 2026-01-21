---
title: "Huayra 5 a Huayra 6 e Instalación de Docker"
date: 2024-12-22T11:52:04-03:00
tags: ['huayra']
draft: true
---
Primero vamos a pasar de Debian 10 a Debian 11.
En `/etc/apt/sources.list` tenes que cambiar buster a bullseye y comentá las líneas bulleyes-updates porque está deprecado.

```bash
sudo apt update
sudo apt upgrade
sudo vim /etc/apt/sources.list
```

Cambia `buster` por `bulleye` luego ejecutá: `sudo apt disc-upgrade`.

Luego seguí éstos pasos: https://imlauera.github.io/install_docker_debian/
