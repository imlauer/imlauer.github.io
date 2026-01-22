---
title: "Ricardo Narvaja: Exámen 23 (kernel32.dll) 64 bits"
date: 2024-08-27T14:54:39-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  int v4; // ebx
  char Buffer[4]; // [rsp+20h] [rbp-E8h] BYREF

  qword_140003628 = GetModuleHandleA("kernel32.dll");
  while ( 1 )
  {
    Stream = fopen("fichero.dat", "a+");
    if ( !Stream )
      break;
    v3 = _acrt_iob_func(0);
    fgets(Buffer, 450, v3);
    fwrite(Buffer, 1uLL, 450uLL, Stream);
    v4 = *Buffer;
    fclose(Stream);
    if ( v4 == 0x41424344 )
      return 0;
  }
  perror("No se puede escribir fichero.dat");
  printf("%x");
  return -1;
}
```
