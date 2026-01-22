---
title: "Ricardo Narvaja: Exámen 17 (Servidor, zlib.dll)"
date: 2024-08-27T14:54:39-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v3; // al
  char v5; // al
  char v6; // al
  char v7; // al
  char v8; // [esp+0h] [ebp-12E0h]
  char v9; // [esp+0h] [ebp-12E0h]
  char v10; // [esp+0h] [ebp-12E0h]
  char v11; // [esp+0h] [ebp-12E0h]
  char v12[4096]; // [esp+8h] [ebp-12D8h] BYREF
  char v13[400]; // [esp+1008h] [ebp-2D8h] BYREF
  char Format[200]; // [esp+1198h] [ebp-148h] BYREF
  char v15[64]; // [esp+1260h] [ebp-80h] BYREF
  char v16[16]; // [esp+12A0h] [ebp-40h] BYREF
  __int16 v17[2]; // [esp+12B0h] [ebp-30h] BYREF
  int v18; // [esp+12B4h] [ebp-2Ch]
  int v19; // [esp+12C0h] [ebp-20h]
  int v20; // [esp+12C4h] [ebp-1Ch] BYREF
  char v21[4]; // [esp+12C8h] [ebp-18h]
  char v22[4]; // [esp+12CCh] [ebp-14h]
  int v23; // [esp+12D0h] [ebp-10h]
  int i; // [esp+12D4h] [ebp-Ch]
  int v25; // [esp+12D8h] [ebp-8h]
  char v26; // [esp+12DFh] [ebp-1h]

  strcpy(v15, "Hello Client , I have received your connection your key is %d.\n");
  *v21 = GetTickCount();
  Src = malloc(0x2000u);
  LoadLibraryA("zlib.dll");
  printf("\nInitialising Winsock...", v8);
  if ( WS2_32_115(514, v13) )
  {
    v3 = WS2_32_111();
    printf("Failed. Error Code : %d", v3);
    return 1;
  }
  else
  {
    printf("Initialised.\n", v9);
    v25 = WS2_32_23(2, 1, 0);
    if ( v25 == -1 )
    {
      v5 = WS2_32_111();
      printf("Could not create socket : %d", v5);
    }
    printf("Socket created.\n", v10);
    v17[0] = 2;
    v18 = 0;
    v17[1] = WS2_32_9(8888);
    if ( WS2_32_2(v25, v17, 16) == -1 )
    {
      v6 = WS2_32_111();
      printf("Bind failed with error code : %d", v6);
    }
    puts("Bind done");
    WS2_32_13(v25, 3);
    puts("Waiting for incoming connections...port 8888");
    v20 = 16;
    do
    {
      v23 = WS2_32_1(v25, v16, &v20);
      if ( v23 == -1 )
      {
        v7 = WS2_32_111();
        printf("accept failed with error code : %d", v7);
      }
      puts("Connection accepted\n");
      memset(Format, 0, sizeof(Format));
      sub_401400(Format, v15, v21[0]);
      printf(Format, v11);
      WS2_32_19(v23, Format, 200, 0);
      v19 = dword_404038;
      WS2_32_16(v23, Src, 0x2000, 0);
      *v22 = *(Src + 1) + *Src;
      printf("%x\n\n", v22[0]);
      if ( *v22 == -1 )
      {
        Size = *(Src + 2);
        dword_404030 = *(Src + 3);
      }
      memcpy(v12, Src, Size);
      for ( i = 0; i < Size; ++i )
      {
        v26 = v12[i];
        if ( v26 == 1 )
          exit(1);
      }
    }
    while ( dword_404030 != (*v21 ^ 0x89765432) );
    return 0;
  }
}
```
