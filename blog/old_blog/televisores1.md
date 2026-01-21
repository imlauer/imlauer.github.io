---
title: "Televisores: En la 3era clase se enseña fuente standby no prende"
tags: ['televisores']
---
### 1era parte
Con los televisores TLC tenemos 8 bloques principales.

Son los siguientes: pantalla requiere del bloque de control de pantalla.
Ahí se habla de la defección vertical y horizontal.

Este bloque de pantalla es para que ella dibuje la imágen.

La información de la imágen proviene de un 3er bloque llamado VIDEO.

Además de video tenemos audio tenemos que agregar el bloque para el audio.

Luego el video proviene de un bloque llamado sinto (sintonizaador), el sintonizador captura señales de televisor por aire y por cable tenemos una fuente de audio y video.

Y hay otra que se llama auxiliar y es para cuando ingresamos al televisor señales de audio y de video proveniente de un dvd o un decodificador.

Todos los televisores modernos son controlados por el microprocesador y vamos a llamar ese bloque como de control.


Y vendría a hacer el bloque número 7.

Todos requerirán de energía eléctrica y necesitaremos de una fuente principal ese es el último módulo que sería el nro 8.
 
##### Modulo
1. Pantalla   
2. Control para pantalla   
3. Video   
4. Audio   
5. Sintonizador   
6. Bloque de entradas auxiliares   
7. Control   
8. Fuente   

Refiriendonos a la alimentación a la fuente inicialmente cunado conectamos el televosr la fuente principal me entrega una primera fuente que se conoce con el nombre de standby que es un voltaje bajo para alimentar el 3.3 voltios para energizar el microprocesador.

Esta fuente principal me entrega a los televisores principal una fuente de poder para energizar el control de pantalla se le conoce con el nombre de B+, **oscila entre 95 voltios y puede llegar a ser +145 voltios de corriente continua**.

Esto con solo conectar el televisor, **acá todavía no encendió el televisor**, cuando damos la orden power on, el **bloque de control entrega una orden para la fuente principal,** con el fin de que la fuente principal entregue un voltaje para el módulo de video.

El modelo y la marca puede diferir un poco en si la fuente realmente sale de la fuente principal, puede que esté presente y esté controlado por un circuito integrado de por medio. Cuando el módulo de video recibe el **VCC** de que funcione en algunos casos el **VCC** se puede hacer presente con solo conectar el televisor (modo standby) pero la orden de encendido no le llegará hasta que no se de la orden power.

Digamos que está con VCC y que la orden power on la entregue el microprocesador, con eso el bloque de video entrega una señal de control para el módulo de control de pantalla con el fin de que entonces ya este módulo de control de pantalla entregue los voltajes que necesita la pantalla para funcionar y a la vez el módulo de video está listo para entregar las 3 señales necesarias de video que requiere la pantalla: rojo, verde y azul.

La fuente principal le tiene que entregar al módulo de audio su B+ o VCC puede recibir cualquiera de los dos nombres, para que el módulo esté habilitado se puede dar que en algunos con solo conectar el televisor junto con la fuente B+ este voltaje se haga presente en el módulo de audio, pero no funcionará hasta que no le llegue una orden del microprocesador: una orden on o op, o mute (silenciar).

Lo que me hace falta es la señal de audio, la señal de audio sale del módulo de video. Del modulo de video sale las señales R y L para el modulo de audio.

Todavía no tenemos audio ni video porque al módulo de video todavía no tiene señal.

Si la vamos a aplicar de sintonizador se requiere que tenga su VCC (alimentación).

Además de que la señal de audio y video ingrese al modulo procesador del video.

El sintonizador captura el canal a través de la antena de aire o del cable y lo entrega al módulo del video, en muchos casos esa señal viene integrada con el audio, en algunos modernos el sintonizador entrega el audio y el video separado.

Por una sola linea ingresa ambas la del video como la del audio.

El sintonizador requiere de varios voltajes.

Análisis de una cantidad de fallas que de entrada nos servirán en donde posiblemente hayan causas que lo llevarán al módulo en donde hay que buscar el daño.

### 2da parte.
Repasemos los bloques con los nombres actualizados.

1. TLC: tubo de rayos catódicos.
2. V-H para referirnos a la deflexión horizontal cuando escuchamos hablar del horizontal o vertical.
3. El 3 continúa llamándose video.
4. Audio
5. Sintonizador
6. Módulo de control entradas auxiliares.
7. Micro
8. Power Supply (PS).

Desde el power supply sale la fuente standby y la energía que requiere el micro para estar debidamente energizado.

Para que el micro funcione requiere de esta fuente de standby. Ese voltaje es de 5 voltios (standby) con eso se alimenta el procesador, en los más modernos es 3.3V.

La power supply nos entrega para el modulo vertical y horizontal o modulo de control para la pantalla que es llamado +B o B+.

Cuando escuchás como está el +B se está refiriendo a esa fuente que sale de la fuente principal y llega a este modulo.

#### El +B puede estar entre 95 voltios y 145 voltios. A más pulgadas más voltaje.

Ahí todo está normal en algunos casos la powersupply entrega el voltaje para el modulo de video, normalmente está entre 9 voltios o 12 voltios. Con eso el televisor no enciende.

Para que empiece a funcionar necesitamos que la powersupply energice todos los módulos.

Si el módulo de video ya se energizó falta la orden de funcionamiento, eso la da el micro.

En algunos casos esa orden lo que hace es activar una fuente interna para que el voltaje que está acá en la entrada del modulo en otro lo que hace es suspender una señal que cuando este modulo está encendido se viene para el módulo de control de la pantalla o el módulo V/H.

Si analizamos vemos que inicialmente el módulo V/H está energizado más no activo requiere de esta orden o de este control para que funcione el módulo del video está energizado más no activo hasta que no reciba la orden ON procedente del micro que es el que lo está controlando y en algunos casos cabe aquí enfatizar que había que hablar de que el micro también entrega una orden o una señal para la power supply con el fin de que entregue los voltajes a plenitud o al máximo que quiere decir con eso que muchas veces vas a encontrar televisores donde este +B por ejemplo que normalmente por poner un ejemplo de 115 voltios normal resulta que cuando conecta el televisor y mide la salida de la fuente o mide +B no lo encuentra en 115 sabiendo que el normal es de 115 y puede engañarnos creyendo que el voltaje está mal **resulta que lo encontramos por decir algo en 70 voltios o en 90 voltios muy por debajo del normal**.
###### Es muy posible que no esté dañada la fuente, sino que la fuente está en modo ráfaga (modo de reposo standby).

Entrega toda la potencia cuando el micro le entregue la orden o cuando le dice el micro ahora si al máximo, hace esto con el fin de ahorrar energía cuando el aparato está en reposo.

Entonces esto no significa que esté dañada la fuente.

El voltaje de standby sigue estando igual ese no se puede reducir porque si se reduce o si lo vemos reducido ahí el problema es de la **fuente standby**.

Standby está diseñado para digamos una suplir de éstas está diseñado para que cuando estemos en modo ráfaga de todas maneras me entregue voltaje suficiente para el micro.

Cuando el modulo V/H funciona entonces el va a entregar los distintos voltajes que requiere la pantalla para funcionar son muchos los voltajes. Los vamos a estudiar en modulo 13.

De acá salen también unas señales de control.

Cuando llega esa orden es cuando ese módulo le entrega los voltajes necesarios al tubo trc mientras tanto no vamos a tener funcionamiento correcto en la pantalla y habíamos dicho que junto con la orden que da el módulo de video para este módulo de control de pantalla íbamos a los 3 colores o las 3 señales de color que van a la pantalla con información de el video que se conoce con los nombres de R de red, G green, y B blue (RGB).

#### 3era parte.

Hasta acá sólo tenemos una parte del televisor energizado así que continuando con el tema tenemos lo siguiente ya con eso tenemos una gran parte del televisor encendido sin embargo no vamos a tener imágen tenga en cuenta no vamos a tener audio porque todo está todavía desconectado.

#### Lo que se va a necesitar para por ejemplo haya audio pues mínimo que el módulo de audio esté energizado que tenga un VCC y las señales de audio que en los últimos televisores de estéreo serán dos señales R y L - r de right y l de left.

Esas señales salen del módulo de video hay excepciones como que llegan directamente del sintonizador pero es muy particulares.

En algunos modelos los sintonizadores entregan audio puro análogo es decir si yo coloco unos audífonos ahí puedo colocar un rastreador de señal y voy a escuchar el audio perfectamente y a la salida del video si yo lo aplico ahí un osciloscopio o si llego esa señal a un amplificador de video análogo puede tener la señal perfectamente porque lo entrega puro **pero esto es un caso especial**.

Normalmente entonces el audio sale del modulo de video después vamos a ver porque bien aún así si tuviéramos el modulo conectado incluso con su speaker o con su par de parlantes aún así no tenemos audio porque no tenemos una fuente que no está entregando ese tipo de información ¿qué tipo de fuente? un dvd un decodificador o un canal sintonizado por aire o por cable entonces si pensamos en el sintonizador lógicamente tiene que venir de acá e ingresar al módulo de video si estamos pensando en él módulo auxiliar lógicamente pues él es el que entrega esa señal cuando aquí vemos un / cuando le conectemos un decodificador por ejemplo tengo en cuenta esto.

Normalmente la señal que entrega el sintonizador al módulo de video es una línea en realidad es un cable coaxial (cable como de micrófono aislado) con una sola línea y el otro es el blindaje esa línea es especial lleva la información trae la información de audio y video en un formato que lo vamos a estudiar como FI (frecuencia intermedia)

Entonces tenemos nuestro sintonizador conectado a nuestro módulo de video pero le falta el voltaje VCC o una alimentación porque todo servicio electrónico necesita de una alimentación de un VCC.

El sintonizador en realidad requiere más de un voltaje pero por ahora dejemos que solamente es que necesita energía y que esa energía la coloca una fuente y parte de esa fuente está en la power supply pero que también hay un control que lo tiene el micro para cambiar el canal.

Podemos dibujar que del micro sale unas señales de control para que lo tengamos en cuenta eso el audio tmb tiene una señal de control para controlar el volumen y esa señal es controlada por el micro.

Ahora podemos analizar ciertas fallas o por lo menos ubicar ciertos módulos o ciertas condiciones que nos indiquen dónde pudiera estar una falla.

#### Hablamos de una falla FATAL.

La fuente no entrega ni la fuente standby, sin standby el televisor no prende (Minuto 07:12) por más que los demás módulos están buenos no están energizados no van a funcionar entonces primero tenemos que solucionar el problema de la fuente standby.

**Le damos la orden de encendido y no pasa nada.** Si medimos la fuente +B no la encontramos está dañada, sólo tenemos la fuente standby. 

¿Que pasaría ahí?

Cuando le damos la orden power el micro no hace su función.

Mínimo la que indica el módulo de video pero antes recordemos que hay unas fuentes que debemos chequear antes de seguir... (Minuto 09:30) +B  

Vamos a escuchar a hablar del jungla se refiere al modulo de video. Microjungla es el procesador.

Puede ser rectangular de pines tipo peine dual o tipo cmd que va soldado por debajo.

Entonces eso es un chip que integra a los dos tanto el micro como el jungla que son los últimos modelos que salieron dentro de un solo chip puede ser cuadrado con sus distintas terminales.

Microjungla = dos modulos dentro de 1 solo chip, siguen siendo independientes. Cuando la fuente standby está bien entra a energizar solo la sección del micro dentro del chip no es que energice todo el integrado sino solamente la sección del chip. 

Si el micro tiene el diseño de que recibe los 9 voltios para su funcionamiento de una parte del jungla imaginemos que esté aquí CBS de 9 voltios pues lo va a tener y lo vamos a encontrar ahí presente sin embargo el micro todavía o el jungla no lo vamos a encontrar funcionando porque aún no recibió la orden de control, la orden de control se la da el micro. Así esté energizado no funcionará y al no funcionar no entregará su orden que va para el módulo vertical y horizontal entonces ya podemos ir digamos sacando conclusiones o haciendo un buen análisis para poder de que el jungla trabaje recordemos que tenemos que chequear que tenga el voltaje y que tenga la orden de control.

Tiene el voltaje +b pero está caido porque la funte todavía no ha salido del micro yo **no debo ir a buscar daños aquí en el módulo horizontal, ni en la pantalla ni en el audio ni en el video** salvo en el **MICRO**. El micro es el que no me está entregando la orden hacer eso que buscaré en otros módulos equivale a buscar el daño donde no está y nunca lo vas a encontrar y esl o que vas a ahcer es perder el tiempo y plata.

#### Si el +b no está correcto debo verificar si es que el micro no está entregando la orden o si es que la fuente realmente está dañada y no depende de la orden del micro.

#### Ahí necesitaríamos ver el diagrama para asegurarnos que necesita de ese control.

Hay que saber si esa fuente requiere de una orden del micro para trabajar a plenitud  si es que la encuentro caída pero ya podemos irnos ubicando y expresarnos bien ante una consulta siendo más específicos para una mejor ayuda.

La pantalla no puedo pretender que la pantalla me funcione si el módulo V/H no está trabajando.

Si el módulo V/H está trabajando pero el de video tiene problemas para entregar sus señales de video pues tal vez tenga algunos funcionamientos de la pantalla tenga una respuesta pueda yo comprobar eso pero me falta todavía la señal de video claro eso es otra parte que tenemos que estudiarlo en detalle.


Tengo la pantalla dándome lo que llaman el rastro es más me da menú sube volumen baja si le aplico señal por el módulo auxiliar me responde veo bien el video solo el problema es con el sintonizador entonces debemos buscar el fallo en el **SINTONIZADOR**.

Empezando con los voltajes como la alimentación porque aún si el sintonizador está buena perfectamente sano, sino tiene voltaje **está muerto**.

La otra condición es la **señal de control** ahí hay una parte muy amplia...

#### Si un sintonizador no está funcionando lo primero que hay que hacer mes medir los voltajes, si sabés leer diagramas leelo y mirá cuáles son los voltajes que necesita un sintonizador para funcionar y simplemente comprueba si están los voltajes y si están correctos.


### 4ta parte: clase práctica con la placa para medir voltajes. Como saber si estoy en tierra fría o caliente. Como usar serie. Que hacer si no prende la serie: verificar memoria. Toco la terminal 8 y observo el multímetro que me indica que ahí están los 5 voltios. El jungla siempre está sin alimentación hasta que le das la orden de encendido. Si nos paramos ahí equivale a pararnos en el lado positivo del filtro principal por lo tanto ahí debe haber el voltaje de entrada después de rectificado. Como está recibiendo 120 voltios de AC entonces tiene 160 voltios que es más o menos el voltaje que aparece luego de estar rectificado.

##### Como está recibiendo 120 voltios de AC entonces tiene 160 voltios que es más o menos el voltaje que aparece luego de estar rectificado.

Vamos preparar nuestro multímetro para las medidas, lo colocamos en modo de alarma con el fin de confirmar de que he colocado la punta negra en el punto correcto.

#### Este tipo de tarjetas tiene 2 tierras la HOT y la la COLD. Las medidas que vamos a hacer: notemos lo siguiente:

COLD GROUND (Minuto 01:05) Me está especificando que esta es la tierra fría, y este otro símbolo HOT GOUND es la tierra caliente.

Por eso observamos aquí el símbolo de tierra caliente y en este otro lado el símbolo de tierra fría.

#### Las medidas que vamos a hacer es el lado secundario en el lado frío.

##### Una manera fácil de asegurarse es conectar la punta negra la tierra fría es en el cuerpo del sintonizador con eso no hay pérdida.

Si comprobamos colocando en la continuidad para que me diga el pitido de que está correcto.

Si miramos por algo por acá en otra tierra vamos a notar de que me confirma qué si en el otro lado ya no hay continuidad.

Entonces en este tipo de disipadores de aluminio van conectado a tierra entonces, esta que es la sección del vertical está **aterrizado** entonces me confirma que sí.

Este no porque es el refrigerador del regulador, que está en la parte caliente.

##### Entonces ya me aseguré que estoy en el punto correcto.

Agarro el multímetro y lo pongo en escala para corriente continua, vamos a conectar el televisor y lo llevo a la **serie**. 

Serie: 3 bombillas de 100 vatios a través de los switches voy a habilitar cada uno de ellos. Para hacer esta prueba solo necesito una bombilla de 100 vatios.

Ese encendido breve es porque la fuente consuma un poquito para poder arrancar.

#### En caso de que haya un problema serio la bombilla se prenderá de manera intensa y me indicará que hay un problema en la fuente pero no me ocasionará ningún otro problema.

##### Una manera rápida de saber si la fuente está trabajando, si viste que el bombillo prendió ya me dice de que la fuente está arrancando, pero suponiendo de que no hubiera ocurrido eso entonces hay que ir a ubicar un chip memoria.

#### Identificar la memoria: 
Dip 8, no es de superficie, si fuera de superficie estaría por debajo y serían las mismas 8 terminales.

Acá me indica que esta es la terminal 1 (el puntito).

Toco la terminal 8 y observo el multímetro que me indica que ahí están los 5 voltios alimentando la memoria, eso me indica de que la fuente standby está trabajando correctamente. 

Si no estuviera esos 5 voltios, entonces me tengo que ir a la fuente a ver en donde está el problema, esos 5 voltios también me confirman que igual el micro que acompaña la memoria. (Minuto 5) También está alimentado.

Y a este otro integrado que viene a hacer el **jungla** estaría necesitando un voltaje que con la ayuda del diagrama descubriríamos por donde entra y qué momento debe entrar muy probablemente solo aparece cuando el micro da la orden de encendido, mientras es probable que él vaya a estar sin alimentación porque es la manera en que el microprocesador controla el encendido y el apagado del televisor.

### Esa es la primer prueba de voltaje, el voltaje de standby.

Vamos a irnos ahora a la fuente para comprobar el voltaje de las salidas de los dos voltajes que salen de la fuente.

Vamos al diagrama y hablábamos del **diodo 820**, debe estar en la parte secundaria este filtro seguramente por su tamaño nos dice que es el filtro principal de esa **fuente secundaria**, vamos a observar acá que es el de 820 buscamos la sección el cátodo nos paramos en él y observamos el voltaje: 133 voltios.

El diagrama me dice que 135 está dentro del rango permitido. Esa fuente está buena.

La otra otra fuente que es la del 825 ya podemos deducir de que debe estar bien puesto que tenemos los 5 voltios. De ahí es donde salen los 5 voltios.


Yo voy a buscar el diodo que es el de 825 vamos a buscarlo en el circuito.

##### Diodo de 825: tocámos el cátodo y miramos el voltímetro y encontramos que hay 16.68 voltios el diagrama nos dice que deben haber 18 voltios.

Probablemente esos voltajes se estabilicen cuando el televisor ya esté encendido.

En el momento estamos a modo standby y los diagramas a veces no especifican los voltajes cuando están en standby.

Un televisor genético por lo general no trae ninguna información.

##### Esa es la manera de medir voltajes en el lado frío

### Medimos voltaje en el lado caliente.

Quitamos la tierra del lado frío y buscamos un punto que nos garantice que estamos en el lado caliente.

Una manera es pararnos del chasis del integrador regulador vamos a buscar el filtro principal que es este por **ser más grande** sabemos que es ese.

Vamos al diagrama que nos ayude con unos detalles adicionales.

#### Hablamos que cuando analizamos aquí el comienzo que luego del puente rectificador había una resistencia de 801 de 1 ohmio a 5 vatios.

Y que luego ese voltaje saliente del puente rectificador llegaba al c802 que es exactamente este condensador grande.

Quiere decir nos habló de la r801 si miramos acá dice r801 la letra está invertida  

Quiere decir que si nos paramos y notamos el valor de la resistencia si tiene 5 vatios... 1R 1ohmio.

Si nos paramos ahí equivale a pararnos en el lado positivo del filtro principal por lo tanto ahí debe haber el voltaje de entrada después de rectificado.

##### Como está recibiendo 120 voltios de AC entonces tiene 160 voltios que es más o menos el voltaje que aparece luego de estar rectificado.

Ahí tenemos voltajes en el filtro principal, quiere decir que si vamos al diagrama, es lo mismo que pararnos acá o en la terminal 1. **En la terminal 2 hay que tener cuidado pararnos ahí porque ese voltaje de acá puede tner unos voltajes transitorios que puede tener picos altos que puede que nuestro multímetro no soporte y lo vamos a dañar.**

##### Hay que tener cuidado con esos voltajes porque revienta el multímetro. (Minuto 11)

###### Acá yo tenía el problema (Minuto 12): Nos falta medir estos otros voltajes secundarios con respecto al circuito integrado que sería necesario medirlos en caso de la fuente estuviera muerta.

### Video 5: Medir voltajes. La información técnica del televisor no se busca a partir de la marca y del modelo se busca por el código de la referencia del chasis. Hay dos fuentes una que entrega 135 voltios del flyback y la otra entrega 8 voltios (Minuto 5). Hay diodos especiales, los diodos comunes y corrientes como el 1N4007 trabajan a frecuencias de los 60 ciclos pero las fuentes conmutadas trabajan de los 15 mil hasta más ciclos por segundos el diodo no es capaz de trabajar se calienta y se daña.  Esta otra viene acá pasa por este chopper y llega al puente rectificador, y esta otra llega por acá y llega al otro lado del puente rectificador porque este switch es un relay que me entrega la energía que pasa para la bobina de gauss. Como chequear voltajes sin prender televisor. Tenemos el símbolo de transistor HOT (transistor horizontal) hay que puentearlo entre base y emisor o retirarlo para que no dañe el flyback. Vamos a ubicarnos sobre el transistor sobre esta parte. Tengo acá un pedazo de alambre, cautín precalentado y vamos a hacerla entre dijimos emisor y base. No hay manera de equivocarnos porque son las dos terminales de los extremos, el del centro es el colector. Entonces agarramos los dos alambres los dos extremos de los dos terminales del transistor calentamos y ahí nos quedó soldado, con eso el televisor ya no nos va a encender cuando los conectemos. Minuto 13. Vamos a dar vuelta la tarjeta vamos a colocarla de un modo tal que nos permita tomar voltajes, por precaución debemos poner esta ventosa colocarla por caso tal de que no algo pase no nos haga un daño. Para este caso que es un televisor de 14 pulgadas pueden salir alrededor de los 35.000 voltios.

Vamos a aprender a tomar voltajes de una manera preliminar en un televisor existen muchos porque realmente en un televisor existen muchos bloques en donde será necesario tomar voltaje.

Claro que mucho dependerá del síntoma del aparato.
###### Vamos a asumir de que este televisor tiene problemas de fuente.
Que no vemos ningún indicio de que esté funcionando.

Vamos a aprender a tomar voltajes con el multímetro.

Vamos a usar un televisor Challenger.

Tengo la placa que saqué del aparato para trabajarlo por fuera.

En otras ocasiones hablábamos de la referencia del chasis que es **PT wm01 g1d** que es como **se consigue la información técnica**

Vamos a irnos al diagrama para hacer comparaciones de que debemos a hacer todas las veces que necesitamos comprobar el estado de la fuente.

Acá tenemos la computadora y el diagrama que está puesto como Challenger TC 1220 aunque el modelo del televisor que estamos trabajando es un **CT 1421**. 

El televisor que tengo acá es un televisor de 14 pulgadas.

### Vamos a irnos por parte para simplificar el asunto vamos a iniciar por la fuente.
Vamos a imaginarnos que tenemos problemas con la fuente.

Aunque es una fuente conmutada trabaja con un circuito integrado y un transformador chopper (ferrita) sólo entrega 2 voltajes.

#### El primero es esta fuente de 135 voltios que es la que va para el flyback.
Este es el símbolo del flyback (Minuto 5)

##### Y la otra fuente es esta otra que entrega 18 voltios que salen del diodo
Minuto 05:10

Acá hay un devanado secundario del **transformador chopper** que sale alterno a través de este 821 que llega a este diodo d825 se filtra o se aplana a través de este condensador c821 ? de 1000 microfaradios a 25 voltios y sale por este chopper a distribuir voltaje entonces acá deben haber 18 voltios.

Con la otra fuente que es la fuente del +B tenemos otro devanado entre las terminales 5 y 6 una bobina en serie un chopper el diodo rectificador d820 ru3a hace referencia a que es un diodo especial, nunca vaya a cambiar ese diodo por un diodo común y corriente.

Los diodos común y corriente no trabajan a la alta frecuencia que trabaja a este tipo de fuente.

Hay diodos especiales, los diodos comunes y corrientes como el 1N4007 trabajan a frecuencias de los 60 ciclos pero las fuentes conmutadas trabajan de los 15 mil hasta más ciclos por segundos el diodo no es capaz de trabajar se calienta y se daña.

Luego de que salga rectificado tenemos 2 filtros(capacitores) aplanadores el primero el **c821** y luego el **c822** que vamos a volver más adelante.

Luego tenemos a la salida **135 voltios** que una parte se deriva para acá y luego veremos para dónde va y luego esta otra que va para el flyback.

Lo primero que debemos de hacer es comprobar esos voltajes están saliendo, no hay un switch de por medio para que ella entregue voltaje con solo conectarla si seguimos la línea aquí está la primera pasa por el fusible pasa por el fusible.

Acá parece un error porque no veo el empalme para que llegue al puente rectificador.

Esta otra viene acá pasa por este chopper y llega al puente rectificador, y esta otra llega por acá y llega al otro lado del puente rectificador porque este switch es un **relay que me entrega la energía que pasa para la bobina de gauss**.

Por ahora me interesa saber que acá hay voltaje alterno al puente rectificador pasando por esta resistencia r801 que es de 1 ohm a 5 vatios llega al filtro principal c802 que es un punto de prueba que debemos de hacer si a la salida no encontramos ninguna muestra de voltaje.

Entonces vamos a hacerlo a hacer esas medidas en la tarjeta pero antes vamos a hablar de un asunto importante.

Antes de energizar la tarjeta antes de energizar una tarjeta y antes de empezar las primeras pruebas.

Si vamos a trabajar sobre las fuentes con el propósito de chequear el comportamiento de ellas sin prender el televisor.

#### Lo recomendable es sacar del compartimiento pero para que no haya riesgos de que se genere alto voltaje y que al estar desconectado el yugo nunca debemos hacerlo si no está conectado porque dañaríamos la parte que corresponde al alto voltaje (el flyback).
Para evitar ese riesgo debemos bloquear esta sección con el propósito de que ella no trabaje (Minuto 10:25) y solamente nos permita comprobar el estado de la fuente para eso lo recomendado es que vayamos al diagrama.

Acá tenemos el símbolo de transistor HOT (transistor horizontal) hay que puentearlo entre base y emisor o retirarlo.

Para muchos es más fácil hacerle un puente (un jumper) entre la base y el emisor y con eso bloqueamos el transistor horizontal al estar bloqueado el no va a trabajar entonces toda esta parte del flyback no nos va a trabajar entonces no hay ningún problema de riesgo para el aparato.

Vamos a hacer eso tomar la tarjeta y hacerle ese primer paso de bloquearla para que no dañe el flyback. (Minuto 11:30)

Identificamos el transistor HOT por el tamaño y la resistencia y por la referencia, si nos fijamos por debajo vamos a ver que dice Q404 y acá están las 3 terminales del transitor vamos al diagrama y observemos que dice Q404: H OUT (transistor horizontal de salida).

Vamos a ubicarnos sobre el transistor sobre esta parte. 

Tengo acá un pedazo de alambre, cautín precalentado y vamos a hacerla entre dijimos emisor y base. No hay manera de equivocarnos porque son las dos terminales de los extremos, el del centro es el colector. Entonces agarramos los dos alambres los dos extremos de los dos terminales del transistor calentamos y ahí nos quedó soldado, con eso el televisor ya no nos va a encender cuando los conectemos. Minuto 13.

VAmos a dar vuelta la tarjeta vamos a colocarla de un modo tal que nos permita tomar voltajes, por precausión debemos poner esta ventosa colocarla por caso tal de que no algo pase no nos haga un daño. 

### Para este caso que es un televisor de 14 pulgadas pueden salir alrededor de los 35.000 voltios porque la corriente es muy poca. Si está conectado a la pantalla la corriente aumenta porque la pantalla es un condensador.

Entonces vamos a hacer la prueba voltaje.

#### Video 7 (no había 6) Loquendo XD.

Empezamos con un blanco y negro. Las fallas más comunes y los métodos más prácticos.

Instructor autor en esta imágen tenemos los bloques que componen un televisor a blano y negro aunque haya pasado a la historia estudiarlo facilita el entendimiento.

Hay 15 bloques. Conozcámoslo comenzando por donde entra la señal al televisor, la antena o entrada del radio/frecuencia si ubicamos el puntero del ratón sobre este bloque se despliega una breve pero útil.

Puede ser receptor terreste o receptor satellital.

Cuando nos referimos a la antena del TV estamos hablando de la antena exterior sin importar el tipo de antena que estemos usando aunque existen varios tipos, como la que venía con el TV (figura 1) o la tipo espina de pescado (figura 2) todas cumplen la misma función captar las señales radiadas al aire por las emisoras, las dos últimas se usan en donde las señales son muy débiles por razones de distancia o por un obstáculo como un edificio o una montaña. Usan el mismo principio que la radio ondas al aire. Al chocar con la antena como está conectada a un transformador conocido como valum en los televisores viejos se ve en el conector de la antena esta señal es capaz de inducir en el secundario del valum un pequeño voltaje suficiente para ser amplificado por un primer bloque que forma el sintonizador llamado amplicador de RF (radio frecuencia) los distintos tipos de antena se originaron debido a la necesidad de mejorar su rendimiento ya que se debe procurar que capte la señal directa de la antena transmisora y no las provenientes de espejos como árboles, edificios, montañas, etc.

El transformador valum, transforma la impendancia de la antena de alta impendacia a baja impendancia. La entrada del sintonizador es de 75 ohm.

Si observas una antena tipo espina de pescado verás como hay una espina cerrando el circuito primario del valum.

Volvamos al diagrama en bloques. (Minuto 04:40)

Ahora vemos el bloque selector de canales.
El sector sintoniza un canal y lo entrega en formato FI.

El sintonizador o selector de canales como también suele llamarse es la parte del televisor que se encarga de seleccionar un solo canal de los muchos que pueden estar llegando en un momento a la antena si se trata de un sistema de televisión por cable. Esa selección la hace el usuario a voluntad y puede cambiarla tantas veces como desee.

Usted como técnico reparador como el circuito hace la selección para poder entrar a reparar cuando este presente fallas.

##### Sintonizador está conformado por 3 bloques:

No se puede verificar porque es de alta frecuencia.

1. Amplificador DNF: se encarga de recibir la señal de la antena la amplifica a un nivel que se pueda trabajar ya que la señal es muy pequeña. Antes es pasado por un filtro bobina condensadores para solo dejar pasar las señales de televisión y eliminar las demás señales como AM y FM. Con la señal filtrada y amplificada es pasada al mezclador.
2. Oscilador local: se comporta como una pequeña estación transmisora.
3. Mezclador MIPS? (Minuto 06:23): se le llama así porque debe mezclar la señal procedente de la antena con la señal que se genera en el bloque oscilador local, el objetivo de esta mezcla es sintonizar el canal deseado y desechar los demás. Para eso se aplica que se llama esteroque? (Minuto 06:43) se suman dos señales distintas para obtener siempre el mismo resultado se necesita eso porque con 1 sólo amplificador en la siguiente etapa se puede conseguir la amplificación necesaria para continuar con el proceso de la señal pues esta como la entrega el selector sigue siendo muy pequeña y por lo tanto es necesario amplificar más, de no ser así se necesitaría un amplificador independiente por cada canal sintonizado hemos vuelto al diagrama de bloques.

El rayo es el que caga todo. El rayo puede entrar por la antena o por los 220, todo lo que entra o sale puede ser una entrada de rayo. En el campo es mucho peor. Protectores gaseosos, protectores de antena. Los cables de antena tienen protectores. Se hace todo puesta a tierra. Cayó un rayo en el pira pytá y la instalación eléctrica y no había más nada desapareció todo. Vimos que caía en el espigón (el muelle). Estaba la lucecita roja y verde. Yo estaba sentado en una de madera y yo sentí el rayo.

#### Video 8. Como funciona la televisión a color.
Continuamos a ver cada uno de los bloques.

Tenemos 2 tipos de antena: de aire que son muy usadas en zonas de señales muy bajas antena tipo yagi, y la antena tipo espira de pescado.

Yendo al sintonizador de canales tenemos para resaltar de que él se compone de 3 bloques, independientemente si sea mecánico o digital dentro de la cajita vamos a encontrar un bloque como amplificador de radiofrecuencia, un oscilador local y un mezclador en combinación de ellos son los que hacen el trabajo de entregar finalmente la frecuencia intermedia (FI) resultado de un efecto que se conoce coo eterodinación acá tenemos un dibujo del sintonizador viejo de perilla rotatorio (Minuto 01:12) en donde tenemos las distintas conexiones si vamos al amplificador acá hay una representación gráfica o un diagrama de un antiguo televisor a transistores. (Minuto 01:29)

Y esta etapa de bloqueo es intermedia donde encontramos tres pasos amplificadores a transistores con la bobina un sistema bastante complejo que ahorita está muy reducido a través de los circuitos integrados esto es sólo como para que tengas idea de la forma de la señal FI y como lo entregaba él sintonizador y acá ya como se entrega una entrada de punto 4000 voltios para entregarla ya a un nivel mucho más alto de 3.2 voltios pico pico.

Realmente recibía una amplificación de unas 8000 veces ya cuando se tiene ese nivel tan bueno 3.2 voltios entonces es donde pasamos al **amplificador de video**.

#### Como decíamos en la primera parte esa señal de video debe llevarse a un circuito detector de vídeo (que no es nada más que un diodo)
El diodo se se encarga de recortar la media onda de la señal FI que llega de esta forma al instalarle un circuito tanque un circuito filtro con esta resistencia este condensador tenemos al final limpia quitamos la señal RF de la portadora y queda únicamente la señal de video lista para llevar al amplificador final que en la entrega a la pantalla.

#### En cuanto al amplificador de frecuencia intermedia de audio es un circuito similar que recibe la FI y la lleva a un amplificador común y corriente como ya se dijo para llegar finalmente al parlante.

Si nos vamos a la parte de la pantalla hay que recordar que como el tubo de rayos catódicos funciona igual que una válvula al vacío donde un elemento precalentador filamento calienta un elemento segundo llamado cátodo que es el que libera electrones cuando se calienta allá dentro de la válvula al vacío porque eso en realidad es una pantalla. Pero que cuando hay un control si cuando se tiene una segunda fuente aquí alimentando la placa estoy voy a hacer el alto voltaje los electrones son atraídos hacia la parte de la placa que en este caso es la parte frontal de la pantalla al tratarse de alto voltaje entonces se genera un haz de electrones a muy alta velocidad que al chocar contra el fondo de la pantalla entonces nos produce una luz tal como lo mostramos acá en la pantalla requiere de un filamento el cátodo que es el que recibe la señal de video la información de video para estar regulando el haz de electrones hacia el centro sólo que en este momento están saliendo de manera recta hacia adelante lo veríamos realmente como un punto en el centro de la pantalla por eso aquí está la señal de video. Acá son 120 voltios depende del plan del tamaño de la pantalla si he llevado al final aquí está demarcada la línea la máscara que contiene el alto voltaje que viene a ser como la placa para que sean atraídos por su alto voltaje positivo¿? (**no era que era hacia el negativo?**) hacia el frente.

El haz se mueve a través del yugo . Este es el yugo y acá está representado el alto voltaje que viene a ser como la placa para que sean atraídos por su alto voltaje positivo hacia el frente.

El haz se mueve a través del yugo. Este es el yugo y acá está representado este es el cañón aquí tenemos el haz de electrones de frente. Y acá están las bobinas del yugo estos son las verticales y estas son las verticales y estas son las horizontales cuando no hay ningún funcionamiento ningún comportamiento de la bobina del yugo sobre el haz del electrones el se viene hacia el centro cuando no es un punto en la pantalla quedaría así ese sería el efecto si estos componentes de yugos el circuito que maneja el yugo no hace ninguna acción contra el haz electrónico entonces se quedaría convertido en un punto esta es una representación de lo que haría o lo que hace un yugo vertical (Minuto 06:20): por momentos los sube luego lo va bajando luego se invierte la corriente y aquí llega y lo baja hasta el final cuando este circuito falla por eso es que queda una línea horizontal porque el circuito horizontal o la deflexión horizontal está trabajando o sea está moviendo el haz en sentido horizontal como el vertical no está funcionando entonces él se cierra en ese sentido.

### Por eso es que decimos que cuando tenemos una raya horizontal la falla es vertical y viceversa. Si tenemos una raya vertical la falla es horizontal.

Acá podemos ver otra animación (Minuto 07:15)

Solamente está trabajando acá el efecto para un lado y para el otro de una manera tan rápida que lo que vemos es una imagen completamente funcionando.

Minuto 07:33 - Acá hay una animación del precalentado del filamento liberando electrones.

Y acá como son atraídos por la placa.

Acá está la acumulación de electrones y vemos como son atraídos hacia la parte de adelante produciendo el punto luminoso.

Y aquí está el dibujo en cámara lenta de cada una de las líneas (Minuto 08:07) acá ya es algo simple comience como arriba no hay información y acá ya comienza a haber ese momento de dibujar los puntos negros simplemente hace el corte del haz electrónico y el instrumento entonces no hay impacto en la pantalla en el fondo sur y por lo tanto se forma la imagen.

Ahora para producir esa deflexión vertical.

### El circuito vertical es el encargado de aplicarle a las bobina del yugo no solo una corriente suficiente para modelarla en el sentido vertical sino también de sincronizarse con la señal recibida
Entonces acá tenemos una forma de onda diente de sierra que es la que finalmente ya en el circuito final entrega esta forma de señal que la que hace que la suba hasta arriba la pantalla se vaya bajando poco a poco y luego retorne otra vez o sea sube y comienza a bajar y en ese momento se va llegando la imagen.

Porque el haz electrónico está moviendo en sentido horizontal solamente para que suba y baja, y el horizontal se encarga de hacer el resto. La diferencia es en cuanto a la velocidad obviamente **el horizontal lo hace en una velocidad mucho más alta** en este caso es de 15750 para nuestro sistema de televisión.

Hay otros sistemas que trabajan a unas velocidades distintas.

##### En cuanto al separador de sincronismo acá tenemos la representación gráfica de una falla por sincronismo vertical acá la imagen nos queda partida (Minuto 10:20). Se veía mucho esta falla en los televisores antiguos.
Era tan inestable el circuito de sincronismo vertical que venía una perilla un botón para que el usuario lo ajustará cuando fuera necesario.

Y ahora son tan precisos que no requieren de ese control y por lo tanto ha desaparecido.

Acá a la derecha tenemos el defecto cuando se pierde el sincronismo horizontal (líneas oblicuas) (Minuto 10:50)

Acá tenemos una simulación de los pulsos de sincronismo estos son pulsos a 60 ciclos que podemos verlo on un osciloscopio acá está con la portadora con la información de video recordemos que el diagrama bloque veamos de que ya el video se sacan esos pulsos.

Acá estan los pulsos de extremo vertical a 60 ciclos para nuestro sistema y acá están los de 15750 para los pulsos de sincronismo horizontal, en realidad el circuito de sincronismo no es más que un filtro pasa banda, el cuál hace el bloqueo de las frecuencias de baja para el caso de sacar el sincronismo horizontal, y un pasa banda para frecuencias altas para extraer solamente los de vertical que trabaja a 60 ciclos. Esto a 60 y estos a 15700 Hz.

### Ahora pasando al televisor a color
Tendríamos una representación a bloques de lo que es el amplificador de color.
Siguen estando los mismos adicionalmente tenemos un bloque amplificador de señal J?? (Minuto 12:41) o señal a blanco y negro. Un amplificador de color que será llevado a cada uno de los cátodos hay un paso en el que se hace la separación de color es una información que también ya viene a través de la FI.

Llega a la sección de video se extrae la información de color es llevada al amplificador de color y se entrega individualmente a cada uno de los cátodos eso es la **TELEVISIÓN A COLOR**, lo demás es lo mismo. Hay algunas diferencias en cuanto al voltaje porque ya no es una sola sino que hace 3 en una, **pero es a groso modo lo que es la diferencia entre el televisor de blanco y negro**.

##### Repaso enfocado en las fallas:

Una pantalla sea de blanco o negro o a color va a necesitar para que pueda dibujar alto voltaje, si no hay alto voltaje no habrá ninguna imagen así todo lo demás esté funcionando recordemos que es el que produce el brillo en la pantalla. Si falla alguno de los colores vamos a tener imagen con ese color faltante. 

Hay fallas que son exclusivas del módulo hay fallas que tienen que ver con todo el aparato supongamos que **falla el selector de canales**, todo lo demás debe funcionar por ejemplo la pantalla nos va a dar una pantalla llena. Vamos a tener ruster una pantalla llena con iluminación podemos manejar brillo contraste, es más el televisor tiene entradas de audio y video **auxiliares si aplicamos por ahí una señal un DVD un VHS o cualquier fuente externa vamos a tener en pantalla el funcionamiento aparentemente normal, únicamente tendremos falla con la sección del televisor como tal porque es el sintonizador el que está fallando**

###### Lo mismo ocurriría si la falla fuera en la etapa de FRECUENCIA INTERMEDIA o si fuera de la GC tendríamos fallas a relacionadas únicamente con la sintonía o con la parte de RF y FI, lo demás estaría de manera correcta funcionando.

###### Una pérdida de sincronismo si sería general para todos para el funcionamiento de TV como el funcionamiento para entradas auxiliares.

#### Una falla en el vertical ya sabemos que es total porque afecta todo el funcionamiento.

#### Una falla de audio será general tanto de televisión como en modo video porque es común para todos ellos.

Estos son los conceptos que hay que tener en claro.

#### Video 10: Primer video de la nueva serie.

Vamos a iniciarnos.

....

#### Video 14: Seguimos trabajando con un televisor que no prende. (Salté acá porque acá tenía el problema).
Puede ser porque sufrió una descarga. La fuente principal ha fallado para entrar a hacer el análisis hay que ubicar la fuente para ello entonces tenemos una fotografía de una placa o de una placa universal en donde debemos centrarnos principalmente en los siguientes componentes o partes de la fuente.

1. La entrada de AC.
2. Fusible.
3. Puente rectificador.
4. Filtro principal.
5. Transformador chopper.
6. Transistor o circuito integrado conmutador.

Acá tenemos una linea demarcadora que nos separa la fuente principal (Minuto 02:04) especialmente la parte "HOT". Nota personal: separa la parte continua de la alterna.

Podemos ver la entrada de AC esta es la que va por el cordón el interruptor algunos no los tienen pero puede tenerlo este suspende la AC las dos líneas inclusive, cuando apagás todo queda desenergizado para poder trabajar sin necesidad de desenchufar el cordón, el fusible de entrada un transformador con unos condensadores que hacen el filtro de ruido que entra o que pueda salir de la fuente luego tendríamos los 4 diodos que conforman el puente rectificador que finalmente entregan el voltaje ya rectificado y en este caso si es de 120 voltios de CA serán 150 V de CC.

Esos 150 V de CC pasan por el transformador chopper el devanado primario para llegar al transistor conmutador pero bien podría ser un circuito integrado como lo vamos a ver al final de este módulo.

Acá se me pasó por alto esta resistencia de 3,9 ohmios a 7 vatios que está en serie con el puente rectificador que está en la entrada de la AC una de las líneas de AC a lo que es amortiguar la entrada de corriente para proteger los diodos del puente rectificador recordemos **un filtro cuando está descargado se comporta como un corto circuito** entonces la corriente ahí es muy alta para evitar que se puedan dañar los diodos se coloca esa resistencia con el fin de amortiguar ese primer arranque de carga para el filtro entonces aquí tenemos ubicada todo lo principal de la fuente principal de este televisor.

El interruptor viene al chipper entrada de AC fusible puente rectificador filtro principal transformador transistor conmutador flyback transistor de salida horizontal salida vertical jungla sintonizador entrada auxiliar transformador de horizontal amplificador de audio, micro, memoria, etc. Animación (Minuto 06:40)


Ahora vamos a chequear el fusible, puente rectificador y el filtro principal

En otras palabras confirmar de que tengamos energía al menos en la parte primaria de nuestra primaria de nuestra fuente hay 2 métodos:

1. Chequear cada uno de los 3 componentes que hemos hablado: el fusible, el puente rectificador y el filtro principal con el multímetro en modo diodo tiene una alarma que cuando esté en corto sonará, **en el caso de los diodos no lo debería hacer ni con el filtro sólo con el fusible.**
2. Éste método es más fácil: conectar el televisor a una serie. 

Ahora explico las diferencias con el primer método de conectarlo a una serie si al conectar el televisor el bombillo enciende unos instantes y luego se apaga a no ser que sintamos que el televisor sigue como intentando prender y apagar, si lo hace de una manera repetida nos indica que al menos esos tres elementos: **el fusible el puente rectificador y el filtro principal están buenos.**

Acá explica como armar una serie (Minuto 10).

... Sigamos ...      
Lo hemos conectado a una serie encendió unos instantes y luego se apagó, encendió unos instantes mientras se cargó el filtro. También puede ocurrir que hay una parte que no le mostré en la imagen.

##### Bobina desmagnetizadora.
###### Acá hay un enchufe en donde va un conector parecido a este que es el que va para una bobina que va rodeando la pantalla: la bomba desmagnetizadora que en combinación con este elemento una **resistencia PTC** que se calienta para interrumpir el paso de la corriente hacia la bobina esa bobina si está conectada y este elemento todavía no se ha calentado lo suficiente no va a tener un consumo alto y por lo tanto lo recomendable es desconectarla al momento de hacer pruebas con la fuente entonces desconéctela y ya no tendrá ese problema porque de otra manera si está conectado nos podrá engañar al encender la serie. (Minuto 12) por la actividad así que hay que desconectarla así cuando el filtro se haya descargado al momento de conectar la serie nos va a iluminar un momento mientras se carga mientras ese consumo alto se reduce.

Si esta parte está bueno: fusible todo esta parte los 4 diodos y el filtro principal e inclusive el transistor conmutador **si el transistor conmutador está en corto lógicamente también se nos va a quedar encendida todo el tiempo**.

##### Bien estábamos ante un aparato que hemos conectado a la serie encendió unos instantes y luego se apagó habíamos dicho de que ya con eso comprobábamos de que los 3 componentes de entrada estaban correctos entonces podemos continuar con la parte fría de la fuente.

Vamos a la sección COLD de la fuente.

Acá hay un filtro dos 3 4 eso nos indica de que por lo menos hay 4 fuentes y se alcanzan a ver los diodos.

Tratemos de identificar los diodos rectificadores acá está el principal para este filtro acá hay dos seguramente este que se alcanza a ver acá para este filtro y acá tenemos un cuarto rectificador para este filtro podemos colocar la punta de nuestro tester con un cocodrilo a esta parte del sintonizador que es una buena tierra y la punta roja positiva tocar estos puntos estos cátodos (Minuto 15) es un voltaje al rededor de 110 voltios en condiciones normales y acá pueden haber 12 24 y 18 Voltios.

Depende del tipo de fuente pero acá habrá voltaje si la fuente está activa.

Otras dos opciones si acá en este conector tenemos conectado el teclado que como vimos acá dice que es el conector para el teclado, vamos a tener probablemente en frente diodos LED que indica en la parte frontal al usuario cuando el televisor está encendido está en modo apagado o standby si ese LED enciende es una buena señal es un indicio de que la fuente está trabajando si la fuente principal está trabajando quiere decir que ya acá se están generando unos voltajes que finalmente terminan en alimentar el microprocesador y está digamos que casi listo para recibir órdenes del comando de control remoto del teclado si esa luz de LEDs es intermitente nos indica que hay un problema pero que por lo menos la fuente está intentando trabajar.

Mira todos el trabajo que se nos ahorra con solo hacer esto y tener en claro que es lo que estamos haciendo.

Ahora nos queda comprobar si el voltaje que está recibiendo el microprocesador es el correcto. Eso depende de la edad del televisor los microprocesadores de viejos televisores trabajan con 5 voltios, los modernos con 3,3 voltios.

Dice que en este punto es probable que si tiene el piloto este encienda lo que nos confirmaría que la fuente está trabajando y que si el televisor no prende es por otra causa de modo que lo que seguiría sería confirmar que el voltaje de standby esté en el valor correcto 5v o 3,3 voltios.

#### Donde y como lo mido?
En los televisores existen muchos puntos de prueba para este voltaje como veníamos ahora en los diodos de la fuente en la parte fría.

La dificultad para muchos es asegurarse de hacer las medidas en el punto correcto.

#### Un punto rápido de ubicar es la memoria que siempre acompaña al microprocesador.
Si no la vez por encima es porque está por debajo por tratarse de una tecnología SMD o de superficie.

Este componente junto con el microprocesador siempre que el televisor esté conectado y en el caso de que tenga un switch esté encendido de otro modo no estará en modo de espera listo para obedecer ordenes entonces al estar encendido el switch al estar conectado debe estar energizado aunque el televisor no esté funcionando aunque esté apagado... En ello vamos **a encontrar el llamado +B de standby** 

#### pero en qué pin es? Es el pin 8, en donde debemos encontrar el voltaje.
El huequito indica el pin 1 del integrado.

Pin 1 si contás de izquierda a derecha llegás al pin 8. (Minuto 20).

Ahí colocamos la punta roja la otra debe estar en el cuerpo del sintonizador y nos debe dar la lectura del voltaje con el cual está alimentado este circuito principalmente el microprocesador ya hemos dicho de que debe ser 5 voltios, 5.1, 5,2 o 3,3 si es moderno.

Si estamos tratando con una memoria de superficie vamos a tener la siguiente figura este es el pin 1 .... y acá el pin 8.  

### El PIN 8 es el VCC de la memoria, el GND es el PIN 4.

Si hemos llegado a este punto y el televisor no nos prende podemos descartar gran parte de la falla a la fuente. No podemos descartarla del todo porque puede haber alguna de la fuente fallada pero por lo menos esta que corresponde a la parte caliente de la fuente y gran parte de la sesión secundaria de la fuente nos indica al tomar esta lectura de que está trabajando la fuente y que por lo menos el microprocesador está energizado y probablemente listo para recibir ordenes.

Luego estudiaremos la situación en que enfrentaremos como enfrentar ese tipo de falla.

Vamos a retomar el caso en cuando la serie se nos quede encendida y no se apaga aunque tenga la bobina desmagnetizadora desconectada porque es el caso que nos aplica en este módulo es aprender toda la parte primaria de la fuente.

### Video 16

Cuando recibimos un televisor lo primero a comprobar es la fuente de pantalla porque cuando el usuario presiona la tecla power hay un circuito que debe estar eternamente energizado, ese circuito es conformado por el microprocesador la memoria el teclado y el sensor de remoto.

Tenemos el micro, la memoria, el sensor remoto, y tenemos el teclado.

Tanto el micro como la memoria y el sensor remoto trabajan con la misma de alimentación de 5 voltios si se trata de un televisor viejo. O si se trata de un televisor de última generación 3,3 voltios.

Ese voltaje se conoce como standby que cuando falta o si no está en correctas condiciones el aparato no funciona.

En el pin 8 de la memoria con respecto a la tierra fría.

Si efectivamente no hay voltaje de standby. Debemos identificar esta fuente teniendo presente que puede estar en dos posibles configuraciones que pueden confundir:
1. Integrada en la fuente principal: el único transformador chopper se saca también el voltaje de standby.
1. Independiente de la fuente principal: Tiene un circuito con su propio transformador chopper generalmente de tamaño pequeño con el cual se obtiene el voltaje de standby.

El no tenerlo en cuenta pudiera causar dificultad ubicarlo. 

Aunque esto solo se ve en pocas marcas y modelos.

Observen lo siguiente: entrada de AC los filtros de ruido y acá tenemos el transformador chopper principal que si lo miramos físicamente es un transformador grande pero acá hay un transformador secundario chopper standby. 5 voltios de standby salen de esta configuración este transistor MOSFET(oscilador) **es un transformador pequeño que solo entrega los 5 voltios**, mientras eso no trabaje entonces el televisor estará completamente inoperante.

Observa que acá hay un relevo con relay. A veces confundimos ese sonido de relevo cuando le damos la orden power lo confundimos con otro relay. En los televisores algunos traen doble relay uno para la bobina desmagnetizadora y otra para la bobina principal.

Este relevo mientras no se cierre no alimentará o llevará voltaje al puente rectificador que viene a ser el principal para alimentar toda la etapa de potencia de la fuente principal del televisor. La pregunta es **quién comanda este relay?** debe haber una energía antes de esto.

El microprocesador comanda el relay pero esta parte debe estar energizado con la fuente standby.

Entrada AC las dos líneas acá hay un juego de rectificadores un filtro principal y acá está el circuito de standby esos pocos elementos hacen que este transformador chopper transfiera energía que al rectificarla nos entrega un voltaje superior a los 5 voltios con el diodo regulador de 5 voltios en 3 entradas una de entrada, la tierra y la de salida aparecen los 5 voltios de standby para el microprocesador.

Reparar este tipo de fuentes de standby es más fácil, consiste en menos componentes y un transformador chopper más chico con una sola salida a la que llega 9 voltios.

Estos desvanados acá secundarios son para crear la oscilación y un autoalimentación y un autocontrol acá está la parte primaria.

El secundario es el que entrega el voltaje que es convertido en el voltaje de standby cuando está integrada la fuente de standby es más complejo. (Minuto 10:40) porque ya son multiples salidas, una falla en una de ellas puede transtornar incluyendo la de standby.

Para poner un ejemplo es cuando el transistor HOT se pone en corto. La fuente arranca desde el corto y se protege por sobrecorriente, bajo esa condición la fuente puede presentar varios síntomas:

1. Led frontal piloto titilando (flasheando): se confirma con cualquiera de los voltajes fluctluantes a la salida.
2. Son tan bajos los voltajes entregados que no alcanza a encender, sin embargo se puede llegar a escuchar la oscilación como un grillo.

#### Cuando el voltaje standby es correcto pero el televisor no enciende.
La falla no está en la fuente.

Cuando el voltaje entregado es muy bajo no debemos concluir que hay falla en la fuente, a no ser que se trate de la fuente standby.

Si chequear sin el diagrama, ocurre algún cambio en la fuente secundaria al momento de dar la orden de power, si ocurre es porque el microprocesador está dando la orden correctamente.

Fallas frecuentes: filtros.

Cuando los voltajes se bajan es causado por un mal filtrado.

Para chequear filtros es engorroso hay que desoldar 1 a 1 porque nos dan una medida errónea.

Otro es cambiarlo por descarte.

Capacheck (Minuto 18) si le interesa como medir.


### Veremos el caso cuando los voltajes son fluctuantes. Entonces significa que hay una sobrecarga en una de las fuentes o la fuente se encuentra sin control de voltaje entonces arranca se desboca y se apaga se protege.

Tenemos el diagrama de un televisor chino.

Acá tenemos la parte primaria (CALIENTE) ya estudiamos los transistores MOSFET.

Acá tenemos la parte secundaria para efectos de mejor calidad de imagen voy a hacer uso del diagrama original.

Ahora nos vamos a centrar en la parte de control.

Minuto 21:30: Esta es la parte secundaria la salida de los 12 voltios, la salida de 9 voltios y acá tenemos un regulador de 12.

Este transistor Q212 en condiciones normales que en su base son transistores digitales por eso aparecen estas resistencias.

Este transistor de referencia C124 por su base en condiciones de standby no hay voltaje por lo tanto estos 5 voltios de standby pasan a la base de este Q211 quiere decir que estará activo por lo tanto el voltaje que pudiera haber en la base del Q832 estará aterrizado. 

En la base del Q832 no hay voltaje y por lo tanto este transistor estará inactivo, quiere decir que estos 8 voltios que salen de la fuente y polarizan este diodo led que en realidad es la mitad del optoacoplador está una primera parte 802.

IC802 le informa al integrado un cambio al estar este optoacoplador apagado por lo tanto acá el fototransistor que estará dentro del optoacoplador también estará apagado, también estará dentro. Eso le indica al integrado modulador de ancho de pulsos que trabaje en modo de espera normalmente lo que hace es que aumenta la frecuencia entrega unos pulsos muy angostos con el fin de que la corriente transferida sea muy baja.

Sus voltajes secundarios estarán por debajo del nominal, acá no van a ver 12 voltios sino que 6 voltios.

Acá no habrán los 106 sino que habrán 80 voltios menos y así con todos los voltajes.

Sin embargo vale la pena resaltar que acá si saldrán los 8 voltios y más adelante vamos.

Cuando la fuente está en modo de espera en estas condiciones está el micro alimentado si le damos la orden de encendido el va a entregarle al Q212 transistor 5 voltios, en realidad no porque le entrega el micro por su puerto en el PIN que corresponde a la salida power acá no llegan 5 voltios porque hay una resistencia en el camino para que llegue .7 voltios que es lo que necesita el transistor para activarse.

Lo que sucede es que cuando el televisor recibe la orden de encendido el micro interpreta esa orden y entra 5 voltios con los cuales llegan acá .7 el transistor Q12 ya aterriza este voltaje, por lo tanto Q12 ya al estar su base en 0 voltios entonces el deja de trabajar y el voltaje que pasa por acá ya le llega al Q832 sucede que él va a trabajar, al trabajar es como que acá se cerrara entonces el LED el interno optoacoplador se va a encender cuando el se enciende entonces el optoacoplador y el fototransistor va a conducir cuando él conduce, cuando el cierra su juntura colector emisor a través de la resistencia le dice al integrado IC801 por el PIN 3 a trabajar mi amigo XD.

Lo que hace es ampliar los pulsos con el fin de que acá haya más transferencia de energía, al haber más transferencia de energía los voltajes se normalizan. Acá aparecen los 12 voltios acá los 206 y así con los demás.

Es la manera de como se hace la conmutación de la fuente cuando se trabaja en ráfaga a cuando trabaja a pleno.

#### Video 17.

Transistores: Q211 Q212 Q832, el LED simula el optoacoplador: es el que hace los cambios. En modo standby los 5 voltios no le llegan a la base del Q212.


