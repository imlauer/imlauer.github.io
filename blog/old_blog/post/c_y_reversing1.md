---
title: "C y reversing"
date: 2024-09-03T20:02:06-03:00
tags: ['reversing','ricardo','narvaja']
---
Reverseamos un hola mundo.

```c
#include <stdio.h>

int main(){
	printf("Hola Mundo\n");
	return 0;
}
```

![](/img/cracking/curso/ida_hello_world.png)

Aquí vemos que el compilador modifico nuestro main haciéndolo una función de tres argumentos que no son nuestros, sino del compilador,  y tiene una variable. `var_4`  que creo el compilador la cual si hacemos las cuentas devolverá siempre 10 y la utilizara el compilador al cerrar el programa,  por supuesto nada de esto es código propio, vayamos a nuestro código, propiamente dicho.

**.text:004012BA mov     dword ptr [esp], offset aHola ; "hola"**
**.text:004012C1 call    printf**

Allí vemos que pone en el stack un puntero a la string hola que esta en la sección rdata, si hacemos click en aHola, nos muestra que esta exactamente en 403000 y que es el argumento de la funcion printf.

![Dirección de memoria del hola](/img/cracking/curso/hola.png)

Si vamos a DEBUGGER y elegimos por ejemplo el debugger local de win32

![Seleccionar debugger](/img/cracking/curso/select_debugger.png)

y ponemos breakpoint alli.

![breakpoint](/img/cracking/curso/breakpoint.png)
