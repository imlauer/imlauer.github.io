---
title: "Buffer overflow exámen 5 (Ricardo Narvaja Reversing)"
date: 2024-08-07T18:31:16-03:00
tags: ['ricardo','narvaja','cracking','examen','buffer','overflow','ida','reversing']
---
Lo que el decompilador de IDA me generó con algunas modificaciones.
```c
int check(char *buffer)
{
  // Copia el buffer a partir de la posición 216 al comienzo del buffer a partir de la posición 4.
  // 11 caracteres insertando al buffer
  // 4+4+11 = 19
  char savedregs; 
  
  // 199 -4 + 11
  sprintf(&buffer[4], "Bien ? con %s", buffer + 216);

  // 52-19 = 33
  // La posición 33 del archivo example.txt tiene que ser igual a el hexadecimal 45 ('E').
  if ( buffer[52] != 0x45 )
  {
    printf("Mal camino \n");
    exit(1);
  }
  if ( buffer[0] != 0xD )
    buffer[0] = 2;

  printf("valor= %x\n", buffer[0]);
  printf("number= %x\n", buffer[204]);

  // 51-19 = 32
  // La posición 32 del archivo example.txt tiene que ser igual a el hexadecimal 44.
  if ( 2 + buffer[51] != 0x46 )
  {
    printf("Noooo, %x \n", buffer[0] + buffer[204]);
    exit(1);
  }
  printf("Aprobaste level 5");
  getchar();
  return 0;
}

int main(int argc, const char **argv)
{
  char *buffer = malloc(416*sizeof(char));

  buffer[51] = 1;
  buffer[52] = 'E';

  // Inicializa el buffer
  memset(&buffer[216], 0, 200*sizeof(char));
  memset(&buffer[4], 0, 200*sizeof(char));

  buffer[53] = fopen("example.txt", "rb");

  if ( !buffer[53] )
  {
    printf("No se puede leer el archivo bye bye \n");
    exit(1);
  }

  // Carga a partir de la posición 216 el contenido del archivo.
  // 216-53 = 163
  // 216+163 = 379
  // 416-216 = 200
  fread(&buffer[216], 200*sizeof(char), 1*sizeof(char), buffer[53]);

  // Copia el buffer a partir de la posición 216 al comienzo del buffer a partir de la posición 4

  strcpy(&buffer[4], &buffer[216]);

  // El carácter de la posición 47 del texto example.txt tiene que ser igual 1
  if ( buffer[51] != 1 )
  {
    printf("Mal \n", buffer);
    exit(1);
  }
  check(buffer);
  return 0;
}
```

Primero pasamos el primer if.
Agregamos las 4 As al comienzo para saber cual es la posición 51, hasta 190 caracteres.
```
AAAAPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP1PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
```

Luego eliminamos las As y agregamos otra vez 4 As y 11 caracteres al comienzo

```
AAAA12345678911PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPDEPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
```

Luego eliminamos las As y los 11 caracteres.

#### exploit:
```
00000000: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000010: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000020: 4444 4444 4544 4444 4444 4444 4444 3144  DDDDEDDDDDDDDD1D
00000030: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000040: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000050: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000060: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000070: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000080: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
00000090: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
000000a0: 4444 4444 4444 4444 4444 4444 4444 4444  DDDDDDDDDDDDDDDD
000000b0: 4444 4444 4444 4444 4444 4444 4444       DDDDDDDDDDDDDD
```
