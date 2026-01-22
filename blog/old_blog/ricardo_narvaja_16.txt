---
title: "Ricardo Narvaja: Exámen 16 (Servidor, MObexDll.dll)"
date: 2024-08-27T14:54:38-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v3; // al
  char v5; // al
  char v6; // al
  char v7; // al
  char v8; // [esp+0h] [ebp-12D0h]
  char v9; // [esp+0h] [ebp-12D0h]
  char v10; // [esp+0h] [ebp-12D0h]
  char v11[4096]; // [esp+8h] [ebp-12C8h] BYREF
  char v12[400]; // [esp+1008h] [ebp-2C8h] BYREF
  char Destination[200]; // [esp+1198h] [ebp-138h] BYREF
  char Source[52]; // [esp+1260h] [ebp-70h] BYREF
  char v15[16]; // [esp+1294h] [ebp-3Ch] BYREF
  __int16 v16[2]; // [esp+12A4h] [ebp-2Ch] BYREF
  int v17; // [esp+12A8h] [ebp-28h]
  int v18; // [esp+12B4h] [ebp-1Ch]
  int v19; // [esp+12B8h] [ebp-18h] BYREF
  char v20[4]; // [esp+12BCh] [ebp-14h]
  int v21; // [esp+12C0h] [ebp-10h]
  int i; // [esp+12C4h] [ebp-Ch]
  int v23; // [esp+12C8h] [ebp-8h]

  strcpy(Source, "Hello Client , I have received your connection.\n");
  Src = malloc(8192u);
  LoadLibraryA("MObexDll.dll");
  printf("\nInitialising Winsock...", v8);
  if ( WS2_32_115(514, v12) )
  {
    v3 = WS2_32_111();
    printf("Failed. Error Code : %d", v3);
    return 1;
  }
  else
  {
    printf("Initialised.\n", v9);
    v23 = WS2_32_23(2, 1, 0);
    if ( v23 == -1 )
    {
      v5 = WS2_32_111();
      printf("Could not create socket : %d", v5);
    }
    printf("Socket created.\n", v10);
    v16[0] = 2;
    v17 = 0;
    v16[1] = WS2_32_9(8888);
    if ( WS2_32_2(v23, v16, 16) == -1 )
    {
      v6 = WS2_32_111();
      printf("Bind failed with error code : %d", v6);
    }
    puts("Bind done");
    WS2_32_13(v23, 3);
    puts("Waiting for incoming connections...port 8888");
    v19 = 16;
    do
    {
      v21 = WS2_32_1(v23, v15, &v19);
      if ( v21 == -1 )
      {
        v7 = WS2_32_111();
        printf("accept failed with error code : %d", v7);
      }
      puts("Connection accepted\n");
      strcpy(Destination, Source);
      WS2_32_19(v21, Destination, 200, 0);
      v18 = dword_403038;
      WS2_32_16(v21, Src, 8192, 0);
      *v20 = *(Src + 1) + *Src;
      printf("%x\n\n", v20[0]);
      if ( *v20 == -1 )
      {
        Size = *(Src + 2);
        dword_403030 = *(Src + 3);
      }
      memcpy(v11, Src, Size);
      for ( i = 0; i < Size; ++i )
      {
        if ( !v11[i] )
          exit(1);
      }
    }
    while ( dword_403030 != -1988733902 );
    return 0;
  }
}
```
