---
title: "Sizeof: no puede usarse para determinar longitud de un arreglo declarado con malloc"
date: 2025-02-01T20:32:49-03:00
tags: ['c']
---
Sizeof cannot be used on dynamically allocated memory.

You cannot use `SIZEOF_ARRAY` to tell you the size of an array you created using `malloc`. You're getting a size of one because your macro is using the size of the pointer to the "mallocated" memory to calculate its result. The pointer is two bytes, as is sizeof int, so 2/2 gives one.

```c
struct remember_the_size
{
    size_t len;
    int * arr;
};
int main() {
  struct remember_the_size a = { 10, NULL };
  a.arr = (int*) malloc(a.len * sizeof(int));
  int i;
  for(i=0;i<a.len;i++){
    Serial.println(a.arr[i]);
  }
  Serial.print("Size :");
  Serial.println(a.len);
  free(a.arr);
}

```

https://stackoverflow.com/questions/71503505/do-i-need-to-put-sizeof-after-array-length-in-malloc
