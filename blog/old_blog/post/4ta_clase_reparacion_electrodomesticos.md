---
title: "[AUDIO][APUNTE] Taller reparacion de electrodometicos (Clase 4) - Capacitores, Transformadores - Fuente lineal, switching o conmutada, y capacitiva. Rectificador onda completa. Núcleo ferrita, núcleo hierro."
date: 2024-07-26T04:31:20-03:00
tags: ['electrodomesticos']
---
## Audio de la clase:
https://youtu.be/OSlqnhmQsMQ

https://vocaroo.com/1dD9MmKu95UO

O miralo desde una instancia de invidious https://redirect.invidious.io/watch?v=OSlqnhmQsMQ


**Para que sirve el siguiente elemento:**
![elemento extraño](/img/4ta_clase_electrodomesticos/elemento.jpg)

![capator](/img/4ta_clase_electrodomesticos/capacitor.jpg)
![diferentes capacitores](/img/4ta_clase_electrodomesticos/capacitores2.jpg)
![dibujo pizarrón](/img/4ta_clase_electrodomesticos/pizarron.jpg)
![taladro](/img/4ta_clase_electrodomesticos/taladro.jpg)

Al no tener osciloscopio creo ese elemento y medir los pulsos de la fuente switching es difícil porque es muy alta, tampoco se puede medir con tester porque te quemará el tester y es necesario saber si está funcionando la fuente o no. Si está funcionando hasta antes del transformador el oscilor, si le pongo eso, como eso es un foco de neon entonces sí titila, NO puedo contar la frecuencia, pero por lo menos me da un acercamiento de que está funcionando hasta ahí, entonces ahí si yo puedo decir, el transformador es el que está mal. Sin eso no puedo saber si es el transformador o la fuente. 
**El tester quema porque no tiene alta frecuencia para medir transformadores de alta frecuencia**
Todo viene sin la batería la pinza, el tester y el buscapolo.
Buscapolo digital es mejor porque se puede decir si es una descarga directa o si es una corriente de inducción. Aparte es mejor porque el analógico hace una lucesita y no se ve a la luz del sol.

Este capacitor se lo llaman doble, los demas son capacitores simples.
Todos son genéricos hay 1 que es distinto.

Todos son capacitores para la bobina de trabajo de los aires acondicionados, hay capacitores de 50 microfaradios, 45 microfaradios, 35 microfaradios.
Muchas veces cuando nosotros vemos capacitores el tamaño puede llegar ser una orientación.
##### NO hay que confiarse en los tamaños de los capacitores
Medir capacitores no sirve porque tenés que saber si está bueno, porque podemos medir y nos da 65 microfaradios y en realidad es de 90 microfaradios, no va a funcionar por más que vos necesites usar uno de 65 está malo.

###### Hay capacitores no polarizados y polarizados.
Si nosotros colocamos un inverso el positivo en la conexión negativa también explota. Sólo se puede colocar en esa polaridad, no podemos invertir cruzando polo, tampoco podemos colocar en corriente alterna porque explota. **Cuando no es polarizado es para corriente alterna.**

**Casi siempre: viene polarizado del lado del pin negativo.**
Si trabajos con placa, vamos a ver algunos capacitores que viene polarizado en el lado positivo, siempre polaricen solo 1 lado. 

Agregar foto capacitores.

Los capacitores siempre tienen 2 medidas, una en microfaradios y otra en voltios. Los capacitores siempre se cargan al valor pico de la corriente. 

### Por qué ahora no se puede mentir mas en el consumo eléctrico?  
Ahora son medidores digitales y no se puede falsear.   
### Como hacen para mentir en el consumo?   
Desconectaban un puente.   
Si te descubrían te sacaban el medidor y te cobraban lo que gastabas siempre.

#### Consejo: de donde vos comés no podés enseñar, porque entre vos y yo hay una mínima diferencia y es ese pequeño tip que te hace distinto a los demás.
Hay que ser respetuoso con el cliente. Hay que cuidar mucho la imágen.

#### La parte más difícil: el manejo de la electricidad. 
Siempre vamos a encontrar electromagnetismo. 
Entonces:    
Transformador, bobina primaria, núcleo de hierro.   
Transformador, bobina secundaria.    

Con corriente continua no se puede hacer trabajar un transformador, porque tiene que haber variación del campo magnético.
Si no hay variación del campo magnético sólo creamos un electroimán.

Corriente directa = corriente continua
Si yo tengo una batería de 9 voltios y la quiero llevar a 12 voltios, NO SE PUEDE.
En realidad si se puede pero de otra forma.
En forma directa no se puede porque no tengo variación de campo magnético, necesito una corriente alterna, que tenga positivo y negativo y que sea una variación constante. Cada vez que nosotros tenemos una variación de corriente positiva y negativa, vamos a tener una variacion de polo norte y polo sur, porque al ser de hierro al pasar un campo magnético y que yo hago una bobina para sumar fuerza magnética entonces en algun momento el campo magnetico va a salir de un salo y va a entrar y va a quedar magnetizado, cuando cambia la corriente.

Agregar foto como se mueve la energía.

Si un lado era polo norte y polo sur, ahora es al revés, gracias a la variación de la corriente alterna. En el otro ciclo es al revés y en el otro ciclo al revés, constantemente siempre los polos son opuestos.

Cuando un imán se rompe, no se puede unir, quedaron 2 imanes. 
Es decir para juntar monedas del piso si puedo unir pero para **GENERAR UN CAMPO MAGNÉTICO** NO, ya no sirve.

Cuando la corriente empieza de 0, nunca se puede saber cuando la corriente empieza porque el generador queda ahí.
Cuando comienza la funcion de esa energía es formar un campo magnético para imantar el hierro.

El campo magnético sale para todos lados, pero para los estudios se hace para el lado que se quiere fundamentar el trabajo.

Cuando se crea el medio ciclo se va a generar un campo magnético.
Si tocamos el transformador está imantado.

Agregar foto de líneas de fuerzas.

Vamos a suponer que tenemos norte y que tenemos sur.
Ahora la corriente alterna empezó en el medio ciclo negativo 

En el 1er ciclo se imantó el hierro, cuando empezó a armarse el 2do ciclo entonces ese campo magnético al perder fuerza el generador ellos vuelvan, a medida que uno pierde fuerza otro vuelve.

Si nosotros en la entrada tenemos corriente alterna entonces en el secundario también vamos a tener corriente alterna. La diferencia puede ser el voltaje. 

El neutro de la corriente alterna es el mismo valor que la tierra.  
En cambio el negativo no, el positivo no.

El negativo en una batería no es lo mismo que tierra, porque no hay forma que yo pueda cerrar un circuito de la batería con tierra. Si agarro el positivo de la batería y coloco una lamparita y lo pongo a tierra nunca va a prender. 

Si yo agarro la corriente alterna fase y neutro pongo un foco, enciende.
Si yo agarro la corriente alterna fase y al neutro lo pongo a tierra, enciende.

Así muchos roban la luz (con el medidor viejo, el nuevo ya no XD).

Si nosotros conectamos así una heladera (usando la tierra como neutro), la tensión baja.
Pongo una heladera y conecto el neutro a tierra y el motor se siente que pistonea, ¿por qué me falta energía? Porque está mal echa la tierra, para la tierra se necesita que el suelo sea bastante húmedo y que tenga sal.

La electricidad siempre va por el lugar en donde tenga menos resistencia.
Cuando clavamos la lanza para tierra para resguardo nuestro, en cualquier lugar la tierra seca que no pasa nada, algo de tierra tiene pero igual vamos a sentir un sacudón fuerte. Porque la electricidad siempre va por el lugar en donde tiene menos resistencia, tanto la jabalina que está en la tierra como yo tenemos la mismo tierra seca, así que a la energía le da lo mismo pasar por mí o por la jabalina, pero si la jabalina está bien hecha, la corriente se irá por la jabalina y yo voy a sentir un cosquilleo.

##### Instalación de una jabalina a tierra:
https://m.youtube.com/watch?v=OsNM_0ogp3Y    


Algunas personas pueden intentar utilizar la jabalina a tierra para manipular el sistema eléctrico y así reducir costos en su factura de electricidad, como reemplazar el neutro por tierra. 


#### Tierra = neutro (tierra buena)
Nunca podemos comparar la corriente continua con tierra.
Cuando nos dicen que el chasis es vivo de la corriente alterna, es porque pusieron el neutro al chasis.
Pero cuando pusieron la fase al chasis y quedó vivo, en que manera yo agarro y me equivoco en la batería y coloco el positivo al chasis del auto y muchas cosas voy a quemar del auto porque está hecho para que no tenga chasis vivo.
En un trabajo de laboratorio es lo mismo corremos alto riesgo de que cuando esté el chasis a vivo se queme pero en cambio si yo tengo el transformador 1 por 1 220 y 220 del otro lado, yo tengo aislado, nunca voy a tener la misma tierra que tengo acá en la parte primaria. Y eso se llama **aislación galbánica**.
Si hacés un corto circuito siempre se quema el primario. Microondas me da 2000 voltios a la salida.
En un transformador siempre se quema el primario porque la exigencia del consumo la sobre el primario.

Potencia = tensión por intensidad

Los capacitores de color negro se usan para el arranque del motor.
El relay elimina la bobina de arranque.

#### Hora del audio: 01:06:15

Está mal decir **cargador** de batería.
Nosotros decimos que se descarga porque para que exista una cierta cantidad de carga en la batería debe haber una diferencia de potencial. Si nosotros decimos que la batería tiene 5 voltios es porque del borner negativo al positivo hay 5 voltios de diferencias, la diferencia de potencial que hay. Pero cuando esos potenciales se van igualando se van perdiendo a 0. 
Está mal decir se **descarga** la batería, porque los que están en el movimiento los que nos da ese movimiento para poder medir esa cantidad de potencian serían los electrones, eso ocurre porque la placa positiva debe medir cierta cantidad de agujeros y la placa negativa debe medir tanta cantidad de electrones para que exista esa fuerza de potencial, pero si esos electrones cuando hacen el recorrido por el trabajo vuelven a la placa y en lugar de pasar por el ácido (que es neutro) a la placa negativa, se va quedando durmiendo en la placa positiva que ya no tiene más fuerza como para sacarse de encima esos electrones esos electrones quedan pegados ahí XD entonces se van igualando las dos placas, las dos placas son tan positivos y tan negativos que van perdiendo el voltaje. 

Entonces cuando nosotros ponemos a cargar NO hay una carga, lo que hacemos es limpiar la placa positiva le sacamos todos los electrones y le mandamos todos esos electrones a la placa negativa en donde debe estar y quedó con ese agujero por falta de electrones.

220 voltios es el valor eficaz, si cargamos un capacitor nos va a dar 320 voltios porque se carga el valor pico.


Nosotros debemos procesar la electricidad para que a nuestro chip le llegue los 3 voltios. Puede valer hasta 9 voltios el chip.

#### Por qué necesitamos en el chip 3 voltios?
Necesita una activación para que el chip funcione.

Estos chips se lo pueden llamar junta, procesador, y su función es recibir la órden. Una de las fallas que puede tener nuestra placa es que el chip no tenga corriente.

Deberíamos ir a un datasheet para ver en cual de las patitas le entra el voltaje de la alimentación positiva y negativa porque con sólo la alimentación positiva sólo no puede porque necesita una diferencia de potencial, porque si no tengo un valor de tierra no voy a poder llegar a los 3 voltios que se necesita. Cuando está muerto una de las posibilidades que tenemos es verificar si le está llegando los 3 voltios al chip, puede haber una bobina quemana, un transistor, resistencia, diodos quemados o la pista quebrada. Habría que buscar un microescopio para identificar donde está rota la pista.

Necesitamos una energía para poner en funcionamiento al chip.

#### Lavarropas: consulta.
Alumno: "Me compré un lavarropas nuevo pero recuerdo el lavarropas viejo no sé como se llama el dial ese, vos le ponés y va volviendo"
Profesor: Esos son selectores mecánico, voltaíco mecánico
Alumno: Pero este lavarropas no vuelve es un dream, es correcto el funcionamiento?
Profesor: Sí, porque es electrónico.

Cuando hablemos de un lavarropas voy a explicar las dos puntas de un lavarropa.

Nosotros agarramos el selector de la lavadora la que es con placa.

La lavadora tiene placa y tiene memoria, tiene un programador. Hasta ahí la placa no se enteró de nada, cuando ponemos que funcione ahí recién leerá lo que escribimos.

Para que el chip funcione tenemos que llegar a 3 voltios y tiene que ser corriente directa. Hay chips que incluso hasta las frecuencias parásitas que hay en el aire le afecta, son chips muy sensibles.


Para medir el capacitor, el capacitor tiene que estar totalmente descargado, para que recién puedas medirlo.
Para descargarlo hay que puentearlo.

La única forma que puede trabajar en esa escala es la de alto rango.

Nosotros vamos a tener como puente, 220 voltios de corriente de alterna, no nos sirve para nada. NO nos sirve ni como corriente alterna ni como 220 voltios.

Tenemos que llevar esa corriente alterna que tiene unos ciclos variantes a una corriente lineal directa. 

Componentes de la electrónica:
1. resistencia, como sabemos si es una resistencia? Siempre va a estar el símbolo de ohm al lado:  Si me ponen 2k vale 2000 ohms.
2. capacitor: **no polarizado** o **polarizado sólo es para corriente continua y no puede estar conectado de forma inversa**.
3. bobinas: algunas se llaman toloide, bobinas muy parecidas a las resistencias.
**¿Cómo nos damos cuenta si es resistencia o si es bobina en placa?**
Porque siempre hay una letra R, en un lado aparecerá el símbolo de ohm y en el otro lado aparecerá el símbolo de faradeos.

Si es una resistencia en lugar de tener una R o venga con el número del valor de la resistencia, vendrá con una letra L.  

**Es difícil que les venga con el valor de la L.**
La L es inductancia (hace referencia a la bobina).


4. Diodos: hay muchísimos para diferentes tipos de trabajos. **Diodo rectificador**: nos sirve para rectificar la corriente alterna y pasarla a corriente continua. Tiene nombre sus terminales: **ánodo y cátodo**.
#### El diodo permite el paso de la electricidad para 1 sólo lado.  
En realidad toda electricidad pasa pero como es corriente alterna cuando viene el ciclo negativo no pasa o al revés cuando viene el positivo no pasa depende de como esté situado el diodo.


**Va a pasar el tipo de corriente en forma de como está colocado el diodo.**

Cuando viene el ciclo de la corriente positiva ella pasa, cuando viene el ciclo de la corriente negativa no pasa.

Muchas veces se dice que el ánodo es positivo y el cátodo es negativo, pero es mejor aprender hacia que lado va a la corriente si la corriente viene del ánodo(positiva) hacia el cátodo pasa. Si la corriente negativa viene del cátodo hacia el ánodo pasa.
**Vamos a trabajar con el diodo para anular la corriente alterna y tener corriente continua.**
Dejo pasar positivo para un lado y negativa para el otro.

El paso de la corriente tiene que estar en serie con la corriente que va ingresando. Si de un lado tengo 220 voltios y depende de la fuente con la que voy a trabajar.

**Un transformador con núcleo de hierro sirve para fuentes lineales.**
Fuentes lineales a la que opera con el mismo ciclo de la corriente con la que nosotros trabajamos  a 50 hertz.
Un transformador con núcleo de hierro siempre va a trabajar con 50 o 60 ciclos.

**Hay otros transformadores que tienen un núcleo de ferrita**
La particularidad que tienen los dos es que tienen campos magnéticos, el campo magnético se produce en la variación de la corriente alterna, porque en el primer movimiento no hay corriente en el secundario, recién cuando la corriente invierte la polaridad ahí recién salta esa corriente al secundario, porque primero imanto y es el imán que atraviesa los rulos del bobinado para que se genere la electricidad. Si la corriente alterna varía a 50 ciclos por segundo el hierro puede magnetizarse y perder su magnetización en el mismo ciclo de la corriente. **Si al transformador lineal le elevo a 50.000 ciclos por segundos: NO SE MAGNETIZA, queda constantemente magnetizado con el 1er campo, porque NO TIENE LA VELOCIDAD DE PERDER FUERTE EL IMÁN.**

Esto lo vemos con mayor precisión en la punta de los destornilladores, casi siempre en la punta de los destornilladores están magnetizados. Se magnetiza porque es un tipo de mental que permite que el imán sea permanente.

**El transformador tiene que magnetizarse y desmagnetizarse cada ciclo. Si siempre está imantado no nos sirve**
Las placas de un transformador son un montón de letras E y una recta.

Hay un bobinado entra al secundario y al primario.

Cuando vamos a trabajar con una placa de las que se llaman switching o conmutada, y las otras son lineales, se llaman así porque usamos el ciclo de la línea. 
#### Acuérdense: el transformador lineal trabaja al ciclo de la línea.
La lineal nació primero.

La ventaja que tiene la fuerte conmutada es que trabaja a un ciclo altísimo, en 1 segundo la fuente trabaja de 10.000 ciclos por segundo a 100.000 ciclos por segundo.


Si yo trabajo con un transformado lineal puedo reemplazarlo si más o menos está en el mismo amperaje, EN LA SWITCHING NO, no puedo sacar el transformador de ese y ponerlo uno parecido, porque los transformadores en la switching están hecho para frecuencias, le puedo hacer para 25.000 ciclos y uno muy parecido a ese puede tener 55.000 ciclos o 10.000 ciclos, por lo tanto no va a servir. 

Si vas a una tienda y pedís quiero un transformador que tenga salida 5 voltios y 12 voltios no se puede porque tenés que saber la frecuencia, a 10.000 a 70.000 etc.

Cuando reparamos y se quemó el transformador tenes que tener una fuente igual a esa para reemplazar el transformador, porque está hecho a base de frecuencia.

Lineal: Uno tiene hierro al silicio, el otro al cromo.
Conmutada: En cambio el otro es ferrita.

En una parte de la fuente vamos a tener que definir para cual de los transformadores vamos a hacer la rectificación, para la lineal o para la fuente switching o conmutada.

Ese es el primer paso para hacer la rectificación saber si querés hacerlo en una fuente lineal o switching.

01:51:50
[Agregar foto] (4 diodos y 1 capacitor lo más básico)
ahí yo tengo 12 voltios de corriente continua puedo usar para relay, prender un foco, 

Si yo ahí tengo 12 voltios y necesito 9 voltios tengo que poner un regulador de voltaje de 9 voltios, lo mismo si necesito 5 si es 5,1 tengo que poner de 5,1.

Con lo mismos componentes tengo que usar si es otro tipo de transformador.

#### Vamos a empezar hacer el proceso de rectificación con una fuente lineal.
Para poder hacer una buena rectificación se usa un puente rectificador de onda completa. 

**Los diodos de los rectificadores se lo representa con un dibujo de rombo.**

Pero cuando nosotros vemos la placa no está puesto en un sistema rombo, porque en la pista de las placas no se puede hacer eso.

En un lugar voy a poner una de las faces de la corriente alterna, y en el otro lado la otra, siempre tiene que estar en el modo opuesto.

##### Qué tipo de corriente me va a andar ahí a mi acá? 
Corriente alterna. De un lado tendrás ingreso de corriente alterna y del otro lado también ingreso de corriente alterna, vamos a suponer que sea fase y neutro.
#### Proceso de rectificación
Yo quiero que la corriente positiva me salga de un lado y la corriente negativa me salga del otro lado

Los diodos no son de colores.

##### La corriente positiva por donde entra y por donde sale?
Entra por el ánodo y sale por el cátodo.

Entonces me voy a fijar como está el ánodo entonces quiere decir que un ciclo voy a tener una corriente positiva. Independientemente de que lado venga siempre tengo que tener una salida positiva.

Voy a hacer que la corriente positiva ingrese desde el ánodo otra vez.

En cualquiera de los ciclos, cuando el ciclo de la corriente se está moviendo voy a tener por un lado o por el otro lado.


Cuando la corriente cambia de ciclo y me empieza aparecer la negativa.
### Qué tengo que poner para que me aparezca la negativa?
La negativa va a ingresar por el cátodo, y cuando viene del otro lado también tiene que entrar por el cátodo. Por eso se llama puente rectificador de onda completa, porque hay otros rectificadores que son de medio ciclo y hay otros puentes rectificadores que son de onda completa pero con punto intermedio en el transformador.

La corriente que voy a tener es la corriente continua PUNZANTE no la 

https://m.youtube.com/watch?v=y6x-zToySP4

En el tester tengo el voltaje de la corriente directa, la escala y ahí mido el voltaje.

### Consulta alumno
Teníamos un inversor que se hacía continua tenía un inversor para hacer alterna. Y la forma de onda del inversor no era buena entonces la fotocélula quemaba y la electromagnetica se banca un poco. 
Igual que el florescente, forma inducción cuando corta, cuando corta queda un campo inductivo, cuando vos cortás como no tiene campo inductivo como para volver vuelve a la línea y vuelve muy alta y quema la fotocélula.

### Hay sistemas de protección que se llaman filtros uber: diodo resistencia capacitor
Para que no baje, diodo invertido, en paralelo resistencia y un capacitor para que absorba esa energía restante

### Transformador reductor
De 220 vamos a lograr 12 voltios. Siempre en corriente alterna.


#### Hora 02:16:10
Si yo empiezo a sentir cosquilleo tengo que aislarme, mientras que yo esté aislado no hay peligro con la electricidad, no hay que cerrar el circuito.

La electrónica nació a partir del diodo

### Preguntar.
Si la corriente es continua es muy alta y vos tocás TE QUEMA, pero no te da un sacudón. Lo que te sacude son los ciclos de corriente alterna, y cuando tocas y te patea es el alternador que no rectifica.

02:39:20
#### En las fuentes switching NO hay corriente alterna, pero llegamos a altísimo VOLTAJE., pero llegamos a altísimo VOLTAJE.

Corriente alterna, rectificamos a través de los diodos, filtramos a través de transistores, y tenemos una corriente continua PURA.

El capacitor se coloca en paralelo. No en serio porque yo debo cargar las dos placas la positiva y la negativa.

Rizado: para muchas cosas sirve para otras no.
Depende de como está mi capacitor y si yo hice bien la ecuación para poner el capacitor necesario. Son como 4 páginas para calcularlo. No viene al caso porque nosotros somos técnicos. El capacitor tiene ventaja pero muchas desventajas también en la corriente alterna.


Si voy a llegar a una fuente lineal, lo primero que llego es al transformador ahí recién rectifico, después que subí o bajé la tensión, ese es en el caso de la fuente lineales.

Cuando son fuentes lineales, a la entrada ponés el transformador y después rectificas.

#### Fuentes switching o conmutada: 
Tenemos que anular 50 ciclos, porque no sirven para nada.
Vamos a tener una fuente con fase y neutro: corriente alterna.
Es una corriente alterna a 50 ciclos, y para mi fuente switching no sirve eso tengo que hacer corriente continua, tengo que rectificar inmediatamente. En la fuente lineal primero bajaba el voltaje para poder rectificar si yo quería una fuente de 15 voltios entonces tenía que crear una fuente lineal para 15 voltios y después recién rectificar, primero se baja el voltaje del transformador y después se rectifica.

Si yo quiero expresar a 12 voltios es conveniente que entre 1
Hay veces que están calculados así porque los transformadores trabajan con reguladores de voltaje, entonces si yo quiero expresarla 12 voltios es conveniente que entre 14, 12 voltios.

#### Vamos a volver al mismo puente rectificador de onda completa.

Otra vez vamos a elegir de que lado está el positivo y cual el negativo.

#### Hora 02:52:20
Entonces ahora tengo una corriente continua, por lo general a la fuente se lo trabaja más tiene mucho más componentes como bobina , más capacitores.

En muchas de las fuentes switching suelen tener dos o más salidas se hace 1 para que vaya al circuito integrado (procesador) y otro manejar el voltaje de los relays.

Muchas veces necesitamos mover relay para que arranque los lavarropas y muchas veces esos relay se mueven en 12,24 o 30 voltios depende del relay que ponga el fabricante para que dispare la bobina.
El chip es el que dispara el relay, pero existen otros componentes como transistores triac que permiten tomar 30 voltios y con 1 disparo de 1 lleguen los 30 al relay.

Al transformador que tiene ferrita le dicen chopper.

#### Luego de hacer la rectificación no hay más frecuencia.

En una pila no hay **FRECUENCIA**.
El transformador para que funcione necesita FRECUENCIA.

Si me pongo a jugar puedo hacer trabajar un transformador.
### Que tengo que hacer para generar frecuencia en corriente continua?
Que voy a necesitar: un generador de pulsos.
Cuando yo uno la batería se crea un chispazo y ahí si armó un campo magnético pero se destruyó. Subió hubo 1 pulso y cayó.
Hay unos generadores de pulsos que elevan desde los 10.000 hasta 12.000 pulsos.

Hay muchos circuitos de generadores de pulsos, por lo general todos tienen 8 pines, se empieza a contar desde la marca a la izquierda en 1 y se sigue a la inversa del reloj al contar los pines del otro lado.

Es importante saber esto porque cuando mirás un diagrama te dice para que funciona cada pin.

Algunos de los integrados generan pulsos, otros generan pulsos y controlan, hay varios tipos de estos integrados y hay distintos tipos de conexiones.
Lo primero que tenemos que hacer es alimentar al chip, vamos a suponer que se alimenta de 3 a 5 voltios, de ahí me va a decir que es la pata 1 y la pata 8, en uno el positivo y en el otro el negativo.

La corriente irá al bobinado, ¿cuantos voltios irá al bobinado? 311 voltios porque el capacitor se carga al valor pico.

### 03:06:12
Los 220 voltios de la corriente alterna equivale a los 220 voltios de la corriente continua y los cálculos para la potencia se usa el mismo. La raíz cuadrada de 1??

Entonces vamos a tener 311 voltios, no podemos meter ese voltaje al circuito, hay circuitos que sí permiten que llegue los 311 voltios, entre el circuito integrado y el transformador encontraremos un componente que se llama **transistor mosfet**.

Las oscilaciones que se forman acá esas oscilaciones va a tener el mosfet para hacer funcionar el transistor.???

Tener una corriente directa que no sirve para nada, entonces ahí va a oscilar 15.000 17.000 25.000 ciclos por segundos le va a alimentar a un mosfet para que soporte a ese voltaje esa oscilación para que luego tengamos el valor para que vaya al integrado y el valor para seguir ocupando los dos circuitos de la fuente. 

#### Haciendo oscilar/conmutar una corriente continua es como si yo estuviera trabajando con una corriente alterna. 
#### Pero con un núcleo de hierro no se puede hacer eso, por eso usamos un transistor de ferrita.

Hay en algunos componentes de ahora que estos mosfets ya no están más afuera, sino que están adentro en ese caso en lugar de pasar por el mosfet, vamos a suponer que entra por la pata 6 porque la pata 6 es la que está conectado en mosfet, el mosfet está adentro. 

En los primeros circuitos el mosfet estaba afuera, o sea nosotros teníamos la fuente rectificadora, teníamos el mosfet y el integrado, ahora NO. Incluso hay en estos circuitos la pata 7 no viene. O sea ya no trabajan más las 8 patas, sino que trabajan 7, pero viene como para 8.
