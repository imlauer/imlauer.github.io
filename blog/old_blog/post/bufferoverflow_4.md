---
title: "Explotando buffer overflows: copia un buffer de 200 bytes a otro del mismo tamaño pero con una string agregada."
date: 2024-08-07T13:37:58-03:00
tags: ['reversing','ricardo','narvaja','examen','4','bufferoverflow']
---
El overflow se produce porque tenemos dos buffers de 200, tenemos un sprintf toma un buffer de 200 y le agrega un texto y lo guarda en el otro buffer de 200. Entonces como la otra puede ser cercana a 200 (200 menos el byte del `'\0'`), va a haber un overflow.

### Una posible primer solución (no funciona en este caso)
Dos buffers de 200 bytes. Llenamos el buffer con 200, strcpy copiará hasta donde encuentre un 0 y como el store de bp no puede ser 0 porque guarda el valor de bp de la función padre entonces esa dirección va a pendear(concatenar) y la va a copiar al buffer de destino y podemos producir un overflow por no poner un 0 final en la string, porque como estamos leyendo de un archivo de texto binario podemos poner cualquier byte y los 200 puede ser todas As y no necesariamente terminar en 0, entonces luego al copiarlo se copian las 200 As más cualquier cosa que haya a continuación hasta que encuentre un 0.
### Una mejor solución
Hacemos un archivo con 200 bytes pero con un final de 0 para que no se lee pendee(concatena) nada al final.
![](/img/cracking/4.png)

Si tenés `dword ptr [edx+0CCh], 45h` podes apretar T y ver si es un puntero de una estructura.

`cmp [edx+MyStruct.const_45], 45h`
Si yo overfloodee la constante de 45 ya no será de 45.

Agrego BBBBBBBBBB(10) para representar la primera parte del sprintf (Bien ? con) es decir para ver el offset.

Un offset dentro de una estructura de datos es un entero que indica el desplazamiento desde el incio del objeto hasta un punto o elemento dado.

