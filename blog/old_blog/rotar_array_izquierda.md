---
title: "Rotar array a la izquierda"
date: 2025-02-01T22:11:37-03:00
tags: ['c']
---
```c
#include <stdio.h>
#include <stdlib.h>

struct array_len {
  size_t len;
  int *array;
};

int main(){
  struct array_len arr = { 4, NULL };
  arr.array = (int*)malloc(arr.len*sizeof(int));

  printf("Longitud del array: %d\n",arr.len);

  for (int i = 0; i < arr.len; i++){
    arr.array[i] = i+1;
  }

  printf("Rotar a la izquierda\n");
  printf("Cuantos movimientos hacia la izquierda desea rotar:");

  int movimientos;
  scanf("%d",&movimientos);

  for (int i = 0; i < movimientos; i++){
    int *array2 = malloc(arr.len*sizeof(int));
    for (int j = 1; j < arr.len; j++){
      array2[j-1] = arr.array[j];
    }
    array2[arr.len-1] = arr.array[0];
    free(arr.array);
    arr.array = array2;
  }

  printf("Array rotado a la izquierda: {");
  for (int i = 0; i < arr.len; i++){
    if (i == arr.len-1) printf("%d", arr.array[i]);
    else printf("%d,", arr.array[i]);
  }
  printf("}\n");

  return 0;
}

```
