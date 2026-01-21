---
title: "Por que es importante aprender bajo nivel?"
date: 2024-10-11T12:19:01-03:00
tags: ['bajo','nivel']
---
Hoy en día la gente programa en un framework que está escrito sobre un lenguaje por ejemplo Laravel está escrito en PHP, a su vez PHP está escrito en C, y C está escrito en C. Cuando aprendés ASM entendés por qué existe C, cuando aprendés C entendés por qué existe C++, cuando aprendés C++ entendés por qué existe Python.
Y también programan sobre un framework de Javascript como Vue.JS o Angular o una librería como ReactJS, que a su vez Javascript está escrito en C, hay toda una complejidad que se están salteando, tenés que entender el bajo nivel para saber por se llegó a hacer esa solución.

Le pointers and le C
```c
#include <stdio.h>
#include <string.h>

int main()
{
    int a;
    char buffer[20];
    char buffer2[10];

    printf("Ingresá tu nombre: ");
    scanf("%s",buffer); // Por qué acá buffer es un puntero? Si sabés ASM al toque te darás cuenta cuando generás el código asm con gcc -S

    printf("Ingresá un número: ");
    scanf("%d",&a);
    printf("El valor de buffer2 es: %s\n",buffer2);
    return 0;
}
```

Para ingresar una entrada de datos tenés que escribir `"%s"` para demostrar que querés ingresar una cadena. En cambio en C++ miremos un ejemplo en C++:


```cpp
#include <iostream>
using namespace std;

int main()
{
    int a;
    cout << "Ingresá un número" << endl;
    cin >> a;
    cout << "La variable a vale: " << a;
}
```

Acá ni siquiera tenés que pasarle el puntero.
