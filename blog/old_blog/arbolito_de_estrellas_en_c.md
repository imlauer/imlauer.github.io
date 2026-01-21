---
title: "Arbolito de estrellas en C"
date: 2025-01-30T15:48:50-03:00
tags: ['c']
---
```c
#include <stdio.h>

int main(){
  int filas;
  printf("Ingrese número de filas (mínimo 3): ");
  scanf("%d",&filas);

  if (filas < 3) {
    fprintf(stderr,"Te dije que el número de filas no puede ser menor que 3\n");
    return(-1);
  }

  int espacios = filas;
  for (int i = 0; i < filas; i++){
    for (int espacios = filas-i-1; espacios > 0; espacios--){
      printf(" ");
    }
    for (int z = 0; z <= i*2; z++) printf("*");
    printf("\n");
  }
	return 0;
}
```
