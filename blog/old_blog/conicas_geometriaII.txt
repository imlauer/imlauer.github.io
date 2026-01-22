---
title: "Cónicas (Geometria II)"
date: 2024-08-13T21:43:12-03:00
tags: ['conicas','geometriaII','matematicas']
---

## Circunferencia
#### Consigna 1. Encontrar la ecuación canónica de la circunferencia:
a. con radio 5/2 y de centro (-1;2)

La ecuación canónica de la circunferencia es: $$ (x-h)^2+(y-k)^2=r^2 $$

Entonces para este caso sería: $$ (x+1)^2+(y-2)^2=(5/2)^2 $$

b. con centro C(5;-2) y que pase por el punto (-1;5)
Tenemos que hacer que pase por ese centro y evaluarla en el punto `(-1;5)`
$$ (x+1)^2+(y-5)^2=r^2 $$

c. cuyos gráficos son los siguientes:

#### Consigna 3: Determinar la ecuación canónica de la circunferencia que pasa por los puntos (2;3) y (-1;1) y cuyo centro está contenido en la recta \\( x-3y-11=0 \\)

Lo primero que vamos a hacer es reconocer la forma que tiene la **Ecuación Canónica de una Circunferencia**:

$$ (x-h)^2+(y-k)^2 = r^2 $$

Donde "h" y "k" son las coordenadas del centro de la circunferencia C=(h,k) y "r" es el radio de la circunferencia.

El problema nos da 2 puntos que pertenecen a la circunferencia: \\( P_1=(2,3) \\) y \\( P_2=(-1,1) \\). Y sabemos que el centro "C", pertenece a la recta \\( s: x-3y-11=0 \\).

Entonces para determinar el centro debemos plantear otra condición, ya que este es un punto específico de la recta "s" y no uno cualquiera. El centro "C" va a ser el punto de la recta desde el cual la distancia a los puntos "\\( P_1 \\)" y "\\( P_2 \\)" es la misma (radio), ya que estos justamente pertenecen a la circunferencia. En símbolos: 
$$ d(C,P_1) = r = \sqrt{(2-h)^2+(3-k)^2} $$
$$ d(C,P_2) = r = \sqrt{(-1-h)^2+(1-k)^2} $$

Al ser ambas expresiones iguales al radio, podemos plantear que:
$$ d(C,P_1) = d(C,P_2) $$
$$ \sqrt{(2-h)^2+(3-k)^2} = \sqrt{(-1-h)^2+(1-k)^2} $$
$$ (2-h)^2+(3-k)^2 = (-1-h)^2+(1-k)^2 $$
$$ (4-4h+h^2)+(9-6k+k^2) = (1+2h+h^2)+(1-2k+k^2) $$
$$ 13-4k-6k = 2+2h-2k $$
$$ 13-2-4h-2h = -2k+6k $$
$$ 11-6h=4k \rightarrow \boxed{\frac{11-6h}{4} = k} $$

Por otro lado, sabemos que el punto \\( C=(h,k) \\) pertenece a la recta \\( s: x-3y-11=0 \\). Es decir, 
$$ \boxed{C(h,k) \in s \rightarrow \text{se debe cumplir que: } h-3k-11=0 } $$ 
Reemplazando, en la ecuación de la recta, la expresión de k obtenida anteriormente podemos determinar el valor de la primera coordenada del centro C, que pertenece a la recta:   
$$ h-3\Big(\frac{11-6h}{4}\Big)-11=0 $$
$$ h-\frac{33}{4} + \frac{18h}{4}-11=0 $$
$$ \frac{11}{2}h = 11+\frac{33}{4} $$
$$ h = \frac{77}{4}\cdot\frac{2}{11} \rightarrow h = \frac{7}{2} = 3,5 $$
Conociendo esto, podemos determinar el valor de "k":

$$ \frac{11-6\cdot(3,5)}{4} = k \rightarrow \boxed{k=-\frac{5}{2}=-2,5} $$
Solo resta determinar el valor del radio para poder completar la **Ecuación Canónica**, para ello usamos una de las expresiones anteriores del radio y reemplazamos los valores "h" y "k" obtenidos:

$$ r = \sqrt{\Big(2-\frac{7}{2}\Big)^2+\Big(3+\frac{5}{2}\Big)^2} $$
$$ r = \sqrt{\Big(-\frac{7}{2}\Big)^2+\Big(\frac{11}{2}\Big)^2} $$
$$ r = \sqrt{\frac{9}{4} + \frac{121}{4}} $$
$$ r^2 = \sqrt{\frac{130}{4}} $$
Entonces la Ecuación Canónica de la Circunferencia que pasa por los puntos "\\(P_1\\)" y "\\(P_2\\)" cuyo centro "C" está contenido en la recta "s" es:

$$ \boxed{\Big(x-\frac{7}{2}\Big)^2 + \Big(y+\frac{5}{2} \Big)=\frac{130}{4}} $$
