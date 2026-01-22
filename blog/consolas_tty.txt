---
title: "Emuladores de consolas en TTY: fbterm, yaft y kmscon"
date: 2025-07-14T13:12:19-03:00
tags: ['linux']
---
Kmscon es un emulador de terminal simple basado en la configuración del modo kernel de Linux. Reemplaza la implementación de VT en el kernel con una consola de espacio de usuario.

##### Instalación en ArchLinux.
```bash
yay -S kmscon-patched-git
```
##### Iniciando el servicio.
```bash
sudo systemctl start kmscon 
```

---

FBTerm es una terminal de emulación de VT100 que se ejecuta en modo framebuffer, que es una forma de mostrar gráficos en una pantalla de computadora sin utilizar un servidor de ventanas como X11. En otras palabras, FBTerm permite utilizar una terminal de comando en un entorno gráfico sin necesidad de arrancar un sistema de ventanas completo.

```bash
yay -S fbterm yaft
```

Uso: `fbterm`
