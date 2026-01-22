---
title: "Desactivar greeting message fish"
date: 2024-11-04T15:14:01-03:00
tags: ['fish']
---
```bash
cd .config/fish/
touch fish_greeting.fish
```
En el archivo `config.fish` agregá:

```bash
set fish_greeting
```

Alternativamente podés usar: `set -U fish_greeting ""`
