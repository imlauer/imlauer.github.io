---
title: "STRING FACIL reversing"
date: 2024-09-27T03:07:18-03:00
tags: ['reversing']
---
Ejercicio `STRING_FACIL.exe` de https://drive.google.com/file/d/1QRIk3zBGGXH54nSZorX3jnuNmURCHw6K/view?pli=1

### Código que me generó el IDA:
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  size_t longitud_segunda_cadena; // [esp+0h] [ebp-44h]
  int v5; // [esp+4h] [ebp-40h]
  int v6; // [esp+8h] [ebp-3Ch]
  signed int j; // [esp+Ch] [ebp-38h]
  signed int i; // [esp+10h] [ebp-34h]
  signed int longitud_primer_cadena; // [esp+14h] [ebp-30h]
  char Str2[20]; // [esp+18h] [ebp-2Ch] BYREF
  char Str[20]; // [esp+2Ch] [ebp-18h] BYREF

  v5 = 0;
  sub_401090(std::cout, "Enter the First String: ");
  sub_401070(std::cin, Str);
  sub_401090(std::cout, "Enter the Second String: ");
  sub_401070(std::cin, Str2);
  longitud_primer_cadena = strlen(Str);
  longitud_segunda_cadena = strlen(Str2);

  // Las cadenas NO tienen que ser iguales, pero a su vez la longitud de la primer cadena tiene que ser igual a la longitud de la segunda. 

  if ( !strcmp(Str, Str2) )
  {
    sub_401090(std::cout, "NOP");
    exit(1);
  }
  // O sea que la longitud de la primer cadena tiene que ser mayor o igual 8.
  if ( longitud_primer_cadena < 8 )
    exit(1);
  if ( longitud_primer_cadena == longitud_segunda_cadena )
  {
    for ( i = 0; i < longitud_primer_cadena; ++i )
    {
      v6 = 0;
      for ( j = 0; j < longitud_primer_cadena; ++j )
      {
        if ( Str[i] == Str2[j] )
        {
          v6 = 1;
          break;
        }
      }
      // Cuando escribís esto significa que if ( v6 ) v6 tiene que cualquier número distinto de 0. Cuando escribís if ( !v6 ) esto es verdadero cuando v6 vale 0.
      if ( v6 == 0 )
      {
        v5 = 1;
        break;
      }
    }
    // Queremos que v5 sea distinto de 1.
    if ( v5 == 1 )
      sub_401090(std::cout, "\nFAIL");
    else
      sub_401090(std::cout, "\nCORRECT");
  }
  else
  {
    sub_401090(std::cout, "\nFAIL!");
  }
  std::ostream::operator<<(std::cout, sub_401640);
  return 0;
}
```

### Exploit: 

```bash
Enter the first string: 11111111
Enter the second string: 00000001
```
