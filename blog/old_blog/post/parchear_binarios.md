---
title: "Parcheando una variable int en IDA (Parcheando binario)"
date: 2024-09-21T09:16:36-03:00
tags: ['binarios']
---
Primero instalá IDA y gcc.

Vamos a parchear el siguiente código.
```c
#include <stdio.h>
int main(){
 int the_number = 5;
 printf("Welcome to patch experiment.\n");
 printf("your number is: %d\n", the_number);
 return 0;
}
```
Lo compilamos con: `gcc patching.c -o patching`

Para saber que tipo de binario es: `file patching`

Abrimos el binario con IDA: `ida64 patching` con f5 decompilás el programa.

![codigo](/img/reversing/codigo.webp)

> `.text:0000000000001151 mov [rbp+var_4], 5`

Vamos a cambiar el valor del entero `the_number` a `77`.

#### Parcheamos 
Edit tab > patch program > change bytes > change bytes.

Ahí te saldrá la siguiente alerta:
![patch bytes](/img/reversing/patch_bytes.webp)

`05` es el valor del entero 5 de la variable `the_number` vamos a cambiar el valor a 77 para ello reemplazaremos `05` por `4d` y darle aceptar. 

La instrucción que era `mov [rbp+var_4], 5` ahora es `mov [rbp+var_4],77`. El siguiente paso es recompilar el programa a ELF (así se llama el tipo de binario en linux).

`Edit tab > Patch program > Apply patches to input file.`


Podemos ignorar la opción `start EA` y `end EA` en este caso (porque queremos que se vuelva a compilar todo el programa). Asegúrese de que el `input file` muestre la ruta a su archivo binario original.

Lo único que tenemos que hacer es hacer clic en Aceptar y el archivo de programa que ingresamos anteriormente se sobrescribirá con el nuevo programa que hemos parcheado. Alternativamente, podemos consultar la lista de verificación "Create Backup" si no desea que los archivos antiguos se sobrescriban con los nuevos.

Después de eso, simplemente ejecute el programa parcheado.
`chmod +x patching && ./patching`

Y listo, cambiamos el valor de la variable `the_number` de 5 a 77.
