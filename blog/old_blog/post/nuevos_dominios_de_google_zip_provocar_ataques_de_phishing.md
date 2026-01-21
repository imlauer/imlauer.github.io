---
title: "Posibles riesgos con los nuevos dominios de google: zip y mov"
date: 2023-05-27T04:51:28-03:00
tags: ['google','domains']
categories: ['web','domains']
---
#### Google anuncio nuevos dominios que hacen referencia a extensiones de archivos
.zip y .mov son los nuevos dominios de Google. La preocupación, es que las URL que se parecen a nombres de archivo darán aún más posibilidades a estafas digitales como el [https://es.wikipedia.org/wiki/Phishing](phishing), que engañan a los internautas para que hagan clic en enlaces maliciosos que se hacen pasar por algo legítimo. Y los dos dominios también podrían agravar el problema de los programas que reconocen erróneamente nombres de archivo como URL y les añaden automáticamente enlaces. Teniendo esto en cuenta, los estafadores podrían comprar estratégicamente algunas URL .zip y .mov que también fueran nombres de archivo comunes.
[https://medium.com/@bobbyrsec/the-dangers-of-googles-zip-tld-5e1e675e59a5](Aca se explica un tipo de ataque con estos dominios)

#### TLDR
Los atacantes pueden utilizar el nuevo dominio de nivel superior .zip de Google, junto con el operador @ y un carácter Unicode ∕ (U+2215), para crear un phish de apariencia muy convincente. Los navegadores modernos ignoran todos los datos en la sección de usuario de una URL, y simplemente dirigen al usuario a la parte del nombre de host de la URL. Sin embargo, si se agregan barras diagonales a la URL que viene antes del operador @, el navegador comenzará a analizar todo después de la barra diagonal como la ruta, lo que puede llevar a los usuarios a un sitio malicioso. Los atacantes pueden aprovechar esto para crear un phish convincente de un archivo .zip legítimo con el nuevo dominio .zip de Google. La información también proporciona consejos para detectar este tipo de ataques, como buscar dominios que contengan los caracteres Unicode U+2044 (⁄) y U+2215 (∕), buscar dominios que contengan el operador @ seguido de archivos .zip, y tener precaución al descargar archivos de URL enviados por remitentes desconocidos.

## Ejemplo de dominio
[https://yourmom.zip](https://yourmom.zip)

#### Problemas con otros dominios: .io
El dominio de nivel superior .io es popular entre las empresas de tecnología debido a la asociación del acrónimo "IO" con "Input/Output", un término común en informática. Sin embargo, el dominio .io es asignado por país y pertenece a los Territorios Británicos del Océano Índico, que consisten en el archipiélago de Chagos, donde los habitantes originales, los chagosianos, fueron expulsados ​​por la fuerza para dar cabida a operaciones militares en los años 60 y 70. Los chagosianos han solicitado regularmente el regreso a su hogar, pero el gobierno del Reino Unido se lo ha negado continuamente.

El problema para las empresas que utilizan el dominio .io es que representa la opresión continua de los habitantes originales del archipiélago de Chagos. Todos los ingresos de la registración de los nombres de dominio van al Internet Computer Bureau, una empresa británica que ahora es propiedad de Affilias, una empresa estadounidense. Se suponía que algunos de los beneficios de las ventas irían a apoyar a los territorios, pero el gobierno británico declaró que nunca recibió dinero por esto y negó cualquier responsabilidad por el apoyo a los chagosianos.

En 2019, la ONU votó que el archipiélago de Chagos es parte del territorio de Mauricio, donde la mayoría de los chagosianos fueron expulsados. Según la resolución y los hallazgos de la Corte Internacional de Justicia, el Reino Unido debe devolver el archipiélago a los chagosianos. Sin embargo, el Reino Unido ha negado esto, manteniendo su soberanía sobre las islas.

A pesar de que esta expulsión forzada se considera un crimen de lesa humanidad, los chagosianos no reciben ningún apoyo o remuneración por el uso y la popularidad del dominio .io. En mi opinión, si se utiliza un nombre de dominio .io, es necesario hacer una contribución a los chagosianos y establecer políticas claras y inequívocas con respecto a las reparaciones y su repatriación. Además, sería recomendable buscar un dominio diferente.

