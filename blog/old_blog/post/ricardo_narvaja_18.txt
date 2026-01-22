---
title: "Ricardo Narvaja: Exámen 18 (Servidor, libw32pth-0.dll)"
date: 2024-08-27T14:54:39-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
int sub_4014E0(char *Buffer, char *Format, ...)
{
  va_list va; // [esp+18h] [ebp+10h] BYREF

  va_start(va, Format);
  sub_401010();
  return sub_401450(Buffer, Format, 0, va);
}
int __cdecl sub_401020(int a1)
{
  char v1; // al
  char v3; // al
  char v4; // al
  char v5; // al
  size_t v6; // eax
  char v7; // [esp+0h] [ebp-12DCh]
  char v8; // [esp+0h] [ebp-12DCh]
  char v9; // [esp+0h] [ebp-12DCh]
  char v10; // [esp+0h] [ebp-12DCh]
  char v11[4096]; // [esp+8h] [ebp-12D4h] BYREF
  char v12[400]; // [esp+1008h] [ebp-2D4h] BYREF
  char Format[64]; // [esp+1198h] [ebp-144h] BYREF
  char Str[200]; // [esp+11D8h] [ebp-104h] BYREF
  char v15[16]; // [esp+12A0h] [ebp-3Ch] BYREF
  __int16 v16[2]; // [esp+12B0h] [ebp-2Ch] BYREF
  int v17; // [esp+12B4h] [ebp-28h]
  int v18; // [esp+12C0h] [ebp-1Ch]
  int v19; // [esp+12C4h] [ebp-18h] BYREF
  char v20[4]; // [esp+12C8h] [ebp-14h]
  int i; // [esp+12CCh] [ebp-10h]
  int v22; // [esp+12D0h] [ebp-Ch]
  int v23; // [esp+12D4h] [ebp-8h]
  char v24; // [esp+12DBh] [ebp-1h]

  strcpy(Format, "Hello Client , I have received your connection your key is %d.\n");
  *dword_404038 = GetTickCount();
  Src = malloc(0x2000u);
  LoadLibraryA("libw32pth-0.dll");
  printf("\nInitialising Winsock...", v7);
  if ( WS2_32_115(514, v12) )
  {
    v1 = WS2_32_111();
    printf("Failed. Error Code : %d", v1);
    return 1;
  }
  else
  {
    printf("Initialised.\n", v8);
    v23 = WS2_32_23(2, 1, 0);
    if ( v23 == -1 )
    {
      v3 = WS2_32_111();
      printf("Could not create socket : %d", v3);
    }
    printf("Socket created.\n", v9);
    v16[0] = 2;
    v17 = 0;
    v16[1] = WS2_32_9(a1);
    if ( WS2_32_2(v23, v16, 16) == -1 )
    {
      v4 = WS2_32_111();
      printf("Bind failed with error code : %d", v4);
    }
    puts("Bind done");
    WS2_32_13(v23, 3);
    puts("Waiting for incoming connections...\n");
    v19 = 16;
    v22 = WS2_32_1(v23, v15, &v19);
    if ( v22 == -1 )
    {
      v5 = WS2_32_111();
      printf("accept failed with error code : %d", v5);
    }
    puts("Connection accepted\n");
    memset(Str, 0, sizeof(Str));
    if ( a1 == 8888 )
    {
      sub_4014E0(Str, "Port is = %d", 252);
      WS2_32_19(v22, Str, 200, 0);
      v6 = strlen(Str);
      WS2_32_16(v22, Src, v6, 0);
      if ( *Src != 1094861636 )
      {
        puts("Bye Bye\n");
        exit(1);
      }
      WS2_32_3(v23);
      return 0;
    }
    else
    {
      sub_4014E0(Str, Format, dword_404038[0]);
      printf(Str, v10);
      WS2_32_19(v22, Str, 200, 0);
      v18 = dword_40403C;
      WS2_32_16(v22, Src, 0x2000, 0);
      *v20 = *(Src + 1) + *Src;
      printf("%x\n\n", v20[0]);
      if ( *v20 == -1 )
      {
        Size = *(Src + 2);
        dword_404030 = *(Src + 3);
      }
      memcpy(v11, Src, Size);
      for ( i = 0; i < Size; ++i )
      {
        v24 = v11[i];
        if ( v24 == 1 )
          exit(1);
      }
      if ( dword_404030 != (*dword_404038 ^ 0x89765432) )
      {
        puts("Bye Bye\n");
        exit(1);
      }
      return 0;
    }
  }
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  sub_401020(8888);
  sub_401020(7676);
  return 0;
}
```
