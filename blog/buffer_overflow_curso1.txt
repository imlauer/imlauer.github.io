---
title: "Explotando un buffer overflow provocado al querer restringir/comparar el tamaño del buffer sin considerar el signo."
date: 2024-08-06T16:59:15-03:00
tags: ["reversing","ida",'cracking','examen','1','bufferoverflow','ida']
---
Archivo del examen: `EXAMEN_LEVEL_1b.7z`
[EXAMENES LA CONTRASEÑA es A](/CRACKING.7z)

O descargalo desde acá: http://ricardonarvaja.info/WEB/IDA%20DESDE%20CERO/EXAMENES/EXAMENES%20Password=a.7z

La comparación se realizó con `jl`.
Luego pisamos la variable `numero_random` con `44434241` que luego se xorea con la variable `numero_2` que es 0, y eso hará que pasemos el nivel.

##### Inicio
Concepto fundamental: Qué es un offset? 

>En informática, un offset dentro de un array u otra estructura de datos es un entero que indica la distancia (desplazamiento) desde el inicio del objeto hasta un punto o elemento dado, presumiblemente dentro del mismo objeto. El concepto de distancia es solamente válido si todos los elementos del objeto son del mismo tamaño (típicamente dados en bytes o palabras). 


View -> Open subviews -> Strings

Las strings son clickeables y apretando la x podemos ver adonde la utilizan.  
Podemos pintarla de algún color en la parte izquierda de la ventana.      
Cuando no tenés símbolos NO son registradas, tenés que identificar las llamadas por ejemplo: `call sub_4011C0` es `printf` si le das click al nombre y otra vez al nombre, verás una llamada a `_studio_common_vfprintf`. Por lo tanto podemos renombrarla boton derecho en la palabra `sub_4011C0` y Rename o apretando `N` como `_printf`   
Podemos renombrar todo tipo de variables para facilitar la lectura. Como por ejemplo renombrar la `var_10` como `numero_random`.    
Memset es para inicializar un buffer, generalmente se lo pone a 0 todo el buffer para iniciarlo, y el puntero es la variable Destination (`Dst`), por lo tanto ese es el inicio del buffer.
Si hacemos doble click en `Dst` vamos a la representación estática y haciendo click derecho a `Dst` luego Array, le ponemos como Size(Tamaño) que hayamos visto con el que inicializó (0xC8).
Una vez que inicializó el buffer, lee un archivo con el nombre `example.txt` lo llenamos de `AAAAABBBB`
Colorea las dos ventanas de abajo, si no es 0, izquierda roja, derecha verde.   
Identifica el fread y luego llama a atoi, el count es 1 o sea que lee 1 elemento de tamaño 4 bytes, y lo guarda en Destination buffer(DstBuf), me da a entender que ese buffer es un array de enteros(o dwords) no de bytes. 

> dword:en inglés double word, doble palabra, es una unidad de datos que es dos veces el tamaño de una palabra. En las plataformas x86, que tienen una longitud de palabra de 16 bits, una unidad dword tiene una longitud de 32 bits.



Entonces podemos cambiarlo nuevamente apretando Dst -> dd (hasta que cambia a dd) -> Botón derecho en Dst -> Array -> y ahora nos detecta el size porque habíamos inicializado el buffer en este caso con 50 bytes decimal, puesto que son `50 x 4 dword` serían 200 porque se maneja todo en decimal.     
Ahí iría el primer entero `fread` que lee las A que puse en el archivo.   
Imprime lo que leyó el archivo, el contenido.   
Luego llega a la función atoi
atoi: convierte string en un número.   
y lo coloca en ElementSize.   

Le puso elementsize porque en un fread anterior luego de comparar con el size máximovamos a poner que elementsize es numero porque hay un mensaje que dice `numero:`

O sea que lee un primer número que luego lo comparará con un máximo y lee otro número con fread. El primer número lo compara con C8 si es menor. Si ese número es más grande que C8 y el buffer que teníamos era de C8 tenemos que tratar de desbordarlo.

`jl` toma en cuenta el signo, por lo tanto si ese número es negativo se toma como si fuera menor y podés desbordar el buffer.

Luego en el fread los argumentos de fread son todos con signed o sea que no se considera el signo, ese `-1` o ese `ffffff` lo tomará como valor positivo y podemos leer la cantidad de bytes que queramos porque es la cantidad de bytes leídos que es el count por el elementSize que en este caso es un valor negativo.
Por lo tanto podemos cambiar el número.

Al hacer el archivo tenemos que tener en cuenta de que atoi lee una string. Tenemos que armar una string por ejemplo usando un editor hexadecimal:      
31 para ponerle el menos adelante.   
`20 20 20 20 31 42 42 42`

![](/img/cracking/curso1_hxd.png)

Entonces ya sabemos que el número será negativo interpretado y pasado a dword. Pasará esa comparación porque el número es grande pero negativo y tratará de hacer un `fread` y escribir en el `Dst`.

Como `Dst`(Destination) está arriba de todo podemos pisar, las demás variables.

Para tomar la decisión de si aprobaste el nivel uno, toma el número random y lo xorea con la variable: `numero_2` y lo guarda en `resultado`, ese resultado lo compara con `41424344h`.
Esto quiere decir que si nosotros podemos pisar el número random con lo que nosotros queremos, porque si ese número random es verdadero no sabemos con que xorearlo para que nos dé un valor constante, pero si pisamos ese número random que esta justo debajo del buffer lo podemos transformar en constante y al hacer xor con el `numero2` podemos lograr que sea `41424344h` ahora cuanto tenemos que pisar para llegar hasta número random desde `Dst` a `resultado` si marcamos vemos que en realidad serían 51 dword: `51*4=204 bytes` y a continuación vendría el número random.   
Y ahora insertamos esa cantidad de bytes en el archivo `example.txt` y a continuación de esos bytes tenemos que pisar `numero_random` podemos poner que sea `41424344h` en realidad tiene que estar al revés por `little indian`. 

Y el otro valor `numero_random` ya es 0 y se xorea con el `numero_2`
El `numero_2` es el 2do valor que lo pasa como atoi, lo podemos poner en 0 también pero como es una string tenemos que ponerlo como `20` en el editor hexadecimal.
Y ese valor lo xorea con `414243`. 

![](/img/cracking/resultado.png)
Ahí tenemos el -1 del primer valor y el 0 del segundo.
Y eso lo xorea con `414243` al revés y si hicimos bien la cuenta nos daría que está todo bien.

Esa fue la forma de reversearlo.

Pisamos el numero random con `44434241` y se xoree con la variable `numero_2` que es 0, y eso hará que pasemos el nivel

Podemos apretar el número a la izquierda de la linea y apretar F2 para arrancar el debugger desde el menú luego debugger -> start process. 
Vemos que el primer número fue tomado bien como -1 y el segundo 0 y luego el número random `41424344` y la comparación es `41424344` con `41424344`


Miralo en YouTube: https://youtube.com/watch?v=viv-bdTpOpI

O en una instancia de invidious: https://redirect.invidious.io/watch?v=viv-bdTpOpI

### Más tutoriales
https://revteam.re/forum/forums/tutorial-documents.13/   
https://forum.tuts4you.com/topic/44152-revteam-reverse-engineering-collection/

#### Otra herramienta que ví que se usa además de ida y ghidra.
https://binary.ninja/

##### Página para pedir algún crack de algún programa
https://revteam.re/forum/forums/crack-request.5/

#### Explotando un buffer overflow básico
https://gist.github.com/apolloclark/6cffb33f179cc9162d0a


---

#### Aprobé sin necesidad de leer el ASM sólo usando el decomipilador con F5:
![](/img/cracking/EXAMEN_LEVEL_1b/aprobe.png)

#### Sólo puse un -200 la comienzo del example.txt y funcionó pero en realidad sólo tenía que poner un -1 sin necesidad de agregar el 0 para el xor, así me quedó example.txt:

![](/img/cracking/EXAMEN_LEVEL_1b/aprobe1.png)


#### Este es el código que decompila el IDA.
Sólo hay que hacer un par de renombres: `sub_401200(0)`: time(0) printf: `sub_4011C0` y 1094861636 significa "ABCD" o `0x41424344`, cuando hacés el exploit tenés que ponerlo al revés por little indian.

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  char Buffer[200]; // [esp+0h] [ebp-DCh] BYREF
  int v6; // [esp+C8h] [ebp-14h]
  char v7[4]; // [esp+CCh] [ebp-10h]
  char v8[4]; // [esp+D0h] [ebp-Ch]
  size_t ElementSize; // [esp+D4h] [ebp-8h]
  FILE *Stream; // [esp+D8h] [ebp-4h]

  ElementSize = 0;
  *(_DWORD *)v8 = 0;
  v3 = sub_401200(0);
  srand(v3);
  *(_DWORD *)v7 = rand();
  memset(Buffer, 0, sizeof(Buffer));
  Stream = fopen("example.txt", "rb");
  if ( !Stream )
  {
    sub_4011C0("No se puede leer el archivo bye bye \n", Buffer[0]);
    exit(1);
  }
  fread(Buffer, 4u, 1u, Stream);
  sub_4011C0("contenido %s\n", (char)Buffer);
  ElementSize = atoi(Buffer);
  fread(&Buffer[4], 4u, 1u, Stream);
  *(_DWORD *)v8 = atoi(&Buffer[4]);
  sub_4011C0("numero %x\n", ElementSize);
  sub_4011C0("numero2 %x\n", v8[0]);
  if ( (int)ElementSize >= 200 )
    exit(1);
  fread(Buffer, ElementSize, 1u, Stream);
  sub_4011C0("numero random %x\n", v7[0]);
  v6 = *(_DWORD *)v8 ^ *(_DWORD *)v7;
  if ( (*(_DWORD *)v8 ^ *(_DWORD *)v7) == 1094861636 )
    sub_4011C0("Aprobaste level 1", Buffer[0]);
  return *(_DWORD *)v7;
}
```
