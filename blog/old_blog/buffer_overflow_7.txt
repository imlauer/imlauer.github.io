---
title: "Buffer overflow 7 (Ricardo navarja reversing)"
date: 2024-08-20T23:49:30-03:00
tags: ['ricardo','narvaja','cracking','reversing','examen','buffer','overflow','ida']
---
Este es el código que me generó el IDA con mis modificaciones:
```c

int __cdecl check(char *Stream)
{
  char savedregs; // [esp+0h] [ebp+0h]

  sprintf(Stream + 220, "Bieeeeeeeeeeeeeeeeeeeen ? con %s", Stream + 4);
  if ( *(Stream + 52) != 'E' )
  {
    printf("Mal camino \n", savedregs);
    exit(1);
  }
  if ( Stream[216] != 0xD )
    *(Stream + 54) = 2;
  printf("valor= %x\n", Stream[216]);
  printf("number= %x\n", Stream[204]);
  if ( *(Stream + 53) == 'F' )
    printf("Aprobaste level 7", savedregs);
  else
    printf("Que pasa, %x \n", Stream[216] + Stream[204]);
  return 0;
}


int main(int argc, const char **argv)
{
  FILE *Stream; // [esp+0h] [ebp-1A4h] BYREF
  char Buffer[200]; // [esp+4h] [ebp-1A0h] BYREF
  int v6; // [esp+CCh] [ebp-D8h]
  int v7; // [esp+D0h] [ebp-D4h]
  int v8; // [esp+D4h] [ebp-D0h]
  char Destination[200]; // [esp+DCh] [ebp-C8h] BYREF

  v6 = 1;
  v8 = 1;
  v7 = 69;
  memset(Buffer, 0, sizeof(Buffer));
  memset(Destination, 0, sizeof(Destination));
  Stream = fopen("example.txt", "rb");
  if ( !Stream )
  {
    printf("No se puede leer el archivo bye bye \n", 0);
    exit(1);
  }
  fread(Buffer, 200*sizeof(char), 1*sizeof(char), Stream);

  // Acá se produce el bufferoverflow
  // Copiamos el contenido del Buffer a Destination.
  // strcpy copia hasta encontrar un caracter nulo ('\0')
  strcpy(Destination, Buffer);
  if ( v6 != 1 )
  {
    printf("Mal \n", (char)Stream);
    exit(1);
  }
  check((int)&Stream);
  return 0;
}
```

Hasta 173 no se produce el buffer overflow. Los caracteres que agregamos luego de 173 caracteres pisan el `return address`.

Para hacer una prueba al pisar el return address le puse la dirección del printf que decía `"No se puede leer el archivo bye bye \n"` que estaba en la dirección `0x401215` con el siguiente exploit:
```
00000000: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000010: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000020: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000030: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000040: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000050: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000060: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000070: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000080: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000090: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
000000a0: 4141 4141 4141 4141 4141 4141 4141 1512  AAAAAAAAAAAAAA..
000000b0: 4000                                     @.
```

Pisamos el return address con la dirección en donde dice "Aprobaste level 7" que se puede ubicar en el gráfico de IDA apretando el icono del lapiz en el dialogo en mi caso era la dirección: `0x4010AA` pasado a little indian: `aa1040`.

#### exploit
```
00000000: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000010: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000020: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000030: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000040: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000050: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000060: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000070: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000080: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
00000090: 4141 4141 4141 4141 4141 4141 4141 4141  AAAAAAAAAAAAAAAA
000000a0: 4141 4141 4141 4141 4141 4141 4141 aa10  AAAAAAAAAAAAAA..
000000b0: 40                                       @
```

