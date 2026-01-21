---
title: "Explotando buffer overflow provocado por copiar un buffer de 300 a uno de 200"
date: 2024-08-07T07:24:45-03:00
tags: ['reversing','ida','ricardo','narvaja','examen','3','buffer','overflow','cracking']
---
Lo único que hacemos es pisar la variable que está abajo del buffer de 200 porque copia el contenido del buffer de 200 a un buffer de 300. Le ponemos de valor 0 a la variable que está debajo del buffer de 200 porque hace esta comparación `cmp ptr [eax+0C8h],0` para ganar el reto. En donde `0C8h` es un offset que hace referencia a una variable que está dentro de estructura en donde está también declarado el buffer.     
Algo así sería en C:    
```c
struct MyStruct {
	char buffer[200];
	int flag;
}
```

**Este tutorial tiene mucho blabla de como usar el IDA pero existen muchos métodos algunos hasta automáticos.**

Si miramos la representación estática del stack podemos ver que hay un buffer e identificar su tamaño automáticamente haciendo un click derecho Array.    
Tip: Es recomendable darle un nombre al buffer que haga referencia a su tamaño, por ejemplo: `buffer_200`

`push 12Ch ; Size` # Hace referencia al tamaño del buffer, que detectó automáticamente en el paso anterior.

Lee un archivo si es correcto, EAX será distinto de 0.
Podemos desbordar el buffer de 200 y pisar la variable que está abajo.

Renombramos `sub_4010B0` a `check` e identificamos que el argumento es el puntero a `Buffer_200`. Damos doble click a `sub_4010B0` luego rename a `arg_0` en donde dice: `enter stack variable name` asignamos un nombre por ejemplo `puntero_buffer_200`

Luego click derecho en check `set type` para propagar el nombre de la función ya que asignamos como argumento a `buffer_200`

Lo mueve a eax y le suma `C8` entonces lo que está haciendo acá es checkear la variable flag porque a continuación del buffer de 200 está la variable flag.

Ejemplo: `cmp ptr [eax+0C8h],0`
### Ese es el típico caso de una estructura cuando vos accedes a una variable de una función anterior a través de un puntero más un offset, en este caso 0C8h.    
Estamos hablando de que es un campo de una estructura, **porque sino no se podría acceder a la estructura a través de sumarle un offset a un puntero**

Entonces podemos volver al código entrar al `buffer_200` en la representación estática y definir `buffer_200` y la variable de abajo como una estructura, selecciona click derecho `create struct from selection`, si querés podés renombrar la estructura a `MyStruct`.


Entonces nos damos cuenta que lo que está haciendo es pasar el puntero de la estructura a la función `check`

Entonces vamos a cambiar los nombres de `buffer_200` a MyStruct y de `puntero_buffer_200` a `puntero_MyStruct`

Si ahora accedemos a check y apretamos en la linea `cmp ptr [eax+0C8h],0` y luego `p` nos damos cuenta que apunta al campo `flag`.


Compara si esa variable es 0, si es 0 sale, pero si mirás las referencias a esa variable se inicializa en 1.

Luego creamos el example.txt con 200 A y 4 bytes de 0s y con eso pasaríamos pero eso no es todo!
![](/img/cracking/3.png)

Luego tenemos otro `call sub_401010` que es otro check porque verifica si vas o no por buen camino, así que lo renombraremos `check2`, el argumento de la función check es un puntero a la estructura. Entonces ingresamos a check2 y al `arg_0` no renombramos como `p_MyStruct` y el de arriba `Str1` si apretás boton derecho y le das array automaticamente te reconoce el tamaño.

Vamos a reconocer todos los printf: todas las `call sub_401270` como `_printf`, pero después nos encontramos con otra función que es sprintf esa función escribe en un archivo, el primer argumento es un buffer y el segundo es el formato.

Luego compara ese string con N.

9:00
