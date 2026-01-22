---
title: "Ricardo Narvaja: Exámen 15 (Servidor, MObexDll.dll)"
date: 2024-08-27T14:54:36-03:00
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
  char v9[4096]; // [esp+0h] [ebp-11D8h] BYREF
  char v10[400]; // [esp+1000h] [ebp-1D8h] BYREF
  char v11[16]; // [esp+1190h] [ebp-48h] BYREF
  __int16 v12[2]; // [esp+11A0h] [ebp-38h] BYREF
  int v13; // [esp+11A4h] [ebp-34h]
  int v14; // [esp+11B0h] [ebp-28h]
  int v15; // [esp+11B4h] [ebp-24h] BYREF
  size_t Size; // [esp+11B8h] [ebp-20h]
  char v17[4]; // [esp+11BCh] [ebp-1Ch]
  char *Str; // [esp+11C0h] [ebp-18h]
  int v19; // [esp+11C4h] [ebp-14h]
  int i; // [esp+11C8h] [ebp-10h]
  int v21; // [esp+11CCh] [ebp-Ch]
  void *Src; // [esp+11D4h] [ebp-4h]

  Size = 4096;
  Src = malloc(0x2000u);
  LoadLibraryA("MObexDll.dll");
  printf("\nInitialising Winsock...", v9[0]);
  if ( WS2_32_115(514, v10) )
  {
    v3 = WS2_32_111();
    printf("Failed. Error Code : %d", v3);
    return 1;
  }
  else
  {
    printf("Initialised.\n", v9[0]);
    v21 = WS2_32_23(2, 1, 0);
    if ( v21 == -1 )
    {
      v5 = WS2_32_111();
      printf("Could not create socket : %d", v5);
    }
    printf("Socket created.\n", v9[0]);
    v12[0] = 2;
    v13 = 0;
    v12[1] = WS2_32_9(8888);
    if ( WS2_32_2(v21, v12, 16) == -1 )
    {
      v6 = WS2_32_111();
      printf("Bind failed with error code : %d", v6);
    }
    puts("Bind done");
    WS2_32_13(v21, 3);
    puts("Waiting for incoming connections...port 8888");
    v15 = 16;
    do
    {
      v19 = WS2_32_1(v21, v11, &v15);
      if ( v19 == -1 )
      {
        v7 = WS2_32_111();
        printf("accept failed with error code : %d", v7);
      }
      puts("Connection accepted\n");
      Str = "Hello Client , I have received your connection.\n";
      v8 = strlen("Hello Client , I have received your connection.\n");
      WS2_32_19(v19, "Hello Client , I have received your connection.\n", v8, 0);
      v14 = dword_403024;
      WS2_32_16(v19, Src, 0x2000, 0);
      *v17 = *(Src + 1) + *Src;
      printf("%x\n\n", v17[0]);
      if ( *v17 == -1 )
      {
        Size = *(Src + 2);
        dword_403020 = *(Src + 3);
        Src = Src + 72;
      }
      memcpy(v9, Src, Size);
      for ( i = 0; i < 3840; ++i )
      {
        if ( !v9[i] )
          exit(1);
      }
    }
    while ( dword_403020 != 0x89765432 );
    return 0;
  }
}
```

