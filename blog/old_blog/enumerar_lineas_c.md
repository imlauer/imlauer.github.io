---
title: "Agregar enumeración líneas en C"
date: 2025-02-15T22:01:09-03:00
tags: ['C']
---
```bash
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Agregá enumeración de cada línea de un archivo.
// Vim agrega un salto de línea siempre al final, 
// por lo tanto usaremos echo: 
// echo -n -e "Hola\nEsto es\nuna prueba"
int main(void){
    FILE *fp = fopen("/tmp/asdf", "rw+");
    FILE *fq = fopen("/tmp/resultado", "w+");
    int lineas = 1;

    int c;

    char buffer[3] = "1: ";
    for (int i = 0; i < strlen(buffer); i++){
        putc(buffer[i], fq);
    }

    while (( c = getc(fp) ) != EOF){
        putc(c, fq);
        if ( c == '\n'){ 
            lineas++;
            sprintf(buffer, "%d :", lineas); 
            for (int i = 0; i < strlen(buffer); i++){
                putc(buffer[i], fq);
            }
        }
    }
    printf("\n");

    printf("Cantidad de lineas: %d\n",lineas);

    return 0;
}
```
