---
title: "Dos comandos de vim alucinantes"
date: 2023-11-17T00:46:54-03:00
tags: ['vim']
---

**Alguna vez quisiste usar las keybindings de VIM al escribir un comando después de presionar Escape y los dos puntos (:) ?**

Bueno, hay una forma de hacerlo y es usando Control-F luego de escribir los dos puntos, ahí escribís el comando usando las keybindings y le das enter para ejecutarlo.

___
Seleccionar todas las líneas que empiecen con una palabra y agregar algo al final y al comienzo de esas líneas seleccionadas

```bash
Shift+v (seleccioná las líneas) con j y k te movés.
:g/^pacman/norm!Iescribí acá el texto que se agregará al comienzo
:g/^pacman/norm!Aescribí acá el texto que se agregará al final
```

O si lo querés hacer globalmente en todo el texto:
```bash
:g/^12138/norm!Asomething_at_the_end
```


![Mind Blown](/files/mindblown.gif)
