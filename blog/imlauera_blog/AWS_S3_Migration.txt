---
title: "AWS S3 Migration"
date: 2024-09-27T21:29:34-03:00
tags: ['aws','s3','migration']
---

Tenemos 100 TB de datos almacenados en Backblaze B2, que es un almacenamiento de objetos compatible con S3. Queremos transferir esto a Amazon S3 Glacier Deep Archive. Necesito ayuda para migrar estos datos directamente desde Backblaze a Glacier.



Hice los mismos cálculos hace un tiempo, comparando el glaciar profundo S3 con el wasabi. Y encontró resultados similares: el glaciar puede ser más barato, especialmente si solo se usa en un desastre y cuanto más tiempo pase entre desastres, más “barato” se vuelve. Pongo más barato entre comillas porque todavía no es barato pero relativamente el S3 es más barato.

Cifro y hago copias de seguridad de datos críticos en S3 y también en OneDrive (también podría hacerlo, ya que tengo 365). Pero hay grandes partes de mi almacenamiento que no tienen copia de seguridad. Puedo sufrir algunas fallas en el disco, pero eso es todo. Parece que no puedo justificar el costo de gastar potencialmente cientos por mes almacenando decenas de TB de datos. Los datos son importantes para mí y quiero encontrar una solución, pero el precio es un factor clave en esa ecuación.
