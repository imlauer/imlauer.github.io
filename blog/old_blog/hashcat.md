---
title: "Hashcat cracking handshakes"
date: 2025-02-01T23:56:46-03:00
tags: ['hacking']
---
`hashcat64 --help`

Seria basicamente ver la ayuda.

Para iniciar un proceso cualquiera lo podemos hacer con la siguiente linea de
comando (modo mascaras -a3)

```bash
hashcat64 -m2500 -a3 captura.hccapx ?d?d?d?d?d?d?d?d -w4
```

`-m2500` = es el modo de WPA, este numero puede cambiar segun el tipo de hash que
usemos, dejo algunos a modo de ejemplo.

```bash
-m0 = MD5
-m1000 = NTLM
-m2500 = WPA/WPA2 EAPOL
-m16800 = WPA/WPA2 PMKID
```

#### Modos de ataque:

-a3 = modo para ataque usando mascaras
-a0 = modo de ataque con diccionarios

Hay otros modos mas de ataque pero los basicos son estos 2.

Modo de uso de GPU/CPU, el modo recomendado es el -w3 si uno usa sistema operativo
windows 7, con windows 10 se puede usar el modo -w4, en linux no sabria decirles.

-w4 = modo extremo
-w3 = modo semi extremo
-w2 = modo semi light
-w1 = modo light

ejemplo de modo con diccionario

hashcat64 -m2500 -a0 captura.hccapx diccionario.txt -w4


Ahora paso a explicarles como instalar el OPENCL para CPU ya que es posible que en
muchas notebook quizas muchos tengan un buen CPU Core i3 o superior y no saben que
pueden aprovecharlo o simplemente por ahi por un tema de drivers la GPU onboard no
se las tome pero si les puede tomar el CPU, para esto primero deben bajar los
drivers correspondientes de su GPU onboard ademas del archivo de OPENCL para el CPU.

Para saber que GPU tienen deben ir a la parte de sistema y ubicar en adaptadores de
video el modelo de GPU que tengan, en este caso voy a ejemplificar con la Intel UHD
630.

Una vez que saben el modelo basta con ir a google y pone en el cuadro de busqueda el
modelo de GPU, bajar los drivers correspondientes segun su version de windows y
tenerlos guardados.


```bash
hashcat -b -m2500 -w4 -D1,2

-D1 = usa solo CPU
-D2 = usa solo GPU
-D1,2 = combina CPU+GPU
```

**Hay varias claves de este tipo: abcd1234.**
Se puede construir usando la siguiente máscara:

```console
Guess.Mask.......: f?l?l?l?d?d?d?d [8]
```
