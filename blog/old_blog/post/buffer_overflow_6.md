---
title: "Buffer Overflow Examen 6 (Ricardo Narvaja Reversing)"
date: 2024-08-20T18:04:05-03:00
tags: ['ricardo','narvaja','reversing','examen','ida']
---

El IDA me lo decompila a :
```c
void *check(void *this)
{
  this[102] = 0;
  this[104] = "Aprobaste level 6";
  this[105] = "A practicar y repasar mas ...";
  return this;
}

int check3(char *Destination)
{
  // Concatenación.
  strcat(Destination, Destination[105]);
  if ( strlen(Destination) == 229 )
  {
    if ( Destination[4] == 0x49 )
      Destination[50] = 1;
    if ( Destination[5] != 0x50 )
      Destination[50] = 0;
  }
  return 0;
}

int check2(char *Destination)
{
  check3(Destination);
  if ( Destination[50] == 1 )
    printf("%s\n", Destination[104]);
  else
    printf("%s\n", Destination[105]);
  return 0;
}


int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Destination[200]; // [esp+0h] [ebp-1A8h] BYREF
  int v5; // [esp+C8h] [ebp-E0h] BYREF
  FILE *Stream; // [esp+CCh] [ebp-DCh]
  char Buffer[200]; // [esp+D0h] [ebp-D8h] BYREF
  int *puntero_a_v5; // [esp+19Ch] [ebp-Ch]

  check(Destination);
  v5 = 0;
  puntero_a_v5 = &v5;
  memset(Buffer, 0, 200*sizeof(char));
  memset(Destination, 0, sizeof(Destination));
  Stream = fopen("example.txt", "rb");
  if ( !Stream )
  {
    printf("No se puede leer el archivo bye bye \n", Destination[0]);
    exit(1);
  }
  fread(Buffer, 200*sizeof(char), 1u, Stream);
  strcpy(Destination, Buffer);
  check2(Destination);
  return 0;
}
```

Tenés que hacer que Destination[4] (el 5to caracter porque empieza desde 0) tiene el valor de 0x49 que representa la letra **I** y si ese vale I entonces Destination[50] valdrá 1 y el 6to caracter tiene que ser cualquier cosa diferente de P (0x50) porque sino Destination[50] se hace 0 y si Destination[50] es 1 **aprobamos el examen!** porque muestra el texto Destination[104] que contiene el string de aprobamos el examen.

### exploit
```c
AAAAIPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```
