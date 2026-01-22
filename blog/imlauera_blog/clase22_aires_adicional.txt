---
title: "[AUDIO][APUNTE] Taller de instalación y reparación de aires acondicionados (Clase 22) - Capacitación reparación de placas Inverter. Frecuencia. Componente con más fallas: diodos. Conmutador: componente de 7 patitas. El optoacoplador es un integrado que de un lado tiene un diodo y del otro lado tiene un fototransistor. Optoacoplador: Es como una especie de relay. Cuando lo desenergizas el relay se despega, y cuando lo energizás se pega, es una especie de relay electrónico. El optoacoplador aisla y se banca hasta 5000 voltios. Conectás mal fase y neutro y explota el integrado. Verificar si transformador roto: de un lado te da 220v pero del otro lado no XD. La memoria es difícil que se dañe. A veces vienen 4 diodos, a veces un puente. Efecto hall. Componente que falla mucho TRIAC, le da la velocidad al ventilador. Cuando se daña el TRIAC: apagás el compresor y el forzador sigue andando o prendes pero no prende el forzador, tenes que revisar motor capacitor si no encontras defectos entonces es el TRIAC de la unidad interior.  Factor de potencia: Cuando conectamos una bobina ya sea un motor, un transformador lo que pasa con la corriente eléctrica es que nosotros tenemos la corriente electrónica cuando conectamos una bobinas se produce un adelantamiento de la corriente con respecto de la tensión. Se produce un adelantamiento y un desfasage, la corriente adelanta y la tensión atrasa. Los capacitores atrasan a la corriente con respecto a la tensión. La bobina adelante la corriente, el capacitor atrasa. Si no tiene capacitor tenes que mirar la tablita. Con un inverter nunca te vas a encontrar con eso porque no tiene capacitor. Hay que respetar capacitor por el factor de potencia. Si le pones un capacitor más grande no es que va a ir más rápido estás arruinando el factor de potencia. Cuando el control remoto no les funciona no le responde, hay que desarmar el display y nos encontraremos con el receptor infrarojo tiene 3 patas y es lo mismo que el sensor RPM. Tiene una pata de alimentación positivo negativo y otro de señal, puede estar invertido positivo negativo, señal. Eso suele dañarse, sacan la tapita vamos a encontrar el sensor. Sacar humedad placa: ponele tiner aunque saca el esmalte es más barato que alcohol isopropilico. Como comprar cables. El cable de señal debe ir separado y la puesta a tierra es importante, a veces tarda en fallar si no tiene tierra a veces pasa meses o años. Si no el equipo no le trajo el cable tenés que comprar 2 cables bipolar tipo taller de 2x1 y medio o de 2x2,5 de acuerdo a la potencia del equipo. Cuando te marca un error y se apaga el equipo casi siempre es un error de señal. En neutro y señal con el equipo prendido en continuidad tu tester debe dar entre 5 y 15 voltios, pone tester en escala de 20, en los equipos grandes entre 25 y 50v (en la unidad exterior e interior). Poner terminales si o si porque mete ruido en el cable de señal. Las 3 bobinas tienen que marcar un valor igual o casi igual. En el inverter es difícil volver a cargar hay que poner motor a pleno asegurarse que esté bien hecha pestaña. La deuda del 30. Tener un secretario para que tenga el sensor de ambiente. El inverter siempre usa R-410. El modulo IPM le da el uso a las bobinas. Lo que más se quema es el varistor(protector de alta tensión) que se pone en corto y quema fusible. En los aires tenemos sonda NTC. Al aumentar la temperatura en el ambiente el sensor está bajando su resistencia hasta que llega a un punto que deja pasar la tensión y el microprocesador enciende el motocompresor cuando la temperatura del ambiente comienza a bajar, la resistencia comienza a subir hasta que no deja pasar más la corriente y el procesador apaga el equipo, así maneja el sensor de ambiente. Sensor: Como esto es una resistencia estos 5 voltios tienen que tener una caída de tensión, y acá a mi me tiene que medir entre 2,5 y 2,9 con el sensor enchufado en la placa, tocamos el tester y tiene que tomar esta medición, retiran el sensor y le tiene que marcar 5 voltios porque ahí no hay resistencia si medimos solo los pines (sacando el sensor), con el sensor colocado la resistencia se divide en dos. Bobina toroidal. Filtro pasabajos doble filtro, la placa tiene 2 varistores. Varistor produce cortocircuito para hacer saltar el fusible. Fijarse que no sea un problema de falso contacto hay que mirar con lupa que no esté rajada placa sobre todo en la parte de potencia. Esta bobina toroidal es el corrector del factor de potencia así como en la industria tiene mucha bobina mucha carga reactiva nosotros acá tenemos mucha carga capacitiva, entonces en vez de agregar capacitor tenemos que agregar bobinas.  El módulo IPM le dará uso a las diferentes bobinas: U,V,W. Si invertimos la fase habrá U y el motor querrá girar y va a cagar pero podemos corregir no se quema porque las bobinas son las 3 iguales.  La bobina adelanta. El capacitor atrasa.  De ahí tendremos el diodo y el transistor que corrige el factor de potencia, porque en la industria el corrector de factor de potencia es del modo estático como este varía la velocidad del motor entonces el constantemente tiene que estar corrigiendo el factor de potencia, el transistor junto con el integrado va tomando la señal y va tomando el consumo y van corrigiendo el factor de potencia.  Acá no hay maestro esclavo, son independientes las placas.  Tiene 3 placas, la 3era es el banco de capacitores.  Cuando es un equipo grande tiene una diferente conexión sino se conecta igual que el otro.  Medir optoacoplador: De un lado te mide como un diodo como un fototransistor. El punto marca de que lado está el diodo. Para un lado marca 1,047 para el otro lado no te tiene que marcar nada (a veces marca porque estás midiendo mal otra cosa).  El motocompresor puede cortar por temperatura pero es improbable antes se te va a dañar el IPM (hay que cambiar la parta térmica).  El IPM es un módulo inteligente de potencia.  Lo que tiene el IPM son 6 transistores IGBT que manejan a las bobinas del motor, desde el módulo del IPM podemos medir los 310 voltios entre positivo y negativo. Los 310 voltios que sería la entrada y nos queda una tensión de 15 voltios que estará también en el módulo que va a excitar a los transistores para que vaya dándole señal a las diferentes bobinas, el procesador le va a ir mostrando a qué bobina tiene que energizar.  El va a ir dando diferentes pulsos a diferentes bobinas para que el motor funcione y también va a ir variando la frecuencia más o menos ancho de pulso para que el motor baje o aumente la velocidad esa parte del circuito se llama PWN (modulación por ancho de pulso) también está puesta acá.  Cuando la unidad interior le pide a través del cable de señal más potencia porque hace más temperatura el circuito PWN le va dando más frecuencia.  Entonces nosotros acá tenemos los IGBT los transistores esto está todo encapsulado podemos medir los 310 voltios y podemos medir los 15 voltios que esté presente para que energize a los transistores si esas tensiones no están no funcionará el compresor o se les va a cortar, esa tensión ustedes pueden medirla con el equipo funcionando negativo y buscar la tensión, si están esas tensiones y no funciona entonces es problema del IPM. Cada 2 IGBT por cada bobina, ellos están cerrados los 15 voltios energiza el transistor hace conducir a través de la bobina y cierra el circuito. Necesitamos los pulsos de 15 voltios constantes.  Probador conectá las dos pinzas de cocodrilo U,V,W y les marcará los leds.  En esta placa nos encontraremos con 5 cables en el forzador de la unidad exterior si es inverter si es que tiene U,V, y W porque a veces usan de corriente alterna.  Color de cables al final. 5 cables: blanco: alimentación excita los IGBT, amarillo: el que le dice a que velocidad girar al micro y azul: el que le informa a que velocidad está girando.  Ya saben como medir el cable de señal, para saber si tenemos o no en el equipo medir el voltaje y si no tenemos medimos el optoacoplador para saber en qué condición está el optoacoplador es un diodo emisor de luz que del otro lado tiene un fotoreceptor.  Medir relay: El relay tiene una bobina y cuando la bobina se energiza esto se conecta y acá hay continuidad cuando la bobina se desconecta esto se abre y se despega, a veces suele pasar que al tener contacto se forma una chispa y el relay queda pegado. Pero si el relay está dañado algún componente se te va a dañar, si ves algún componente dañado relacionado con el relay revisá la bobina.  Según el profesor por buscar la falla no se cobra (en mi opinión nunca le tenés que decir al cliente cuál es la falla porque hay mucha gente que googlea y lo arreglan ellos)"
date: 2024-12-15T04:15:33-03:00
tags: ['AC']
---
### Audio en Vocaroo
https://vocaroo.com/16n8De5RYP7x

### Audio en YouTube
https://www.youtube.com/watch?v=T-g1ASyonHk

### Audio en Invidious
https://redirect.invidious.io/watch?v=T-g1ASyonHk

### Audio observación de mi padre:
https://imlauer.blogspot.com/2024/12/inverter-aire-acondicionado-teoria.html

### Fotos: https://imlauer.blogspot.com/2024/12/clase-22-adicional-aire-acondicionado.html

Dato de mi padre: Si te da una patada el capacitor significa que el diodo está rectificando XD.

### Transcripción
No sé cuanto ustedes saben de inverter, si trabajaron con algún equipo con tecnología inverter si nunca lo vieron, no hay tener verguenza ni miedo.

Alumno: Lo más importante es la puesta a tierra, si o si jabalina a tierra.

Acá estamos para compartir ideas y conocimiento.

Siempre trato de que si hay alguna experiencia me digan, por ahí ustedes tienen otro concepto.

Con respecto a la parte de tecnología inverter, nosotros vamos a empezar desde el principio.

La tecnología inverter se diferencia en ciertas cuestiones sobre los equipos convencionales que ya conocen, que ya instalaron y están haciendo mantenimiento o alguna reparación.

El equipo con tecnología inverter no cambia, todo el principio de funcionamiento es el mismo, vamos a tener un compresor, un forzador, el fan exterior, placa que comanda todo los periféricos que están conectados en la placa.

Tenemos que tener mucho cuidado en inverter. 

Si el equipo fue mal instalado o se presenta alguna falla el cliente le llama y le dice el equipo está tirando un error tanto no hay que quedar loco y ponerse a desarmar o tocar, lo primero tenemos que observar el equipo, **el cliente nunca te va a decir específicamente lo que es. Puede ser que el cliente tenga una baja tensión.**

Vos te vas pensando si será la placa de afuera o la de adentro, te vas complicado, tenés que irte a ver el trabajo con seguridad, nunca dudando, a partir de ahí analizan la falla.

Con el tiempo con más experiencia, se van a dar cuenta que no es tan difícil hay que comprender como funciona un equipo inverter, de prestar atención.

**Inverter lo que viene a cambiar es la parte del compresor y los motores.**
Eso es lo que se cambió en los AC.

Los aires que no son inverter tienen un compresor que tiene 2 bobinas. 
Los inverters tienen 3 bobinas.

**Se terminó la bobina de arranque y la de trabajo y el capacitor de marcha.** El equipo que tiene tecnología inverter ya no usa eso, porque es del tipo trifásico.


Cuando yo digo trifásico no me refiero a la tensión de 380 me refiero a las fases: tiene 3 bobinados, 3 fases.

No es necesariamente positivo pero se desprende de linea, U, V, W.

Eso es todo manejado a través de un módulo que está puesto en la placa de la unidad exterior.

Vamos a analizar ahora cuál es el módulo ese y como trabaja, es el módulo IPM que significa: módulo inteligente de potencia.

Ese es el módulo que le va a dar la corriente trifásica al motor en una onda del tipo cuadrática (creo que en realidad quiso decir cuadrada), ahí lo que hace el módulo es manejar la frecuencia.

**¿Qué es la frecuencia?**
Nosotros lo que tenemos normalmente es una nos van a entregar una onda sinosoidal si ponemos osciloscopio y vamos a ver como se dibuja la onda, vamos a tener esta forma:
INSERTAR FOTO

Esto nos dará 220 voltios y 50 hertz, la frecuencia es la cantidad de veces que la onda se invierte entre el positivo y el negativo la polaridad en corriente alterna.

En corriente alterna hablamos de línea y neutro no de positivo y negativo.

¿Qué hace la placa una vez que recibe los 220 voltios de corriente alterna 120 amper?
La placa de la unidad exterior lo que primero hace es rectificarla (convertirla a corriente continua).

Con un componentes que se llama diodo nosotros podemos rectificarla y pasar el medio ciclo negativo arriba.

Una vez que nosotros corregimos la corriente continua, no vamos a tener frecuencia porque no se va a invertir la polaridad.

Estos 4 componentes negros son los diodos y es el puente rectificador.

El diodo tiene un cátodo y un ánodo.

De un lado van a ver que el componente es así y el componente tiene una rallita.

Ese componente tiene la particularidad de que deja pasar la corriente en una sola dirección.

Los electrones circulan del negativo al positivo. En el testar escala de diodo, van a medir más o menos 0,6 0,8 voltios. 

Cuando la corriente eléctrica se invierte el medio ciclo pasará arriba. Y ahí tendré la rectificación de la onda.

Si pongo 4 diodos tendré una rectificación de onda completa.

##### Es uno de los componentes que más fallas tiene en la placa: 50% son problemas en los diodos.
Porque son componentes que trabajan a mucha frecuencia.

Para medir diodos: Ponemos el tester en la escala de diodo, para un lado tiene que marcar y para el otro lado no. Se mide con la placa desenchufada, se puede trabajar con la placa enchufada tenés que poner en corriente continua porque si ponés en diodo es continuidad y chau tu tester. Y acordarse descargar capacitor.

Si cualquiera de los diodos se me pone en corto. 

El puente rectificador está compuesto por 4 diodos.

**Esta es una placa de un equipo más nueva, se llama de doble faz tiene componentes de ambos lados.** La placa tiene uniones.

Alumno: El diodo este me marcó de un lado y del otro, así que este diodo está mal.
Profesor: Lo que pasa es que cuando medís en la placa estás midiendo otra cosa. Lo recomendable es extraer el diodo. Medirlo desde la placa es cuando tenés más años de experiencia. **Lo ideal es sacar el componente y medirlo afuera.**

El componente que yo les mostré acá es este que es de montaje superficial, y van a ver que tiene el símbolo de la corriente alterna y del otro lado tiene positivo y negativo bien marcado, ese es uno de los dos.

Hay varios aspectos de los componentes, van a encontrar otros.

El puente rectificador puede ser de otra forma en la placa de la unidad exterior, tiene 4 patas.

Acá tenemos 220 voltios de corriente alterna, pasará por 2 patas del puente rectificador y del otro lado tiene positivo y negativo y eso se pasa por lo siguiente.

Cuando los electrones vienen por este lado, el electrón se encontrará con un diodo que está polarizado de forma inversa. **Los electrones circulan del negativo al positivo.** Entonces tomará otro camino, pasará por la carga volverá por el otro lado y llegará a este punto.

Como el electrón en este punto y en este punto tienen la misma diferencia de potencial. Entonces él va a tomar acá y volverá a la fuente de alimentación o a la red. Cuando se inverta la polaridad.

El negativo se encontrará con un diodo que está en inversa, entonces el camino que seguirá será por arriba pasará por la carga y al llegar a este punto va a encontrarse con este diodo que está polarizado inversa, pero como esta diferencia de potencia es mayor será atraído por esto y volverá por el mismo camino.

Y así es como el puente rectificador rectifica la onda... Bloquea el negativo de la onda y lo manda arriba.

Una vez que lo tenemos rectificado los 220 voltios... Acá la tensión es 0.

Acá la tensión tenemos un pico de la onda, pero acá tenemos más espacio un vacío (la separación de las ondas), en donde la tensión va a tender a caer acá, **para que esto no suceda está el famoso capacitor que está al lado.** ... Esta placa confunde un poco porque hay que darla vuelta, acá tenemos el puente rectificador y enseguida vamos a tener el capacitor, el capacitor es de 450 voltios, 10 mf.

Los microfaradios(mf) es la capacidad que tiene de almacenar energía, cuando él se carga en este punto, cuando la fuente comienza a caer **el capacitor se banca la tensión mantiene hasta que él puede otra vez cargarse**. El resultado de eso será una corriente continua, entonces ahí recién voy a tener corriente continua.

De un lado voy a tener corriente alterna 220 voltios, del otro lado del rectificador voy a tener 310 voltios, por eso el capacitor es de 450 voltios.

Una vez que nosotros tenemos rectificado y filtrado la corriente eléctrica: el tester no mide el pico de la onda porque es corriente alterna, el mide un 70% me hace un promedio, pero cuando nosotros rectificamos lo hacemos en el pico de la onda.

Y acá nosotros ya no tenemos 220 voltios, porque rectificamos el pico de la onda.

##### Hay una fórmula: voltaje por raíz de 2 y eso me dará 311 voltios.

###### Cuando pasamos de corriente alterna a continua no tenemos 220 tenemos 311 voltios.

Por eso el capacitor es de 450 porque no se bancará... Y acá nosotros NO TENEMOS FRECUENCIA.

Hay placas con transformador lineal y otras con switching o conmutada.

Una vez que nosotros rectificamos a esta tensión a esta corriente. Nosotros vamos a tener un componente que sería este que tiene 7 patitas **ese integrado se llama conmutador**. Ahora nos estamos refiriendo fuente **conmutada** que es la fuente de alimentación de la placa de los inverters.

Una vez que nosotros tenemos rectificado los 311 voltios y pasado por el capacitor para que nos haga los más parejo posible, **esa tensión se la aplica al conmutador o switching o integrado**, tiene varios nombres.

**El conmutador convierte esta corriente continua que teníamos acá de 311 voltios la vuelve a transformar en una corriente alterna, pero la vuelve a transformar de tipo cuadrada, ya no es más una onda sinusoidal como teníamos al principio**.

Fijense la transformación que hubo de los pines de entrada de los 220 pasando por el rectificador el capacitor aplicado al conmutador, como nosotros transformamos la corriente de 220 a 50 hertz a una corriente del tipo cuadrada.

Vamos a manejar una frecuencia entre 90 y 150 kilohertz. Vamos a tener entre 90 mil y 150 mil hertz.

Con esa frecuencia vamos a variar la velocidad del compresor.

Manejando la velocidad del compresor podemos manejar las presiones, la temperatura del ambiente, hacer que el compresor no corte.


**La tecnología inverter es el manejo de la frecuencia** y esto lo hace el MODULO IPM.

Acá tengo un diodo que es el de más potencia de por lo menos de 3 amper, también se usa como rectificador. Estos diodos rectificadores no son tan de alta recuperación o tan rápidos.


Son de rápida recuperación porque la frecuencia que manejan no es la misma. 

Los diodos de alta recuperación se llaman diodos shocking.

#### Otros componentes
Resistencias, optoacopladores.

##### La única diferencia que tiene una placa de AC común de la inverter es que las placas que son full inverter tienen un IPM que es el que maneja el FAN de la unidad interior. 

Cambia un poco el diseño pero los demás componentes son iguales. 

La placa electrónica de los AC son un mando que reciben una señal que le da el usuario la decodifica a través de los integrados y la envía a los periféricos.

Y esto lo hace a través de componentes electrónicos.

El 90% de la placa lo van a poder arreglar, salvo que sea el integrado, pero para que se queme el integrado ustedes tienen que hacer la cagada, tiene muchas protección.

No tiene forma de que haya una baja tensión, porque el integrado trabaja con 5 voltios. Tiene diodo zener y regulador de voltaje y no le puede pasar más de 5 voltios.

Tenemos 2 partes en la placa, está bien dividida entre alta tensión, ahí manejaremos la entrada de corriente alterna, el filtrado, el motocompresor.

Y la otra parte es la parte lógica de la placa maneja los integrados, el buzzer, el display son periféricos que no necesitan alta tensión.

Si de este lado de la placa está unida a través de un optoacoplador.

#### El optoacoplador es un integrado que de un lado tiene un diodo y del otro lado tiene un fototransistor. Del diodo tiene un puntito. El diodo es led un emisor de luz.

Con el optoacoplador puedo manejar de un lado tensiones altas y del otro lado tensiones bajas, para que el circuito esté unido.

Cuando yo le aplique del lado del diodo siempre va a estar el microprocesador. Del lado del fototransistor estará la parte de potencia, puedo manejar mucha potencia con una señal baja.

Cuando el diodo es focalizado en forma directa se va a iluminar, cuando ilumina el fototransistor cuando recibe luz conduce y ahí cerrará el circuito y hará que circule.

#### Es como una especie de relay. Cuando lo desenergizas el relay se despega, y cuando lo energizás se pega, es una especie de relay electrónico.

Cuando hago que el diodo ilumine el fototransistor conduce cierra el circuito y cuando se apaga el diodo el circuito se abre y hay una aislación galvánica.

Si del lado en donde hay potencia explota algo, del lado del microprocesador no pasa nada.

#### El optoacoplador aisla y se banca hasta 5000 voltios.

Es raro que un microprocesador explote salvo que en vez de poner línea y neutro pusiste neutro y línea.

Alumno muestra una foto de una placa lineal.

Profesor: Este capacitor es de 25 voltios porque trabaja con lineal, tiene un transformador afuera. Y en la fuente switching tenés un capacitor de 400 voltios en el otro es de 25.


### ¿Cómo te das cuenta si es una placa switching o lineal?
La lineal primero baja la tensión y luego rectifica, no trabaja con 220 sino con 12v. La conmutada rectifica luego pasa por el capacitor y luego al conmutador.

#### Los integrados son difíciles de conseguir

A un alumno le cobraron 130 mil el año pasado por reparar una placa y aún así no sirvió el arreglo, desinstaló el aire.

Si observan en la placa van a ver la importancia de conectar bien el AC.

La placa de un AC es un mando que recibe la señal decodifica para que haga lo que el cliente le pida.


Tenemos que analizar que parte de la placa no funciona...

**Si la placa se te apagó y el equipo no prende hay que revisar la entrada de alimentación, por qué esa placa no está recibiendo alimentación, voy a ver el neutro y la línea.**

Si analizamos esta placa veremos que tenemos lo mismo: acá tenemos los pines de la entrada del neutro, luego en el final del relay entrada de línea y luego el que va al compresor. En este caso alimenta a este terminal que sería el transformador pasa por 220 voltios por el transformador y lo vuelve a aplicar a la placa en 12 voltios.

El transformador reduce la tensión.

El transformador está compuesto por 2 bobinas, uno es el primario y el otro secundario sobre un núcleo de ferrita. En el primario vamos a encontrar, podemos medir de 2 formas el transformador la primera nosotros conectamos el tester en la escala de ohm y medimos la resistencia 

Hora 01:06

Podemos medir de 2 formas el transformador la primera vamos a poner el tester en la escala de OHM y medimos la resistencia porque es un comienzo de una bobina que está enrollado en un núcleo de ferrita, esto me dará un valor en OHM alto.

500 OHM aproximadamente, del otro lado me dará 50.

El arollamiento en el primario es mayor y el alambre que se ocupa en el primario es más fino, secundario es más grueso y menos vueltas.

Si está cortado el transformador marcará abierto.

**Normalmente se quema la parte del primario porque trabaja con más tensión y es más finito.**

**Algunos transformadores que vienen en los ventiladores en la bobina tienen un protector térmico, un fusible.**

Ese protector térmico tiene 110 grados de temperatura, cuando llega a esa temperatura se corta y abre el circuito.

Reemplazando este protector térmico o poniendo un cablecito solucionaste el problema, está sobre la bobina apenas sacamos la tapa.

Te va a marcar OL (no mide nada).

Ahí la placa no te encenderá.

**Entre línea y neutro te marca 220v pero acá no tenés tensión entonces el problema es el transformador.**

Cada placa tiene su tensión diferente, pero el 90% es de 12v.

La placa trabaja con tensiones mixtas porque trabaja con 220v trabaja con 12 voltios en la parte de baja. Y trabaja con 5 voltios en la parte lógica.

Donde recibe la tensión de 12 voltios tenemos este integrado, transistor regulador de tensión recibe los 20 voltios y en la otra pata de la salida sale 5 voltios. Acá hay una caída de 7 voltios sí o sí por más que aumente o baje la tensión te va a entregar 5 voltios.


**Es casi imposible de quemar el integrado, solo tenes que conectar mal fase y neutro ¬¬(-.-)**

Después de la entrada de la alimentación tenemos acá el puente rectificador se puede hacer con 4 diodos se puede poner un puente.

Luego tenemos algunas resistencias que tenemos que medir, reguladores de voltaje, la memoria muy difícil que se dañe la memoria. La sonda maneja la temperatura del ambiente y del refrigerante, luego conexión del swing y tenemos el RPM que maneja el motor de la unidad exterior que sería el efecto Hall.

El efecto hall mide que velocidad que gira el ventilador y si está acorde con la velocidad que ha sido seleccionada, si pusiste rápido y gira lento salta el error y corta.

Las dos placas mandan, entre ambas hay una comunicación constante por eso se usa el cable de señal.

Hora 01:15

Si tenemos solo un diodo tenemos un rectificador de media onda y queda un espacio vacío. Esto se llama corriente punsante, nosotros en inverter al tener una frecuencia tan alta no necesitamos un puente rectificador, el diodo shoking se conecta a solo diodo porque es tan alta la frecuencia tantas veces que completa.

Por eso ustedes se van a encontrar con un solo diodo, son diodos de rápida recuperación, no hace falta poner 4 diodos.

Tiene como una pinza amperométrica y por ahí pasa el cable que va al compresor eso es para tomar el amperage.

Si el compresor me está consumiendo más porque el capacitor se desvalorizó entonces va a apagar la placa.

Muchos técnicos sacan eso.

Otro componente que suele fallar: TRIAC es como un transistor.

El TRIAC le da la velocidad al FAN. Es un transistor de corriente alterna, el puede manejar de 2 formas la velocidad de la unidad interior.

Es como una llave supongamos que yo le doy la orden para que me pongan la velocidad mínima, lo que hará el TRIAC es entregar una parte de la onda. El me va a conectar el FAN cuando llegue a este punto el se va a apagar, la onda recorrerá todo y cuando llegue acá se volverá a encender...

Y así me dará una velocidad baja.

Ahí estará más tiempo conectado y apagará con eso logro que el ventilador gire más rápido.

Me imagino que me dará toda la vuelta, estará al máximo, es la velocidad máximo del motor, cuando se daña el TRIAC: apagás el compresor y el forzador sigue andando.

Cuando se daña el TRIAC: apagás el compresor y el forzador sigue andando o prendes pero no prende el forzador, tenes que revisar motor capacitor si no encontras defectos entonces es el TRIAC.

Microfaradios: capacidad de almacenar energía, es como una pila.

Capacitor corrige factor de potencia.

##### **Factor de potencia** en la parte de la limpieza, pero en nuestro caso ....

Cuando conectamos una bobina ya sea un motor, un transformador lo que pasa con la corriente eléctrica es que nosotros tenemos la corriente electrónica cuando conectamos una bobinas se produce un adelantamiento de la corriente con respecto de la tensión.

Corriente cantidad de electrones. Se mide en amper.

Tensión fuerza de los electrones.

Cuando conectamos una bobina ya sea un motor, un transformador lo que pasa con la corriente eléctrica es que nosotros tenemos la corriente electrónica cuando conectamos una bobinas se produce un adelantamiento de la corriente con respecto de la tensión. Se produce un adelantamiento y un desfasage, la corriente adelante y la tensión atrás. Los capacitores atrasan a la corriente con respecto a la tensión.

##### En los aserraderos, secaderos la cooperativa le exige que tengan un banco de capacitores para compenzar el factor de potencia.


La bobina adelante la corriente, el capacitor atrasa.

Eso se llama coseno del ángulo PI tiene que ser lo más cercano a 1: 0,95.

Si le ponés un capacitor muy grande vas a invertir otra vez, hay que respetar el valor de los capacitores.

Alumno: Hay alguna manera de saber que capacitor colocar?

Profesor: Mirando la tablita.

**A través de la potencia del motocompresor podés sacar que capacitor lleva.**


Filtros pasa bajos, sirve para filtrar el ruido.

**Alumno: se acuerda de esos estabilizadores de chapa.**

Esta es la válvula inversora y este es el forzador, acá tenemos los relay que manejan a la válvula y al forzador. Si miran la placa de este lado está conectado al microprocesador que es el que energizará a las bobinas de los relay cuando le damos la orden el microprocesador entiende que tiene que prender la válvula inversora entonces le manda los 12 voltios a la bobina se conectará y por este cable irá la alimentación a la bobina, neutro ya lo tenemos.

Lo mismo que en el inverter.

Cuando el control remoto no les funciona no le responde, hay que desarmar el display y nos encontraremos con el receptor infrarojo tiene 3 patas y es lo mismo que el sensor RPM. Tiene una pata de alimentación positivo negativo y otro de señal, puede estar invertido positivo negativo, señal. Eso suele dañarse, sacan la tapita vamos a encontrar el sensor.

Esto se prueba así: poné tu tester el da señal al control remoto nos tiene que marcar 5 voltios, negativo, señal y no marcará nada. Le damos la orden desde el control remoto el tester le va a causar 1 pulso.

Primero hay que medir que hayan los 5 voltios (enchufado)   
Luego cambiamos ponemos negativo y señal entonces ahí le das el pulso y ahí te da...

Rango 20 volt.

Si no te da pulso entonces sustituí.

Tenemos que buscar el positivo y negativo. El negativo irá por todo lo ancho de la placa. El positivo vendrá directamente al regulador, acá entrarán 12 voltios y acá 5.

El cable de señal irá al microprocesador en el display porque ahí vendrá el pulso de la señal.


Si no te da los 5 voltios tenés que buscar la alimentación.

Si te da 5 voltios y no te da señal


Si acá en este punto el tester no te marca nada quiere decir que la señal no funciona.

Si vos querés apagar el equipo el recibirá una serie de pulso en una frecuencia y ahí el procesador decodificará para que el relay se apague.

Ni me digas que me hicieron ir como 8 kilómetros por la pila del control.

Alumno: con qué tipo de soldador se trabaja? 
Profesor: Soldador de punta cerámica de 40 vatios hasta que se acostumbren y que compren 60% estaño, no de paraguay.

Profesor: Y si está muy sulfatado le limpio con un cepillo de dientes yo le pongo Tiner, el alcohol isopropílico no lo uso porque es caro. 

Si la placa para sacar la humedad que se mojó sumergilo en un tacho con un cepillo de dientes.

El alcohol isopropílico es caro al pedo XD.

Hora 01:50

Alumno: El tiner no le disuelve el esmalte que trae.
Profesor: En parte sí pero vos necesitás limpiar porque no podés soldar no te saldrá la soldadura.

Tenés que limpiar porque viene con un baño la placa.

## Como instalar bien un inverter.

#### Lo más importante en el inverter es tener cuidado en la instalación.
Nosotros ya hablamos de la alta frecuencia que manejamos en un equipo inverter.

Lo que tenemos que hacer es respetar algo, en el inverter se van a encontrar con la bornera que tiene línea, neutro, señal, tierra. 

Si no el equipo no le trajo el cable tenés que comprar 2 cables bipolar tipo taller de 2x1 y medio o de 2x2,5 de acuerdo a la potencia del equipo.

Lo primero que tienen que hacer es conectar unos terminales con terminales, **NO METAN LOS CABLES SIN EL TERMINAL, porque se forma un sulfato como un polvo verde en el cable de señal les va a meter un error**.

Dirección: José Ingeniero 229, Oberá.

Se forma una pequeña resistencia y les meterá un error, COMPRAR TERMINALES.

#### Como 2da medida: conectar este paquete de cables línea y neutro aparte del cable del señal y tierra, dos paquetes.

De los caños que van a aislar pasen línea y neutro por arriba y el cable de señal y tierra separado del caño no junto.

Con eso se ahorran de que la alta frecuencia que habrá en el cable de señal entre el cable de señal entre la comunicación del equipo de afuera y de adentro, el campo magnético que genera el consumo de línea y neutro no le afecte, sino les marcará error.

Hora 01:59

Resulta que vos te vas y dan un paquete de 5 cables porque compran 5 por 1 y medio y conectan 4.

#### Así sin terminar funciona... Empezó a marcar un error lo primero que tenés que observar es que está mal instalado, no importa si lo instaló Siri...

El paquete de cables NO lo podés poner junto porque la alta frecuencia 90 mil a 150 mil hertz el campo magnético que genera la línea y neutro por inducción se mete en el cable de señal y me va a afectar la señal... Entonces uno me tirará error de comunicación se me va a apagar el equipo.

Cualquier cosa que esté mal vas a quedar loco.

Alumno: Si está conectado todo junto y le salta error al cliente voy desarmo todo y lo vuelvo a armar.    
Profesor: directamente anulá acá poné un cable para afuera, el de señal un cable solo el otro dejalo no pasa nada.

### El de señal debe estar separado del resto y se aprovecha porque es 2 y 2 entonces señal y neutro y tierra.
### Y la puesta a tierra es importante.

Alumno: Pero eso falla en el momento o tarda?     
Profesor: No, depende del equipo. A veces pasan meses a veces años.

La tierra va a drenar las corrientes parásitas que hay en el equipo.

Cuando te marca señal, error de comunicación, tenés que ir a la bornera de la unidad exterior.

#### En el neutro y señal. 

Vas con tu tester poné en corriente continua poné el negativo y el positivo acá, prendés el equipo tiene que variar entre 5 y 15 voltios si no varía quiere decir que tendrá un problema de señal.

Vos ponés tu tester en los equipos grandes te dará entre 25 y 50 voltios.

Si ahí vos tenés señal, te vas a la unidad interior y hacés lo mismo, si no te sale señal no te marca nada, es porque tu problema está en la unidad interior.

Siempre hay que separar.

Ahí podés ver como detectar el problema, TIENE QUE HABER VARIACIÓN PORQUE LA SEÑAL VA Y VIENE.

##### Este equipo vino con un cable que tiene una aislación para manejar la alta frecuencia.

Es el cable que viene con el equipo en el caso de que ustedes tengan que ir a comprar el cable. Ven que este cable es de goma. Es como medio cromado. Hay que poner terminales si o si.

Consulta alumno: El apagaba todo cierra la unidad interior pero la exterior no apagaba. Resulta que fue un técnico.
El técnico le dijo que tenía que cambiar la placa. YO fui y le puse placa universal.

Profesor: Ahí tendrías que revisar la conexión. Tratá de guiarte por la placa no por el diagrama.

Puede que sea tu relay.

Entonces está mal conectado...

Yo no le dí la órden, prendí y encendió el motocompresor..


Profesor: Tenés que apagarlo con el control remoto y volver a prenderlo. A veces pasa que cuando está desconectado el equipo. Habría que revisar el relay pero me parece que te apuraste, sin desenchufar puede ser que haya quedado en la memoria los datos.


Hora 02:17

### Con respecto al compresor de los aires inverter, lo único que podemos hacer es medir las bobinas, las 3 bobinas nos tienen que marcar un valor igual o muy parecido.

Entre U,V,W tienen que ser iguales o muy parecidos, si nos da variada es porque el motor no está funcionando.

Hay que prestar mucha atención en las pestañas del equipo, hay que hacerla bien para que no perdamos el líquido refrigerante.

Es difícil volver a cargar hay que poner el motor a pleno para que nos dé la presión para volver a cargar...

Alumno: cuál es la presión correcta?   
Profesor: depende de la temperatura del ambiente, entre 118 y 310 (ruido Hora 02:19)

En un equipo inverter al variar la velocidad no podemos saber que presión tenemos porque varia la presión al variar velocidad.

A medida que empiece a enfriar baja la velocidad y baja la presión


Nosotros vamos a medir en el manómetro cuando arrancó 128 PSI, vamos a medir 125 PSI, 130 hasta 160 PSI.

Capaz que cuando medimos a pleno el motor cuando recién arrancó nos marca 90 PSI.
Hay que darle un tiempo para que el trabaje y que quede estable.

Lo ideal ahí es si nosotros perdemos el 30%-60% del refrigerante 410 tenés que tirar todo, no podemos volver a cargar.

Si nosotros perdemos cierta cantidad de refrigerante lo ideal es vaciar todo el equipo y cargar por peso.

### Refrigerante 410 1,36 kilo 
Entonces agarrá una garrafita poné en una balance cargá el refrigerante hacé el vacío y cargan por peso entonces cargando por ese peso te asegurás que el equipo está en el punto exacto.

Cargando por peso te vas a asegurar de que el equipo está en el punto exacto de la carga de refrigerante.

Si vos querés cargar a ojo corrés mucho riesgo de equivocarte. La variación de la temperatura ambiente te va a molestar un poquito y hay una deuda que se llama la deuda del 30.

Supongamos que estamos a 25 grados a esos 25 grados le sumamos 30. 30 es una constante como PI. A ese resultado 55 lo multiplicamos por 2 entonces ahí me dará 110 PSI.

A 25 grados de temperatura la presión ideal es 110 PSI.

Cuando tenemos 20 grados la presión pasará a ser 100 PSI.


#### Eso es para R-410 y para R-22 es la temperatura ambiente más 30.

O sea que la presión a 25 grados la presión tiene que ser 55 PSI.

Hora 02:24

Con eso nos vamos a asegurar de hacer una carga correcta en el equipo y para poder ponerlo a pleno lo que tenemos que hacer es tener un secretario para que **tenga en la mano el sensor de ambiente** entonces ahí vamos a engañar el equipo pensará que está en 36/37 grados, y va a funcionar a pleno y ahí podemos hacer la carga siempre respetando las presiones.

Si llegamos a perder hay que hacer por peso sino el equipo no rendirá.

Alumno: Se puede cargar apagado?   
Profesor: Sí es mejor cargar apagado, le cargás el peso lo dejás un rato y lo prendes.  
Alumno: Hay que tapar la válvula.....
Alumno2: Le hacés un vacío y entra el kilo necesario.   
Profesor: Siempre tenés que hacerle un buen vacío.

Hora 02:26

Lo mismo que cuando medimos la bobina del compresor del inverter tambien pueden medir la bobina del forzador y también la bobina del fan, pero en el caso de que sea full inverter va a tener los 3 motores con tecnología inverter.

El resto del equipo es igual, pero en la placa que conecta a mayor frecuencia al ir variando la velocidad aumentará la presión.

Se siente cuando arranca y apaga el convencional.

No podemos probar la única manera de probar es con la placa, el modulo IPM es el que le dará el diferente uso a las diferentes bobinas.

Hora 02:29

Le da el pico corta, se invierte le da el pico corta.

##### Vamos a desarmarlo

Hora 02:37:40

Varistor está ubicado entre línea y neutro.

La función que tiene el varistor: si tenemos una alta tensión ponele que sea un varistor de 250, si la tensión pasa los 250 se pone en corto, es un cortocircuito controlado entonces al producir un corto se me corta el fusible.

Entonces voy a revisar el fusible y el varistor, si se puso en corto y cambias el fusible volverá a producir el corto, tenés que sacar.

Si no lo conseguís podés dejar sin el varistor y con un fusible y funcionará pero sin protección.

Hay que fijarse como quemó el fusible... Si el fusible explotó rompió el vidrio o adentro, es porque hay un corto circuito puede ser que **el diodo está en corto**.

#### Fusible se fundirá de 2 formas diferentes:
1. Cortocircuito
2. Exceso de consumo

Si tengo más consumo de lo que el fusible está diseñado se me va a cortar. Normalmente las placas usan 3,1 3,15.

Hay que respetar eso, no podés poner un fusible de 4 o de 5 amper, si tu placa te dice que es de 3,15.

Varistor, puente rectificador, diodos, capacitor, conmutador tiene patitas linea y neutro, positivo y negativo ahí tienen que medir 310 volitos en las patas del conmutador (integrado de 7 patas), 

Si en el conmutador tenemos los 310 voltios y la fuente no te arranca entonces todo esto que es de la parte de entrada todo venía bien y el conmutador está fallando porque se abrío adentro tuvo algún problema. Falló este componente y no me está dando los puntos para manejar el transformador.

Hora 02:44


#### Viene por el fusible, varistor, pasamos por los diodos, y llegamos al conmutador si recibe acá y no te enciende la placa tu problema está afuera... Igual siempre es conveniente medir los componentes periféricos que están alrededor por si hay alguna resistencia diodo algo que está mal. Pero como trabaja a una trabaja tan alta se corta y se abre.


02:45

Hay que aprender el concepto.

Hay millones de diseños de placas: hay que dividir etapa de potencia, esta es (sensores) y van a ver como funciona.

#### Para medir las sondas NTC.

Los sensores de temperatura son sondas NTC (coeficiente de temperatura negativa)

Cuando la temperatura aumenta la resistencia disminuye.

Después tenemos los PTC que son los que tienen los motores de heladera en el freezer, ya no vienen con relay vienen con PTC.

Son coeficiente de temperatura positiva cuando aumenta la temperatura la resistencia aumenta.

La sonda NTC las tenemos en los aires.

Al aumentar la temperatura en el ambiente el sensor está bajando su resistencia hasta que llega a un punto que deja pasar la tensión y el microprocesador enciende el motocompresor cuando la temperatura del ambiente comienza a bajar, la resistencia comienza a subir hasta que no deja pasar más la corriente y el procesador apaga el equipo, así maneja el sensor de ambiente.

Para medir el sensor de ambiente lo que podemos hacer es agarrar un vaso con agua con hielo ponerlo adentro dejarlo con un termómetro van a ver la temperatura que marcará el termómetro en el agua y ahí hagan medición en escala de OHM y hay una tabla de valores a tantos grados de temperatura tiene que medir tantos grados de 10k 15k 5k y ustedes verán si el sensor está bien.

Ponés un poco de hielo, ponés el sensor lo dejás con el termómetro, cuando te marcó 25, 8 grados medís y comparás.

### Medición en placa
En los pines en donde va enchufado el sensor tenemos que medir 5 voltios. Como es una resistencia los 5 voltios vienen por acá van por acá se dividen y van a neutro.

Como esto es una resistencia estos 5 voltios tienen que tener una caída de tensión, y acá a mi me tiene que medir entre 2,5 y 2,9 con el sensor enchufado en la placa, tocamos el tester y tiene que tomar esta medición, retiran el sensor y le tiene que marcar 5 voltios porque ahí no hay resistencia si medimos solo los pines (sacando el sensor), con el sensor colocado la resistencia se divide en dos.

#### Otra cosa: Siempre respeten la línea y el neutro.
Si miran la placa tenemos línea al fusible y sigue la línea y ahí va por los componentes, el neutro lo que hace es recorrer toda la placa: microprocesador, etc. 

#### Cuando nosotros conectamos invertido se nos produce un cortocircuito y quema toda la placa porque la línea irá por el neutro.

A veces los electricistas conectan al revés la fase y el neutro.

#### Como sacar la línea y neutro.
Lo que tenés que hacer es poner tu tester escala corriente alterna y ahí ponés la punta roja acá y la punta negra acá , de un lado no te marcará nada, si te marca sabés que ahí está la línea y allá el neutro.

O con un buscapolo.

#### Esta placa solo me manejará la unidad exterior, manejará el equipo de afuera.
Hora 3 
Estas dos placas estarán comunicadas a través del cable de señal. Esto
Esto es un filtro le saca le elimina la alta frecuencia al circuito. 
Si ven esta placa, tenemos línea y neutro y señal y tierra.

Vamos a dar vuelta la placa y veremos que la línea viene directamente a uno de los pines del fusible (la primer protección). Del fusible pasará a una bobina toroidal con un capacitor. La bobina está conectada en serie con el capacitor el capacitor está conectado en paralelo y esto es un filtro doble filtro o filtro pasabajos, que sirve para filtrar la alta frecuencia. Después en este caso tiene protector gaseoso (Hora 03:02) que es para las altas tensiones por si le cae un rayo.

Acá tenemos el varistor que está entre la línea y neutro para producir el cortocircuito controlado para que el fusible se prenda. Hay 2 varistores.

Cuando miren la placa de la parte de atrás de la soldadura. Tenemos que tomar en cuenta que no estén rajadas con el tiempo la temperatura esto suele calentar entonces el estaño se funde y no hace buen contacto los componentes con una simple resoldada podemos solucionar un problema, en realidad era un problema de falso contacto sobre todo en la parte de potencia.


Si seguimos el circuito en la placa nos vamos a encontrar con el PTC (creo que se equivocó en realidad quiso decir NTC) aumenta la temperatura disminuye resistencia.

#### Esta bobina toroidal es el corrector del factor de potencia así como en la industria tiene mucha bobina mucha carga reactiva nosotros acá tenemos mucha carga capacitiva, entonces en vez de agregar capacitor tenemos que agregar bobinas.

##### La bobina adelanta. El capacitor atrasa.

Ahí tenemos el relay, y pasa por diferentes componentes acá tenemos el conmutador porque es una fuente conmutada, el conmutador maneja a este transformador que es de alta frecuencia y con ese transformador chico tenemos una frecuencia alta.

Luego del otro lado redujo la tensión, tenemos los capacitores diodos que rectifican, tenemos tensiones bajas 12 voltios.

Fijense ahí que están los diodos que son de alta recuperación los negritos (3 diodos).

Luego tenemos el módulo IPM que en este caso tiene el forzador de la unidad exterior también inverter no es de corriente alterna, por eso es manejado por este módulo IPM, tiene la particularidad de manejar al forzador U,V,W. No nos podemos equivocar.


El módulo IPM le dará uso a las diferentes bobinas: U,V,W.

Acá tenemos la válvula inversora.

Una vez que el relay se conecta, la fuente de alimentación cuando energizamos el equipo ella me alimentará toda la parte lógica y cuando le doy la orden de encendido, el microprocesador me va a alimentar el relay y ahí me dará la tensión de 220 en esta parte.

Miren acá el circuito esto es el rectificador de onda completa, acá entrará corriente alterna y saldrá positivo y negativo.

De ahí tendremos el diodo y el transistor que corrige el factor de potencia, porque en la industria el corrector de factor de potencia es del modo estático como este varía la velocidad del motor entonces el constantemente tiene que estar corrigiendo el factor de potencia, el transistor junto con el integrado va tomando la señal y va tomando el consumo y van corrigiendo el factor de potencia.

Luego tenemos el módulo IPM que recibe la señal de 310 voltios y ahí me dará U,V y W para que yo le encienda y funcione.


### Y esa sería la estructura de la placa de la unidad exterior.

Lo mismo vamos a encontrar en la unidad interior:
Si no te enciende la placa de afuera, hay que ver afuera.

Acá no hay maestro esclavo, son independientes las placas.

Alumno: En este caso lleva 1 sola placa este equipo?  
Profesor: Este lleva una acá (unidad exterior) y otra acá (interior).  
  
Alumno: Yo entendí que llevaban 2 placas acá y una acá.      
Profesor: Nonono.

Alumno: pero tiene que haber un proceso en el cual, vos venís con el control le pongo esta le manda señal a la placa y cuando se entera que prendió ahí actúa.   
Profesor: Por supuesto que sí por eso les digo que están conectadas a través del cable de señal, si vos querés conectar esta placa y la ponés sólo va a encender con 220. A los segundos de no funcionar al no tener la señal te tirará un error.

El armó la placa de la unidad interior armó en la mesa todo junto, hizo las 3. 

Profesor: La tercer placa que usted me dice es solo el banco de capacitores.

Mostró una placa universal para este y luego una placa para el común.

Profesor: Con esa placa que anda por ahí solo funciona el compresor porque no tenemos el módulo IPM acá.

Alumno: Lo que cambia en un inverter es que la alimentación a la red está en el equipo de afuera.   
Profesor: No. Depende la frigoría es igual que el otro.

Alumno: Este es el cable de intercomunicación pero es porque este es un equipo grande, los chicos son exactamente iguales.

Alumno2: Ah esta alimentación se conecta acá.    
Profesor: Este si porque es un equipo grande 6000 frigorías, sino se conecta igual que el otro.

Alumno3: Sería L1,N1,S, y luego vuelve a repetir.

Alumno4: Como llevas ese cable tenés que llevarlo todo empaquetado hacia adentro para conectar a la línea?   
Alumno5: Claro, yo decía que estaba pantallado el cable.

Profesor: Este si porque es sólo línea y este es el cable que vas a traer la línea neutro y la señal y tierra.


Alumno5: Y como lo enchufás al toma?

Profesor: Tenés que tener un toma para ese afuera o podes pasar para adentro. Y cuando ustedes revisen el cable de señal y no tenga la señal de intercomunicación tenemos que medir los optoacopladores eso son los encargados de pasar señal de un equipo al otro.

#### Medir optoacoplador: De un lado te mide como un diodo como un fototransistor. El punto marca de que lado está el diodo.
Cuando hay un problema de señal siempre tira el error.

Ese punto te va a marcar que desde ese lado está el diodo en el optoacoplador.

Medí las dos patas hay que tocar las dos puntas del tester para asegurarse de que está funcionando. Ahora invertí y le tiene que marcar como si fuera un diodo, no está tomando porque no le está sacando el barniz. 

Del otro lado te va a marcar 0(infinito) PIIII, un cortocircuito.

Profesor: Ya mediste uno y te dió 1,047.

Alumno: Ya te da la señal sonora y listo  

Profesor: No. Viste que yo te dije que era 0,8 en un diodo pero como es un diodo led es un poco más alto el voltaje 1 y algo... Ya te marcó para un lado ese voltaje y par el otro lado te vuelve a marcar... Si está mal te va a marcar un cortocircuito el varistor y si está abierto no marcará nada.

Alumno: Claro pero cuando uno va a la casa del cliente no se puede sacar, agarrá y cambiá la plaqueta chiste XD

##### Otros errores que pueden surgir y se pueden medir: el módulo IPM.

Hora 03:22

Otro de los errores que puede surgir es que corte el motocompresor por temperatura pasta térmica.

### El módulo IPM es un módulo inteligente de potencia.
Lo que tiene el IPM son 6 transistores IGBT que manejan a las bobinas del motor, desde el módulo del IPM podemos medir los 310 voltios entre positivo y negativo. Los 310 voltios que sería la entrada y nos queda una tensión de 15 voltios que estará también en el módulo que va a excitar a los transistores para que vaya dándole señal a las diferentes bobinas, el procesador le va a ir mostrando a qué bobina tiene que energizar.

Eso es un módulo ese es el IPM.


##### El va a ir dando diferentes pulsos a diferentes bobinas para que el motor funcione y también va a ir variando la frecuencia más o menos ancho de pulso para que el motor baje o aumente la velocidad esa parte del circuito se llama PWN (modulación por ancho de pulso) también está puesta acá.

##### Cuando la unidad interior le pide a través del cable de señal más potencia porque hace más temperatura el circuito PWN le va dando más frecuencia.

Hora 03:27

Entonces nosotros acá tenemos los IGBT los transistores esto está todo encapsulado podemos medir los 310 voltios y podemos medir los 15 voltios que esté presente para que energize a los transistores si esas tensiones no están no funcionará el compresor o se les va a cortar, esa tensión ustedes pueden medirla con el equipo funcionando negativo y buscar la tensión, si están esas tensiones y no funciona entonces es problema del IPM.

Hora 03:29

Eso son transistores y ese es un diodo 

Lo que podemos medir con la pinza entre el positivo y negativo podemos medir los diodos que están ahí para un lado y para el otro. Si un diodo de estos está mal el IPM chau..

Yo no cambié ningún IPM todavía.

Entra acá la línea pasa por este transistor acá el cruza los 15 voltios y hace circuilar la corriente sale por la U pasa por la bobina cierra en V, baja por este otro IGBT y cierra el circuito.

Y así le va combinando el va por acá pasa por acá sale por la bobina pasa por la bobina cierra en V y vuelve acá y cierra.

Por ejemplo pasa por acá sale por W pasa por la bobina, cierra el led cruza por acá y cierra.

Cada 2 IGBT por cada bobina.
Cada 2 IGBT por cada bobina, ellos están cerrados los 15 voltios energiza el transistor hace conducir a través de la bobina y cierra el circuito. Necesitamos los pulsos de 15 voltios constantes.

Entre un V y W con la punta del positivo en U vamos a medir un diodo.

Con la punta positivo en V vamos a medir otro diodo y con la punta positiva en W otro diodo.

### U,V y W eso te dará la medición de que estado está el IPM, si alguna de esas mediciones está mal el IPM está dañado

Positivo en U,V,W para un lado me medirá y con la otra punta del tester positivo U,V,W no me tiene que medir nada.

Voy al negativo U,V,W para un lado sí, para el otro lado NO.

Entonces ahí el IPM está bien, entonces es el compresor medimos las bobinas del compresor y vemos que problema tiene.

Aparte de esa medición no podemos hacer otra cosa.

## Con el probador NO PODEMOS MEDIR EL IPM, solo sabemos si anda o no anda.

### Salen del compresor conectamos ese con las dos pincitas de cocodrilo U,V,W y ahí le va a marcar los leds.

Esta es una placa del forzador de la unidad exterior, esta es una placa de la unidad exterior le voy a explicar como son los cables que están conectados ahí.

En esta placa se van a encontrar con 5 cables. 

En el Facebook figura como Marcelo Santini y en la foto de perfil dice M&G.


En esta placa nos encontraremos con 5 cables en el forzador de la unidad exterior si es inverter si es que tiene U,V, y W porque a veces usan de corriente alterna.

### CABLES

El IPM lo tiene adentro, no está afuera. Está adentro en la placa, pero afuera vamos a tener un cable rojo que le va a medir 310 voltios que es el positivo, luego cable negro entre rojo y negro van a tener 310 (corriente continua) que sería el negativo, luego tendrán un cable blanco que ese es el cable le tiene que medir 15 voltios, ese es el que va a excitar a los IGBT del IPM de este integrado, exactamente igual con el motor de afuera con el forzador.

Luego vamos a tener un cable de color amarillo y ese le va a medir aprox. 17 voltios ese le va a informar a que velocidad el está girando el forzador (efecto hall).

Luego se encontrarán con cable de color azul que ese cable les va a informar al microprocesador a que velocidad tiene que girar el amarillo le dirá al microprocesador que velocidad tiene que girar, y el azul le dice a que velocidad gira el ventilador.

Y este varía entre 1 y 7 voltios que les va a decir a qué velocidad tiene que girar, así que cuando vean los 5 cables no se asusten.

Ya saben como medir el cable de señal, para saber si tenemos o no en el equipo medir el voltaje y si no tenemos medimos el optoacoplador para saber en qué condición está el optoacoplador es un diodo emisor de luz que del otro lado tiene un fotoreceptor.

De un lado tiene un puntito cuando vos localizas el diodo el prende, al iluminarse conduce del otro lado y del otro lado siempre maneja el microprocesador.
El diodo para un lado conduce y para el otro no.

#### Medir relay
El relay tiene una bobina y cuando la bobina se energiza esto se conecta y acá hay continuidad cuando la bobina se desconecta esto se abre y se despega, a veces suele pasar que al tener contacto se forma una chispa y el relay queda pegado.

Si te da continuidad entre tal y tal pata quiere decir que está pegado (Marcelo Barrios lo explicó mejor en una de las clases)

Pero si el relay está dañado algún componente se te va a dañar, si ves algún componente dañado relacionado con el relay revisá la bobina.

Te tiene que marcar una resistencia baja pero nunca un cortocircuito.

Chiste: Se puede probar con una pila? Sí señor solo que vas a tener que invertir la pila 50 veces por segundos rápido XDD

Una reparación desde 40 mil tenés que sacar el precio desde lo que vale una placa universal.

Llevá la placa y te digo el problema es tal cosa te hago un presupuesto te digo te sale tanto, por hacer el presupuesto no cobro nada porque hay mucha gente que no quiere mandar a reparar.

FIN
