---
title: "[AUDIO][APUNTE] Taller de instalación y reparación de aires acondicionados (Clase 20) - Preguntas de examen. Diagrama placa aire acondicionado: Por pulsos y por relay. Comprar tablerito para probar placa."
date: 2024-11-30T12:29:38-03:00
tags: ['AC']
---
### Audio en Vocaroo
https://vocaroo.com/1lMKm7jBm17G
### Audio en YouTube
https://www.youtube.com/watch?v=5-TSjvdLMFA
### Audio en Invidious
https://redirect.invidious.io/watch?v=5-TSjvdLMFA

PDF: [Resumen de todo lo dado en clase](/files/aires/Clases_230206_123534.pdf)

## FOTOS: https://imlauer.blogspot.com/2024/11/clase-20-aires-acondicionados-placa-con.html

### Notas de clase:

Preguntas de exámen en el:
- Minuto 45:15
- Minuto 55:00 (antes)
- Hora 01:25:01 

### Transcripción (Desde minuto 04:52) La teoría empieza en el minuto 16.
Algunos aires de ventana no traen tornillo traen seguritos, tenés que tener un cuidado para que no se rompa nada, uno que se rompa queda todo traqueteado.

Cuestión que eran las 12 y media de la noche, cuando estiro el segurito suelta vos sabés que miro y me agarró al principio ví todo blanco fue un golpazo, cuando veo mi mano estaba llena de sangre.

#### El secreto para que no te quede negro el ojo abundante hielo con manteca.

Me dió 83 con el aparato para medir azucar en sangre, después de un recital de Andrés Calamardo chupando fernet.


Un día se le dió por saltar al hijo del profesor y se abrió una herida, el profesor le enjuagó todo le cerró y le puso la gotita, ahí nos fuimos al médico. 

... El profesor cuenta anécdotas que tuvo con su hijo ...
Alumno: El fruto no cae lejos del árbol.


# Acá comienza teoría: arrancamos con placa electrónica.
Hay dos clases: una placa a pulsos y otra a relay.

# Cuando necesitamos hacer una reparación, vamos a tener que desarmar la unidad evaporadora para saber que tipo de placa lleva, una a pulsos o una a relay.

### Como se van a dar cuenta que placa lleva? Mediante el diagrama eléctrico

## Cuál es línea, arranque y trabajo?
La línea siempre está sólo. El trabajo está acompañado del neutro. Y el arranque está conectado al capacitor sin el neutro. El capacitor está entre trabajo y arranque.

Línea arranque y trabajo, del capacitor para acá es trabajo y del capcitor para allá es el neutro, y en esta parte del forzador también vamos a encontrar 3 cables que van a hacer los encargados de manejar los RPM y el LGD y el serial del forzador, eso se llama sensor hall. Si yo veo este tipo de forzador me marcará que es el forzador que se va a manejar mediante una placa a pulsos. 

### RPM LGD 

### La conexión es fácil si nosotros necesitamos identificar linea arranque y trabajo tenemos que medir los 3 cables entre el rojo y negro, negro con blanco y blanco con rojo, y ahí me va a dar la resistencia y con eso saco la línea arranque y trabajo.

En caso contrario en nuestro forzador siempre estará el diagrama eléctrico, el sentido de giro los amperages y los watts de ese forzador y ahí verán por que es tan difícil de conseguir el mismo forzador.

El amperage 0,15. Los watts 0,2. Ahora vamos a ver por qué es poco.

De esta parte tenemos un equipo de 200 frigorías.

#### Ahora esa flechita me está diciendo que ese forzador siempre tirará para el lado derecho.

# Neutro en la placa electrónica siempre vamos a encontrar una bornera de neutro y va a ir conectado siempre a neutro. 

### Línea va a ir conectado al PG, el PG es el encargado de manejar la variación de velocidad en este forzador.

Este tipo de placa es la que mejoraron para desarrollar la tecnología inverter por eso se llama placa a pulsos porque una placa inverter se maneja mediante pulsos.

### Entonces como vamos a aumentar y disminuir la velocidad?

Entonces como va a aumentar y disminuir la velocidad, vamos a tener un relé térmico que dirá **90 grados** por ejemplo, si este forzador se pasa de temperatura ese térmico va a cortar.

Ahora nosotros tenemos línea directa, como va a aumentar mediante una variación de velocidad en este caso de voltaje, vamos a tener 80 100 y 190 voltios.

### Entonces que significa? Que todas esas velocidades va a alimentar una sola bobina lo único que va a hacer es aumentar o disminuir el voltaje, si disminuye irá más lento si aumenta el voltaje irá más rápido. Esas son las 3 velocidades que encontramos en una placa a pulsos, luego de esas 3 velocidades vamos a encontrarnos con una bornera de interconexión, una línea un neutro línea 3 línea 4 y tierra.

### COM es entrada al 220
### ON es salida línea directa al motocompresor. (LC)

Neutro se divide en los diversos componentes acuérdense que esta señal va a la unidad exterior en donde está el motocompresor y que se iría en el motocompresor? Neutro para el motocompresor, neutro para el forzador, neutro para valvula inversora y neutro para el neutro. Para lo que era el capacitor se acuerdan que estaba el de trabajo y también se dividía en 2.

Línea 3. Va a representar a lo que es válvula inversora.  
VR significa válvula inversora  
Y FAN OUT significa forzador exterior  

Lo que yo tengo que tener en cuenta que hay una parte que lleva un fusible. 

**Si dice COM no es de compresor, porque este sensor que está acá es el sensor de ambiente, el sensor de ambiente vamos a tener un transformador de 220 a 12 voltios**. 

Nuestra placa estará dividida en dos partes la parte de 220 y la de 12 voltios.

La parte de 12 voltios va a manejar todo lo que sea sensors, visores en el caso que sea digital, swing, manejará el display.

Si yo necesito reparar mi placa lo primero que tengo que hacer es revisar si el transformador me manda 220, **como lo voy a hacer?** Si no entra 220 al transformador reviso el fusible si no se cortó.

### Una vez que tengo alimentación en la otra parte de la placa vamos a encontrar un parlantecito si no suena el parlante es que no le está llegando 12 voltios a la placa entonces es probable que sea mi transformador, lo cambio y terminó el problema.

Una vez que reviso el transformador y prende mi placa en el caso que no prenda entonces es el fusible.

Una vez que funciona la placa yo prendo con el control recibe la señal del mando sensa la temperatura ambiente y la temperatura de ambiente es la que manda la señal al relay para que ese relay pegue, **como es la alimentación al relay?** Entra 220 y sale línea directa al motocompresor, la línea siempre es directa al motocompresor.

Pega el relay y sale línea al motocompresor. 

No estoy siendo muy específico como funciona realmente, pero sí estamos siguiendo el circuito del sistema impreso para tener una identificación.

### En el forzador yo puedo llegar a observar que en el forzador aparte de línea arranque y trabajo me salen otros 3 cablecitos más, esos 3 cables juntos se llaman **sensor hall**
#### Ese sensor Hall lo podemos también en la placa es el GND.

## Van a encontrar en esta parte que yo puse GND, una S de señal y un VCC (sentido de giro del forzador).

## GND es neutro.

Tenés una señal, tenés un voltaje, y tenés un neutro, van a ver por qué alimentan a esa señal y para que sirve, normalmente ese sistema si es positivo siempre se encuentra cerrado.

Ahora este cablecito que es del tacómetro del sensor hal, va conectado al GND ese y el VCC, es utilizado en muchos componentes como por ejemplo el lavarropas que atrás tiene un tacómetro marca las revoluciones que está girando ese forzador, es un sistema de seguridad que trae para proteger.

Si yo alimento mi forzador con la velocidad alta, esto tiene que girar a ciertas revoluciones ahora si yo tengo velocidad alta y esto está girando a media velocidad el sensor hal manda una señal a la placa la placa abre el circuito y se desconecta la línea al compresor no importa que el ambiente siga a temperatura sino que por medio del forzador corta y empieza proteger nuevamente el motocompresor.

Entonces al estar conectado ..?? acá en esta parte en donde tenemos el visor, vamos a empezar a ver los primeros códigos de errores, puede ser que si solo tengan luces intermitentes como tienen en esa placa puede ser que prendan una luz amarilla y verde y empiece tatata (3 veces).

### Que puede ser? Tengo que leer el manual, puede ser el forzador sucio, que esté totalmente tapado de mugre y quede pesado el forzador por eso no llega las revoluciones altas y llega a medias nada más, puede ser capacitor agotado, entonces yo como técnico viendo ese código de error, voy y ataco solo a lo que es.

Y empieza tatata (3 veces).

Supongamos que ahora me parpadea 5 veces, miro el código de error, y me dice sensor ambiente capacitor y forzador ahí ya me está marcando más código de error porque no solamente el GND me está recibiendo una señal sino que también los otros sensores me están recibiendo otras señales y en este caso es el sensor de POZO.

### Qué significa el sensor de POZO?
Que está pasando líquido refrigerante, el líquido refrigerante al motocompresor tiene que llegar gaseoso, si ese sensor empieza a detectar que está pasando líquido refrigerante es porque las revoluciones del forzador no es el adecuado y no le da para sacar todo ese calor, acuérdense que el líquido refrigerante se tiene que evaporar junto con el calor que está absorbiendo del ambiente, si el líquido refrigerante empieza a retornar al motocompresor pasa por el sensor de pozo y cuando esto sensa el líquido refrigerante tira el error. Lo mismo va a cortar la señal y va a apagar el equipo.

Otra cosa que nos podemos llegar a encontrar hay que ver el diagrama para saber si es una placa a pulsos o a relé.

### Después de esta parte acá pueden encontrar lo siguiente: en todos los controles suelen tener Power y esto es poder velocidad máxima, si queremos en el control tenemos un power que es el turbo, velocidad máxima. Y ahí tenemos el 220 directo a la bobina su máxima velocidad funciona, ambiente y pozo.

El sensor ambiente es el encargado de tomar la temperatura del entorno para saber si cortar o no y va a mandar una señal en corto cuando llegue a la temperatura de 24 y el sensor del pozo hará lo mismo.

La semana pasada cuando fuimos a hacer el trabajo tenía un equipo de 6000 frigorías que no traía contactor yo les recomendé colocarle un contactor a ese equipo.

## Los equipos grandes traían los cables mucho más preparados que los de ahora, pero el que hacía todo el trabajo era el relay de placa, los relays de placa soportan hasta 30 amper, entonces es más que obvio que antes los materiales eran de mejor calidad.

El relé de la placa maneja un contactor y el contactor maneja la potencia.

## Hoy en día podés poner una placa universidad que maneje un motocompresor y en poco tiempo si es un contactor mi placa está cocinada por más que digan que se banca 30 amperes, la arrancada y las paradas le va a matar a la placa.

### Fijense que ese equipo es viejito y no tiene contactor o a lo mejor anularon el contactor. Que era lo que yo supuse y le pusieron ese relay directo que tenía. Y yo le dije tiene mucho espacio para mi que acá anularon el contactor y le pusieron eso, conviene comprar un contactor y le pusieron eso pero no es lo correcto, conviene comprar un contactor y colocarlo a ese equipo van a proteger al motocompresor y todos los componentes.

Encima estaba conectado el forzador, es más andá a saber si andaba el motocompresor pero ya lo vendieron. 

El equipo del alumno tenía 2 capacitores uno de 60 mf y otro de 16.

La función más común que utilizamos en un tester es medir continuidad.

Detrás de la placa vamos a tener un circuito impreso y es el circuito más sencillo porque son todos gruesos, vamos a tener que ir mirando.

A veces con la temperatura se levanta la pista, lo único que tenemos que hacer un puente y somos terribles técnicos electrónicos, pero los otros componentes son re fáciles: un relay puedo cambiarlo, un transformador lo puedo cambiar porque solo enchufo y desenchufo, los ambiente y de pozo lo puedo cambiar también.

Para medir los sensores puedo utilizar en ohmeage para este lado tenía 100 y 200, para el otro lado voy a tener otra cosa voy a tener 60 20, son resistencias pequeñas.

Ahí recién voy a poder medir los sensores, todos los sensores tienen que decir de cuántos k es, el que lee de cuentos ohmios es paga el asado, ahí se van a dar cuenta por qué todos los técnicos electrónicos usan su lupa.

Alumno: El pozo adonde va? El de temperatura siempre está en el del evaporador por la rejilla.     
Profesor: Va en la serpentina del evaporador a la salida casi prácticamente porque tiene que sensar si está regresando líquido refrigerante al motocompresor, y en todos los equipos trae un hueco en donde va alojado ahí, que tiene contacto con el conducto de retorno.

El swing se abre y se cierra es el flap del equipo.

### Pregunta de exámen
El swing tiene 4 posiciones vamos a ver que en el pin tiene 7 y los cablecitos de su motorcito swing tiene 6. Si yo tengo 6 en el swing y en placa me falta 1 al neutro.

# PREGUNTAR
# Por qué tengo 4 posiciones? Tengo que conectar estos 4 acá. CALZA PERO SOBRA 1. Ahí resolvieron lo primero y en la primer posición, como encuentro la 2da posición si no funcionó mi swing en esa posición, si le pongo uno abajo sobra uno arriba esa es la segunda posición, ahora te faltan 2 más... Los pines pero dado vuelta.

## Ahora el GND pasa exactamente lo mismo, tengo 3 yo coloco la placa universal si yo agarro enchufo pero no funciona que tengo que hacer? Invertirlos no hay otra forma.

Arranque siempre va solo.

Che enchufé el swing y no me anduvo, intentá darlo vuelta.

# Errores del examen
## En COM ponen la línea y en ON ponen el NEUTRO, y ahí que pasa se pega el relay y queda en corto.

Dibujen el motor y vayan conectado la línea PG que es el que maneja la variedad de velocidad.

# El swing tiene 4 posiciones: Una arriba otra abajo y las dos posiciones que probaste al principio le probás dado vuelta: una arriba otra abajo. Una arriba otra abajo das vuelta una y después ?¿? de nuevo... 4 (Minuto 52) Al invertir el pin te seguirá cerrado y tenés una opcion más.

La línea va al COM (al común) y después el NEUTRO va al NEUTRO de la bornera, ahí ya tengo alimentación a mi placa, nadie se dió cuenta que faltaba el neutro.

# Examen

# En la prueba son 60 preguntas: verificar cual de los dos esquemas es el correcto.
# Método de compresión: 2 métodos de compresión diferentes y marcar cual es el correcto mostraba el ciclo de la refrigeración circulaba salia por el motocompresor en forma de gas y marcar cuál de los dos era el correcto.

# Que tipo de refrigerantes conocés y a que presión trabaja? 
# Marcar lo que corresponde por cuál medimos el refrigerante? En el caso correcto justificar su respuesta. Opciones: Capilar, retorno y válvula inversora o ninguna es correcta. La respuesta correcta es: ninguna es correcta porque es por el robinete, el robinete es la única manera de medir, o al menos que sea un aire de ventana y se tenga una válvula de servicio.

# Otra placa: Minuto 58 / Vamos a avanzar con esto, esta placa es la misma cosa

Esta es la misma cosa, forzador fan IN. A diferencia del otro forzador en este forzador encontraremos 6 cables, y en el otro 3 cables.

Aquel no tiene sensor ahora en ese tipo de forzador. 

Fijense como cambió de la placa a relay, porque aquella es una placa totalmente a relay, tenemos un relay al motocompresor a la velocidad alta media y baja, sus velocidades son por separado.

La diferencia que hay entre una placa y la otra es que en esta maneja una variación de velocidad y en esta maneja su velocidades por separado. O sea que uno de los cables será bajo medio y alto, neutro y capacitor.

## El aire de ventana que tipo de placa lleva? ... Mira yo tengo 2 velocidades bueno compra una placa de relay para 2 velocidades.

Si tenés 2 velocidades en aire de ventana y en qué velocidad vas a colocar? Alta y baja y te sobra el medio y si el cliente pone en media no va alimentar a nada así que el forzador no hará nada y el compresor seguirá andando. No podés colocar algo que no va en el componente.

Hay veces que falta una alimentación, yo mirando me doy cuenta el neutro no entra si sale salió el neutro.

Qué necesito para que la lamparita prenda? Positivo y negativo.


# Como controla el exámen el circuito el profesor.
Para que ese circuito se cierre yo lo miro de lejos, hago lo siguiente: decime el negativo, viene el negativo se va pasa por todos los componentes y sale al positivo cerró el circuito listo está aprobado, es lo único que controlo.

### Ahora hay una diferencia, si yo pongo negativo acá y positivo acá funciona eso?  Sí, funciona pero el equipo debería pasar exactamente lo mismo pero la protección de lo que es el component es diferente, porque si yo toco lo que sea neutro y toco masa me puede generar un corto en base a cuando el **positivo es el único que pasa por lo que es el fusible**. Si no tengo fusible y está todo invertido voy a terminar quemando la placa.

Seguimos... A lo mejor sin querer invirtió y quemó la placa, invirtió el neutro y la fase 

## La diferencia de las placas es que uno alimenta mediante una variación de velocidades y el otro maneja diferentes bobinas.
# Eso significa que arranque ALTA irá conectado a ALTA. Media irá conectado a media y baja irá conectado a baja, neutro y termina esto es una línea linea y linea.

Las 3 líneas manejan 220, y la otra 80, 100 y 190.


# EXAMEN
# Tenemos 220 220 220, entonces ¿cómo aumenta y disminuye su velocidad ese forzador? Si todos son 220? Por la resistencia de la bobina, alimenta una bobina diferente vamos a tener la conexión al neutro y hará esto la **baja es la mas larga**: alta media y baja. Mientras más largo sea la bobina pasa menos corriente, o sea que su velocidad irá disminuyendo, mientras más corta pasa más corriente.

Yo con este diagrama eléctrico con baja, media alta automáticamente sé que lleva una placa a relay, su velocidad aumenta o disminuye según el campo en la bobina que voy a alimentar, y ahi viene si yo tengo uno que tiene 2 velocidades voy a tener una alta y una baja y qyo quiero colocar una aplaca placa voy a alimentar a la alta a la baja y mla media me va a sobrar, cuando elcliente ponga la media el forzador se va a detener el compresor seguira funcionando porque todo lo otro sigue funcionando

La conexión: línea salsía del COM, va a ir alimentado vamos a alimentar rápido un motocompresor con un forzador exterior con su vamos a hacerle así: linea, neutro, linea 1, linea 2 y tierra todos sabemos que linea va con linea, neutro va con neutro 1 con 1, 2 va con 2 y tierra va con tierra.

# Esa es la conexión del evaporador y el condensador. 
# Algunos en el examen MAL hacen esto:
Hora 1:08 (conectan mal el capacitor)

En el forzador pasará exactamente lo mismo y la línea irá al 1 porque ese va a conectado con frío solenoide, línea solenoide y luego vamos a tener otro neutro al solenoide al neutro. Esto a veces se agrega y a veces se le saca hay que leer el diagrama eléctrico, esto es un dispositivo con el solenoide que tiene una pequeña bobina que actúa por inducción y todo lo que tiene adentro de ese campo es absorbido y esto trabaja con 220.

Alumno: Y es convención que el L1 es forzador, L2 es ...
Profesor: Dónde van a ver eso? En el diagrama de la tapa, por eso siempre recomiendo pasar un trapito que no se borre el diagrama. Sino no hay problema y tendrán que abrir su carpeta y ustedes hacer su conexión eléctrica no lo que representa el aire.

Por eso uno va a ver el diagrama eléctrico y dice che pero esto no coincide con el diagrama, y a lo mejor hicieron su propio diagrama.

# Importante
Linea 1: fan.  
PR válvula inversora  
Línea 2: válvula inversora  
Y el PG que yo acá les quería mostrar que en esta placa NO VA, va FAN OUT que va al neutro.

Allá no le agregué esto y ustedes entendieron re bien, ahora le agregué un tema que ya dieron y se les complicó.

Esto es la unidad evaporadora la parte eléctrica y esto es la unidad condensadora.

Alumno: No termino de entender el solenoide, donde está trabajando?
### Profesor: El solenoide trabaja en la válvula inversora. La válvula inversora así como el motocompresor está dividido por dos partes, la parte mecánica la que divide si es frío calor la que selecciona el frío/calor y dentro de esa tiene un tubo cuando activa el 220, la válvula el solenoide absorbe su tubito y manda el refrigerante para abajo, el condensador pasa ser el evaporador y el evaporador pasa a ser el condensador.
Hora 01:12

## Como probamos si el solenoide funciona o no, agarramos nuestro tester ponemos en voltaje y común siempre común, agarran manda señal al compresor colocan ponemos 220 listo, está en modo frío coloco en el 1, 1 es fan out manda señal 220 sí, PR manda 220? No, porque esta en modo frío, no tiene que mandar. Si manda 220 acá y en FAN OUT no manda está en modo calor.

Por eso en invierno en modo frío siempre prende el compresor solo no el forzador, necesitamos levantar temperatura en ese compresor para que mande gas refrigerante adentro.
Alumno: En linea 2 tiene que pasar 220 en el modo frio sí y en el 1 calor.

Profesor: Cuando esta en modo calor el forzador está sin señal es decir sin 220, y en frío el motocompresor y el forzador esta funcionando. Eso igual lo hace en un instante cuando llegó??? a temperatura el motocompresor automáticamente vuelve a prender el condensador porque eso se tiene que congelarse, acuérdense que el condensador pasa a ser evaporador y entonces el que se va a hacer hielo es el de lado de afuera.

Hora 01:14

Yo conozco muchísimos técnicos que dicen: "ah no anda el forzador che no está arrancando tu motocompresor" como va por separado entonces que hacen? La línea del FAN OUT le anulan y tenemos el ventilador acá y el motocompresor acá y le sacan la línea y la línea del motocompresor entonces si vos activás el calor que es el VR prende el motocompresor pero **tarda el doble para levantar temperatura** porque está el forzador a full, es como el auto cuando es invierno cuando hace frío prendés la calefacción es peor, lo que hacían era prender el auto un rato antes de salir levantaba temperatura y ahí prendían la calefacción y ahí desempañaba el vidrio.

### Lo mismo pasa en la unidad evaporadora adentro del domicilio, yo pongo en modo calor prende el compresor afuera y adentro no tira nada. Porque imaginate si prende automáticamente en invierno me va a empezar a tirar aire frío me voy a congelar hasta que tire el aire caliente, NO PRENDE POR ESE MOTIVO para que el usuario no sienta el frío, sino que sienta la corriente de calor una vez que actúo, los dos trabajan por separado si o si, cuando es calor una cosa y cuando es frío otra cosa.

Alguna duda con respecto a eso?

La clase que viene vamos a ir conectando esto.

### Conexión de capacitor tiene que ser una papa 
El que no entiende puede venir los días viernes de 2 a 6:30.

### Alumno: que se hace con un aire al que no le hicieron vacío e hicieron el barrido?
Profesor: Y nada, podés seguir utilizando el tema es que cuando vos coloques el manómetro te vas a dar cuenta si está contaminado o no, te vas a dar cuenta porque la aguja empieza a oscilar, porque siente el fluido de escarcha, en vez de que sea gas y mantenga la presión de gas al pasar genera turbulencia entonces la aguja empieza a oscilar.

Alumno: Supongamos que se sanidar eso.
Profesor: Tirá todo el refrigerante y hacé un vacío de 20 minutos
Alumno: No hace falta cambiar el aceite
Profesor: No, no es. Lo que si es el aceite es que cuando vos saques vas a sentir el olor porque está cocinado se tuvo que desoldar el motocompresor así como comprás nuevo voltear y tirar todo el aceite **obviamente que en un recipiente** porque no sabés cuanto aceite necesita y necesitás saber la cantidad de aceite que sale porque tenés que ponerle la misma cantidad de aceite.


Mientras que eso de la zundilla sale todo el aceite??? (Hora 01:21) tenés que estar sacudiendo todo para que salga el aceite.

Alumno: Supongamos muere el motocompresor y el gas que vamos a recuperar se puede en un recipiente recuperar?
Profesor: Tenés que comprarte un recuperador de refrigerante, tenés que tener una balance electrónica de carga de refrigerante también.

Alumno: El 410 no se puede encimar
Profesor: El 410 no se puede encimar, son diferentes componentes si perdió un poco casi siempre va a perder la parte más liviana, la parte más pesada siempre se queda alojado pero quedará el pesado dentro del compresor, entonces quedará composición cuando tenga que chocarse para generar la reacción química no funcionará, rendirá poco porque tiene desparejas composiciones. Hay que tirar todo.

El R-32 es un poco inflamable, no te va a matar pero lo es, hay otro método para tirar el refrigerante.

Hace tiempo que querían sacar el R-22 de circulación cuando vos lo querías tirar tenías que hacerlo en embaces en una casa de refrigeración te tienen que regalar la garrafita para que vos puedas embazar el refrigerante viejo y eso se manda a córdoba y en córdoba lo limpian lo purifican y se vuelve a re-utilizar el refrigerante.

Para solucionar ese problema salió el R-32, 100% ecológico es puro.

El R-32 no es peligroso con su carga, es peligroso cuando está vacío.

Pero el R-32 no es nada, está el R-600 que traen las heladeras.

Una vez el vacío todo y le dejó un día entero y en el aceite quedan burbujas y las burbujas del aceite tienen un gas empieza a hervir ese aceite por la temp... y parecía un escape el motocompresor, nos reíamos.

Vieron como cuando ustedes se pasaron con el soplete, así.

# El otro día un alumno vino a llorar acá, una de las preguntas era como debo chequear un equipo de refrigerante en el caso de que tenga pérdida, y ahí hizo todo los procedimiento y en el caso de que tenga pérdida y agarró y puso presurizar la cañería con oxígeno.

Ahora les voy a compartir el PDF.

### Hay que comprar placa a pulso o a relay
Voy a ver si le consigo un forzador a relay, es muy difícil conseguir y el que se quiere comprar un tablerito así, me avisa y yo les digo que componentes se tienen que comprar entonces practiquen para el día del examen práctico.

Es re útil tener ese tablerito por ejemplo si se te fundió la placa ponele el tablerito ese ponele la placa original y ves que componente está fallando.

## Ahora vamos a ver bobinado

## Cuál es la diferencia entre el R-22 y el R-410? La presión

Alumno: La válvula del aire de los autos tienen la parte superior del limpiaparabrizas, normalmente tienen la válvula de baja que es la parte de arriba.

Ahí tienen una placa a relay.

# Todo lo que está acá entra en el examen el PDF, lo único que no entra es el capacitor de arranque porque eso se trabaja en heladeras y el arrancador también es de heladeras. Hay una parte que era lo que ibamos a dar hoy,
# que es instalación de un aire acondicionado tipo split, es largo.

# El número 1 habla sobre el trato del cliente es recomendable siempre pasar el presupuesto mano de obra y el de los materiales por el otro.

# La alimentación eléctrica al equipo no incluye la instalación eléctrica de la unidad no puedo instalar un equipo y tmb hacer el toma corriente, soy técnico en refrigeración no electricista, tenemos que hacer otro presupuesto para lo que es instalación eléctrica y por ende es otro tipo de trabajo, y los clientes no quieren reconocer.

# El número 2: instalación de la unidad como va a ir ubicado que capacidad si es o no para el ambiente, como yo sabía si era o no para el ambiente esto se llama balance térmico, y habla sobre el lugar específico de como ubicar el equipo a 10 centímetro mínimo del techo y 20 en el caso de que esté a una pared lateral. Y siempre aprovechando lo largo de la habitación.

La presión que tiene que tener el refrigerante es relativa.

Que lo que querés ahora polaco? Tomá mi vida ponete cómodo XD

## Cuando nosotros instalamos el equipo y liberamos el refrigerante lo que pasó es que se descompenzó el equipo y empezó a subir de a poquito la presión lo que significa que si nosotros tenemos una temperatura de 35 grados en un R-22 se va a ir a 


### La presión del equipo cuando instalamos el equipo y liberamos el refrigerante lo que pasa es que se descompenza el equipo vuelve a 0 y vuelve a subir despacio la presión, eso significa que si nosotros tenemos una temperatura de 35 grados en un R22 se va a ir a los 5 minutos a

## Si se conecta un equipo y se pone en marcha la presión del refrigerante va a bajar si es R-22 a 35 grados en 5 minutos, la presión se estabilizará entre 57 a 60 psi a 35 grados, pero nosotros acá tenemos normalmente 45 grados o sea que la presión se irá a 65 PSI, imagínense en invierno que tenemos una temperatura de 24/25 hacer una reparación se puede hacer pero no dejamos los 60 PSI dejamos 45 o 50 psi, en el verano cuando funciona se va a ir. Si dejo 60 psi en invierno en verano se va a ir la baja a 80-90 psi y la alta 181 PSI, el motocompresor no aguantará.

Lo mismo pasa con el R-410

## Recuperación del refrigerante
Si se debe instalar un equipo en donde la unidad condensadora es mucho más alta que la unidad evaporadora llegando hasta 3 metros de alto, se debe utilizar una trampa de aceite, la trampa de aceite se hace en el campo de succión, retorno, la línea de gas.

### Acuérdense que si está mucho más alto siempre va a pasar poco aceite por el líquido refrigerante entonces lo que sucederá es que al motocompresor le va a costar regresar ese aceite y va a llegar un punto en que el motocompresor va a trabajar con poco aceite, ni hablar si ese equipo comienza a perder refrigerante ahí si que va a faltar todo el aceite y ahí el equipo al quedarse sin aceite el equipo se clava.

Abajo en el PDF hay código de errores.

#### Hoy en día colocás código de errores para tal equipo y te aparece el PDF de esa unidad o en el Meta de WhatsApp.

#### Hablando del manómetro (el manómetro del compañero es de 410 entonces tiene un acople para usarlo en R-22)
Válvula de pinche?? Esto es para R-410, entonces esto son acoples (un adaptador) para equipo 22 vos vas a tener que colocar en el 22 este para poder colocar como queda?? (01:41), son de 1/4 o sea que es la válvula de 410 no son de mediaes para no contaminar no mezclar.

## Siempre usá el azul para el R-22, y usá el rojo para el R-410 SIEMPRE, no se le saca el plástico porque eso es el orrin en ese caso vas a tener que agarrar una pinza punta fina y desenrozcar en el medio o con un sacabollo XD ??? para que salga un poco más y haga presión en este (está hablando de la válvula de pinche de la adaptación del manómetro de R-410 a R-22)

Yo busqué tuerca y me apareció una foto que dice para turca de 5/8 caño de 5.

Profesor: Yo mido y te digo este ni a palos es 5/8

El caño es 5/8 y el otro 3/8.

Alumno: Yo le medí son 3,40 metros

## Profesor: Vieron que en la casa de mi viejo el split que superaba la altura, el condensador estaba más alto que el evaporador y no hicimos una trampa de aceite, en el aire de techo como no hicimos trampa de aceite hicimos un RULO ALTO que superaba al equipo, o sea que pasaba por arriba del equipo y ahí recién entraba al robinete, entonces el equipo tiene que empujar hacia arriba y el aceite se mantiene abajo.

Hoy en día se compra la trampa de aceite, imaginate doblar un caño de 5/8 en forma de S.
