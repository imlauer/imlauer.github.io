---
title: "Ricardo Narvaja: Exámen 20 (Servidor, libiconv-2.dll, iconv.dll, intl.dll)"
date: 2024-08-27T14:54:39-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
#### Hay 3 exámenes 
## Examen a
```c
_BYTE *__cdecl sub_40ADB0(_BYTE *a1, _BYTE *a2)
{
  _BYTE *v2; // edi
  _BYTE *v3; // ecx
  int v4; // edx
  int v5; // eax
  _BYTE *result; // eax

  v2 = a1;
  v3 = a2;
  if ( ((unsigned __int8)a2 & 3) == 0 )
  {
    while ( 1 )
    {
LABEL_6:
      v5 = (*(_DWORD *)v3 + 2130640639) ^ ~*(_DWORD *)v3;
      v4 = *(_DWORD *)v3;
      v3 += 4;
      if ( (v5 & 0x81010100) != 0 )
      {
        if ( !(_BYTE)v4 )
          goto LABEL_14;
        if ( !BYTE1(v4) )
        {
          *(_WORD *)v2 = (unsigned __int8)v4;
          return a1;
        }
        if ( (v4 & 0xFF0000) == 0 )
        {
          *(_WORD *)v2 = v4;
          result = a1;
          v2[2] = 0;
          return result;
        }
        if ( (v4 & 0xFF000000) == 0 )
        {
          *(_DWORD *)v2 = v4;
          return a1;
        }
      }
      *(_DWORD *)v2 = v4;
      v2 += 4;
    }
  }
  while ( 1 )
  {
    LOBYTE(v4) = *v3++;
    if ( !(_BYTE)v4 )
      break;
    *v2++ = v4;
    if ( ((unsigned __int8)v3 & 3) == 0 )
      goto LABEL_6;
  }
LABEL_14:
  *v2 = v4;
  return a1;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char *v3; // ebx
  void (__thiscall **v4)(char *, int); // edx
  void (__thiscall **v5)(void *, int); // edx
  FILE *v6; // eax
  FILE *v7; // eax
  int v8; // eax
  char *v9; // esi
  FILE *v10; // eax
  char v11; // si
  char v13; // [esp+0h] [ebp-14h]
  char v14; // [esp+0h] [ebp-14h]
  char v15; // [esp+0h] [ebp-14h]
  void *Block; // [esp+Ch] [ebp-8h]
  size_t Size; // [esp+10h] [ebp-4h] BYREF

  Size = 0;
  LoadLibraryA("iconv.dll");
  LoadLibraryA("intl.dll");
  v3 = malloc(416u);
  *v3 = &off_40327C;
  *(v3 + 52) = 0;
  v4 = *v3;
  *(v3 + 53) = 2010;
  *(v3 + 52) = 35;
  (*v4)(v3, 2000);
  strncpy(v3 + 216, "pepe", 0xC8u);
  (*(*v3 + 8))(v3);
  Block = malloc(0x1A0u);
  *Block = &off_40327C;
  *(Block + 52) = 0;
  v5 = *Block;
  *(Block + 53) = 2011;
  *(Block + 52) = 39;
  (*v5)(Block, 3000);
  strncpy(Block + 216, "jose", 0xC8u);
  (*(*Block + 8))(Block);
  printf("Ingrese Curriculum Empleados\n", v13);
  v6 = _acrt_iob_func(0);
  fgets(v3 + 8, 200, v6);
  v7 = _acrt_iob_func(0);
  fgets(Block + 8, 200, v7);
  if ( strlen(v3 + 8) >= 0x14 )
  {
    if ( strlen(Block + 8) >= 0x14 )
      goto LABEL_9;
    printf("Despedir empleado curriculum insuficiente\n", v14);
    *Block = &off_40327C;
    sub_401318(Block);
  }
  else
  {
    printf("Despedir empleado curriculum insuficiente\n", v14);
    *v3 = &off_40327C;
    sub_401318(v3);
  }
  printf("Ingrese largo de curriculum de nuevo empleado\n", v15);
  scanf("%d", &Size);
  do
    v8 = getchar();
  while ( v8 != 10 && v8 != -1 );
  v9 = malloc(Size);
  v10 = _acrt_iob_func(0);
  fgets(v9, Size, v10);
LABEL_9:
  printf("Calcular ahorro en sueldos\n", v14);
  v11 = (*(*v3 + 4))(v3);
  (*(*Block + 4))(Block);
  printf("gasto actual% d", v11);
  return 0;
}
```
