---
title: "Race conditions, ejemplo en C"
date: 2024-11-24T19:41:56-03:00
tags: ['hacking']
---
Race conditions en C son situaciones en las que, al ejecutar múltiples hilos o subprocesos de forma concurrente, la secuencia de ejecución de las operaciones puede generar un comportamiento inesperado o incorrecto. **Esto se deber a que los hilos acceden y modifican variables compartidas sin sincronizar apropiadamente.**

### Ejemplo en C:

Supongamos dos hilos que intentan cambiar el valor de una variable compartida, x, entre 0 y 1:

```c
#include <stdio.h>
#include <threads.h>

// Variable compartida
int x = 0;

void *hilo1(void *arg) {
    // Cambiar x de 0 a 1
    x = 1;
    // Esperar un tiempo aleatorio
    thrd_sleep((struct timespec[]){{1, 0}}, NULL);
    return NULL;
}

void *hilo2(void *arg) {
    // Cambiar x de 1 a 0
    x = 0;
    return NULL;
}

int main() {
    thrd_t h1, h2;
    thrd_create(&h1, hilo1, NULL);
    thrd_create(&h2, hilo2, NULL);
    thrd_join(h1, NULL);
    thrd_join(h2, NULL);

    // Imprimir el valor de x
    printf("x = %d\n", x);
}
```

Sin sincronización adecuada, el resultado final de x podría ser inesperado, ya que los hilos pueden ejecutarse en orden erróneo. Por ejemplo, puede que hilo2 cambie x a 0 antes de que hilo1 cambie x a 1. Un posible resultado incorrecto sería que x sea 0.

Para resolver este problema, se deberían utilizar mecanismos de sincronización, como semáforos, mutexes o condiciones de variación, para asegurar el acceso apropiado a las variables compartidas.
