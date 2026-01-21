---
title: "Reversing CrackMe simple con el decompilador de Ghidra"
date: 2024-08-06T07:37:45-03:00
tags: ['reversing','ghidra']
---
Instalá ghidra: `sudo apt install -y ghidra`
O lo podés descargar e instalar desde acá: https://github.com/NationalSecurityAgency/ghidra

Descargá el archivo del desafío `unlock_me1`, acá: https://secur3.us/GhidraFiles/unlock_me1

Los pasos básicos para afrontar un desafío como este son:
1. Crea un proyecto Ghidra e importa el programa de desafío.
2. Abrí `unlock_me1` en CodeBrowser e inicia el análisis automático.
3. Busca la función principal (primer argumento de `__libc_start_main()`
4. Renombra el nombre de las variables y funciones hasta que comprendas la lógica.
5. Reconstruí la lógica utilizada para verificar los códigos de entrada.
6. Genere y pruebe un código de entrada válido.

### Encontrando el main
Después de importar y analizar `unlock_me1`, necesitarás ubicar el punto de entrada para la función. Para una aplicación libc como ésta, `__libc_start_main()` se utiliza para cargar `main()` dentro de un entorno apropiado. Puedes encontrar esto en el binario usando el método abreviado de teclado 'G' desde la vista de listado de Ghidra para `unlock_me1` y saltando a `__libc_start_main()` que se encontrará como una función Thunked como se muestra aquí:

![goto](/img/ghidra/goto.webp)

![libc start main](/img/ghidra/libc_start_main.webp)       
Thunked-Function tiene un XREF de `FUN_00101080`

Al abrir el XREF de llamada desde `FUN_00101080:001010a4` se muestra lo siguiente:   
![](/img/ghidra/libc_start_main_decompile.webp)
Entrada descompilada en main()

Según la [documentación](https://refspecs.linuxbase.org/LSB_3.1.0/LSB-generic/LSB-generic/baselib---libc-start-main-.html), el primer argumento de `__libc_start_main()` es la función main(). Puede hacer doble clic en `FUN_00101165` para acceder a la vista descompilada de esta función y actualizar la firma para que coincida con la convención estándar:

![](/img/ghidra/decompile_fun.webp)


![](/img/ghidra/edit_function.png)

Ahora podemos mirar el resultado descompilado y comenzar a buscar variables para cambiar el nombre dentro de la función. Para empezar Ghidra nos muestra el siguiente código:

![](/imgi/ghidra/decompile_main.webp)

Comenzando desde arriba, vemos que la entrada del usuario se recopila mediante scanf en la línea 13 y se almacena en `local_38` y la longitud de la cadena se coloca en sVar2. A estas variables se les puede cambiar el nombre de `input` y `input_len` respectivamente, generando el resultado descompilado como se muestra aquí:


![](/img/ghidra/decompile_main2.webp)

Ahora está claro que la línea 15 está verificando la longitud de la entrada y rechazará cualquier entrada a menos que tenga una longitud exacta de 0x14 (20 en decimal). Podemos ver que `local_1c` y `local_20` se inicializan a 0 antes de ingresar a un ciclo while. Dentro del bucle podemos ver que `local_20` se utiliza como índice en la entrada en la línea 22 y luego `local_20` se incrementa en la línea 23. También en la línea 22 vemos que los caracteres de la cadena de entrada se suman en `local_1c`, lo que nos da la lógica nombres `input_sum` e `index` para `local_1c` y `local_20` respectivamente, como se muestra en la descompilación actualizada:

![](decompile_main3.webp)


Al leer el código ahora, debería quedar claro que la entrada debe satisfacer dos propiedades para llegar al mensaje 'Unlock!' en la línea 26. Por línea 15, la entrada debe tener exactamente 20 bytes de longitud. Según la línea 25, la suma de los bytes en la entrada debe ser un múltiplo de 7.


## Solución

A partir de este punto, el desafío crackme se ha transformado en un problema matemático básico. Debería ser posible sumar 20 caracteres imprimibles y luego usar el módulo para determinar cuántos bytes sumar o restar para producir un múltiplo de 7.

Por ejemplo, podemos calcular la suma de 20 caracteres "0" y encontrar que es uno de un múltiplo de 7.

```python
>>> ord("0")*20 % 7
1
```

Esto significa que sólo necesitamos agregar 6 bytes a la suma total. Esto se hace fácilmente cambiando un '0' (0x30) por '6' (0x36) dándonos la siguiente solución:


```python
$ ./unlock_me1
Enter the unlock key: 00000000000000000006
Unlocked!
```

### Tarea
El ejemplo de tarea para esta publicación sigue la misma idea básica, pero tiene algunas comprobaciones adicionales que necesitarás realizar para producir una entrada válida. La función principal descompilada en este ejemplo se muestra a continuación:

![](/img/ghidra/decompile_main_homework.png)


[Descargá el 2do reto acá](https://secur3.us/GhidraFiles/unlock_me2)

Fuente: https://medium.com/@cy1337/reversing-a-simple-crackme-with-ghidra-decompiler-5dd1b1c3c0ba


#### Querés aprender más de reversing?
https://youtube.com/channel/UCPNPSP20z4FGfgMJ71VOJjw/playlists


O miralo en alguna instanacia de invidious: https://redirect.invidious.io/channel/UCPNPSP20z4FGfgMJ71VOJjw/playlists
