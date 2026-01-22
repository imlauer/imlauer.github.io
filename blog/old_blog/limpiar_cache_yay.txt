---
title: "Limpiar cache de yay en Arch"
date: 2024-11-12T10:34:17-03:00
tags: ['yay']
---
```bash
yay -Sc --aur
yay -Scc
sudo paccache -rk1
```

Alias para Simplificar: Si prefieres que yay siempre limpie solo la caché de AUR, puedes crear un alias en tu archivo .bashrc o .zshrc:
bash
```bash
alias yay='yay --aur'
```
