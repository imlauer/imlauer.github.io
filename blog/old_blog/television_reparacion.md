---
title: "Intento arreglo televisor tubo de rayos catodicos: enciende ni el LED de standby."
tags: ['Marcelo']
---
Marca: Philips. Modelo: 21PT5432/77R

Le cambiamos el transistor del switching y el integrado(oscilador) pero igual no arrancó, no prende standby.
Después pensamos que había que cambiar junto el integrado(oscilador) y el transistor, porque cuando yo puse el transistor, ya se cagó otra vez el integrado(oscilador).

Integrado (oscilador): TEA1507
Transistor: 15

En la proveduría electrónica.

El fayback es una fuente de alta tensin para el horizontal tambien se usa para la fuente.
El fayback es una fuente switching usa eso para hacer la fuente que usa para el standby.

El fayback genera alta tension

De 220 voltios de entrada, genera 400 voltios y luego genera 12 mil voltios.
Necesita 12 vopltios para el barrido horizontal de 15 725 hertz, que es  la frec del barido horizontal

La frecuencia del barido vertical es de linea 50 hertz.

Entra 220 con diodo capacitor genera 400 voltios. Y ahí con una fuente switching genera los 12 mil voltios.

La fuente switching está comandado por un transistor y un integrado(oscilador), ese integrado(oscilador) se alimenta 400 tiene una resistencia yu va derecho al integrado(oscilador).

No oscila el transistor cambiamos, medí una tensión del integrado(oscilador) y no daba la tensión que le daba al microprocesador.

Podes medir con un osciloscopio si oscila el transistor, pero no hicimos eso medimos si el integrado(oscilador) le daba la tensino al microprocesador.


#### FOTOS: https://imlauer.blogspot.com/2024/12/televisor-tubo-de-rayos-catodicos.html

Archivo PDF del circuito: [Chassis L01 1LAC-2K3 Manual_de_servicio.pdf](/files/televisor/9537_Chassis_L01.1LAC-2K3_Manual_de_servicio.pdf)

Archivo PDF del circuito: [TEA1507.pdf](/files/televisor/TEA1507.pdf)

Preguntas sobre teoría:
https://www.revisely.com/quiz/tzG07d

Las formas de onda de las que se habla se muestran en la imagen.

Los capacitores electrolíticos son los que son polarizados para corriente continua.

![Ayuda para estudiantes y aficionados en reparación de televisores](https://lh3.googleusercontent.com/blogger_img_proxy/AEn0k_ugk_YNqqH_XRnj2gKaOny3RzMSEw76GKFngHkH9OQZNfJ5eLA45J8pToJg1z07oyxNEp7vuZpDD_e9CjAnRRgpas_768qLtwN4zM0wypwBqoKE4eqECNsk_6ZlEjNvLTR87oMLxs8fDpsqY4rbd3wSBZfLdN0XKqFNMSop9iTKYVYl01IhMYykFmU8MblHzcH4BLM2qmEgLu025AEI4A=s0-d) 

De acá saqué la imagen: https://www.tecnicosaurios.com/foro/viewtopic.php?f=90&t=7842

Preguntas sobre teoría:
https://www.revisely.com/quiz/XcQM76

Cualquier curiosidad que surja de esas preguntas podés buscar en el foro por palabras claves por ejemplo: https://tecnicosaurios.com/foro/search.php?keywords=una+l%C3%A1mpara+de+60+watts&terms=all&author=&sv=0&sc=1&sf=all&sk=t&sd=d&sr=posts&st=0&ch=300&t=0&submit=Buscar

**Cuando se encuentran con que el aparato no arranca**, y el técnico capacitado les dice que desconecten la etapa horizontal y carguen la fuente con una lámpara, vean en el ejemplo dónde se debe interrumpir la alimentación del fly-back, y colocar entre ese punto,que es el pin de entrada al bobinado primario del mismo, la lámpara de 60 watts con el otro extremo a masa del fly-back y NO en ningún otro lugar, o sea, en el punto indicado con una X y masa es donde deben medir la tensión de la fuente y/ó colocar la carga.

Hay que medir con el oscilospico porque hay que ver la forma de onda aparte eso arruina el tester.

Si alguno de ustedes ahorró y pudo llegar a comprar el osciloscopio, pueden ver en el diagrama, dentro de los recuadros verde limón los oscilogramas ó formas de onda en los puntos clave de la etapa de salida horizontal a saber: 1 es la forma de onda en la base del transistor driver, o sea la señal que viene del jungla, para determinar si el transistor está funcionando, deberíamos ver la forma de onda 2, en el colector del driver, siguiendo con la forma de onda en la base del transistor de salida horizontal, 3, y por último, la forma de onda en el colector del transistor de salida, 4, pulso horizontal donde NO deben medir con tester ó multímetro, sólo con el osciloscopio con la punta adecuada en atenuación.

Si les piden que verifiquen los capacitores de sintonía del horizontal y el filtro del driver, los encuentran dentro de un círculo en el diagrama de ejemplo en color rojo.

Fuente: https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=7842

---

##### Diferentes publicaciones de problemas similares a este: el standby no enciende: 

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=40882

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=40190

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=48685

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=38718

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=36641

Diagramas de diferentes marcas y modelos de televisores: https://www.tecnicosaurios.com/foro/viewtopic.php?f=107&t=9537#p57982

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=59373

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=58258

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=58257

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=57233

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=56007

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=55680

https://tecnicosaurios.com/foro/viewtopic.php?f=205&t=55609

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=53098

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=52506

https://tecnicosaurios.com/foro/viewtopic.php?f=90&t=51912 



---

* Teoría (Hasta la línea 763 de un archivo de 31834 líneas): https://www.revisely.com/quiz/CsjlEu      
* Teoría (Hasta la línea 1400 de un archivo de 31834 líneas): https://www.revisely.com/quiz/OZs4D5  
* Teoría (Hasta la línea 2100 de un archivo de 31834 líneas): https://www.revisely.com/quiz/ynZqN7  

Cautín con diodos: https://www.youtube.com/watch?v=tuFjfuL-IfU

https://elrincondesolucionestv.blogspot.com/2021/06/el-circuito-de-desmagnetizacion-en.html

##### Varias fallas televisores
https://elrincondesolucionestv.blogspot.com/p/television.html

Bobina de choque desmagnetiza el televisor.

> voltaje entre DRAIN y GND del regulador: (310v) ?? no se supone que este circuito deberia conmutar a alta frecuencia e impedir que mi tester detectase este voltaje?  Fuente: https://www.forosdeelectronica.com/threads/monitor-crt-completamente-muerto.75294/


* Teoría (Hasta la línea 2800 de un archivo de 31834 líneas): https://www.revisely.com/quiz/x57YR6  
* Teoría (Hasta la línea 3500 de un archivo de 31834 líneas): https://www.revisely.com/quiz/zyiKn8  
* Teoría (Hasta la línea 4200 de un archivo de 31834 líneas): https://www.revisely.com/quiz/rwobYW  
* Teoría (Hasta la línea 4900 de un archivo de 31834 líneas): https://www.revisely.com/quiz/PnCRGf  
* Teoría (Hasta la línea 5600 de un archivo de 31834 líneas): https://www.revisely.com/quiz/eaDod6  
* Teoría (Hasta la línea 6300 de un archivo de 31834 líneas): https://www.revisely.com/quiz/or8yhY  
* Teoría (Hasta la línea 7000 de un archivo de 31834 líneas): https://www.revisely.com/quiz/uM3GAD  
* Teoría (Hasta la línea 7700 de un archivo de 31834 líneas): https://www.revisely.com/quiz/86HZAE  
* Teoría (Hasta la línea 8400 de un archivo de 31834 líneas): https://www.revisely.com/quiz/zuEeSy  
* Teoría (Hasta la línea 9100 de un archivo de 31834 líneas): https://www.revisely.com/quiz/XonBGJ  
* Teoría (Hasta la línea 9800 de un archivo de 31834 líneas): https://www.revisely.com/quiz/EqE4ZM  
* Teoría (Hasta la línea 10500 de un archivo de 31834 líneas): https://www.revisely.com/quiz/GbNUL3  
* Teoría (Hasta la línea 11200 de un archivo de 31834 líneas): https://www.revisely.com/quiz/ZjLLHJ  
* Teoría (Hasta la línea 11900 de un archivo de 31834 líneas): https://www.revisely.com/quiz/wQAcpv  
* Teoría (Hasta la línea 12600 de un archivo de 31834 líneas): https://www.revisely.com/quiz/QcTJrb  
* Teoría (Hasta la línea 13300 de un archivo de 31834 líneas): https://www.revisely.com/quiz/7GYxQL   
* Teoría (Hasta la línea 14000 de un archivo de 31834 líneas): https://www.revisely.com/quiz/6JtJtP  
* Teoría (Hasta la línea 14700 de un archivo de 31834 líneas): https://www.revisely.com/quiz/gHO0vt  
* Teoría (Hasta la línea 15400 de un archivo de 31834 líneas): https://www.revisely.com/quiz/lkNWGa  
* Teoría (Hasta la línea 16100 de un archivo de 31834 líneas): https://www.revisely.com/quiz/UAFehX
* Teoría (Hasta la línea 16800 de un archivo de 31834 líneas): https://www.revisely.com/quiz/X8jJHd
* Teoría (Hasta la línea 17500 de un archivo de 31834 líneas): https://www.revisely.com/quiz/u6HITj
* Teoría (Hasta la línea 18200 de un archivo de 31834 líneas): https://www.revisely.com/quiz/X8neP6
* Teoría (Hasta la línea 18900 de un archivo de 31834 líneas): https://www.revisely.com/quiz/Yy0bFR
* Teoría (Hasta la línea 19600 de un archivo de 31834 líneas): https://www.revisely.com/quiz/gxvagf
* Teoría (Hasta la línea 20300 de un archivo de 31834 líneas): https://www.revisely.com/quiz/X7UTAI
* Teoría (Hasta la línea 21000 de un archivo de 31834 líneas): https://www.revisely.com/quiz/RfuTJR  
* Teoría (Hasta la línea 21700 de un archivo de 31834 líneas): https://www.revisely.com/quiz/ykLt83
* Teoría (Hasta la línea 22400 de un archivo de 31834 líneas): https://www.revisely.com/quiz/WfQNbc
* Teoría (Hasta la línea 23100 de un archivo de 31834 líneas): https://www.revisely.com/quiz/qXwrPT
* Teoría (Hasta la línea 23800 de un archivo de 31834 líneas): https://www.revisely.com/quiz/tu2mvy
* Teoría (Hasta la línea 24500 de un archivo de 31834 líneas): https://www.revisely.com/quiz/HaquYV
* Teoría (Hasta la línea 25200 de un archivo de 31834 líneas): https://www.revisely.com/quiz/wPjApx
* Teoría (Hasta la línea 25900 de un archivo de 31834 líneas): https://www.revisely.com/quiz/9iEriU
* Teoría (Hasta la línea 26600 de un archivo de 31834 líneas): https://www.revisely.com/quiz/PCPmaY
* Teoría (Hasta la línea 27300 de un archivo de 31834 líneas): https://www.revisely.com/quiz/xCAWr6
* Teoría (Hasta la línea 28000 de un archivo de 31834 líneas): https://www.revisely.com/quiz/Sypvjg
* Teoría (Hasta la línea 28700 de un archivo de 31834 líneas): https://www.revisely.com/quiz/h8v8eI
* Teoría (Hasta la línea 29400 de un archivo de 31834 líneas): https://www.revisely.com/quiz/aY4V1y
* Teoría (Hasta la línea 30100 de un archivo de 31834 líneas): https://www.revisely.com/quiz/itBolm
* Teoría (Hasta la línea 30800 de un archivo de 31834 líneas): https://www.revisely.com/quiz/P6DsHs
* Teoría (Hasta la línea 31500 de un archivo de 31834 líneas): https://www.revisely.com/quiz/SZo49D
  
[Archivo de subtitulo de un canal de Reparación de Televisores en YouTube](/files/todo_televisores.txt)




---

Anécdotas encontradas:
https://www.facebook.com/yoyneersalinas06/posts/reparaci%C3%B3n-de-televisor-phillips-chassis-l03-2l-aafalla-el-televisor-no-enciende/1198030507005933/

**Reparación de televisor Phillips chassis L03 2L AA.**

Falla: el televisor no enciende, al conectarlo a la red eléctrica no se percibe ningún sonido ni ningún signo de vida, es decir, "totalmente muerto".
el cliente alega (molesto) que lo había llevado a un servicio técnico de acá del centro de mi ciudad y le habían mandado a comprar un flyback nuevo y resulta que no funciono y el cliente estaba molesto porque perdió dinero allí.
1.) al abrir el receptor, vi en muy buen estado los componentes al igual que las soldaduras.
2.)se procedió a tomar lectura de tensión en 3 puntos vitales del televisor (filtro principal,+ B, sistema de control).
3. en el filtro principal se encontró 160v ( OK), en el sistema de control, específicamente en la pata 8 de la memoria eeprom se encontró 5v (OK), PERO  en el pin + B del transformador de lineas/flyback había 0v.
4.se tomo lecturas en escala de diodos en la linea de +B no se hallaron cortos PERO en el C2564 ESTA VEZ EN ESCALA D.C si se hallo el voltaje correspondiente de +B para este modelo el cual en stanby es de 98v y al encender el televisor sube a 110v.
5. ¿ EL CULPABLE ? bobina 5563 ABIERTA,  que esta en serie en la linea de + B
TAL VEZ UNA REPARACIÓN no muy difícil y para algunos aburrida, PERO RECUERDEN QUE NO QUIERO QUE VEAN SOLAMENTE COMO SE REPARA UN ARTEFACTO ELECTRÓNICO, SI NO TAMBIÉN EL PROCEDIMIENTO QUE SE LLEVA A CABO, HAY QUE ANALIZAR, LEER, ESTUDIAR, APRENDER PARA ASÍ NO HACER INVERTIR AL CLIENTE EN VANO Y PERDER NUESTRO VALIOSO TIEMPO. ANIMO Y ESPERO QUE LES SEA DE AYUDA.


### Teoria sobre el no encendido.
https://www.revisely.com/quiz/BpkCZ5

https://www.revisely.com/quiz/8uv2TM

https://www.revisely.com/quiz/G65LWT

https://www.revisely.com/quiz/uCcVn4

https://www.revisely.com/quiz/SW6sqY

https://www.revisely.com/quiz/K5K8kz

https://www.revisely.com/quiz/8szO5Y

