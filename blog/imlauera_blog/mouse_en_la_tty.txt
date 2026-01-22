---
title: "Mouse en la TTY con GPM"
date: 2024-11-01T15:01:16-03:00
tags: ['tty']
---

```bash
sudo pacman -S gpm
```

Editá el archivo `/etc/conf.d/gpm`:

```text
GPM_ARGS="-m
/dev/input/mice -t imps2"
```


```bash
sudo systemctl enable gpm
sudo systemctl start gpm
```

Podés copiar y pegar seleccionando el texto y pegandolo con click derecho. 
