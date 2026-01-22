---
title: "Debuggear c con GDB"
date: 2025-02-08T02:22:43-03:00
tags: ['c']
---
```bash
gcc -ggdb find_length_string.c -o  find_length_string
gdb -q ./find_length_string
break main
run
tui enable
n
n
n
p variable
p puntero
p *puntero
n
n
...
O podes usar enter para repetir comando anterior.
```

Me gusta el debugger porque te obliga a analizar cada pequeño detalle porque si solo leyeras el código los ignorarías. El debugger te motiva a mirar los pequeños detalles porque podés mirar los específicos valores de una variable, eso es lo que hace más fácil de encontrar errores lógicos.
