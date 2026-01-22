---
title: "Como funciona static en C"
date: 2024-12-29T08:06:08-03:00
tags: ['static']
---
Respuesta corta ... depende.

1. Las variables locales definidas static no pierden su valor entre las llamadas de función. En otras palabras, son variables globales, pero alcanzan la función local en la que se definen.

2. Las variables globales static no son visibles fuera del archivo C en el que se definen.

3. Las funciones static no son visibles fuera del archivo C en el que se definen.

**Ejemplo:**

```c
#include <stdio.h>

const char *string(){
        static char *helloworld = "Hello World.\n";
        return helloworld;
}

int main(){
        printf("%s",string());
        return 0;
}
```
