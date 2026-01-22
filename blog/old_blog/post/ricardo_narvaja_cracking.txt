---
title: "Explicación de todos los exámenes de buffer overflow de Ricardo Narvaja Reversing"
date: 2024-08-08T06:01:01-03:00
tags: ['reversing','ricardo','narvaja','examen']
---
Todos sus videos consisten en explotar diferentes tipos de buffer overflows en programas 32 bits, y me parece que a veces se enfoca demasiado en la utilización de la herramienta IDA en lugar de explicar primero lo más importante que es: ¿por qué la aplicación es vulnerable a esos ataques? Si se entiende eso, se tiene una mejor intuición de como funciona. Estoy hablando específicamente de los cursos que tiene en su canal Ricardo Narvaja. Otra cosa es que no muestra el código C vulnerable, creo que si mostrara el código C vulnerable sería más entendible. Claramente no está hecho para principiantes, parece que hizo esos videos para no olvidarse de los métodos que usa no con el objetivo de enseñar, es muy improvisado. De todas formas es valiosa la información.

https://redirect.invidious.io/channel/UCDeWwrp2LUWkDSymrmnfKDQ

#### Examen 1
[Explotando un buffer overflow provocado al querer restringir/comparar el tamaño del buffer sin considerar el signo.](/post/buffer_overflow_curso1/)
#### Examen 2
[Explotando el típico buffer overflow copia un buffer mas grande a uno más chico.](/post/bufferoverflow_strcpy/)
#### Examen 3
[Explotando buffer overflow provocado por copiar un buffer de 300 a uno de 200](/post/bufferoverflow_3/)
#### Examen 4
[Explotando buffer overflows: copia un buffer de 200 bytes a otro del mismo tamaño pero con una string agregada.](/post/bufferoverflow_4/)   
#### Examen 5
[Un poco más complejo, juega copiando contenido del archivo en diferentes posiciones del buffer e insertando texto comienzo](/post/bufferoverflow_5/)   
#### Examen 6
[No es un bufferoverflow simplemente comparaciones para familiarizarte con ASM](/post/buffer_overflow_6/)   

Tiene dos buffers de 200 bytes, pero copia de un buffer al otro usando un sprintf que agrega una cadena al final de la cadena del 1er buffer al 2do buffer de 200 entonces se produce un overflow en el buffer2.    
Algo así como:   
```c
char buffer1[200], char buffer2[200];

// Copia el contenido del buffer1 al buffer2 pero le agrega "Bien ? con" que hace desboardarlo porque sobrepasa los 200 bytes.
sprintf(buffer2, "Bien ? con %s", buffer1);
```

#### Examen 7
[Exploit](/post/buffer_overflow_7/)   

Casi lo mismo que el exámen 6, la diferencia es que ahora el buffer no está arriba de todo y no podés pisar todas las variables que están debajo porque el buffer vulnerable está al final de la pila.   

Tiene dos buffers del mismo tamaño (200 bytes), pero se produce el overflow porque usa una sprintf que agrega una cadena al comienzo de la cadena y lo completa con una string: `"Bieeeeeeeeeeeeeeeeeeeeeeeeeeen ? con %s"`

El problema de este exámen es que debajo del buffer2 no hay ninguna variable para pisar, porque en los exámenes anteriores al pisar el buffer como estaba arriba de todo podiamos pisar las variables de abajo, ahora no.

Pero en este caso desbordando el buffer2 pisar el puntero `return address` de la función `check` y vamos a hacer que apunte a la dirección en donde dice `"Aprobaste level 7"`

Tenemos que desbordar el buffer2 y desbordar la struct que está debajo y con 4 bytes más pisamos el store de bp, y otros 4 bytes más pisamos el return address y ahí tenés que poner la dirección de memoria adonde querés que tu programa salte.

---

En este video te enseña a usar el debugger y poner breakpoints en el return address y mirar el stack view con IDA, para verificar que la cuenta estaba bien.

En estos tutoriales el tema es reversearlos lo mas estaticamente posible con la menor cantidad de debugging.
Hay algunos shellcodes que dejaron de funcionar a partir de ciertos udpates de windows posteriores a la fecha de publicacion del video, si es asi reemplazarlo por otro shellcode, en Internet hay miles, o pueden armar uno propio, el GOAL es ejecutar codigo y eso se logra aunque el shellcode haya dejado de funcionar.

---

#### Examen 8
Buffer overflow provocado por una concatenación (strcat), va a overfloodear porque tenemos dos buffers cada uno de 200 bytes, pero el strcat concatena ambas cadenas y la guarda en el primer buffer y esto overflodea porque el buffer solo permite 200 y concatenandolo le agregamos 200 bytes mas.   
El objetivo ejecutar una calculadora.
Lee 200 bytes esos 200 lo lee a buffer2 y despues lo copia al incio de la estructura. 

#### Examen 9
Es un poco mas complicado.

No se si hay un buffer overflow acá, el objetivo es ejecutar una calculadora también.

Dos buffers de 200 bytes.
Puntero a una funcion llamada system que nos permitirá ejecutar la calculadora si podemos modificar el return address.
El 1er byte del buffer1 tiene que ser 30 para que no saltee una función.
Luego concatena strings con strcat pero verifica la longitud, entonces para saltear esa protección pone un `'\0'` en el medio porque strcpy copia hasta ahí.   
Le pone un `'00'` en la posicion 12 del buffer1, con el strcpy solo copiara hasta esa posicion.     
Pero en el buffer2 se va leer todo porque es un fread y no se corta con el 0.
Tenemos que hacer que la suma nos de 38 al concatenar con `string_a_ejecutar`.

#### Examen 10
Apretando t si armamos toda la estructura podemos convertir 
`dword ptr [eax+1A8h]` a `mov [eax+My_struct.var_C], offset aAEjecutarLaCal`


Hace lo mismo que el ejercicio anterior, hace un `strcat` lee la string a ejecutar con el buffer1, que es la string que tiene en el buffer1 es hasta el 1er 0 y el largo tiene que ser 38.
La string a ejecutar tiene 36 de largo y el total que tengo que tener es 38, entonces el lugar en donde tengo que poner el 00 es la posición 12 como en el video anterior.
Por lo cual en el buffer2 vamos a tener todo pero en el buffer1 solo hasta la posición 12 porque tenemos el 00, porque strcpy solo copia hasta el 0.

---
El resto de los videos son una pérdida de tiempo para mi.
