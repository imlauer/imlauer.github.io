---
title: "Ed editor"
date: 2024-12-17T21:43:52-03:00
tags: ['unix']
---
Con este editor Dennis Ritchie y Ken Thompson programaron un sistema operativo completo.

**Instalación**

```bash
sudo pacman -S ed
```

**Uso**

```bash
ed hola.txt
a # Te pone en modo insert
Escribi tu texto
. # Te saca del modo insert
w # Escribe al archivo
p # Imprime en donde esta el cursor
1 # Mueve el cursor a la linea 1.
/algo # Mueve el cursor en donde esta algo
,n # Muestra todas las líneas
/return 
c # Borra una linea y te pone en modo insert luego tenés que usar . para salir de insert mode.
d # Borra una linea
```
