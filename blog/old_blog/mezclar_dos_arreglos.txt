---
title: "Mezclar dos arreglos"
date: 2025-02-02T20:53:13-03:00
tags: ['c']
---
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  size_t len;
  int *array;
}size_array;

int main(){
  size_array arr1 = { 20, NULL };
  arr1.array = malloc(arr1.len*sizeof(*arr1.array));

  size_array arr2 = { 10, NULL };
  arr2.array = malloc(arr2.len*sizeof(*arr2.array));

  for (int i = 0; i < arr1.len; i++){
    arr1.array[i] = i+4;
  }
  printf("Array 1:");
  for (int i = 0; i < arr1.len; i++){
    if (i == arr1.len-1) printf("%d", arr1.array[i]);
    else printf("%d,", arr1.array[i]);
  }
  printf("\n");
  for (int i = 0; i < arr2.len; i++){
    arr2.array[i] = i+24;
  }
  printf("Array 2:");
  for (int i = 0; i < arr2.len; i++){
    if (i == arr2.len-1) printf("%d", arr2.array[i]);
    else printf("%d,", arr2.array[i]);
  }
  printf("\n");

  size_array arr3 = { arr1.len+arr2.len, NULL };
  arr3.array = malloc(arr3.len*sizeof(*arr3.array));

  int j = 0;
  for (int i = 0; i < arr3.len; i++){
    if (i < arr1.len){
      arr3.array[i] = arr1.array[i];
    }else{
      arr3.array[i] = arr2.array[j++];
    }
  }

  printf("Merge array: ");
  for (int i = 0; i < arr3.len; i++){
    if (i == arr3.len-1) printf("%d", arr3.array[i]);
    else printf("%d,", arr3.array[i]);
  }

	return 0;
}
```
