---
title: "[AUDIO][APUNTE] Taller reparacion de electrodometicos (Clase 3) - Ducha Eléctrica"
date: 2024-07-19T03:29:15-03:00
tags: ['electrodomesticos']
---
### Audio de la clase:
[https://www.youtube.com/watch?v=FEQ6iXWc2FQ&feature=youtu.be](https://www.youtube.com/watch?v=FEQ6iXWc2FQ&feature=youtu.be)

https://vocaroo.com/1eCHVsZwszT6

O miralo desde una instancia de invidious https://redirect.invidious.io/watch?v=FEQ6iXWc2FQ



Hablando de la corriente alterna también existe la corriente continua pura y la corriente continua punzante.

Tenemos que comenzar a arreglar algo de placas.

Ya no hay más lavarropas que funcionen con timer mecánico ya vienen todos con placas. Y dentro de esas placas hay cosas que es posible arreglar sin un estudio de electrónica.

O sea necesitamos saber que es lo que está fallando si es en la parte mecánica o si es en la parte electrónica.

En la placa siempre nos encontraremos con un procesador, y otro circuito que se llama dry, es como si fuera un relay.

Obedece las órdenes que vienen desde chip para desenvolver en la parte de trabajo.
La ducha eléctrica no tiene un circuito de control.
No tiene procesador.


Cuando lleguemos a lavarropas aprenderemos lo que son las placas con timer mecánicos.
El primer timer mecánico que nosotros vimos fue en los lavarropas que se los llaman semiautomáticos.

Lo único que tiene de automático es el temporizador. Donde nosotros elegimos que tiempo de lavado queremos que haga después el enjuagado tenemos que tener un secarropa al lado o a mano.

El microondas tiene un sistema de control distinto al de lavarropas pero cuando nosotros miramos la placa es lo mismo.
Por ejemplo todas las placas tienen: resistencia (componente pasivo), 

¿Por qué la resistencia es una resistencia a la tensión?
La resistencia y el voltaje son inversamente proporcionales.
Si nosotros estamos en una placa o en cualquier circuito y tenemos que tener cuidado con el voltaje que se está trabajando porque no se adapta a ese circuito lo primero que hacemos es controlarlo a través de una resistencia.
Aumentamos la resistencia para bajar el voltaje.
El otro componente de la electricidad es la intensidad.
Como unidad de medida: voltaje y amperaje.

La manifestación física es tensión e intensidad.
Nosotros reclamamos una medida de tensión.

No se dice que voltaje es, se dice que tensión.

La unidad de medida está en kilos. 

Componentes eléctricos: tensión e intensidad.
Como unidad de medida a la tensión medimos el voltaje y a la intensidad la medimos en amperaje.

Cuándo aparece la intensidad?
El voltaje está siempre. La intensidad aparece cuando hay trabajo.

El voltaje yo puedo medir en cualquier momento la intensidad no.
El voltaje es constante.

Una vez que nosotros estamos en un circuito eléctrico nosotros en cualquier momento podemos medir la tensión.

Necesitamos dos hilos conductores para cerrar el circuito y ahí no hace un cortocircuito sino que hace un trabajo eléctrico sea un secarropas, una lámpara, estamos haciendo un trabajo eléctrico, cuando este trabajo eléctrico. 

Que se caga de un motor? La bobina. 
Qué parte de la bobina? El aislante. Porque ya no está más separado sino que está en masa. En lugar de tener cierta cantidad de resistencia para que se trabaje, SI medimos ya no vamos a tener esa unidad en Ohm, va a ser mucho más inferior. Eso explota porque NO CAE la tensión.

220 voltios es la parte eficaz de una corriente senoidal.

La velocidad del motor de la lavadora con programa son señales cuadradas.
Los lavarropas el 1er movimiento lo hace muy débil, en las primeras 3 vueltas lo hace débil para acomodar la ropa en las siguientes las hace más rápido.
Lo mismo con la velocidad, de acuerdo con la velocidad.

Componentes de la corriente alterna: tensión, intensión.
Hay intensidad cuando hay trabajo eléctrico.

¿Cuál es el lugar más extremo en donde puedo medir una tensión (220 voltios)?
![/img/medir_tension_extremo.jpg](/img/medir_tension_extremo.jpg)

La corriente eléctrica no termina a la entrada de la carga, la carga también es un conductor.
Supongamos que estamos instalando una ducha.

Ventiladores ahora son plástico, pero antes era metal.
Las lavadoras de antes eran de chapa enlozada.
Las lavadoras siempre están en la parte más húmeda, mucha gente murió por eso.

La corriente que nos puede hacer daño es la fase.
El neutro no va a tener electricidad.

El peligro más fuerte de recibir una descarga eléctrica está en las manos porque las manos se cierran.

No tenés que pegarle con una percha tenés que contar la continuidad de esa energía eléctrica. Cortá el cable, bajá la llave.

###

Siempre y cuando la electricidad pueda pasar por mi cuerpo
Si yo estoy parado en esta mesa y agarro la fase, estoy electrocutado tengo que cuidarme de alguna persona que me quiera tocar por chiste porque ahí sí va a pasar por mi cuerpo para ir por el de él para ir por la tierra.

La transpiración es peligrosa porque tiene sal y la sal lo hace más conductora.

51 minutos: como se cual es la fase y el neutro?

La corriente alterna es una energía electromagnética, al rededor del conductor se forman campos magnéticos, esos campos magnéticos si yo no tengo neutro se me va a inducir. 
Cuando? Cuando yo puse el switch en no sé donde.

Vamos a suponer que yo tengo un sistema de relay y no pasó la corriente, pero esta corriente de fase indujo la corriente en el neutro y eso es una corriente por inducción.
Y es lo mismo que pasó en la lavadora, que yo le dije que el buscapolo prende pero a mi no me descarga porque es una corriente parásita de muy poco voltaje.
Y eso pasa cuando la llave corta el neutro.
Todos los conductores pueden llevar corriente a uno de los lugares en donde vos creés que tocaste y pasa cuando la llave corta el neutro. 

Si vos cortaste invertida, cortaste neutro pero todo queda por inducción


La intensidad vamos a poder medir cuando el circuito se cierre, ahí recién vamos a poder medir el amperaje.

Teorías
1. Las partículas de electrones se transfieren a través del conductor.
2. Los electrones no atraviesan sino que se mueven.
3. Los electrones pasan de positivo a negativo y de adelante hacia atrás y también se trasladan. 


La vieja teoría dice que la corriente pasa del positivo al negativo.

Después de varios experimentos llegaron a la conclusión de que: 
En un osciloscopio puedo ver si la onda es cuadrada, triangulo, senoidal 

Los ingenieros nos daran el diagrama de que la corriente va desde el positivo al negativo, cuando es al revés. Porque donde yo tengo los electrones de ahí se mueven, se mueven hacia el positivo. 


La nueva teoría dice que la fuerza voltaica si va desde el positivo al negativo, pero las partículas de electrones se mueven desde el positivo hacia el negativo.
La resistencia es inversamente proporcional, cae la resistencia sube el voltaje, sube el voltaje sube el amper.

Si yo agarro una lamparita de 45 watts de 12 voltios, no es lo mismo que una lámpara de 40 watts de 220 voltios. Porque la cantidad de electrones que muevo son distintas por la fuerza voltaica.


El amper es proporcional al voltaje. Y la resistencia es inversamente proporcional, cae la resistencia sube el voltaje, si sube el voltaje sube el amper.
Si se me quema el transistor es porque me está llegando más corriente.
Entonces yo tengo que analizar medir esa resistencia que me está alimentado a la base del transistor o de un triag porque me está haciendo pasar demasiado voltaje.


Entonces como hago tengo que hacer de vuelta los cálculos para mejorar esa resistencia, si yo manejo la caída de voltaje manejo también la cantidad de intensidad que puede recibir ese componente.


La tensión y la intensidad son los componentes de la electricidad.

Cuando yo multiplico tensión por intensidad entonces ahí yo sé que potencia tiene ese motor.
Si tengo un motor que mide 0,90 amper y me está midiendo 1,3 amper algo está mal en ese motor.
En una resistencia como una ducha, estufa, plancha no se va a dar eso. Las duchas que tienen resistencia no es lo mismo que las planchas ni que las estufas.
01:07:35

Si yo a la ducha la quiero usar de estufa no se puede porque necesita estar en el agua, es el mismo material pero tiene mucho menos caída que las otras resistencias.

Resistencia en serie = multiplico el ????
(01:08:46)

#### Como funciona la ducha?
Nunca ustedes pusieron una térmica en la ducha?

Esta llave tiene el switch, yo ahora encendí ¿trabaja la ducha? No, porque si anduviera fundiríamos la ducha porque no tiene agua.


La termomagnética si tengo en ohm no prende la ducha.
Y por qué se funde la ducha si prendo?
Supongamos que este sea la llave que va a ingresar a la ducha. En la termomagnética si tengo en ohm, no prende la ducha.

Puede prender o no?
Si puede, y en donde está la falla de por qué prendió?, cuando la termomagnetica estaba prendida y comienza a calentar la resistencia de la ducha

Yo puse ohm la termomagnética pero no hay cruce de agua sin embargo comenzó a calentar la ducha.

Si tiene agua debe tener un contacto adentro, cuando llena el agua tiene que levantar ese contacto para que haga masa y encienda.

Cuando yo hago ohm con la termomagnetica siento que calienta la ducha y apago de golpe, las duchas cierran con una cuchilla que tiene arriba, hay veces que los contactos de arriba se sueldan. Como es un componente de muy alto consumo, entonces en cada prender y cerrar siempre hay un arco voltaico.

No es aconsejable cambiar la temperatura de la ducha cuando el agua está saliendo. Hay que cerrar el grifo. Cuando la cuchilla ya está cerrada, porque en el momento que yo corto con un material aislante que pasa por el medio.

![/img/ducha_electrica.jpg](/img/ducha_electrica.jpg)
![/img/ducha_electrica2.jpg](/img/ducha_electrica2.jpg)

Un hombre muere mientras se bañaba con ducha eléctrica: https://m.youtube.com/watch?v=lp4l9TaKoHk
O miralo en una instancia de invidious: https://redirect.invidious.io/watch?v=lp4l9TaKoHk


No es bueno doblar
Por qué hay que cargarle agua arriba de la ducha?
Porque hay veces que cuando cerrás la ducha sigue andando es como que agarró aire.
Cuando cambiamos la resistencia que viene en un tratemos de sacar la parte más sana, porque hay una de las resistencias que es un cachito más grande y a simple vista no te das cuenta 

Inaudible (01:26:10)
Cada vuelta es como una resistencia está toda en 0.
Si yo uno va a tener menos caída y va a tener más resistencia.

Cuando elijo el agua caliente se mueve el plástico(aislante) y une los contactos de la resistencia.

### Por qué la llave se llama termomagnética?
Porque tiene 2 defensa, esto sería un fusible que interrumpe pero yo puedo volver encender.  

Hay fusibles que se funden y tenés que reemplazar por otro porque ya se cortó.

Hay fusibles bimetálicos una vez que corre peligro la instalación el se abre porque calentó por el exceso de corriente.
![/ducha.png](/ducha.png)

El termomagnetico trabaja por temperatura y por campo magnético.

Si yo tengo un consumo estoy generando cruce de electrones, ese cruce de electrones me genera un campo magnético. Cuando el consumo es más alto se me hace más fuerte el campo magnético la llave salta porque el campo magnético es muy alto (el consumo).

[https://www.youtube.com/watch?v=bODm_rIzxTw](https://www.youtube.com/watch?v=bODm_rIzxTw)

Pasó a 20 amper a 35 de la nada.
No por temperatura sino por campo magnético (se mide en amper).

Cuando nosotros colocamos algún tipo de defensa algún tipo de fusible que puede ser el fusible fijo, el bimetálico o el termomagnético, lo que tenemos que cuidar son los conductores.  
No quiero decir cables porque son conductores.  

Tenemos que proteger los conductores, no la ducha, no la heladera, no el split. Hay que colocar una protección de acuerdo a la capacidad de los conductores. Nunca de acuerdo al consumo del artefacto.

#### Error:
Nosotros siempre nos fijamos: 
- Che de cuanto amper es esto 
- De 25 amper.
- Bueno dame una llave de 30 amper 

Y ponemos cables para 10 amper.
#### Que pasará?
Calienta los conductores y se derrite y prende fuego.


Yo me tengo que fijar en la potencia del consumo, o me tengo que fijar en el amper del consumo.
Entonces que tengo que hacer, no hay cable para tantos WATTS. Tengo que ir a pedir por amperaje.
#### Que tengo que hacer para saber de cuanto amperaje?

Tengo que hacer el triangulito.
![/ohm.jpg](/ohm.jpg)

Alguna noción de en que amper tiene que andar tenemos o si estás con el tester hay que ir del más alto al más bajo (amper).


La pinza amperométrica no puedo usar con los dos cables, porque se cancelan.

### ¿En una plaqueta como medís el amperaje?
Para medir amper siempre se debe hacer en serie.

##### Si yo coloco el amperímetro en paralelo, el amper nunca va a querer entrar por el amperimetro y va a seguir de largo.
##### En cambio el voltaje siempre se mide en paralelo
### Por qué siempre se mide en paralelo el voltaje?
Porque tengo que medir la diferencia de potencial.
Una de las teorías del amper es que es igual en todo el circuito una vez que el circuito esté trabajando.
Vamos a suponer que yo coloco el amperímetro y no en la placa es porque por donde va ese circuito en la placa siempre va a tener 3 amper.

El amperaje es solo lo que la carga hace trabajar.

Para medir, agarro la placa voy a cualquier parte de la pista corto la pista con una aguja 
Interrumpo en donde queda más cómodo.
Corto y miro cuando hay continuidad.
Se tiene una navajita a mano se limpia todo el cobre traigo el caotrín le caliento y le pongo un puntito.

### El amperaje es en serie y el voltaje en paralelo
Hablando de la resistencia, en la ducha.  
Acá dentro hay un diafragma de goma.

Es parecido al diafragma del regulador de la cocina a gas, o sea que sufre un desplazamiento de acuerdo a la presión que tengamos.
Los presostatos de la lavadora también funcionan así. Toman como beneficio una presión para hacer cierta cantidad de fuerza, acá yo necesito una cantidad de fuerza para poder vencer la fuerza de las dos cuchillas.

Cuando se llena de agua levanta las cuchillas dentro de la ducha.

El error más grande es agrandar el agujero de la ducha, porque habrán 2 problemas.
1. Si fui generoso con el agujero no voy a tener la presión necesaria para acumular presión para que levante la goma, porque esta presión está dada por el caudal de agua que ingresa al recipiente de agua por la cantidad de agua que sale. El agua que entra tiene que ser mayor para mayor presión.  
La presión del agua tiene que vencer la fuerza de la cuchilla.

En la ducha no hay polaridad.
En un lugar en donde la presión es excesiva, hay una moneda para hacer un agujero.

Hay duchas que patean. Porque está muy cerca de la ducha. Adentro de la ducha hay un cable que va a tierra y somos pocos los que conectamos ese cable a tierra.

Sergio conecta el cable a tierra de la ducha en el ituzaigó salta el diyuntor.

Agregar fotos de ducha, la nueva y la vieja.

Toma de 30 amper y enchufe de 30 amper.
Envolví el cable para que cambiar más fácil.
No hace falta 30 amper.

Cable para una ducha 2 y medio.
Todos los conductores tienen resistencia.

Bipolar es porque corta el vivo y el neutro.
![/img/intensidad_potencia.jpg](/img/intensidad_potencia.jpg)

### La ducha consume amper, si yo digo consume menos amper y consume menos potencia estoy diciendo lo mismo o no?
Sí. Si consume más amper consume más potencia.

Cuanto más suba la intensidad voy a tener más potencia. No puedo bajar la potencia para que baje la intensidad, la tensión me controla la intensidad y la intensidad me controla a la potencia.

Si yo pongo una termomagnética muy grande no va a cortar. Cuando yo pongo un conductor siempre voy a colocar de acuerdo a la **POTENCIA**

Para un cable de 4 milítros podés poner 40 amper.
![/img/amper.webp](/img/amper.webp)

2 y medio cable = 20 amper = 4400 vatios. 
Las duchas son de 2000.


No es por inducción, fue porque cortó el neutro. Es porque está en vivo.

Cuando vos cortás el neutro tenés el vivo a la ida y a la vuelta.


El consumo está expresado en horas.
10 amper horas.
Si coloqué un cable de 10 milímetros y uso 10 15 minutos la ducha funciona.


Las térmicas son más chotas ahora.
Se sopló la térmica = corta antes.
La térmica queda muy sensible, está fallada.


Hay capacitores con polaridad y sin polaridad.
Foco de neon.
Muchos técnicos te quieren correr porque dicen que ese no es un filtro.
A la salida del puente retificador.

#### Importante
Para que sea continua a la salida de ese puente retificador de onda completa debe llevar un capacitor polarizado.
Muchos técnicos dicen "filtro" al capacitor polarizado, y muchos no.
Los que dicen que es un filtro sostienen que a la salida del puente retificador yo voy a tener la corriente positiva,  y voy a tener la corriente negativa. Ya no tengo más fase y neutro tengo positivo y negativo. 
Para poder filtrar esto, cuando acá sale la corriente va a salir así: va a tener pequeños saltos porque es punzante, a medida que los diodos fueron retificando fueron apareciendo el lado positivo y el negativo.

Cuando nosotros queremos retificar esa corriente colocamos un **CAPACITOR POLARIZADO**

Para tener continua siempre hay que hacer un circuito mucho más complejo.

02:39:40 hablamos de la jara del termostato


![/img/boton_temperatura.jpg](/img/boton_temperatura.jpg)


### Diagrama plancha
![Plancha](/img/plancha.jpeg)
### Diagrama ventilador
![Ventilador](/img/diagrama_ventilador.jpeg)
