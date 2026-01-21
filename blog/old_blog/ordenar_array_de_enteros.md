---
title: "Ordenar array de enteros por la sumatoria más grande."
date: 2025-02-09T20:11:09-03:00
tags: ['c']
---

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmpint(int *p1, int *p2){
  int suma_p1 = 0;
  int suma_p2 = 0;
  //printf("elementos p1: %d\n",*(const int **)p1/sizeof(**(const int **)p1));

  for (int i = 0; i < 3; i++){
    suma_p1 += p1[i];
  }
  for (int i = 0; i < 3; i++){
    suma_p2 += p2[i];
  }
  printf("Suma p1: %d\n", suma_p1);
  printf("Suma p2: %d\n", suma_p2);

  if (suma_p1 < suma_p2) return 1;
  return 0;

}

static int
cmpstringp(const void *p1, const void *p2)
{
  // strcmp(*(const char **) p1, *(const char **) p2);
  // **(const int **)p1 = 1 
  // **(const int **)p2 = 20 

  return cmpint( *(int**)p1, *(int**)p2);
}

int
main(int argc, char *argv[])
{

    int *num1 = malloc(sizeof(int)*3);
    int *num2 = malloc(sizeof(int)*3);

    int **numeros = malloc(sizeof(int*)*2);
    

    num1[0] = 999;
    num1[1] = 9;
    num1[2] = 10;

    num2[0] = 20;
    num2[1] = 4;
    num2[2] = 123;

    numeros[0] = num1;
    numeros[1] = num2;

    // char **argv
    // qsort(&argv[1], argc - 1, sizeof(char*), cmpstringp);
    qsort(
			&numeros[0],
			2,
      sizeof(int*),
      cmpstringp
    );

    printf("Imprimimos el array con la suma más grande\n");
    for (int i = 0; i < 3; i++) {
      printf("%d ", numeros[0][i]);
    }
    
    exit(EXIT_SUCCESS);
}
```
