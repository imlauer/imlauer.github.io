---
title: "Sizeof(int) vs sizeof *var"
date: 2025-02-02T20:22:06-03:00
tags: ['c']
---
Un profesor me dijo que no debería usar.
```c
int *array = malloc(sizeof *array * length);
```

And that it should instead be:

```c
int *array = malloc(length * sizeof(int));
```

Both are valid, but many veteran programmers will prefer the way you did it.

The advantage of using sizeof \*array as opposed to sizeof(int) is that if you happen
to change the type of array then you don't need to change how you do the allocation.

There's also no technical reason to multiply by length first instead of the element
size. If anything, when looking at a call to malloc the first thing you want to know
is how many "things" you're allocating, so from a readability standpoint putting the
length first might make more sense. On the other hand, because the result of the
sizeof operator is unsigned, putting it first guarantees that the math is done with
unsigned types if you have multiple array dimensions.

You also don't want to cast the return value of malloc as that can mask other errors
in your code, specifically a missing #include <stdlib.h>

