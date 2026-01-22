---
title: "[AUDIO][APUNTE] Taller reparación de electrodomésticos (Clase 5) - Lavarropas y Termotanque. Triac. Mosfet. Osciladores. Fabricar plástico para nivel el succionador (fallo común)."
date: 2024-08-02T07:46:16-03:00
tags: ['electrodomesticos']
---
#### Audio de la clase
https://youtu.be/LWxML1Yv3IY

https://voca.ro/1hQISTl592Dx

#### O miralo en invidious (es más ligero y sin publicidad)
https://redirect.invidious.io/watch?v=LWxML1Yv3IY



Lavarropas: auto-balance, por eso es malo lavar zapatillas en el lavarropas.  
Hicismos un cambio de amortiguadores 

![lavarropas](/img/clase5_electrodomesticos/IMG_20240801_164015497.jpg)  
![termotanque](/img/clase5_electrodomesticos/IMG_20240801_164034577.jpg)  
![tapa termotanque](/img/clase5_electrodomesticos/IMG_20240801_164148125.jpg)  
![tapa termotanque2](/img/clase5_electrodomesticos/IMG_20240801_164149252.jpg)  
![tapa termotanque3](/img/clase5_electrodomesticos/IMG_20240801_164202579.jpg)  
![termotanque interior](/img/clase5_electrodomesticos/IMG_20240801_164209363.jpg)  
![termotanque interior](/img/clase5_electrodomesticos/IMG_20240801_164229792_HDR.jpg)  
![midiendo continuidad termotanque](/img/clase5_electrodomesticos/IMG_20240801_164906410.jpg)  
![termotanque](/img/clase5_electrodomesticos/IMG_20240801_165552890.jpg)  
![termotanque](/img/clase5_electrodomesticos/IMG_20240801_165556439.jpg)  
![termotanque sacando tuerca](/img/clase5_electrodomesticos/IMG_20240801_165602193.jpg)  
![termotanque](/img/clase5_electrodomesticos/IMG_20240801_170056048.jpg)  
![resistencia y sensor temperatura](/img/clase5_electrodomesticos/IMG_20240801_170103998.jpg)  
![resistencia y sensor temperatura](/img/clase5_electrodomesticos/IMG_20240801_170101031.jpg)  
![IMG_20240801_170501204.jpg](/img/clase5_electrodomesticos/IMG_20240801_170501204.jpg)  


#### Apuntes
Cuando estudiamos vamos a encontrar la placa y el periférico.
El periférico son todos los otros componentes que tiene el lavarropas.

En esos tipos de placas de lavarropas todos los componentes que están ahí menos los sensores, trabajan con 220.

#### Hay muchos sistemas de bloca puertas.
Casi todas las lavadoras traen este: Solenoide de carga o electroválvula.

1ero bloquea, el blocapuertas le comunica a la placa que ya está bloqueada, ahí pasa una conexión para el blocapuertas y para el solenoide de carga entonces la placa le ordena que empiece a cargar agua.

X1,X2,X3 son los papeles que fue agregando a los cables antes de desarmar.

presostato


Verificar el solenoide, la bomba de carga de agua, o sea la electroválvula y la electrobomba y el presostato porque ellos queman placa.

Triac = transistor de corriente alterna.

Antes del triac existía el diac pero eso es sólo para corriente continua.

El diodo no puede trabajar en corriente alterna, por eso inventaron el triac, son dos diodos opuestos.

#### Averiguar sobre triac y mosfet.

En base a este se construyeron los transistores con pintura

mosfet es un semiconductor de oxido metálico

Dentro de la fuente switching hay un oscilador de 8 patitas que a un costado tiene un oscilador conmutador. Hay que poner un mosfet si o si a ese oscilador conmutador, porque trabaja 

Lo primero que haciamos en una fuente switching rectificamos y al lado tenía un capacitor, y con eso nivelavamos las ondas. Eso es una fuente básica porque hay fuentes que son mucho más complicadas y traen filtros incluso inductivos, y si le pongo filtro inductivo con un capacitivo se me va la frecuencia, se sale de face.

Teníamos ese circuito oscilador de 8 patitas y aparte teníamos un mosfet, porque esa fuente switching tenía 311 voltios.
Quiere decir que cuando yo salgo del filtro capacitor esa corriente va al transformador.

Hay una aislación galbánica porque la tierra del primario no es la misma que el secundario 

El blocapuertas es un negocio más no aporta seguridad.


### TRIAC

Un TRIAC es un componente electrónico semiconductor de tres terminales para controlar la corriente.

Su nombre viene del término TRIode for Alternating Current = Triodo Para Corriente Alterna.

Podríamos decir que un triac se utiliza para controlar una carga de CA (corriente alterna), semejante a como un transistor se puede utilizar para controlar una carga de CC (corriente continua).

En definitiva es un interruptor electrónico pero para corriente alterna.

Los triac se utilizan en muchas ocasiones como alternativas al relé.

Su funcionamiento básico es cerrar un contacto entre dos terminales (ánodo 1 y 2) para dejar pasar la corriente (corriente de salida) cuando se le aplica una pequeña corriente a otro terminal llamado “puerta” o Gate (corriente de activación).

Se seguirá permitiendo que la corriente fluya hasta que la corriente de salida disminuya por debajo de un valor determinado, llamada corriente umbral, o se corte la corriente totalmente de alguna forma, por ejemplo con un interruptor o pulsador como luego veremos.

### MOSFET

El transistor de efecto de campo metal-óxido-semiconductor o MOSFET (en inglés Metal-oxide-semiconductor Field-effect transistor) es un transistor utilizado para amplificar o conmutar señales electrónicas. Es el transistor más utilizado en la industria microelectrónica, ya sea en circuitos analógicos o digitales.

Los Mosfet son la mejor combinación de cambio rápido, resistente, bajo en resistencias, y rentabilidad. La baja resistencia térmica y el bajo costo contribuyen a su amplia aceptación en toda la industria


### Transcripción  

###### Primero: reconocimiento visual del lavarropas, puede haber algo suelto algo caído, si nosotros probamos así como está podemos arruinar peor el producto.

Cuando estamos seguro que no hay peligro con la conexión ahí conectamos. 
En este caso no conviene testear con tester, porque el cliente dijo que tenía un problema de que se sacude mucho, por experiencia son los **amortiguadores**.

Siempre antes de enchufar hay que abrir y mirar lo más que se pueda a ver si hay algo roto o algo suelto porque sino lo podemos destruir peor.

Vamos a ver si podemos desarmar el lavarropas.
La puerta del lavarropas siempre conviene tener cerrada porque se rompe muy fácil y sale cara.

Vamos a sacar la mesa de arriba y la tapa de atrás. 

Para sacar la tapa de atrás siempre es conveniente sacar todo menos el de más abajo en el caso de que tenga (tornillos), así nos permite sacar y no caerse de golpe.

Cuando tiene 1 o 2 tornillos en la parte de abajo a eso se lo afloja un par de vueltas y nada más después se saca todo lo de arriba entonces ahí sale fácil.

En este caso este tipo de tapa no viene con **ojal**, sino que viene con medio ojal (los huecos), este lavarropas tiene medio ojal, o sea que este caso apenas sacamos y la tapa ya va a ir quedando suelta.

Este (no sé) es una parte muy delicada del lavarropas y conviene sacar, esto es peligroso cuando queda en el suelo, si hace calor aguanta un pizotón pero si hace frío se parte, está muy cristalizado.

Por lo general todas las tuercas que traen el lavarropas a no ser que un técnico lo haya cambiado, es de **1/4 (6.5 milímetros)**, boca hexagonal con llave la que tengamos. **Hexagonal es más cómoda.**

Que está podrido al costado también puede ser la causa de la sacudida.

Todas las llaves son de 1/4, todas van a servir.

Dejá 1 o dos tornillos y hay que sacar las trabas.


En las lavadoras no todas tienen el mismo sistema de enganche, hay algunas lavadoras que la tapa termina acá adelante entonces suelen traen un "encastre" que hay que correr para adelante, hay otras que hay hacerle para atrás y hay que hay que levantar y hace un ruido que como se rompe pero no está roto XD. El que rompe paga.

Por lo general nos darán la placa y el periférico. El periférico son todos los demás componentes que tiene el lavarropas.

Periférico es lo que nosotros vamos a reparar.

###### Como funcionan todas las cosas que hay adentro?
Por electricidad.

En este tipo de lavarropas con este tipo de placa todos los componentes que están acá menos los sensores trabajan con 220 voltios así que no hay problemas de medirle.

Vamos a suponer que tenemos un problema con 1 componente nosotros podemos desenganchar ponemos 2 pinzas de 220 y probamos si anda.

Entonces una de las primeras cosas que funciona en el lavarropas es el **blocapuertas**. La única función del blocapuertas es trabajar la puerta no tiene otra función, cuando nosotros aprendamos a engañarle a la placa que el blocapuertas está funcionando, **puenteamos el blocapuertas y el lavarropas ni se entera**. 

¿Por qué?
Porque la función de ella es el termostato 1 viene a ser el común, 1 es entrada a la fase porque funciona con 220 voltios, cuando calienta un componente que tiene adentro viene a ser un **PTC** cuando eso calienta hace que se bloquea en esa posición, una vez que se bloquea para a cerrar un switch.

Una vez que la puerta quedó cerrada y el switch cerró todo está en serie, el que queda en paralelo es el componente térmico, que hace que se bloquee. En el blocapuertas todo funciona con 220 no hay problema. **Hay que tener mucho cuidado con un puente que se hace porque sino podemos colocar fase y neutro y ahí viene la explosión, tiene que ser neutro fase y fase siguiente. **

O sea que este neutro que está acá es para que el componente térmico que está acá **cierre el circuito tanto el switch como el candado**. 

Hay muchos sistemas de blocapuertas.

Solenoide de carga o electroválvula por lo general hay 1 sólo.

### Solenoide de carga

##### Pasos de un lavarropas
Bloquea, el blocapuertas le comunica a la placa que ya está bloqueda.
Ahí inmediatamente pasa una conexión para el presostato y para el blocapuertas y para el solenoide de carga entonces la placa le ordena que empiece a cargar agua, porque no tiene.

Si nosotros miramos este sería el dispenser, jabón en polvo, jabón líquido y suavizante. 

Nunca va a traer sólo para jabón líquido, hay sistemas que suele traer acá una especie de bandejita que viene calculado para jabón líquido.

Viene con una bandejita acá arriba que se puede sacar para colocar el jabón líquido, si no uso el jabón líquido entonces saco esta bandejita y me queda para jabón en polvo.

Esto que viene acá es para usar acá XDD (era una trabita del dispenser)

Ahora yo le voy a poner acá porque perdieron el otro.

La trabita de plástico es para auxiliar a otro lado.

#### Por qué?

Porque esto que tiene acá tiene un orificio ciego que hace trabajar como función por caída de gravedad (la trabita de plástico), o sea que el agua va a entrar acá en la bandeja a este nivel y va a empezar a derramarse por ese orificio que está ahí, pero **si yo no tengo este componente como no tenía el jabón líquido acá ya se cae todo abajo**, no pasa nada pero no es lo correcto, entonces trae este "tabique" XD.

Entonces si yo pongo el jabón líquido, acá tiene una carga máxima y si yo quiero más potencia al jabón líquido cargale dos veces, pero no te pases porque el jabón líquido es muy viscoso es muy pesado, entonces eso no tiene la fuerza necesaria para hacer la succión, debemos colocar el jabón líquido hasta acá, para que la válvula que está ahí carga el agua acá.

Entonces cuando la placa ordena que se cargue agua, a la primera que la va a ordenar será a la azul, yo tengo 2 ahí. Como me doy cuenta cual es la primer válvula, **porque la carga es en diagonal**. No es directa, entonces eso quiere decir que tiene que pasar todo allá para caer acá el agua, entonces lo que yo tengo acá como componente líquido para lavar va a empezar a caer desde la lluvia que está acá dentro al dispenser va a permitir que se empiece a mezclar el líquido pesado con el agua, entonces lo hará más soluble más liviana, y acá va a caer un buen porcentaje de agua.

### Siempre carga cruzado.

Entonces la función del nivel es para eso entonces si nosotros colocamos el jabón líquido y vemos que la ropa necesitará más, nosotros mirándole ponemos pausa esperamos que el agua caiga todo adentro, volvemos a cargar jabón líquido y con 2 cargas ya es más que suficiente.

Nunca pongan más porque le va a costar, va a comenzar a aparecer por decantación que por succión.

Una vez que el nivel llegó acá arriba, como este agujerito está más abajo va a empezar a caer el agua por el agujerito y como no hay por donde ella pueda tomar aire va a ser el mismo trabajo como cuando nosotros colocamos un valde chupamos con la manguera y lo dejamos caer, hasta que no haya una filtración de aire porque el aire es más liviano que el agua, no te va a afectar la caída del agua.

El aire es más liviano, así que si entra aire va a pasar primero el aire antes que el agua y va a interrumpir, va a dejar de caer agua, hasta que no chupe aire acá abajo el agua se va a decantar todo.

Una de las primeras cosas que vamos a ver en el lavarropas es que cuando la enchufamos bloqueó la puerta, es en el otro lado donde va a caer la lluvia 1 minuto más.

Primero va a cargar con esta manguera y después con la manguera marrón, hasta que el **presostato** diga listo, ya está bien de agua.

El vinagre blanco le saca más y sale un aroma especial XD, mejor que el suavizante.

Mi sobrina me dijo que el mejor lavado es con desodorante para piso.

Eso hacen en los hoteles, tenemos un alquiler TEMPORARIO XD, **las toallas blancas limpiamos con vinagre**.

Los primeros minutos de entrada verán que el agua caerá acá XD aunque le pusiste jabón en polvo, porque la lavadora no tiene un sensor saber que tipo de limpiador nosotros pusimos, entonces ella se asegura con los dos, con 1 minuto ya le basta para alivianar el líquido.

Entonces si hay jabón líquido con ese ya le alcanza, si hay jabón en polvo le va a costar más mandar el líquido.

Vamos a ver funcionar en dos partes, corta una lluvia y después empieza de la otra.

Ya sabemos como está hecho el lavado, no importa el limpiador que nosotros usemos siempre va a ser lo mismo. 

Por mi experiencia el jabón líquido destruye la estrella.
El jabón en polvo también pero el jabón líquido le hace mierda rápido.

#### Que es la estrella?
Es un sistema que va acá dentro para que de vuelta tina. Tómenlo como comentarios.

Cuando va a ser el líquido de lavado otra vez nosotros tenemos el nivel en donde debe ir el líquido, necesita alivianarse porque acá otra vez tiene el mismo sistema.

Cuando se pierde esto, si somos ingeniosos debemos inventar el succionador para que funcione, es fácil de fabricar.

Entonces después viene acá el líquido depende de la cantidad de agua que haya en que tiempo va a lavar.

Lo interesante es que nosotros tenemos 3 compartimientos, lo bueno de esto es que acá nosotros tenemos 3 compartimientos y tenemos sólo 2 electroválvulas. 

Los lavarropas tenían 1 sólo, pero tenían el programa sin placa sino mecánico, entonces tenía una violeta que hacía manejar un hierrito donde acomodaba para lado tenía que ir el chorro de agua, en lavado o en enguaje.

#### A LA MIERDA TREMENDOS GENIOS.

Como esto es electrónico nosotros una vez que colocamos el programa, no se mueve. El hace cumplir por placa, los técnicos superaron esto **hacen funcionar las dos electroválvulas juntas**.

A veces nos van a decir que el lavarropas funciona bien, pero no lleva el líquido suavizante.

### Está lavando bien, pero no lleva líquido suavizante.

Lo que pasó es que una de las electroválvulas no está andando entonces está tirando para 1 sólo lado.

Cuando entra a funcionar la que carga el jabón en polvo si funciona, pero la otra no. Entonces cuando tiene que enguajar no tiene donde chocar el agua entonces el agua viene todo para acá.

Tengo que ver la segunda y se verifca con 220, tengo que tener el power ("chicote de prueba").

El agua al tener más volumen no puede pasar, la valvula que es un solenoide que trabaja por campo magnético entonces está cerrada, cuando yo activo el campo magnético el émbolo abre y ahí pasa el agua, cuando está bien y el presostato le dice a la placa que ya está bien de agua, la placa le corta la corriente al solenoide, entonces al émbolo lo lleva para abajo y no pasa más el agua. Esto yo lo puedo poner en mi cocina con una perillita que prende y apaga.

Se puede regar el jardín con un timer porque el consumo de esto es muy bajo.

Entonces nosotros con un chicote de prueba, dos pinzas de cocodrilo, o dos fasto hembra, entonces desconectamos acá le ponemos el fasto (o pinza de cocodrilo).

El fasto son los terminales.

Tengo un chicote de prueba con interruptor para no desenchufar y enchufar.

Vamos a tener que poner un clavo para tenerlo siempre a mano. 

Acá hay 2 chicotes de prueba con fasto aislado, y acá tengo 2 sin aislantes, porque a veces cuando estás tirado en algún lado es imposible de ver y hay lugares en donde no es seguro usar el sin el aislante.

El sistema puede tener varias electroválvulas.

### Si le pruebo con 220 hace algún ruido? Como compruebo si anda o no ?

Podés ponerle una manguera de agua desde la canilla con la canilla abierta no va a salir el agua, cuando le ponés 220 sale el agua, se puede hacer también soplando pero no es preciso, cuando no hay pan vienen las tortas.

### Los semiautomático tienen el presostato que vos le soplás. El presostato es el que controla cuando le falta agua.???

Este es el que controla cuando le falta agua y cuando ya está completo, presostato hay muchísimos, blocapuertas hay muchísimos

Este es el que controla cuando le falta agua y cuando ya está completo, presostato hay muchísimos, blocapuertas hay muchísimos. Esto son todos iguales, puede tener una electroválvula 2 3 4 pero todas son iguales, ahora para comprar son distintas porque si comprás 2 de 1, no lo mismo que 1 de 2, pero a veces sirve para reparar.

Esto va puesto como si fuera una especie de presión, si en ese momento quedó incómodo el azul de abajo podemos aflojar un poquitito si se agachan vamos a ver que hay dos iguales. Hundimos de nuevo y seguimos dando vuelta para el mismo lado ,podemos hacer eso y desenganchar acá para medir porque está incómodo ahí, y para colocar.

El primer enganche tienen que ser las aletas y los pines van a quedar afuera. Recién cuando giramos los pines van a ingresar.

Ya cargó jabón está lavando terminó el ciclo de lavado, entonces ahora tiene que desagotar, porque esa agua tiene jabón y tiene suciedad. Es como lavar una pileta una vez que terminamos de lavar, tiramos el agua que está sucia y escurrimos, porque tengo que sacar toda la roña que está dejando casi seco y ahí es donde entra en un proceso de centrifugado que no es el centrifugado final, es un centrifugado previo al enguaje y ahi recién va a hacer un enguaje 2 enguajes y después recién va entrar para que suavice la ropa, cuando ya está lavado.

Es peligroso que el lavarropas se deslice.

## Lo hago con un cajón de coca o un cajón de tuppi para que no se deslice el lavarropas.

#### La bomba
Entonces donde comienza esta manguera allá bajo ahí está la bomba que saca el agua.

Yo hice miles de experimientos para reparar bombas, el eje es de acero inoxidable y se gasta, y el eje viene soldado adentro del imán. No hay forma de sacar sin que se rompa.

Acá tenemos el tacho que tiene unos resortes de lana suspedidos esos van engachados cuando ustedes saquen acuerdense que van en forma opuesta no van los dos del mismo lado.

Uno de los motivos es que uno de los resortes se haya roto por fatiga una sola vez hice el cambio de uno pero no dió resultado, generalmente son por los amortiguadores que hay abajo.

Los amortiguadores no tienen nada de tecnología, ni resorte ni líquido, es sólo un cilindro caño y lleva como si fuera engrasar no es bueno, tiene que duro.

Los amortiguadores son iguales para la mayoría de los lavarropas, tienen un poquito de freno.

### Si no podemos comprar uno nuevo

53:40

Sólo hay que cambiar la parte de arriba del brazo ya está solucionado.

Para sacar los amortiguadores tiene una lenguetita 


Los amortiguadores no tienen tecnología, sólo tiene un cañito fino y un retén muy fuerte, es de silicona no es de plástico.

### Entonces los resortes de arriba no se cambian?
Yo he cambiado alguno en donde se partieron, y casi siempre son iguales las medidas o pones dos cortitos o dos largos.


Esta piedra que está tiene 1 que es más o menos de este tamaño, este tacho hay muchas formas de este tacho muchas medidas, se une la tapa de atrás con la de adelante.


En la tapa de atrás siempre viene puesto 2 asientos de rulemanes, un rulemán del lado de afuera y del lado de adentro.

En el lado de adentro trae 1 retén. Lo que generalmente hace que haya que cambiar los rulemanes es porque el retén perdió su precisión de sellado entonces comienza a filtrarse agua y arruina el ruleman.

**Y ese cuesta un poquito más cambiar**, si en algún momento yo puedo traer una tapa trasera voy a traer para que ustedes vean como está puesto el rulemán.

Para cambiar el ruleman hay que sacar este que se llama puente esto permite que eso no se desamolde es una chapa muy finita, y acá es donde va el resorte al tambor.

El dispenser acá adelante va agarrada a la caja con 3 tornillos que son tornillos especiales, si hay algún phillips vamos a sacar 1.

Siempre cuando vamos sacar estos tornillos de acá, siempre conviene en la garganta cubrirlo porque sino se va adentro y el tornillo es muy especial. Con un trapito vamos a tapar así así no se va a caer, ese tornillo tiene una medida especial. Así no se cae.

**Hay técnicos que colocan cualquier tornillo no van, y se agrietan rompe porque le ponen tornillo más grande.**

La mayoría no coloca los 4 tornillos porque dificulta el translado.

#### Siempre cuando vamos a sacar esto lo vamos a colocar, siempre conviene acá en esta **garganta** cubrirle porque sino se va adentro y ese tornillo es muy especial. Tapar con un trapito porque si nos llega a caer no se nos va adentro.


Se rompe porque apretar porque le ponen tornillo más grande. y este tiene una medida especial que si ustedes ven está devastado, yo tengo muchos tornillos, pero los que son de esta caja yo guardo porque muchas veces se pierde.

Guardo en una cajita de tiktak.

No son tornillos tan largos, lo que tienen bueno es el ala de la rosca, no tienen arandela, acá el **ala de la rosca** son bien grandes par que si hacemos fuerza de más no se lave fácil. Antes pasaba mucho con las lavadoras, te pasas con un poco de fuerza y lavaba el plástico.

#### ¿Qué significa que se lava?
**Como son ala más grande no se lavan fácil**, cuando uno ajusta y safa ya no ajusta más, redondea la rosca.

Hay que separar todas las conexiones del lavarropas.

Y después les voy a mostrar como van las conexiones: x1,x2,x3,x4,...x10.

Vamos a sacar el blocapuertas, como hay que saber cuando hay que sacar el tambor por debajo o por arriba?

El blocapuertas no se repara. Cambianle siempre.

El blocapuertas, el solenoide, y la bomba, son dolores de cabeza que QUEMAN placa, cuando van a cambiar la placa que está quemada, verifiquen que funcione el solenoide, verifiquen que funciona el blocapuertas y que funcione la bomba de agua. 

### Antes de eso verificar el solenoide, la bomba de carga de agua, la electroválvula, la electrobomba y el presostato porque QUEMAN placa.

Si nosotros miramos tenemos unos números, blocapuertas hay muchos y no todos son iguales. La fase es el común el neutro es el común cuando la placa ordena que funcione el blocapuertas.

El chip es el que da la órden, pero no puede hacer funcionar el blocapuertas porque funciona con 220 voltios, necesita dos componentes: TRIAC se usa para disparar los 220 voltios.

TRIAC: transistor de corriente alterna.

Antes existía el DIAC pero es sólo para corriente continua. Entonces inventaron el TRIAC en el símbolo el TRIAC son dos diodos opuestos.

Que vendría a ser la barrida del cátodo, si entra el ciclo positivo, estamos en la corriente alterna el diodo vamos a medir los diodos, este que era: cátodo. Esto es el cátodo y el otro es el anódo, **la corriente positiva va desde el anodo hacia el catodo, y el voltaje positivo, y el negativo desde el cátodo hacia el anódo**.

### Entonces si viene la corriente positiva por donde va a pasar?? 

Cuando está el ciclo negativo no puede pasar, entonces va a entrar por el cátodo cuando viene la negativa y siempre va a psar los dos ciclos. El problema será con qué cantidad de cantidad de voltaje se dispara, porque hay veces que el chip no tiene la **cantidad de voltaje que necesita el triac, por eso no se puede poner cualquier triac**.

Y hay que ver si es para un blocapuertas o un motor, hay que ver el amperaje.

En internet hay unas páginas llamadas datasheet.

Traten de leer un poquito sobre triac y mosfet.

No importa si no entienden.

Voy a estar a la distancia de una voluntad de ustedes.
Es otro transistor en base a ese se construyeron los transistores con cuntura por cuntura de las **obleas** como están hechas.

Y el mosfet está hecho con óxido metálico, entonces el que primero apareció es el de cultura común sigue dando beneficios, cuando entramos a la fuente switching o conmutada.

En la fuente lineal lo primero que aparece es el transformador, y luego se rectifica. En la fuente switching lo que primero se hace se rectifica porque no sirve los 50 ciclos, una vez que tenemos corriente continua sí necesitamos ahora oscilar a 10.000 a 100.000

### y ahí le dije que si yo tengo dos transformadores para fuente lineal,
Si yo necesito un transformador de 3 amper y conseguí uno de 5 amper, me va de lujo pongo ya está, **en la fuente switching no se puede porque está hecho para determinada frecuencia. Los ciclos no son iguales.**



Si yo quito la fuente switching de una placa del mismo lavarropas y le pongo a la otra sí va a funcionar.

El transistor de cuntura no sirve porque es muy bajo ciclo a muy baja frecuencia, ahí apareció el MOSFET.

Yo le había dicho que dentro de la fuente switching hay un oscilador de 8 patitas y a un costado suele haber un oscilador conmutador, entonces primeramente ese oscilador había que poner si o si un transistor MOSFET porque el oscilador, la fuente switching trabaja con bajo voltaje.

La fuente switching primero rectificamos y luego bajamos el voltaje.

El transistor de cuntura no sirve porque es muy bajo ciclo a muy baja frecuencia, ahí apareció el MOSFET.

Yo le había dicho que dentro de la fuente switching hay un oscilador de 8 patitas y a un costado suele haber un oscilador conmutador, entonces primeramente ese oscilador había que poner si o si un transistor MOSFET porque el oscilador, la fuente switching trabaja con bajo voltaje.

La fuente switching primero rectificamos y luego bajamos el voltaje.

El transistor de cuntura no sirve porque es muy bajo ciclo a muy baja frecuencia, ahí apareció el MOSFET.

Yo le había dicho que dentro de la fuente switching hay un oscilador de 8 patitas y a un costado suele haber un oscilador conmutador, entonces primeramente ese oscilador había que poner si o si un transistor MOSFET porque el oscilador, la fuente switching trabaja con bajo voltaje.

La fuente switching primero rectificamos y luego venía el capacitor, y con el capacitor lograbamos nivelar un poquito las ondas que sea más pareja, en forma básica porque hay fuentes que tienen filtros inductivos **si le pongo un filtro inductivo le tengo que poner un capacitivo y se me va la frecuencia**. Se sale de fase.


Entonces tenemos ese circuito oscilador de 8 patitas y aparte teníamos un MOSFET porque cuantos voltios tiene esa fuente switching hasta antes de oscilar? 311 voltios

311 es el valor pico, quiere decir que cuando yo salgo del ciclo ese capacitor va directamente al transformador pasa por todo el devanado del transformador y que polo tiene esa corriente? **Positiva**.

### Por qué no va la negativa?

###### Yo les había dicho que por lo general en la corriente continua se usa uno del 1 del polo para chasis vivo o para chasis.
???????
Es decir que yo apenas saco el saco del transistor negativo y le mando al chasis.

En cualquiera de las partes de la fuente sea la primaria o la secundaria yo saco del transformador y ya le mando al chasis negativo, **en cualquier parte del chasis yo tengo negativo**. En el primario yo también tengo el mismo un valor negativo, **pero no son iguales los valores negativos.** Están aislados por la **aislación galvánica**.

#### Hay una aislación galvánica porque la tierra del primario no es la misma que el secundario si bien oscilan iguales las dos, como oscila el primario tiene que oscilar el secundario al mismo ciclo, pero las tierras son distintas por eso tenés que **tener cuidado de no tomar una tierra del primario para medir el secundario.**

No es así, quiere decir que del filtro a donde va? Al transformador al primario del transformador de alta frecuencia y para que eso funcione necesita para que funcione? 

- Yo le puse un positivo pasé por todo el devanado primario y que necesita ahora?
Vamos a suponer que no es un transformador, es un foquito, le pongo el positivo al foquito y el negativo al chasis, porque tiene que tener los dos polos: fase y neutro o positivo y negativo.

Entonces quiere decir que yo le mando el positivo ya ajustado directamente al devanado y necesito ahora en el otro extremo del transformador el negativo o el chasis.

### Si yo le pongo no funciona porque es corriente continua pura, entonces quiere decir que una de esas partes yo le tengo que mandar al integrado que oscila, porque el va a oscilar con el negativo, va a ser un platino que estará conectado al chasis y de este lado va a ser así y le va a mandar ese negativo para poder oscilar y poder mandar corriente al secundario.

?????

Entonces necesito 1 **OSCILADOR**, son un montón de componentes que está dentro del integradito de 8 patitas, 

como se logra esa frecuencia?

Con los componentes que van alrededor con los capacitores y resistencia, o sea que esos componentes pueden servir para varias frecuencia, todo depende de como esté hecha la resistencia y los capacitores de alrededor de ese chip.

Entonces como el chip no se banca el **voltaje** para trabajar a 311 voltios, necesita algo que le haga de intermediario y se usa un MOSFET.

Entonces en la compuerta del mosfet trabajaba la salida del oscilador, a 15.000 ciclos entonces una de estas patas va a tierra y la otra al transformador. 

# En la fuente switching ya no van a encontrar más el MOSFET porque le pusieron el MOSFET adentro del integrado.

Dentro de la fuente switching vamos a encontrar fuentes switching con transformador MOSFET visto y otros no vistos, pero de que está está, dentro del integrado.


Entonces tenemos el blocapuertas que sirve para asegurar puertas, el blocapuertas se inventó para que los niños no entren dentro de la lavadora, pero es demasiado difícil que pase eso.

# Los lavadores de ahora no lleva hasta arriba el agua, entonces es por eso, 
pero es un negocio más, se quema se rompe quema placa, por eso no sacan ya está al pedo.


### Blocapuertas (puentear)
En el caso de que esto esté quemado o tienen miedo de que esto le queme la placa, tienen que **pelar los dos marrones unimos los dos marrones y ya quedó**, nunca va a quedar trabada la puerta, estamos **engañando al lavarropas** puenteando el blocapuertas. Entonces esa es la manera de que si el blocapuertas está jodiendo asegurarse que no te **queme la placa.** 

En la bomba de agua no podemos hacer lo mismo, en el solenoide tampoco creo, entonces ??????? cuando tengas dudas, tenemos que probar esto con la serie.

Cuando conectamos y corremos esto para atrás no queda, volvemos cuando esto conectamos y funciona eso queda ahí porque el térmico que está dentro ya 

Cuando termina de lavar la placa le corta la corriente y como sigue **caliente le sigue bloqueando**, se tiene que enfriar la pastilla, ahí abre y ahí si se puede sacar.

cuando le mandamos corriente a el y esperamos ya no anda hay que cambiar, si no tienen para cambiar sacan esto esto colocamos allá porque sino la puerta no va a cerrar y esto dejenlo suelto, pelen acá y pelen acá y hagan un tornillo, aislenlo para que no toque en ningún lado y quede con corriente o sea yo le saco el forro de acá y estos dos forros que no tienen ahí yo le uno.


Lo que es conveniente es que quede suelto, este le volvemos atornillar allá y que quede colgando.


Entonces a'ca tenemos el numero 2 3 y 1 , no hay formas de colocar al revés esto porque tiene guía, no hay formas de poner de una manera que no sea esta.

### Le colocamos del lado correcto y entra solo si vemos el 1 está en común, entre el 2 y el 1 hacen calentar la pastilla y con el 2 se va a la placa.


Si miramos dice RF (resistencia) pero no todos traen eso.


### Vamos a armar eso.
Cuando compras un blocapuertas nuevo viene sin el cable

Muchas veces pasa que tiene una falla y queda trabada el blocapuertas.

01:46 ¿quién se quiere para colocar los amortiguadores?

#### Yo coloqué el amortiguador no lo saqué.
Tenés que ubicar el agujerito del amortiguador, tenemos que contar 3 orificios si hay 2 no te sirve, acá no te vas a lastimar.

Quién tiene la tuerca?

Ahí va el perno, agarralo y ahora le ponemos la tuerquita y la arandela, vamos a ajustarle un apriete normal nada fuerte. 

ahora acostate este ojal que está acá tenemos que colocarle acá dentro de este, y para hacer eso movemos, este es el pin que va allá.

Acá está la lengueta que tenemos que empujar, dale con fuerza , tocá el ojal de abajo y apretá la lengueta.

Hay que sacar la arandelita.

### Donde venden amortiguadores?
Uruguay casi mitre (electroservice hugo)
San lorenzo y sarmiento en la esquina.
Santa fé y san lorenzo (rubén)

Santa fé y san lorenzo subiendo para sarmiento, por la misma sarmiento por san lorenzo subí hasta sarmiento antes de llegar la esquina

Y el otro lavalle de martín fierro para allá media cuadra para este lado.

Otro por san martín y santa cruz, y otro santa catalinacasi santa cruz.


Después garupá está el bingo que está ahí en san martín santa cruz, antes del casino después de fátima media cuadra para allá.

Tacuarí y no se qué de andreas está el otro.

Otro: itaimbé mini flapé.

Otro: francisco de aro por cocomarola.
---

Vamos a poner en marcha sin la tapa.

En ferretería común hay correa de lavarropas.

Este lavarropas la primera vez se rompió el tacho, **se rompe la estrella ya está mala y sigue lavando y rompe la tina**. Y otras veces donde va el asiento del roleman ahí se gasta.

Hay lavarropas que suelen tener tomas como estas uno que dice encendido y esta no tiene, tiene una que dice inicio y pausa, con este encendemos y elegimos el programa que queremos.

Ahora vamos a elegir el tiempo que queremos lavar.

No está puesto en temperatura a 1200 revoluciones va a secar y va a tardar 1 hora y media el lavado.

Volvemos a girar la perita hasta que sea el mínimo tiempo posible. Así como nos da el tiempo también nos dice que tipo de ropa va a lavar porque tiene que ver que tipo de ropa lavará porque tiene que ver con el sistema de agitación de acá dentro.


#### ¿Cuando mi mamá lavaba a manos?
Cuando tenía ropa fina, mi mamá las ropas delicadas no quería poner en el lavarropas. Este lavarropas permite lavar la ropa fina, si poné un jean y poné una ropa fina **no lava la ropa fina**.

**No podés cambiar el programa, la única forma es apagarlo y ahí darle la función deseable**.

El vaiven cuando queremos probar el lavado a mano no se asusten porque es para la ropa muy delicada.

### Que es lo que primero hace?
El blocapuertas se bloquea, y empieza a cargar el agua, ahora cortó y ahora verifica si la bomba funciona está testeando si no funciona la bomba te marca el error. Primero hizo un testeo 1 solenoide y testeó el otro solenoide y testeó la bomba. 

Ahora los dos chorros de agua van a chocar y va a ir en el medio (los dos solenoides de carga chocarán)


**Dependiendo de donde tenés el tornillo se saca el tambor por arriba por el centro o por abajo**.

Es depende de donde está el tornillo.

##### En diferentes lavarropas se desarma distinto. Se saca todo, se saca la piedra, el cuello, el motor, desconectar la bomba, desconectar los amortiguadores, y después tenés que sacar el rulemán de adentro chiquito.

Alumno: me compré un tester marca el positivo, no chilla el negativo.
Profesor: yo te enseñé, por qué mide eso? Yo tengo un tester común pasamos por un cable ese me mide y el tester común no. Por qué?
Alumno: Por el campo magnético
Profesor: Entonces eso se da en la corriente alterna.


????????? A qué hace referencia acá?

Porque yo tengo un tester común y pongo y no me mide pasamos por un cable no me mide y ese tester si, por qué? Por el campo magnético y eso de da 

Ese me mide y el tester común no, por el campo magnético, entonces eso se da en la corriente alterna en la continua no podés usar no podés usar eso.

Donde no se te prendió más ahí está el corte, 

### Esto negro que es?

Es la parte interna del chasis, la tina fue rosando y fue cortando el chasis, esta es la parte de afuera.

Ahí está la estrella y le recontra comió el jabón líquido.

El jabón en polvo le deja todo blanco oxidado.

### Los rulemanes están sanitos pero hay que cambiar porque ya lo abrimos, 

## se rompió cada aspa de la estrella porque le comió el jabón líquido, 

# Trabajos que se le hizo a este lavarropas.
## El lavarropas primero entró por problema de placa, le solucionamos y lo llevamos. Traigo y se había clavado la caja, lo reseteamos y lo llevamos de nuevo. 1 mes habrá andado me decía que el rulemán tal error, traje y se había comido los **carbones**. Le cambiamos los carbones. Los amortiguadores andan todavía pero no sé durante cuanto tiempo.

El cliente Lava todos los días 2 veces a la mañana , 2 veces a la tarde. Habrá pasado 20 días, Marcelo mi lavarropas hace un ruido terrible, el profesor se dió cuenta que era la estrella, dejá de lavar porque vas a romper el tacho le dijo. 


#### Siempre el cliente te dice que es lo mismo que hacía antes.
Mi luz alta de un lado andaba pero antes de llevarte sí andaba, así te tira la culpa el cliente.

Primero yo soportaba todo pero de apoco fui eligiendo el cliente, ¿y cuál era la manera? El precio. Al que me molestaba mucho, yo le ponía un precio altísimo.

### Por qué? Porque el cliente va a decir ese técnico es bueno, pero se volvió muy carero nada más XD
Yo no siento que esto es un trabajo, esto es un hobbie.

Ninguno de mis hijos es técnico. Yo tengo técnicos amigos mios que saben arreglar de memoria le dicen quitale tal cosa pero no saben lo que es.
Hace 7 años que arregló uno de esos y se acuerda.
Che marce viste la heladera que tiene tal manija, mirá si me voy a acordar eso.
Si yo le digo sácame un gráfico se mueren, tienen una fobia, cable por cable y así fui aprendiendo.

Podés encontrar un profesor que te enseñe split, estufa aires acondicionado, heladear cámaras, pero que te enseñe como hago yo difícil.

Las revistas, los libros no están escritos para como uno habla.

Esto ya lava, así que vamos a pasar al centrifugado.

Vas a cometer un error, no cometas el error: Cuando uno va a cambiar el programa tiene que poner en 0, para cambiarlo.

Es sólo para probar el funcionamiento.

El profesor enumera las conexiones: x1,x2,x3,...,x10 para que cuando agarra la maraña de cables para ir colocando para no estar perdiendo el tiempo. Los x1,x2,x3,...,x10 hacen referencia a la placa.

#### Es una fuente resistiva resistiva por eso muchos no lo consideran fuente: tiene resistencia y tiene capacitor.

### Cuál es la función de la fuente?
Tengo que modificar el voltaje, tengo que llevar de 220 al voltaje que necesita el chip.
Si nosotros miramos nos preguntamos con qué transformador trabaja esto? Como baja de 220 a 5voltios.

Tenés que buscar esa escala para poder medir, yo te puedo decir esto es una resistencia vos te vas a ir a la placa y vas a encontrar uno igual y es una bobina, o un condensador.

A medida de que vayamos avanzando o mirando 

#### La clase que viene vamos a medir los TRIAC y los MOSFETS

#### Ahora está trabajando la bomba, no tiene más agua pero sigue trabajando, no hay forma en que se le pueda parar, esto es así.

AB = Auto balance, está acomodando la ropa para que el sacudón sea lo menos posible, por eso no es recomendable no lavar **zapatillas** sino que le produce un gran desvalanceo.
No van a quedar una zapatilla enfrente de la otra, no podés hacer que centrifuge.

#### Podés lavar la zapatilla pero no centrifugarla.

El chitido puede ser rulemán y estrella, y como se puede saber si es rulemán o estrella.

El rulemán hace mucho ruido como piedra algo que choca, cuando los rulemán están rotos. 

Para que se rompa la estrella el rulemán tiene que estar recontra destruído que se va a escuchar fuertísimo.

02:29:19
Una de las particularidades generalmente el galopeo del ruleman se siente cuando una de las aspas está punto de quebrar o sea ya se desarmó del centro que tiene que mantener latina o ya uno se rompió, es difícil que se rompa todo.

# Importante 
????
Entonces cuando es rulemán sin ruido? Si somos sordos.
#### No siempre es con ruido porque a veces el rulemán revienta, entonces ahí no hace ruido.
Cuando sentimos ruido adentro del tacho, para que podamos saber si es rulemán roto o es estrella, **hay que mover la TINA del lado de adentro el agujerito, el de metal el tacho o el tambor.** Ahí es donde va el eje. Cuando está roto uno de los brazos de la estrella nosotros miramos adentro nosotros movemos adentro y es como que no hay extrapresión es como que está todo bien , pero hace ruido, en algún lado pega TOC TOC TOC.

02:31:18
### Como saber si es rulemán o estrella.
Si yo abro la puerta tomo la tina y muevo: rulemán.
Si yo abro la tina y no se mueve la tina: la estrella.

Para arreglar chapa rota: buscá una chapa 26,24 de ancha y el número, le tenés que pegar 10 centímetros para arriba y 10 centímetros para abajo. Yo siempre remaché, un día un amigo me dijo que el **pegar con la tela del zapato**.

Queda lindo pero no me acostumbré así.

Le hago la línea, le mido cuanto remache voy a poner.

### Mandó a arreglar mi señora la heladera, le cortó con tijera quedó todo feo y le colocó **remache**. Quedó andando pero fue horrible.

Le pinto de nuevo de blanco o sino a veces le coloco un beigh (color) clarito de un lado y del otro.

Lo importante es no debilitar la parte de abajo.

Soldar no es una buena opción porque es carísimo, remache no más y nadie te va a **pagar**.

Un tiempo que arreglaba heladeras familiares fabriqué una pega, pero hay dos cosas que no me gustan:

* No me gustan sacar las piezas del auto.

Yo soy de la época de las reparaciones porque eso dejé la electrónica.

Una época que no caía nada, empezaron a caer televisores y equipos de audio. Voy a empezar con bobinado.

De una voleadora está cortado el bobinado: tenés un bobinado en el rotor y en el campo. El del campo es fácil. El alambre sale caro.

### Termotanque

Yo sé que se come de adentro, se pudre por dentro, se le pone brea.

Es para que en vez de que las sales del agua se mantengan dentro del tacho, se pegue a él, como un imán de porquerías.
Para que no lo oxide más rápido.

Tiene un térmico cuando el agua está fría caliente y después se apaga ya sí.

Vamos a medir la resistencia, vamos a traer un tester y vamos a medir.

Vamos a medir primero si anda la llave.
Vamos a pelarle el cable del termotanque arriba.

Mide el del azul y el marron?

Marca algo que no dijieron.

Al desarmar el termostato nos encontramos con el termostato y la resistencia.
Primeramente no venía el termostato y se quemaba mucho la resistencia.

La mayoría cobra por testear el problema: 5000 pesos una miseria.

#### ¿Como funciona el termostato? Como si fuera un switch.

Cuantos tipos de switch conocen? Dos: normalmente abierto y normalmente cerrado. 
#### Este cual vendría a ser: normalmente cerrado, porque abre cuando ya llegó a la temperatura, pero cuando está en estado normal está cerrado porque sino calentaría.

Entonces quiere decir que si nosotros medimos continuidad nos tiene que funcionar, anda la resistencia y el termostato.

##### Puede llegar a tener un error así como yo medí? Sí, puede ser que el termostato esté pegado y que siempre esté cerrado o sea que llega a la temperatura pero no corta.
Ahí vamos a tener que ir con la pinza amperométrica controlandole que esté en los 9 amper, 10 amper, hasta que llegue a 0 amper... Y si no corta y el agua empieza a hervir hay que cambiar el **termostato**.


### ¿Hay campo magnético acá?
NOO, trabaja todo por electricidad y por temperatura o sea que el termostato no trabaja por inducción sino por temperatura, es un **termostato térmico**.

Son interruptores térmicos.

Por qué van con capacitores por qué sin capacitores? Motores.

Semiautomático: enguaja y desagota no centrifuga.

Mi ropa no queda seca, queda húmeda. Yo no me preocuparía por eso porque es una fuerza antiproductiva para las lavadoras el centrifugado en alto. 

Con hacerle funcionar a 800 vueltas y que no saque bien seco, acá en nuestro lugar no es un problema. Aurora y pasarlo por secarropas, pero no hace falta.

Cuando la ropa sale más seca, sale más arrugada.

Si yo enseñara cámara frigorífica ahí si enseñaría trifásico.

Trifásico: Si está dando vueltas para un lado o para el otro: cambiado uno en uno.

Trifásico: RST UVW 

No hay fase, solo RST. 


Si no tenemos un detector de fase, no podemos saber cuales son las fases, cual está adelantada y cual atrasada, si no anda cambiamos dos polos y listo ya solucionamos el problema.
