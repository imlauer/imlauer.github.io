---
title: "[AUDIO][APUNTE] Taller reparacion de electrodometicos (Clase 12) - Microondas Repaso: Componentes con más fallas. Por qué existen las fuentes. Etapa control. Etapa Potencia. Tipos transformadores. Regulador voltaje. Diodo zener. Puente rectificador. MOSFET. CC pura: punsante. Capacitores suben voltaje. Diagrama fuente switching. No existe transformador en CC. Oscilador. Medir capacitor. Estrella lavarropas. Octoacoplador. Todas las fuentes tienen el mismo objetivo. Electricidad y magnetismo.Imanes: si se rompen hay que cambiar. Como medir transformadores. Profesor robaron herramientas. Compañero arregló parlante con soldadura fácil. Siempre juntar la máxima cantidad de información posible. Dividir la etapa de control y de potencia para identificar falla más rápido. Donde estan los tornillos dependiendo el microondas. Si o si hay que comprar fusible de alta tensión. Componentes MO: Tiene 2 fusibles para alta y para baja. Forzador de aire elicoidal.  El que está arriba es un fusible cualquiera pero no todos son del mismo tamaño. Hay que conseguir fusible del mismo amperage y del mismo tamaño. Switch de puertas no son todos iguales en los microondas algunos traen 2, otros 3, otros 4. Algunos microondas traen térmicos arriba de la parte del horno, algunos arriba del magnetrón, no todos tienen. Switch sistema de seguridad para que no funcione cuando se corte la puerta. Si se cortó el fusible en la parte de baja tampoco no anda todo. Si uno de los switch ya juntó basura tampoco anda todo etc. Lo más común que se cambia en un microondas: magnetrón, fusible de baja o de alta, capacitor y el diodo. Función de la fuente: bajar la tensión y rectificar. La placa maneja muchísima potencia. Heladera . Luego de la entrada de 220 está el transformador. Para una fuente de 3 voltios puedo poner transformador de 12 voltios con un regulador de voltaje de 12 a 3, si recalienta demasiado el regulador de voltaje, hay que poner uno de 12 a 9 y otro al lado de 9 a 3. El único diodo que regula voltaje: diodo zener. Los últimos 2 dígitos del regulador te dice el voltaje. Después de bajar el voltaje hay que poner un puente rectificador de onda completa. Hay 4 diodos en un puente rectificador de onda completa. Como pasar de corriente alterna a continua: transformador usa puente rectificador, regulador de voltaje. Hay reguladores programables para la fuente switching que le hace trabajar al otocoplador y también tiene un componente totalmente distinto. Diodos dobles: cátodo común ánodo común. Con el rectificador de 15 bajó a 12. Diodos tienen caída de tensión. Corriente positiva del ánodo atraviesa el cátodo.Corriente negativa entra por el cátodo y atraviesa el ánodo. Luego del diodo hay una corriente continua con pulsos. Capacitor polarizado vuelve la corriente continua con pulsos a pura. Medir capacitor debe dar los faradios que dice. Hay lugares en donde poner el capacitor tampoco es bueno porque de ser puntante queda con un pequeña ondita, con bobina y capacitores se mejora eso. Si a una fuente capacisitva resistiva le agregas un regulador queda igual que una lineal switching pero no te puede dar mucho amper. Lo primero encontramos fuente lineal: transformador. Lo primero que encontramos en fuente switching: rectificador, en la switching no nos sirve los 50 hertz. Switching: diodo rectificador, capacitor antes transformador. Ningún transformador trabaja en CC hay que dotarlo de generador de pulsos. Oscilador y aparte un mosfet, porque el oscilador no soporta los 311 voltios. Si no me trabaja la parte secundaria tengo que medir mosfet, si el mosfet está bien entonces es el oscilador. Ahora en las fuentes switching viene el mosfet adentro. Controlador oscilador tomará los 311 voltios positivo con puesta a tierra y mandará pulsos para que de esa forma pueda trabajar el transformador en la corriente continua. Por convenio la corriente va del positivo al negativo pero no es así el que va de positivo al negativo es la tensión. La corriente va del negativo al positivo, pero así se explicó. Hay profesores que hablan de corriente pero en realidad se refieren a la tensión. Es la tensión no la corriente. En switching: CC no podemos bajar de 311 a 3 voltios, no se puede usar capacitores porque recalientan, tenemos que entrar en el transformador para tenemos que crear pulsos y usar un oscilador. El octoaclopador regula el oscildor. Finalidad de fuente: bajar tensión y rectificar porque alterna aunque sea 3 voltios no te sirve. Un sábado 1 de la tarde cerraron todas las tiendas y feriado lardo desde el miércoles hasta el jueves, si tengo un transformador de 4 voltios le pongo, le hago el puente rectificador y le hago bajar el voltaje  se me quemó la fuente busco un cargador de celular de 5 voltios le pongo la resistencia le bajo a 3, el chip ya funciona, pero todavía me falta una fuente de 24 voltios porque sino no puedo hacer funcionar mi relay. La bobina del relay pin 2 y 3 sirve para abrir y cerrar el platino. Los conductores tienen resistencia caida de tension. Relay: 1 al 4: corto. 1 al 5: abierto. 2 al 3 impedancia. Medir el platino: 1 y 4 cerrado. 1 y 5 abierto, sino puede ser que el platino esté sucio. A veces tiene 1 pernito en el medio por eso tratemos de buscar llave con agujerito en el medio, si tenés llave ciega no sirve. Transistor: base colector emisor. La carga: transformador, magnetrón, lo que hace uso de la corriente. Etapa de potencia se inicia en el transformador. El magnetrón tiene una saliente tiene un dedal con un agujerito en el medio porque el magnetrón es el encargado de acumular electrones de ponerlos juntos y disparalos El campo magnético del imán hace que los electrones queden en fila. 1 primario 2 secundarios. Lo primero que hacemos desconectar el transformador. El cliente se queja de la plata como siempre porque dice cambiaste una pavadita y me cobrate carísimo. Lo difícil es el análisis. Presostato por la presión del agua se cierra. El termostato por la temperatura . Los 3 tienen 3 cables el que está abierto se cierra y el que está cerrado se abre. Los 3 tienen 3 contactos, pero uno es por presión, temperatura y electromagnético. Termostato tiene una termocupla que varía la tensión de la batería y ahí pega o no un electroimán. Si la lámpara se encendió tengo que controlar desde el transformador al otro lado. Para sacar 220 de una batería necesito un octoacoplador y un oscilador. No hay forma de probar el magnetrón: El magnetrón sólo trabaja con medio ciclo y no se puede probar con 220 porque necesita 2000. Nunca probar el magnetrón arriba de la mesa. Hay formas de medir el magnetrón pero es muy difícil. El compañero se va sin decir CHAU (Hora 01:58:30) XD. Los técnicos miden la fuente le da los 311 voltios en el capacitor inmediatamente sacan el magnetrón y ponen otro, ahí recién miran el octoacomplador, el regulador, recién ahí. Magnetrón es metálico una parte tiene parte de porcelana (aislante). Con 3000 voltios trabaja el filamento. Los imanes del magnetrón NO se compran, hay que sacar y guardar. El filamento genera los electrones. Una vez que se rompió el filamento CHAU. Si pongo el tester en las dos patitas y toco el chassis y queda mudo quiere decir que está bueno, si suena quiere decir que está en corto, o sea que el filamento me marcó que estaba bien, pero cuando yo voy a revisar resulta que cuando yo toco una de las puntas que va para el filamento y toco cualquier parte de la chapa del magnetrón me da continuidad quiere decir que está malo porque tiene que estar aislado. Al medir el magnetrón si hay sonido es porque está en corto. Si te da bien tenés que mirar imanes. El imán no sirve roto.  Cuando sacás un magnetrón si o si tenemos que volver a poner en el lugar y con la puerta cerrada. En el bobinado primario vamos a tener en el conductor grueso 3 VOLTIOS. Cuando se trata de bobina siempre hay un principio y final. Ninguno tiene que tener continuidad con el chasis excepto el de alta. Lo que se bobinaba mucho: bomba de agua es la bobina la más para hacer, cortadoras de cesped, motor lavarropas cuando no existía el automatico se mandaba a bobinar. El transformador del microondas es de hierro al silicio.  LOS 2000 VOLTIOS NO LE SIRVE AL MAGNETRÓN, NECESITA 4000 VOLTIOS. Tenemos que hacer un circuito con un capacitor y un diodo.  Muchos dicen que la pipeta de este magnetrón es cancerígera.  Acá está la malla dorada bronce que algunos dicen que cuando está sucio no anda.  Cuando esa elicoidal no funciona no hay ventilación esto sobre calienta acá arriba suele ir un protector térmico se levanta entonces corta hasta que se enfríe.  Hay símbología de dinstinta de tierra para alterna y para continua.  Manejar un capacitor de un microondas que está apagado o que está acá y se desenchufó no debería traer peligro, pero el problema es que nosotros no podemos saber cuál es el estado NO SABEMOS SI ESA RESISTENCIA DE DESOLDÓ INTERNAMENTE SE CORTÓ BAJÓ SU VALOR. Siempre cortocircuitear. El diodo del MO trabaja de forma inversa va el cátodo a tierra. En un microondas el diodo puede aparecer en cualquier lado pero siempre tiene que estar a la salida, en un extremo el capacitor debe estar sólo en el extremo que no va a tierra. Uno de la alta va solo con el fusible, en el otro extremo si van todos. En el otro extremo va el diodo el capacitor y el magnetrón van juntos. En los últimos 5 minutos termina explicando como conectar una bornera aislada, es un imaginario para interpretar la conexión: son 4 conexiones pero aparecen 3 cables porque uno se toma como base del otro, si yo a ese mando todo al unir todo junto voy a tener 4 cables son 4 conexiones: capacitor, punta del de baja, diodo, magnetrón, en cambio del otro lado hay 1 sóla que es de alta ESTO GRABENLO EN SUS CEREBROS. Muchos dicen que la porquería más grande que colocaron en las hidros: la válvula de presión tiene un componente que activa el switch eso jode el orrin, porque le hace juntar presión para adentro. Hay que cortar por llave y hay que poner una abrazadera en el gatillo. A el lo que le paso es que le debaja un rato y no arrancaba era el termo del fusible, abrí el contacto y estaba oxidado el platino. Si vos le decís le soldé un cablecito no te pagan."
date: 2024-09-19T22:55:49-03:00
tags: ['electrodomesticos']
---
#### Audio de la clase en YouTube
https://youtu.be/kCyNtZ1t94s

#### Audio de la clase en Invidious
https://redirect.invidious.io/watch?v=kCyNtZ1t94s

#### Audio de la clase en Vocaroo
https://vocaroo.com/19Vtiubsk6Mq

### Medir relay

1-4 (Normalmente cerrado) debe dar corto  
1-5 (Normalmente abierto)  
2-3 debe marcar impedancia    

**El 99% de los técnicos sacan el chip, miden la fuente le da 311 voltios en el capacitor en el filtro, sacan el oscilador.** Si no le anduvo ahí recién mirará el octoacoplador, el regulador el controlador.

El magnetrón es metálico y dentro hay un filamento que trabaja con 3,7 voltios y lo otro es para crear la potencia del disparo de los electrones.
Para que le doy energía al filamento, porque ahí van a parecer los electrones y el imán los contiene.

Tiene que sonar o tiene que haber resistencia o sino se rompió el filamento y esa es la causa por la que no funciona el magnetrón.


El "chicote de prueba" era un enchufe con dos cocodrilo.

La parte de potencia se inicia en el transformador y termina en el magnetrón. Termina en el magnetrón porque tiene un dedal con un agujerito en el medio, porque el magnetrón es el encargado de acumular electrones y dispararlos como si fuera un laser.
El magnetrón agarra todos los electrones que está creando en un tubo de vacío y los pone en fila a todos.

Oscilador no se banca 220 voltios, sólo 3,5 voltios. Se usa el MOSFET para eso.
Si no anda la parte secundaria medí el MOSFET.   
Las primeras fuentes switching tenían el MOSFET afuera, ahora vienen adentro.

La gente dice equivocadamente capacitor de arranque, bobina de arranque.

El flujo de la corriente: es la tensión no es la corriente.

Calculadora no tiene fuente, tiene batería.

#### ¿ Para que sirven las fuentes ?
Bajar la tensión y rectificar.

El relay tiene 5 pines.
Entre los pines 2 y 3 hay una bobina y deberían dar continuidad.

Los pines 1 y 4 son normalmente cerrados tiene que pitar.
El pitido indica que está en corto

Solución rápida: enchufar transformador directo.

## Problemas microondas
Imanes: si se rompen hay que cambiar.

Deterioro antena.

**Nunca probar magnetrón arriba de la mesa, probarlo en el lugar y con la puerta cerrada y probarlo de forma muy breve sino es peligroso.**

Profesor: "Con el televisor recibí patadas de todo tipo con el microondas nada."

#### ¿Como se mide un transformador?
Se mide continuidad bobina.

Tiene 3 enrollamientos: 1 es el primario de alta (completar) (2:29:00)


## Imágenes: [https://imlauer.blogspot.com/2024/11/audioapunte-taller-reparacion-de_36.html](https://imlauer.blogspot.com/2024/11/audioapunte-taller-reparacion-de_36.html)


---

### Transcripción

Las últimas veces que le robaron parece como si le hubieran entrado con un camión, le robaron todo. Minuto 6 describe todas las herramientas que le robaron.



Profesor robaron herramientas. Compañero arregló parlante con soldadura fácil.

El ácido de la batería de la moto hace mierda todo

### Microondas
Tienen 2 etapas: etapa de control y de potencia.

#### Qué hay que hacer para revisar el funcionamiento de un microondas?
Tenemos 2 etapas en el microondas, tenemos que saber donde empieza una y donde termina la otra.
**Tenemos que dividir ambas etapas.**

En donde eso se une quiere decir que esta etapa tiene un comienzo, ¿por qué coloco 2 figuras?

Quiere decir que esto acá puede tener muchísimas etapas hasta llegar a su final, y acá voy a tener un principio. Acá voy a tener el principio de esta etapa y acá tendré final, **porque estoy separando la etapa de control y la de potencia**.


Tuvimos la mala suerte de que cuando fuimos a buscar el microondas nos atendió la empleada y no nos dijo cual era el problema que tenía. Siempre hay que juntar la máxima cantidad de información posible.

### Qué tenemos que hacer si no nos da ninguna información?
Desarmamos: puede traer 6 tornillos, 5, algunos suelen traer 2 abajo, hay otros que suelen traer de 1 lado, de costado abajo, no hay ninguna norma: lo que sí todos tienen un sistema de chapita que va enganchado en la parte del frente del gabinete, sacamos los tornillos que están atrás levantamos un poquito y tiramos hacia atrás.

Una vez que sacamos la carcasa nos quedamos con toda la parte del funcionamiento del microonda.

Vamos a encontrarnos con:
1. Transformador
2. Capacitor
3. Fusible plástico
4. Diodo más grande de lo normal (tiene que soportar alto voltaje)
5. Forzador de aire licoidal
6. Arriba de esa elicoildal vamos a ver una plaqueta electrónica (no es nada más que un fusible).

2 fusibles uno para la parte de alta y uno para la parte de baja.

El fusible de alta hay que comprarlo si o si porque es un fusible especial.

El que está arriba es un fusible cualquiera pero no todos son del mismo tamaño.

Hay que tratar de conseguir el fusible del mismo amperage.

7. Magnetrón
8. Del lado en donde traba la puerta vamos a encontrar switchs, no hay una norma de cuántos switch llega, hay microondas que trae 2, 3, 4.

Hay algunos que traen de un lado normal abierto, o normalmente cerrado y hay algunos de estos switch que la parte de arriba trae normalmente abierto y en el mismo switch trae normalmente cerrado.

No son todos iguales.


Todos son propenso a fallas, desde el fusible de baja, el térmico no todos los microondas traen.

El cable lin ??? si no fue bien montado el fasto, puede tener falla  (Minuto 21)

Vamos a suponer que no prende el foquito, pero resulta que sí hay corriente, entonces el problema que no le llega corriente.

Si se cortó el cable del enchufe ya no anda todo, si se cortó el fusible en la parte de baja tampoco no anda todo. Si uno de los switch ya juntó basura tampoco anda todo. Switch sistema de seguridad para que no funcione cuando se corte la puerta. 


Lo más común que se cambia en un microondas: magnetrón, fusible de baja o de alta, capacitor y el diodo.

Mucho de los artefacto que trabajan con electrónica suelen tener problemas en la placa, por eso hablamos de que es una fuente.

Tipos de fuentes:
1. Capacitiva resistiva
2. Switching o conmutada
3. Lineal.

La función de la fuente bajar la tensión y rectificar.

### Cuando hablamos de la fuente lineal significa que trabaja con la frecuencia de la línea.
El chip necesita corriente continua pura, no podés poner corriente alterna.


Es un voltaje de corriente alterna y el chip no tolera ninguna fluctuación de corriente. 

Dónde está la fuente en esta placa electrónica? Si pongo 220 conecta no porque yo acá tengo un chip que es como si fuera un procesador, tenemos un relay, un selector de funciones esto es una heladera.

Sin embargo tiene que tener fuente porque acá yo tengo un circuito integrado y con esto tengo que alimentar 3 voltios, si enchufo acá cuántos voltios estoy enchufando acá? 220.

Y acá me tiene que arrancar el motor y acá me tiene que arrancar la resistencia, maneja muchísima potencia la placa.

Sin mirar la frost porque el otro dice **mecánico no frost**.

Quiere decir que una de esas fuentes está acá, la heladera tiene transformador.

Transformador lineal: construido por hierro al silicio.

Para que sea una fuente switching que tiene que tener?

La primer fuente descartamos porque este transformador ya no está.

#### La 2da fuente dice fuente switching para que sea switching que debo tener yo como dato?
Tiene que haber otro transformador más chico de ferrita, que para poder llegar a que esa fuente funcione, cuando yo trabajo con una fuente lineal, tendré acá la entrada de 220 inmediatamente tendré el transformador porque tengo que modificar la tensión porque no puedo mandar 220 al chip, tengo que bajar a 12, 9. 

O sea para una fuente de 3 voltios puedo poner un transformador de 12 voltios, colocando un regulador de 12 a 3. Y si **recalienta** demasiado el regulador de voltaje, hay que poner uno de 12 a 9 y otro al lado de 9 a 3.

Tiene 3 patitas el regulador de voltaje (78xx)

### Qué pasa?
Tengo que buscar un 7803, 7805, 7809, 7812, 7832 (hay muchísmos), tenemos que buscar el que es para 3 voltios.

Los últimos 2 números te dicen el voltaje.

### Que yo tengo acá?
Corriente alterna, vamos a suponer que tengo 15 voltios, sigo teniendo corriente alterna, ahora tengo que poner un puente rectificador de onda completa también hay rectificador de media onda.

### Cuantos diodos hay en un puente rectificador de onda completa? 4
Minuto 40

Acá tengo 15 voltios

Hay reguladores programables para la fuente switching que le hace trabajar al otocoplador y también tiene un componente totalmente distinto.

Hay transistores mosfet.

Diodo común: ánodo común, cátodo común.

Llego al rectificador.

Con el rectificador de 15 me bajó a 12, porque los diodos tiene caída de tensión.

Acá tengo 12 voltios. Hasta antes del diodo rectificador tengo corriente alterna.

Pero ahora tiene que ser corriente completamente pura.

#### A partir del minuto 48 empecé a resumir tanto palabrerio.

Rectificar = baja voltaje. 

Con capacitor vuelve a 15 voltios.

Capacitor siempre será más alto que el de la fuente.

Capacitor se carga eléctricamente, bobinas magnéticamente.

Ahora vamos a poner un regulador de voltaje para llegar a los 3 voltios y ahora empezará a trabajar el chip queda en standby.

En las fuentes lineal lo primero que hay es un transformador.

En las fuentes switching lo primero que vamos a encontrar será el rectificador, no nos sirve los 50 hertz.

Vamos a tener capacitor polarizado

Ahora viene un circuito oscilador.

En una fuente switching lo primero que hay que hacer es ver el capacitor tiene que dar 311 el valor pico.

Oscilador: 8 patitas

Ahora el mosfet viene adentro en las fuentes switching.

### Controlador oscilador tomará los 311 voltios positivo con puesta a tierra y mandará pulsos para que de esa forma pueda trabajar el transformador en la corriente continua.

Van a encontrar en algunos texto que les dicen corriente alterna.

El profesor detesta cuando le dicen a la bobina común trabajo y arranque, el profesor cuestiona donde está el capacitor de arranque, bueno entonces no es de arranque. Es decir si no tiene capacitor de arranque no hay bobina de arranque.

Tenemos que respetar esos modismos pero nos tenemos que dar cuenta que no es así.

Cuando el lavarropas para de lavar entonces el plástico se tomó, lo que tenés que hacer es sacar la tapa de atrás sacar la correa tratá de girar sólo el tacho, si girás del lado de afuera cuidado porque esa rueda es muy filosa, por eso te recomiendo que vayas del lado del frente abres la puerta y trates de girar al tacho si no se puede está rota la estrella.

En switching: CC no podemos bajar de 311 a 3 voltios, no se puede usar capacitores porque recalientan, tenemos que entrar en el transformador para tenemos que crear pulsos y usar un oscilador.

Del otro lado hay un octoacoplador, él toma el voltaje de acá si en un pin hay 11 voltios, cuando hay 12 o 13 le manda una señal para que el oscilador baje.

Supongamos que sea 11 voltios pero llegó a 9 entonces le manda una señal para que el oscilador acelere, y así va regulando.

Cuando acá sea 11 quiere decir que acá será 3 voltios y acá 30.

Si acá se dispara va a quemar el chip, o sea esto que está haciendo acá.

Todas fuentes están hechas para lo mismo pero la conmutativa resistiva es me peor que esta.

La placa de la calculadora tiene batería no tiene fuente.

---

Hay mucho de análisis que estamos haciendo, qué estamos haciendo?

Vamos a suponer que este transformador de 12 es para el split, un sábado 1 de la tarde cerraron todas las tiendas y feriado lardo desde el miércoles hasta el jueves, si tengo un transformador de 4 voltios le pongo, le hago el puente rectificador y le hago bajar el voltaje hasta el voltaje que se necesite.

Vamos a suponer que un relay necesita 4 voltios, esta fuente dice 3-30 le pongo un regulador de voltaje de 24 le puedo mandar hasta 30 no pasa nada, ya tengo 24 para el chip.

Esto que está acá es sólo para que funcione esto y esto, se me quemó la fuente busco un cargador de celular de 5 voltios le pongo la resistencia le bajo a 3, el chip ya funciona, pero todavía me falta una fuente de 24 voltios porque sino no puedo hacer funcionar mi relay.

Cuántos pin tiene un relay? 5 pines.

#### Relay
En momento de reposo si coloco el tester en el pin 1.

Si existe campo magnético entre ellos y acá yo tengo electricidad gracias al primario sí es un trasnformador, sino son bobinas.

Esto son bobinas, los conductores como parte positiva conducen como parte negativa tienen resistencia.

Si pongo el tester acá me marcará algún valor en ohmios.

### Si coloco la otra punta del tester acá y la otra acá no me va a dar nada porque son polos distintos (no hay continuidad)

## Medición del relay
1 al 4 corto   
1 al 5 abierto  
2 al 3 resistencia  

### Herramientas para el taller: juego de llaves, que otra cosa herramienta?
- Juego de la llave alen (traten de buscar el que tiene el agujerito en el medio)
A veces trae un pernito en el medio y no se puede romper con nada.


Hora 01:30

El relay quiere decir que acá yo voy a poner 220 voltios y acá voy a poner el motor, y acá voy a activar con esta tierra (negativo) y este a 24 voltios, voy a tener que hacer todo manual, ya no necesitaré la placa, porque se me rompió la fuente.
O le voy a hacer funcionar con un cargador en los pines de 3 voltios del chip y tengo que alimentarle acá tiene que haber un transistor: base colector y emisor.


Alumno: le desarmé todo y gira pero calienta demasiado pero no tiene la fuerza.
Falta de limpieza, lubricación, capacitor etc.

### Estamos en el microondas o sea que tenemos una etapa inicial en donde enchufamos y tenemos una etapa final que es la etapa de control que hace trabajar a la etapa de potencia.

La carga: transformador, magnetrón, lo que hace uso de la corriente.


### Vamos a tener una etapa inicial de la etapa de poder que será el transformador
Y termina en el magnetrón, porque el magnetrón tiene una saliente tiene un dedal con un agujerito en el medio porque el magnetrón es el encargado de acumular electrones de ponerlos juntos y disparalos como si fuera un laser.

El campo magnético del imán hace que los electrones queden en fila.

Si una señora te dice que el microonda no calienta.
## Separar
Inmediatamente separo la etapa de control sacar los fasto porque ahí está la bobina primaria.

Esto que está acá es un paquete, es una bobina empaquetada en un papel especial que se usa como aislante, y acá abajo tengo todo el bobinado del primario. 

O sea que esto que está acá también lo tengo acá.

El azul es el bobinado secundario, el verde bobinado primario.

Acá habrá otro bobinado que estará entre el bobinado, entre los dos paquetes hay un cable muy gruesos que tiene 2 o 3 vueltas nada más.

O sea que tengo 1 primario, 2 secundarios.

Este es de 3,7 voltios por eso es cortito la vuelta.
Y este que está acá es de 2000 voltios, o sea que los transformadores que vimos hasta ahora son transformadores reductores de voltaje porque le ponía 220 en el primario y en el secundario tenía 15-17 voltios.

Acá tengo un transformador reductor y uno elevador de voltaje.

En el transformador reductor: tengo 3,7 voltios

En otro transformador tengo 2000 voltios.


Cuando colocamos el microondas desconecto el transformador, me quedará un final y un principio.

Hora 01:45 

Todos los transformadores que vimos hasta ahora son transformadores reductores de voltaje porque yo le daba 220 en el primario y en el secundario tenía 15/17 voltios.

Acá tengo un transformador reductor y otro elevador de voltaje, en el reductor tengo sólo 3,7 voltios y en el otro tengo 2000 voltios.

### Lo primero que hacemos es desconectar el transformador
Me quedará 1 final y 1 principio.

En el final en donde tengo los dos fasto.

Agarraré una serie, y la colocaré acá dentro y voy a enchufar esto a mi fuente de corriente alterna.

### Si todo funciona bien mi lámpara enciende.
Yo saqué del transformador enchufé cerré la puerta, coloqué el programa y prende la lámpara, esto quiere decir que mi etapa de control está buena.

Si yo vuelvo a enchufar esto acá tiene que andar de maravilla.

Yo coloco esto acá vuelvo a enchufar mi fuente mi toma corriente, pongo una tasa con agua se escucha que anda calienta el agua que pasó??

Puede haber problemas en los enchufes de la casa de la señora, si está bien el enchufe puede ser que esté un poco estrangulado el cable.

Si es el cable que hace falso contacto, todos cortamos el cable y enchufamos.

Un relay cuesta entender porque nos cuesta entender la electricidad y el magnetismo, porque sino rápido lo sacamos.

### Yo les puedo hablar de un presostato, termostato, un relay nada que ver una cosa con la otra.

El presostato si trabaja como switching cerrará el switching cuando haya presión.

El relay trabaja con campo magnético, 

Nada que ver con un termostato que se modificará de acuerdo con la temperatura.

No hay que medir todo, hay que saber separar.

Acá me dió que está bien porque la lámpara se encendió quiere decir que desde el transformador para acá tengo que controlar.

### Que voy a hacer con mi chicote de prueba?
Para que lo saqué para trabajar? Voy a probar la parte secundaria, como yo saqué esto lo voy a enchufar ahí enchufo en la fuente y todo debería funcionar.


Yo anulé la parte de control.

Si yo tengo que cocinar algo en mi casa, lo conecto directo. Lo voy a tener que desenchufar y enchufar si no tengo la parte de control.


Alumno: "Cocina eléctrica no le corta el termostato a la ornalla, le quiere poner directo, vamos a cambiar la resistencia si hacemos eso?"
Profesor: "No conviene hacer nada porque el termostato está para eso."

Para cortar el termostato tiene una termocupla y tiene que estar en posición y tiene que estar bien.

La termocupla del calefón es un sí no. El termostato de la cocina eléctrica es lineal.

Vos creés que el que fabricó eso no le pudo haber colocado un mejor termostato de más temperatura pero le dura 2 horas, ni eso 


Entonces con un chicote de estos yo coloco acá y pruebo, y se escucha que anda.

### Cuando yo saco miro fría el agua, que está pasando?
Descartamos el transformador.

Cuando nosotros escuchamos que anda el que vibra es el transformador. Acá también hay una especie de fasto. 

Yo podría agarrar este probador mandarlo al magnetrón para ver si es el magnetrón. NO no es cierto??? Por qué? Porque el voltaje es muy bajo 220 aparte el magnetrón necesita trabajar casi a medio ciclo por eso tiene diodo.

No hay forma de probar el magnetrón. 

Hay varios modelos del magnetrón, hay que sacarle y ponerle otro que mejor se adapte, si calienta adentro entonces el magnetrón está mal.

## Medir magnetrón
Es difícil el control exacto del magnetrón existen formas de como controlar, el magnetrón esta parte es todo metálico, salvo una parte de porcelana.

### Filamento con cuántos voltios trabaja? 3000 voltios.
Acá dentro del filamento, el filamento trabajan con 3000 voltios. Y lo otro es para crear la potencia el disparo de los electrones 


Entonces este conector que está acá es una cosa más o menos de plástico **(cual será el conector)**, antes era de muy buena calidad. Dentro de este hay una bobina de cada lado. 

## Probar magnetrón
Una de las formas de probar es poner el tester en continuidad y medir la continuidad del filamento.
 
### Para qué necesito encender el filamento?
Una vez el profesor cambiando imanes perdió el filamento.

Alumno: "Se compran esos imanes?"   
Profesor: No

### Entonces esto para que sirve? Estos fasto machos? Para darle energía al filamento para que? Porque de ahí aparecerán los electrones. Y ahí quedarán locos los electrones.
Si yo toco acá que tiene que pasar?

Pongo en continuidad mi tester que haber una impedancia, sino quiere decir que se rompió el filamento. Si todo lo otro está bien ya no sirve, si todo lo otro está mal ya no sirve.

Una vez que se rompió el filamento CHAU.

### Una de las pruebas es medir la continuidad de estos terminales a ver si tiene impedancia

Coloco en ambas patitas y toco el chasis
Coloco acá en el fasto y todo el chasis está mudo como ahora.

Agarro la otra patita toco el chasis está mudo como ahora que pasó? ¡¡¡Está bueno!!! (Hora 2:05)

Ahora yo coloco acá y coloco en la chapa significa que está en corto.

#### Si pongo el tester en las dos patitas y toco el chassis y queda mudo quiere decir que está bueno, si suena quiere decir que está en corto.

## o sea que el filamento me marcó que estaba bien, pero cuando yo voy a revisar resulta que cuando yo toco una de las puntas que va para el filamento y toco cualquier parte de la chapa del magnetrón me da continuidad quiere decir que está malo porque tiene que estar aislado. 
# Está en corto
# Quiere decir que el filamento me marcó que estaba bien pero cuando voy a revisar resulta que cuando yo toco una de las puntas que va al filamento y toco cualquier parte de la CHAPA del magnetrón está malo porque tiene que estar aislado, no debe haber sonido.

Estos si venden hay que cambiar este y hay que cortar. Acá está soldado como si estuviera derretido como una soldadura de puntos así está soldado porque ambos son un alambre grueso de cobre, está soldado por fundición, tenemos que agarrar un alicate y tenemos que cortar acá.

De acá para acá no sirve porque es eso lo que está mal porque es eso lo que está aterrizado en la tierra, de acá adentro del magnetrón todo sirve, acá nosotros cortamos.


Nosotros vamos a la casa del repuesto y compramos esto, esto es de plástico.


Hay veces que acá traen suelen traer dos machocitos. Tiene que ser con cuidado porque si somos brutos se corta el filamento por el golpe por la vibración es lo mismo que un foco.

Sino con un taladro livianito tratamos de comer el machecito.

Si tenemos un remacho remacho, no puede ser un remache a golpe tiene que ser con la pistola o sino tornillito chico con tuerquita.

Ahí medimos de nuevo NO da continuidad es probable que ya funcione. **(DONDE ESTÁ ESE REMACHE???)**

### Esta parte no entendí bien, hora 02:09:10
O sea que el remache hace que no esté bien aislado el microondas.


Supongamos que no pasó que yo toqué acá y no da nada, DA ABIERTO. ESTÁ BUENO, entonces que tengo que hacer? Colocar una buena luz y entrar a mirar el magnetrón, voy a ver si el compañero trae para la próxima clase. (NO LO TRAJO)

### Que tengo que hacer?
Traer la luz al magnetrón y mirar el estado de los imanes.

Porque es muy común que esos imanes se partan.
El imán no sirve roto.

Hay que mirar detenidamente para ver si algún imán está roto.

Si está roto ya no puede juntar los electrones, vamos a suponer que tiene que tirar por décima de segundo 10 millones de electrones a lo mejor tira 1 millón.

Cambiá los imanes de los magnetrones viejos que fuiste guardando.



### Si se rompió el filamento que repuesto nos queda
Los dos imanes y la ficha.

Si ustedes quieren desarmar y guardar en una cajita pero corren el riesgo de que va a pasar de una cajita a la otra.

Hasta ahí se puede revisar un microondas.

No lleva capacitor en el magnetrón.

---

### Que otras cosas le puede pasar a un magnetrón?
Se suele deteriorar la antena, se suele quemar se agranda el agujero puede ser que no haya un laser, cuesta calentar, cambiamos esa antena, en algunos magnetrones son diferentes pero no hay problema.

Ya probamos el transformador? No. Tiene 1 bobina primaria y 2 secundarias.

El magnetrón ya probamos completo todo.

La otra que faltaría es cuando ya te rompés la cabeza hiciste todas las medidas, pero no calienta hay algunos que en la boquilla hay una malla de color bien amarillo como si fuera bronce oro, dicen que cuando esa mallita se en sucia con el residuo de las comidas que se cocina adentro dicen que **suelen tener problemas el magnetrón**, A MI NUNCA ME PASÓ. Sí leí.

Es como que pierde eficiencia el vacío que está dentro de la porcelana (A MI NUNCA ME PASÓ)

## **Lo mejor que hay es traer otro magnetrón y ponerle**

Otras de las cosas que medimos el iman si está todo bien, hay que cambiar el magnetrón.

Cuando es para el cliente es lindo porque paga él.

Todo lo que estoy enseñando acá es acá arriba desenchufado.

### Cuando sacás un magnetrón si o si tenemos que volver a poner en el lugar.

### El magnetrón tiene que ir en el mismo lugar, porque sino es peligroso, y la puerta tiene que estar cerrada.

# Todas estas pruebas estando acá arriba cuando se va a enchufar tiene que estar todo en su lugar
Es el electrodoméstico más peligroso de todos.
### Que todos las pruebas que sea lo más cortito posible

Con los televisores recibí MILES de patadas de todos los voltajes, pero con el microondas nunca.

Con este transformador cuando le conectamos la energía en el bobinado primario vamos a tener en este conductor grueso que está acá... Cuántos voltios? 3 VOLTIOS.

Luego saldrá uno más finito con un **porta fusible**, este es el fusible es especial porque es para 2000 voltios.

Ahora yo acá estoy poniendo principio y final, venimos bien!?


El final de la bobina secundaria está montada acá, sale de acá un alambrecito y va montada ahí o sea que si yo agarro el transformador y dejo este para el lado de atrás y este para el lado de adelante, mi transformador hará así??? (HORA 02:22) Acá va a estar el paquetito de alta, ....
Acá venía un par de vueltas el de 3 VOLTIOS. Y ahora (ver foto) acá viene el bobinado del primario (el verde).

Acá voy a tener un secundario con un fusible, y el otro va a estar acá, o sea que si enchufo el primario y coloco el negro acá y en cualquier parte del transformador que pasa? Son 2000 voltios.

Acá está el principio y acá esta el final y acá está el principio, **ASÍ TRABAJA EL TRANSFORMADOR**.

Alumno: "El fusible de baja tensión capaz que si ponés un fusible y no es de alta tensión capaz que no va a cortar, porque ... El fusible común en alta tensión no corta nunca porque como es alta tensión.. "  
Profesor: "O sea el de baja tensión no va a cortar nunca el de alta?"  
Profesor: "No no, vos fijate que con 2000 voltios el mínimo amperage que hay es alta la potencia"
Alumno: "Como un rayo se arma mucha diferencia de potencial por más que no haya por más que no haya ... Pasa igual la tensión se arma un arco eléctrico"
Profesor: "Ah ahora entiendo, hasta ahí venimos ... XD, **no le contestó?**"

### Como servía el transformador? Se mide la continuidad de las bobinas
No puedo enchufar acá los 220 voltios y medir los 3 voltios y medir los 2000 voltios acá porque no hay **herramientas para eso** aparte es muy alto el riesgo.

# Entonces no es muy aconsejable hacer ese experimiento XDD (HORA 02:27:10)
Profesor:Yo sí experimento y enchufo XDD

Ninguno tiene que tener continuidad con el chasis excepto el de alta.

El de alta sí está puesto al chasis.

### Cuantos tipos de enrollamiento de alambre tiene este transformador? 3.
Tiene 3, cuáles son?
1. 1 primario (de alta).
2. 2 secundario (2 de baja)

El fusible de alta, el único de alta es el rojo.

La bomba de agua era lo que más se arreglaba.  
La bomba de agua es la bobina la más para hacer.

### Lo que se bobinaba mucho:
1. Bomba de agua
2. Cortadoras de pasto
3. Motor lavarropas cuando no existía el automatico se mandaba a bobinar.

Los ventiladores no se hacen porque es muy chico el alambre, bobinar no es nada, soldar todos los alambrecitos eso.

Cuando agarraba los primeros lavarropas de este tipo hay veces que sólo te traen la placa de un EX?? (Hora 02:41) tiene componentes con funcionamiento electrónico que otros lavarropas no tienen, tienen mecánico.

### Si yo hiciera sólo moto y dentro de la moto hago salera, listo.
Siri me retaba mucho. El profesor después de 20 años decidió volver al taller y empezó a estudiar electrónica. Siri le decía que deje que no iba a entender, hace poco le dijo que en su reencarnación estudiará electrónica, como él se quedó atrás con la informática.
La calentura de la pollera te hace mierda, te hace perder oportunidades.

#### La 1er parte es el transformador, del transformador tenemos que llegar hasta el magnetrón.

Porque tenemos que llegar hasta el magnetrón porque ahí se realiza la función de las ondas que calentarán dentro del recipiente o sea que el magnetrón será **la única carga**.


Es para que todo el motocompresor arranque y tire el frío que está acá, con el magnetrón ocurre eso.

Hora 02:46:24

Entonces ya pusimos en funcionamiento el transformador y obtuve 3 voltios que le voy a mandar al filamento y 2000 voltios que le tengo que mandar a la parte de alta del magnetrón.


LOS 2000 VOLTIOS NO LE SIRVE AL MAGNETRÓN, NECESITA 4000 VOLTIOS.
Tenemos que hacer un circuito con un capacitor y un diodo. Con una configuración que se llama doblador de voltaje, si pongo 3 voltios la salida es de 6 voltios porque duplica el voltaje.

El magnetrón necesita 4000 voltios para poder disparar esos electrones a la velocidad que tienen que ir.

Si yo tengo el magnetrón voy a dibujar sólo la parte de acá atrás.

Acá tenemos el magnetrón, de esta tapita entra un pin y otro pin, en esos pin va puesto una bobina y va soldado a los pines que van adentro de una porcelana de vacío que va dentro del magnetrón y ahí termina en el filamento, esto viene acá acá parece un PIN desde acá viene soldado como fundido un alambre de cobre más grueso que este donde debe tener unas 9 texturas más o menos.
Y de ahí va soldado con el otro pin que va hacia dentro, lo que nosotros ponemos acá va para allá dentro.
### Desarmar
Ahí se ve una forma de transformador.
Acá está el paquetito que les decía y acá abajo está el bobinado del primario.

Acá está de nuevo el magnetrón en el mismo perfil, acá otra vez en el mismo perfil que estaba allá esta tapita se saca tiene como un doblez acá hay que ir enderezando con cuidado por favor no golpear porque te vas a quedar sin filamento todo se levanta y se abre acá para cortar y sacar, acá van 2 remaches.

Tiene que ir para arriba porque acá hay como un labio ???, hay que sacar para cambiar y acá está el magnetrón acá está la antena donde dispara del lado de adentro la fuga de electrones y acá está la malla dorada bronce que algunos dicen que cuando está sucio no anda.

Muchos dicen que la pipeta de este magnetrón es cancerígera.

Esto es lo que va amurado a la caja, acá hay un imán y acá está el otro imán.

Esta es la parte que yo les mostraba como que es todo un vacío estas aletas que están acá es para refrigerar el magnetrón, son disipadores de calor porque incluso de este lado hay un forzador una elicoidal, cuando esa elicoidal no funciona no hay ventilación esto sobre calienta acá arriba suele ir un protector térmico se levanta entonces corta hasta que se enfríe.

Este es el imán y este es el otro imán, esto se suele rajar pero se puede rajar de cualquier lado, hay que mirar con cuidado.

Las aletas están bien que estén juntas no hay problemas en las aletas.

Este es un capacitor de más o menos de 0-90 a 1,1 microfaradio hay de 0-90 0-87. Ahí está midiendo la base de adentro con el de afuera (ver foto)

Profesor: Esa medida no dará nunca, algún día podés agarrar uno pero porque ya cortó y se ve a la vista. (prueba de corto circuito no existirá nunca ver foto)

Son capacitores de bajo valor:
* 0-87microfaradio
* 0-90 microfaradio
* 0-95 microfaradio
* 1 microfaradio
* 1,1 microfaradio


### Hay una parte bastante complicada a mi siempre me costó entender claramente porque tiene sus problemas.

Les dibujaré un diagrama 

Entonces será:  (ver fotos)

Primario del transformador. Esto es tierra de corriente alterna? Y hay otro símbolo para corriente continua.

Se va un alumno (Hora 3) XD

### Dibujando... (Hora 3)
Ver fotos

Este HV (high voltage), el diodo y el capacitor es para alto voltaje,

El transformador ya tengo dibujado y el magnetrón también.

#### Que componentes me está faltando ahí ?
Capacitor y diodos.

Algunos capacitores traen acá marcado una resistencia, este es el dibujo del capacitor.

Y este es el dibujo de la resistencia, y este es el de la bobina.

Entonces muchos capacitores tienen al lado una resistencia que dice 1 MegOhm.

Porque esta resistencia cuando se les enchufa el microonda, esta resistencia pone en corto los dos extremos y consume porque quedó cargado el capacitor como todos los capcitores para que no tenga peligro..

Manejar un capacitor de un microondas que está apagado o que está acá y se desenchufó no debería traer peligro, pero el problema es que nosotros no podemos saber cuál es el estado **NO SABEMOS SI ESA RESISTENCIA DE DESOLDÓ INTERNAMENTE SE CORTÓ BAJÓ SU VALOR**

Dice que carga hasta 2000.

#### Qué falta dibujar ahora?
El diodo, este diodo trabaja en forma inversa, porque va el cátodo a tierra.

No podés saber si es el principio o el final porque es corriente alterna, una de las puntas cualquiera va ahí.

Acá está una punta del capacitor entonces una punta de este capacitor va al diodo lo que sí hicimos es una punta del de bajo voltaje y una punta al magnetrón, tengo salida de alto voltaje uno con el diodo y uno con el de 3 voltios y va junto al magnetrón, entonces uno este con este. Qué tengo que hacer yo? Unir el de alto voltaje adonde? Y qué me queda ahora? El de bajo voltaje, y eso va al magnetrón. Y ahora el diodo va acá.

En un microondas el diodo puede aparecer en cualquier lado pero siempre tiene que estar este circuito un extremo de bajo voltaje con la salida del capacitor con uno de estos.


