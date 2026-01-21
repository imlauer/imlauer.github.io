---
title: "Portón eléctrico con Arduino"
tags: ['electronica','Marcelo']
---
![circuito](/img/porton/1.jpg)
Agarraste una fuente switching de 12 voltios, el arduino es de 5 voltios, y le agregaste un relé en el pin 32.

El pin 32 va a un transistor bipolar, podría haber usado un mosfet y de ahí conecté al relé.

El portón hay relé de 220 y comanda todo con fin de carrera, sólo tengo que cerrar el circuito

Corto la fase y lo puse en el relé o le doy fase o no le doy fase, si yo le saco la fase despega
el relé.

Le doy fase a la bobina de afuera del relé.

220 relé, lógica cableada, 3 relés. Hago todo a relé porque no quiero que queme todo cuando caiga un rayo.


Le doy la fase para un lado o para el otro lado. El fin de carrera le saca la fase. Y después el
relé de arduino le da la fase para el otro lado.

#### FOTOS: https://imlauer.blogspot.com/2024/12/porton-electrico-cargador-de-celular.html
