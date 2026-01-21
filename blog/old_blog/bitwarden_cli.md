---
title: "Bitwarden cli"
date: 2024-12-18T13:20:55-03:00
tags: ['cli']
---
```bash
sudo npm install -g @bitwarden/cli
bw --help
bw login
```

Agregá `export BW_SESSION=...` a tu `.bashrc` o `.config/fish/config.fish`

Luego para buscar y listar los items.
```bash
bw list items --search google | jq .
```
