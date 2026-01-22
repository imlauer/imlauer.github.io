---
title: "Error de Segmentación (Segmentation Fault) en C"
date: 2023-10-05T05:22:12-03:00
tags: ['c','programacion']
---
### Escenarios comunes de fallas de segmentación
En una falla de segmentación, un programa intenta acceder a una memoria a la que no está autorizado o que no existe. Algunos escenarios comunes que pueden causar fallas de segmentación son:

1. Modificar una cadena de solo lectura
2. Acceder a una dirección que está liberada
3. Acceder a límites de índice fuera de la matriz
4. Uso inadecuado de scanf()
5. Desbordamiento de pila
6. Desreferenciación de puntero no inicializado

#### 1. Modificar una cadena de sólo lectura
Los literales de cadena se almacenan en la sección de solo lectura de la memoria. Es por eso que el siguiente programa puede fallar (da un error de segmentación) porque la línea *(str+1) = 'n' intenta escribir una memoria de solo lectura.

```c
// Programa de C para demostrar error de segmento (segmentation fault)
// modificando una cadena de sólo lectura
#include <stdio.h>

int main()
{
	char* str;

	// Se almacena en la parte de solo lectura del segmento de datos
	str = "GfG";

	// Problema: intentando modificar memoria de sólo lectura
	*(str + 1) = 'n';
	return 0;
}
```

### 2. Acceder a una dirección liberada
Aquí, en el siguiente código, se elimina la referencia al puntero p después de liberar el bloque de memoria, lo cual no está permitido por el compilador. Estos punteros se denominan punteros colgantes y producen fallos de segmento o terminaciones anormales del programa en tiempo de ejecución.

```c
// Programa C para demostrar el error de segmentación
// Accediendo a una dirección que está liberada
#incluir <stdio.h>
#incluir <stdlib.h>

int main(void)
{
	// asignando memoria a p
	int* p = (int*)malloc(8);
	*p = 100;

	// se libera el espacio asignado a p
	free(p);

	// core dump/segmentation fault
	*p = 110;
	printf("%d", *p);

	return 0;
}
```

#### 3. Acceder al índice de matriz fuera de límites
En C y C++, acceder a un índice de matriz fuera de límites puede provocar un error de segmentación u otro comportamiento indefinido. No hay verificación de límites para matrices en C y C++. Aunque en C++, el uso de contenedores, como con el método std::vector::at() o con una declaración if(), puede evitar errores fuera de límite.

```c
// programa C para demostrar la segmentación
// falla cuando se accede a la matriz fuera de límite.
#incluir <stdio.h>

int main(void)
{
	int arr[2];

	// Accediendo fuera de límites
	arr[3] = 10;

	return (0);
}
```

#### 4. Uso inadecuado de scanf()
La función scanf() espera la dirección de una variable como entrada. Aquí, en este programa, n toma un valor de 2 y asume que su dirección es 1000. Si pasamos n a scanf(), la entrada obtenida de STDIN se coloca en la memoria 2 no válida, que debería ser 1000. Esto provoca daños en la memoria y provoca un error de segmentación.

```c
// Programa C para demostrar la segmentación
// error cuando se pasa valor a scanf
#incluir <stdio.h>

int main()
{
	int n = 2;
	scanf("%d", n);
	return 0;
}
```

#### 5. Desbordamiento de pila
No es un problema relacionado con el puntero, incluso es posible que el código no tenga un solo puntero. Es por quedarse sin memoria en la pila. También es un tipo de corrupción de memoria que puede ocurrir debido a un gran tamaño de matriz, una gran cantidad de llamadas recursivas, muchas variables locales, etc.

```c
// Programa en C para ilustrar el
// error de segmentación debido a
// desbordamiento de pila
#incluir <stdio.h>

int main()
{
	int arr[2000000000];
	return 0;
}
```

#### 6. Desbordamiento del búfer
Si los datos que se almacenan en el búfer son mayores que el tamaño asignado del búfer, se produce un desbordamiento del búfer que provoca un error de segmentación. La mayoría de los métodos en lenguaje C no realizan verificación de límites, por lo que el desbordamiento del búfer ocurre con frecuencia cuando olvidamos asignar el tamaño requerido al búfer.

```c
// Programa en C para ilustrar el
// fallo de segmentación debido a
// desbordamiento del buffer
#incluir <stdio.h>

int main()
{
	char ref[20] = "Esta es una cadena larga";
	char buf[10];
	sscanf(ref, "%s", buf);
	return 0;
}
```

#### 7. Desreferenciar un puntero NULL o no inicializado
Es un error de programación común eliminar la referencia a un puntero no inicializado (puntero salvaje), lo que puede dar como resultado un comportamiento indefinido. Cuando se utiliza un puntero en un contexto que lo trata como un puntero válido y accede a su valor subyacente, aunque no se haya inicializado para apuntar a una ubicación de memoria válida, se produce este error. Esto puede provocar daños en los datos, errores de programa o fallos de segmentación. Dependiendo de su entorno y estado al eliminar la referencia, los punteros no inicializados pueden producir resultados diferentes.

Como sabemos, el puntero NULL no apunta a ninguna ubicación de memoria, por lo que eliminar la referencia resultará en un error de segmentación.

```c
// Programa C para demostrar la segmentación
// error cuando el puntero no está inicializado
// se accede
#incluir <stdio.h>

int main()
{
	int* ptr;
	int* nptr = NULL;
	printf("%d %d", *ptr, *nptr);
	return 0;
}
```
