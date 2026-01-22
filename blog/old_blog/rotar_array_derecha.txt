---
title: "C: Rotar array derecha"
date: 2025-02-02T19:56:29-03:00
tags: ['c']
---
```c
#include <stdio.h>
#include <stdlib.h>

struct myarray {
  size_t len;
  int *array;
};

int main(){
  struct myarray arr = { 4, NULL };
  arr.array = (int*)malloc(arr.len*sizeof(arr.array));
  int movimientos;
  printf("Cuantos movimientos querés rotar hacia la derecha?: ");
  scanf("%d",&movimientos);

  for (int i = 0; i < arr.len; i++){
    arr.array[i] = i+1;
  }
  for (int i = 0; i < movimientos; i++){
    struct myarray arr2 = { arr.len , NULL };
    // Armo un nuevo array con los 3 elementos menos exceptuando el primero 
    // y el último elemento será el primero.
    // 4 movimientos
    // [1,2,3,4]
    // [4,1,2,3]
    // [3,4,1,2]
    // [2,3,4,1]
    // [1,2,3,4]
    arr2.array = (int *) malloc(arr.len*sizeof(int));
    for (int i = 1; i < arr.len; i++){
      arr2.array[i] = arr.array[i-1];
    }
    arr2.array[0] = arr.array[arr.len-1];
    free(arr.array);
    arr.array = arr2.array;
  }

  for (int i = 0; i < arr.len; i++){
    if (i == arr.len-1) printf("%d",arr.array[i]);
    else printf("%d,",arr.array[i]);
  }

	return 0;
}
```
