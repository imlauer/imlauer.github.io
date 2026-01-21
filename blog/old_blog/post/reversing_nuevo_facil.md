---
title: "Reversing nuevo facil"
date: 2024-09-21T04:36:50-03:00
tags: ['reversing']
---
El keygen se encuentra en: https://drive.google.com/file/d/1QRIk3zBGGXH54nSZorX3jnuNmURCHw6K/view?pli=1



```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *gets_s(char *s, size_t n)
{
    if(!s) return NULL;

    size_t i=0;
    int ch;

    for(i=0; i<n-1; i++) {
        ch = fgetc(stdin);

        // If end-of-file is encountered and no characters have been read into the array,                          
        // or if a read error occurs during the operation, then s[0] is set to the null character                  
        if(ferror(stdin) || (ch == EOF && i == 0)) {
            s[0] = '\0';
            return NULL;
        }

        // If EOF and we have read at least one character                                                          
        if(ch == EOF) {
            s[0] = '\0';
            return s;
        }

        s[i] = ch;

        if(ch == '\n') {
            s[i] = '\0';
            return s;
        }
    }

    while ((ch = getchar()) != '\n' && ch != EOF);
    s[0] = '\0';
    return NULL;
}

int main(int argc, const char **argv, const char **envp)
{
  char v4; // [esp+0h] [ebp-74h]
  char v5; // [esp+0h] [ebp-74h]
  int v6; // [esp+0h] [ebp-74h]
  int v7; // [esp+8h] [ebp-6Ch]
  size_t i; // [esp+Ch] [ebp-68h]
  size_t v9; // [esp+10h] [ebp-64h]
  char Destination[52]; // [esp+14h] [ebp-60h] BYREF
  char serial[20]; // [esp+48h] [ebp-2Ch] BYREF
  char key[20]; // [esp+5Ch] [ebp-18h] BYREF

  strcpy(Destination, "_bondi");
  memset(&Destination[7], 0, 43u);
  v7 = 0;
  printf("Ingresa una key: ", v4);
  gets_s(key, 20u);
  v9 = strlen(key);
  if ( v9 < 5 )
    strcat(Destination, key);
  printf("Ingresa un serial: ", v5);
  gets_s(serial, 20u);
  if ( strlen(serial) < 2 )
    exit(1);
  if ( v9 < 5 )
    strcat(Destination, "50431");
  v6 = atoi(serial);
  if ( !v6 )
    exit(1);
  for ( i = 0; i < v9; ++i )
    v7 ^= key[i];

  printf("serial introducido: %d\n",v6);
  printf("serial que tiene que ser: %d\n",v7);
  if ( v7 == v6 )
    printf("Bien hecho !\n", v6);
  else
    printf("Nada que verrrrrr....\n", v6);
  system("pause");
  return 0;
}
```

![win](/img/reversing_facil.png)
