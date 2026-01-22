---
title: "Free pointer of pointers"
date: 2025-02-08T18:44:48-03:00
tags: ['c']
---
Sólo tenés que pensar en liberar memoria cuando tenés un programa muy grande que pide un poco de memoria en un loop y eso acumula memoria con el tiempo, pero si tenés un programa batch (por lotes) que pide memoria (allocated memory), no hay necesidad de liberar esa memoria porque el sistema operativo lo hará por vos cuando el programa finalice. (Leer al final más info).

No podes "liberar" un puntero de punteros. **Tenés que liberar todo lo que fue creado con malloc.**

Si definiste así: `static char buffer[25]` esto no necesita ser liberado.

### Ejemplo
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(){
  FILE *f = fopen("/tmp/asdf", "r+");
  if ( f == NULL ){
    printf("%s\n",strerror(errno));
    return -1;
  }
  char *palabra = malloc(30*sizeof(char));

  char **texto = malloc(sizeof(char*));
  int cantidad_palabras = 0;
  while ( fscanf(f, "%30s", palabra) == 1 ){
    puts(palabra);
    texto[cantidad_palabras] = malloc(30*sizeof(char));
    strncpy(texto[cantidad_palabras], palabra, 30);
    cantidad_palabras++;
    texto = realloc(texto, (cantidad_palabras+1)*sizeof(char*));
  }

  printf("Palabras cargadas: \n");
  for (int i = 0; i < cantidad_palabras; i++){
    printf("%s\n",texto[i]);
  }
  printf("Cantidad de palabras leídas: %d\n",cantidad_palabras);

  free(palabra);
  for (int i = 0; i < cantidad_palabras; i++){
    free(texto[i]);
  }
  free(texto);

	return 0;
}
```

https://stackoverflow.com/questions/33170802/c-does-freeing-an-array-of-pointers-also-free-what-theyre-pointing-to

Quizás como es un programa de lotes (batch program) podés alocarlo y no desalocar nada porque todo será "desalocado" (free) al final del programa de todas formas porque será desalocado por el sistema operativo cuando el programa terminó.  Los sistemas operativos modernos cerrarán todos los archivos que abriste y unmap todas las regiones de memoria en las que hiciste un map.


