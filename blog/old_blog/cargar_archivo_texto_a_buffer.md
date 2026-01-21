---
title: "Cargar texto de archivo a un array de arrays"
date: 2025-02-07T21:08:05-03:00
tags: ['c']
---
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(){
  FILE *f = fopen("/tmp/asdf","r+");
  if (f == NULL){ 
    fprintf(stderr, "Error al abrir el archivo: %d.\n", errno);
    printf("%s\n",strerror(errno));
    return -1;
  }

  char *palabra = malloc(sizeof(char)*20);
  int cantidad_palabras = 0;

  char **words = malloc(sizeof(char*));

  while ( fscanf(f, "%20s", palabra) == 1 ){
    words[cantidad_palabras] = malloc(sizeof(char)*20);
    strncpy(words[cantidad_palabras], palabra,20);
    cantidad_palabras++;
    words = realloc(words,(cantidad_palabras+1)*sizeof(char*));
  }
  printf("Ahora todas las palabras han sido cargadas a un arreglo de un arreglo\n");
  for (int i = 0; i < cantidad_palabras; i++){
    printf("%s ",words[i]);
  }

	return 0;
}
```
