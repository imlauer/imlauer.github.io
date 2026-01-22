---
title: "Ricardo Narvaja: Exámen 14 (Servidor, helixprodctrl.dll)"
date: 2024-08-27T14:54:34-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v3; // al
  char v5; // al
  char v6; // al
  char v7; // al
  size_t v8; // eax
  char v9[400]; // [esp+0h] [ebp-28Ch] BYREF
  char v10[200]; // [esp+190h] [ebp-FCh] BYREF
  char v11[16]; // [esp+258h] [ebp-34h] BYREF
  __int16 v12[2]; // [esp+268h] [ebp-24h] BYREF
  int v13; // [esp+26Ch] [ebp-20h]
  int v14; // [esp+278h] [ebp-14h]
  int v15[2]; // [esp+27Ch] [ebp-10h] BYREF
  int v16; // [esp+284h] [ebp-8h]
  int v17; // [esp+288h] [ebp-4h]

  LoadLibraryA("helixprodctrl.dll");
  printf("\nInitialising Winsock...", v9[0]);
  if ( WS2_32_115(514, v9) )
  {
    v3 = WS2_32_111();
    printf("Failed. Error Code : %d", v3);
    return 1;
  }
  else
  {
    printf("Initialised.\n", v9[0]);
    v17 = WS2_32_23(2, 1, 0);
    if ( v17 == -1 )
    {
      v5 = WS2_32_111();
      printf("Could not create socket : %d", v5);
    }
    printf("Socket created.\n", v9[0]);
    v12[0] = 2;
    v13 = 0;
    v12[1] = WS2_32_9(8888);
    if ( WS2_32_2(v17, v12, 16) == -1 )
    {
      v6 = WS2_32_111();
      printf("Bind failed with error code : %d", v6);
    }
    puts("Bind done");
    WS2_32_13(v17, 3);
    puts("Waiting for incoming connections...port 8888");
    v15[0] = 16;
    v16 = WS2_32_1(v17, v11, v15);
    if ( v16 == -1 )
    {
      v7 = WS2_32_111();
      printf("accept failed with error code : %d", v7);
    }
    puts("Connection accepted");
    v15[1] = (int)"Hello Client , I have received your connection.\n";
    v8 = strlen("Hello Client , I have received your connection.\n");
    WS2_32_19(v16, "Hello Client , I have received your connection.\n", v8, 0);
    v14 = dword_403028;
    WS2_32_16(v16, v10, 500, 0);
    WS2_32_3(v17);
    WS2_32_116();
    return 0;
  }
}
```
