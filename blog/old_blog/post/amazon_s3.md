---
title: "Amazon s3 y CLI"
date: 2024-09-23T21:50:37-03:00
tags: ['s3','aws']
---
Amazon S3 (Simple Storage Service) es un servicio de almacenamiento de objetos en la nube que permite a los usuarios almacenar y recuperar cualquier cantidad de datos desde cualquier ubicación, ofreciendo alta durabilidad, disponibilidad y escalabilidad a un costo reducido.

> Hello, looking for a talented system admin who knows AWS S3 management who can help us remove files that are no longer in use from our S3 buckets. Our current monthly AWS bill needs to drop considerably.

### Como usarlo
Primero hagamos un backup

Amazon S3 > create bucket > tinyflix > choose bucket 

Podemos crear acceso público a nuestros buckets de varias formas, dar acceso publico no es buena idea. Con bucket versioning podés tener muchas versiones de un archivo. Quizas tengas que volver a una versión anterior, o de alguna foto o archivo accidentalmente borrado y se necesita recuperarlo, o por algún tipo de falla, está desactivado porque sale más caro.

En opciones avanzadas object lock evitará que los objetos se sobreescriban o se eliminen, la dejamos deshabilitada y creamos el bucket.

Apretá en el nombre > creá una carpeta llamada videos y otra llamada photos

Tinyflix es para trabajar equipo en paralelo.

Así que ingrese al servicio de almacenamiento simple (Simple Storage Service S3) (3 eses XD)

Este es un almacenamiento de objetos económico en aws. Ahora si el almacenamiento de objetos no tiene sentido para vos para este ejercicio supongamos que se tratan de fotos, videos, un pdf, cualquier archivo.

Amazon ofrece un sistema de archivos elástico llamado efs service este no es tecnicamente un file server (servidor de archivos) tiene ilimitada capacidad.


#### En la consola
https://docs.aws.amazon.com/cli/latest/reference/s3/


```bash
sudo apt install -y awscli
aws configure
aws s3 ls
aws s3 ls s3://thebucketofstephane
aws s3 cp help
### Descargar una imagen
aws s3 cp s3://thebucketofstephane/coffee.jpg coffee.png
ll
### Crear bucker
aws s3 mb s3://dsoifjsoner
### Listar buckets
aws s3 ls
### Eliminar bucket
aws s3 rb s3://dsoifjsoner
aws s3 ls
aws s3 rb s3://dsoifjsoner
aws s3 cp "C:\users\asfsdf.jpg" s3://dsoifjsoner/
aws s3 cp s3://dsoifjsoner/ ./
aws s3 rm s3://dsoifjsoner/asfsdf.jpg 
```
