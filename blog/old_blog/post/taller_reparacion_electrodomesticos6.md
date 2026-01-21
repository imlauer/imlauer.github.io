---
title: "[AUDIO][APUNTE] Taller reparacion electrodomesticos (Clase 6) - Relay. Triac: corriente alterna. Mosfet: continua y alterna?. Contactora. Varistor. Termistor. Fuentes. Puente Rectificador. Mosfet. Soldador no funcionó."
date: 2024-08-08T20:45:09-03:00
tags: ['electrodomesticos']
---
#### Audio de la clase
https://youtu.be/4LCbuu2Wa_4

https://voca.ro/1m9YA0YHQNHw

O miralo en una instancia de invidious: https://redirect.invidious.io/watch?v=4LCbuu2Wa_4

![](/img/6ta_clase_electro/IMG_20240808_150958712.jpg)
![](/img/6ta_clase_electro/IMG_20240808_153826709.jpg)
![](/img/6ta_clase_electro/IMG_20240808_153613841.jpg)
![](/img/6ta_clase_electro/IMG_20240808_165602100.jpg)
![](/img/6ta_clase_electro/IMG_20240808_171255203.jpg)
![](/img/6ta_clase_electro/IMG_20240808_172118414.jpg)
![](/img/6ta_clase_electro/fuente_sin_transformador.jpg)
![](/img/6ta_clase_electro/IMG_20240808_172556719.jpg)


##### Problemas comunes.

Placa electrónica de un televisor: tal circuito integrado no está aguantando, por problemas de temperatura muchas veces se repiten.

Consumo es la potencia.

Para la fuente tengo que tener dos conductores: fase y neutro.

Si yo tengo algo que no anda lo primero que tengo que medir es **continuidad**


Puedo tener un switch, un pulsador, si es algo que está en paralelo a no ser que esté en corto NO ME VA A QUITAR la continuidad.

Siempre mi continuidad se va a caer cuando yo tengo las cosas en serie, porque cuando las cosas están en serie tienen que funcionar todas porque 1 que no funcione, no funciona ninguna.

Todas las cosas que controlan el trabajo están en serie, por eso hay que medir la continuidad primero.

Si conecto directo el aire funciona.


Una bobina puede quedar en corto.

Resistencia: carga
Capacitores: potencia

Casi todos los problemas de planchita, microonda, secador cabello, liquadora, están en la fuente o en la parte de potencia.      

En la parte de potencia nosotros vamos a encontrar problemas con la parte que dan el trabajo a la potencia porque si esto es una placa, ya no es una carga se llama control y trabaja con 3 voltios. La carga va a trabajar con 220 voltios, quiere decir que esos 220 va servir para que una determinada parte de la placa haya una parte de fuente y por el otro lado haya una parte de alimentación de potencia que vamos a encontrar en la parte de alimentación para que funcione la potencia.

#### Preguntar 
#### Como llegan los 220 voltios (alimentación de potencia)
Por relé o relevadores.

Funcionamiento relé: 
https://www.youtube.com/watch?v=aHttlFviaDQ

https://www.youtube.com/watch?v=1ee8QlvUkr8

#### 43 minuto:
Tenía 2 placas, una lineal y otra switching.

Switching: no trabaja con voltaje alto, porque trabaja con corriente continua hasta 30 voltios porque es una placa de PC.

Cuando no hay relevadores hay un **triac**.

Triac: transistor de corriente alterna.

Primero apareció el diac: rectificador controlado de silicio, pero era para corriente continua, era como un conmutador.

La placa va a disparar tu relay con 9 voltios, y le pongo un relay de 30 voltios, los 9 voltios que dispara la placa no va a disparar el relay.

Vamos a suponer que es un relay unicamente de 1 pulso y terminó.

Los relay trabajan con magnetismo, los triac no. 

## En la parte de la potencia vamos a encontrar: relay y triac.


---

En la parte de potencia vamos a encontrar un relay.

TRIAC = transistor para corriente alterna.


Relay para chequear si funciona tenés que medir la continuidad de la bobina. En el relay tenés un pin que se llama normalmente abierto y en el otro normalmente cerrado.

De la misma manera vamos a encontrar las contactoras.

Una contactora es un relay para múltiples funciones de apertura y cerrado, y donde se vió la necesidad? En un trabajo trifásico. Corremos el riesgo de que una máquina un motor esté sufriendo un zumbido o cosa así.

### Relay
220 trabaja entre el 1, el 4 y el 5.

## Muchas placas no traen varistor.

El varistor trabaja porque varía la resistencia por la tensión, es un PTC O un NTC.



Coeficiente térmico positivo, 
Coeficiente térmico negativo, 

Si la tensión sube, el coeficiente térmico positivo la resistencia también sube.    
Si la tensión sube, el coeficiente térmico negativo la resistencia baja.


El varistor esta en paralelo y el tester debe estar en escala en ohm muy alta.

Varistor es una protección si tenés una sobre tensión se pone en corto.


1.180.000 de ohm. Es altísimo por eso la electricidad no se entera que él está.

Lo que más se jode de una fuente de computadora es el oscilador,

### Oscilador
La corriente continua de 311 voltios salía del capacitor venía directamente a la bobina del primario el extremo de la bobina del primario tiene que venir al chip pero va a quemar porque tiene 311 voltios, entonces pasa por un MOSFET, la que entra al mosfet que es la otra parte del neutro va a la otra patita y por el del medio va la oscilación del chip.

#### 02:27:50
La entrada de los 220, el puente rectificador, el capacitor, vamos a encontrar el chopper, el oscilador y el mosfet. El nuevo chip el mosfet ya no está ahí está adentro.

Cuando el mosfet está afuera lo cambiamos, si está adentro hay que cambiar todo el integrado.


Un capacitor en corriente continua no puede trabajar, no puedo poner un capacitor en corriente continua en serie es como si estuviera abierto el circuito.

---

#### Transcripción

##### Cual es el problema más común de los televisores?
Depende de la marca de televisores hay problemas comunes.

Profesor: "Mi profesor me dijo que nunca son iguales los problemas, pero se equivocó muchos los problemas dependen de la marca, hay ciertos lavarropas y ciertos televisores que se sabe de entrada cual es el problema que tienen".

Tal aire acondicionado si presenta tal problema cambiale el valor de tal cosa, en tal parte. Esos problemas se repiten.

Vamos a hablar de la placa electrónica de un televisor, está dejando de funcionar tal cosa es porque tal circuito integrado no está aguantando, o está aguantando en donde hace frío cerca de 0 pero en los lugares subtropicales está fracasado.

Todas las herramientas son buenas. Hay que insistir con la parte electrónica magnética.

Si tiene rulemán entonces el ruleman.
Si tiene buje y eje entonces es eso.

Si es un lavarropas de carga superior y hace ruido, hay que desarmar la transmisión aflojar tornillo y sacarlo y listo, pero los técnicos fracasan en donde yo sigo mis clases, para la mayoría le cuesta mucho entender esto.

O vos le llevás y te dicen a si es un capacitor ese, pero hay veces que alguien por el camino le cambió el capacitor y ellos ya **no saben**.

Porque a mi me pueden traer un motor con un problema, lo primero que voy a hacer es **medir el consumo**, ¿por qué mido el consumo? 
#### ¿qué es el consumo?
**La potencia**
#### Por qué es la potencia?
Porque yo la tensión ya tengo, si yo acá tengo una carga acá tengo la fuente quiere decir que yo si o si tengo que tener dos conductores vamos a hablar de corriente alterna porque si no no funciona.

Esos conductores se llaman **fase y neutro**. Sin fase y neutro no va a funcionar nunca, si yo tengo algo que no anda, inmediatamente tengo que hacer un **control de continuidad**.

Por acá puedo tener un pulsador, puedo tener un switch, **si es algo que está en paralelo a no ser que esté en corto no me va a quitar la continuidad, siempre mi continuidad se va a caer cuando yo tengo las cosas en serie**.

Todas las que están conectadas en serie tienen que funcionar, porque 1 que no funcione ya no anda nada.

Si el cable se soltó internamente, ya no va a andar.

Si se rompió algo que está en paralelo.

Todas las cosas que controlan el trabajo, siempre van a estar en serie. Con que 1 no me funcione ya no funciona nada.

## Respuesta exámen
#### Tengo que hacer una comprobación de continuidad entonces primero voy a verificar el switch, pulsador, térmico, fusible.

Directamente que puedo hacer?

Agarro el tester y mido la continuidad.

Entonces una de las formas es medir acá, en la clase anterior habíamos medido una jara eléctrica, medimos la resistencia.

Porque si la resistencia no funciona, ¿para que quiero ver el resto de los componentes?

Si me anda la resistencia, yo voy a poder trabajar de forma directa, pero voy a tener que estar al lado controlando.

No voy a poder hacer ningún tipo de control porque está conectado directamente: cuando enchufo arranca, cuando hace frío desconecto, pero de que va a funcionar funciona.

Mi ventilador lo voy a poner en directo. 

### Siempre y cuando no sea un **reductor de voltaje**.
Porque si tengo un componente que trabaja en menos de 220, y yo le pongo 220 hace explotar todo.

Si es algo electrónico que está ahí controlándome la tensión no voy a poder sustituirlo, pero lo otro sí puedo poner en directo.

El ventilador, el compresor en directo todo funcione, no voy a tener control hasta que compre una placa nueva.

Habría que hacer una medición de continuidad: cierro la llave del switch dejo conectado el pulsador.

Yo desenchufo y hago un puente, vamos a suponer que sea un termostato, **puenteo** y ahí si me quedó directa la carga. Yo coloco el tester en ambas puntas en la escala de continuidad.

Si me mide que está hecha la continuidad y no funciona hay otro problema, ¿cuál puede ser el problema?

Vamos a suponer que sea un ventilador.

Una de las bobinas está en corto, por eso **me da continuidad**, si yo mido un ventilador y me dá 37 ohm de impedancia cuando está en corto me va a dar 20/15/11, porque en algún lado los cables dejaron de estar aislados.


Si es una plancha no puede haber variación entre la nueva y la usada tiene que ser la misma impedancia, la resistencia del elemento de trabajo es tan corta que no habrá problemas siempre marcará 0, algo. 

Pero por el problemas del tester a lo mejor me va a marcar 1 o 2 ohm , o no me va a marcar nada.

**No puede quedar en corto la resistencia de la plancha.**

Lo mismo la resistencia de la jarra eléctrica, **lo que si me puede quedar en corto es una bobina, porque las bobinas son individuales cada bobina, y son individuales gracias al esmalte del alambre: CABLE MAGNETO**. 

No podemos usar un cable grueso porque a la segunda vuelta ya no tenemos más espacio.

Una bobina nueva me puede estar rindiendo 18 ohm, y si está quemada me marcará 5/4/3 ohm, porque en algún lado el esmalte se borró y se UNIERON las bobinas, y corta camino en lugar de hacer el recorrido completo.

Alumno: a mi me pasó con un ventilador industrial, se juntaron los cables y yo re manija, metí más cable y reventó todo.


Profesor: pero aprendiste, si te enojás y pateás perdiste tiempo.

En una fuente para un equipo electrónico, por lo general lo que más deja de funcionar es la parte de la fuente, el 70% más o menos de los componentes electrónicos siempre se queman la fuente.

**Por qué?**

Porque es la que soporta mayor el trabajo, todo el trabajo que hace, todos los trabajos que hacen toda la cantidad de cosas que están acá dentro soporta la fuente.


La que soporta todo el trabajo es la fuente, igual que los transformadores el que soporta todo el trabajo es el bobinado primario.

**Cuando un transformador se quema el 99% se quema el primario.**

Nunca encontré un transformador quemado el secundario, aunque puede pasar por la humedad, o una cucaracha o se golpeó algo.

**Si hay un corto en el secundario se quema el primario**, porque es el que soporta la carga, el secundario consume, cuando analicen transformadores quemados, siempre está achicharrado o de color quemado, el bobinado primario, a veces se corta porque es demasiada la carga que soporta.

Los fusibles deben estar puestos siempre mirando al conductor que le llega hasta el fusible. Si yo tengo puesto un fusible acá, tengo que mirar de acá para allá, lo correcto es el completo. Acá es donde se resiente el conductor.


El fusible siempre debe ponerse de acuerdo a la medida del conductor, o sea que este circuito a mi me está gastando 5 amper, yo tengo que colocar acá NO un fusible de 5 amper, **si yo acá tengo un cable para dos amper yo voy a poner un fusible de 2 amper NO uno de 5.**

"Eh, pero no voy a poder usar, apenas uso 5 minutos y vuela, bueno está bien, querés usar completo cambiá el conductor, poné conductor para 7 amper para 6 amper, una vez que colocás un protector para 6/7 amper, **el que no va a soportar nunca es el conductor**.

Si yo coloco un conductor para 3 amper y hay un consumo de 7 y coloco un fusible de 7 amper, **pero el conductor no va aguantar**. Va a prender fuego, es preferible que el fusible vuele todas las veces porque el conductor ya viene hasta que vos digas **voy a poner un cable como tiene que ser porque no va**.

#### El fusible siempre debe ponerse a la medida del conductor.

### La funcionalidad de la fuente es adaptar mi fuente a la carga.

Por qué se llama fuente lineal? Porque trabaja con la frecuencia de la línea.

Tipos de fuente: capacitiva resistiva, lineal, switching o conmutativa.

Si yo tengo un chip de 3 voltios de voltaje directo, en la fuente tengo 220, entonces tengo que adaptar la fuente a los voltajes del chip.

## Por qué nosotros decimos que una fuente es lineal?
Porque trabaja a 50 ciclos.
Como es un transformador para 50 ciclos? Con núcleo de hierro al silicio.

Hierro al silicio porque se magnetiza y desmagnetiza dentro del tiempo 50 ciclos por segundo.

La fuente switching no se puede poner un transformador de hierro porque trabaja a 10.000 hasta 100.000 ciclos.

Entonces quiere decir que se magnetiza y desmagnetiza mucho más rápido, **si fuera hierro al cromo tampoco sirve** porque se magnetiza y queda magnetizado como pasa con la punta de los destornilladores.

Se inventó la fuente lineal porque trabaja con la frecuencia de la línea.

Que es lo que le hace que el hierro al silicio se desmagnetice? Porqué yo magnetizo esto y se desmagnetiza otra vez, y por qué el hierro al cromo se magnetiza y queda.

Estoy hablando del metal, la particularidad del metal.

**Porque en el hierro al silicio las partículas magnéticas están desorientadas, no están en fila. En el hierro al cromo sí.**

En el hierro al silicio las partículas magnéticas están desorientadas, no están en fila, en el hierro al cromo sí.

No se hacen ferrita para los transformadores lineales por la frecuencia, son muy acelerados.


Un transformador de ferrita ya se pone a trabajar a partir de los 90 voltios para arriba, llega a tener la potencia de un transformador lineal.

### Casi todos los problemas estarán en la parte de la fuente, o en la parte de potencia
En la parte de potencia vamos a encontrar problemas con la parte que dan el trabajo a la potencia.

### Que vamos a encontrar en la parte de alimentación para que funcione la potencia?
Relé, relay, relevador.

En donde no tenemos relé vamos a encontrar TRIAC.

TRIAC: transistor de corriente alterna.
**El que primero apareció era el DIAC:  rectificador controlado por silicio.**
Sólo para corriente continua, como un conmutador.

Vamos a suponer que la placa va a disparar el relay con 9 voltios y yo le pongo uno de 30 voltios, los 9 voltios que dispara la placa no va a disparar el relay, si le ponés una fuente switching en vez de liineal.

### Vamos a suponer que es un relay únicamente de 1 pulso y terminó, si yo acá tengo un relay de 9 voltios y me dispara 30, no va a pasar nada.

### Pero si es un relay de trabajo continuo sí. Por ejemplo para la bomba punzora, todo ese tiempo que trabaja la bomba se va a quemar el bobinado, porque era para 9 voltios y la placa le está dando 30, se quemará la bobina del relay.

El relay tiene 5 pines. Está hecho para 5 pines, muchos relay traen 4 pines porque hay 1 que le sacan.

Cuando van a comprar le van a dar con 5 pines. O agarran un alicate y lo cortan. **Porque es el que no tiene circuito, los demás sí.**

El 1 es la entrada de energía: 220 voltios.
Necesito los 220 para que la carga funcione.

**Si es bomba de agua, solenoide de carga trabaja con TRIAC.**

### bobinas = generan campo magnético

Para que sirve la bobina? Generan campo magnético, dentro del campo magnético si yo coloco un émbolo ferroso que ocurre? Vamos a suponer que yo tengo un molde de plástico de cartón o de lo que sea, y le entro a enrollar acá alambre. Si yo conecto estas dos puntas a 12 voltios de corriente directa, que va a ocurrir? Se va a crear un campo magnético, será constante.

Polo norte, polo sur y se va a ir variando.


Depende de como este hechas las vueltas del alambre, el émbolo de hierro o va a saltar para arriba o para abajo.

Crea una fuerza magnética que le hace correr al émbolo, entonces este relay.

Para que el émbolo vaya hacia arriba o hacia abajo hay que invertir la polaridad.


Me quedé en el minuto 51.

O sino puedo desarmar todo el bobinado y envolver al otro lado. De acuerdo a como esté hecho el bobinado genera la fuerza hacia arriba o hacia abajo.

El positivo de un lado y el negativo del otro.

Esto ocurre en los motores. 

Lo único que hacemos es invertir el lado por donde entra la corriente, por eso las lavadoras con placas son motores universales, trabajan con continua, como alterna.

La placa está generando un sistema de pulso con dirección por eso cambia la rotación, en los lavarropas viejos no se podía porque no tenía una placa que le haga cambiar la polaridad.

Lo único que hacemos es invertir el lado en donde entra la corriente, los motores de las lavadoras son motores universales.

El relay tiene una bobina, dentro de la bobina tiene un émbolo un hierro que no está asegurado. Acá vamos a tener un émbolo que pasará por dentro y generará una base rígida. Esto genera un campo magnético que magnetiza al émbolo, porque el émbolo es ferroso. El cobre y el bronce no se magnetiza, únicamente me sirve los materiales que son ferrosos.

Si no se puede mover genera una fuerza magnética pero queda firme porque está abulonado a la chapa.

Platinos que cierran y abren.

Cuando la chapa se magnetiza, lo hace con 12 voltios.    
Cuando la placa magnetiza la bobina, el platino se cierra, por lo general es un resorte para que el platino esté siempre abierto. Cuando se magnetiza el campo magnético que está acá tiene que vencer la fuerza del resorte.

Termostato de la plancha tiene un platino, es un material más firme que permite que fogonazo de la corriente.

El platino cuando la placa ordena el platino se cierra, y como tengo una entrada de 12 voltios.

El relay hace que el motor pueda girar en ambos sentidos porque conecta la bobina al reves.

Mi padre agregó un relay para proteger el triac.
Proteje porque el relay es más duro para resistir alto voltaje o alto voltaje, si se pone en corto va a saltar el fusible.

Si le agregás el fusible al triac, el fusible es muy lento y se caga antes el TRIAC.

### El semiconductor triac no aguanta, nunca podés proteger a un semiconductor con un fusible, el fusible es lento.


Pusieron un potenciómetro lineal para saber la posición de la mariposa o acelerador en un BMW. Cuando pusieron electrónica, porque le tenían que saber donde estaba el acelerador y eso traía mucha falla. Y en Inglaterra con fue sustituido con efecto hall, valía 200 dólares la reparación.

Cuando vos usas el ventilador baja velocidad calienta el plástico.

El térmico cuando se calienta abre y no funciona más no es como un termostato.

Los ventiladores son más lentos porque el motor es de mala calidad. En un motor la velocidad está dada por la cantidad de polos, cuanto menos polo tiene un ventilador más velocidad. Los polos hacen un electroimán.
Está hecho con la cantidad de espiras necesarias.

Mas bobinas menos espinas = mala calidad   
Menos bobinas más espinas = mejor calidad    

El ventilador de piso no tiene bobina en el reactor, pero el de techo sí.


### En la parte de la potencia encontraremos relay y triac

Al mirar el relay lo primero que haceos es medir continuidad de la bobina. En el relay tenemos un pin que se llama normalmente abierto y otro que se llama normalmente cerrado, por lo general este pin no aparece con la letra A aparece con la letra O.

En los relay vamos a tener dos tipos de corriente siempre y cuando sea un relay que está trabajando en un motor, de la misma manera vamos a encontrar en las contactoras.

Las contactoras son iguales que los relay para multi apertura y cerrado, se vió la necesidad en un trabajo trifásico. Con una sola funcion la contactora conecta las 3 funciones o 4 o 5. 

Una contactora se puede usar en una monofásica también.
Incluso si yo estoy haciendo un trabajo para mí puedo usar una contactora para prender varias cosas a la vez.

No es nada más que unas cuchillas que se abren y usa una fuerza magnética. 

Si esto fuera una contactora en uno de estos lugares tendría que ver una conexión para la bobina, porque tengo que alimentar la bobina para que cierre el contacto cuando yo largo la fuerza de mi resorte abro.

El relay va a abrir y funcionar a través de una fuerza magnética tenemos que estar atento al voltaje con que nosotros vamos a disparar la fuerza del relay.

01:10:30

El relay va a abrir y cerrar a través de una fuerza magnética tenemos que estar atentos al voltaje con que nosotros vamos a disparar la fuerza del relay.

A y B son los extremos de la bobina, en los extremos tiene que haber 12 voltios de corriente continua, no me sirve 12 voltios de corriente alterna tiene que ser corriente continua para que el relay cierre y cuando le dejamos de alimentar sube porque el resorte le abre, y cuadno le doy los 12 voltios el campomagnetico vence la fuerza del iman y los platinos se toman.

Nosotros

En los extremos de la bobina tiene que haber 12 voltios de corriente continua, para que el relay cierre y cuando le dejamos de alimentar el sube porque el resorte le abre y cuando yo le doy los 12 voltios el campo magnético vence la fuerza del imán y los platinos se tocan.

Medimos unos de estos relay y se escucha el tiqui, yo mido la continuidad primero luego con una fuente de 12 voltios con un transformador que va a transferir la corriente de 220 voltios a 12, que por lo general andará entre los 15 y 16 voltios, que le sigue después de eso?

Tiene que ser un transformador de hierro, luego del transformador sigue un puente rectificador o sea que yo voy a tener 220 voltios, voy a tener 15 16 voltios de corriente alterna en el transformador.

Voy a hacer un puente rectificador con 4 diodos

Le sigue un capacitor para dejarlo mejor a la tensión, ahí ya podemos probar si el relay funciona on o.

Cualquier cargador de herramientas eléctricas de 19 voltios o de 12 voltios podemos probar relay con eso, porque el relay no tiene consumo.


Cualquier cargador de herramientas eléctricas de 19 voltios o de 12 voltios podemos probar relay con eso, porque el relay no tiene consumo.


Guarden los cargadores que se les fundió el cable porque les puede servir para medir relay.

Hay de 5 voltios, 9 voltios, 30 voltios.

El celular solo tiene 5 voltios, el de la carga para la batería tiene 19 voltios.

O nos hacemos una fuente de 12 voltios y podemos medir con eso..


Ahora vamos a ver si está habilitado el paso de la corriente


Si entra la fase de los 220 voltios.

Si yo le mando los 12 voltios va a abrir el normalmente cerrado, pero va a cerrar el normalmente cerrado

Que quedaría por probar? Si la corriente que entra esté saliendo.


