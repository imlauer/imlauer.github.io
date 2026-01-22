---
title: "Ricardo Narvaja: Exámen 13 (Ejecutar calculadora)"
date: 2024-08-27T14:54:32-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
_DWORD *__thiscall this_50(_DWORD *this)
{
  this[50] = "A ejecutar la calculadora de nuevo...\n";
  return this;
}
int __cdecl sub_401040(int a1, int a2, char *FileName)
{
  FILE *Stream; // [esp+0h] [ebp-4h]

  Stream = fopen(FileName, "rb");
  fread(FileName + 204, 300u, 1u, Stream);
  printf("Salida %s\n", a2);
  dword_403020 = dword_403024 + *(FileName + 102);
  (dword_403020)(a2);
  return 0;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char Buffer[200]; // [esp+0h] [ebp-268h] BYREF
  char Destination[404]; // [esp+C8h] [ebp-1A0h] BYREF
  FILE *Stream; // [esp+25Ch] [ebp-Ch]
  int (__cdecl *v7)(char *, char); // [esp+260h] [ebp-8h]
  char v8[4]; // [esp+264h] [ebp-4h]

  if ( argc < 2 )
  {
    printf("bye: \n", Buffer[0]);
    exit(1);
  }
  this_50(Destination);
  v7 = (&system + 110);
  dword_403024 = &system + 110;
  memset(Destination, 0, 0xC8u);
  memset(&Destination[204], 0, 0xC8u);
  memset(Buffer, 0, sizeof(Buffer));
  strcpy(Destination, argv[1]);
  Stream = fopen(Destination, "r");
  if ( !Stream )
  {
    printf("No se puede leer el archivo bye bye \n", Buffer[0]);
    exit(1);
  }
  printf("%s\n", Destination[200]);
  fread(Buffer, 200u, 1u, Stream);
  *v8 = strlen(Buffer);
  printf("Largo =%d\n", v8[0]);
  fclose(Stream);
  if ( *v8 != 4 )
    v7 = printf;
  sub_401040(*v8, Buffer, Destination);
  return 0;
}
```
