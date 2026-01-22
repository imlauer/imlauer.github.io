---
title: "Conectar ventilador y motocompresor de un Aire Acondicionado"
date: 2024-12-08T23:38:42-03:00
tags: ['AC']
---
Medir con el multímetro los terminales del motocompresor obtener línea, arranque y trabajo (las dos resistencias más grandes son arranque, los dos más chicos son línea y el que sobra es el trabajo). Lo mismo hacer con los cables del ventilador(forzador) identificar cual es L,A,T.  
  
Hay 2 líneas distintas, una va directa al motocompresor y otra va directa al ventilador.

#### Procedimiento si usas 2 capacitores: un capacitor para el motocompresor y otro chiquito cuadrado para el ventilador.
Necesitamos 2 cablecitos adicionales: uno para conectar el arranque del motocompresor al capacitor, y otro para conectar el neutro del capacitor al trabajo del motocompresor.

### Motocompresor  
Para saber cual es fase y neutro tengo que con el multímetro en ohm tocar el tornillo de la bornera y tocar la fase y me tiene que dar 1 o menos de 1.

Ahora para conectar el motocompresor tengo 2 cables (fase y neutro).  
La fase(línea) va directa al motocompresor, el neutro va al capacitor del motocompresor de ahí el que está al lado (en la misma terminal) va al trabajo del motocompresor y tengo que agregar un cable que vaya del arranque del motocompresor al capacitor SÓLO.  
  
### Ventilador  
Tengo 3 cables, identificar cual es L,A,T. La línea del ventilador va directo a la bornera. El arranque va al capacitor chiquito SÓLO. Y el trabajo va al capacitor.  
Neutro del capacitor (que está al lado de trabajo) grande conecto al neutro del capacitor chico (al lado del trabajo) o sino conecto al neutro de la bornera.  
  
Siempre cuando conectás poné la pinza  
Siempre descargá el capacitor.  

**Cables del ventilador a identificar L,A,T**
![Ventilador](/img/aires/cables_ventilador.jpg)

**Como conectar 2 capacitores explicado anteriormente gráficamente**
![Capacitor forzador y motocompresor](/img/aires/conectar_motocompresor_forzador_dos_capacitores.jpg)

## Capacitor doble, gráfico de la conexión
En el caso del capacitor doble, el arranque del forzador va en F(fan), el arranque del motocompresor va en H(hermetic), ambas líneas siempre van directo a la bornera. Los trabajos del motocompresor y del forzador van al común y el neutro de la bornera va al neutro del capacitor (que está al lado del trabajo), el arranque siempre va solo.

![Capacitor doble](/img/aires/capacitor_compuesto.jpg)

Toman examen dibujar ambos.

Fotos: https://imlauer.blogspot.com/2024/12/motocompresor-ventilador-capacitores.html
