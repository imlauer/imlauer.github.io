---
title: "Ricardo Narvaja: Exámen 19 (Servidor, WCMZIP32.DLL)"
date: 2024-08-27T14:54:39-03:00
tags: ['reversing','cracking','ricardo','narvaja','examen','calculadora']
---

```c
_DWORD *__thiscall sub_401020(_DWORD *this)
{
  sub_4010C0(this);
  *this = off_403348;
  this[2] = 0;
  this[113] = 0;
  this[114] = 0;
  *((_BYTE *)this + 4756) = 0;
  memset(this + 115, 0, 0xC8u);
  memset(this + 165, 0, 0x1000u);
  memset((char *)this + 4757, 0, 0xC8u);
  return this;
}
_DWORD *__thiscall sub_401650(_DWORD *this, int a2)
{
  _DWORD *result; // eax

  result = this;
  this[2] = a2;
  return result;
}
int __thiscall sub_4010E0(char *this)
{
  char v1; // al
  char v2; // al
  size_t v3; // eax

  sub_4014D0(this);
  *((_DWORD *)this + 104) = WS2_32_1(*((_DWORD *)this + 103), this + 436, this + 452);
  if ( *((_DWORD *)this + 104) == -1 )
  {
    v1 = WS2_32_111();
    sub_4017F0("accept failed with error code : %d", v1);
  }
  puts("Connection accepted\n");
  memset(this + 4757, 0, 0xC8u);
  sub_4017F0("number= %d\n", *((_DWORD *)this + 2));
  v2 = sub_401490(8888);
  sub_401830(this + 4757, "Nuevo Port is = %d\n", v2);
  WS2_32_19(*((_DWORD *)this + 104), this + 4757, 200, 0);
  v3 = strlen(this + 4757);
  WS2_32_16(*((_DWORD *)this + 104), Src, v3, 0);
  if ( *(_DWORD *)Src == 1094861636 )
  {
    WS2_32_3(*((_DWORD *)this + 103));
    return 1;
  }
  else
  {
    puts("Bye Bye love\n");
    return 0;
  }
}

int __thiscall sub_401240(int this)
{
  char v1; // al
  char v3; // [esp+0h] [ebp-Ch]
  int v4; // [esp+0h] [ebp-Ch]
  signed int i; // [esp+4h] [ebp-8h]

  sub_4014D0(this);
  *(_DWORD *)(this + 416) = WS2_32_1(*(_DWORD *)(this + 412), this + 436, this + 452);
  if ( *(_DWORD *)(this + 416) == -1 )
  {
    v1 = WS2_32_111();
    sub_4017F0("accept failed with error code : %d", v1);
  }
  puts("Connection accepted\n");
  memset((void *)(this + 4757), 0, 0xC8u);
  sub_4017F0("number= %d\n", *(_DWORD *)(this + 8));
  sub_401830((char *)(this + 4757), (char *)(this + 460), dword_404080[0]);
  sub_4017F0((char *)(this + 4757), v3);
  WS2_32_19(*(_DWORD *)(this + 416), this + 4757, 200, 0);
  *(_DWORD *)(this + 456) = dword_404084;
  WS2_32_16(*(_DWORD *)(this + 416), Src, 12288, 0);
  v4 = *((_DWORD *)Src + 1) + *(_DWORD *)Src;
  sub_4017F0("%x\n\n", v4);
  if ( v4 == -1 )
  {
    Size = *((_DWORD *)Src + 2);
    dword_404078 = *((_DWORD *)Src + 3);
  }
  memcpy((void *)(this + 660), Src, Size);
  for ( i = 0; i < (int)Size; ++i )
  {
    *(_BYTE *)(this + 4756) = *(_BYTE *)(i + this + 660);
    if ( *(_BYTE *)(this + 4756) == 4 )
      exit(1);
    if ( *(_BYTE *)(this + 4756) == 65 )
      exit(1);
  }
  if ( dword_404078 != (*(_DWORD *)dword_404080 ^ 0x89765432) )
  {
    puts("Bye Bye\n");
    exit(1);
  }
  return 1;
}

int __cdecl __noreturn main(int argc, const char **argv, const char **envp)
{
  int v3; // eax
  char v4[4960]; // [esp+0h] [ebp-26C0h] BYREF
  char v5[4960]; // [esp+1360h] [ebp-1360h] BYREF

  LoadLibraryA("WCMZIP32.DLL");
  sub_401020(v5);
  sub_401650(8888);
  if ( sub_4010E0(v5) == 1 )
  {
    sub_401020(v4);
    v3 = sub_401490(8888);
    sub_401650(v3);
    sub_401240(v4);
  }
  exit(1);
}
```

