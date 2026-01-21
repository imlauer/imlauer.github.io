---
title: "Ricardo Narvaja: Exámen 21 (Ejecutar la calculadora, con base de datos:ConsoleApplication4.pdb)"
date: 2024-08-27T14:54:39-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
int __thiscall sub_401050(_DWORD *this, int a2, int a3, int *a4, int *a5)
{
  int v6[256]; // [esp+0h] [ebp-404h] BYREF
  _DWORD *v7; // [esp+400h] [ebp-4h]

  v7 = this;
  sub_401010(this, a2, a3, a4, a5);
  *v7 = &off_41A348;
  a2 = 0;
  a3 = 0;
  a4 = &a2;
  a5 = &a3;
  *(v7 + 1024) = 0;
  *(v7 + 1025) = 0;
  *(v7 + 1026) = 0;
  sub_401010(v6, a2, a3, a4, a5);
  return v7;
}
_DWORD *__thiscall sub_401010(_DWORD *this, int a2, int a3, int a4, int a5)
{
  *this = &off_41A33C;
  this[2] = a2;
  this[3] = a3;
  this[5] = a5;
  this[4] = a4;
  return this;
}
LPVOID __cdecl sub_40C2D8(SIZE_T dwBytes)
{
  SIZE_T v1; // esi
  LPVOID result; // eax

  v1 = dwBytes;
  if ( dwBytes > 0xFFFFFFE0 )
  {
LABEL_8:
    *(_DWORD *)sub_40CBC6() = 12;
    return 0;
  }
  else
  {
    if ( !dwBytes )
      v1 = 1;
    while ( 1 )
    {
      result = HeapAlloc(hHeap, 0, v1);
      if ( result )
        break;
      if ( !sub_40BC66() || !sub_40AEC7(v1) )
        goto LABEL_8;
    }
  }
  return result;
}
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
int __cdecl sub_404E0C(int a1, int a2, int a3)
{
  return sub_404CCB(a1, a2, a3);
}
_DWORD *__thiscall sub_401010(_DWORD *this, int a2, int a3, int a4, int a5)
{
  *this = &off_41A33C;
  this[2] = a2;
  this[3] = a3;
  this[5] = a5;
  this[4] = a4;
  return this;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  int v4; // eax
  char v6[500]; // [esp+0h] [ebp-238h] BYREF
  int v7; // [esp+1F4h] [ebp-44h]
  int v8; // [esp+1F8h] [ebp-40h]
  int v9; // [esp+1FCh] [ebp-3Ch]
  int v10; // [esp+200h] [ebp-38h]
  int v11; // [esp+204h] [ebp-34h]
  int v12; // [esp+208h] [ebp-30h]
  int v13; // [esp+20Ch] [ebp-2Ch]
  int v14; // [esp+210h] [ebp-28h]
  int v15; // [esp+214h] [ebp-24h] BYREF
  int v16; // [esp+218h] [ebp-20h] BYREF
  int v17; // [esp+21Ch] [ebp-1Ch] BYREF
  int v18; // [esp+220h] [ebp-18h]
  int v19; // [esp+224h] [ebp-14h]
  int v20; // [esp+228h] [ebp-10h]
  int v21; // [esp+234h] [ebp-4h]

  v17 = 0;
  v15 = 1;
  v16 = 0;
  off_421000 = printf;
  MessageBoxA(0, "A ejecutar la calculadora..\n", "Vamosss", 0);
  v14 = heapalloc(1228);
  v21 = 0;
  if ( v14 )
    v13 = sub_401050(0, 0, &v17, &v15);
  else
    v13 = 0;
  v9 = v13;
  v21 = -1;
  v18 = v13;
  sub_40ADB0(v13 + 24, "San_Mastil");
  sub_40ADB0(v18 + 1027, "San_Mastil_Capital");
  *(v18 + 224) = "Liga_trastornada";
  printf("Equipo de la B es %s\n", (v18 + 24));
  v12 = heapalloc(1024);
  v21 = 1;
  if ( v12 )
    v11 = sub_401010(1, 1, &v15, &v17);
  else
    v11 = 0;
  v8 = v11;
  v21 = -1;
  v19 = v11;
  sub_40ADB0(v11 + 24, "Mal_Boys");
  *(v19 + 224) = &v17;
  printf("Equipo de la A es %s\n", (v19 + 24));
  (**v19)(v19, 2000);
  (**v18)(v18, 1000);
  *(v18 + 1026) = 1;
  printf("Equipo de la A Descendio borrarlo de equipos de la A \n");
  v7 = v19;
  sub_401562(v19);
  printf("Ingrese largo de nombre de nuevo equipo ascendido a la A\n");
  sub_4014F0("%d", &v16);
  do
    v20 = sub_404F69();
  while ( v20 != 10 && v20 != -1 );
  v10 = sub_40AEA8(v16);
  printf("Escriba nombre de nuevo equipo ascendido\n");
  v3 = sub_404C47(0);
  sub_404E0C(v10, v16, v3);
  do
    v20 = sub_404F69();
  while ( v20 != 10 && v20 != -1 );
  printf("Escriba nombre de la liga de equipo ascendido\n");
  v4 = sub_404C47(0);
  sub_404E0C(v6, 500, v4);
  do
    v20 = sub_404F69();
  while ( v20 != 10 && v20 != -1 );
  **(v19 + 20) = v15;
  sub_4021E0(*(v19 + 224), v6, 200);
  printf("Nombre de nuevo equipo ascendido\n");
  off_421000(v10);
  printf("Nombre de la liga de equipo ascendido\n");
  off_421000(v6);
  return 0;
}int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  int v4; // eax
  char v6[500]; // [esp+0h] [ebp-238h] BYREF
  int v7; // [esp+1F4h] [ebp-44h]
  int v8; // [esp+1F8h] [ebp-40h]
  int v9; // [esp+1FCh] [ebp-3Ch]
  int v10; // [esp+200h] [ebp-38h]
  int v11; // [esp+204h] [ebp-34h]
  int v12; // [esp+208h] [ebp-30h]
  int v13; // [esp+20Ch] [ebp-2Ch]
  int v14; // [esp+210h] [ebp-28h]
  int v15; // [esp+214h] [ebp-24h] BYREF
  int v16; // [esp+218h] [ebp-20h] BYREF
  int v17; // [esp+21Ch] [ebp-1Ch] BYREF
  int v18; // [esp+220h] [ebp-18h]
  int v19; // [esp+224h] [ebp-14h]
  int v20; // [esp+228h] [ebp-10h]
  int v21; // [esp+234h] [ebp-4h]

  v17 = 0;
  v15 = 1;
  v16 = 0;
  off_421000 = printf;
  MessageBoxA(0, "A ejecutar la calculadora..\n", "Vamosss", 0);
  v14 = heapalloc(1228);
  v21 = 0;
  if ( v14 )
    v13 = sub_401050(0, 0, &v17, &v15);
  else
    v13 = 0;
  v9 = v13;
  v21 = -1;
  v18 = v13;
  sub_40ADB0(v13 + 24, "San_Mastil");
  sub_40ADB0(v18 + 1027, "San_Mastil_Capital");
  *(v18 + 224) = "Liga_trastornada";
  printf("Equipo de la B es %s\n", (v18 + 24));
  v12 = heapalloc(1024);
  v21 = 1;
  if ( v12 )
    v11 = sub_401010(1, 1, &v15, &v17);
  else
    v11 = 0;
  v8 = v11;
  v21 = -1;
  v19 = v11;
  sub_40ADB0(v11 + 24, "Mal_Boys");
  *(v19 + 224) = &v17;
  printf("Equipo de la A es %s\n", (v19 + 24));
  (**v19)(v19, 2000);
  (**v18)(v18, 1000);
  *(v18 + 1026) = 1;
  printf("Equipo de la A Descendio borrarlo de equipos de la A \n");
  v7 = v19;
  sub_401562(v19);
  printf("Ingrese largo de nombre de nuevo equipo ascendido a la A\n");
  sub_4014F0("%d", &v16);
  do
    v20 = sub_404F69();
  while ( v20 != 10 && v20 != -1 );
  v10 = sub_40AEA8(v16);
  printf("Escriba nombre de nuevo equipo ascendido\n");
  v3 = sub_404C47(0);
  sub_404E0C(v10, v16, v3);
  do
    v20 = sub_404F69();
  while ( v20 != 10 && v20 != -1 );
  printf("Escriba nombre de la liga de equipo ascendido\n");
  v4 = sub_404C47(0);
  sub_404E0C(v6, 500, v4);
  do
    v20 = sub_404F69();
  while ( v20 != 10 && v20 != -1 );
  **(v19 + 20) = v15;
  sub_4021E0(*(v19 + 224), v6, 200);
  printf("Nombre de nuevo equipo ascendido\n");
  off_421000(v10);
  printf("Nombre de la liga de equipo ascendido\n");
  off_421000(v6);
  return 0;
}
```
