---
title: "Vim EOF como UNIX"
date: 2024-11-01T07:21:00-03:00
tags: ['eof','linux']
---

[https://imlauer.blogspot.com/2024/10/vim-eof-como-unix.html](https://imlauer.blogspot.com/2024/10/vim-eof-como-unix.html)

El comando `:e ++ff=unix` te hará ver los ^M al final de cada línea.

Luego ejecutá `:%s/.\{1}$//` para eliminar el último caracter de todas las líneas


