---
title: "[AUDIO][APUNTE] Taller reparacion electrodomesticos (Clase 9) - Tipos de fuentes. Fuente standBy. Rectificador. Tipos de relay y como medirlos. Regulador de voltaje. Reparación ventilador. Cargador de celular con fuente lineal. Problema: Capacitor TRIAC. Como medir capacitor. Capacitor transforma la corriente de punzante a pura. Estator: parte fija del motor. Rotor: jaula de ardilla el que rota (el que gira). Hasta antes de los diodos es corriente alterna. Como medir relay. Bobinas en paralelo, capacitor para corregir factor de potencia. Ventilador tiene bobina de arranque y de trabajo. Hay que corregir factor de potencia con un capacitor. Split no tiene bobina de arranque, la heladera sí. Calcular impendancia entre cables para calcular arranque, trabajo. Como medir si funciona un ventilador paso por paso en hora 2:40. Hay que ir cambiando las velocidades al medir cables. El fusible del ventilador al parecer estaba bien, pero la bobina estaba cortada, pero no quemada. Como medir bobina quemada."
date: 2024-08-30T21:13:12-03:00
tags: ['electrodomesticos']
---
### Audio de la clase:
https://youtu.be/xniJUxh04qI

### O mirala en invidious
https://redirect.invidious.io/watch?v=xniJUxh04qI

### Audio en Vocaroo:
https://voca.ro/14o6t9RexjMx

#### Temas tocados en esta clase:
Tipos de fuentes, transformadores, procesadores, fuente standby en aires acondicionados, placas con más de 1 fuente. 

Transformadores función: bajar la tensión.

En el transformador del microondas el bobinado tiene más vueltas en la segunda bobina.
Todo conductor tiene impedancia.

Cable más largo: mayor impedancia.

#### ¿Cómo haces para identificar cual es el primario y el secundario?
El primario tiene menos resistencia.

Capacitor polarizado: corriente continua.   
Capacitor no polarizado se puede usar en corriente continua.

De la placa sale 220v y entra 12v.

Fuente resistiva/capacitativa, rectificador.

Hasta antes del rectificador es corriente alterna.

No siempre el rectificador de onda completa se verá representado como un rombo en un circuito, lo importante es hacer los pares de salida.

Capacitor: transforma de corriente continua punzante a corriente continua pura.

### Poner capacitor en paralelo para rápida prueba. Se puede medir capacitor sin sacar. 

Medir en frío/caliente da diferentes resultados.

Se puede crear un cargador de celular con una fuente lineal.

Para medir reley tenés que medir los pines 2 y 3 de los 3 pines de arriba.

Reparación ventilador.

Tipos de relay: amperimétrico, voltáico.



Lastimosamente tenía poca batería no pude sacar fotos y tuve que escribir, no hice mucho esfuerzo para escribir bien, escribí con la intención, si tenés mandámelas por wpp.

## Imágenes: [https://imlauer.blogspot.com/2024/11/audioapunte-taller-reparacion_14.html](https://imlauer.blogspot.com/2024/11/audioapunte-taller-reparacion_14.html)


### Transcripción
En donde siempre vamos a tener dudas es en la parte eléctrica.

Por ejemplo un split agarramos un botón enciende, subimos bajamos la temperatura damos más o menos velocidad pero todo está acá en el control.

Por lo menos yo quiero que ustedes sepan y estén seguros.

Cuantos tipos de corriente se trabaja acá (en la placa)? Continua y alterna.

O sea que para poder decir bueno yo quiero inclinarme para reparar esa plaqueta porque yo se que está ahí el problema, entonces yo tengo que saber si tenemos que medir en corriente continua o alterna, si es peligrosa la parte que estoy midiendo.

Lo peligroso son los altos voltajes, en la mayoría de la placa está bien dividida la parte de alto voltaje y la de bajo voltaje.

Por ahí una pista de bajo voltaje puede pasar cerca de una de alto voltaje, porque el espacio es muy chico.

Vamos a suponer que queres hacer el service de un split, cuando 1 vez hacés ya lo sabés para siempre.

### A veces cuando hacés el service del split, tenés que tener más cuidado
Porque cuesta armar después que se desarma.

Siempre que desarmás un split vean que quede bien armado, no dejen ni siquiera la tapa de arriba mal armada.

Hay veces que conviene de atras para adelante, otras veces de adelante para atras es cuestión de observar cuando se desarma

Igual que los tornillos, no vayan a empezar a desarmar y tirar los tornillos, dividilos bien porque sino va a marcar el plástico o vas a poner otro que va a bailar, separalo en diferentes recipientes.

Incluso hay veces que algunos tornillos vienen con philips y otros vienen con tor, marcá.

Vamos a suponer una tostadora hay muchos tipos de tostadora o una plancha, no todos se desarman igual, algunos tienen un tornillo que no se encuentra, no tenés que palanquear.


Entonces en las placas electrónicas, van a tener que saber que siempre en las placas electrónicas habrá corriente alterna y continua.

Si nosotros miramos son los mismos componentes: resistencias, capacitores, bobinas, mosfets, triac, relay. Casi siempre son los mismos componentes.

Entonces deben saber que las placas hay que trabajar con corriente continua y alterna.

### Que se necesita para hacer una corriente continua?
### Cuantos tipos de fuentes hay?
3 fuentes: lineal, switching o conmutada o resistiva capacitativa. 

Hay muchos que no consideran la última una fuente, pero del momento en que tenemos una corriente alterna de 220 voltios de un valor eficaz y lo bajamos a 5, 3, 9 voltios de corriente continua.

Estas placas que están acá, trabajan con transformadores. 

Y hay otras placas electrónicas que trabajan con otro tipo de transformador, y ambos cumplen la misma función.


### Que función tiene un transformador?
Reducir el voltaje y rectificar.

Porque necesito un voltaje muy bajo para que trabaje el microprocesador. 

En todas las placas necesitamos un transformador, y todos tienen un procesador sin el procesador no podría trabajar.

El procesador es el que va a recibir la órden y el va a procesar y ordenar los trabajos en los tiempos que se tengan que hacer.

En el caso de un split el va a tomar la temperatura que nosotros le dijimos que encienda, si yo les estoy diciendo al split que encienda y ahí recién enciende, como es eso?

### Como hizo para responder a la órden?
El recibió la órden del control porque estaba encendido (fuente standby).

##### En las fuentes, hay una fuente aparte que se llama standby

Esa fuente standby está siempre encendida para tener activo el chip, porque el único que está activo en ese momento es el microprocesador.

Hay una fuente especial para él o hay una parte de una fuente que va solo para el.

Es parte de la fuente.


#### Entonces las fuentes tienen 2 circuitos:
1. Standby: 
2. 

Hay placas que tienen 3 fuentes, otras placas tienen 2 fuentes. No son todas las placas iguales, pero si me pongo a repararlas y uno de los sectores no me andan, todas las placas son practicamente iguales.

Cuantos tipos de fuentes hay: 3 fuentes:
1. Lineal se alimenta de la misma frecuencia que la tensión. (220 voltios x 50 hertz)
2. Resistiva capacitiva: 
Cuál es la misión del transformador? Bajar la tensión , con un capacitor y con la resistencia hago exactamente lo mismo, los capacitores cuando están en serie hacen caer la tensión.
## Que es para la tensión el capacitor?
El capacitor es un reductor de tensión.
## Por qué cae la tensión en un capacitor?
## Por qué cae la tensión en un transformador?
Porque en un transformador hay una espira primaria, nuestro núcleo de hierro y una espira secundaria. 
En el primario tengo muchas vueltas y en el secundario tengo pocas vueltas, si fuera al revés aumentaría la tensión como para en un **microondas**.

Acá yo hago bajar la tensión porque en el secundario tengo pocas espiras.

Si yo te pregunto cual es el primario y el secundario es fácil de saber.

### Todos los conductores tienen impedancia
La impedancia es la dificultad del paso de la tensión.

Si yo tengo el mismo calibre de cable y tengo uno con 5 metros y otro 50 metros.  Voy a encontrar mayor impedancia en el cable más largo, porque tiene más caída de tensión.

### Cuál de los dos tendrá mayor impedancia: el primario o el secundario?
El primario. Entonces inmediatamente identificamos cual es el primario.

Ahí se produce la caída de tensión.

En la fuente capacitativa resistiva no tengo transformador, sino un capacitor en serie.
Uno será la fase y el otro el neutro, en una de las líneas el capacitor está en serie.

Positivo y negativo sólo en la corriente continua. En la alterna: neutro o fase.

Tiene que estar en serie el capacitor. 

Cuando el trae el signo positivo o el signo negativo es polarizado.

### Sólo está polarizado el negativo. Esto es un capacitor únicamente para corriente continua.
En la corriente continua sí tengo corriente positiva y negativa.

# No se puede conectar en forma inversa porque explota.

Si yo tengo una corriente continua y conecto al revés el capacitor explota el capacitor, porque no soporta la corriente **inversa**, y lo que hace la corriente alterna es eso: cambia de siglo.

En la corriente alterna tenemos que usar capacitores **no polarizados**.

Vamos a ver estos tipos de capacitores en donde nunca vamos a ver que diga positivo y negativo. Al contrario dice que es para 220 voltios o 400 voltios de corriente alterna a 50 ciclos 60 ciclos, pero nunca dice cual es el positivo y cual el negativo.

#### Cuando no tiene polaridad es para corriente alterna
# Se puede poner en corriente continua?
Sí, porque no tiene polaridad. Cuando miramos un diagrama no hay un sólo dibujo en los diagramas para los capacitores.

Los capacitores causan impedancia al circuito.

Si miramos las placas con transformadores en algún lugar tienen para colocar el primario del transformador y una vez que pasa por el transformador tiene una salida o un ingreso a la placa.

O sea que la placa salen 220 voltios y van al transformador y vuelve ingresa a la placa con 12 voltios con 13, 30 con lo que se le hizo a la placa.

Tiene una salida de 220 y tiene un ingreso de un voltaje muy reducido, por lo general este tipo de placas trabajan con 12 voltios.

El chip es alimentado con 3, 5 voltios por qué no puso un transformador de 3 o 5 voltios.

### Por qué? Porque de la misma manera tienen que usar relevadores o relay.

Es posible que yo tenga en mi laboratorio **donde nosotros trabamos con electrónica ya no es taller es un laboratorio**. Es el lugar de trabajo de electrónica.

No son iguales las herramientas de un taller de un laboratorio.

En el taller tenemos llave, martillo, contrapinza de mucha fuerza soldadora de muy alta potencia.

Y en la parte electrónica todo es **medir intensidad voltaje TODO**, entonces necesitamos herramientas para esos trabajos.

Vamos a suponer que yo no tengo un transformador de 12 voltios.

Y estoy trabajando y me envenené, pero sólo tengo un transformador de 30, sirve o no?

No, tengo que hacer caer esos voltios a los 12. 

Existen distintos tipos de **reguladores de voltaje**.

No todos los componentes que tienen 3 patitas son transistores, algunos son reguladores de voltajes, siempre el voltaje tiene que ser mayor que el regulador.

Hay reguladores para distintos voltajes, como hay diodos zener porque tambien son reguladores de voltajes, como también de pontencia.

Cuando ustedes están ante esta placa y dicen por el error que tiene el lavarropas es problema de fuente, ustedes ya saben que trabajan con este tipo de placa que no vamos a encontrar transformadores, vamos a encontrar capacitiva resistiva.

### Cuando no prende nada sabemos que es problema de fuente.
Cuando no prende nada tenemos un problema con el chicote de power, se cortó un cable o es la fuente.

Estas placas son de aire acondicionado que trabajan con este transformar por lo tanto tiene fuente con transformador porque si o si, las placas necesitan corriente continua y de bajo valor, a comparación de los 220, necesitamos 30, 12 9 voltios, depende de la placa con la que estemos trabajando.

Entonces si o si vamos a necesitar **hacer caer el voltaje**. 

Una forma es usando un transformador lineal, porque trabajan a la misma frecuencia de la línea: 50 hertz, pero en este tipo de fuente tiene una fuente switching o conmutada la diferencia entre este y este que la otra trabaja desde los 10.000 hasta los 100.000 , y no se puede reemplazar porque estos transformadores están hechos para trabajar a una determinada cantidad de ciclos, podemos poner de otra placa de repuesto.

### En la lineal no pasa eso, mientras que yo tenga un transformador que me de salida 12 voltios listo le pongo. Vamos a suponer que tengo uno que es para 2 amper, y el que yo tengo es de 1 amper NO CONVIENE PONER. Pero si tengo uno de 5 amper, SÍ le puedo poner porque quiere decir que está grande y va a trabajar de lujo.

#### Por qué el fabricante no le puso de 5 amper ? 

Es porque es más barato poner uno más chico. Se trabaja con el tamaño lo más reducido y el precio lo más reducido.

Hay muchísimos transformadores, el mínimo valor da un resultado muy alto en el precio, se cuidan todas las diferencias.

En nuestro taller si podemos colocar uno más grande, si calza no pasa nada.

Entonces, teníamos las fuentes lineales, capacitivas resistivas (sin transformador), switching o conmutativa (un transformador muy chiquito) pero con la misma potencia que el lineal, y es una fuente switching en donde yo tengo que filtrar la electricidad hacerlo una corriente **punsante entre 10.000 y 100.000 ciclos para que pueda trabajar**.


Entonces si yo voy a trabajar tenemos que fijarnos que capacitor está en serie con la entrada de los 220 y ese es el transformador que forma parte de la fuente.

Luego puede tener posiblemente 2 resistencias en paralelo que pueden ir.

Qué nosotros logramos ahí? Hacer caer la tensión.

O sea que nosotros con estos dos componentes que vamos a encontrar en esa linea de los 220, no vamos a encontrar un transformador, acá yo hice caer de los 220 a 12 voltios y allá también.

**Ahora en calidad la switching es superior a la capacitativa resistiva**

La capacitativa resistiva falla mucho por eso muchos no la quieren. 

### Qué faltaría acá para que sea una fuente? Que es lo primordial?

Que rectifique.

El switching necesita una corriente punzante entre 10.000 y 100.000 para que pueda trabajar el chip.

Si no rectifico el procesador no me va a trabajar, porque el procesador leerá el pulso y lo va a confundir.

Cuando nosotros apretamos el botón al split, la placa recibió una orden y si no filtramos entonces seguirá recibiendo órdenes y no sabrá lo que nosotros mandamos, porque la corriente alterna tiene pulsos. Ahora tenemos que rectificar, así que seguido de esto estará el diodo rectificador.

Que es lo mismo que nosotros en el dibujo con 4 diodos esa es una fuente rectificadora de ciclo completo, es un **puente rectificador de ciclo completo**.

Nosotros le dabamos allá, los 4 diodos que están acá nunca están puestos en la placa, nunca están puestos en triángulos, depende de como me queda el espacio vamos colocando los diferentes componentes.

### Qué tenemos que saber del puente rectificador?
Donde está la entrada y la salida: cátodo y ánodo.

Vamos a poner todos los cátodos del mismo lado, o sea que yo no acomodé y ahora tengo que armar el circuito vamos a suponer que yo caso estos dos, que definí ahí?

Es lo que estamos queriendo que nosotros salga por un lado, o sea yo ya hizo así porque según las pistas necesito que el positivo salga de ese lado.

O sea si entra por ahí significa que yo por los dos tendré salida negativa, yo tengo que sacar dos para salida y dos para entrada. Porque tengo fase y neutro y tengo que electrificar a los 4, y de 4 tiene que salir 2 salida.

Yo de acá voy a tener una salida: positiva. Entonces quiere decir que yo voy a elegir acá alterna, entonces yo voy a elegir donde quiero positiva.

Tenés que poner siempre en pares enfrentados, en estos dos ángulos tengo la corriente alterna de 15 voltios y acá yo tenía 220 voltios de corriente alterna, entonces vamos a rectificar de que lado quiero el positivo vamos a suponer que yo elegí el positivo de acá.

Tengo que poner el diodo para acá y para acá, yo ya elegí quiere decir que yo acá voy a tener salida positiva. 


Luego de traer la corriente positiva y negativa, tengo que armar los pares. Una con señal de ánodo y una señal de cátodo.

#### No importa como estén ubicados los diodos, lo importante es formar los pares.

Y ahí ya vamos a tener corriente directa, en cualquier parte de la placa hasta los diodos será corriente alterna, luego de los diodos corriente continua.

En la fuente lineal lo primero que encontraremos será el transformador, sobre que entra los 220 voltios va directamente al terminal que va al transformador que está afuera.

En la fuente switching lo primero que encontraremos será el rectificador.


### Lo más importante es saber hacer los dos pares
Después viene el **filtro** que es colocar el capacitor con mucho cuidado porque es polarizado.

Acá está la salida del capacitor, entonces agarramos el capacitor.

54 minutos.

Vamos a suponer que yo tengo un capacitor acá está la salida del capacitor. Entonces voy a agarrar el capacitor.

### En cualquier parte del conductor después de los diodos se puede poner el capacitor.

Entonces a partir de que yo puse el diodo en cualquiera de las partes de la salida ya es corriente continua pura, porque ya estará filtrada.

Antes de poner el capacitor tenía una corriente punzante, una vez que puse el capacitor tengo una corriente continua pura.

Así que si la fuente no me funciona muy bien y yo mido y está bien, seguro que el problema está en el capacitor, o sea que el **capacitor ya no filtra bien**.

Para saber eso se mide, o se cambia. Hay técnicos que toman la molestia de medir, hay técnicos que van cambiando.

Con el que por último yo me puse al día, tenía por costumbre tomar un capacitor y ponerlo en paralelo.

El profesor siempre mide nunca hace eso, si no anda cambio.

**Si sigue el problema dejo el nuevo y guardo el viejo**
Yo nunca le diré que esto está mal, si veo que están soldando invertido eso está mal.

### ¿Se puede medir en la placa o hay que sacarlo?
Hay veces que hay componentes que se pueden medir en la placa porque están en serie, pero cuando esos componentes están en paralelo suelen traer problemas (**suelen mentir**)

Hay que sacar 1 de los pines o sacarlo completo.

Depende de si está en paralelo o no, te va a mentir si es un valor muy bajo no, **pero si es una resistencia muy alta te va a mentir.**

La resistencia se puede medir donde está.


Ahora lo que si puedo decir es que cuando no mejora hay que cambiar los componentes, cuando medimos en **frío (sin poner en funcinamiento)** los componentes de electrónica tienen distorsiones. 
O sea cuando medimos en frío da **BIEN** pero cuando forzamos el trabajo comienza a funcionar mal.

Estos días pasó con una placa con un capacitor que NUNCA cambió, y el capacitor estaba en corto sobre un TRIAC. 

Lo hacía funcionar a un TRIAC como que recibía la señal el TRIAC, no es que el TRIAC recibía la señal, él ponía en directo el se hacía cargo de hacer funcionar el componente.

Pero cuando me dí cuenta cambié hasta el procesador pero igual no funcionaba.

Seguí el circuito y llegué a la conclusión que era el capacitor.

---

Hasta ahí la fuente.

Entonces yo había dicho que no tengo uno para 12 voltios tengo uno de 30 voltios.

**Qué voy a hacer?**

Vamos a suponer que este es el secundario del transformador, el primario vamos a obviarlo.

El transformador me da 30 voltios de corriente alterna. Necesito 12. Tengo que hacer caer esa tensión, hay reguladores de voltajes que le podemos colocar un regulador de voltaje de 12 voltios.

Ahora ya pusimos el capacitor y tenemos el rectificador, pero tenemos 30 voltios.

Hay un componente de 3 patitas que es un **regulador de voltaje**.

Que tendrá 1 entrada, 1 puesta a tierra, y 1 salida. 

El circuito por acá seguirá este está puesto a tierra, no seguirá nada.



Profesor hablando con un alumno:
Todos los 78xx son reguladores. Esos son componentes lógicos ya, ahí hay algunos de ellos si tenés un 0 sale 1. Si tenés un 1 sale 0. Son circuitos lógicos (xor, and, ) después hay otros que necesitás un 0 y un 1 para que salga un 1.

Nosotros vamos a tener la puesta a tierra, vamos a tener el ingreso, va a ingresar 30 voltios.
Y saldrá 12 voltios.

#### Donde mandamos eso? Si estamos en la placa? 

Este vendría a ser la salida del transformador si tuvieramos 12 voltios, pero tenemos 30 voltios, así que no le podemos dar ingreso al pin que está acá que viene del transformador para 12 voltios.

## Porque ingresa 15 voltios de corriente alterna, y sin embargo yo ya me tomé la molestia que entre este punto y tierra habrán 12 voltios de corriente directa, **entonces yo tengo que ver de colocarle estos 12 voltios adonde está el capacitor que filtraba la salida del transformador de 12 voltios ahí tenemos que soldar el positivo y el negativo. Hasta ahí tenemos que ir**.

Habíamos hecho un transformador que salía para 15 voltios que era para usar en 12, rectificamos y poníamos el filtro, ahí en ese filtro nosotros vamos a desconectar ese transformador y vamos a colocar este.

## **Ahí cortamos la pista**, para que se desconecte, porque no podemos colocar en otro sector.

#### A partir de ahí ya funciona todo
A partir de ahí ya hay reguladores de tensión para 9 voltios, para 5 para 3 voltios, de ahí para adelante.

Porque se rompió de ahí para atrás porque se había roto el transformador.


Yo no puedo bajar la tensión de 30 voltios a 15 voltios porque no puedo bajar la corriente alterna de esa forma, a no ser que haga cosa como esta: que haga una **capacitiva resistiva** pero para muchos es la peor fuente que existe porque es la **más insegura**.

### Nosotros tenemos que ir hasta el primer filtro que está después del puente rectificador

O sino podríamos agarrar el secundario del transformador pero corremos el riesgo de quemar la plaqueta.

# Eso fue importantísimo.

Podemos hacer un cargador de celular usando un transformador lineal. Para cargar un celular sólo necesitamos tener 5 voltios de corriente directa, con una batería de moto podés cargar el celular, lo que sí necesitás es el cablecito del celular.

**No hay nada que cargar en una batería lo único que hacemos es limpiar la placa o la "paste de iones".**

Esta es la parte más complicada, como se cambia un rulemán es fácil.

---

Ya sacamos la corriente continua punzante, **el negativo siempre va a tierra siempre va al chasis porque es el punto común de toda la placa.**

Cada capacitor va siempre al punto común, cualquiera de los capacitores que son polarizados.

O sea después hay una pista positiva para cada uno de ellos está el de 16 voltios, 10, 30 voltios pero el negativo de todos estos es el mismo: es el punto en común o el chasis o tierra.

O sea que yo una vez que busco el negativo de este capacitor, tengo el negativo de toda la placa: es el chasis, no hay 2 negativos en este sector.

O sea que vamos a suponer que tengo un componente X. Tiene positivo y negativo bueno a mi de la placa del procesador me va a llegar acá. Acá van a ver transistores, condensadores un montón de cosas.

Pero en el negativo va a existir siempre el chasis, acá voy a tener el relay. El relay tiene 5 pines.

Nosotros teníamos 3 puntitos arriba **el del medio puede ser la entrada de 220 como puede ser la salida de 220**.

Entonces hay veces que es normal que la entrada esté sola pero en más de una vez vamos a encontrar también en la salida porque es lo mismo. 

Tenemos un switching llave conmutador, tenemos una lámpara, tengo el NEUTRO, que le falta para que funcione? La fase. Entonces yo agarro la fase y le puedo dar el ingreso acá, entonces cuando yo cierro acá llega ahí, no quiero dar el ingreso ahí le quiero dar el ingreso acá. Le doy el ingreso acá y este que esta acá le mando acá. XDD

Con los relay pasa lo mismo por eso esta vez aclararle que la entrada puede estar por ese lado o no, pero siempre todas las teorías nos van a mostrar que se entra por acá pero puede entrar como salir.

Esto que está acá si o si es una bobina para crear un campo magnético. Que logramos con el campo magnético? **Mover**, el campo magnético mueve.

Vamos a suponer que tenemos un émbolo todo enrollamiento de alambre cuando le pongo una tensión eléctrica la bobina genera campo magnético y este magnetiza el hierro.

Cualquier metal ferroso que esté acá se pega, y yo el que se pegue puedo usarlo para que se abra o se cierre.

Vamos a suponer que tenemos acá la corriente, si acá abajo coloco así, vamos a suponer que viene a un foquito y este a otro foquito. Quiere decir que en estado de reposo uno de los dos estará perdido, vamos a suponer que en estado de reposo la corriente que viene de allá le pasa a este.


Entonces prendió este. Cuando yo le inyecto corriente acá en la bobina quiere decir que esto se inmanta y la chapa baja, al bajar la chapa acá deja de prender ese, porque no tiene más corriente y ahora prenderá este.

Entonces esto que esta acá representa a la bobina para crear el campo magnético en el relay, entonces yo voy a hacer otra representación acá. Lo haré así:

Abajo tengo 2 relay, acá tengo un 5 pines. En los dos de abajo tenemos NORMALMENTE CERRADO Y NORMALMENTE ABIERTO, que es como el primer dibujo que habíamos hecho en estado de reposo la corriente que entra entrará al ABIERTO, porque en reposo el otro esta cerrado.

**Los relay tiene 5 pines pero en muchas placas vamos a encontrar solo 4, el normalmente cerrado lo corta.**

#### Si entra la corriente el que esta cerrado queda abierto y el que está abierto queda cerrado

Hay relés que tienen 8 pines es así pero doble, 2 normal cerrado 2 normal abierto y 2 pines de la bobina.

Doble inversora y hasta triple inversora.

Por qué se llama inversora? Porque invierte.

--- 

Cuando compras relay solo hay de 5 no hay de 4 (podes cortar el normalmente cerrado)

El normalmente abierto funcionará cuando excite esta bobina con 12 voltios. Y este adonde va? A chasis a tierra.

Vamos a suponer que viene la orden desde el chip desde el procesador, viene que tiene que funcionar la electrobomba, entonces cuando activa quiere decir que la electrobomba estará conectado acá.

Con cuanta tensión trabaja la electrobomba? 220 de corriente alterna.

Este con cuanto trabaja? Con 12 voltios de corriente directa.

Ahora yo este voy a poner a tierra también, pero no puedo usar este símbolo de tierra porque es exclusivo para la **corriente continua**, pero voy a usar otro dibujo de tierra porque no me alcanza el dibujo.

O sea que dentro de la placa habrán circuito que traerrán la tierra de la CD y también habrán algunos circuitos, porque sino no puede funcionar o sea que dentro esta placa hay tierra en CC y hay pista en donde va la fase y el neutro.

No vayan a querer encontrar ese símbolo porque no hay es solo para los diagramas.

Hay veces que se hacen combinación de relay como este caso, para que el motor gire de 1 lado o del otro, entonces van a ver que en uno de esos diagramas el ingreso será otro y la salida será otra.

Por eso le digo que puede estar de 1 lado o del otro.


Pero cuando se explica casi siempre le dan el ingreso por el 1, pero yo le puedo dar la entrada por donde quiero, hagan memoria que esto es un **switch que será ordenado por medio de una señal electrónica, con una señal de 12 voltios arrancará un motor de 220**.


#### Vamos a suponer que la electrobomba no funciona, no me tira el agua.

Una de las primeras cosas que hago yo, me voy directamente al TRIAC. Vamos a suponer que tenemos un TRIAC,y voy a ir al relay a medir.

### Como se mide el relay?

Primero vamos a medir si tengo ohm, si no tengo ohm es porque se cortó la bobina de acá.
Tenés que medir la bobina del pin 2 y el 3.

Para que te sea más fácil siempre es así. 


Vamos a suponer que tiene número así será más fácil para comunicarme con ustedes.

Tenemos el 1, 2, 3, 4, 5.

Entre el 2 y el 3 hay una bobina: debe medir 16, 15 y algo.   

### Ustedes van a ver que a simple vista parece un relay y es un capacitor.

Siempre tiene que ser inmediato superior, el inmediato superior de 1,5 es 2.

Tiene que estar en verde.

El más chico está bien, debe dar 200.

## Tenemos que ir a 2. **El inmediato debe ser**, podés medir ahí pero te puede dar diferencia, en cambio ahí te dará exacta la escala.

# Al medir capacitor siempre hay que descargar

### Porque son capacitores que trabajan a 311 voltios.

¿Un caramelo quién quiere? XD

Esto que esta acá es un RELAY, similar a los demás, se usa generalmente para mucho más amperage que los chiquitos. Así que esto hay que medir como relay. Estos relay tiene la particularidad que esta bobinita sería el 2 y el 3 aunque dice que es el 1 y el 2. Y arriba muestra como si fuera un switching es decir que cuando yo excito ahí me tiene que dar acá.

O sea que uno de los pins están en común con uno de estos dos, y el otro también con uno de los dos.

Tiene común y el normal abierto arriba.
Por acá tiene que venir la fase del 220, y cuando ordena que arranque el motocompresor tiene que salir por acá. Entonces vamos a medir la bobina.

Porque sale por este cuando esta positivo viene del lado del rojo, cuando esta negativo viene del lado del negro, porque tiene oscilaciones la frecuencia alterna.

Quiere decir que yo acá debería tener cerca de 12 voltios de corriente continua.

Si queremos cargar un celular que le falta ? Reducir con qué? Con un regulador de voltaje (7812 es el código del reductor).

#### Los dos últimos números te dicen para cuantos voltios es.

7805 = saldrá 5 voltios y podemos cargar el celular.

Ponemos positivo negativo y cargamos el celular.


Lo peligroso del celular es que el cargador de celular tiene un circuito adentro controlador de carga, cuando el celular cada vez tiene menos carga le larga menos carga, cuando tiene la carga completa no le larga más carga.

No importa la entrada tengo que medir la salida.

La entrada al regulador de voltaje siempre tiene que ser mayor que 5, porque si la salida de tu transformador es 4 el no te eleva.

#### Regulador: el voltaje sobrante te manda a tierra, como puede ser una resistencia.

Las alarmas usas relé, las alarmas tienen una tierra hace pegar a l rele

Falta corriente alterna, grupo en serivicio, temperatura de radio, grupo en falla, batería baja, rectificador falla.

Cada vez que alguno de esos da falla te tira una tierra, esa tierra pega el relé y eso manda la señal en otro equipo al centro en buenos aires, lo manda a buenos aires por un equipo de comunicaciones que acepta entrada de alarmas.

Prendés la bobina conectado a tierra, no maneja mucha corriente es muy sencible. En donde van los relé son sócalos, tiene 4 inversores.

Por qué tiene tantos inversores? Porque se usan para varias cosas, por ejemplo prender una lámpara hacer sonar una chicharra y mandar la señal a un equipo de buenos aires, todo independiende y aislado por problemas de tierra y voltaje.

Uno maneja 220 otro 48, no me sirve porque la bobina es 48 voltios. En telefonía todo se usa continua 48 voltios que son 4 bobinas en serie.

---

Como todo motor el funcionamiento se debe a una parte muy importa que es el campo magnético que crea la bobina y la parte magnetizada que es el núcleo.


O sea que vamos a tener un núcleo que se llamará estator, por qué estator? Porque es la parte fija del motor


Luego tenemos otro componente que será el rotor, es rotor porque es la parte que girará dentro del estator.


#### El estator generará el campo magnético para que gire el rotor.

Por qué gira dentro del campo magnético? Porque si el rotor fuera una **chapa única no giraría**, porque no vamos a poder encontrar los polos nortes sur que varíen a cambios de la variación del estator.

Y por qué el estator si varia su polo norte y su polo sur, porque la corriente alterna es variable, cuando pasa del positivo al medio ciclo negativo, cambia su polaridad o sea que nosotros durante un determinado momento supongamos que tenemos bobinas, si tenemos bobinas en un determinado momento yo acá tengo el norte sur cuando cambia tengo acá el sur el norte, así constantemente.

Si fuera un motor sólo con 2 bobinas que se llama polo opuesto, norte sur sur norte, pero cuando tengo el radio es 1 y 1.

No es norte sur porque no tendríamos 2 nortes, entonces acá si es norte sur norte sur, sur norte sur norte, norte sur, constantemente cambiará.

A 50 veces por segundo, lo mismo que hace el transformador hace el motor exactamente lo mismo la electricidad a través de la bobina genera un campo magnético y ese campo magnético es variable porque la corriente es alterna.


Entonces como yo tengo un motor que es **jaula de ardilla** entonces las chapas de acero con sus aislante de aluminio están en diagonales, polos iguales se atraen y polos distintos se apelan.

Entonces cuando la bobina de acá magnetiza sur en este lado magnetizó norte, acá quedó el sur acá quedó el norte, acá quedó el norte acá quedó el sur.

Repelen y atraen y ahí comienza a girar, los motores hay **muchísimas clases de fabricación distintas de motores**, o


Los ventiladores en CC tienen imán permanente y rotor bobinado.
La bobina también es un imán cuando genera un campo magnético es un imán no es una bobina.

La bobina también genera un campo magnético pero la bobina necesita la tensión, y el imán da el campo magnético sin tensión.

El imán queda permanente pero varías la bobina, norte sur.


--- 

Este es un motor que tiene sus campos tiene varios campos, y también está puesto en jaula de ardilla, entonces este tipo de motor que es similar al del ventilador nosotros vamos a tener **dos bobinas para hacer funcionar el motor.** 

Vamos a tener 1 bobina de trabajo, y vamos a tener 1 bobina de arranque.

Esto también se puede representar como las dos bobinas, la de arranque y la de trabajo.

Son las dos bobinas que necesita ese motor para trabajar, muchas veces es el común de los motores necesita 2 bobinas: de arranque y de trabajo.

### Si es una bobina puramente de arranque, si o si necesitará algún tipo de dispositivo que corte cuando el motor arranque, no pueden quedar las dos porque son de diferentes velocidades.

Necesitaremos un componente que corte la bobina de arranque cuando la de trabajo ya rompió el torque de estar quieto.

Por lo general esos componentes se llaman **relay**, existen varios tipos de relay.

### Tipos de relay
1. Amperométricos
2. Volumétricos
3. Fuerza centrífuga son una especie de plaqueta acá iría una chapa y otra chapa y unos resortes.

Entonces cuando está en estado quieto este cierra y cuando el motor comienza a funcionar a mucha velocidad vence la fuerza del resorte y se abre el otro. NO es por ningún sistema eléctrico ni electrónico sino por fuerza centrífuga podemos ver esto **en las cortadoras de cesped**.

#### Relé amperométrico.
Entonces nosotros en algunos relay vamos a necesitar un cierto grado de consumo para que ese relay que está en estado de reposo cierre el circuito deje pasar la electricidad al arranque cuando llega a la velocidad deseada cae ese alto consumo entonces ese relay pierde fuerza y **desconecta**.


#### Relé voltaico.
Trabaja similar pero ya trabaja arrancando al revés de la amperométrica. No se da en el caso del ventilador. 

#### Son motores que necesitan bobinado de arranque como es el motor de la heladera, del freezer, en cambio del motor del split no tiene bobina de arranque.

El horno eléctrico los motorcitos que tienen la mayoría son paso a paso.

Acá voy a tener el bobinado de arranque y acá voy a tener el de trabajo, entonces si esto fuera un motor este sería el punto en común, es decir que si yo le pongo fase o neutro, llega ahí y en los extremos si le puse fase tendré fase, si le pongo neutro voy a tener neutro.

Para hacer funcionar esto yo tengo que determinar si es un motor **con bobina de arranque o con bobina auxiliar** , el split no tiene bobina de arranque como la heladera, quiere decir que las dos bobinas trabajan a la vez, exactamente pasa lo mismo con el motor del ventilador. 

Entonces en los diagramas que aparece como arranque léanlo como **auxiliar o secundario**, porque no vamos a encontrar en el ventilador ningún elemento que sea capaz de cortar la bobina. Esta bobina funciona con esta, o sea que esta y esta me dará el punto en común y ahora viene el ventilador que van a trabajar las **dos bobinas juntas**, la corriente la fase la tensión y el amperage van en la misma frecuencia, vamos a suponer que este es la cresta de la tensión y el voltaje, y en valor acá esta el amperage si bien en amplitud es más pequeño el amper que el voltaje pero siempre van en la misma frecuencia, van juntos. 

#### Cuando ponemos 2 bobinas en paralelo esto se rompe porque se va a levantar, queda desfasado y esto provoca un mayor consumo un exceso de calentamiento y ese exceso hace que el esmalte de la bobina comience a despegarse y empiece a caer en cortocircuito y lo que todos decimos se quemó
Hay que corregir esto, y a eso se llama **corrección de factor de potencia**, porque esto trae un exceso de consumo, a lo mejor yo voy a estar usando 10k kilowatts y voy a pagar 17k kilowatts estará consumiendo más entonces hay que corregir el factor de potencia y esto se hace con un capacitor.

El error de una inductancia se corrige con una capacitancia   
El error de una capacitancia se corrige con una inductancia

### Por eso hay fuentes que son un poco más complicadas y vamos a ver que hay una especie de bobina que está en paralelo porque se usa para corregir el factor de potencia que está teniendo de más la placa entonces corrigiendo esos factores de potencia tenemos un consumo más o menos verdadero.

Igual se pierde pero no es tan significativo.

Si yo pago 10k kilwatts, no quiero pagar 10k kilowatts y tengo que pagar por 17k kilowats, se busca el 1 por 1 pero no se logra. Se llega al 1.93 1.97 por ahí se anda. 

Por eso no es conveniente modificar los microfaradios de los capacitores, ya está calculado por ingenieros pero se da que **venía con una capacidad de microfaradios que no era el indicado, modificaban el capacitor y andaba bien**, es posible que se calculo para 60 ciclos entonces en 50 ciclos ese capacitor queda chico entonces hay que elevar un poquito el capacitor.

Pero si el que le tira el dato es uno que se da de técnico presten atención, ahora si te da el dato uno que está en eso y te tira de buena onda yo le creo.

### Como saber si ese dato es bueno o no?
Tenés que medir el amperage.

Si un ventilador me tira 10 amper y lo modifico y me tira 8 amper, está mucho mejor, porque no hay forma de reducir el factor de potencia que no sea el ideal, porque si yo me excedo igual tendré exceso de consumo porque quiere decir que esta bobina disparó a una velocidad que supera a la bobina principal, porque puedo decir que este tiene que tener 1000 revoluciones por minuto pero si tengo falta de capacitor voy a andar a 1200 si yo tengo por capacitor excesivo voy a superar pero ocasionaré una sobrecarga entonces voy a tener más amper de consumo.

Cuesta saber el verdadero valor, traten de tener algún alargue apropiado.


Vamos a suponer que tengo fase y neutro para probar el motor y si es muy chico el amperage hagan esto pelen acá y pelen acá.

Un secreto cuando uses trincheta yo acostumbro a forzarle el trompito una vez que apoyo ella sóla vuelve al lugar y me facilita el trabajo, porque sino tendríamos que estar haciendo.


### La bobina se puede probar con un foco en serie. NO es como la bobina del relé que te da 2000 ohm.

Entonces yo tengo hecho acá una bobina, y una bobina crea campo magnético entonces si acá a mi me tiene que medir medio amper, con todo esto me dará 5 6 amper.

Si estamos haciendo esto y el resultado es poco, tengo que poner solo en 1 no en dos porque hago cortocircuito y acá si irán las 2 partes del motor, entonces acá pondríamos la pinza amperométrica y ahí medirá en vez de 0,1 a lo mejor medirá 10 15 20 amper lo que sea.

Podemos poner 1 capacitor y miran que amperage le da, ponemos el otro capacitor y medimos entonces está bien lo que dijo el técnico.

### Lo que hay que lograr es el menor consumo.
Cuando está mal se excede el consumo.

En vez de 2,1 me va a marcar 21 22 y me va a hacer más fácil de medir. Todo depende de la cantidad de vueltas que tenga.

Entonces nosotros lo que hacemos con los capacitores en los ventiladores, sirven para corregir **el factor de potencia**, el desfasage que hay entre un campo inductivo que se genera acá porque se generan 2 campos inductivos uno con este y con este, entonces yo tengo que corregirle a este fijense que cuando se va a colocar el capacitor vamos a suponer que yo aca coloco lafase y ahora colocaré el neutro para que esto ande tengo que poner el neutro en los dos pero voy a provocar un desfasage porque no tengo, si yo tengo un relay que corta entonces sí es una **bobina de arranque** porque arranque una vez que tomó velocidad y que el consumo cayó queda sólo el trabajo.

Pero este es un caso que las dos bobinas trabajan entonces yo tengo que corregir el factor de potencia.

# Está mal dicho bobina de arranque y de trabajo en el caso del ventilador porque ambas trabajan en paralelo???

Yo tengo que corregir el factor de potencia entonces voy a poner el capacitor acá.

Motor y los dos cables, hay 2 bobinados pero tengo 3 cables porque adentro del motor las dos bobinas están en un 1 punto en común, vamos a tratar de poner este en común. 

Entonces vamos a suponer que este en común, vamos a poner que este es de trabajo y este es de arranque, como sabemos quién es quien? **Medimos**.

### Cual de acá es de trabajo y cual es de arranque?
El de afuera es el de trabajo y el de adentro es el de arranque.

En los bobinados siempre cuando miramos el bobinado veremos 2 tipos de bobinado, el que está de afuera es el trabajo y la de arranque es la que está dentro.

Pusimos las dos bobinas en común unimos, las dos.

Ahora vamos a poner el de arranque y vamos a poner el de trabajo.


Entonces nosotros tenemos un capacitor que tiene 2 pines, entonces yo voy a tener la fase y el neutro y acá va a estar mi fuente.

Entonces que hice acá yo? A 1 lo mandé directamente al común, vamos a suponer que uso un switch y le mando acá, ahora yo tengo que poner un neutro a estos dos para que funcione porque los 2 ya tienen fase, si agarro un buscapolo me va a prender .


02:19:00

#### Si yo coloco el neutro debería funcionar pero el neutro del trabajo va directo en cambio el neutro de arranque debe ir al capacitor pero con la misma polaridad con la que polaricé el trabajo. No puedo usar esta otra polaridad, no la uso. 
# Para el extremo de esta bobina tengo que usar la misma polaridad porque los dos tienen la polaridad hasta acá, yo del neutro alimento el capacitor y de la salida del capacitor alimento el arranque.

Ahora si me decís que leíste en un libro que acá iba el neutro vamos a respetar tu libro, no hay problema.


Porque es corriente alterna, si yo tengo un switch a mi siempre me gusta que corte la fase.

02:20

Incluso hay muchos problemas que a veces se dan en los electrodomésticos electrónicos y es porque queda el chasis en vivo y no en tierra, el neutro no va a tierra sino que la fase va a tierra y eso provoca ciclos magnetismo, hay que invertir el toma para que quede bien.


#### Como cambia de velocidad el ventilador eléctricamente?

Con el bobinado. Quiere decir que lo que yo pongo acá yo puedo distribuir en cualquiera de estos puntos si estoy acá no va a salir para ningún lado el ventilador está apagado. A medida que voy seleccionando quiere decir que cada uno de estos es una salida, pero el selector no hace nada.

## Entonces los ventiladores de techo no, los de pie sí. 

Los de pie tienen una bobina que no se usa como inducida son bobinas que provocan inducción, estas no se usan para eso, se usan para la impedancia porque los conductores tienen caída de tensión tiene resistencia, es tan largo que es considerable la caída de tensión que hay.

En el ventilador de techo ponen la reactancia o una bobina en serie.

### Tengo que colocar cual capacitor?

Esta es una de las conexiones para 1 ventilador, luego traeré las otras formas que se puede conectar.

## El de techo no tiene bobina de impedancia por eso trae la llave de afuera, primeramente venía una cajita que iba al colector que tenía 3 conexiones, y ahí está el bobinado.

Entonces cuando ustedes le colocan uno de estos, lo único que no hay que hacer es colocar la entrada acá, vamos a suponer que acá está el motor del ventilador, entonces vamos a suponer que tengo la fase, y viene acá al selector, vamos a suponer que acá arriba del selector que tengo la carcasa plática, 0 2 3 y 1 : lo que no hay que hacer es esto: le podemos dar ingreso acá en este como en el otro no hay problema , **porque es solo una bobina para la impedancia**, en el medio no se puede porque es la velocidad 1 y la velocidad 2, quiere decir que vamos a suponer que de acá a acá está el enrollamiento de alambre y sigue este enrollamiento de alambre y ahí tengo los 3 lugares, porque si yo coloco acá voy a tener 1 velocidades: la máxima .


Supongamos que la corriente entró por acá, entonces quiere decir que esta de acá es la velocidad más alta, después tenemos la velocidad 2 y la velocidad 1, entonces quiere decir que esta que está acá es la 2, y esta que está acá es la 1. De acá a acá tengo una impedancia que sea 11, acá voy a tener 22.

Voy a tener más impedancia, 1 es la velocidad más baja, 3 la más alta.

La velocidad más alta está directo. 

### Lo único que no hay que hacer es poner en el medio.
Si ponés la 3 la más alta o la 1 la más alta, es cuestión de número nada más.


## Esto es un selector a impedancia.
Hay otros que son electrónicos, se está dejando de usar el selector a impedancia. 

NO es que sea malo, pero te venden el otro.

Vos no tenés impedancia
Si vos comprás esa cajita de impedancia quiere decir que esa conexión que tenés hecha la tenés acá.

#### Vamos a suponer que les traen el ventilador desarmado, o ustedes quieren saber si está bien o no.

Hay que sacar las tapitas. Las tapitas son cilíndricas

Vamos a suponer que tenemos 6 cables. 

### Cuál es cual?
Los colores no importan porque desde que llegaron los chinos ponen cualquier color.

Negro, marrón, rojo, blanco, azul, gris.

Tenemos que medir la impedancia de los cables: vamos a medir el negro con el marrón voy a medir con el rojo, con el azul, con el gris, con el blanco.

Luego tenemos que medir el marrón con rojo, con azul, con gris, blanco.

Luego tenemos que medir el rojo con azul, gris, blanco.

Luego tenemos que medir el azul con gris, blanco.

Luego tenemos que medir el gris con blanco.

### De las medidas que obtengamos nos darán 2 valores altos y de esos dos valores altos
Negro marrón rojo seguiría el 03 que es naranja, el 04 que es amarillo, el 05 que es verde, después el 06 

Puedo poner el 04, pero no así, significa que si son los cables blancos y el terminal es rojo entonces yo l....(inaudible 02:38:36) significa que no hay cable.

07 es el violeta.

## El valor mayor corresponde al arranque. El que le sigue es la del trabajo y las otras 2 son de impedancia.

Vamos a suponer que te da 22 ohm, 11 ohm, 6 ohm o 5/6 ohm.

Te va a dar muchísimas medidas hasta que te acostumbres, van a ver que hay colores que se repiten en las medidas.

### Las medidas parecidas son las impedancias. Vamos a suponer que son 33 las dos (no es arranque son impedancia)
Todo depende del que hizo el bobinado para que hizo porque puede ser tanto motores ventilador como otra cosa que se usa como impedancia.

Si tenés un fusible adentro y tenés 1 fusible de capacitor y el otro va a estar en común con otro bobinado, porque acordate que nosotros tenemos la fase el neutro y el neutro estará acá sin, entonces vamos a suponer que acá hay 1 cable y acá hay 1 cable y este cable estará en común con ese acá y de acá va a tomar el capacitor entonces acá tenés 2 cables. Si tocás acá y acá te dará 0.

### Vamos a suponer que negro con azul te dará 0 ohm porque pasó eso.

Blanco con rojo te dará 0, porque ahí está puesto el **fusible**.

Cuando vos cortás acá y acá te va a dar 0 porque **ES EL MISMO CABLE**. Y si no tiene fusible no pasa eso porque **NO TENÉS ESE CABLE**.

Negro con azul 0 ohm porque pasó esto, o a lo mejor te va a dar blanco con rojo te va a dar 0 porque ahí está puesto el fusible.

Y si no tiene fusible no pasa eso porque no vas a tener **ese cable**.


### Fusible corta por corto circuito y por la temperatura

Quién entra al selector? La fase, y el neutro sigue de largo solo al negro, quiere decir que hay alguno de estos colores que me tienen que dar en común con el negro.

Vamos a suponer que el negro llegó hasta acá me tiene que dar en común con el capacitor y es posible que de acá también deba salir un fusible.

Quiere decir que alguno de estos cables tiene que ir al fusible pasar y volver el tiene que ir al capacitor.

#### Como sabés si tiene fusible?
Por la cantidad de cables, si te da común es porque está el fusible ahí.

Puede venir blanco como puede venir cualquier color.

Está puede entrar un naranja o un azul, como puede ser todos **BLANCOS**.

### Como haríamos ahí? Vamos marcando los cablecitos con algo
Yo recomiendo la cinta de papel papel de enmascarar, ponemos 1,2,3,4,... o A,B,C,D,... de seguido porque son todos blanco.

Cualquier cosa que vayan a desarmar identifiquen, acá podemos poner A y del otro lado A por más que sea blanco o negro será A con A, después del otro lado será B con B.

Entonces el chico llegó a tirar allá no importa, a lo mejor puede caer 1 papelito o 2, lo otro razonando se consigue.


Estos capacitores no son polarizados porque son para CA.

Hay muchos de estos que vienen uno negro y uno rojo, no le hagan caso al color.


NO SON POLARIZADOS.

Si se cagó el fusible es delicado, porque el cable del ventilador son muy finitos.

Entonces vos tenés que sacar lo que está bien escondido, no todos los ventiladores traen fusible como no todas las planchas trae.

### Se le puede hacer un puente al fusible
Pero tenés que tener cuidado porque de un lado va agarrado al filamento del alambre del bobinado y tenés que tener cuidado ahí. Es un peligro, es delicado.

Muchas veces que terminan el bobinado, el fusible se pone antes de atar.

Una vez que se pone eso, ahí va el barniz, lo mejor que hay es una herramienta plástica para que no pele el bobinado, porque tenés que ir abriendo el bobinado hasta encontrar el fusible y sacarle el fusible.

### Si el fusible es de aluminio ni toques.
No tiene más solución.

Alumno: Hay algunos fusibles para un cambiazo rápido que los "destornillás" como en un equipo de música.
Profesor: Claro, pero este fusible es térmico, si el bobinado calienta demasiado porque se ensució o porque el capacitor no anda, **siempre se corta**.

Vamos a medir como si tuviéramos haciendo una continuidad. 

La fase de acá con quién tiene que darme? Con el marrón. 

### Cual es marrón? Este XD. La fase siempre tiene que estar a la derecha. A la izquierda siempre neutro.
Si enchufo me queda en el lado derecho.

## Profesor: "Muchísimas veces en ventiladores nuevos yo encontré que la fase de acá es el neutro de acá"
Hay que cambiarlo, los chinos hacen cualquier cosa.

Este respetó el azul está en neutro.

### Ahora tengo que medir el marrón como lo mido? **Vamos a ir jugando con el selector.**
Si me da continuidad quiere decir que no hay problemas de que el cable esté cortado en ningún lado.

Y que por lo menos acá me está funcionando, a lo mejor tengo problemas en las demás velocidades pero esa velocidad si funciona.

#### O sea tengo en buenas condiciones el neutro y tengo salida del selector en la fase, o sea que eso debería funcionar.

Guardamos el tester y probaremos el funcionamiento, **CON UNA SERIE**.

Hay que tocar el motor con la mano invertida por si las dudas te patea.

#### Adonde coloco la pinza amperométrica? 
En 1 no se puede, en la fase no se puede porque es muy corto muy chico. Entonces iré al neutro en la parte en donde está el negro.

### No mide nada. 
El buscapolo no sirve, necesitamos la pinza amperométrica. A esta pinza amperometrica no le **creo mucho porque es de rango extendido**.

Ahí no anda, no hay 1 triste consumo acá puede ser **problema del cable a lo mejor no llega el neutro pero si la fase, vamos a tener que usar el multímetro en corriente alterna**.

¿Este símbolo que es?
Sube y baja: corriente alterna.

Cuántos voltios vamos a medir acá? Más de 220. 750 

Si el tester tiene 500 iríamos al 500.

Vamos a cambiar las pinzas porque está hecha mierda esa que trajiste.

Acá nosotros tenemos electricidad directa, vamos a mirar de nuevo estamos bien, estamos en la esala que corresponde, esta vez mido yo después vos, Voy a colocar en el neutro porque yo sé que es buenito y luego iré al **violento** XD.


Puede ser que esté cortado el neutro, pero te dió continuidad pero aparentemente tiene porque le marca la fase (no sabían si andaba el enchufe).

En la hora 02:59 se estaban fijando por qué no funcionaba el enchufe.

#### Conectá y estate atento por si chispea.

Yo tengo fase y neutro y quiero saber cual es está cortada, me tiene que dar si el neutro está bien me tiene que dar los 220, porque tengo la fase que le estoy mandando al tester y tengo que tener el neutro.

Ahí no tengo el neutro, pero acá si porque estaba invertido, entonces quiere decir que el neutro tengo, **ahora mediremos la fase**, ahora busco la fase, tengo acá la fase y busco el neutro.

Por qué me da 192 ahí?

Mirá ahí me da los 220 y esta es mi fase, o sea que este rojo es neutro.

Yo mido acá y no me da nada porque este es neutro y el otro es neutro, yo tengo acá la fase, tengo donde tendría que tener neutro y me marca 190.

Y me da 185 por qué pasa eso?

Porque la bobina está cerrado, la caída de tensión que tengo es por la impedancia de la bobina, o sea que la bobina está bien.

Ahí me da con la fase que comprobé con el busca polo los 220 de voltios.

#### Será que el cable está cortado?

Tengo la fase 220, tengo neutro con la fase. 

### Estaba cortado el fusible.

Alumno: Para medir resistencia en serie no me va a querer por el tema del foco, pasará la corriente más alta o algo así?  Para medir resistencia (continuidad), ¿no afecta por el tema del foco?

Profesor: No, lo bueno de esto es que si acá hago un corto prende la lámpara no vuela, va a prender únicamente si está en corto.

Pongo así porque poner acá suelto es un peligro, siempre vamos a tener que buscar algo que esté aislante para poder apoyar sin necesidad que haya un corto.

### Cuando vos tenés dos y hiciste la serie, yo uso dos tomas, hay algunos que le ponen un porta lámpara, porque si yo quiero usar este mismo como alargue y no como serie, yo le hago el corto y ya me queda con alargue.

## Yo le hago un corto y lo puedo usar como alargue, tendré 220 directo sin serie.

Ahora vamos a tener que romper el precinto de la bobina para saber cuál es el fusible, está muy duro el barniz que le pusieron,

Alumno: ¿cuándo le cambiamos el térmico se puede poner otra cosa?
Profesor: ...No contestó.

### Siempre está ahí en el bobinado, no al lado porque tiene que medir la temperatura del bobinado.

Acá está suelto un pelito de la bobina, ese es el fusible.


### Está bien el fusible, acá hay un cable suelto.

A mi se me hace que es el fusible, acá la posibilidad que habría es levantar con paciencia todo, y achicar esto pelar acá y soldar del otro lado porque acá son dos patitas acá hay un alambre y acá está el otro y hay que soldarle sobre el otro. Porque esto no tendría que venir hasta ahí, pero es posible que esto salga de ahí y la otra parte está en otro lado, o sea que este a lo mejor está soldado contra la pata. 

Ahora vamos a medir la otra bobina y no era.

O sea que ese es el problema? No. O sea ese es el problema pero tenes que encontrar la otra parte que está de este lado de la bobina, **porque en el fusible está soldado lo que se soltó del otro lado de la bobina**. Un cablecito dentro del bobinado se soltó.

### Como medir cuando la bobina está quemada?
Lo que pasa es que es más fácil cortar todos los cables, pero no quiero hacer esto porque no es práctico.

### Decile que está cortada la bobina, no está quemada pero está cortada.
