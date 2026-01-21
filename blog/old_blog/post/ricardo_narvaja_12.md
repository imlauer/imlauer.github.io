---
title: "Ricardo narvaja: Exámen 12 (Ejecutar calculadora)"
date: 2024-08-27T14:54:22-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
Este tiene bufferoverflow en el nombre del archivo. Tenés que crear un archivo con un nombre muy largo y desborda y pisa el EIP.
Ejemplo: 
```
└─$ wine ConsoleApplication11.exe AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAA
wine: Unhandled page fault on read access to 41414141 at address 7B3630C6 (thread 00
24), starting debugger...
Unhandled exception: page fault on read access to 0x41414141 in wow64 32-bit code (0
x7b3630c6).
0114:err:dbghelp_msc:pe_load_debug_directory Got a page fault while loading symbols
winedbg: Internal crash at 7AC68CF4

```

Lo que me decompila el IDA:
```c
_DWORD *__thiscall this_50(_DWORD *this)
{
  this[50] = "A ejecutar la calculadora de nuevo...\n";
  return this;
}


int leer_buffer(int a1, void *Buffer, ...)
{
  FILE *Stream; // [esp+0h] [ebp-4h]
  va_list va; // [esp+14h] [ebp+10h] BYREF

  va_start(va, Buffer);
  Stream = fopen(va, "rb");
  fread(Buffer, 2000u, 1u, Stream);
  printf("Salida %s\n", Buffer);
  return 0;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[412]; // [esp-19Ch] [ebp-40Ch] BYREF
  char v5; // [esp+0h] [ebp-270h]
  char Buffer[200]; // [esp+8h] [ebp-268h] BYREF
  char Destination[412]; // [esp+D0h] [ebp-1A0h] BYREF
  char v8[4]; // [esp+26Ch] [ebp-4h]

  if ( argc < 2 )
  {
    printf("bye: \n", v5);
    exit(1);
  }
  this_50(Destination);

  Destination[408] = system;

  memset(Destination, 0, 200u);
  memset(&Destination[204], 0, 200u);
  memset(Buffer, 0, sizeof(Buffer));

  strcpy(Destination, argv[1]);

  Destination[404] = fopen(Destination, "r");

  if ( !Destination[404] )
  {
    printf("No se puede leer el archivo bye bye \n", v5);
    exit(1);
  }

  printf("%s\n", Destination[200]);
  fread(Buffer, 200u, 1u, Destination[404]);
  *v8 = strlen(Buffer);
  printf("Largo =%d\n", v8[0]);
  fclose(Destination[404]);
  //if ( *v8 >= 200 )
  if ( v8[0] >= 200 )
    exit(1);

  qmemcpy(v4, Destination, sizeof(v4));
  leer_buffer(*v8, Buffer, v4[0]);
  return 0;
}
```

#### Con ghidra
```c

undefined4 __cdecl leer_buffer(undefined4 param_1,void *param_2)

{
  FILE *_File;
  
  _File = fopen(&stack0x0000000c,"rb");
  fread(param_2,2000,1,_File);
  printf("Salida %s\n",(char)param_2);
  return 0;
}


int __cdecl main(int argc,char **argv)

{
  int iVar1;
  undefined4 *puVar2;
  undefined1 unaff_DI;
  undefined4 *puVar3;
  undefined4 auStack_410 [98];
  undefined4 uStack_288;
  char local_26c [200];
  undefined4 local_1a4 [50];
  undefined local_dc;
  undefined local_d8 [200];
  FILE *local_10;
  code *local_c;
  size_t local_8;
  
  if (argc < 2) {
    printf("bye: \n",unaff_DI);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  this_50((char *)local_1a4);

  local_c = system_exref;
  memset(local_1a4,0,200);
  memset(local_d8,0,200);
  memset(local_26c,0,200);

  strcpy((char *)local_1a4,argv[1]);

  local_10 = fopen((char *)local_1a4,"r");
  if (local_10 == (FILE *)0x0) {
    printf("No se puede leer el archivo bye bye \n",unaff_DI);
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  printf(&DAT_00402154,local_dc);
  uStack_288 = 0x4011b8;
  fread(local_26c,200,1,local_10);
  local_8 = strlen(local_26c);
  printf("Largo =%d\n",(char)local_8);
  fclose(local_10);
  if (199 < (int)local_8) {
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  puVar2 = local_1a4;
  puVar3 = auStack_410;
  for (iVar1 = 0x67; iVar1 != 0; iVar1 = iVar1 + -1) {
    *puVar3 = *puVar2;
    puVar2 = puVar2 + 1;
    puVar3 = puVar3 + 1;
  }
  leer_buffer(local_8,local_26c);
  return 0;
}

```
