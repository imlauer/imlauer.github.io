---
title: "Cómo jugar league of legends en ArchLinux"
date: 2023-12-08T14:45:36-03:00
tags: ['league','of','legends','linux']
---

Primero de todo no lo recomiendo es una basura de juego y el instalador sólo me levantó a 80 grados la temperatura del procesador.

Se lo instalá con los siguientes comandos:
Primero instalá yay:

```bash
sudo pacman -Syu
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
### Comprobar si se instaló correctamente
yay --version
```

Ahora instalá el juego:	

```bash
yay -S wine-lol-bin
yay -S leagueoflegends-git
```
Primero instalá wine-lol-bin porque si instalás leagueoflegends-git sólo te va a compilar wine-lol cuando te podés bajar el binario directamente.


Eso es todo.
