---
title: "Explotando el típico buffer overflow copia un buffer mas grande a uno más chico."
date: 2024-08-07T06:03:47-03:00
tags: ['reversing','buffer','overflow','examen','2','bufferoverflow']
---

Lee 210 de un archivo en el 1er buffer, pero en el 2do buffer está el overflow porque `Dst`(Destination) es un buffer de 200 bytes. Le pasa un puntero, o sea la dirección del buffer Dst a la función `check`.


Si en una función se pasa un puntero y a partir de esa dirección se le suma un offset y se encuentran valores para comparar o distintos campos, sabemos que ahí hay una estructura, podría haber una estructura que abarque todas las variables de la primera función.

Sabemos que desde el inicio de `Dst` hasta C8(200) pertenecen a la estructura.
Entonces cuando llama a check está pasando la dirección de la estructura, 

De `cmp dword ptr [eax+0C8h],0` pasamos a `cmp [eax+struct_0.const_uno],0` definiendolo como estructura en el ida.


Chequea si es 0 la variable `constante_uno` que está dentro de la estructura.
Podemos hacer que esa variable sea 0 overflodeando **cuando hacemos el strcpy overfloademos el buffer Dst**.

El siguiente byte o dword a partir de 200 será la `constante_uno` 
#### Solucion
creamos un archivo llamado example.txt lo llenamos de cualquier letra por ejemplo: un montón de As (200 As) y luego 0(ceros), porque necesitamos pisar el valor de `constante_uno` para que la comparación de la `constante_uno` con 0 nos de verdadera.

